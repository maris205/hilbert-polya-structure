# HCS-C31 derivation package

## 1. Symbolic and coordinate conventions

For an admissible state sequence, write

\[
w_i=(\varepsilon_i,\varepsilon_{i-1}),
\qquad \varepsilon_i\in\{-1,+1\}.
\]

The scalar Hénon recurrence is

\[
q_{i+1}=1-6q_i^2-q_{i-1},
\]

or, on the prescribed sign branch,

\[
q_i=\varepsilon_i
\sqrt{\frac{1-q_{i-1}-q_{i+1}}6}.
\]

The graph rule says that the two neighbors of a symbol cannot both be
positive.  Therefore their possible sums give

\[
\frac{1-q_{i-1}-q_{i+1}}6
\in
\left[\frac5{18},\frac38\right]
\cup
\left[\frac{17}{144},\frac{31}{144}\right].
\]

Every realized coordinate consequently satisfies

\[
\frac{\sqrt{17}}{12}\le |q_i|\le\sqrt{\frac38}.
\tag{1}
\]

This is stronger than merely retaining the h-set bound \(1/3\le|q_i|\le5/8\).

## 2. Self-consistent unstable slope

Let

\[
r=\frac{123}{112},\qquad a_0=\frac{112}{123}.
\]

The normalized derivative is

\[
D\widehat H_i=
\begin{pmatrix}
-12q_i&-r\\
a_0&0
\end{pmatrix}.
\]

If the unstable line at time \(i\) is spanned by \((1,\mu_i)\), invariance
means

\[
D\widehat H_i(1,\mu_i)
=\lambda_i(1,\mu_{i+1}),
\]

where

\[
\lambda_i=-12q_i-r\mu_i,
\qquad
\mu_{i+1}=\frac{a_0}{-12q_i-r\mu_i}.
\tag{2}
\]

Let \(M_u=\max_{\Lambda_*}|\mu^u|\).  The maximum exists because the invariant
bundle is continuous and \(\Lambda_*\) is compact.  The inherited cone gives
\(M_u\le1/2\).  From (1)--(2),

\[
M_u\le\frac{a_0}{\sqrt{17}-rM_u}.
\]

The denominator is positive under the inherited cone bound.  Rearranging,

\[
rM_u^2-\sqrt{17}M_u+a_0\ge0.
\]

Since \(ra_0=1\), the two roots are

\[
\frac{\sqrt{17}\pm\sqrt{13}}{2r}
=a_0\rho_0,\quad \frac{a_0}{\rho_0},
\qquad
\rho_0:=\frac{\sqrt{17}-\sqrt{13}}2.
\]

The large root is bigger than \(1/2\).  The inherited cone excludes that
branch, so

\[
M_u\le a_0\rho_0.
\tag{3}
\]

Substitution into \(\lambda_i\) gives

\[
|\lambda_i|
\ge\sqrt{17}-r(a_0\rho_0)
=\sqrt{17}-\rho_0
=\rho_0^{-1}
=\frac{\sqrt{17}+\sqrt{13}}2.
\tag{4}
\]

The last identity uses

\[
\rho_0^2-\sqrt{17}\rho_0+1=0.
\]

Similarly,

\[
|\lambda_i|
\le 12\sqrt{\frac38}+r(a_0\rho_0)
=3\sqrt6+\rho_0.
\tag{5}
\]

Equations (3)--(5) are exact algebraic bounds, not observed extrema.

## 3. Explicit Euclidean norm gauge

Let

\[
S=\operatorname{diag}\left(\frac7{48},\frac{41}{256}\right).
\]

The normalized derivative was defined by

\[
D\widehat H=S^{-1}DH_6S.
\]

Set

\[
e^u_{\rm ad}(z)=S(1,\mu^u(z))
=\left(\frac7{48},\frac{41}{256}\mu^u(z)\right).
\]

Multiplying the invariant-frame equation by \(S\) gives the physical identity

\[
DH_6(z)e^u_{\rm ad}(z)
=\lambda_u(z)e^u_{\rm ad}(H_6z).
\tag{6}
\]

Let

\[
b_u(z)=\log\|e^u_{\rm ad}(z)\|_2.
\]

After normalizing the source vector in (6),

\[
\begin{aligned}
\tau_E^u(z)
&=\log\left\|DH_6(z)
\frac{e^u_{\rm ad}(z)}{\|e^u_{\rm ad}(z)\|_2}\right\|_2\\
&=\log|\lambda_u(z)|
 +\log\|e^u_{\rm ad}(H_6z)\|_2
 -\log\|e^u_{\rm ad}(z)\|_2\\
&=\tau_{\rm ad}(z)+b_u(H_6z)-b_u(z).
\end{aligned}
\tag{7}
\]

