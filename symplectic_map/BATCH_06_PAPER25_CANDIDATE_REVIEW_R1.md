# Paper 25 Candidate Review R1

## Review identity and frozen candidate

- Review date and public-search cutoff: 2026-08-26 UTC.
- Candidate ID: `support_rank_sharp_unbounded_perron_v1`.
- Working title: **Sharp Support-Rank Bounds and Unbounded Perron Degree in
  Hamiltonian Product Shears**.
- Review mode: fresh proof-first R1, with local Papers 20--24 lineage review
  and a bounded public primary-source collision screen.
- Evidence boundary: exact symbolic derivation only. No CAS, numerical
  experiment, manuscript, build, project directory, external message, or
  downstream lifecycle action was used.

The frozen candidate passes the proof, novelty, standalone, and portfolio
gates. The pass is for the complete conjunction below, not for the elementary
rank lemma, matrix determinant lemma, Perron--Frobenius theory, finite-field
binomial criterion, or Hamiltonian gradient-shear construction in isolation.

## Finding ledger and scores

| Gate | Score | Disposition | Reason |
|---|---:|---|---|
| proof correctness / plausibility | 9.6 / 10 | PASS | Every displayed formula and every cone, carry, visibility, arithmetic, and scalar-minimality implication rederives exactly. |
| novelty / portfolio differentiation | 8.4 / 10 | PASS | The arbitrary-degree sharp family is materially beyond Paper 22's bounded cubic quotient and Paper 23's fixed quartic escape. |
| standalone-paper potential | 8.6 / 10 | PASS | The factor theorem, uniform selector cone, temporal carry, visibility, arithmetic construction, and exact minimal recurrence form one coherent proof-first article. |
| bounded public noncollision | PASS with limitation | PASS | No direct collision with the complete conjunction was found through the stated cutoff; the search is not exhaustive and licenses no priority claim. |

Hard blockers: zero. Major proof defects: zero. Required theorem narrowings:
zero beyond the frozen anti-claims. Mandatory wording qualifications are
recorded below.

## 1. Strict-face support-rank factor theorem

Let

\[
A=-I_n+PQ,\qquad B=-I_n+RS,
\]

where

\[
P\in K^{n\times \alpha},\quad Q\in K^{\alpha\times n},
\quad R\in K^{n\times \beta},\quad S\in K^{\beta\times n},
\]

and put (C=BA). Direct multiplication gives

\[
C-I_n=-PQ-RS+RSPQ
=\begin{bmatrix}RSP-P&-R\end{bmatrix}
 \begin{bmatrix}Q\\S\end{bmatrix}.
\]

Write

\[
U=\begin{bmatrix}RSP-P&-R\end{bmatrix},\qquad
Y=\begin{bmatrix}Q\\S\end{bmatrix},\qquad r=\operatorname{rank}Y.
\]

Choose a row-basis matrix (T_0\in K^{r\times n}) and a coefficient
matrix (L\in K^{(\alpha+\beta)\times r}) such that (Y=LT_0). Set

\[
X=UL\in K^{n\times r}.
\]

Then (C=I_n+XT_0). With (z=t-1), Sylvester's determinant identity
gives the polynomial identity

\[
\begin{aligned}
\chi_C(t)
&=\det(zI_n-XT_0)\\
&=z^{n-r}\det(zI_r-T_0X)\\
&=(t-1)^{n-r}
  \det\!\bigl((t-1)I_r-T_0X\bigr).
\end{aligned}
\]

This remains valid at (z=0) because it is an identity of polynomials,
even if one first proves the determinant identity over (K(z)).

There is also a direct common-kernel interpretation. Since

\[
\ker Y=\ker Q\cap\ker S=\ker T_0,
\]

this space has dimension (n-r). If (v\in\ker Y), then (Av=-v)
and (C v=B(-v)=v). Thus the geometric, and hence algebraic,
multiplicity of (1) is at least (n-r). The reduced determinant may
itself vanish at (t=1), so exact unit multiplicity is not implied.

