# Derivation Package

## Target

Construct the first genuinely non-scalar finite-symmetry reduction of the
homogeneous Hénon generating kernel, and decide whether its integral
augmentation determinant gives a credible Route-A Euler object.

The central object is not a cubic root of the scalar chirp.  It is the
order-three symmetry of the full two-variable generating function

\[
S_0(q,Q)=qQ+2q^3.
\]

## Status

`POSITIVE_EULER_GERM / STOP_RAW_ROUTE_A_PROMOTION`

The construction closes three exact gates:

1. the symmetry is intrinsic to the Hénon kernel and is not a scalar gauge;
2. the integral augmentation determinant has a chronological trace formula;
3. its canonical prime Euler superproduct converges locally uniformly and is
   nonzero on \(\operatorname{Re}s>1\).

The raw single-additive-character candidate then fails a necessary Route-A
gate exactly: its first split-prime coefficient, at \(p=7\), is nonreal, so
global conjugation symmetry is impossible.  Exact finite-field controls also
show that the augmentation has virtual rank two but does **not** reduce to a
rank-two local rational function: its reduced numerator and denominator
degrees grow linearly with the prime in every tested case.

## Invariant Object

For each prime \(p\equiv1\pmod3\), let

\[
\mathcal H_p=\mathbb C^{\mathbb F_p},
\qquad
(U_pf)(Q)=p^{-1/2}\sum_{q\in\mathbb F_p}
e_p(qQ+2q^3)f(q),
\]

where \(e_p(x)=\exp(2\pi i x/p)\).  Choose
\(\zeta_p\in\mathbb F_p^\times\) of order three and define

\[
(R_pf)(x)=f(\zeta_px).
\]

The choice \(\zeta_p\leftrightarrow\zeta_p^{-1}\) only exchanges the two
nontrivial sectors.  It does not change the integral augmentation factor.

The two-step Hénon quantum time is

\[
T_p=U_p^2.
\]

## Assumptions and Scope

1. Only primes \(p>3\) with \(p\equiv1\pmod3\) enter the split-sector Euler
   product.
2. The Fourier normalization is exactly \(p^{-1/2}\); no fitted phase or
   scale is allowed.
3. The global clock is \(\log p\), inherited from the prime Euler index.  A
   prime is not claimed to be a classical primitive orbit of one real Hénon
   map.
4. The determinant is a rational finite-dimensional local superdeterminant,
   not an ordinary determinant of a fixed-rank global operator.
5. No Riemann-zero table, prime fitting, or post hoc zero cancellation is
   used.
6. Global meromorphic continuation, a functional equation, the Gamma factor,
   and equality with \(\xi\) remain open.

## Derivation Map

1. Derive the area-preserving homogeneous Hénon map from \(S_0\).
2. Prove the intrinsic \(\mu_3\) symmetry of the full generating kernel.
3. Quantize and prove the dihedral relation \(U_pR_p=R_p^{-1}U_p\).
4. Pass to two-step time \(T_p=U_p^2\), which preserves the three sectors.
5. Form the integral augmentation virtual sector \((2,-1,-1)\).
6. Rewrite all logarithmic moments as chronological twisted Hénon traces.
7. Use the smooth cubic leading form to bound every fixed moment uniformly in
   \(p\).
8. Prove absolute local-uniform convergence of the canonical prime Euler
   superproduct on \(\operatorname{Re}s>1\).
9. Test whether local characteristic polynomials cancel.  Exact modular
   controls say no: the reduced local complexity grows with \(p\).

## Main Derivation

### Step 1. Classical Hénon map

With the convention

\[
p=-\partial_qS_0(q,Q),\qquad P=\partial_QS_0(q,Q),
\]

one obtains

\[
H_0(q,p)=(-6q^2-p,q),
\qquad
DH_0(q,p)=
\begin{pmatrix}-12q&-1\\1&0\end{pmatrix},
\qquad
\det DH_0=1.
\]

### Step 2. Intrinsic order-three symmetry

Let \(\zeta^3=1\).  Then

