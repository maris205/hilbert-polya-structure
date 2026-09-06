# Finite-adelic radial coefficients: a rationality/natural-boundary criterion

2026-09-06. Author-side proposed proof for the new arithmetic scouting
batch. No C-number, manuscript admission, publication-priority certificate,
or target-arithmetic conclusion is assigned by this file.

## Claim

An exact finite criterion classifies the ordinary generating function of
a finite sum of unit-modulus exponential phases multiplied by periodic,
finite-adelic radial coefficients: it is rational, or its unit circle is
a natural boundary. In the second case the actual coefficient measure
has a dense set of nonzero atoms, even after all coincident phases are
aggregated.

The FAD consequence is that the Artin–Mazur zeta function of every
genuinely distorted positive-entropy FAD system has its entropy circle
as a natural boundary, without a unique-dominant-root hypothesis and
without an integrality assumption on the wild exponents. The comparison
is with BCH, arXiv:2209.00085v2 (19 April 2024), Theorem 11.3.8,
Remark 11.3.10, and Problem 14.1.2. The no-wild algebraic cases must
additionally be deducted against Baril Boudreau–Holmes–Nguyen,
*Adelic perturbation of rational functions and applications*,
arXiv:2307.07910v1 / Math. Ann. 392 (2025), 2253–2275: their
Theorems 1.2, 2.14, and 4.6 already remove the dominant-root restriction
in important no-wild regimes. The specifically new dynamical test here
is the nonhyperbolic **wild** regime, exemplified in
`REALIZED_EXAMPLE.md`; its perturbation violates their sublinear-height
assumption. The exact complex-coefficient active-fibre criterion also
does not assume algebraicity or a height bound. Current/final-version
ownership remains a separate source-audit question.

## Status

**PROVABLE AS STATED — author-side complete argument below; independent
mathematical and source admission review still required.**

## Assumptions and notation

1. $S$ is a finite set of primes. For $p\in S$, $(s_{p,n})$ and
   $(t_{p,n})$ are periodic sequences of nonnegative real numbers.
   For the abstract theorem, their periods may be divisible by $p$.
2. $(r_n)$ is a complex periodic sequence, allowed to vanish.
3. $u_n=\sum_{j=1}^J c_j\eta_j^n$, where the $\eta_j$ are distinct
   points of the complex unit circle and the $c_j$ are nonzero complex
   numbers. The empty phase sum is also permitted and gives zero.
4. All periodic data are extended to integer indices. At zero, set
   $v_p(0)=+\infty$ and use the continuous radial kernel
   $$
   H_{p;s,t}(x)=p^{-s v_p(x)-t p^{v_p(x)}}\quad(x\neq0),
   \qquad
   H_{p;s,t}(0)=
   \begin{cases}0,&(s,t)\neq(0,0),\\1,&(s,t)=(0,0).
   \end{cases}
   $$
   The pair $(s,t)$ is *active* when it is not $(0,0)$.
5. Define the bounded coefficient sequence
   $$
   a_n=u_n r_n\prod_{p\in S}H_{p;s_{p,n},t_{p,n}}(n),
   \qquad F(z)=\sum_{n\geq1}a_n z^n\quad(|z|<1).
   $$
   The clock remains the ordinary integer $n$.

Partition the phases by
$$
\eta_i\sim\eta_j\quad\Longleftrightarrow\quad
\eta_i/\eta_j\text{ is a root of unity}.
$$
For each class $C$, choose a representative $\rho_C$, and write
$\eta_j=\rho_C\omega_j$ with $\omega_j$ a root of unity. Choose a
positive integer $W$ divisible by all periods of the given sequences
and all orders of the $\omega_j$. For $a\in\mathbb Z/W\mathbb Z$, put
$$
b_C(a)=r_a\sum_{j\in C}c_j\omega_j^a,
\qquad \nu_p=v_p(W).
$$
The finite *active-fibre condition* is
$$
\tag{AF}
\text{there exist }C,p,a\text{ such that }
b_C(a)\neq0,\quad (s_{p,a},t_{p,a})\neq(0,0),\quad
a\equiv0\pmod{p^{\nu_p}}.
$$
If $p\nmid W$, its congruence condition is vacuous.

## Theorem 1: exact analytic classification

If (AF) fails, $F$ is rational. If (AF) holds, the unit circle is a
natural boundary for $F$, and $F$ cannot be meromorphically continued
through any point of that circle. In the latter case there is a finite
complex atomic measure $\mu$ on the unit circle such that
$$
a_n=\int \xi^n\,d\mu(\xi),
$$
whose nonzero atoms are dense, and for every atom at $\xi_0$,
$$
\tag{RL}
\lim_{r\uparrow1}(1-r)F(r\xi_0^{-1})=\mu(\{\xi_0\}).
$$

