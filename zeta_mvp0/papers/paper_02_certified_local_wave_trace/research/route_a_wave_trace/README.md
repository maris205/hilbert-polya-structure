# Route A4 — Certified Local Relative Gutzwiller Bridge

This directory is the theorem-engineering continuation of Paper 7.  It turns
the existing relative spectral container into a fixed-energy,
eigenvalue-only periodic-orbit theorem while keeping the high-energy
arithmetic gate explicitly open.

## Core result

At \(a=1.02\), the one-step Hénon warp splits the radial \(1{:}1\) bottom
frequency into two exact normal modes.  The fast Lyapunov family has

\[
 T_+^0=0.6638439766792985,
 \qquad
 |\det(I-P_+)|\to3.8627220445155035,
\]

and

\[
 T_+(2\pi+\delta)
 =T_+^0-0.0274450756283701\,\delta+o(\delta).
\]

The radial reference returns near integer times at the bottom, so the window
\([0.60,0.75]\) excludes it for sufficiently small energy excess.  A4.8
blows up the complete warped shell and proves that the fast orbit is its only
return with \(0<T\le0.75\).  A4.9 then applies the finite-time CRR trace
formula with observable symbol \(A_{\rm obs}\equiv1\).  The final local trace
is therefore determined by the
two eigenvalue lists; the observable-localized construction remains only an
intermediate proof route.  A4.10 fixes the positive-time term, in the project
Fourier convention, as

\[
 i\,\widehat g(T_+)
 \frac{T_+}{2\pi\sqrt{|\det(I-P_+)|}}
 e^{iS_+/\hbar}.
\]

R401-SC evaluates exactly this complex coefficient at \(\delta=0.01\) on an
eight-point \(\hbar\) ladder.  Its finest normalized value is
\(1.0065230645+0.0133004473i\); all integrity gates and the independent
58-check recomputation pass, together with all 74 current regression tests.
A4.11a now certifies the radial component
\(\bar\delta(0.75)\ge0.010201\), while A4.11b excludes every warped return
with \(T\le0.60\) on the same energy band.  R401-VAL-L1-V2 now validates one
connected primitive fast-orbit branch locally for
\(0\le\epsilon\le0.101\) (equivalently \(0\le\delta\le0.010201\) in the
reduced scaling).  A4.13, backed by `R401-VAL-L1-MG-V2`, now additionally
proves on that entire branch that

\[
 \det(I-D\Pi_\epsilon)=4-\operatorname{tr}M_\epsilon>3.
\]

The root-complement and global phase-space covers, the independent
event-projected \(D\Pi\) computation, and the frozen Taylor-model identity
residual remain open, so \(\delta_{\rm tr}\) is not promoted.

A4.14 now separately records `R401-VAL-L2-S0`: all six frozen
local-complement trees on the representative slabs `S000`, `S025`, and
`S050` close at 128 and 256 MPFR bits.  Their 3,016 evaluated nodes contain
no root candidate, invalid leaf, or unresolved leaf, and the independent
exact-decimal checker passes 89,962 checks with zero failures.  This is
`PASS_IMPLEMENTATION_SMOKE`, not an all-51-slab complement theorem; the
other 48 slabs and every phase/global-cover gate remain open.

## Files

- A408_WHOLE_SHELL_UNIQUENESS_PROOF.md: standalone global uniqueness proof;
- A411_RADIAL_PERIOD_BOUND.md: analytic radial period bound proving
  \(\bar\delta(0.75)\ge0.010201\);
- A411_WARPED_PERIOD_FLOOR.md: analytic convex-box Hessian bound excluding
  every warped return with \(0<T\le0.60\) through \(\delta=0.010201\);
- [A412_CONTIGUOUS_FAST_BRANCH_CERTIFICATE.md](A412_CONTIGUOUS_FAST_BRANCH_CERTIFICATE.md):
  local-box computer-assisted theorem for the validated primitive fast
  branch on \(0\le\epsilon\le0.101\);
- [A413_LOCAL_MONODROMY_GAP_CERTIFICATE.md](A413_LOCAL_MONODROMY_GAP_CERTIFICATE.md):
  invariant-quotient proof and validated uniform
  \(\det(I-D\Pi_\epsilon)>3\) bound on the A4.12 branch;
- [A414_REPRESENTATIVE_LOCAL_COMPLEMENT_SMOKE.md](A414_REPRESENTATIVE_LOCAL_COMPLEMENT_SMOKE.md):
  bounded six-tree local-complement implementation certificate on three
  representative slabs, with explicit non-promotion boundary;
