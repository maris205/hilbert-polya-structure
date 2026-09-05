# C390 proof: positive-real Lyness dynamics and the rational torsion boundary

## Claim, assumptions and status

Status: **PROVABLE AS STATED WITH EXPLICIT CLASSICAL INPUTS**.
Fix $a>0$ and the discrete-time source
$$F_a(x,y)=(y,(a+y)/x),\qquad Q=(0,\infty)^2.$$
All real conclusions below refer to this autonomous map on $Q$, not to a
periodically forced Lyness equation, a finite-field totalization, or a map on
the whole projective plane. Rational conclusions additionally require
$a,x,y\in\mathbb Q_{>0}$. A period always means a **least positive iterate
period**, unless an iterate is explicitly specified; a prime period means that
this integer is a rational prime only when the word "prime integer" is used.

The complete source contract is: every point is the unique center or lies on a
unique compact regular oval; every oval map is an explicitly normalized Abel
rotation; rational and irrational rotations give all periodic and dense oval
orbits, respectively; all repetitions and return multipliers follow from an
exact shear formula. For $a\ne1$, every sufficiently large prime integer occurs
as a real least period, whereas rational periodic points have only periods
$1,5,9$. Five occurs only at $a=1$; nine does not occur at every rational $a$.
The ordinary real orbit-cardinality zeta is undefined. A finite invariant
annulus has a native Koopman unitary, not a target quantum operator.

## Classical inputs and dependency map

1. **BR endpoints.** Bastien--Rogalski, *Global Behavior of the Solutions of
   Lyness' Difference Equation*, J. Difference Equations Appl. 10 (2004),
   977--1003, DOI 10.1080/10236190410001728104, Propositions 6 and 7:
   the clockwise oval rotation has limits $1/5$ at infinite energy and
   $\rho_0(a)=(2\pi)^{-1}\arccos(1/(2\ell))$ at the center, where
   $\ell=(1+\sqrt{1+4a})/2$. We invoke these two endpoint theorems, not their
   proofs, and do not claim a new endpoint calculation.
2. **GMX positive rational classification.** Gasull--Mañosa--Xarles,
   *Rational periodic sequences for the Lyness recurrence*, Discrete Contin.
   Dyn. Syst. 32 (2012), 587--604, DOI 10.3934/dcds.2012.32.587;
   arXiv:1004.5511v1, Introduction and Sections 2--4: positive rational
   parameters and positive rational periodic points have least periods only
   $1,5,9$. The period-nine example at $a=7$ below is theirs. This is an
   expressly external classification, not inferred from our finite grid.
3. **Mazur torsion theorem.** A rational point on an elliptic curve over
   $\mathbb Q$ has finite order only in $\{1,\ldots,10,12\}$. The deep
   theorem is credited to Mazur, *Modular curves and the Eisenstein ideal*,
   Publ. Math. IHÉS 47 (1977), 33--186. We explain the reduction to it, but
   do not purport to reprove it or the sharper positive-coordinate exclusion.
4. Elementary smooth plane cubic group law, extension of birational maps
   between smooth projective curves, and the genus-one involution law with
   a fixed point are standard algebraic-geometry inputs. The translation
   identification is also explicitly given in GMX Section 2.1.

The all-oval geometry, integral normalization, return matrices, rational
versus real prime-period contrast, finite-annulus spectral consequences and
cardinality obstruction are derived below. Beukers--Cushman's 1998
monotonicity theorem is a positive prior owner, but **no global monotonicity
or everywhere nonzero derivative assumption is needed by this package**.

## 1. Global map, invariant geometry and exhaustion

Put
$$H_a(x,y)=\frac{(x+1)(y+1)(x+y+a)}{xy},\qquad
\omega=\frac{dx\wedge dy}{xy},\qquad R(x,y)=(y,x).$$
Substitution gives $F_a^{-1}(x,y)=((a+x)/y,x)$,
$R F_a R=F_a^{-1}$ and $H_a\circ F_a=H_a$. Its Jacobian is
$$D F_a(x,y)=\begin{pmatrix}0&1\\-(a+y)/x^2&1/x\end{pmatrix},
\qquad\det D F_a=(a+y)/x^2>0.$$
The determinant is **not** one in Cartesian coordinates. Dividing by the
new coordinate product $y(a+y)/x$ proves $F_a^*\omega=\omega$;
$R^*\omega=-\omega$. Positivity of every forward and backward coordinate
proves that $F_a$ is a global analytic diffeomorphism of $Q$.

