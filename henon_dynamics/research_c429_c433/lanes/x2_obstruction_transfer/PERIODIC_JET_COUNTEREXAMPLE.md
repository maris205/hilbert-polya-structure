# Proof package: no degree-independent finite-jet integrality criterion

2026-09-09 UTC. X2 hand derivation; no mathematical program or external
model was used. This is a scoped interface falsifier, not an admitted paper
or a formal evaluation. Primary consumer: B4; secondary consumer: B3.

## Claim

Fix a prime $p$ and a positive integer $N$. There is a polynomial Hénon
automorphism $F/\mathbb Q_p$ such that:

1. No finite extension of $\mathbb Q_p$ admits an affine coordinate change
   giving $F$ good reduction in the precise C426/GR5 sense.
2. At every geometric periodic point, the centered order-$N$ jets of
   every forward and inverse native return have integral coefficients
   and invertible linear part. This holds at every repetition as well.
3. In the standard centered coordinates the forward step jet reduces,
   through order $N$, to the same linear map $J(u,v)=(v,-u)$ at every
   point of every periodic orbit.

Thus the converse “all periodic return jets through one fixed order are
integral and locally invertible, hence potential affine good reduction”
is false when the degree is unrestricted. No claim is made about every
exact finite-jet invariant, a cutoff depending on degree, or a single
globally compatible integral model covering the periodic points.

## Status

PROVABLE AS STATED, conditional only on the already proved C426/GR5
all-affine local-rigidity theorem stated below. The new estimate is
proved here. It has not yet received an independent internal check.

## Assumptions and notation

Normalize $|p|=p^{-1}$ on $\overline{\mathbb Q}_p$. Integral means
absolute value at most one, over any finite extension containing the
finitely many coefficients and points in question. Put

$$
 L=\lfloor\log_p N\rfloor,\qquad r=L+3,\qquad
 k=p^r,\qquad d=p^{r+1},\qquad \Delta=d-k,
$$

$$
 f(Y)=Y^d+p^{-1}Y^k,\qquad
 F(x,y)=(y,f(y)-x),\qquad R=p^{1/\Delta}>1.
 \tag{1}
$$

In particular $N<k<d$. An order-$N$ jet means truncation in total
degree at $N$, using polynomial coefficients/Hasse derivatives, not
unscaled ordinary derivative values. For a periodic point
$P_i=(z_i,z_{i+1})$, the centered step is

$$
 \tau_{P_{i+1}}^{-1}F\tau_{P_i}(u,v)
 =(v,f(z_{i+1}+v)-f(z_{i+1})-u),
 \quad \tau_P(w)=P+w.
 \tag{2}
$$

Good reduction means forward and inverse coefficients integral, both
degrees preserved, and the two reduced indeterminacy sets at infinity
disjoint. It is not mere integrality of a finite jet.

## Proof strategy and dependency map

1. The native periodic recurrence bounds all coordinates by $R$.
2. A binomial valuation identity bounds every coefficient through $N$.
3. Composition in the truncated power-series ring transports the bound
   to every return and inverse return without losing the native clock.
4. C426's all-affine local rigidity fixes the only possible good-disc
   radius at one. Two fixed points of its scalar auxiliary polynomial
   are farther than one apart, ruling out that disc after every finite
   base extension.

Imported source: [C426 classification](../../../research_c424_c428/papers/C426_affine_good_models/sections/02_classification.tex),
Theorem `thm:main`, local parts;
[local rigidity](../../../research_c424_c428/papers/C426_affine_good_models/sections/03_local_rigidity.tex),
Lemma `lem:rigidity`; and
[disc uniqueness](../../../research_c424_c428/papers/C426_affine_good_models/sections/04_local_test.tex),
Lemmas `lem:scalar`, `lem:unique`. The proofs use only a
characteristic-zero complete discretely valued field at these steps.
WM6 already owns the $N=1$ norm-platform mechanism and the large-root
argument; this supplement's increment is the uniform prescribed-$N$
estimate, not a new proof of GR5 or WM6.

## Proof

### Step 1. All native periodic coordinates are bounded

Write the orbit recurrence, with cyclic indices, as

$$z_{i+2}+z_i=z_{i+1}^{d}+p^{-1}z_{i+1}^{k}. \tag{3}$$

Let $M=\max_i|z_i|$. If $M>R$, at a maximizing coordinate the
degree-$d$ term strictly dominates the other right-hand term, because
$M^{d-k}>p$. The right-hand side has norm $M^d>M$, whereas the
left-hand side has norm at most $M$. This is impossible. Hence
$|z_i|\le R$ for every point on every periodic orbit, including
periods one and two.

### Step 2. Every prescribed low coefficient is small

