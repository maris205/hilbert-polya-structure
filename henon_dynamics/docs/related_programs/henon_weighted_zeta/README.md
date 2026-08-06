# Hénon Weighted Zeta

Reproducible experiments for periodic orbits, weighted dynamical zeta functions,
open transfer operators, and exploratory semiclassical diagnostics of the reversible
area-preserving Hénon map

\[
H_a(x,y)=(1-a x^2-y,x).
\]

This repository is currently an experiment workspace. Numerical observations are
recorded with evidence levels and are not treated as arithmetic or Riemann-zero
claims.

## Current milestones

- M0: analytic/numerical geometry certificate and known-truth controls;
- M1: low-period orbit search, primitive classification, multiplier and action audit;
- M2: orbit-saturation and finite-order anomaly scan;
- M3: weighted cycle expansion and absorbing operator cross-check;
- M4: semiclassical, symbolic-parity, symmetry-class, and blinded external benchmarks.

The detailed strict plan lives at ../PAPER3_PLAN.md and the exploratory hypotheses
at ../PAPER3_EXPLORATORY.md while the workspace is being assembled.
Legacy parameter and implementation provenance is recorded in
research/LEGACY_HENON_AUDIT.md.

## Quick start

~~~bash
python scripts/verify_geometry.py
pytest -q
python scripts/search_periodic_orbits.py --a 1.0056 1.02 --max-period 6
python scripts/solve_complex_root_census.py --a 0.9 1.0056 1.02 --max-period 8
python scripts/run_open_ulam.py --a 1.02 --radius 2.0 2.5 3.0 --grid 64 96 128
python scripts/run_parameter_continuation.py --output-stem parameter_continuation_r042
python scripts/run_open_ulam.py --a 6 --radius 1 --grid 64 96 128 --method sobol --samples-per-cell 64 --seed 20260801 20260802
python scripts/run_open_ulam.py --a 6 --radius 0.6380064794363034 --grid 64 128 256 --method overlap --output-stem open_ulam_overlap_demo
python scripts/analyze_shifted_holdout.py
python scripts/audit_interval_cover.py
python scripts/audit_subdivided_cover.py
python scripts/analyze_subdivided_cover.py
python scripts/audit_adaptive_rounded_cover.py
python scripts/analyze_adaptive_rounded_cover.py
python scripts/audit_exact_closed_cover.py --workers 4
python scripts/check_exact_closed_cover.py --workers 4
python scripts/analyze_exact_closed_cover.py
python scripts/audit_outer_graph_r054.py --workers 4
python scripts/analyze_outer_graph_r054.py
python scripts/audit_true_image_graph_r055.py --workers 4
python scripts/analyze_true_image_graph_r055.py
python scripts/check_true_image_graph_r055.py
python scripts/audit_true_image_refinement_r056.py --workers 6
python scripts/check_true_image_refinement_r056.py --workers 32
python scripts/analyze_true_image_refinement_r056.py
python scripts/audit_mutual_separation_r057.py --workers 32
python scripts/check_mutual_separation_r057.py
python scripts/analyze_mutual_separation_r057.py
python scripts/audit_even_parameter_stress_r057s1.py --workers 32
python scripts/audit_hyperbolic_covering_r058.py
python scripts/audit_hyperbolic_filament_r058.py --workers 6
python scripts/check_hyperbolic_filament_r058.py --workers 32
python scripts/analyze_hyperbolic_filament_r058.py
~~~

