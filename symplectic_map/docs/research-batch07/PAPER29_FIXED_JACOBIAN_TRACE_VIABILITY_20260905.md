# Fixed-Jacobian trace coordinates: bounded proof and viability check

Date: 2026-09-05. Independent bounded mathematical check of a new,
unselected Paper29 candidate. No manuscript or candidate PASS is issued.
The preceding cancellation and centralizer candidates are not enlarged.
Only this designated report is written by this check.

## 1. Existing Paper18 boundary

The complete frozen
[Paper18 research question](../../papers/18-marked-henon-scalar-boundary/notes/RESEARCH_QUESTION.md)
was read. Its SHA256 is
`cc04ee1db562f04f2291779481b52c2902020a8853bf1fdf186432560c892f24`.

Its RQ4 concerns a nonempty Zariski-open set of nonzero Jacobian
parameters. Anti-claims A3 and A4 explicitly exclude an assertion for
every nonzero parameter or a prescribed parameter such as $b=-1$.
The new fixed-$b$ quantifier is therefore not contained in that frozen
statement. This identifies an internal theorem boundary, not external
novelty. Nothing in Paper18 is edited or silently reinterpreted.

The actual author input subsequently read in full is
[PAPER29_FIXED_JACOBIAN_TRACE_PROOF_V1_20260905.md](PAPER29_FIXED_JACOBIAN_TRACE_PROOF_V1_20260905.md),
449 lines, SHA256
`8307ce9e82a8066b91c9f7a751299d32941c93e45cc9cb7df164dbae840afd1e`.
The checks below apply to that version, including its uniform entry and
determinant bounds, not merely to the earlier finite-period sketch.

## 2. Claims and status

Write
$$
H_{b,p}(x,y)=(p(x)+by,x),\qquad
p(x)=x^d+\sum_{j=0}^{d-2}a_jx^j,\qquad b\ne0.
$$
For every $d\ge2$, every fixed $b\in\mathbb C^*$, and every vector of
positive periods $(n_1,\ldots,n_{d-1})$, the original proposed claim is
the existence of $d-1$ labeled, pairwise-disjoint, simple exact cycles
for which
$$
\det\left(\frac{\partial\rho_i}{\partial a_j}\right)
_{1\le i\le d-1,\ 0\le j\le d-2}\ne0,
\qquad\rho_i=\operatorname{tr}DH_{b,p}^{n_i}.
\tag{1}
$$
The derivatives use the local continuation of the selected cycles while
$b$ is held fixed.

**Status: PROVABLE AS STATED.** The stronger uniform formulation proposed
during the check is also supported by the argument below:

> For every $d\ge2$ and $B>0$, there are $A_0(d,B)>0$ and a
> neighborhood $U_{d,B}$ of zero in $\mathbb C^{d-1}$ such that, for all
> $|A|>A_0(d,B)$, $0<|b|\le B$, $u\in U_{d,B}$, and all positive period
> vectors, the polynomial
> $$
> p_{A,u}(x)=x^d-A^d+\sum_{j=0}^{d-2}u_jA^{d-j}x^j
> $$
> has a tuple satisfying (1).

In particular, one polynomial $p_{A,0}=x^d-A^d$ works for every period
vector, with the tuple chosen separately for each vector. This is not a
claim that one tuple works for different prescribed periods, or that
tuples belonging to different vectors must be mutually disjoint.

The neighborhood $U_{d,B}$ concerns the normalized coefficients $u$. The
corresponding neighborhood in the actual coefficients of $p$ is scaled
by $A^{d-j}$ and is not claimed independent of $A$.

## 3. Assumptions, conventions and dependencies

- A cycle of period $n$ is simple when
  $\det(DH_{b,p}^n-I)\ne0$.
- The cycles are labeled by their indices $i$. Passing from point to
  cycle markings removes cyclic shifts only; no quotient by permutation
  of equal-period labels or by normal-form conjugacies is taken.
- Put $r=d-1$,
  $$f_u(z)=z^d-1+\sum_{j=0}^{d-2}u_jz^j,\qquad
  \varepsilon=A^{1-d}.$$
- The proof uses local holomorphic inverse branches, the contraction
  theorem in the maximum norm, Cauchy estimates on a smaller coefficient
  neighborhood, and finite-dimensional determinant algebra.
- No irreducibility theorem, empirical orbit search, full horseshoe
  theorem, or assertion about all marked components is a dependency.