## Proof strategy and dependency map

1. Expand each radial kernel into indicators of $p$-adic balls. Each
   indicator has Fourier norm one, giving an absolutely summable
   character expansion on the relevant compact finite-adelic group.
2. Aggregate phases modulo roots of unity *before* constructing the
   actual coefficient measure. Distinct phase classes then have disjoint
   rational-frequency translates, and character evaluation at the dense
   integer generator is injective.
3. An active fibre forces unbounded $p$-conductor in one grouped Fourier
   expansion. Invariance under multiplication of the $p$-coordinate by
   units congruent to one gives increasingly fine full grids of equal,
   nonzero coefficients. This proves dense support after aggregation.
4. A dominated radial limit extracts each actual atomic mass. Dense
   nonzero masses rule out meromorphic continuation across every arc.
5. If there is no active fibre, every grouped function depends only on
   the finite residue coordinate, giving an explicit rational series.

The harmonic facts used below are character orthogonality for compact
groups, invariance of Haar probability under group automorphisms, the
finite Fourier identity for a subgroup indicator, and dominated
convergence. Each use is justified in place. The elementary radial
expansion and Cauchy-transform observation are not advertised as new
in isolation. The additional argument is the exact active-fibre criterion
and its phase-safe conductor-grid consequence.

## Proof of Theorem 1

### Step 1. The finite-adelic group

Let
$$
D=\overline{\{(n\bmod W,(n)_{p\in S}):n\in\mathbb Z\}}
\subset (\mathbb Z/W\mathbb Z)\times\prod_{p\in S}\mathbb Z_p,
$$
and let $g_0=(1\bmod W,(1)_{p\in S})$. Direct use of the Chinese
remainder theorem gives
$$
\tag{1}
D=\{(a,x):x_p\equiv a\pmod{p^{\nu_p}}\text{ for all }p\in S\}.
$$
Indeed, these congruences hold on the diagonal and define a closed set.
Conversely, a compatible specification modulo $W$ and finitely many
$p^{K_p}$, with $K_p\geq\nu_p$, is one solvable generalized CRT system,
so every neighborhood of a point on the right contains a diagonal
integer. This proves (1).

Every character appearing below has finite order. Moreover the map
$\chi\mapsto\chi(g_0)$ is injective on the continuous characters of
$D$: if two characters agree at $g_0$, they agree at every $ng_0$,
and hence everywhere by density and continuity.

### Step 2. Absolutely summable radial Fourier expansions

For an active pair, write $h(v)=p^{-sv-tp^v}$ for $v\geq0$ and
$\delta_j=h(j-1)-h(j)>0$. Since $h(v)\downarrow0$,
$$
\tag{2}
H_{p;s,t}(x)=h(0)-\sum_{j\geq1}\delta_j\mathbf1_{p^j\mathbb Z_p}(x),
\qquad \sum_{j\geq1}\delta_j=h(0)\leq1.
$$
The identity holds at zero as well as off zero; the numerical tail
uniformly bounds the functional tail. The finite identity
$$
\tag{3}
\mathbf1_{p^j\mathbb Z_p}(x)
=p^{-j}\sum_{b=0}^{p^j-1}\exp(2\pi i b[x]_{p^j}/p^j)
$$
shows that this indicator has an absolutely summable character
expansion of total coefficient mass one. Combining (2) and (3), then
collecting repeated characters, gives a uniformly absolutely convergent
character expansion for $H_{p;s,t}$ of total coefficient mass at most
$2h(0)\leq2$. The inactive kernel is the single character one.

Define the grouped functions on $D$ by
$$
\tag{4}
q_C(a,x)=b_C(a)\prod_{p\in S}H_{p;s_{p,a},t_{p,a}}(x_p).
$$
On the ambient product group, first write this as a finite sum over
$a\in\mathbb Z/W\mathbb Z$ using the finite-coordinate singleton
indicators. Each such indicator has Fourier norm one. Multiplying the
absolutely convergent kernel expansions and summing over $a$ gives a
character expansion with total coefficient mass at most
$2^{|S|}\sum_a|b_C(a)|$. Restrict it to $D$ and collect characters
that become equal there. This cannot increase the total absolute mass.
Consequently
$$
\tag{5}
q_C(g)=\sum_\chi\widehat q_C(\chi)\chi(g),
\qquad \sum_\chi|\widehat q_C(\chi)|<\infty,
$$
uniformly on $D$. The coefficients after collection are indeed the
Haar Fourier coefficients: integrate against $\overline\chi$ termwise.
A nontrivial character has integral zero, because a translation
multiplying it by a value different from one leaves its integral
unchanged. This proves the required orthogonality and identification.