All experiment outputs are JSON or CSV files under results/. The execution table is
research/refine-logs/EXPERIMENT_TRACKER.md. The common-box, finite-survivor, and
analytic-overlap audit is summarized in
research/refine-logs/R044_R047_OVERLAP_ANALYSIS.md.
The dense grid-phase follow-up is summarized in
research/refine-logs/R048_GRID_PHASE_ANALYSIS.md.
The shifted-origin clipped-boundary follow-up is summarized in
research/refine-logs/R049_SHIFTED_OVERLAP_ANALYSIS.md.
The pre-frozen hold-out replication is summarized in
research/refine-logs/R049_HOLDOUT_ANALYSIS.md.
The full-cell interval-image geometry diagnostic is summarized in
research/refine-logs/R050_INTERVAL_COVER_ANALYSIS.md.
The subdivided-strip tightening diagnostic is summarized in
research/refine-logs/R051_STRIP_COVER_ANALYSIS.md.
The adaptive one-ulp endpoint-expansion diagnostic is summarized in
research/refine-logs/R052_ADAPTIVE_ROUNDED_ANALYSIS.md.
The exact-rational closed-cell outer-cover audit is summarized in
research/refine-logs/R053_EXACT_CLOSED_COVER_ANALYSIS.md.
The exploratory exact outer-cover directed-graph diagnostic is summarized in
research/refine-logs/R054_OUTER_GRAPH_ANALYSIS.md.
The exact analytic true-image graph strictification is summarized in
research/refine-logs/R055_TRUE_IMAGE_GRAPH_ANALYSIS.md.
The held-out true-image replication and exact 2x refinement audit is summarized
in research/refine-logs/R056_TRUE_IMAGE_REFINEMENT_ANALYSIS.md.
The exact mutual-outer separation theorem, constructive counterexamples, and
failure-oriented scan are summarized in
research/refine-logs/R057_MUTUAL_SEPARATION_ANALYSIS.md. The paper-ready theory
line is in DERIVATION_PACKAGE.md and PROOF_PACKAGE.md.
The post-primary centered-even a/eta staircase supplement is summarized in
research/refine-logs/R057S1_EVEN_PARAMETER_STRESS_ANALYSIS.md.
The exact four-h-set hyperbolic-survivor theorem, locked nine-grid filament
replication, and independent audit are summarized in
research/refine-logs/R058_HYPERBOLIC_FILAMENT_ANALYSIS.md. The theorem proof
and independent proof audit are in R058_COVERING_PROOF.md and
research/refine-logs/R058_HYPERBOLIC_THEOREM_AUDIT.md.

## Scope boundary

The code may test heuristic spectral similarities, but no finite-period fit is
interpreted as a dynamical realization of Riemann zeros, a Hilbert--Pólya operator,
or evidence for the Riemann hypothesis.

The R058 covering/exclusion and cone audit established a nonempty compact
uniformly hyperbolic four-h-set survivor with a continuous symbolic factor.
R059 then adds an exact contraction theorem on the explicitly defined full
four-h-set survivor \(\Lambda_*\): its itinerary is conjugate to the frozen
four-state subshift and
\(h_{\rm top}(H_6|_{\Lambda_*})=\log\varphi\). This exact equality is local to
\(\Lambda_*\); it is not a claim about the full Hénon nonwandering set, a global
Markov partition, or the whole finite-grid filament.

