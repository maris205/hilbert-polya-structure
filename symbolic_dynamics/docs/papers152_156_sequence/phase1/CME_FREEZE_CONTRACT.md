# CME reduced hostile freeze contract

**Decision:** `PASS_FREEZE_REDUCED`.  **External status:** `HOLD_EXTERNAL`.
**Proposed paper:** P155, conditional on the separate numbering decision.
This contract freezes an exact image/fibre note and expressly excludes the
unproved power clock.  It makes no novelty, priority, authorship, submission,
or release claim.

## 1. Literal map and carrier

For `pi in S_n`, let `B_1,...,B_m` be its cycle supports ordered by

```text
min B_1<...<min B_m.
```

Define

```text
C(pi)=std(max B_1,...,max B_m) in S_m.                    (1)
```

For a finite ambient cutoff `N`, this is a self-map of
`S_{<=N}=disjoint_union_{1<=n<=N}S_n`.

## 2. Frozen theorem A — strict rank and recurrence

Freeze:

```text
|C(pi)| = number of cycles of pi;                         (A1)
C(pi)=pi iff pi=id_n;                                     (A2)
every nonidentity step strictly lowers rank;              (A3)
the recurrent states in S_{<=N} are id_1,...,id_N.        (A4)
```

### Proof status: `PROVABLE AS STATED`

There is one output entry per cycle, proving (A1).  Equality of source and
target ranks means every cycle is a singleton, so `pi=id_n`; identities are
fixed.  Strictly decreasing positive rank precludes every other recurrent
state.

No formula for the absorption time of an arbitrary source is frozen.

## 3. Frozen theorem B — exact target image threshold

For `sigma=sigma_1...sigma_m`, let `rlmin(sigma)` be its number of
right-to-left minima and put

```text
mu(sigma)=2m-rlmin(sigma).                                (B1)
```

Freeze, for every `n>=m`,

```text
sigma in C(S_n) iff n>=mu(sigma).                         (B2)
```

Moreover the proof gives a deterministic support section at the minimum rank
and at every larger rank.

### Necessity

Call a cycle support a singleton if its minimum and maximum are the same
ground-set coordinate.  If `B_i` is singleton, then for every `j>i`,

```text
max B_j>=min B_j>min B_i=max B_i.
```

Therefore `sigma_i` is a right-to-left minimum.  At most
`rlmin(sigma)` blocks can use one coordinate; every other block needs distinct
minimum and maximum coordinates.  Hence every source has at least
`2m-rlmin(sigma)=mu(sigma)` points.

### Constructive sufficiency

Use formal opener and closer chains

```text
O_1<...<O_m,       K_1<...<K_m,
```

and pair `O_i` with `K_{sigma_i}`.  For a non-singleton impose
`O_i<K_{sigma_i}`.  Identify `O_i=K_{sigma_i}` exactly when `sigma_i` is a
right-to-left minimum.

These identifications are compatible.  If `sigma_i=v` is a right-to-left
minimum, every smaller value `u<v` occurs at a position before `i`; hence all
predecessors of `K_v` in the closer chain have paired openers no later than
`O_i`.  Right-to-left-minimum pairs occur in the same order in the opener and
closer chains.  Thus the quotient precedence relation is acyclic.  A linear
extension provides a word of opener-only, closer-only, and simultaneous
events of length `mu(sigma)`.  Its paired coordinates are ordered supports
whose standardized maxima are `sigma`.

Equivalently, the exact endpoint DP allows `O`, an available `K`, or a
simultaneous event; the simultaneous events are precisely the right-to-left
minimum indices.  This proves that its optimum is (B1), not just that the DP
finds a source.

To realize a larger rank, first replace a simultaneous endpoint by separate
opener/closer endpoints when needed, then insert interior coordinates into an
open block.  The order of minima and maxima is unchanged.  This includes the
identity target, for which all minimum-rank blocks are singleton.

## 4. Frozen theorem C — every-target weighted fibres

For `sigma in S_m`, let `P_n(sigma)` be the ordered set partitions

```text
(B_1,...,B_m) of [n]
such that min B_1<...<min B_m and
std(max B_1,...,max B_m)=sigma.                           (C1)
```

Freeze

