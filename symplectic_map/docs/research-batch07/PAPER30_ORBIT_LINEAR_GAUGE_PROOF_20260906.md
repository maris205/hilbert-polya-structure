# Orbit-linear Hamiltonians: an exact second-order rigidity statement

Date: 2026-09-06. Author proof preflight, not an independent audit or a
selected Paper30 project. Route applicability: NOT_APPLICABLE.

## Claim and status

**PROVABLE AS STATED.** Let $K$ be a field of characteristic zero,
$p\in K[t]$ have degree $d\ge2$ and leading coefficient $a\ne0$, and set
$H(x,y)=(p(x)-y,x)$ and $\sigma=H^*$ on $A=K[x,y]$. Use the Poisson
bracket $\{f,g\}=f_xg_y-f_yg_x$ and define
$X_0=x$, $X_{-1}=y$, $X_{i+1}+X_{i-1}=p(X_i)$.

For a finite orbit-linear Hamiltonian
$$
h=b+\sum_{i\in\mathbb Z} a_iX_i,
$$
the class of $\{h,\sigma h\}$ in
$$
\overline{\mathcal H}=A/((1-\sigma)A+K)
$$
vanishes if and only if at most one coefficient $a_i$ is nonzero.
Consequently the formal automorphism
$$
U_\varepsilon=\exp(\varepsilon\operatorname{ad}_{h-\sigma h})\sigma
$$
is conjugate to $\sigma$ by a Hamiltonian automorphism
$C_\varepsilon=\exp(\operatorname{ad}_{\varepsilon h+arepsilon^2h_2+\cdots})$
with polynomial coefficients if and only if at most one $a_i$ is nonzero.
In that case $C_\varepsilon=\exp(\varepsilon\operatorname{ad}_h)$ suffices.
Here $\operatorname{ad}_h(f)=\{h,f\}$ and conjugacy means
$U_\varepsilon=C_\varepsilon\sigma C_\varepsilon^{-1}$.

The parameter series is formal in $\varepsilon$; no completeness of the
Hamiltonian flow in analytic time is asserted. The coefficients are global
polynomials, not germs or formal power series in $x,y$.

## Assumptions, strategy, and dependencies

1. The orbit-basis and orbit-coefficient criterion are the already accepted
   tools of Paper29, Sections 2 and 3. In the scalar case the standard words
   are $\prod_iX_i^{e_i}$, with finite support and $0\le e_i<d$;
   $\sigma$ translates every index by one. A polynomial belongs to
   $(1-\sigma)A+K$ precisely when its coefficient sum on each nonconstant
   translation orbit is zero. These facts are deducted, not claimed as new.
2. A continuant computes brackets of two orbit coordinates. Its top word
   will be standard without further reduction.
3. The two extreme nonzero coefficients of $h$ produce a unique top word
   in $\{h,\sigma h\}$. Its nonconstant orbit sum cannot vanish.
4. The second-order BCH coefficient gives necessity for conjugacy. A
   constant bracket gives an exact commuting-derivation identity for the
   one-coordinate case.

Only scalar $p$ and the orbit-linear subspace are in this claim. Arbitrary
polynomial Hamiltonians, even of ordinary degree four, are not covered.

## Proof

### 1. Brackets of two coordinates

Since $H$ is symplectic, $\sigma$ preserves the Poisson bracket.
As $\{X_0,X_1\}=\{x,p(x)-y\}=-1$, one has
$\{X_i,X_{i+1}\}=-1$ for every $i\in\mathbb Z$. This also follows for
negative $i$ because $\sigma$ is invertible and Poisson.

For $m\ge0$ define the continuant
$$
K_0=1,\qquad K_1(t_1)=t_1,\qquad
K_m(t_1,\ldots,t_m)
=t_mK_{m-1}(t_1,\ldots,t_{m-1})-K_{m-2}(t_1,\ldots,t_{m-2}).
$$
Then for $j>i$,
$$
\{X_i,X_j\}
=-K_{j-i-1}\bigl(p'(X_{i+1}),\ldots,p'(X_{j-1})\bigr). \tag{1}
$$
The case $j=i+1$ is the adjacent bracket. The next case follows by
bracketing $X_{i+2}=p(X_{i+1})-X_i$ with $X_i$. For each later case,
$$
\{X_i,X_{j+1}\}=p'(X_j)\{X_i,X_j\}-\{X_i,X_{j-1}\},
$$
which is exactly the defining continuant recurrence.

For completeness, the continuant also equals the sum over matchings $M$
of the path on vertices $1,\ldots,m$:
$$
K_m(t_1,\ldots,t_m)=
\sum_M(-1)^{|M|}\prod_{r\notin V(M)}t_r. \tag{2}
$$
Partitioning these matchings according to whether vertex $m$ is unmatched
or paired with $m-1$ proves the same recurrence and initial values.
In each summand, every $t_r$ occurs at most once.

