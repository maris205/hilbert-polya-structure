# Singular arithmetic Gram limits at the critical line

Date: 2026-09-06. Unnumbered proposed contract; not yet independently reviewed
or admitted as a paper. This package distinguishes proof completeness from
novelty and paper-level significance, which remain under source/admission review.

## Claim

Let $L:[1,\infty)\to(0,\infty)$ be measurable and slowly varying at infinity,
bounded above and away from zero on compact intervals. Set
$$a(k)=k^{-1/2}L(k),\qquad F(N)=\sum_{k\le N}a(k)^2.$$
On $\mathcal H=\ell^2(\mathbb N)$ define the finite matrix, extended by zero,
$$T_N(r,m)=\begin{cases}a(r/m),&m\mid r\le N,\\0,&\text{otherwise},\end{cases}
\qquad A_N=F(N)^{-1}T_N^*T_N.$$
The clock is the integer truncation $N$; the observable is the positive Gram
operator and its resolvent, not a zero-counting function.

**Main theorem (proposed).**

1. If $F(N)\to\infty$, then for every fixed $m,n$,
   $$A_N(m,n)\longrightarrow K(m,n)=\frac{\gcd(m,n)}{\sqrt{mn}}.$$
   Nevertheless, for every $\lambda>0$,
   $$(A_N+\lambda I)^{-1}\longrightarrow\lambda^{-1}I\quad\text{strongly},
   \qquad \|A_N\|\longrightarrow\infty.$$
   The quadratic form with matrix $K$ on $c_{00}(\mathbb N)$ has no nonzero
   nonnegative closable minorant. In particular, it has no nonnegative closed
   extension agreeing with it on $c_{00}$.
2. If $F(N)\to F_\infty<\infty$, let $C$ be the maximal rowwise Dirichlet
   convolution operator
   $$(Cx)(r)=\sum_{m\mid r}a(r/m)x(m),\qquad
   D(C)=\{x\in\mathcal H:Cx\in\mathcal H\}.$$
   It is densely defined and closed, and
   $$(A_N+\lambda I)^{-1}\longrightarrow
   (F_\infty^{-1}C^*C+\lambda I)^{-1}\quad\text{strongly}.$$
   This limiting nonnegative self-adjoint operator is nonzero.

Both alternatives allow nonmultiplicative $L$. This is one critical-limit
question, not separate papers for each slowly varying weight or each lemma.

## Status

`PROVABLE AS STATED` is the author's present mathematical assessment, subject
to independent checking. The paper-level increment is provisional. No claim
of global priority, target Euler factors, target zeros, or Hilbert–Pólya
realization is made.

## Assumptions, notation, and classical inputs

Inner products are conjugate-linear in the first argument. A form $q$ on
$c_{00}$ is **closable** if $x_j\to0$ in $\mathcal H$ and
$q[x_j-x_k]\to0$ imply $q[x_j]\to0$. A nonnegative closable minorant means a
nonnegative closable form $b$ defined on $c_{00}$ with $b[x]\le q[x]$ there.
An extension may have a larger domain, but its restriction to $c_{00}$ is
necessarily closable. A form is called purely singular here only in the
explicit sense that every such minorant is zero.

The proof uses unique prime factorization, divergence of $\sum_p1/p$, the
uniform convergence theorem for measurable slowly varying functions, and
standard Hilbert-space facts for closed operators and positive quadratic
forms. The latter identify the form $\|Cx\|^2$ with $C^*C$. No prime-density
asymptotic, infinite-dimensional F. and M. Riesz theorem, or Kakutani theorem
is required. Source ownership is recorded separately; these are classical
inputs, not claimed contributions.

The regular/singular decomposition of general nonnegative forms and the
largest closable minorant are classical, notably Simon (1978), §2. The
explicit prime-tail witness below identifies the singular case for this
arithmetic kernel. Section 3 is a direct recovery-vector/variational
consequence, not a claim to introduce a new general theory of form
relaxation. Simon's §3 monotone-limit results are not silently used as an
arbitrary-entrywise convergence theorem.

## Proof strategy and dependency map

1. A general product kernel admits explicit prime-tail vectors that approximate
   each finite vector in form norm while tending to zero in Hilbert norm.
2. This proves pure singularity and gives low-energy recovery vectors.
3. A variational lemma converts those recovery vectors into resolvent collapse
   for **any** positive operators with the given entrywise limit.