Separately, the period-12 cycle and flat-trace diagnostics stabilize near
0.526171, while Gauss--Legendre, randomized-shift Sobol, and semi-analytic
cell-overlap finite-volume implementations support a common finite-resolution
window. Their shared nonmonotone grid oscillation leaves the
continuous-operator convergence gate open. These operator calculations have
not yet been restricted to the R058 certified survivor and do not establish an
exact cycle--operator equivalence. R049 also shows that internal boundary phase is a measurable source of the
finite-resolution variation; offset averaging is retained only as a diagnostic
possibility, not as a convergence theorem. The R049-HO hold-out reproduces an
aggregate improvement but includes a box/grid counterexample, so no universal
offset correction is enabled. The subsequent full-cell diagnostic finds that
simple axis-aligned image boxes are too conservative for a direct covering
certificate, motivating oriented or adaptive geometric bounds.
The subdivided-strip follow-up substantially tightens the finite cell-image
enclosure. The adaptive follow-up keeps median inflation near 1.18--1.24 and
passes final one-ulp endpoint nesting plus deterministic containment smoke
tests without hitting its subdivision cap. It remains a float64 geometric
diagnostic, because intermediate operations are not directed interval
arithmetic and target-cell enumeration still uses half-open semantics.
The subsequent R053 exact-rational audit removes those two finite-grid caveats
for a frozen four-configuration subset: all exact rectangle/closed-cell core
checks and an independent adjacency reconstruction pass, while the B1 bridge
confirms that final one-ulp expansion alone is not directed interval arithmetic.
R054 then builds all-closed, positive-area, and mutual forward/inverse graphs
from those exact outer rectangles. Nontrivial SCCs occur in all three variants,
but they are only candidate cores of an outer-cover graph; they do not certify
an invariant set, Markov partition, covering relation, true-image graph, or
operator spectrum. The shifted-sign control is close but not identical, and
graph refinement remains an open strictification step.
R055 performs that strictification at the edge level for the frozen grids: its
exact true-image graph equals the R054 mutual graph, and its positive-area graph
equals the R054 positive-area graph. This is a finite analytic incidence result
and does not certify an invariant set, Markov partition, covering relation, or
operator convergence.
R056 then replicates both identities on six predeclared held-outs, including an
odd centered grid and one-third shifted phases near the subdivision cap. Three
exact 2x chains pass complete and matched-support edge projection, active-node
lift, and multi-node SCC-descendant checks. The largest SCC grows approximately
linearly in N while its cell-union area shrinks, a filament-compatible but still
descriptive finite-grid observation. It is not a graph-limit or invariant-set
certificate.
R057 then shows that the R055--R056 closed-edge identity is not universal.
For \(a>0\), one common closed partition, and exact quadratic slab ranges, equality is
equivalent to strict upper/lower boundary overshoot-gap separation at every
internal edge. A centered N=60 exact false-mutual edge and three new pre-frozen
shifted counterexamples realize the failure mechanism. By contrast, the
positive-area outer and true graphs are equal under the stated a>0 semantics
without mutual filtering. The independent checker validates complete
microgrids, 102,494 persisted boundary rows, and all 11 failure witnesses.
The strict R057 all-gates decision remains false because sixteen frozen
plus/minus-three-eighth phase stresses activate the K=64 cap; they are retained
unchanged. These are finite incidence statements, not invariant, covering,
graph-limit, or operator-convergence results.
R057S1 further reduces the centered-even case to the scalar center-boundary
condition with K=ceil(2*a*h/eta). Its 266-configuration mechanism map has 157
passes and 109 failures, all at p=0. Eta scans are one-direction staircases,
whereas a scans show exact fail/pass re-entry at N=46,92,106 because K jumps.
This is post-primary partition arithmetic, not a dynamical bifurcation claim.
R058 then closes the orbit-witness gap on a deliberately conservative domain.
All six exact coverings and ten forbidden-transition exclusions pass; the
minimum exit and entry margins are 1/48 and 1/128. Three new locked 4x
true-positive lineages have size exponents 1.026800, 1.045203, and 1.043580,
with mean 1.038528 versus the R056 positive slope 1.038202. Their finite-grid
symbolic bridges realize exactly the six certified transitions, but this
replication remains supporting evidence rather than a dimension or graph-limit
theorem. Continuous transfer-operator convergence is still open.

## R059 update: exact contraction and certified-domain ledger

R059 strengthens the local R058 theorem on the explicit four-h-set survivor.
For every admissible sign itinerary,

$$
(T_\varepsilon q)_i
=\varepsilon_i\sqrt{\frac{1-q_{i-1}-q_{i+1}}6},
\qquad
\operatorname{Lip}_\infty(T_\varepsilon)\le\frac{2}{\sqrt{17}}<1.
$$

The exact arithmetic audit is PROVABLE AS STATED. Consequently the explicit
survivor is conjugate to the four-state subshift, has entropy
$\log((1+\sqrt5)/2)$, and has restricted determinant
$\det(I-zA)=1-z-z^3-z^4$. This is not a theorem about the full Hénon
nonwandering set.

The high-precision catalog bridge confirms 79 inside and 668 outside records
out of 747, with zero unresolved or root-failed records. The 79 canonical words
match the independent SFT enumeration through period 12. The earlier float64
development precheck is disclosed, so this is confirmation rather than
held-out discovery.

The restricted operator production uses four separately indexed h-sets,
$m=24,32,48,64,96,128$, Gauss--Legendre order 8, and two 64-sample randomized
Sobol seeds. G3 and the independent matrix/schema checker pass for all 18
configurations. The frozen G4 refinement gate remains negative for two Sobol
dyadic trajectories; this is retained as a finite-resolution stability result,
not continuous-operator convergence.

Reproduction:

    python scripts/audit_symbolic_contraction_r059.py
    python scripts/audit_certified_domain_r059.py --workers 16
    python scripts/check_certified_domain_r059.py
python scripts/run_restricted_operator_r059.py --workers 4
python scripts/check_restricted_operator_r059.py
python scripts/run_operator_variance_r060.py --workers 8
python scripts/check_operator_variance_r060.py
python scripts/analyze_operator_variance_r060.py

Primary R059 outputs are stored in results/certified_domain_r059.json,
results/certified_domain_r059_check.json,
results/restricted_operator_r059.json,
results/restricted_operator_r059_check.json, and
results/restricted_operator_r059_matrices/.