In logarithmic coordinates $(u,v)=(\log x,\log y)$, the integral is
$$K_a=e^u+e^v+e^{u-v}+e^{v-u}
+(a+1)(e^{-u}+e^{-v})+a e^{-u-v}+a+2.$$
Its Hessian is a sum of positive multiples of outer products of the exponent
vectors. The terms $e^u$ and $e^v$ already span $\mathbb R^2$, so that
Hessian is positive definite at every point. The four terms
$e^u,e^v,(a+1)e^{-u},(a+1)e^{-v}$ show $K_a\to\infty$ as
$|(u,v)|\to\infty$. Therefore $K_a$ has exactly one critical point, its
nondegenerate global minimum. Symmetry forces $u=v$ there; along the
diagonal the derivative is
$$\frac{d}{dr}H_a(r,r)=\frac{2(r+1)(r^2-r-a)}{r^3}.$$
Consequently the critical point is $c_a=(\ell,\ell)$ and
$$h_*:=H_a(c_a)=(\ell+1)^3/\ell.$$
For every $h>h_*$, each ray from the minimum in log coordinates meets
$K_a=h$ once: its derivative starts at zero and is strictly increasing,
and its value tends to infinity. The implicit function theorem gives a
smooth closed radial graph. Thus $C^+_{a,h}=Q\cap\{H_a=h\}$ is exactly one
analytic oval. There are no other positive components, no positive
separatrices and no positive escape orbits. Each two-sided orbit remains
in its compact oval, at a positive distance from the coordinate axes.
The single center is the whole positive fiber at $h=h_*$.

## 2. Smooth elliptic curves and excluded singular fibers

The projective cubic is
$$P_{a,h}(X,Y,Z)=(X+Z)(Y+Z)(X+Y+aZ)-hXYZ=0.$$
For affine $x$, write its quadratic in $y$ as
$$P_{a,h}(x,y,1)=(x+1)y^2+B(x)y+(x+1)(x+a),
\quad B(x)=(x+1)(x+a+1)-hx.$$
Its discriminant is
$$D(x)=B(x)^2-4(x+1)^2(x+a).$$
Direct polynomial elimination gives
$$\operatorname{disc}_x D=256h^3(a-h-1)^2\,a(h-h_+)(h-h_-),$$
where
$$h_\pm=\frac{2a^2+10a-1\pm(4a+1)\sqrt{4a+1}}{2a},
\qquad h_+=h_*.$$
One can verify the elimination by expanding the quartic and its Sylvester
determinant; the exact symbolic audit independently performs that check.
For $h>h_*$, $h>0$, $h>a-1$ and $h>h_-$, so the discriminant is nonzero.
For example $h_*>a+2$ follows on substituting $a=\ell^2-\ell$, since
$h_*-a-2=4\ell+1+1/\ell>0$.
An affine singular point with $x\ne-1$ would give a repeated root of $D$.
At $x=-1$, the cubic forces $y=0$ when $h\ne0$, and $P_y=h\ne0$.
At infinity the three points $[1:-1:0],[1:0:0],[0:1:0]$ have a nonzero
partial derivative. Hence the cubic is smooth over $\mathbb C$ for every
positive regular energy. A smooth projective plane cubic has genus one.

The possible singular energies $0,a-1,h_\pm$ are therefore never met by a
noncentral positive orbit. We do not apply an elliptic torsion theorem to
the singular center fiber. We also do not extend the positive classification
to the excluded real/projective components of these fibers.

## 3. Abel rotation with a fixed discrete clock

Use the Hamiltonian vector field defined by $\iota_{X_H}\omega=dH$:
$$X_H=xy(H_y\partial_x-H_x\partial_y).$$
Its flow is an auxiliary parametrization, not a replacement for the unit
iterate clock of $F_a$. It is nonzero on each regular oval and complete on
that compact oval. Preservation of both $H$ and $\omega$ implies
$D F_a X_H=X_H\circ F_a$, so $F_a$ commutes with this flow.

