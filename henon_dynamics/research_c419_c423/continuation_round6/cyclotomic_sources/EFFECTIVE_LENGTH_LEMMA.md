# An explicit root-of-unity length bound

Date: 2026-09-08 UTC. Auxiliary input to the unchanged AF5-C contract in
[the sixth-pass plan](../SCOUT_PLAN.md), not a separate candidate or admission.
This document supplies a deliberately coarse effective substitute for the
initial Loxton bound. No mathematical program was executed to obtain it.

## Claim

For an integer $H\geq1$, define
$$
B_H=\prod_{\substack{p\text{ prime}\\p\leq4H}}(p-1),\qquad
L_H=H B_H(2H)^{2H},\qquad M_H=L_H+2.
$$
Every cyclotomic algebraic integer $\alpha$ of house at most $\sqrt H$
is a sum of at most $L_H$ roots of unity, and is a sum of exactly $M_H$
roots of unity. Repetitions are allowed. Zero is included.

The conclusion also holds under the weaker assumption $A(\alpha)\leq H$,
where $A$ is the mean squared modulus of all conjugates, defined below.
This stronger internal formulation is a proof device, not a change to the
AF5-C periodic-point question.

All constants are explicit integers. If a formula without a prime product
is preferred, $H(4H)^{4H}(2H)^{2H}$ can replace $L_H$ throughout.

For $q=|c|$ with $c\in\mathbb Z$, the choice $H=2q+4$ applies to every
coordinate whose house is at most $1+\sqrt{1+q}$. Thus the initial torus
dimension in AF5-C can be chosen to be $2M_H$ by an integer-arithmetic
formula, without an unspecified asymptotic constant.

## Status and assumptions

**PROVABLE AS STATED** as an auxiliary length lemma. The proof below does
not assert the global atlas algorithm, a practical running time, optimality,
or independent research novelty. Non-author mathematical review is still
required by the parent contract.

Assumptions are characteristic zero, $H\in\mathbb Z_{\geq1}$, and
$\alpha\in\mathbb Q^{\rm cyc}$ integral over $\mathbb Z$. Here
$\mathbb Q^{\rm cyc}=\bigcup_{N\geq1}\mathbb Q(\zeta_N)$ and
$\zeta_N=e^{2\pi i/N}$.

## Notation and classical inputs

For any algebraic number $\beta$ and a number field $K$ containing it,
$$
A(\beta)=\frac{1}{[K:\mathbb Q]}
\sum_{\sigma:K\hookrightarrow\mathbb C}|\sigma(\beta)|^2.
$$
Every embedding of $\mathbb Q(\beta)$ has the same number of extensions
to $K$, so this definition is independent of $K$. It satisfies
$A(0)=0$, $A(\xi\beta)=A(\beta)$ for a root of unity $\xi$, and
$A(\beta)\leq\operatorname{house}(\beta)^2$. If $\beta\neq0$ is an
algebraic integer, then $A(\beta)\geq1$: its nonzero integer norm has
absolute value at least one, and the arithmetic-geometric mean inequality
applied to the positive numbers $|\sigma(\beta)|^2$ gives the assertion.

Write $\ell(\beta)$ for the least number of roots of unity in a sum equal
to a cyclotomic integer $\beta$, taking $\ell(0)=0$. It is finite because
$\mathcal O_{\mathbb Q(\zeta_N)}=\mathbb Z[\zeta_N]$ and integer
coefficients can be expanded into repeated roots; a negative sign is itself
absorbed into a root of unity. In particular,
$$
\ell(\xi\beta)=\ell(\beta),\qquad
\ell(\beta_1+\cdots+\beta_s)\leq\sum_i\ell(\beta_i).
$$
The only structural input about cyclotomic integers is the usual ring of
integers theorem just stated, together with elementary cyclotomic extension
degrees. The two trace identities used below are proved here. Their
classical source locators are:

