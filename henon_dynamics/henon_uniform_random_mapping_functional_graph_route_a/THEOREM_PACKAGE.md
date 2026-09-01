# Proof package

## Claim

Let `n>=1`, and choose a function `f:[n]->[n]` uniformly from the `n^n`
labelled functions.  Let `C_n` be the number of vertices on directed cycles and
`K_n` the number of weak components.  Write `c(k,r)` for the unsigned Stirling
number of the first kind.  Then, for `1<=r<=k<=n`,

$$
\#\{f:C_n=k,K_n=r\}
=\binom nk c(k,r)\,k n^{n-k-1},                                      \tag{1}
$$

where the forest factor is interpreted as `1` when `k=n`.  Consequently,

$$
\mathbb P(C_n=k)=\frac{(n)_k k}{n^{k+1}},                              \tag{2}
$$

and, for `1<=ell<=n`,

$$
\mathbb E[\text{number of cycles of length }\ell]
=\frac{(n)_\ell}{\ell n^\ell}.                                      \tag{3}
$$

Start at a fixed marked vertex and let `mu>=0` be the number of transient
steps before its eventual cycle, and `lambda>=1` that cycle's length.  For
`mu+lambda<=n`,

$$
\mathbb P(\mu=u,\lambda=\ell)
=\frac{(n-1)_{u+\ell-1}}{n^{u+\ell}}.                                \tag{4}
$$

Thus `R_n=mu+lambda` and `C_n` have exactly the same distribution.  Moreover,

$$
\frac{C_n}{\sqrt n},\ \frac{R_n}{\sqrt n}
\Rightarrow X,
\qquad \mathbb P(X\in dx)=x e^{-x^2/2}\mathbf1_{x\ge0}\,dx,          \tag{5}
$$

and

$$
\left(\frac\mu{\sqrt n},\frac\lambda{\sqrt n}\right)
\Rightarrow (U,V),
\qquad f_{U,V}(x,y)=e^{-(x+y)^2/2}\mathbf1_{x,y\ge0}.                 \tag{6}
$$

## Status

**PROVABLE AS STATED**

## Assumptions and notation

- The sample space is exactly all labelled functions `[n]->[n]`, each with
  mass `n^(-n)`.
- `(a)_j=a(a-1)...(a-j+1)` and `(a)_0=1`.
- Components are weak components of the directed functional graph; each has
  exactly one directed cycle.
- The marked starting vertex is fixed before the random map is sampled.
- Formula (4) has zero mass outside `u>=0`, `ell>=1`, `u+ell<=n`.

## Dependency map

1. Functional-graph decomposition reduces `(C_n,K_n)` to a permutation on
   cyclic labels plus an in-forest rooted at those labels.
2. The complete-graph Laplacian minor counts the rooted forest.
3. Summing unsigned Stirling numbers yields the cyclic marginal.
4. Cycle indicators yield (3) without any independence assumption.
5. An ordered collision-free marked prefix and its forced closing edge yield
   (4).
6. Summing (4) at fixed `u+ell` proves `C_n =_d R_n`.
7. The birthday-product tail proves Rayleigh convergence; conditional
   uniformity of `mu` at fixed `R_n` proves the joint limit.

## Proof

### 1. Cycle–forest decomposition

Fix the set `S` of `k` cyclic vertices.  Its induced edges form a permutation
of `S`; exactly `c(k,r)` such permutations have `r` cycles.  Every vertex
outside `S` belongs to a directed tree whose edges point toward a root in `S`.

The all-minors matrix-tree theorem counts these forests.  After deleting the
`k` root rows and columns from the complete-graph Laplacian, the remaining
matrix of size `m=n-k` is

$$
L_S=nI_m-J_m.
$$

For `m>0`, it has eigenvalue `k=n-m` once and eigenvalue `n` with
multiplicity `m-1`; hence

$$
\det L_S=k n^{n-k-1}.                                                  \tag{7}
$$

When `m=0`, the empty determinant is `1`, which is the unique empty forest.
Choosing `S`, its permutation, and its forest proves (1).  This decomposition
is bijective: its three pieces are recovered uniquely from the functional
graph.

### 2. Cyclic marginal and cycle expectations