For each $h>h_*$ let $r>\ell$ be the unique upper diagonal intersection,
$H_a(r,r)=h$, and put $p_h=(r,r)$. Let $\alpha$ and $\beta$ denote the
minimum and maximum $x$ coordinates on the positive oval. Vertical slices
of the strictly convex log sublevel set are intervals; their two boundaries
give the positive upper and lower roots of the quadratic above.
The two turning points are simple because $D$ has no multiple roots.
On the upper arc, $\dot x=P_y=\sqrt{D(x)}$; on the lower arc,
$\dot x=-\sqrt{D(x)}$. The full auxiliary flow period is therefore
$$T_a(h)=2\int_\alpha^\beta\frac{dx}{\sqrt{D(x)}}.$$
At $x=r$ the two positive roots are $r$ and $(a+r)/r<r$, so
$F_a(p_h)$ is the lower point on the same vertical line. The forward
clockwise flow from $p_h$ reaches it by going through $\beta$, giving
$$\tau_a(h)=2\int_r^\beta\frac{dx}{\sqrt{D(x)}},\qquad
\rho_a(h)=\frac{\tau_a(h)}{T_a(h)}\in(0,1).$$
This explicit arc choice removes the modulo-one and reversal ambiguity.
In fact the arc is shorter than half the orbit, but that sharper bound is
not needed here. The integrable endpoint square-root singularities can be
removed locally by the substitution $x=\alpha+(\beta-\alpha)\sin^2 t$;
analytic dependence on $h$ follows on each compact regular energy interval.
Thus $T,\tau,\rho$ are real analytic on $(h_*,\infty)$.

Define $\theta\in\mathbb R/\mathbb Z$ by elapsed positive $X_H$ time from
$p_h$, divided by $T_a(h)$. The section $p_h$ is analytic, hence these are
smooth coordinates on any regular energy annulus, and
$$F_a(h,\theta)=(h,\theta+\rho_a(h)),\qquad
R(h,\theta)=(h,-\theta).$$
The second formula follows because $R$ fixes $p_h$ and reverses $X_H$.
Also $\omega=T_a(h)\,d\theta\wedge dh$. In particular, the mass of a
compact regular annulus $h\in[h_1,h_2]$ is
$\int_{h_1}^{h_2}T_a(h)\,dh$, finite and positive.

## 4. All periods, repetitions, stability and real prime integers

The rotation coordinate proves a complete pointwise classification.
If $\rho_a(h)=m/n$ with $\gcd(m,n)=1$, **every** point of that oval has
least period $n$, and its orbit contains exactly $n$ points. Its distinct
primitive orbits are parametrized by $\mathbb R/((1/n)\mathbb Z)$, hence
uncountably many. If $\rho_a(h)$ is irrational, every forward and backward
orbit is dense in that oval; it is not dense in the whole quadrant.
For every positive integer $N$ the entire fixed set is exactly
$$\operatorname{Fix}(F_a^N)=\{c_a\}\ \cup\!!!
\bigcup_{\substack{h>h_*\\N\rho_a(h)\in\mathbb Z}} C^+_{a,h}.$$
No count from a finite search replaces this formula.

At an $n$-periodic oval, the return derivative in $(h,\theta)$ is
$$D F_a^n=\begin{pmatrix}1&0\\n\rho_a'(h)&1\end{pmatrix}.$$
For repetition $k$ it has the same form with $kn$; both multipliers are
one and its nilpotent part squares to zero. Cartesian monodromy is
conjugate to this matrix at a return point. A nonzero shear is claimed
only if $\rho_a'(h)\ne0$. If that derivative vanishes the first derivative
of the return is identity; higher-order terms are not silently discarded.
At the center the one-step derivative has characteristic polynomial
$$\lambda^2-\ell^{-1}\lambda+1,$$
so its eigenvalues are $e^{\pm2\pi i\rho_0(a)}$. The center is Lyapunov
stable by the strict minimum of $H$, but no asymptotic stability is claimed.

The two explicitly imported BR endpoint limits give
$$\lim_{h\downarrow h_*}\rho_a(h)=\rho_0(a),\qquad
\lim_{h\to\infty}\rho_a(h)=1/5.$$
Here $\ell>1$, so $1/6<\rho_0(a)<1/4$ and $\rho_0(a)=1/5$ exactly at
$a=1$. For $a\ne1$, $\rho$ is analytic and nonconstant, and the open
interval $J_a$ between these two endpoints is contained in its image by
the intermediate value theorem. Equality of the image with $J_a$, global
monotonicity, uniqueness of an energy with a prescribed rotation and
everywhere nonzero twist are **not claimed**.

