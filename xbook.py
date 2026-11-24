#!/usr/bin/env python3
"""xbook.py -- which book moves first, measured across snapshots.

CORRECTS A CLAIM THIS PROJECT TREATED AS SETTLED. CLAUDE.md and the brain doc said
cross-book lead-lag was "permanently unmeasurable with the existing archive, because all
seven books share our snapshot timestamp". The first half is true and the conclusion does
not follow. Books share a timestamp WITHIN a snapshot, so sub-snapshot ordering is gone
for good -- but which snapshot a book FIRST shows a new number is recorded, for all seven
books, in every snapshot we have ever taken. That is ordering at our sampling resolution:
3 min inside 2h of kickoff, 10 min inside 12h, 60 min otherwise.

The overstatement closed off this whole line of analysis on 2026-11-22 and it stayed
closed until 2026-11-24.

METHOD. For each (game, market, side), find every snapshot where a book's number changed.
Group changes in the same direction inside a 4-snapshot window into one "move event".
A book LED an event if it was among those showing the change at the earliest snapshot in
the window.

THE CORRECTION THAT MATTERS. Raw lead rate is meaningless on its own, because a book that
mostly appears in 2-book events has a ~50% baseline while one in 6-book events has ~17%.
Comparing raw rates is the same composition error as the Pinnacle-limit/market-mix
confound that produced a false monotonic finding on 2026-11-22. So each book is scored
against the null set by the sizes of the groups it actually appeared in.

FIRST RUN, 1227 snapshots, 1110 multi-book events:

    book     led   part   actual     null    diff      z
    b75      473    808    58.5%    52.1%   +6.5    +3.67
    b49      290    564    51.4%    50.8%   +0.6    +0.31
    b15      378    712    53.1%    53.4%   -0.3    -0.14
    b68      259    513    50.5%    52.8%   -2.3    -1.05
    b71      288    601    47.9%    50.0%   -2.1    -1.03
    FanDuel  110    284    38.7%    49.1%  -10.3    -3.49

Six books tested; chance gives ~0.3 at |z|>=2. Two sit past 3.4, in opposite directions,
with the middle four flat -- the shape of a real effect rather than an artifact, and the
group-size correction has already been applied.

FanDuel lagging is mechanistically unsurprising: it is the retail book, and every signal
in this project reads its number. Book 75 leading is the useful half, and book 75 is
ANONYMOUS -- only 69 (FanDuel) and 30 (opener) are identified anywhere in this codebase.
Naming 15, 49, 68, 71 and 75 is now the blocking step, not the measurement.

This does NOT reopen rule 22 in propwatch-line-value-state.md (0-for-17 on "line moved
against the money" without checking whether Pinnacle led). That tested Pinnacle against
FanDuel and is still closed. This is a different and finer instrument.
"""
import gzip,json,glob,collections
BOOKS={'15':'b15','30':'opener','49':'b49','68':'b68','69':'FanDuel','71':'b71','75':'b75'}
fs=sorted(glob.glob('raw/actionnet/*/*.json.gz'))
ser=collections.defaultdict(dict)
for f in fs:
    ts=f.split('/')[-1].replace('.json.gz','')
    try: j=json.load(gzip.open(f,'rt'))
    except Exception: continue
    for g in j.get('games',[]):
        for bid,m in (g.get('markets') or {}).items():
            ev=m.get('event') or {}
            for mk in ('spread','total'):
                for x in (ev.get(mk) or []):
                    if x.get('is_alt_market') or x.get('is_live') or x.get('value') is None: continue
                    ser[(g.get('id'),mk,x.get('side'),bid)][ts]=x['value']
firstmap=collections.defaultdict(lambda: collections.defaultdict(list))
for (gid,mk,sd,bid),d in ser.items():
    tss=sorted(d); v=[d[t] for t in tss]
    for i in range(1,len(v)):
        if v[i]!=v[i-1]: firstmap[(gid,mk,sd)][tss[i]].append((bid,v[i-1],v[i]))
WIN=4
lead=collections.Counter(); part=collections.Counter()
exp=collections.defaultdict(float)          # expected leads under the null
gsizes=collections.Counter()
for key,bytime in firstmap.items():
    times=sorted(bytime); used=set()
    for t in times:
        if t in used: continue
        idx=times.index(t); window=times[idx:idx+WIN]
        group=collections.defaultdict(list)
        for w in window:
            for bid,o,n in bytime[w]: group[1 if n>o else -1].append((w,bid))
        for direction,items in group.items():
            books={b for _,b in items}
            if len(books)<2: continue
            items.sort(); first_t=items[0][0]
            n_lead=len({b for w,b in items if w==first_t})
            m=len(books)
            gsizes[m]+=1
            for b in books:
                part[b]+=1
                # null: every book equally likely to be in the leading set
                exp[b]+= n_lead/m
            for w,b in items:
                if w==first_t: lead[b]+=1
            for w in window: used.add(w)
print("SANITY: if ordering were random, each book leads at the rate set by the SIZE of")
print("the groups it appears in. A book mostly in 2-book events has a ~50% baseline; one")
print("in 5-book events has ~20%. Comparing raw lead rates without this is the same")
print("composition error as the Pinnacle-limit/market-mix confound.\n")
print("group sizes:", dict(sorted(gsizes.items())))
print()
import math
print(f'{"book":10} {"led":>5} {"part":>6} {"actual":>8} {"null":>8} {"diff":>7} {"z":>6}')
for b in sorted(part, key=lambda x:-(lead[x]-exp[x])/max(math.sqrt(exp[x]),1)):
    if part[b]<30: continue
    a=100*lead[b]/part[b]; e=100*exp[b]/part[b]
    z=(lead[b]-exp[b])/math.sqrt(exp[b]*(1-exp[b]/part[b])) if exp[b]>0 else 0
    print(f'{BOOKS.get(b,b):10} {lead[b]:>5} {part[b]:>6} {a:>7.1f}% {e:>7.1f}% {a-e:>+6.1f} {z:>6.2f}')
print()
print("Multiple comparisons: 6 books tested. Chance gives ~1 at |z|>=1.65, ~0.3 at |z|>=2.")
