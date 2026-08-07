# Frozen experiment plan: HCS-C15

## Candidate contract

- **base dynamics:** nonbacktracking shift on a finite directed-edge graph;
- **voltage data:** inverse-compatible map from oriented edges to a finite
  group \(G\);
- **resolved twist:** a constant finite-dimensional unitary representation
  \(\rho\);
- **clock:** positive finite-memory, locally constant edge or transition roofs
  \(\tau_j\);
- **determinant:**

  \[
  D_\rho(s)=\det(I-B_\rho(s)),\qquad
  B_\rho(s)=\sum_{j=1}^r e^{-s\tau_j}B_{\rho,j};
  \]

- **canonical aggregate:**

  \[
  Z_{\rm new}=Z_Y/Z_X
  =\prod_{\rho\ne\mathbf1}L(s,\rho)^{\dim\rho};
  \]

- **tower control:** \(H(\mathbb Z/3^m\mathbb Z)\) with generators
  \(x^{\pm1},y^{\pm1}\);
- **normalization:** no fitted spectral rescaling and no imported zero data;
- **forbidden replacement:** no chronological product may be replaced by a
  symbol average or an empirical transition matrix.

## Claims and kill conditions

| Claim | Required evidence | Falsifier |
|---|---|---|
| C1 Artin factorization control | exact D4 regular-cover determinant equals the irrep product with regular multiplicities | any coefficient mismatch |
| C2 order-only aggregate | regular multiplication by an order-\(o\) holonomy has \(|G|/o\) cycles of length \(o\) | the frozen canonical aggregate depends on more than \(o\) |
| C3 chronology witness | equal cyclic bigram ledgers, non-dihedral primitive words, distinct central holonomy | words are equivalent, imprimitive, or give equal/inverse holonomy |
| C4 resolved observability | a fixed nontrivial central character gives distinct phases | every resolved sector gives the same determinant |
| C5 finite-roof density | determinant is a finite exponential polynomial and Jensen gives \(O(T)\) zeros | an allowed coefficient hides extra \(s\)-dependence or infinitely many roofs |
| C6 Riemann mismatch | compare C5 with Riemann--von Mangoldt \(\Theta(T\log T)\) | a moving truncation is silently substituted for a fixed determinant |
| C7 tower branch return | exact-conductor abelian and primitive Schrödinger eigenvalues tend to four | the sectors factor through a lower level or stay uniformly Ramanujan |

## Mandatory controls

1. **Full regular-cover control.** Compute the D4 cover directly rather than
   assuming representation factorization in code.
2. **Representation-multiplicity control.** Use each Artin factor with
   exponent \(\dim\rho\); aggregation once per irrep is a different object.
3. **Chronology control.** Match every directed bigram count, not only the
   Parikh vector, while retaining exact ordered multiplication.
4. **Time-reversal control.** Reject cyclic shifts and rotations of the
   inverse word.
5. **Noncommensurate-roof control.** Prove the exponential-type bound for an
   arbitrary finite positive roof alphabet; do not rely only on lattice
   periodicity.
6. **Independent implementation.** Verify the Heisenberg collapse by
   regular-permutation cycle decomposition and the level-nine character by
   direct application of adjacency.
7. **Tower-scope control.** Distinguish trivial-only subtraction, deletion of
   all abelian sectors, and an actual infinite determinant.

## Stopping rule

Close HCS-C15 once the following dichotomy is rigorous:

- aggregate all nontrivial sectors canonically and lose conjugacy-level
  holonomy;
- retain any fixed finite ledger and fail the Riemann zero-count law;
- take the natural amenable Heisenberg congruence tower and recover branching
  poles even in primitive nonabelian sectors.

Do not optimize finite-group parameters after this gate. The next system must
change at least one structural premise: use a nonamenable arithmetic joint
flow, an infinite non-finite-type transfer operator, or a genuinely
non-locally-constant roof with a proved determinant.