The identity `sum_r c(k,r)=k!` and (1) give

$$
\#\{f:C_n=k\}=\binom nk k!\,k n^{n-k-1}.
$$

Dividing by `n^n` gives (2), including `k=n`.

There are `binom(n,ell)(ell-1)!=(n)_ell/ell` directed cycles on `ell`
distinct labels.  Each candidate cycle requires `ell` prescribed function
values and therefore occurs with probability `n^(-ell)`.  Linearity of
expectation proves (3).

### 3. Marked-orbit law

Put `t=u+ell`.  Before the first repeat, the orbit contains `t` distinct
vertices, beginning at the fixed mark.  Its remaining `t-1` ordered vertices
can be chosen in `(n-1)_(t-1)` ways.  Once this prefix is fixed, the next edge
must return to the prefix vertex at index `u`; all later, unexposed function
values are arbitrary.  Consequently the number of maps in this cell is

$$
(n-1)_{t-1}n^{n-t},
$$

and division by `n^n` proves (4).  At fixed `t`, there are exactly `t` choices
`u=0,...,t-1`, so

$$
\mathbb P(R_n=t)=\frac{t(n-1)_{t-1}}{n^t}
=\frac{(n)_t t}{n^{t+1}}=\mathbb P(C_n=t).                            \tag{8}
$$

This proves the finite distributional identity and also shows that
`mu | {R_n=t}` is uniform on `{0,...,t-1}`.

### 4. One-dimensional limit

For integers `0<=m<=n`, no repeat in the first `m` transitions gives

$$
\mathbb P(R_n>m)=\frac{(n-1)_m}{n^m}
=\prod_{j=1}^m\left(1-\frac jn\right).                               \tag{9}
$$

If `m=floor(x sqrt(n))`, Taylor expansion of the logarithm, uniformly for
bounded `x`, yields

$$
\log\mathbb P(R_n>m)
=-\frac{m(m+1)}{2n}+O\!\left(\frac{m^3}{n^2}\right)
\longrightarrow-\frac{x^2}{2}.                                      \tag{10}
$$

For large `m`, the elementary bound `log(1-z)<=-z` supplies tightness.
Equations (9)–(10) therefore give the Rayleigh survival function
`exp(-x^2/2)`.  Identity (8) transfers the same limit to `C_n`.

### 5. Joint limit

Given `R_n=t`, set `V_n=mu/t`.  Its conditional law is the uniform grid
`{0,1/t,...,(t-1)/t}`.  Since `R_n/sqrt(n)` has a continuous limit with no
mass at zero, conditional Riemann sums show

$$
(R_n/\sqrt n,V_n)\Rightarrow(S,W),
$$

where `S` has density `s exp(-s^2/2)` and `W` is independent uniform on
`[0,1]`.  The continuous map `(s,w)->(sw,s(1-w))` gives the limit of
`(mu,lambda)/sqrt(n)`.  Its Jacobian from `(s,w)` to `(x,y)` is `s`, so the
factor `s` cancels and the density is `exp(-(x+y)^2/2)`.  It is normalized:

$$
\int_0^\infty\!\int_0^\infty e^{-(x+y)^2/2}\,dx\,dy
=\int_0^\infty s e^{-s^2/2}\,ds=1.
$$

## Boundary and degeneration audit

- At `n=1`, the sole map is a fixed point: `(C_1,K_1,mu,lambda)=(1,1,0,1)`.
- At `k=n`, the forest is empty and (1) becomes `c(n,r)`, as required for
  permutations.
- At `mu=0`, the mark is itself cyclic; at `lambda=1`, its eventual cycle is a
  fixed point.  Formula (4) includes both faces.
- At `mu+lambda=n`, every label appears before closure and the arbitrary-edge
  factor is `n^0=1`.
- The limiting density includes the axes as support boundaries, but assigns
  them zero Lebesgue mass.

## Evidence boundary

Exhaustive enumeration audits every map through `n=7`; exact atlases and
symbolic determinants extend the regression window.  Those computations do
not prove (1)–(6).  The proof owners are the bijection, determinant, indicator
count, prefix count, and product limit above.  Internal checking is not peer
review, and workspace ownership is not a priority claim.
