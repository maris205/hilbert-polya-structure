# Experiment Plan

## Claim–experiment matrix

| ID | Claim tested | Method | Promotion level |
|---|---|---|---|
| R400-A | bottom period/stability oracle is implemented correctly | exact Hessian/tensor checks | implementation |
| R400-B | fast reversible branch exists numerically and closes | six-cell shooting continuation | classical certificate |
| R400-C | \(T,S,D\) approach analytic intercepts/slopes | prospective small-\(\delta\) fits | asymptotic diagnostic |
| R400-D | result is independently reproducible | no-package checker | implementation/classical |
| R401-A | analytic propositions survive proof audit | independent mathematical review | theorem |
| R401-B | eigenvalue-only relative trace follows the predicted orbit term | decreasing \(\hbar\) ladder | semiclassical diagnostic |
| [A4.12 / R401-VAL-L1-V2](../A412_CONTIGUOUS_FAST_BRANCH_CERTIFICATE.md) | the fast harmonic orbit continues as one primitive full-state return branch over \(\epsilon\in[0,0.101]\), uniquely inside prescribed local boxes | 51 primary and 50 bridge CAPD/Krawczyk jobs at both 128/256 MPFR bits plus exact-rational proof-object replay | local-box computer-assisted theorem |
| [A4.13 / R401-VAL-L1-MG-V2](../A413_LOCAL_MONODROMY_GAP_CERTIFICATE.md) | the A4.12 branch has \(\det(I-D\Pi)=4-\operatorname{tr}M>3\) uniformly | invariant-quotient reduction, 202 total frozen monodromy and phase-slope replays (101 per precision), and independent directed-decimal checker | local-branch computer-assisted theorem |
| R402 | fixed-operator high-energy scaling admits uniform control | two-parameter analysis | HP-facing theorem |

## Completed R400 design

Energy excesses:

\[
 \{0.01,0.02,0.05,0.10,0.20,0.40\}.
\]

Primary outputs per cell:

- initial state and full trajectory;
- period and action;
- energy drift and closure;
- monodromy and all Floquet multipliers;
- symplectic defect;
- transverse \(\det(I-P)\);
- limiting trace amplitude.

Hard gates and tolerances are frozen in `R400_LOCAL_PERIOD_PROTOCOL.md`.

## Completed R401-SC design

Using the proved positive-time CRR phase \(+i\):

1. freeze eight \(\hbar\) values from \(4\times10^{-4}\) to
   \(4\times10^{-5}\) at \(\delta=0.01\);
2. use one fixed compact energy cutoff and compact Fourier-time support inside
   the radial-free interval;
3. compute the unobserved eigenvalue-only relative trace, not a global
   Gaussian magnitude peak;
4. compare the complex residual after subtracting the fully frozen term
   \(i[T/(2\pi\sqrt D)]e^{iS/\hbar}\) (with the chosen plateau
   \(\widehat g(T)=1\));
5. retain the exact harmonic finite-window result as a preregistered
   pre-asymptotic baseline and use an independent radial Laguerre solver;
6. use \(\sigma_+^{\mathrm{CRR}}=1\bmod4\) and
   \(T/(2\pi\sqrt D)\) without refitting a phase or scale.

The final archive passes all integrity and scientific gates.  At the finest
cell,

\[
 Z_\hbar=1.0065230645+0.0133004473i,
 \qquad |Z_\hbar-1|=0.0148139.
\]

## Kill conditions

- any classical orbit gate fails under refinement;
- the analytic slope fails independent derivation;
- the trace test requires looking at primes, zeros, or post hoc times;
- complex traces fail while magnitudes appear stable;
- radial returns collide with the support;
- a claimed \(O(\hbar)\) residual is dominated by eigenvalue phase error.

## Resources

R400 takes seconds and less than 1 GB.  R401 completed on the current
32-vCPU/60-GB host without a resource increase; the exact-coordinate
Galerkin route remained comfortably inside memory.  The next strict gate
within A4.11/R401-VAL is the local-complement/global cover and independent
event-projected/Taylor-identity certificate,
which is needed for a validated lower bound for
\(\delta_{\rm tr}\).  A4.11a already proves
\(\bar\delta(0.75)\ge0.010201\); the validated computation must therefore
close the warped \(\delta_*\) component and the protocol-level independent
\(\delta_{\rm nd}\) cross-check; A4.13 below already closes the local
branch's strict \(D>3\) inequality.  A4.11b
removes \(T\le0.60\), and the 128/256-bit R401-VAL-A0 analytic/shell smoke
plus its 15-check independent checker now pass.  R401-VAL-L0 has since
been explicitly invalidated because its first Jacobian row used a midpoint
energy gradient instead of the full root box.  The first L1 production is
also retained as non-licensing because unpadded bridge hulls failed literal
printed-box containment after separate directed rounding.

The prospectively frozen R401-VAL-L1-V2 rerun now proves the local-box
computer-assisted theorem
[A4.12](../A412_CONTIGUOUS_FAST_BRANCH_CERTIFICATE.md): 51 primary slabs
and 50 guarded bridge hulls cover \(\epsilon\in[0,0.101]\), with all 101 jobs
passing at each of 128 and 256 MPFR bits (202 total).  The independent
checker passes 202 exact-rational Krawczyk replays and 3973 aggregate gates.
The analytic fast anchor lies in the first box; exact energy conservation
and strict \(Q_+\)-energy monotonicity recover the omitted full-state return;
and the certified period window plus A4.11b makes every positive-\(\epsilon\)
return primitive, while exact harmonic dynamics handles \(\epsilon=0\).

The derived R401-VAL-L1-MG-V2 run now proves
[A4.13](../A413_LOCAL_MONODROMY_GAP_CERTIFICATE.md).  The positive phase
slope makes the energy section regular and transverse; the invariant
quotient proves
\(\det(I-D\Pi)=4-\operatorname{tr}M\) without a semisimplicity assumption.
The checker passes 202 determinant replays, 202 phase-slope replays, all 815
directed-decimal payloads, and 8302 aggregate checks.  The 128/256-bit
minimum lower endpoints are `3.835992606647717183` and
`3.850741968945794693`.

This is a local-box certificate only.  The next implementation units are
the local root-box complement, the phase/global cover, and the independent
event-projected \(D\Pi\) plus Taylor-model identity-residual checks.  Until
those pass, neither \(\delta_{\rm tr}\) nor \(P_0\) is promoted.

Optional finer fixed-energy continuation and an
independent warped discretization are named R401-FC and R401-ID; the R402
identifier remains reserved for the fixed-\(\hbar=1\) high-energy route.
