# Route A4 Derivation Status Ledger

## Problem anchor

The missing Paper-7 bridge is not another level-spacing statistic.  It is a
mathematically valid passage

\[
 \text{signed relative spectrum}
 \longrightarrow
 \text{closed Hamiltonian trajectories with }(T,S,P,\mu)
 \longrightarrow
 \text{eventual arithmetic carrier}.
\]

This package addresses only the first arrow, locally and in a fixed-energy
semiclassical limit.

## Derivation table

| Item | Formula or statement | Type | Current status |
|---|---|---|---|
| D1 | \(\nabla V_a=2\pi V_aD\Psi_a^T\Psi_a\) | Identity | Checked symbolically and in code |
| D2 | unique critical energy \(2\pi\) | Proposition | Proved from D1 and invertibility |
| D3 | compact regular shells for \(E>2\pi\) | Proposition | Proved from properness |
| D4 | exact phase volume and shell measure | Identity | Inherited from Paper 7 and differentiated |
| D5 | cutoff relative wave trace is finite rank | Proposition | Immediate functional calculus |
| D6 | cutoff wave trace–staircase integral | Identity | Exact Stieltjes integration by parts |
| D7 | fixed-energy Fourier bridge | Identity | Exact Fourier inversion |
| D8 | \(D^2V_a(0)=4\pi^2A_a^TA_a\) | Identity | Direct Taylor expansion |
| D9 | \(\omega_\pm=2\pi s_\pm\), \(T_+^0=s_-\) | Identity | Exact singular-value algebra |
| D10 | fast Lyapunov family exists | Proposition via literature | Exact integer-nonresonance hypotheses matched; amplitude-to-energy parameterization written and independently reviewed |
| D11 | \(D_+^0=4\sin^2(\pi/\rho_a)\) | Proposition | Follows from limiting transverse multipliers |
| D12 | \(dS/dE=T\) | Proposition | Standard Hamilton–Jacobi identity; branch smoothness required |
| D13 | nonlinear slope formula for \(T\) | Proved proposition | Poincaré--Lindstedt solvability calculation and constants independently derived |
| D14 | radial return exclusion off integer times | Proved proposition | Uniform compact-shell and bounded-time flow-convergence contradiction written in full |
| D15 | one-orbit relative Gutzwiller term | Conditional theorem | Coefficient/conventions audited; needs either CRR's global orbit hypotheses or a written observable-supported local corollary |
| D15b | remove the observable and recover a \(\xi_\hbar\)-determined trace | Proved theorem | Whole-shell blow-up, return classification, Poincaré-map IFT, and iterate exclusion close A4.8 |
| D15c | unobserved local relative Gutzwiller formula | Theorem via finite-time CRR corollary | A4.8 verifies H.2--H.3 on the Fourier time support through 0.75; radial shell has no return |
| D15d | positive-time CRR phase \(e^{i\pi\sigma/2}=i\) | Proved proposition | Exact anisotropic-oscillator trace selects \(\sigma=1\bmod4\); nondegenerate continuation preserves it |
| D15e | quantitative radial short-period exclusion through \(\delta=0.010201\) | Proved proposition A4.11a | Vector Wirtinger inequality and exact radial Hessian bound give \(T>0.99\), hence \(\bar\delta(0.75)\ge0.010201\) |
| D15f | quantitative warped short-period floor through \(\delta=0.010201\) | Proved proposition A4.11b | Convex configuration enclosure and outward rational Hessian bound \(\|\nabla^2V_a\|<103\) give \(T>0.60\); full-shell validation remains on \([0.60,0.75]\) |
| D15g | one connected primitive full-return fast branch on \(\epsilon\in[0,0.101]\) | Local-box computer-assisted theorem [A4.12](A412_CONTIGUOUS_FAST_BRANCH_CERTIFICATE.md), backed by `PASS_CONTIGUOUS_LOCAL_BRANCH` | R401-VAL-L1-V2 passes 51 primary plus 50 bridge jobs at each of 128/256 MPFR bits (202 total); 202 exact-rational Krawczyk replays and 3973 aggregate checker gates pass; the analytic \(\epsilon=0\) fast anchor identifies the branch, energy monotonicity recovers the full-state return, A4.11b proves primitivity for \(\epsilon>0\), and exact harmonic dynamics handles \(\epsilon=0\); A4.12 alone gives uniqueness only inside the frozen boxes, while A4.15 separately closes their local complement |
| D15h | uniform transverse gap \(\det(I-D\Pi_\epsilon)=4-\operatorname{tr}M_\epsilon>3\) on the A4.12 branch | Local-branch computer-assisted theorem [A4.13](A413_LOCAL_MONODROMY_GAP_CERTIFICATE.md), backed by `PASS_LOCAL_MONODROMY_GAP` | Positive phase slope gives shell regularity and event transversality; the invariant quotient \(\ker(dK)/\operatorname{span}(X_K)\) proves the exact trace/determinant identity without semisimplicity; 202 determinant plus 202 phase-slope replays, 815 directed-decimal payloads, and 8302 aggregate checker gates pass; rigorous minimum lower endpoints are 3.835992606647717183/3.850741968945794693 at 128/256 bits; independent event-projected \(D\Pi\), Taylor residual, phase/global cover, \(\delta_{\rm tr}\), and P0 remain open |
| D15i | no reduced return root in the frozen local-box complement on representative slabs S000, S025, and S050 | Representative computer-assisted certificate [A4.14](A414_REPRESENTATIVE_LOCAL_COMPLEMENT_SMOKE.md), backed by `PASS_IMPLEMENTATION_SMOKE` | Six 128/256-bit trees cover the exact eight-shell complements with 3,016 evaluated nodes; all 1,532 leaves are energy or return exclusions; an independent exact-decimal checker passes 89,962 checks with zero failures. This licenses exactly three parameter slabs, not the other 48, an all-slab complement theorem, a phase/global cover, or any promotion of \(\delta_{\rm tr}\) or P0 |
| D15j | pointwise reduced-root uniqueness in the frozen local box on all 51 slabs | All-slab computer-assisted theorem [A4.15](A415_ALL_SLAB_LOCAL_COMPLEMENT_CERTIFICATE.md), backed by `PASS_LOCAL_COMPLEMENT_ALL_SLABS` and the accepted L1 release | The 102 trees contain 52,790 nodes and close every frontier at 128/256 bits; all 26,803 leaves are energy or necessary-return exclusions; the independent exact-rational checker passes 158,782 checks with zero failures. This closes the local complement only; phase/global covers, event-projected \(D\Pi\), the Taylor residual, \(\delta_{\rm tr}\), P0, zeta-zero, and RH claims remain open or unauthorized |
| D16 | radial high-energy characteristic time is \(\tau_E\asymp\sqrt{\log E/E}\) | Exact radial scaling interpretation | Does not establish the period law for warped fixed-complexity orbits |
| D17 | radial fixed prime times require scaled time \(\asymp\sqrt{E/\log E}\) | Scaling interpretation | Warped extension is an open heuristic, not a no-go theorem |

