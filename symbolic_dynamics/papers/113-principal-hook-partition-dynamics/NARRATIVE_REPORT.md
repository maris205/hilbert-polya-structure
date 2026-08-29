# Narrative report

## What the system does

Draw the Ferrers diagram of an integer partition and look at the hooks rooted
on its main diagonal. Their lengths form another partition of the same
integer. Repeating this regrouping gives a finite deterministic orbit.

The one-step combinatorics is owned background. Gutschwager directly defines
the principal-hook length partition and records its first-hook identity;
Goupil gives the adjacent-gap image and exact product fibre; Chern--Yee give
direct prior work on diagonal-hook data and a hook-preserving involution.
Those statements, standard one-step symmetries, and the usual Frobenius setup
receive zero credit here.

## Why every orbit collapses

The first principal hook contains the whole first row and first column. Its
length is therefore

```text
lambda_1 + ell(lambda) - 1.
```

Unless the diagram already has one row, this is strictly larger than the old
first row. The first part is bounded above by `n`, so every orbit must end at
the one-row partition `(n)`. Thus `(n)` is globally absorbing in the precise
finite-time sense that every state reaches it; it is also the unique fixed
and periodic point. The identity itself is Gutschwager-owned, so these are
recorded only as low-credit dynamical consequences.

## The temporal statistic

The useful progress variable is the first adjacent gap
`g=lambda_1-lambda_2`. When the Durfee square has size at least two, direct
subtraction of the first two hook lengths gives

```text
g(H lambda)-g(lambda)
  = ell(lambda)-lambda'_2+2
  = 2+m_1(lambda).
```

Thus every nonterminal step gains at least two. In Durfee size one, the
partition is `(a,1^b)` and collapses immediately to `(n)`; the final gap gain
is exactly `b+1`, again at least two. Because the terminal gap is `n`, the
number of remaining steps is at most `floor((n-g)/2)`.

This bound is globally exact. Starting with the balanced two-row diagram, a
two-row update moves one cell from the second row into the first:

```text
(a,b) -> (a+1,b-1).
```

For `n>=2` and `b=floor(n/2)`, this two-row formula is used `b-1` times (zero
when `b=1`), reaching `(n-1,1)`. One final principal-hook step reaches `(n)`,
for exactly `b` steps in total. At `n=1`, `(1)` is already terminal. Exact gap
growth plus this sharp infinite family form the paper's sole main theorem.

## Counting temporal layers

The fixed layer contains only `(n)`. The fibre over `(n)` has `n` diagrams,
one of which is already fixed, so the depth-one layer has size `n-1`. At all
later depths, a state has depth `t` exactly when its first image has depth
`t-1`. Summing the owned product fibre weight over all eligible first images
gives an exact depth-state-weighted transport identity for every layer. Its
right side still needs the depths of individual image states, so it is not a
closed scalar recurrence in the layer sizes.

This division of labor is important: the fibre weights receive zero credit,
the layer transport is low credit, and only the gap calculation with its
sharp depth is promoted to the main theorem. No external originality
conclusion is drawn while owner status remains HOLD.

## Conjugation and periodic data

Conjugating a Ferrers diagram swaps every Frobenius arm with its corresponding
leg. Hook lengths therefore do not change, so conjugate partitions have the
same image and the same orbit after time one. Their entrance depths agree too,
except for `(n)` and its conjugate `(1^n)` when `n>1`: the former starts at
the globally absorbing fixed point and the latter reaches it in one step.

For each fixed weight `n>=1`, write `H_n` for the finite self-map on `P(n)`.
Since `(n)` is its sole periodic point, every iterate has exactly one fixed
point and `zeta_{H_n}(z)=(1-z)^(-1)`. No zeta function on the disjoint union
of all weights is meant.

## Boundaries and controls

The paper's statements explicitly include `n=1` and `n=2`; empty products
are one and empty layer-transport sums are zero. Exact enumeration through `n=40`
checks every formula and kills three stronger but false guesses:

- the map is not idempotent;
- depth is not unconditionally invariant under conjugation;
- a naive rectangular-boundary condition does not characterize deepest
  states.

The verifier contributes falsification evidence only; every result has a
symbolic proof in the manuscript.

## Ownership and firewall status

The direct owners for the map/first-hook, image/fibre, and diagonal-hook
background are cited and itemized; those claims receive zero credit. A
bounded search found no exact temporal owner, but a missing search result is
not novelty evidence. P110 is separated at the level of state space and
mechanism: P113 has unlabelled integer partitions and diagonal-hook regrouping, whereas
P110 has labelled set partitions, a cyclic action, and a lattice join.
External dissemination, novelty, and priority remain **HOLD**.