\[
S_0(\zeta q,\zeta^{-1}Q)=S_0(q,Q).
\]

On phase space put

\[
g(q,p)=(\zeta q,\zeta^{-1}p).
\]

Direct substitution gives

\[
H_0g=g^{-1}H_0.
\]

This is not an equivariant commuting symmetry of one Hénon step.  It is a
reversing order-three symmetry: one Hénon step exchanges the two nontrivial
characters, while two Hénon steps preserve every character sector.

### Step 3. Exact quantum relation

The operator \(U_p\) is a finite Fourier transform followed by multiplication
by \(e_p(2q^3)\), hence is unitary.  Substituting \(q=\zeta_pr\) gives

\[
U_pR_p=R_p^{-1}U_p.
\]

Consequently

\[
[T_p,R_p]=0,
\qquad T_p=U_p^2.
\]

Let \(\omega=e^{2\pi i/3}\) and

\[
\mathcal H_{p,k}=\ker(R_p-\omega^kI),\qquad k=0,1,2.
\]

The orbit decomposition of multiplication by \(\zeta_p\) on \(\mathbb F_p\)
has the fixed orbit \(\{0\}\) and \((p-1)/3\) free orbits, so

\[
d_{p,0}=\frac{p+2}{3},
\qquad
d_{p,1}=d_{p,2}=\frac{p-1}{3}.
\]

Moreover \(U_p:\mathcal H_{p,1}\to\mathcal H_{p,2}\) is a unitary
intertwiner for \(T_p\).  Hence

\[
T_{p,1}\simeq T_{p,2}
\]

unitarily, including multiplicities.

### Step 4. Integral augmentation superdeterminant

The complex color weights \((1,\omega,\omega^2)\) would require nonintegral
powers of determinants and would not define an ordinary single-valued
meromorphic function.  The canonical integral alternative is the augmentation
virtual representation

\[
(w_0,w_1,w_2)=(2,-1,-1).
\]

Define

\[
D_p^{\mathrm{aug}}(z)
=\prod_{k=0}^2\det(I-zT_{p,k})^{w_k}
=\frac{\det(I-zT_{p,0})^2}
{\det(I-zT_{p,1})\det(I-zT_{p,2})}.
\]

Since \(T_{p,1}\simeq T_{p,2}\),

\[
D_p^{\mathrm{aug}}(z)
=\left(
\frac{\det(I-zT_{p,0})}{\det(I-zT_{p,1})}
\right)^2.
\]

Its virtual dimension is

\[
2d_{p,0}-d_{p,1}-d_{p,2}=2.
\]

This number is only a virtual leading degree.  It does not imply cancellation
of the two high-degree characteristic polynomials.

There is nevertheless an all-prime leading invariant.  Write \(U_p=F_pM_p\),
with \(F_p\) the normalized Fourier transform and
\(M_p(q)=e_p(2q^3)\).  On every nonzero \(\mu_3\)-orbit the chirp is scalar,
and the product of these scalars is one because the sum of the cube subgroup
is zero.  Thus \(\det(M_p|\mathcal H_{p,k})=1\).  Also

\[
F_p^2=J,\qquad (Jf)(x)=f(-x).
\]

Since \(-1\) is a cube for \(p\equiv1\pmod3\), \(J\) preserves every grade.
Writing \(m=(p-1)/3\), the nonzero orbits form \(m/2\) pairs under negation,
so

\[
\det(T_{p,0})=\det(T_{p,1})=\det(T_{p,2})
=(-1)^{(p-1)/6}.
\]

Consequently, even after arbitrary common-factor cancellation,
\(D_{p,0}/D_{p,1}\) has degree difference one and tends to \(-z\) at
infinity, while

\[
D_p^{\mathrm{aug}}(z)\sim z^2.
\]

Thus the augmentation factor can never collapse to a constant.

### Step 5. Projector and chronological trace identity

Let

\[
P_k=\frac13\sum_{j=0}^2\omega^{-kj}R_p^j.
\]

Then the exact representation-ring identity