The earlier R401-VAL-L0 status is explicitly withdrawn: that archive used a
midpoint energy gradient in the first Krawczyk Jacobian row and is retained
only as `r401_val_local_slab_smoke.attempt0-invalid-energy-jacobian`.  The
first L1 archive is likewise non-licensing because separately rounded
unpadded bridge hulls failed literal containment.  Only the prospectively
frozen and rerun L1-V2 archive supports D15g.  D15h certifies the strict
uniform transverse determinant inequality on that branch, but it does not
independently construct the event-projected return derivative or close the
frozen Taylor-model identity residual.  D15i validates the complement engine
on three representative slabs, and D15j closes the local-box complement on
all 51 slabs.  D15g--D15j do not establish the phase/flow-box or global
phase-space covers and do not promote \(\delta_{\rm tr}\); hence they do not
close \(P_0\).

## Nonlinear coefficient derivation

In normal coordinates, write the mechanical equations as

\[
 \ddot Q_i+\omega_i^2Q_i
 +\frac12C_{ijk}Q_jQ_k
 +\frac16D_{ijkl}Q_jQ_kQ_l+\cdots=0.
\]

For a fast-mode amplitude \(A\), use

\[
 Q_+=A\cos\tau
 +A^2(b_{+0}+b_{+2}\cos2\tau)+O(A^3),
\]

