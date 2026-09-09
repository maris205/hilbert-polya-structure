# Independent bounded review of the original Adler question

2026-09-08 UTC. Current-team internal mathematical review, not human peer
review, not a new candidate and not an admission decision. The original
[NL424-3 contract](../FROZEN_SCOUTS.md) and [first-pass report](../SCOUT_REPORT.md)
were read completely. The parameter triple, invariant map, affine rational
points, factorwise cancellation convention and native transfer clock are
unchanged. No mathematical program, parameter census, symbolic engine,
old experiment, external-model review, TeX build or Git mutation was run.

## Claim and status

The proposed closure route is assessed against the original request to
classify every ordinary rational periodic point on every invariant fibre,
including its maximal factorwise two-sided regular domain.

**Original full contract: NOT CURRENTLY JUSTIFIED by the route supplied for
this review.** This is a proof-status statement at this review's cutoff,
not a verdict on the coordinator's concurrent singular-fibre work.

**Smooth-fibre claim: PROVABLE AFTER CORRECTION.** The transfer is indeed
translation by the specified nonzero point at infinity. Its possible
native rational least periods on smooth fibres are exactly
$\{2,3,4,5,6,7,8,9,10,12\}$ as all rational parameters and smooth levels
vary. The proposed exclusion of period two is false, with a native-domain
counterexample below. The bound, two-involution mechanism and availability
of positive-rank torsion examples are classical/source-owned; the corrected
smooth result is not recommended as a separate paper.

## Assumptions, notation and dependencies

Write $x=x_1$, $y=x_2$, $z=s-x-y$, and let $C$ be the projective completion
of the full affine level. Its affine equation is

$$
f(x,y)=(x+y)(s-x)(s-y)+\beta_1(s-x)+\beta_2(s-y)
       +\beta_3(x+y)-h=0.
$$

Let $\rho_{12}$ and $\rho_{13}$ denote the original two-site operations
restricted to this level, in that order, so $T=\rho_{13}\rho_{12}$.
On a smooth projective fibre they extend to curve automorphisms; this
extension is a proof device, not a replacement of the native affine domain.

The dependency chain is:

1. Direct homogenization and tangent calculation determine the three
   rational points at infinity and detect the nonflex-origin error.
2. The genus-one divisor group law determines the actual two chord
   involutions, whose constant terms cancel in their composition.
3. Mazur's rational torsion theorem bounds the nonzero translation order.
4. A finite factorwise bad set restores the exact native domain for a
   torsion translation; an explicit counterexample supplies period two.
5. A rational coordinate normalization plus published positive-rank
   torsion examples supplies the converse for the other allowed orders.
6. Elementary factorization observations reduce, but do not complete,
   the singular-fibre part of the original contract.