The first component of \(e^u_{\rm ad}\) is fixed and nonzero.  In fact (3)
and \((41/256)a_0=7/48\) imply

\[
\frac7{48}
\le \|e^u_{\rm ad}(z)\|_2
\le \frac7{48}\sqrt{1+\rho_0^2}.
\tag{8}
\]

The unstable bundle is Hölder on the compact uniformly hyperbolic set, so
\(\mu^u\), \(b_u\), and both roofs are Hölder.

If \(H_6^nz=z\), summing (7) telescopes:

\[
\sum_{j=0}^{n-1}\tau_E^u(H_6^jz)
=\sum_{j=0}^{n-1}\tau_{\rm ad}(H_6^jz).
\tag{9}
\]

The product of the \(\lambda_u(H_6^jz)\) is the unstable eigenvalue of
\(DH_6^n(z)\), so both sides of (9) equal
\(\log|\Lambda_u(z,n)|\).  For every invariant probability measure, the
integral of the coboundary in (7) is zero; the variational principle therefore
gives equality of the two pressure functions.

## 4. Stable slope and angle coboundary

Write a stable normalized vector as \((\nu,1)\).  The inverse normalized
derivative is

\[
D\widehat H^{-1}(q,p)
=
\begin{pmatrix}
0&r\\
-a_0&-12p
\end{pmatrix}.
\]

Backward invariance yields the scalar recursion

\[
\nu(H_6^{-1}z)=\frac{r}{-a_0\nu(z)-12p}.
\]

Let \(M_s=\max|\nu^s|\).  The inherited stable cone gives \(M_s\le1/2\), and
the same quadratic argument gives

\[
M_s\le r\rho_0.
\tag{10}
\]

Physical spanning vectors can be chosen as

\[
e_u=\left(\frac7{48},\frac{41}{256}\mu\right),
\qquad
e_s=\left(\frac7{48}\nu,\frac{41}{256}\right).
\]

Using (3), (10), and the scale identities

\[
\frac{41}{256}a_0=\frac7{48},
\qquad
\frac7{48}r=\frac{41}{256},
\]

gives

\[
|\det(e_u,e_s)|
\ge\frac7{48}\frac{41}{256}(1-\rho_0^2)
\]

and

\[
\|e_u\|_2\|e_s\|_2
\le\frac7{48}\frac{41}{256}(1+\rho_0^2).
\]

Thus the Euclidean angle satisfies

\[
\sin\alpha(z)\ge\frac{1-\rho_0^2}{1+\rho_0^2}>0.
\tag{11}
\]

Let \(u_z,s_z\) be Euclidean unit vectors in the two invariant directions.
Since \(\det DH_6=1\), the area of their parallelogram gives

\[
J_E^u(z)J_E^s(z)\sin\alpha(H_6z)=\sin\alpha(z).
\tag{12}
\]

Taking logarithms, with

\[
\tau_E^u=\log J_E^u,\qquad
\tau_E^s=-\log J_E^s,\qquad
g=\log\sin\alpha,
\]

gives

\[
\tau_E^s=\tau_E^u-g+g\circ H_6.
\tag{13}
\]

The angle bound (11) and Hölder invariant bundles make \(g\) bounded Hölder.

## 5. Local maximality and mixing

Let

\[
N=\bigcup_{s,t}X_s\times Y_t,
\qquad U=\operatorname{int}N.
\]

R059 defines

\[
\Lambda_*=\bigcap_{k\in\mathbb Z}H_6^{-k}(N).
\]

The strict square-root range places every \(q_i\) in
\(\operatorname{int}X_{\varepsilon_i}\).  Its predecessor coordinate belongs
to

\[
\operatorname{int}X_{\varepsilon_{i-1}}
\subset\operatorname{int}Y_{\varepsilon_{i-1}}.
\]

Therefore every point of \(\Lambda_*\), at every iterate, is in \(U\).  Hence

\[
\Lambda_*\subset\operatorname{Inv}(U)
\subset\operatorname{Inv}(N)=\Lambda_*,
\]

so

\[
\Lambda_*=\operatorname{Inv}(U).
\tag{14}
\]

This proves local maximality.  The exact matrix power is

\[
A^4=
\begin{pmatrix}
4&2&2&1\\
2&2&1&1\\
2&1&2&1\\
1&1&1&1
\end{pmatrix}>0.
\tag{15}
\]

Thus the SFT is mixing.  R059's conjugacy transfers mixing and density of
periodic points, while R058 supplies uniform hyperbolicity.  This proves the
local-basic-set theorem without claiming anything about the full bounded
Hénon set.

## 6. Analytic decay inside a centered cylinder