## R060 update: Sobol variance and Gauss-order mechanism audit

R060 leaves the frozen R059 G4 decision unchanged and asks why two individual
64-sample Sobol dyadic trajectories were nonmonotone.  The frozen design uses
six grids, 16 fresh seeds, paired 64/256-sample Sobol budgets, and Gauss orders
4/8/12.  This expands to 210 configurations; the protocol's G0 prose still
says 162, and the independent checker records that arithmetic inconsistency as
a warning rather than silently changing the frozen file.

All 210 matrices pass the independent hash/schema/source-row/Sobol-prefix
checks, nonnegativity and substochasticity, zero sampled boundary hits, and the
eigenpair-residual threshold.  Increasing the Sobol budget reduces cross-seed
standard deviation at every grid: the six SD(256)/SD(64) ratios lie between
0.250 and 0.512, with median 0.321.  Nevertheless G1 is false because the
mean paired absolute shift exceeds 1% at m=24 and m=32.  G2 is also false:
q=8/q=12 gaps remain above 0.5% on five of six grids.  G3 passes because both
256-sample ensemble-mean dyadic trajectories shrink at the final step and the
m=96,128 means are within 1% of the R059 Fredholm reference.

The defensible interpretation is mixed finite-resolution evidence: sampling
variance is materially reduced, but coarse-grid and target-boundary phase
sensitivity are not resolved.  R060 neither rescues R059 G4 nor proves
continuous transfer-operator convergence.

Primary R060 outputs are
results/operator_variance_r060.json,
results/operator_variance_r060_check.json,
results/operator_variance_r060_analysis.json, and
research/refine-logs/R060_OPERATOR_VARIANCE_ANALYSIS.md.

## R061 update: common-cloud coarsening and localization audit (updated 2026-08-04)

R061 reuses the frozen R060 matrices read-only and projects the same finest-grid
cloud onto both coarser levels of the two historical R059 dyadic chains:
`96 -> 48 -> 24` and `128 -> 64 -> 32`.  It produces 136 derived CSR matrices
from 68 parent references.  The common-cloud rows inherit `s*r^2` fine samples
per coarse source cell, so they are not silently pooled with direct `s`-sample
estimators.

The independent CSR checker and the independent row-array checker both pass.
The spectral-gap component of G1 passes (all eight Sobol group medians are at
most 2%), while the stricter dyadic-smoothing component fails: the first chain
is smoothed, but the `32 -> 64 -> 128` chain is not uniformly rescued.  The
formal frozen G2 calculation also passes, but a post-freeze read-only audit
shows that its tau=1 cell-exposure variable is exactly the binary indicator of
nonzero target occupancy in all 136 arrays.  It therefore supports an
occupancy/support association, not internal target-cell boundary phase.  After
conditioning on occupancy-positive rows, the tau=0.125/0.25 correlations are
small, mixed, or negative.  G3 passes for common-cloud Gauss q=8 versus q=12 at
all four target grids, limited to the reported leading modulus.

The defensible conclusion is mixed and useful: common projection produces
small direct/common leading-modulus gaps and smooths one chain, but it also has
four or sixteen times the direct effective sample budget and does not establish
a universal smooth dyadic path.  Row discrepancy is concentrated on rows with
target support; internal-cell boundary phase remains unresolved.  These are
finite-matrix audit results, not a continuous operator limit, a global Hénon
zeta identity, or a Riemann/Hilbert--Pólya claim.  R059 G4 and all R060
decisions remain unchanged.

Reproduction:

    python scripts/run_common_coarsen_r061.py
    python scripts/check_common_coarsen_r061.py
    python scripts/localize_boundary_rows_r061.py --workers 8
    python scripts/check_boundary_localization_r061.py
    python scripts/analyze_common_coarsen_r061.py
    python scripts/audit_localization_interpretation_r061.py

Primary R061 outputs are
`results/common_coarsen_r061.json`,
`results/common_coarsen_r061_check.json`,
`results/boundary_localization_r061.json`,
`results/boundary_localization_r061_check.json`,
`results/common_coarsen_r061_analysis.json`,
`results/localization_interpretation_audit_r061.json`,
`research/refine-logs/R061_COMMON_CLOUD_ANALYSIS.md`, and
`research/refine-logs/R061_LOCALIZATION_INTERPRETATION_AUDIT.md`.
The reproducibility ledger is
`research/refine-logs/R061_COMMON_CLOUD_MANIFEST.md`.
