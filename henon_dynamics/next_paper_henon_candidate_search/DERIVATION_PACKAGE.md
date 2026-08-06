# C02C derivation package: effective pinning and trace algebra for \(H_6\)

Date: 2026-08-06  
Status: **analytic derivation and independent computational audit complete**

## 1. Target

For the exact Paper-5 family member

\[
H_6(q,p)=(1-6q^2-p,q),
\]

turn the proved signed-root sequence-polydisc certificate into an effective
finite-window pinning theorem.  The target package consists of:

1. a unique holomorphic endpoint solver on the full frozen endpoint disks;
2. explicit exponential endpoint-localization bounds;
3. exact two-coordinate chronological gluing;
4. a matching/Hill/monodromy determinant identity;
5. an exact complex-base projective-fibre disk certificate and a composed
   endpoint-sensitivity bound.

This package is a quantitative specialization, not a claim that pinning
coordinates, crossed maps, or analytic dynamical determinants are new.

## 2. Status

| Item | Current status |
|---|---|
| Full-disk finite-window existence and uniqueness | `PROVED` below from the C02B contraction |
| Joint holomorphy in the endpoints | `PROVED` below |
| One-sided endpoint localization | `PROVED` below |
| Two-window chronological gluing | `PROVED` below |
| Crossed identity and continuant formulas | `PROVED` below |
| Matching/Hill determinant identity | `PROVED` below |
| Exact complex-\(q\) projective child disks | `PROVED` below |
| Composed projective endpoint sensitivity | `PROVED` below |
| Numerical/adversarial regression | `PASS`; complete producer and independent Newton checker |
| Nuclear operator or Fredholm determinant | `OPEN`; outside C02C |
| Route-A A2 promotion | `DO_NOT_PROMOTE; NOT_ESTABLISHED` |

## 3. Invariant Object

The invariant object is the genuine second-order Hénon chronology

\[
q_{i+1}=1-6q_i^2-q_{i-1},
\qquad z_i=(q_i,q_{i-1}),
\qquad H_6(z_i)=z_{i+1}.
\]

No transition matrix is averaged over time.  Every product of Jacobians,
projective maps, endpoint equations, and orbit weights is ordered in the same
chronology.  A finite block must be glued through the consecutive pair
\((q_k,q_{k+1})\), not through a scalar average.

## 4. Assumptions

### A1. Frozen complex coordinate disks

\[
c=\frac{23}{48},\qquad \rho=\frac7{48},\qquad
D_\sigma=\overline D(\sigma c,\rho),\quad \sigma\in\{-1,+1\}.
\]

These are inherited from C02B.  In particular, every \(q\in D_\sigma\)
satisfies

\[
|q|\ge c-\rho=\frac13.
\]

### A2. Local admissibility

For an extended sign word
\(\varepsilon_0,\ldots,\varepsilon_{N+1}\), require

\[
\neg(\varepsilon_{i-1}=\varepsilon_{i+1}=+1),
\qquad 1\le i\le N.
\]

The two neighbors are chronological occurrences.  They remain two
occurrences when periodic identification makes them refer to the same
coordinate.

### A3. Principal signed-root branch

For internal coordinates use

\[
(T_{\varepsilon;u,v}Q)_i
=\varepsilon_i\sqrt{\frac{1-Q_{i-1}-Q_{i+1}}6},
\]

with \(Q_0=u\), \(Q_{N+1}=v\), and the principal square root.  C02B proves
that all relevant radicands lie in one of

\[
\overline D\!\left(\frac16,\frac7{144}\right),
\qquad
\overline D\!\left(\frac{47}{144},\frac7{144}\right),
\]

strictly inside the right half-plane.

### A4. Frozen constants

\[
a_0=\frac1{\sqrt{17}},\qquad
\kappa=\frac2{\sqrt{17}}<1,\qquad
\beta=\frac{a_0}{1-\kappa}=\frac1{\sqrt{17}-2}<\frac12.
\]

The last strict inequality follows from \(\sqrt{17}>4\).  Thus
\(2\beta<1\).

## 5. Notation

- \(Q(u,v)=(Q_1,\ldots,Q_N)\): the finite-window fixed point.
- \(g_i=-\varepsilon_i/(12\sqrt{r_i})=-1/(12Q_i)\): a signed-root
  neighbor derivative at the fixed point.
