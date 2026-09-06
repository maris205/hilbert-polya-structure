# Rectangular common returns: convergence and joint meromorphic boundary

2026-09-06. Author-side candidate developed after the initial five-way
screen. No C-number, manuscript admission, literature-first claim or
target-arithmetic conclusion is assigned. The question is not the
diagonal gcd estimate, not Lind's subgroup-index zeta function and not
a second specialization of the wild FAD theorem.

## 1. Native object, clocks and observable

Let $a,b\geq2$ be arbitrary integers; they need not be coprime. On the
circle $X=\mathbb R/\mathbb Z$, let $T_a(x)=ax$ and $T_b(x)=bx$.
These commuting endomorphisms define an ordinary $\mathbb N^2$-action.
For two independent integer clocks $n,m\geq1$, put
$$
 C_{a,b}(n,m)=\#\bigl(\operatorname{Fix}(T_a^n)
                         \cap\operatorname{Fix}(T_b^m)\bigr),
 \qquad
 R_{a,b}(x,y)=\sum_{n,m\geq1}C_{a,b}(n,m)x^ny^m.
$$
The elementary cyclic-group identity is
$$
 \tag{1}
 C_{a,b}(n,m)=\gcd(a^n-1,b^m-1).
$$
Indeed, the common kernel of multiplication by two positive integers
on $\mathbb R/\mathbb Z$ is the cyclic subgroup whose order is their
gcd. This identity and the native action are classical, not new claims.

The same counts occur for the automorphisms dual to multiplication by
$a$ and $b$ on $\mathbb Z[(ab)^{-1}]$: the gcd in (1) is coprime to
$ab$, so this localization removes none of the common finite kernel.
This alternative realization is not needed below.

Write $\mathbb D=\{z\in\mathbb C:|z|<1\}$. By the *open absolute
convergence domain* we mean the interior of the set on which the
double series of absolute values is finite. The coordinate axes
outside this open domain require a harmless but explicit distinction:
all summands are zero when either variable is zero, so the series
converges pointwise there without defining a neighborhood of
convergence.

## 2. Proposed complete analytic classification

**Theorem.** For all integers $a,b\geq2$:

1. If $a,b$ are multiplicatively independent, the open absolute
   convergence domain of $R_{a,b}$ is exactly $\mathbb D^2$.
2. If $a,b$ are multiplicatively dependent, write uniquely
   $a=c^r$, $b=c^s$ with $c\geq2$ an integer and coprime positive
   integers $r,s$. The open absolute convergence domain is
   $$
   \tag{2}
   \Omega_{r,s,c}=
   \{(x,y)\in\mathbb D^2:
                       c^{rs}|x|^s|y|^r<1\}.
   $$
   The function has a meromorphic continuation to $\mathbb D^2$,
   given by the locally normally convergent meromorphic expansion
   $$
   \tag{3}
   R_{a,b}(x,y)=
   \sum_{\substack{i,j\geq1\\\gcd(i,j)=1}}
     \frac{c^{h_{i,j}}x^iy^j}{1-c^{h_{i,j}}x^iy^j}
       -\frac{xy}{(1-x)(1-y)},
   \qquad h_{i,j}=\gcd(ri,sj).
   $$
   Its polar hypersurfaces in the bidisc are exactly
   $$
   \tag{4}
   P_{i,j}=\{(x,y)\in\mathbb D^2:
                          c^{h_{i,j}}x^iy^j=1\},
   \qquad \gcd(i,j)=1.
   $$
   Each component is genuine and has pole order one. At any fixed
   $y_0\in\mathbb D$ and any pole $x_0\in\mathbb D$ of the resulting
   one-variable meromorphic function, its residue is
   $$
   \tag{5}
   -x_0\sum_{\substack{(i,j)\ {m primitive}\\
                 c^{h_{i,j}}x_0^iy_0^j=1}}\frac1i\neq0.
   $$
   The sum is finite, so coincident poles do not cancel.
