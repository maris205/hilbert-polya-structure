# Round 4: complete short proofs, no admission claim

Date: 2026-09-08 UTC. These are AI-generated internal mathematical notes
for the two [frozen contracts](FROZEN_CONTRACTS.md), not a new paper,
C-number, evaluator result, or claim of priority. Both questions close
mathematically, but their residual contribution is too short/classical
for the requested substantial-paper gate. No mathematical program was
created, imported, executed, or rerun.

The inherited directory name does not change the clock: every iterate
below is the native **forward** iterate of a Jacobian-2 map. It expands
real area; only its inverse has Jacobian 1/2.

## Status, assumptions, strategy, and dependency map

**Status for both frozen mathematical claims: PROVABLE AS STATED.**
This is separate from paper admission: neither is admitted.

The assumptions are exactly $c\in\mathbb Z$ and initial coordinates
in $\mathbb Q^2$ for DH1; DH2 fixes $c=0$ and $P=(0,1)$ and ranges
over all $n\geq1$. Notation for each map, coordinate sequence, prime
valuation, constant, and backward denominator is defined where used
below; $\log$ is the natural logarithm. No hidden height bound is an
assumption: the needed height growth is proved.

The strategy is a direct local proof for DH1 and backward modular
comparison for DH2. The dependencies are:

1. DH1 integrality uses only the periodic recurrence and integral $c$.
2. DH1's period bound uses Lemmas 1–3 and the complete two-state
   residue-cycle analysis; its parameter list then uses quadratic
   equations and their converses.
3. DH2's limit uses parity, escape and the fixed constant in Lemma 4,
   inverse-polynomial congruences in Lemma 5, and the explicitly
   ordered limits in (7).
4. The recent-theorem cross-check in Section 3 depends on the cited
   sources but is not a dependency of either elementary proof.

## 1. DH1: all rational periodic points for every integer parameter

### Exact classification

For $c\in\mathbb Z$, let

$$
H_c(x,y)=(y,y^2+c-2x).
$$

Its entire ordinary periodic locus in $\mathbb Q^2$ is as follows.

| Parameter, with $k\in\mathbb Z_{\geq0}$ | Complete periodic locus | Least periods |
| --- | --- | --- |
| $c=2-k(k+1)$ | $(1-k,1-k)$ and $(2+k,2+k)$ | Both fixed |
| $c=-7-k(k+1)$ | $(-k-2,k-1)$ and $(k-1,-k-2)$ | One two-cycle |
| Every other integer $c$ | Empty | None |

The first two parameter sets are disjoint: the first is even and the
second is odd. Within each row, $k\geq0$ is unique. There is no rational
period greater than two and there are either zero or two periodic points.
These claims are for every integer $c$, without a size or height bound.

### Lemma 1: periodic rational coordinates are integral

A periodic orbit can be written $(a_i,a_{i+1})$, with indices modulo
its period, and

$$
a_i^2=a_{i+1}+2a_{i-1}-c.                       \tag{1}
$$

Fix a prime $p$, set $v_p(0)=+\infty$, and let
$m=\min_i v_p(a_i)$. If $m<0$, choose $i$ attaining it.
The right side of (1) has valuation at least

$$
\min\{m,m+v_p(2),0\}=m,
$$

whereas the left side has valuation $2m<m$. This is impossible.
Thus every coordinate is integral at every prime, hence an integer.
The argument includes the bad prime two; good invertible reduction is
not being assumed there. $\square$

### Lemma 2: two iterations improve shared 2-adic precision

If $P=(x,y)$ and $Q=(x',y')$ in $\mathbb Z^2$ satisfy
$P\equiv Q\pmod{2^r}$ for $r\geq1$, then

$$
H_c^2(P)\equiv H_c^2(Q)\pmod{2^{r+1}}.          \tag{2}
$$

Indeed, put $\delta x=x-x'$ and $\delta y=y-y'$. The two coordinate
differences after one iteration are