\[
2P_0-P_1-P_2=R_p+R_p^2
\]

gives, for every \(n\ge1\),

\[
A_{p,n}
:=2\operatorname{Tr}(T_{p,0}^n)
-\operatorname{Tr}(T_{p,1}^n)
-\operatorname{Tr}(T_{p,2}^n)
=\operatorname{Tr}\bigl((R_p+R_p^2)U_p^{2n}\bigr).
\]

Therefore, on \(|z|<1\),

\[
\log D_p^{\mathrm{aug}}(z)
=-\sum_{n\ge1}\frac{A_{p,n}}n z^n.
\]

Writing the kernel composition chronologically yields

\[
\operatorname{Tr}(R_p^jU_p^{2n})
=p^{-n}\sum_{x_0,\ldots,x_{2n-1}\in\mathbb F_p}
e_p\!\left(
\sum_{i=0}^{2n-1}(x_ix_{i+1}+2x_i^3)
\right),
\]

where the twisted closure is

\[
x_{2n}=\zeta_p^jx_0,
\qquad j=1,2.
\]

Thus chronology is retained exactly.  No averaged transition matrix replaces
the ordered Hénon kernel.

### Step 6. Uniform fixed-moment bound

For either twisted closure, the polynomial in \(2n\) variables has degree
three and leading homogeneous part

\[
2\sum_{i=0}^{2n-1}x_i^3.
\]

For \(p>3\), its partial derivatives are \(6x_i^2\) and have no common
projective zero.  Deligne's smooth-leading-form estimate therefore gives

\[
\left|\operatorname{Tr}(R_p^jU_p^{2n})\right|
\le 2^{2n}=4^n.
\]

Hence

\[
|A_{p,n}|\le2\cdot4^n,
\]

uniformly in every split prime \(p\).

The bound is deliberately coarse.  Its role is to prove a common analytic
half-plane, not to fit arithmetic coefficients.

### Step 7. Prime Euler superproduct

Freeze the canonical prime clock by

\[
\mathcal D_{\mu_3}(s)
=\prod_{\substack{p>3\\p\equiv1\ (3)}}
D_p^{\mathrm{aug}}\!\left(p^{-s}\right).
\]

For \(\sigma=\operatorname{Re}s>1\),

\[
\sum_{p\equiv1(3)}\sum_{n\ge1}
\frac{|A_{p,n}|}{n}p^{-n\sigma}
\le
2\sum_{p\equiv1(3)}\sum_{n\ge1}
\frac{(4p^{-\sigma})^n}{n}<\infty.
\]

The convergence is locally uniform on \(\operatorname{Re}s>1\).  Therefore
\(\mathcal D_{\mu_3}\) is holomorphic and nonzero there, with the displayed
trace-log as its canonical branch.

The optional display variable \(p^{1/2-s}\) shifts this theorem to
\(\operatorname{Re}s>3/2\) and puts the local unitary divisor on the critical
line.  That shift is useful for Route-A comparison but is not the canonical
unshifted Euler normalization.

### Step 8. Local divisor symmetry

Every \(T_{p,k}\) is unitary.  Hence all zeros and poles of the reduced local
factor lie on \(|z|=1\).  Under the optional coordinate
\(z=p^{1/2-s}\), the local divisor lies on

\[
\operatorname{Re}s=\frac12.
\]

There is an exact local reciprocal duality.  Writing \(U=FM\), symmetry of
the normalized Fourier kernel gives

\[
\overline U=F^{-1}M^{-1}=MU^{-1}M^{-1}.
\]

Because \(M\) commutes with \(R\), conjugation sends grade \(k\) to grade
\(-k\) and gives cross-grade similarity between
\(\overline{T_{p,k}}\) and \(T_{p,-k}^{-1}\).  Grade zero is self-dual; for
grades one and two, combine this relation with the independently proved
isospectrality \(D_{p,1}=D_{p,2}\).  The equal sector determinants and
dimension difference one then give, for