```text
|C_n^{-1}(sigma)|=
 sum_{(B_1,...,B_m) in P_n(sigma)} prod_i (|B_i|-1)!.     (C2)
```

### Proof status: `PROVABLE AS STATED`

The support partition of a source permutation is unique.  On a fixed support
`B_i`, the number of cyclic orders is `(|B_i|-1)!`; choices on different
supports are independent.  Conversely any supports satisfying (C1), equipped
with one cyclic order per block, form a unique source permutation mapped to
`sigma`.  Summing gives (C2), including zero fibres.  The total of (C2) over
all targets and ranks is checked against `n!`, but that check is not the proof.

## 5. Explicit clock exclusion

The observed functional-graph maxima through rank ten are

```text
0,1,2,2,3,3,3,3,4,4.
```

Reverse permutations give witnesses at ranks `1,2,3,5,9,17`.  Nevertheless
the statement

```text
min{mu(sigma):tau(sigma)=t}=2^t+1                       (GATE)
```

has no all-parameter lower-bound proof.  It is therefore excluded from the
title, abstract, theorem statements, implications, and conclusions.  The
paper may mention it only as a computationally supported open question in its
limitations paragraph.  It must not claim:

- a sharp global maximum clock;
- an explicit absorption time for every source;
- global minimum rank of iterated preimages; or
- that enumeration through rank ten proves any of these.

## 6. Owner and portfolio subtraction

The following receive zero contribution credit:

- cycle maxima and prescribed cycle-maxima sets;
- ordering cycles by their minima;
- set-partition opener/closer/singleton/transient configurations;
- crossing/nesting distributions with block endpoints fixed;
- the factor `(|B|-1)!` counting cyclic orders on a fixed support; and
- generic finite-map rank monotonicity.

Mandatory nearby primary sources are Chen--Deng--Du--Stanley--Yan on fixed
block minima/maxima, Rubey--Stump on opener/closer configurations, Mongelli on
cycles ordered by minima, and Andrews--Egge--Gawronski--Littlejohn on cycle
maxima.  `OWNER_SEARCH_LOG.md` records the exact links and bounded exact-map
queries.  A non-hit is not novelty evidence.

### Separation from P105

P105 preserves `[n]` and removes the current minimum from every nontrivial
cycle by arrow surgery; its clock is largest-cycle length minus one.  CME
forgets cyclic order after reading support endpoints, changes rank to the
number of cycles, and has a target-resolved opener/closer inverse.  P105's
cycle-pruning normal form and arrow-surgery fibres do not prove (B2) or (C2).

### Separation from P149 and WEX

P149 uses local endpoint peaks and alternating-slot fibres.  WEX uses diagonal
weak-excedance selection, maximum drop, and deficient Ferrers completions.
CME uses disjoint-cycle supports, right-to-left minima as singleton capacity,
and factorially weighted ordered set partitions.  “Rank-changing permutation
followed by standardization” receives zero credit; the literal selectors,
image obstructions, sections, and fibre proofs remain different.

## 7. Hostile paper-size gate

**Verdict: PASS for a narrow 4--6 page short note, under this reduced
ceiling.**  The justification is conjunctive:

1. Theorem B is a sharp, all-parameter, target-dependent image theorem with a
   minimum-rank constructive inverse, not a one-step closure observation.
2. Theorem C independently resolves every target fibre and exposes the exact
   labelled-cycle species behind the map.
3. Theorem A supplies a complete recurrent classification and proves genuine
   absorption on every finite cutoff.

The note becomes too thin if either B or C is removed.  The open clock is not
needed for this honest image/fibre paper and is forbidden as a result.  The
paper must frame itself as an exact inverse-geometry note, not as a solved
clock paper.

## 8. Verification ceiling

The paper-local verifier may be copied from the replacement-2 scout.  Its
frozen replay currently covers

```text
4,037,913 literal CME states through rank ten;
145,684 image/schedule boxes;
53,218 target fibre checks;
12,567,139 assertions across all ten scout systems.
```

The paper-local copy should isolate CME assertions and state explicitly:

```text
image/fibre/recurrent theorems: exact PASS
power clock: NOT CLAIMED
external status: HOLD_EXTERNAL
```

