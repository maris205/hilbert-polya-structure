# HCS-C55 theorem package

Status: **DOCS_FINAL_NO_MORE_EDITS; exact finite gates, independent hostile
paper audit, and official compilation passed**. The statements below are the
locked theorem package.

## 1. Source data

Let $K=\mathbf Q(\rho)$, with $\rho^2+\rho+1=0$, and let

\[
X=V(C,Q)\subset\mathbf P^7_K,
\qquad
C=\sum_{i=0}^{7}x_i^3,
\qquad
Q=\sum_{i=0}^{6}x_ix_{i+1}+\rho x_7x_0.
\]

Let $X_0/\mathbf Q$ be the explicit HCS-C53 equation model. Let

\[
G=\operatorname{Dih}(C_{12})
=\langle r,s\mid r^{12}=s^2=1,\ srs=r^{-1}\rangle.
\]

HCS-C53/HCS-C54 descend the ambient projective action to a nonconstant
finite etale $\mathbf Q$-group scheme $\mathscr G$ of rank $24$, split
by $K$, with transport

\[
\delta(r)=r^{-1},\qquad \delta(s)=rs.
\]

The C55 exact certificate replays the induced morphism
$\mathscr G\to\operatorname{PGL}_{8,\mathbf Q}$. The statement does not
classify the full projective automorphism group.

## 2. Algebraic equivariant deformation germ

### Theorem A

There exist a pointed smooth locally closed $\mathbf Q$-germ
$(B_{\rm core},0)$ of dimension four, a smooth projective family

\[
f:\mathcal X\longrightarrow B_{\rm core},
\]

and a fiberwise action of
$\mathscr G_B=\mathscr G\times_{\mathbf Q}B_{\rm core}$ such that

\[
\mathcal X_0=X_0
\]

and the Kodaira--Spencer map is an isomorphism

\[
\operatorname{KS}_0:T_{B_{\rm core},0}
\xrightarrow{\sim}H^1(X_0,T_{X_0})^{\mathscr G}.
\tag{A.1}
\]

After base change to $K$, the completion of this family maps formally
etale to the fixed germ of a $G$-equivariant semiuniversal deformation.

The germ $B_{\rm core}$ is a transverse slice in the fixed Hilbert locus.
The full fixed Hilbert locus is not asserted to be four-dimensional, and no
literal family $C+\sum t_ip_i=Q=0$ is asserted.

## 3. Relative Reynolds variation

Let

\[
\alpha:\mathscr G_B\times_B\mathcal X
\longrightarrow\mathcal X\times_B\mathcal X,
\qquad (g,x)\longmapsto(x,gx),
\]

and define

\[
e_{\rm rel}
=\frac1{24}\alpha_*[\mathscr G_B\times_B\mathcal X]
\in\operatorname{CH}^5(\mathcal X\times_B\mathcal X)_{\mathbf Q}.
\tag{B.1}
\]

### Theorem B

The correspondence in (B.1) is self-transpose and idempotent:

\[
e_{\rm rel}^2=e_{\rm rel},\qquad {}^te_{\rm rel}=e_{\rm rel}.
\tag{B.2}
\]

On the complex analytic germ,

\[
\mathbb V_{\rm core}
=\operatorname{im}\!\left(
e_{\rm rel}:R^5f_*\mathbf Q\to R^5f_*\mathbf Q
\right)(1)
\tag{B.3}
\]

is a polarizable rational VHS of weight three and rank ten with Hodge numbers

\[
(h^{3,0},h^{2,1},h^{1,2},h^{0,3})=(1,4,4,1).
\tag{B.4}
\]

Contraction by a generator of the invariant $H^{4,1}$ line identifies

\[
T_{B_{\rm core},0}\xrightarrow{\sim}
F^2\mathbb V_{{\rm core},0}/F^3\mathbb V_{{\rm core},0}.
\tag{B.5}
\]

Thus the projected period map is immersive at the origin and, after
shrinking, is a local immersion.

The twist in (B.3) is exactly $\mathbf Q(1)$: it sends
$(4,1),(3,2),(2,3),(1,4)$ to
$(3,0),(2,1),(1,2),(0,3)$. The theorem does not construct a CY3.

On the central $H^5$, $e_{\rm rel}$ agrees with the HCS-C53 Chow core
$\pi_5e_{\mathscr G}$. No relative Chow--Künneth projector is claimed.

## 4. Cayley ring and projective Yukawa cubic

Set

\[
F=yC+zQ,
\qquad
\deg x_i=(0,1),\quad
\deg y=(1,-3),\quad
\deg z=(1,-2),
\]

and

\[
R=K[x_0,\ldots,x_7,y,z]/J(F).
\tag{C.1}
\]

The semilinear descent convention on the Cayley presentation is

\[
D(p)(x)=\tau(p)(M^{-1}x),\qquad
D(C)=C,\qquad D(Q_\rho)=\rho^2Q_\rho,
\]

and therefore

\[
D(y)=y,\qquad D(z)=\rho z,\qquad D(F)=F.
\tag{C.1a}
\]

In particular \(D(z)\ne\rho^2z\).

The exact calculation gives

