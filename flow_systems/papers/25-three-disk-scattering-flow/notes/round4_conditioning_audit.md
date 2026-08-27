# P25 Round-4 conditioning and fallback-selection audit

Date: **2026-08-27**

## Material Passport

- Origin Skill: `ars-codex:academic-research-suite`
- Origin Workflow: Stage-1 research plus experiment-agent validation
- Input: frozen 2,241-row Round-3 direct-return-map ledger
- Input SHA-256:
  `1b932a5ca3cf7123e9428b3eb2f26078d8e289eabb11dd828379ecf39eeb414e`
- Verification Status: `VERIFIED / REPRODUCIBLE`
- Core-output combined SHA-256:
  `85566062639b3e42efb4ae47816be5a967e8948233727fc1d0ef24bdeb432265`

## Paper-facing result

Round 4 audits the only method switch in the completed Round-3 calculation.
Of 2,241 certified rows, 2,202 use direct fixed-point Newton and 39 first use a
high-precision specular-stationarity solve before the stability is recomputed
from the same direct physical return map.

`[NUMERICALLY_CERTIFIED]` for the frozen ledger:

- the 39 fallback rows were all `OPEN` in the historical Round-2 binary64
  check;
- their topological-length split is one row at length 11 and 38 at length 12;
- their geometry split is `4 / 10 / 25` at `d/a=5.8 / 6.0 / 6.2`;
- 38 have `|trace|>10^12`, and the remaining row has
  `10^9<|trace|<=10^12`;
- all 39 pass exactly the same post-refinement, multiscale, determinant,
  parity-corrected trace, and half-density thresholds as the direct-Newton
  rows; and
- the largest fallback half-density relative residual is
  `1.6711766389230827e-15`.

The static source-dependency audit checks ten functions in the Round-3 direct
map/refinement path.  None reads the paraxial trace, source half-density, prime
data, or zero data.  It also verifies that the fallback call occurs before the
paraxial trace is converted for numerical comparison inside `validate_row`.
The trace string is copied earlier into the output row for provenance, but the
refinement functions never consume it.  Thus the method switch was not selected
using success against the comparison target.

## Exact inference boundary

This is a post-hoc descriptive conditioning audit.  The source check proves an
implementation-order and dependency property; it does **not** prove statistical
unbiasedness, a causal law relating length to solver failure, or correctness
outside the frozen cutoff.  The fallback counts by `d/a` are reported, not
interpreted as a geometry effect.

The audit strengthens the prospective paper's methods and limitations sections:
the negative-control result is not being driven by silently dropping the 39
fallback-requiring refinement rows or by choosing their fallback after inspecting the
paraxial agreement.  It does not turn the finite-cutoff stability calibration
into a theorem.

## Route boundary

```text
PROPOSAL_STAGE=1
ROUTE_A_SCOPE=A0-A1_NEGATIVE_CONTROL
ROUND4_CONDITIONING_AUDIT=NUMERICALLY_CERTIFIED
ROUND4_INFERENCE_BOUNDARY=POST_HOC_DESCRIPTIVE_ONLY
HALF_DENSITY_EVIDENCE=NUMERICAL_OBSERVATION
HALF_DENSITY_CONTROL_VERDICT=STOP_SCOPED / PROVES_TOO_MUCH
FORMAL_A0_A4_TUPLE=UNASSIGNED
A2_EVALUATION=NOT_RUN
ROUTE_B_EVALUATION=NOT_RUN
ROUTE_B_INVOCATION_ALLOWED=false
GATES_A_E=NOT_REACHED
```

No new orbit solve, prime table, Riemann-zero data, exact determinant claim, or
Route promotion is part of Round 4.