Choose any rational interval $(s,t)\subset J_a$. For every prime integer
$p>1/(t-s)$, $(ps,pt)$ has length greater than one and contains an integer
$m$. Since $0<s<t<1$, $1\le m\le p-1$, and $\gcd(m,p)=1$.
Some finite regular energy has rotation $m/p$, proving an entire oval of
least period $p$. Thus real least periods include every sufficiently
large prime integer for each fixed $a>0$, $a\ne1$. This conclusion needs
neither prime-number asymptotics nor a numerical rotation fit. Analytic
nonconstancy also implies that the zero set of $\rho'$ is discrete and
that both rational-rotation ovals and irrational-rotation ovals are dense
in the foliation. It does not identify a specific rational rotation as
a noncritical energy without a separate check.

## 5. The exceptional five-periodic parameter

Direct symbolic iteration at $a=1$ gives $F_1^5=I$ on $Q$. Since $5$ is
prime and $F_1$ has exactly one fixed point, all its other points have
least period five. The continuous real-valued rotation is therefore
constant; the center endpoint fixes the constant as $1/5$.

Conversely, suppose $a\ne1$ and $F_a^5(x,y)=(x,y)$ in $Q$. Removing
strictly positive denominators and the factor $a-1$ from the two coordinate
equations gives
$$p=a x-a y+a-y^2+y=0,$$
$$q=-a^2x-a^2+a x^2y+a x^2-a xy+a x-2ay+xy-y^2=0.$$
The first equation gives $x=(a+y)(y-1)/a$. Substitution in the second is
$$q=\frac{y(a+y)^2}{a}\,(y^2-y-a).$$
Hence $y^2-y-a=0$, positivity gives $y=\ell$, and the first equation gives
$x=\ell$. There is no noncentral five-periodic positive oval at $a\ne1$.
The boundary $a=0$ is deliberately excluded: its map is globally
six-periodic, so the nonconstant-rotation argument must not be extended
to $a=0$. The axes and infinity are not states in $Q$.

## 6. Elliptic translation and the rational obstruction

On every smooth cubic from Section 2, take $O=[1:-1:0]$ as identity and
$Q_0=[1:0:0]$. The tangent at $O$ is $X+Y=(h-a)Z$; its substitution
into $P_{a,h}$ gives $h(h-a+1)Z^3$. Thus $O$ is a flex in every regular
positive energy. The swap $R$ fixes $O$, reverses the holomorphic
differential and acts as negation in this group law.

The other involution $J(x,y)=((a+y)/x,y)$ has fixed points over the smooth
complex cubic and is not a fixed-point-free translation by two-torsion.
For completeness a fixed point follows from $x^2=a+y$: substituting
$y=x^2-a$ into the cubic gives a nonconstant polynomial with a complex
root on its projective closure; the induced degree-two projection to the
$y$ line also has branch points by Riemann--Hurwitz. An involution of an
elliptic curve with a fixed point is $P\mapsto B-P$.
Here $J(O)=[0:1:0]=-Q_0$ (evaluate in a local chart, or use the tangent
extension of the displayed rational map). Since $F_a=R\circ J$, this gives
$$F_a(P)=P+Q_0.$$
This translation identity agrees with GMX Section 2.1. It holds on the
smooth projective curve after resolving the displayed rational coordinate
formula, not by declaring its base points to be ordinary affine states.

When $a,x,y\in\mathbb Q_{>0}$ and the point is not the center,
$h=H_a(x,y)\in\mathbb Q$, and Section 2 proves that the cubic is smooth.
The point $Q_0$ and group law are defined over $\mathbb Q$. Thus
$$F_a^n(P)=P\quad\Longleftrightarrow\quad nQ_0=O,$$
and a finite least orbit period equals the order of this **translation
point**, not the order of the starting point $P$. Mazur restricts this
order to $1,\ldots,10,12$. The sharper positive-coordinate classification
in GMX restricts it to $5$ or $9$, after the center is removed. We cite
that sharper exclusion as an external theorem, rather than pretending
that Mazur alone proves it. A rational fixed point exists exactly when
$a=r(r-1)$ for some rational $r>1$, and is then $(r,r)$.

