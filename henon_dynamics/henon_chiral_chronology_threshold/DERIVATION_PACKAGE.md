# HCS-C21 derivation package

## 1. Frozen recurrence and notation

Work with

\[
H_A(x,y)=(A-x^2-y,x),
\qquad
x_{i+1}=A-x_i^2-x_{i-1}.
\]

The source radical is denoted by $\eta$:

\[
\eta^2=A-3.
\]

Frobenius degree, when later needed, is $r_F$; it is never identified with
$\eta$, Hénon period $n$, or chronological phase $s$.

The code stores a forward edge $(x_i,x_{i+1})$, so its edge shift is
$H_A^{-1}$.  HCS-C20 stores $(x_i,x_{i-1})$, so its edge shift is $H_A$.
Reversal conjugates the two generators.  All subgroup, quotient, and
isotypic statements below are invariant under $\tau\leftrightarrow\tau^{-1}$.

## 2. Published period-six carrier

Endler--Gallas's chiral factor is

\[
f_{\eta}(x)
=x^3-(1+\eta)x^2-Ax+A(1+\eta)-1.
\]

Its conjugate is $f_{-\eta}$, and the degree-six coordinate carrier is

\[
P_6(A,x)=f_{\eta}(x)f_{-\eta}(x).
\]

Eliminating $\eta^2=A-3$ gives

\[
\begin{aligned}
P_6={}&x^6-2x^5+(4-3A)x^4+(4A-2)x^3\\
&+(3A^2-8A+2)x^2+(-2A^2+2A)x\\
&-A^3+4A^2-2A+1,
\end{aligned}
\]

with

\[
\operatorname{Disc}_xP_6
=64(A-3)^3(16A^2-8A+5)^2.
\]

The conjugate-cubic factorization is prior work.  The expanded sextic and
its displayed discriminant are direct exact consequences recomputed here;
neither is promoted as a new theorem.  The new object is the ordered-edge
normalization built from the published factors.

## 3. Matching the two cubic root sets

Set

\[
m_{\eta}(x)=x^2+1-A-\eta.
\]

Direct polynomial division gives

\[
f_{-\eta}(m_{\eta}(x))\equiv0\pmod{f_{\eta}(x)}
\]

after $A=\eta^2+3$.  Similarly,

\[
m_{-\eta}(m_{\eta}(x))\equiv x\pmod{f_{\eta}(x)}.
\]

Thus $m_{\eta}$ is a bijection from the three roots of $f_{\eta}$ to
the three roots of $f_{-\eta}$.  It is the forbidden perfect matching in
the bipartite neighbor graph.

Let $\alpha,\beta,\gamma$ be the roots of $f_{\eta}$, ordered with
$\alpha\ne\beta$.  Vieta gives

\[
\alpha+\beta+\gamma=1+\eta.
\]

Reduction modulo the two Vieta relations verifies all six recurrence
equations for

\[
\mathcal O(\alpha,\beta)=
(\alpha,m_{\eta}(\beta),\gamma,
 m_{\eta}(\alpha),\beta,m_{\eta}(\gamma)).
\]

For each sign of $\eta$, there are $3\cdot2=6$ ordered choices, hence
twelve generic states over the $A$-line.  Their adjacency graph is
$K_{3,3}$ minus the forbidden matching.

## 4. An ordered edge recovers the splitting field

The coordinate sums satisfy

\[
x_0+x_2+x_4=1+\eta,
\qquad
x_1+x_3+x_5=1-\eta.
\]

Therefore

\[
\boxed{
\eta=\frac{x_0-x_1+x_2-x_3+x_4-x_5}{2}.
}
\]

One ordered edge generates the complete six-cycle by the Hénon recurrence.
It consequently recovers $\eta$ and all three roots of $f_{\eta}$.  The
ordered-edge function field is the full cubic splitting field, rather than a
base curve with a formally attached sign.

## 5. Absolute irreducibility of the cubic

After substituting $A=\eta^2+3$, write

\[
\begin{aligned}
F(\eta,x)={}&\eta^3-\eta^2x+\eta^2-\eta x^2+3\eta\\
&+x^3-x^2-3x+2.
\end{aligned}
\]

Suppose this monic cubic is reducible over
$\overline{\mathbb Q}(\eta)$.  It then has a root integral over
$\overline{\mathbb Q}[\eta]$, hence a polynomial root $q(\eta)$.  A
degree comparison in $F(\eta,q(\eta))$ forces
$q=c\eta+d$.  Substitution gives the coefficient ledger

