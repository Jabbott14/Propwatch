# Propwatch — read before doing anything in this repo

This file loads automatically. The rest of the knowledge base does not, which is why
this file exists.

## Step 0, every session, before answering anything substantive

Search the attached claude.ai project before investigating anything. Not after. The docs
are in the project, not on disk — use `project_search` / `project_read`, not grep.

Open `claude/AAA-propwatch-brain-read-first.md` first. It is the index to 31 other docs
and it says what is already known.

**Why this is a rule and not a suggestion:** an hour was spent on 2026-11-22
investigating whether Pinnacle moving before FanDuel predicts anything. The answer was
already in `propwatch-line-value-state.md` rule 22, tested, **0-for-17**. The knowledge
existed and was unfindable. That is worse than not knowing — the time is spent and the
conclusion arrives with false novelty.

Also search `propwatch-line-value-state.md` specifically before any line / money /
Pinnacle question. It is a parallel knowledge base with its own numbered rules and it
does not show up in casual search.

## The five rules that caught every false finding

Five false findings were caught in one session. None was caught by care. Each was caught
by a number being *absurd*.

1. **Compute from the primary source.** Never infer a result from another signal's W/L,
   never quote a board scalar, never reuse a figure from an earlier run. The two worst
   errors both came from inference.
2. **State a sanity check and its value alongside every finding.** A −110 market's
   pooled rate must sit near 50%. If it doesn't, the measurement is wrong.
3. **Split by market before reporting any pooled rate.** This has failed four times.
4. **An empty filter is evidence about the filter first.** "Pinnacle never collects prop
   prices" was a `designation` filter matching nothing.
5. **An absurd number is a bug until proven otherwise.** Three of the five.

Rules 2, 3 and 4 now run mechanically in both graders (`check_rate`, `composition`,
`field_coverage`) and print to the Actions log. Rules 1 and 5 depend on a person.

## Multiple comparisons bound everything

806 graded cells with n≥30. Chance alone produces ~40 at z≥1.65 and ~18 at z≥2.0.
**Every finding this project has produced sits inside that range.** Quote this number
next to any new cell before calling it a finding.

## What is known

**No signal has demonstrated an edge, in-sample or out.** The strongest-looking one
(`pin_value`, 108-68 in CBB first halves, survived three attempts to break it) went
**8-11, −20.6%** forward. That is the project's single most important data point.

Closed with evidence — do not relitigate without new data: price gating, the dog angle,
"line moved against the money" without checking whether Pinnacle led (0-for-17), hit
rate as the currency.

## How the work is scored

- **FIT = in-sample = a hypothesis. FORWARD = out-of-sample = evidence.** Never present
  a FIT record as a reason to bet. `HOLDOUT_FROM` currently `2026-11-21`.
- Changing any threshold moves the holdout and restarts the forward test. That cost is
  deliberate.
- **ROI, not hit rate.** `money_level` hit 73.4% against a 69.8% base and lost 14.87
  units, because it lays −880 favourites.
- Base rates **per market and per stat**. Pooling is the recurring killer.
- `picks.json` logs what **the system suggested**, not what Justin bet. A bet he found
  himself is a miss on our side, and is not logged as a win.

## Working with Justin

- He makes the bet calls. Flagging is not deciding. Unit = $100.
- **Track every method in parallel.** His words: *"I don't want to hyperfocus on any
  method till we find the right one that produces the most consistent returns."*
- His ideas are hypotheses held to the same bar as everything else, **and the bar runs
  both ways**: his price-gating instinct overturned a gate that was costing plays; his
  dog-week read was tested and closed. His words: *"I don't want to say just be strict
  to what I'm saying bc if it doesn't work it doesn't."*
- Do not disregard a stated thesis without measuring it. `rlm_quiet` — low tickets AND
  low money, line moves there anyway — exists because it was disregarded twice first.
- His most-repeated idea is most-bet games as the place to fade the public. Measured
  2026-11-22: it **inverts with volume** (52.1% under 1k bets → 47.4% at 4k+; spreads at
  4k+ read 43.0%, −17.9% on n=114). Not promoted. Volume stays a slice, not a signal.
  NFL is untested there (n=43).
- Be specific about units and sides. Sign errors on CLV have happened.

## The register

`claude/propwatch-idea-register.md`, printed on every grader run. Items marked RECORDED
are computed and consumed by nothing. `audit.py` prints how long each has sat there.
Recorded-and-forgotten is the failure mode this repo is prone to.

## The scheduled line watch

`watch.py` runs on a schedule, writes `WATCH.md` and commits it every run. BROKEN /
LOADED / FOLLOWED. The committed `WATCH.md` IS the prior state — compare against it via
git history, never against memory, and **before calling anything a new crossing, diff the
FILE** (`git diff <last WATCH.md commit> HEAD -- watch.py`), not the commit list, which is
noisy from collector commits. A detector change makes two consecutive boards
non-comparable; when one has happened, run the previous version against the current
snapshot before saying a market moved. That rule exists because a rewrite on 2026-11-24
put a market in BROKEN with no market event behind it.

Run logs, and they are a CHAIN that casual search does not surface:
`claude/propwatch-watch-runs.md` holds runs 1-3 **and the procedure above**, then
`claude/propwatch-watch-run4.md`, `-run5.md`, `-run6.md`, one per run. **Read the latest
one before reading any `WATCH.md` bucket as a new setup** — most entries on any given
board are re-reports with the kill already written down, and each run ends with
pre-declared conditions that the next run is expected to resolve by name.

Standing debts as of run 6: **no closers have ever been stored for a declined board**
(ten of them now), so the watch has no feedback loop; and the single positive price rung
has decayed to nothing by the following run five runs running, which is latency, not edge.

## Before building a signal from a data cut

Ask what mechanism it trades against, and whether that mechanism is documented anywhere
outside our own archive. A correlation with no mechanism is a hypothesis. A mechanism
that shows up in the data is a finding.

## Known traps in the code

- **NFL stores pin rows as `(t, ty, d, pts, PRICE, LIMIT)`; CBB stores
  `(t, ty, d, pts, LIMIT, price)`.** Fields 4 and 5 are swapped between the two graders.
  Reading index 4 as a limit in NFL produced "Pinnacle limit of $105".
- Cross-book lead-lag is measurable ACROSS snapshots, not within one. All seven books
  share our snapshot timestamp, so sub-snapshot ordering is gone — but which snapshot a
  book first showed a new number is recorded for every book in every snapshot. That is
  ordering at 3 min (inside 2h of kickoff) / 10 min / 60 min resolution. **This file
  previously called it "permanently unmeasurable", which was wrong and closed the line
  of analysis for two days.** `xbook.py` measures it: FanDuel lags at z = −3.49 and an
  unnamed book 75 leads at z = +3.67, both after correcting for group size, on 1,110
  multi-book move events. Steam as breadth is still valid and still unbuilt.
- **Books 15, 49, 68, 71 and 75 are unnamed anywhere in this codebase** — only 69
  (FanDuel) and 30 (the opener) are identified. The book that leads the market is
  therefore anonymous, which is the blocking step on the finding above.
- CBB series must be truncated at tip. Not doing so contaminated 26.7% of series and
  changed 10% of graded closes.
- Moneyline openers are `[handicap, price]`; index 0 is a literal 0 for a moneyline.
