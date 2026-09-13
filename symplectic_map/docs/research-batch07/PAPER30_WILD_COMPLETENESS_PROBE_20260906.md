# Paper30 wild-cover completeness probe: a rigorous bounded exclusion

Date: 2026-09-06. This is a bounded proof-feasibility probe, not a candidate
score, a complete classification, or a formal paper project.

Input: `PAPER30_WILD_COVER_FIRST_PROBE_20260906.md`, 202 lines, supplied SHA256
`0a0db518aff8cba19ca56cff2d687c0e5ac6bbd5428efa3a1523706aa05c2e42`.
The independent audit of that input is a different agent's assignment;
this document does not duplicate it. The proof-writer workflow is used here.
No Route A/B claim, cross-candidate page pooling, or external effect occurs.

## Claim

Fix an algebraically closed field $K$ of characteristic two and set
$$
A=K[x,y],\qquad H(x,y)=(x^3+1+y,x),\qquad \sigma=H^*.
$$
Write $\wp(u)=u^2+u$ and $Q=A/\wp(A)$ as an additive
$\mathbb F_2$-vector space. The original, unrestricted completeness target is
$$
Q^\sigma\stackrel{?}{=}\{[a xy]:a^4=a\}.                 \tag{C}
$$
The right side is the known two-dimensional $\mathbb F_2$-space from the
author's first probe. The restriction to this one map is deliberate.

**Actual new theorem.** Let $R(g)$ be the unique zero-constant representative
whose monomials $x^i y^j$ have $i,j$ not both even. If $[g]\in Q^\sigma$
and
$$
\deg_x R(g)\le6,\qquad \deg_y R(g)\le6,
$$
then $R(g)=a xy$ with $a^4=a$. Conversely all these polynomials represent
invariant classes. More generally, every nonzero invariant reduced
representative has equal $x$ and $y$ degrees. Consequently an invariant class
outside the known slice, if one exists, has both partial degrees at least
seven. An invariant class admitting any representative of $y$ degree at most
one belongs to the known slice, with no imposed bound on its $x$ degree.

## Status

Original target (C): **NOT CURRENTLY JUSTIFIED / OPEN**.

Actual bounded theorem: **PROVABLE AS STATED / PROVED below**. This is a
strictly weaker statement, not a replacement of (C) without notice. No
outside-slice counterexample was obtained. No global degree bound was proved.

## Assumptions and notation

- Coefficients range over all of $K$, not just a finite subfield.
- Frobenius is bijective on $K$. The notation $a^{1/2^s}$ denotes its unique
  inverse image, not a choice among several roots.
- For a nonzero reduced polynomial $g$, write
  $g=\sum c_{ij}x^iy^j$ with finite support and $c_{00}=0$.
- The quotient $Q$ is not a $K$-linear quotient or an algebra. All reduction
  formulas below are additive and $\mathbb F_2$-linear; their dependence on
  coefficients can be Frobenius-semilinear.
- The zero class is included in the theorem and is handled separately from
  partial-degree statements.

## Proof strategy

Use the actual Frobenius-reduced highest rows rather than a degree-growth
heuristic before reduction. First show that substitution retains its top
$y$ row exactly. This balances both partial degrees for an invariant class
and identifies its two boundary coefficient rows. Next eliminate balanced
degrees $6,5,4,3,2$ through mixed or pure monomials with unique sources.
All possible extra contributions from Frobenius reduction are bounded
explicitly. Finally solve the remaining bidegree-one equation.

## Dependency map

1. Frobenius-chain normal form establishes equality testing in $Q$.
2. The highest-row lemma uses normal form and the monicity of $H_1$ in $y$.
3. The mixed-row estimate controls terms lowered into a chosen row by
   Frobenius reduction.
4. The bounded exclusion uses steps 2–3 and five explicit highest-term
   arguments; it has no dependence on a finite-field search.
5. The unrestricted target (C) would additionally require an argument for
   arbitrarily large balanced partial degree; no such dependency is closed.

## Proof

### Step 1. Bivariate normal form

Every nonconstant exponent pair can be written uniquely as
$2^s(i,j)$ with $i,j$ not both even. On each such Frobenius chain replace
$$
a x^{2i}y^{2j}\quad\hbox{by}\quad a^{1/2}x^iy^j.
$$
The difference is $\wp(a^{1/2}x^iy^j)$. Repetition terminates, and constants
can be removed because $K$ is algebraically closed. This proves existence
of $R(g)$.