The chain is: root branches $\to$ period-independent cyclic contraction
$\to$ period-independent slope contraction $\to$ normalized trace
derivatives $\to$ a uniform determinant gap $\to$ exact/simple/disjoint
cycles and descent to cycle markings.

## 4. Proof

### 4.1 Uniform root branches and periodic-word solutions

Label the $d$ roots of $z^d-1$ as
$$\alpha_1,\ldots,\alpha_r,\alpha_d=1,$$
where the first $r$ roots are all the nonidentity roots, in an order to
be chosen later. Since every root is simple, the holomorphic implicit
function theorem supplies inverse branches
$$\xi_j(t,u),\qquad f_u(\xi_j(t,u))=t,\qquad
\alpha_j(u)=\xi_j(0,u)$$
for all $j$, on a common product of a small $t$ disk and a coefficient
polydisk. Shrink that polydisk with compact closure in the original one.
The branches lie in fixed disjoint root disks. Their derivatives and
root values are bounded there, and
$$|f'_u(\alpha_j(u))|\ge\kappa_0>0.$$
All these choices depend only on $d$.

For an arbitrary word $\mathbf s=(s_0,\ldots,s_{n-1})$ in the $d$ root
labels, use indices modulo $n$ and solve
$$
f_u(z_k)=\varepsilon(z_{k+1}-bz_{k-1}).
\tag{2}
$$
The fixed-point form is
$$z_k=\xi_{s_k}\bigl(\varepsilon(z_{k+1}-bz_{k-1}),u\bigr).$$
On the product of small root disks, its maximum-norm Lipschitz constant
is at most $C|\varepsilon|(1+B)$. Its values stay in those disks for
sufficiently small $|\varepsilon|$, because the arguments of the inverse
branches have the same uniform bound. Choose the constant below one
half. These requirements do not depend on $n$ or the word.

The contraction theorem now gives a unique solution in the prescribed
product of disks. Holomorphic dependence follows either from the
convergent iterates or from the inverse of $I-D_z\mathcal F$, whose
Neumann-series norm is bounded uniformly. The defining equation gives
$$\max_k|z_k-\alpha_{s_k}(u)|\le C_1|\varepsilon|.$$
Use a slightly larger coefficient polydisk for this construction and
then restrict to a smaller one. Cauchy's estimate for each coefficient
derivative gives, uniformly in $n,k,\mathbf s$,
$$
z_k-\alpha_{s_k}(u)=O(\varepsilon),\qquad
\partial_{u_j}z_k-\partial_{u_j}\alpha_{s_k}(u)=O(\varepsilon).
\tag{3}
$$
The constants may depend on $d,B$, but not on the dimension $n$ of the
cyclic system. For holomorphic parameter domains one may perform the
construction on $|b|<B+1$ before restricting to $|b|\le B$.

Equation (2) is exactly the scaled periodicity equation: the points
$$Z_k=(Az_k,Az_{k-1})$$
satisfy $H_{b,p_{A,u}}(Z_k)=Z_{k+1}$. Thus this is a construction of
actual periodic points, not merely formal limiting itineraries.

### 4.2 Uniform periodic slopes and the trace formula

Put $a_k=f'_u(z_k)$ and $s_k^0=f'_u(\alpha_{s_k}(u))$. Equation (3)
gives $a_k-s_k^0=O(\varepsilon)$, including coefficient derivatives.
Solve the second cyclic system
$$w_k=a_k+\frac{b\varepsilon^2}{w_{k-1}}.\tag{4}$$
Take small fixed disks about the nonzero $s_k^0$. For sufficiently small
$|\varepsilon|$, their denominators stay bounded away from zero, the
map preserves the product of disks, and its maximum-norm Lipschitz
constant is bounded by $C_2B|\varepsilon|^2<1/2$. The contraction theorem
and the coefficient-domain argument above yield
$$
|w_k|\ge\kappa>0,\qquad
w_k-s_k^0=O(\varepsilon),\qquad
\partial_{u_j}w_k-\partial_{u_j}s_k^0=O(\varepsilon),
\tag{5}
$$
uniformly in the word and period.

The actual derivative matrix at $Z_k$ is
$$M_k=\begin{pmatrix}\varepsilon^{-1}a_k&b\\1&0\end{pmatrix}.$$
The index convention in (4) gives the exact identity
$$
M_k\begin{pmatrix}1\\\varepsilon/w_{k-1}\end{pmatrix}
=\varepsilon^{-1}w_k
 \begin{pmatrix}1\\\varepsilon/w_k\end{pmatrix}.
