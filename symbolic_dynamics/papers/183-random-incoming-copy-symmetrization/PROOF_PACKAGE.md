# Proof package — P183

## Status

`PROVABLE AS STATED`

## Assumptions

- `n >= 1` and vertices are labelled by `[n]`.
- A state has one binary arc bit `A_uv` for every ordered pair `u != v`; loops
  are excluded and opposite arcs are independent.
- `C_v` replaces every outgoing bit `A_vu` by the old incoming bit `A_uv` and
  leaves all other bits unchanged.
- At each Markov epoch, `v` is sampled uniformly and independently from `[n]`.
- `S(t,r)` is the Stirling number of the second kind, including `S(0,0)=1`.

## Notation

- `H(A)` is the simple conflict graph with edge `{u,v}` iff `A_uv != A_vu`.
- A history `W` has support `S(W)` and missing set `M(W)=[n]\S(W)`.
- `I(H)` denotes all independent vertex sets of `H`.
- `k(B)` is the number of isolated vertices in `H(B)`.

## Proof strategy

Analyze each unordered pair independently under a selected vertex.  This gives
monotone conflict deletion.  Coarsen histories first by missing set for
absorption, then refine by first-occurrence order for labelled endpoints.
Invert one local update directly for the fibre formulas.

## Dependency map

1. Pairwise bit calculation proves conflict deletion and idempotence.
2. Iterated conflict deletion proves the history-residue lemma and recurrence.
3. History residue plus surjection enumeration proves the absorption CDF.
4. Pairwise bit calculation plus first-occurrence partitions proves the
   every-target kernel.
5. Direct star inversion plus an intersection lemma proves both fibre counts.

## Proof

### Step 1: one selected vertex deletes its conflict star

Fix distinct vertices `u,v`.  When `v` is selected, the outgoing arc `v->u`
is overwritten by the old bit on `u->v`; the latter arc is unchanged.  Thus
the two output bits are equal.  If neither endpoint of an unordered pair is
the selected vertex, both bits remain unchanged.  It follows that

`E(H(C_v A)) = {e in E(H(A)): v notin e}`.

Applying `C_v` again reads and writes equal bits, proving idempotence.  If
`{u,v}` is initially a conflict, `C_u` first preserves the old bit entering
`u`, whereas `C_v` first preserves the old bit entering `v`; these bits differ.
Hence `C_u C_v A != C_v C_u A` on that pair.

### Step 2: history residue and recurrence

Apply Step 1 along a history.  An initial conflict survives exactly when
neither endpoint occurs in the history.  Therefore

`H(C_W A)=H(A)[M(W)]`.

A symmetric state has empty conflict graph and every update fixes it.  From a
nonsymmetric state, selecting an endpoint of a conflict has positive
probability and strictly decreases the conflict set; no later move can restore
it.  The state cannot belong to a recurrent communicating class.  Hence the
recurrent states are exactly the `2^binom(n,2)` symmetric digraphs.

### Step 3: absorption CDF

By Step 2, the endpoint is symmetric iff the missing set `M(W)` induces no
conflict, equivalently iff `M(W)` is independent in `H(A)`.  For a fixed
missing set `M`, a history has exactly this missing set iff it is a surjection
from `[t]` to the prescribed alphabet `[n]\M`.  The number is

`(n-|M|)! S(t,n-|M|)`.

Distinct missing sets give disjoint history classes.  Summing over independent
`M` and dividing by `n^t` proves the stated CDF.  At `t=0`, only `M=[n]`
contributes, and it is independent exactly when the initial state is already
symmetric.

### Step 4: endpoint kernel

Fix a conflict `{u,v}`.  If neither endpoint is selected, it remains.  If at
least one is selected, let `e` be the endpoint with earliest occurrence and
`o` the other endpoint, treating an unselected endpoint as having infinite
rank.  The first action at `e` makes both bits equal to the old incoming bit
`A_oe`.  Their equality then persists.  This is precisely the defined endpoint
`E_(S,pi)(A)`.

For a prescribed support `S` of size `r` and prescribed first-occurrence order
`pi`, partition the `t` time positions by their labels.  Order the nonempty
blocks by their least elements and label them successively by `pi`.  This is a
bijection from set partitions of `[t]` into `r` blocks to the desired histories.
There are `S(t,r)` histories.  Summing this weight over the support/order pairs
whose explicit endpoint equals `B` proves the complete multiplicity and, after
division by `n^t`, the Markov kernel.

### Step 5: labelled one-step fibres

If `C_v A=B`, every pair incident with `v` is symmetric in `B`; hence `v` is
isolated in `H(B)`.  Conversely, for each isolated `v`, all source arcs not
leaving `v` are forced by `B`, while the `n-1` overwritten outgoing arcs are
free.  This gives `2^(n-1)` sources for each of `k(B)` labelled actions, hence
`k(B)2^(n-1)` labelled pairs.

### Step 6: distinct one-step fibres

Every admissible-vertex predecessor family contains `B`.  If a source lies in
the families for distinct `v,w`, the `w`-family forces all arcs leaving `v`
except possibly `v->w`, and the `v`-family forces all arcs leaving `w` except
possibly `w->v`.  On `{v,w}`, the two family conditions separately force those
last two arcs.  All source bits therefore equal `B`.  Pairwise intersections
are exactly `{B}`, so for `k(B)>0` the union has

`1+k(B)(2^(n-1)-1)`

states.  With `k(B)=0` there is no admissible action and the source set is
empty.

The claims follow. ∎

## Boundary audit

- `n=1`: one state, one action, one labelled and distinct predecessor.
- `t=0`: the Stirling convention gives the identity endpoint and correct
  absorption indicator.
- Initially symmetric states: all missing sets are independent, and the
  surjection sum counts every history.
- Targets with no isolated conflict vertex: both one-step fibre counts are
  zero.

## Corrections or missing assumptions

None identified.  The uniform-choice assumption is required only when turning
history counts into probabilities; all integer multiplicities remain valid
without it.

## Open risks

- External ownership of the literal update has not received a comprehensive
  audit.
- No isomorphism-class endpoint formula or asymptotic graph-family analysis is
  claimed.

