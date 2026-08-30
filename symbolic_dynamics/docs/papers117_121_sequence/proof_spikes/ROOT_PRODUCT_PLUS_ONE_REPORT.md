# Root proof spike: random adjacent product-plus-one coalescence

> **SUPERSEDED OWNER VERDICT (2026-08-30).**  This preliminary spike predates
> the direct-owner audit.  Disanto--Fuchs--Paningbatan--Rosenberg own the same
> statistic after `X_n=R_n+1`, including its split/law, unmarked antichains,
> mean, and second-moment neighbourhood.  Andriantiana--Wagner--Wang own the
> fixed-tree cardinality marker, while Chang--Fuchs/Rosenberg own the
> caterpillar minimum-probability neighbourhood.  The current P121 residual
> is only the Yule-averaged marked transform and the strict `r>=3`
> continuation of the owned low-order pole/radius ladder.  All broader
> statements below are retained as historical proof-development records;
> external status remains HOLD.

**Status:** infinite theorem package proved; hostile owner gate pending  
**External status:** `HOLD_EXTERNAL`

## Literal process

Start from the ordered word `(1,...,1)` of length `n`.  At every step choose
one of the currently adjacent pairs uniformly and replace

\[
                   (x,y)\longmapsto xy+1.
\]

After `n-1` steps one random integer `X_n` remains.  This is a stochastic
rank-decreasing dynamics, not a choice of a uniformly random Catalan tree.

The original `n-1` gaps remain identifiable until they are deleted.  At a
state with `j` blocks, the process chooses one of the `j-1` surviving gaps
uniformly.  Therefore the complete deletion order is a uniform permutation
of the original gaps.  The last-deleted gap is uniform on
`{1,...,n-1}`; conditional on its location, the relative deletion orders to
its left and right are independent and uniform.  Consequently

\[
 X_1=1,\qquad
 X_n\ \stackrel d=\ 1+X_{I_n}X'_{n-I_n},                 \tag{1}
\]

where `I_n` is uniform on `{1,...,n-1}` and the two variables on the right
are independent conditional on `I_n`.  Equivalently, the coalescence tree
has the random-binary-search-tree split law.  The use of that classical law
receives zero contribution credit.

## Exact distribution and all-moment hierarchy

If `p_n(v)=P(X_n=v)`, (1) gives the finite exact recursion

\[
 p_n(v)=\frac1{n-1}\sum_{i=1}^{n-1}
 \sum_{\substack{a,b\ge1\\1+ab=v}}p_i(a)p_{n-i}(b).       \tag{2}
\]

For an integer `r>=0`, put

\[
 m_{r,n}=\mathbb E X_n^r,
 \qquad F_r(z)=\sum_{n\ge1}m_{r,n}z^{n-1}.
\]

With `m_(0,n)=1`, expansion of `(1+ab)^r` yields the triangular hierarchy

\[
 (n-1)m_{r,n}=
 \sum_{i=1}^{n-1}\sum_{k=0}^r
 \binom rk m_{k,i}m_{k,n-i},                             \tag{3}
\]

and hence

\[
 \boxed{\quad
 F_r'(z)=\sum_{k=0}^r\binom rk F_k(z)^2,
 \qquad F_r(0)=1.
 \quad}                                                   \tag{4}
\]

This is closed successively in `r`: the only occurrence of the new function
on the right is `F_r^2`.  In particular `F_0=(1-z)^(-1)`.

## Closed mean and exact exponential constant

Write `M=F_1`.  The first member of (4) is

\[
 M'=M^2+\frac1{(1-z)^2},\qquad M(0)=1.                   \tag{5}
\]

The logarithmic-derivative substitution `M=-u'/u` turns (5) into

\[
 u''+\frac{u}{(1-z)^2}=0,
 \qquad u(0)=1,\quad u'(0)=-1.                           \tag{6}
\]

Set `w=1-z`.  Direct solution of the Euler equation gives

\[
 u(z)=\frac{2}{\sqrt3}\,w^{1/2}
 \cos\!\left(\frac{\sqrt3}{2}\log w-\frac{\pi}{6}\right)
\]

and therefore

\[
 \boxed{
 M(z)=\frac1w\left[
 \frac12-\frac{\sqrt3}{2}
 \tan\!\left(\frac{\sqrt3}{2}\log w-\frac{\pi}{6}\right)
 \right].}                                               \tag{7}
\]

Inside `|z|<1`, the variable `w=1-z` lies in the right half-plane, so the
principal logarithm is single valued.  Zeros of `u` in this disk must have
real logarithm and hence lie on the positive real `z` axis.  The first is

\[
 \rho=1-\exp\!\left(-\frac{2\pi}{3\sqrt3}\right).
\]

It is simple.  Thus `M` has the local form
`1/(rho-z)+O(1)`.  The next zero is strictly farther from the origin, and
standard coefficient extraction gives the exact leading asymptotic

\[
 \boxed{\mathbb E X_n\sim\rho^{-n}},
 \qquad \rho^{-1}=1.4253868276\ldots .                    \tag{8}
\]

The leading constant is one, not an unspecified multiplicative factor.

## A strict pole ladder for every raw moment

The hierarchy also determines a nontrivial exponential scale at every
moment order. Put `rho_0=1`. For `r>=1`, define

\[
 G_r(z)=\sum_{k=0}^{r-1}\binom rk F_k(z)^2
\]

and let `u_r` solve

\[
 u_r''+G_ru_r=0,
 \qquad u_r(0)=1,\quad u_r'(0)=-1.                       \tag{10}
\]

Equation (4) and logarithmic differentiation give `F_r=-u_r'/u_r`. Let
`rho_r` be the first positive zero of `u_r`. These zeros form a strict
ladder