\[
R_{1,-3}=K[y],\qquad
\dim_KR_{2,-3}=83,
\qquad
\dim_KR_{5,-6}=1.
\tag{C.2}
\]

The release-candidate gate proves that the induced semilinear action on
\(R_{5,-6}\) satisfies the quadratic cocycle and has a one-dimensional
\(\mathbf Q\)-fixed form. A trace coordinate on that rational line is then
unique up to \(\mathbf Q^\times\).

Let $v_i=[yp_i]\in R_{1,0}$, $0\le i\le3$, be the four frozen
descended tangent operators and let $\omega=[y]\in R_{1,-3}$. The
successive objects are

\[
yp_i\in R_{1,0},\quad
y^2p_i\in R_{2,-3},\quad
y^4p_ip_jp_k\in R_{4,-3},\quad
y^5p_ip_jp_k\in R_{5,-6}.
\tag{C.3}
\]

### Theorem C

For any nonzero top trace $\operatorname{Tr}:R_{5,-6}\to K$, the
projective Yukawa tensor at the origin is

\[
Y_{ijk}
=\operatorname{Tr}\bigl(y^5p_ip_jp_k\bigr)
\tag{C.4}
\]

up to one common nonzero normalization. In the locked rational tangent basis,
the primitive integral polynomial is

\[
\begin{aligned}
Y_H={}&75081586157u_0^3-28576620789u_0^2u_1
+164150208636u_0u_1^2+6898957820u_1^3\\
&-122000922135u_0^2u_2-415458334296u_0u_1u_2
+1132596902196u_1^2u_2\\
&+1158143874300u_0u_2^2-2054867641020u_1u_2^2
+2646295985484u_2^3\\
&-5364921951u_0^2u_3+151070718312u_0u_1u_3
-30413540316u_1^2u_3\\
&+114691988016u_0u_2u_3+151980984216u_1u_2u_3
+560186573940u_2^2u_3\\
&+113572676646u_0u_3^2+36794420832u_1u_3^2
+706181383584u_2u_3^2+1884468968u_3^3.
\end{aligned}
\tag{C.5}
\]

The coefficient gcd is one. The exact release candidate further proves

\[
\operatorname{Hilb}
\frac{\mathbf Q[u_0,u_1,u_2,u_3]}
{(\partial_{u_0}Y_H,\ldots,\partial_{u_3}Y_H)}(t)
=(1+t)^4,
\tag{C.6}
\]

so the gradient quotient has length $16$. Therefore

\[
S_H=V(Y_H)\subset\mathbf P^3_{\mathbf Q}
\tag{C.7}
\]

is a smooth geometrically irreducible cubic surface.

Here “rational” refers to the field of definition of the cubic form and of
\(S_H\). No claim that \(S_H\) is a rational variety over \(\mathbf Q\) is
made.

The displayed polynomial depends on the rational basis and trace coordinate.
Its projective class is invariant under a common nonzero rescaling, and a
rational tangent-basis change acts through $\operatorname{GL}_4(\mathbf Q)$.

## 5. Honest-CY3 necessary gate

### Theorem D

Let $g:Y\to S$ be a smooth projective family of Calabi--Yau threefolds with
$h^{2,1}=4$. Suppose an isomorphism of pointed complex base germs
$\phi:(S,s)\to(B_{\rm core},0)$ and an isomorphism of polarized rational VHS

\[
\Phi:R^3g_*\mathbf Q\xrightarrow{\sim}\phi^*\mathbb V_{\rm core}
\tag{D.1}
\]

are given. If $A=d\phi_s$, then

\[
Y_Y(v)=\lambda Y_H(Av),
\qquad \lambda\in\mathbf C^\times.
\tag{D.2}
\]

Thus failure of projective $\operatorname{GL}_4(\mathbf C)$-equivalence is
a pointed local polarized-VHS no-go. The same necessity follows from a
relative algebraic correspondence only if it induces the horizontal
isomorphism (D.1). A central-fiber correspondence is insufficient.

Projective equivalence is not sufficient for a VHS isomorphism and is never,
by itself, evidence for an isomorphism of motives.

## 6. Comparator branch

The generic four-parameter Braun--Candelas--Davies
$\operatorname{Dic}_3$ and $\mathbf Z_{12}$ quotients are admitted as
honest $(1,4)$ CY3 comparators. A named comparison requires their complete
four-variable B-model tensor and an exact incidence calculation

\[
Y_{\rm BCD}(c;u)=\lambda Y_H(Au).
\tag{E.1}
\]

The mirror-side one-parameter special geometry and the generically nodal
enhanced-dihedral locus are inadmissible substitutes. Until (E.1) is
computed, the comparator label is NOT-COMPARABLE-WITH-CURRENT-DATA.

## 7. Release scope

Theorems A, B, and D are written proofs; Theorem C additionally uses the
exact producer/checker certificate. The release-candidate tuple has payload
SHA-256
`6afc529d2ab9e849592d9eba7b76324cc7a840670f50c669f90fdd079c0b4323`
and certificate SHA-256
`aa6a57bc496d78afd5728640083179bb0dd24963deb44e31459c59edc71c381f`.
The implementation commit remains a later provenance field and is not a
theorem input.
