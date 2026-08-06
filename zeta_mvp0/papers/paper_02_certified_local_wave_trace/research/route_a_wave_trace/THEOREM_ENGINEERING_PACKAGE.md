# Route A4 Theorem-Engineering Package

## 1. Outcome first

For the one-step scalar family

\[
 P_{a,\hbar}=-\frac{\hbar^2}{2}\Delta+V_a(q),
 \qquad
 V_a(q)=2\pi e^{\pi|\Psi_a(q)|^2},
\]

with

\[
 \Psi_a(x,y)=(-c_ax-ax^2-y,x),
 \qquad c_a=2(\sqrt{1+a}-1),
\]

there is a short, honest route from the existing operator family to a
**microlocally isolated nonzero-time semiclassical propagator-trace term**.  At the
flagship value \(a=1.02\), the relevant orbit is the fast Lyapunov family
born from the unique well bottom.  Its limiting period, action slope, and
stability determinant are explicit and are separated from the radial
reference return times.

The observable-localized intermediate route is denoted
\(P^*_{\mathrm{loc,obs}}\).  The full-shell blow-up and Poincaré-map argument
in Theorem A4.8 removes that observable for all sufficiently small fixed
positive energy excesses.  Consequently Theorem A4.9 closes a genuine
fixed-energy relative-spectral bridge, denoted \(P^*_{\mathrm{loc}}\), whose
input is only the two eigenvalue lists.  This remains a local semiclassical
periodic-orbit result; it does **not** close the high-energy arithmetic P
gate.

## 2. Claim-status convention

Every statement below is labelled as one of:

- **IDENTITY:** exact algebra or functional calculus;
- **PROPOSITION:** proved from stated hypotheses and standard cited theorems;
- **CONDITIONAL THEOREM:** conclusion is rigorous after the displayed
  microlocal hypotheses are verified;
- **NUMERICAL CERTIFICATE:** reproducible finite-precision evidence;
- **INTERPRETATION:** a research meaning, not a mathematical implication.

## 3. Exact geometric foundation

### Proposition A4.1 — regular compact energy shells

**Status: PROPOSITION.**  For every \(a>-1\), the classical Hamiltonian

\[
 h_a(q,p)=\frac{|p|^2}{2}+V_a(q)
\]

has exactly one critical point, \((q,p)=(0,0)\), at energy \(2\pi\).  Every
\(E>2\pi\) is a regular value, \(h_a^{-1}(E)\) is compact, and the flow is
complete on compact energy bands.

**Proof.**  The polynomial automorphism \(\Psi_a\) is proper.  Therefore
\(V_a(q)\to\infty\) as \(|q|\to\infty\).  Moreover,

\[
 \nabla V_a(q)=2\pi V_a(q)D\Psi_a(q)^T\Psi_a(q).
\]

Since \(D\Psi_a\) is invertible and \(\Psi_a(q)=0\) only at \(q=0\), the
potential has one critical point.  The momentum derivative is \(p\), so the
Hamiltonian has the stated unique critical point.  Properness gives
compactness; smoothness and compact energy confinement give completeness.

### Proposition A4.2 — exact shell volume

**Status: IDENTITY.**  Area preservation gives

\[
 \operatorname{vol}\{h_a<E\}
 =2\pi E\log\frac{E}{2\pi}-2\pi E+4\pi^2,
\]

and hence

\[
 \int_{h_a=E}\frac{d\Sigma}{|\nabla h_a|}
 =2\pi\log\frac{E}{2\pi}.
\]

Both expressions are independent of \(a\).  This is the classical origin of
the common two-term clock.  It does not imply equality of quantum spectra.

## 4. Exact relative localized trace

Fix \(\chi\in C_c^\infty((2\pi,\infty))\).  For \(j\in\{0,a\}\), write
\(N_{j,\hbar}\) for the counting function and

\[
 \xi_\hbar(E)=N_{0,\hbar}(E)-N_{a,\hbar}(E).
\]

Define

\[
 W_{\mathrm{rel},\hbar}^{\chi}(t)
 =\operatorname{Tr}\!\left[
 \chi(P_{a,\hbar})^2e^{-itP_{a,\hbar}/\hbar}
 -\chi(P_{0,\hbar})^2e^{-itP_{0,\hbar}/\hbar}
 \right].
\]

### Proposition A4.3 — finite-rank trace and staircase identity

**Status: IDENTITY.**  Each cutoff is finite rank, so the displayed trace is
an ordinary finite sum.  Stieltjes integration gives

