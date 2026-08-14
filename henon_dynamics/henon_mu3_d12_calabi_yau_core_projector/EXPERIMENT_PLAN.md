# HCS-C52 reproducible experiment plan

Status: **B0--B2 experiment completed; release scope frozen**

## Experiment objective

The experiment must independently certify one amber theorem package:

\[
 \text{source lock}
 \longrightarrow
 \operatorname{Dih}(C_{12})\text{ monomial group}
 \longrightarrow
 \text{middle Chow projectors}
 \longrightarrow
 10+158\text{ Hodge split}
 \longrightarrow
 \mathbf Q[G]\text{ optimum}.
\]

It must not attempt a projected Frobenius polynomial or an incidence
correspondence outside the graph algebra.  Those are C53 tasks.

## B0. Source and model lock

### Inputs

- Frozen C47--C51 certificates and payloads, with hashes read directly from
  the repository by the released producer rather than copied from this
  planning file.
- The inherited field \(K=\mathbf Q(\rho)\).
- The exact cubic and chronological quadric.
- The C50 characteristic-zero smoothness certificate and C51 Hodge/twist
  ledger.

### Replay

1. Verify every inherited certificate and payload hash.
2. Reconstruct
   \[
   C=\sum_{i=0}^{7}x_i^3,
   \qquad
   Q=\sum_{i=0}^{6}x_ix_{i+1}+\rho x_7x_0.
   \]
3. Verify \(\rho^2+\rho+1=0\), \(\dim X=5\), \(\deg X=6\), and the
   declared smoothness scope.
4. Recompute the C51 source ledger
   \[
   \dim H^5(X)=168,
   \qquad
   h^{4,1}=1,
   \qquad
   h^{3,2}=83.
   \]
5. Reject any deletion, rescaling, or chronology-averaging of the terminal
   \(\rho x_7x_0\) edge.

### Decision

- **PASS:** all equations, hashes, dimensions, and normalizations agree.
- **FAIL:** stop without changing inherited artifacts.

## B1. Projective monomial group

### Enumeration

Represent a map by \((\sigma,e)\), where

\[
 x_i\longmapsto \rho^{e_i}x_{\sigma(i)},
 \qquad e_i\in\mathbf F_3,
\]

and quotient by a common phase.  Enumerate cycle-graph permutations and
phase choices, retaining exactly those for which

\[
 C(gx)=C(x),
 \qquad
 Q(gx)=\lambda_gQ(x)
\]

for some \(\lambda_g\in\mu_3\).

### Required outputs

- Exactly 24 distinct projective maps.
- Complete multiplication and inverse tables.
- Explicit generators satisfying
  \[
  r^{12}=s^2=1,
  \qquad srs=r^{-1}.
  \]
- Element-order histogram
  \[
  1^1,\ 2^{13},\ 3^2,\ 4^2,\ 6^2,\ 12^4.
  \]
- Graph-transpose identity
  \([\Gamma_g]^t=[\Gamma_{g^{-1}}]\).

### Negative controls

- Delete the closing edge.
- Replace \(\rho\) by an unrelated scalar.
- Alter one phase exponent.
- Admit a common scalar twice instead of quotienting projectively.
- Test a forbidden odd rotation or even reflection.

Each mutation must change the relevant semantic gate from PASS to FAIL,
not terminate with an unclassified error.

## B1. Middle Chow--Künneth controls

Reconstruct

\[
 \pi_{2i}=\frac1{6}h^{5-i}\times h^i,
 \quad 0\le i\le5,
 \qquad
 \pi_5=\Delta_X-\sum_{i=0}^{5}\pi_{2i}.
\]

Verify symbolically:

1. \(\int_Xh^5=6\);
2. the six \(\pi_{2i}\) are mutually orthogonal idempotents;
3. every graph correspondence commutes with \(\pi_5\);
4. \(e_G^2=e_G=e_G^t\);
5. \(\pi_{\mathrm{core}}=\pi_5e_G\) and
   \(\pi_{\mathrm{lev}}=\pi_5-\pi_5e_G\) are mutually orthogonal
   self-transpose Chow idempotents.