Consequently the part of the characteristic polynomial not forced to be a
unit-root factor has degree at most (r). Rank data alone do not force that
degree to equal (r): further unit roots or other quotient degeneracies may
occur. The frozen claim correctly states a lower bound on unit multiplicity
and an upper bound on nonunit degree, not an exact profile theorem.

## 2. The explicit sharp family

Fix (d\ge2), strictly increasing positive integers

\[
a_1<a_2<\cdots<a_d,qquad
D=\operatorname{diag}(a_1,\ldots,a_d),qquad
S_a=\sum_{i=1}^d a_i,qquad M=a_d,
\]

and an integer (b\ge2). Define

\[
V(q)=\prod_{j=1}^d q_j^2+\sum_{i=1}^d q_i^{a_i+1},
\qquad
W(p)=\prod_{j=1}^d p_j^b,
\]

and the positive Hamiltonian shears

\[
S_V(q,p)=(q,p+\nabla V(q)),\qquad
T_W(q,p)=(q+\nabla W(p),p),\qquad
F=T_W\circ S_V.
\]

Their inverses replace the displayed plus signs by minus signs. Their
Jacobian blocks contain the symmetric Hessians of (V) and (W), so each
shear, and therefore (F), preserves the standard symplectic form.

For a positive position-degree vector (u=(u_1,\ldots,u_d)^{\mathsf T}),
the two competitors in component (i) of \(\nabla V\) have weighted
degrees

\[
a_i u_i
\quad\hbox{and}\quad
u_i+2\sum_{j\ne i}u_j=2\sum_j u_j-u_i.
\]

When the pure spike is strict in every component, the first phase has degree
matrix (A=D). The unique monomial in component (i) of \(\nabla W\) has
row

\[
(b,\ldots,b)-e_i^{\mathsf T},
\]

so the second phase has matrix

\[
B=bJ-I_d.
\]

The complete-step matrix is therefore

\[
C=BD=b\mathbf1 a^{\mathsf T}-D,
\qquad a=(a_1,\ldots,a_d)^{\mathsf T}.
\]

Every entry of (C) is positive: its off-diagonal entries are (ba_j),
and its diagonal entries are ((b-1)a_i).

### 2.1 The invariant cone and strict selector

Put

\[
R=1+\frac{2M}{bS_a},\qquad
K_R=\{u\in\mathbb R_{>0}^d:\max_i u_i\le R\min_i u_i\}.
\]

Assume

\[
a_1+1>4d,\qquad R^2<2.
\]

If (u\in K_R) and (m=\min_i u_i), then

\[
a_i u_i\ge a_1m,
\]

whereas

\[
2\sum_j u_j-u_i\le (2dR-1)m.
\]

Since (R<\sqrt2<2),

\[
2dR-1<4d-1<a_1.
\]

Thus every pure spike is selected strictly throughout (K_R), including at
the ordinary seed \(\mathbf1\).

### 2.2 Strict cone invariance

For (u\in K_R), write

\[
H=a^{\mathsf T}u,
\qquad z=Cu,
\qquad z_i=bH-a_i u_i.
\]

Then (H\ge S_a m), (a_i u_i\le MRm), and hence

\[
\frac{\max_i z_i}{\min_i z_i}
\le \frac{bH}{bH-MRm}
\le \frac1{1-\alpha R},
\qquad
\alpha=\frac{M}{bS_a}=\frac{R-1}{2}.
\]

Now

\[
\frac1{1-\alpha R}<R
\iff
(R-1)\left(1-\frac{R^2}{2}\right)>0,
\]

which follows from (1<R<\sqrt2). Therefore

\[
C(K_R)\subset\operatorname{int}K_R.
\]

This also proves positivity of every completed degree vector.

### 2.3 All temporal carries and cross-phase domination

The same (R^2<2) hypothesis gives

\[
bS_a>2MR.
\]

Indeed, using (bS_a=2M/(R-1)), this is equivalent to

(R(R-1)<1), and