- Malik–Stan–Zaharescu, *The Siegel norm, the length function and character
  values of finite groups* (2014), author-hosted
  [PDF](https://sites.math.rutgers.edu/~am2365/MSZ.pdf), Lemmas 2.1 and 2.2
  on PDF page 4 and the unnumbered Corollary 1 in §3 on PDF page 8.
  The statements apply to a specified containing cyclotomic field, without
  requiring minimal conductor.
- Bajpai–Das–Kedlaya–Le–Lee–Leudière–Mello, arXiv:2510.20435v1,
  [§§2.3–2.4](https://arxiv.org/html/2510.20435v1), Remark 2.9,
  Lemmas 2.10 and 2.12, especially equations (7), (9) and the proof of
  Lemma 2.12(c). These restate the trace identities and explain the
  largest equal-coefficient class normalization. Their minimal-level
  convention is not imported into the proof below.

These are classical inputs, not a claim that either paper states our coarse
formula $L_H$. Source existence, version and access details are kept in
[SOURCE_AUDIT.md](SOURCE_AUDIT.md).

## Strategy and dependency map

1. Prove the prime and prime-power trace decompositions with integral
   coefficients.
2. In fields with only primes at most $4H$, prove a length bound by induction
   on the containing-field index, independent of prime-power exponents.
3. Remove larger primes. At every genuine branch, the mean square drops
   by at least $1/2$ along each child, and the branching factor is at most
   $2H$. Unary steps cost no length and strictly decrease the ambient index.
4. Bound the number of leaves, apply the small-prime estimate, and pad the
   resulting sums with vanishing sums of lengths two and three.

## Proof

### 1. Ambient-field bookkeeping and exact decompositions

Choose any $N\geq1$ with $\beta\in\mathbb Q(\zeta_N)$. Minimality is
not needed. Whenever $N\equiv2\pmod4$, replace it by $N/2$; the field is
unchanged. Consequently an index used below is odd or divisible by four.
Every child is tagged by an index no larger than $N/p<N$, with the same
normalization applied if necessary. No statement that the tag is the
minimal conductor is used.

Suppose first $p^r\Vert N$ with $r\geq2$, write $m=N/p^r$, and put
$K=\mathbb Q(\zeta_{N/p})$, $\zeta=\zeta_{p^r}$. Since
$\mathbb Q(\zeta_N)=K(\zeta)$ and
$$
[\mathbb Q(\zeta_N):K]=\frac{\varphi(N)}{\varphi(N/p)}=p,
$$
the powers $1,\zeta,\ldots,\zeta^{p-1}$ form a $K$-basis. The equality
of integer rings
$\mathbb Z[\zeta_N]=\mathbb Z[\zeta_{N/p}][\zeta]$ follows by expressing
$\zeta_N$ using the coprime-order roots $\zeta_m,\zeta_{p^r}$ and conversely.
Grouping an integral polynomial in $\zeta$ modulo $p$ therefore gives
$$
\beta=\sum_{j=0}^{p-1}a_j\zeta^j,
\qquad a_j\in\mathbb Z[\zeta_{N/p}].                     \tag{1}
$$
The relative automorphisms send $\zeta$ to $\zeta\zeta_p^t$,
$0\leq t<p$. Averaging squared moduli over these automorphisms kills
cross terms by $\sum_{t=0}^{p-1}\zeta_p^{t(i-j)}=0$ for $i\neq j$.
Averaging also over embeddings of $K$ yields
$$
A(\beta)=\sum_{j=0}^{p-1}A(a_j).                        \tag{2}
$$
This includes $p=2,r=2$; the degree ratio is two, even though the child
index may subsequently normalize from $2m$ to $m$.

Suppose next $p\Vert N$. The normalization ensures $p$ is odd. Put
$m=N/p$ and $K=\mathbb Q(\zeta_m)$. The compositum has relative degree
$p-1$, and the minimal polynomial of $\zeta_p$ over $K$ is
$1+X+\cdots+X^{p-1}$. The integer-ring theorem gives
$$
\beta=\sum_{j=0}^{p-1}a_j\zeta_p^j,
\qquad a_j\in\mathbb Z[\zeta_m].                        \tag{3}
$$
Subtracting a common coefficient from every $a_j$ leaves $\beta$
unchanged. In particular one coefficient can always be set to zero.

For fixed complex numbers $b_0,\ldots,b_{p-1}$, orthogonality gives
$$
\sum_{t=1}^{p-1}\left|\sum_j b_j\zeta_p^{jt}\right|^2
=p\sum_j|b_j|^2-\left|\sum_jb_j\right|^2
=\sum_{i<j}|b_i-b_j|^2.
$$
Apply this at every embedding of $K$. Division by $p-1$ proves
$$
(p-1)A(\beta)=\sum_{0\leq i<j<p}A(a_i-a_j).             \tag{4}
$$
After a common shift, suppose exactly $X$ coefficients are nonzero.
Separate zero–nonzero from nonzero–nonzero pairs in (4), writing the
nonzero coefficients as $\gamma_1,\ldots,\gamma_X$. Then
$$
(p-1)A(\beta)
=(p-X)\sum_{i=1}^X A(\gamma_i)
 +\sum_{1\leq i<j\leq X}A(\gamma_i-\gamma_j).            \tag{5}
$$

### 2. A small-prime bound independent of prime powers

For an index $N$, define
$$
B(N)=\prod_{p\mid N}(p-1),\qquad B(1)=1.
$$
We prove for every cyclotomic integer $\beta\in\mathbb Q(\zeta_N)$ that
$$
\ell(\beta)\leq B(N)A(\beta).                           \tag{6}
$$
Use strong induction on the normalized index $N$; zero satisfies (6).
If $N=1$, $\beta$ is a rational integer and
$\ell(\beta)\leq|\beta|\leq\beta^2=A(\beta)$.

If $p^2\mid N$, apply (1), induction to each coefficient and (2):
$$
\ell(\beta)\leq\sum_j\ell(a_j)
\leq B(N/p)\sum_jA(a_j)=B(N)A(\beta).
$$
Normalizing the child index cannot increase $B$; in the only removed-prime
case the prime is two and its factor $p-1$ equals one.

If no square divides $N>1$, choose any prime $p\mid N$ and use (3) with
one coefficient zero, so $X\leq p-1$. Positivity in (5) gives
$\sum_iA(\gamma_i)\leq(p-1)A(\beta)$ because $p-X\geq1$.
Induction in $\mathbb Q(\zeta_{N/p})$ now gives
$$
\ell(\beta)\leq\sum_i\ell(\gamma_i)
\leq B(N/p)\sum_iA(\gamma_i)
\leq B(N)A(\beta).
$$
This completes the induction. In particular, if all primes dividing $N$
are at most $4H$ and $A(\beta)\leq H$, then
$$
\ell(\beta)\leq B_H H.                                 \tag{7}
$$

### 3. Large-prime descent and the height drop

Begin with nonzero $\alpha$ satisfying $A(\alpha)\leq H$, tagged by a
normalized containing index. At a nonzero node $\beta$, if its tag has a
prime $p>4H$, perform the decomposition for that prime. Discard zero
coefficients and regard every remaining coefficient as a child. Every edge
also records the root-of-unity multiplier from (1) or (3). Its modulus at
each embedding is one, so accumulated edge multipliers change neither
$A$ nor length. If there is no such large prime, stop at that node.

For the prime-power case (2), let $a=A(\beta)$ and let $X$ be the number
of children. Every child is a nonzero algebraic integer, hence
$$
X\leq a\leq H,
\qquad A(\gamma_i)\leq a-(X-1).                         \tag{8}
$$
When $X=1$ this is a unary root twist; when $X\geq2$, every child has
mean square at most $a-1$.

For $p\Vert N$, shift the coefficients in (3) by a value occurring most
frequently, to make that value zero. Let its multiplicity be $r$, so
$X=p-r$. If the distinct coefficient values have multiplicities
$r_1,\ldots,r_s$, each $r_i\leq r$ and $\sum_i r_i=p$. The number of
pairs of unequal coefficients is
$$
\frac{p^2-\sum_i r_i^2}{2}
\geq\frac{p^2-rp}{2}=\frac{pX}{2}.
$$
Every unequal difference is a nonzero algebraic integer and has $A\geq1$.
Equation (4) therefore implies
$$
(p-1)a\geq pX/2,\qquad X\leq2a\leq2H.                 \tag{9}
$$
For $X\geq2$, put $S=\sum_i A(\gamma_i)$. Equation (5) implies
$S\leq a(p-1)/(p-X)$, so for each child
$$
\begin{aligned}
A(\gamma_i)
&\leq S-(X-1)\\
&\leq a\frac{p-1}{p-X}-(X-1)\\
&=a-(X-1)\left(1-\frac{a}{p-X}\right)\\
&\leq a-\tfrac12.
\end{aligned}                                         \tag{10}
$$
The final inequality uses $p>4H$, $X\leq2H$ and $a\leq H$, which give
$p-X>2H\geq2a$. For $X=1$, the equality
$\beta=\gamma_1\zeta_p^j$ gives $A(\gamma_1)=a$ directly.

Thus every child again satisfies $A\leq H$. A genuine branch has at most
$2H$ children and drops $A$ by at least $1/2$ along every outgoing edge.

### 4. Termination and branch accounting

Every edge strictly decreases the positive ambient index. This proves
termination of every path, including arbitrarily long sequences of unary
root-twist steps. More formally the recursive construction is a finite
tree by induction on the initial index: a node has finitely many children,
all of whose indices are smaller. It is not necessary to bound the length
of a unary run uniformly in $H$.

Suppress unary nodes in this finite tree. Along any path with $b$ genuine
branches, the successive nonzero mean squares are bounded above by
$H,H-1/2,\ldots,H-b/2$ and bounded below by one. Hence
$b\leq2(H-1)\leq2H$. A finite rooted tree of depth at most $2H$ and
branching at most $2H$ has at most $(2H)^{2H}$ leaves; this follows by
induction on depth, with one leaf at depth zero and at most $2H$ child
subtrees at each subsequent depth. Suppressing unary nodes does not alter
the leaf count.

Each terminal coefficient lies in a field with no prime divisor larger
than $4H$, and has $A\leq H$. By (7) it is a sum of at most $B_H H$
roots of unity. Substituting all leaf representations back up the tree
multiplies summands only by accumulated roots of unity. Consequently
$$
\ell(\alpha)\leq (2H)^{2H}B_H H=L_H.                    \tag{11}
$$
The same bound holds for zero using its empty sum. This proves the
mean-square formulation and hence the original house formulation.

### 5. Fixed-length padding and the Hénon parameter

Let a representation have length $\ell\leq L_H$. Its gap to $M_H=L_H+2$
is an integer $d\geq2$. If $d$ is even use $d/2$ copies of
$1+(-1)=0$; if $d$ is odd use one copy of
$1+\zeta_3+\zeta_3^2=0$ and $(d-3)/2$ copies of $1+(-1)=0$.
This gives exactly $M_H$ nonzero roots of unity, including when the
represented coordinate is zero. No zero torus coordinate is introduced.

There are at most $4H$ primes at most $4H$ and each $p-1\leq4H$, so
$B_H\leq(4H)^{4H}$, proving the displayed elementary majorant.
Finally, for $q\geq0$,
$$
(1+\sqrt{1+q})^2=q+2+2\sqrt{1+q}\leq2q+4,
$$
because $(q+2)^2-4(q+1)=q^2\geq0$. Thus $H=2|c|+4$ suffices. ∎

## Corrections, boundaries and verification status

- The argument uses a decreasing **containing-field index**, not a claim
  that every coefficient or root twist has a particular minimal conductor.
- The root-length bound is uniform over all cyclotomic fields; the much
  simpler fixed-field enumeration algorithm of Malik–Stan–Zaharescu alone
  would not establish that uniformity.
- This proof does not use an unspecified Loxton constant, the
  Loxton–Kedlaya multiplicative rank, or a bound on the conductor of the
  original coordinate. The latter can be arbitrarily large even for a
  single root of unity.
- The local proof checks cover zero, $H=1$, rational integers, the
  $p=2,r=2$ degree change, nonminimal ambient fields, repeated
  coefficients, repeated roots and unary paths. No finite census is
  offered as a proof of the uniform claim.
- The bound is extraordinarily large and establishes theoretical
  computability only. This classical trace-based auxiliary argument is
  not counted as an independent paper-level increment.

AI-assisted authorship and primary-source verification are disclosed here;
no human-read attestation or external peer review is asserted.
