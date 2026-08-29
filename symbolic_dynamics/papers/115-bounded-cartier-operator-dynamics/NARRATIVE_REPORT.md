# Narrative Report — P115

## Central story

Degree truncation turns one classical Cartier selector into a finite map with
two clean pieces. Positive coefficient indices form disjoint `p`-adic chains
that die, while the constant coefficient remains and evolves by inverse
Frobenius. The paper converts that split into an exact bounded temporal and
component census.

The strongest early signal is the iterate

```text
C^t(sum c_j x^j) = sum_(p^t j <= n) c_(p^t j)^(p^(-t)) x^j.
```

Writing each positive index as `j=u*p^v` and replacing its coefficient by
`d_(u,v)=sigma^(-v)(c_(u*p^v))` untwists every positive chain into a finite
nilpotent shift, while the constant coordinate remains inverse Frobenius.
This gives the product and component structure. A complementary `F_p`-linear
factorization then recounts uniform affine fibres after the iterate is known.
The transient side is governed by the largest `p`-adic valuation among
occupied positive indices; the recurrent side is exactly inverse Frobenius on
`F_(p^a)`.

## Results a reader should remember

- Every nonempty `t`-fibre has `q^(n-floor(n/p^t))` elements.
- A Frobenius cycle of length `d` supports one weak component of size
  `d*q^n`; its cycle vertices carry isomorphic nilpotent-chain in-trees.
- Under the uniform law,
  `P(tau <= t)=q^(-floor(n/p^t))`.
- The sharp depth is `0` for `n=0` and
  `1+floor(log_p n)` for `n>0`.
- `#Fix(C^m)=p^gcd(a,m)` and the zeta function is the Euler product over
  inverse-Frobenius cycles.
- At `n_L=floor(alpha*p^L)`, every fixed reverse-depth tail becomes exactly
  `q^(-floor(alpha*p^(k-1)))` once `L>=k-1`.
- Phase size and the full fixed sequence recover `(p,a,n)` without exceptions.

## Owner subtraction

The paper does not claim the Cartier operator, the coefficient-selector
formula in the power-series setting, finite-field Frobenius/subfield facts,
Möbius inversion, or generic linear functional-graph structure. Bridy is a
direct source for the precise `Lambda_i` coefficient convention used here;
Cartier is cited for the originating operation; Jeong is a close primary
Cartier-family owner; and Lidl--Niederreiter cover the finite-field facts.
Restriction of scalars makes the map a classical finite `F_p`-linear system:
Elspas, Wang, Hernández Toledo, Panario--Reis, and Reis mark the generic
state-diagram, cyclic--nilpotent, component, and attached-tree territory.

The residual scope is only the exact bounded Cartier specialization and its
lattice/recovery conjunction. Internally it
is separated from P100’s digit-erasure phase space, P103’s adjugate matrix
map, P107’s ideal-lattice map, and P109’s nilpotent image map on subspaces.
The closest internal engine is P109, but neither phase space nor recurrent
core agrees: P115 evolves coefficient vectors and retains an inverse-
Frobenius permutation core. External owner review remains incomplete, so
release, novelty, and priority are **HOLD**.

## Evidence posture

The verifier uses actual polynomial-basis models of six finite fields and
does not treat a prime power as a label permutation. Its 2,259,162 assertion
executions include statewise coordinate-conjugacy, inverse-coordinate,
component-size, and per-root tree-layer checks in addition to the earlier
finite formulas, edge lanes, zeta coefficients, and rational lattice windows.
The raw counter is mechanical, not a number of independent claims.
Computation is positioned only as exact finite falsification; every general
statement has a self-contained proof in `main.tex`.