\[
G_p(z)=\frac{\det(I-zT_{p,0})}{\det(I-zT_{p,1})},
\]

the identities

\[
G_p(z)=-z\,\overline{G_p(1/\overline z)}
\]

and

\[
D_p^{\mathrm{aug}}(z)
=z^2\overline{D_p^{\mathrm{aug}}(1/\overline z)}.
\]

This is a local unitary symmetry centered on \(\operatorname{Re}s=1/2\), not
a global Riemann functional equation.  Substitution
\(z=p^{1/2-s}\) creates a factor \(p^{1-2s}\); its product over primes
diverges and no conductor or Gamma completion has been constructed.

### Step 9. Exact noncancellation gate

To avoid unreliable floating-point eigenvalue matching, reduce the entire
construction modulo an auxiliary prime

\[
\ell\equiv1\pmod{3p}.
\]

The field \(\mathbb F_\ell\) then contains exact roots of unity of orders
\(p\) and three.  Since \(T_p=U_p^2\), the factor \(p^{-1}\) is defined
without choosing a square root.  Sector bases and characteristic polynomials
can therefore be reconstructed exactly.

If the two sector characteristic polynomials are coprime after one good
reduction, they were coprime in characteristic zero.  The current control
ledger tests

\[
p\in\{7,13,19,31,37,43,61,67,73\}.
\]

For every control:

\[
\chi_{p,1}=\chi_{p,2},
\qquad
\gcd(\chi_{p,0},\chi_{p,1})=1.
\]

Thus the reduced numerator and denominator degrees are exactly

\[
2\frac{p+2}{3}
\quad\text{and}\quad
2\frac{p-1}{3}
\]

for these primes.  The net degree is two, but no local eigenvalue cancellation
occurs.

This finite ledger does not prove coprimality for every split prime.  It does
prove that the \(\mu_3\) representation theory alone cannot supply the hoped
for bounded-rank cancellation, and it exposes the exact gate required for a
global continuation theorem.

### Step 10. Exact conjugation obstruction at \(p=7\)

Take \(p=7\), \(\zeta_7=2\), and write
\(\xi=e^{2\pi i/7}\).  The first twisted trace is governed by

\[
2x^3+2y^3+3xy.
\]

Its exact residue histogram for residues \(0,\ldots,6\) is

\[
(4,9,18,3,6,6,3).
\]

Therefore

\[
A_{7,1}
=\frac{2}{7}\left(
4+9\xi+18\xi^2+3\xi^3+6\xi^4+6\xi^5+3\xi^6
\right).
\]

Subtracting the conjugate gives the coefficient vector

\[
(0,6,12,-3,3,-12,-6).
\]

If this vanished at \(\xi\), its degree-at-most-six polynomial over
\(\mathbb Q\) would be a scalar multiple of

\[
\Phi_7(X)=1+X+\cdots+X^6.
\]

The displayed coefficients are not constant, so

\[
A_{7,1}\notin\mathbb R.
\]

Since

\[
D_7^{\mathrm{aug}}(z)=1-A_{7,1}z+O(z^2),
\]

the coefficient of the unique prime label seven in the absolutely convergent
global expansion is nonreal.  Hence the raw product fails

\[
\mathcal D_{\mu_3}(\overline s)
=\overline{\mathcal D_{\mu_3}(s)}.
\]

Changing \(\zeta_7\) to its inverse does not repair the defect: the two
twisted traces are equal by the exact sector symmetry.

## Controls and Failed Variants

### Scalar cubic Kummer control

The cover

\[
u^3=2x^3
\]

becomes, after \(t=u/x\),

\[
t^3=2.
\]

It is a constant-field cover rather than a geometrically nontrivial Hénon
local system.  Likewise, for an order-three multiplicative character \(\chi\),

\[
\chi(2x^3)=\chi(2)
\]

on \(\mathbb G_m\).  The geometric scaling local system is constant; residual
arithmetic Frobenius may retain a constant-field factor, but that factor
carries no \(x\)-dependent Hénon chronology.  Any nontrivial prime weight in
this scalar model therefore comes from an externally supplied cubic
character.  This control is stopped.

