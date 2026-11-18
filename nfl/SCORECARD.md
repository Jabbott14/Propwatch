# NFL scorecard

Generated 2026-11-18 12:09 UTC. 42 graded games (0 finished games had no final score and are not graded).

## Read this first: fit vs forward

**41 games before 2026-11-17 (fit) · 1 on or after it (forward).**

Every signal here, every threshold, and every PROMOTE/DROP label this scorecard
has printed was chosen while looking at the games before 2026-11-17.
Scoring those choices on those same games is grading the exam you studied from.
`pin_value` was 108-68 in CBB first halves and 10-1 on NFL spreads; both numbers
were fitted and scored on one sample, and neither has ever been tested on a game
it did not help choose. So every record below appears twice:

- **FIT** — in-sample. A label here is a **hypothesis**. It is what we guessed.
- **FORWARD** — out-of-sample. A label here is **evidence**. It is what happened.

Base rates are measured separately in each period. Scoring the forward test
against the fit window's chalk rate would re-import the bias the split exists to
remove — the fit window ran
65.9% favourites, and a signal that is
structurally long favourites would look like a discovery the week dogs cover.

The board follows the same rule: a signal is weighted by its FIT edge until it
has 30 decided forward outcomes, and by its FORWARD edge from then on. It
migrates onto out-of-sample evidence on its own, with no hand-tuning.

**Changing any threshold moves the holdout date to the day of the change and
restarts the forward test.** That is the real cost of fiddling with the engine,
and it is deliberately expensive.

Each signal is graded on **every** game it had an opinion on, at the FanDuel price
available at that moment. EARLY = one hour after the line was first seen. CLOSE =
last number before kickoff. Break-even at -110 is 52.4%. CLV = points of
closing-line value; positive means the number you would have taken beat the close.

`expected %` is the base rate of the sides that signal actually picked, measured on
this sample. `edge` is hit% minus that. A signal that is structurally long dogs or
unders will beat 50% in any week dogs or unders run, which is not an edge --
this sample ran **64.3% favourites** (n=42)
**54.8% overs** (n=42) and **78.6% moneyline favourites** (n=42) and **50.0% team-total overs** (n=84).

Moneyline has no handicap, so its `follow_move` reads price, its CLV is
percentage points of implied probability, and `pin_value` is a pure price
comparison against Pinnacle's no-vig fair -- no half-points involved.

Proposals appear once a signal has 30 decided games. Nothing changes
automatically.

**Gate B is these signals. Gate A is the Pinnacle columns on the board — a price
floor, never a veto.** EV against Pinnacle can essentially never be positive,
because Pinnacle is the fair-value definition. Using it as a veto rejects every
signal this system exists to find. See fault 4 in propwatch-news-vs-coherence.md.

# FORWARD (out-of-sample — this is the evidence)

Games kicking off on or after 2026-11-17. Nothing in the engine was chosen using these. n=1 games.

## EARLY  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pre_move | both | 1-0 | 100.0 | 100.0 | 0.0 | +1.94 | 194.0 | 0.5 | 100.0 | keep collecting (1/30) |
| follow_move | both | 0-1 | 0.0 | 0.0 | 0.0 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| rlm | both | 0-1 | 0.0 | 0.0 | 0.0 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| money_level | both | 2-1 | 66.7 | 66.7 | 0.0 | +0.74 | 24.7 | 0.5 | 66.7 | keep collecting (3/30) |
| sharp_gap | both | 2-1 | 66.7 | 66.7 | 0.0 | +1.81 | 60.3 | 0.17 | 66.7 | keep collecting (3/30) |
| money_moving | both | 2-0 | 100.0 | 100.0 | 0.0 | +1.74 | 87.0 | 1.0 | 100.0 | keep collecting (2/30) |
| pin_value | both | 2-0 | 100.0 | 75.0 | 25.0 | +1.72 | 85.9 | 1.0 | 100.0 | keep collecting (2/30) |
| consensus_gap | both | 2-0 | 100.0 | 100.0 | 0.0 | +2.81 | 140.5 | 0.75 | 100.0 | keep collecting (2/30) |
| consensus_gap+money_level | both | 1-0 | 100.0 | 100.0 | 0.0 | +0.87 | 87.0 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_moving | both | 1-0 | 100.0 | 100.0 | 0.0 | +0.87 | 87.0 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+pin_value | both | 1-0 | 100.0 | 100.0 | 0.0 | +0.87 | 87.0 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+sharp_gap | both | 2-0 | 100.0 | 100.0 | 0.0 | +2.81 | 140.5 | 0.75 | 100.0 | redundant -- identical record to consensus_gap alone, not independent confirmation |
| follow_move+rlm | both | 0-1 | 0.0 | 0.0 | 0.0 | -1.0 | -100.0 | -1.0 | 0.0 | redundant -- identical record to follow_move alone, not independent confirmation |
| money_level+money_moving | both | 2-0 | 100.0 | 100.0 | 0.0 | +1.74 | 87.0 | 1.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| money_level+pin_value | both | 1-0 | 100.0 | 100.0 | 0.0 | +0.87 | 87.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+sharp_gap | both | 1-0 | 100.0 | 100.0 | 0.0 | +0.87 | 87.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_moving+pin_value | both | 1-0 | 100.0 | 100.0 | 0.0 | +0.87 | 87.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_moving+sharp_gap | both | 1-0 | 100.0 | 100.0 | 0.0 | +0.87 | 87.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value+sharp_gap | both | 1-0 | 100.0 | 100.0 | 0.0 | +0.87 | 87.0 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+pre_move | both | 1-0 | 100.0 | 100.0 | 0.0 | +1.94 | 194.0 | 0.5 | 100.0 | redundant -- identical record to pre_move alone, not independent confirmation |
| pre_move+sharp_gap | both | 1-0 | 100.0 | 100.0 | 0.0 | +1.94 | 194.0 | 0.5 | 100.0 | redundant -- identical record to pre_move alone, not independent confirmation |
| pre_move | moneyline | 1-0 | 100.0 | 100.0 | 0.0 | +1.94 | 194.0 | 0.5 | 100.0 | keep collecting (1/30) |
| follow_move | spread | 0-1 | 0.0 | 0.0 | 0.0 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| rlm | spread | 0-1 | 0.0 | 0.0 | 0.0 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| money_level | moneyline | 0-1 | 0.0 | 0.0 | 0.0 | -1.0 | -100.0 | -0.5 | 0.0 | keep collecting (1/30) |
| money_level | spread | 1-0 | 100.0 | 100.0 | 0.0 | +0.87 | 87.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level | total | 1-0 | 100.0 | 100.0 | 0.0 | +0.87 | 87.0 | 1.0 | 100.0 | keep collecting (1/30) |
| sharp_gap | moneyline | 1-0 | 100.0 | 100.0 | 0.0 | +1.94 | 194.0 | 0.5 | 100.0 | keep collecting (1/30) |
| sharp_gap | spread | 1-0 | 100.0 | 100.0 | 0.0 | +0.87 | 87.0 | 1.0 | 100.0 | keep collecting (1/30) |
| sharp_gap | total | 0-1 | 0.0 | 0.0 | 0.0 | -1.0 | -100.0 | -1.0 | 0.0 | keep collecting (1/30) |
| money_moving | spread | 1-0 | 100.0 | 100.0 | 0.0 | +0.87 | 87.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_moving | total | 1-0 | 100.0 | 100.0 | 0.0 | +0.87 | 87.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value | spread | 1-0 | 100.0 | 100.0 | 0.0 | +0.87 | 87.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_value | tt_home | 1-0 | 100.0 | 50.0 | 50.0 | +0.85 | 84.7 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap | moneyline | 1-0 | 100.0 | 100.0 | 0.0 | +1.94 | 194.0 | 0.5 | 100.0 | keep collecting (1/30) |
| consensus_gap | spread | 1-0 | 100.0 | 100.0 | 0.0 | +0.87 | 87.0 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+pre_move | moneyline | 1-0 | 100.0 | 100.0 | 0.0 | +1.94 | 194.0 | 0.5 | 100.0 | redundant -- identical record to consensus_gap alone, not independent confirmation |
| consensus_gap+sharp_gap | moneyline | 1-0 | 100.0 | 100.0 | 0.0 | +1.94 | 194.0 | 0.5 | 100.0 | redundant -- identical record to consensus_gap alone, not independent confirmation |
| pre_move+sharp_gap | moneyline | 1-0 | 100.0 | 100.0 | 0.0 | +1.94 | 194.0 | 0.5 | 100.0 | redundant -- identical record to pre_move alone, not independent confirmation |
| consensus_gap+money_level | spread | 1-0 | 100.0 | 100.0 | 0.0 | +0.87 | 87.0 | 1.0 | 100.0 | redundant -- identical record to consensus_gap alone, not independent confirmation |
| consensus_gap+money_moving | spread | 1-0 | 100.0 | 100.0 | 0.0 | +0.87 | 87.0 | 1.0 | 100.0 | redundant -- identical record to consensus_gap alone, not independent confirmation |
| consensus_gap+pin_value | spread | 1-0 | 100.0 | 100.0 | 0.0 | +0.87 | 87.0 | 1.0 | 100.0 | redundant -- identical record to consensus_gap alone, not independent confirmation |
| consensus_gap+sharp_gap | spread | 1-0 | 100.0 | 100.0 | 0.0 | +0.87 | 87.0 | 1.0 | 100.0 | redundant -- identical record to consensus_gap alone, not independent confirmation |
| follow_move+rlm | spread | 0-1 | 0.0 | 0.0 | 0.0 | -1.0 | -100.0 | -1.0 | 0.0 | redundant -- identical record to follow_move alone, not independent confirmation |
| money_level+money_moving | spread | 1-0 | 100.0 | 100.0 | 0.0 | +0.87 | 87.0 | 1.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| money_level+pin_value | spread | 1-0 | 100.0 | 100.0 | 0.0 | +0.87 | 87.0 | 1.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| money_level+sharp_gap | spread | 1-0 | 100.0 | 100.0 | 0.0 | +0.87 | 87.0 | 1.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |
| money_moving+pin_value | spread | 1-0 | 100.0 | 100.0 | 0.0 | +0.87 | 87.0 | 1.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| money_moving+sharp_gap | spread | 1-0 | 100.0 | 100.0 | 0.0 | +0.87 | 87.0 | 1.0 | 100.0 | redundant -- identical record to money_moving alone, not independent confirmation |
| pin_value+sharp_gap | spread | 1-0 | 100.0 | 100.0 | 0.0 | +0.87 | 87.0 | 1.0 | 100.0 | redundant -- identical record to pin_value alone, not independent confirmation |
| money_level+money_moving | total | 1-0 | 100.0 | 100.0 | 0.0 | +0.87 | 87.0 | 1.0 | 100.0 | redundant -- identical record to money_level alone, not independent confirmation |

## CLOSE  (fwd)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| follow_move | both | 3-1 | 75.0 | 62.5 | 12.5 | +2.78 | 69.5 |  |  | keep collecting (4/30) |
| rlm | both | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | keep collecting (1/30) |
| rlm_ratio | both | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | keep collecting (1/30) |
| money_level | both | 1-2 | 33.3 | 33.3 | 0.0 | -1.05 | -34.9 |  |  | keep collecting (3/30) |
| sharp_gap | both | 2-1 | 66.7 | 66.7 | 0.0 | +1.85 | 61.7 |  |  | keep collecting (3/30) |
| money_moving | both | 2-1 | 66.7 | 66.7 | 0.0 | +1.85 | 61.7 |  |  | keep collecting (3/30) |
| pin_value | both | 1-1 | 50.0 | 25.0 | 25.0 | -0.07 | -3.7 |  |  | keep collecting (2/30) |
| consensus_gap | both | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | keep collecting (1/30) |
| follow_move+money_level | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.05 | -2.4 |  |  | keep collecting (2/30) |
| follow_move+money_moving | both | 2-1 | 66.7 | 66.7 | 0.0 | +1.85 | 61.7 |  |  | redundant -- identical record to money_moving alone, not independent confirmation |
| follow_move+sharp_gap | both | 2-1 | 66.7 | 66.7 | 0.0 | +1.85 | 61.7 |  |  | redundant -- identical record to sharp_gap alone, not independent confirmation |
| money_level+money_moving | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.05 | -2.4 |  |  | keep collecting (2/30) |
| money_level+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.05 | -2.4 |  |  | keep collecting (2/30) |
| money_moving+sharp_gap | both | 2-1 | 66.7 | 66.7 | 0.0 | +1.85 | 61.7 |  |  | redundant -- identical record to money_moving alone, not independent confirmation |
| consensus_gap+follow_move | both | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | redundant -- identical record to consensus_gap alone, not independent confirmation |
| consensus_gap+money_moving | both | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | redundant -- identical record to consensus_gap alone, not independent confirmation |
| consensus_gap+rlm | both | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | redundant -- identical record to consensus_gap alone, not independent confirmation |
| consensus_gap+rlm_ratio | both | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | redundant -- identical record to consensus_gap alone, not independent confirmation |
| consensus_gap+sharp_gap | both | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | redundant -- identical record to consensus_gap alone, not independent confirmation |
| follow_move+rlm | both | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | both | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+rlm | both | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| money_moving+rlm_ratio | both | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+rlm_ratio | both | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| rlm+sharp_gap | both | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| rlm_ratio+sharp_gap | both | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_value | both | 1-0 | 100.0 | 50.0 | 50.0 | +0.93 | 92.6 |  |  | keep collecting (1/30) |
| follow_move | moneyline | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | keep collecting (1/30) |
| follow_move | spread | 0-1 | 0.0 | 0.0 | 0.0 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| follow_move | total | 1-0 | 100.0 | 100.0 | 0.0 | +0.95 | 95.2 |  |  | keep collecting (1/30) |
| follow_move | tt_home | 1-0 | 100.0 | 50.0 | 50.0 | +0.93 | 92.6 |  |  | keep collecting (1/30) |
| rlm | moneyline | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | keep collecting (1/30) |
| rlm_ratio | moneyline | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | keep collecting (1/30) |
| money_level | moneyline | 0-1 | 0.0 | 0.0 | 0.0 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_level | spread | 0-1 | 0.0 | 0.0 | 0.0 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_level | total | 1-0 | 100.0 | 100.0 | 0.0 | +0.95 | 95.2 |  |  | keep collecting (1/30) |
| sharp_gap | moneyline | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | keep collecting (1/30) |
| sharp_gap | spread | 0-1 | 0.0 | 0.0 | 0.0 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| sharp_gap | total | 1-0 | 100.0 | 100.0 | 0.0 | +0.95 | 95.2 |  |  | keep collecting (1/30) |
| money_moving | moneyline | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | keep collecting (1/30) |
| money_moving | spread | 0-1 | 0.0 | 0.0 | 0.0 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_moving | total | 1-0 | 100.0 | 100.0 | 0.0 | +0.95 | 95.2 |  |  | keep collecting (1/30) |
| pin_value | total | 0-1 | 0.0 | 0.0 | 0.0 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_value | tt_home | 1-0 | 100.0 | 50.0 | 50.0 | +0.93 | 92.6 |  |  | keep collecting (1/30) |
| consensus_gap | moneyline | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | keep collecting (1/30) |
| consensus_gap+follow_move | moneyline | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | redundant -- identical record to consensus_gap alone, not independent confirmation |
| consensus_gap+money_moving | moneyline | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | redundant -- identical record to consensus_gap alone, not independent confirmation |
| consensus_gap+rlm | moneyline | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | redundant -- identical record to consensus_gap alone, not independent confirmation |
| consensus_gap+rlm_ratio | moneyline | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | redundant -- identical record to consensus_gap alone, not independent confirmation |
| consensus_gap+sharp_gap | moneyline | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | redundant -- identical record to consensus_gap alone, not independent confirmation |
| follow_move+money_moving | moneyline | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | redundant -- identical record to follow_move alone, not independent confirmation |
| follow_move+rlm | moneyline | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | redundant -- identical record to follow_move alone, not independent confirmation |
| follow_move+rlm_ratio | moneyline | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | redundant -- identical record to follow_move alone, not independent confirmation |
| follow_move+sharp_gap | moneyline | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | redundant -- identical record to follow_move alone, not independent confirmation |
| money_moving+rlm | moneyline | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | redundant -- identical record to money_moving alone, not independent confirmation |
| money_moving+rlm_ratio | moneyline | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | redundant -- identical record to money_moving alone, not independent confirmation |
| money_moving+sharp_gap | moneyline | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | redundant -- identical record to money_moving alone, not independent confirmation |
| rlm+rlm_ratio | moneyline | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| rlm+sharp_gap | moneyline | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| rlm_ratio+sharp_gap | moneyline | 1-0 | 100.0 | 100.0 | 0.0 | +1.9 | 190.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 0-1 | 0.0 | 0.0 | 0.0 | -1.0 | -100.0 |  |  | redundant -- identical record to follow_move alone, not independent confirmation |
| follow_move+money_moving | spread | 0-1 | 0.0 | 0.0 | 0.0 | -1.0 | -100.0 |  |  | redundant -- identical record to follow_move alone, not independent confirmation |
| follow_move+sharp_gap | spread | 0-1 | 0.0 | 0.0 | 0.0 | -1.0 | -100.0 |  |  | redundant -- identical record to follow_move alone, not independent confirmation |
| money_level+money_moving | spread | 0-1 | 0.0 | 0.0 | 0.0 | -1.0 | -100.0 |  |  | redundant -- identical record to money_level alone, not independent confirmation |
| money_level+sharp_gap | spread | 0-1 | 0.0 | 0.0 | 0.0 | -1.0 | -100.0 |  |  | redundant -- identical record to money_level alone, not independent confirmation |
| money_moving+sharp_gap | spread | 0-1 | 0.0 | 0.0 | 0.0 | -1.0 | -100.0 |  |  | redundant -- identical record to money_moving alone, not independent confirmation |
| follow_move+money_level | total | 1-0 | 100.0 | 100.0 | 0.0 | +0.95 | 95.2 |  |  | redundant -- identical record to follow_move alone, not independent confirmation |
| follow_move+money_moving | total | 1-0 | 100.0 | 100.0 | 0.0 | +0.95 | 95.2 |  |  | redundant -- identical record to follow_move alone, not independent confirmation |
| follow_move+sharp_gap | total | 1-0 | 100.0 | 100.0 | 0.0 | +0.95 | 95.2 |  |  | redundant -- identical record to follow_move alone, not independent confirmation |
| money_level+money_moving | total | 1-0 | 100.0 | 100.0 | 0.0 | +0.95 | 95.2 |  |  | redundant -- identical record to money_level alone, not independent confirmation |
| money_level+sharp_gap | total | 1-0 | 100.0 | 100.0 | 0.0 | +0.95 | 95.2 |  |  | redundant -- identical record to money_level alone, not independent confirmation |
| money_moving+sharp_gap | total | 1-0 | 100.0 | 100.0 | 0.0 | +0.95 | 95.2 |  |  | redundant -- identical record to money_moving alone, not independent confirmation |
| follow_move+pin_value | tt_home | 1-0 | 100.0 | 50.0 | 50.0 | +0.93 | 92.6 |  |  | redundant -- identical record to follow_move alone, not independent confirmation |

# FIT (in-sample — this is the hypothesis)

Games before 2026-11-17. The signals and thresholds were chosen by looking at these, so a strong record here is expected and proves nothing. n=41 games.

