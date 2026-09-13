# Uniform arbitrary-period trace coordinates at fixed Hénon Jacobian

Date: 2026-09-05. New author-side Paper29 viability proof. No candidate
PASS, project, scientific/publication lock or manuscript is created.
The earlier first-integral, cancellation and centralizer candidates are
not being enlarged or repackaged.

## Claim

Fix an integer $d\ge2$ and a real number $B>0$. Put $r=d-1$ and
$$
f_u(z)=z^d-1+\sum_{j=0}^{d-2}u_jz^j,
\qquad
p_{A,u}(x)=A^d f_u(x/A)
=x^d-A^d+\sum_{j=0}^{d-2}u_jA^{d-j}x^j.
$$
For $b\in\mathbb C$ set
$$H_{b,p}(x,y)=(p(x)+by,x).$$
Its Jacobian determinant is $-b$, so $b=-1$ is the area-preserving
slice. All headline automorphism statements below restrict to $b\ne0$.

There exist constants $\eta>0$, $A_0>0$ and $M<\infty$, depending
only on $d,B$, with the following property. Whenever
$$
|A|>A_0,\qquad 0<|b|\le B,\qquad
\max_j|u_j|<\eta,
$$
and whenever an arbitrary period vector
$$\boldsymbol n=(n_1,\ldots,n_r)\in\mathbb Z_{>0}^{r}$$
is prescribed, one can choose $r$ labeled pairwise-disjoint simple cycles
of $H_{b,p_{A,u}}$, with exact periods $n_i$, such that their return traces
$\rho_i$ satisfy
$$
K_{ij}:=\frac{1}{n_i\rho_i}\frac{\partial\rho_i}{\partial u_j},
\qquad 1\le i\le r,\quad0\le j\le d-2,
$$
$$
\boxed{\quad |K_{ij}|\le M,\qquad
|\det K|\ge\frac{(d-1)!}{2^d d^{d/2}}>0.\quad}
\tag{1}
$$
The traces do not vanish. Derivatives use the holomorphic continuation
of the chosen cycles on the common $u$-neighborhood. The constants and
that neighborhood are independent of every $n_i$.

The cycle choice uses a permutation of the nontrivial $d$-th roots of
unity depending on $\boldsymbol n$, but not on $A,b,u$. In particular,
the same parameter region works for **all** prescribed period vectors,
not merely one vector at a time or a countable intersection of unspecified
generic loci. The estimates concern the displayed normalized differential,
not an unscaled Euclidean condition number in the original coefficients.

Writing $p(x)=x^d+\sum_{j=0}^{d-2}a_jx^j$, the coordinate change is
diagonal and invertible for $A\ne0$:
$$
\frac{\partial\rho_i}{\partial u_j}
=A^{d-j}\frac{\partial\rho_i}{\partial a_j}.
$$
Consequently the ordinary trace Jacobian with respect to the $a_j$ is
invertible as well. For each fixed $b\ne0$ and each period vector,
at least one irreducible component of the simple exact disjoint
cycle-marked incidence has a dominant, generically étale trace map to
$\mathbb A^r$.

No assertion is made for every incidence component, for every polynomial,
or for global injectivity. The construction does not identify the selected
component with Paper18's scalar-boundary component.

## Status, dependencies and strategy

**Author status: PROVABLE AS STATED. Independent review: requested.**

This proof uses finite-dimensional holomorphic inverse functions, the
contraction principle with the sup norm, Cauchy derivative bounds, a
Vandermonde determinant and elementary $2\times2$ monodromy. It does not
infer a fixed nonzero $b$ theorem by specializing a generic-$b$ result.
The anti-integrable construction is established methodology and is not
claimed as a new general technique. The literature/value assessment must
evaluate the exact uniform trace-coordinate assertion separately.

Dependency order:

1. Uniform inverse branches of $f_u$ near the roots of $z^d-1$.
2. Period-independent contraction for every cyclic symbolic word.
3. A second cyclic contraction for a Riccati slope, giving an exact
   eigenvalue product and a period-uniform normalized trace differential.
4. A root-permutation averaging certificate with a uniform determinant gap.
5. Perturbation on one common parameter neighborhood, then algebraic descent
   from a simple marked tuple to the relevant incidence component.

## Proof

### 1. Inverse branches with fixed neighborhoods