For $s\ge1$ and $1\le j<p^s$,

$$v_p\binom{p^s}{j}=s-v_p(j). \tag{4}$$

Indeed, $\binom{p^s}{j}=(p^s/j)\binom{p^s-1}{j-1}$, and the latter
binomial coefficient is a $p$-adic unit. To see the unit assertion
directly, in $\mathbb F_p[T]$ the coefficients of
$(1+T)^{p^s-1}=(1+T^{p^s})/(1+T)$ in degrees below $p^s$ are
$(-1)^a$, which are nonzero. This also includes $p=2$.

For $1\le j\le N$, let $b_j(z)$ be the coefficient of $u^j$ in
$f(z+u)-f(z)$. When $|z|\le R$, (4) gives

$$
\begin{aligned}
 |b_j(z)|
 &\le\max\left\{
 p^{-(r+1)+v_p(j)}R^{d-j},
 p\,p^{-r+v_p(j)}R^{k-j}\right\}\\
 &\le p^{-r+v_p(j)}R^{d-j}\qquad(R^{d-k}=p)\\
 &=p^{-r+v_p(j)+(d-j)/(d-k)}<1.
\end{aligned}
\tag{5}
$$

The last exponent is strictly smaller than
$-r+L+p/(p-1)\le-3+2=-1$. Consequently the order-$N$ truncation
of (2) has integral coefficients and reduces to $J$. Its linear
determinant is one, independent of $b_1$.

The inverse map is $F^{-1}(x,y)=(f(x)-y,x)$. The centered inverse
step uses the same $b_j(z_i)$, so it is integral through degree $N$
and reduces to $J^{-1}$.

### Step 3. Every return, every repetition, and base extension

All centered step maps have zero constant term. Therefore a coefficient
of total degree at most $N$ in a composition depends only on step
coefficients of degrees at most $N$; omitted higher terms cannot
contribute. The truncated polynomial ring over a valuation ring is
closed under composition of zero-constant-term maps. It follows that
the order-$N$ jet of $F^n$ at a period-$n$ point and that of $F^{-n}$
are integral, with linear determinant one. Repeating the same argument
gives all positive repetitions; inverse steps give all negative ones.
Modulo the maximal ideal, the return jet is $J^n$.

These are statements over a finite extension containing the particular
orbit. Extending that field preserves all displayed absolute values
and the integrality conclusions. Integral linear changes of each
centered tangent basis also preserve integrality. Arbitrary nonintegral
rescalings need not preserve the raw coefficient inequalities.

### Step 4. No potential all-affine good model

Suppose there were a good model over a finite extension $E/\mathbb Q_p$.
For the monic single-factor Hénon map, C426/GR5 forces its image lattice
to be $(u+s\mathcal O_E)^2$ with $|s|^{d-1}=1$, hence $|s|=1$.
Moreover the scalar auxiliary polynomial $q=f-Y$ has a good scalar
model on $u+s\mathcal O_E$ and its bounded forward set is that disc.

The polynomial

$$g(Y)=Y^{d-1}+p^{-1}Y^{k-1}-2 \tag{6}$$

has a root $\xi$ with $|\xi|=R$. No root can have norm greater than
$R$, since the leading term would dominate the other two. If all
$d-1$ roots had norm less than $R$, their elementary symmetric
polynomial of order $d-k$ would have norm less than $R^{d-k}=p$.
Vieta's formula identifies that coefficient, up to sign, with
$p^{-1}$, whose norm is $p$, a contradiction. Repeated and zero
roots do not affect this argument.

After further finite extension to contain $\xi$, goodness persists.
But (6) gives $q(\xi)=\xi$, and also $q(0)=0$. These two bounded
points have distance $R>1$ and cannot both lie in a radius-one disc.
This contradicts GR5. It proves assertion 1 and completes the claim.
$\square$

## Corrections or missing assumptions

There is no claim that the exact jet coefficients coincide with those
of a good map, or that the complete period-count ledger coincides.
For comparison the good map $F_0=(y,y^d-x)$ also has reduced
order-$N$ step jets equal to $J$ at all periodic points, but the
number and least periods of the points have not been matched.

The independent local charts in (2) are not one global good chart.
Their failure to patch is explicit: $0$ and $\xi$ cannot share the
required unit disc. A proposed intrinsic B4 observable may use this
cross-point information; this proof does not rule that out.

## Open risks

- The source's good-reduction definition and its all-affine restriction
  are essential; nonaffine polynomial or birational models are outside
  the claim.
- This is a family with degree growing with $N$. It does not settle
  the fixed-degree question or an order cutoff $N(d)$.
- A source/collision check and independent proof check are still required
  before any stronger admission claim. No novelty priority is asserted.