- \(\mathcal A=D_QT_{\varepsilon;u,v}(Q)\): internal fixed-point derivative.
- \(a_i=-12Q_i\): the diagonal coefficient of the orbit residual Jacobian.
- \(L_N\): the open tridiagonal orbit Jacobian with diagonal \(a_i\) and
  off-diagonal entries \(-1\).
- \(K_{r,s}\): the continuant of the subblock \(r,\ldots,s\), with
  \(K_{r,r-2}=0\), \(K_{r,r-1}=1\).
- \(\theta_N=K_{1,N}=\det L_N\).
- \(M_N=DH_6^N(Q_1,u)\): chronological monodromy.
- \(\Phi_N(u,v)=(Q_N(u,v),Q_1(u,v))\): endpoint response ordered for
  periodic matching.
- \(F_N(u,v)=\Phi_N(u,v)-(u,v)\): periodic matching residual.
- \(R=123/224\): inherited projective parent-disk radius.

## 6. Derivation Strategy

The proof has four independent layers.

1. Apply the parameter-dependent contraction theorem on the full endpoint
   disks; use the nearest-neighbor support of powers of \(\mathcal A\) to
   retain distance information in the Neumann series.
2. Rewrite the same implicit problem using its tridiagonal orbit Jacobian.
   Continuants then expose every endpoint derivative and the top-left entry
   of chronological monodromy.
3. Express periodic closure as a two-variable matching residual.  Its Schur
   complement gives the Hill determinant and the fixed-point trace
   denominator without losing signs.
4. Invert the exact denominator disk of
   \(\phi_q(m)=(-12q-m)^{-1}\), then combine its fibre derivative with the
   endpoint-localization estimates.  The base sensitivity is not itself a
   contraction and is never described as one.

## 7. Derivation Map

\[
\text{C02B strict self-map}
\Longrightarrow Q(u,v)\text{ holomorphic}
\Longrightarrow (I-\mathcal A)^{-1}\text{ localization}
\]

\[
Q(u,v)
\Longrightarrow L_N\text{ continuants}
\Longrightarrow M_N\text{ entries}
\Longrightarrow \det DF_N=-\frac{\det(I-M_N)}{\det L_N}
\]

\[
q\in D_{\varepsilon},\ m\in D(0,R)
\Longrightarrow \text{exact reciprocal child disk}
\Longrightarrow \delta\text{-fibre contraction}
\Longrightarrow \text{remote-endpoint projective error bound}.
\]

## 8. Main Derivation

### 8.1 Full-disk endpoint theorem

Fix

\[
(u,v)\in D_{\varepsilon_0}\times D_{\varepsilon_{N+1}}.
\]

The same two radicand cases as in C02B apply to every internal row, including
the first and last rows, because the endpoint signs are part of the extended
admissible word.  Hence \(T_{\varepsilon;u,v}\) strictly maps

\[
\prod_{i=1}^N D_{\varepsilon_i}
\]

into itself.  Its derivative has at most two chronological neighbor
coefficients per row, each bounded by \(a_0\), so

\[
\|D_QT_{\varepsilon;u,v}\|_\infty\le\kappa<1.
\]

Banach's fixed-point theorem gives a unique \(Q(u,v)\).  The strict image
margins and compactness permit a common open enlargement of the endpoint and
internal polydisks on which the same map is holomorphic and remains uniformly
contracting.  Holomorphic iterates converge uniformly there, proving joint
holomorphy of \(Q\) on a neighborhood of the closed endpoint product.

### 8.2 Neumann-path localization

At the fixed point, let \(\mathcal A=D_QT\).  An endpoint enters only one
boundary row:

\[
b_L=g_1e_1,\qquad b_R=g_Ne_N,\qquad |g_i|\le a_0.
\]

Implicit differentiation gives

\[
Q_u=(I-\mathcal A)^{-1}b_L,
\qquad
Q_v=(I-\mathcal A)^{-1}b_R.
\]

Because \(\mathcal A\) is nearest-neighbor,
\((\mathcal A^rb_L)_i=0\) for \(r<i-1\).  Therefore

\[
\boxed{
|\partial_uQ_i|
\le \frac{a_0\kappa^{i-1}}{1-\kappa}
=\beta\kappa^{i-1}
}
\]

and, symmetrically,

\[
\boxed{
|\partial_vQ_i|
\le \frac{a_0\kappa^{N-i}}{1-\kappa}
=\beta\kappa^{N-i}.
}
\]

