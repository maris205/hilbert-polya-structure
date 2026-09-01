# Narrative report — P149

**Status:** anonymous internal theorem draft / `HOLD_EXTERNAL`  
**Literal carrier:** `S_{<=N}=disjoint_union_{1<=m<=N} S_m`

## Literal dynamics

For `pi=pi_1...pi_n`, set the two fictitious neighbours to zero.  Read all
values larger than both neighbours from left to right and standardize the
resulting nonempty word.  This defines `P(pi)`.  The global maximum guarantees
nonemptiness.  For `n>1`, peak positions are nonadjacent, so the rank drops to
at most `ceil(n/2)`.

This variable-rank formulation is essential.  `P` is not a self-map of one
symmetric group; it is a literal self-map of the finite disjoint union.

## Right section and all-rank images

For a target `sigma in S_m` and source rank `n>=2m-1`, turn the top `m` values
into the target order:

```text
h_i=n-m+sigma_i.
```

Place `1,2,...,m-1` between consecutive highs and append every unused low
value in decreasing order.  The highs are exactly the endpoint-inclusive
peaks.  Valleys and the final decreasing slope create none.  Standardizing
the high word returns `sigma`.

After `k` extractions the packing bound gives rank at most
`ceil(n/2^k)`.  Conversely, if `m` is at most that bound, the minimal required
source length is `2^k m-(2^k-1)`.  Build `k-1` minimal odd lifts backward from
`sigma`, then use the available length `n` in the outer lift.  This proves,
constructively,

```text
P^k(S_n)=disjoint_union_{m<=ceil(n/2^k)} S_m.
```

Disjoint ranks immediately give the cardinality sum of factorials.

## Sharp clock

Every nonsingleton rank strictly decreases, so the singleton is the unique
recurrent state.  Packing gives `tau(pi)<=ceil(log2 n)`.  Define `w_1=1` and
lift a deepest witness at rank `ceil(n/2)` into rank `n`.  Then

```text
P(w_n)=w_ceil(n/2),
tau(w_n)=1+tau(w_ceil(n/2))=ceil(log2 n).
```

This supplies an equality witness for every `n`, not only powers of two.

## Secondary fibre atlas

A comparison word records every adjacent rise and fall.  Its
endpoint-inclusive peak positions are determined without values.  The
adjacent comparisons define a zigzag poset on positions.  To force target
`sigma`, chain the peak positions in increasing order of their ranks in
`sigma`.  Linear extensions then assign the values `1,...,n` bijectively.
Summing over all comparison words with `m` peaks gives the exact fibre over
`sigma in S_m`.

This formula is deliberately secondary.  Ji directly owns static peak
distributions under the exact two-zero boundary convention.  Fu instead
uses a one-sided exterior-peak convention that admits the left endpoint and
excludes the right.  Ordinary
interior pinnacle sets/orders connect only through the explicit padding
`1,(pi_i+2),2`; their fixed-set enumeration and generic linear-extension
machinery receive zero contribution credit.  Run-sorting contributes a
bijective equidistribution, not a pointwise invariant, and also receives zero
credit.

## Evidence and boundary

`verify_p149.py` enumerates all 409,113 permutations through rank 9.  It checks
iterate images through five steps, explicit right sections for every feasible
target through rank 8, recursive sharp witnesses, and every target fibre
through rank 8 by an independent subset-DP linear-extension count.  The
1,228,181 exact assertions are counterexample pressure, not proof or novelty
evidence.

The source search is bounded and cannot establish novelty or priority.  No
public posting, submission, specialist contact, or release is authorized.