For uniqueness, suppose a reduced polynomial equals $\wp(u)$. Decompose the
nonconstant terms of $u$ into their disjoint Frobenius chains. If a chain of
$u$ is nonempty, choose its largest occupied index $s$. The coefficient at
index $s+1$ in $u^2+u$ is the nonzero square of the coefficient at $s$;
there is no term of $u$ at $s+1$ to cancel it. It cannot occur in a reduced
polynomial, whose only allowed chain index is zero. Thus $u$ is constant
and the zero-constant reduced polynomial is zero. Subtraction proves
uniqueness. In particular,
$$
[g]=[h]\quad\Longleftrightarrow\quad R(g)=R(h).
$$

### Step 2. Highest-row preservation and degree balance

Let $g\ne0$ be reduced and put $n=\deg_xg$. For $n>0$, the coefficient of
$y^n$ in
$$
\sigma g=\sum_{i,j}c_{ij}(x^3+y+1)^i x^j
$$
is exactly $\sum_j c_{nj}x^j$. Each monomial in this row is already reduced:
if $n$ is even, reducedness of the input forces every relevant $j$ to be
odd; if $n$ is odd there is no restriction on $j$. No term of smaller
$y$ degree can reduce to a term of $y$ degree $n$, and no larger $y$ degree
is present. The top row therefore survives unchanged. For $n=0$, $g$ is
a nonconstant reduced polynomial in $y$, and $\sigma g=g(x)$ is a nonzero
reduced polynomial of $y$ degree zero. Thus in both cases
$$
\deg_y R(\sigma g)=\deg_xg.                            \tag{1}
$$
If $[g]$ is invariant, uniqueness gives $R(\sigma g)=g$, so
$$
\deg_xg=\deg_yg=n.                                    \tag{2}
$$
For $n>0$, comparison of the top $y$ row also yields
$$
c_{nj}=c_{jn}\qquad(0\le j\le n).                     \tag{3}
$$
Only boundary-row symmetry is asserted; (3) is not a claim that the entire
coefficient matrix is symmetric.

### Step 3. Terms that Frobenius reduction can move into a mixed row

Assume $g$ has both partial degrees at most $n$. Before reduction, the
coefficient of $y^b$ in $\sigma g$ is
$$
\sum_{i\ge b,j}\binom{i}{b}c_{ij}(x^3+1)^{i-b}x^j,    \tag{4}
$$
with binomial coefficients taken in characteristic two. Every monomial
$x^a y^b$ in this row satisfies
$$
a\le3(n-b)+n.
$$
To become a monomial of $y$ degree $k>0$ by at least one Frobenius reduction,
it must have $b=2^s k$ for some $s\ge1$; its resulting $x$ exponent is then
bounded by
$$
\frac{3(n-2^s k)+n}{2^s}
=\frac{4n}{2^s}-3k.                                  \tag{5}
$$
If divisibility of $a$ fails, that contribution does not reach the row at
all. Hence (5), which deliberately allows some nonexistent terms, is still
a valid upper bound. Positive $y$ exponents never reduce to zero.

### Step 4. Exclude balanced degree six

Suppose $g$ is invariant and reduced with the balanced degree $n=6$.
The degree-six $x$ row is supported only at $j=1,3,5$. In (4) with $b=2$,
the indices $i\le6$ for which $\binom{i}{2}$ is odd are exactly $2,3,6$.
The contribution from $i=6$ is
$$
(x^3+1)^4\sum_{j\in\{1,3,5\}}c_{6j}x^j
=(x^{12}+1)\sum_{j\in\{1,3,5\}}c_{6j}x^j.
$$
The contributions from $i=2,3$ have $x$ degree at most $9$. A term reduced
from $y$ degree $4$ into degree $2$ has $x$ degree at most $6$ by (5), and
higher source degrees $8,16,\ldots$ are absent. Consequently the coefficients
of $x^{13}y^2,x^{15}y^2,x^{17}y^2$ in $R(\sigma g)$ are respectively
$c_{61},c_{63},c_{65}$. These monomials are themselves reduced and cannot
occur in $g$, whose $x$ degree is six. All three coefficients vanish,
contradicting $\deg_xg=6$.

### Step 5. Exclude balanced degrees five and three

For $n=5$, the direct $y$-degree-one row receives contributions only from
odd $i=1,3,5$. Its $i=5$ contribution is
$$
(x^3+1)^4\sum_{j=0}^5c_{5j}x^j
=(x^{12}+1)\sum_{j=0}^5c_{5j}x^j.
$$
The other odd $i$ contribute $x$ degree at most $11$. Every contribution
lowered into this row by Frobenius has degree at most $2n-3=7$ by (5).
Thus the coefficients of $x^{12+j}y$, $0\le j\le5$, are exactly $c_{5j}$.
They must vanish by invariance. This contradicts degree five.