This section gives an independent uniform variation proof.  It is useful both
as a cross-check on direct interval cylinders and as a fallback
representative-plus-tail certificate.

Let two codes agree at state indices \([-M,M]\).  Let

\[
d_i=|q_i-q_i'|.
\]

On every common sign branch, the two partial derivatives of the square-root
map have magnitude at most

\[
\alpha_0=\frac1{\sqrt{17}}.
\]

Therefore, for \(-M\le i\le M\),

\[
d_i\le\alpha_0(d_{i-1}+d_{i+1}).
\tag{16}
\]

All realized coordinates lie between
\(-\sqrt{3/8}\) and \(+\sqrt{3/8}\), so one may take

\[
D_q=\sqrt{\frac32}
\]

as a uniform boundary difference.  The number \(\rho_0\) is the smaller root
of

\[
\alpha_0(\rho+\rho^{-1})=1.
\]

The barrier

\[
B_i=D_q\left(
\rho_0^{\,i+M+1}+\rho_0^{\,M+1-i}
\right)
\]

satisfies equality in (16) and dominates the two boundary differences.
If \(d_i-B_i\) had a positive interior maximum, (16) would give

\[
\max(d-B)\le2\alpha_0\max(d-B)<\max(d-B),
\]

a contradiction.  Hence

\[
d_i\le
D_q\left(
\rho_0^{\,i+M+1}+\rho_0^{\,M+1-i}
\right),
\tag{17}
\]

and in particular

\[
|q_0-q_0'|\le Q_M:=2D_q\rho_0^{M+1}.
\tag{18}
\]

## 7. Unstable-slope variation in a cylinder

For a completely conservative formula, let \(J\) be any certified lower
bound for \(|\lambda_u|\).  One may use \(J=J_*\); the older
\(J=773/224\) remains a valid independent check.  Set

\[
\gamma=J^{-2},
\qquad
c_q=12a_0J^{-2}.
\]

The graph map

\[
G(q,\mu)=\frac{a_0}{-12q-r\mu}
\]

has, on a common sign cylinder,

\[
|\partial_\mu G|\le\gamma,\qquad
|\partial_qG|\le c_q.
\tag{19}
\]