3. In both cases, the resulting meromorphic function on $\mathbb D^2$
   has no local joint meromorphic continuation through any point of
   $\partial(\mathbb D^2)$. Thus the bidisc is a joint meromorphic
   natural-boundary domain, although in the dependent case it is
   larger than the original convergence domain.

The third assertion is about a function of **two complex variables**.
It does not claim a natural boundary for every fixed complex slice.
For example, the slice $y=0$ is identically zero and entire. The
theorem nevertheless forbids a joint cap around $(x_0,0)$ when
$|x_0|=1$.

The sole deep arithmetic input below is the classical general
Corvaja–Zannier $S$-unit gcd estimate. The radial singularity mechanism
and the Hartogs/subharmonic propagation argument are classical
analytic tools. All are deducted in the ownership assessment.

## 3. Common-base algebra and the exact convergence domains

### 3.1 The common base

Suppose $a^u=b^v$ for positive integers $u,v$. Divide by
$\gcd(u,v)$ so that $(u,v)=1$. For every prime $p$,
$u v_p(a)=v v_p(b)$, hence $v\mid v_p(a)$ and $u\mid v_p(b)$.
There are therefore nonnegative integers $e_p$ such that
$a=c^v,b=c^u$ with $c=\prod_pp^{e_p}$.
The coprime exponent pair and $c$ are unique by the same valuation
comparison. Set $r=v,s=u$.

The Euclidean algorithm, or multiplicative order modulo a common
divisor, gives
$$
 \tag{6}
 \gcd(c^u-1,c^v-1)=c^{\gcd(u,v)}-1.
$$
Both facts are classical. In particular, in the dependent branch,
$C_{a,b}(n,m)=c^{\gcd(rn,sm)}-1$.

### 3.2 Independent bases