\[
 \boxed{1=\rho_0>\rho_1>\rho_2>\cdots>0.}               \tag{11}
\]

Indeed, suppose inductively that `F_(r-1)` has a unit-residue simple pole at
`rho_(r-1)`. Then

\[
 G_r(z)\ge rF_{r-1}(z)^2
 \sim\frac{r}{(\rho_{r-1}-z)^2}
 \qquad(z\uparrow\rho_{r-1}).
\]

Sturm comparison with
`v''+c(rho_(r-1)-z)^(-2)v=0`, where `1/4<c<r`, forces a zero of `u_r`
strictly before `rho_(r-1)`. The first zero is simple by uniqueness for the
linear ODE. Hence `F_r` has local form `1/(rho_r-z)+O(1)`.

All coefficients of `F_r` are positive. Pringsheim's theorem identifies
`rho_r` with the radius of convergence: a smaller radius would force a
positive-axis singularity before the first zero, while the zero itself
supplies a singularity at `rho_r`. Consequently

\[
 \boxed{
 \limsup_{n\to\infty}m_{r,n}^{1/n}=\rho_r^{-1}.}         \tag{12}
\]

Thus every raw-moment order has a strictly larger exponential base than the
preceding order. Formula (8) is the closed first member of this pole ladder.

## Smallest output and its exact probability

Induction in (1) gives `X_n>=n`.  Indeed, if the root split has sizes `i,j`
and its two values are at least `i,j`, then

\[
 1+X_iX_j\ge 1+ij=i+j+(i-1)(j-1)\ge n.
\]

Equality forces equality in both subtrees and `i=1` or `j=1`.  Thus the
minimum trees are exactly the planar combs.  For `n>=3`, their probability
`a_n` obeys `a_n=2a_(n-1)/(n-1)`, with `a_2=1`.  Hence

\[
 \boxed{
 \min\operatorname{supp}X_n=n,
 \qquad
 \mathbb P(X_n=n)=\frac{2^{n-2}}{(n-1)!}\quad(n\ge2).
 }                                                        \tag{9}
\]

## Interpretation and owner subtraction

For the planar full binary tree encoded by a deletion order, the recursion
`A(leaf)=1`, `A(T)=1+A(T_L)A(T_R)` counts antichains of internal nodes
(including the empty antichain).  Antichain enumeration on deterministic
trees, random-BST splitting, Riccati linearization, and generic singularity
analysis are therefore background and receive zero credit.  The proposed
residual is narrower: the literal adjacent coalescence, its exact law (2),
the closed all-moment hierarchy (4), the explicit mean (7)--(8), the strict
pole ladder (10)--(12), and the minimum atom (9) as one temporal package.

Bounded exact-phrase, formula, random-BST, and antichain searches have not
located a source stating that package.  This is only a search non-hit.  A
hostile owner gate must still decide whether an existing random-tree
parameter paper already evaluates this particular antichain statistic.
No novelty or priority claim is authorized.

### A cardinality-marked antichain refinement

The tree interpretation retains more information than the specialization at
one.  For an evaluation tree \(T\), let

\[
 P_T(s)=\sum_{B\text{ an internal-node antichain}}s^{|B|}.
\]

Thus \(P_{\rm leaf}(s)=1\),
\(P_T(s)=s+P_{T_L}(s)P_{T_R}(s)\), and \(P_T(1)=X(T)\).  Put

\[
 h_n(s)=\mathbb E P_{T_n}(s),\qquad
 H(z,s)=\sum_{n\ge1}h_n(s)z^{n-1}.
\]

The uniform boundary-order model gives, coefficient by coefficient in \(s\),

\[
 \boxed{\quad
 \partial_zH=H^2+\frac{s}{(1-z)^2},\qquad H(0,s)=1.
 \quad}                                                  \tag{13}
\]

Consequently \([s^k]h_n(s)\) is the exact expected number of size-\(k\)
antichains in the internal-node poset of the induced random search tree.  The
whole marked series is elementary.  With \(w=1-z\),
\(\delta=\sqrt{1-4s}\), and
\(\beta_\pm=(1\pm\delta)/2\), define

\[
 Y(w,s)=\frac{\beta_+w^{\beta_+}-\beta_-w^{\beta_-}}{\delta},
\]

using the removable limit at \(\delta=0\).  The Euler equation
\(Y_{ww}+sY/w^2=0\), together with
\(Y(1,s)=Y_w(1,s)=1\), gives

\[
 \boxed{\quad H(z,s)=\frac{Y_w(1-z,s)}{Y(1-z,s)}.\quad}   \tag{14}
\]

The specialization \(s=1\) is exactly (7), whereas \(s=0\) records the
unique empty antichain.  Equations (13)--(14) supply a marked theorem rather
than a post-hoc interpretation of the scalar mean.  A direct heap-labelled
Cartesian-tree count proves (13); the temporal raw-moment argument proves
(4) and does not introduce this antichain-size marker.

## Independent routes and control

1. Uniform deletion orders prove the split law and (independently by direct
   history enumeration) the finite distribution.
2. The moment recurrence, Riccati--Euler transformation, and zero analysis
   prove the exact expectation and asymptotic constant without enumerating
   histories.

`root_product_plus_one_verify.py` compares all deletion histories with the
recursive law through `n=9`, checks the first five raw-moment equations
through `n=36`, compares exact literal moments through `n=12`, verifies the
minimum atom, and reconstructs the Riccati coefficients from the linear
Euler equation.  It also independently checks the cardinality-marked
antichain series through order 36.  A fresh run passes **185,328 exact
assertions**. It is control evidence, not a replacement for the proofs.