\[
R(R-1)=R^2-R<2-R<1.
\]

Consequently, for every (u\in K_R),

\[
(Cu)_i\ge(bS_a-MR)m>MRm
\ge\max_j a_j u_j.
\]

Thus every new position degree strictly exceeds every momentum degree
created in the preceding (V)-phase. It also exceeds every old position
degree. At the initial (V)-phase, (a_i>1) makes (a_i\) beat the ordinary
momentum seed. At every later (V)-phase, the previous completed-step
inequality gives (u_n>u_{n-1}) componentwise, so

\[
D u_n>D u_{n-1}
\]

componentwise and the fresh momentum terms beat the carried ones. Hence both
phase carries are strict for every iterate.

### 2.4 Positive-semiring survival

All displayed potential coefficients and both shear signs are positive.
Starting from the coordinate variables, every iterate is obtained using only
addition and multiplication with positive integer coefficients. In
characteristic zero these coefficients remain nonzero. Inside each selected
(V)-component the strict weighted-degree inequality separates the spike
from the product competitor; inside each (W)-component there is only one
gradient monomial. Powers and products of nonzero top forms remain nonzero
in the polynomial domain. Together with strict carry, this proves exact
leading-degree survival without a cancellation assumption hidden in the
tropical calculation.

### 2.5 Fixed \(q_1\) visibility

At the first completed step,

\[
(C\mathbf1)_1-(C\mathbf1)_i=a_i-a_1>0
\qquad(i>1).
\]

For later steps, let (u=Cv) with (v\in K_R). Then

\[
\begin{aligned}
a_i u_i-a_1u_1
&=b(a_i-a_1)a^{\mathsf T}v-a_i^2v_i+a_1^2v_1\\
&\ge
\bigl[b(a_i-a_1)S_a-a_i^2R+a_1^2\bigr]\min_jv_j.
\end{aligned}
\]

Therefore the frozen visibility inequalities

\[
b(a_i-a_1)S_a>a_i^2R-a_1^2
\qquad(2\le i\le d)
\]

give (a_i u_i>a_1u_1). Since

\[
(Cu)_1-(Cu)_i=a_i u_i-a_1u_1,
\]

the first position coordinate is strictly largest at every positive
completed iterate. The cross-phase domination already proved shows that it
also beats every momentum coordinate.

It follows inductively from the ordinary seed that

\[
\deg(F^n)=e_1^{\mathsf T}C^n\mathbf1
\qquad(n\ge1).
\]

This is an exact polynomial-degree identity, not only a matrix upper bound.

## 3. Characteristic polynomial and arithmetic construction

The matrix determinant lemma, applied over \(\mathbb Q(t)\), yields

\[
\begin{aligned}
\chi_C(t)
&=\det(tI_d+D-b\mathbf1a^{\mathsf T})\\
&=\prod_{i=1}^d(t+a_i)
-b\sum_{i=1}^d a_i\prod_{j\ne i}(t+a_j).
\end{aligned}
\]

In the coefficient of (t^{d-k}), every (k)-fold product contributing to
(e_k(a)) occurs exactly (k) times in the second sum. Therefore

\[
\boxed{\displaystyle
\chi_C(t)=t^d+\sum_{k=1}^d(1-bk)e_k(a)t^{d-k}.}
\]

### 3.1 Exact finite-field reduction

Choose a prime (p\equiv1\pmod d) and a primitive element
(c\in\mathbb F_p^\times). Let the residues of
(a_1,\ldots,a_d) be exactly the (d)-th roots of unity in
(\mathbb F_p\). Then

\[
\prod_{i=1}^d(t+a_i)
\equiv t^d-(-1)^d\pmod p.
\]

Hence (e_k(a)\equiv0\pmod p) for (1\le k<d), and

\[
e_d(a)\equiv(-1)^{d+1}\pmod p.
\]

Choose (b) in the unique residue class satisfying

\[
bd\equiv1-(-1)^dc\pmod p.
\]

Then