For $n=3$, the direct odd indices are $i=1,3$, and the top contribution is
$$
(x^3+1)^2\sum_{j=0}^3c_{3j}x^j
=(x^6+1)\sum_{j=0}^3c_{3j}x^j.
$$
The $i=1$ contribution has degree at most $3$, as do all contributions
lowered into this row by (5). The coefficients of $x^{6+j}y$,
$0\le j\le3$, are exactly $c_{3j}$ and must vanish. This contradicts
degree three. These two arguments allow arbitrary coefficients in $K$.

### Step 6. Exclude balanced degrees four and two

For $n=4$, the top $x$ row consists of $c_{41}x^4y+c_{43}x^4y^3$.
Every monomial in $\sigma g$ has $x$ degree at most $15$. Its pure term
$x^{15}$ has the unique source $c_{43}x^4y^3$, since all rows $i\le3$
have maximum $x$ degree at most $13$. No Frobenius-reduced term can feed
$x^{15}$: this would require a pure term of degree at least $30$.
Invariance therefore gives $c_{43}=0$. Boundary symmetry (3) then gives
$c_{34}=0$. Now the coefficient of the reduced pure monomial $x^{13}$ is
exactly $c_{41}$: the only other possible leading source, $(i,j)=(3,4)$,
has just vanished. No pure degree at least $26$ is present. Hence
$c_{41}=0$, contradicting degree four.

For $n=2$, the top $x$ row has the single possible term $c_{21}x^2y$.
Its substitution contains $c_{21}x^7$. Every lower $x$ row contributes
degree at most $5$, and the entire substitution has $x$ degree at most
$7$. There is no term that can Frobenius-reduce into $x^7$. It follows
that $c_{21}=0$, contradicting degree two.

### Step 7. Solve degree one and conclude

A nonzero invariant reduced polynomial of balanced degree at most one has
the form
$$
g=a xy+b x+c y.
$$
Direct substitution and chain reduction give
$$
R(\sigma g+g)
=b x^3+(a^{1/4}+a+b+c)x+(b+c)y.                       \tag{6}
$$
Equation (6) vanishes exactly when $b=c=0$ and $a^{1/4}+a=0$, equivalently
$a^4=a$. The root set is the four-element field inside $K$; the map
$a\mapsto[a xy]$ is injective by normal-form uniqueness. Thus these
classes form a two-dimensional $\mathbb F_2$-space. The zero class is the
case $a=0$.

Steps 4–6 eliminate every other balanced degree in the interval from two
to six, proving the bounded theorem. A representative of $y$ degree at
most one reduces to another representative with that property; (1)–(2)
then force its $x$ degree to be at most one, proving the unrestricted-strip
corollary. $\square$

## Verification and counterexample probe boundary

Two small memory-only exact symbolic expansions were used as diagnostics,
at reduced boxes of side three and seven. They retained each coefficient
as a separate variable with its inverse-Frobenius exponent; coefficients
were not restricted to $\mathbb F_2$. The larger check had 48 input monomials
and used only singleton coefficient elimination, not a field enumeration,
numerical fit, or large search. Neither check produced an outside-slice
class. No diagnostic script or data file was created.

Those finite calculations are not evidence for unrestricted completeness.
In particular, the larger diagnostic is not promoted here into an additional
claimed classification theorem. The actual theorem above is proved entirely
by the written unique-source and reduction-bound arguments for partial
degree at most six. It remains subject to independent mathematical review.
No literature novelty claim is made, and no outside theorem is needed in
this elementary proof package.

## Corrections or missing assumptions

The full target (C) has not been shown false, but the present argument does
not justify it. Adding the explicit representative bound
$\deg_xR(g),\deg_yR(g)\le6$ yields the proved statement. That bound is a
restriction on the quantified class, not a consequence already known for
all invariant classes. The degree balance alone imposes no finite bound.

## Open risks and exact next obligation

The next obstruction is unbounded interaction among highest rows. For
example, at balanced degree seven the unreduced $y$-degree-one coefficient
of $x^{18}y$ can receive contributions from both $c_{70}$ and $c_{56}$.
Thus the isolated-highest-row argument used at degrees three and five does
not continue verbatim. Equation (5) still excludes a high-degree
Frobenius-reduction contribution to this particular monomial, but it does
not separate the two direct sources.

A full proof needs a terminating invariant or an injective leading-term
scheme controlling these coupled rows for all degrees, or a description of
the two-operator quotient strong enough to imply such a bound. An actual
counterexample instead needs an explicit reduced polynomial outside the
slice together with an exact identity $\sigma g+g=u^2+u$; none is supplied.

**Disposition:** retain the balanced-degree lemma and bounded exclusion as
real new progress, but keep unrestricted completeness **OPEN** and the
candidate unselected. These short results by themselves are not a
22–30-page paper and are unrelated to the quantum candidate's content.