$$
Hence one return eigenvalue and the other are
$$
\lambda=\varepsilon^{-n}\prod_{k=0}^{n-1}w_k,\qquad
\lambda_s=\frac{(-b)^n}{\lambda}.
\tag{6}
$$
This also checks the placement of the cyclic indices in the multiplier
product.

Define
$$
\eta=\frac{((-b)\varepsilon^2)^n}{(\prod_kw_k)^2}.
$$
The trace is $\rho=\lambda(1+\eta)$ and
$$|\eta|\le\left(\frac{B|\varepsilon|^2}{\kappa^2}\right)^n.$$
Choose the parenthesized quantity below $1/4$. Then $\rho\ne0$, and
differentiation with $b,\varepsilon$ fixed gives the exact row identity
$$
\boxed{
\frac{1}{n}\frac{d_u\rho}{\rho}
=\frac{1-\eta}{1+\eta}\,
 \frac1n\sum_{k=0}^{n-1}\frac{d_uw_k}{w_k}.}
\tag{7}
$$
This formulation avoids a hidden factor growing with $n$ when
differentiating the trace correction. The notation is a logarithmic
differential; a global branch of the logarithm is not required.

Let
$$v_j(u)=\frac{d_u f'_u(\alpha_j(u))}{f'_u(\alpha_j(u))}.$$
Equations (5)--(7) give
$$
\frac{1}{n}\frac{d_u\rho}{\rho}
=\frac1n\sum_kv_{s_k}(u)+O(\varepsilon),
\tag{8}
$$
with a row-entry error bounded uniformly for every period and word.
Indeed (5) gives that bound for each summand, division by $n$ removes
the number of summands, and $|\eta|\le C|\varepsilon|^2$ uniformly in
$n\ge1$ controls the scalar correction in (7).

### 4.3 Exact root-slope derivatives and the determinant gap

At $u=0$ and $\alpha^d=1$, implicit differentiation gives
$$
\partial_{u_j}\alpha=-\frac{\alpha^{j+1}}d,\qquad
\partial_{u_j}\log f'_u(\alpha(u))\big|_{u=0}
=-\frac{d-1-j}{d}\alpha^j,
\quad0\le j\le d-2.
\tag{9}
$$
Write this row as $v(\alpha)$. The matrix $V$ whose rows are
$v(\alpha_1),\ldots,v(\alpha_r)$ is an invertible Vandermonde matrix
times nonzero column scalars. The root-of-unity sums also give
$$v(1)=-\sum_{i=1}^r\alpha_i v(\alpha_i).\tag{10}$$
For its $j$-th component, this uses
$\sum_{i=1}^r\alpha_i^{j+1}=-1$, where $1\le j+1\le d-1$.

For the requested vector of periods choose words
$$
\mathbf s_i=
\begin{cases}
(\alpha_i),&n_i=1,\\
(\underbrace{\alpha_i,\ldots,\alpha_i}_{n_i-1},1),&n_i\ge2.
\end{cases}
\tag{11}
$$
These symbols label inverse branches. When $u\ne0$, the marker $1$
means the branch $\alpha_d(u)$ near one, not a coordinate forced to
equal one.
Put $k_i=1$ when $n_i=1$ and $k_i=n_i-1$ otherwise. The limiting
normalized row in (8) is $v(\alpha_i)$ in the first case and
$(k_i v(\alpha_i)+v(1))/n_i$ in the second. Call the matrix of these
rows $C_{\mathbf n}$. Equation (10) and the rank-one determinant formula
give
$$
\det C_{\mathbf n}
=\left(\prod_i\frac{k_i}{n_i}\right)\det V
 \left(1-\sum_{n_i>1}\frac{\alpha_i}{n_i-1}\right).
\tag{12}
$$

Permute the nonidentity roots among the $r$ labels. The average of the
last factor is
$$1+\frac1r\sum_{n_i>1}\frac1{n_i-1}\ge1.$$
Therefore some permutation has the modulus of this factor at least one.
The modulus of $\det V$ does not change under a row permutation, and
$k_i/n_i\ge1/2$. For that assignment,
$$
|\det C_{\mathbf n}|\ge
\gamma_d:=2^{-r}|\det V|>0,
\tag{13}
$$
independently of the period vector.