4. Critical regular variation gives precisely this entrywise kernel, without
   a false inference from entrywise convergence to strong operator convergence.
5. In the square-summable alternative, rowwise convolution and a direct
   variational argument give the different, nonzero closed-operator limit.

## Proof

### 1. Product kernels and positivity

For numbers $0\le r_p<1$, indexed by rational primes, put
$$K_r(m,n)=\prod_p r_p^{|v_p(m)-v_p(n)|},$$
where $0^0=1$. Every product in this formula is finite. On $c_{00}$ let
$$q_r[x]=\sum_{m,n}\overline{x(m)}K_r(m,n)x(n).$$
For one prime, the sequence $r^{|j-k|}$ is the Fourier coefficient matrix of
the probability density
$$P_r(e^{it})=\frac{1-r^2}{|1-re^{it}|^2}$$
on the unit circle; for $r=0$ this is $1$. Expanding the two geometric series
and integrating proves that identity. A finite product of these probability
measures shows that $q_r[x]\ge0$ for every finite $x$. Only finitely many
primes occur in a given finite vector, so no infinite product measure is
needed for this assertion.

For a prime $p$ define the isometric shift $S_p e_m=e_{pm}$. If the prime
factors of all indices in the support of $f\in c_{00}$ belong to a finite set
$S$, and $p,\ell\notin S$ are distinct primes, direct factorization gives
$$q_r[S_pf]=q_r[f],\qquad
q_r(f,S_pf)=r_pq_r[f],\qquad
q_r(S_pf,S_\ell f)=r_pr_\ell q_r[f]. \tag{1}$$
The supports of $S_pf$ for different such primes are pairwise disjoint and
disjoint from the support of $f$. This also follows by unique factorization.

### 2. Explicit tail vectors and pure singularity

Suppose $\sum_pr_p^2=\infty$. Fix $f\in c_{00}$ and its finite prime set $S$.
For any finite set $E$ of primes outside $S$, with
$s_E=\sum_{p\in E}r_p^2>0$, define
$$h_E=\frac1{s_E}\sum_{p\in E}r_pS_pf.$$
Disjointness and (1) imply the exact identities
$$\|h_E\|^2=\frac{\|f\|^2}{s_E},\qquad
q_r(f,h_E)=q_r[f],$$
$$q_r[h_E]=q_r[f]\left(1+
\frac{\sum_{p\in E}r_p^2(1-r_p^2)}{s_E^2}\right),$$
and hence
$$q_r[h_E-f]=q_r[f]
\frac{\sum_{p\in E}r_p^2(1-r_p^2)}{s_E^2}
\le\frac{q_r[f]}{s_E}. \tag{2}$$
Choose finite $E_j$ outside $S$ with $s_{E_j}\to\infty$. Thus $h_{E_j}\to0$
in $\mathcal H$, whereas $q_r[h_{E_j}-f]\to0$.

Let $b\le q_r$ be a nonnegative closable minorant. The triangle inequality
for the form seminorm gives $b[h_{E_j}-h_{E_k}]\to0$. Closability and
$h_{E_j}\to0$ then imply $b[h_{E_j}]\to0$. Since also
$b[h_{E_j}-f]\le q_r[h_{E_j}-f]\to0$, the same triangle inequality yields
$b[f]=0$. This holds for every $f\in c_{00}$, proving pure singularity.
Since $q_r[e_1]=1$, the form itself is nonzero and cannot be closable.

The related vectors $u_j=f-h_{E_j}$ satisfy
$$u_j\to f\text{ in }\mathcal H,\qquad q_r[u_j]\to0. \tag{3}$$
They will be used for resolvents; a nonclosability witness alone would not
justify an operator-limit statement without this additional argument.

For context, the converse closability statement also has an elementary proof.
If $\sum_pr_p^2<\infty$, every column of $K_r$ is in $\ell^2$: for fixed $m$,
the factors at primes dividing $m$ are finite sums plus convergent geometric
tails; the remaining factors have product $\prod_{p\nmid m}(1-r_p^2)^{-1}<\infty$.
Thus $K_r$ defines a nonnegative symmetric operator on $c_{00}$, whose
quadratic form is closable. This converse is supporting operator theory, not
the proposed main increment. Together the two arguments give the exact
closability criterion $\sum_pr_p^2<\infty$ for this product-kernel class.

### 3. A universal variational collapse lemma