Let formal word degree mean $\sum_i e_i$ for a standard word, not its
ordinary degree in $x,y$. Since $\deg p'=d-1<d$, every product in (2)
after substitution in (1) is already a linear combination of standard
words. If $j-i-1=m$, its unique term of formal word degree $(d-1)m$ is
$$
-(da)^m\prod_{s=i+1}^{j-1}X_s^{d-1}. \tag{3}
$$
Indeed, this comes from the empty matching and from the leading term of
each $p'$. Every nonempty matching removes two factors, and selecting any
lower-degree coefficient of a remaining derivative lowers the degree.
For $m=0$, (3) means the constant $-1$.

### 2. Extreme endpoints detect every nonsingleton linear combination

Suppose at least two coefficients of $h$ are nonzero. Set
$$
L=\min\{i:a_i\ne0\},\qquad
R=\max\{i:a_i\ne0\},\qquad r=R-L\ge1.
$$
One has
$$
\{h,\sigma h\}=
\sum_{i=L}^R\sum_{j=L}^R a_i a_j\{X_i,X_{j+1}\}. \tag{4}
$$
The distance $|(j+1)-i|$ in (4) is at most $r+1$. Equality occurs only
for $(i,j)=(L,R)$: the opposite signed distance has maximum $r-1$.
For every other nonzero bracket, (1), with antisymmetry if needed, gives
formal word degree at most $(d-1)(r-1)$. The possible equal-index bracket
is zero.

Thus (4) has a unique standard word of formal degree $(d-1)r$:
$$
W=\prod_{s=L+1}^R X_s^{d-1},\qquad
[W]\{h,\sigma h\}=-a_La_R(da)^r\ne0. \tag{5}
$$
This word is nonconstant since $r\ge1$ and $d\ge2$. Translation of a
standard word preserves its formal word degree. No lower-degree term of
(4) can therefore be in the translation orbit of $W$. Since $W$ is the
only top-degree word, the complete coefficient sum of this orbit is the
nonzero value in (5). The orbit-coefficient criterion gives
$\{h,\sigma h\}\notin(1-\sigma)A+K$.

If no coefficient is nonzero, $h=b$ and the bracket is zero. If exactly
one is nonzero, say $h=b+uX_i$, the bracket is $-u^2\in K$.
These computations prove both directions of the first assertion.

### 3. The formal conjugacy condition

Put $H_\varepsilon=\varepsilon h+\varepsilon^2h_2+\cdots$. Since
$\sigma\operatorname{ad}_f\sigma^{-1}=\operatorname{ad}_{\sigma f}$,
one has
$$
C_\varepsilon\sigma C_\varepsilon^{-1}\sigma^{-1}
=\exp(\operatorname{ad}_{H_\varepsilon})
 \exp(-\operatorname{ad}_{\sigma H_\varepsilon}).
$$
Formal logarithms in the $\varepsilon$-adically complete derivation
algebra are defined because both exponents have positive parameter order.
The order-two BCH term is
$$
\operatorname{ad}_{\,
\varepsilon(h-\sigma h)+\varepsilon^2
\left((1-\sigma)h_2-\tfrac12\{h,\sigma h\}\right)}.
$$
The kernel of $f\mapsto\operatorname{ad}_f$ on $K[x,y]$ consists of
constants: vanishing on $x,y$ makes both partial derivatives zero in
characteristic zero. Hence equality with
$\exp(\varepsilon\operatorname{ad}_{h-\sigma h})$ requires
$$
(1-\sigma)h_2-\tfrac12\{h,\sigma h\}\in K. \tag{6}
$$
For a nonsingleton orbit-linear $h$, (5) makes (6) impossible.

For a singleton, $\{h,\sigma h\}$ is constant, so
$[\operatorname{ad}_h,\operatorname{ad}_{\sigma h}]
=\operatorname{ad}_{\{h,\sigma h\}}=0$.
The exponential product identity for commuting derivations gives
$$
\exp(\varepsilon\operatorname{ad}_h)
\exp(-\varepsilon\operatorname{ad}_{\sigma h})
=\exp(\varepsilon\operatorname{ad}_{h-\sigma h})
$$
to every parameter order. The constant case is included. This proves
the claimed exact conjugacy and completes the proof.

## Scope, deductions, and open risks

- This is an author proof using the accepted scalar orbit basis and the
  standard BCH formula. It has not yet received an independent check.
- It gives no classification of general polynomial $h$. Products of
  different coordinates introduce additional bracket terms and reductions;
  the extreme-pair argument above cannot simply be reused for those terms.
- In particular, the concurrent degree-four probe has found a candidate
  non-orbit-linear second-order kernel. That does not contradict the present
  theorem, which has a strict subspace hypothesis.
- This result is a bounded structural input, not a novelty score, a long
  manuscript capacity claim, or permission to revive a stopped candidate.