\[
\begin{aligned}
&(c-1)^2(c+1),\\
&3c^2d-c^2-2cd-d+1,\\
&3cd^2-2cd-3c-d^2+3,\\
&d^3-d^2-3d+2.
\end{aligned}
\]

The leading coefficient gives $c=1$ or $c=-1$.

- If $c=1$, the coefficient of $\eta$ is $2d(d-1)$, so
  $d=0$ or $1$; the constants are respectively $2$ and $-1$.
- If $c=-1$, the coefficient of $\eta^2$ is $4d$, so $d=0$;
  the coefficient of $\eta$ is then $6$.

Both cases contradict $F(\eta,q)=0$.  Hence $F$ is absolutely
irreducible over $\overline{\mathbb Q}(\eta)$.

Its discriminant is

\[
\Delta(\eta)=16\eta^4+88\eta^2+125.
\]

This polynomial is squarefree and therefore nonsquare over
$\overline{\mathbb Q}(\eta)$.  The geometric cubic Galois group is $S_3$.

The projective plane cubic $F=0$ has no affine singularities.  At infinity
it has one ordinary node at $[\eta:x:z]=[1:1:0]$, with tangent cone
$2X(X-Z)$, and one smooth point $[1:-1:0]$.  Its scalar normalization
therefore has genus zero.  This scalar statement is distinct from the genus
of the splitting curve.

## 6. The twelve-state group

Represent a state by

\[
(\epsilon,(a,b,c)),
\qquad
\epsilon\in\{+1,-1\},
\quad
(a,b,c)\in S_3.
\]

The formal time and reversal actions are

\[
\tau(\epsilon,(a,b,c))
=(-\epsilon,(b,c,a)),
\]

\[
\rho(\epsilon,(a,b,c))
=(-\epsilon,(b,a,c)).
\]

Exact enumeration gives

\[
\tau^6=\rho^2=1,
\qquad
\rho\tau\rho=\tau^{-1},
\]

and a free transitive orbit of size twelve.  The central sheet involution
$\iota:\eta\mapsto-\eta$ commutes with the root $S_3$-action, so

\[
\operatorname{Gal}(E_6/\mathbb P^1_A)
\simeq S_3\times C_2\simeq D_6.
\]

Here $D_6$ means the dihedral group of order $12$.  If $c$ is a root
three-cycle, then

\[
\tau=\iota c,
\qquad
\tau^2\text{ generates }A_3,
\qquad
\tau^3=\iota.
\]

Connectedness and the exact-period state interpretation are asserted on the
generic open obtained by deleting the discriminant and lower-period
collision locus.  The curve $E_6$ below is the smooth projective
normalization of the resulting function field.

## 7. Branches and genus of $E_6$

Over the $\eta$-line, the $S_3$ splitting cover has degree six.  The four
simple zeros of $\Delta(\eta)$ carry transposition inertia.  Each contributes

\[
6\left(1-\frac12\right)=3
\]

to Riemann--Hurwitz.

Infinity requires a separate calculation.  Put $t=1/\eta$ and
$x=u/t$.  Then

\[
t^3F(1/t,u/t)
=(u-1)^2(u+1)+t(1-u^2)+3t^2(1-u)+2t^3.
\]

The $u=-1$ slope is simple.  At the double slope put $u=1+ct$; the
lowest coefficient is

\[
2c(c-1).
\]

Thus the two branches separate with integral slopes $c=0,1$; no fractional
power occurs and infinity is unramified.  Therefore

\[
2g(E_6)-2=6(-2)+4\cdot3=0,
\]

so

\[
\boxed{g(E_6)=1}.
\]

## 8. Exact rotation quotient and $H^1$-collapse

Let

\[
w=(\alpha-\beta)(\alpha-\gamma)(\beta-\gamma),
\qquad
w^2=\Delta(\eta).
\]

The matching involution changes the Vandermonde by

\[
\prod_{i<j}(\alpha_i+\alpha_j)
=e_1e_2-e_3=-1.
\]

Hence

\[
\iota:(\eta,w)\longmapsto(-\eta,-w).
\]

The $A_3$-fixed field of the cubic splitting field is
$\mathbb Q(\eta,w)$.  Since

\[
\langle\tau\rangle=A_3\times\langle\iota\rangle,
\]

the element $v=\eta w$ is fixed.  It satisfies

\[
v^2
=\eta^2\Delta(\eta)
=(A-3)(16A^2-8A+5).
\]

The right side is nonsquare in $\mathbb Q(A)$, so
$\mathbb Q(A,v)$ has degree two over $\mathbb Q(A)$.  The subgroup
$\langle\tau\rangle$ has index two in $D_6$, so its fixed field also has
degree two.  Inclusion plus equal degree proves