Let $B_N$ be bounded nonnegative self-adjoint operators on $\mathcal H$ whose
matrix entries converge to $K_r(m,n)$, with $\sum_pr_p^2=\infty$.
For each fixed $u\in c_{00}$, finite summation gives
$$\langle u,B_Nu\rangle\to q_r[u]. \tag{4}$$
For each $g\in\mathcal H$, there exist finite vectors $v_j\to g$ with
$q_r[v_j]\to0$: first approximate $g$ by finite $f_j$, then apply (3) to each
$f_j$, choosing its tail far enough to make both errors smaller than $1/j$.
By (4), choose increasing integers $N_j$ such that for all $N\ge N_j$,
$$|\langle v_j,B_Nv_j\rangle-q_r[v_j]|<1/j.$$
Let $j(N)$ tend to infinity slowly enough that $N\ge N_{j(N)}$. Then
$$v_{j(N)}\to g,\qquad\langle v_{j(N)},B_Nv_{j(N)}\rangle\to0. \tag{5}$$

Fix $\lambda>0$ and $f\in\mathcal H$, and set
$x_N=(B_N+\lambda I)^{-1}f$. Completing the square, or differentiating the
bounded quadratic functional, shows that $x_N$ minimizes
$$J_N(x)=\langle x,B_Nx\rangle+
\lambda\|x-\lambda^{-1}f\|^2.$$
Apply (5) with $g=\lambda^{-1}f$. Nonnegativity and minimality give
$$0\le\lambda\|x_N-\lambda^{-1}f\|^2\le J_N(x_N)
\le J_N(v_{j(N)})\longrightarrow0.$$
This proves strong resolvent convergence to the zero operator.

In addition $\|B_N\|\to\infty$. Otherwise a subsequence with uniformly
bounded norms, together with (4), would make $q_r$ a bounded form on $c_{00}$,
and hence a nonzero closable minorant of itself. More explicitly, unboundedness
of $q_r$ supplies, for every $M$, a finite unit vector $u$ with $q_r[u]>2M$;
then (4) forces $\|B_N\|>M$ for every sufficiently large $N$.

This lemma does not assume monotonicity, a Følner condition, or a specific
finite-section geometry. Positivity and entrywise convergence are essential
to the proof. It makes no assertion for arbitrary signed approximants.

### 4. Critical regular variation

Assume $F(N)\to\infty$. We first prove the two estimates
$$L(N)^2=o(F(N)),\qquad \frac{F(N/c)}{F(N)}\to1
\quad(c\ge1\text{ fixed}), \tag{6}$$
where floors in $F$ are understood. For fixed $A>1$, uniform slow variation
on $[1/A,1]$ gives
$$\frac1{L(N)^2}\sum_{N/A\le k\le N}\frac{L(k)^2}{k}
\longrightarrow\log A.$$
It follows that $\liminf F(N)/L(N)^2\ge\log A$. Letting $A$ be arbitrarily
large proves the first assertion of (6). Applying the same uniform estimate
on $[1/c,1]$ bounds $F(N)-F(N/c)$ by a constant times $L(N)^2$ for large $N$.
This proves the second assertion. The case $c=1$ is immediate.

Let $\ell=\operatorname{lcm}(m,n)$. Direct multiplication of the finite
divisibility matrices yields, once $N\ge\ell$,
$$A_N(m,n)=\frac{\sqrt{mn}}{\ell F(N)}
\sum_{k\le N/\ell}\frac{L(k\ell/m)L(k\ell/n)}{k}. \tag{7}$$
For fixed $m,n$, the ratio of each summand in (7) to $L(k)^2/k$ tends to one
as $k\to\infty$. Since their cumulative denominator diverges, splitting the
sum at a fixed sufficiently large index proves
$$\sum_{k\le N/\ell}\frac{L(k\ell/m)L(k\ell/n)}{k}
\sim F(N/\ell)\sim F(N).$$
The finite initial segment is negligible after division by $F(N/\ell)$;
positivity and the eventual ratio bounds justify both inequalities. Thus (7)
converges to $\sqrt{mn}/\ell=\gcd(m,n)/\sqrt{mn}$.

This kernel is $K_r$ with $r_p=p^{-1/2}$, so $\sum_pr_p^2=\sum_p1/p=\infty$.
Sections 2 and 3 prove all assertions in alternative 1. Notice in particular
that $A_N(1,1)=1$ for every $N$, despite the strong-resolvent zero limit.
Neither entrywise convergence nor this diagonal identity gives strong
operator convergence.