The checker must reject the replacement
\(\pi_{\mathrm{core}}=e_G\), because that object retains ambient Tate
classes and does not have middle rank 10.

## B2. Exact Cayley-ring representation

### Producer route

1. Work over exact \(\mathbf Q[\rho]/(\rho^2+\rho+1)\).
2. Form
   \[
   \mathscr F=yC+zQ,
   \qquad
   R=K[x_0,\ldots,x_7,y,z]/J(\mathscr F).
   \]
3. Compute fixed-term-order bases for \(R_{1,-3}\) and
   \(R_{2,-3}\).
4. Record the ambient bidegree basis, relation matrix, pivots, quotient
   basis, and exact dimension.
5. For every group element, build the residue-twisted action using
   \(\det(M_g)/\det(A_g)\).

### Independent checker route

The producer uses custom exact pair arithmetic and dense RREF.  The checker
rebuilds the finite bidegree vector spaces and relation matrices with an
independent SymPy `DomainMatrix` over a separately constructed
\(\mathbf Q(\rho)\).  It must not consume the producer's pivot or quotient
basis as a proof transcript.

### Mandatory equalities

\[
 \dim R_{1,-3}=1,
 \qquad
 \dim R_{2,-3}=83.
\]

For a fixed presentation \(G=\langle r,s\rangle\), require

\[
 \operatorname{tr}(r^k)
 =(83,-1,-3,-1,-7,-1,3,-1,-7,-1,-3,-1),
\]

\[
 \operatorname{tr}(sr^k)=3.
\]

Character inner products must give

\[
 (4,1,3,3)
 \quad\text{and}\quad
 (7,8,6,8,7)
\]

for the one- and two-dimensional complex irreducibles, respectively.  The
checker independently verifies integer multiplicities and total dimension
83.  It also proves that the one-dimensional \(H^{4,1}\) generator is the
trivial representation.

### Scalar-lift control

Replace one \(M_g\) by a scalar multiple representing the same projective
map.  The residue-twisted action must remain unchanged.  Removing the
orientation multiplier must fail this test.

## B2. Projector ranks and optimum theorem

From the trivial multiplicities, independently reconstruct

\[
 \operatorname{rank}\pi_{\mathrm{core}}=1+4+4+1=10,
\]

\[
 \operatorname{rank}\pi_{\mathrm{lev}}=168-10=158.
\]

Verify the untwisted ledgers

\[
 h(\pi_{\mathrm{core}}H^5)=(1,4,4,1),
 \qquad
 h(\pi_{\mathrm{lev}}H^5)=(0,79,79,0).
\]

The graph-algebra checker represents an arbitrary element by its exact
coefficients, computes its augmentation on the trivial isotypic block, and
verifies:

> an idempotent that acts as one on \(H^{4,1}\) acts as one on every
> trivial copy in \(H^{3,2}\), and hence cannot have rank two on middle
> cohomology.

This gate must reject the false generalization “no algebraic rank-two
projector exists.”

## Frozen fail-closed certificate scope

The released schema contains semantic objects corresponding to:

```text
source_lock
frozen_model
projective_monomial_group
middle_chow_kuenneth
cayley_jacobian
residue_twisted_representation
graph_projectors
group_algebra_no_go
theorem_decision
scope
```

It does not pre-populate fields for local Frobenius polynomials, local
irreducibility, Fano-line incidence, or a rank-two projector.  Those fields
belong to the C53 schema if that project is launched.

## Release gate

The only permitted C52 theorem decision is

```text
AMBER_DIHEDRAL_CHOW_DECOMPOSITION_AND_GRAPH_ALGEBRA_OPTIMUM
```

and only after B0--B2 pass with independent semantic replay and hostile
mutations.  Otherwise the decision is `NOT_READY`.
