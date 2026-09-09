# A2 proof supplement: finite-cover obstruction and bounded-graph bridge

2026-09-09 UTC. Current-team author proof, not independent review.
Mathematical program executions: **0**. These are auxiliary statements
for the unchanged [PC424-L question](REPORT.md), not independent papers.

## Claim, status and assumptions

Throughout, $p$ is odd, $k=\overline{\mathbb F}_p$, $c\in k$,
$f(x)=x^2+c$ and $h\in k[x]$. Write

$$\Delta Q=Q\circ f-Q,\qquad
S_rh=\sum_{i=0}^{r-1}h\circ f^{\circ i},\qquad
T(x,y)=(f(x),y+h(x)).$$

The following three auxiliary conclusions are **PROVABLE AS STATED**:

1. A connected finite étale cover of $\mathbb A^1_k$ carrying a
   self-map over $f$ has degree one.
2. A global Artin–Schreier compatibility identity
   $\Delta b=h^p-h$ exists with $b\in k(x)$ if and only if
   $h=\Delta Q+\beta$ with $Q\in k[x]$, $\beta\in\mathbb F_p$.
   Vanishing at any fixed point of $f$ removes $\beta$.
3. Let $d_T=\max(2,\deg h)$, with $d_T=2$ if $h=0$.
   Suppose $S\subset k$ is finite and $f(S)\subseteq S$, and there is
   $U:S\to k$ satisfying $U(f(a))-U(a)=h(a)$ for every $a\in S$.
   If a nonzero $P\in k[X,Y]$ of total degree at most $D\ge1$
   vanishes on its graph and

   $$|S|>2^D d_TD^4,\tag{A2.1}$$

   then $h=\Delta Q+\beta$ for some $Q\in k[x]$, $\beta\in k$.
   Vanishing of all ordinary primitive-orbit sums again removes
   $\beta$ and gives a genuine finite algebraic transfer, namely $Q$.

The original assertion that ordinary-orbit vanishing **supplies** one
of these certificates remains **NOT CURRENTLY JUSTIFIED**. Neither
the finite étale obstruction nor (A2.1) asserts that the required cover
or bounded-degree graph exists.

## Strategy and dependency map

The finite-cover theorem uses compactification, the curve/function-field
correspondence and Riemann–Hurwitz with the different. The
Artin–Schreier statement uses an explicit $p$-reduced normal form;
this is a quotient by $b^p-b$, not A1's quotient by $\Delta$.
The bounded-graph statement uses Bézout to find a periodic component,
then imports the already proved R6 algebraic-transfer descent for
$f^{\circ r}$, of degree $2^r$ prime to $p$.

