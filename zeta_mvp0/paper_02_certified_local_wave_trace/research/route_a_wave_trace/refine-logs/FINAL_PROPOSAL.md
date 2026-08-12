# Final Refined Proposal — Route A4

## Working title

**A Certified Local Relative Gutzwiller Bridge for an Equimeasurable
Hénon-Warped Exponential Well**

## Problem anchor

Paper 7 proves a self-adjoint discrete operator, the two growing
Riemann--von Mangoldt counting terms, strict one-step spectral activity, and
valid relative spectral objects.  It does not prove that a nonzero-time
relative trace is carried by actual continuous Hamiltonian closed orbits.

The minimum next bridge is therefore:

> Produce one analytically controlled, nondegenerate Hénon-warped periodic
> orbit whose physical time is separated from the radial reference, and
> place its period, action, stability, and phase in a rigorous fixed-energy
> semiclassical relative trace formula.

## Refined thesis

For the one-step scalar family at \(a=1.02\), the Hénon warp analytically
splits the radial bottom resonance.  Its fast Lyapunov branch has an explicit
noninteger limiting period, a nonzero stability determinant, and an explicit
first nonlinear period/action coefficient.  A compact time interval around
that period excludes all radial returns sufficiently near the bottom.
The complete-shell blow-up proves that this is the only warped return with
\(0<T\le0.75\), while the radial shell has none.  Consequently the
finite-time CRR formula yields a single warped Gutzwiller contribution in an
**unobserved**, eigenvalue-only relative trace as \(\hbar\to0\) at each
fixed sufficiently small positive energy excess.

## Invariant object

\[
 \rho_{\mathrm{rel},\hbar}(E;g)
 =\operatorname{Tr}\!\left[
 \chi(P_{a,\hbar})^2
 g\!\left(\frac{E-P_{a,\hbar}}\hbar\right)
 \right]-(a\to0),
\]

where \(0\notin\operatorname{supp}\widehat g\).  No phase-space observable
appears in the final object.

## Main theorem target

For sufficiently small \(\delta=E-2\pi>0\), choose
\(\operatorname{supp}\widehat g\Subset(0,0.75)\) around the fast period.
Then A4.10 fixes the positive-time CRR phase and gives