$$
\delta y,\qquad (y+y')\delta y-2\delta x.
$$

Because $y+y'$ is even, these are divisible by $2^r$ and
$2^{r+1}$ respectively. After a second iteration the first difference
is divisible by $2^{r+1}$. Its second difference is the sum of a multiple
of the previous second difference and minus twice the previous first
difference, so it too is divisible by $2^{r+1}$. This proves (2).
Iterating gives precision $2^{r+j}$ after $H_c^{2j}$. $\square$

### Lemma 3: reduction is injective on all integer periodic points

Let periodic $P,Q$ have the same reduction modulo two. Choose an even
positive integer $N$ divisible by both periods. For every $j\geq1$,
$H_c^{jN}$ fixes both points; Lemma 2 therefore gives

$$
P-Q=H_c^{jN}(P)-H_c^{jN}(Q)\equiv0
\pmod{2^{1+jN/2}}.
$$

An integer divisible by arbitrarily large powers of two is zero, so
$P=Q$. This is injectivity on the whole periodic locus, not just the
uniqueness of a preselected lifted cycle. $\square$

### Reduction and the exact native period bound

Modulo two, the map is

$$
\overline H_c(x,y)=(y,y+\bar c).
$$

If $c$ is even, every image lies on the diagonal and both diagonal
states are fixed. Thus its only periodic states have period one.
If $c$ is odd, every image lies on the anti-diagonal and its two states
form one two-cycle. Thus its only periodic states have period two.

For any integer periodic point $P$, let $m\in\{1,2\}$ be its residue
period. Both $P$ and $H_c^m(P)$ are periodic and have the same residue;
Lemma 3 implies $H_c^m(P)=P$. The least period upstairs equals $m$,
since reduction could not have larger period. Consequently even $c$
permits only fixed points, and odd $c$ permits only genuine two-cycles.
By Lemma 1 this exhausts the rational domain as well.

### Solving the two remaining equations

A fixed point has $x=y=t$ and

$$
t^2-3t+c=0.
$$

Integral roots occur precisely when $9-4c=(2k+1)^2$ for a unique
$k\geq0$. Equivalently $c=2-k(k+1)$, with roots $1-k$ and $2+k$.
They are distinct; a double root would equal $3/2$.

A genuine period-two point is exchanged with $(y,x)$, so

$$
y^2+c=3x,\qquad x^2+c=3y,\qquad x\ne y.
$$

Subtracting gives $(y-x)(x+y+3)=0$, hence $x+y=-3$. Substitution
gives $x^2+3x+c+9=0$. Its integral roots occur precisely when
$-4c-27=(2k+1)^2$, that is, $c=-7-k(k+1)$. They are $-k-2$ and
$k-1$, always distinct. Conversely these identities directly verify
the displayed two-cycle. This proves both necessity and sufficiency
in all rows of the classification. $\square$

### Contribution boundary

The mechanism is monic-integral local escape followed by strictly
contracting residue-cycle lifting and quadratic equations. The
actually inspected nearby sources do not literally state this exact
Jacobian-2 table, but the proof is a short application of classical
local reasoning. A failure to find the literal table is not evidence
of substantial novelty. DH1 is not admitted.

## 2. DH2: full-time return-gcd limit, elementary closure

### Exact statement

Let $H=H_0$, $P=(0,1)$, and define

$$
H^n(P)=(u_n,u_{n+1}),\quad
u_0=0,\quad u_1=1,\quad u_{n+2}=u_{n+1}^2-2u_n.
$$

For every $n\geq1$ put

$$
D_n=\gcd(|u_n|,|u_{n+1}-1|).
$$

Then $D_n$ is a positive odd integer, the orbit is nonperiodic, and
unconditionally

$$
\lim_{n\to\infty}\frac{\log D_n}{2^n}=0.        \tag{3}
$$

The proof uses no conjectural height bound, density-one restriction,
selected subsequence, finite numerical prefix, or altered clock.

### Lemma 4: parity and explicit escape bounds

The recurrence gives by hand

$$
(u_0,u_1,u_2,u_3,u_4,u_5,u_6)=(0,1,1,-1,-1,3,11).
$$

Induction modulo two shows $u_j$ is odd for every $j\geq1$. In
particular it is nonzero and $D_n$ is positive and odd. The orbit
cannot return to $P$, whose first coordinate is zero. Since $H$ is
invertible over $\mathbb Q$, any repeated forward point would imply
a return to $P$; hence the whole forward orbit has distinct points.

For $j\geq6$ one has

$$
u_j\geq2u_{j-1}>0,\qquad
\frac{u_j^2}{2}\leq u_{j+1}\leq u_j^2.          \tag{4}
$$

The base condition is $11\geq2\cdot3$. Assuming it at $j$,

$$
u_{j+1}=u_j^2-2u_{j-1}\geq u_j^2-u_j
\geq\frac{u_j^2}{2}\geq2u_j,
$$

using $u_j\geq11$. The upper bound follows from $u_{j-1}>0$.
This proves the induction. Iterating the logarithmic inequalities in
(4), for every $j\geq6$,

$$
2^{j-6}\log(11/2)+\log2
\leq\log u_j\leq2^{j-6}\log11.                \tag{5}
$$

Thus $u_j\to+\infty$ and the constant $C=2^{-6}\log11$ satisfies
$\log u_j\leq C2^j$ for all $j\geq6$. Crucially $C$ does not depend
on any backward shift used next. $\square$

### Lemma 5: fixed backward shifts bound the return ideal

Fix an arbitrary integer $k\geq1$. The polynomial inverse

$$
H^{-1}(x,y)=((x^2-y)/2,x)
$$

is defined over $R=\mathbb Z[1/2]$, so every fixed backward iterate
$H^{-k}(P)$ belongs to $R^2$. Write its first coordinate as
$B_k/A_k$ with $B_k\in\mathbb Z$ and $A_k$ a positive power of two
(including $2^0$ if appropriate). These are constants for fixed $k$.

By definition $H^n(P)\equiv P\pmod{D_n}$. Because $D_n$ is odd,
reduction of $R$ modulo $D_n$ is defined and the polynomial $H^{-k}$
preserves this congruence. For every $n\geq k$ it follows that

$$
H^{n-k}(P)=H^{-k}(H^n(P))\equiv H^{-k}(P)\pmod{D_n},
$$

and hence

$$
D_n\mid A_k u_{n-k}-B_k.                       \tag{6}
$$

Divisibility here is in $\mathbb Z$: $A_k$ is a unit modulo the odd
integer $D_n$. The convention for the trivial modulus $D_n=1$ causes
no exception. By Lemma 4, for fixed $k$ the integer on the right of
(6) is nonzero once $n$ is sufficiently large. For such $n$, also
taking $n-k\geq6$,

$$
1\leq D_n\leq |A_ku_{n-k}-B_k|
\leq (A_k+|B_k|)u_{n-k}.
$$

Consequently

$$
0\leq\frac{\log D_n}{2^n}
\leq C2^{-k}+\frac{\log(A_k+|B_k|)}{2^n}.       \tag{7}
$$

First let $n\to\infty$ with $k$ fixed. The last term vanishes and
the limsup is at most $C2^{-k}$. Now let $k\to\infty$. Nonnegativity
gives (3). This order of limits does not require any uniform control
on $A_k,B_k$ as $k$ varies. $\square$

### Scope relative to the general Hénon gcd question

This argument explicitly verifies three facts: a polynomial inverse over
$\mathbb Z[1/2]$, absence of the bad prime two from every $D_n$, and
an explicit exponentially scaled upper bound with escape for this
fixed orbit. The inverse-congruence mechanism is portable, but this
document proves exactly the frozen instance; no broader theorem over
number fields or all targets is formulated or claimed here. In
particular, applying an inverse modulo an even $D_n$ without first
controlling its 2-part would be invalid.

Section 11, Question 47, of the [2024 Hénon problem list](https://armj.math.stonybrook.edu/html-articles/Files-2015-2024/23-70/index.html)
already supplies the broader return-gcd research question. Here the
residual instance has only a short inverse-congruence proof; it is not
admitted as a new substantial paper. The separate bounded-ideal
infinitely-often part of Question 47 is not addressed by (3).

## 3. Recent-source cross-check, not a proof dependency

The source-first search also located Matsuzawa's
[2025 preprint](https://arxiv.org/html/2507.05027v1).
Theorem 1.5 gives an unconditional vanishing gcd-height ratio for a
generic orbit when the target satisfies its regular-embedding and
iterative-finiteness hypotheses and its codimension dynamical degree
after taking the reciprocal-codimension power is below the orbit
arithmetic degree. Proposition 3.4 supplies
density, and genericity when dynamical Mordell–Lang is known, for
quasi-finite maps with $d_1>d_2$ and maximal arithmetic degree.

For completeness, the following is our map-specific hypothesis
verification, rather than a new general theorem.

- On $\mathbb P^2$, $H$ extends to
  $[X:Y:Z]\mapsto[YZ:Y^2-2XZ:Z^2]$. Its affine restriction is an
  isomorphism, so is quasi-finite and étale. The target
  $Y_0=\{[0:1:1]\}$ is a smooth reduced point, of codimension two.
- The second affine coordinate of $H^n$ has total degree $2^n$,
  by induction from its monic leading term. Hence $d_1(H)=2$.
  Birationality gives $d_2(H)=1$; **$d_2$ is not the Jacobian 2**.
- Every inverse iterate is a morphism on $\mathbb A^2$. Over an
  affine target, the graph projection of $H^n$ is the graph of this
  inverse, an isomorphism with unique affine source. There are no
  additional sources at indeterminacy or infinity over this open
  set: its graph is closed in $\mathbb P^2\times\mathbb A^2$ and
  agrees with the dense affine inverse graph. All backward targets
  stay affine. Thus $Y_0$ lies in the required iterative finite locus.
- Equation (5) implies the usual projective height of $H^n(P)$ is
  $\Theta(2^n)$, and its arithmetic degree is 2. The affine version
  of Proposition 3.4 therefore gives Zariski density. Genericity
  follows also from Bell–Ghioca–Tucker's étale result,
  [Corollary 1.4](https://arxiv.org/pdf/0808.3266v1), since intersections
  with proper affine subvarieties are finite; adding infinity adds
  no orbit points. The target-degree inequality is
  $d_2(H)^{1/2}=1<2=\alpha_H(P)$.
- Translate affine coordinates by $(x,y)\mapsto(x,y-1)$. For this
  orbit the resulting homogeneous coordinates are
  $[u_n:u_{n+1}-1:1]$, which are primitive integers and do not equal
  the origin. The point gcd-height is $\log D_n$ for the customary
  normalization, up to the permitted bounded change of height;
  the Archimedean correction is zero because the maximum absolute
  value of the two integer coordinates, not simultaneously zero, is
  at least 1. Together with $h(H^n(P))=O(2^n)$, the cited vanishing
  ratio gives (3) again.

This verifies applicability, not the full internal proof of that
24-page preprint. The elementary proof in Section 2 is independent
of it and of all of these geometric facts. It would remain a complete
proof if this cross-check were removed.

The [Barrios correction, published 22 July 2026](https://doi.org/10.1017/S0004972726101543),
adds an ample-normal-bundle condition to the earlier positive-dimensional
bound. It explicitly distinguishes Matsuzawa's alternative inequality.
Neither the superseded bound nor its correction is used above. No
unverified version-2 preprint or Vojta conditional result is substituted
for the actually accessed version 1.

## 4. Proof audit and limits

All rational points, all integer parameters in DH1, and all positive
native times in DH2 have been treated. The integrality proof includes
all primes; the return-gcd proof separately explains why its inverse
step is legitimate at every prime dividing $D_n$. No genericity
assumption or conjecture is hidden in either elementary proof.

Terminology correction to the frozen source-test prose: its phrase
“diagonal target” is a wording error, not a different contract. The
displayed return gcd there and throughout this note specifies the
fixed point $(0,1)$, a codimension-two target; no diagonal subvariety
or new target has been substituted. The frozen equations are unchanged.

This is author-side reasoning, not an independent referee certificate.
Both frozen mathematical statements close, but neither has a
substantial independent increment after classical/source deduction.
No further candidate, parameter scan, prefix test, or manuscript is
recommended on these contracts. `NO_BAD_EULER_OR_ROOT_NUMBER` is
unchanged: neither arithmetic result identifies target Euler factors,
root numbers, automorphy, target zeros, or a Hilbert–Pólya operator.