Label the $d$ distinct roots of unity as $\alpha_1,\ldots,\alpha_d$,
with $\alpha_d=1$. The derivative of $f_0$ at each root is nonzero.
The holomorphic implicit function theorem gives, after choosing positive
constants $\eta_1,w_1$, inverse branches
$$
g_s(u,w),\qquad f_u(g_s(u,w))=w,
\qquad \alpha_s(u):=g_s(u,0),\quad1\le s\le d,
$$
on a product of a $u$-polydisc and a $w$-disc, containing the closures
$|u_j|\le2\eta_1$ and $|w|\le2w_1$. Shrink them so that the images
for different $s$ remain in disjoint fixed root discs.

All functions in this finite collection and their first derivatives are
bounded on the indicated compact product. There are constants $C_1,R_1$
such that
$$
|\partial_w g_s|\le C_1,\qquad
|g_s(u,w)-\alpha_s(u)|\le C_1|w|,\qquad
|\alpha_s(u)|\le R_1.
$$
The second inequality follows by integrating $\partial_wg_s$ along the
straight segment from zero to $w$. There is also $\mu>0$ such that
$$|f_u'(\alpha_s(u))|\ge4\mu$$
on this compact $u$-polydisc. Further shrink a root-disc radius $h>0$
so that $|f_u'(z)|\ge3\mu$ whenever
$|z-\alpha_s(u)|\le h$; these discs remain pairwise disjoint.

All ensuing constructions are made first on a slightly larger open
parameter product than the final region, including $|b|<B+1$. This leaves
room for uniform Cauchy estimates and for the closed bound $|b|\le B$.

### 2. Periodic words and a period-independent orbit contraction

Put $\epsilon=A^{1-d}$. An ordered $n$-cycle of $H_{b,p_{A,u}}$ can
be written as $(Az_k,Az_{k-1})$, with $k$ read modulo $n$, where
$$
f_u(z_k)=\epsilon(z_{k+1}-bz_{k-1}).
\tag{2}
$$
Fix any cyclic word $\boldsymbol s=(s_0,\ldots,s_{n-1})$ in the
alphabet $\{1,\ldots,d\}$. On the product of discs
$|z_k-\alpha_{s_k}(u)|\le h$, define
$$
\mathcal F(z)_k=
g_{s_k}\bigl(u,\epsilon(z_{k+1}-bz_{k-1})\bigr).
\tag{3}
$$
The sup norm is used for every $n$. Coordinates in these discs have
absolute value at most $R_1+h$. Thus the arguments of $g_s$ have
absolute value at most
$$|\epsilon|(1+B+1)(R_1+h).$$
For all sufficiently small $|\epsilon|$, this is less than $w_1$, and
$C_1|\epsilon|(B+2)(R_1+h)<h$. Hence (3) maps the product into itself.
For two points of this product, its Lipschitz constant is at most
$$C_1|\epsilon|(B+2),$$
which can be made less than $1/2$ independently of $n$ and the word.

The contraction principle gives a unique solution
$z^{\boldsymbol s}(u,\epsilon,b)$ of (2) in these discs. Iterating
(3) from the root vector yields uniform limits of holomorphic functions,
so the solution is holomorphic in the parameters. It satisfies
$$
\max_k|z_k-\alpha_{s_k}(u)|\le C_2|\epsilon|,
\tag{4}
$$
where $C_2$ is independent of the period and word.

Apply Cauchy's formula in each coefficient variable on a smaller common
$u$-polydisc. Since (4) holds on the larger one, there is $C_3$ such that
$$
\max_{k,j}\left|
\partial_{u_j}z_k-\partial_{u_j}\alpha_{s_k}(u)
\right|\le C_3|\epsilon|.
\tag{5}
$$
No factor of $n$ occurs: Cauchy's formula is applied to each scalar
coordinate with the same radius and the same bound. The convergence and
the bounds hold uniformly over the finite-dimensional spaces of every
period because the contraction constants do not depend on their dimension.

When $n=1$ or $n=2$, some cyclic neighbors coincide. Their coefficients
then add, but the estimate by $1+|b|$ used above remains valid. Thus
neither small period is excluded.

If the word has least cyclic period $n$, so does the resulting orbit.
A smaller orbit period would make the sequence $z_k$ periodic with that
smaller period; disjointness of the root discs would force the same
period for its symbolic word. Two words not related by cyclic shift
produce disjoint orbits, by the same root-disc argument. This reasoning
uses the actual phase-space points, not just a formal symbol count.