Starting at time \(-M\), the inherited cone gives the conservative initial
difference \(|\mu_{-M}-\mu_{-M}'|\le1\).  Propagating (19) to time zero and
using (17) gives

\[
|\mu_0-\mu_0'|\le U_M,
\tag{20}
\]

where

\[
\begin{aligned}
U_M={}&\gamma^M\\
&+c_qD_q\left[
\rho_0\frac{\rho_0^M-\gamma^M}{\rho_0-\gamma}
+
\rho_0^{M+2}
\frac{1-(\gamma\rho_0)^M}{1-\gamma\rho_0}
\right].
\end{aligned}
\tag{21}
\]

The first term can be sharpened using the self-consistent cone diameter, but
(21) is already rigorous and avoids relying on that secondary optimization.

Since \(|\lambda_u|\ge J\), the logarithm is \(J^{-1}\)-Lipschitz in the
multiplier.  Equations (18), (20) give the full-cylinder roof oscillation

\[
\operatorname{osc}_{[-M,M]}\tau_{\rm ad}
\le
V_M:=\frac{12Q_M+rU_M}{J}.
\tag{22}
\]

Thus, if \(\widehat\tau_e\) is a rigorously enclosed value at one extension of
edge \(e\),

\[
\widehat\tau_e-V_M
\le\tau(x)\le
\widehat\tau_e+V_M
\qquad(x\in[e]).
\]

A floating periodic representative becomes a proof input only after its own
rounding error is added to \(V_M\).

## 8. Direct interval pressure sandwich

The production route uses \(M=6\), so an edge has length \(2M+1=13\).
Admissible length-\(12\) words are vertices, and admissible length-\(13\)
words are chronological edges.  Direct counting gives

\[
\#V=\mathbf1^TA^{11}\mathbf1=714,
\qquad
\#E=\mathbf1^TA^{12}\mathbf1=1156.
\tag{23}
\]

For each edge \(e:u\to v\), suppose interval graph transforms give

\[
\tau_e^-\le\tau(x)\le\tau_e^+
\qquad(x\in[e]).
\tag{24}
\]

For \(s\ge0\), define

\[
(L_s^-)_{uv}
=\sum_{e:u\to v}\exp(-s\tau_e^+),
\qquad
(L_s^+)_{uv}
=\sum_{e:u\to v}\exp(-s\tau_e^-).
\tag{25}
\]

Let \(\tau^-\) and \(\tau^+\) be the locally constant edge functions formed
from the lower and upper roof endpoints.  Then

\[
-s\tau^+\le-s\tau\le-s\tau^-.
\]

The variational definition of pressure is monotone, and a locally constant
edge potential has pressure equal to the logarithm of the Perron root of its
transfer matrix.  Therefore

\[
\log\rho(L_s^-)
\le P(-s\tau)
\le\log\rho(L_s^+).
\tag{26}
\]

If directed Perron bounds prove

\[
\log\rho(L_{s_L}^-)>0,
\qquad
\log\rho(L_{s_U}^+)<0,
\tag{27}
\]

then strict monotonicity from the positive roof yields

\[
s_L<h_*<s_U.
\tag{28}
\]

Equations (24), (26), and (27), not the central floating eigenvalue, are the
mathematical certificate.

## 9. Pressure-root semantics

For the two-variable formal weighted determinant,

\[
D(z,s)=
\exp\left(
-\sum_{n\ge1}\frac{z^n}{n}
\sum_{\sigma^nx=x}e^{-s\tau_n(x)}
\right),
\tag{29}
\]

the thermodynamic boundary is

\[
\log|z|+P(-\operatorname{Re}s\,\tau)=0.
\tag{30}
\]

At \(z=1\), the positive-real boundary is the unique

\[
P(-h_*\tau)=0.
\]

For a standard non-arithmetic suspension under the usual zeta continuation
theorem, the suspension zeta has its leading pole at \(h_*\); its inverse has
a zero there.  Equation (30) by itself does not construct a Fredholm
determinant or prove that a particular sequence of degree-truncated cycle
sections converges at the boundary.

The independently computed pressure interval can therefore explain the old
positive finite-section zero without retroactively turning the finite section
into a proved limiting determinant.

## 10. Absolute instability-trace radius

From (4), every \(n\)-periodic point has

\[
e^{-\tau_n(x)}\le J_*^{-n}.
\]

There are \(\operatorname{tr}A^n\) fixed symbolic points, so

\[
B_n(1):=\sum_{\sigma^nx=x}e^{-\tau_n(x)}
\le\operatorname{tr}(A^n)J_*^{-n}.
\tag{31}
\]

Because

\[
\limsup_{n\to\infty}(\operatorname{tr}A^n)^{1/n}=\varphi,
\]

the absolute trace-log majorant converges for

\[
|z|<\frac{J_*}{\varphi}
=\frac{\sqrt{17}+\sqrt{13}}{1+\sqrt5}.
\tag{32}
\]

At general real \(s\ge0\), replace \(J_*\) by \(J_*^s\).

At \(z=1\), (31) proves absolute convergence only when

\[
s>\frac{\log\varphi}{\log J_*}.
\tag{33}
\]

The pressure root near \(0.27798\) lies below the right side of (33).  This is
the exact obstruction explaining why a uniform expansion bound cannot replace
the cylinder-pressure theorem.

## 11. Bowen-dimension bridge and the locked local interfaces

Theorem 3 proves

\[
P(-s\tau_{\rm ad})
=P(-s\tau_E^u).
\]

The angle coboundary (13) proves equality of stable and unstable geometric
pressure roots after the stable \(H_6^{-1}\) convention is reindexed to the
same symbolic shift.

The source-scope check is now complete.  Pesin--Sadovskaya (2001), Remark 4.1
(printed page 284), applies to a \(u\)-conformal diffeomorphism on a locally
maximal hyperbolic set and identifies the unstable-slice dimension with the
root of \(P(-t\log b^u)=0\).  In one unstable dimension, conformality is
automatic.  Applying the same statement to \(H_6^{-1}\) gives the stable
slice.

Barreira, *Dimension Theory of Hyperbolic Flows* (2013), Introduction,
Theorem 1.2, states for a locally maximal hyperbolic set of a \(C^1\) surface
diffeomorphism with \(\dim E^s=\dim E^u=1\) that

\[
\dim_H\Lambda=t_s+t_u.
\]

Neither local statement requires a global Axiom-A extension or a compact
ambient surface.  The local-basic-set theorem, the adapted/Euclidean
coboundary, and the stable/unstable angle coboundary verify all the relevant
dynamical hypotheses.  Thus

~~~text
local_basic_set: PROVED
adapted_euclidean_pressure_equality: PROVED
stable_unstable_pressure_equality: PROVED
unstable_slice_dimension_equals_h_star: PROVED
total_Hausdorff_dimension_equals_2h_star: PROVED
~~~

No dimension interface remains open.  The pressure enclosure itself has a
different evidence type from these analytic deductions:

~~~text
pressure: NUMERICALLY_CERTIFIED
analytic_pressure_implication: PROVED

Route-A: (A1_WEAK,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)
overall: ROUTE_A_REJECTED
Route B authorized: false
~~~

The pressure and implication lines are theorem-ledger statuses, not Route-A
grades.
