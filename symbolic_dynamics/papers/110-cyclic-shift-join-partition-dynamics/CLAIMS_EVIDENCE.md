# Claims and evidence — P110

Status: **CROSS-HOSTILE A/B PASS / FINAL MECHANICAL QA PASS / EXTERNAL
HOLD**.

## Proof status

All theorem statements in `main.tex`, including the complete deepest-shell
classification, have status **PROVABLE AS STATED** under the definitions in
the manuscript.  No theorem relies on the finite computation.

| Claim | Infinite-family proof route | Independent exact control |
|---|---|---|
| consecutive-orbit iterate `J^t(pi)=join_{j=0}^t rho^j(pi)` | induction using that rotation is a lattice automorphism | literal one-step iteration compared at every time with a separately accumulated join and an independently constructed translated graph |
| endpoint is the coset partition of `H(pi)` | all translated block edges have difference in `H(pi)`; translated generators connect each full coset | endpoint compared with a separately built residue/coset partition for every state through `n=10` |
| fixed and recurrent states are the cyclic block systems | fixedness forces rotation invariance; the block of zero is a subgroup; monotone coarsening excludes nontrivial cycles | all literal fixed states counted and compared with the divisor count in every exhaustive lane |
| `Fix(J^r)=tau(n)` and `zeta=(1-z)^(-tau(n))` | every recurrent point is fixed; temporal Möbius inversion and the Artin–Mazur definition | temporal Möbius and formal-series coefficient recurrences checked through period 60 |
| endpoint-subgroup basin `sum_{d|h} mu(h/d) B_d^(n/d)` | partitions below the order-`h` coset partition factor into `n/h` independent Bell choices; divisor inversion isolates exact subgroup | every literal basin through `n=10`; independent divisor convolutions and total-basin identities through `n=50` |
| sharp upper depth `n-2` | each chord-translate orbit is a union of cycles; omitting one translate leaves every component connected | literal maximum in every exhaustive lane |
| depth `n-2` iff the state is a primitive-chord atom | a component cut at time `n-3` makes all initial chords admissible; nonprimitive chords create forbidden periods, while a primitive chord has exactly two defects and is uniquely recovered by the cut | checked state by state for all 142,417 partitions through `n=10`; a separate lane exhausts every nonconstant binary cut through `n=12` and checks the defect/stabilizer/uniqueness lemma directly |
| deepest-shell size `n*phi(n)/2` | choose a base vertex and a unit difference, then divide the oriented count by two | exact deepest counts `3,4,10,6,21,16,27,20` for `n=3,...,10` |
| transient recovery of `n` | for `n>=3`, `n=max_depth+2`; phase sizes distinguish `n=1,2` | all endpoint conventions included in the exhaustive lanes |

## Two proof routes

### Route A — semilattice and cyclic subgroup incidence

This route proves the iterate formula, subgroup-coset endpoint, recurrence,
zeta, and Möbius–Bell basins.  Its counting step is a divisor-lattice
inversion of `B_h^(n/h)`.

### Route B — translated graphs and binary cut defects

This route realizes joins as graph components.  One missing translate from
each chord orbit is redundant.  If two translates are missing and a terminal
component is still split, its indicator supplies a binary cut.  Defect parity
on translation cycles eliminates every nonprimitive chord unless it is a
true period of the cut; a primitive chord leaves exactly two boundary edges,
has a trivial cut stabilizer, and is uniquely reconstructed.  Therefore a
deepest partition contains exactly that one chord.

The routes share only the definition of the map.  Route A does not prove the
sharp-time classification, and Route B does not use the Bell/Möbius basin
enumeration.

## Owner-subtracted boundary

- Standard partition-lattice joins, Bell numbers, and elementary divisor
  inversion are background, not claimed contributions.
- Invariant partitions as permutation block systems and structural lattices
  of invariant partitions are assigned to their direct literature.
- Orbit-coherence work is cited for joins and meets among orbit partitions;
  it is not presented as evidence of novelty for the temporal map.
- The Artin–Mazur zeta definition is positively attributed.
- The least invariant coarsening obtained by joining translates, the cyclic
  coset classification of invariant partitions, and the
  join/generated-subgroup mechanism are background and receive no standalone
  contribution credit.  The residual scope begins only with the bounded
  temporal conjunction of basin and sharp-depth formulas.

The paper does not claim absolute novelty, exhaustive literature clearance,
or priority.  External release remains **HOLD**.

Internally, P97 acts on subsets by nonlinear sumset squaring and P105 acts on
labelled permutations by cycle-minimum pruning.  Within P107--P111, P107 acts
on residue-ring ideals, P108 on a capped integer square, P109 on finite-field
subspaces, and P111 on random positive Heisenberg products.  P110 acts on set
partitions by a join with a cyclic relabelling.  These differ at both
phase-space and update-rule level; common Bell, cyclic, Möbius, transient-time,
and zeta ingredients are explicitly noncredit-bearing.