Every character in (5) is a restriction of a product character of
$\mathbb Z/W\mathbb Z$ and finitely many finite-conductor $p$-adic
characters. No assertion that an arbitrary continuous function has an
absolutely summable expansion is used.

### Step 3. An active fibre forces unbounded conductor

Assume (AF), and fix witnesses $C,p,a$. In the fibre over $a$, choose
for every $q\neq p$ a nonzero $x_q\in a+q^{\nu_q}\mathbb Z_q$.
Such a point exists in each infinite ball. Their kernel factors are
strictly positive, including the value one of an inactive kernel.
By (1) the remaining coordinate can vary throughout $p^{\nu_p}\mathbb Z_p$.
On this slice,
$$
\tag{6}
q_C(a,x)=B_0 H_{p;s_{p,a},t_{p,a}}(x_p),
\qquad B_0\neq0.
$$
Here $B_0=b_C(a)\prod_{q\neq p}H_{q;s_{q,a},t_{q,a}}(x_q)$.
The values at $x_p=0$ and $x_p=p^K$ are different for every
$K\geq\nu_p$: the first is zero and the second is nonzero.

For $K\geq\nu_p$, let $U_p(K)$ be the subgroup of $D$ having
finite coordinate zero, $p$-coordinate in $p^K\mathbb Z_p$, and all
other coordinates zero. If every character with nonzero coefficient
in (5) were trivial on $U_p(K)$, uniform convergence would make
$q_C$ invariant under translation by $U_p(K)$. This contradicts the
two values just exhibited. Thus, for arbitrarily large $K$, a nonzero
coefficient has a character nontrivial on $U_p(K)$.

For such a character, represent its $p$-coordinate as
$x_p\mapsto\exp(2\pi i b[x_p]_{p^k}/p^k)$, with $p\nmid b$.
Nontriviality on $U_p(K)$ forces $k>K$. When $k>\nu_p$, this high
conductor cannot be removed by changing the finite-coordinate part:
its restriction to $U_p(\nu_p)$ has conductor $p^{k-\nu_p}$.
In particular, the nonzero Fourier coefficients have unbounded such
$k$ in this one fixed class $C$ and prime $p$.

### Step 4. Unit invariance produces dense grids of nonzero coefficients

Set $\kappa=\max(1,\nu_p)$. For any $p$-adic unit
$v\equiv1\pmod{p^\kappa}$, define $\alpha_v:D\to D$ by
multiplying only $x_p$ by $v$ and leaving the other coordinates,
including $a$, unchanged. Formula (1) shows that this is a continuous
group automorphism. Every radial factor is unchanged, so
$q_C\circ\alpha_v=q_C$.
Haar probability is invariant under a compact-group automorphism;
a change of variables in the defining Fourier integral gives
$$
\tag{7}
\widehat q_C(\chi\circ\alpha_v)=\widehat q_C(\chi).
$$

Take a nonzero coefficient with $p$-conductor $p^k$, where
$k>\kappa$, as in Step 3. Use the units
$v=1+p^\kappa t$ for $0\leq t<p^{k-\kappa}$. Its frequency at
the diagonal generator changes by
$$
\tag{8}
(\chi\circ\alpha_v)(g_0)
=\chi(g_0)\exp(2\pi i b t/p^{k-\kappa}).
$$
Since $p\nmid b$, these are all points of one rotated full grid of
$p^{k-\kappa}$ equally spaced roots of unity, and (7) gives the same
nonzero coefficient at each. The points are distinct, and hence so
are their characters by injectivity of generator evaluation.
The possible $k$ are unbounded. Every nonempty open arc therefore
contains a nonzero Fourier frequency from this class: choose a grid
whose spacing is smaller than the arc length.

This step uses more than the existence of infinitely many coefficients.
Infinitely many arbitrary frequencies need not be dense. The full unit
orbit in (8) is what supplies density.

### Step 5. The actual coefficient measure has no remaining phase collision

Evaluating (4) on $ng_0$ and undoing the phase grouping gives
$$
\tag{9}
a_n=\sum_C\rho_C^n q_C(ng_0)
=\sum_C\sum_\chi\widehat q_C(\chi)
                     (\rho_C\chi(g_0))^n.
$$
Define
$$
\tag{10}
\mu=\sum_C\sum_\chi\widehat q_C(\chi)
                       \delta_{\rho_C\chi(g_0)}.