The author's explicit constant also checks. The full $d$-root
Vandermonde is a Fourier matrix with determinant modulus $d^{d/2}$.
Removing the root $1$ divides this modulus by
$\prod_{i<d}|1-\alpha_i|=d$. The additional column factors in (9)
have modulus product $(d-1)!/d^{d-1}$. Consequently our slope matrix
$V$ has modulus
$$|\det V|=\frac{(d-1)!}{d^{d/2}},\qquad
\gamma_d=\frac{(d-1)!}{2^{d-1}d^{d/2}}.$$
Here $V$ includes the column factors, whereas the author's $V$ denotes
the raw Vandermonde. This notation difference does not change the bound.

Every limiting row is an average of rows in the fixed finite set
$\{v(\alpha_j)\}$, so its entries are uniformly bounded. Determinant
is uniformly Lipschitz on a fixed bounded set of $r\times r$ matrices,
as follows directly by expanding its $r!$ products. Choose a row-entry
tolerance small enough to change the determinant by less than
$\gamma_d/2$.

Shrink the coefficient neighborhood so that every $v_j(u)$ differs
from $v_j(0)$ by less than half that tolerance. This choice depends
only on $d$, and occupation averages obey the same bound for every
word. Next choose $|\varepsilon|$ small enough, depending on $d,B$, to
make the error in (8) less than the other half. Equations (8) and (13)
then show that
$$
\left|\det\left(\frac{1}{n_i\rho_i}
                 \frac{\partial\rho_i}{\partial u_j}\right)\right|
\ge\frac{\gamma_d}{2}
=\frac{(d-1)!}{2^d d^{d/2}}>0
\tag{14}
$$
for the chosen tuple, uniformly over all period vectors.
The root assignment can depend on the period vector; it is chosen at
$u=0$ and the same assignment works throughout this neighborhood and
the uniform $b,\varepsilon$ range.
The entry bound in the author claim follows from the same estimates.
If all entries have modulus at most $M$, the displayed smallest-singular-
value consequence is valid as well:
$\sigma_{\min}\ge(\gamma_d/2)/(rM)^{r-1}$, since the largest singular
value is at most $rM$. This is only a bound for the normalized matrix.

### 4.4 Exactness, disjointness and simplicity

For $n_i>1$, the word in (11) contains the marker $1$ exactly once,
so it is not a repetition of a shorter cyclic word. For $n_i=1$ it is
already a one-letter word. If an actual orbit from (2) had a smaller
period, its full coordinate sequence would have that smaller period.
Reading the labels of the fixed disjoint root disks would force the
same smaller period in (11), a contradiction.

Different selected words contain different nonmarker roots. No cyclic
rotation of one selected itinerary equals another. Actual coincidence of
two cycles would imply equality of their cyclic itineraries, so the
selected cycles are pairwise disjoint. This argument does not rely on
all adjacent pairs being distinct at $\varepsilon=0$; repeated letters
do produce repeated adjacent pairs in long words.

Choose $|\varepsilon|$ still smaller so that
$$\frac{\kappa}{|\varepsilon|}>2,\qquad
\frac{B|\varepsilon|}{\kappa}<\frac12.$$
Equation (6) gives
$$|\lambda|>2^n,\qquad |\lambda_s|<2^{-n}.$$
Neither return eigenvalue is one. Every selected cycle is therefore
simple, uniformly over all periods. This is stronger and safer than
merely asserting that the trace dominates $1+|b|^n$ without a
period-independent bound.

### 4.5 Actual coefficient derivatives and cycle markings

For fixed $A$, the coefficient change is
$$a_j=-A^d\mathbf1_{j=0}+A^{d-j}u_j,$$
whose Jacobian is the invertible diagonal matrix
$\operatorname{diag}(A^{d-j})$. Equation (14), together with
$n_i\rho_i\ne0$, proves the actual coefficient Jacobian (1).
This uses the full $d-1$ coefficient directions, not only the
one-dimensional family obtained by varying $A$.

The ordered cyclic equations locally parametrize point-marked periodic
points by the coefficient base: the contraction derivative has
invertible $I-D_z\mathcal F$. Exactness makes the action of each cyclic
shift group $\mathbb Z/n_i\mathbb Z$ free. There are only finitely many
phase copies of the selected tuple, and they have disjoint small
neighborhoods. Their quotient therefore has the same local coefficient
chart. Algebraically this is the familiar finite étale cycle quotient
on the simple exact locus used in Paper18.

Trace is invariant under these shifts, either by cyclic invariance of
matrix trace or by conjugacy of the return derivative at different
points of an invertible orbit. Thus the Jacobian calculation descends
unchanged to cycle markings. No quotient by residual normal-form
conjugacies is needed for the claim.

