# HCS-C336 theorem package

## Frozen model

Let `X={0,1}^L`, let `F_i` flip bit `i`, and set

```text
M_L=(U/L) sum_i(F_i-I),      A_L=M_L+s e_0 e_0^T,
```

where `L>=1`, `U,s>0`, and `e_0` is the all-zero genotype.  Columns and rows
are indexed by `X`; `M_L` is symmetric with zero column sums.  On the simplex,

```text
p'=A_L p-(1^T A_L p)p = A_L p-s p_0 p.
```

## Main theorem

For every simplex initial state,

```text
p(t)=exp(tA_L)p(0)/(1^T exp(tA_L)p(0)).
```

The semigroup is strictly positive for `t>0`, so `A_L` has a simple Perron
eigenvalue `rho_0`, a positive eigenvector `v_0`, and every simplex orbit
converges to `v_0/(1^T v_0)`.

Write

```text
d_k=-2Uk/L,             w_k=binom(L,k)/2^L,   0<=k<=L.
```

The complete spectrum consists of:

1. `d_k` with multiplicity `binom(L,k)-1` for every `k`; a zero multiplicity
   means that no copy is retained.
2. `L+1` simple roots of

   ```text
   1 = s sum_k w_k/(lambda-d_k).
   ```

There is exactly one secular root above `d_0=0` and exactly one in each open
gap `(d_k,d_(k-1))`, `1<=k<=L`; there is none below `d_L`.  Thus the two
largest full eigenvalues are the top two secular roots `rho_0>0>rho_1>d_1`,
and

```text
Delta_L(U,s)=rho_0-rho_1
```

is the exact projective spectral gap.  Convergence is
`O(exp(-Delta_L t))` for every initial probability vector and has this leading
rate whenever its second-mode coefficient is nonzero.

## Proof

The normalized-semigroup formula follows by differentiating the quotient;
the denominator derivative is `1^T A_L q=s q_0`.  Positivity follows because
the hypercube mutation generator is irreducible and the diagonal selection
term preserves positivity.  Perron--Frobenius and the real-symmetric spectral
theorem then give convergence.

In the normalized Walsh basis `phi_S`, `M_L phi_S=d_|S| phi_S`, while
`<e_0,phi_S>=2^(-L/2)`.  Inside the weight-`k` Walsh space, the codimension-one
subspace whose coefficients sum to zero is killed by `e_0 e_0^T`, hence
retains `d_k` with multiplicity `binom(L,k)-1`.

The orthogonal complement is spanned by the normalized sums of Walsh vectors
of each weight.  In that basis the restriction is

```text
D+s vv^T,   D=diag(d_0,...,d_L),   v_k=sqrt(w_k).
```

The matrix determinant lemma gives

```text
det(lambda I-D-svv^T)
= prod_k(lambda-d_k) * (1-s sum_k w_k/(lambda-d_k)).
```

Every `w_k` is positive.  On each pole-free gap the right-hand sum has
strictly negative derivative, with opposite infinite limits at the two ends;
the exterior intervals give one root above `d_0` and none below `d_L`.
This proves simplicity and strict interlacing.  Expanding the spectral quotient
proves the rate statement and its generic sharpness.

## Boundary closure

- `s=0`: `A_L=M_L`; `d_k` has its full binomial multiplicity and the simplex
  flow is the mutation semigroup converging to uniform.
- `U=0`: if `p_0(0)>0`, then `p_0` obeys the logistic equation and the state
  converges to the master sequence; if `p_0(0)=0`, the entire master-free face
  is stationary.  Irreducible Perron language is not used.
- `L=1`: no mutation eigenvalue is retained.  The two eigenvalues are
  `(s-2U +/- sqrt(s^2+4U^2))/2`.
- Finite `L`: every eigenvalue depends analytically away from the explicit
  reducible faces.  No singular infinite-length error threshold is inferred.

## Route-A obstruction HEN-O320

The Hamming cube and its finite Walsh spectrum provide no rational-prime
carrier or logarithmic prime clock.  The normalized flow is not an isolated
primitive-orbit system, and its characteristic polynomial is a source-side
finite matrix identity, not a target Euler factor or determinant.  Symmetry
is at most a formal operator hint.  The strict tuple is

`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)`;
overall verdict `ROUTE_A_REJECTED`, with Route B locked.
