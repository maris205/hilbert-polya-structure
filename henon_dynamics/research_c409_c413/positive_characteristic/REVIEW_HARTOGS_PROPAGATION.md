# Independent review: propagation of a slice natural boundary to a joint face

2026-09-06. Requested by the parent agent as a bounded, independent
several-complex-variables check. This document does not edit or certify
the arithmetic author's separate gcd estimates or atomic-measure proof.

## Claim

Let $\mathbb D=\{z\in\mathbb C:|z|<1\}$ and let
$F\in\mathcal O(\mathbb D_x\times\mathbb D_y)$. Suppose there is
$y_*\in\mathbb D$ such that the holomorphic function
$x\mapsto F(x,y_*)$ has the entire unit circle as a natural boundary.
Then $F$ has no local joint holomorphic continuation through any point
of the face

$$
\Gamma_x=\{(x,y):|x|=1,\ |y|<1\}.
$$

The same conclusion holds for local joint meromorphic continuation.
The symmetric statement with the two coordinates exchanged also holds.

Here a local continuation through $P\in\Gamma_x$ means a function on
an open neighborhood of $P$ agreeing with $F$ on the interior overlap.
It is not a statement about a disconnected exterior germ, and it is not
a statement that every fixed complex-parameter slice has a natural
boundary.

## Status

**PROVABLE AS STATED.** The proposed Taylor-coefficient argument closes.
No nonpolar-parameter hypothesis, generic-slice qualification or extra
growth hypothesis is needed beyond joint holomorphy on the bidisc.

## Assumptions and notation

- The two discs have radius one and the parameter disc is connected.
- The distinguished parameter $y_*$ is an interior point.
- Natural boundary means that no germ of the distinguished slice
  continues holomorphically across any point of $\partial\mathbb D$.
- For a locally upper-bounded function $h$, its upper semicontinuous
  regularization is
  $$h^*(y)=\lim_{r\downarrow0}\sup_{|z-y|<r}h(z).$$
  The supremum includes $z=y$, so $h^*\geq h$ pointwise.
- We use $\log0=-\infty$ and allow the identically negative-infinite
  subharmonic function when forming envelopes.

## Proof strategy and dependencies

1. Expand in the first coordinate about a center inside the unit disc,
   close to the hypothetical continuation point.
2. Cauchy's inequality gives locally uniform upper bounds for the
   logarithmic coefficient sequence throughout the parameter disc.
3. Upper-envelope regularization and a decreasing limit give a genuine
   subharmonic majorant. Cauchy--Hadamard at $y_*$ forces it to achieve
   its global maximum, hence be constant.
4. A joint holomorphic cap would improve its coefficient bound on an
   open set of parameters, contradicting that constant value.
5. A meromorphic cap has a denominator nonzero at some nearby point
   of the same face, reducing to the holomorphic impossibility.

Classical analytic inputs are Cauchy's inequality, Cauchy--Hadamard,
the upper-envelope and decreasing-limit theorems for subharmonic
functions, their strong maximum principle, and the one-variable
identity theorem. Applicable source locations are recorded below.

## Proof

### Step 1. Assume a joint holomorphic cap and choose the center

Suppose a joint holomorphic continuation $H$ exists near
$(x_0,y_0)\in\Gamma_x$. Shrinking its neighborhood, choose $\rho>0$
and $\eta>0$ such that

$$
H\in\mathcal O(B(x_0,\rho)\times B(y_0,\eta)),\qquad
\overline{B(y_0,\eta)}\subset\mathbb D,
$$

and $H=F$ on the product's intersection with the bidisc. If the
continuation is initially specified by agreement on a nonempty open
part of that intersection, equality on the entire intersection follows
from the identity theorem: the intersection is a connected product of
intersections of discs.

Choose

$$
0<\delta<\min\{1/2,\rho/4\},\qquad
c=(1-\delta)x_0,\qquad M=-\log\delta.
$$

The center $c$ lies in $\mathbb D$ and its distance from the unit
circle is exactly $\delta$.

### Step 2. The Taylor coefficients are holomorphic in the parameter

For $n\geq0$, define

$$
a_n(y)=\frac{1}{n!}\partial_x^nF(c,y).
$$

Joint holomorphy makes every $a_n$ holomorphic on $\mathbb D$.
For any $0<r<\delta$ and any compact $K\subset\mathbb D$, Cauchy's
inequality on the compact product of the circle $|x-c|=r$ with $K$
gives a finite constant $C_{r,K}\geq1$ such that

