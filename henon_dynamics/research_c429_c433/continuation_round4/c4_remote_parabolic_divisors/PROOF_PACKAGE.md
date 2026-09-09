# R4 proof package: slice cusps and a paired-unfolding bridge

2026-09-09. All calculations are by hand. The accepted R3 package is
read-only. This package does not claim SF2.

## 0. Claim, assumptions, status and dependency map

The original question remains: for the native map $T=s_zs_ys_x$ on
$$
x^2+y^2+z^2-xyz-Ax-By-Cz=D,
$$
is every ordinary exact-period-$n$ splitting field, $n\ge3$,
unramified at the generic point of the accepted irreducible smooth-fold
divisor $\mathscr F$?

**SF2 status: NOT CURRENTLY JUSTIFIED.** The following local results
are proved, and the proposed sufficient global bridge is explicitly
conditional. No distinct-period transversality assertion is inferred
from dimension or genericity.

The inputs are the accepted rational cycle map
$$
\Phi(q,X,Y,Z)=(X-qYZ,Y-qXZ,Z-qXY,
q(XYZ-X^2-Y^2-Z^2)),
\tag{1}
$$
the geometric irreducibility of its critical hypersurface and image
$\mathscr F$, and R3's finite-flat/no-escape and period-two isolation
theorems. The parameters belong to characteristic zero; analytic
arguments below are made after an embedding in $\mathbb C$.

Strategy and dependencies:

1. Compute the germ of (1) on the explicit subfamily
   $A=B=0,D=-C$. This identifies the candidate witness curve precisely.
2. Derive the conormal of the generic marked two-cycle fold from (1).
3. Derive a coordinate-independent remote-fold unfolding covector
   from a periodic return and its parameter variation.
4. State exactly what independence of these covectors would imply,
   and separate satellite and higher-degeneracy strata which the
   simple-fold test does not cover.

Steps 1–3 are elementary local calculations, not a proof of the
all-period independence needed in Step 4. Source applicability is
recorded in REPORT.md; the closest retrieved theorems do not supply
that missing relative statement.

## 1. The $D=-C$ slice is generically a cusp of the cycle map

Fix $c\in\mathbb C\setminus\{0,3,4,-4/3\}$. Consider
$$
\xi_c=(q,X,Y,Z)=(1/c,0,0,c),\qquad
\Phi(\xi_c)=(0,0,c,-c).
\tag{2}
$$
This point lies on the critical hypersurface of (1), hence its image
lies on the accepted global divisor $\mathscr F$.

Introduce source and target coordinates
$$
s=(X+Y)/2,\quad h=(X-Y)/2,\qquad
a=(A+B)/2,\quad b=(A-B)/2,
$$
and write the remaining target coordinates as $C$ and $t=D+C$.
The equations of (1) become
$$
\begin{aligned}
a&=s(1-qZ),& b&=h(1+qZ),\\
C&=Z-q(s^2-h^2),\qquad&
D&=q\bigl((s^2-h^2)Z-2(s^2+h^2)-Z^2\bigr).
\end{aligned}
\tag{3}
$$
At (2), the derivative of $(b,C,D)$ with respect to $(h,Z,q)$
is invertible: its diagonal blocks are $2$ and
$$
\begin{pmatrix}1&0\\-2&-c^2\end{pmatrix}.
$$
The implicit-function theorem therefore solves $h,Z,q$ as functions
of $(s,b,C,t)$ near $(0,0,c,0)$. Thus the local map is equivalent to
$$
(s,b,C,t)\longmapsto
\bigl(a=F(s,b,C,t),\ b,C,t\bigr).
\tag{4}
$$

When $b=0$, equation (3) gives $h=0$. First put $C=c,t=0$.
The solutions for $q,Z$ are even in $s$. Write
$$
q=\frac1c+q_2s^2+O(s^4),\qquad
Z=c+\frac{s^2}{c}+O(s^4).
$$
Using $D=-c$ in (3), the coefficient of $s^2$ is
$-c^2q_2+(c-4)/c$, so
$$
q_2=\frac{c-4}{c^3},\qquad
qZ=1+\frac{c-3}{c^2}s^2+O(s^4).
$$
Consequently
$$
F(s,0,c,0)=-\frac{c-3}{c^2}s^3+O(s^5).
\tag{5}
$$
For $s=b=0$ and variable $t$, equations (3) give
$Z=c$ and $q=(c-t)/c^2$ exactly. Since the equations for $q,Z$
are even in $s$ when $b=0$, this yields
$$
F_s(0,0,c,t)=\frac{t}{c},\qquad
F(s,0,c,t)=\frac{t}{c}s-\frac{c-3}{c^2}s^3
+O(ts^3,s^5).
\tag{6}
$$
The nonzero derivatives needed below are thus
$$
F_{sss}(0,0,c,0)=-\frac{6(c-3)}{c^2}\ne0,
\qquad F_{st}(0,0,c,0)=\frac1c\ne0.
\tag{7}
$$