\[
(1-bd)e_d(a)
\equiv (-1)^dc\,(-1)^{d+1}=-c\pmod p,
\]

and therefore

\[
\chi_C(t)\equiv t^d-c\pmod p.
\]

### 3.2 Binomial irreducibility, including the \(4\mid d\) clause

For a finite field \(\mathbb F_q\), the exact binomial criterion says that
(x^d-c) is irreducible when every prime divisor of (d) divides
(\operatorname{ord}(c)) but not
((q-1)/\operatorname{ord}(c)), and, if (4\mid d), one additionally has
(q\equiv1\pmod4).

Here (q=p) and (c) is primitive, so

\[
\operatorname{ord}(c)=p-1,
\qquad
\frac{p-1}{\operatorname{ord}(c)}=1.
\]

Every prime divisor of (d) divides (p-1) because (d\mid p-1), and
none divides (1). If (4\mid d), then (p\equiv1\pmod d) already implies
(p\equiv1\pmod4). Thus (t^d-c) is irreducible over \(\mathbb F_p\).
Since \(\chi_C\) is monic integral, irreducibility of its reduction proves
that \(\chi_C\) is irreducible over \(\mathbb Q\).

### 3.3 Boundary audits at \(d=2\) and \(d=4\)

- For (d=2), (p\equiv1\pmod2) is odd and a primitive (c) is a
  nonsquare. The two roots of unity are \(\{1,-1\}\), the congruence for
  (b) is soluble because (2\) is invertible modulo (p), and the
  quadratic binomial is irreducible. There is one visibility inequality,
  and all cone estimates above remain strict once (a_1+1>8) and (b) is
  sufficiently large.
- For (d=4), the often-missed binomial clause is satisfied rather than
  assumed: (p\equiv1\pmod4) follows directly from the chosen progression.
  The four fourth roots of unity exist and are distinct, (4) is invertible
  modulo (p), and the same large-(b) argument satisfies all three
  visibility inequalities simultaneously.

## 4. Parameter existence and quantifier order

The required choices can be made in the frozen order.

1. Fix (d\ge2).
2. Dirichlet's theorem supplies primes (p\equiv1\pmod d); choose one.
   The cyclic group \(\mathbb F_p^\times\) supplies a primitive (c).
3. Enumerate the (d)-th roots of unity modulo (p). Choose distinct
   positive lifts and add sufficiently large multiples of (p); after
   ordering them, their residue set is unchanged and
   (a_1+1>4d) holds. A particularly transparent choice is one common
   large multiple of (p) plus the least positive representatives, followed
   by sorting.
4. Because (d) is invertible modulo (p), the displayed congruence fixes
   one residue class for (b). That arithmetic progression contains
   arbitrarily large positive integers. Along it,
   (R=1+2M/(bS_a)\downarrow1), so (R^2<2) eventually. For each
   (i>1), the left side of
   \[
   b(a_i-a_1)S_a>a_i^2R-a_1^2
   \]
   grows linearly in (b), while the right side stays bounded and tends to
   (a_i^2-a_1^2). Since there are finitely many (i), one sufficiently
   large (b) in the fixed class satisfies all inequalities, as well as
   (b\ge2), simultaneously.

No circular choice occurs: the lifts are frozen before (b), and only (R)
changes after (b) is selected.

## 5. Perron degree and exact scalar recurrence minimality

The matrix (C) is positive, so Perron--Frobenius gives a simple eigenvalue
(\rho(C)>0), positive left and right eigenvectors, and strict dominance in
modulus over all other eigenvalues. Since \(\chi_C\) is irreducible of degree
(d), it is the minimal polynomial of (C) and of (\rho(C)). Hence

\[
[\mathbb Q(\rho(C)):\mathbb Q]=d.
\]

From the exact visible degree identity and positivity,

\[
e_1^{\mathsf T}C^n\mathbf1
=\gamma\rho(C)^n+O(\theta^n),
\qquad
\gamma>0,quad 0\le\theta<\rho(C).
\]

Therefore

