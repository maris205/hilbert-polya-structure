# Proof Package: finite-real Boole cycles across the parabolic transition

## Claim

For every pair of real parameters $a,b>0$, let
$$
T_{a,b}(x)=ax-\frac b x,\qquad
X_{a,b}=\mathbb R\setminus\bigcup_{j\ge0}T_{a,b}^{-j}\{0\}.
$$
The inverse images in this definition are computed using the rational map
on the Riemann sphere; only finite real points are removed. The restriction
$T:X_{a,b}\to X_{a,b}$ is the physical map. Time means one original
iteration. Infinity is not a physical state or a physical primitive orbit.

The following single source-system contract holds.

1. The subcritical map has an invariant Cauchy probability, the critical map
   preserves infinite Lebesgue measure, and the supercritical map has a
   compact two-symbol Cantor survivor with exact Lebesgue escape rate.
2. Every finite real periodic point is simple and has positive multiplier
   greater than one. All iterates and all primitive counts are determined.
3. The finite-real stability sums, their primitive product and their analytic
   continuation are explicit for all parameters.
4. The complete zero/pole cancellation rule, including the discrete
   subcritical parameters at which the stability germ becomes entire, is
   determined.
5. The critical stability germ is not meromorphic across its positive unit
   boundary point. Both the subcritical germ and the correctly
   fixed-orbit-reduced supercritical germ tend to it locally uniformly on
   the open unit disk.

None of these assertions identifies the finite-real stability germ with a
specified natural trace-class Perron operator. An abstract diagonal
realization at some parameters is not such an identification.

## Status

PROVABLE AS STATED for the explicit contract above. This is current-model
author material for admission review, not an independently accepted paper,
publication-priority claim, formal Route-A evaluation or release package.

## Assumptions

- The parameters are real and strictly positive. The excluded faces $a=0$
  and $b=0$ change rational degree and are not continuity claims.
- Fixed points are distinct finite geometric points; local multiplicity on
  the sphere is a separate proof ledger.
- Stability uses the positive derivative in the original real coordinate,
  and repetition uses its actual derivative product.
- Analytic germs are normalized by $D_a(0)=1$, without time rescaling.
- The ordinary complex residue theorem, Cauchy's mean-value formula,
  Weierstrass convergence for absolutely summable products, and elementary
  compactness facts are the only analytic background used below.

## Notation