**Proposition 1.1 (ordinary cycle-map cusp).** Near $\xi_c$, the
finite local cycle map (1) is analytically equivalent to a depressed
cubic family
$$
w^3+u w+v=0
\tag{8}
$$
over coordinates $(u,v)$ and two passive parameters. Its local branch
image is the cusp $4u^3+27v^2=0$. In particular the image point is
not a simple-fold point of this local map.

**Proof.** Apply Weierstrass preparation to $F(s,b,C,t)-a$ at
$(s,a,b,C,t)=(0,0,0,c,0)$. By (5), its order in $s$ is exactly three.
After multiplication by an invertible function it is a monic cubic in
$s$ with analytic parameter coefficients. A shift removes the
quadratic coefficient. At the central point, the derivative of its
constant coefficient with respect to $a$ is nonzero. Its linear
coefficient has nonzero derivative with respect to $t$, by (6), while
the constant coefficient is identically zero on $a=b=0$ before that
shift and has zero first $t$ derivative afterwards. Thus the two
depressed-cubic coefficients are independent target coordinates near
the central point. This proves (8). Eliminating $w$ from (8) and
$3w^2+u=0$ gives $4u^3+27v^2=0$. $\square$

The cusp is a local branch of the same global divisor $\mathscr F$;
this assertion uses its accepted global identification, not a new
divisor defined by restricting a discriminant to a line.

### Smoothness and exact-period exclusions

At $A=B=0,D=-C$, a singular point must satisfy
$$
2x-yz=0,\qquad2y-xz=0,\qquad2z-xy-C=0.
$$
If $x=y=0$, then $z=C/2$ and $C(C-4)=0$. If $x,y\ne0$, the
first two equations give $z=2,y=x$ or $z=-2,y=-x$.
The first option yields $C=4$ on this level; the second yields
$C=-4/3$, with $x^2=8/3$. If exactly one of $x,y$ vanishes the
first two equations force the other to vanish, already covered.
Thus the smooth-fibre exclusions are precisely $C=0,4,-4/3$.
The additional exclusion $C=3$ in Proposition 1.1 concerns the
vanishing cubic coefficient, not a singular surface.

The phase discriminant of the cycle map is $1-4/c\ne0$. Hence the
two ordered phases over (2) are distinct native period-two points,
and the phase cover does not change the local cusp calculation.
Their fixed-scheme tangent has dimension one and the $T^2$ return
is unipotent, by the invariant two-form as in accepted R3.
The iterate-ideal lemma therefore still isolates these particular
germs from all higher native periods. That does not control remote
points on this slice.

For $\varepsilon\in\{1,-1\}$, the even sign change
$(X,Y,Z)\mapsto(X,\varepsilon Y,\varepsilon Z)$ sends
$(A,B,C,D)$ to $(A,\varepsilon B,\varepsilon C,D)$ and leaves $q$
unchanged. Thus the same result holds on
$A=B=0,D=-\varepsilon C$, with $c=\varepsilon C$ and
$a=(A+\varepsilon B)/2$.

### What the cusp does not say

On the line $a=b=0$, equation (6) has an analytic axis branch
$s=0$ and a pair satisfying
$$
s^2=\frac{c}{c-3}t+O(t^2).
\tag{9}
$$
Thus a transverse loop in this **slice** exchanges two labels and
fixes the third; a central three-label collision is not an inertia
3-cycle. Formula (9) is a local marked-block statement. It is not the
global degree-eleven cycle-sign squareclass: other blocks can supply
unramified unit factors. D2 owns the exact full slice character.

The cusp calculation explains why this curve cannot simply be used as
a transverse generic-fold test. It does not rule out using it as an
all-period witness, if such a witness theorem is proved separately.
No real or non-Archimedean all-higher-period hyperbolicity statement
along this curve has been established in this round.

## 2. Explicit conormal of the generic marked two-cycle fold

