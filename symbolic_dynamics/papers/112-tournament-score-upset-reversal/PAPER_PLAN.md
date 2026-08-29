# P112 paper plan — synchronous tournament score-upset reversal

Status: **PROVABLE AS REPAIRED / ANONYMOUS WORKING MANUSCRIPT / EXTERNAL HOLD**.

## One-sentence contribution

For the specified synchronous orientation-valued self-map, the residual
scope is only the conjunction of its simultaneous Lyapunov identity,
permanent equal-score-block factorization, exact recursive pointwise depth,
universal non-sharp bound, and map-specific fixed-set identification.

## Frozen claim boundary

The paper may claim only:

1. the arbitrary-label-set update, its simultaneous incidence formula, the
   local fixed criterion, exact quadratic-energy increment, and absence of
   nontrivial cycles;
2. the equal-score ordinal-sum image and all-iterate recursive factorization;
3. pointwise depth equal to recursive refinement-tree height and `tau <= n-1`
   for `n >= 1`, with `n=0,1` handled separately;
4. fixed tournaments equal unique ordered sums of regular tournaments;
5. as explicitly zero/low-credit corollaries, the fixed recurrence,
   exponential generating function, regular counts, and one-factor zeta;
6. under the stated increasing-order then increasing-numeric-mask scan,
   mask `148` is the least nonidempotent state through `n=6`.

The paper must not claim a sharp global depth formula, a complete transient
enumerator, absolute novelty, priority, or external owner clearance.

## Proof feasibility and dependency map

Proof status: **PROVABLE AS STATED**.

1. The energy theorem expands squared scores after first writing each score
   change as the signed incidence count of all simultaneously reversed arcs.
2. The factorization theorem depends on ordering old score classes and on the
   disjoint intervals `[L_i,L_i+|C_i|-1]` after one update.
3. A one-score-class tournament is fixed, so every expanded node has at least
   two smaller nonempty children and the tree is well-founded.  Restricting
   two consecutive global iterates to each frozen block proves the
   stabilization equivalence and exact `tau` recursion in both directions.
   The `n-1` bound then follows by induction.
4. Fixed classification uses uniform external wins within a score class in
   one direction and strictly separated regular-block scores in the other.
5. The recurrence chooses the unique top regular block; the standard labelled
   sequence construction gives `F(x)=1/(1-R(x))`.  Both are low-credit.
6. The zero-credit zeta formula uses the energy theorem to identify every
   periodic point with a fixed point.

The two termination routes are materially different: energy compares
successive global score vectors, while recursive factorization terminates by
induction on induced block size and simultaneously computes pointwise depth.

## Section plan

1. Introduction: specified rule, exact conjunction, strict subtraction, HOLD.
2. Definition and energy: exact update, Lyapunov identity, recurrence exclusion.
3. Equal-score blocks: ordinal sum, disjoint intervals, recursive iterates,
   tree height, `n-1` bound.
4. Fixed enumeration: map-specific fixed set, low-credit recurrence/EGF/zeta,
   and boundaries.
5. Controls and scope: exact lanes, scan-qualified nonidempotence, mechanics
   comparison, itemized zero-credit ledger, P106 firewall, explicit nonclaims.
6. Conclusion: one concise synthesis without adding claims.

No figure is needed; the defining formula, recursion, and compact exact table
carry the full argument.

## Citation and credit boundary

- Landau owns the classical score-sequence theorem; Moon owns the standard
  tournament, regular-tournament, ordinal-sum, and Ryser-lineage background.
- Rubinstein and Henriet own static points ranking/Copeland-choice neighbors.
- Bouyssou owns ranking by successive choice on shrinking sets; Linares
  Lejarraga--Bodanza own the current “Iterative Copeland from below” usage.
- Ryser and Thomassen own direct triangle/arc-reversal neighborhoods; Ghosh
  et al. (ESA 2026) are the verified contemporary score-sequence/cycle-reversal
  neighbor.
- McKay is a direct regular-tournament enumeration owner; Flajolet--Sedgewick
  own generic labelled-EGF bookkeeping; Artin--Mazur own dynamical zeta.
- Monsuur owns mature upset/backward-edge inconsistency language.

All listed material receives zero contribution credit.  The bounded search
miss is not novelty or priority evidence, and the residual conjunction remains
owner-HOLD.