\[
 Q_-=A^2(b_{-0}+b_{-2}\cos2\tau)+O(A^3),
\]

and

\[
 \Omega_+(A)=\omega_++\nu_+A^2+O(A^3).
\]

The order-\(A^2\) constant and second-harmonic equations give

\[
 b_{j0}=-\frac{C_{++j}}{4\omega_j^2},
 \qquad
 b_{j2}=-\frac{C_{++j}}
 {4(\omega_j^2-4\omega_+^2)}.
\]

The order-\(A^3\) fast fundamental solvability condition is

\[
 2\omega_+\nu_+
 =\frac{D_{++++}}8+
 \sum_jC_{++j}\left(b_{j0}+\frac12b_{j2}\right).
\]

Since

\[
 E-2\pi=\frac12\omega_+^2A^2+o(A^2),
\]

differentiation of \(T=2\pi/\Omega\) gives

\[
 \left.\frac{dT_+}{dE}\right|_{2\pi+}
 =-\frac{2T_+^0\nu_+}{\omega_+^3}.
\]

For the exponential Hénon potential, the needed tensors can be generated
without numerical differentiation.  If

\[
 \phi(q)=\pi|\Psi_a(q)|^2,
 \qquad V_a=2\pi e^\phi,
\]

then \(\nabla\phi(0)=0\), so

\[
 V^{(3)}(0)=2\pi\,\phi^{(3)}(0),
\]

\[
 V^{(4)}_{ijkl}(0)=2\pi\left[
 \phi^{(4)}_{ijkl}
 +\phi^{(2)}_{ij}\phi^{(2)}_{kl}
 +\phi^{(2)}_{ik}\phi^{(2)}_{jl}
 +\phi^{(2)}_{il}\phi^{(2)}_{jk}
 \right].
\]

The only nonzero independent higher derivatives in physical coordinates are

\[
 \phi_{xxx}=12\pi ac_a,\qquad
 \phi_{xxy}=4\pi a,\qquad
 \phi_{xxxx}=24\pi a^2.
\]

The production and independent implementations transform these tensors
separately and recover the same coefficient.

## Exact, approximate, and interpretive boundaries

### Exact

- all cutoff trace identities;
- all bottom Hessian and singular-value formulas;
- the analytic tensors entering the period slope;
- numerical ODE equations and action integral.

### Proposition-level after standard theorem invocation

- existence and nondegeneracy of the small fast Lyapunov family;
- action derivative identity;
- radial off-integer return exclusion;
- quantitative radial and warped period lower bounds A4.11a--A4.11b;
- local-branch invariant-quotient monodromy gap A4.13;
- microlocally localized trace expansion;
- whole-shell fast-orbit uniqueness and the unobserved finite-time CRR
  specialization.

### Approximation

- truncating the normal form after its first energy correction;
- finite-precision shooting and monodromy integration;
- quadratic extrapolation in the three smallest R400 cells.

### Interpretation only

- calling the result a partial Hilbert--Pólya structural feature;
- treating \(P^*_{\mathrm{loc}}\) as evidence that Route A is alive;
- the claim that a future high-complexity family might overcome shrinking
  high-energy time scales.

## Forbidden upgrades

The package does not justify any of the following:

- replacing \(\hbar\downarrow0\) by \(\hbar=1\);
- replacing near-bottom \(E\downarrow2\pi\) by \(E\to\infty\);
- deleting the microlocal observable without invoking the A4.8 whole-shell
  audit (A4.9 deletes it only after that theorem);
- claiming A4.7 is determined by \(\xi_\hbar\); its spectral sum also contains
  eigenfunction matrix elements of \(A_\hbar\);
- assigning a Maslov phase before computing it;
- identifying \(0.6638\ldots\) with any prime logarithm;
- inferring von Mangoldt amplitudes, zeta zeros, or RH.
