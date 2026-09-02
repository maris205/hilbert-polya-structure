# Focused combinatorial collision gate

**Date:** 2026-09-02 UTC  
**Scope:** `LCP` against P114/P126/P148; `PAE` against P149/P155/P156 and the
permanent selector/extraction exclusion  
**External state:** `HOLD_EXTERNAL`  
**Paper allocation:** none

## Verdict first

```text
LCP  KILL_PROOF_ENGINE_TRANSFER_P148
PAE  KILL_PERMANENT_SELECTOR_EXTRACTION
     KILL_PROOF_ENGINE_TRANSFER_P156
```

Both proposed theorem packages are correct.  That is not enough.  LCP has the
same state space and mechanically transferable coordinate/inverse engine as
P148.  PAE has the same literal extraction shell and mechanically transferable
selected-set/section/complement engine as P156, reinforced by P149 and P155.
The PAE rank-eight `+4` anomaly is real but cannot override either hard kill.

## Scoring convention

Each of the five required layers receives one of:

- `0`: no material collision;
- `1`: shared vocabulary or a zero-credit generic ingredient;
- `2`: substantive theorem silhouette or reusable subproof;
- `3`: same carrier/interface or a proof that transfers mechanically.

One `3` in all-iterate coordinates or the dominant inverse/proof engine is a
kill.  Scores are diagnostic, not averages.

## LCP five-layer matrix

| closest occupied paper | literal update | state space | all-iterate coordinates | inverse/fibre | dominant proof engine | local verdict |
|---|---:|---:|---:|---:|---:|---|
| P114 rooted-forest leaf peeling | 1 | 1 | 1 | 1 | 2 | not decisive alone |
| P126 balanced composition refinement | 0 | 0 | 2 | 2 | 2 | strong analogy, not decisive alone |
| P148 even-level plane-tree contraction | 2 | 3 | 3 | 3 | 3 | **hard kill** |

### Literal layer

P114 deletes exposed nonroot leaves; LCP deletes a whole first-child subtree
at every surviving plane-tree vertex.  P126 splits composition letters.  P148
deletes odd generations and promotes ordered grandchildren.  LCP is not
literally any of these rules, but its update and P148's update are both local
rank-lowering endomorphisms of recursively ordered child lists.

Literal novelty does not rescue a candidate once the main proof transfers.

### State-space layer

LCP and P148 use exactly the same finite carrier
`PT_{<=N}=disjoint_union_(1<=n<=N) PT_n`.  They also make the same essential
exact-layer distinction: `PT_n` is a source layer, not an invariant carrier.
P114 uses labelled rooted forests on subsets, and P126 uses fixed-weight
compositions, so those two collisions are weaker at this layer.

### All-iterate layer

P148 tracks original vertex identities and proves

```text
vertex survives E^t  iff  2^t divides original depth.
```

The same induction, without any new combinatorial device, proves

```text
vertex survives L^t  iff  every Ulam--Harris coordinate exceeds t.
```

In both cases the coordinate is updated deterministically after one round
(divide depth by two; subtract one from every child index), and the sharp clock
is obtained by taking the extremal surviving coordinate.  This is precisely
the gate's “all-iterate coordinate mechanically migrates” kill condition.

P126 adds a secondary warning: its all-iterate theorem also reduces a recursive
word system to a canonical coordinate code and reads the clock and image tower
from that code.

### Fibre layer

P148 builds every predecessor independently at target vertices, multiplies
local factors, extracts an exact-size coefficient, and reads the image
threshold from the lowest degree.  LCP does exactly the same:

```text
P_(t,U)=z^|U| T(z)^(t i(U)) (1+T(z)+...+T(z)^t)^l(U).
```

Only the local factor changes from P148's productive block-and-gap insertion
to LCP's arbitrary deleted prefix subtrees.  P126's product over canonical
one-runs is another close local-product inverse, but P148 already supplies the
decisive transfer.

### Proof-engine layer and owner subtraction

After subtracting Catalan enumeration, generic plane-tree recursion, pruning,
expansion operators, strict vertex loss, and coefficient positivity, the LCP
package is:

1. original-coordinate survival under iteration;
2. a sharp coordinate clock;
3. a target-local recursive inverse;
4. its minimum-source/image condition.