\[
\boxed{
\mathbb Q(E_6)^{\langle\tau\rangle}=\mathbb Q(A,v).
}
\]

The cubic

\[
(A-3)(16A^2-8A+5)
\]

has discriminant $-4{,}000{,}000$, hence the quotient curve has genus one.
Riemann--Hurwitz for the degree-six quotient gives zero total ramification.
Thus $\tau$ is a fixed-point-free automorphism of a genus-one curve, hence
a translation by a point of exact order six.  Translations act trivially on
weight-one cohomology:

\[
\boxed{
\chi_{\tau^*}(T)=(T-1)^2,
\qquad
\mu_{\tau^*}(T)=T-1.
}
\]

Since the full $D_6$-quotient has genus zero, reversal cannot act trivially.
Consequently

\[
H^1(E_6,\mathbb Q)
\simeq \varepsilon_{\mathrm{refl}}^{\oplus2}.
\]

This is a chronology--cohomology collapse: the time generator remains exact
on points but is invisible to ordinary $H^1$.

## 9. Scoped comparison with period seven

The HCS-C20 byte-locked certificate proves for one adopted and dynamically
certified period-seven chiral component that

\[
g(E_7)=8,
\qquad
g(E_7/\langle\tau\rangle)=2.
\]

Therefore

\[
\dim H^1(E_7)_{\tau\ne1}
=2g(E_7)-2g(E_7/\langle\tau\rangle)
=16-4=12.
\]

Published class counts give no chiral orbit below period six; the unique
period-six chiral doublet has zero nontrivial time dimension by the theorem
above; and the certified period-seven component has dimension twelve.  The
valid conclusion is therefore existential and scoped:

> Among source-identified and repository-certified Hamiltonian Hénon chiral
> ordered components with $n\le7$, the smallest period at which at least one
> certified component has nontrivial weight-one time characters is $n=7$.

This does not classify the full saturated period-seven scheme or every
diagonal/non-diagonal component at lower periods.

## 10. Lower-period marker shadow

Define the fixed-point marker

\[
D_1(u)=u^2+2u-A.
\]

The period-six reversible marker and period-seven chiral marker obey

\[
D^{\mathrm{mark}}_6(s_6)
=s_6^2+4s_6-4A
=4D_1(s_6/2),
\]

\[
C^{\mathrm{mark}}_7(s_7)
=s_7^2-2s_7-A
=D_1(s_7-2).
\]

Their common quadratic field is therefore
$\mathbb Q(A,\sqrt{A+1})$, but this field is inherited from period one.
Eliminating $A$ gives

\[
(s_6-2s_7+4)(s_6+2s_7)=0.
\]

The two graph components meet before normalization at
$(A,s_6,s_7)=(-1,-2,1)$; over $A\ne-1$, or after normalization, they are
disjoint.

Half-orbit controls were generated directly from $x_{-1}=x_0=z$.  After
removing the fixed-point factor and base-changing along $D_1$, the
period-six candidate splits into three quadratics, whereas the period-five
and period-seven controls remain irreducible over $\mathbb Q(u)$.  This is a
control for the observed alias, not a classification of all primitive
components.

## 11. Clock-equivariant divisibility theorem

Let $X_m,X_n$ be integral exact-period covers, with $H_m,H_n$ of exact
orders $m,n$.  Suppose a dominant nonconstant rational map satisfies

\[
\phi\circ H_m=H_n^k\circ\phi.
\]

Iterating $m$ times yields

\[
H_n^{km}\circ\phi=\phi.
\]

Dominance makes the image dense, so $H_n^{km}=1$, and therefore

\[
\boxed{n\mid km.}
\]

If the target clock remains faithful, $\gcd(k,n)=1$, then $n\mid m$.
No distinct pair in $\{5,6,7\}$ satisfies this divisibility.  The theorem
does not prohibit non-dominant boundary maps, $k=0$ clock-forgetting maps,
or multivalued algebraic correspondences.

## 12. Hilbert--Pólya boundary

The results are exact but fixed-period and algebraic.  They do not define:

- an all-period primitive repetition law;
- a cross-period transfer operator;
- a trace-class or Fredholm determinant;
- a global Euler product or functional equation;
- a Riemann-zero divisor map;
- a Hilbert--Pólya operator.

Accordingly, A2 and A3 fail.  The period-six collapse is an obstruction, and
the period-seven real correspondence remains only a finite-dimensional
formal A4 hint.