We use Corvaja–Zannier,
*A lower bound for the height of a rational function at $S$-unit points*,
[arXiv:math/0311030v2](https://arxiv.org/pdf/math/0311030v2),
Corollary 1 and its equivalent inequality (1.3). For positive integer
$S$-units $u,v$ that are multiplicatively independent, it implies,
with finitely many exceptions for each $\epsilon>0$,
$$
 \gcd(u-1,v-1)<\max(u,v)^\epsilon.
$$
This is the two-exponent $S$-unit statement, not an unjustified use of
the one-clock diagonal BCZ estimate.

Apply it to $u=a^n,v=b^m$, with $S$ containing the prime divisors of
$ab$. These two integers are multiplicatively independent for every
$n,m\geq1$. Absorb the finitely many exceptions in $K_\epsilon$:
$$
 \tag{7}
 C_{a,b}(n,m)\leq
 K_\epsilon\exp\bigl(\epsilon\max(n\log a,m\log b)\bigr).
$$
For any $0<u,v<1$, choose $\epsilon$ sufficiently small that
$u\exp(\epsilon L)<1$ and $v\exp(\epsilon L)<1$, where
$L=\max(\log a,\log b)$. Since
$\max(n\log a,m\log b)\leq L(n+m)$, (7) bounds the double
series on $|x|\leq u,|y|\leq v$ by a product of geometric series.
This proves locally normal absolute convergence in $\mathbb D^2$.

For any $y\neq0$ and $|x|\geq1$, the terms with a fixed $m$ already
have divergent absolute sum, since $C_{a,b}(n,m)\geq1$. The other
variable is symmetric. This proves the asserted open domain and the
pointwise-axis exception.

### 3.3 Dependent bases

Put $u=|x|,v=|y|$, first with both nonzero. The condition in (2) is
equivalent to
$$c u^{1/r}v^{1/s}<1.$$
Choose $0<\theta<1$ sufficiently close to one that
$c u^{\theta/r}v^{\theta/s}<1$. For
$g=\gcd(rn,sm)$, the inequalities $n\geq g/r$ and $m\geq g/s$
give
$$
 \begin{aligned}
 C_{a,b}(n,m)u^nv^m
 &\leq c^g u^nv^m\\
 &\leq
 (c u^{\theta/r}v^{\theta/s})^g
            u^{(1-\theta)n}v^{(1-\theta)m}\\
 &\leq u^{(1-\theta)n}v^{(1-\theta)m}.
 \end{aligned}
$$
This proves absolute convergence and locally normal convergence
throughout (2), including its axes by continuity or the original
elementary count bound.

If $c^{rs}u^sv^r\geq1$, the terms on the primitive ray
$(n,m)=(sk,rk)$ satisfy
$$
 C_{a,b}(sk,rk)u^{sk}v^{rk}
   =(c^{rsk}-1)u^{sk}v^{rk}
$$
and fail to tend to zero. If $u\geq1$ or $v\geq1$ with neither
coordinate zero, the fixed-row argument from the independent case
applies. This proves the exact convergence domain, with no claim of
analytic singularity at every point of its curved boundary.

## 4. The dependent meromorphic expansion and noncancellation

Write $(n,m)=k(i,j)$ uniquely with $k\geq1$, $i,j\geq1$ and
$(i,j)=1$. Then
$\gcd(rn,sm)=k h_{i,j}$. Summing the geometric series on each such
ray gives
$$
 \sum_{k\geq1}(c^{kh_{i,j}}-1)x^{ki}y^{kj}
 =\frac{c^{h_{i,j}}x^iy^j}{1-c^{h_{i,j}}x^iy^j}
   -\frac{x^iy^j}{1-x^iy^j}.
$$
Summation is justified by absolute convergence on (2). Unique
primitive-ray decomposition also gives
$$
 \sum_{(i,j)=1}\frac{x^iy^j}{1-x^iy^j}
 =\sum_{n,m\geq1}x^ny^m=\frac{xy}{(1-x)(1-y)}.
$$
This proves (3) on its original domain.

Since $(r,s)=(i,j)=1$, prime-by-prime comparison gives
$$
 \tag{8}
 h_{i,j}=\gcd(r,j)\gcd(s,i)\mid rs.
$$
For every compact sub-bidisc $|x|\leq u<1$, $|y|\leq v<1$,
$$|c^{h_{i,j}}x^iy^j|\leq c^{rs}u^iv^j.$$
Only finitely many pairs have this upper bound greater than $1/2$.
The remaining summands in (3) are bounded by
$2c^{rs}u^iv^j$, a summable family. Consequently (3) defines a
meromorphic function in $\mathbb D^2$, with a locally finite family
of potential polar hypersurfaces (4).

These hypersurfaces are distinct. The primitive monomial
$x^iy^j$ has connected level sets in $(\mathbb C^\times)^2$:
choose integers completing $(i,j)$ to a unimodular $2\times2$
matrix and use the corresponding invertible monomial coordinates.
Thus each $P_{i,j}$ is a smooth irreducible hypersurface in the
algebraic torus; its portion in the bidisc is nonempty. Different
primitive exponent pairs cannot give the same hypersurface.

At a generic point of any one component, all other terms are
holomorphic and its own term has a simple pole. This proves that the
component is genuine. It also proves that intersections of components
do not remove any of the polar divisor. More explicitly, at fixed
$y_0$ each pole is away from $x=0$ and its individual residue is
$$
 \lim_{x\to x_0}(x-x_0)
       \frac{c^{h_{i,j}}x^iy_0^j}
            {1-c^{h_{i,j}}x^iy_0^j}
   =-\frac{x_0}{i}.
$$
Only finitely many components meet a compact neighborhood of an
interior point. Their residues therefore sum as in (5), and cannot
cancel. This verifies the actual polar set, not merely a collection
of formal candidate denominators.

## 5. A genuine natural-boundary slice for every pair of bases

Fix any real $t$ with $0<t<1/b$. The count bound
$C_{a,b}(n,m)\leq b^m-1$ shows that
$$
 R_{a,b}(x,t)=\sum_{n\geq1}A_n(t)x^n,\qquad
 A_n(t)=\sum_{m\geq1}C_{a,b}(n,m)t^m
$$
has bounded coefficients, uniformly in $n$. We construct a finite
positive measure giving these coefficients exactly.

For a positive integer $d$ coprime to $a$, write
$k_a(d)=\operatorname{ord}_d(a)$ and set $k_a(1)=1$.
Let $\nu_k$ denote uniform probability on the $k$-th roots of unity.
The elementary totient identity $N=\sum_{d\mid N}\varphi(d)$ gives
$$
 \tag{9}
 C_{a,b}(n,m)=
 \sum_{\substack{d\mid b^m-1\\(d,a)=1}}
      \varphi(d)\,\mathbf1_{k_a(d)\mid n}.
$$
Define
$$
 \tag{10}
 \mu_t=\sum_{m\geq1}t^m
       \sum_{\substack{d\mid b^m-1\\(d,a)=1}}
               \varphi(d)\nu_{k_a(d)}.
$$
It is a positive atomic measure and
$$
 \mu_t(\mathbb T)
 \leq\sum_{m\geq1}(b^m-1)t^m<\infty.
$$
Since $\int\xi^n\,d\nu_k(\xi)=\mathbf1_{k\mid n}$, (9) gives
$$A_n(t)=\int\xi^n\,d\mu_t(\xi).$$

Choose a prime $\ell\nmid ab$. For every $j\geq1$, the integer
$d_j=\ell^j$ divides $b^{m_j}-1$ with
$m_j=\operatorname{ord}_{\ell^j}(b)$, and hence the support of
$\mu_t$ contains every $k_j$-th root of unity, where
$k_j=\operatorname{ord}_{\ell^j}(a)$. The integers $k_j$ are
unbounded. Otherwise, with $N$ the lcm of all positive integers up
to a uniform bound, one would have $\ell^j\mid a^N-1$ for every
$j$, which is impossible for $a\geq2$. The union of these complete
root grids is dense in the unit circle. Positivity of (10) ensures
that every displayed atom has nonzero **actual** mass.

For $|x|<1$, absolute convergence gives the Cauchy representation
$$
 R_{a,b}(x,t)=\int\frac{\xi x}{1-\xi x}\,d\mu_t(\xi).
$$
At an atom $\xi_0$ and for $0<\rho<1$,
$$
 \left|(1-\rho)\frac{\rho\xi\xi_0^{-1}}
                              {1-\rho\xi\xi_0^{-1}}\right|
 \leq1.
$$
Dominated convergence therefore yields
$$
 \tag{11}
 \lim_{\rho\uparrow1}(1-\rho)
               R_{a,b}(\rho\xi_0^{-1},t)
       =\mu_t(\{\xi_0\})>0.
$$
The dense set of such singularities rules out holomorphic
continuation through any arc. A meromorphic continuation would
require poles at a dense subset of that arc, also impossible. Thus
this real slice has the whole unit circle as a natural boundary.
No effective gcd estimate or Diophantine lower bound is used here.

## 6. Classical Hartogs propagation in the form needed here

For a primary textbook account of the machinery, see Jaap Korevaar
and Jan Wiegerinck, *Several Complex Variables*, version 23 August
2017, [author-hosted notes](https://staff.science.uva.nl/j.j.o.o.wiegerinck/edu/scv/scvboek.pdf),
Section 4.8, equations (4.8.4)–(4.8.5), and Properties 8.4.3.
These give the logarithmic Taylor-coefficient envelope and
upper-semicontinuous regularization principles used below. The
following explicit cap formulation is proved here as an application,
not claimed as a new Hartogs theorem.

**Lemma (joint-cap propagation).** Let $V\subset\mathbb C$ be a
connected domain and let $F$ be holomorphic on $\mathbb D\times V$.
Suppose that for one $t\in V$, $x\mapsto F(x,t)$ has the whole
unit circle as a natural boundary. Then there is no local joint
holomorphic or meromorphic continuation through any
$(x_0,y_0)\in\mathbb T\times V$.

**Proof.** First suppose that there is a holomorphic cap. Shrinking
it, take product discs $B(x_0,\eta)\times B(y_0,\eta)$ on which
the extension is holomorphic and agrees with $F$ on the interior
overlap. Choose $0<\delta<\min(1,\eta/4)$ and let
$c=(1-\delta)x_0$. Then $B(c,2\delta)\subset B(x_0,\eta)$.
For $n\geq0$, the Taylor coefficients
$$a_n(y)=\frac1{n!}\partial_x^n F(c,y)$$
are holomorphic on $V$.

For $n\geq1$ put $u_n(y)=n^{-1}\log|a_n(y)|$, permitting the
value $-\infty$. These are subharmonic functions. Cauchy's estimate
on every radius $0<q<\delta$ about $c$, uniformly for $y$ in a
compact subset of $V$, gives
$$\limsup_{n\to\infty}u_n(y)\leq-\log\delta$$
locally uniformly in the upper-bound sense. In particular the family
is locally bounded above. The classical upper-envelope theorem for
subharmonic functions makes
$$
 U(y)=\left(\limsup_{n\to\infty}u_n(y)\right)^*
$$
subharmonic or identically $-\infty$, and gives
$U\leq-\log\delta$. Here the star denotes upper-semicontinuous
regularization.

The slice at $t$ is holomorphic in the disc $B(c,\delta)$ and
singular at its boundary point $x_0$. Its Taylor radius about $c$
is therefore exactly $\delta$. The Cauchy–Hadamard formula gives
$\limsup_nu_n(t)=-\log\delta$. Since regularization is no smaller
than the original function, $U(t)=-\log\delta$. The maximum
principle on the connected domain $V$ forces
$U\equiv-\log\delta$.

On the other hand, choose any $q_1$ with
$\delta<q_1<2\delta$. The cap and Cauchy's estimate on
$|x-c|=q_1$, uniformly for $y$ in a smaller neighborhood of $y_0$,
give $U\leq-\log q_1<-\log\delta$ there, a contradiction.
This proves the holomorphic assertion. The regularization step is
important: the proof does not assert that the unregularized Taylor
radius is constant on every exceptional slice.

For a meromorphic cap, represent it locally as $A/B$ with $A,B$
holomorphic and $B$ not identically zero. The denominator cannot
vanish at every point of a product of a unit-circle arc and an open
parameter disc. Otherwise, for each parameter, the one-variable
identity theorem in $x$ makes $B$ identically zero; hence $B$ is
zero on the whole product, a contradiction. There is consequently
a nearby point of $\mathbb T\times V$ where $B\neq0$, producing
a holomorphic cap already excluded above. This proves the lemma.
$\square$

This is an explicit application of classical Hartogs/subharmonic
machinery, not a claimed new several-complex-variables theorem.

## 7. Joint boundary for the independent branch

For independent bases, Section 3 proves that $R_{a,b}$ is holomorphic
on $\mathbb D^2$. Choose $t\in(0,1/b)$ and apply Section 5 followed
by the lemma with $V=\mathbb D$. This excludes every joint
meromorphic cap at $\mathbb T\times\mathbb D$.
Interchanging $(a,x)$ and $(b,y)$ excludes
$\mathbb D\times\mathbb T$. A cap at a corner point in
$\mathbb T^2$ would restrict to a cap at a nearby point of one of
these faces. Thus no point of $\partial(\mathbb D^2)$ admits a
joint meromorphic cap.

## 8. Joint boundary for the dependent branch

The elementary bound $C_{a,b}(n,m)\leq b^m-1$ shows that the original
series is holomorphic on $\mathbb D\times\mathbb D_{1/b}$, where
$\mathbb D_{1/b}=\{|y|<1/b\}$. Apply Sections 5–6 on this product.
There is no joint meromorphic cap at any
$(x_0,y_0)$ with $|x_0|=1$ and $|y_0|<1/b$.

Now suppose that $1/b<|y_0|<1$. For arbitrarily large positive
integers $k$ with $(k,r)=1$, the pair
$(i,j)=(sk,r)$ is primitive. Its exponent is
$$h_{sk,r}=\gcd(rsk,sr)=rs.$$
Consequently the actual slice poles from (4) include all roots of
$$
 \tag{12}
 c^{rs}x^{sk}y_0^r=1.
$$
Their common modulus is
$(c^{rs}|y_0|^r)^{-1/(sk)}<1$, tending to one, and they form complete
equally spaced root grids whose mesh tends to zero. The
noncancellation statement (5) makes each a genuine pole. Thus, near
every $x_0\in\mathbb T$, infinitely many interior slice poles tend
to $x_0$.

Suppose a joint meromorphic cap $A/B$ existed at $(x_0,y_0)$.
Shrink its parameter disc so that every $y$ in that disc has
$1/b<|y|<1$. For **each** such $y$, the same root-grid argument
gives infinitely many genuine slice poles inside the cap's
$x$-disc tending to $x_0$. At every such pole $B(x,y)=0$;
otherwise $A/B$ would be holomorphic there. The one-variable
identity theorem implies $B(\cdot,y)\equiv0$ on that disc.
Doing this for all $y$ in an open set forces $B\equiv0$, a
contradiction. This excludes these remaining open face points.

If $|y_0|=1/b$, every putative cap contains nearby face points
with $|y|>1/b$, which have just been excluded. Together with the
strip argument, this blocks all of $\mathbb T\times\mathbb D$.
Symmetry blocks $\mathbb D\times\mathbb T$, and the corner
argument from Section 7 finishes the proof of the theorem.
$\square$

## 9. Classical deductions and limits of the present claim

The native count identity, the common-base identity, elementary
totient expansions, positive Cauchy measures, primitive-lattice-ray
summation, and Hartogs propagation are classical ingredients. The
independent-domain argument is a direct application of the general
Corvaja–Zannier theorem, whose arithmetic content is not reproved or
claimed here. No effective value of its exceptional threshold is
needed or supplied.

Richard Miles's 2015 natural-boundary theorem for the Lind zeta of
commuting group automorphisms is a close owner, but counts all
finite-index subgroups by index; it is not the two-variable ordinary
rectangular series defined in Section 1. It must not be cited as if
it already proved, or as if it left open, this exact formulation.
Ward's 1989 thesis already defines a rectangular zeta, with the
rectangles first aggregated by volume into one variable; Ward's 1992
Example 3.1 already studies the two independent rectangular clocks
for the circle multiplication action. Miles's 2013 synchronization
generating functions retain one common time variable. These objects,
their counting identities and their classical analytic conclusions
are also deducted, with exact read scopes and version boundaries in
`RECTANGULAR_SOURCE_AUDIT.md`.

Khai-Hoan Nguyen-Dang,
*On the sequence $\gcd(a^n-1,b^n-1)$*,
[arXiv:2606.07959v2](https://arxiv.org/pdf/2606.07959v2),
25 August 2026, Theorem 1.1 already classifies the diagonal sequence
as C-finite exactly for multiplicatively dependent bases. In the
independent case, its result plus the classical Pólya–Carlson theorem
gives the diagonal natural boundary. The corresponding
non-D-finiteness consequence for the two-variable series, using
closure under diagonals, is therefore not an independent novelty
claim. The candidate under consideration is the full two-variable
convergence/polar-divisor/joint-boundary classification above.

No source-completeness or priority certificate follows from this
proof. The bounded nearest-owner audit is recorded separately; an
independent substance decision remains necessary. In particular,
changing the name of a
generating function or merely retaining a second variable would not
alone justify a manuscript. There is no claim that these return
counts supply rational-prime orbit labels, a logarithmic prime clock,
a Hilbert–Pólya operator or a Riemann-zeta conclusion.
