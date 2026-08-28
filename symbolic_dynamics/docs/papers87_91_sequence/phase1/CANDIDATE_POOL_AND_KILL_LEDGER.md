# Papers 87–91 candidate pool and kill ledger

Evidence cutoff: 2026-08-28 UTC. Route: **A / Symbolic Dynamics**.
External release: **HOLD**.

This round again used a two-probe early-signal gate. A candidate survived only
when a small exact calculation exposed a theorem-sized phenomenon and a second
independent probe showed that the phenomenon was structural. Directly owned
systems, close internal lifts, and candidates without a closed theorem after
the second probe were stopped rather than polished. Search absence is recorded
only as `BOUNDED_NO_EXACT_COLLISION_FOUND`, never as a worldwide novelty claim.

## Selected sequence

| ID | Primary dynamical system | Concrete residual advance | Gate |
|---:|---|---|---|
| P87 | nonzero-socle product shifts over finite commutative chain rings | exact valuation decomposition into equal-entropy complete-bipartite components, odd/even mixing transition, full zeta/MME ledger, rank collapse, and recovery of `(q,a)` from four periods | `GO_SHORT_NOTE_WITH_ZERO_DIVISOR_FIREWALL` |
| P88 | finite-field linear parity tree shifts | exact leaf parametrization, normalized tree complexity, iid Bernoulli restriction on every ray, and full-level coordinate-deletion reconstruction of the root | `GO_SHORT_NOTE_WITH_TREE_ENTROPY_FIREWALL` |
| P89 | Bernoulli-reset golden-mean random SFT | Fibonacci regeneration gives closed quenched entropy, annealed exponent, a strict disorder gap, and a renewal CLT with explicit variance | `GO_SHORT_NOTE_WITH_RANDOM_RPF_FIREWALL` |
| P90 | Rule 184 on finite binary rings | density-resolved periodic set, exact worst entry depth `max(0,min(k,n-k)-1)`, particle-weighted temporal fixed polynomial, Möbius orbit census, and temporal zeta | `GO_SHORT_NOTE_WITH_TRAFFIC_OWNER_SUBTRACTION` |
| P91 | generalized-dihedral reverser-relation shifts | a `2N`-state mixing SFT compresses to a cubic quotient plus one repeated eigenvalue; two period counts recover `(N,|A[2]|)` and classify the family | `GO_SHORT_NOTE_WITH_RELATION_GRAPH_FIREWALL` |

The five mechanisms are intentionally separated: a reducible arithmetic
relation SFT, a semigroup tree-SFT, a random Markov cocycle, a conservative
cellular automaton, and a mixing group-relation SFT. P87 and P91 are both
one-dimensional finite-state shifts, but their primary dynamical structures
are opposite: P87 is a disjoint equal-entropy component phase transition,
whereas P91 is primitive and proves two-period group-parameter rigidity.

## Frozen theorem contracts

### P87 — finite-chain-ring socle-product shift

For a chain ring of length `a+1`, residue-field size `q`, and valuation layers
of sizes `w_i=(q-1)q^{a-i}`, the rule `xy in Soc(R)\{0}` is exactly
`v(x)+v(y)=a`. The graph is a disjoint union of complete bipartite components,
and, for even `a`, one full-shift component. Every component has Perron value
`rho=(q-1)q^{a/2}`. The contract includes the complete fixed-count and zeta
formulas, the ergodic MME count, adjacency rank `a+1`, ring-structure collapse
to `(q,a)`, and parameter recovery from `F_1,...,F_4`.

### P88 — finite-field parity tree shift

On the full `d`-ary rooted tree, impose
`x_w=sum_j c_j x_{wj}` with every `c_j` nonzero in `F_q`. Height-`h` blocks
are in bijection with arbitrary level-`h` boundary data, hence number
`q^{d^h}`. Under the compatible uniform measure every ray is iid uniform, yet
the complete level reconstructs the root exactly while every proper subset of
that level is independent of the root. The contract includes the explicit
boundary reconstruction coefficients and normalized complexity rate.

### P89 — Bernoulli-reset golden random SFT