$$
Its total variation is finite by (5). Within one class, generator
evaluation is injective. Between distinct classes, an equality
$\rho_C\chi(g_0)=\rho_{C'}\chi'(g_0)$ would imply that
$\rho_C/\rho_{C'}$ is a root of unity, contrary to the class
construction. Thus (10) is already the aggregated actual measure:
every displayed nonzero Fourier coefficient is a nonzero atomic mass.
In particular Step 4 gives a dense set of its nonzero atoms.

### Step 6. Radial passage and the natural boundary

Absolute summability permits interchange of the geometric series with
the finite-variation measure, giving
$$
\tag{11}
F(z)=\int\frac{\xi z}{1-\xi z}\,d\mu(\xi),\qquad |z|<1.
$$
For any fixed $\xi_0$ on the circle,
$$
\left|(1-r)\frac{r\xi\xi_0^{-1}}{1-r\xi\xi_0^{-1}}\right|
\leq r\leq1,
$$
because $|1-r\xi\xi_0^{-1}|\geq1-r$. The expression tends to
one when $\xi=\xi_0$, and to zero otherwise. Dominated convergence
with respect to $|\mu|$ proves (RL).

At every nonzero atom this limit excludes a holomorphic extension of
$F$ at the corresponding inverse point: a function holomorphic there
is locally bounded and would have zero limit after multiplication by
$1-r$. Since these inverse atom points are dense, no open boundary arc
can admit holomorphic continuation. Meromorphic continuation is also
excluded. In a neighborhood where such a continuation existed, each
nonzero atom point would have to be a pole, but poles of a meromorphic
function are discrete and cannot be dense in a nonempty arc inside that
neighborhood. This proves the asserted natural boundary.

### Step 7. The rational alternative

Suppose (AF) fails. On a fibre over $a$, either $b_C(a)=0$ and
$q_C$ is zero, or every active coordinate satisfies
$a\not\equiv0\pmod{p^{\nu_p}}$. In the latter case its valuation is
constant on that coordinate ball, equal to the valuation of the residue
representative below $\nu_p$. Inactive coordinates have constant
kernel one. Hence $q_C$ is constant on every fibre and depends only on
$a$. Write this value as $d_C(a)$, with residue zero represented by $W$.
Then
$$
\tag{12}
F(z)=\sum_C
\frac{\displaystyle\sum_{a=1}^{W}d_C(a)(\rho_Cz)^a}
     {1-(\rho_Cz)^W},
$$
which is rational. The empty phase sum or prime set is included in
this calculation. This completes Theorem 1. $\square$

## Corollary 2: the FAD natural boundary without hyperbolicity

Let $(X,f)$ be a confined FAD system with positive entropy
$\log\Lambda>0$ and fixed-point counts
$$
\tag{13}
f_n=|\det(A^n-I)|c^n r_n
\prod_{p\in S}|n|_p^{s_{p,n}}p^{-t_{p,n}|n|_p^{-1}}.
$$
Use exactly BCH Definition 7.1.1–7.1.2: $A$ is integral, $c>0$,
$(r_n)$ is a positive real gcd sequence, and $(s_{p,n}),(t_{p,n})$
are nonnegative real gcd sequences of periods coprime to $p$.
Discard inactive primes. If at least one prime remains, both
$$
Z_f(z)=\sum_{n\geq1}f_nz^n,
\qquad
\zeta_f(z)=\exp\left(\sum_{n\geq1}f_n\frac{z^n}{n}\right)
$$
have the circle $|z|=\Lambda^{-1}$ as a natural boundary, with no
meromorphic continuation through any point of that circle.

### Proof

The classical multiplicative-part expansion is
$$
|\det(A^n-I)|c^n=\Lambda^n u_n+O((\Lambda\tau)^n),\qquad 0\leq\tau<1,
$$
where $u_n$ is a finite sum of unit-modulus phases and is strictly
positive for every positive integer $n$. These facts are given in BCH
Section 10.3, especially (10.4)–(10.8) and Lemma 10.3.10. They do not
require hyperbolicity. To make the relevant positivity transparent,
the unit-circle eigenvalues of an integral real matrix occur in
conjugate pairs. Their contribution is a product of factors
$2-\eta^n-\eta^{-n}=|1-\eta^n|^2>0$, because no such eigenvalue is
a root of unity in the nonzero confined case. Off the unit circle,
the normalized factors tend to one exponentially. This gives the
displayed expansion and positivity directly as well.

The exclusion of a root-of-unity eigenvalue is also forced by
realizability when the fixed-count sequence is nonzero: if one eigenvalue
has order $h$, then $f_n=0$ at every multiple of $h$. Any positive
$f_m$ would give a periodic point also fixed by $f^{hm}$, a
contradiction. The identically zero sequence has no positive counting
entropy and is outside the stated hypothesis.

Apply Theorem 1 to the dominant phase sum $u_n$ and the radial factor
in (13). Fix an active prime $p$ and an active exponent residue
$n_0\bmod m_p$, where $m_p$ is a common exponent period coprime to
$p$. Form $W$ as in that theorem. CRT supplies a residue $a\bmod W$
with
$$
a\equiv0\pmod{p^{\nu_p}},\qquad a\equiv n_0\pmod{m_p}.
$$
The exponent pair at $a$ is active. If $b_C(a)$ were zero for every
phase class, positivity of $r_a$ would make every corresponding
periodic phase sum zero. Then $u_n$ would vanish for every positive
$n\equiv a\pmod W$, contradicting its strict positivity. Therefore
(AF) holds for at least one phase class at this same residue and prime.

It follows that the dominant normalized series has the unit circle as
a natural boundary, with dense nonzero radial residues. The subdominant
error contributes a function holomorphic in a disc of radius greater
than one, since the radial factors and $r_n$ are uniformly bounded.
It neither changes (RL) nor removes the dense boundary singularities.
Rescaling gives the assertion for $Z_f$ at radius $\Lambda^{-1}$.

Finally, inside this disc,
$$
\tag{14}
z\frac{\zeta_f'(z)}{\zeta_f(z)}=Z_f(z).
$$
If $\zeta_f$ admitted meromorphic continuation through any boundary
point, it would not be identically zero there, because it agrees with
its nonvanishing exponential on the interior. Its zeros and poles in
that neighborhood would be discrete. Choose a smaller boundary arc
and a neighborhood avoiding them. Equation (14) would give
holomorphic continuation of $Z_f$ across that arc, contrary to the
dense radial singularities already proved. The defining exponential
is holomorphic inside $|z|<\Lambda^{-1}$, so this is exactly its
circle of convergence and natural boundary. $\square$

The root-rational classification in BCH Theorem 11.3.4 is classical
input, not reproved or counted as new here. Together with that result,
Corollary 2 gives the alternative requested in their Problem 14.1.2
for the checked 2024 public version.

## Decisive scope tests

1. **Coincident phases can remove every active fibre.** Take $S=\{2\}$,
   $r_n=1$, $s_{2,n}=1$, $t_{2,n}=0$, and $u_n=1-(-1)^n$.
   On odd $n$ the radial factor is one, and on even $n$ the phase
   weight is zero. Thus
   $$F(z)=2z/(1-z^2).$$
   The phases belong to one torsion class, $W=2$, and its grouped
   coefficient vanishes at the sole residue with unbounded $2$-adic
   valuation. Hence (AF) fails exactly as it should. An argument merely
   adding natural-boundary component series would give a false answer.
2. **An active fibre need not have positive grouped coefficients.**
   The proof only requires $b_C(a)\neq0$, not a sign. Possible signed
   cancellations are already resolved in the grouping and Fourier
   coefficient collection, before the atomic measure is used.
3. **A nonzero atom alone does not give a natural boundary.** The proof
   explicitly uses the arbitrarily fine grids from (8); infinite or
   unbounded-conductor support without the unit invariance would not
   justify the conclusion.
4. **The FAD gcd/coprime hypotheses have a precise role.** Positivity of
   the normalized leading phase sum and coprimality of each exponent
   period force (AF). The abstract classification itself does not need
   those hypotheses and records the rational masked cases rather than
   incorrectly excluding them.

## Corrections or missing assumptions

No claimed no-cancellation result applies to arbitrary sums of functions
that individually have natural boundaries. The torsion-class grouping,
absolute Fourier summability, radial unit invariance, and active-fibre
criterion are all part of the proved mechanism. No conclusion for
infinitely many distortion primes is made.

## Open risks and ownership boundary

- Independent review must check (7)–(10), especially invariance on the
  congruence subgroup and injectivity/noncollision of actual atoms.
- The final EMS revision of BCH was not obtained in the preceding
  batch; a new bounded 2026 source check is being recorded separately.
  This proof is not itself evidence that the worldwide problem remains
  open or that the argument has not appeared elsewhere.
- The result concerns source dynamical zeta functions and native orbit
  counts. It supplies no target Euler factor, root number, target zero
  correspondence, automorphy statement, or Hilbert–Pólya realization.
- C407's Cantor/cover theorem is not used. Its adaptive cover and
  positive translated-kernel nonconstancy argument do not imply this
  analytic continuation criterion. The elementary single-center radial
  expansion shared by the arguments is deducted as an input technique,
  not promoted into a separate result.
