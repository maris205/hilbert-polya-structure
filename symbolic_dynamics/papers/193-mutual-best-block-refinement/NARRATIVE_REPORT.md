# Narrative report — P193 mutual-best block refinement

## Status and scope

`PASS_INTERNAL / OWNER_AMBER / HOLD_EXTERNAL`

The carrier is the symmetric group in one-line notation.  The update is
deterministic and simultaneous: a left position chooses the smallest value
among its later smaller entries, a right value chooses the earliest position
among its earlier larger entries, and every mutual choice swaps.  No random
kernel or asynchronous scheduler is present.

## Problem anchor

The local nomination rule initially looks like a matching-market process.
Its exact structural content is different and much simpler to state: the
selected pairs are precisely the first entry and minimum of every current
non-singleton direct-sum indecomposable block.  This reformulation is not a
quotient of the dynamics; it identifies the literal pairs before any update.

The paper asks four complete questions.

1. Which pairs exchange, and why can all exchanges be made simultaneously?
2. What is the exact absorption time of each permutation and the sharp global
   maximum?
3. How many states occupy every transient layer?
4. For each labelled target, what is its complete one-step fibre?

## Main deductive spine

### Block normal form

An active inversion cannot cross a direct-sum cut.  Inside an indecomposable
block, the first entry and the minimum mutually nominate.  If another pair
`(i,j)` with lower value `b` were active, then the positions before `i` would
be exactly the values `1,...,b-1`, producing a forbidden sum cut.  Thus every
nontrivial block has exactly one active pair.

### Temporal axis

Exchanging the first entry and minimum of an indecomposable block produces
`1 direct-sum gamma`.  Therefore the direct-sum component count strictly
increases at every nonfixed epoch.  The identity is the unique recurrent
state.

The pointwise clock is recursive.  A direct sum takes the maximum of the
component clocks.  An indecomposable block has clock one plus the clock of
the suffix `gamma` exposed after the exchange.  This selection-decomposition
height is exactly the orbit tail, not merely an upper bound.

Induction yields maximum tail `n-1`; `(2,3,...,n,1)` realizes the bound.
Deepest states must be indecomposable, and the image suffix must itself be
deepest.  Every deepest suffix of size `n-1` has exactly `n-1`
indecomposable parents, so the deepest population obeys
`d_n=(n-1)d_(n-1)` and equals `(n-1)!`.

### Layer axis

Let `A_t` count all permutations of depth at most `t`, and `B_t` count only
indecomposable ones, by ordinary size generating functions.  Unique
direct-sum factorization gives `A_t=1/(1-B_t)`.  To build an indecomposable
state of depth at most `t+1`, take an arbitrary depth-`t` prefix sequence,
mark one position in its final indecomposable component, and insert a new
leading minimum.  Hence

```text
B_0 = x,
B_(t+1) = x + x^2 A_t B_t'.
```

Coefficient differences `A_t-A_(t-1)` give exact layers.

### Inverse axis

For `gamma`, the indecomposable parents of `1 direct-sum gamma` correspond
exactly to the positions in the last direct-sum component of `gamma`.
For a general target, group consecutive target components into old source
blocks.  Every group must start at a singleton component, and a group ending
at a component of size `c` has `c` parents.  Summing over optional group
boundaries factors, giving

```text
c_s * product over j>=2 with c_j=1 of (1+c_(j-1)).
```

The support condition is `c_1=1`, equivalently first target entry `1`.
The product is at most `2^(n-1)`, with equality only when every component is
a singleton, so the identity uniquely maximizes the fibre.

## Evidence discipline

The paper-local verifier enumerates every permutation through `S_9`.  It
checks literal/structural pair equality, every pointwise clock, every target
fibre, exact layer-recurrence coefficients, image support, sharp extrema, and
fibre mass.  Its transition digest is deterministic.  None of this finite
work substitutes for the all-parameter proofs.

## Zero-credit and collision boundary

- common-master stable matching and inversion/blocking-pair language;
- direct sums and unique indecomposable factorization;
- generic monotone Lyapunov arguments, formal-series algebra, and finite-map
  fibre mass;
- P105's cycle-minimum pruning clock;
- P122's parity-selected record-block reversal;
- P155/P156's rank-changing extraction rules;
- P181's single first-descent prefix reversal and depth-two recurrent core.

P193 is not P181: on `132`, P193 returns `123`, while P181 reverses the first
three entries and returns `231`.  P193 has a strictly refining block count and
one absorber; P181 has a half-image and nontrivial two-cycles.  These local
differences establish internal nonidentity, not external ownership.

## Open boundary

No claim is made for a nonrecursive closed form for all depth layers,
all-time target fibres, limiting laws, or an external owner search.  A direct
owner under terminology such as parallel selection sorting or component
decomposition sorting would require withdrawal or repositioning.  The
artifact remains `OWNER_AMBER/HOLD_EXTERNAL`.