On the dense open of the critical hypersurface where
$$
J=I-qH\quad\text{is invertible},\qquad
H=\begin{pmatrix}0&Z&Y\\Z&0&X\\Y&X&0\end{pmatrix},
$$
put $v_0=(X,Y,Z)^t$ and $g=(YZ,XZ,XY)^t$. This open is nonempty:
it contains the accepted fold at $(2/3,3/2,3/2,3/2)$.
Writing $d\mathbf A=(dA,dB,dC)^t$, differentiation of (1) gives
$$
d\mathbf A=J\,dv_0-g\,dq,
$$
and
$$
dD=q(g-2v_0)^t\,dv_0+(XYZ-X^2-Y^2-Z^2)\,dq.
$$
Substitute $dv_0=J^{-1}(d\mathbf A+g\,dq)$. On the critical
hypersurface the coefficient of $dq$ vanishes, since it is the
Schur complement of the Jacobian and $\det J\ne0$. Therefore the
conormal line of the branch image at an ordinary fold is generated by
$$
\boxed{\quad
\nu_f=dD-q(g-2v_0)^tJ^{-1}d\mathbf A.
\quad}
\tag{10}
$$
At the all-positive accepted fold this is
$$
\nu_f=dD-\tfrac12(dA+dB+dC).
\tag{11}
$$
This is a rational expression on the marked critical chart. At the
cusp points of §1, $J$ is singular, so formula (10) is not used there.

## 3. The remote-fold unfolding covector

Let $a_0\in B^{\rm sm}$ and let $p$ have native least period $n$.
Choose local analytic coordinates on the surface fibres near the
finite orbit and write its return as $f_a^n$ in a coordinate $z\in
\mathbb C^2$ near $p$. Set
$$
G(a,z)=f_a^n(z)-z,\qquad L=D_zG(a_0,p).
$$
Suppose $L$ has rank one. Let $v\ne0$ span its kernel and let a
nonzero row vector $\ell$ span its left cokernel, so $\ell L=0$.
Define
$$
\alpha_n=\ell D_aG(a_0,p),\qquad
\beta_n=\ell D_z^2G(a_0,p)[v,v].
\tag{12}
$$
Changing $v$ or $\ell$ scales the relevant nonzero quantities but
does not alter the following tests.

**Lemma 3.1 (simple-fold covector).** If
$\beta_n\ne0$ and $\alpha_n\ne0$, then the local fixed incidence
$G=0$ maps to parameter space as a simple fold. Its smooth local
branch divisor has conormal line $\mathbb C\alpha_n$.

**Proof.** Choose one state direction complementary to $v$ and one
equation component on which $L$ is nonzero. The implicit-function
theorem solves that state direction from that equation. The remaining
scalar equation is $\varphi(a,s)=0$, with
$$
\varphi_s(a_0,0)=0,\quad
\varphi_{ss}(a_0,0)=\beta_n,\quad
d_a\varphi(a_0,0)=\alpha_n
$$
up to nonzero constant factors. Terms arising from the solved state
direction are killed by $\ell L=0$. Solve
$\varphi_s(a,s)=0$ for its critical point $s_c(a)$ using
$\beta_n\ne0$. The critical-value equation is
$\rho_n(a)=\varphi(a,s_c(a))=0$, and
$d\rho_n(a_0)=\alpha_n\ne0$. The Taylor expansion about $s_c(a)$
has nonzero quadratic coefficient. Taking its analytic square root
gives the simple-fold normal form. $\square$

The conormal test is independent of how the nearby surface fibres
were trivialized. A parameter-dependent state-coordinate change
alters $D_aG$ by a term in the image of $L$, together with the
invertible change of equation coordinates. The cokernel kills the
first term and transports by the second. Thus $\alpha_n$ defines
the same conormal line.

It is also an explicit finite-orbit quantity. If $p_j=f_{a_0}^j(p)$,
and $V_j(\dot a)=\partial_a f_a(p_j)|_{a_0}(\dot a)$ in compatible
orbit charts, the chain rule gives
$$
\alpha_n(\dot a)=
\ell\sum_{j=0}^{n-1}
Df_{a_0}^{\,n-1-j}|_{p_{j+1}}\,V_j(\dot a).
\tag{13}
$$
The last factor is the identity for $j=n-1$. Formula (13) is the
parameter variation of the actual native return; no unforced or
permuted-clock replacement is made.

**Corollary 3.2 (paired simple-fold test).** Suppose a marked
period-two fold and a distinct native-period-$n$ simple fold occur
at the same smooth parameter, where (10) and Lemma 3.1 apply. If
$$
\alpha_n\wedge\nu_f\ne0,
\tag{14}
$$
their local branch divisors are distinct and meet transversely. In
particular the remote branch germ does not equal the marked fold germ.

**Proof.** The two smooth branch hypersurfaces have conormal lines
$\mathbb C\alpha_n$ and $\mathbb C\nu_f$. Equation (14) says
these lines are independent. The implicit-function theorem applied
to their two local defining functions gives the claimed transverse
intersection. $\square$