### 3. Uniform slope contraction and the exact trace identity

For a solution of (2), put
$$a_k=f_u'(z_k),\qquad \beta_s(u)=f_u'(\alpha_s(u)).$$
Equations (4)--(5) and the bounded derivatives of $f_u$ imply
$$
a_k=\beta_{s_k}(u)+O(\epsilon)
\quad\text{in the coefficient }C^1\text{ norm},
\tag{6}
$$
uniformly in $n,k,\boldsymbol s,b$. The bounds retain $|a_k|\ge2\mu$
after decreasing the common $\epsilon$ radius if needed.

The derivative in the scaled coordinates is
$$M_k=\begin{pmatrix}\epsilon^{-1}a_k&b\\1&0\end{pmatrix}.$$
On cyclic sequences near the $a_k$, solve
$$w_k=a_k+\frac{b\epsilon^2}{w_{k-1}}.\tag{7}$$
For example, use the product $|w_k-a_k|\le\mu/2$. Denominators there
are at least $3\mu/2$ in absolute value. The right side maps this product
into itself and is a contraction when $|\epsilon|$ is small: its
displacement is bounded by $(B+1)|\epsilon|^2/(3\mu/2)$, and its
Lipschitz constant by $(B+1)|\epsilon|^2/(3\mu/2)^2$. Both bounds
are independent of period.

There is a unique cyclic solution, holomorphic in the same parameters,
with $w_k-a_k=O(\epsilon^2)$. Cauchy's formula on a further smaller
common coefficient neighborhood gives the same estimate in coefficient
$C^1$. Consequently
$$
|w_k|\ge\mu,\qquad
\partial_{u_j}\log w_k
=\partial_{u_j}\log\beta_{s_k}(u)+O(\epsilon),
\tag{8}
$$
with period-independent constants. Here and below $\partial\log h$
means $(\partial h)/h$ for a nonzero holomorphic function; no global
choice of a multivalued logarithm is required.

The following identity fixes the indexing of the periodic line:
$$
M_k\binom{1}{\epsilon/w_{k-1}}
=\epsilon^{-1}w_k\binom{1}{\epsilon/w_k}.
$$
Hence the return matrix has an eigenvalue
$$\lambda_u=\epsilon^{-n}\prod_{k=0}^{n-1}w_k.$$
Its determinant is $(-b)^n$, so the other eigenvalue is
$$\lambda_s=\frac{(-b)^n}{\lambda_u}.$$
After imposing the uniform inequalities
$$\mu/|\epsilon|>2,\qquad B|\epsilon|/\mu<1/2,$$
they satisfy
$$|\lambda_u|>2^n,\qquad |\lambda_s|<2^{-n}.$$
Thus the cycles are simple: neither return eigenvalue is one. The
eigenvalues are distinct, and the return trace $\rho=\lambda_u+\lambda_s$
is nonzero.

Set
$$
\theta=\frac{((-b)\epsilon^2)^n}{(\prod_k w_k)^2}.
$$
There is a constant $0<q<1$ independent of $n$ such that
$|\theta|\le q^n$, with $q$ tending to zero as $\epsilon$ tends to zero.
The exact trace expression is
$$\rho=\epsilon^{-n}\prod_k w_k\,(1+\theta).$$
Differentiate with respect to a coefficient $u_j$, holding $A,b$ fixed.
Since $\partial\theta=-2\theta\sum_k\partial\log w_k$, one obtains
$$
\frac1n\partial_{u_j}\log\rho
=\frac{1-\theta}{1+\theta}\,
  \frac1n\sum_k\partial_{u_j}\log w_k.
\tag{9}
$$
There is no uncontrolled factor of $n$ in this formula.
The logarithmic derivatives in (8) are uniformly bounded, and
$|(1-\theta)/(1+\theta)-1|\le2q^n/(1-q^n)\le2q/(1-q)$.
Combining (8)--(9) proves
$$
\boxed{
\frac1n\partial_{u_j}\log\rho_{\boldsymbol s}
=\frac1n\sum_{k=0}^{n-1}\partial_{u_j}\log\beta_{s_k}(u)
 +O(\epsilon).
}
\tag{10}
$$
All errors, entry bounds and coefficient neighborhoods in (10) are
independent of the word and its period. This is a differential estimate,
not only an asymptotic formula for the value of the trace.

### 4. The coefficient differential at the roots of unity