Write $q=2a-1$, $N_n=\#\operatorname{Fix}_{X_{a,b}}T^n$ and
$$
\tau_n(a)=\sum_{x\in\operatorname{Fix}_{X_{a,b}}T^n}
\frac1{(T^n)'(x)-1},\qquad
D_a(u)=\exp\left(-\sum_{n\ge1}\frac{\tau_n(a)}n u^n\right).
$$
The formula for $D_a$ initially means a germ at zero. A primitive orbit
$\gamma$ has least period $p_\gamma$ and multiplier
$\Lambda_\gamma=(T^{p_\gamma})'(x)$ for any point $x$ on it. Lebesgue measure
is denoted by $m$. The dilogarithm on $|u|<1$ is defined here by its series
$\operatorname{Li}_2(u)=\sum_{n\ge1}u^n/n^2$.

## Proof Strategy

Use the half-plane/Blaschke description only to locate and certify all
periodic points. Compute weighted sums independently by residues on the
sphere, retaining the non-simple index at infinity. Then pass from the
exact all-iterate sums to convergent products, exact divisors and dominated
critical limits. This avoids inferring an operator from a formal product.

## Dependency Map

1. Steps 1--3 establish the physical domain and classical phase structure.
2. Steps 2 and 4 establish all fixed points and their multipliers.
3. Step 5 proves the residue identity including the critical index.
4. Step 6 uses Steps 4--5 to compute the stability sums.
5. Steps 7--8 use those sums to establish the primitive product and full
   zero/pole resonance rule.
6. Steps 9--10 prove the singular boundary and the locally uniform limits.
7. Step 11 separates these results from the old circle operator and target
   arithmetic claims.

## Proof

### Step 1. Domain, scale and the exact inverse Jacobian

The deleted set is countable: a rational map of degree two has at most
$2^j$ inverse images of a specified point at depth $j$. Every finite
periodic point avoids zero, since zero maps to infinity and infinity is
fixed. Such a periodic point therefore belongs to $X_{a,b}$.

For $S_b(y)=\sqrt b\,y$, direct substitution gives
$T_{a,b}S_b=S_bT_{a,1}$. This is a proof device retaining the original
parameter family and clock; $b$ is not an independent dynamical subtype.
The real derivative is
$$
T'(x)=a+\frac b{x^2}>0\quad(x\ne0).
$$
Each half-line maps increasingly onto the real line, with inverse branches
$$
h_\pm(y)=\frac{y\pm\sqrt{y^2+4ab}}{2a},\qquad
h_\pm'(y)=\frac1{2a}\left(1\pm\frac y{\sqrt{y^2+4ab}}\right)>0.
$$
Consequently $h_+'+h_-'=1/a$ and, by change of variables for any measurable
set $A$,
$$
m(T^{-1}A)=\frac1a m(A).                                      \tag{1}
$$
The formula allows an infinite value on both sides and is unaffected by
the countable deleted set. At $a=1$ it proves invariance of infinite
Lebesgue measure. We do not infer ergodicity from this identity.

### Step 2. Subcritical Cauchy law, Blaschke conjugacy and repulsion

Suppose $0<a<1$ and put $c=\sqrt{b/(1-a)}$. The Cayley map
$C(z)=(z-ic)/(z+ic)$ sends the upper half-plane to the unit disk and sends
infinity to $1$. A substitution, including at removable coordinate
singularities, gives
$$
C\circ T\circ C^{-1}(w)=B_q(w)
=w\,\frac{w+q}{1+qw},\qquad -1<q<1.                           \tag{2}
$$
For $|w|<1$, the second factor has modulus strictly less than one.
Indeed,
$$
|1+qw|^2-|w+q|^2=(1-q^2)(1-|w|^2)>0.
$$
Thus $|B_q(w)|<|w|$ for nonzero disk points. No such point can be periodic.
The reflection identity
$B_q(1/\bar w)=1/\overline{B_q(w)}$ gives the corresponding conclusion
outside the closed disk. Its two off-circle periodic points are exactly
$0$ and infinity, both fixed with local multiplier $q$; in the original
coordinate they are $ic$ and $-ic$.

For $w=e^{i\theta}$, write $B_q(w)=e^{i\psi(\theta)}$ using an increasing
lift. Logarithmic differentiation gives
$$
\psi'(\theta)
=1+\frac{1-q^2}{|e^{i\theta}+q|^2}
\ge 1+\frac{1-|q|}{1+|q|}>1.                                 \tag{3}
$$
Every circle periodic point is therefore simple and repelling. At a
finite real periodic point, differentiation of the conjugacy over the
whole period cancels its coordinate derivatives, so its real multiplier
is exactly the positive angular multiplier. The physical exclusion of
infinity does not change this calculation for finite points.

For completeness the invariant probability is proved rather than inferred
from expansion. The mean of $B_q(w)^k$ on the circle is zero for every
positive integer $k$, by Cauchy's mean-value formula and $B_q(0)=0$.
For negative $k$ the same mean is the complex conjugate of a positive
one. Approximation of continuous circle functions by trigonometric
polynomials proves that $B_q$ preserves normalized angular Lebesgue
measure. Pulling it back under $C$ gives
$$
d\mu_{a,b}(x)=\frac{c}{\pi(x^2+c^2)}\,dx.                      \tag{4}
$$
The countable removed set has measure zero. No mixing theorem or
uniqueness claim is needed for the present contract.

### Step 3. Supercritical survivor and exact escape

Suppose $a>1$, set $r=\sqrt{b/(a-1)}$, and let $I=[-r,r]$.
Its endpoints are fixed and satisfy $T'(\pm r)=2a-1=q>1$.
The inverse images are the disjoint closed intervals
$$
h_-(I)=[-r,-(a-1)r/a],\qquad
h_+(I)=[(a-1)r/a,r].                                        \tag{5}
$$
On them each inverse has derivative $1/T'(h_\pm(y))<1/a$.
For a word $\epsilon_1\cdots\epsilon_n$ of signs, its cylinder
$h_{\epsilon_1}\circ\cdots\circ h_{\epsilon_n}(I)$ therefore has diameter
at most $2r\,a^{-n}$. The $2^n$ cylinders are pairwise disjoint:
first-level images are disjoint, and injective compositions preserve
disjointness after the first place where two words differ.

For every infinite sign sequence the nested cylinders have a single
point. Their coding map is continuous by the diameter bound, injective
by disjointness, and surjective onto
$$
K=\bigcap_{n\ge0}T^{-n}(I).
$$
It is a homeomorphism from the compact one-sided binary shift space to
$K$, and applying $T$ removes the first sign. No point of $K$ or one of
its iterates is zero, by the first-level gap. Thus $K\subset X_{a,b}$.
This proves a Cantor full-shift survivor, including its endpoints.

If $x>r$, then
$$
T(x)-x=(a-1)x-\frac b x>0.
$$
An increasing forward orbit starting there cannot have a finite limit:
continuity would make that limit a fixed point greater than $r$, whereas
the only positive fixed point is $r$. It tends to positive infinity.
Oddness proves negative escape for $x<-r$. Every point of $X_{a,b}\setminus K$
eventually leaves $I$ and hence escapes. In particular, all finite
periodic points lie in $K$.

Iterating (1), and using $T^{-1}I\subset I$, proves the exact survival law
$$
m(T^{-n}I)=2r\,a^{-n},\quad m(K)=0,\quad
-\lim_{n\to\infty}\frac1n
\log\frac{m(T^{-n}I)}{m(I)}=\log a.                          \tag{6}
$$
This is an initial-Lebesgue survival statement, not a probability
invariant measure on the repeller.

### Step 4. Every iterate, fixed multiplicities and primitive counts

For $z=x+iy$ off the real line,
$$
\Im T(z)=y\left(a+\frac b{|z|^2}\right).                     \tag{7}
$$
If $a\ge1$ its absolute imaginary part strictly increases at each finite
step. It never reaches zero or infinity in finitely many steps, since the
only finite pole is real. It cannot be periodic. In addition every finite
real periodic multiplier is greater than one, because each derivative is
greater than one when $a\ge1$. This proves simple positive repulsion also
in the critical and supercritical regimes.

The degree of $T^n$ on the sphere is $2^n$. One can see multiplication of
degrees by composing its relatively prime homogeneous degree-two
coordinates; a common zero of the composed coordinates would map to a
common zero of the original pair, which does not exist. If $[U:V]$ are
homogeneous degree-$2^n$ coordinates for $T^n$, its fixed equation
$UZ-VX=0$ is a nonzero homogeneous polynomial of degree $2^n+1$.
It is nonzero because a degree greater than one map is not the identity.
The fundamental theorem of algebra on the projective line therefore
counts exactly $2^n+1$ fixed points with local multiplicity.

At infinity use $w=1/z$:
$$
g_a(w)=\frac1{T(1/w)}=\frac{w}{a-bw^2}.                       \tag{8}
$$
For $a\ne1$, its $n$th iterate has multiplier $a^{-n}\ne1$;
infinity has fixed multiplicity one.
For $a=1$, write
$g_1^n(w)=w+A_nw^3+B_nw^5+O(w^7)$.
Composition with $g_1(w)=w+bw^3+b^2w^5+O(w^7)$ yields
$$
A_{n+1}=A_n+b,\qquad
B_{n+1}=B_n+3bA_n+b^2.
$$
Starting from $A_1=b$, $B_1=b^2$, induction gives
$$
g_1^n(w)=w+nbw^3+\frac{n(3n-1)}2b^2w^5+O(w^7).              \tag{9}
$$
Because $nb\ne0$, infinity has fixed multiplicity three, for every $n$.

If $a<1$, Step 2 supplies exactly two nonreal fixed points, each of
multiplier $q^n\ne1$, and all other fixed points are real. If $a\ge1$,
(7) excludes all nonreal fixed points. Subtracting these contributions
and the correct infinity multiplicity gives
$$
N_n=
\begin{cases}
2^n-2,&0<a\le1,\\
2^n,&a>1.
\end{cases}                                                 \tag{10}
$$
Every physical point has already been proved simple. A point of least
period $d$ is fixed by $T^n$ exactly when $d$ divides $n$, and an orbit
of least period $d$ has $d$ points. Möbius inversion therefore gives
$$
P_n=\frac1n\sum_{d\mid n}\mu(n/d)N_d.                         \tag{11}
$$
There is no overcount from poles or preperiodic points. The unweighted
physical zeta, initially for $|u|<1/2$, is
$$
Z_{\mathrm{AM},a}(u)=
\begin{cases}
(1-u)^2/(1-2u),&0<a\le1,\\
1/(1-2u),&a>1.
\end{cases}                                                 \tag{12}
$$

### Step 5. Holomorphic index identity including infinity

For a rational map $F$ fixing infinity, use the rational one-form
$\eta=dz/(z-F(z))$. A finite pole of $F$ is a zero, not a pole, of
this form. Its finite poles are therefore exactly the fixed points of
$F$. At a simple fixed point its residue is $1/(1-F'(z))$.

Write $g(w)=1/F(1/w)$. Direct coordinate transformation, not a
simple-fixed-point assumption at infinity, gives
$$
\eta=\left(\frac1{w-g(w)}-\frac1w\right)dw.
$$
Thus if $I_\infty(F)$ denotes the coefficient of $w^{-1}$ in
$1/(w-g(w))$, the residue of $\eta$ at infinity is $I_\infty(F)-1$.
The sum of residues of a rational one-form on the sphere is zero, so
$$
\sum_{\substack{F(z)=z\\z\ \mathrm{finite}}}
\operatorname{Res}_z\frac{d\zeta}{\zeta-F(\zeta)}
+I_\infty(F)=1.                                             \tag{13}
$$
For $F=T^n$ all finite points are simple by Step 4 and the subcritical
off-real calculation. When $a\ne1$,
$$
I_\infty(T^n)=\frac1{1-a^{-n}}.                              \tag{14}
$$
For $a=1$, (9) gives
$$
\frac1{w-g_1^n(w)}
=-\frac1{nb\,w^3}+\frac{3n-1}{2n}\frac1w+O(w),
\qquad I_\infty(T^n)=\frac{3n-1}{2n}.                        \tag{15}
$$
This index is not the fixed multiplicity three, and neither quantity is
the multiplier one. Keeping the three distinct is necessary.

### Step 6. All finite-real weighted sums

Changing signs in the finite terms of (13) gives
$$
\sum_{\substack{T^n(z)=z\\z\ \mathrm{finite}}}
\frac1{(T^n)'(z)-1}=I_\infty(T^n)-1.
$$
For $a\ne1$ its right side is $1/(a^n-1)$.
If $a<1$, the two nonreal fixed points each contribute
$1/(q^n-1)$ and must be subtracted. If $a>1$ there are none.
At $a=1$ use (15). The result is
$$
\tau_n(a)=
\begin{cases}
\displaystyle\frac2{1-q^n}-\frac1{1-a^n},&0<a<1,\\[4pt]
\displaystyle\frac{n-1}{2n},&a=1,\\[4pt]
\displaystyle\frac1{a^n-1},&a>1.
\end{cases}                                                 \tag{16}
$$
All these expressions are nonnegative because their original terms are
positive. At $a\le1$, $N_1=\tau_1=0$; the critical two-cycle, for example,
is $\{\sqrt{b/2},-\sqrt{b/2}\}$, has multiplier $9$, and contributes
$2/(9-1)=1/4$, agreeing with (16).

### Step 7. Primitive stability product and analytic continuation

For fixed $0<a<1$, the denominators in (16) are uniformly separated
from zero in $n$: $1-a^n\ge1-a$ and
$1-q^n\ge1-|q|$. Hence $\tau_n$ is bounded in $n$. At $a=1$ it is
bounded by $1/2$; at $a>1$ it decays exponentially. The defining logarithmic
series is absolutely convergent on $|u|<1$ for all parameters.

By the chain rule, repetition $s$ of $\gamma$ has multiplier
$\Lambda_\gamma^s$, and
$$
\frac1{\Lambda_\gamma^s-1}
=\sum_{j\ge1}\Lambda_\gamma^{-js}.
$$
The total series with $|u|$ substituted is finite by (16). Absolute
convergence therefore justifies grouping first by primitive orbits and
then by $j$, proving
$$
D_a(u)=\prod_{\gamma\ \mathrm{primitive}}\prod_{j\ge1}
\left(1-\frac{u^{p_\gamma}}{\Lambda_\gamma^j}\right),
\qquad |u|<1.                                               \tag{17}
$$
Only the finite-real primitives occur in this formula. The product's
global continuation is not asserted to follow from global primitive
product convergence.

Expanding (16) into geometric series on this disk and then summing
$-\sum v^n/n=\log(1-v)$ yields
$$
D_a(u)=
\begin{cases}
\displaystyle(1-u)
\frac{\prod_{j\ge1}(1-q^ju)^2}{\prod_{k\ge1}(1-a^ku)},
&0<a<1,\\[8pt]
\displaystyle(1-u)^{1/2}\exp(\operatorname{Li}_2(u)/2),&a=1,\\[4pt]
\displaystyle\prod_{k\ge1}(1-a^{-k}u),&a>1.
\end{cases}                                                 \tag{18}
$$
The square root is the branch equal to one at zero. Each separate
geometric product converges locally uniformly in the whole complex plane,
since its eigenvalue sequence is absolutely summable. Away from its
listed zeros the tail is nonzero: after the factors have modulus of their
arguments at most $1/2$, the series of their logarithms converges
absolutely. Thus the first line is a meromorphic continuation with exactly
the zeros and poles analyzed next; the third line is entire, with simple
zeros $a^k$, $k\ge1$.

### Step 8. Complete cancellation rule and entire resonance

For $a<1$ the numerator has a simple zero at $u=1$ and, if $q\ne0$,
double zeros at $u=q^{-j}$, $j\ge1$. These points are distinct and are
different from $1$. The denominator has simple zeros at $u=a^{-k}$,
$k\ge1$. Therefore its complete divisor rule is:

- a denominator point is a simple pole if it is not a numerator point;
- a coincident double numerator/simple denominator point is a simple zero;
- all other $q^{-j}$ are double zeros, and $1$ is always a simple zero.

The coincidence equation is exactly $a^k=q^j$. When $q=0$ there are
no such coincidences. When $q>0$, $q<a<1$, so the first denominator
zero $u=1/a$ cannot cancel. More explicitly, if
$\log a/\log q=M/N$ is rational in lowest positive terms, then the
coincidences are exactly $k=N\ell$, $j=M\ell$, $\ell\ge1$; if the ratio is
irrational there are none. Here $M<N$.

When $q<0$, only even $j$ can occur. If
$\log a/\log(q^2)=M/N$ in lowest positive terms, the coincidences are
exactly $k=N\ell$, $j=2M\ell$; an irrational ratio gives none. Odd-indexed
numerator zeros are negative and never cancel a denominator zero.

In particular the entire classification follows already by asking whether
the first denominator zero cancels:
$$
D_a\text{ is entire for }0<a<1
\quad\Longleftrightarrow\quad
0<a<\tfrac12,\quad a=(1-2a)^{2m}
\text{ for some integer }m\ge1.                             \tag{19}
$$
Necessity uses $a=q^{2m}$. Under this condition every denominator factor
is the numerator factor with index $2mk$, so it is also sufficient.
For each fixed $m$, the function $(1-2a)^{2m}-a$ is continuous and
strictly decreasing on $(0,1/2)$, has endpoint limits $1$ and $-1/2$,
and thus has exactly one zero $a_m$. These zeros are distinct because
different powers of the same number in $(0,1)$ cannot agree. The first
one is $a_1=1/4$.

At such a parameter the surviving product is
$$
D_{a_m}(u)=(1-u)\prod_{j\ge1}
(1-q^ju)^{\,2-\mathbf1_{\{2m\mid j\}}}.                      \tag{20}
$$
On a Hilbert space with an orthonormal basis indexed by these
multiplicities, the real diagonal entries $1$ once and $q^j$ with
multiplicity $2-\mathbf1_{\{2m\mid j\}}$ define a self-adjoint trace-class
operator: the sum of their absolute values is at most
$1+2|q|/(1-|q|)$. Its Fredholm determinant is (20). The analogous
diagonal entries $a^{-k}$ realize the entire supercritical product.
These are abstract constructions after determining the source germ.
No conjugacy to a naturally specified physical transfer operator or
Hamiltonian has been proved.

### Step 9. Critical fractional order, not a circle natural boundary

The critical line of (18) and the power series derivative of
$\operatorname{Li}_2$ give
$$
\frac{D_1'(u)}{D_1(u)}
=-\frac1{2(1-u)}-\frac{\log(1-u)}{2u},\qquad |u|<1.
$$
Along real $u\uparrow1$, $(u-1)\log(1-u)\to0$ and hence
$$
\lim_{u\uparrow1}(u-1)\frac{D_1'(u)}{D_1(u)}=\frac12.          \tag{21}
$$
A nonzero meromorphic function near $1$ has the local form
$(u-1)^k h(u)$ with $k$ an integer and $h(1)\ne0$ holomorphic; the same
limit would be $k$. Thus the germ has no meromorphic continuation through
$1$. In particular it is not the germ of an entire ordinary trace-class
Fredholm determinant.

This does not assert a natural boundary on the entire unit circle.
The logarithm and dilogarithm supply holomorphic continuation through
other unit-circle points in neighborhoods avoiding $1$, with compatible
local branches.

### Step 10. Two-sided locally uniform critical limits

For a fixed $n$, put $a=1-\varepsilon$, $q=1-2\varepsilon$. The binomial
expansion gives
$$
\frac1{1-(1-h)^n}
=\frac1{nh}+\frac{n-1}{2n}+O_n(h).
$$
Substitution into (16) proves
$\tau_n(a)\to(n-1)/(2n)$ as $a\uparrow1$. This fixed-$n$ calculation
alone would not justify passage through the infinite logarithmic series.

For $1/2<a<1$, $0<q<a$ and $q\le a^2$ because
$a^2-q=(a-1)^2$. The convexity of $x\mapsto x^n$ on the positive line
gives $1-2a^n+q^n\ge0$, since $a=(1+q)/2$.
Consequently
$$
0\le\tau_n(a)
=\frac{1-2a^n+q^n}{(1-a^n)(1-q^n)}
\le\frac2{1-a^{2n}}-\frac1{1-a^n}
=\frac1{1+a^n}\le1.                                        \tag{22}
$$

For $a>1$, the two finite fixed points $\pm r$ each have multiplier
$q=2a-1>1$. Their complete primitive stability factor is
$$
F_a(u)=\prod_{j\ge1}(1-q^{-j}u)^2.
$$
Removing exactly these two primitive orbits, including every repetition,
therefore means
$$
D_a^{\mathrm{red}}(u)=D_a(u)/F_a(u),\quad
\tau_n^{\mathrm{red}}(a)
=\frac1{a^n-1}-\frac2{q^n-1}.                               \tag{23}
$$
It does not mean subtracting only their first-iterate counts. On $|u|<1$,
$F_a$ is nonzero, so this quotient is unambiguous.
The expansion
$$
\frac1{(1+h)^n-1}
=\frac1{nh}-\frac{n-1}{2n}+O_n(h)
$$
with $a=1+\varepsilon$, $q=1+2\varepsilon$ gives
$\tau_n^{\mathrm{red}}(a)\to(n-1)/(2n)$.
Convexity and $q\le a^2$ now give
$$
0\le\tau_n^{\mathrm{red}}(a)
=\frac{q^n-2a^n+1}{(a^n-1)(q^n-1)}
\le\frac1{a^n-1}-\frac2{a^{2n}-1}
=\frac1{1+a^n}\le\frac12.                                  \tag{24}
$$

For every fixed $\rho<1$, (22)--(24) dominate the logarithmic terms
uniformly on $|u|\le\rho$ by $\rho^n/n$, whose sum is finite. A finite-head,
uniform-tail argument gives uniform convergence of the normalized
logarithms; exponentiation preserves uniform convergence on this compact
disk. Therefore
$$
D_a\longrightarrow D_1\ (a\uparrow1),\qquad
D_a^{\mathrm{red}}\longrightarrow D_1\ (a\downarrow1)
$$
locally uniformly on $|u|<1$. No assertion includes $u=1$ or is uniform
on the whole complex plane.

The unreduced supercritical limit is different: for real $0<u<1$,
$\log D_a(u)\le-\tau_1(a)u=-u/(a-1)\to-\infty$, whereas $D_a(0)=1$.
It cannot converge locally uniformly to $D_1$. The removal in (23) is
forced by the collision of these two real fixed points with infinity.

### Step 11. Physical owner, old Blaschke collision and arithmetic scope

For $a<1$, infinity is a repelling fixed point of the projective-real
map, with multiplier $a^{-1}$. Its full primitive factor is
$$
D_{\infty,a}(u)=\prod_{k\ge1}(1-a^ku).
$$
Thus the full projective-circle stability germ is
$$
D_{\mathrm{circle},a}=D_aD_{\infty,a}
=(1-u)\prod_{j\ge1}(1-q^ju)^2.                              \tag{25}
$$
This is the established Blaschke determinant mechanism, and it is entire.
The finite-real map deletes this actual primitive orbit, so dividing by
its factor can create poles. Deleting a measure-zero orbit leaves ordinary
$L^p$ classes unchanged; it does not prove that the same operator's trace
has lost that orbit. Accordingly (25) is a periodic-product identity, not
an asserted restriction theorem for the old operator.

The nearest repository package C380 treats
$w(w-\alpha)/(1-\alpha w)$ with $0\le\alpha<1$, so its direct overlap here
is $q=-\alpha$, $0<a\le1/2$. The wider Blaschke theorem in the literature
also owns positive $q$. Moreover the coordinate $c=\sqrt{b/(1-a)}$
diverges as $a\uparrow1$; the critical real map is not obtained by
silently substituting $q=1$ into a nonsingular fixed Cayley chart.

No intrinsic prime labels, target zeros, target Euler factors, root
numbers, automorphy, target functional equation or Hilbert--Pólya
correspondence is established. The exploratory strict ceiling remains
$A0\_FAIL$, $A1\_WEAK$, $A2\_FAIL$, $A3\_FAIL$,
$A4\_FORMAL\_HINT$; this is not a formal evaluator run.
All target/Route-B claims and permission remain false under
NO_BAD_EULER_OR_ROOT_NUMBER.

Therefore the stated source-system contract follows. $\square$

## Corrections or Missing Assumptions

- No weakening of the explicit scout contract was needed. The scope above
  spells out what the phrase “three phases” proves: invariant measures and
  survivor/escape geometry, not a new ergodicity or mixing theorem.
- The full-circle determinant and the finite-real stability germ are
  distinct objects even though their measure spaces differ by a null set.
- Critical non-meromorphic continuation at $1$ is not a whole-circle
  natural-boundary theorem.
- The abstract diagonal realization at resonant parameters is intentionally
  not called a natural dynamical transfer realization or target A2 progress.

## Open Risks

- The proof needs a substantive independent internal mathematical review.
  No such review has yet been claimed for this author draft.
- Directed literature search is recorded in SOURCE_AUDIT.md. It supports
  classical attribution and a bounded no-match observation, not publication
  novelty. Discovery of a prior full physical-deletion/resonance/critical-limit
  theorem would change admission significance without changing these formulas.
- The small executable tests inspect exact finite consequences and selected
  local identities. They do not prove the all-parameter statements.
- No natural finite-real transfer-operator domain or trace theorem has been
  supplied. This is an explicit boundary, not an omitted step of the claim.