That four-part conjunction is P148's proof architecture.  P114 also owns the
portfolio's parallel tree-peeling slot, while P126 owns the recursive
all-iterate code/product-fibre silhouette.  The external old-leaf/old-path
literature further removes generic leftmost-pruning language.  No paper-scale
residual remains.

## PAE five-layer matrix

| closest occupied paper | literal update | state space | all-iterate/tower | inverse/fibre | dominant proof engine | local verdict |
|---|---:|---:|---:|---:|---:|---|
| P149 endpoint-peak extraction | 3 | 3 | 2 | 1 | 2 | selected-word architecture occupied |
| P155 cycle-maximum extraction | 1 | 3 | 1 | 2 | 3 | threshold/scheduler/weighted-fibre conjunction occupied |
| P156 weak-excedance extraction | 3 | 3 | 3 | 3 | 3 | **hard kill** |
| permanent selector/extraction rule | 3 | 3 | 3 | 3 | 3 | **controlling hard kill** |

### Literal layer

PAE and P156 both perform exactly this meta-operation on a permutation:

```text
evaluate an absolute predicate involving position and value;
retain the qualifying subword in old order;
standardize it.
```

PAE substitutes congruence modulo two for P156's weak-excedance inequality.
P149 has the same selected-subword/standardization interface with a local-peak
predicate.  P155 selects one summary value per ordered cycle support rather
than a literal subword, so its literal collision is weaker.

### State-space layer

All four maps act on rank-varying symmetric groups.  PAE adds `S_0`, but one
boundary state does not change the carrier architecture.  The source/target
rank and standardization conventions are the same.

### All-iterate and tower layer

P149 composes explicit one-step right sections to obtain all-rank iterate
sections and a sharp clock.  P156 iterates a canonical minimum-rank section,
tracks a two-resource update, and shifts the tail by one at each lift.  PAE's
even-loss clock and explicit two-rank inverse tower use the same strategy:
prove a one-step section, iterate it, and certify one unit of extra tail.
Different resource recurrences do not constitute a different proof engine.

P155 deliberately excludes a clock, so it is not the all-iterate owner; its
collision occurs in the one-step target geometry below.

### Fibre layer

P156 chooses increasing selected positions `P` and values `A`, forces
`p_i -> a_(sigma_i)`, checks a compatibility condition, and counts bijections
of the complements.  Its Ferrers completion product becomes, under parity
colors, two complete bipartite matching factors.  The resulting PAE formula

```text
(h!)^2 sum_c E_n(c) E_n(c o sigma^(-1))
```

is therefore a direct two-color specialization of the same decomposition.

P155 adds the same higher-level silhouette: optimize a target-dependent
minimum source rank by interleaving two orders, extend the minimum construction
to every larger rank, and sum factorial weights over compatible supports.

### Proof-engine layer and permanent rule

The exact PAE threshold proof is sound, but its steps are mechanically those
of P156:

1. expose selected position and value sets;
2. translate the predicate into a target compatibility obstruction;
3. greedily embed a minimum section;
4. fill the complements;
5. sum the completion multiplicities;
6. use rank equality to identify recurrence;
7. iterate a chosen section for sharpness.

`docs/papers157_161_sequence/phase1/HISTORICAL_OCCUPANCY.md` independently
forbids another record/border/run/palindrome/Lyndon/peak/excedance selector
obtained only by changing parity, direction, standardization, or endpoint
convention.  PAE is the literal test case named by that rule: parity changes
the predicate but not the theorem or inverse architecture.

## Owner subtraction summary

| candidate | externally owned input | internally occupied residual | result |
|---|---|---|---|
| LCP | leftmost-leaf/path pruning, inverse expansions, Catalan tree recursion | P148 coordinate iteration + vertex-local inverse; P114 pruning; P126 recursive product fibre | `KILL` |
| PAE | parity-alternating fixed class and its static enumeration | P149 selected-word sections; P155 target scheduler; P156 selected-set fibres/tower; permanent selector rule | `KILL` |

The full theorem statements and proofs are in
`THEOREM_CONTRACTS_AND_PROOFS.md`; direct-owner chains are in
`DIRECT_OWNER_CHAINS.md`.  `verify_collision_gate.py` independently searches
for counterexamples and its frozen output is `COLLISION_CANONICAL.txt`.

## Release boundary

No system is numbered or frozen, no manuscript is drafted, and no priority or
novelty inference is made from a bounded search.  External state remains
`HOLD_EXTERNAL`.