## EARLY  (fit)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 1-4 | 20.0 | 19.5 | 0.5 | -2.92 | -58.4 | -0.8 | 80.0 | keep collecting (5/30) |
| pre_move | both | 6-15 | 28.6 | 31.1 | -2.6 | -8.45 | -40.2 | -0.27 | 47.6 | keep collecting (21/30) |
| follow_move | both | 12-12 | 50.0 | 54.8 | -4.8 | -1.46 | -6.1 | -0.07 | 20.8 | keep collecting (24/30) |
| rlm | both | 1-5 | 16.7 | 42.3 | -25.6 | -4.17 | -69.5 | 0.25 | 33.3 | keep collecting (6/30) |
| rlm_ratio | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| money_level | both | 66-31 | 68.0 | 61.1 | 7.0 | +16.72 | 17.2 | -0.4 | 23.7 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| sharp_gap | both | 56-39 | 58.9 | 50.7 | 8.3 | +8.36 | 8.8 | 0.05 | 33.7 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | both | 13-9 | 59.1 | 53.2 | 5.9 | +1.64 | 7.5 | -0.12 | 27.3 | keep collecting (22/30) |
| pin_value | both | 30-25 | 54.5 | 48.2 | 6.4 | +0.99 | 1.8 | 0.14 | 27.3 | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag | both | 2-3 | 40.0 | 41.0 | -1.0 | -1.05 | -21.0 | 0.76 | 80.0 | keep collecting (5/30) |
| consensus_gap | both | 15-30 | 33.3 | 30.4 | 3.0 | -14.4 | -32.0 | 0.13 | 51.1 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+rlm | both | 1-5 | 16.7 | 42.3 | -25.6 | -4.17 | -69.5 | 0.25 | 33.3 | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 10-6 | 62.5 | 55.9 | 6.6 | +3.14 | 19.7 | 0.19 | 18.8 | keep collecting (16/30) |
| rlm+rlm_ratio | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| rlm_ratio+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_value | both | 9-3 | 75.0 | 57.5 | 17.5 | +5.04 | 42.0 | -0.21 | 8.3 | keep collecting (12/30) |
| money_level+sharp_gap | both | 44-20 | 68.8 | 58.8 | 10.0 | +14.61 | 22.8 | -0.26 | 23.4 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| pin_value+sharp_gap | both | 11-5 | 68.8 | 47.7 | 21.0 | +4.74 | 29.6 | 0.54 | 31.2 | keep collecting (16/30) |
| consensus_gap+pin_value | both | 3-7 | 30.0 | 36.3 | -6.3 | -4.53 | -45.3 | 1.02 | 60.0 | keep collecting (10/30) |
| money_level+pre_move | both | 2-4 | 33.3 | 39.0 | -5.7 | -2.22 | -37.0 | -1.6 | 16.7 | keep collecting (6/30) |
| pre_move+sharp_gap | both | 6-15 | 28.6 | 31.1 | -2.6 | -8.45 | -40.2 | -0.27 | 47.6 | redundant -- identical record to pre_move alone, not independent confirmation |
| follow_move+pin_value | both | 4-1 | 80.0 | 59.5 | 20.5 | +2.47 | 49.3 | 0.0 | 0.0 | keep collecting (5/30) |
| consensus_gap+follow_move | both | 1-1 | 50.0 | 42.7 | 7.3 | -0.18 | -9.0 | 0.25 | 50.0 | keep collecting (2/30) |
| consensus_gap+money_level | both | 6-1 | 85.7 | 56.8 | 28.9 | +3.46 | 49.4 | -1.34 | 42.9 | keep collecting (7/30) |
| consensus_gap+sharp_gap | both | 10-14 | 41.7 | 32.3 | 9.3 | -3.88 | -16.2 | 0.38 | 62.5 | keep collecting (24/30) |
| follow_move+money_level | both | 9-6 | 60.0 | 61.8 | -1.8 | +2.04 | 13.6 | -0.21 | 20.0 | keep collecting (15/30) |
| consensus_gap+pre_move | both | 3-9 | 25.0 | 19.5 | 5.5 | -5.18 | -43.2 | -0.26 | 66.7 | keep collecting (12/30) |
| follow_move+money_moving | both | 3-2 | 60.0 | 62.4 | -2.4 | +0.38 | 7.5 | -0.62 | 0.0 | keep collecting (5/30) |
| money_level+money_moving | both | 8-3 | 72.7 | 64.3 | 8.4 | +2.83 | 25.7 | -0.74 | 18.2 | keep collecting (11/30) |
| money_moving+pin_value | both | 4-2 | 66.7 | 49.6 | 17.1 | +1.69 | 28.2 | 1.0 | 33.3 | keep collecting (6/30) |
| money_moving+sharp_gap | both | 6-3 | 66.7 | 51.5 | 15.2 | +2.28 | 25.4 | -0.08 | 22.2 | keep collecting (9/30) |
| consensus_gap+rlm | both | 0-1 | 0.0 | 19.5 | -19.5 | -1.0 | -100.0 | 0.5 | 100.0 | keep collecting (1/30) |
| book_lag+consensus_gap | both | 2-2 | 50.0 | 34.8 | 15.2 | -0.05 | -1.2 | 1.45 | 100.0 | keep collecting (4/30) |
| consensus_gap+pin_rlm | both | 1-4 | 20.0 | 19.5 | 0.5 | -2.92 | -58.4 | -0.8 | 80.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | both | 0-1 | 0.0 | 19.5 | -19.5 | -1.0 | -100.0 | -10.6 | 0.0 | keep collecting (1/30) |
| pin_rlm+pre_move | both | 1-4 | 20.0 | 19.5 | 0.5 | -2.92 | -58.4 | -0.8 | 80.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | both | 1-4 | 20.0 | 19.5 | 0.5 | -2.92 | -58.4 | -0.8 | 80.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+money_level | both | 1-1 | 50.0 | 65.9 | -15.9 | -0.13 | -6.5 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 42.7 | 7.3 | +0.08 | 4.0 | -0.05 | 50.0 | keep collecting (2/30) |
| book_lag+sharp_gap | both | 2-1 | 66.7 | 50.4 | 16.3 | +0.95 | 31.7 | 0.3 | 66.7 | keep collecting (3/30) |
| pin_value+pre_move | both | 0-3 | 0.0 | 19.5 | -19.5 | -3.0 | -100.0 | 3.03 | 100.0 | keep collecting (3/30) |
| consensus_gap+money_moving | both | 1-1 | 50.0 | 19.5 | 30.5 | +0.08 | 4.0 | 3.45 | 100.0 | keep collecting (2/30) |
| money_moving+pre_move | both | 2-1 | 66.7 | 28.5 | 38.2 | +1.03 | 34.4 | 1.63 | 66.7 | keep collecting (3/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 19.5 | -19.5 | -1.0 | -100.0 | 1.8 | 100.0 | keep collecting (1/30) |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 19.5 | 80.5 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| book_lag+pre_move | both | 1-0 | 100.0 | 19.5 | 80.5 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| money_moving+pin_rlm | both | 1-0 | 100.0 | 19.5 | 80.5 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| money_moving+rlm | both | 0-1 | 0.0 | 34.1 | -34.1 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| book_lag+pin_value | both | 1-0 | 100.0 | 65.9 | 34.1 | +0.87 | 87.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_rlm | moneyline | 1-4 | 20.0 | 19.5 | 0.5 | -2.92 | -58.4 | -0.8 | 80.0 | keep collecting (5/30) |
| pre_move | moneyline | 3-9 | 25.0 | 19.5 | 5.5 | -5.18 | -43.2 | -0.26 | 66.7 | keep collecting (12/30) |
| pre_move | spread | 1-2 | 33.3 | 44.7 | -11.4 | -1.09 | -36.4 | -0.5 | 33.3 | keep collecting (3/30) |
| pre_move | total | 2-4 | 33.3 | 47.6 | -14.2 | -2.18 | -36.3 | -0.17 | 16.7 | keep collecting (6/30) |
| follow_move | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | -0.44 | -21.9 | -1.3 | 50.0 | keep collecting (2/30) |
| follow_move | spread | 11-10 | 52.4 | 55.3 | -2.9 | -0.02 | -0.1 | 0.19 | 19.0 | keep collecting (21/30) |
| follow_move | total | 0-1 | 0.0 | 53.7 | -53.7 | -1.0 | -100.0 | -3.0 | 0.0 | keep collecting (1/30) |
| rlm | moneyline | 0-1 | 0.0 | 19.5 | -19.5 | -1.0 | -100.0 | 0.5 | 100.0 | keep collecting (1/30) |
| rlm | spread | 1-4 | 20.0 | 46.8 | -26.8 | -3.17 | -63.3 | 0.2 | 20.0 | keep collecting (5/30) |
| rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| money_level | moneyline | 26-6 | 81.2 | 76.7 | 4.6 | +5.05 | 15.8 | -0.76 | 34.4 | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 22-10 | 68.8 | 55.0 | 13.8 | +10.37 | 32.4 | -0.17 | 12.5 | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level | total | 18-15 | 54.5 | 51.9 | 2.7 | +1.3 | 4.0 | -0.27 | 24.2 | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | moneyline | 16-15 | 51.6 | 45.1 | 6.5 | -4.0 | -12.9 | 0.33 | 51.6 | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | spread | 20-13 | 60.6 | 55.3 | 5.3 | +5.27 | 16.0 | 0.02 | 21.2 | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | total | 20-11 | 64.5 | 51.3 | 13.2 | +7.08 | 22.9 | -0.19 | 29.0 | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | moneyline | 5-2 | 71.4 | 54.4 | 17.1 | +1.1 | 15.6 | 0.33 | 57.1 | keep collecting (7/30) |
| money_moving | spread | 4-5 | 44.4 | 55.3 | -10.8 | -1.28 | -14.3 | -0.11 | 22.2 | keep collecting (9/30) |
| money_moving | total | 4-2 | 66.7 | 48.8 | 17.9 | +1.83 | 30.5 | -0.67 | 0.0 | keep collecting (6/30) |
| pin_value | moneyline | 0-6 | 0.0 | 19.5 | -19.5 | -6.0 | -100.0 | 1.68 | 83.3 | keep collecting (6/30) |
| pin_value | spread | 11-4 | 73.3 | 55.3 | 18.0 | +5.64 | 37.6 | -0.03 | 20.0 | keep collecting (15/30) |
| pin_value | total | 5-6 | 45.5 | 50.3 | -4.9 | -1.52 | -13.8 | 0.0 | 18.2 | keep collecting (11/30) |
| pin_value | tt_away | 8-4 | 66.7 | 50.0 | 16.7 | +2.88 | 24.0 | 0.0 | 25.0 | keep collecting (12/30) |
| pin_value | tt_home | 6-5 | 54.5 | 50.0 | 4.5 | -0.02 | -0.1 | -0.18 | 18.2 | keep collecting (11/30) |
| book_lag | moneyline | 1-1 | 50.0 | 19.5 | 30.5 | +0.08 | 4.0 | 2.15 | 100.0 | keep collecting (2/30) |
| book_lag | spread | 1-2 | 33.3 | 55.3 | -22.0 | -1.13 | -37.7 | -0.17 | 66.7 | keep collecting (3/30) |
| consensus_gap | moneyline | 9-24 | 27.3 | 23.2 | 4.1 | -13.54 | -41.0 | 0.09 | 57.6 | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap | spread | 6-6 | 50.0 | 50.0 | 0.0 | -0.86 | -7.1 | 0.25 | 33.3 | keep collecting (12/30) |
| money_level+sharp_gap | moneyline | 12-3 | 80.0 | 72.4 | 7.6 | +2.34 | 15.6 | -0.53 | 33.3 | keep collecting (15/30) |
| consensus_gap+pre_move | moneyline | 3-9 | 25.0 | 19.5 | 5.5 | -5.18 | -43.2 | -0.26 | 66.7 | redundant -- identical record to pre_move alone, not independent confirmation |
| consensus_gap+sharp_gap | moneyline | 7-13 | 35.0 | 25.6 | 9.4 | -5.44 | -27.2 | 0.39 | 65.0 | keep collecting (20/30) |
| pre_move+sharp_gap | moneyline | 3-9 | 25.0 | 19.5 | 5.5 | -5.18 | -43.2 | -0.26 | 66.7 | redundant -- identical record to pre_move alone, not independent confirmation |
| consensus_gap+follow_move | moneyline | 0-1 | 0.0 | 19.5 | -19.5 | -1.0 | -100.0 | 0.5 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm | moneyline | 0-1 | 0.0 | 19.5 | -19.5 | -1.0 | -100.0 | 0.5 | 100.0 | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm | moneyline | 0-1 | 0.0 | 19.5 | -19.5 | -1.0 | -100.0 | 0.5 | 100.0 | redundant -- identical record to rlm alone, not independent confirmation |
| money_level+money_moving | moneyline | 4-0 | 100.0 | 80.5 | 19.5 | +2.02 | 50.4 | -0.78 | 50.0 | keep collecting (4/30) |
| follow_move+money_level | moneyline | 1-0 | 100.0 | 80.5 | 19.5 | +0.56 | 56.2 | -3.1 | 0.0 | keep collecting (1/30) |
| follow_move+money_moving | moneyline | 1-0 | 100.0 | 80.5 | 19.5 | +0.56 | 56.2 | -3.1 | 0.0 | keep collecting (1/30) |
| consensus_gap+money_level | moneyline | 3-1 | 75.0 | 50.0 | 25.0 | +0.9 | 22.4 | -2.6 | 50.0 | keep collecting (4/30) |
| consensus_gap+pin_value | moneyline | 0-5 | 0.0 | 19.5 | -19.5 | -5.0 | -100.0 | 1.64 | 80.0 | keep collecting (5/30) |
| consensus_gap+pin_rlm | moneyline | 1-4 | 20.0 | 19.5 | 0.5 | -2.92 | -58.4 | -0.8 | 80.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | moneyline | 0-1 | 0.0 | 19.5 | -19.5 | -1.0 | -100.0 | -10.6 | 0.0 | keep collecting (1/30) |
| money_level+pre_move | moneyline | 0-1 | 0.0 | 19.5 | -19.5 | -1.0 | -100.0 | -10.6 | 0.0 | keep collecting (1/30) |
| pin_rlm+pre_move | moneyline | 1-4 | 20.0 | 19.5 | 0.5 | -2.92 | -58.4 | -0.8 | 80.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | moneyline | 1-4 | 20.0 | 19.5 | 0.5 | -2.92 | -58.4 | -0.8 | 80.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+sharp_gap | moneyline | 2-1 | 66.7 | 39.8 | 26.8 | +0.47 | 15.7 | 1.1 | 66.7 | keep collecting (3/30) |
| pin_value+pre_move | moneyline | 0-3 | 0.0 | 19.5 | -19.5 | -3.0 | -100.0 | 3.03 | 100.0 | keep collecting (3/30) |
| pin_value+sharp_gap | moneyline | 0-3 | 0.0 | 19.5 | -19.5 | -3.0 | -100.0 | 3.03 | 100.0 | keep collecting (3/30) |
| consensus_gap+money_moving | moneyline | 1-1 | 50.0 | 19.5 | 30.5 | +0.08 | 4.0 | 3.45 | 100.0 | keep collecting (2/30) |
| money_moving+pin_value | moneyline | 0-1 | 0.0 | 19.5 | -19.5 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_moving+pre_move | moneyline | 1-1 | 50.0 | 19.5 | 30.5 | +0.08 | 4.0 | 3.45 | 100.0 | keep collecting (2/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 19.5 | -19.5 | -1.0 | -100.0 | 1.8 | 100.0 | keep collecting (1/30) |
| book_lag+consensus_gap | moneyline | 1-1 | 50.0 | 19.5 | 30.5 | +0.08 | 4.0 | 2.15 | 100.0 | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | moneyline | 1-0 | 100.0 | 19.5 | 80.5 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| book_lag+pin_rlm | moneyline | 1-0 | 100.0 | 19.5 | 80.5 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| book_lag+pre_move | moneyline | 1-0 | 100.0 | 19.5 | 80.5 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| book_lag+sharp_gap | moneyline | 1-0 | 100.0 | 19.5 | 80.5 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| money_moving+pin_rlm | moneyline | 1-0 | 100.0 | 19.5 | 80.5 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| follow_move+rlm | spread | 1-4 | 20.0 | 46.8 | -26.8 | -3.17 | -63.3 | 0.2 | 20.0 | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-6 | 62.5 | 55.9 | 6.6 | +3.14 | 19.7 | 0.19 | 18.8 | keep collecting (16/30) |
| rlm+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| rlm_ratio+sharp_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+pin_value | spread | 3-2 | 60.0 | 53.2 | 6.8 | +0.47 | 9.4 | 0.4 | 40.0 | keep collecting (5/30) |
| money_level+sharp_gap | spread | 17-8 | 68.0 | 57.0 | 11.0 | +7.65 | 30.6 | -0.1 | 16.0 | keep collecting (25/30) |
| follow_move+pin_value | spread | 4-1 | 80.0 | 59.5 | 20.5 | +2.47 | 49.3 | 0.0 | 0.0 | keep collecting (5/30) |
| pin_value+sharp_gap | spread | 7-0 | 100.0 | 56.8 | 43.2 | +6.17 | 88.1 | -0.07 | 14.3 | keep collecting (7/30) |
| consensus_gap+follow_move | spread | 1-0 | 100.0 | 65.9 | 34.1 | +0.82 | 82.0 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 3-0 | 100.0 | 65.9 | 34.1 | +2.56 | 85.3 | 0.33 | 33.3 | keep collecting (3/30) |
| consensus_gap+sharp_gap | spread | 3-1 | 75.0 | 65.9 | 9.1 | +1.56 | 39.0 | 0.38 | 50.0 | keep collecting (4/30) |
| follow_move+money_level | spread | 8-5 | 61.5 | 61.0 | 0.6 | +2.48 | 19.1 | 0.23 | 23.1 | keep collecting (13/30) |
| money_level+pin_value | spread | 6-1 | 85.7 | 61.3 | 24.4 | +4.33 | 61.9 | -0.07 | 14.3 | keep collecting (7/30) |
| follow_move+money_moving | spread | 2-2 | 50.0 | 57.9 | -7.9 | -0.19 | -4.7 | 0.0 | 0.0 | keep collecting (4/30) |
| money_level+money_moving | spread | 2-2 | 50.0 | 57.9 | -7.9 | -0.07 | -1.7 | -1.0 | 0.0 | keep collecting (4/30) |
| money_moving+pin_value | spread | 3-1 | 75.0 | 57.9 | 17.1 | +1.76 | 44.1 | 0.25 | 25.0 | keep collecting (4/30) |
| money_moving+sharp_gap | spread | 1-2 | 33.3 | 65.9 | -32.5 | -1.02 | -34.0 | -0.67 | 0.0 | keep collecting (3/30) |
| book_lag+consensus_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.13 | -6.5 | 0.75 | 100.0 | keep collecting (2/30) |
| money_level+pre_move | spread | 1-1 | 50.0 | 34.1 | 15.9 | -0.09 | -4.5 | -1.0 | 0.0 | keep collecting (2/30) |
| pre_move+sharp_gap | spread | 1-2 | 33.3 | 44.7 | -11.4 | -1.09 | -36.4 | -0.5 | 33.3 | redundant -- identical record to pre_move alone, not independent confirmation |
| book_lag+money_level | spread | 1-1 | 50.0 | 65.9 | -15.9 | -0.13 | -6.5 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+money_moving | spread | 0-1 | 0.0 | 65.9 | -65.9 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| book_lag+sharp_gap | spread | 1-1 | 50.0 | 65.9 | -15.9 | -0.13 | -6.5 | -0.5 | 50.0 | keep collecting (2/30) |
| money_moving+rlm | spread | 0-1 | 0.0 | 34.1 | -34.1 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| book_lag+pin_value | spread | 1-0 | 100.0 | 65.9 | 34.1 | +0.87 | 87.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+pin_value | total | 3-2 | 60.0 | 52.2 | 7.8 | +0.71 | 14.1 | -0.4 | 0.0 | keep collecting (5/30) |
| money_level+sharp_gap | total | 15-9 | 62.5 | 52.1 | 10.4 | +4.61 | 19.2 | -0.25 | 25.0 | keep collecting (24/30) |
| pin_value+sharp_gap | total | 4-2 | 66.7 | 51.2 | 15.4 | +1.58 | 26.3 | 0.0 | 16.7 | keep collecting (6/30) |
| money_level+pre_move | total | 1-2 | 33.3 | 48.8 | -15.4 | -1.13 | -37.7 | 1.0 | 33.3 | keep collecting (3/30) |
| pre_move+sharp_gap | total | 2-4 | 33.3 | 47.6 | -14.2 | -2.18 | -36.3 | -0.17 | 16.7 | redundant -- identical record to pre_move alone, not independent confirmation |
| follow_move+money_level | total | 0-1 | 0.0 | 53.7 | -53.7 | -1.0 | -100.0 | -3.0 | 0.0 | redundant -- identical record to follow_move alone, not independent confirmation |
| money_level+money_moving | total | 2-1 | 66.7 | 51.2 | 15.4 | +0.88 | 29.3 | -0.33 | 0.0 | keep collecting (3/30) |
| money_moving+sharp_gap | total | 3-0 | 100.0 | 48.8 | 51.2 | +2.83 | 94.3 | -0.67 | 0.0 | keep collecting (3/30) |
| money_moving+pin_value | total | 1-0 | 100.0 | 46.3 | 53.7 | +0.93 | 92.6 | 0.0 | 0.0 | keep collecting (1/30) |
| money_moving+pre_move | total | 1-0 | 100.0 | 46.3 | 53.7 | +0.95 | 95.2 | -2.0 | 0.0 | keep collecting (1/30) |

## CLOSE  (fit)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 5-10 | 33.3 | 30.7 | 2.6 | -5.07 | -33.8 |  |  | keep collecting (15/30) |
| pre_move | both | 3-8 | 27.3 | 37.7 | -10.4 | -3.38 | -30.8 |  |  | keep collecting (11/30) |
| follow_move | both | 55-63 | 46.6 | 50.2 | -3.6 | -18.15 | -15.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| rlm | both | 8-32 | 20.0 | 34.1 | -14.1 | -23.67 | -59.2 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| rlm_ratio | both | 5-14 | 26.3 | 33.1 | -6.8 | -9.07 | -47.7 |  |  | keep collecting (19/30) |
| money_level | both | 80-40 | 66.7 | 61.8 | 4.9 | +18.18 | 15.1 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 55-64 | 46.2 | 48.6 | -2.4 | -18.31 | -15.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | both | 35-56 | 38.5 | 43.1 | -4.6 | -26.49 | -29.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| pin_value | both | 57-42 | 57.6 | 49.2 | 8.4 | +6.93 | 7.0 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| book_lag | both | 5-1 | 83.3 | 65.4 | 17.9 | +2.86 | 47.7 |  |  | keep collecting (6/30) |
| consensus_gap | both | 17-32 | 34.7 | 29.5 | 5.2 | -13.57 | -27.7 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+rlm | both | 8-32 | 20.0 | 34.1 | -14.1 | -23.67 | -59.2 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | both | 5-14 | 26.3 | 33.1 | -6.8 | -9.07 | -47.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 22-28 | 44.0 | 48.2 | -4.2 | -10.11 | -20.2 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level+pin_value | both | 15-6 | 71.4 | 57.7 | 13.7 | +6.96 | 33.1 |  |  | keep collecting (21/30) |
| rlm+rlm_ratio | both | 5-14 | 26.3 | 33.1 | -6.8 | -9.07 | -47.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | both | 6-19 | 24.0 | 34.8 | -10.8 | -13.2 | -52.8 |  |  | keep collecting (25/30) |
| rlm_ratio+sharp_gap | both | 5-14 | 26.3 | 33.1 | -6.8 | -9.07 | -47.7 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 40-25 | 61.5 | 59.4 | 2.1 | +4.82 | 7.4 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+money_level | both | 7-1 | 87.5 | 55.8 | 31.7 | +4.86 | 60.7 |  |  | keep collecting (8/30) |
| pre_move+sharp_gap | both | 3-8 | 27.3 | 37.7 | -10.4 | -3.38 | -30.8 |  |  | redundant -- identical record to pre_move alone, not independent confirmation |
| follow_move+money_level | both | 28-14 | 66.7 | 64.7 | 2.0 | +5.69 | 13.5 |  |  | HYPOTHESIS (in-sample) -- beats break-even but not its base rate -- directional bias, not signal |
| book_lag+money_level | both | 2-1 | 66.7 | 75.6 | -8.9 | +0.4 | 13.4 |  |  | keep collecting (3/30) |
| consensus_gap+pre_move | both | 1-2 | 33.3 | 19.5 | 13.8 | +0.9 | 30.0 |  |  | keep collecting (3/30) |
| consensus_gap+sharp_gap | both | 8-14 | 36.4 | 29.2 | 7.2 | -4.75 | -21.6 |  |  | keep collecting (22/30) |
| follow_move+pin_value | both | 10-7 | 58.8 | 50.9 | 8.0 | +1.43 | 8.4 |  |  | keep collecting (17/30) |
| pin_value+rlm | both | 2-6 | 25.0 | 39.6 | -14.6 | -4.26 | -53.2 |  |  | keep collecting (8/30) |
| pin_value+pre_move | both | 1-1 | 50.0 | 32.9 | 17.1 | -0.15 | -7.7 |  |  | keep collecting (2/30) |
| pin_value+sharp_gap | both | 15-11 | 57.7 | 47.2 | 10.5 | +1.58 | 6.1 |  |  | keep collecting (26/30) |
| consensus_gap+follow_move | both | 5-15 | 25.0 | 27.9 | -2.9 | -9.56 | -47.8 |  |  | keep collecting (20/30) |
| consensus_gap+rlm | both | 3-15 | 16.7 | 22.1 | -5.4 | -11.1 | -61.7 |  |  | keep collecting (18/30) |
| consensus_gap+pin_value | both | 3-6 | 33.3 | 22.8 | 10.6 | -3.42 | -38.0 |  |  | keep collecting (9/30) |
| book_lag+consensus_gap | both | 3-0 | 100.0 | 55.3 | 44.7 | +2.46 | 82.0 |  |  | keep collecting (3/30) |
| book_lag+money_moving | both | 1-0 | 100.0 | 34.1 | 65.9 | +0.78 | 78.1 |  |  | keep collecting (1/30) |
| book_lag+pin_value | both | 2-0 | 100.0 | 50.0 | 50.0 | +1.61 | 80.7 |  |  | keep collecting (2/30) |
| consensus_gap+money_moving | both | 6-15 | 28.6 | 23.1 | 5.5 | -8.63 | -41.1 |  |  | keep collecting (21/30) |
| money_moving+pin_value | both | 10-10 | 50.0 | 44.3 | 5.7 | -1.66 | -8.3 |  |  | keep collecting (20/30) |
| money_moving+pre_move | both | 1-3 | 25.0 | 37.2 | -12.2 | -2.13 | -53.2 |  |  | keep collecting (4/30) |
| money_moving+sharp_gap | both | 24-38 | 38.7 | 43.0 | -4.3 | -17.33 | -28.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| follow_move+money_moving | both | 13-28 | 31.7 | 43.5 | -11.8 | -16.85 | -41.1 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving+rlm | both | 5-22 | 18.5 | 32.9 | -14.4 | -17.07 | -63.2 |  |  | keep collecting (27/30) |
| money_level+money_moving | both | 23-13 | 63.9 | 57.8 | 6.1 | +5.27 | 14.6 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| consensus_gap+pin_rlm | both | 2-6 | 25.0 | 19.5 | 5.5 | -3.76 | -47.0 |  |  | keep collecting (8/30) |
| consensus_gap+rlm_ratio | both | 2-6 | 25.0 | 19.5 | 5.5 | -3.76 | -47.0 |  |  | keep collecting (8/30) |
| follow_move+pin_rlm | both | 5-10 | 33.3 | 30.7 | 2.6 | -5.07 | -33.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | both | 0-3 | 0.0 | 39.8 | -39.8 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| money_level+rlm | both | 0-3 | 0.0 | 39.8 | -39.8 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| money_level+rlm_ratio | both | 0-3 | 0.0 | 39.8 | -39.8 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| money_moving+pin_rlm | both | 5-10 | 33.3 | 30.7 | 2.6 | -5.07 | -33.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+rlm_ratio | both | 5-12 | 29.4 | 31.1 | -1.7 | -7.07 | -41.6 |  |  | keep collecting (17/30) |
| pin_rlm+rlm | both | 5-10 | 33.3 | 30.7 | 2.6 | -5.07 | -33.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | both | 5-10 | 33.3 | 30.7 | 2.6 | -5.07 | -33.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | both | 5-10 | 33.3 | 30.7 | 2.6 | -5.07 | -33.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+pin_value | both | 1-3 | 25.0 | 32.9 | -7.9 | -2.13 | -53.2 |  |  | keep collecting (4/30) |
| pin_value+rlm_ratio | both | 1-3 | 25.0 | 32.9 | -7.9 | -2.13 | -53.2 |  |  | keep collecting (4/30) |
| money_level+pre_move | both | 1-1 | 50.0 | 34.1 | 15.9 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| pin_rlm | moneyline | 2-7 | 22.2 | 19.5 | 2.7 | -4.76 | -52.9 |  |  | keep collecting (9/30) |
| pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_rlm | total | 3-1 | 75.0 | 46.3 | 28.7 | +1.69 | 42.2 |  |  | keep collecting (4/30) |
| pre_move | moneyline | 1-3 | 25.0 | 34.8 | -9.8 | -0.1 | -2.5 |  |  | keep collecting (4/30) |
| pre_move | spread | 1-3 | 25.0 | 34.1 | -9.1 | -2.13 | -53.2 |  |  | keep collecting (4/30) |
| pre_move | total | 1-2 | 33.3 | 46.3 | -13.0 | -1.15 | -38.4 |  |  | keep collecting (3/30) |
| follow_move | moneyline | 15-18 | 45.5 | 45.4 | 0.1 | -9.14 | -27.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move | spread | 15-20 | 42.9 | 55.0 | -12.1 | -6.23 | -17.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| follow_move | total | 9-9 | 50.0 | 50.0 | 0.0 | -0.8 | -4.5 |  |  | keep collecting (18/30) |
| follow_move | tt_away | 8-7 | 53.3 | 50.0 | 3.3 | -0.0 | -0.0 |  |  | keep collecting (15/30) |
| follow_move | tt_home | 8-9 | 47.1 | 50.0 | -2.9 | -1.97 | -11.6 |  |  | keep collecting (17/30) |
| rlm | moneyline | 3-16 | 15.8 | 19.5 | -3.7 | -12.1 | -63.7 |  |  | keep collecting (19/30) |
| rlm | spread | 1-11 | 8.3 | 47.4 | -39.0 | -10.13 | -84.4 |  |  | keep collecting (12/30) |
| rlm | total | 4-5 | 44.4 | 47.2 | -2.7 | -1.44 | -16.0 |  |  | keep collecting (9/30) |
| rlm_ratio | moneyline | 2-7 | 22.2 | 19.5 | 2.7 | -4.76 | -52.9 |  |  | keep collecting (9/30) |
| rlm_ratio | spread | 0-6 | 0.0 | 44.7 | -44.7 | -6.0 | -100.0 |  |  | keep collecting (6/30) |
| rlm_ratio | total | 3-1 | 75.0 | 46.3 | 28.7 | +1.69 | 42.2 |  |  | keep collecting (4/30) |
| money_level | moneyline | 34-6 | 85.0 | 75.9 | 9.1 | +10.25 | 25.6 |  |  | HYPOTHESIS (in-sample) -- PROMOTE: beats break-even and its own base rate |
| money_level | spread | 24-16 | 60.0 | 56.3 | 3.7 | +5.72 | 14.3 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_level | total | 22-18 | 55.0 | 53.1 | 1.9 | +2.21 | 5.5 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | moneyline | 20-18 | 52.6 | 51.6 | 1.0 | -3.69 | -9.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| sharp_gap | spread | 16-24 | 40.0 | 43.7 | -3.7 | -9.82 | -24.5 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| sharp_gap | total | 19-22 | 46.3 | 50.6 | -4.3 | -4.8 | -11.7 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| money_moving | moneyline | 12-19 | 38.7 | 37.2 | 1.5 | -10.22 | -33.0 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| money_moving | spread | 9-20 | 31.0 | 41.8 | -10.8 | -12.0 | -41.4 |  |  | keep collecting (29/30) |
| money_moving | total | 14-17 | 45.2 | 50.1 | -5.0 | -4.27 | -13.8 |  |  | HYPOTHESIS (in-sample) -- no edge shown yet |
| pin_value | moneyline | 2-6 | 25.0 | 27.1 | -2.1 | -4.59 | -57.4 |  |  | keep collecting (8/30) |
| pin_value | spread | 15-3 | 83.3 | 55.3 | 28.0 | +10.04 | 55.8 |  |  | keep collecting (18/30) |
| pin_value | total | 11-10 | 52.4 | 50.5 | 1.9 | -0.38 | -1.8 |  |  | keep collecting (21/30) |
| pin_value | tt_away | 14-11 | 56.0 | 50.0 | 6.0 | +1.14 | 4.6 |  |  | keep collecting (25/30) |
| pin_value | tt_home | 15-12 | 55.6 | 50.0 | 5.6 | +0.73 | 2.7 |  |  | keep collecting (27/30) |
| book_lag | moneyline | 1-1 | 50.0 | 80.5 | -30.5 | -0.43 | -21.6 |  |  | keep collecting (2/30) |
| book_lag | spread | 4-0 | 100.0 | 57.9 | 42.1 | +3.29 | 82.4 |  |  | keep collecting (4/30) |
| consensus_gap | moneyline | 12-29 | 29.3 | 25.5 | 3.8 | -14.7 | -35.8 |  |  | HYPOTHESIS (in-sample) -- DROP: below break-even |
| consensus_gap | spread | 5-3 | 62.5 | 50.0 | 12.5 | +1.13 | 14.1 |  |  | keep collecting (8/30) |
| consensus_gap+money_level | moneyline | 6-1 | 85.7 | 54.4 | 31.4 | +4.02 | 57.5 |  |  | keep collecting (7/30) |
| pre_move+sharp_gap | moneyline | 1-3 | 25.0 | 34.8 | -9.8 | -0.1 | -2.5 |  |  | redundant -- identical record to pre_move alone, not independent confirmation |
| book_lag+money_level | moneyline | 1-1 | 50.0 | 80.5 | -30.5 | -0.43 | -21.6 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| consensus_gap+pre_move | moneyline | 1-2 | 33.3 | 19.5 | 13.8 | +0.9 | 30.0 |  |  | keep collecting (3/30) |
| consensus_gap+sharp_gap | moneyline | 7-13 | 35.0 | 28.7 | 6.3 | -4.58 | -22.9 |  |  | keep collecting (20/30) |
| money_level+sharp_gap | moneyline | 17-4 | 81.0 | 74.7 | 6.3 | +5.17 | 24.6 |  |  | keep collecting (21/30) |
| consensus_gap+follow_move | moneyline | 5-14 | 26.3 | 25.9 | 0.4 | -8.56 | -45.1 |  |  | keep collecting (19/30) |
| consensus_gap+rlm | moneyline | 3-14 | 17.6 | 19.5 | -1.9 | -10.1 | -59.4 |  |  | keep collecting (17/30) |
| follow_move+rlm | moneyline | 3-16 | 15.8 | 19.5 | -3.7 | -12.1 | -63.7 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 1-6 | 14.3 | 19.5 | -5.2 | -5.04 | -72.0 |  |  | keep collecting (7/30) |
| pin_value+pre_move | moneyline | 0-1 | 0.0 | 19.5 | -19.5 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 1-4 | 20.0 | 31.7 | -11.7 | -3.56 | -71.1 |  |  | keep collecting (5/30) |
| follow_move+money_level | moneyline | 12-2 | 85.7 | 76.1 | 9.6 | +2.96 | 21.1 |  |  | keep collecting (14/30) |
| follow_move+sharp_gap | moneyline | 8-8 | 50.0 | 46.2 | 3.8 | -2.79 | -17.5 |  |  | keep collecting (16/30) |
| follow_move+money_moving | moneyline | 6-12 | 33.3 | 36.4 | -3.1 | -7.35 | -40.8 |  |  | keep collecting (18/30) |
| money_moving+rlm | moneyline | 2-11 | 15.4 | 19.5 | -4.1 | -8.76 | -67.4 |  |  | keep collecting (13/30) |
| consensus_gap+money_moving | moneyline | 5-15 | 25.0 | 22.6 | 2.4 | -9.41 | -47.1 |  |  | keep collecting (20/30) |
| money_moving+pin_value | moneyline | 2-4 | 33.3 | 29.7 | 3.7 | -2.59 | -43.2 |  |  | keep collecting (6/30) |
| consensus_gap+pin_rlm | moneyline | 2-6 | 25.0 | 19.5 | 5.5 | -3.76 | -47.0 |  |  | keep collecting (8/30) |
| consensus_gap+rlm_ratio | moneyline | 2-6 | 25.0 | 19.5 | 5.5 | -3.76 | -47.0 |  |  | keep collecting (8/30) |
| follow_move+pin_rlm | moneyline | 2-7 | 22.2 | 19.5 | 2.7 | -4.76 | -52.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+rlm_ratio | moneyline | 2-7 | 22.2 | 19.5 | 2.7 | -4.76 | -52.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+money_moving | moneyline | 9-2 | 81.8 | 69.4 | 12.4 | +3.57 | 32.5 |  |  | keep collecting (11/30) |
| money_level+pin_rlm | moneyline | 0-1 | 0.0 | 19.5 | -19.5 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_level+rlm | moneyline | 0-1 | 0.0 | 19.5 | -19.5 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_level+rlm_ratio | moneyline | 0-1 | 0.0 | 19.5 | -19.5 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_moving+pin_rlm | moneyline | 2-7 | 22.2 | 19.5 | 2.7 | -4.76 | -52.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+rlm_ratio | moneyline | 2-7 | 22.2 | 19.5 | 2.7 | -4.76 | -52.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+sharp_gap | moneyline | 9-12 | 42.9 | 39.8 | 3.0 | -4.87 | -23.2 |  |  | keep collecting (21/30) |
| pin_rlm+rlm | moneyline | 2-7 | 22.2 | 19.5 | 2.7 | -4.76 | -52.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | moneyline | 2-7 | 22.2 | 19.5 | 2.7 | -4.76 | -52.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | moneyline | 2-7 | 22.2 | 19.5 | 2.7 | -4.76 | -52.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm+rlm_ratio | moneyline | 2-7 | 22.2 | 19.5 | 2.7 | -4.76 | -52.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | moneyline | 2-7 | 22.2 | 19.5 | 2.7 | -4.76 | -52.9 |  |  | keep collecting (9/30) |
| rlm_ratio+sharp_gap | moneyline | 2-7 | 22.2 | 19.5 | 2.7 | -4.76 | -52.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_value | moneyline | 1-3 | 25.0 | 34.8 | -9.8 | -2.56 | -63.9 |  |  | keep collecting (4/30) |
| pin_rlm+pin_value | moneyline | 0-2 | 0.0 | 19.5 | -19.5 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_value+rlm | moneyline | 0-3 | 0.0 | 19.5 | -19.5 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| pin_value+rlm_ratio | moneyline | 0-2 | 0.0 | 19.5 | -19.5 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_level+pin_value | moneyline | 1-0 | 100.0 | 80.5 | 19.5 | +0.44 | 44.4 |  |  | keep collecting (1/30) |
| follow_move+rlm | spread | 1-11 | 8.3 | 47.4 | -39.0 | -10.13 | -84.4 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 0-6 | 0.0 | 44.7 | -44.7 | -6.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 8-13 | 38.1 | 49.2 | -11.1 | -5.74 | -27.3 |  |  | keep collecting (21/30) |
| money_level+pin_value | spread | 8-2 | 80.0 | 59.5 | 20.5 | +5.18 | 51.8 |  |  | keep collecting (10/30) |
| rlm+rlm_ratio | spread | 0-6 | 0.0 | 44.7 | -44.7 | -6.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | spread | 0-9 | 0.0 | 41.2 | -41.2 | -9.0 | -100.0 |  |  | keep collecting (9/30) |
| rlm_ratio+sharp_gap | spread | 0-6 | 0.0 | 44.7 | -44.7 | -6.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 11-9 | 55.0 | 61.1 | -6.1 | +1.09 | 5.4 |  |  | keep collecting (20/30) |
| follow_move+pin_value | spread | 6-1 | 85.7 | 61.3 | 24.4 | +4.28 | 61.2 |  |  | keep collecting (7/30) |
| pin_value+rlm | spread | 1-0 | 100.0 | 65.9 | 34.1 | +0.87 | 87.0 |  |  | keep collecting (1/30) |
| money_level+sharp_gap | spread | 10-9 | 52.6 | 50.8 | 1.8 | -0.14 | -0.8 |  |  | keep collecting (19/30) |
| consensus_gap+sharp_gap | spread | 1-1 | 50.0 | 34.1 | 15.9 | -0.17 | -8.4 |  |  | keep collecting (2/30) |
| book_lag+consensus_gap | spread | 3-0 | 100.0 | 55.3 | 44.7 | +2.46 | 82.0 |  |  | keep collecting (3/30) |
| pin_value+sharp_gap | spread | 7-1 | 87.5 | 50.0 | 37.5 | +5.0 | 62.6 |  |  | keep collecting (8/30) |
| book_lag+money_moving | spread | 1-0 | 100.0 | 34.1 | 65.9 | +0.78 | 78.1 |  |  | keep collecting (1/30) |
| book_lag+pin_value | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.61 | 80.7 |  |  | keep collecting (2/30) |
| consensus_gap+money_moving | spread | 1-0 | 100.0 | 34.1 | 65.9 | +0.78 | 78.1 |  |  | keep collecting (1/30) |
| consensus_gap+pin_value | spread | 2-0 | 100.0 | 34.1 | 65.9 | +1.61 | 80.7 |  |  | keep collecting (2/30) |
| money_moving+pin_value | spread | 4-0 | 100.0 | 50.0 | 50.0 | +3.43 | 85.8 |  |  | keep collecting (4/30) |
| money_level+money_moving | spread | 6-5 | 54.5 | 51.4 | 3.1 | +0.39 | 3.6 |  |  | keep collecting (11/30) |
| money_moving+sharp_gap | spread | 6-14 | 30.0 | 38.9 | -8.9 | -8.55 | -42.8 |  |  | keep collecting (20/30) |
| money_level+pre_move | spread | 1-1 | 50.0 | 34.1 | 15.9 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| money_moving+pre_move | spread | 1-2 | 33.3 | 34.1 | -0.8 | -1.13 | -37.7 |  |  | keep collecting (3/30) |
| pre_move+sharp_gap | spread | 1-3 | 25.0 | 34.1 | -9.1 | -2.13 | -53.2 |  |  | redundant -- identical record to pre_move alone, not independent confirmation |
| follow_move+money_moving | spread | 2-9 | 18.2 | 48.6 | -30.4 | -7.09 | -64.5 |  |  | keep collecting (11/30) |
| money_moving+rlm | spread | 0-7 | 0.0 | 43.2 | -43.2 | -7.0 | -100.0 |  |  | keep collecting (7/30) |
| follow_move+pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_level+rlm_ratio | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_moving+pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+rlm_ratio | spread | 0-4 | 0.0 | 42.1 | -42.1 | -4.0 | -100.0 |  |  | keep collecting (4/30) |
| pin_rlm+rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+follow_move | spread | 0-1 | 0.0 | 65.9 | -65.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| consensus_gap+rlm | spread | 0-1 | 0.0 | 65.9 | -65.9 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| book_lag+money_level | spread | 1-0 | 100.0 | 65.9 | 34.1 | +0.83 | 83.3 |  |  | keep collecting (1/30) |
| consensus_gap+money_level | spread | 1-0 | 100.0 | 65.9 | 34.1 | +0.83 | 83.3 |  |  | keep collecting (1/30) |
| money_level+sharp_gap | total | 13-12 | 52.0 | 53.1 | -1.1 | -0.2 | -0.8 |  |  | keep collecting (25/30) |
| pin_value+pre_move | total | 1-0 | 100.0 | 46.3 | 53.7 | +0.85 | 84.7 |  |  | keep collecting (1/30) |
| pin_value+sharp_gap | total | 7-6 | 53.8 | 51.4 | 2.4 | +0.13 | 1.0 |  |  | keep collecting (13/30) |
| pre_move+sharp_gap | total | 1-2 | 33.3 | 46.3 | -13.0 | -1.15 | -38.4 |  |  | redundant -- identical record to pre_move alone, not independent confirmation |
| money_level+pin_value | total | 6-4 | 60.0 | 53.7 | 6.3 | +1.33 | 13.3 |  |  | keep collecting (10/30) |
| money_moving+pre_move | total | 0-1 | 0.0 | 46.3 | -46.3 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_moving+sharp_gap | total | 9-12 | 42.9 | 50.2 | -7.3 | -3.91 | -18.6 |  |  | keep collecting (21/30) |
| money_level+money_moving | total | 8-6 | 57.1 | 53.7 | 3.5 | +1.31 | 9.3 |  |  | keep collecting (14/30) |
| money_moving+pin_value | total | 4-6 | 40.0 | 50.7 | -10.7 | -2.5 | -25.0 |  |  | keep collecting (10/30) |
| follow_move+money_moving | total | 5-7 | 41.7 | 49.4 | -7.7 | -2.4 | -20.0 |  |  | keep collecting (12/30) |
| follow_move+pin_rlm | total | 3-1 | 75.0 | 46.3 | 28.7 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+pin_value | total | 2-3 | 40.0 | 49.3 | -9.3 | -1.18 | -23.6 |  |  | keep collecting (5/30) |
| follow_move+rlm | total | 4-5 | 44.4 | 47.2 | -2.7 | -1.44 | -16.0 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | total | 3-1 | 75.0 | 46.3 | 28.7 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 6-7 | 46.2 | 49.2 | -3.0 | -1.58 | -12.2 |  |  | keep collecting (13/30) |
| money_moving+pin_rlm | total | 3-1 | 75.0 | 46.3 | 28.7 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+rlm | total | 3-4 | 42.9 | 47.4 | -4.5 | -1.31 | -18.7 |  |  | keep collecting (7/30) |
| money_moving+rlm_ratio | total | 3-1 | 75.0 | 46.3 | 28.7 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| pin_rlm+pin_value | total | 1-1 | 50.0 | 46.3 | 3.7 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| pin_rlm+rlm | total | 3-1 | 75.0 | 46.3 | 28.7 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | total | 3-1 | 75.0 | 46.3 | 28.7 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | total | 3-1 | 75.0 | 46.3 | 28.7 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm | total | 1-3 | 25.0 | 48.2 | -23.2 | -2.13 | -53.2 |  |  | keep collecting (4/30) |
| pin_value+rlm_ratio | total | 1-1 | 50.0 | 46.3 | 3.7 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| rlm+rlm_ratio | total | 3-1 | 75.0 | 46.3 | 28.7 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | total | 4-3 | 57.1 | 46.3 | 10.8 | +0.56 | 8.0 |  |  | keep collecting (7/30) |
| rlm_ratio+sharp_gap | total | 3-1 | 75.0 | 46.3 | 28.7 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | total | 5-3 | 62.5 | 53.7 | 8.8 | +1.64 | 20.5 |  |  | keep collecting (8/30) |
| follow_move+pin_value | tt_home | 1-0 | 100.0 | 50.0 | 50.0 | +0.89 | 88.5 |  |  | keep collecting (1/30) |

# Pooled (fit + forward together)

Kept for continuity with earlier runs. **This table is contaminated** — it
mixes the games the engine was built on with the games testing it. Use the
forward table for any decision.

## EARLY  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 1-4 | 20.0 | 21.4 | -1.4 | -2.92 | -58.4 | -0.8 | 80.0 | keep collecting (5/30) |
| pre_move | both | 7-15 | 31.8 | 31.6 | 0.2 | -6.51 | -29.6 | -0.23 | 50.0 | keep collecting (22/30) |
| follow_move | both | 12-13 | 48.0 | 54.8 | -6.8 | -2.46 | -9.8 | -0.1 | 20.0 | keep collecting (25/30) |
| rlm | both | 1-6 | 14.3 | 45.9 | -31.6 | -5.17 | -73.8 | 0.07 | 28.6 | keep collecting (7/30) |
| rlm_ratio | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| money_level | both | 68-32 | 68.0 | 60.4 | 7.6 | +17.46 | 17.5 | -0.37 | 25.0 | PROMOTE: beats break-even and its own base rate |
| sharp_gap | both | 58-40 | 59.2 | 50.2 | 9.0 | +10.17 | 10.4 | 0.05 | 34.7 | no edge shown yet |
| money_moving | both | 15-9 | 62.5 | 52.2 | 10.3 | +3.38 | 14.1 | -0.03 | 33.3 | keep collecting (24/30) |
| pin_value | both | 32-25 | 56.1 | 48.1 | 8.1 | +2.71 | 4.7 | 0.17 | 29.8 | no edge shown yet |
| book_lag | both | 2-3 | 40.0 | 41.4 | -1.4 | -1.05 | -21.0 | 0.76 | 80.0 | keep collecting (5/30) |
| consensus_gap | both | 17-30 | 36.2 | 31.5 | 4.7 | -11.59 | -24.7 | 0.16 | 53.2 | DROP: below break-even |
| follow_move+rlm | both | 1-6 | 14.3 | 45.9 | -31.6 | -5.17 | -73.8 | 0.07 | 28.6 | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 10-6 | 62.5 | 55.4 | 7.1 | +3.14 | 19.7 | 0.19 | 18.8 | keep collecting (16/30) |
| rlm+rlm_ratio | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| rlm_ratio+sharp_gap | both | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+pin_value | both | 10-3 | 76.9 | 55.5 | 21.4 | +5.91 | 45.4 | -0.12 | 15.4 | keep collecting (13/30) |
| money_level+sharp_gap | both | 45-20 | 69.2 | 58.1 | 11.2 | +15.48 | 23.8 | -0.24 | 24.6 | PROMOTE: beats break-even and its own base rate |
| pin_value+sharp_gap | both | 12-5 | 70.6 | 47.2 | 23.4 | +5.61 | 33.0 | 0.56 | 35.3 | keep collecting (17/30) |
| consensus_gap+pin_value | both | 4-7 | 36.4 | 37.0 | -0.6 | -3.66 | -33.3 | 1.02 | 63.6 | keep collecting (11/30) |
| money_level+pre_move | both | 2-4 | 33.3 | 39.7 | -6.3 | -2.22 | -37.0 | -1.6 | 16.7 | keep collecting (6/30) |
| pre_move+sharp_gap | both | 7-15 | 31.8 | 31.6 | 0.2 | -6.51 | -29.6 | -0.23 | 50.0 | redundant -- identical record to pre_move alone, not independent confirmation |
| follow_move+pin_value | both | 4-1 | 80.0 | 58.6 | 21.4 | +2.47 | 49.3 | 0.0 | 0.0 | keep collecting (5/30) |
| consensus_gap+follow_move | both | 1-1 | 50.0 | 42.9 | 7.1 | -0.18 | -9.0 | 0.25 | 50.0 | keep collecting (2/30) |
| consensus_gap+money_level | both | 7-1 | 87.5 | 53.6 | 33.9 | +4.33 | 54.1 | -1.05 | 50.0 | keep collecting (8/30) |
| consensus_gap+sharp_gap | both | 12-14 | 46.2 | 33.0 | 13.2 | -1.07 | -4.1 | 0.41 | 65.4 | keep collecting (26/30) |
| follow_move+money_level | both | 9-6 | 60.0 | 60.8 | -0.8 | +2.04 | 13.6 | -0.21 | 20.0 | keep collecting (15/30) |
| consensus_gap+pre_move | both | 4-9 | 30.8 | 21.4 | 9.3 | -3.24 | -24.9 | -0.2 | 69.2 | keep collecting (13/30) |
| follow_move+money_moving | both | 3-2 | 60.0 | 61.4 | -1.4 | +0.38 | 7.5 | -0.62 | 0.0 | keep collecting (5/30) |
| money_level+money_moving | both | 10-3 | 76.9 | 60.6 | 16.3 | +4.57 | 35.1 | -0.47 | 30.8 | keep collecting (13/30) |
| money_moving+pin_value | both | 5-2 | 71.4 | 47.3 | 24.1 | +2.56 | 36.6 | 1.0 | 42.9 | keep collecting (7/30) |
| money_moving+sharp_gap | both | 7-3 | 70.0 | 49.5 | 20.5 | +3.15 | 31.5 | 0.03 | 30.0 | keep collecting (10/30) |
| consensus_gap+rlm | both | 0-1 | 0.0 | 21.4 | -21.4 | -1.0 | -100.0 | 0.5 | 100.0 | keep collecting (1/30) |
| book_lag+consensus_gap | both | 2-2 | 50.0 | 35.7 | 14.3 | -0.05 | -1.2 | 1.45 | 100.0 | keep collecting (4/30) |
| consensus_gap+pin_rlm | both | 1-4 | 20.0 | 21.4 | -1.4 | -2.92 | -58.4 | -0.8 | 80.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | both | 0-1 | 0.0 | 21.4 | -21.4 | -1.0 | -100.0 | -10.6 | 0.0 | keep collecting (1/30) |
| pin_rlm+pre_move | both | 1-4 | 20.0 | 21.4 | -1.4 | -2.92 | -58.4 | -0.8 | 80.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | both | 1-4 | 20.0 | 21.4 | -1.4 | -2.92 | -58.4 | -0.8 | 80.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| book_lag+money_level | both | 1-1 | 50.0 | 64.3 | -14.3 | -0.13 | -6.5 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+money_moving | both | 1-1 | 50.0 | 42.9 | 7.1 | +0.08 | 4.0 | -0.05 | 50.0 | keep collecting (2/30) |
| book_lag+sharp_gap | both | 2-1 | 66.7 | 50.0 | 16.7 | +0.95 | 31.7 | 0.3 | 66.7 | keep collecting (3/30) |
| pin_value+pre_move | both | 0-3 | 0.0 | 21.4 | -21.4 | -3.0 | -100.0 | 3.03 | 100.0 | keep collecting (3/30) |
| consensus_gap+money_moving | both | 2-1 | 66.7 | 26.2 | 40.5 | +0.95 | 31.7 | 2.63 | 100.0 | keep collecting (3/30) |
| money_moving+pre_move | both | 2-1 | 66.7 | 29.4 | 37.3 | +1.03 | 34.4 | 1.63 | 66.7 | keep collecting (3/30) |
| pin_rlm+pin_value | both | 0-1 | 0.0 | 21.4 | -21.4 | -1.0 | -100.0 | 1.8 | 100.0 | keep collecting (1/30) |
| book_lag+pin_rlm | both | 1-0 | 100.0 | 21.4 | 78.6 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| book_lag+pre_move | both | 1-0 | 100.0 | 21.4 | 78.6 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| money_moving+pin_rlm | both | 1-0 | 100.0 | 21.4 | 78.6 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| money_moving+rlm | both | 0-1 | 0.0 | 35.7 | -35.7 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| book_lag+pin_value | both | 1-0 | 100.0 | 64.3 | 35.7 | +0.87 | 87.0 | 1.0 | 100.0 | keep collecting (1/30) |
| pin_rlm | moneyline | 1-4 | 20.0 | 21.4 | -1.4 | -2.92 | -58.4 | -0.8 | 80.0 | keep collecting (5/30) |
| pre_move | moneyline | 4-9 | 30.8 | 21.4 | 9.3 | -3.24 | -24.9 | -0.2 | 69.2 | keep collecting (13/30) |
| pre_move | spread | 1-2 | 33.3 | 45.2 | -11.9 | -1.09 | -36.4 | -0.5 | 33.3 | keep collecting (3/30) |
| pre_move | total | 2-4 | 33.3 | 46.8 | -13.5 | -2.18 | -36.3 | -0.17 | 16.7 | keep collecting (6/30) |
| follow_move | moneyline | 1-1 | 50.0 | 50.0 | 0.0 | -0.44 | -21.9 | -1.3 | 50.0 | keep collecting (2/30) |
| follow_move | spread | 11-11 | 50.0 | 55.2 | -5.2 | -1.02 | -4.6 | 0.14 | 18.2 | keep collecting (22/30) |
| follow_move | total | 0-1 | 0.0 | 54.8 | -54.8 | -1.0 | -100.0 | -3.0 | 0.0 | keep collecting (1/30) |
| rlm | moneyline | 0-1 | 0.0 | 21.4 | -21.4 | -1.0 | -100.0 | 0.5 | 100.0 | keep collecting (1/30) |
| rlm | spread | 1-5 | 16.7 | 50.0 | -33.3 | -4.17 | -69.5 | 0.0 | 16.7 | keep collecting (6/30) |
| rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| money_level | moneyline | 26-7 | 78.8 | 75.1 | 3.7 | +4.05 | 12.3 | -0.75 | 33.3 | beats break-even but not its base rate -- directional bias, not signal |
| money_level | spread | 23-10 | 69.7 | 53.9 | 15.8 | +11.23 | 34.0 | -0.14 | 15.2 | PROMOTE: beats break-even and its own base rate |
| money_level | total | 19-15 | 55.9 | 52.5 | 3.4 | +2.17 | 6.4 | -0.24 | 26.5 | no edge shown yet |
| sharp_gap | moneyline | 17-15 | 53.1 | 44.6 | 8.5 | -2.06 | -6.4 | 0.33 | 53.1 | no edge shown yet |
| sharp_gap | spread | 21-13 | 61.8 | 54.2 | 7.6 | +6.14 | 18.1 | 0.04 | 23.5 | no edge shown yet |
| sharp_gap | total | 20-12 | 62.5 | 51.5 | 11.0 | +6.08 | 19.0 | -0.22 | 28.1 | no edge shown yet |
| money_moving | moneyline | 5-2 | 71.4 | 54.1 | 17.3 | +1.1 | 15.6 | 0.33 | 57.1 | keep collecting (7/30) |
| money_moving | spread | 5-5 | 50.0 | 52.9 | -2.9 | -0.41 | -4.1 | 0.0 | 30.0 | keep collecting (10/30) |
| money_moving | total | 5-2 | 71.4 | 49.3 | 22.1 | +2.7 | 38.6 | -0.43 | 14.3 | keep collecting (7/30) |
| pin_value | moneyline | 0-6 | 0.0 | 21.4 | -21.4 | -6.0 | -100.0 | 1.68 | 83.3 | keep collecting (6/30) |
| pin_value | spread | 12-4 | 75.0 | 53.6 | 21.4 | +6.51 | 40.7 | 0.03 | 25.0 | keep collecting (16/30) |
| pin_value | total | 5-6 | 45.5 | 50.4 | -5.0 | -1.52 | -13.8 | 0.0 | 18.2 | keep collecting (11/30) |
| pin_value | tt_away | 8-4 | 66.7 | 50.0 | 16.7 | +2.88 | 24.0 | 0.0 | 25.0 | keep collecting (12/30) |
| pin_value | tt_home | 7-5 | 58.3 | 50.0 | 8.3 | +0.83 | 6.9 | -0.08 | 25.0 | keep collecting (12/30) |
| book_lag | moneyline | 1-1 | 50.0 | 21.4 | 28.6 | +0.08 | 4.0 | 2.15 | 100.0 | keep collecting (2/30) |
| book_lag | spread | 1-2 | 33.3 | 54.8 | -21.4 | -1.13 | -37.7 | -0.17 | 66.7 | keep collecting (3/30) |
| consensus_gap | moneyline | 10-24 | 29.4 | 24.8 | 4.6 | -11.6 | -34.1 | 0.1 | 58.8 | DROP: below break-even |
| consensus_gap | spread | 7-6 | 53.8 | 48.9 | 4.9 | +0.01 | 0.1 | 0.31 | 38.5 | keep collecting (13/30) |
| money_level+sharp_gap | moneyline | 12-3 | 80.0 | 71.0 | 9.0 | +2.34 | 15.6 | -0.53 | 33.3 | keep collecting (15/30) |
| consensus_gap+pre_move | moneyline | 4-9 | 30.8 | 21.4 | 9.3 | -3.24 | -24.9 | -0.2 | 69.2 | redundant -- identical record to pre_move alone, not independent confirmation |
| consensus_gap+sharp_gap | moneyline | 8-13 | 38.1 | 26.9 | 11.2 | -3.5 | -16.7 | 0.39 | 66.7 | keep collecting (21/30) |
| pre_move+sharp_gap | moneyline | 4-9 | 30.8 | 21.4 | 9.3 | -3.24 | -24.9 | -0.2 | 69.2 | redundant -- identical record to pre_move alone, not independent confirmation |
| consensus_gap+follow_move | moneyline | 0-1 | 0.0 | 21.4 | -21.4 | -1.0 | -100.0 | 0.5 | 100.0 | keep collecting (1/30) |
| consensus_gap+rlm | moneyline | 0-1 | 0.0 | 21.4 | -21.4 | -1.0 | -100.0 | 0.5 | 100.0 | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm | moneyline | 0-1 | 0.0 | 21.4 | -21.4 | -1.0 | -100.0 | 0.5 | 100.0 | redundant -- identical record to rlm alone, not independent confirmation |
| money_level+money_moving | moneyline | 4-0 | 100.0 | 78.6 | 21.4 | +2.02 | 50.4 | -0.78 | 50.0 | keep collecting (4/30) |
| follow_move+money_level | moneyline | 1-0 | 100.0 | 78.6 | 21.4 | +0.56 | 56.2 | -3.1 | 0.0 | keep collecting (1/30) |
| follow_move+money_moving | moneyline | 1-0 | 100.0 | 78.6 | 21.4 | +0.56 | 56.2 | -3.1 | 0.0 | keep collecting (1/30) |
| consensus_gap+money_level | moneyline | 3-1 | 75.0 | 50.0 | 25.0 | +0.9 | 22.4 | -2.6 | 50.0 | keep collecting (4/30) |
| consensus_gap+pin_value | moneyline | 0-5 | 0.0 | 21.4 | -21.4 | -5.0 | -100.0 | 1.64 | 80.0 | keep collecting (5/30) |
| consensus_gap+pin_rlm | moneyline | 1-4 | 20.0 | 21.4 | -1.4 | -2.92 | -58.4 | -0.8 | 80.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | moneyline | 0-1 | 0.0 | 21.4 | -21.4 | -1.0 | -100.0 | -10.6 | 0.0 | keep collecting (1/30) |
| money_level+pre_move | moneyline | 0-1 | 0.0 | 21.4 | -21.4 | -1.0 | -100.0 | -10.6 | 0.0 | keep collecting (1/30) |
| pin_rlm+pre_move | moneyline | 1-4 | 20.0 | 21.4 | -1.4 | -2.92 | -58.4 | -0.8 | 80.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | moneyline | 1-4 | 20.0 | 21.4 | -1.4 | -2.92 | -58.4 | -0.8 | 80.0 | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+sharp_gap | moneyline | 2-1 | 66.7 | 40.5 | 26.2 | +0.47 | 15.7 | 1.1 | 66.7 | keep collecting (3/30) |
| pin_value+pre_move | moneyline | 0-3 | 0.0 | 21.4 | -21.4 | -3.0 | -100.0 | 3.03 | 100.0 | keep collecting (3/30) |
| pin_value+sharp_gap | moneyline | 0-3 | 0.0 | 21.4 | -21.4 | -3.0 | -100.0 | 3.03 | 100.0 | keep collecting (3/30) |
| consensus_gap+money_moving | moneyline | 1-1 | 50.0 | 21.4 | 28.6 | +0.08 | 4.0 | 3.45 | 100.0 | keep collecting (2/30) |
| money_moving+pin_value | moneyline | 0-1 | 0.0 | 21.4 | -21.4 | -1.0 | -100.0 | 5.0 | 100.0 | keep collecting (1/30) |
| money_moving+pre_move | moneyline | 1-1 | 50.0 | 21.4 | 28.6 | +0.08 | 4.0 | 3.45 | 100.0 | keep collecting (2/30) |
| pin_rlm+pin_value | moneyline | 0-1 | 0.0 | 21.4 | -21.4 | -1.0 | -100.0 | 1.8 | 100.0 | keep collecting (1/30) |
| book_lag+consensus_gap | moneyline | 1-1 | 50.0 | 21.4 | 28.6 | +0.08 | 4.0 | 2.15 | 100.0 | redundant -- identical record to book_lag alone, not independent confirmation |
| book_lag+money_moving | moneyline | 1-0 | 100.0 | 21.4 | 78.6 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| book_lag+pin_rlm | moneyline | 1-0 | 100.0 | 21.4 | 78.6 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| book_lag+pre_move | moneyline | 1-0 | 100.0 | 21.4 | 78.6 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| book_lag+sharp_gap | moneyline | 1-0 | 100.0 | 21.4 | 78.6 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| money_moving+pin_rlm | moneyline | 1-0 | 100.0 | 21.4 | 78.6 | +1.08 | 108.0 | 1.9 | 100.0 | keep collecting (1/30) |
| follow_move+rlm | spread | 1-5 | 16.7 | 50.0 | -33.3 | -4.17 | -69.5 | 0.0 | 16.7 | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 10-6 | 62.5 | 55.4 | 7.1 | +3.14 | 19.7 | 0.19 | 18.8 | keep collecting (16/30) |
| rlm+rlm_ratio | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | keep collecting (2/30) |
| rlm_ratio+sharp_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.17 | -8.4 | 0.0 | 0.0 | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| consensus_gap+pin_value | spread | 4-2 | 66.7 | 50.0 | 16.7 | +1.34 | 22.4 | 0.5 | 50.0 | keep collecting (6/30) |
| money_level+sharp_gap | spread | 18-8 | 69.2 | 55.5 | 13.7 | +8.52 | 32.8 | -0.06 | 19.2 | keep collecting (26/30) |
| follow_move+pin_value | spread | 4-1 | 80.0 | 58.6 | 21.4 | +2.47 | 49.3 | 0.0 | 0.0 | keep collecting (5/30) |
| pin_value+sharp_gap | spread | 8-0 | 100.0 | 53.6 | 46.4 | +7.04 | 87.9 | 0.06 | 25.0 | keep collecting (8/30) |
| consensus_gap+follow_move | spread | 1-0 | 100.0 | 64.3 | 35.7 | +0.82 | 82.0 | 0.0 | 0.0 | keep collecting (1/30) |
| consensus_gap+money_level | spread | 4-0 | 100.0 | 57.1 | 42.9 | +3.43 | 85.8 | 0.5 | 50.0 | keep collecting (4/30) |
| consensus_gap+sharp_gap | spread | 4-1 | 80.0 | 58.6 | 21.4 | +2.43 | 48.6 | 0.5 | 60.0 | keep collecting (5/30) |
| follow_move+money_level | spread | 8-5 | 61.5 | 59.9 | 1.6 | +2.48 | 19.1 | 0.23 | 23.1 | keep collecting (13/30) |
| money_level+pin_value | spread | 7-1 | 87.5 | 57.1 | 30.4 | +5.2 | 65.0 | 0.06 | 25.0 | keep collecting (8/30) |
| follow_move+money_moving | spread | 2-2 | 50.0 | 57.1 | -7.1 | -0.19 | -4.7 | 0.0 | 0.0 | keep collecting (4/30) |
| money_level+money_moving | spread | 3-2 | 60.0 | 52.9 | 7.1 | +0.8 | 16.0 | -0.6 | 20.0 | keep collecting (5/30) |
| money_moving+pin_value | spread | 4-1 | 80.0 | 52.9 | 27.1 | +2.63 | 52.7 | 0.4 | 40.0 | keep collecting (5/30) |
| money_moving+sharp_gap | spread | 2-2 | 50.0 | 57.1 | -7.1 | -0.15 | -3.8 | -0.25 | 25.0 | keep collecting (4/30) |
| book_lag+consensus_gap | spread | 1-1 | 50.0 | 50.0 | 0.0 | -0.13 | -6.5 | 0.75 | 100.0 | keep collecting (2/30) |
| money_level+pre_move | spread | 1-1 | 50.0 | 35.7 | 14.3 | -0.09 | -4.5 | -1.0 | 0.0 | keep collecting (2/30) |
| pre_move+sharp_gap | spread | 1-2 | 33.3 | 45.2 | -11.9 | -1.09 | -36.4 | -0.5 | 33.3 | redundant -- identical record to pre_move alone, not independent confirmation |
| book_lag+money_level | spread | 1-1 | 50.0 | 64.3 | -14.3 | -0.13 | -6.5 | -0.5 | 50.0 | keep collecting (2/30) |
| book_lag+money_moving | spread | 0-1 | 0.0 | 64.3 | -64.3 | -1.0 | -100.0 | -2.0 | 0.0 | keep collecting (1/30) |
| book_lag+sharp_gap | spread | 1-1 | 50.0 | 64.3 | -14.3 | -0.13 | -6.5 | -0.5 | 50.0 | keep collecting (2/30) |
| money_moving+rlm | spread | 0-1 | 0.0 | 35.7 | -35.7 | -1.0 | -100.0 | 0.0 | 0.0 | keep collecting (1/30) |
| book_lag+pin_value | spread | 1-0 | 100.0 | 64.3 | 35.7 | +0.87 | 87.0 | 1.0 | 100.0 | keep collecting (1/30) |
| consensus_gap+money_moving | spread | 1-0 | 100.0 | 35.7 | 64.3 | +0.87 | 87.0 | 1.0 | 100.0 | keep collecting (1/30) |
| money_level+pin_value | total | 3-2 | 60.0 | 52.9 | 7.1 | +0.71 | 14.1 | -0.4 | 0.0 | keep collecting (5/30) |
| money_level+sharp_gap | total | 15-9 | 62.5 | 52.8 | 9.7 | +4.61 | 19.2 | -0.25 | 25.0 | keep collecting (24/30) |
| pin_value+sharp_gap | total | 4-2 | 66.7 | 51.6 | 15.1 | +1.58 | 26.3 | 0.0 | 16.7 | keep collecting (6/30) |
| money_level+pre_move | total | 1-2 | 33.3 | 48.4 | -15.1 | -1.13 | -37.7 | 1.0 | 33.3 | keep collecting (3/30) |
| pre_move+sharp_gap | total | 2-4 | 33.3 | 46.8 | -13.5 | -2.18 | -36.3 | -0.17 | 16.7 | redundant -- identical record to pre_move alone, not independent confirmation |
| follow_move+money_level | total | 0-1 | 0.0 | 54.8 | -54.8 | -1.0 | -100.0 | -3.0 | 0.0 | redundant -- identical record to follow_move alone, not independent confirmation |
| money_level+money_moving | total | 3-1 | 75.0 | 52.4 | 22.6 | +1.75 | 43.7 | 0.0 | 25.0 | keep collecting (4/30) |
| money_moving+sharp_gap | total | 3-0 | 100.0 | 48.4 | 51.6 | +2.83 | 94.3 | -0.67 | 0.0 | keep collecting (3/30) |
| money_moving+pin_value | total | 1-0 | 100.0 | 45.2 | 54.8 | +0.93 | 92.6 | 0.0 | 0.0 | keep collecting (1/30) |
| money_moving+pre_move | total | 1-0 | 100.0 | 45.2 | 54.8 | +0.95 | 95.2 | -2.0 | 0.0 | keep collecting (1/30) |

## CLOSE  (pooled)

| signal | market | record | hit % | expected % | edge | units | ROI % | CLV avg | CLV + % | status |
|---|---|---|---|---|---|---|---|---|---|---|
| pin_rlm | both | 5-10 | 33.3 | 31.6 | 1.7 | -5.07 | -33.8 |  |  | keep collecting (15/30) |
| pre_move | both | 3-8 | 27.3 | 38.3 | -11.0 | -3.38 | -30.8 |  |  | keep collecting (11/30) |
| follow_move | both | 58-64 | 47.5 | 50.0 | -2.5 | -15.37 | -12.6 |  |  | no edge shown yet |
| rlm | both | 9-32 | 22.0 | 34.6 | -12.6 | -21.77 | -53.1 |  |  | DROP: below break-even |
| rlm_ratio | both | 6-14 | 30.0 | 33.3 | -3.3 | -7.17 | -35.9 |  |  | keep collecting (20/30) |
| money_level | both | 81-42 | 65.9 | 61.5 | 4.4 | +17.13 | 13.9 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| sharp_gap | both | 57-65 | 46.7 | 48.8 | -2.1 | -16.46 | -13.5 |  |  | no edge shown yet |
| money_moving | both | 37-57 | 39.4 | 43.7 | -4.4 | -24.64 | -26.2 |  |  | DROP: below break-even |
| pin_value | both | 58-43 | 57.4 | 49.2 | 8.2 | +6.86 | 6.8 |  |  | no edge shown yet |
| book_lag | both | 5-1 | 83.3 | 64.3 | 19.0 | +2.86 | 47.7 |  |  | keep collecting (6/30) |
| consensus_gap | both | 18-32 | 36.0 | 30.6 | 5.4 | -11.67 | -23.3 |  |  | DROP: below break-even |
| follow_move+rlm | both | 9-32 | 22.0 | 34.6 | -12.6 | -21.77 | -53.1 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | both | 6-14 | 30.0 | 33.3 | -3.3 | -7.17 | -35.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | both | 24-29 | 45.3 | 48.2 | -2.9 | -8.26 | -15.6 |  |  | no edge shown yet |
| money_level+pin_value | both | 15-6 | 71.4 | 57.7 | 13.7 | +6.96 | 33.1 |  |  | keep collecting (21/30) |
| rlm+rlm_ratio | both | 6-14 | 30.0 | 33.3 | -3.3 | -7.17 | -35.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | both | 7-19 | 26.9 | 35.0 | -8.1 | -11.3 | -43.5 |  |  | keep collecting (26/30) |
| rlm_ratio+sharp_gap | both | 6-14 | 30.0 | 33.3 | -3.3 | -7.17 | -35.9 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+sharp_gap | both | 41-26 | 61.2 | 59.2 | 2.0 | +4.77 | 7.1 |  |  | no edge shown yet |
| consensus_gap+money_level | both | 7-1 | 87.5 | 55.4 | 32.1 | +4.86 | 60.7 |  |  | keep collecting (8/30) |
| pre_move+sharp_gap | both | 3-8 | 27.3 | 38.3 | -11.0 | -3.38 | -30.8 |  |  | redundant -- identical record to pre_move alone, not independent confirmation |
| follow_move+money_level | both | 29-15 | 65.9 | 63.6 | 2.3 | +5.64 | 12.8 |  |  | beats break-even but not its base rate -- directional bias, not signal |
| book_lag+money_level | both | 2-1 | 66.7 | 73.8 | -7.1 | +0.4 | 13.4 |  |  | keep collecting (3/30) |
| consensus_gap+pre_move | both | 1-2 | 33.3 | 21.4 | 11.9 | +0.9 | 30.0 |  |  | keep collecting (3/30) |
| consensus_gap+sharp_gap | both | 9-14 | 39.1 | 30.1 | 9.0 | -2.85 | -12.4 |  |  | keep collecting (23/30) |
| follow_move+pin_value | both | 11-7 | 61.1 | 50.5 | 10.6 | +2.36 | 13.1 |  |  | keep collecting (18/30) |
| pin_value+rlm | both | 2-6 | 25.0 | 39.9 | -14.9 | -4.26 | -53.2 |  |  | keep collecting (8/30) |
| pin_value+pre_move | both | 1-1 | 50.0 | 33.3 | 16.7 | -0.15 | -7.7 |  |  | keep collecting (2/30) |
| pin_value+sharp_gap | both | 15-11 | 57.7 | 47.6 | 10.1 | +1.58 | 6.1 |  |  | keep collecting (26/30) |
| consensus_gap+follow_move | both | 6-15 | 28.6 | 28.9 | -0.3 | -7.66 | -36.5 |  |  | keep collecting (21/30) |
| consensus_gap+rlm | both | 4-15 | 21.1 | 23.7 | -2.6 | -9.2 | -48.4 |  |  | keep collecting (19/30) |
| consensus_gap+pin_value | both | 3-6 | 33.3 | 24.6 | 8.7 | -3.42 | -38.0 |  |  | keep collecting (9/30) |
| book_lag+consensus_gap | both | 3-0 | 100.0 | 54.8 | 45.2 | +2.46 | 82.0 |  |  | keep collecting (3/30) |
| book_lag+money_moving | both | 1-0 | 100.0 | 35.7 | 64.3 | +0.78 | 78.1 |  |  | keep collecting (1/30) |
| book_lag+pin_value | both | 2-0 | 100.0 | 50.0 | 50.0 | +1.61 | 80.7 |  |  | keep collecting (2/30) |
| consensus_gap+money_moving | both | 7-15 | 31.8 | 24.7 | 7.1 | -6.73 | -30.6 |  |  | keep collecting (22/30) |
| money_moving+pin_value | both | 10-10 | 50.0 | 44.8 | 5.2 | -1.66 | -8.3 |  |  | keep collecting (20/30) |
| money_moving+pre_move | both | 1-3 | 25.0 | 38.1 | -13.1 | -2.13 | -53.2 |  |  | keep collecting (4/30) |
| money_moving+sharp_gap | both | 26-39 | 40.0 | 43.8 | -3.8 | -15.48 | -23.8 |  |  | DROP: below break-even |
| follow_move+money_moving | both | 15-29 | 34.1 | 44.0 | -10.0 | -14.99 | -34.1 |  |  | DROP: below break-even |
| money_moving+rlm | both | 6-22 | 21.4 | 33.3 | -11.9 | -15.17 | -54.2 |  |  | keep collecting (28/30) |
| money_level+money_moving | both | 24-14 | 63.2 | 57.9 | 5.3 | +5.22 | 13.8 |  |  | no edge shown yet |
| consensus_gap+pin_rlm | both | 2-6 | 25.0 | 21.4 | 3.6 | -3.76 | -47.0 |  |  | keep collecting (8/30) |
| consensus_gap+rlm_ratio | both | 3-6 | 33.3 | 21.4 | 11.9 | -1.86 | -20.7 |  |  | keep collecting (9/30) |
| follow_move+pin_rlm | both | 5-10 | 33.3 | 31.6 | 1.7 | -5.07 | -33.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | both | 0-3 | 0.0 | 40.5 | -40.5 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| money_level+rlm | both | 0-3 | 0.0 | 40.5 | -40.5 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| money_level+rlm_ratio | both | 0-3 | 0.0 | 40.5 | -40.5 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| money_moving+pin_rlm | both | 5-10 | 33.3 | 31.6 | 1.7 | -5.07 | -33.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+rlm_ratio | both | 6-12 | 33.3 | 31.5 | 1.9 | -5.17 | -28.7 |  |  | keep collecting (18/30) |
| pin_rlm+rlm | both | 5-10 | 33.3 | 31.6 | 1.7 | -5.07 | -33.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | both | 5-10 | 33.3 | 31.6 | 1.7 | -5.07 | -33.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | both | 5-10 | 33.3 | 31.6 | 1.7 | -5.07 | -33.8 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+pin_value | both | 1-3 | 25.0 | 33.3 | -8.3 | -2.13 | -53.2 |  |  | keep collecting (4/30) |
| pin_value+rlm_ratio | both | 1-3 | 25.0 | 33.3 | -8.3 | -2.13 | -53.2 |  |  | keep collecting (4/30) |
| money_level+pre_move | both | 1-1 | 50.0 | 35.7 | 14.3 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| pin_rlm | moneyline | 2-7 | 22.2 | 21.4 | 0.8 | -4.76 | -52.9 |  |  | keep collecting (9/30) |
| pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_rlm | total | 3-1 | 75.0 | 45.2 | 29.8 | +1.69 | 42.2 |  |  | keep collecting (4/30) |
| pre_move | moneyline | 1-3 | 25.0 | 35.7 | -10.7 | -0.1 | -2.5 |  |  | keep collecting (4/30) |
| pre_move | spread | 1-3 | 25.0 | 35.7 | -10.7 | -2.13 | -53.2 |  |  | keep collecting (4/30) |
| pre_move | total | 1-2 | 33.3 | 45.2 | -11.9 | -1.15 | -38.4 |  |  | keep collecting (3/30) |
| follow_move | moneyline | 16-18 | 47.1 | 45.0 | 2.1 | -7.24 | -21.3 |  |  | no edge shown yet |
| follow_move | spread | 15-21 | 41.7 | 54.8 | -13.1 | -7.23 | -20.1 |  |  | no edge shown yet |
| follow_move | total | 10-9 | 52.6 | 50.3 | 2.4 | +0.15 | 0.8 |  |  | keep collecting (19/30) |
| follow_move | tt_away | 8-7 | 53.3 | 50.0 | 3.3 | -0.0 | -0.0 |  |  | keep collecting (15/30) |
| follow_move | tt_home | 9-9 | 50.0 | 50.0 | 0.0 | -1.04 | -5.8 |  |  | keep collecting (18/30) |
| rlm | moneyline | 4-16 | 20.0 | 21.4 | -1.4 | -10.2 | -51.0 |  |  | keep collecting (20/30) |
| rlm | spread | 1-11 | 8.3 | 47.6 | -39.3 | -10.13 | -84.4 |  |  | keep collecting (12/30) |
| rlm | total | 4-5 | 44.4 | 46.3 | -1.9 | -1.44 | -16.0 |  |  | keep collecting (9/30) |
| rlm_ratio | moneyline | 3-7 | 30.0 | 21.4 | 8.6 | -2.86 | -28.6 |  |  | keep collecting (10/30) |
| rlm_ratio | spread | 0-6 | 0.0 | 45.2 | -45.2 | -6.0 | -100.0 |  |  | keep collecting (6/30) |
| rlm_ratio | total | 3-1 | 75.0 | 45.2 | 29.8 | +1.69 | 42.2 |  |  | keep collecting (4/30) |
| money_level | moneyline | 34-7 | 82.9 | 74.4 | 8.5 | +9.25 | 22.6 |  |  | PROMOTE: beats break-even and its own base rate |
| money_level | spread | 24-17 | 58.5 | 55.9 | 2.6 | +4.72 | 11.5 |  |  | no edge shown yet |
| money_level | total | 23-18 | 56.1 | 54.1 | 2.0 | +3.16 | 7.7 |  |  | no edge shown yet |
| sharp_gap | moneyline | 21-18 | 53.8 | 50.7 | 3.1 | -1.79 | -4.6 |  |  | no edge shown yet |
| sharp_gap | spread | 16-25 | 39.0 | 44.8 | -5.7 | -10.82 | -26.4 |  |  | DROP: below break-even |
| sharp_gap | total | 20-22 | 47.6 | 50.9 | -3.3 | -3.84 | -9.2 |  |  | no edge shown yet |
| money_moving | moneyline | 13-19 | 40.6 | 37.5 | 3.1 | -8.32 | -26.0 |  |  | no edge shown yet |
| money_moving | spread | 9-21 | 30.0 | 43.3 | -13.3 | -13.0 | -43.3 |  |  | DROP: below break-even |
| money_moving | total | 15-17 | 46.9 | 50.3 | -3.4 | -3.32 | -10.4 |  |  | no edge shown yet |
| pin_value | moneyline | 2-6 | 25.0 | 28.6 | -3.6 | -4.59 | -57.4 |  |  | keep collecting (8/30) |
| pin_value | spread | 15-3 | 83.3 | 54.8 | 28.6 | +10.04 | 55.8 |  |  | keep collecting (18/30) |
| pin_value | total | 11-11 | 50.0 | 50.4 | -0.4 | -1.38 | -6.3 |  |  | keep collecting (22/30) |
| pin_value | tt_away | 14-11 | 56.0 | 50.0 | 6.0 | +1.14 | 4.6 |  |  | keep collecting (25/30) |
| pin_value | tt_home | 16-12 | 57.1 | 50.0 | 7.1 | +1.65 | 5.9 |  |  | keep collecting (28/30) |
| book_lag | moneyline | 1-1 | 50.0 | 78.6 | -28.6 | -0.43 | -21.6 |  |  | keep collecting (2/30) |
| book_lag | spread | 4-0 | 100.0 | 57.1 | 42.9 | +3.29 | 82.4 |  |  | keep collecting (4/30) |
| consensus_gap | moneyline | 13-29 | 31.0 | 26.9 | 4.1 | -12.79 | -30.5 |  |  | DROP: below break-even |
| consensus_gap | spread | 5-3 | 62.5 | 50.0 | 12.5 | +1.13 | 14.1 |  |  | keep collecting (8/30) |
| consensus_gap+money_level | moneyline | 6-1 | 85.7 | 54.1 | 31.6 | +4.02 | 57.5 |  |  | keep collecting (7/30) |
| pre_move+sharp_gap | moneyline | 1-3 | 25.0 | 35.7 | -10.7 | -0.1 | -2.5 |  |  | redundant -- identical record to pre_move alone, not independent confirmation |
| book_lag+money_level | moneyline | 1-1 | 50.0 | 78.6 | -28.6 | -0.43 | -21.6 |  |  | redundant -- identical record to book_lag alone, not independent confirmation |
| consensus_gap+pre_move | moneyline | 1-2 | 33.3 | 21.4 | 11.9 | +0.9 | 30.0 |  |  | keep collecting (3/30) |
| consensus_gap+sharp_gap | moneyline | 8-13 | 38.1 | 29.6 | 8.5 | -2.68 | -12.8 |  |  | keep collecting (21/30) |
| money_level+sharp_gap | moneyline | 17-4 | 81.0 | 73.1 | 7.8 | +5.17 | 24.6 |  |  | keep collecting (21/30) |
| consensus_gap+follow_move | moneyline | 6-14 | 30.0 | 27.1 | 2.9 | -6.66 | -33.3 |  |  | keep collecting (20/30) |
| consensus_gap+rlm | moneyline | 4-14 | 22.2 | 21.4 | 0.8 | -8.2 | -45.6 |  |  | keep collecting (18/30) |
| follow_move+rlm | moneyline | 4-16 | 20.0 | 21.4 | -1.4 | -10.2 | -51.0 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| consensus_gap+pin_value | moneyline | 1-6 | 14.3 | 21.4 | -7.1 | -5.04 | -72.0 |  |  | keep collecting (7/30) |
| pin_value+pre_move | moneyline | 0-1 | 0.0 | 21.4 | -21.4 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| pin_value+sharp_gap | moneyline | 1-4 | 20.0 | 32.9 | -12.9 | -3.56 | -71.1 |  |  | keep collecting (5/30) |
| follow_move+money_level | moneyline | 12-2 | 85.7 | 74.5 | 11.2 | +2.96 | 21.1 |  |  | keep collecting (14/30) |
| follow_move+sharp_gap | moneyline | 9-8 | 52.9 | 45.0 | 8.0 | -0.89 | -5.3 |  |  | keep collecting (17/30) |
| follow_move+money_moving | moneyline | 7-12 | 36.8 | 36.5 | 0.4 | -5.45 | -28.7 |  |  | keep collecting (19/30) |
| money_moving+rlm | moneyline | 3-11 | 21.4 | 21.4 | -0.0 | -6.86 | -49.0 |  |  | keep collecting (14/30) |
| consensus_gap+money_moving | moneyline | 6-15 | 28.6 | 24.1 | 4.4 | -7.51 | -35.8 |  |  | keep collecting (21/30) |
| money_moving+pin_value | moneyline | 2-4 | 33.3 | 31.0 | 2.4 | -2.59 | -43.2 |  |  | keep collecting (6/30) |
| consensus_gap+pin_rlm | moneyline | 2-6 | 25.0 | 21.4 | 3.6 | -3.76 | -47.0 |  |  | keep collecting (8/30) |
| consensus_gap+rlm_ratio | moneyline | 3-6 | 33.3 | 21.4 | 11.9 | -1.86 | -20.7 |  |  | keep collecting (9/30) |
| follow_move+pin_rlm | moneyline | 2-7 | 22.2 | 21.4 | 0.8 | -4.76 | -52.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+rlm_ratio | moneyline | 3-7 | 30.0 | 21.4 | 8.6 | -2.86 | -28.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_level+money_moving | moneyline | 9-2 | 81.8 | 68.2 | 13.6 | +3.57 | 32.5 |  |  | keep collecting (11/30) |
| money_level+pin_rlm | moneyline | 0-1 | 0.0 | 21.4 | -21.4 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_level+rlm | moneyline | 0-1 | 0.0 | 21.4 | -21.4 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_level+rlm_ratio | moneyline | 0-1 | 0.0 | 21.4 | -21.4 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_moving+pin_rlm | moneyline | 2-7 | 22.2 | 21.4 | 0.8 | -4.76 | -52.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+rlm_ratio | moneyline | 3-7 | 30.0 | 21.4 | 8.6 | -2.86 | -28.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| money_moving+sharp_gap | moneyline | 10-12 | 45.5 | 39.6 | 5.8 | -2.97 | -13.5 |  |  | keep collecting (22/30) |
| pin_rlm+rlm | moneyline | 2-7 | 22.2 | 21.4 | 0.8 | -4.76 | -52.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | moneyline | 2-7 | 22.2 | 21.4 | 0.8 | -4.76 | -52.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | moneyline | 2-7 | 22.2 | 21.4 | 0.8 | -4.76 | -52.9 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| rlm+rlm_ratio | moneyline | 3-7 | 30.0 | 21.4 | 8.6 | -2.86 | -28.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | moneyline | 3-7 | 30.0 | 21.4 | 8.6 | -2.86 | -28.6 |  |  | keep collecting (10/30) |
| rlm_ratio+sharp_gap | moneyline | 3-7 | 30.0 | 21.4 | 8.6 | -2.86 | -28.6 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+pin_value | moneyline | 1-3 | 25.0 | 35.7 | -10.7 | -2.56 | -63.9 |  |  | keep collecting (4/30) |
| pin_rlm+pin_value | moneyline | 0-2 | 0.0 | 21.4 | -21.4 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| pin_value+rlm | moneyline | 0-3 | 0.0 | 21.4 | -21.4 | -3.0 | -100.0 |  |  | keep collecting (3/30) |
| pin_value+rlm_ratio | moneyline | 0-2 | 0.0 | 21.4 | -21.4 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_level+pin_value | moneyline | 1-0 | 100.0 | 78.6 | 21.4 | +0.44 | 44.4 |  |  | keep collecting (1/30) |
| follow_move+rlm | spread | 1-11 | 8.3 | 47.6 | -39.3 | -10.13 | -84.4 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | spread | 0-6 | 0.0 | 45.2 | -45.2 | -6.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | spread | 8-14 | 36.4 | 50.0 | -13.6 | -6.74 | -30.6 |  |  | keep collecting (22/30) |
| money_level+pin_value | spread | 8-2 | 80.0 | 58.6 | 21.4 | +5.18 | 51.8 |  |  | keep collecting (10/30) |
| rlm+rlm_ratio | spread | 0-6 | 0.0 | 45.2 | -45.2 | -6.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | spread | 0-9 | 0.0 | 42.1 | -42.1 | -9.0 | -100.0 |  |  | keep collecting (9/30) |
| rlm_ratio+sharp_gap | spread | 0-6 | 0.0 | 45.2 | -45.2 | -6.0 | -100.0 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | spread | 11-10 | 52.4 | 60.2 | -7.8 | +0.09 | 0.4 |  |  | keep collecting (21/30) |
| follow_move+pin_value | spread | 6-1 | 85.7 | 60.2 | 25.5 | +4.28 | 61.2 |  |  | keep collecting (7/30) |
| pin_value+rlm | spread | 1-0 | 100.0 | 64.3 | 35.7 | +0.87 | 87.0 |  |  | keep collecting (1/30) |
| money_level+sharp_gap | spread | 10-10 | 50.0 | 51.4 | -1.4 | -1.14 | -5.7 |  |  | keep collecting (20/30) |
| consensus_gap+sharp_gap | spread | 1-1 | 50.0 | 35.7 | 14.3 | -0.17 | -8.4 |  |  | keep collecting (2/30) |
| book_lag+consensus_gap | spread | 3-0 | 100.0 | 54.8 | 45.2 | +2.46 | 82.0 |  |  | keep collecting (3/30) |
| pin_value+sharp_gap | spread | 7-1 | 87.5 | 50.0 | 37.5 | +5.0 | 62.6 |  |  | keep collecting (8/30) |
| book_lag+money_moving | spread | 1-0 | 100.0 | 35.7 | 64.3 | +0.78 | 78.1 |  |  | keep collecting (1/30) |
| book_lag+pin_value | spread | 2-0 | 100.0 | 50.0 | 50.0 | +1.61 | 80.7 |  |  | keep collecting (2/30) |
| consensus_gap+money_moving | spread | 1-0 | 100.0 | 35.7 | 64.3 | +0.78 | 78.1 |  |  | keep collecting (1/30) |
| consensus_gap+pin_value | spread | 2-0 | 100.0 | 35.7 | 64.3 | +1.61 | 80.7 |  |  | keep collecting (2/30) |
| money_moving+pin_value | spread | 4-0 | 100.0 | 50.0 | 50.0 | +3.43 | 85.8 |  |  | keep collecting (4/30) |
| money_level+money_moving | spread | 6-6 | 50.0 | 52.4 | -2.4 | -0.61 | -5.1 |  |  | keep collecting (12/30) |
| money_moving+sharp_gap | spread | 6-15 | 28.6 | 41.2 | -12.6 | -9.55 | -45.5 |  |  | keep collecting (21/30) |
| money_level+pre_move | spread | 1-1 | 50.0 | 35.7 | 14.3 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| money_moving+pre_move | spread | 1-2 | 33.3 | 35.7 | -2.4 | -1.13 | -37.7 |  |  | keep collecting (3/30) |
| pre_move+sharp_gap | spread | 1-3 | 25.0 | 35.7 | -10.7 | -2.13 | -53.2 |  |  | redundant -- identical record to pre_move alone, not independent confirmation |
| follow_move+money_moving | spread | 2-10 | 16.7 | 50.0 | -33.3 | -8.09 | -67.4 |  |  | keep collecting (12/30) |
| money_moving+rlm | spread | 0-7 | 0.0 | 43.9 | -43.9 | -7.0 | -100.0 |  |  | keep collecting (7/30) |
| follow_move+pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_level+rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_level+rlm_ratio | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | keep collecting (2/30) |
| money_moving+pin_rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+rlm_ratio | spread | 0-4 | 0.0 | 42.9 | -42.9 | -4.0 | -100.0 |  |  | keep collecting (4/30) |
| pin_rlm+rlm | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | spread | 0-2 | 0.0 | 50.0 | -50.0 | -2.0 | -100.0 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| consensus_gap+follow_move | spread | 0-1 | 0.0 | 64.3 | -64.3 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| consensus_gap+rlm | spread | 0-1 | 0.0 | 64.3 | -64.3 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| book_lag+money_level | spread | 1-0 | 100.0 | 64.3 | 35.7 | +0.83 | 83.3 |  |  | keep collecting (1/30) |
| consensus_gap+money_level | spread | 1-0 | 100.0 | 64.3 | 35.7 | +0.83 | 83.3 |  |  | keep collecting (1/30) |
| money_level+sharp_gap | total | 14-12 | 53.8 | 54.0 | -0.2 | +0.75 | 2.9 |  |  | keep collecting (26/30) |
| pin_value+pre_move | total | 1-0 | 100.0 | 45.2 | 54.8 | +0.85 | 84.7 |  |  | keep collecting (1/30) |
| pin_value+sharp_gap | total | 7-6 | 53.8 | 51.8 | 2.0 | +0.13 | 1.0 |  |  | keep collecting (13/30) |
| pre_move+sharp_gap | total | 1-2 | 33.3 | 45.2 | -11.9 | -1.15 | -38.4 |  |  | redundant -- identical record to pre_move alone, not independent confirmation |
| money_level+pin_value | total | 6-4 | 60.0 | 54.8 | 5.2 | +1.33 | 13.3 |  |  | keep collecting (10/30) |
| money_moving+pre_move | total | 0-1 | 0.0 | 45.2 | -45.2 | -1.0 | -100.0 |  |  | keep collecting (1/30) |
| money_moving+sharp_gap | total | 10-12 | 45.5 | 50.4 | -5.0 | -2.96 | -13.5 |  |  | keep collecting (22/30) |
| money_level+money_moving | total | 9-6 | 60.0 | 54.8 | 5.2 | +2.26 | 15.1 |  |  | keep collecting (15/30) |
| money_moving+pin_value | total | 4-6 | 40.0 | 51.0 | -11.0 | -2.5 | -25.0 |  |  | keep collecting (10/30) |
| follow_move+money_moving | total | 6-7 | 46.2 | 49.6 | -3.5 | -1.45 | -11.2 |  |  | keep collecting (13/30) |
| follow_move+pin_rlm | total | 3-1 | 75.0 | 45.2 | 29.8 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| follow_move+pin_value | total | 2-3 | 40.0 | 49.0 | -9.0 | -1.18 | -23.6 |  |  | keep collecting (5/30) |
| follow_move+rlm | total | 4-5 | 44.4 | 46.3 | -1.9 | -1.44 | -16.0 |  |  | redundant -- identical record to rlm alone, not independent confirmation |
| follow_move+rlm_ratio | total | 3-1 | 75.0 | 45.2 | 29.8 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+sharp_gap | total | 7-7 | 50.0 | 49.3 | 0.7 | -0.63 | -4.5 |  |  | keep collecting (14/30) |
| money_moving+pin_rlm | total | 3-1 | 75.0 | 45.2 | 29.8 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| money_moving+rlm | total | 3-4 | 42.9 | 46.6 | -3.7 | -1.31 | -18.7 |  |  | keep collecting (7/30) |
| money_moving+rlm_ratio | total | 3-1 | 75.0 | 45.2 | 29.8 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| pin_rlm+pin_value | total | 1-1 | 50.0 | 45.2 | 4.8 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| pin_rlm+rlm | total | 3-1 | 75.0 | 45.2 | 29.8 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+rlm_ratio | total | 3-1 | 75.0 | 45.2 | 29.8 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_rlm+sharp_gap | total | 3-1 | 75.0 | 45.2 | 29.8 | +1.69 | 42.2 |  |  | redundant -- identical record to pin_rlm alone, not independent confirmation |
| pin_value+rlm | total | 1-3 | 25.0 | 47.6 | -22.6 | -2.13 | -53.2 |  |  | keep collecting (4/30) |
| pin_value+rlm_ratio | total | 1-1 | 50.0 | 45.2 | 4.8 | -0.13 | -6.5 |  |  | keep collecting (2/30) |
| rlm+rlm_ratio | total | 3-1 | 75.0 | 45.2 | 29.8 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| rlm+sharp_gap | total | 4-3 | 57.1 | 45.2 | 11.9 | +0.56 | 8.0 |  |  | keep collecting (7/30) |
| rlm_ratio+sharp_gap | total | 3-1 | 75.0 | 45.2 | 29.8 | +1.69 | 42.2 |  |  | redundant -- identical record to rlm_ratio alone, not independent confirmation |
| follow_move+money_level | total | 6-3 | 66.7 | 54.8 | 11.9 | +2.59 | 28.8 |  |  | keep collecting (9/30) |
| follow_move+pin_value | tt_home | 2-0 | 100.0 | 50.0 | 50.0 | +1.81 | 90.5 |  |  | keep collecting (2/30) |

## By ticket volume and Pinnacle limit (both markets, pooled)

| signal | checkpoint | slice | record | hit % | edge | ROI % | CLV avg |
|---|---|---|---|---|---|---|---|
| pin_rlm | close | 40k+ bets | 5-10 | 33.3 | 1.7 | -33.8 |  |
| pin_rlm | close | pin $10-50k | 3-2 | 60.0 | 19.5 | 13.8 |  |
| pin_rlm | close | pin $50k+ | 2-8 | 20.0 | -7.1 | -57.6 |  |
| pre_move | close | 40k+ bets | 3-8 | 27.3 | -11.0 | -30.8 |  |
| pre_move | close | pin $10-50k | 1-2 | 33.3 | -11.9 | -38.4 |  |
| pre_move | close | pin $50k+ | 2-6 | 25.0 | -10.7 | -27.9 |  |
| follow_move | close | 40k+ bets | 58-64 | 47.5 | -2.5 | -12.6 |  |
| follow_move | close | pin $10-50k | 12-12 | 50.0 | -0.0 | -12.0 |  |
| follow_move | close | pin $50k+ | 29-36 | 44.6 | -5.5 | -17.6 |  |
| follow_move | close | pin limit <$10k | 17-16 | 51.5 | 1.5 | -3.2 |  |
| rlm | close | 40k+ bets | 9-32 | 22.0 | -12.6 | -53.1 |  |
| rlm | close | pin $10-50k | 4-8 | 33.3 | -6.7 | -37.0 |  |
| rlm | close | pin $50k+ | 5-24 | 17.2 | -15.0 | -59.8 |  |
| rlm_ratio | close | 40k+ bets | 6-14 | 30.0 | -3.3 | -35.9 |  |
| rlm_ratio | close | pin $10-50k | 3-2 | 60.0 | 19.5 | 13.8 |  |
| rlm_ratio | close | pin $50k+ | 3-12 | 20.0 | -11.0 | -52.4 |  |
| money_level | close | 40k+ bets | 81-42 | 65.9 | 4.4 | 13.9 |  |
| money_level | close | pin $10-50k | 27-18 | 60.0 | 2.7 | 6.5 |  |
| money_level | close | pin $50k+ | 54-24 | 69.2 | 5.4 | 18.2 |  |
| sharp_gap | close | 40k+ bets | 57-65 | 46.7 | -2.1 | -13.5 |  |
| sharp_gap | close | pin $10-50k | 21-23 | 47.7 | -4.2 | -13.0 |  |
| sharp_gap | close | pin $50k+ | 36-42 | 46.2 | -0.9 | -13.8 |  |
| money_moving | close | 40k+ bets | 37-57 | 39.4 | -4.4 | -26.2 |  |
| money_moving | close | pin $10-50k | 15-20 | 42.9 | -6.3 | -21.1 |  |
| money_moving | close | pin $50k+ | 22-37 | 37.3 | -3.2 | -29.3 |  |
| pin_value | close | 40k+ bets | 58-43 | 57.4 | 8.2 | 6.8 |  |
| pin_value | close | pin $10-50k | 11-13 | 45.8 | -2.2 | -14.1 |  |
| pin_value | close | pin $50k+ | 17-7 | 70.8 | 22.0 | 31.0 |  |
| pin_value | close | pin limit <$10k | 30-23 | 56.6 | 6.6 | 5.3 |  |
| book_lag | close | 40k+ bets | 5-1 | 83.3 | 19.0 | 47.7 |  |
| book_lag | close | pin $50k+ | 5-1 | 83.3 | 19.0 | 47.7 |  |
| consensus_gap | close | 40k+ bets | 18-32 | 36.0 | 5.4 | -23.3 |  |
| consensus_gap | close | pin $10-50k | 1-5 | 16.7 | -14.3 | -78.6 |  |
| consensus_gap | close | pin $50k+ | 17-27 | 38.6 | 8.1 | -15.8 |  |
| follow_move+rlm | close | 40k+ bets | 9-32 | 22.0 | -12.6 | -53.1 |  |
| follow_move+rlm_ratio | close | 40k+ bets | 6-14 | 30.0 | -3.3 | -35.9 |  |
| follow_move+sharp_gap | close | 40k+ bets | 24-29 | 45.3 | -2.9 | -15.6 |  |
| money_level+pin_value | close | 40k+ bets | 15-6 | 71.4 | 13.7 | 33.1 |  |
| rlm+rlm_ratio | close | 40k+ bets | 6-14 | 30.0 | -3.3 | -35.9 |  |
| rlm+sharp_gap | close | 40k+ bets | 7-19 | 26.9 | -8.1 | -43.5 |  |
| rlm_ratio+sharp_gap | close | 40k+ bets | 6-14 | 30.0 | -3.3 | -35.9 |  |
| money_level+sharp_gap | close | 40k+ bets | 41-26 | 61.2 | 2.0 | 7.1 |  |
| consensus_gap+money_level | close | 40k+ bets | 7-1 | 87.5 | 32.1 | 60.7 |  |
| pre_move+sharp_gap | close | 40k+ bets | 3-8 | 27.3 | -11.0 | -30.8 |  |
| follow_move+money_level | close | 40k+ bets | 29-15 | 65.9 | 2.3 | 12.8 |  |
| book_lag+money_level | close | 40k+ bets | 2-1 | 66.7 | -7.1 | 13.4 |  |
| consensus_gap+pre_move | close | 40k+ bets | 1-2 | 33.3 | 11.9 | 30.0 |  |
| consensus_gap+sharp_gap | close | 40k+ bets | 9-14 | 39.1 | 9.0 | -12.4 |  |
| follow_move+pin_value | close | 40k+ bets | 11-7 | 61.1 | 10.6 | 13.1 |  |
| pin_value+rlm | close | 40k+ bets | 2-6 | 25.0 | -14.9 | -53.2 |  |
| pin_value+pre_move | close | 40k+ bets | 1-1 | 50.0 | 16.7 | -7.7 |  |
| pin_value+sharp_gap | close | 40k+ bets | 15-11 | 57.7 | 10.1 | 6.1 |  |
| consensus_gap+follow_move | close | 40k+ bets | 6-15 | 28.6 | -0.3 | -36.5 |  |
| consensus_gap+rlm | close | 40k+ bets | 4-15 | 21.1 | -2.6 | -48.4 |  |
| consensus_gap+pin_value | close | 40k+ bets | 3-6 | 33.3 | 8.7 | -38.0 |  |
| book_lag+consensus_gap | close | 40k+ bets | 3-0 | 100.0 | 45.2 | 82.0 |  |
| book_lag+money_moving | close | 40k+ bets | 1-0 | 100.0 | 64.3 | 78.1 |  |
| book_lag+pin_value | close | 40k+ bets | 2-0 | 100.0 | 50.0 | 80.7 |  |
| consensus_gap+money_moving | close | 40k+ bets | 7-15 | 31.8 | 7.1 | -30.6 |  |
| money_moving+pin_value | close | 40k+ bets | 10-10 | 50.0 | 5.2 | -8.3 |  |
| money_moving+pre_move | close | 40k+ bets | 1-3 | 25.0 | -13.1 | -53.2 |  |
| money_moving+sharp_gap | close | 40k+ bets | 26-39 | 40.0 | -3.8 | -23.8 |  |
| follow_move+money_moving | close | 40k+ bets | 15-29 | 34.1 | -10.0 | -34.1 |  |
| money_moving+rlm | close | 40k+ bets | 6-22 | 21.4 | -11.9 | -54.2 |  |
| money_level+money_moving | close | 40k+ bets | 24-14 | 63.2 | 5.3 | 13.8 |  |
| consensus_gap+pin_rlm | close | 40k+ bets | 2-6 | 25.0 | 3.6 | -47.0 |  |
| consensus_gap+rlm_ratio | close | 40k+ bets | 3-6 | 33.3 | 11.9 | -20.7 |  |
| follow_move+pin_rlm | close | 40k+ bets | 5-10 | 33.3 | 1.7 | -33.8 |  |
| money_level+pin_rlm | close | 40k+ bets | 0-3 | 0.0 | -40.5 | -100.0 |  |
| money_level+rlm | close | 40k+ bets | 0-3 | 0.0 | -40.5 | -100.0 |  |
| money_level+rlm_ratio | close | 40k+ bets | 0-3 | 0.0 | -40.5 | -100.0 |  |
| money_moving+pin_rlm | close | 40k+ bets | 5-10 | 33.3 | 1.7 | -33.8 |  |
| money_moving+rlm_ratio | close | 40k+ bets | 6-12 | 33.3 | 1.9 | -28.7 |  |
| pin_rlm+rlm | close | 40k+ bets | 5-10 | 33.3 | 1.7 | -33.8 |  |
| pin_rlm+rlm_ratio | close | 40k+ bets | 5-10 | 33.3 | 1.7 | -33.8 |  |
| pin_rlm+sharp_gap | close | 40k+ bets | 5-10 | 33.3 | 1.7 | -33.8 |  |
| pin_rlm+pin_value | close | 40k+ bets | 1-3 | 25.0 | -8.3 | -53.2 |  |
| pin_value+rlm_ratio | close | 40k+ bets | 1-3 | 25.0 | -8.3 | -53.2 |  |
| money_level+pre_move | close | 40k+ bets | 1-1 | 50.0 | 14.3 | -6.5 |  |
| money_level+sharp_gap | close | pin $10-50k | 15-12 | 55.6 | -1.1 | -0.5 |  |
| pin_value+pre_move | close | pin $10-50k | 1-0 | 100.0 | 54.8 | 84.7 |  |
| pin_value+sharp_gap | close | pin $10-50k | 7-7 | 50.0 | 0.3 | -6.2 |  |
| pre_move+sharp_gap | close | pin $10-50k | 1-2 | 33.3 | -11.9 | -38.4 |  |
| money_level+pin_value | close | pin $10-50k | 6-4 | 60.0 | 5.2 | 13.3 |  |
| consensus_gap+pin_value | close | pin $10-50k | 0-2 | 0.0 | -21.4 | -100.0 |  |
| follow_move+money_level | close | pin $10-50k | 8-3 | 72.7 | 11.5 | 23.2 |  |
| follow_move+sharp_gap | close | pin $10-50k | 8-8 | 50.0 | -0.9 | -11.8 |  |
| money_moving+pre_move | close | pin $10-50k | 0-1 | 0.0 | -45.2 | -100.0 |  |
| money_moving+sharp_gap | close | pin $10-50k | 9-13 | 40.9 | -9.1 | -23.7 |  |
| consensus_gap+money_level | close | pin $10-50k | 1-0 | 100.0 | 21.4 | 28.6 |  |
| consensus_gap+sharp_gap | close | pin $10-50k | 1-1 | 50.0 | 0.0 | -35.7 |  |
| follow_move+money_moving | close | pin $10-50k | 6-9 | 40.0 | -7.5 | -25.3 |  |
| follow_move+rlm | close | pin $10-50k | 4-8 | 33.3 | -6.7 | -37.0 |  |
| money_moving+rlm | close | pin $10-50k | 3-6 | 33.3 | -7.7 | -36.8 |  |
| money_level+money_moving | close | pin $10-50k | 9-6 | 60.0 | 2.1 | 8.1 |  |
| money_moving+pin_value | close | pin $10-50k | 4-7 | 36.4 | -11.9 | -31.8 |  |
| follow_move+pin_rlm | close | pin $10-50k | 3-2 | 60.0 | 19.5 | 13.8 |  |
| follow_move+pin_value | close | pin $10-50k | 2-4 | 33.3 | -11.1 | -36.3 |  |
| follow_move+rlm_ratio | close | pin $10-50k | 3-2 | 60.0 | 19.5 | 13.8 |  |
| money_moving+pin_rlm | close | pin $10-50k | 3-2 | 60.0 | 19.5 | 13.8 |  |
| money_moving+rlm_ratio | close | pin $10-50k | 3-2 | 60.0 | 19.5 | 13.8 |  |
| pin_rlm+pin_value | close | pin $10-50k | 1-2 | 33.3 | -4.0 | -37.7 |  |
| pin_rlm+rlm | close | pin $10-50k | 3-2 | 60.0 | 19.5 | 13.8 |  |
| pin_rlm+rlm_ratio | close | pin $10-50k | 3-2 | 60.0 | 19.5 | 13.8 |  |
| pin_rlm+sharp_gap | close | pin $10-50k | 3-2 | 60.0 | 19.5 | 13.8 |  |
| pin_value+rlm | close | pin $10-50k | 1-4 | 20.0 | -22.4 | -62.6 |  |
| pin_value+rlm_ratio | close | pin $10-50k | 1-2 | 33.3 | -4.0 | -37.7 |  |
| rlm+rlm_ratio | close | pin $10-50k | 3-2 | 60.0 | 19.5 | 13.8 |  |
| rlm+sharp_gap | close | pin $10-50k | 4-4 | 50.0 | 7.7 | -5.5 |  |
| rlm_ratio+sharp_gap | close | pin $10-50k | 3-2 | 60.0 | 19.5 | 13.8 |  |
| consensus_gap+follow_move | close | pin $10-50k | 0-2 | 0.0 | -21.4 | -100.0 |  |
| consensus_gap+rlm | close | pin $10-50k | 0-2 | 0.0 | -21.4 | -100.0 |  |
| consensus_gap+money_moving | close | pin $10-50k | 0-2 | 0.0 | -21.4 | -100.0 |  |
| consensus_gap+pin_rlm | close | pin $10-50k | 0-1 | 0.0 | -21.4 | -100.0 |  |
| consensus_gap+rlm_ratio | close | pin $10-50k | 0-1 | 0.0 | -21.4 | -100.0 |  |
| follow_move+rlm | close | pin $50k+ | 5-24 | 17.2 | -15.0 | -59.8 |  |
| follow_move+rlm_ratio | close | pin $50k+ | 3-12 | 20.0 | -11.0 | -52.4 |  |
| follow_move+sharp_gap | close | pin $50k+ | 16-21 | 43.2 | -3.8 | -17.2 |  |
| money_level+pin_value | close | pin $50k+ | 9-2 | 81.8 | 21.4 | 51.2 |  |
| rlm+rlm_ratio | close | pin $50k+ | 3-12 | 20.0 | -11.0 | -52.4 |  |
| rlm+sharp_gap | close | pin $50k+ | 3-15 | 16.7 | -15.1 | -60.3 |  |
| rlm_ratio+sharp_gap | close | pin $50k+ | 3-12 | 20.0 | -11.0 | -52.4 |  |
| consensus_gap+money_level | close | pin $50k+ | 6-1 | 85.7 | 33.7 | 65.3 |  |
| pre_move+sharp_gap | close | pin $50k+ | 2-6 | 25.0 | -10.7 | -27.9 |  |
| follow_move+money_level | close | pin $50k+ | 21-12 | 63.6 | -0.8 | 9.3 |  |
| book_lag+money_level | close | pin $50k+ | 2-1 | 66.7 | -7.1 | 13.4 |  |
| consensus_gap+pre_move | close | pin $50k+ | 1-2 | 33.3 | 11.9 | 30.0 |  |
| consensus_gap+sharp_gap | close | pin $50k+ | 8-13 | 38.1 | 9.9 | -10.1 |  |
| follow_move+pin_value | close | pin $50k+ | 7-3 | 70.0 | 15.7 | 27.3 |  |
| pin_value+rlm | close | pin $50k+ | 1-2 | 33.3 | -2.4 | -37.7 |  |
| money_level+sharp_gap | close | pin $50k+ | 26-14 | 65.0 | 4.0 | 12.3 |  |
| consensus_gap+follow_move | close | pin $50k+ | 6-13 | 31.6 | 1.9 | -29.8 |  |
| consensus_gap+rlm | close | pin $50k+ | 4-13 | 23.5 | -0.4 | -42.4 |  |
| consensus_gap+pin_value | close | pin $50k+ | 3-4 | 42.9 | 17.3 | -20.3 |  |
| pin_value+pre_move | close | pin $50k+ | 0-1 | 0.0 | -21.4 | -100.0 |  |
| pin_value+sharp_gap | close | pin $50k+ | 8-4 | 66.7 | 21.4 | 20.4 |  |
| book_lag+consensus_gap | close | pin $50k+ | 3-0 | 100.0 | 45.2 | 82.0 |  |
| book_lag+money_moving | close | pin $50k+ | 1-0 | 100.0 | 64.3 | 78.1 |  |
| book_lag+pin_value | close | pin $50k+ | 2-0 | 100.0 | 50.0 | 80.7 |  |
| consensus_gap+money_moving | close | pin $50k+ | 7-13 | 35.0 | 10.0 | -23.7 |  |
| money_moving+pin_value | close | pin $50k+ | 6-3 | 66.7 | 26.2 | 20.4 |  |
| consensus_gap+pin_rlm | close | pin $50k+ | 2-5 | 28.6 | 7.1 | -39.4 |  |
| consensus_gap+rlm_ratio | close | pin $50k+ | 3-5 | 37.5 | 16.1 | -10.7 |  |
| follow_move+money_moving | close | pin $50k+ | 9-20 | 31.0 | -11.2 | -38.6 |  |
| follow_move+pin_rlm | close | pin $50k+ | 2-8 | 20.0 | -7.1 | -57.6 |  |
| money_level+money_moving | close | pin $50k+ | 15-8 | 65.2 | 7.3 | 17.5 |  |
| money_level+pin_rlm | close | pin $50k+ | 0-3 | 0.0 | -40.5 | -100.0 |  |
| money_level+rlm | close | pin $50k+ | 0-3 | 0.0 | -40.5 | -100.0 |  |
| money_level+rlm_ratio | close | pin $50k+ | 0-3 | 0.0 | -40.5 | -100.0 |  |
| money_moving+pin_rlm | close | pin $50k+ | 2-8 | 20.0 | -7.1 | -57.6 |  |
| money_moving+rlm | close | pin $50k+ | 3-16 | 15.8 | -13.9 | -62.4 |  |
| money_moving+rlm_ratio | close | pin $50k+ | 3-10 | 23.1 | -4.9 | -45.1 |  |
| money_moving+sharp_gap | close | pin $50k+ | 17-26 | 39.5 | -1.1 | -23.9 |  |
| pin_rlm+rlm | close | pin $50k+ | 2-8 | 20.0 | -7.1 | -57.6 |  |
| pin_rlm+rlm_ratio | close | pin $50k+ | 2-8 | 20.0 | -7.1 | -57.6 |  |
| pin_rlm+sharp_gap | close | pin $50k+ | 2-8 | 20.0 | -7.1 | -57.6 |  |
| pin_rlm+pin_value | close | pin $50k+ | 0-1 | 0.0 | -21.4 | -100.0 |  |
| pin_value+rlm_ratio | close | pin $50k+ | 0-1 | 0.0 | -21.4 | -100.0 |  |
| money_level+pre_move | close | pin $50k+ | 1-1 | 50.0 | 14.3 | -6.5 |  |
| money_moving+pre_move | close | pin $50k+ | 1-2 | 33.3 | -2.4 | -37.7 |  |
| follow_move+pin_value | close | pin limit <$10k | 2-0 | 100.0 | 50.0 | 90.5 |  |
| pin_rlm | early | <10k bets | 1-4 | 20.0 | -1.4 | -58.4 | -0.8 |
| pin_rlm | early | pin $10-50k | 1-0 | 100.0 | 78.6 | 108.0 | 1.9 |
| pin_rlm | early | pin limit <$10k | 0-4 | 0.0 | -21.4 | -100.0 | -1.47 |
| pre_move | early | 10-40k bets | 1-1 | 50.0 | 28.6 | 23.0 | 0.55 |
| pre_move | early | 40k+ bets | 0-1 | 0.0 | -45.2 | -100.0 | 0.0 |
| pre_move | early | <10k bets | 6-13 | 31.6 | -0.4 | -31.4 | -0.33 |
| pre_move | early | pin $10-50k | 2-3 | 40.0 | 2.4 | -9.2 | 0.28 |
| pre_move | early | pin $50k+ | 0-1 | 0.0 | -21.4 | -100.0 | 2.1 |
| pre_move | early | pin limit <$10k | 4-11 | 26.7 | -2.7 | -40.0 | -0.44 |
| follow_move | early | 10-40k bets | 1-0 | 100.0 | 35.7 | 82.0 | 0.0 |
| follow_move | early | 40k+ bets | 1-1 | 50.0 | 14.3 | -8.4 | 0.0 |
| follow_move | early | <10k bets | 10-12 | 45.5 | -10.6 | -14.2 | -0.12 |
| follow_move | early | pin $10-50k | 6-3 | 66.7 | 11.9 | 26.9 | 0.33 |
| follow_move | early | pin $50k+ | 2-1 | 66.7 | 21.4 | 21.8 | 0.0 |
| follow_move | early | pin limit <$10k | 4-7 | 36.4 | -21.9 | -32.1 | -0.33 |
| rlm | early | 40k+ bets | 0-1 | 0.0 | -35.7 | -100.0 | 0.0 |
| rlm | early | <10k bets | 1-5 | 16.7 | -31.0 | -69.5 | 0.08 |
| rlm | early | pin $10-50k | 1-1 | 50.0 | 0.0 | -8.4 | 0.5 |
| rlm | early | pin $50k+ | 0-1 | 0.0 | -35.7 | -100.0 | 0.0 |
| rlm | early | pin limit <$10k | 0-3 | 0.0 | -50.0 | -100.0 | -0.17 |
| rlm_ratio | early | 40k+ bets | 0-1 | 0.0 | -35.7 | -100.0 | 0.0 |
| rlm_ratio | early | <10k bets | 1-0 | 100.0 | 35.7 | 83.3 | 0.0 |
| rlm_ratio | early | pin $10-50k | 1-0 | 100.0 | 35.7 | 83.3 | 0.0 |
| rlm_ratio | early | pin $50k+ | 0-1 | 0.0 | -35.7 | -100.0 | 0.0 |
| money_level | early | 10-40k bets | 3-3 | 50.0 | -9.5 | -13.8 | -0.28 |
| money_level | early | 40k+ bets | 4-4 | 50.0 | -14.9 | -19.9 | -0.06 |
| money_level | early | <10k bets | 61-25 | 70.9 | 10.9 | 23.1 | -0.41 |
| money_level | early | pin $10-50k | 12-11 | 52.2 | -2.0 | -2.3 | -0.23 |
| money_level | early | pin $50k+ | 5-2 | 71.4 | 5.1 | 20.1 | -0.36 |
| money_level | early | pin limit <$10k | 49-15 | 76.6 | 15.0 | 30.3 | -0.33 |
| sharp_gap | early | 10-40k bets | 3-3 | 50.0 | 3.2 | 3.1 | 0.27 |
| sharp_gap | early | 40k+ bets | 4-5 | 44.4 | -14.0 | -29.5 | -0.06 |
| sharp_gap | early | <10k bets | 51-32 | 61.4 | 11.9 | 15.2 | 0.05 |
| sharp_gap | early | pin $10-50k | 13-10 | 56.5 | 3.6 | 8.3 | 0.06 |
| sharp_gap | early | pin $50k+ | 3-5 | 37.5 | -17.9 | -37.5 | 0.33 |
| sharp_gap | early | pin limit <$10k | 38-23 | 62.3 | 14.2 | 15.2 | -0.09 |
| money_moving | early | <10k bets | 15-9 | 62.5 | 10.3 | 14.1 | -0.03 |
| money_moving | early | pin $10-50k | 5-2 | 71.4 | 21.4 | 40.0 | -0.16 |
| money_moving | early | pin limit <$10k | 9-6 | 60.0 | 5.2 | 4.2 | 0.16 |
| pin_value | early | 10-40k bets | 1-2 | 33.3 | -21.4 | -39.3 | 0.0 |
| pin_value | early | 40k+ bets | 4-2 | 66.7 | 20.6 | 22.5 | 0.0 |
| pin_value | early | <10k bets | 27-21 | 56.2 | 8.3 | 5.3 | 0.2 |
| pin_value | early | pin $10-50k | 6-3 | 66.7 | 6.6 | 27.8 | -0.28 |
| pin_value | early | pin $50k+ | 3-0 | 100.0 | 54.8 | 81.1 | 0.0 |
| pin_value | early | pin limit <$10k | 23-22 | 51.1 | 5.2 | -5.0 | 0.27 |
| book_lag | early | <10k bets | 2-3 | 40.0 | -1.4 | -21.0 | 0.76 |
| book_lag | early | pin $10-50k | 1-2 | 33.3 | -7.1 | -30.7 | 0.13 |
| book_lag | early | pin limit <$10k | 1-1 | 50.0 | 7.1 | -6.5 | 1.7 |
| consensus_gap | early | 10-40k bets | 2-2 | 50.0 | 7.1 | 7.0 | 0.4 |
| consensus_gap | early | 40k+ bets | 2-2 | 50.0 | 25.0 | -6.4 | 0.17 |
| consensus_gap | early | <10k bets | 13-26 | 33.3 | 2.4 | -29.8 | 0.13 |
| consensus_gap | early | pin $10-50k | 4-5 | 44.4 | 4.0 | -7.6 | 0.23 |
| consensus_gap | early | pin $50k+ | 3-3 | 50.0 | 11.9 | -7.3 | 0.43 |
| consensus_gap | early | pin limit <$10k | 9-21 | 30.0 | 1.9 | -37.7 | -0.19 |
| consensus_gap+follow_move | early | 10-40k bets | 1-0 | 100.0 | 35.7 | 82.0 | 0.0 |
| consensus_gap+money_level | early | 10-40k bets | 1-0 | 100.0 | 35.7 | 82.0 | 0.0 |
| consensus_gap+pin_value | early | 10-40k bets | 1-0 | 100.0 | 35.7 | 82.0 | 0.0 |
| consensus_gap+sharp_gap | early | 10-40k bets | 2-2 | 50.0 | 7.1 | 7.0 | 0.4 |
| follow_move+money_level | early | 10-40k bets | 1-0 | 100.0 | 35.7 | 82.0 | 0.0 |
| follow_move+pin_value | early | 10-40k bets | 1-0 | 100.0 | 35.7 | 82.0 | 0.0 |
| follow_move+sharp_gap | early | 10-40k bets | 1-0 | 100.0 | 35.7 | 82.0 | 0.0 |
| money_level+pin_value | early | 10-40k bets | 1-0 | 100.0 | 35.7 | 82.0 | 0.0 |
| money_level+sharp_gap | early | 10-40k bets | 1-1 | 50.0 | -9.5 | -9.0 | 0.0 |
| pin_value+sharp_gap | early | 10-40k bets | 1-0 | 100.0 | 35.7 | 82.0 | 0.0 |
| consensus_gap+pre_move | early | 10-40k bets | 1-1 | 50.0 | 28.6 | 23.0 | 0.55 |
| pre_move+sharp_gap | early | 10-40k bets | 1-1 | 50.0 | 28.6 | 23.0 | 0.55 |
| follow_move+rlm | early | 40k+ bets | 0-1 | 0.0 | -35.7 | -100.0 | 0.0 |
| follow_move+rlm_ratio | early | 40k+ bets | 0-1 | 0.0 | -35.7 | -100.0 | 0.0 |
| follow_move+sharp_gap | early | 40k+ bets | 1-1 | 50.0 | 14.3 | -8.4 | 0.0 |
| rlm+rlm_ratio | early | 40k+ bets | 0-1 | 0.0 | -35.7 | -100.0 | 0.0 |
| rlm+sharp_gap | early | 40k+ bets | 0-1 | 0.0 | -35.7 | -100.0 | 0.0 |
| rlm_ratio+sharp_gap | early | 40k+ bets | 0-1 | 0.0 | -35.7 | -100.0 | 0.0 |
| money_level+pin_value | early | 40k+ bets | 0-1 | 0.0 | -54.8 | -100.0 | 0.0 |
| money_level+sharp_gap | early | 40k+ bets | 3-4 | 42.9 | -22.1 | -35.5 | -0.07 |
| pin_value+sharp_gap | early | 40k+ bets | 1-1 | 50.0 | 4.8 | -8.4 | 0.0 |
| consensus_gap+pin_value | early | 40k+ bets | 1-0 | 100.0 | 64.3 | 78.1 | 0.0 |
| money_level+pre_move | early | 40k+ bets | 0-1 | 0.0 | -45.2 | -100.0 | 0.0 |
| pre_move+sharp_gap | early | 40k+ bets | 0-1 | 0.0 | -45.2 | -100.0 | 0.0 |
| follow_move+pin_value | early | 40k+ bets | 1-0 | 100.0 | 64.3 | 83.3 | 0.0 |
| follow_move+money_level | early | <10k bets | 8-6 | 57.1 | -3.4 | 8.7 | -0.22 |
| follow_move+money_moving | early | <10k bets | 3-2 | 60.0 | -1.4 | 7.5 | -0.62 |
| follow_move+pin_value | early | <10k bets | 2-1 | 66.7 | 2.4 | 27.1 | 0.0 |
| follow_move+sharp_gap | early | <10k bets | 8-5 | 61.5 | 3.8 | 19.2 | 0.23 |
| money_level+money_moving | early | <10k bets | 10-3 | 76.9 | 16.3 | 35.1 | -0.47 |
| money_level+pin_value | early | <10k bets | 9-2 | 81.8 | 27.1 | 55.3 | -0.14 |
| money_level+sharp_gap | early | <10k bets | 41-15 | 73.2 | 16.1 | 32.4 | -0.27 |
| money_moving+pin_value | early | <10k bets | 5-2 | 71.4 | 24.1 | 36.6 | 1.0 |
| money_moving+sharp_gap | early | <10k bets | 7-3 | 70.0 | 20.5 | 31.5 | 0.03 |
| pin_value+sharp_gap | early | <10k bets | 10-4 | 71.4 | 25.2 | 35.4 | 0.69 |
| consensus_gap+follow_move | early | <10k bets | 0-1 | 0.0 | -21.4 | -100.0 | 0.5 |
| consensus_gap+rlm | early | <10k bets | 0-1 | 0.0 | -21.4 | -100.0 | 0.5 |
| follow_move+rlm | early | <10k bets | 1-5 | 16.7 | -31.0 | -69.5 | 0.08 |
| consensus_gap+sharp_gap | early | <10k bets | 10-12 | 45.5 | 14.3 | -6.1 | 0.41 |
| consensus_gap+money_level | early | <10k bets | 6-1 | 85.7 | 33.7 | 50.1 | -1.2 |
| book_lag+consensus_gap | early | <10k bets | 2-2 | 50.0 | 14.3 | -1.2 | 1.45 |
| money_level+pre_move | early | <10k bets | 2-3 | 40.0 | 1.4 | -24.4 | -1.92 |
| pre_move+sharp_gap | early | <10k bets | 6-13 | 31.6 | -0.4 | -31.4 | -0.33 |
| consensus_gap+pin_value | early | <10k bets | 2-7 | 22.2 | -11.9 | -58.4 | 1.24 |
| consensus_gap+pin_rlm | early | <10k bets | 1-4 | 20.0 | -1.4 | -58.4 | -0.8 |
| consensus_gap+pre_move | early | <10k bets | 3-8 | 27.3 | 5.8 | -33.6 | -0.34 |
| money_level+pin_rlm | early | <10k bets | 0-1 | 0.0 | -21.4 | -100.0 | -10.6 |
| pin_rlm+pre_move | early | <10k bets | 1-4 | 20.0 | -1.4 | -58.4 | -0.8 |
| pin_rlm+sharp_gap | early | <10k bets | 1-4 | 20.0 | -1.4 | -58.4 | -0.8 |
| book_lag+money_level | early | <10k bets | 1-1 | 50.0 | -14.3 | -6.5 | -0.5 |
| book_lag+money_moving | early | <10k bets | 1-1 | 50.0 | 7.1 | 4.0 | -0.05 |
| book_lag+sharp_gap | early | <10k bets | 2-1 | 66.7 | 16.7 | 31.7 | 0.3 |
| pin_value+pre_move | early | <10k bets | 0-3 | 0.0 | -21.4 | -100.0 | 3.03 |
| consensus_gap+money_moving | early | <10k bets | 2-1 | 66.7 | 40.5 | 31.7 | 2.63 |
| money_moving+pre_move | early | <10k bets | 2-1 | 66.7 | 37.3 | 34.4 | 1.63 |
| pin_rlm+pin_value | early | <10k bets | 0-1 | 0.0 | -21.4 | -100.0 | 1.8 |
| book_lag+pin_rlm | early | <10k bets | 1-0 | 100.0 | 78.6 | 108.0 | 1.9 |
| book_lag+pre_move | early | <10k bets | 1-0 | 100.0 | 78.6 | 108.0 | 1.9 |
| money_moving+pin_rlm | early | <10k bets | 1-0 | 100.0 | 78.6 | 108.0 | 1.9 |
| follow_move+rlm_ratio | early | <10k bets | 1-0 | 100.0 | 35.7 | 83.3 | 0.0 |
| rlm+rlm_ratio | early | <10k bets | 1-0 | 100.0 | 35.7 | 83.3 | 0.0 |
| rlm+sharp_gap | early | <10k bets | 1-0 | 100.0 | 35.7 | 83.3 | 0.0 |
| rlm_ratio+sharp_gap | early | <10k bets | 1-0 | 100.0 | 35.7 | 83.3 | 0.0 |
| money_moving+rlm | early | <10k bets | 0-1 | 0.0 | -35.7 | -100.0 | 0.0 |
| book_lag+pin_value | early | <10k bets | 1-0 | 100.0 | 35.7 | 87.0 | 1.0 |
| money_level+pin_value | early | pin $10-50k | 3-1 | 75.0 | 13.1 | 45.2 | -0.38 |
| money_level+sharp_gap | early | pin $10-50k | 10-8 | 55.6 | 1.1 | 3.0 | -0.11 |
| pin_value+sharp_gap | early | pin $10-50k | 3-1 | 75.0 | 13.1 | 45.2 | -0.38 |
| money_level+pre_move | early | pin $10-50k | 0-2 | 0.0 | -40.5 | -100.0 | 0.0 |
| pre_move+sharp_gap | early | pin $10-50k | 2-3 | 40.0 | 2.4 | -9.2 | 0.28 |
| consensus_gap+pre_move | early | pin $10-50k | 2-0 | 100.0 | 78.6 | 127.0 | 0.45 |
| consensus_gap+sharp_gap | early | pin $10-50k | 3-0 | 100.0 | 64.3 | 113.7 | 0.3 |
| follow_move+money_level | early | pin $10-50k | 4-2 | 66.7 | 11.9 | 29.2 | 0.33 |
| follow_move+money_moving | early | pin $10-50k | 2-0 | 100.0 | 35.7 | 90.6 | 0.0 |
| follow_move+pin_value | early | pin $10-50k | 2-0 | 100.0 | 35.7 | 90.6 | 0.0 |
| follow_move+sharp_gap | early | pin $10-50k | 5-2 | 71.4 | 15.3 | 37.0 | 0.29 |
| money_level+money_moving | early | pin $10-50k | 2-1 | 66.7 | 11.9 | 31.1 | -1.33 |
| money_moving+pin_value | early | pin $10-50k | 3-1 | 75.0 | 17.9 | 44.1 | 0.25 |
| money_moving+sharp_gap | early | pin $10-50k | 2-1 | 66.7 | 16.7 | 35.3 | -0.03 |
| book_lag+consensus_gap | early | pin $10-50k | 1-1 | 50.0 | 21.4 | 4.0 | 1.2 |
| follow_move+rlm | early | pin $10-50k | 1-1 | 50.0 | 0.0 | -8.4 | 0.5 |
| book_lag+money_level | early | pin $10-50k | 0-1 | 0.0 | -64.3 | -100.0 | -2.0 |
| book_lag+money_moving | early | pin $10-50k | 1-1 | 50.0 | 7.1 | 4.0 | -0.05 |
| book_lag+sharp_gap | early | pin $10-50k | 1-1 | 50.0 | 7.1 | 4.0 | -0.05 |
| consensus_gap+money_level | early | pin $10-50k | 1-0 | 100.0 | 35.7 | 87.0 | 0.0 |
| consensus_gap+pin_value | early | pin $10-50k | 0-1 | 0.0 | -64.3 | -100.0 | 0.0 |
| book_lag+pin_rlm | early | pin $10-50k | 1-0 | 100.0 | 78.6 | 108.0 | 1.9 |
| book_lag+pre_move | early | pin $10-50k | 1-0 | 100.0 | 78.6 | 108.0 | 1.9 |
| consensus_gap+money_moving | early | pin $10-50k | 1-0 | 100.0 | 78.6 | 108.0 | 1.9 |
| consensus_gap+pin_rlm | early | pin $10-50k | 1-0 | 100.0 | 78.6 | 108.0 | 1.9 |
| money_moving+pin_rlm | early | pin $10-50k | 1-0 | 100.0 | 78.6 | 108.0 | 1.9 |
| money_moving+pre_move | early | pin $10-50k | 1-0 | 100.0 | 78.6 | 108.0 | 1.9 |
| pin_rlm+pre_move | early | pin $10-50k | 1-0 | 100.0 | 78.6 | 108.0 | 1.9 |
| pin_rlm+sharp_gap | early | pin $10-50k | 1-0 | 100.0 | 78.6 | 108.0 | 1.9 |
| follow_move+rlm_ratio | early | pin $10-50k | 1-0 | 100.0 | 35.7 | 83.3 | 0.0 |
| rlm+rlm_ratio | early | pin $10-50k | 1-0 | 100.0 | 35.7 | 83.3 | 0.0 |
| rlm+sharp_gap | early | pin $10-50k | 1-0 | 100.0 | 35.7 | 83.3 | 0.0 |
| rlm_ratio+sharp_gap | early | pin $10-50k | 1-0 | 100.0 | 35.7 | 83.3 | 0.0 |
| follow_move+rlm | early | pin $50k+ | 0-1 | 0.0 | -35.7 | -100.0 | 0.0 |
| follow_move+rlm_ratio | early | pin $50k+ | 0-1 | 0.0 | -35.7 | -100.0 | 0.0 |
| follow_move+sharp_gap | early | pin $50k+ | 2-1 | 66.7 | 21.4 | 21.8 | 0.0 |
| rlm+rlm_ratio | early | pin $50k+ | 0-1 | 0.0 | -35.7 | -100.0 | 0.0 |
| rlm+sharp_gap | early | pin $50k+ | 0-1 | 0.0 | -35.7 | -100.0 | 0.0 |
| rlm_ratio+sharp_gap | early | pin $50k+ | 0-1 | 0.0 | -35.7 | -100.0 | 0.0 |
| money_level+sharp_gap | early | pin $50k+ | 2-2 | 50.0 | -21.4 | -20.9 | 0.0 |
| consensus_gap+pin_value | early | pin $50k+ | 2-0 | 100.0 | 50.0 | 80.0 | 0.0 |
| follow_move+pin_value | early | pin $50k+ | 2-0 | 100.0 | 50.0 | 82.7 | 0.0 |
| pin_value+sharp_gap | early | pin $50k+ | 2-0 | 100.0 | 50.0 | 82.7 | 0.0 |
| consensus_gap+follow_move | early | pin $50k+ | 1-0 | 100.0 | 35.7 | 82.0 | 0.0 |
| consensus_gap+money_level | early | pin $50k+ | 1-0 | 100.0 | 35.7 | 82.0 | 0.0 |
| consensus_gap+sharp_gap | early | pin $50k+ | 1-2 | 33.3 | -16.7 | -39.3 | 0.87 |
| follow_move+money_level | early | pin $50k+ | 1-0 | 100.0 | 35.7 | 82.0 | 0.0 |
| money_level+pin_value | early | pin $50k+ | 1-0 | 100.0 | 35.7 | 82.0 | 0.0 |
| consensus_gap+pre_move | early | pin $50k+ | 0-1 | 0.0 | -21.4 | -100.0 | 2.1 |
| pre_move+sharp_gap | early | pin $50k+ | 0-1 | 0.0 | -21.4 | -100.0 | 2.1 |
| money_level+pin_value | early | pin limit <$10k | 6-2 | 75.0 | 23.8 | 41.0 | 0.0 |
| money_level+sharp_gap | early | pin limit <$10k | 31-8 | 79.5 | 21.9 | 42.5 | -0.32 |
| pin_value+sharp_gap | early | pin limit <$10k | 7-4 | 63.6 | 22.3 | 19.5 | 1.01 |
| consensus_gap+follow_move | early | pin limit <$10k | 0-1 | 0.0 | -21.4 | -100.0 | 0.5 |
| consensus_gap+rlm | early | pin limit <$10k | 0-1 | 0.0 | -21.4 | -100.0 | 0.5 |
| follow_move+rlm | early | pin limit <$10k | 0-3 | 0.0 | -50.0 | -100.0 | -0.17 |
| consensus_gap+sharp_gap | early | pin limit <$10k | 7-12 | 36.8 | 6.4 | -27.1 | -0.12 |
| money_level+money_moving | early | pin limit <$10k | 8-2 | 80.0 | 17.6 | 36.3 | -0.21 |
| follow_move+money_level | early | pin limit <$10k | 4-3 | 57.1 | -7.8 | 6.7 | -0.44 |
| follow_move+money_moving | early | pin limit <$10k | 1-1 | 50.0 | -21.4 | -21.9 | -1.55 |
| consensus_gap+money_level | early | pin limit <$10k | 5-1 | 83.3 | 33.3 | 43.9 | -1.4 |
| money_level+pre_move | early | pin limit <$10k | 2-2 | 50.0 | 10.7 | -5.5 | -2.4 |
| pre_move+sharp_gap | early | pin limit <$10k | 4-11 | 26.7 | -2.7 | -40.0 | -0.44 |
| consensus_gap+pin_value | early | pin limit <$10k | 2-6 | 25.0 | -5.4 | -53.2 | 1.4 |
| money_moving+sharp_gap | early | pin limit <$10k | 4-2 | 66.7 | 16.7 | 19.0 | 0.4 |
| consensus_gap+pin_rlm | early | pin limit <$10k | 0-4 | 0.0 | -21.4 | -100.0 | -1.47 |
| consensus_gap+pre_move | early | pin limit <$10k | 2-8 | 20.0 | -1.4 | -47.8 | -0.56 |
| money_level+pin_rlm | early | pin limit <$10k | 0-1 | 0.0 | -21.4 | -100.0 | -10.6 |
| pin_rlm+pre_move | early | pin limit <$10k | 0-4 | 0.0 | -21.4 | -100.0 | -1.47 |
| pin_rlm+sharp_gap | early | pin limit <$10k | 0-4 | 0.0 | -21.4 | -100.0 | -1.47 |
| money_moving+pin_value | early | pin limit <$10k | 2-1 | 66.7 | 32.5 | 26.5 | 2.0 |
| pin_value+pre_move | early | pin limit <$10k | 0-3 | 0.0 | -21.4 | -100.0 | 3.03 |
| consensus_gap+money_moving | early | pin limit <$10k | 1-1 | 50.0 | 21.4 | -6.5 | 3.0 |
| money_moving+pre_move | early | pin limit <$10k | 0-1 | 0.0 | -21.4 | -100.0 | 5.0 |
| follow_move+sharp_gap | early | pin limit <$10k | 3-2 | 60.0 | 1.4 | 18.1 | 0.6 |
| pin_rlm+pin_value | early | pin limit <$10k | 0-1 | 0.0 | -21.4 | -100.0 | 1.8 |
| book_lag+consensus_gap | early | pin limit <$10k | 1-1 | 50.0 | 7.1 | -6.5 | 1.7 |
| follow_move+pin_value | early | pin limit <$10k | 0-1 | 0.0 | -64.3 | -100.0 | 0.0 |
| book_lag+money_level | early | pin limit <$10k | 1-0 | 100.0 | 35.7 | 87.0 | 1.0 |
| book_lag+pin_value | early | pin limit <$10k | 1-0 | 100.0 | 35.7 | 87.0 | 1.0 |
| book_lag+sharp_gap | early | pin limit <$10k | 1-0 | 100.0 | 35.7 | 87.0 | 1.0 |