$$
|a_n(y)|\leq C_{r,K}r^{-n}\qquad(y\in K, n\geq1).
\tag{1}
$$

For $n\geq1$ put $u_n(y)=n^{-1}\log|a_n(y)|$. Each $u_n$ is
subharmonic, possibly identically $-\infty$. Equation (1) proves the
essential locally uniform upper bound

$$
u_n(y)\leq-\log r+\frac{\log C_{r,K}}n.
\tag{2}
$$

### Step 3. A regularized tail envelope avoids all exceptional-set issues

Use the following convenient proof device:

$$
V_N=\left(\sup_{n\geq N}u_n\right)^*,\qquad
V=\lim_{N\to\infty}V_N.
\tag{3}
$$

The locally uniform upper bounds make each $V_N$ subharmonic by the
upper-envelope theorem. The functions $V_N$ decrease with $N$.
Their limit is therefore subharmonic or identically $-\infty$.

To retain (2) after regularization, first choose a compact neighborhood
of an arbitrary parameter point and apply (2) on that larger compact
set. Then, on its interior,

$$
V_N\leq-\log r+\frac{\log C_{r,K}}N.
$$

Taking $N\to\infty$ and then $r\uparrow\delta$ yields

$$V(y)\leq M\qquad(y\in\mathbb D).\tag{4}$$

At every parameter, regularization only raises the relevant supremum;
in particular

$$V(y_*)\geq\limsup_{n\to\infty}u_n(y_*).\tag{5}$$

The Taylor series of $F(\cdot,y_*)$ about $c$ has radius exactly
$\delta$. It has radius at least $\delta$ because the disc
$B(c,\delta)$ is inside $\mathbb D$. If its radius exceeded
$\delta$, the Taylor sum would extend that slice across $x_0$,
contradicting the natural-boundary hypothesis. Cauchy--Hadamard thus
gives

$$\limsup_{n\to\infty}u_n(y_*)=-\log\delta=M.\tag{6}$$

Equations (4)--(6) imply $V(y_*)=M$, so $V$ is not identically
$-\infty$. It is a subharmonic function on the connected parameter
disc that attains its global upper bound at an interior point. The
strong maximum principle gives

$$V\equiv M\quad\hbox{on }\mathbb D.\tag{7}$$

### Step 4. The cap gives a contradictory larger Taylor disc

The geometric estimate needed here is particularly short. If
$|x-c|\leq2\delta$, then

$$|x-x_0|\leq |x-c|+|c-x_0|\leq3\delta<\rho.$$

Consequently the entire closed disc $\overline{B(c,2\delta)}$ lies
inside the holomorphic cap in the first coordinate. This does not
require a glued-disc or tangency argument.

