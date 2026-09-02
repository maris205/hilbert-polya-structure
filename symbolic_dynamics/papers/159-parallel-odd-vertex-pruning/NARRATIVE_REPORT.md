# Narrative report — P159

**Status:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

## The dynamics in plain language

Fix an ambient label set `[n]`.  A state is any simple graph on any subset of
those labels.  One parallel update examines all current degrees, deletes every
odd-degree vertex simultaneously, and keeps the induced graph on the
survivors.  Graphs in which every degree is even are fixed; “even” here does
not imply connectivity.

The forward clock is elementary.  The odd-degree set has even cardinality, so
each active round removes at least two vertices.  The path loses exactly its
two endpoints in every active round, attaining `floor(n/2)`.  This clock is
structural context and receives no independent contribution credit.

## The useful signal

The backward map is uniform over targets.  Fix a target graph `H` on `s`
labels and ask for a strict predecessor on `s+d` labels.  Once the deleted
label set `D` is fixed, all target-internal edges are fixed and the free edges
are precisely those meeting `D`.  The requirements “survivors even before
deletion” and “deleted vertices odd” form the binary incidence system of one
connected graph.

The system is consistent exactly for positive even `d`.  Its nullity gives

```text
2^[s(d-1)+binom(d-1,2)]
```

solutions for fixed `D`; choosing `D` gives

```text
B_n(s,s+d)
 = binom(n-s,d) 2^[s(d-1)+binom(d-1,2)].
```

Only the automatically even sum of the target degree-parity vector enters the
rank calculation.  The exact fibre therefore does not depend on the target
edges.

## Why one matrix controls every time

The strict transfer uses target rank as row and source rank as column.  A
strict predecessor contains a nonempty odd-degree set and hence cannot wait.
Target-independence then makes conventional matrix multiplication count
literal reverse orbit chains without quotient correction:

- a non-even target has rank-refined time-`t` fibre `B_n^t`;
- an even target has `I+B_n+...+B_n^t`, because it may be reached early and
  then held fixed.

This yields an exact image criterion: at `t>=1`, a rank-`s` target occurs if
and only if it is even or `n-s>=2t`.  Summing the fixed-target fibres produces
the complete depth CDF and exact shells.

## Mandatory boundaries

- `d=0` does not belong to the strict matrix: the same-rank one-step fibre is
  the target itself exactly when the target is even.
- For a fixed deleted pair over the empty target (`s=0,d=2`), the unique
  source is `K_2`; aggregated over labels, `B_n(0,2)=binom(n,2)`.
- Rows are targets and columns are sources.  At `n=4`, the sentinels are
  `B_4(0,2)=6`, `B_4(2,0)=0`, and `(B_4^2)(0,4)=24`.
- At `t=0` every state occurs; the later image criterion is stated only for
  `t>=1`.
- At `n=0` there is one fixed state.  At `n=1` the empty graph and singleton
  are both fixed.  Both maximum clocks are zero.

## Ownership and collision boundary

Sequential parity deletion games own odd/even vertex-removal game language
and the even terminal locus.  Eulerian deletion and editing own optimization
over chosen parity-correcting deletions.  Parallel peeling owns simultaneous
round terminology.  The handshaking lemma, connected binary incidence rank,
cycle-space enumeration, generic absorption, matrix multiplication, and the
path clock all receive zero credit.

The retained object is only the conjunction of target-uniform strict inverse
enumeration, correctly oriented all-time powers, and exact image/CDF
consequences for the literal simultaneous rule.  The bounded source search is
not a novelty, priority, ownership-completeness, or release result.

Internally, P114 shares synchronous deletion vocabulary, and P148 shares the
clock/fibre/image silhouette.  Their tree-height, attachment, and ordered
grammar proofs do not mechanically yield the connected `F_2` incidence
extension.  P123, P141, and P146 differ in both literal dynamics and proof
engine.  Generic portfolio packaging is nevertheless subtracted.

## Evidence and limitations

The all-parameter proof is symbolic.  The unchanged paper-local verifier checks
3,167,525 exact assertions.  It enumerates all 41,658 graph states through
ambient order six, tests every target and relevant time, and independently
row-reduces 511 parity systems through total order nine.  Two cold runs match
the frozen transcript byte for byte.  Computation is counterexample pressure,
not proof or owner clearance.

The manuscript does not address asynchronous or random deletion, directed
graphs or multigraphs, unlabelled quotients, weighted edges, selected deletion sets,
or asymptotic random-graph laws.  Formal Review A returned zero findings;
Review B found only a stale lifecycle sentence in the evidence ledger, now
closed without a mathematical change.