Convexity of the endpoint disks and integration along a straight segment give

\[
\boxed{
|Q_i(u,v)-Q_i(u',v')|
\le\beta\left(
\kappa^{i-1}|u-u'|+
\kappa^{N-i}|v-v'|
\right).
}
\]

The two terms must both be retained when both endpoints change.  In
particular, \(\beta\) is a one-endpoint constant; the crude joint endpoint
constant is \(2\beta<1\).

For an open window of length one, \(\mathcal A=0\) and each separate endpoint
derivative is exactly \(g_1\).  For length two,

\[
\mathcal A=\begin{pmatrix}0&g_1\\g_2&0\end{pmatrix},
\]

which yields the sharper uniform near/far bounds

\[
\frac{a_0}{1-a_0^2}=\frac{\sqrt{17}}{16},
\qquad
\frac{a_0^2}{1-a_0^2}=\frac1{16}.
\]

### 8.3 Exact two-window gluing

Split a length-\(m+n\) window at the consecutive interface pair

\[
(q_m,q_{m+1})=(\xi,\eta).
\]

The left window has endpoints \((u,\eta)\), and the right window has endpoints
\((\xi,v)\).  Define

\[
G(\xi,\eta)=
\begin{pmatrix}
\xi-Q_m^L(u,\eta)\\
\eta-Q_1^R(\xi,v)
\end{pmatrix}.
\]

Equivalently, solve the interface fixed-point problem

\[
(\xi,\eta)\mapsto
\bigl(Q_m^L(u,\eta),Q_1^R(\xi,v)\bigr).
\]

Each row contains one endpoint response bounded by \(\beta<1\), so this map is
a contraction in the product supremum norm.  Its fixed point concatenates to
a solution of the union recurrence; uniqueness of the union solution proves
exact chronological gluing.

If \(\theta_L,\theta_R,\theta_{m+n}\) denote the three open continuants, then

\[
\boxed{
\det D_{(\xi,\eta)}G
=\frac{\theta_{m+n}}{\theta_L\theta_R}.
}
\]

This is the exact two-interface composition law.  Identifying or averaging
\(\xi\) and \(\eta\) changes the dynamical problem.

### 8.4 Crossed identity and open continuants

The finite solution satisfies

\[
H_6^k(Q_1,u)=(Q_{k+1},Q_k),\qquad 0\le k\le N,
\]

and hence

\[
\boxed{
H_6^N(Q_1(u,v),u)=(v,Q_N(u,v)).
}
\]

Define the orbit residual

\[
E_i(Q;u,v)=1-6Q_i^2-Q_{i-1}-Q_{i+1}.
\]

Its internal Jacobian is

\[
L_N=
\begin{pmatrix}
a_1&-1\\
-1&a_2&-1\\
&\ddots&\ddots&\ddots\\
&&-1&a_N
\end{pmatrix},
\qquad a_i=-12Q_i.
\]

Since \(|a_i|\ge4>2\), this matrix is uniformly strictly diagonally
dominant.  It is also related directly to the contraction certificate by

\[
L_N=-12\operatorname{diag}(Q_i)(I-\mathcal A).
\]

Set

\[
K_{r,r-2}=0,\quad K_{r,r-1}=1,\quad
K_{r,s}=a_sK_{r,s-1}-K_{r,s-2}.
\]

Then \(K_{r,s}\) is the corresponding subblock determinant and
\(\theta_N=K_{1,N}=\det L_N\).  Differentiating \(E=0\) yields

\[
L_NQ_u=e_1,\qquad L_NQ_v=e_N,
\]

so

\[
\boxed{
\partial_uQ_i=\frac{K_{i+1,N}}{\theta_N},
\qquad
\partial_vQ_i=\frac{K_{1,i-1}}{\theta_N}.
}
\]

In particular,

\[
\boxed{
\partial_vQ_1=\partial_uQ_N=\frac1{\theta_N}.
}
\]

### 8.5 Chronological monodromy

Let

\[
A_i=DH_6(Q_i,Q_{i-1})=
\begin{pmatrix}a_i&-1\\1&0\end{pmatrix}.
\]

The genuine time-ordered product is

\[
M_N=A_NA_{N-1}\cdots A_1.
\]

An induction gives

\[
\boxed{
M_N=
\begin{pmatrix}
K_{1,N}&-K_{2,N}\\
K_{1,N-1}&-K_{2,N-1}
\end{pmatrix}.
}
\]

