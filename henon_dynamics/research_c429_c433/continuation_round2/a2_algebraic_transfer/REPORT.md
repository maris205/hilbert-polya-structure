# Round 2 A2: native-periodic graph complexity and algebraic transfer

2026-09-09 UTC. Frozen question and source subtraction before the full
proof write-up; hand feasibility reasoning and targeted source discovery
have already occurred. This is the same PC424-L candidate as A1, not an
independent paper. All first-pass artifacts remain read-only.

## Unchanged original claim

For every odd prime $p$, put $k=\overline{\mathbb F}_p$. For every
$c\in k$ and $h\in k[x]$, let $f=x^2+c$ and
$\Delta Q=Q\circ f-Q$. Define explicitly

$$K_c=\left\{h\in k[x]:\sum_{a\in O}h(a)=0
\text{ for every ordinary primitive }f\text{-orbit }O\right\},
\qquad B_c=\Delta k[x].$$

Each distinct point of an orbit is counted once, including when its
primitive length is divisible by $p$. The native clock is one application
of $T(x,y)=(f(x),y+h(x))$. The claim to settle is

$$h\in K_c\Longrightarrow
\exists E/k(x)\text{ finite},\ \sigma:E\hookrightarrow E,
\ \sigma|_k=\mathrm{id},\ \sigma(x)=f(x),\
\exists u\in E:\ \sigma(u)-u=h.$$

By the accepted R6 descent theorem this is exactly $K_c=B_c$.
Success requires the actual finite algebraic object, not an assumed
complexity bound or a function in a completion. A genuine counterexample
must satisfy all original orbit conditions while admitting no such field
extension. No such counterexample is currently established.

## Source subtraction and bounded Round 2 attack

Imported, not reproved or counted as Round 2 results:

- [R6 algebraic-transfer descent](../../../research_c424_c428/continuation_round6/positive_characteristic/PROOF_AND_GAPS.md),
  including wild extension degrees and purely inseparable transfers.
- [First-pass A2 supplement](../../lanes/a2_transfer_bridge/PROOF_SUPPLEMENT.md):
  connected finite étale obstruction, exact Artin–Schreier certificate,
  and the Bézout threshold $N>2^Dd_TD^4$ for a graph on an arbitrary
  finite forward-invariant set.
- [First-pass A1 report, Section C](../../lanes/a1_periodic_coboundary/REPORT.md):
  each finite-field transfer may already be chosen with coefficients in
  the base field $\mathbb F_q$. Compatible reduced-profinite transfers
  follow by finite inverse-limit compactness; no surjectivity of the
  transition maps is needed. An explicit twisted-cycle Hilbert–90
  construction would only repackage this accepted solvability input.
- [First-pass decision](../../FIRST_PASS_DECISION.md) and
  [E4 review](../../reviews/e4_covers/REVIEW.md): accepted auxiliary
  mathematics, original existence gap still open. The definition of
  $K_c$ above handles the optional notation clarification without
  altering the historical supplement.

This round's prospective non-formal bridge is narrower: exploit that
$T$ is a **permutation** of a transfer graph whose base consists only
of periodic points. For a curve equation of total degree $D$, the
nonvertical components form a finite directed containment graph under
$T$. A directed cycle would supply an algebraic transfer for an iterate
and hence, by R6, a polynomial one up to a constant. Otherwise Bézout
at terminal components may give a polynomial, rather than exponential,
upper bound for the number of graph points.

The target auxiliary bound is

$$N\le D+d_TD^3,\qquad d_T=\max(2,\deg h),$$

for a non-coboundary satisfying the original orbit condition. If proved,
it makes algebraic degree $o(N^{1/3})$ sufficient for actual polynomial
transfer. The original sums have not been shown to supply that growth
bound. Uniform boundedness is not assumed, and finite-degree-slice
compactness is not used to infer it.

## Status and actual new auxiliary claim

Original PC424-L: **NOT CURRENTLY JUSTIFIED / OPEN**. The following
auxiliary statement is **PROVABLE AS STATED** by the hand proof below.
It is current-team author work, not yet independently checked.

**Native-periodic complexity theorem.** Let $S\subset k$ be a finite
union of ordinary primitive $f$-orbits, and let $U:S\to k$ satisfy
$U(f(a))-U(a)=h(a)$ for all $a\in S$. Put
$\Gamma=\{(a,U(a)):a\in S\}$ and $N=|S|$. If a nonzero
$P\in k[X,Y]$ of total degree at most $D\ge1$ vanishes on $\Gamma$
and

$$N>D+d_TD^3,\tag{R2-A2.1}$$

then $h=\Delta Q+\beta$ with $Q\in k[x]$ and $\beta\in k$.
If $h\in K_c$, then $\beta=0$ and this is a genuine polynomial
transfer for the original one-step equation.

For $h=0$ use $d_T=2$. For nonzero constant $h$ also $d_T=2$.
The theorem itself does not assume that $h\in K_c$; that hypothesis
is used only to remove its final constant.

