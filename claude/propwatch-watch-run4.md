# Propwatch — scheduled line watch, run 4

Continues `propwatch-watch-runs.md`, which holds runs 1-3, the procedure that must survive a
code change, and the index role. Split into its own doc following the convention
`propwatch-line-value-state.md` / `propwatch-line-value-run31..49` already uses.

**Read `propwatch-watch-runs.md` first** — its §"The procedure that must survive a code
change" governs every comparison made below.

---

## Run 4 — 2026-11-25T12:43Z. MESSAGE SENT. Pinnacle moved DEN@PIT 6h49m before the Rodgers benching was announced, and the detector then dropped the market as the public money left

**Board: 3 BROKEN, 12 LOADED, 6 FOLLOWED.** Compared against `WATCH.md` at `bf0245c`.
Committed at `2faeaf2`.

**Detector test passes.** `git diff bf0245c HEAD -- watch.py` is empty — byte-identical to
the version that produced the last committed `WATCH.md`, so the two boards are directly
comparable and run 1's §procedure does not need to run. (Run 3's note held: the commit list
is noisy from collector commits, the file diff is not. **Diff the file.**)

**Feed healthy; run 3's open gap self-recovered.** Newest `raw/actionnet` and
`raw/pin_prices` both `2026-11-25T1208Z`, **35 min** old against a 12:43Z wall clock at a
~60-minute cadence — inside the >75min rule and inside defect 14's 90-minute threshold.
Run 3's gap closed at `0329Z` having run **3h01m** (`0028Z` -> `0329Z`), then nine clean
intervals of 48-61 min. That is the seventh >75min gap in the window and the seventh to
self-recover, consistent with defect 17's job-ceiling pattern and **not a death** — run 3's
pre-declared escalation ("no snapshot newer than `0028Z` = ~5h+ and it stops looking like
defect 17") did not fire. Derived from the snap series, not `_diag`.

### What changed against run 3

| market | run 3 | run 4 | verdict |
|---|---|---|---|
| **DEN@PIT total/over** | BROKEN, Pin 37 confirmed over 4 snaps | **OFF THE BOARD.** Pin **36**, limits cut, over money 70% -> 64% | **resolved — and it is news, not flow** |
| **SEA@SF total/over** | BROKEN, over money 81% | BROKEN, over money **77%** | **pre-declared money trigger fired** |
| **NYJ@MIA total/over** | BROKEN, board 40.5/41 | BROKEN, **board 40.5 at all seven books** | **pre-declared close condition fired — series finished** |
| **SEA@SF spread/SF** | BROKEN, one print of FanDuel juice, Pin stationary 27.2h | BROKEN, **Pinnacle followed FanDuel** -116 -> -112 | not a defect-11 instance after all |

### DEN@PIT — the most important thing the watch has produced, and it is not a bet

Run 3's carry asked whether FanDuel would ever follow Pinnacle's 37.0. It did, and far more
happened besides. **Pinnacle took the total down a second full point and cut its limits in
both markets, and the cause is public knowledge: Pittsburgh benched Aaron Rodgers and named
Mason Rudolph the Week 12 starter.**

| | |
|---|---|
| **Pinnacle total** | 38.0 (72 snaps, ~36h) -> **37.0** `11-24T2138Z` -> **36.0** `11-25T0517Z` |
| 36.0 held | 8 consecutive snaps, **6h51m** (`0517Z` -> `1208Z`), **no retrace** |
| **Pinnacle total limit** | **$5,000 -> $3,000** at `0517Z` (-40%), still cut |
| **Pinnacle spread** | DEN -2.5 (69 snaps) -> **DEN -3.5** at `0517Z`; -106 / PIT +3.5 -106 |
| **Pinnacle spread limit** | **$20,000 -> $5,000** at `0517Z` (**-75%**), still cut |
| FanDuel total | 37.5 (-115) -> 37.5 (-105) -> **36.5 (-106)** at `0517Z`, now (-110) |
| board | 36.5 at bk15/68/69/71/75; **bk49 36**; bk30 frozen 39.5 |
| public | over **79% tickets / 64% money**, 11,046 bets |
| kickoff | 2026-11-27 20:00Z (Thanksgiving, ~2.3 days) |

**The limit cut is targeted, not a board-wide rescale — checked against every game.**
Pinnacle's limits rise steeply toward kickoff: GB@LA tonight is **$50,000 / $10,000**, and
the other three Thanksgiving-week games are **$30,000 / $5,000**. DEN@PIT kicks off *before*
six of the Sunday games and sits at **$5,000 / $3,000** — one sixth of the spread limit its
same-week peers carry, and below Sunday games four days further out. **A limit that falls as
kickoff approaches is Pinnacle withdrawing conviction, and it is the only market on the board
doing it.**

**This is register item #10 — "a limit SLASHED mid-week means news Pinnacle has not priced"
— occurring in NFL, live, for the first time.** Status has been RECORDED since 2026-11-21:
measured in CBB (161 cuts, bimodal, all >=25%, 28 at 50%+) and consumed by nothing. The
mechanism is documented outside our archive, which per CLAUDE.md is the distinction between
a finding and a correlation. **The NFL instance is dated and should move the item off
RECORDED.**

#### The move preceded the news by 6h49m, and that is only establishable because the prior state was committed

| event | time (UTC) |
|---|---|
| Pinnacle 38.0 -> 37.0, after ~36h of 38.0 | **2026-11-24T2138Z** |
| run 2 commits that move to `WATCH.md` at `96b2043` | **2026-11-24T2242Z** |
| Steelers press release (secondhand, 11:10 PM ET) | ~2026-11-25T0410Z |
| NBC Sports publishes, `meta-parsely-pub-date` | **2026-11-25T0427Z** |
| Pinnacle 37.0 -> 36.0, spread to -3.5, **both limits cut** | 2026-11-25T0517Z |

**Pinnacle's first point moved 6h49m before the announcement. The second point and the limit
cuts came 50 minutes after it.** The first half is recorded in a file committed to git
**before the news existed**, which is the one thing that makes it a measurement rather than
hindsight — and it is exactly what this task was created to capture.

**What this does and does not demonstrate.** It demonstrates that a Pinnacle move preceded
public information by most of a day, verified from both sides: the Pinnacle series, and the
publisher's own timestamp metadata. It does **not** demonstrate anything tradeable. **n=1.**
And the fade side never priced positive at any book at any point in the series and still does
not — best under 36.5 is bk69 at -110 = **-1.992%**; best PIT +3.5 is bk68 at -101 =
**-0.495%**. There was never a number to take. One instance is an anecdote, and the standing
rule for promoting one is a pre-declared test and a stated sample.

**It does, however, refine defect 22 rather than contradict it.** Defect 22 reads
"Pinnacle LED, therefore the money is chasing a repriced line," 0-for-19, and runs 2 and 3
both applied it here correctly on the mechanics. What this instance adds is *why* Pinnacle
led: it had information. That changes the interpretation, not the record — nothing here says
you can profit by following, and the price board says plainly that you cannot. **The useful
distinction is between Pinnacle leading on flow and Pinnacle leading on news, and the limit
is what separates them.** Pinnacle leading with its limit INTACT is flow. Pinnacle leading
with its limit CUT is news it has not finished pricing. The watch has not been reading the
limit as a state change; it prints the level only.

#### watch.py defect: a successful fade erases itself from the board

**DEN@PIT is in no bucket at all this run.** Over money fell 70% -> 64%, below `PUBLIC_MNY`
= 65, so the market stopped qualifying as public and vanished. The two-point move is still
there; the detector simply cannot see it any more.

**This is structural, not incidental.** BROKEN requires the public split to still exceed the
threshold *at the moment of observation*. But the thing the setup is waiting for is the
public being wrong and the money leaving — so a market that does what the thesis wants
**deletes itself from the board** while one where the public never budges stays visible
forever. The detector is biased toward unresolved setups and against resolved ones, and
without a message Justin would have seen the nearest-kickoff game he was told about twice
simply disappear.

**Fix (not applied this run, to avoid a detector change invalidating the next comparison):**
qualify a market as LOADED/BROKEN on the public split at its *entry* snapshot, carrying it
forward, with the current split printed alongside so the decay is visible. Changing it will
make run 5's board non-comparable with this one, so it belongs in its own commit with run 1's
§procedure applied.

### SEA@SF total — run 3's money trigger fired; the money is leaving and the tickets are not

Run 3's carry: *"Over money is 81%. If it drops below 80%, that is the first real test of
whether the money was chasing."* **It fired, and it has held below for ~6.5h.**

| | |
|---|---|
| public | **82% tickets / 77% money** on the over, 4,872 bets |
| money series | 86% -> 85 -> 84 -> 83 -> 82 -> 81 -> 80 -> 79 -> 78 -> **77%**, monotonic over 28h |
| tickets | 81% -> 82%, flat |
| **Pinnacle** | **45.0 held 21 snaps / 19h31m** (`11-24T1637Z` -> `1208Z`), over -111 / under -103, **no retrace** |
| Pinnacle limit | $3,000 |
| board | 45 at bk49/75; 45.5 at bk15/68/69; bk71 46; bk30 frozen 46.5 |

**Tickets flat while money decays nine points is money leaving, not tickets arriving** — the
reading run 3 pre-declared as the test of whether the money was chasing the repriced line.
It was. But Pinnacle LED this move too (`1637Z`, before FanDuel at `1737Z`), its limit was
never cut, and so by the distinction drawn above this is Pinnacle leading on **flow**, and
defect 22 applies unmodified. **Best under is bk71's 46.0 at -112 = -0.130%** — the board's
best rung and still negative.

### NYJ@MIA total — run 1's close condition fired. Finished

Run 1's carry: *"watch whether bk15/49/75 fold from 41 to 40.5; if the whole board goes to
40.5 the under at 41 disappears and the series is finished."* **All seven books, bk30
included, now read 40.5.** The 41 rung does not exist anywhere.

Pinnacle's handicap has been **41.0 across all 78 snaps (~39h)**, byte-identical for the
first 65, but its price has swung hard: over -105 -> -101 -> **+102**, under -109 -> -114 ->
**-117**. So Pinnacle holds 41 and now prices the under there as the clear side, while the
entire retail board has folded half a point *past* it to 40.5. **Defect 11 category 7 in its
purest form — the consensus overshooting past a stationary sharp number — and the fade side
is the worst number on the board.** Closed. Do not re-open without a handicap move.

### SEA@SF spread — Pinnacle followed FanDuel. Not the defect-11 instance run 3 anticipated

Run 3 left two conditions and the series met neither cleanly: Pinnacle's **handicap** never
moved off -3 (all 78 snaps, ~39h), but its **price** did, and in FanDuel's direction.

- FanDuel: SF -3 (-115) -> **(-110)** at `11-25T0028Z`, now held 8 snaps / 12h.
- Pinnacle: SF -116 -> **-113** at `0128Z` -> **-112** at `0228Z`, held 8 snaps. SEA +103 ->
  +100. Limit $10,000, raised at `11-24T1737Z` and **not cut**.

**So FanDuel led by one print and Pinnacle confirmed 60 minutes later.** That removes run 3's
"retail drifting past a stationary sharp number" reading — Pinnacle did not stay stationary,
it agreed. It should **not** be logged as a defect-11 instance. SF money has also decayed
66% -> 65%, sitting exactly on the threshold, so this market is one point from dropping off
the board the same way DEN@PIT did. Best SF -3 is bk71 at -108 = **-1.053%**; the fade side
SEA +3 is worse still, -1.780% at best.

### The price board — 72 rungs, ONE positive, and it is the same dead rung as run 3

Priced against **Pinnacle's no-vig fair at the identical rung** (defect 21), using the
alternate ladder to reach rungs the main does not sit on (run 44's method). bk30 excluded
(defect 15).

| rung | book | price | Pinnacle pair | limit | fair | EV |
|---|---|---|---|---|---|---|
| NYJ@MIA spread MIA +3.5 | bk69 | -100 | -120 / -103 MAIN | $10,000 | 50.229% | **+0.458%** |
| SEA@SF under 46.0 | bk71 | -112 | +104 / -121 ALT | $3,000 | 52.762% | -0.130% |
| DEN@PIT spread PIT +3.5 | bk68 | -101 | -106 / -106 MAIN | $5,000 | 50.000% | -0.495% |
| SEA@SF spread SF -3 | bk71 | -108 | -112 / +100 MAIN | $10,000 | 51.376% | -1.053% |
| SEA@SF over 45.0 | bk49 | -108 | -111 / -103 MAIN | $3,000 | 50.904% | -1.963% |
| DEN@PIT under 36.5 | bk69 | -110 | -114 / -102 ALT | $3,000 | 51.338% | -1.992% |

**Rule 5 fired on the first attempt and caught a real bug — record this.** The first run of
the price screen returned **+26.78% on NYJ@MIA NYJ -3.5** with a Pinnacle **overround of
-23.53%**. A negative overround is impossible, so per rule 5 it was treated as a bug and was
one: the screen keyed Pinnacle's ladder by `points` and paired each retail rung with *the
same* `points` value on the opposite side. That works for a total, where both sides sit at
the same number, and is wrong for a spread, where the opposite side sits at **-points** — so
it paired NYJ -3.5 against MIA -3.5 (an alternate, MIA laying 3.5) instead of MIA +3.5, i.e.
**both sides laying the favourite.** Eleven of 58 rungs read positive, all spreads, all
absurd. Corrected: 72 rungs, **one** positive. **The totals were never affected**, which is
why runs 2 and 3 — which priced only totals plus one main-line spread — were not wrong.
This belongs in `line-value-state.md`: *a spread's opposite side is at -points, a total's is
at the same points, and an overround below zero means the pair is wrong.*

**Sanity check, stated with its value (rule 2):** Pinnacle's overround is **2.83-3.77%**
across these ladders, against 2.88-4.09% in run 3 and 3.35-4.09% in run 2 — consistent across
three runs. A retail book at -100 to -112 against a tight sharp fair should price out
slightly negative, and **71 of 72 rungs do.** The single positive sits within half a point of
fair. That is the expected shape; **no absurd number survives, so nothing in the corrected
table is suspected to be a bug.**

**The one positive is the same rung run 3 already disqualified**, at the same book and the
same figure: NYJ@MIA spread is **64%/63% public**, below the 65/65 threshold, so it never
entered LOADED and pricing it is incidental. It is not a new datapoint.

**Run 37's pre-declared test 5 — the count stays at four.** Run 3 had three books holding
three positives. Run 4 has one positive at bk69, a book that has not owned a board before, so
there is no fifth single-book sweep and the test's threshold is still not met. What is worth
recording instead: **the board's best rung has fallen +2.957% (run 2) -> +0.881% (run 3) ->
+0.458% (run 4) across three consecutive runs**, while each run's leader expired before the
next. That is three consecutive confirmations that the screen measures latency and latency
decays.

**Composition check (rule 3):** BROKEN is **2 totals and 1 spread**. DEN@PIT, discussed at
length, is in **no** bucket and is explicitly not counted as a BROKEN entry. No pooling across
spread and total, and no pooled rate is quoted anywhere in this run.

**Multiple comparisons:** no new cell is claimed, so the 806-cell bound is not engaged. The
pre-news timing observation is **n=1** and is recorded as a dated instance, not a finding.

### Why a message was sent

1. **Run 3 promised this resolution** — *"the open question is no longer whether it is real
   but whether FanDuel ever follows."* It followed, and the market then left the board
   entirely. A promised resolution that also disappears from the output is the exact failure
   the carry section exists to prevent.
2. **Two pre-declared conditions fired** (SEA@SF money below 80%, NYJ@MIA board folding to
   40.5), both of them closing markets he was messaged about in runs 2 and 3.
3. **A documented mechanism showed up in the data for the first time in NFL** — register #10,
   the limit slash — with a verifiable pre-news timestamp. That is the "mechanism, not
   correlation" case CLAUDE.md asks for.

**The message says there is no play and why.** Every rung on every market in this run is
negative except one that does not qualify, the DEN@PIT move is spent and explained by public
news, and n=1 on the timing. It is a read, not a pick.

### Carry to run 5

- **Compare against `WATCH.md` at `2faeaf2`** (2026-11-25T12:43Z), and run the detector test
  by **diffing the file**: `git diff 2faeaf2 HEAD -- watch.py`.
- **Apply the watch.py entry-split fix in its own commit, and apply run 1's §procedure when
  you do.** Qualifying on the entry snapshot's split with the current split printed alongside
  is the fix; until it lands, a market vanishing from the board is as likely to mean the setup
  worked as that it never existed. **DEN@PIT is the first instance and SEA@SF spread, at 65%
  exactly, is about to be the second.**
- **Read Pinnacle's limit as a STATE CHANGE, not a level.** The distinction this run drew —
  Pinnacle leading with its limit intact is flow (defect 22, 0-for-19); Pinnacle leading with
  its limit cut is news it has not priced — is the first thing the watch has produced that
  could change what a BROKEN entry means. `lim_drop_frac` already exists and is portable. The
  watch prints the level and ignores the change.
- **Move register item #10 off RECORDED with this dated NFL instance.** Four days at RECORDED
  in CBB and the NFL instance is now observed end to end with a timestamped cause.
- **DEN@PIT closes first, on 2026-11-27 20:00Z, and defect 19 is now five runs old.** Runs 1-4
  have declined seven distinct boards with **no stored closers.** Record what DEN@PIT total
  (Pin 36.0), DEN@PIT spread (Pin DEN -3.5), SEA@SF total (Pin 45.0), SEA@SF spread (Pin -3)
  and NYJ@MIA total (Pin 41.0) close at. **Without this the watch has no feedback loop at all
  and four runs of reasoning are unfalsifiable.** This is now the single largest debt in the
  task.
- **SEA@SF total: the money trigger has fired, so the remaining live question is whether
  Pinnacle follows its own number down.** If Pinnacle comes off 45.0 while money keeps
  decaying, the whole series was flow correctly priced. If 45.0 holds to close with money
  under 75%, the public money left and the number did not — which is the first configuration
  in four runs that would be worth pricing on its own.
- **NYJ@MIA and SEA@SF spread are closed.** Do not re-report either without a Pinnacle
  **handicap** move.
- **The price-screen pairing bug belongs in `line-value-state.md`**, with the overround-below-
  zero check as the mechanical test. It would have produced eleven false positive rungs this
  run and rule 5 is the only thing that caught it.
- **The "opener" caveat stands, five runs on.** `watch.py` has `rec["snaps"]` and still prints
  "open" without it.