Thus

\[
(M_N)_{11}=\theta_N,
\qquad
\operatorname{tr}M_N=K_{1,N}-K_{2,N-1}.
\]

This also proves that the pinning chart has a nonzero crossed derivative:

\[
\partial_vQ_1=\frac1{(M_N)_{11}}\ne0.
\]

### 8.6 Periodic matching and the Hill determinant

Periodic closure is the pair of equations

\[
u=Q_N(u,v),\qquad v=Q_1(u,v).
\]

With

\[
\Phi_N(u,v)=(Q_N,Q_1),\qquad F_N=\Phi_N-(u,v),
\]

the endpoint derivative is

\[
D\Phi_N=
\frac1{(M_N)_{11}}
\begin{pmatrix}
1&(M_N)_{21}\\
-(M_N)_{12}&1
\end{pmatrix}.
\]

Using \(\det M_N=1\),

\[
\boxed{
\det DF_N
=-\frac{\det(I-M_N)}{(M_N)_{11}}
=-\frac{\det(I-M_N)}{\det L_N}.
}
\]

Let \(C_N\) be the Jacobian of the cyclic orbit residual.  Chronological
multiplicity gives

\[
C_1=[a_1-2],
\qquad
C_2=\begin{pmatrix}a_1&-2\\-2&a_2\end{pmatrix},
\]

while for \(N\ge3\), \(C_N\) is the usual cyclic tridiagonal matrix with two
off-diagonal \(-1\) occurrences in each row.  Uniformly for all \(N\ge1\),

\[
\boxed{
\det C_N=\operatorname{tr}M_N-2=-\det(I-M_N).
}
\]

Consequently,

\[
\boxed{
\det DF_N=\frac{\det C_N}{\det L_N}.
}
\]

The signed periodic-point denominator therefore has the exact boundary
residue form

\[
\boxed{
\frac1{\det(I-M_N)}
=-\frac1{\det L_N\,\det DF_N}
=-\frac{\partial_vQ_1}{\det DF_N}.
}
\]

This is an algebraic bridge to a Cauchy-residue trace.  It is not yet an
operator trace theorem.

### 8.7 Exact complex-base projective disks

For a tangent slope \(m=\delta p/\delta q\), one Hénon step gives

\[
\phi_q(m)=\frac1{-12q-m}.
\]

Take

\[
q\in D_{\varepsilon},\qquad |m|\le R=\frac{123}{224}.
\]

Set

\[
A=12c=\frac{23}{4},\qquad
S=12\rho+R=\frac{515}{224}.
\]

The denominator fills the exact disk

\[
\overline D(-\varepsilon A,S),
\]

whose pole clearance is

\[
A-S=\frac{773}{224}>0.
\]

Inverting that disk gives the exact and minimal circular image

\[
\boxed{
\phi\bigl(D_\varepsilon\times D(0,R)\bigr)
=D(-\varepsilon C_*,r_*),
}
\]

where

\[
C_*=\frac{288512}{1393719},
\qquad
r_*=\frac{115360}{1393719}.
\]

The inner and outer radii are

\[
C_*-r_*=\frac{224}{1803},
\qquad
C_*+r_*=\frac{224}{773}.
\]

Thus the child disks are separated by

\[
\boxed{\frac{448}{1803}}
\]

and lie inside the parent disk with margin

\[
\boxed{
R-(C_*+r_*)=\frac{44903}{173152}.
}
\]

The old real-base child disks remain valid but are not minimal; the new disk
is internally tangent to their outer boundary.

### 8.8 Projective contraction and composed endpoint error

Define

\[
\delta=\left(\frac{224}{773}\right)^2
=\frac{50176}{597529}.
\]

Uniformly on the frozen complex product,

\[
|\partial_m\phi_q(m)|\le\delta<1,
\qquad
|\partial_q\phi_q(m)|\le12\delta
=\frac{602112}{597529}>1.
\]

Only the fibre variable is a contraction in the unscaled norm.  For the
ordered cocycle

\[
m_i=\phi_{Q_i(u,v)}(m_{i-1}),\qquad 1\le i\le N,
\]

the initial-slope derivative obeys

\[
\boxed{|\partial_{m_0}m_N|\le\delta^N.}
\]

Combining the chain rule with the T2 endpoint bounds gives

