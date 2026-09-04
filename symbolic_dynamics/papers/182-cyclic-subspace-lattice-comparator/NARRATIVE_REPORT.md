# P182 narrative report — cyclic subspace-lattice comparator

**Round:** author Round 0  
**Owner gate:** `OWNER_AMBER`  
**External lifecycle:** `HOLD_EXTERNAL`

## One-sentence contribution

The cyclic rule `(A,B,C) -> (C,A∩B,A+B)` has the universal lattice identity
`T^4=T^2`, and on triples of subspaces of `F_q^d` it admits a complete
two-axis functional-graph census and an every-target predecessor formula in
terms of ordered complementary subspaces.

## Why this system is worth isolating

Meet and join usually suggest monotone sorting.  Cycling a third register
breaks that intuition: the rule retains a genuine period-two core while still
collapsing every tail in two steps.  The temporal collapse uses only lattice
absorption.  The fibre law appears only after specializing to the modular
subspace lattice, where a target interval `M<=J` turns each predecessor into
an ordered direct-sum decomposition of `J/M`.

That separation gives the paper two independent theorem spines:

1. a universal finite-lattice temporal theorem, including the exact recurrent
   set and period-two action;
2. a finite-field enumeration theorem over every prime power `q` and every
   dimension `d`, including image, cycles, all depth populations, every
   target fibre, the fibre histogram, and the sharp maximum.

## Strongest exact statements

Let `g_n(q)` be the number of subspaces of `F_q^n`.  For the subspace lattice
`L_d(q)`:

- the image consists exactly of `(C,M,J)` with `M<=J`;
- recurrent states are exactly `(A,B,C)` with `B<=A,C`, and the map swaps
  `A,C` there;
- the fixed and recurrent populations are Gaussian-binomial sums
  `alpha_d(q)` and `rho_d(q)`;
- depth is 0 on the recurrent core, 1 exactly when `A∩B<=C` outside it, and
  2 otherwise;
- a target `(C,M,J)` has no predecessor when `M` is not contained in `J`; if
  it is, its fibre has size
  `kappa_k(q)=sum_a [k choose a]_q q^{a(k-a)}` for `k=dim(J/M)`;
- the maximum fibre is `kappa_d(q)` and occurs at exactly the `g_d(q)`
  targets `(C,0,V)`.

## Falsification evidence

The paper-local standard-library verifier enumerates all subspaces in
canonical reduced row-echelon form, constructs the literal transition graph,
and checks the theorem target by target.  Its frozen box contains 15 cases:
`q=2,d=0..4`, `q=3,d=0..3`, and `q=5,7,d=0..2`.  It checks 328,700 transitions
with 1,667,850 explicit assertions.  At `(q,d)=(2,4)`, the carrier has 300,763
states, 513 fixed points, 4,376 strict two-cycles, and depths
`9265,157272,134226`.

Enumeration is not used as the all-parameter proof and supplies no owner or
novelty evidence.

## Collision subtraction and selection record

The retained claim excludes generic lattice axioms, Gaussian coefficients,
standard complement counts, monotone meet/join folds, linear/Jordan operator
dynamics, and generic finite-map bookkeeping.  The closest internal
alternative, NFIT, acts on matrices by a nonsingularity-triggered translation
and counts linear derangements.  Its pair reduction is shallower and directly
owned by linear-derangement machinery; it does not yield the comparator's
universal lattice identity or quotient-complement fibres.  The Lie-derived
subspace system is held in reserve.  The transpose-commutator collapse was
killed as a P175 transfer.

## Owner and lifecycle boundary

Verified sources own lattice theory, finite-vector-space enumeration,
subspace complements, Hibi meet/join sorting, and pop operators on lattices.
A bounded exact-rule search found no source for the complete conjunction, but
that non-hit is not a novelty claim.  The paper remains
`OWNER_AMBER / HOLD_EXTERNAL` pending database-level owner search and
independent mathematical review.