\[
\lambda_1(F)=\lim_{n\to\infty}\deg(F^n)^{1/n}=\rho(C),
\]

and its algebraic degree is exactly (d).

Cayley--Hamilton supplies a rational recurrence of order at most (d) for
(s_n=e_1^{\mathsf T}C^n\mathbf1). To prove scalar minimality, suppose a
nonzero rational recurrence polynomial (f) of order (k) annihilates the
tail of (s_n). Divide the recurrence by the relevant power of
(\rho(C)) and pass to the Perron asymptotic limit. Because
(\gamma>0), this gives (f(\rho(C))=0). The minimal polynomial of
(\rho(C)) has degree (d), so (k\ge d). Thus the visible scalar degree
sequence has minimal rational recurrence order exactly (d), not merely a
(d\)-dimensional matrix realization.

## 6. Sharpness of the support-rank bound

For this family,

\[
A=D=-I_d+I_d(D+I_d),
\qquad
B=bJ-I_d=-I_d+(b\mathbf1)\mathbf1^{\mathsf T}.
\]

Taking (Q=D+I_d) and (S=\mathbf1^{\mathsf T}), the stacked support-row
matrix has rank (r=d) because (Q) is invertible. The reduced
characteristic factor is the irreducible degree-(d) polynomial
\(\chi_C\), so the nonunit quotient degree equals (r). This attains the
factor theorem's upper bound for every (d\ge2).

The sharpness statement is existential. It does not say that every
rank-(r) profile has quotient degree (r), that the displayed
factorization is uniquely minimal for an arbitrary presentation, or that
rank alone determines exact unit multiplicity.

## 7. Local lineage and portfolio audit

| Local predecessor | Occupied result | Paper 25 boundary |
|---|---|---|
| Paper 20 | two-mode stationary selector-to-matrix proof architecture and quadratic Perron outcome | architecture is inherited and must be disclosed |
| Paper 21 | three-mode visible cubic recurrence and irreducible cubic subfamilies | fixed cubic rank, not arbitrary algebraic degree |
| Paper 22 | arbitrary-mode endpoint-spike family, common unit sector, and cubic spectral collapse | closest theorem ancestor; its common-kernel lemma is reused infrastructure, while Paper 25 proves the rank factor cleanly and supplies sharp examples in every rank |
| Paper 23 | fixed four-mode removal of the unit sector and an irreducible quartic Perron subfamily | (d=4) is occupied; Paper 25's delta is the uniform every-(d) construction and exact scalar order |
| Paper 24 | two-mode period-two selector exchange and parity monodromy | different nonstationary selector mechanism; Paper 25 remains a stationary strict-face theorem |

The project must not be framed as “a quintic sequel.” The value is the
uniform support-rank law together with sharpness and unbounded Perron/minimal
recurrence degree for all (d\ge2). The factor lemma alone is elementary and
locally anticipated; the complete sharp Hamiltonian realization is the
portfolio delta.

## 8. Bounded public primary-source collision screen

The review searched exact title, author, object, and mechanism combinations
through 2026-08-26 UTC. It used public primary or authoritative records and
did not infer full-text absence from metadata alone.