An exact positive rational nine-cycle, from GMX, is specified by successive
scalar coordinates
$$3/2,\ 5/7,\ 36/7,\ 17,\ 14/3,\ 35/51,\ 28/17,\ 63/5,\ 119/10.$$
Adjacent cyclic pairs obey $x_{j+2}x_j=x_{j+1}+7$. Their distinctness
proves least period nine. Its energy is $258/7$; the exact checker verifies
that value and the complete return matrix. Existence at $a=7$ does not
imply existence at every $a$, nor does a rational energy imply that its
positive oval has a rational point. In particular, the starting points
in this example are not being classified as elliptic nine-torsion.

For any fixed rational $a>0$, $a\ne1$, Section 4 gives real periodic
ovals with every sufficiently large prime-integer period. None contains
a rational point once that prime is at least eleven, by the rational
classification. Thus enlarging the real source ledger cannot manufacture
a rational prime-bearing periodic ledger. No target prime factor or
local arithmetic datum has entered this argument.

## 7. Ordinary cardinality zeta and the finite-annulus operator

For $a=1$, $\operatorname{Fix}(F_1^5)=Q$ is uncountable. For $a\ne1$,
Section 4 supplies a rational-rotation oval, so at some positive iterate
the fixed set is uncountable. Therefore
$$\exp\left(\sum_{n\ge1}\#\operatorname{Fix}(F_a^n)\,z^n/n\right)$$
is not an ordinary formal power series with finite coefficients for any
$a>0$. This obstruction concerns this particular real point-cardinality
definition, not measured, family-weighted, cohomological or regularized
zeta constructions.

On a chosen compact regular annulus $A=[h_1,h_2]\times\mathbb R/\mathbb Z$,
normalize the finite invariant measure $T_a(h)\,dh\,d\theta$ to mass one.
The full-quadrant measure is not asserted to be finite. Define $Uf=f\circ F_a$
on this $L^2$ space. The Fourier decomposition in $\theta$ is
$$L^2(A)=\bigoplus_{k\in\mathbb Z}L^2([h_1,h_2],T_a(h)dh),\quad
U_k g(h)=e^{2\pi i k\rho_a(h)}g(h).$$
This proves unitarity. The radial summand $k=0$ consists of eigenvectors
with eigenvalue one and is infinite-dimensional; hence $U$ is noncompact
and not Schatten-class of any finite order.
For $a\ne1$, analyticity and nonconstancy imply that every level set of
$e^{2\pi i k\rho}$ for $k\ne0$ has measure zero; these summands have no
eigenvectors. On subintervals avoiding the discrete critical set the
multiplier is a smooth local change of variable, so their spectral measures
are absolutely continuous; the critical set itself has measure zero.
Finally $\rho([h_1,h_2])$ contains an interval of positive length; choose
$|k|$ whose multiplied interval has length at least one. Then the essential
range of $e^{2\pi i k\rho}$ is the whole unit circle. Consequently
$$\sigma(U)=S^1,\qquad\sigma_{\mathrm{point}}(U)=\{1\}\quad(a\ne1).$$
For $a=1$, $U^5=I$ and its five fifth-root eigenvalues all have infinite
multiplicity, reproducing the exceptional source without confusing it
with the generic continuous spectral part. This native Koopman construction
does not furnish a distinguished self-adjoint generator with the target
spectrum, and does not upgrade A4 beyond a formal hint.

## Corrections, scope and residual risk

This is **OWNER_HEAVY / classical source-local reconstruction**, not a
literature-priority claim. BR endpoints, GMX rational classification, Mazur
torsion and elementary genus-one facts are explicit dependencies. The
finite exact ledger only tests source identities and certificate handling;
it neither proves a universal classification nor certifies numerical
quadrature. No global monotonicity, uniformly nonzero twist, finite ordinary
cardinality determinant, or target quantum realization is asserted.

Strict tuple:
$(A0\_WEAK\_ARITHMETIC\_RELATION,A1\_WEAK,A2\_FAIL,A3\_FAIL,A4\_FORMAL\_HINT)$.
Overall: `ROUTE_A_REJECTED`. Firewall: `NO_BAD_EULER_OR_ROOT_NUMBER`.
All nine target/Route-B flags are false. Route B remains disabled.