This is an explicit derivative mechanism, not a claim that (14)
automatically holds for two different periods.

## 4. Satellite resonances and the conditional all-period bridge

A higher exact period can also degenerate to an existing native
period $d\ge3$. These satellite cases must not be hidden in a
simple-fold hypothesis. Let $p$ have least period $d$, let
$M_d=DT^d_p$ on the surface, and suppose $M_d-I$ is invertible.
Then the period-$d$ point moves analytically with parameters. Put
$$
\tau_d(a)=\operatorname{tr}(DT^d_{p(a)}),\qquad
\det M_d=(-1)^d.
$$
For a root of unity $\zeta$ such that neither
$\zeta$ nor $(-1)^d/\zeta$ equals one, the condition that $\zeta$
be a return eigenvalue is exactly
$$
\tau_d(a)=\zeta+(-1)^d/\zeta.
\tag{15}
$$
If $d\tau_d\wedge\nu_f\ne0$ at such a point, this resonance
hypersurface is smooth and transverse to $\mathscr F$, so its germ
cannot be the marked fold germ. A resonance with eigenvalue one is
instead part of the fixed-incidence degeneracy in §3 or of a
higher-degeneracy stratum not covered by its hypotheses.

The following is a **conditional route**, not an established property
of the Fricke family:

> For every relevant period, all generic residual ramification
> components are covered either by a simple-fold model of Lemma 3.1
> or by a nondegenerate lower-period multiplier resonance (15), and
> their associated covectors satisfy the respective independent-
> conormal test against (10) at a point for every potentially shared
> image component. Each such test point lies in the smooth loci of
> the global divisor $\mathscr F$ and of that candidate image
> component, and the marked two-cycle branch is the unique local
> germ of $\mathscr F$ there. Any remaining multiple-degeneracy
> stratum has image not containing $\mathscr F$.

Under this assumption no residual ramification component can have
image $\mathscr F$: a shared component would have equal conormal
lines on its common smooth open part, contradicting the test, while
the last clause excludes untested strata. Accepted R3 then gives
SF2. This implication is valid, but **neither the all-component
local-model coverage nor the covector independence has been proved**.
Ordinary dimension counts would assume the very transversality at
issue and are not evidence for it.

The smooth-locus/branch-matching hypothesis is essential for this
global inference. Corollary 3.2 alone distinguishes two local branch
germs. Globally irreducible $\mathscr F$ already has four different
local fold graphs at the accepted parameter $b_f$. Comparing a remote
germ to a different marked germ at such a point can give (14) even
when both belong to the same global divisor. No global noncontainment
is inferred from that comparison.

An alternative stronger sufficient route is an on-$\mathscr F$
all-sheet witness: for each $n$, a parameter in $\mathscr F\cap B^{\rm sm}$ at
which every residual fixed point has $DT^n-I$ invertible. Finite
flatness and closedness of the critical image would then exclude
domination. Here the residual points at a special witness mean **all
points in the finite closure inside $\operatorname{Fix}(T^n)$ of the
generic point sets $P_d$ for $d\mid n$, $d\ge3$**. A limit is not
deleted merely because its least period at the witness drops to one
or two. R3's period-two isolation holds at generic $\mathscr F$ and
does not authorize such deletion at an arbitrary special parameter.
The derivative condition makes the ambient fixed incidence étale at
every point of this closure's witness fibre. The image of the ambient
critical locus intersected with this finite closure therefore cannot
contain $\mathscr F$. Section 1 does not supply such a witness; it
identifies the exact geometry of one proposed witness curve.

Finally, these derivative exclusions are sufficient but need not be
necessary for SF2. A nonreduced raw fixed fibre may normalize without
ramification. The exact target remains the normalized residual
different of accepted R3 §5, not the absence of every raw degeneracy.

## 5. Missing input and reusable output

The reusable local outputs are the cusp equations (5)–(9), the marked
fold conormal (10), and the finite-orbit unfolding covector (13).
They distinguish a genuine paired-unfolding proof from an appeal to
genericity. They do not evaluate the higher-period covectors.

The missing global input is an all-period independence/coverage
theorem as specified in §4, or a proved all-residual-sheet witness
on $\mathscr F$. Primary sources checked in this round establish
ambient genericity or concern different dynamical families and do
not provide that input. The search boundary is not a theorem that no
such result exists in the literature.

No higher-period branch divisor has been shown to coincide with
$\mathscr F$, so SF2 is neither proved nor refuted. No higher wreath
group, layer independence, target arithmetic, or completion of FGT
is claimed. No mathematical execution or modification of frozen,
shared, evaluator, manuscript or Git files was performed.