\[
 \rho_{\mathrm{rel},\hbar}(E;g)
 =i\,\widehat g(T_+(E))
 \frac{T_+^{\#}(E)}
 {2\pi\sqrt{|\det(I-P_+(E))|}}
 e^{iS_+(E)/\hbar}
 +O_{\delta,\chi,g}(\hbar).
\]

The radial term is \(O(\hbar^\infty)\) because it has no return in the
chosen window.

The quantifiers are: choose each fixed \(0<\delta<\delta_0\), then choose
the \(\delta\)-dependent cutoffs, and only afterward take
\(\hbar\downarrow0\).  No uniform two-parameter limit is claimed.

A4.8 proves whole-shell uniqueness and primitivity through time \(0.75\).
Thus A4.9 is determined by the two eigenvalue lists and exactly connects to
\(\xi_\hbar\).  The earlier observable-localized route is retained only to
document the logical intermediate stage.

## Analytic payload

The proposal aims to promote the following from the theorem package:

1. exact regular-shell and phase-volume lemmas;
2. exact cutoff-trace/staircase identities;
3. Lyapunov-centre existence and near-bottom Poincaré nondegeneracy;
4. the explicit period/action normal-form slope;
5. uniform radial return exclusion away from integer time;
6. whole-shell uniqueness by blow-up and a Poincaré-map implicit-function
   theorem;
7. one-orbit eigenvalue-only relative trace expansion;
8. a precise statement of why fixed-energy \(\hbar\to0\) does not solve the
   fixed-operator high-energy prime-time problem.

## Empirical payload

R400 is a formula/convention audit, not the proof:

- six energy excesses from 0.01 to 0.40;
- independent period, action, monodromy, and energy integration;
- exact intercept and first-slope oracles;
- separate implementation checker;
- no prime, zero, or spectral-peak input.

R401-SC subsequently audited the eigenvalue-only trace itself:

- exact area-preserving coordinate transformation before Galerkin
  discretization, ensuring the basis lies in the operator form domain;
- eight \(\hbar\) values from \(4\times10^{-4}\) to
  \(4\times10^{-5}\);
- independent radial Laguerre and exact harmonic finite-window oracles;
- absolute \(T/(2\pi\sqrt D)\) amplitude and \(+i\) phase fixed before the
  run;
- finest normalized trace \(1.0065230645+0.0133004473i\);
- all integrity gates, 58 independent recomputation checks, and all 74
  current regression tests passed.

The first quantitative theorem-domain reductions are now also complete:

- A4.11a proves \(T_{\rm radial}>0.99\) throughout
  \(0<\delta\le0.010201\), so
  \(\bar\delta(0.75)\ge0.010201\);
- A4.11b proves \(T_{\rm warped}>0.60\) on the same band from a convex-box
  Hessian bound;
- R401-VAL prospectively specifies the no-gap interval-flow and
  Poincaré/Krawczyk certificate on \([0.60,0.75]\); L1-V2 below closes its
  connected local fast-branch component, and A4.13 closes the strict
  transverse gap on that branch; the local complement, global cover,
  independent event-projected derivative, and Taylor identity remain open.

R401-VAL-A0 has since passed the non-claiming implementation smoke at 128 and
256 Arb bits: every analytic/special-function gate and 60 shell identities
per precision pass, followed by a 15-check no-production-import checker.
The former R401-VAL-L0 status is withdrawn.  Its first Krawczyk Jacobian row
used a midpoint energy gradient rather than the full root box, so the archive
is retained only as an explicitly invalidated attempt.  A first L1 production
is likewise non-licensing because separately rounded unpadded bridge hulls
missed literal containment by a final decimal ULP.

The prospectively frozen R401-VAL-L1-V2 rerun now proves the local-box
computer-assisted theorem
[A4.12](../A412_CONTIGUOUS_FAST_BRANCH_CERTIFICATE.md).  CAPD C1
Taylor/Lohner flow and parameterized
Krawczyk inclusions certify 51 overlapping primary slabs plus 50 guarded
bridge hulls at each of 128 and 256 MPFR bits: all 202 jobs pass.  The
independent proof-object checker passes 202 exact-rational arithmetic replays
and 3973 aggregate checks.  The exact fast harmonic solution anchors the
chain at \(\epsilon=0\), and the chain covers all
\(\epsilon\in[0,0.101]\).  Exact energy conservation and the monotone
\(Q_+\)-energy gate recover the full-state return equation; the period window
together with A4.11b proves the connected branch primitive for
\(\epsilon>0\), and exact harmonic dynamics proves it at \(\epsilon=0\).

The result proves uniqueness only in the frozen local primary boxes and
bridge hulls.  The companion
[A4.13](../A413_LOCAL_MONODROMY_GAP_CERTIFICATE.md) uses the invariant
quotient \(\ker(dK)/\operatorname{span}(X_K)\) to prove

\[
 \det(I-D\Pi_\epsilon)=4-\operatorname{tr}M_\epsilon>3
\]

uniformly on this branch.  R401-VAL-L1-MG-V2 passes 202 determinant replays,
202 phase-slope replays, all 815 directed-decimal payloads, and 8302
aggregate checks.  Its status is `PASS_LOCAL_MONODROMY_GAP` with
`final_status: null`.  Root-complement exclusion, the global phase-space
cover, independent event-projected \(D\Pi\), and the Taylor-model identity
residual remain pending.  Therefore neither local milestone is
`PASS_ENDPOINT` or `PASS_FULL`; they do not promote \(\delta_{\rm tr}\),
close \(P_0\), or authorize a zeta claim.

## Novelty boundary

The general fixed-energy trace formula is standard.  Newness, if any, lies
in this Hénon exponential model's exact normal-form data, radial-free time
window, and model-specific relative specialization.  The immediate
high-value target is the R401-VAL theorem-domain certificate; the subsequent
Hilbert--Pólya-facing target is a uniform high-energy hard-wall/Hénon-metric
calculus.

## Success criterion

The fixed-energy local spectral criterion is now met: independent reviews
accept the dynamics proof after precision edits, the finite-time CRR
hypotheses are explicitly mapped, and the R400 archive remains reproducible.
R401-SC adds high-accuracy numerical support for the full complex
eigenvalue-only coefficient.  A4.11a--A4.11b quantitatively close the radial
component and the warped short-time interval; A4.12--A4.13 now close the
local branch and its strict transverse gap.  The complement/global and
independent identity gates still prevent the full
\(\delta_{\mathrm{tr}}\ge0.01\) claim.  No prime or zero comparison is
authorized.

## Failure criterion

Demote or split the theorem if:

- the Lyapunov-centre theorem does not supply the claimed branch regularity;
- the nonlinear coefficient has a missing resonant or amplitude term;
- radial returns enter every admissible window;
- the observable-localized trace theorem has incompatible symbol or support
  hypotheses;
- the Maslov convention cannot be fixed consistently;
- the result is only valid after fitting to quantum peaks.

## Arithmetic boundary

Even full success leaves

\[
 T_{\gamma_{p,r}}(E)\to r\log p,\qquad
 A_{\gamma_{p,r}}(E)\to C(\log p)p^{-r/2}
\]

completely open.  No P, Z, Hilbert--Pólya spectrum, or RH claim is made.
