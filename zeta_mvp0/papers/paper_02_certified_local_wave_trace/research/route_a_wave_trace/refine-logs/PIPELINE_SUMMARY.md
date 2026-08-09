# Route A4 Pipeline Summary

## Outcome

The research-refinement pipeline converted a broad wave-trace aspiration
into a precise local theorem programme and executed its first zero-input
certificate.

The principal discovery is analytic:

\[
 T_+^0=0.6638439766792985,\qquad
 D_+^0=3.8627220445155035,
\]

with

\[
 \left.\frac{dT_+}{dE}\right|_{2\pi+}
 =-0.0274450756283701.
\]

This fast branch lies away from the radial integer return time.  The
full-shell A4.8 proof shows that it is the only warped return through time
\(0.75\), so the window supports an eigenvalue-only relative Gutzwiller
formula.

## Delivered artifacts

- theorem-engineering package;
- derivation-status ledger;
- primary-source literature audit;
- frozen R400 protocol;
- production orbit/variational/action module;
- six-cell immutable result archive;
- independent no-package checker;
- R200 phase-error diagnosis;
- frozen R401 protocol, exact-coordinate transformed Galerkin solver,
  radial Laguerre oracle, eight-cell PASS archive, and independent checker.
- frozen R401-VAL-L1-V2 protocol and guarded slab plan, CAPD C1
  Taylor/Lohner branch engine, 202-job PASS archive, and independent
  exact-rational proof-object checker;
- A4.13 invariant-quotient certificate and the R401-VAL-L1-MG-V2 derived
  archive, with 202 determinant and 202 phase-slope replays.

## Current gate ledger

\[
 \boxed{
 C\text{ proved};\quad
 P^*_{\mathrm{loc}}\text{ proved at fixed energy};
 \quad P^*_{\mathrm{loc,num}}\text{ passed at }\delta=0.01;
 \quad P_0\text{ open};\quad Z\text{ unauthorized}.}
\]

## R401 outcome and next gate

Independent dynamics review accepted the normal-form coefficient, exact
Lyapunov-centre hypothesis match, radial compactness proof, and A4.8
whole-shell uniqueness after minor precision edits.  Trace review accepted
the eigenvalue-only A4.9 coefficient and required finite-time CRR and common
threshold language, now inserted.  A4.10 fixes the positive-time CRR phase to
\(+i\) and the absolute project coefficient to \(T/(2\pi\sqrt D)\).
R401-SC has now passed from \(\hbar=4\times10^{-4}\) down to
\(4\times10^{-5}\).  At the finest point,

\[
 Z_\hbar=1.0065230645+0.0133004473i,
 \qquad |Z_\hbar-1|=0.0148139,
\]

while its separation from the exact harmonic finite-window baseline is only
\(0.002051\).  All integrity gates, the independent 58-check recomputation,
and all 74 current regression tests passed.  The next strict gate within
A4.11/R401-VAL is the local-complement/global cover together with the
independent event-projected/Taylor-identity cross-check needed
for a quantitative lower bound for
\(\delta_{\rm tr}\), targeting
\(\delta_{\rm tr}\ge0.010201>0.01\), without inferring it
from numerical agreement.  A4.11a has already proved the radial component
\(\bar\delta(0.75)\ge0.010201\); the remaining targets are \(\delta_*\) and
the protocol-level independent \(\delta_{\rm nd}\) cross-check (A4.13 below
already proves the local branch's strict \(D>3\) inequality).  A4.11b also proves a warped period floor \(T>0.60\),
and `R401_VALIDATED_THEOREM_DOMAIN_PROTOCOL.md` prospectively specifies the
global/local validated cover on \([0.60,0.75]\).  R401-VAL-A0 has
now passed the 128/256-bit Arb analytic/shell smoke and its independent
15-check recomputation.  The independently amended/frozen V2 protocol then
governed the local continuation work.  The earlier R401-VAL-L0 archive is
explicitly invalid because its first Krawczyk Jacobian row used a midpoint
energy gradient rather than the full root box; the first L1 archive is also
non-licensing because unpadded, separately rounded bridge hulls failed
literal containment.

The prospectively frozen and rerun R401-VAL-L1-V2 certificate proves the
local-box computer-assisted theorem
[A4.12](../A412_CONTIGUOUS_FAST_BRANCH_CERTIFICATE.md).  Its
51 overlapping primary slabs and 50 guarded bridge hulls cover
\(\epsilon\in[0,0.101]\); all 101 jobs pass at each of 128 and 256 MPFR bits,
for 202/202 total.  An independent checker passes 202 exact-rational
Krawczyk replays and 3973 aggregate checks.  The exact fast harmonic solution
anchors the first slab, energy conservation plus the monotone \(Q_+\) gate
recovers a full-state return, and the A4.11b short-period exclusion proves
the connected branch primitive for \(\epsilon>0\), with exact harmonic
dynamics handling \(\epsilon=0\).  This remains uniqueness only in
the frozen local boxes and bridge hulls: it is not a root-complement,
global-cover, or \(\delta_{\rm tr}\) claim, and `final_status` remains null.

[A4.13](../A413_LOCAL_MONODROMY_GAP_CERTIFICATE.md) now proves the local
transverse gap

\[
 \det(I-D\Pi_\epsilon)=4-\operatorname{tr}M_\epsilon>3
\]

throughout that A4.12 branch.  The exact invariant-quotient argument covers
unit-multiplier Jordan blocks, while the R401-VAL-L1-MG-V2 checker passes 202
determinant replays, 202 phase-slope replays, all 815 directed-decimal
payloads, and 8302 aggregate checks.  This is
`PASS_LOCAL_MONODROMY_GAP` with `final_status: null`: the independent
event-projected \(D\Pi\) computation, Taylor-model identity residual,
phase/global covers, \(\delta_{\rm tr}\), and P0 remain open.  A4.15
separately closes the local complement described next.

[A4.15](../A415_ALL_SLAB_LOCAL_COMPLEMENT_CERTIFICATE.md) closes all 102
frozen local-complement trees on the 51 slabs at 128 and 256 MPFR bits.  The
archive contains 52,790 evaluated nodes and 26,803 certified terminal
exclusions; its independent exact-rational checker passes 158,782 checks
with zero failures.  Combined with A4.12, this gives pointwise reduced-root
uniqueness throughout the declared \(B_{\mathrm{loc}}\), but only in the
frozen \(P_+=0\) reduced chart.  It does not provide the missing phase or
flow-box cover, a full energy-shell/global theorem, a quantitative
\(\delta_{\rm tr}\), P0, a Hilbert--P\'olya operator, zeta-zero
reconstruction, or RH.

Optional finer and independent-discretization audits are R401-FC and
R401-ID; R402 remains reserved for the fixed-\(\hbar=1\) high-energy route.
The arithmetic P gate remains open.