## Proof strategy and dependency map

1. Native periodicity makes $T|_\Gamma$ bijective.
2. Factor the graph-containing curve into its vertical and nonvertical
   components. At most one directed containment edge leaves each
   nonvertical component.
3. A directed cycle of nonvertical components is already covered by
   the accepted R6/first-pass periodic-curve argument and gives
   $h\in B_c+k$.
4. If there is no directed cycle, each component reaches a terminal
   component. Bijectivity preserves its graph-point count along this
   chain. Bézout bounds terminal counts and summing gives the cubic bound.

The only external numerical intersection input is the distinct-point
form of [Bézout, Milne, Algebraic Geometry, Theorem 6.37](https://www.jmilne.org/math/CourseNotes/AG.pdf),
whose author-hosted statement and displayed proof were read in the first
pass. The component argument and its cubic estimate are the present
deduction, not attributed to Milne or to the old R6 theorem.

## Proof

### 1. The permutation and curve components

Since $S$ is a finite union of periodic orbits, $f|_S$ is a permutation.
The transfer identity sends $(a,U(a))$ to $(f(a),U(f(a)))$, so
$T|_\Gamma$ is a permutation as well. For every integer $r\ge0$
and every subset $A\subseteq\Gamma$,

$$|T^{\circ r}(A)|=|A|.\tag{R2-A2.2}$$

Replace $P$ by the product of its distinct irreducible factors; this
does not change its zero set or increase its degree. Let
$C_1,\ldots,C_s$ be its nonvertical irreducible components, with
degrees $d_1,\ldots,d_s$. The remaining components are vertical
lines. Each vertical line contains at most one point of $\Gamma$.
There are at most $D$ such lines, while

$$s\le D,\qquad \sum_{i=1}^s d_i\le D.\tag{R2-A2.3}$$

Draw an edge $i\to j$ if $T(C_i)\subseteq C_j$. A nonvertical
curve cannot be contracted to a point or mapped into a vertical
line: its first coordinate is nonconstant and remains so after
composition with $f$. Its image is therefore dense in one
irreducible nonvertical curve. Consequently at most one edge leaves
each vertex.

### 2. Directed cycles supply the already-understood finite object

If the directed graph has a cycle, some nonvertical irreducible
curve $C$ has a dominant self-map $T^{\circ r}:C\to C$, for
some $r\ge1$. Its function field is finite over $k(x)$, and the
induced embedding satisfies

$$\tau(x)=f^{\circ r}(x),\qquad
\tau(y)-y=S_rh(x),\qquad
S_rh=\sum_{i=0}^{r-1}h\circ f^{\circ i}.$$

Apply the imported R6 descent theorem to the base degree $2^r$,
which is prime to $p$. It gives $y=Q(x)$ and
$\Delta_{f^{\circ r}}Q=S_rh$. As checked in the accepted first-pass
argument, commutation of the two polynomial difference operators gives

$$\Delta_{f^{\circ r}}(h-\Delta Q)=0.$$

Positive polynomial degree is multiplied by $2^r>1$ on composition,
so the invariant polynomial $h-\Delta Q$ is a constant. This proves
the conclusion in the directed-cycle case. No new R6 proof is claimed.

For the rest of the argument, assume $h\notin B_c+k$. The preceding
implication makes the finite directed graph acyclic. Every vertex $i$
then follows its unique outgoing edges to a terminal vertex, denoted
$t(i)$. This also covers vertices already terminal.

### 3. Terminal intersections have bounded size

Let $C_t$ be terminal, and put $M_t=|\Gamma\cap C_t|$.
Every point of $\Gamma\cap C_t$ belongs to
$C_t\cap T^{-1}(Z(P))$, since $T\Gamma=\Gamma\subseteq Z(P)$.

The polynomial $P\circ T$ is nonzero. Indeed, $T$ is surjective
on $k$-points: solve $x^2+c=a$ and then $y+h(x)=b$ for an
arbitrary target $(a,b)\in k^2$. Thus $T$ is dominant and its
pullback on the polynomial ring is injective. Moreover

$$\deg(P\circ T)\le d_TD.$$

There is no common irreducible component between $C_t$ and
$Z(P\circ T)$. If there were, $P\circ T$ would vanish on $C_t$;
the irreducible nonconstant image of $C_t$ would lie in one
component of $Z(P)$. It cannot be a vertical component, and a
nonvertical one would supply an outgoing edge from $t$, contrary
to terminality.

Bézout therefore gives the bound on distinct affine points

$$M_t\le d_t d_TD.\tag{R2-A2.4}$$

### 4. Propagate without loss and sum

The directed path from $i$ to $t(i)$ has some length $r_i\ge0$.
It sends $\Gamma\cap C_i$ into $\Gamma\cap C_{t(i)}$.
Equation (R2-A2.2), rather than a generic two-to-one fiber bound,
gives

$$|\Gamma\cap C_i|\le M_{t(i)}\le d_TD\,d_{t(i)}.$$

Every graph point lies on at least one component of $Z(P)$, and
the vertical components account for at most $D$ points. Overcounting
points shared by several components only increases the following
upper bound. Using (R2-A2.3),

$$\begin{aligned}
N
&\le D+\sum_{i=1}^s|\Gamma\cap C_i|\\
&\le D+d_TD\sum_{i=1}^s d_{t(i)}\\
&\le D+d_TD\,(sD)\\
&\le D+d_TD^3.
\end{aligned}$$

This contradicts (R2-A2.1), so $h\in B_c+k$. Finally $f(x)-x$
has a root $a\in k$. If $h\in K_c$ and $h=\Delta Q+\beta$,
the one-point ordinary orbit gives $0=h(a)=\beta$.
The native-periodic complexity theorem follows. $\square$

## Actual partial bridge, and the exact regularity still missing

For $h\in K_c$, transfers on any finite union $S$ of cycles exist
by the imported cycle-by-cycle construction. The new theorem proves:

> If for some growing finite unions of ordinary cycles $S_j$ with
> $N_j=|S_j|\to\infty$, some transfer graphs admit nonzero equations
> of total degrees $D_j=o(N_j^{1/3})$, then $h\in B_c$.

The bound follows since $d_T$ is fixed and
$(D_j+d_TD_j^3)/N_j\to0$. One sufficiently large graph then
produces $Q$; the equation $Y-Q(X)=0$ supplies an actual fixed
total-degree bound thereafter. This criterion permits unbounded
$D_j$ and is strictly weaker as a regularity assumption than asking
for a uniformly bounded degree in advance.

Conversely, if a hypothetical $h\in K_c\setminus B_c$ exists,
then for **every** finite union of cycles, every transfer choice and
every nonzero graph equation of total degree $D\ge1$,

$$N\le D+d_TD^3\le(d_T+1)D^3,
\qquad D\ge\left(\frac{N}{d_T+1}\right)^{1/3}.\tag{R2-A2.5}$$

This is a genuine lower bound on all possible algebraic interpolants
of a hypothetical defect's periodic transfer graph, not merely on a
poorly chosen sequence of interpolants. It does not construct such a
defect. General interpolation does not contradict (R2-A2.5): the
elementary dimension count only guarantees a nonzero bivariate
equation of degree on the order of $N^{1/2}$ for arbitrary $N$
points, which is larger than the cube-root threshold. Neither the
ordinary orbit equations nor the accepted finite-field coefficient
descent currently improves that estimate to $o(N^{1/3})$.

Thus the unresolved existence step is now a concrete **sub-cube-root
algebraic-complexity bound on some periodic transfer graphs**, or
another theorem genuinely constructing a finite algebraic transfer.
No such bound was obtained. The all-parameter/all-degree original
question remains unchanged and open.

## Failed routes and source limits

An arithmetic-coherence construction using Frobenius-twisted cycle
equations was considered, then subtracted after reading A1 Section C
and receiving the coordinator's source pointer. It gives no finite
algebraic complexity beyond the accepted finite-field solvability.
No new theorem or major proof is claimed for it. The inverse limit
of reduced residue algebras is not a finite extension of $k(x)$.

Targeted primary-source discovery was made for positive-characteristic
periodic multiplicities, algebraic cohomological equations and
Livšic-type results. It did not yield a verified theorem converting
these ordinary quadratic orbit sums into finite algebraicity. Search
results about real/ultrametric regularity and specialized zeta functions
were not used as mathematical inputs; no unseen body theorem is
credited, and no claim of exhaustive literature coverage is made.
The only external theorem used in the new proof is the already-read
Bézout bound cited above. Its classical ownership, R6 descent and the
first-pass periodic-curve argument are fully subtracted.

## Handoff, skills and execution receipt

The exact new hypothesis/output interface is (R2-A2.1), or equivalently
the sufficient growth condition above. Consumers A1/root must supply
the actual sub-cube-root graph equations; compatibility does not follow
from finite-dimensional degree slices, field descent, a coherent
profinite solution, genus-zero interpolating graphs, or a fixed degree
in $Y$ alone. No claim of an independent paper or admission follows.

Proof-writer kept the original existence claim separate from the proved
auxiliary estimate. The batch workflow and continuous-run contract
kept accepted first-pass results read-only and required an actual
regularity gain rather than repeating those results. This report
records a stricter quantitative obstruction and weaker sufficient
regularity condition, not an asserted original-question closure.

New writes: only this `REPORT.md` in the assigned Round 2 directory.
Mathematical programs, old reruns, manuscripts, PDFs, evaluations, Git
actions, external model/API calls and nested workers: **0**. No shared
or first-pass artifact was modified. The estimate is an author hand
proof pending a nonauthor check; no human peer review, global novelty,
or target Euler-factor/root-number/Hilbert–Pólya claim is made.
