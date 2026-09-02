# Theorem package — exact finite dimer RSA on paths and cycles

## Model and notation

Let `P_n` have vertices `1,...,n` and edges `e_i={i,i+1}`.  Set `P_0` to be
empty.  Give all edges iid continuous priorities and inspect them from lowest
to highest; equivalently, choose a uniformly random permutation of the labeled
edges.  Accept an inspected edge precisely when neither endpoint has already
been matched.  Let `M_n` be the number accepted and

`F_n(z)=E[z^{M_n}]`.

For the simple labeled cycle `C_n`, `n>=3`, use the same rule and write its
accepted-edge count as `K_n` and PGF as `G_n(z)`.

## Main theorem — PROVABLE AS STATED

For `F_0=F_1=1`, every `n>=2` satisfies

`(n-1) F_n(z) = z sum_{a+b=n-2} F_a(z) F_b(z)`.

Consequently the formal ordinary generating function
`F(x,z)=sum_{n>=0}F_n(z)x^n` is the unique formal solution with constant and
linear coefficients one of

`F_x=(F-1)/x+z x F^2`, equivalently `xF_x-F+1=z x^2F^2`.

Put `H_r(x)=partial_z^r F(x,z)|_{z=1}` and `H_0=(1-x)^(-1)`.  For every
integer `r>=1`, `H_r(0)=0` and

```text
H_r'-(1/x+2x/(1-x))H_r
 = x sum_{a=1}^{r-1} binom(r,a) H_a H_{r-a}
   + r x sum_{a=0}^{r-1} binom(r-1,a) H_a H_{r-1-a}.
```

This is triangular in `r` and determines all factorial moments.  In particular,

`H_1=x(1-e^{-2x})/[2(1-x)^2]`,

and, with `H_2=sum E[(M_n)_2]x^n`,

```text
H_2 = x e^{-4x}(4x^2e^{2x}-3xe^{4x}-x+e^{4x}-1)
      /[4(x-1)^3].
```

Therefore, for `n>=2`,

`E[M_n]=sum_{j=1}^{n-1}(n-j)(-1)^{j+1}2^{j-1}/j!`,

and, writing `a=e^{-2}` and `alpha=(1-a)/2`,

`E[M_n]=alpha n-a+o(1)`,

`Var(M_n)=a^2 n+2a^2+o(1)=e^{-4}n+O(1)`.

The exact path support is `{0}` for `n=0,1`; for every `n>=2` it is every
integer in

`ceil((n-1)/3) <= k <= floor(n/2)`.

For every simple cycle `n>=3`, conditioning on its first edge gives the exact
identity

`G_n(z)=zF_{n-2}(z)`.

Thus the cycle support is every integer from `ceil(n/3)` through `floor(n/2)`,

`E[K_n]=1+E[M_{n-2}]=alpha n+o(1)`,

`E[K_n]-E[M_n]=e^{-2}+o(1)`, and

`Var(K_n)=Var(M_{n-2})=e^{-4}n+o(1)`.

In both geometries the limiting expected occupied-vertex fraction is
`1-e^{-2}`.

## Proof spine

The first path edge in the random order is always accepted.  If it is `e_i`,
the untouched eligible vertices split into `P_{i-1}` and `P_{n-i-1}`.  Given
this event, the induced relative orders on those two disjoint edge sets are
independent and uniform; their interleaving is irrelevant.  This proves the
PGF convolution.  Summing it with weight `x^{n-1}` proves the Riccati OGF.

At `z=1`, normalization gives `F(x,1)=(1-x)^{-1}`.  Applying Leibniz's rule to
`zF^2`, and isolating the two terms containing `H_r`, gives the displayed
all-`r` triangle.  Solving its first two linear equations gives `H_1,H_2`.
Coefficient extraction from `H_1` proves the exact finite mean.

The only finite singularity of `H_1,H_2` is `x=1`.  With `s=1-x`,

```text
H_1 = alpha/s^2 -(1+a)/(2s) + entire remainder,
H_2 = c3/s^3+c2/s^2+c1/s + entire remainder,
c3=(1-a)^2/2,
c2=-5/4+a+5a^2/4,
c1=3/4+a+5a^2/4.
```

The remainders have factorially decaying coefficients.  Using
`Var(M_n)=E[(M_n)_2]+E[M_n]-E[M_n]^2` and simplifying the pole coefficients
gives `a^2n+2a^2+o(1)`.

For support, a maximal path matching with `k` dimers has `k+1` gaps of
unmatched vertices, each of size zero or one; hence
`n=2k+g_0+...+g_k` with `g_i in {0,1}`.  Conversely every such binary gap word
constructs a maximal matching.  This gives exactly `2k<=n<=3k+1`.  The cyclic
version has `k` binary gaps and gives `2k<=n<=3k`.  Every specified maximal
matching has positive probability: order its chosen edges first, then all
other edges.  This proves that the combinatorial supports are exactly the RSA
supports.

On `C_n` the first edge is accepted, deletes its two endpoints from further
competition, and leaves a path on `n-2` vertices.  The residual relative order
is uniform, proving `G_n=zF_{n-2}` and every cycle consequence.

## Boundaries and nonclaims

- `P_0,P_1` have no edges and count zero; `P_2` accepts its sole edge.
- `C_n` means a simple cycle only for `n>=3`; loops and parallel-edge versions
  are different models.
- Continuous priorities make ties null.  Discrete priorities need an explicit
  tie-break rule and are outside the theorem as stated.
- The output is maximal under adding an edge.  It is not asserted maximum.
- Finite order enumeration independently tests the formulas through the
  declared window, but does not prove their continuation to all `n`.
- Classical RSA ownership is explicit.  This is a reproducible reconstruction,
  not a claim of invention or literature priority.
- No arithmetic local factors, root numbers, target divisor, target functional
  equation, target zero match, or Hilbert–Pólya operator is claimed.

The resulting Route-A tuple is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, the overall verdict is
`ROUTE_A_REJECTED`, Route B is false, and the governing obstruction is
`HEN-O275`.
