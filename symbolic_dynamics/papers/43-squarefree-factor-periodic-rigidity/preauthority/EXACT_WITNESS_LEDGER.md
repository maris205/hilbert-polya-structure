# Exact witness ledger

## W0: fixed-point anchor

```text
source point = 0^Z
source membership = PASS
source period = 1
factor image = y0 = pi(0^Z)
factor period = 1 by equivariance
```

This witness guarantees at least one periodic point in every lawful factor.

## W1: source-only periodic collapse

Let \(x\) have period \(n\) and suppose \(x_a=1\). Choose a rational prime
\(p\nmid n\). Then

\[
a+n\mathbb Z\subseteq\operatorname{supp}(x)
\]

and multiplication by \(n\) is invertible modulo \(p^2\). Therefore this one
occupied period class meets every residue modulo \(p^2\), contradicting
admissibility. Hence the only source periodic point is \(0^{\mathbb Z}\).

This is the historical Paper-1 witness and is not claimed as new.

## W2: general CRT proximity certificate

For a window \([-L,L]\), the exact certificate contains

```text
number of source points = 2
number of coordinates per point = 2L+1
number of distinct primes = 2(2L+1)
moduli = pairwise-coprime prime squares
congruences = n + j equals a missing residue for each point-coordinate pair
CRT status = uniquely solvable modulo the product
output block = both shifted points are zero on [-L,L]
```

The residues depend only on admissibility of the chosen points. No numerical
target is fitted.

## W3: smallest window certificate

For \(L=0\), choose distinct primes \(p_x,p_y\) and missing residues
\(a_x,a_y\). The two congruences

\[
n\equiv a_x\pmod{p_x^2},
\qquad
n\equiv a_y\pmod{p_y^2}
\]

have a solution modulo \(p_x^2p_y^2\). At that time both central symbols are
zero. Larger windows repeat the same construction with fresh primes.

## W4: finite periodic-orbit separation

If \(y\) has least period \(r>1\), the exact finite witness is

\[
\delta_r=\min_{0\le k<r}d_Y(S^k y,S^{k+1}y)>0.
\]

Every future distance for the pair \((y,Sy)\) is one of these finitely many
positive values. This directly falsifies proximality.

## W5: determinant certificate

```text
Fix(S^m) = {y0} for every m >= 1
fixed-point count sequence = 1,1,1,...
log zeta = sum_(m>=1) z^m/m
zeta = 1/(1-z)
inverse determinant = 1-z
periodic-core operator = [1]
trace([1]^m) = 1
det(I-z[1]) = 1-z
```

## W6: finite-exclusion sharpness control

Let \(P_0\) be any finite set of rational primes and put

\[
Q=\prod_{p\in P_0}p^2,
\qquad
x_n=1\quad\Longleftrightarrow\quad n\equiv1\pmod Q.
\]

For nonempty \(P_0\), this point is nonzero with least period \(Q\). For each
\(p\in P_0\),

\[
\operatorname{supp}(x)\bmod p^2=\{1\bmod p^2\},
\]

so it omits every other residue and satisfies the finite admissibility
constraints. If \(P_0=\varnothing\), take \(Q=1\) and
\(x=1^{\mathbb Z}\); together with \(0^{\mathbb Z}\), it gives two fixed
points. Hence every finite approximation fails the full periodic-collapse
and proximality conclusions.

For the concrete singleton \(P_0=\{2\}\), the alternative sequence

\[
x=(0111)^{\mathbb Z}
\]

has support residues \(\{1,2,3\}\bmod4\), so it misses residue zero and is
admissible for this finite approximant. It also has least period four.

## W7: lawful point-factor positive control

The constant map to a one-point system is continuous, onto, and equivariant.
Its unique point is fixed, and its determinant is \(1-z\). This realizes the
theorem without adding any primitive orbit.

## W8: rational-prime support mismatch

```text
factor primitive support cardinality = 1
rational-prime primitive support cardinality = countably infinite
factor repetitions = O0^r, r >= 1
rational-prime primitives = distinct atoms p
same-type bijection = impossible
```

The mismatch is independent of how clock weights are assigned.

## W9: predecessor-boundary witnesses

- Paper 3 provides periodic factors after wheel-clock erasure, showing that
  source aperiodicity alone would be insufficient.
- Paper 40 concerns Gauss--Mayer pair projections, not proximal squarefree
  factors.
- Paper 41 concerns rooted Knauf clock/sign descent.
- Paper 42 concerns full-shift function-field marker and clock descent.

None supplies the present proof or ranks C02. Their role is collision control.

## Independent recomputation checklist

1. Verify that the CRT moduli are pairwise coprime and that every congruence
   forces a zero coordinate.
2. Verify the product-metric tail bound.
3. Verify uniform-continuity transport through an arbitrary surjective factor.
4. Verify both cases of the finite periodic-orbit separation lemma.
5. Recompute the fixed-point series and \([1]\) determinant.
6. Prove the arbitrary finite-\(P_0\) periodic construction, including its
   least period and empty-set case; then check the modulus-four example.
7. Confirm that no traversal has been counted as a new primitive orbit.
