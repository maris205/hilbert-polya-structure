# Paper 35 preregistration — affine semigroup object firewall

## 1. Candidate

Candidate `SD-C37` is the composite-baseline two-generator affine monoid

```text
P_4=<u,v | vu=u^4 v>^+,
```

together with its positive right Cayley graph, formal symmetrization, and
Hashimoto edge graph. The full `N_0 semidirect N^times` source and the
Bost--Connes diagonal Gibbs operator are comparison objects.

## 2. Freeze order

This file and `SOURCE_LOCK.md` precede canonical authority outputs. Candidate
generation and post-source evaluation must be physically separated. All
canonical results are generated twice in cleared directories before freezing.

## 3. Exact experiments

### E1 — positive height

For `r=2,3,4,5` and frozen finite boxes, enumerate all retained U/V edges and
verify strict increase of `h_r(b,k)=b+r^k`. Record that the finite box is a
proxy; the infinite DAG statement is proved.

### E2 — symmetrized backtracks

Add formal reverse edges and enumerate primitive cyclic words through the
frozen word cutoff. Verify one two-step backtrack class per unoriented edge.

### E3 — Hashimoto relation cycles

Forbid immediate reversal, including at the cyclic join. Verify that
`vuv^{-1}u^{-r}` is reduced, primitive, closed, and of length `r+3`. Enumerate
short reduced classes and separate affine relation cycles from generic
cycles.

### E4 — operator windows

Build exact finite windows of the positive, symmetrized, and Hashimoto
operators. Verify bounded-degree norm bounds and construct orthogonal local
witnesses whose image norms are uniformly nonzero. Finite singular values are
reported only as diagnostics; noncompactness is theorem-level.

### E5 — finite quotients

For frozen moduli, reconstruct affine generator maps, the labeled relation
word, the additional translation cycle `U_q^q`, and small-modulus polygon
degenerations. The predeclared success is relation preservation together with
ledger nonfaithfulness, not quotient equality.

### E6 — diagonal partition trace firewall

For finite arithmetic cutoffs and exact symbolic coefficients, compare
`Tr(D_beta)`, coefficients of `-log det(I-zD_beta)`, and the list
`zeta(m beta)/m`. Verify that the first coefficient is the partition trace and
higher coefficients are not repetitions of the same scalar.

### E7 — bosonic marker firewall

At finite prime-basis fixtures, compare the one-particle determinant at free
fugacity `z` with its `z=1` Euler specialization. Record the prime-seeded basis
as a control, never as source emergence.

### E8 — arbitrary-presentation controls

Repeat relation-cycle and marker gates on composite, mutated, and relabeled
affine presentations. A mechanism that survives them is `PROVES_TOO_MUCH`.

### E9 — signed/matrix boundaries

Include exact nilpotent or orthogonal cancellations showing why positive
ordinary path semantics is essential. These controls do not refute the
literal relation-cycle census.

## 4. Source separation

The candidate core must not contain identifiers or imports for primality,
factorization support, target zeros, fitted coefficients, or accepted labels.
The evaluator may attach descriptive labels only after serialized neutral
artifacts exist and must independently recompute every decisive identity.

## 5. Stop rules

- If the positive graph has a nonempty directed cycle, stop and repair the
  height/source claim.
- If Hashimoto reduction removes the affine relation word, inspect cyclic
  join conventions before any conclusion.
- If a finite quotient is described as ledger-faithful despite `U_q^q`, stop.
- If `zeta(beta)` is called a graph determinant rather than a first trace
  coefficient, stop.
- If the bosonic prime basis is presented as prime discovery, stop.
- If any result uses target-zero data or Route B, invalidate the candidate.

## 6. Frozen Route outcome

```text
(A0_STRUCTURAL_ARITHMETIC_RELATION,
 A1_FAIL,
 A2_FAIL,
 A3_FAIL,
 A4_FAIL)

overall: ROUTE_A_REJECTED
route_b_invocation_allowed: false
```

All target-zero and root metrics in the Route artifact must be literal
`not_applicable; ...` strings. Before the first artifact commit, all three
provenance fields are `PENDING_FIRST_ARTIFACT_COMMIT`; a metadata-only second
stage seals them to the same lowercase 40-hex artifact commit.
