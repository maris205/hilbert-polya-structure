# P25 Stage-1 research brief

## Exact research question

For the frozen equilateral three-disk exterior billiard, does any statistic
derived solely from primitive periods, Poincare stability, orientation, and
reflection phase show arithmetic specificity that fails matched generic
controls?

## Object freeze

- Phase space: unit-energy exterior billiard flow for three radius-`a` disks.
- Centers: `(0,0)`, `(6a,0)`, `(3a,3 sqrt(3) a)`.
- Generator: unit-speed free flight plus specular reflection.
- Clock: Euclidean flight length.
- Primitive objects: primitive oriented cyclic words with no adjacent repeated
  disk symbol, subject to geometric realization.
- Repetition: the `r`th traversal of one primitive orbit; primitive and repeated
  words are never pooled.
- Quantum surface: exact multiple-scattering matrix determinant.
- Semiclassical surface: separately labeled curvature-expanded orbit zeta.

## Derived Stage-1 result

The altitude of the center triangle is `(sqrt(3)/2)d`.  The third disk does not
intersect the convex hull of either pair when `(sqrt(3)/2)d>2a`.  The frozen
value `d=6a` satisfies this strictly.  Thus `[PROVED]` the starting geometry is
not chosen at a pruning/eclipsing boundary.

## Arithmetic classification

The geometry contains a continuously variable shape parameter `d/a` and no
intrinsic arithmetic source, rational-prime owner, or prime-power repetition
law.  P25 is therefore an internally prespecified non-arithmetic calibrator.
Its A0-source status is `[MODELING_CHOICE] ABSENT_BY_CONSTRUCTION`; no formal A0
verdict or Route-A tuple is assigned at this Stage-1 checkpoint.

## Internally prespecified target-free falsification contract

The following design is `[MODELING_CHOICE]`; Round-2 execution is now complete:

1. Primitive words through topological word length 12 at neighboring
   geometries `d/a=5.8,6.0,6.2`.
2. Shuffled periods at fixed word/repetition structure.
3. Random phase and random stability controls.
4. Matched-density random integers and composites.
5. Exact multiple-scattering determinant kept distinct from the semiclassical
   truncated zeta at every cutoff.

## Two logically separate outcomes

1. **A0-source absence.** `[MODELING_CHOICE]` The frozen three-disk control has
   no intrinsic arithmetic owner.  This statement is part of the object design
   and is not estimated from the orbit ledger.
2. **Half-density proves-too-much test.** `[NUMERICAL_OBSERVATION]` All 747
   symbolic primitive words have reliable actual-orbit solutions at all three
   neighboring parameters.  Log-half-density correlations with the central
   geometry are `0.999998520` and `0.999998755`, above the frozen `0.98` stop
   threshold.  The half-density statistic therefore receives `[STOP_SCOPED] /
   PROVES_TOO_MUCH` as arithmetic evidence.  This does not supply the missing
   A0 arithmetic source.

## Concrete next artifact

Round 2 executed `results/three_disk_primitive_ledger_round2.csv` and
`results/three_disk_controls_round2.csv`.  The former separates exact symbolic
enumeration, center-polygon proxy, and actual reflection solutions; the latter
records neighboring parameters, deterministic period shuffling, random phase,
random stability, rank-integer, guaranteed-composite, and deterministic
random-integer controls.  See `notes/round2_conclusion.md`.

Round 3 additionally executes
`results/three_disk_return_map_validation_round3.csv`: a 100-digit physical
ray-map calculation with three finite-difference scales.  It expands the
independent stability validation from 9 to all 2,241 geometry rows and records
the trace-parity convention and condition-aware refinement method explicitly.
See `notes/round3_conclusion.md`.  The next paper-facing artifact is a
theorem/experiment boundary outline for the negative-control manuscript, not
an A2 evaluation.

Round 4 adds a conditioning and fallback-selection audit.  All 39 fallback
rows are exposed, retain the same final acceptance thresholds, and were chosen
by a refinement path that does not read the paraxial target fields.  The audit
is explicitly post-hoc and descriptive; it does not infer a causal dependence
on word length or geometry.  See `notes/round4_conditioning_audit.md`.

## Route mapping

```text
PROPOSAL_STAGE=1
ROUTE_A_SCOPE=A0-A1_NEGATIVE_CONTROL
A0_SOURCE_EVIDENCE=MODELING_CHOICE
A0_SOURCE_STATUS=ABSENT_BY_CONSTRUCTION
HALF_DENSITY_CONTROL_EVIDENCE=NUMERICAL_OBSERVATION
HALF_DENSITY_CONTROL_SCOPE=TOPOLOGICAL_WORD_LENGTH_LE_12
PROVES_TOO_MUCH_VERDICT=STOP_SCOPED_FOR_HALF_DENSITY_AS_ARITHMETIC_EVIDENCE
FORMAL_A0_A4_TUPLE=UNASSIGNED
FORMAL_EVALUATION_TRIGGER=UNMET_REQUIRED_INPUTS_AND_NO_ARITHMETIC_OWNER
ROUTE_B_EVALUATION=NOT_RUN
ROUTE_B_INVOCATION_ALLOWED=false
GATES_A_E=NOT_REACHED
```

Bracketed evidence tokens in the prose are restricted to `PROVED`,
`HEURISTIC`, `MODELING_CHOICE`, `OPEN`, `NUMERICAL_OBSERVATION`, and (only
after a positive control failure) `STOP_SCOPED`, as defined by
`skills/route-a-evaluator.md`.

## Primary sources checked on 2026-08-26

- Gaspard and Rice, *Semiclassical quantization of the scattering from a
  classically chaotic repellor*, https://doi.org/10.1063/1.456018.  Supports
  three-disk symbolic cycles and the semiclassical orbit/zeta surface.
- Gaspard and Rice, *Exact quantization of the scattering from a classically
  chaotic repellor*, https://doi.org/10.1063/1.456019.  Supports the exact
  multiple-scattering `S`-matrix surface.
- Wirzba, *Quantum mechanics and semiclassics of hyperbolic n-disk scattering
  systems*, https://doi.org/10.1016/S0370-1573(98)00036-2 and
  https://arxiv.org/abs/chao-dyn/9712015.  Supports the trace-class Fredholm
  determinant and the noncommuting cumulant/semiclassical limits.
- Ikawa, *Decay of solutions of the wave equation in the exterior of several
  convex bodies*, https://doi.org/10.5802/aif.1137.  Supports the hyperbolic
  exterior-scattering/no-eclipse setting.