Finally choose $A_0(d,B)$ so that $|A|>A_0$ implies all imposed bounds
on $|\varepsilon|=|A|^{1-d}$. This proves the uniform statement and
hence the original fixed-$b$ claim. $\square$

## 5. Targeted adversarial checks

- **Period one.** Equation (2) becomes
  $f_u(z)=\varepsilon(1-b)z$. The same contraction bound applies; at
  $b=1$ it reduces to the simple root branch itself. The slope equation
  is $w=a+b\varepsilon^2/w$, which is covered by the second contraction.
- **Period two.** Both neighbors are the other coordinate, so the right
  side is $\varepsilon(1-b)z_{1-k}$. The maximum-norm bound still uses
  at most $1+B$. The scaled trace is exactly
  $a_0a_1+2b\varepsilon^2$, consistent with (6)--(7).
- **Quadratic degree.** There is one nonmarker root, $-1$, and one
  coefficient direction. Formula (9) gives $v(-1)=v(1)=-1/2$; the
  normalized limiting row is nonzero for every period.
- **Not every root assignment works.** For $d=6$ and periods
  $(2,2,1,1,1)$, assigning the two period-two words the roots
  $e^{\pi i/3},e^{-\pi i/3}$ makes the last factor of (12) zero.
  The permutation argument is an actual existence step, not permission
  to choose an arbitrary assignment.
- **Word-disjointness scope.** The author's Section2 sentence about
  words not related by cyclic shift should be read for equal lengths,
  or explicitly restricted to primitive words when lengths differ.
  Without either qualification, the words $(a)$ and $(a,a)$ give the
  same fixed orbit despite having different lengths. Every word actually
  selected in Section4 is primitive, so this is a nonblocking scope
  clarification, not a counterexample to the main theorem.
- **Holomorphic trace rescaling.** For any fixed word,
  $\varepsilon^n\rho$ also extends holomorphically to zero as
  $\operatorname{tr}\prod_k\begin{pmatrix}a_k&\varepsilon b\\
  \varepsilon&0\end{pmatrix}$, with limiting product of root slopes.
  This proves the finite-period version directly. The separate slope
  estimates are what make the bound uniform in unbounded periods.
- **Fixed Jacobian.** The determinant of a return derivative remains
  $(-b)^n$. No variation of $b$ is used in the coefficient Jacobian;
  allowing $|b|\le B$ only makes the estimates uniform.
- **Algebraic incidence consequence.** At the constructed simple tuple,
  the point-variable Jacobian is block diagonal with invertible blocks
  $DH^{n_i}-I$. The local component therefore has dimension $r$ and is
  étale over the coefficient base. A nonzero trace differential makes
  its trace map dominant; equal dimensions give generic finiteness and
  characteristic zero gives generic étaleness. The author's assertion
  about at least one component is justified, without an all-component
  or irreducibility conclusion.

## 6. Scope, missing claims and substantive length

The proof provides a full-rank tuple and its local continuation. It does
not say that every tuple has full rank, that all components of a fixed-$b$
marked space dominate, or that the trace map is globally injective.
It does not prove new irreducibility, compactification, ramification or
normal-form quotient theorems. No individual eigenvalue is asserted to
be a global coordinate, even though a distinguished expanding branch is
available within this construction.

The finite-period pointwise theorem is naturally a short strengthening
of the Paper18 boundary statement: a complete treatment would plausibly
occupy about 8--12 substantive mathematical pages. The uniform theorem
is a genuine stronger quantifier. It requires the two period-independent
$C^1$ estimates and the uniform determinant gap; they cannot be replaced
by finitely many applications of the implicit function theorem.
This does not assign novelty to the established anti-integrable method,
periodic inverse-branch continuation, or uniform continuation itself.

Nevertheless, those estimates belong to the same compact proof. They
replace the finite-period construction rather than furnish a second
independent proof to be printed in full. A natural complete treatment of
the uniform theorem appears closer to roughly 12--16 substantive pages
than to 22--30. This is a content estimate, not a compiled page count or
a formal candidate gate. Repeating Paper18's incidence, finite-free,
completed-boundary and Fitting-scheme material would not create new
proof mass for this result.

No literature-agent conclusions were read for this check. External
novelty and research-value scores remain outside its scope. Correctness
of the new quantifier and its separation from the frozen Paper18 claim
must not be confused with standalone long-paper suitability.

The `proof-writer` workflow guided the explicit quantifiers, uniform
estimates, edge cases and separation of proof status from candidate
status. The frozen Paper18 files and all other projects remain unchanged.