| Source | Checked public result | Collision disposition |
|---|---|---|
| J. Blanc and I. van Santen, *Dynamical degrees of affine-triangular automorphisms of affine spaces*, arXiv:1912.01324, DOI `10.1017/etds.2021.90` | realizes every weak Perron number by an affine-triangular automorphism in some dimension and develops matrix/valuation methods | strong realization neighbor, but not the frozen positive Hamiltonian product-shear family, support-rank factor/sharpness package, or exact ordinary-degree visibility proof |
| E. Shao and X. Sun, *Dynamical degrees of affine-triangular automorphisms in dimension four*, arXiv:2509.14584 | proves a degree-at-most-four result for affine-triangular maps and explores higher-dimensional cases | directly cautions against advertising degree four; no arbitrary-(d) Hamiltonian sharp family or matching support theorem was located in the public full-text record |
| N.-B. Dang and C. Favre, *Spectral interpretations of dynamical degrees and applications*, Annals of Mathematics 194 (2021), 299--359, DOI `10.4007/annals.2021.194.1.5` | general spectral interpretation and algebraicity results | broad spectral context only; no finite selected-gradient support certificate or candidate construction |
| P. Berger and D. Turaev, *Generators of groups of Hamiltonian maps*, arXiv:2210.14710 | approximation of analytic Hamiltonian dynamics by position and momentum shears | shear-generation background, not an exact iterate-degree theorem |
| H. Koch and H. E. Lomelí, *On Hamiltonian flows whose orbits are straight lines*, arXiv:1304.3377 | Hamiltonian shear and factorization structure | construction background, with no matching rank-sharp degree recurrence |
| J. Déserti, *Degree growth of polynomial automorphisms and birational maps: some examples*, arXiv:1602.04642 | higher-dimensional polynomial and birational degree-growth examples | different polynomial-growth examples, not the present exponential visible Perron family |
| M. Abboud and J. Xie, *Dynamical degrees of twisted rational maps*, arXiv:2608.09275 | 2026 algebraicity and relative/twisted dynamical-degree framework | current but object-distinct; no collision with polynomial Hamiltonian product shears |
| A. Heyman and I. E. Shparlinski, *Counting irreducible binomials over finite fields*, arXiv:1504.01172 | records the standard finite-field irreducible-binomial criterion, including the (4\mid d) condition | arithmetic infrastructure only, not a novelty claim |

No direct public statement of the complete conjunction was found in this
bounded screen. This is a search-bounded noncollision conclusion, not an
exhaustive theorem and not evidence for “first,” “only,” “unprecedented,” or
absolute priority.

## 9. Precise allowed novelty wording

The strongest defensible wording is:

> For every integer (d\ge2), this paper gives an explicit positive
> Hamiltonian product shear on (2d) affine coordinates whose ordinary
> iterate degrees are exactly visible through a positive (d\times d)
> matrix, whose Perron dynamical degree has algebraic degree (d), and whose
> scalar degree sequence has minimal rational recurrence order (d). A
> selected-support row-rank factor theorem bounds the nonunit characteristic
> degree, and the family attains that bound in every rank.

An admissible literature qualifier is:

> No direct collision with this complete support-rank/sharp-Hamiltonian
> package was found in the bounded primary-source screen through
> 2026-08-26 UTC.

The paper must explicitly say that weak-Perron realization, Hamiltonian
gradient shears, matrix determinant identities, common-kernel reasoning,
Perron--Frobenius, Cayley--Hamilton, and finite-field binomial irreducibility
are established infrastructure. It must disclose Papers 20--24 as the local
lineage, with Paper 22 as the closest rank-bound ancestor and Paper 23 as the
occupied quartic case.

## 10. Mandatory scope and anti-claims

The frozen scope is positive coefficients and characteristic zero. It does
not support arbitrary signs or supports, every-exponent validity, arbitrary
weak-Perron realization, minimal ambient dimension, optimal sparsity,
inverse or higher dynamical degrees, entropy equality, integrability,
automata, selector periodicity, genericity, classification, nonconjugacy, or
absolute priority. It does not assert exact unit multiplicity in the factor
theorem, and it does not assert that rank profiles alone force quotient
degree. A (d=5) instance is only one specialization and must not replace the
unbounded theorem as the headline.

## Final gate decision

The strict-face determinant factorization is correct; the cone and all
temporal carries are strict; positive-semiring leading forms survive; fixed
(q_1) visibility gives the exact scalar degree; the characteristic formula
and reduction to (t^d-c) are exact; the full binomial criterion, including
the (4\mid d) clause, is satisfied; parameter choices occur in the required
order; the Perron degree and scalar recurrence order are exactly (d); and
the construction attains the support-rank bound for every (d\ge2).
Together with the bounded noncollision and portfolio audit, this clears the
frozen candidate for the next separately authorized source-design stage.

PAPER25_CANDIDATE_GATE_PASS_R1