For the standard inputs, the arbitrary-origin group construction and its
identification with $\operatorname{Pic}^0$ are stated in Milne, I.3.1 and
I.4.10; his II.5.11 records Mazur's torsion list. These are mathematical
inputs, not new claims of this review. [Milne, author-hosted second edition](https://www.jmilne.org/math/Books/EC2.pdf).

## Proof and counterexample

### 1. The origin need not be a flex

The homogeneous cubic is

$$
\begin{aligned}
F(X,Y,W)={}&XY(X+Y)-s(X+Y)^2W\\
 &+\bigl((s^2+\beta_3-\beta_1)X
          +(s^2+\beta_3-\beta_2)Y\bigr)W^2\\
 &+\bigl(s(\beta_1+\beta_2)-h\bigr)W^3.
\end{aligned}
$$

The only points with $W=0$ are

$$
O=[1:0:0],\qquad Q=[0:1:0],\qquad R=[1:-1:0].
$$

At $O$, $F_Y=1$; at $Q$, $F_X=1$; at $R$, $F_X=F_Y=-1$.
Thus all three are smooth points of every projective fibre, whether or
not that fibre is smooth elsewhere.

The tangent at $O$ is $Y=sW$. Substitution gives the exact restriction

$$
F(X,sW,W)=W^2\bigl((\beta_3-\beta_1)X
             +(s(\beta_1+\beta_3)-h)W\bigr).
$$

Consequently $O$ is not a flex when $\beta_3\ne\beta_1$.
On a smooth fibre it is a flex when $\beta_3=\beta_1$: the remaining
coefficient cannot also vanish, since that would make the tangent line
a component of a smooth cubic.

Choose $O$ as group origin, and let $K$ denote the degree-zero divisor
class of a line section minus $3[O]$, viewed as a point of $(C,O)$.
Collinear intersections, with multiplicities, have group sum $K$, not
necessarily zero. In particular

$$
Q+R=K.
$$

The inference $Q\ne R\Longrightarrow 2R\ne O$ therefore fails in this
general embedding. It would be valid after additionally proving $K=O$,
which is not an assumption of the frozen family.

### 2. The translation conclusion nevertheless survives

Lines with $x+y$ fixed pass through $R$. On such a line put $q=x+y$.
For $q\ne0$, the sum of the two residual roots in $x$ of $f(x,q-x)=0$
is

$$
q+\frac{\beta_2-\beta_1}{q}.
$$

The other root is exactly the first coordinate produced by $\rho_{12}$.
Thus this operation is the chord involution through $R$. Lines with $y$
fixed pass through $O$, and the same two-site root identity identifies
$\rho_{13}$ with the chord involution through $O$. These identities hold
on a dense open subset, hence for their extensions on the smooth curve.
When a parameter difference is zero, the original operation is still
the everywhere-regular swap stipulated in the contract.

The actual group formulas are

$$
\rho_{12}(P)=K-R-P,\qquad \rho_{13}(P)=K-P.
$$

Their composition in the frozen order is therefore

$$
T(P)=K-(K-R-P)=P+R.
$$

Since $R\ne O$, there are no fixed points of this translation on a smooth
fibre. If $R$ has infinite order there are no periodic points there. If
$R$ has finite order $n$, every projective point has exact period $n$:
the equality $P+jR=P$ is equivalent to $jR=O$.

As $C$ and $O,R$ are defined over $\mathbb Q$, Mazur's theorem gives

$$
n\in\{2,3,4,5,6,7,8,9,10,12\}.
$$

This argument bounds point order, not the cardinality of the torsion
subgroup, and does not change one transfer tick into an extended-transfer
tick.

### 3. The factorwise native domain must be retained

Let $U\subset C(\mathbb Q)$ consist of affine points for which the two
successive original operations $\rho_{12}$ and $\rho_{13}$ are regular
under the contract's zero-difference cancellation convention. Set
$B=C(\mathbb Q)\setminus U$.

This is a finite set on a smooth fibre. It contains the three points at
infinity. Its other members are the forbidden zeros of $x+y$ when
$\beta_1\ne\beta_2$, and the forbidden zeros of the first-plus-third
coordinate after a regular $\rho_{12}$ when $\beta_1\ne\beta_3$.
Each condition is a zero of a nonzero rational function on a smooth
irreducible cubic. No forbidden denominator is deleted when its parameter
difference is zero.

The exact two-sided native set is

$$
D_{\mathrm{nat}}=C(\mathbb Q)\setminus
                  \bigcup_{j\in\mathbb Z}T^{-j}B.
$$

Indeed, membership means that every starting point of every transfer tick
is affine and both operations of that tick are regular. Conversely, a
native two-sided trajectory avoids every such inverse image. Each two-site
operation is an involution on its regular locus, so these same admissible
factor steps also give the required inverse iterations.

When $R$ has order $n$, the union can be taken over $0\le j<n$.
Equivalently, a finite affine point has the predicted native period iff
all $2n$ factor steps around its projective cycle are admissible. For
infinite-order $R$, no domain point can be periodic, regardless of whether
the displayed infinite union is easy to enumerate.

This is a fibrewise group-theoretic description, not a claimed unconditional
algorithm for finding Mordell--Weil generators of every rational elliptic
curve. In particular, projective periodicity alone is not sufficient.

### 4. A smooth native period-two counterexample

Take

$$
(\beta_1,\beta_2,\beta_3)=(0,4,1),\qquad s=h=0,
\qquad P=(1,1,-2).
$$

The affine fibre is

$$
f(x,y)=xy(x+y)+x-3y=0.
$$

It is geometrically smooth. If an affine singular point existed, the
equalities $f=f_x=f_y=0$ and
$xf_x+yf_y=3xy(x+y)+x-3y$ would imply both $xy(x+y)=0$ and $x-3y=0$.
They force $x=y=0$, where $(f_x,f_y)=(1,-3)$ is nonzero. Smoothness at
infinity was already checked in Step 1.

The original factor operations give

$$
\begin{aligned}
(1,1,-2)&\xrightarrow{\rho_{12}}(3,-1,-2)
          \xrightarrow{\rho_{13}}(-1,-1,2),\\
(-1,-1,2)&\xrightarrow{\rho_{12}}(-3,1,2)
          \xrightarrow{\rho_{13}}(1,1,-2).
\end{aligned}
$$

The four denominators are $2,1,-2,-1$, respectively. They are all nonzero;
reversing these involutions is also regular. The two transfer states are
distinct, so this is exact native period two, not a pole-crossing or
singular-fibre artifact. All equalities in this example were checked by
direct hand substitution, without a mathematical program.

### 5. The proposed converse works for orders at least three

Let $(E,O)$ be a rational elliptic curve with a rational point $A$ of
order $n\ge3$. Use its plane Weierstrass embedding. The three distinct
points $O,A,-A$ lie on a rational line. A rational projective coordinate
change sends that line to $W=0$, and sends the ordered points to the
three positions $O,R,Q$ above. After scaling the equation, the affine
cubic has the form

$$
g(x,y)=xy(x+y)+a x^2+bxy+c y^2+d x+e y+f_0.
$$

Set

$$
s=\frac{b-2a-2c}{2},\qquad
x=u+p,\quad y=v+q,\qquad p=-s-c,\quad q=-s-a.
$$

The new quadratic coefficients are $a+q$, $b+2(p+q)$ and $c+p$,
which are $-s,-2s,-s$. If the remaining new coefficients are $d',e',f'$
then the choices

$$
\beta_3=0,\qquad \beta_1=s^2-d',\qquad
\beta_2=s^2-e',\qquad h=s(\beta_1+\beta_2)-f'
$$

give exactly the original Adler fibre equation. The transformation keeps
the labelled points at infinity, so Step 2 makes the native transfer's
projective extension translation by $A$.

The smooth Weierstrass origin remains a flex under these transformations;
therefore this construction lands in the subfamily $\beta_1=\beta_3$.
That is sufficient for existence, but explains why its flex property must
not be imposed on the entire frozen three-parameter family.

For every $n\in\{3,4,5,6,7,8,9,10,12\}$, rational elliptic curves with
positive rank and a rational point of exact order $n$ are already supplied
by Los--Mepschen--Top. We import that existence assertion, not their
Poncelet coordinate formulas. [Author-uploaded text, Sections 3.1 and 5](https://www.researchgate.net/publication/325299681_Rational_Poncelet).

On each such curve the finite set $\bigcup_{j=0}^{n-1}T^{-j}B$ contains
at most $n|B|$ rational points, while $E(\mathbb Q)$ is infinite. There
are therefore rational points outside it, and each has exact native period
$n$. Combined with Step 4, this proves sharpness of the corrected smooth
period list. The finite-set avoidance is an elementary inference in the
present coordinates, not a new positive-rank construction.

## Boundary checks that do not finish the original full contract

### All fibres are geometrically reduced

If the homogeneous cubic had a repeated homogeneous factor $G^2$ over
$\overline{\mathbb Q}$, then either its restriction $G(X,Y,0)$ is
nonzero, forcing a repeated factor in $XY(X+Y)$, or that restriction is
zero, forcing $W\mid G$ and hence $W^2\mid F$. Both are impossible.
Thus there is no nonreduced-fibre branch to classify for this exact family.

Every geometric component meets $W=0$. At each of the three rational
points there is only one component, because the cubic is smooth there.
Galois therefore fixes each component containing that point; since every
component contains at least one such point, every geometric component is
defined over $\mathbb Q$.

### The three-line case is the all-swap case

If the cubic is a union of three lines, the leading directions force its
affine equation, with leading coefficient normalized, to be

$$
(x-a)(y-b)(x+y-c).
$$

Comparing the three quadratic coefficients with $-s(x+y)^2$ gives
$a=b=s$ and $c=0$. Comparing the remaining coefficients gives
$\beta_1=\beta_2=\beta_3$ and $h=2s\beta_1$. Thus it is exactly

$$
(x-s)(y-s)(x+y)=0.
$$

Both original operations are regular swaps, so the full native map is
$(x,y,z)\mapsto(z,x,y)$. Every point has least period one or three,
with period one precisely when all three coordinates agree. This treats
both the triangle and the concurrent-line specialization and does not
create a possible period eighteen by multiplying loose component bounds.

### Remaining proof obligations

The smooth-fibre argument does not classify the irreducible singular
cubics or the line--conic fibres. A complete reviewable closure still needs
their precise parameter conditions, restrictions of both original factors,
component permutation, rational return map, all ordinary component
intersections and singular points, and the factorwise deleted-pole test.
This report does not assert that those obligations are difficult, impossible
or still unmet by work the coordinator completes after this cutoff.

In particular, the phrase “chord involution through $R$” cannot simply be
applied to a whole line component containing $R$: its chord is then the
component itself, and the generic two-residual-intersection argument no
longer defines the map there. The original rational formula, including
the equal-parameter swap convention, decides that restriction.

## Source subtraction and exact access record

The following are fresh bounded checks on 2026-09-08, not worldwide
novelty certification. Remote text sections were read; no local downloaded
PDF page anchor or structural preflight is asserted.

- **Milne:** author-hosted second-edition PDF opened successfully. Actual
  mathematical access: I.3.1 and its group construction, I.4.10, II.5.11;
  not all 241 displayed PDF pages. Arbitrary-origin divisor arithmetic and
  the rational torsion restriction are fully deducted. The large original
  Mazur proof was not read here. [Author PDF](https://www.jmilne.org/math/Books/EC2.pdf).
- **Los--Mepschen--Top, Rational Poncelet:** institution metadata verifies
  IJNT 14(10), 2641--2655 (2018), DOI 10.1142/S1793042118501580. The
  author-site PDF timed out; the institution's final-author PDF returned
  403. Its author-uploaded ResearchGate text was then read in the
  introduction, Theorems 1.1--1.2, Corollary 1.3, Section 2 through the
  quotient construction, Section 3.1 and the period-three part of Section
  5. These already supply the two-involution torsion mechanism and
  positive-rank examples for all relevant orders. Not all explicit
  configuration tables or quadratic-field constructions were audited.
  [Institution record](https://research.rug.nl/nl/publications/rational-poncelet/),
  [author-uploaded text](https://www.researchgate.net/publication/325299681_Rational_Poncelet).
- **Inherited Adler ownership:** the original report's Veselov and
  Kassotakis audit remains the source for the already-owned exact transfer,
  invariants and extended-clock distinction. It was read as a local audit,
  not represented as a fresh full-text verification in this follow-up.
- **Coordinator-only additional leads:** Adler's triad-map preprint and
  the old rational Lyness classification were reported by the coordinator.
  No new theorem from their unseen text is imported here. Their possible
  residual collision strengthens the need for subtraction; it does not
  by itself prove that they solve this same original native Adler contract.

Actual new search strings were:

```text
"Rational Poncelet" Top
elliptic curve plane cubic rational origin not flex collinear divisor group law
"Los" "Mepschen" "Rational Poncelet" pdf
"Rational Poncelet" "rank"
site.jmilne.org elliptic curves arbitrary point origin plane cubic divisor
```

Search results were locators. The theorem dependencies above use authored
mathematical sources, not secondary search summaries. The failed primary
PDF URLs are preserved as access failures rather than marked read.

## Disposition and stopping boundary

The initial lower-period claim is refuted. Its smooth translation mechanism
is repaired and the corrected smooth period set is sharp, with the native
domain explicitly restored. Some degenerate boundary branches are eliminated
or classified, but the original all-fibre contract has not been certified
by this bounded review. No favourable paper-level increment or admission
follows from this file; a generic torsion corollary must not occupy a paper
slot. The coordinator's full singular-fibre algebra, if completed, requires
its own actual proof/source/increment adjudication.

The research-review and proof-writer skills shaped this counterexample-first,
corrected-claim report. Under the active repository batch instruction, the
current selected team was used instead of the legacy review skill's named
external GPT-5.4/MCP workflow; no such external review is claimed. The
bounded report is the only file written by this subtask. The earlier AM1
author package and all shared or frozen files remain untouched.

`NO_BAD_EULER_OR_ROOT_NUMBER` remains unconditional. No formal Route-A
evaluation, target Euler factor, root number, automorphy, divisor matching
or Hilbert--Pólya conclusion is made.