\[
\boxed{
|\partial_um_N|
\le12\delta\beta
\frac{\kappa^N-\delta^N}{\kappa-\delta}.
}
\]

This tends to zero exponentially and quantifies loss of memory of the remote
left endpoint.  For the right endpoint,

\[
\boxed{
|\partial_vm_N|
\le12\delta\beta
\frac{1-(\delta\kappa)^N}{1-\delta\kappa}.
}
\]

The right endpoint is adjacent to the final projective step, so no decay in
\(N\) is expected in this orientation.  Reversal gives the symmetric remote
endpoint statement for the stable/backward cocycle, but that counterpart is
not included in the present certificate unless implemented separately.

### 8.9 Real orientation character

On the real certified survivor, the invariant unstable slope remains in
\(|m|\le R\), while \(|12q_i|\ge4\).  Hence the horizontal expansion factor

\[
-12q_i-m_{i-1}
\]

has sign \(-\varepsilon_i\).  For a real period-\(N\) orbit,

\[
\operatorname{sgn}\lambda_u
=\prod_{i=1}^N(-\varepsilon_i).
\]

Since \(M_N\) is area-preserving and hyperbolic,

\[
\boxed{
\operatorname{sgn}\det(I-M_N)
=-\prod_{i=1}^N(-\varepsilon_i).
}
\]

Thus passing from the signed holomorphic denominator to its absolute value
introduces an explicit orientation character.  These are different trace
objects and must not be interchanged silently.

## 9. Remarks

1. The finite-window contraction gives global uniqueness on the frozen
   polydisks; the continuant formulas explain its finite-dimensional
   differential algebra.
2. The matching identity is a Schur-complement/Hill identity in explicit
   coordinates.  Its likely value is as a trace-compatible implementation
   bridge, not as a standalone novelty claim.
3. The exact projective child disk is stronger than boundary sampling: the
   denominator product fills an exact disk, and inversion maps it to an exact
   disk.
4. The bound \(|\partial_q\phi|>1\) is an important negative fact.  It blocks
   any claim of joint base-fibre contraction in the unscaled product norm.
5. Period-one and period-two signed-root derivatives contain doubled neighbor
   occurrences after cyclic identification.  Projective dynamics still uses
   exactly one \(\phi_{q_i}\) per Hénon step.

## 10. Boundaries

- The theorem concerns the certified local \(H_6\) survivor, not the full
  bounded Hénon set.
- The parameter \(a=6\) belongs to the same exact Paper-5 family but is not
  Paper 5's fitted near-critical value.  It is used because a rigorous local
  hyperbolic certificate exists there.
- No Riemann zeros, primes, or target spectra enter the derivation.
- No Hilbert space, edge kernel, potential, nuclearity proof, or Fredholm
  determinant is supplied here.
- The signed and absolute determinant conventions remain separate.
- Sterling--Dullin--Meiss Theorem 3 already covers the conjugate real
  \(b=1,k=6\) forbidden-neighbor SFT and real signed-root uniqueness.
- General complex pinning/composition and the orientation-twisted
  absolute-denominator analytic determinant mechanism are prior art; only the
  explicit complex effective specialization and a possible future signed
  aggregate error theorem are under study.

## 11. Open Risks

1. The explicit constants may be mathematically correct but too elementary to
   support a standalone paper after a complete constructive-dynamics novelty
   audit.
2. A trace-compatible Cauchy-kernel operator may require mixed
   interior/exterior spaces and orientation signs not captured by the endpoint
   algebra alone.
3. The projective right-endpoint sensitivity does not decay in the forward
   orientation; a useful two-sided approximation theorem may require coupling
   forward unstable and backward stable cocycles.
4. The source-locked polydisks are effective, not claimed optimal for the
   base dynamics.
5. Route A remains closed unless a natural clock, potential, normalization,
   operator, and infinite determinant are frozen and independently validated.

## 12. Audit outcome

The frozen producer persisted 432 open rows and 120 cyclic rows, and summarized
120 endpoint-boundary probes in the certificate.  The independent checker
used a separate complex Newton solver, revisited the two worst-conditioned
cases at high precision, verified complete case-ID sets and rejected three
truncated/tampered variants.  All checks pass.  Exact metrics and artifact
hashes are recorded in
`results/c02c_finite_window/certificate.json` and
`results/c02c_finite_window/independent_check.json`.

This audit validates the implementation against the derivation; it is not a
numerical proof of the analytic claims and does not certify novelty.