### Complex color determinant control

Weights \((1,\omega,\omega^2)\) have virtual rank zero but require complex
powers of determinants.  They define a formal logarithm only after a branch
choice and are not an ordinary Fredholm/Berezinian determinant.  They are not
used.

### One-step grading control

The one-step operator \(U_p\) exchanges the nontrivial sectors.  Taking three
independent one-step determinants would erase this genuine chronology.  The
minimal sector-preserving time is exactly two Hénon steps.

## Claim Dependency Graph

\[
S_0\text{ symmetry}
\Longrightarrow U_pR_p=R_p^{-1}U_p
\Longrightarrow [U_p^2,R_p]=0
\Longrightarrow \mu_3\text{ sector decomposition}
\]

\[
\text{augmentation identity}
\Longrightarrow A_{p,n}=\operatorname{Tr}((R_p+R_p^2)U_p^{2n})
\Longrightarrow |A_{p,n}|\le2\cdot4^n
\Longrightarrow \mathcal D_{\mu_3}\text{ analytic on }\Re s>1.
\]

The local unitary divisor theorem and the global analytic-half-plane theorem
are independent of the finite coprimality controls.  Those controls address
the next global-continuation gate.

## Route-A Evaluation

- **A1: `A1_WEAK`.**  The prime clock and repetition are exact, and the
  ordered Hénon kernel is intrinsic, but primes are arithmetic fibers rather
  than classical primitive Hénon orbits.  There is no von-Mangoldt matching.
- **A2: `A2_ANALYTIC_DETERMINANT`.**  The rational local superdeterminants and
  the nonzero canonical Euler trace-log on \(\Re s>1\) are proved.
- **A3: `A3_FAIL`.**  Every local divisor is on the unit circle and, in the
  optional shifted coordinate, on the critical line; it has a reciprocal
  unitary relation, but the first global prime coefficient is
  exactly nonreal.  Thus the raw product fails conjugation symmetry; it also
  has no global functional equation or Gamma factor.
- **A4: `A4_NATURAL_QUANTIZATION`.**  \(U_p\) is a canonical unitary
  quantization of the Hénon generating kernel, and the two-step grading is
  forced by chronology.

Overall status: `ROUTE_A_REJECTED`.

Route B is not authorized.

## Decisive Next Gate

The raw single-character augmentation is stopped.  The companion C41--C42
chain also closes the obvious finite-dimensional Eisenstein repair: the
intrinsic \(j=0\) CM factor is arithmetic but not Hénon-native, and within
the finite span of its \(H^1\) and the two Tate pieces, matching the Riemann
local factor at three primes forces the CM coefficient to vanish.  There is
one larger replacement question left:

> After pairing \(\psi\) with \(\psi^{-1}\) and including split and inert
> places, can the two-step Hénon Fourier--Deligne moment sequences descend to
> a pure self-dual compatible system over a fixed coefficient field, with
> rank and conductor bounded
> independently of \(p\), with Frobenius power traces equal to the
> chronological augmentation moments?

A compatible system over one number field \(E\) first forces every paired
moment \(B_{\mathfrak p,1}=A_{\mathfrak p,1}(\psi)+
A_{\mathfrak p,1}(\psi^{-1})\) to have degree at most \([E:\mathbb Q]\).
Thus coefficient-field descent precedes operator rank.  If that gate
survives, a rank-\(R\) system forces every local moment sequence to satisfy a
recurrence of order at most \(R\), equivalently a uniform Hankel-rank bound.
The present coprimality ledger shows reduced degrees growing through
\(50/48\), but only at finitely many primes and before conjugate pairing.  The
next theorem is therefore staged but decisive: prove unbounded paired trace
degrees and stop; otherwise prove or refute uniform paired Hankel rank.
It is not enough to package each time \(n\) separately: those phase
cohomologies have rank \(4^n\).  Merely multiplying the raw product by its
conjugate repairs real-type symmetry but doubles local degree and supplies no
functional equation.