Choose $0<\eta'<\eta$. Cauchy's inequality for $H$ on the compact
product $\{|x-c|=2\delta\}\times\overline{B(y_0,\eta')}$ gives a
finite constant $C'\geq1$ such that

$$
|a_n(y)|\leq C'(2\delta)^{-n}
\quad(y\in\overline{B(y_0,\eta')},\ n\geq1).
$$

These are the same coefficients as those of $F$, since $c$ is an
interior point and $H=F$ there. Repeating the tail-envelope estimate
on the interior of this parameter disc yields

$$V(y)\leq-\log(2\delta)=M-\log2<M.$$

This contradicts (7). Thus there is no joint holomorphic cap at any
point of $\Gamma_x$.

### Step 5. A meromorphic cap would contain a holomorphic cap

Suppose instead that a joint meromorphic continuation exists near a
point of $\Gamma_x$. By the local definition of a meromorphic
function, after shrinking to a product
$B(x_0,\rho)\times B(y_0,\eta)$ it can be written as $P/Q$, where
$P,Q$ are holomorphic and $Q$ is not identically zero.

Let $A=\partial\mathbb D\cap B(x_0,\rho)$, shrinking $\rho$ if
necessary to make $A$ a nonempty arc. The denominator cannot vanish
at every point of $A\times B(y_0,\eta)$. If it did, for each fixed
$y$ the holomorphic function $x\mapsto Q(x,y)$ would vanish on an
arc lying inside its complex domain; the one-variable identity
theorem would give $Q(\cdot,y)\equiv0$. This for every $y$ would
contradict $Q\not\equiv0$.

There is therefore a point $(x_1,y_1)$ on that face patch at which
$Q(x_1,y_1)\ne0$. On a smaller neighborhood of this point, $P/Q$
is holomorphic and agrees with $F$ on the interior overlap. It is a
joint holomorphic cap, already ruled out in Step 4. No joint
meromorphic cap exists. This completes the proof. $\square$

## Audit of the originally proposed limsup notation

The proposed choice

$$U=\left(\limsup_{n\to\infty}u_n\right)^*$$

also works, using the classical regularized-upper-limit theorem for a
locally uniformly upper-bounded sequence of subharmonic functions.
The bounds above give $U\leq M$, while $U\geq\limsup u_n$ holds
pointwise, including at $y_*$. Thus $U(y_*)=M$ without assuming that
$y_*$ avoids an exceptional polar set. A uniform improved Cauchy bound
on an open parameter disc survives regularization and forces $U<M$
there. The proof with (3) has the advantage that it does not need any
identification of the exceptional set, or even equality between the
tail-envelope limit and the regularized raw limsup.

It would be incorrect to declare the raw pointwise limsup itself
subharmonic, or to infer equality of raw and regularized limits at all
parameters. Neither assertion is used.

## Why this does not prove all complex slices have a natural boundary

Let $h\in\mathcal O(\mathbb D)$ have the unit circle as a natural
boundary, let $y_0\in\mathbb D$, and set

$$F(x,y)=(y-y_0)h(x).$$

Every slice with $y\ne y_0$ has that natural boundary, whereas
$F(\cdot,y_0)\equiv0$ is entire. Nevertheless no joint holomorphic or
meromorphic cap exists anywhere on $\Gamma_x$, by the theorem.
This example also illustrates exactly why the upper regularization can
strictly exceed the raw limsup at an exceptional parameter.

## Classical source ownership and read scope

The propagation lemma is a short application of classical Hartogs and
subharmonic-function theory, not an independently new analytic owner.
Its use in a particular arithmetic generating function can contribute
to that arithmetic theorem, but should not be counted as a separate
research contract.

1. Fritz Hartogs, *Zur Theorie der analytischen Funktionen mehrerer
   unabhängiger Veränderlichen, insbesondere über die Darstellung
   derselben durch Reihen, welche nach Potenzen einer Veränderlichen
   fortschreiten*, Mathematische Annalen 62 (1906), 1--88,
   DOI 10.1007/BF01448415.
   [Primary publisher record](https://link.springer.com/article/10.1007/BF01448415).
   The publisher confirms the author, title, March 1906 issue, volume
   and pages. The full original scan was not accessible in this check;
   no claim to have freshly verified an exact theorem number or the
   exact modern wording in all 88 pages is made. This is the classical
   Hartogs-series/radius-of-convergence origin, not a claim that the
   present joint-meromorphic corollary appears verbatim there.

2. Jaap Korevaar and Jan Wiegerinck, *Several Complex Variables*,
   author-hosted lecture notes, 2017 version.
   [Primary author PDF](https://staff.science.uva.nl/j.j.o.o.wiegerinck/edu/scv/scvboek.pdf).
   Actual relevant read scope: the argument around equations
   (4.8.4)--(4.8.5), applying regularized logarithmic coefficient
   limsups and Hartogs' lemma to a continuation problem; and
   Properties 8.4.3, printed p. 152, stating upper-envelope
   regularization and decreasing-limit closure for psh functions.
   These supply the exact modern analytic inputs used here. The
   material was read through the primary PDF's returned text; failed
   later fetches and inaccessible screenshot output are not treated
   as additional reading of the book.

No source search was used as evidence for the arithmetic input itself.
There was no relevant local PDF library or configured Zotero/Obsidian
tool available in this branch, and no PDF was downloaded.

## Corrections or missing assumptions

There is no missing hypothesis in the stated bidisc theorem. The
proof device (3) is a presentation refinement, not a strengthening of
the assumptions or weakening of the conclusion. The local meaning of
continuation and the requirement $y_*\in\mathbb D$ should be kept
explicit in a manuscript.

## Open risks and downstream boundary

There is no remaining analytic gap in this lemma under the stated
assumptions. For an arithmetic application, the author must separately
establish joint holomorphy on the entire bidisc and the natural
boundary of at least one interior slice. A dependent-parameter example
whose genuine pole hypersurfaces already enter the bidisc does not
satisfy the lemma's holomorphy hypothesis and cannot be inserted into
this proof. This review does not certify those separate arithmetic
claims, fixed complex slices, or any extension beyond the stated faces.
