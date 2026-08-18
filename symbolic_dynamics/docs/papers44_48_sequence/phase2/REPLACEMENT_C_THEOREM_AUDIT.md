# Replacement C Theorem Audit — q-adic Boundary Spectra

## Status and ownership subtraction

`PHASE2 GO / TWO INDEPENDENT AUDITS PASSED / NO AUTHORITY WRITE`

The multiplicative-SFT product decomposition, entropy formula, Hausdorff and
Minkowski dimensions of the multiplicative golden-mean shift, and the recent
notions of boundary complexity and surface entropy are prior-owned.  They
receive zero novelty credit here.

The candidate studies the bounded order-one remainder after the entropy
term.  Its proposed contribution is an exact `q`-adic extension and a full
description of every finite-size accumulation value; the golden-mean control
then produces a quantitatively separated Cantor boundary spectrum and dense
pole-type boundary singularities forcing a natural boundary.

## Frozen object

Let `q>=2` and let `A` be a primitive zero-one adjacency matrix.  Define the
one-sided multiplicative SFT

```text
X_A^(q)={x: A[x_n,x_{qn}]=1 for every n>=1}.
```

Let `Z_A,q(N)` be the number of admissible prefixes on `{1,...,N}`.  Put

```text
W_0=1,
W_l=1^T A^(l-1)1  (l>=1),
c_v=log(W_(v+1)/W_v),
rho=PF eigenvalue of A,
d_v=c_v-log rho.
```

## Exact increment and entropy theorem

The `q`-adic chains `i,qi,q^2i,...`, `q` not dividing `i`, are disjoint.
Adding the index `N` extends exactly one chain, by one vertex.  Therefore

```text
log Z(N)-log Z(N-1)=c_(nu_q(N)).
```

Summing valuations gives the known entropy in a sharper exact form:

```text
h=sum_{v>=0}(q-1)q^(-v-1)c_v,
log Z(N)=hN+E(N).
```

The entropy and chain product are validation inputs, not novelty claims.

## q-adic boundary extension

For `r_v(N)=N mod q^v`, exact summation by parts gives

```text
E(N)=-sum_{v>=1}(d_v-d_(v-1)) r_v(N)/q^v.
```

Primitivity gives exponential decay of `d_v` (up to a harmless polynomial
factor if a subdominant Jordan block is present), so the series converges
uniformly on the `q`-adic integers.  It defines a continuous function

```text
E_A,q: Z_q -> R.
```

Every tail of the natural numbers is dense in `Z_q`.  Explicitly, for
`x in Z_q`, the representatives

```text
N_j=(x mod q^j)+q^j
```

tend to infinity and converge `q`-adically to `x`.  Compactness gives the
converse subsequence statement.  Hence the complete finite-size boundary
spectrum is

```text
Acc{Z(N) exp(-hN):N>=1}=exp(E_A,q(Z_q)).
```

This is an equality of compact sets, not only upper and lower fluctuation
bounds.

## Golden-mean Cantor theorem

Take `q=2` and

```text
A=[[1,1],[1,0]],
phi=(1+sqrt(5))/2.
```

Then `W_l=F_(l+2)`.  Binet's formula gives, with `r=-phi^(-2)`,

```text
d_v=log[(1-r^(v+3))/(1-r^(v+2))].
```

Writing `x=sum_{k>=0}epsilon_k 2^k in Z_2`, the boundary function has a
digit series

```text
E(x)=sum_{k>=0}gamma_k epsilon_k,
gamma_k=-sum_{v>=k+1}(d_v-d_(v-1))2^(k-v).
```

Put `t=phi^(-2)` and `r=-t`.  The independently replayed Binet expansion is

```text
gamma_k=sum_(m>=1) a_m r^(m(k+2)),
a_m=(1-r^m)^2/[m(2-r^m)]>0.
```

The proved scalar bound

```text
sum_(m>=2) a_m t^(2m)/(1-t^m) < a_1 t^3
```

implies alternating signs and strong separation

```text
|gamma_k|>sum_{j>k}|gamma_j|,
```

and `gamma_(k+1)/gamma_k -> -phi^(-2)`.  Consequently `E(Z_2)` is a Cantor
set with

```text
dim_H E(Z_2)=dim_B E(Z_2)=log 2/(2 log phi).
```

Ordinary Minkowski-content nonexistence is excluded from the source lock:
the dyadic-scale accumulation theorem alone does not control every continuous
scale.  It may enter only after a separate cylinder-scale lower/upper
oscillation proof and a fresh claim review.

## Boundary generating function

Let

```text
G(z)=sum_{N>=0}E(N)z^N.
```

Since `r_v(N)` has period `q^v`,

```text
G(z)=-sum_{v>=1}(d_v-d_(v-1))q^(-v)
      * [sum_N (N mod q^v)z^N].
```

Every summand is rational with denominator `1-z^(q^v)`.  At a primitive
`q^v`-th root `xi !=1`, the residue of every rational bracket at level
`w>=v` is the same nonzero multiple of `xi/(1-xi)`.  Thus every higher level
participates, and the full Abelian/radial singular coefficient is controlled
by

```text
sum_{w>=v}(d_w-d_(w-1))/q^w.
```

For the golden-mean Binet sequence these tails are nonzero; indeed the level
`v` tail equals `-gamma_(v-1)/2^(v-1)`.  Every primitive `2^v`-th root is
therefore a pole-type boundary singularity with nonzero Abelian/radial
residue.  These non-isolated boundary singularities are dense on the unit
circle and prove that `|z|=1` is a natural boundary for `G`; they are not
called meromorphic poles of the full function.

## Primary-source boundary

- Fan--Liao--Ma and Kenyon--Peres--Solomyak own the multiplicative-SFT
  entropy/dimension framework.
- Ban--Hu--Lai, DOI `10.1063/5.0118652`, own boundary-complexity and surface-
  entropy notions for multiplicative integer systems.
- Those sources do not state a `q`-adic extension of the exact order-one
  remainder, its full compact accumulation set, the golden Cantor dimension,
  or the dense radial-singularity theorem.

The final bibliography must use the primary papers and must not describe the
known product or entropy formulas as new.

## Dual evaluators and mutations

1. direct enumeration of admissible prefixes versus the independent chain
   product;
2. successive log increments versus `c_(nu_q(N))`;
3. direct normalized counts versus the residue-series evaluator on long
   congruent `q`-adic prefixes;
4. exhaustive finite `2`-adic digit images versus the gamma-series Cantor
   evaluator;
5. rational residue-generating functions versus direct radial singularity
   coefficients at roots of unity;
6. nonprimitive, reducible, periodic, and zero-entry controls that must fail
   the primitive source contract or enter separately scoped variants.

## Admission decision

After deleting the inherited entropy/product machinery, the exact `q`-adic
boundary spectrum, golden Cantor theorem, and natural-boundary theorem remain
one coherent result.  No same-object collision was found in Papers 1--43.
Two independent proof/source replays closed the increment, compact-image,
golden strong-separation, and dense-boundary-singularity arguments.  Final
Phase-2 decision: `GO_WITH_FIREWALL`.
