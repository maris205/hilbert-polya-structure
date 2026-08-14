# HCS-C55 exact experiment plan

Status: **RELEASE_FROZEN; exact machine tuple remains RELEASE_CANDIDATE,
official paper build passed, and implementation provenance is locked**.

This is an exact algebra experiment, not a numerical fit. The frozen
producer/checker tuple closes the finite computations used by Theorems A--C
while all geometric implications remain in the proof package.

## E0. Frozen formal dependencies

Verify byte-for-byte:

- HCS-C52 certificate SHA-256
  \(a2b0b281bfb311f979c7ed65e441a184ebe338b05f5fec8a60768610965c9c94\);
- HCS-C53 theorem SHA-256
  \(e474d938c02d1d9e39e510dfd77ffcdd6383e5dcc8a8442b5b19465be82dbebe\);
- HCS-C54 theorem SHA-256
  \(d234f078cb415db8394fdcece124068cad90dbdf12b82941207105ecd24088b4\).

Kill the run if any dependency differs.

The architecture and theorem-design digests are chronology-only records.
They are unpackaged and must not be treated as replayable theorem inputs.

## E1. Ambient group-scheme replay

For all \(24\) split elements:

1. reconstruct the projective matrices;
2. verify the dihedral presentation and distinctness;
3. verify covariance of the cubic and quadric equation lines;
4. verify
   \(\delta(g)=M\tau(g)M^{-1}\);
5. verify
   \(\tau(B^{-1}gB)=B^{-1}\delta(g)B\);
6. record that the descended action is a rank-\(24\) nonconstant group
   scheme action, not \(24\) rational matrices.

Expected theorem output: PASS/FAIL only; no new automorphism classification.

## E2. Deformation-space ledger

Solve the exact infinitesimal ideal-stabilizer equations
\(\delta_AQ=\nu Q\) and \(\delta_AC=\mu C+LQ\). Certify a
\(73\)-rank system in \(74\) unknowns, with the kernel equal to the scalar
\(\mathfrak{gl}_8\) direction
\((A,\nu,\mu,L)=\lambda(I_8,2,3,0)\) and projective Lie stabilizer zero.
Use this only as the missing \(H^0(T_X)=0\) check; do not promote it to a
classification of the full \(\operatorname{PGL}_8\) automorphism group.

Reconstruct the Cayley quotient and certify:

\[
\dim R_{1,-3}=1,\qquad
\dim R_{2,-3}=83.
\]

Build the four invariant directions and verify:

- invariance under all \(24\) split elements;
- the residue determinant twist;
- semilinear fixedness under \(\tau(\rho)=\rho^2\);
- \(D(y)=y,D(z)=\rho z\), with \(D(C)=C\),
  \(D(Q_\rho)=\rho^2Q_\rho\), and \(D(F)=F\);
- rational basis convention \(q_0=e_0\), not \(2e_0\);
- independence of the four first images
  \([y^2p_i]\in R_{2,-3}\).

Expected theorem output:
\(\dim H^1(T_X)^{\mathscr G}=4\) and invertibility of the projected
infinitesimal period map.

## E3. Top component

Enumerate the ambient monomials of bidegree \((5,-6)\) and certify:

- ambient count \(24145\);
- exactly one surviving standard monomial;
- \(\dim R_{5,-6}=1\);
- the frozen top standard monomial and reduction normalization.
- the raw semilinear image
  \(D(x_6^2x_7^2z^5)=x_1^2x_2^2z^5\) with total prefactor \(1\),
  followed by its exact reduction to the top coordinate.

The top coordinate must be recomputed in the checker using a distinct
Groebner order or implementation.

## E4. Stage-by-stage Yukawa ledger

For each basis direction record separately:

\[
[yp_i]\in R_{1,0},\qquad
[y^2p_i]\in R_{2,-3}.
\]

For every unordered triple \(i\le j\le k\), record:

\[
[y^4p_ip_jp_k]\in R_{4,-3}
\]

and its paired reduction

\[
[y^5p_ip_jp_k]\in R_{5,-6}.
\]

The output must contain all \(20\) top scalars, not only the normalized
polynomial.

## E5. Cubic reconstruction

Construct the cubic in two independent ways:

1. expand the \(20\) unordered tensor values with multiplicities
   \(1,3,6\);
2. directly reduce
   \(y^5(\sum_{i=0}^3u_ip_i)^3\).

Require exact equality. Then:

- prove coefficient ratios lie in \(\mathbf Q\);
- clear denominators;
- divide by the coefficient gcd;
- fix the global sign by the positive \(u_0^3\) coefficient;
- compare all \(20\) coefficients with THEOREM_PACKAGE.md.

## E6. Cubic-surface geometry

Over \(\mathbf Q\):

1. compute the four exact partial derivatives;
2. compute the gradient quotient;
3. verify length \(16\);
4. verify Hilbert series \((1+t)^4\);
5. verify Hilbert numerator
   \(1-4t^2+6t^4-4t^6+t^8\);
6. independently verify projective gradient saturation is the unit ideal.

The theorem derives geometric smoothness and geometric irreducibility from
these assertions. Rational factorization is optional diagnostic evidence,
not the proof.

## E7. Relative-theorem interface

The exact certificate must expose the central data needed by the proof:

- group rank \(24\);
- core cohomology rank \(10\);
- untwisted Hodge ledger \((1,4,4,1)\) in bidegrees
  \((4,1),(3,2),(2,3),(1,4)\);
- invariant tangent dimension \(4\);
- nonzero period derivative determinant;
- exact one-Tate-twist ledger.

It must not claim to compute a relative Chow--Künneth projector or to
construct the Hilbert slice symbolically.

## E8. Independent checker

The checker must:

- reject unknown and duplicate JSON keys;
- recompute every asserted rank;
- rebuild group covariance;
- reconstruct all tangent images;
- recompute the top component without reading a producer Groebner cache;
- reconstruct the cubic both ways;
- recompute the gradient algebra independently;
- compare exact hashes only after semantic verification.

## E9. Hostile negative mutations

Each mutation must fail:

1. \([yp_i]\mapsto[y^2p_i]\);
2. paired \(y^5\mapsto y^4\);
3. \(\tau(\rho)=\rho^2\mapsto\rho\);
4. \(D(z)=\rho z\mapsto\rho^2z\), or deletion of the residue determinant
   twist;
5. \(q_0=e_0\mapsto2e_0\) without polynomial transport;
6. alteration of any one cubic coefficient;
7. deletion of mixed-term multiplicities;
8. replacement of the norm graph by two rational graphs;
9. rational factorization promoted to geometric irreducibility;
10. literal_linear_family or motive_realized set to true.

## E10. Reproducibility

- Run producer twice and require byte-identical semantic payloads.
- Run checker from a clean temporary directory.
- Run the full unit and mutation suite.
- Record software versions and monomial-order conventions.
- Promote only through an atomic manifest step.
- Final hashes were kept null until promotion and are now recorded in the
  integrity, compilation, and Route-A records. Implementation commit
  `e5661e80da6f7de53f574f97f768744095ba8ae0` is provenance-locked.

## Comparator lane

No BCD computation is required for the unconditional C55 theorem. A later
comparator experiment must first obtain a full four-variable B-model tensor
and then solve

\[
Y_{\rm BCD}(c;u)=\lambda Y_H(Au).
\]

Until that separate experiment exists, the comparator label is
NOT-COMPARABLE-WITH-CURRENT-DATA.