\[
 \boxed{
 W_{\mathrm{rel},\hbar}^{\chi}(t)
 =\int_{\mathbb R}
 \left[(\chi^2)'(E)-\frac{it}{\hbar}\chi(E)^2\right]
 e^{-itE/\hbar}\xi_\hbar(E)\,dE.}
\]

No first-resolvent trace-class assumption is used.

With the Fourier convention

\[
 \widehat g(t)=\int e^{-its}g(s)\,ds,
 \qquad
 g(s)=\frac1{2\pi}\int e^{its}\widehat g(t)\,dt,
\]

put

\[
 \rho_{\mathrm{rel},\hbar}(E;g)
 =\operatorname{Tr}\!\left[
 \chi(P_{a,\hbar})^2g\!\left(\frac{E-P_{a,\hbar}}\hbar\right)
 -\chi(P_{0,\hbar})^2g\!\left(\frac{E-P_{0,\hbar}}\hbar\right)
 \right].
\]

Then

\[
 \boxed{
 \rho_{\mathrm{rel},\hbar}(E;g)
 =\frac1{2\pi}\int
 \widehat g(t)e^{itE/\hbar}
 W_{\mathrm{rel},\hbar}^{\chi}(t)\,dt.}
\]

Choosing \(0\notin\operatorname{supp}\widehat g\) removes all distributions
supported only at zero time; it is stronger and cleaner than hoping for a
numerical cancellation of a large \(t=0\) peak.

## 5. Exact bottom normal form

At the equilibrium,

\[
 D\Psi_a(0)=A_a=
 \begin{pmatrix}-c_a&-1\\1&0\end{pmatrix},
 \qquad
 D^2V_a(0)=4\pi^2A_a^TA_a.
\]

Let \(0<s_-<s_+\) be the singular values of \(A_a\).  Since
\(\det A_a=1\),

\[
 s_+s_-=1,
 \qquad
 s_\pm=\frac{\sqrt{c_a^2+4}\pm|c_a|}{2}.
\]

The normal frequencies and periods are

\[
 \omega_\pm=2\pi s_\pm,
 \qquad
 T_\pm^0=\frac{2\pi}{\omega_\pm}=s_\pm^{-1}.
\]

For \(a\ne0\), the frequencies are distinct.  Put

\[
 \rho_a=\frac{\omega_+}{\omega_-}
 =\frac{s_+}{s_-}=s_+^2>1.
\]

### Proposition A4.4 — fast Lyapunov family

**Status: PROPOSITION; LYAPUNOV-CENTRE HYPOTHESES VERIFIED.**  For every
\(a>-1\), \(a\ne0\), a family of periodic trajectories \(\gamma_+(E)\)
emanates from the fast normal mode as \(E\downarrow2\pi\).  Its period obeys

\[
 T_+(E)\longrightarrow T_+^0=s_-.
\]

The linearized Hamiltonian vector field has the two simple pairs

\[
 \pm i\omega_-,\qquad \pm i\omega_+.
\]

For the selected fast pair, the exact nonresonance check is

\[
 \frac{\pm i\omega_-}{i\omega_+}
 =\pm\frac1{\rho_a}\notin\mathbb Z,
 \qquad 0<\frac1{\rho_a}<1.
\]

Thus the classical Lyapunov centre theorem applies in precisely the form
stated in Section 4 of Alligood--Yorke (1986); Weinstein's normal-mode
theorem gives the broader Hamiltonian context.  If \(A>0\) denotes the fast
normal-coordinate amplitude, then

\[
 E(A)-2\pi=\frac12\omega_+^2A^2+O(A^3)>0
\]

for all sufficiently small \(A\).  Consequently the branch may be indexed
by every sufficiently small positive energy excess, rather than merely by
an abstract bifurcation parameter.

The reduced transverse multipliers converge to

\[
 \exp\!\left(\pm 2\pi i\frac{\omega_-}{\omega_+}\right)
 =\exp\!\left(\pm\frac{2\pi i}{\rho_a}\right),
\]

so the branch is Poincaré nondegenerate for all sufficiently small positive
energy excess.  Its stability determinant has the nonzero limit

\[
 D_+^0
 =\lim_{E\downarrow2\pi}|\det(I-P_{\gamma_+(E)})|
 =4\sin^2\!\frac{\pi}{\rho_a}.
\]

The action \(S_+(E)=\oint_{\gamma_+(E)}p\,dq\), normalized by
\(S_+(2\pi)=0\), satisfies

\[
 \frac{dS_+}{dE}=T_+(E),
 \qquad
 S_+(E)=T_+^0(E-2\pi)+o(E-2\pi).
\]

### Proposition A4.5 — first nonlinear period coefficient

**Status: PROPOSITION; ANALYTIC DERIVATION INDEPENDENTLY AUDITED.**  In
orthonormal normal coordinates \((Q_-,Q_+)\), let

\[
 C_{ijk}=\partial_{Q_iQ_jQ_k}V_a(0),
 \qquad
 D_{ijkl}=\partial_{Q_iQ_jQ_kQ_l}V_a(0).
\]

For \(j\in\{-,+\}\), define

\[
 b_{j0}=-\frac{C_{++j}}{4\omega_j^2},
 \qquad
 b_{j2}=-\frac{C_{++j}}
 {4(\omega_j^2-4\omega_+^2)},
\]

and

\[
 \nu_+=\frac1{2\omega_+}
 \left[
 \frac{D_{++++}}8+
 \sum_{j\in\{-,+\}}C_{++j}
 \left(b_{j0}+\frac12b_{j2}\right)
 \right].
\]

For completeness, take \(\tau=\Omega t\) and write

\[
 Q_+=A\cos\tau
 +A^2(b_{+0}+b_{+2}\cos2\tau)+O(A^3),
\]

\[
 Q_-=A^2(b_{-0}+b_{-2}\cos2\tau)+O(A^3),
 \qquad
 \Omega=\omega_++\nu_+A^2+O(A^3).
\]

The constant and second-harmonic equations at order \(A^2\) give the two
displayed formulas for \(b_{j0}\) and \(b_{j2}\).  The coefficient of the
resonant \(A^3\cos\tau\) term is zero exactly when

\[
 -2\omega_+\nu_+
 +\frac{D_{++++}}8
 +\sum_{j\in\{-,+\}}C_{++j}
 \left(b_{j0}+\frac12b_{j2}\right)=0.
\]

This proves the displayed expression for \(\nu_+\).  Since

\[
 E-2\pi=\frac12\omega_+^2A^2+o(A^2),
 \qquad T=\frac{2\pi}{\Omega},
\]

differentiation gives

\[
 \boxed{
 \left.\frac{dT_+}{dE}\right|_{2\pi+}
 =-\frac{2T_+^0\nu_+}{\omega_+^3}.}
\]

For \(a=1.02\), the deterministic normal-coordinate convention used in the
code gives

\[
 \nu_+=17.52709598189346,
\]

and hence

\[
 \boxed{
 T_+(2\pi+\delta)
 =0.6638439766792985
 -0.0274450756283701\,\delta+o(\delta),}
\]

\[
 \boxed{
 \frac{S_+(2\pi+\delta)}{\delta}
 =0.6638439766792985
 -0.0137225378141851\,\delta+o(\delta).}
\]

The limiting geometric orbit amplitude, before translating the Fourier
normalization, the test function, and the Maslov phase, is

\[
 \frac{T_+^0}{\sqrt{D_+^0}}
 =0.3377686126427769.
\]

With the project convention

\[
 \widehat g(t)=\int e^{-its}g(s)\,ds,
 \qquad
 g(s)=\frac1{2\pi}\int e^{its}\widehat g(t)\,dt,
\]

the corresponding spectral-density amplitude contains one further
factor \(1/(2\pi)\):

\[
 \frac{T_+^0}{2\pi\sqrt{D_+^0}}
 =0.0537575443233896.
\]

## 6. Removing the radial reference from one time window

The radial control has an isotropic linearization of period one.  This gives
a useful local theorem that is much stronger than visually comparing two
wave traces.

### Proposition A4.6 — radial return exclusion near the bottom

**Status: PROPOSITION; COMPACTNESS PROOF.**  Let
\(J\Subset\mathbb R\setminus\mathbb Z\).  There exists \(\delta_J>0\) such
that the radial flow has no nonstationary closed trajectory with

\[
 2\pi<E<2\pi+\delta_J,
 \qquad T\in J.
\]

**Proof architecture.**  Rescale \(q=\sqrt\delta Q\) and
\(p=\sqrt\delta P\) on \(E=2\pi+\delta\).  The exact rescaled shell is

\[
 K_\delta=\left\{(Q,P):
 \frac{|P|^2}{2}
 +\frac{2\pi}{\delta}
 \left(e^{\pi\delta|Q|^2}-1\right)=1\right\}.
\]

Because \(e^x-1\ge x\), every such shell lies in the fixed compact set

\[
 |P|\le\sqrt2,
 \qquad |Q|\le\frac1{\sqrt2\,\pi}.
\]

The rescaled vector field is

\[
 F_\delta(Q,P)
 =\left(P,-4\pi^2e^{\pi\delta|Q|^2}Q\right),
\]

which converges in \(C^1\), on a fixed compact neighborhood of the shells,
to

\[
 F_0(Q,P)=(P,-4\pi^2Q).
\]

Suppose the conclusion were false.  Then there would be
\(\delta_n\downarrow0\), \(Z_n\in K_{\delta_n}\), and \(T_n\in J\) with
\(\Phi_{\delta_n}^{T_n}(Z_n)=Z_n\).  After passing to a subsequence,

\[
 Z_n\to Z_*\in K_0,
 \qquad T_n\to T_*\in J.
\]

In particular \(Z_*\ne0\).  Continuous dependence of bounded-time flows on
the vector field and initial condition yields

\[
 \Phi_0^{T_*}(Z_*)=Z_*.
\]

But \(F_0\) is the isotropic oscillator of angular frequency \(2\pi\), so a
nonzero point returns exactly at integer times.  This contradicts
\(J\cap\mathbb Z=\varnothing\) and proves the proposition.

For \(a=1.02\), take the prospective interval

\[
 J=[0.60,0.75].
\]

It contains \(T_+^0=0.6638439767\) and is disjoint from every integer.  By
continuity, the fast Hénon branch remains in \(J\) for small \(\delta\),
whereas the radial reference has no return in \(J\).

The proposition supplies an unspecified sufficiently small \(\delta_J\).
It does **not** certify radial exclusion at the largest R400 continuation
cells, in particular \(\delta=0.40\); those cells are numerical stress tests
of the warped branch only.

### Corollary A4.6b — radial exclusion through the full short-time range

For every \(0<T_{\max}<1\), there is \(\bar\delta(T_{\max})>0\) such that the
radial shell \(h_0=2\pi+\delta\), \(0<\delta<\bar\delta\), has no return with

\[
 0<|T|\le T_{\max}.
\]

Indeed, the preceding compactness argument applies unless \(T_n\to0\).  In
that remaining case,

\[
 0=\frac{\Phi_{\delta_n}^{T_n}(Z_n)-Z_n}{T_n}
 =\frac1{T_n}\int_0^{T_n}
 F_{\delta_n}(\Phi_{\delta_n}^s(Z_n))\,ds
 \longrightarrow F_0(Z_*).
\]

This is impossible on the shell \(\{K_0=1\}\), because the harmonic vector
field vanishes only at the origin.  If the limiting time is positive, the first nonzero
return of the radial limiting oscillator is \(1>T_{\max}\).  We will use
this with \(T_{\max}=0.75\) when checking the global trace hypotheses.

### Proposition A4.11a — quantitative radial exclusion through \(\delta=0.010201\)

**Status: PROVED.**  The nonquantitative radial threshold above can be made
explicit for the R401 energy.  Every nonconstant \(T\)-periodic solution of
\(q''=-\nabla V(q)\) contained in a convex set on which
\(\|\nabla^2V\|_{\rm op}\le L\) satisfies

\[
 T\ge\frac{2\pi}{\sqrt L}.
\]

Indeed, subtract the time average of \(q\), integrate the equation by parts,
use the \(L\)-Lipschitz property of \(\nabla V\), and then apply the periodic
Wirtinger inequality.  For
\(V_0(q)=2\pi e^{\pi|q|^2}\) on the shell \(h_0=E\),

\[
 \|\nabla^2V_0(q)\|_{\rm op}
 \le E\left(2\pi+4\pi\log\frac{E}{2\pi}\right).
\]

Thus, uniformly for \(2\pi<E\le2\pi+0.010201\),

\[
 T\ge
 \frac{2\pi}{\sqrt{(2\pi+0.010201)(2\pi+0.020402)}}>0.99>0.75,
\]

where \(\log(1+x)\le x\) was used in the middle estimate.  Consequently
\(\bar\delta(0.75)\ge0.010201\).  The complete proof and scope boundary are in
`A411_RADIAL_PERIOD_BOUND.md`.

### Proposition A4.11b — quantitative warped period floor through \(\delta=0.010201\)

**Status: PROVED; INDEPENDENT FOCUSED AUDIT ACCEPT.**  The inverse Hénon map
places every warped allowed configuration for
\(0<\delta\le0.010201\) inside the explicit convex box

\[
 |x|<0.02274,
 \qquad |y|<0.042427.
\]

On this whole box, outward rational estimates of
\(D\Psi_a\), \(\Psi_a\), and the exponential factor give

\[
 \|\nabla^2V_a\|_{\rm op}<102.494<103.
\]

The same vector Wirtinger inequality therefore yields

\[
 T\ge\frac{2\pi}{\sqrt{103}}>0.60
\]

for every nonconstant warped periodic orbit in the complete energy band.
Thus the validated whole-shell computation need cover only
\(0.60\le T\le0.75\).  The complete outward arithmetic and the convex-domain
qualification are in `A411_WARPED_PERIOD_FLOOR.md`; this does not itself
exclude additional returns in the remaining interval.

## 7. Local relative Gutzwiller bridge

Let \(E=2\pi+\delta\) be sufficiently close to the bottom and let
\(\gamma_+(E)\) be the fast branch.  Fix the precise trace data

\[
 \chi\in C_c^\infty(\mathbb R;\mathbb R),
 \qquad \chi\equiv1\ \text{near }E,
\]

\[
 A\in C_c^\infty(T^*\mathbb R^2;\mathbb R),
 \qquad A_\hbar=\operatorname{Op}_\hbar^w(A),
\]

where \(A=1\) on \(\gamma_+(E)\) and its support is a small phase-space
neighborhood of that orbit.  Choose

\[
 \widehat g\in C_c^\infty(J),\qquad g\in\mathcal S(\mathbb R),
 \qquad
 \widehat g(T_+(E))\ne0.
\]

Define the observable-localized relative density explicitly by

\[
 \begin{aligned}
 \rho_{\mathrm{rel},\hbar}^{A}(E;g)
 ={}&\operatorname{Tr}\!\left[
 \chi(P_{a,\hbar})A_\hbar\chi(P_{a,\hbar})
 g\!\left(\frac{E-P_{a,\hbar}}\hbar\right)\right]\\
 &-\operatorname{Tr}\!\left[
 \chi(P_{0,\hbar})A_\hbar\chi(P_{0,\hbar})
 g\!\left(\frac{E-P_{0,\hbar}}\hbar\right)\right].
 \end{aligned}
\]

The quantifier order is essential.  The target states that there exists
\(\delta_0>0\) such that, for each **fixed**
\(0<\delta<\delta_0\), one first chooses
\(\chi_\delta,A_\delta,\widehat g_\delta\) and only then lets
\(\hbar\downarrow0\).  No uniform joint limit
\((\delta,\hbar)\to(0,0)\) is asserted.

### Theorem target A4.7 — one-orbit relative trace

**Status: CONDITIONAL THEOREM, WITH STANDARD MICROLOCAL INPUT.**  Assume the
actual stationary set in the selected symbol and time supports is

\[
 \begin{aligned}
 \{(z,t):\;&z\in\Sigma_{a,E}\cap\operatorname{supp}A,
 \qquad t\in\operatorname{supp}\widehat g,\qquad
 \Phi_a^t(z)=z\}\\
 &=\{(\gamma_+(s),T_+(E)):
 s\in\mathbb R/T_+(E)\mathbb Z\}.
 \end{aligned}
\]

Assume this fixed-point cylinder is clean and transversally nondegenerate.
This formulation is stronger and more precise than saying that a tube
“contains no other orbit”: an orbit that merely intersects
\(\operatorname{supp}A\) can contribute.  Under these hypotheses the
fixed-energy semiclassical trace expansion gives

\[
 \boxed{
 \rho_{\mathrm{rel},\hbar}^{A}(E;g)
 =\widehat g(T_+(E))
 \frac{T_+^{\#}(E)}
 {2\pi\sqrt{|\det(I-P_+(E))|}}
 e^{i(S_+(E)/\hbar+\pi\sigma_+^{\mathrm{CRR}}(E)/2)}
 +O_{\delta,\chi,A,g}(\hbar).}
\]

The radial contribution is \(O(\hbar^\infty)\) by Proposition A4.6 and
nonstationary phase.  Here \(\sigma_+^{\mathrm{CRR}}\) denotes the specific
Maslov convention of Combescure--Ralston--Robert (CRR); it is intentionally
not identified with an unsigned generic Maslov or Conley--Zehnder index.

CRR's Theorem 2.3 supplies the displayed coefficient under its global
discreteness and nondegeneracy hypotheses for all periodic orbits up to the
Fourier time bound.  Its Remark 2.5 admits smooth Schrödinger potentials on
compact energy surfaces below \(\liminf_{|q|\to\infty}V(q)\), so exponential
growth of this well is not an obstruction at fixed energy.  To use only the
local stationary-set hypothesis displayed above, the manuscript must still
write a microlocal corollary of CRR's stationary-phase proof showing that
the symbol support removes the unused global fixed sets.  Thus A4.7 is not
yet advertised as a literal direct application under local assumptions
alone.

The observable localization is deliberate.  It makes the first rigorous
target one certified orbit rather than an unproved global census.  Removing
the observable requires a global finite-orbit/nondegeneracy audit or a clean
trace formula for all remaining families.

### Spectral boundary of A4.7

With the observable inserted, the spectral representation contains

\[
 \sum_k\chi(\lambda_{j,k})^2
 g\!\left(\frac{E-\lambda_{j,k}}\hbar\right)
 \langle\psi_{j,k},A_\hbar\psi_{j,k}\rangle.
\]

It therefore depends on eigenfunctions as well as eigenvalues.  Proposition
A4.3 does not turn A4.7 into an identity involving \(\xi_\hbar\) alone.  The
current result is a legitimate observable-localized propagator trace, not a
proof that the unobserved relative spectral wave trace exposes the orbit.

### Theorem target A4.8 — remove the observable

**Status: PROVED FULL-SHELL UNIQUENESS THEOREM.**  Let \(a=1.02\) and
\(T_{\max}=0.75\).  There exists \(\delta_*>0\) such that, for every
\(0<\delta<\delta_*\),

\[
 h_a(z)=2\pi+\delta,\qquad
 0<T\le T_{\max},\qquad
 \Phi_a^T(z)=z
\]

holds if and only if \(z\) lies on the fast Lyapunov orbit
\(\gamma_+(2\pi+\delta)\) and
\(T=T_+(2\pi+\delta)\).  In particular this return is primitive and the
geometric orbit is unique modulo time translation.

**Proof, Step 1: blow up the complete shell.**  Put
\(\epsilon=\sqrt\delta\), \(q=\epsilon Q\), \(p=\epsilon P\), and

\[
 K_\epsilon(Q,P)
 =\frac{h_a(\epsilon Q,\epsilon P)-2\pi}{\epsilon^2}.
\]

Physical time is unchanged and the rescaled equations are Hamilton's
equations for \(K_\epsilon\).  Writing

\[
 \Psi_a(\epsilon Q)
 =\epsilon\bigl(A_aQ+\epsilon B_a(Q)\bigr),
 \qquad B_a(Q)=(-aQ_x^2,0),
\]

gives

\[
 K_\epsilon
 =\frac{|P|^2}{2}
 +\frac{2\pi}{\epsilon^2}
 \left[
 e^{\pi\epsilon^2|A_aQ+\epsilon B_a(Q)|^2}-1
 \right].
\]

It extends smoothly through \(\epsilon=0\), with

\[
 K_0(Q,P)=\frac{|P|^2}{2}+2\pi^2|A_aQ|^2.
\]

The normalized shells are \(\Sigma_\epsilon=\{K_\epsilon=1\}\).  They all
lie in one compact set.  To see this globally rather than only near the
chosen orbit, the original energy equation gives

\[
 |\Psi_a(q)|^2
 \le\frac1\pi\log\left(1+\frac{\epsilon^2}{2\pi}\right)=O(\epsilon^2),
 \qquad |p|\le\sqrt2\,\epsilon,
\]

and the exact inverse

\[
 \Psi_a^{-1}(u,v)=(v,-c_av-av^2-u)
\]

then gives \(|q|=O(\epsilon)\) uniformly over the whole shell.  Hence, on a
common compact neighborhood,

\[
 K_\epsilon\to K_0\quad\text{in }C^2,\qquad
 X_{K_\epsilon}\to X_{K_0}\quad\text{in }C^1.
\]

**Step 2: classify every possible limiting return.**  In orthogonal normal
coordinates,

\[
 K_0=\frac12\left(
 P_-^2+\omega_-^2Q_-^2+P_+^2+\omega_+^2Q_+^2\right).
\]

At \(a=1.02\),

\[
 T_+^0=0.6638439766792985,\qquad
 T_-^0=1.5063780573896775,\qquad
 2T_+^0>0.75.
\]

Suppose \(\epsilon_n\downarrow0\), \(Z_n\in\Sigma_{\epsilon_n}\), and
\(0<T_n\le0.75\) are returns.  Compactness and bounded-time flow convergence
give, after a subsequence,

\[
 Z_n\to Z_0\in\Sigma_0,\qquad T_n\to T_*.
\]

The same averaged-vector-field argument, now applied to
\(X_{K_{\epsilon_n}}\), excludes \(T_*=0\): smooth convergence and
\(\{K_0=1\}\cap\{X_{K_0}=0\}=\varnothing\) would otherwise give a
contradiction.  For \(T_*>0\), the slow component cannot return before
\(T_-^0>0.75\), while the only fast return in the interval is \(T_+^0\).
Therefore

\[
 T_*=T_+^0,\qquad
 Z_0\in\Gamma_0:=\Sigma_0\cap\{Q_-=P_-=0\}.
\]

The circle \(\Gamma_0\) is one geometric orbit, not a continuum of distinct
orbits.

**Step 3: local uniqueness modulo phase.**  Choose the positive fast turning
point

\[
 z_*=(Q_-=P_-=P_+=0,\ Q_+=\sqrt2/\omega_+)
\]

and a sufficiently small neighborhood of \(z_*\) in the varying sections

\[
 \mathcal S_\epsilon
 =\{K_\epsilon=1,\ P_+=0,\ Q_+>0\}.
\]

At the limiting turning point,

\[
 \partial_{Q_+}K_0(z_*)=\sqrt2\,\omega_+\ne0,\qquad
 \dot P_+(z_*)=-\sqrt2\,\omega_+\ne0.
\]

The first inequality lets the energy equation solve for \(Q_+\); the second
gives flow transversality.  After identifying the varying sections by
\((Q_-,P_-)\), their first-return maps \(\Pi_\epsilon\) form a smooth
family.  In normalized slow coordinates

\[
 x_-=\sqrt{\omega_-}Q_-,\qquad
 y_-=\frac{P_-}{\sqrt{\omega_-}},
\]

the limiting derivative is exactly

\[
 D\Pi_0(z_*)=R_{2\pi/\rho_a};
\]

equivalently, the derivative in raw \((Q_-,P_-)\) coordinates is
symplectically conjugate to this rotation.  Thus

\[
 \det(I-D\Pi_0(z_*))
 =4\sin^2\frac{\pi}{\rho_a}
 =3.8627220445155036>0.
\]

The implicit-function theorem produces one and only one nearby fixed point
of \(\Pi_\epsilon\), hence one nearby periodic orbit modulo phase.  By the
Lyapunov-centre construction it is \(\gamma_+(2\pi+\epsilon^2)\).
Moreover \(T_+(2\pi+\epsilon^2)\to T_+^0\).  Shrinking \(\delta_*\) if
necessary gives, throughout the theorem's range,

\[
 0<T_+(2\pi+\delta)<0.75<2T_+(2\pi+\delta).
\]

**Step 4: exclude iterates and globalize.**  If a return \(T_n\) were the
\(m_n\)-fold iterate of a primitive period \(\tau_n\), then \(m_n\to\infty\)
would force \(\tau_n\to0\), contradicting the same averaged-vector-field
argument.  Hence \((m_n)\) is bounded.  Along a subsequence with \(m_n=m\),
flow convergence gives

\[
 \Phi_0^{T_+^0/m}(Z_0)=Z_0.
\]

Because \(Z_0\in\Gamma_0\), this is impossible unless \(m=1\).

If a second orbit nevertheless existed for a sequence
\(\epsilon_n\downarrow0\), bounded-time \(C^1\) flow convergence would
upgrade Step 2 to uniform convergence of the complete phase-aligned
trajectories over their periods to \(\Gamma_0\).  After a time shift, each
trajectory therefore intersects \(\mathcal S_{\epsilon_n}\) in the local
domain of \(\Pi_{\epsilon_n}\).  The return is primitive by the preceding
paragraph, so this intersection is a fixed point of the local first-return
map.  Step 3 says that the only such point is the continued fast point, a
contradiction.  This proves the theorem.

### Theorem A4.9 — eigenvalue-only local relative trace

**Status: THEOREM VIA THE FINITE-TIME COMBESCURE--RALSTON--ROBERT
COROLLARY.**  Let \(\delta_{\mathrm{nd}}>0\) be a
transverse-nondegeneracy threshold from Proposition A4.4 and define

\[
 \delta_{\mathrm{tr}}
 =\min\{\delta_*,\bar\delta(0.75),\delta_{\mathrm{nd}}\}.
\]

Fix \(0<\delta<\delta_{\mathrm{tr}}\), put \(E=2\pi+\delta\), and choose

\[
 \chi\in C_c^\infty(\mathbb R;\mathbb R),\qquad
 \chi\equiv1\ \text{near }E,
\]

with support in a sufficiently small compact regular energy band.  Take

\[
 \widehat g\in C_c^\infty((0,0.75)),\qquad
 \operatorname{supp}\widehat g\ \text{concentrated near }T_+(E),
 \qquad \widehat g(T_+(E))\ne0.
\]

Then the **unobserved** relative density from Proposition A4.3 satisfies

\[
 \boxed{
 \rho_{\mathrm{rel},\hbar}(E;g)
 =\widehat g(T_+(E))
 \frac{T_+^{\#}(E)}
 {2\pi\sqrt{|\det(I-P_+(E))|}}
 e^{i(S_+(E)/\hbar+\pi\sigma_+^{\mathrm{CRR}}(E)/2)}
 +O_{\delta,\chi,g}(\hbar).}
\]

The finite-time corollary used here follows directly from the
stationary-phase proof of CRR Theorem 2.3: when
\(\operatorname{supp}\widehat g\subset[-T_0,T_0]\), the discreteness of
geometric periodic orbits modulo time translation and their transverse
nondegeneracy are needed only for \(0<|T_\gamma|\le T_0\), because the trace
integral has no time support elsewhere.  The corresponding flow fixed
components are clean one-dimensional orbit components, not isolated points.
We apply this corollary with
\(T_0=0.75\); no claim about longer warped periods is required.

To match the remaining hypotheses, Proposition A4.1 gives a compact regular
energy band.  Theorem A4.8 says that every orbit with
\(0<|T|\le0.75\) is the fast orbit or its negative-time orientation and is
transversally nondegenerate; hence CRR hypotheses H.2--H.3 hold up to the
Fourier time bound.  Corollary A4.6b gives an empty radial periodic set in
the same range.  CRR Remark 2.5 permits the smooth exponential potential on
these compact energy surfaces.  Finally, all zero-time coefficients vanish
against \(\widehat g\), whose support avoids zero.

No observable occurs in this formula.  It is therefore determined by the
two eigenvalue lists and, through Proposition A4.3, by the relative counting
staircase \(\xi_\hbar\).

### Proposition A4.10 — explicit CRR phase

**Status: PROVED BY THE EXACT HARMONIC TRACE AND NONDEGENERATE
CONTINUATION.**  CRR equations (58) leave, in two configuration dimensions,

\[
 \sigma_\gamma\in\{1+\sigma',3+\sigma'\},
\]

where \(\sigma'\) counts real reduced multipliers greater than one.  The
near-bottom fast orbit is elliptic, so \(\sigma'=0\).  At the harmonic limit
the Abel-regularized exact transverse quantum sum is

\[
 \lim_{r\uparrow1}\sum_{m=0}^\infty
 r^m e^{-i\theta_0(m+1/2)}
 =\frac{e^{-i\theta_0/2}}{1-e^{-i\theta_0}}
 =-\frac{i}{2\sin(\theta_0/2)},
 \qquad \theta_0=\frac{2\pi}{\rho_a}\in(0,2\pi),
\]

while Poisson summation in the fast quantum number gives the positive
once-traversed coefficient

\[
 -\frac1{\omega_+}=-\frac{T_+^0}{2\pi}.
\]

After stripping off the positive real Jacobian \(1/\omega_+\), its phase is
\(e^{-i\pi}=-1\).  Multiplication by the transverse phase \(-i\) gives
\(+i\).  Hence

\[
 \boxed{
 \sigma_+^{\mathrm{CRR}}\equiv1\pmod4,\qquad
 e^{i\pi\sigma_+^{\mathrm{CRR}}/2}=i.}
\]

The reduced determinant stays nonzero on the sufficiently small nonlinear
branch, so the metaplectic phase is constant under continuation.  The
negative-time orientation has the conjugate phase and index \(3\bmod4\).
The same exact oscillator calculation also locks the absolute
normalization: the longitudinal Poisson Jacobian
\(1/\omega_+=T_+^0/(2\pi)\) is already the entire longitudinal
orbit-measure contribution and must not be multiplied by a second period.
Thus, in the project Fourier convention, the positive-time A4.9 formula is
explicitly

\[
 \boxed{
 \rho_{\mathrm{rel},\hbar}(E;g)
 =i\,\widehat g(T_+(E))
 \frac{T_+(E)}
 {2\pi\sqrt{|\det(I-P_+(E))|}}
 e^{iS_+(E)/\hbar}
 +O_{\delta,\chi,g}(\hbar).}
\]

The full convention audit is recorded in CRR_PHASE_INDEX.md.

## 8. R400 certificate

**Status: NUMERICAL CERTIFICATE.**  R400 continued the fast reversible orbit
at

\[
 \delta\in\{0.01,0.02,0.05,0.10,0.20,0.40\}.
\]

All six cells passed the frozen closure, energy, symplectic, and
nondegeneracy gates.  The three-cell small-energy extrapolations returned:

| Quantity | Fitted | Analytic | Absolute error |
|---|---:|---:|---:|
| \(T_+^0\) | 0.663843973386761 | 0.663843976679299 | \(3.29\times10^{-9}\) |
| \(dT_+/dE\) | -0.0274445154485 | -0.0274450756284 | \(5.60\times10^{-7}\) |
| \(\lim S/\delta\) | 0.663843975854219 | 0.663843976679299 | \(8.25\times10^{-10}\) |
| \(d(S/\delta)/d\delta\) | -0.0137223974763 | -0.0137225378142 | \(1.40\times10^{-7}\) |
| \(D_+^0\) | 3.86272204305148 | 3.86272204451550 | \(1.46\times10^{-9}\) |

The independent checker reimplemented the potential, shooting, variational
flow, and action without importing the project package.  At \(\delta=0.05\)
its period, action, initial state, and stability determinant agreed with the
production path to \(10^{-15}\)-scale absolute differences.

Numerical agreement is not used to prove Proposition A4.5 or Theorem A4.7.
It is a high-sensitivity audit of their formulas and conventions.

## 9. R401-SC eigenvalue-only trace audit

**Status: NUMERICAL CERTIFICATE; ALL FROZEN GATES PASS.**  At
\(\delta=0.01\), R401-SC uses the immutable R400 values

\[
 T=0.6635697917937936,
 \quad S=0.006637068399523644,
 \quad D=3.863271395157721,
\]

and the A4.10 oracle

\[
 \rho_{\rm pred}(\hbar)
 =i\frac{T}{2\pi\sqrt D}e^{iS/\hbar}.
\]

The energy and time cutoffs, coefficient, phase, and eight-point ladder were
fixed before the production archive.  No phase, scale, offset, peak time,
prime, or zero was fitted.  Original-coordinate Hermite functions were
explicitly rejected because the warped \(e^{c x^4}\) tail puts them outside
the potential form domain.  The accepted solver first applies the exact
unitary change \(u=\Psi_a(q)\), after which the potential has quadratic
exponential tails and the kinetic energy is a polynomial divergence form.
An independent angular-momentum Laguerre decomposition checks the radial
reference.

Writing \(Z_\hbar=\rho_{\rm rel,\hbar}/\rho_{\rm pred}(\hbar)\), the frozen
results are:

| \(\hbar\) | \(Z_\hbar\) | \(|Z_\hbar-1|\) |
|---:|---:|---:|
| \(4.0\times10^{-4}\) | \(0.344728+0.367872i\) | 0.7515 |
| \(3.0\times10^{-4}\) | \(1.448682+0.095288i\) | 0.4587 |
| \(2.0\times10^{-4}\) | \(0.317529+0.242788i\) | 0.7244 |
| \(1.5\times10^{-4}\) | \(1.403014-0.489353i\) | 0.6339 |
| \(1.0\times10^{-4}\) | \(0.843838-0.354104i\) | 0.3870 |
| \(7.5\times10^{-5}\) | \(0.785322+0.054500i\) | 0.2215 |
| \(5.0\times10^{-5}\) | \(1.047705+0.011489i\) | 0.0491 |
| \(4.0\times10^{-5}\) | \(1.006523+0.013300i\) | 0.0148 |

The large early deviations are retained: the exactly soluble harmonic limit
under the identical finite windows shows the same pre-asymptotic
oscillations.  At the finest point the nonlinear and harmonic normalized
values differ by only \(0.002051\).  All nested-basis, phase-budget,
quadrature, radial-oracle, guard-mode, and internal-residual gates passed; an
independent checker that does not import the production trace code passed 58
checks.  The full archive is
`results/r401_fixed_energy_trace_smoke/`.

This certificate supports the absolute amplitude and complex phase at one
fixed numerical energy.  It does not prove that \(\delta=0.01\) lies below
the nonquantitative \(\delta_{\rm tr}\), and the short ladder is not used to
claim a measured \(O(\hbar)\) remainder coefficient.

## 10. Quantitative theorem-domain progress

A4.11a--A4.11b now hold uniformly through

\[
 0<\delta\le0.010201,
\]

which supplies a positive parameter margin beyond the R401 value \(0.01\).
They prove

\[
 T_{\rm radial}>0.99,
 \qquad
 T_{\rm warped}>0.60.
\]

The independently accepted and frozen R401-VAL protocol decomposes the
remaining computer-assisted proof into a global/local no-gap cover on
\([0.60,0.75]\), a validated fast-branch root tube, and a uniform transverse
determinant.  R401-VAL-L1-V2 below closes the connected local root-tube
component, and A4.13 closes the strict determinant inequality on that local
branch.  The root complement, global cover, independent event-projected
return derivative, and Taylor-model identity residual remain open.

The first non-claiming implementation smoke is complete.  At both 128 and
256 Arb bits, zero-safe `exprel`/`log1prel`, exact normal coordinates,
analytic bounds, and 60 shell identities pass.  A no-production-import
checker independently passes 15 checks.  The 256-bit enclosures include

\[
 \|\nabla^2V_a\|_{\rm op}
 \le102.444797022348<103,
 \quad
 T_{\rm warped}\ge0.620775995736,
 \quad
 T_{\rm radial}\ge0.997570934052.
\]

This is `PASS_IMPLEMENTATION_SMOKE`, not `PASS_ENDPOINT` or `PASS_FULL`.

The accepted R401-VAL-L1-V2 milestone now proves the local-box
computer-assisted theorem
[A4.12](A412_CONTIGUOUS_FAST_BRANCH_CERTIFICATE.md): a connected validated
local branch over the complete reduced parameter interval

\[
 0\le\epsilon\le0.101.
\]

The proof object consists of 51 overlapping primary slabs and 50 guarded
bridge hulls.  CAPD's C1 Taylor/Lohner flow and a parameterized Krawczyk
operator pass all 101 jobs at each of 128-bit and 256-bit MPFR precision,
for 202/202 validated jobs in total.  The independent checker performs 202
exact-rational replays of the archived Krawczyk arithmetic and passes 3973
aggregate checks, including exact bridge containment and cross-precision
overlap.  Its scope is an independent proof-object replay, not an independent
ODE integration.

This local zero is identified with the fast family rather than an unnamed
branch: the first primary box contains the exact harmonic fast solution at
\(\epsilon=0\).  At every certified reduced zero, exact energy conservation
and strict monotonicity of energy in \(Q_+\) on the common phase interval
recover the omitted \(Q_+(T)=Q_+(0)\) equation, hence give a genuine
full-state return.  For \(\epsilon>0\), every period lies in
\((0.66,0.67)\); if one were a proper repetition, its primitive period would
be below \(0.335<0.60\), contradicting A4.11b.  At \(\epsilon=0\),
primitivity follows directly from the exact fast harmonic period.  The
connected certified family is therefore primitive.

The derived R401-VAL-L1-MG-V2 milestone now proves the companion local
computer-assisted theorem
[A4.13](A413_LOCAL_MONODROMY_GAP_CERTIFICATE.md).  The certified positive
phase slope gives both regularity of \(K_\epsilon=1\) and transversality of
the \(P_+=0\) event.  At a periodic point, the physical four-dimensional
monodromy preserves the invariant flag

\[
 0\subset\operatorname{span}(X_{K_\epsilon})
 \subset\ker(dK_\epsilon)\subset T_z\mathbb R^4.
\]

The induced map on
\(\ker(dK_\epsilon)/\operatorname{span}(X_{K_\epsilon})\) is the derivative
of the two-dimensional energy-section return.  Factoring the characteristic
polynomial along this flag, without assuming semisimplicity of the unit
multipliers, gives

\[
 \chi_{M_\epsilon}(t)=(t-1)^2\chi_{D\Pi_\epsilon}(t).
\]

Hamiltonian reduction gives \(\det D\Pi_\epsilon=1\), and therefore

\[
 \det(I-D\Pi_\epsilon)=4-\operatorname{tr}M_\epsilon.
\]

All 101 frozen determinant intervals at each precision (202 total) have lower
endpoint above \(3\), with rigorous directional minima
`3.835992606647717183` at 128 bits and
`3.850741968945794693` at 256 bits.  The no-analyzer-import checker passes
202 determinant replays, 202 phase-slope replays, all 815 directed-decimal
payloads, and 8302 aggregate checks.  Thus

\[
 \det(I-D\Pi_\epsilon)>3
 \qquad(0\le\epsilon\le0.101)
\]

on the A4.12 branch.

The former R401-VAL-L0 result is not a proof milestone.  Its archived source
used a midpoint energy gradient in the first Krawczyk Jacobian row instead
of the full root box, and it is preserved as
`r401_val_local_slab_smoke.attempt0-invalid-energy-jacobian`.  The first L1
production is also preserved but invalidated: independently constructed
unpadded bridge boxes missed literal containment by a final printed decimal
ULP.  L1-V2 prospectively froze rational \(10^{-18}\) bridge padding and
reran both precisions without a post-hoc tolerance.

The accepted status is `PASS_CONTIGUOUS_LOCAL_BRANCH` with
`final_status: null`, accompanied by the derived
`PASS_LOCAL_MONODROMY_GAP`, also with `final_status: null`; neither is
`PASS_ENDPOINT` or `PASS_FULL`.  Uniqueness and the \(D>3\) inequality hold
only on the branch inside the displayed primary boxes and bridge hulls.  The
local root-box complement, global phase-space cover, independent
event-projected \(D\Pi\) computation, and full Taylor-model identity
residual remain open; consequently neither \(\delta_{\rm tr}\) nor
\(\delta_{\rm nd}\) is promoted.

The subsequent representative L2-S0 calculation is recorded in
[A4.14](A414_REPRESENTATIVE_LOCAL_COMPLEMENT_SMOKE.md).  It decomposes the
complement of the accepted L1 plan box into eight exact coordinate shells
for `S000`, `S025`, and `S050`, and closes all six `(precision, slab)` trees
at 128 and 256 MPFR bits.  The archive contains 3,016 evaluated nodes; every
one of its 1,532 leaves is excluded by an empty validated energy contraction
or a necessary-return component separated from zero.  The independent
exact-decimal replay passes 89,962 checks with zero failures.  Its status is
`PASS_IMPLEMENTATION_SMOKE`, with `final_status: null`.

This finite result proves the local-complement statement only on the three
selected parameter slabs.  It does not interpolate across the remaining 48
slabs and therefore does not change the all-slab, phase-cover, global-cover,
or trace-domain status above.

## 11. Why this still does not pass the arithmetic P gate

The result is in the limit

\[
 E\ \text{fixed},\qquad \hbar\downarrow0.
\]

Hilbert--Pólya ultimately needs one fixed operator, hence fixed physical
\(\hbar=1\), in a high-energy regime.  If

\[
 L_E=\log(E/2\pi),\quad
 R_E=\sqrt{L_E/\pi},\quad
 \tau_E=R_E/\sqrt E,\quad
 h_E=(R_E\sqrt E)^{-1},
\]

then the radial rescaling produces

\[
 \frac{H_0}{E}
 =-\frac{h_E^2}{2}\Delta_Q
 +e^{L_E(|Q|^2-1)}.
\]

This is a simultaneous semiclassical and hard-wall limit, not a fixed smooth
symbol.  For the **radial** system, \(\tau_E\) is the characteristic physical
time scale, so a fixed physical prime time \(r\log p\) would correspond to a
scaled time of order \(\sqrt{E/\log E}\).  This is already far beyond the
ordinary fixed-time trace regime.

The same period law has not been proved for all fixed-complexity warped
orbits.  Indeed,

\[
 \Psi_a^{-1}(u,v)=(v,-c_av-av^2-u),
\]

so the warped allowed region can have an \(O(R_E^2)\) direction even when
the radial \(u\)-region has size \(O(R_E)\).  Establishing a uniform warped
period scale is therefore an explicit open problem, not a consequence of
the radial rescaling.

Therefore the honest gate ledger is

\[
 \boxed{
 C\ \text{proved};\quad
 P^*_{\mathrm{loc,obs}}\ \text{proved as an intermediate route};\quad
 P^*_{\mathrm{loc}}\ \text{proved at fixed energy};
 \quad P^*_{\mathrm{loc,num}}\ \text{passed at }\delta=0.01;
 \quad P_0\ \text{open};\quad Z\ \text{unauthorized}.}
\]

## 12. Immediate next theorem targets

1. Prove a quantitative theorem-domain bound A4.11/R401-VAL, aiming to
   certify \(\delta_{\rm tr}\ge0.010201>0.01\), with independent validation of the
   interval or explicit-estimate certificate.  Propositions A4.11a--A4.11b
   already give \(\bar\delta(0.75)\ge0.010201\) and exclude all warped periods
   \(T\le0.60\); the remaining work is the validated whole-shell cover on
   \([0.60,0.75]\) and certification of \(\delta_{\rm nd}\).  Numerical
   agreement in R401 cannot supply either implication.  R401-VAL-A0 has
   passed, and [A4.12](A412_CONTIGUOUS_FAST_BRANCH_CERTIFICATE.md), backed by
   R401-VAL-L1-V2, now certifies one connected primitive
   full-return branch in its frozen local boxes for
   \(\epsilon\in[0,0.101]\).  [A4.13](A413_LOCAL_MONODROMY_GAP_CERTIFICATE.md)
   now proves \(\det(I-D\Pi)>3\) uniformly on that branch using the invariant
   quotient and 202/202 exact-rational monodromy enclosures.  Next exclude
   the local root-box complement on all 51 slabs (A4.14 currently closes
   only the frozen three-slab implementation smoke), build the phase and global covers, and
   complete the independent event-projected \(D\Pi\) and Taylor-model
   identity-residual gates.  The local branch and gap certificates do not by
   themselves promote \(\delta_{\rm tr}\).
2. Only after that certification, optionally extend the fixed-energy audit
   through R401-FC (finer \(\hbar\)) and R401-ID (an independent warped
   spatial discretization), without refitting phase or amplitude.
3. Develop R402 as the separate high-energy hard-wall/Hénon-metric theorem
   needed to approach fixed physical \(\hbar=1\).
4. Search for an endogenous growing-complexity orbit family before making
   any prime-time comparison.  High-energy fixed-operator work is
   a separate two-parameter theorem, not an extrapolation of R400.
