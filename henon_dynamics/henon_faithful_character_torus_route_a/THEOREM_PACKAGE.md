# C134 theorem package

## Definition 1: scaled separated family

Fix

```text
A=[[3/16,-1/32],[1/4,0]],
B=[[1,1,0],[1,0,1],[1,0,0]],
c=(1/2,1/3,1/5).
```

For `k>=1`, let `(t0,t1,t2)` be any branch permutation of `(-2k,0,2k)` and
set `phi_j(z)=Az+(t_j,0)` on three copies of `H^2(D_(3k)^2)`.  For a labelled
character `u in U(1)`, put

```text
W_t,u = B diag(c_j u^t_j),
(L_t,u f)_i = sum_j B_ij c_j u^t_j f_j(phi_j(z)).
```

## Theorem 1: uniform geometry and primitive owner

The coordinate image radii are `21k/32` and `3k/4`.  The first-coordinate
interior margin is `11k/32`, and the minimum gap between adjacent images is
`11k/16`.  Hence every branch is compactly contained and the three images are
pairwise disjoint, uniformly after scaling by `k`.

Every admissible cyclic word has a unique affine fixed point.  Strong
separation makes the itinerary unique, so primitive admissible necklaces
biject with primitive geometric cycles at every period.

## Theorem 2: all-order character-family determinant

For every `u in U(1)`, `L_t,u` is trace class and, for `n>=1`,

```text
Tr(L_t,u^n)=Tr(W_t,u^n)/((1-8^(-n))(1-16^(-n))).
```

Moreover,

```text
D_t,u(z)=product_(r,s>=0) det(I-z 8^(-r)16^(-s)W_t,u),
```

and

```text
log D_t,u = -sum_[gamma] sum_(m>=1)
 (c_gamma u^(M_gamma) z^ell_gamma)^m
 /(m det(I-A^(m ell_gamma))).
```

The trace-class estimates are uniform in `u` because every character phase
has modulus one.

## Theorem 3: three-jet recovery

Work universally in `Q[X,X^(-1)]`.  Direct calculation gives

```text
det(I-zW_t,X)=1-(1/2)X^t0 z
                 -(1/6)X^(t0+t1) z^2
                 -(1/30)X^(t0+t1+t2) z^3.
```

Let

```text
P_n=-n(1-8^(-n))(1-16^(-n))[z^n] log D_t,X.
```

Then `P_n=Tr(W_t,X^n)`.  Newton's identities give

```text
E1=P1,
E2=(P1^2-P2)/2,
E3=(P1^3-3P1P2+2P3)/6,
```

and consequently

```text
2E1=X^t0,
-6E2=X^(t0+t1),
30E3=X^(t0+t1+t2).
```

If their exponents are `S0,S01,S012`, then

```text
t0=S0,  t1=S01-S0,  t2=S012-S01.
```

Thus the first three labelled universal log jets determine the complete
branch-labelled integer translation triple.  The same proof works at a
single known faithful character.

## Proposition 4: exact faithful anchor and alias control

Take `q=(3+4i)/5`.  It lies on `U(1)` and has quadratic trace `6/5`; hence it
is not an algebraic integer, cannot be a root of unity, and `m -> q^m` is
faithful on `Z`.

For `k=1` and `k=6`, the triples are `(-2,0,2)` and `(-12,0,12)`.  They are
componentwise congruent modulo five, so the full mod-five twisted trace and
determinant data agree.  At the faithful anchor, their linear symbolic
coefficients are `-(1/2)q^(-2)` and `-(1/2)q^(-12)`, which differ.  The
universal Laurent exponents recover both triples exactly.

## Progress and exact boundary

C129 detected only residues modulo five.  C134 removes that kernel and proves
injective recovery within the frozen lattice family.  The character parameter
must remain labelled: without its orientation,

```text
D_{-t,u}(z)=D_{t,u^{-1}}(z).
```

The result is not stable finite-precision inversion, arbitrary real geometry
recovery, target matching, arithmetic information, or a natural unitary
quantization.  The strict tuple is
`(A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` and Route B is unauthorized.
