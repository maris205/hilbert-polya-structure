# HCS-C20 exact experiment plan

## Question

Does the HCS-C19 ordered-edge lift define a nontrivial connected arithmetic
cover, and what genuinely new spectrum survives after its dihedral symmetry
is resolved?

## Frozen inputs

- the exact HCS-C19 septic (P(\sigma,x));
- (a=\sigma^2-2\sigma\);
- its certified seven-cycle neighbor relation;
- \(\operatorname{Disc}_xP=(4\sigma-9)^2Q_6^3\);
- the scalar genus and ramification ledger; and
- the three previously hatted scalar numerator rows at (p=5,11,13\), frozen
  before the selected-prime good-reduction test.

Forbidden inputs are Riemann zeros, prime tables used for fitting, averaged
transition matrices, and any identification of Frobenius degree with Hénon
time.

## Exact tests

### G1: monodromy and connectedness

Verify that the geometric group is transitive, preserves the seven-cycle,
and is not contained in (A_7\).  The preregistered conclusion is
\(D_7\); a split ordered-edge cover would contradict the frozen inputs and
trigger a C19 rollback audit.

### G2: branch divisor and genus

Verify the (Q_6\)-square class, the explicit simple-root coordinate
\(u(\sigma)\), the node value (Q_6(9/4)\), the even infinity valuation, and
both Riemann--Hurwitz calculations.  The target consequences are exactly six
deck-branch points and (g(E)=8\).

### G3: quotients and representation theory

Check the (D_7\) permutation-character identity on identity, rotation, and
reflection classes.  Check the rational cohomology multiplicities
\(\varepsilon^4\oplus W^2\) and the exact cubic of
\(\tau+\tau^{-1}\).  Keep the unnormalized push-pull convention separate
from the idempotent-normalized convention.

### G4: arithmetic controls

At \(p=5,11,13\), test the selected-prime good-reduction criterion before
promoting any scalar row:

- \(Q_6\bmod p\) is squarefree and the two infinity points of \(B\) remain
  separated;
- \(p\ne2,7\) and \(p\not\equiv1\pmod7\), excluding full tame \(C_7\)
  vertical inertia;
- one degree-seven specialization of \(P\bmod p\) is irreducible, forcing
  \(P\) irreducible over \(\mathbb F_p(\sigma)\);
- the only residual affine singularity is the ordinary node at
  \((9/4,1/4)\); and
- the four-plus-three infinity branches remain rational and separated.

Count \(C\) independently over \(\mathbb F_{p^r}\), \(r=1,2,3\), by affine
enumeration plus the proved node/infinity correction.  Reconstruct its
genus-three numerator from Newton identities and the functional equation.

Count (B:w^2=Q_6\) over \(\mathbb F_{p}\) and
\(\mathbb F_{p^2}\) for (p=5,11,13\) in two independent implementations.
Recover the genus-two local polynomials by Newton identities.

In \(\mathbb Z[\theta]/(\theta^3+\theta^2-2\theta-1)\), verify the three exact
norm identities for the reconstructed scalar polynomials.  A coefficient
mutation is a negative control and must fail.

## Independence protocol

The producer may use SymPy and its own finite-field implementation.  The
checker must not import the producer or any HCS-C19 code or artifact; it
should use a separate polynomial-quotient representation, independently
recompute all \(C\)-counts, and validate schema and hashes.

## Stop conditions

Stop and retract the new theorem if any of the following occurs:

- the discriminant square class becomes trivial geometrically;
- the explicit branch point is multiple modulo (Q_6\);
- either genus calculation disagrees;
- the cubic is only annihilating and not minimal on scalar cohomology;
- the norm identities require changing a frozen scalar coefficient; or
- the selected-prime proof ledger or normalization comparison is incomplete;
- either independent implementation fails to reproduce an affine count; or
- a checker cannot reject a mutated certificate.

If the theorem passes, the next system-level move is cross-period marked Hénon
schemes, not another fixed-period scalar point-count sweep.
