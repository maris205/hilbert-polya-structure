# P24 Round-6 validation report

## Material Passport

- Origin Skill: `ars-codex:academic-research-suite` plus experiment validation
- Origin Stage: Stage 1 research
- Verification Status: `VERIFIED / REPRODUCIBLE`
- Core-output SHA-256: `f5d31071c7174d84322c352b9028e334bf30e89a2368a751fbe58f6ab83ed660`
- Freeze SHA-256: `ea2ac26dfab2ff05f7ea4f179d76c96130559d94013d0f0f5b4689a44f730f89`

## Exhaustive panel

- Panel: identity plus all 24 elementary right Nielsen moves.
- Markings per system: `25`.
- Summary rows: `50`.
- Every marking uses four positive generators, alphabet size eight, 2,074
  canonical marked owners, and 19,624 raw cyclically reduced linear words.
- Candidate exact determinant and level-`(3)` checks: `PASS`.
- Maximum control determinant residual: `6.328e-58`.

The feasibility pilot disclosed in the freeze contract is not included as
evidence.  The executed family is canonical and exhaustive rather than a
selected subset, but the result remains exploratory rather than blind
confirmatory.

## Marking sensitivity

```text
candidate z range = [-2.00184797173, -1.08554792773]
candidate width   = 0.916300044002
control z range   = [-0.747750608375, 16.167541998]
control width     = 16.9152926064
signed contrasts = 25 negative / 0 positive
minimum |contrast| = 0.80803590015
```

Frozen exploratory criteria:

- candidate range-width pass: `true`;
- control range-width pass: `false`;
- constant signed-contrast direction: `true`;
- minimum absolute contrast pass: `true`.

Decision: `STOP_SCOPED_CURRENT_PHASE_STATISTIC_AS_MARKING_SENSITIVE`.

## Claim and Route boundary

The exact finite combinatorics and candidate matrix checks do not make the
finite-cutoff statistic presentation-invariant.  The control four-marking is
Tietze-redundant, not a matched presentation.  No full primitive spectrum,
group-conjugacy completeness, Gaussian-prime owner, metric spectrum, A1 pass,
or A2 result follows.

The conservative formal tuple

```text
(A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
overall = ROUTE_A_EXPLORATORY
```

belongs only to `P24-BIANCHI-MARKED-WORD-PROXY`.  The complete Bianchi flow
tuple remains `UNASSIGNED`; in particular, the proxy's explicit `A2_FAIL`
does not claim that a cusp-aware analytic Bianchi determinant is impossible.

```text
FULL_BIANCHI_FLOW_ROUTE_A_TUPLE=UNASSIGNED
ROUTE_B_EVALUATION=NOT_RUN
ROUTE_B_INVOCATION_ALLOWED=false
```