### 5. The square-summable alternative

Suppose $F_\infty<\infty$, so $a\in\ell^2$. Each row of the formal
convolution $C$ has finitely many entries. If $x_j\to x$ and $Cx_j\to y$ in
$\mathcal H$, continuity of every such row gives $(Cx)(r)=y(r)$ for every
$r$. Hence $C$ on its stated maximal domain is closed. Each column has norm
$\|a\|_2$, so $c_{00}\subset D(C)$ and $C$ is densely defined.

Write $P_N$ for the first-coordinate projection. For arbitrary $x\in\mathcal H$
the finite vector $T_Nx$ equals the first $N$ rows of the formal convolution:
an input with index greater than $N$ cannot divide any row at most $N$.
Consequently
$$\langle x,A_Nx\rangle=F(N)^{-1}
\sum_{r\le N}\left|\sum_{m\mid r}a(r/m)x(m)\right|^2. \tag{8}$$
For $x\in D(C)$, (8) converges to $q_\infty[x]=F_\infty^{-1}\|Cx\|^2$.

We give a direct variational convergence proof, avoiding an unproved assertion
that coordinate truncations form a graph core for $C$.
For fixed $f$ and $\lambda>0$, put $x_N=(A_N+\lambda I)^{-1}f$.
The resolvent bound gives $\|x_N\|\le\lambda^{-1}\|f\|$. If a subsequence
converges weakly to $x$, continuity of each finite row and (8) imply
$$q_\infty[x]\le\liminf_N\langle x_N,A_Nx_N\rangle, \tag{9}$$
with $q_\infty[x]=\infty$ outside $D(C)$. To see (9), first retain only the
first $R$ rows, use $F(N)\to F_\infty$, and then let $R\to\infty$.
Weak lower semicontinuity also applies to the Hilbert norm.

Let $x_*=(F_\infty^{-1}C^*C+\lambda I)^{-1}f$, the unique minimizer on $D(C)$
of $q_\infty[x]+\lambda\|x\|^2-2\operatorname{Re}\langle f,x\rangle$.
For this fixed vector, (8) converges to $q_\infty[x_*]$. Minimality of $x_N$
and (9) imply that every weak cluster point is $x_*$. They also imply convergence
of the minimum values to the limiting minimum. Existence of weakly convergent
subsequences follows from the uniform norm bound in this separable Hilbert
space. Therefore the whole sequence converges weakly to $x_*$.

For a direct strong estimate, set
$$E_N(x)=\langle x,A_Nx\rangle+\lambda\|x\|^2
-2\operatorname{Re}\langle f,x\rangle.$$
The resolvent equation gives
$$E_N(x_*)-E_N(x_N)
=\langle x_*-x_N,A_N(x_*-x_N)\rangle+
\lambda\|x_*-x_N\|^2\ge\lambda\|x_*-x_N\|^2.$$
Both functional values tend to the same limiting minimum, so strong convergence
follows. Finally $q_\infty[e_1]=F_\infty^{-1}\sum_ra(r)^2=1$, showing that
the limiting operator is not zero. This completes the theorem.

## Boundary examples and failure controls

For $L(x)=(\log(ex))^{-\beta}$, elementary integral comparison gives
$F_\infty<\infty$ exactly when $\beta>1/2$. Thus the two alternatives occur
inside the same critical power $k^{-1/2}$; slow variation alone does not select
one. The divergence assumption in alternative 1 must not be omitted.

For a finite prime set, or for $\sum_pr_p^2<\infty$, section 2 has no divergent
tail and the nonclosability conclusion is false. Positivity of all finite
matrices by itself is insufficient, but is not an obstruction either: the
summable product-kernel case gives a positive closable comparison.

## Corrections or missing assumptions

No theorem correction is presently required by the author. The maximal-domain
description in alternative 2 is intentional; no unsupported graph-core or
essential-self-adjointness claim is included. In alternative 1, nonexistence
means a nonnegative closed form agreeing with $K$ on $c_{00}$ in this fixed
$\ell^2$ space, not all possible renormalizations, Hilbert spaces, or target
spectral realizations.

## Open risks

- Non-author verification of the pure-singularity/variational argument and the
  arbitrary slowly varying quantifiers is still required.
- Closest-source ownership and substantive increment need adjudication; a
  correct proof is not a priority certificate.
- No formal Route-A evaluation, manuscript, compiled PDF, or release checks
  have been performed for this candidate.