- CRR_HYPOTHESIS_CHECK.md: finite-time trace-theorem assumption map;
- CRR_PHASE_INDEX.md: exact positive/negative-time phase convention;
- INDEPENDENT_REVIEW_ROUND1.md: independent revise--accept audit trail;

- `THEOREM_ENGINEERING_PACKAGE.md`: propositions, conditional theorem, and
  Hilbert--Pólya boundary;
- `DERIVATION_STATUS.md`: formula-by-formula proof status;
- `LITERATURE_AUDIT.md`: primary-source support and novelty boundary;
- `R400_LOCAL_PERIOD_PROTOCOL.md`: frozen zero-input numerical protocol;
- `R400_IMPLEMENTATION_REVIEW.md`: R200 phase diagnosis and R400 review;
- `R401_FIXED_ENERGY_TRACE_PROTOCOL.md`: frozen eigenvalue-only complex-trace
  audit;
- `R401_VALIDATED_THEOREM_DOMAIN_PROTOCOL.md`: prospective interval-proof
  protocol for certifying the remaining \(\delta_*\) and
  \(\delta_{\rm nd}\) thresholds through \(\delta=0.010201\), placing the
  R401 value \(0.01\) strictly inside the target band;
- `R401_VAL_PROTOCOL_FREEZE.md`: accepted pre-execution protocol hashes and
  endpoint-margin semantics;
- `R401_VAL_PROTOCOL_AMENDMENT_V2.md`: independently accepted
  shared-parameter Taylor-model correction to the determinant-width gate;
- `R401_VAL_PROTOCOL_V2_FREEZE.md`: composite V2 protocol hashes and
  namespaced status semantics;
- `R401_VAL_L1_PROTOCOL_V2.md`: frozen contiguous-local-branch protocol,
  including the analytic fast anchor, full-state return recovery, guarded
  bridge hulls, and primitivity gate;
- `R401_VAL_L1_V2_FREEZE.md`: accepted V2 production hashes and the
  pre-frozen \(10^{-18}\) bridge-padding rule;
- `R401_VAL_L1_MONODROMY_GAP_PROTOCOL.md`: derived exact-rational local
  monodromy-gap protocol with invariant-quotient and directed-decimal rules;
- `R401_VAL_L1_MONODROMY_GAP_FREEZE.md`: accepted V2 release hashes and
  strict directional bounds;
- `R401_METHOD_REVIEW.md`: rejected original-coordinate basis and accepted
  exact-coordinate form-domain audit;
- `refine-logs/`: required research-refinement and experiment-planning
  outputs.

Code and immutable final results live at:

- `src/hp_candidate_search/local_periodic_orbits.py`;
- `scripts/run_r400_local_period_smoke.py`;
- `scripts/check_r400_local_period_independent.py`;
- `results/r400_local_period_smoke/`.

R401 code and immutable results live at:

- `src/hp_candidate_search/transformed_galerkin.py`;
- `src/hp_candidate_search/radial_laguerre.py`;
- `src/hp_candidate_search/semiclassical_trace.py`;
- `scripts/run_r401_fixed_energy_trace_smoke.py`;
- `scripts/check_r401_fixed_energy_trace_independent.py`;
- `results/r401_fixed_energy_trace_smoke/`.

R401-VAL analytic-smoke code and results live at:

- `src/hp_candidate_search/validated_analytic.py`;
- `scripts/run_r401_val_analytic_smoke.py`;
- `scripts/check_r401_val_analytic_smoke_independent.py`;
- `results/r401_val_analytic_smoke/`.

This smoke passes at 128/256-bit Arb precision with 60 shell identities per
precision and 15 independent checks.  It does not yet contain validated ODE
flow or a global/local cover certificate by itself.

R401-VAL contiguous-local-branch code and accepted results live at:

- `validated/capd_r401_local_slab_grid_mp.cpp`;
- `validated/CAPD_DEPENDENCY.md`;
- `scripts/run_r401_val_l1_branch.py`;
- `scripts/check_r401_val_l1_independent.py`;
- `results/r401_val_l1_branch/`.

