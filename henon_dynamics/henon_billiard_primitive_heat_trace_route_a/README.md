# HCS-C152: primitive billiard-direction heat transform

C152 gives the clean square-billiard direction ledger a convergent,
source-derived regularization.  For ordered positive coprime directions,

```text
H_prim(t)=sum exp(-4t(m^2+n^2)),  t>0.
```

The transform converges absolutely, retains coincident lengths with their
direction multiplicities, and has the exact factorization

```text
H_prim(t)=sum_(d>=1) mu(d) theta_+(4td^2)^2.
```

An elementary quarter-disk count and Stieltjes integration prove
`H_prim(t)=3/(8 pi t)+O(t^(-1/2) log(1/t))` as `t` decreases to zero.  Exact
coefficient identities are independently checked through
`m^2+n^2<=20000`, with count receipts through radius 200.

This is a primitive-direction heat transform, not a clean wave trace, an
isolated-orbit determinant, or the spectral trace of the Dirichlet Laplacian.
The natural square quantization remains only a boundary object.  Scope:
`NO_BAD_EULER_OR_ROOT_NUMBER`.  Verdict:
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)`, overall
`ROUTE_A_EXPLORATORY`; Route B is not authorized.
