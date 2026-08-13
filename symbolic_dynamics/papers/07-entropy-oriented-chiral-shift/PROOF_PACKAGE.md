# SD-C09 Proof Package

## Theorem 1 — universal one-sided phase gauge

For any positive injective diagonal mass `G` and bounded `K`, put

```text
A_t = G^(1/2+it) K,
B_t = [[0,A_t],[A_t*,0]].
```

Since `A_t=G^(it)A_0`, one has

```text
B_t = diag(G^(it),I) B_0 diag(G^(-it),I).
```

No commutation hypothesis is needed. Mass noncommutation cannot produce
motion in a one-sided phase ansatz.

## Theorem 2 — exact-ledger DAG rigidity

If `D(x)=diag(x_1,...,x_N)` and

```text
det(I-zD(x)K) = product_j (1-zx_j)
```

identically in all variables, comparison of squarefree monomials gives
`det K[S,S]=1` for every vertex subset `S`. Writing `K=I+N`, principal-minor
inversion yields `det N[S,S]=0` for every nonempty `S`. A shortest directed
cycle in the support of `N` has no directed chord, hence contributes the sole
nonzero term to its principal determinant, a contradiction. Thus the
off-diagonal support is a DAG. The converse follows by topological ordering.

Unique factorization makes the same proof valid for the full Dirichlet
ledger after `x_j=p_j^(-s)`.

## Theorem 3 — trace-invisible graded cancellation

For a trace-class graded `T`,

```text
log Ber(I-zT) = -sum_(r>=1) z^r Str(T^r)/r.
```

If every mixed power supertrace vanishes, its Berezinian is one. For `S_q`
relative determinants, equality of even/odd traces for all `r>=q` gives the
same conclusion after regularization. Exact all-order cancellation cannot
generate a divisor in that determinant.

## Theorem 4 — exact entropy-oriented Euler transfer

Let tensor atoms be entropy ordered, let `S e_n=e_(n+1)`, and define

```text
L_s = D_s + (D_s S + S D_s)/2.
```

This is lower bidiagonal. Consequently,

```text
(L_s^r)_(nn)=p_n^(-rs),
Tr L_s^r=sum_p p^(-rs),
det(I-zL_s)=product_p(1-zp^(-s))
```

for `Re(s)>1`. The successor coefficients join unequal masses, so the
transfer is mass-noncommuting.

## Theorem 5 — chiral strip and functional symmetry

Define `B_s=[[0,L_s],[L_(1-s)^T,0]]`. Weighted-shift ideal estimates give
`L_s in S_q` when `q Re(s)>1`. Hence `B_s in S_3` on
`1/3<Re(s)<2/3`. Since `B_(1-s)=B_s^T`,

```text
det_3(I-zB_(1-s))=det_3(I-zB_s).
```

On `s=1/2+it`, `B_s` is self-adjoint.

## Theorem 6 — strict fourth-Schatten motion

Set `u_n=1/p_n` and

```text
x_n(t)=(u_n+u_(n+1)+2 sqrt(u_n u_(n+1)) cos(t log(p_(n+1)/p_n)))/4.
```

For the lower-bidiagonal transfer,

```text
||L_t||_4^4 = sum_n (u_n+x_n(t))^2 + 2 sum_n u_(n+1)x_n(t).
```

Every term increases with `x_n`, and `x_n(t)<=x_n(0)`. Equality for every
`n` would force both `t log(3/2)` and `t log(5/3)` to be multiples of
`2 pi`. Unique factorization forces `t=0`. Thus the norm, fourth chiral
trace, and chiral determinant genuinely move for every nonzero height.

## Exact two-atom crossing

For atoms `2,3`, direct expansion gives

```text
det(I-L_t* L_t) = (3-2 sqrt(6) cos(t log(3/2)))/24.
```

The chiral block has exact unit crossings at

```text
t=(2 pi k +/- arccos(sqrt(6)/4))/log(3/2).
```

Their periodic linear count is a `PROVES_TOO_MUCH` control, not a Riemann
zero claim.

## Adversarial corollary — arbitrary forward phases

Any weighted forward DAG is triangular after topological ordering. Therefore
arbitrary complex phases and amplitudes on its forward edges preserve every
power trace and the full characteristic/Fredholm determinant. They may still
move singular values. The frozen experiment found this behavior in all 24
random DAG controls. A reverse edge is categorically different: it creates a
recurrent two-cycle and a mixed defect at power two.