External classical inputs, with primary access, are the
[Stacks curve/function-field correspondence](https://stacks.math.columbia.edu/tag/0BXX),
[Riemann–Hurwitz and the different bound](https://stacks.math.columbia.edu/tag/0C1B),
the [Artin–Schreier exact sequence](https://stacks.math.columbia.edu/tag/0A3J),
and [Milne, Algebraic Geometry, Theorem 6.37](https://www.jmilne.org/math/CourseNotes/AG.pdf).
The present deductions are author arguments, not attributed to those
sources. R6 is imported from its
[complete proof](../../../research_c424_c428/continuation_round6/positive_characteristic/PROOF_AND_GAPS.md),
Sections 1–7, including its rational-pole lemma in Section 4.

## 1. No nontrivial connected finite étale dynamical cover

Let $\pi:Y\to\mathbb A^1_k$ be finite étale, connected and nonempty,
of degree $m$, and suppose $g:Y\to Y$ satisfies

$$\pi\circ g=f\circ\pi.\tag{A2.2}$$

Because $Y$ is a connected smooth curve, it is integral. Let $C$ be
its smooth projective model. The finite map $\pi$ extends to
$\bar\pi:C\to\mathbb P^1_k$, and $g$ extends to a nonconstant
morphism $\bar g:C\to C$. These extensions follow from the
curve/function-field correspondence and extension of rational maps
from nonsingular curves to proper varieties. Their equality (A2.2)
extends because it holds on a dense open subset.

Put $D_\infty=\bar\pi^{-1}(\infty)$ as a set and
$b=|D_\infty|$. The set is nonempty and finite. Furthermore
$Y=C\setminus D_\infty$: the normalization of $\mathbb A^1$ in
$k(Y)$ is $Y$, since $Y$ is normal and finite over $\mathbb A^1$.
Because $f^{-1}(\infty)=\{\infty\}$, equality (A2.2) gives

$$\bar g^{-1}(D_\infty)=D_\infty.\tag{A2.3}$$

Degrees in (A2.2) give $m\deg\bar g=2m$, hence
$\deg\bar g=2$. Its inseparable degree is a power of $p$ dividing
$2$; because $p$ is odd, $\bar g$ is separable.

Let $\gamma$ be the genus of $C$ and $R_{\bar g}$ the different
divisor of $\bar g$. Riemann–Hurwitz gives

$$\deg R_{\bar g}=2-2\gamma.\tag{A2.4}$$

There are exactly $m$ distinct points in $\pi^{-1}(0)$ because
$\pi$ is étale and $k$ is algebraically closed. If $a$ is one of
them, both $a$ and $g(a)$ belong to $Y$. Multiplicativity of local
ramification indices in (A2.2), together with étaleness of $\pi$,
therefore gives

$$e_{\bar g}(a)=e_f(0)=2.$$

Each of these $m$ points contributes at least one to
$R_{\bar g}$. They lie outside $D_\infty$.

For each $z\in D_\infty$, the sum of ramification indices over
$\bar g^{-1}(z)$ is $2$, since all residue fields equal $k$.
Summing over $z$ and using (A2.3) yields

$$\sum_{a\in D_\infty}e_{\bar g}(a)=2b,
\qquad
\sum_{a\in D_\infty}(e_{\bar g}(a)-1)=b.$$

The different exponent at any point is at least its ramification
index minus one. Thus the two disjoint contributions give

$$2-2\gamma=\deg R_{\bar g}\ge m+b\ge2.$$

It follows that $\gamma=0$ and $m=b=1$. The degree-one finite map
$\pi$ to the normal curve $\mathbb A^1$ is an isomorphism. This
proves statement 1 without assuming that the cover is Galois or
Artin–Schreier, and without assuming any orbit-sum condition. $\square$

The conclusion is deliberately about a **connected** cover with an
actual self-map. A disconnected cover whose components are permuted
does not provide a $\sigma$-stable field component automatically.

## 2. Artin–Schreier compatibility is already the desired regularity

Write $\wp(b)=b^p-b$ and consider the additive quotient

$$\mathcal H=k[x]/\wp(k[x]).$$

It is an $\mathbb F_p$-vector space; it is not being treated as a
$k$-vector-space quotient. The Artin–Schreier sequence and the
vanishing of structure-sheaf cohomology on an affine scheme identify
it with $H^1_{\mathrm{et}}(\mathbb A^1_k,\mathbb F_p)$.

### 2.1 Explicit reduced representatives and degree expansion

Each class in $\mathcal H$ has a unique representative

$$v(x)=\sum_{\substack{j\ge1\\p\nmid j}}a_jx^j,\tag{A2.5}$$

with finite support. For existence, remove the constant term using
surjectivity of $z\mapsto z^p-z$ on $k$. A term $a x^{pj}$ can
be replaced by $a^{1/p}x^j$ modulo $\wp(k[x])$. Eliminate such
terms from highest degree downwards; degrees strictly decrease.
For uniqueness, a nonconstant $q$ has
$\deg(q^p-q)=p\deg q$, whereas any nonzero polynomial of the form
(A2.5) has positive degree prime to $p$. Their difference cannot be
zero. A constant $q$ contributes only a constant, which cannot
equal a nonzero (A2.5).

Composition by $f$ commutes with $\wp$, so it induces $f^*$ on
$\mathcal H$. If a nonzero reduced $v$ has degree $n$, then
$v\circ f$ has degree $2n$, prime to $p$. Reducing its lower terms
by the preceding procedure does not alter its leading term.
Consequently the reduced representative of $(f^*)^r[v]$ has degree
$2^rn$ for every $r\ge0$. In particular

$$\ker((f^*)^r-1)=0\quad(r\ge1),\tag{A2.6}$$

and no nonzero Artin–Schreier class has a finite orbit under $f^*$.

### 2.2 Exact certificate and the constant-component obstruction

Suppose $b\in k(x)$ satisfies $\Delta b=\wp(h)$. Its difference
is polynomial, so the imported R6 rational-pole lemma gives
$b\in k[x]$. In $\mathcal H$ the identity reads
$f^*[b]=[b]$. By (A2.6), $[b]=0$, so $b=\wp(Q)$ for some
$Q\in k[x]$. Commutation of $\wp$ and $\Delta$ now gives

$$\wp(h-\Delta Q)=0.$$

The roots of $Z^p-Z$ in the field $k(x)$ are precisely
$\mathbb F_p$. Hence $h=\Delta Q+\beta$ with
$\beta\in\mathbb F_p$. Conversely this expression yields the
certificate $b=\wp(Q)$. This proves statement 2.

Since $f(x)-x$ has a root $a\in k$, the ordinary fixed-point
condition $h(a)=0$ gives $\beta=0$. Thus, under the original
orbit hypothesis, producing $\Delta b=h^p-h$ is **equivalent**
to producing the polynomial transfer. It is not an easier theorem
already implied by Artin–Schreier theory.

Geometrically, the identity is exactly the condition that

$$C_b:\ y^p-y=b(x),\qquad
(x,y)\longmapsto(f(x),y+h(x))\tag{A2.7}$$

defines a lift. The calculation is
$(y+h)^p-(y+h)-b(f(x))=\wp(h)-\Delta b$ on $C_b$.
The conclusion $b=\wp(Q)$ means that $C_b$ is the disjoint union
of the $p$ graphs $y=Q(x)+j$, $j\in\mathbb F_p$. The lift sends
component $j$ to component $j+\beta$.

The example $h=1$, $b=0$ gives a valid disconnected finite étale
lift that cycles through all $p$ components, but gives **no** stable
field component for the one-step embedding and no algebraic
solution of $\sigma(u)-u=1$, by R6. It violates the fixed-point
orbit condition, so it is not a counterexample to PC424-L. It is
an exact falsifier of the shortcut “a finite étale algebra with a
lift automatically supplies the required stable extension field.”

### 2.3 What geometric point splitting forgets

For any finite reduced subset $Z\subset\mathbb A^1(k)$, its
coordinate ring is a finite product of copies of $k$. The map
$\wp$ is surjective in each factor, hence
$H^1_{\mathrm{et}}(Z,\mathbb F_p)=0$. All restriction maps

$$\mathcal H\longrightarrow
\prod_{O\text{ ordinary primitive orbit}}
H^1_{\mathrm{et}}(O,\mathbb F_p)$$

are therefore zero. In particular, the nonzero class $[x]$ from
(A2.5) restricts to a split cover over every such $O$.
This is a genuine failure of detecting an underlying cover by
geometric fiber splitting, not a counterexample to the extra
dynamical compatibility encoded by the original orbit sums.

## 3. Bounded algebraic complexity creates a periodic curve

Assume the hypotheses of statement 3. Let

$$\Gamma=\{(a,U(a)):a\in S\},\qquad N=|S|.$$

Then $T(\Gamma)\subseteq\Gamma$. Every fiber of $T$ contains at
most two geometric points: $f(x)$ fixes at most two choices of $x$,
and for each choice the second coordinate fixes $y$ uniquely.
In particular, for a finite subset $A\subseteq\mathbb A^2(k)$,
$|T(A)|\ge |A|/2$.

Factor the given nonzero $P$ over $k$, discarding multiplicities.
Its irreducible zero-set components $C_1,\ldots,C_s$ satisfy
$1\le s\le D$, and each has degree at most $D$. Some component
$C_{i_0}$ contains at least $N/D$ points of $\Gamma$.

We first establish a propagation fact. If a component $C_i$ contains
$M>d_TD^3$ points of $\Gamma$, each of their images belongs to at
least one $C_j$. Pigeonhole counting gives a $j$ such that more
than $d_TD^2$ **input** points lie in

$$C_i\cap T^{-1}(C_j).$$

If $P_j$ is an irreducible equation for $C_j$, then
$P_j\circ T$ is nonzero and has total degree at most $d_TD$.
It is nonzero because $T$ is dominant. If it did not vanish
identically on $C_i$, Bézout would bound the number of their
distinct affine intersection points by
$D(d_TD)=d_TD^2$. Thus $T(C_i)\subseteq C_j$.
The image is dense in $C_j$: $T$ has finite fibers, so it does
not contract $C_i$ to a point. In addition,

$$|\Gamma\cap C_j|\ge |T(\Gamma\cap C_i)|\ge M/2.\tag{A2.8}$$

Beginning with $C_{i_0}$, apply this fact $D$ times. At the
$j$th stage, for $0\le j\le D$, the selected component contains
at least $N/(D2^j)$ graph points. By (A2.1), even this lower bound
at $j=D$ is greater than $d_TD^3$. Thus every required propagation
is justified. Among the resulting $D+1$ components at least two
coincide. We have obtained an irreducible component $C$ and an
integer $r$ with $1\le r\le D$ for which

$$T^{\circ r}:C\longrightarrow C$$

is dominant. The component is not vertical, since it contains more
than one graph point and a vertical line meets a graph in at most
one point.

Let $E=k(C)$ and denote the restrictions of the two coordinates by
$x,y$. Nonverticality makes $x$ transcendental over $k$, and $E$
is a finite extension of $k(x)$. The dominant self-map gives an
injective $k$-endomorphism $\tau$ of $E$ with

$$\tau(x)=f^{\circ r}(x),\qquad
\tau(y)-y=S_rh(x).$$

The R6 descent theorem applies: the base degree $2^r$ is prime to
$p$, the right side is polynomial, and the field extension is
finite. It yields $y=Q(x)$ for a polynomial $Q\in k[x]$, and hence

$$Q\circ f^{\circ r}-Q=S_rh.\tag{A2.9}$$

Apply $\Delta$ to (A2.9). The difference operators for $f$ and
$f^{\circ r}$ commute, while
$\Delta S_rh=h\circ f^{\circ r}-h$. Therefore

$$\bigl(h-\Delta Q\bigr)\circ f^{\circ r}
=h-\Delta Q.$$

A nonconstant polynomial cannot be invariant under composition by
$f^{\circ r}$: its positive degree would be multiplied by $2^r>1$.
Thus $h-\Delta Q=\beta\in k$. If the original all-orbit condition
holds, evaluate at a fixed point of $f$ to get $\beta=0$.
This proves statement 3. $\square$

## 4. Exact remaining gap and usable bounded certificate

Choose any finite field $\mathbb F_q$ containing the coefficients
of $f$ and $h$. The imported finite-functional-graph argument gives,
under ordinary-orbit vanishing, a transfer $U_n$ on every
$\mathbb F_{q^n}$. The following is now a sufficient and necessary
completion condition under that orbit hypothesis:

> There is an integer $D\ge1$ such that, for arbitrarily large
> $n$, some transfer graph $\Gamma_n$ is annihilated by a nonzero
> polynomial $P_n(X,Y)$ of total degree at most $D$.

Sufficiency follows once $q^n>2^Dd_TD^4$ by Section 3. Necessity
follows from a polynomial transfer $Q$: take every $U_n$ to be the
restriction of $Q$ and every $P_n=Y-Q(X)$, increasing $D$ if needed.
The $P_n$ need not be equal, and no compatibility of the chosen
finite graph transfers across different fields is assumed.

This is not an execution-based extrapolation: it is a proved
finite-threshold implication. However, ordinary sums have **not**
been shown to provide such a $D$. Unbounded interpolation gives
$\deg_Y P_n=1$ automatically and says nothing about this total-degree
bound. The certificate isolates the precise algebraic-complexity
input still required; it does not furnish that input.

Equivalently, a hypothetical $h\in K_c\setminus\Delta k[x]$
would force every such finite transfer graph and every nonzero
annihilating equation of total degree $D$ to satisfy

$$q^n\le 2^Dd_TD^4.$$

This is a necessary complexity-growth condition for a hypothetical
defect, not an example of one and not a contradiction to interpolation.

## Corrections, boundaries and open risks

- The first genus-zero/one case sketch was replaced by the single
  ramification inequality $2-2\gamma\ge m+b$, so no claim about
  classifying all genus-zero self-maps is needed.
- Artin–Schreier compatibility admits a constant component permutation;
  it is not identified with a one-step stable extension field without
  killing that constant. The fixed-point orbit does kill it here.
- $D$ bounds total degree, not only extension degree or the degree in
  $Y$. No hidden uniform degree bound is asserted.
- The ordinary-cycle hypothesis is retained with all periods, including
  those divisible by $p$. The auxiliary use of an iterate is only a
  proof device, followed by descent back to the one-step equation.
- These arguments have not yet received a nonauthor internal check.
  No global novelty, complete PC424-L proof, original counterexample,
  or independent-paper admission is claimed.