The accepted R401-VAL-L1-V2 run proves the local-box theorem A4.12 and covers
\(0\le\epsilon\le0.101\) with 51 primary slabs and 50 guarded bridge hulls.
All 101 jobs pass at each of 128 and 256 MPFR bits (202/202 total), and the
independent checker passes 202 exact-rational Krawczyk replays and 3973
aggregate checks.  The first box contains the analytically reconstructed
fast harmonic solution at \(\epsilon=0\); exact energy conservation plus the
strict \(Q_+\)-energy monotonicity gate recovers the omitted full-state return
equation; and the certified period window together with A4.11b proves that
the positive-\(\epsilon\) returns are primitive, while exact harmonic
dynamics proves primitivity at \(\epsilon=0\).

For provenance, the former R401-VAL-L0 archive is explicitly invalidated as
`results/r401_val_local_slab_smoke.attempt0-invalid-energy-jacobian/`: its
first Jacobian row used a midpoint energy gradient rather than the full root
box.  The first L1 production is likewise retained as
`results/r401_val_l1_branch.attempt1-invalid-bridge-rounding/`; its separately
printed unpadded bridge hulls missed exact containment by a terminal decimal
ULP.  Neither archive is a passing proof milestone.  The accepted V2 result
uses a pre-frozen rational padding and no post-hoc comparison tolerance.

`PASS_CONTIGUOUS_LOCAL_BRANCH` proves existence and uniqueness only inside
the displayed primary boxes and bridge hulls.  It is not a root-complement,
global phase-space, `PASS_ENDPOINT`, or `PASS_FULL` certificate, and its
result manifest deliberately retains `final_status: null`.

The derived R401-VAL-L1-MG-V2 archive lives at:

- `scripts/run_r401_val_l1_monodromy_gap.py`;
- `scripts/check_r401_val_l1_monodromy_gap_independent.py`;
- `results/r401_val_l1_monodromy_gap/`.

It passes all 202 determinant replays and 202 phase-slope replays, all 815
directed-decimal payloads, and 8302 aggregate checks.  Its rigorous minimum
lower endpoints for \(4-\operatorname{tr}M\) are
`3.835992606647717183` at 128 bits and `3.850741968945794693` at 256 bits.
The invariant quotient
\(\ker(dK)/\operatorname{span}(X_K)\), together with the positive event
phase slope, identifies this quantity exactly with
\(\det(I-D\Pi)\).  This is `PASS_LOCAL_MONODROMY_GAP` only: an independent
event-projected return derivative and the narrow Taylor-model identity
residual remain required by the final protocol.

The V1 derived release is preserved at
`results/r401_val_l1_monodromy_gap.attempt1-superseded-nondirected-display/`.
Its exact-fraction inequality core remains auditable, but nearest-float
human-readable bounds were not directionally rigorous; it is explicitly
superseded and non-licensing in favor of V2.

The accepted representative L2-S0 archive lives at:

- `validated/capd_r401_local_complement_mp.cpp`;
- `scripts/run_r401_val_l2_s0_local_complement.py`;
- `scripts/check_r401_val_l2_s0_local_complement_independent.py`;
- `results/r401_val_l2_s0_local_complement/`.

At 128 bits the three trees contain 486, 546, and 574 evaluated nodes, with
maximum depths 29, 35, and 36.  At 256 bits they contain 436, 488, and 486
nodes, with maximum depths 27, 31, and 31.  Every terminal leaf is an
energy or necessary-return exclusion.  The release status is
`PASS_IMPLEMENTATION_SMOKE` and `final_status` remains null.  This result
licenses only the exact three-slab domains; it supplies implementation and
budget evidence for a future prospectively frozen 102-tree run.

## Gate status

\[
 \boxed{
 C\text{ proved};\quad
 P^*_{\mathrm{loc}}\text{ proved at fixed energy};\quad
 P^*_{\mathrm{loc,num}}\text{ passed at }\delta=0.01;\quad
 P_0\text{ open};\quad Z\text{ unauthorized}.}
\]

The intermediate observable-localized trace depends on eigenfunction matrix
elements, but A4.8 removes it in the final theorem.  The project still does
not identify the local period with a prime logarithm and does not compare any
spectrum with zeta zeros.  The full analytic threshold \(\delta_{\rm tr}\)
is not yet quantitative: A4.11a--A4.11b close the radial and warped
short-time components, R401-VAL-L1-V2 validates the fast branch in its frozen
local boxes, and A4.13 proves the strict transverse determinant gap on that
branch.  A4.14 additionally excludes the local complement on three
representative slabs only.  All-slab complement exclusion, the global cover, the independent
event-projected \(D\Pi\) calculation, and the Taylor-model identity residual
remain open.  Thus neither the R401 trace pass nor the local branch/gap
passes are used to infer that \(0.01<\delta_{\rm tr}\).