At $u=0$, implicit differentiation of $f_u(\alpha_s(u))=0$ gives
$$
\left.\partial_{u_j}\alpha_s(u)\right|_{u=0}
=-\frac{\alpha_s^j}{d\alpha_s^{d-1}}.
$$
Applying the product rule to $f_u'(\alpha_s(u))$ then yields
$$
\left.\partial_{u_j}\log\beta_s(u)\right|_{u=0}
=-\frac{d-1-j}{d}\alpha_s^j,
\qquad 0\le j\le d-2.
\tag{11}
$$
The identity uses $\alpha_s^d=1$; it includes the derivative of the
moving root, not merely the explicit coefficient derivative of $f_u'$.

Let $v(z)=(1,z,\ldots,z^{d-2})$ and let $V$ be the square matrix
with rows $v(\alpha_i)$ for the nontrivial roots $i<d$. It is
invertible. Lagrange interpolation on these $d-1$ nodes gives
$$v(1)=-\sum_{i=1}^{d-1}\alpha_i v(\alpha_i).\tag{12}$$
To check the coefficient, put $Q_0(z)=(z^d-1)/(z-1)$. The Lagrange
coefficient of $v(\alpha_i)$ at $z=1$ is
$$
\frac{Q_0(1)}{(1-\alpha_i)Q_0'(\alpha_i)}
=\frac{d}{(1-\alpha_i)d\alpha_i^{d-1}/(\alpha_i-1)}
=-\alpha_i.
$$

For a prescribed vector $(n_i)$, assign the nontrivial roots to its
indices in an order to be selected below. If $n_i=1$, use the one-letter
word $i$. If $n_i\ge2$, use a cyclic word with $n_i-1$ occurrences of
$i$ and exactly one occurrence of the anchor $d$. These words are
primitive: a nontrivial repetition would make the number of anchor
occurrences greater than one. For different $i$ their cyclic orbits are
distinct, because their non-anchor symbols are different.

Before dividing row $i$ by $n_i$, the limiting matrix in (10)--(11)
is the product of a column-diagonal matrix with a matrix whose rows are
$$
k_i v(\alpha_i)+h_i v(1),\qquad
(k_i,h_i)=
\begin{cases}(1,0),&n_i=1,\\(n_i-1,1),&n_i\ge2.
\end{cases}
$$
The determinant lemma for a rank-one perturbation and (12) give its
non-column part as
$$
\left(\prod_i k_i\right)\det V
\left(1-\sum_{i:n_i\ge2}\frac{\alpha_i}{n_i-1}\right).
\tag{13}
$$
One must choose the root assignment: the bracket need not be nonzero
for every assignment. Average it over all permutations of the nontrivial
roots. Their sum is $-1$, so the average is the positive real number
$$
1+\frac{1}{d-1}\sum_{i:n_i\ge2}\frac1{n_i-1}\ge1.
\tag{14}
$$
At least one bracket therefore has absolute value at least one, by the
triangle inequality. Choose such a permutation for this period vector.
It depends only on the periods and $d$.

Let $K^0_{\boldsymbol n}$ be the resulting normalized limiting matrix
at $u=\epsilon=0$. Each $k_i/n_i$ is at least $1/2$. Equations
(11)--(14) imply
$$
|\det K^0_{\boldsymbol n}|
\ge2^{-(d-1)}|\det V|\frac{(d-1)!}{d^{d-1}}.
$$
The full root-of-unity Vandermonde has absolute determinant $d^{d/2}$,
by the orthogonality of its Fourier columns. Removing the root $1$
removes a product of differences of absolute value
$|Q_0(1)|=d$. Thus $|\det V|=d^{d/2-1}$ and
$$
\boxed{\quad|\det K^0_{\boldsymbol n}|\ge
c_d:=\frac{(d-1)!}{2^{d-1}d^{d/2}}>0.\quad}
\tag{15}
$$
Every entry of these matrices is bounded independently of the periods,
because each normalized row is a convex combination, with real
nonnegative weights summing to one, of two of the finitely many vectors
in (11). The case $d=2$ is included: the Vandermonde is the $1\times1$
matrix $(1)$ and the bound is still valid.

### 5. One coefficient neighborhood for every period vector

The vectors $\partial\log\beta_s(u)$ are a fixed finite collection
of holomorphic functions. They differ from their values at zero by at
most $C_4\max_j|u_j|$ on a sufficiently small common polydisc. Because
the rows in (10) are averages, this changes any entry by the same bound,
without a period factor. Equation (10) consequently gives
$$
\max_{i,j}|K_{ij}-K^0_{\boldsymbol n,ij}|
\le C_5\bigl(\max_j|u_j|+|\epsilon|\bigr),
\tag{16}
$$
uniformly over the root assignments selected using (14), all periods,
and $|b|\le B$.

For precision, if two $r\times r$ matrices have entries bounded by
$M_0+1$ and their entrywise difference is at most $\delta\le1$, their
determinants differ by at most
$$r!\,r(M_0+1)^{r-1}\delta.$$
This follows by expanding the determinant over its $r!$ permutations
and telescoping the difference of two products of $r$ entries.

First choose $\eta$ and then a positive $\epsilon_0$ small enough that
all previous common-domain requirements hold and the right side of this
last determinant estimate, with (16), is at most $c_d/2$. It follows
from (15) that $|\det K|\ge c_d/2$, which is exactly (1). Uniform
entry bounds follow from (10) on the same domain. Take
$A_0=\epsilon_0^{-1/(d-1)}$ and enlarge it if a strict inequality in an
earlier bound requires this. This choice is independent of all periods.

This proves the uniform analytic statement on the displayed family of
actual polynomial Hénon automorphisms. It also gives a uniform lower
bound for the smallest singular value of the normalized matrix: from
$\|K\|_2\le rM$ and (1), one may use
$$\sigma_{\min}(K)\ge(c_d/2)/(rM)^{r-1}.$$
This is only a normalized differential bound in the $u$ coordinates.

### 6. From the actual tuples to algebraic trace coordinates

Fix $b\ne0$ and a period vector. The point-marked periodic incidence
is defined by $H_{b,p}^{n_i}(z_i)=z_i$ for each label $i$; impose the
open exact-period, disjointness and simplicity conditions. At one of the
tuples constructed above, the differential in each marked point block
is $DH_{b,p}^{n_i}-I$, which is invertible by Section3. The incidence
is therefore étale over the coefficient space near this tuple. It is
smooth there and has a unique local irreducible component of dimension
$r$. This does not assert that the whole incidence is irreducible.

The product of cyclic shift groups acts freely on this simple exact
point-marked open. Its quotient gives labeled cycle markings and is
étale locally; traces descend because cyclically conjugate return
matrices have the same trace. These are finite-group quotients in
characteristic zero, not a claim of freeness at lower-period points
that were excluded from the open locus.

Under the resulting local coefficient coordinates, the differential of
the trace map is the ordinary trace Jacobian proved invertible above.
Choose the irreducible component through that tuple. The nonzero
Jacobian proves that its trace map is dominant; source and target both
have dimension $r$, so it is generically finite and generically étale
in characteristic zero. The construction for this fixed $b$ is made
directly at $|A|>A_0$, rather than by an invalid specialization of a
generic nonzero-Jacobian statement. $\square$

## Novelty boundaries and unresolved assessment

- Fixed-Jacobian anti-integrable symbolic continuation is established.
  The orbit contraction alone is not a candidate innovation.
- Gorbovickis's scalar polynomial multiplier theorem already treats
  arbitrary periods and includes one scalar base point working for
  every prescribed period vector. That feature alone is not new.
- Paper18 obtains generic nonzero-Jacobian fibers from the scalar
  boundary, but explicitly excludes a theorem at any prescribed
  $b\ne0$, including $b=-1$. No input here silently changes that old
  theorem or its locks.
- The prospective difference is the direct nonzero-fixed-Jacobian
  theorem on a **common open region**, with the period-independent
  normalized differential bound (1). Its proof must be compared with
  current Hénon multiplier-rigidity and anti-integrable literature.
- The algebraic incidence consequences are standard once the actual
  invertible differential is supplied; they are not a second main
  innovation. A correct uniform theorem can still be too small for
  the batch's independent long-paper gate.
- No global spectral reconstruction, all-component dominance,
  individual eigenvalue coordinate, real-cycle census, entropy,
  quantization, arithmetic determinant or Riemann claim is made.

All calculations are analytic/algebraic proofs. No numerical experiment,
target fitting, CAS certificate or manuscript build is a dependency.
The exact uniform estimates, root assignment, primitive/disjoint words,
small periods and coefficient-coordinate conversion require independent
checking before this can be considered a candidate theorem package.
