# C244 theorem package — spherical pendulum

## Frozen Hamiltonian

On \(T^*S^2\), with unit length, mass, and gravity,
\[
 H=\frac12\left(p_\theta^2+\frac{j^2}{\sin^2\theta}\right)+\cos\theta,
 \qquad J=j=p_\phi .
\]
At the poles we use embedding variables \((r,p)\in\mathbb R^3\times
\mathbb R^3\), \(r\cdot r=1,\ r\cdot p=0\), so the apparent azimuthal
singularity is a chart artifact.

## Reduction and critical values

Writing \(u=\cos\theta\), \(h=H\), gives
\[
 \dot u^2=P_{h,j}(u)=2(1-u^2)(h-u)-j^2
 =2u^3-2hu^2-2u+2h-j^2 .
\]
The discriminant is
\[
 \operatorname{disc}_uP=
 4(16h^4-8h^3j^2-32h^2+72hj^2-27j^4+16).
\]
Solving \(P(s)=P'(s)=0\) with \(s\in(-1,0)\) gives the interior elliptic
critical branch
\[
 h=\frac{3s^2-1}{2s},\qquad j^2=\frac{(1-s^2)^2}{-s}.
\]
The point \(u=-1,h=-1,j=0\) is elliptic-elliptic.  The upright point
\(u=1,h=1,j=0\) is an isolated focus-focus critical value and produces a
pinched fiber; it is not on the interior \(s\in(-1,0)\) branch.

## Regular chambers and quadratures

For every regular row in the evidence, \(r_1<r_2<1<r_3\) and the physical
interval is \((r_1,r_2)\subset(-1,1)\).  With \(m=(r_1+r_2)/2\),
\(d=(r_2-r_1)/2\), and \(u=m+d\cos t\),
\[
 T=2\int_0^\pi\frac{dt}{\sqrt{2(r_3-u(t))}},\qquad
 \Delta\phi=2j\int_0^\pi
 \frac{dt}{(1-u(t)^2)\sqrt{2(r_3-u(t))}},
\]
\[
 I=\frac1\pi\int_0^\pi
 \frac{d^2\sin^2t\,\sqrt{2(r_3-u(t))}}{1-u(t)^2}\,dt .
\]
The last expression is independently checked against
\(I=\pi^{-1}\int_{r_1}^{r_2}\sqrt{P(u)}(1-u^2)^{-1}\,du\).
These are exact quadratures; no elementary closed form is asserted for every
parameter value.  A double root is never assigned a regular period.

For a regular torus, the reconstructed trajectory closes if and only if
\(\Delta\phi/(2\pi)=p/q\) in lowest terms.  Its primitive closure uses \(q\)
u-oscillations; the \(k\)-fold repetition uses \(kq\).  An irrational ratio is
quasiperiodic on the torus.  This clean resonant-family statement does not
turn a one-parameter torus family into an isolated orbit.

## Monodromy convention

Fix \(\alpha\) as the vanishing cycle and \(\beta\) as a transported
complementary cycle.  A positive counterclockwise loop around \((h,j)=(1,0)\)
has transport \(\alpha\mapsto\alpha\), \(\beta\mapsto\beta+\alpha\).
**Matrix columns are the transported basis vectors expressed in the initial
\((\alpha,\beta)\) basis.** Therefore
\[
 M_{(\alpha,\beta)}=\begin{pmatrix}1&1\\0&1\end{pmatrix}.
\]
This convention prevents the common transpose ambiguity; arbitrary changes of
basis may conjugate the displayed matrix.

## Route decision and nonclaims

The theorem is A1_PASS_ANALYTIC, while A0, A2, and A3 fail and A4 is only
A4_NATURAL_QUANTIZATION.  Overall:
(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION),
ROUTE_A_REJECTED.  No arithmetic local data, Euler factors, root numbers,
automorphy, target divisor/functional equation, zero match, or
Hilbert--Pólya operator is claimed.