With `A=[[1,1],[1,0]]`, `E=[[1,1],[0,0]]`, and reset probability `p`, the
identity `EA^kE=F_{k+2}E` turns the cocycle into a renewal-reward process. The
contract includes the almost-sure quenched entropy
`p^2 sum_(k>=0)(1-p)^k log F_(k+2)`, the annealed exponent
`log((1+sqrt(5-4p))/2)`, strict inequality for `0<p<1`, and a CLT with the
explicit renewal variance.

### P90 — Rule 184 temporal dynamics

On an `n`-ring with `k` particles, the recurrent set is the no-`11` shift when
`k<=n/2` and its particle-hole no-`00` counterpart when `k>=n/2`. A min-plus
formula for labeled particle positions proves the sharp worst entry time
`max(0,min(k,n-k)-1)`. The contract then derives particle-weighted temporal
fixed counts from cyclic independent sets, specializes to Lucas/gcd counts,
and applies Möbius inversion to obtain every temporal orbit and the finite-map
Artin--Mazur zeta.

### P91 — generalized-dihedral reverser shift

For `G=Dih(A)` and adjacency `g -> h` iff `hgh^{-1}=g^{-1}`, put
`N=|A|`, `t=|A[2]|`, and `c=N/t`. The contract proves mixing, the equitable
quotient

```
[[t, N-t, N],
 [0,   0, N],
 [t,   0, t]],
```

the full characteristic polynomial and zeta, and
`F_1=N+t`, `F_2=t(3N+t)`. These two counts recover `(N,t)`, while an explicit
cosetwise graph isomorphism proves the converse classification.

## Killed or reserved candidates

| Candidate | Decision | Reason |
|---|---|---|
| rectangular rowmotion on `J([a]x[b])` | `KILL_DIRECT_OWNER` | Striker–Williams and related rowmotion work already give the equivariant binary-word rotation model; fixed counts and zeta are necklace corollaries |
| Černý nonreset survivor shift | `KILL_DIRECT_OWNER` | the pair automaton and its `binom(n,2)` compression are explicit in synchronization work, while Protasov's two-point operator already owns the exponential nonreset rate |
| coprime divisor tensor SFT | `KILL_DIRECT_OWNER_2026` | arXiv:2605.04849 gives the same Kronecker factorization and local eigenvalues |
| characteristic-three Ledrappier resonance | `RESERVE_OWNER_HEAVY` | the finite-torus gcd formula is strong, but the diagonal resonance is too close to established algebraic `Z^2`-action periodic theory and P67/P70 |
| three-window distinct-count hidden process | `RESERVE_INTERNAL_P86` | its plastic-constant support and infinite-memory formula are exact, but the finite-dependence/infinite-Markov narrative is too close to P86 for immediate reuse |
| periodic free/golden schedule | `RESERVE_INTERNAL_P85` | Fibonacci gap products are exact but the system is a near neighbor of P85's periodic nonautonomous normal form |
| Paley increment shift | `KILL_INTERNAL_P84` | standard Gauss-sum Cayley spectrum plus a direct collision with P84 |
| generalized Thue–Morse / valuation Toeplitz candidates | `KILL_OWNER_AND_INTERNAL` | direct substitution/complexity owners and collisions with P50/P54/P73/P77 |
| finite-field bilinear-one relation shift | `KILL_INTERNAL_P81` | a finite incidence analogue of the compact orthogonality relation already used in P81 |

## Two-probe evidence

- P87: valuation-layer SCCs, rank, periods through 10, and nonisomorphic ring
  collapse were checked on small residue realizations.
- P88: all legal blocks and all boundary marginals were enumerated at small
  `(q,d,h)`; full-level reconstruction and proper-subset independence both
  appeared exactly.
- P89: the Fibonacci sandwich identity was checked to gap 50, then complete
  environment words were enumerated independently of matrix products.
- P90: every state on rings through the feasible exhaustive cutoff was placed
  in its functional graph; the sharp depth and Lucas/gcd fixed count appeared
  before the min-plus proof was frozen.
- P91: several nonisomorphic abelian groups with equal `(N,t)` gave identical
  graphs, while all nonzero spectral data collapsed to a cubic quotient and a
  repeated eigenvalue.

## Release boundary

All five selections are internal theorem contracts. Public posting,
submission, author contact, venue selection, specialist priority clearance,
and absolute novelty language remain unauthorized and `HOLD`.
