# HCS-C26 experiment plan

## Objective

Decide the holomorphic/no-localizer gate for the literal unsmoothed AGY
metaplectic transfer family in one large round.  Produce a theorem-level
negative result if bounded constants and point evaluation expose the C24
atomic obstruction; investigate scalar holomorphic nuclearity only as a
separable strengthening.

## Gate ledger

| Gate | Test | Pass condition | Failure action |
|---|---|---|---|
| G1 source lock | Reuse the exact HCS-C25 AGY section, weights, and chronological lifts | No altered dynamics or averaged matrices | Stop and repair conventions |
| G2 slice identity | Compute `E_x0 L_s J` | Exact countable atom sum with coefficients `w_s,gamma(x0)` | Main theorem fails |
| G3 summability | Audit the coefficient sequence | `ell^1`, hence `ell^2`, for every `Re(s)>-sigma_0` | Restrict the half-plane honestly |
| G4 noncancellation | Apply C25 decoder and full-rank projection | Distinct projected symplectic atoms | Aggregate with true central signs |
| G5 essential norm | Apply C24 Theorem 3 and the compact ideal inequality | Strict positive lower bound | Reopen theorem audit |
| G6 exact witness | Rebuild `gamma_*`, `B`, `x0`, `S_*`, and `j_*` | Exact equality with C25 and explicit one-atom bound | Reject certificate |
| G7 independent replay | Separate checker plus mutations | Every gate and mutation passes | Do not release |
| G8 scalar complex domain | Prove common `Omega`, compact containment, log branch, and norm sum | All hypotheses of cited nuclearity theorem verified | Mark scalar half open |
| G9 Route A | Score A1--A4 without optimism | Evidence-linked verdict | No Route B unless authorized |

## Theorem deliverables

1. Evaluation-slice essential-norm theorem for Banach function spaces.
2. AGY holomorphic corollary throughout `Re(s)>-sigma_0`.
3. Explicit lower bound from the certified length-128 branch.
4. A tensor-slice extension for natural anisotropic spaces, stated only
   under explicit bounded slice and summability assumptions.
5. A scalar-versus-oscillator dichotomy if, and only if, G8 passes.

## Code deliverables

- `code/c26_producer.py`: independent exact reconstruction and certificate;
- `code/c26_independent_check.py`: no imports from producer;
- `code/test_c26.py`: unit and mutation tests;
- `code/c26_hash_manifest.py`: release hashes;
- `code/run_c26.sh`: deterministic one-command reproduction;
- `results/`: JSON certificates plus test, validation, and material reports.

The code verifies hypotheses and conventions.  It does not pretend to prove
the infinite-dimensional C24 theorem or the all-length C25 decoder by finite
enumeration.

## Stop and pivot rules

- **CLOSE / PIVOT:** G1--G7 pass.  Publish the no-go theorem and move to
  finite Weil fibres; do not enumerate more AGY return words.
- **STRONG CLOSE:** G1--G8 pass.  Publish the sharp same-domain scalar versus
  oscillator dichotomy, then move to finite Weil fibres.
- **HOLD:** the point-evaluation theorem passes but the scalar complex domain
  remains unproved.  Release only the strict theorem and list the scalar
  statement as an explicit open gate.
- **KILL:** a genuine projected-atom cancellation or coefficient
  nonsummability invalidates the slice.  Record the counterexample and change
  dynamical form.

## Route-A forecast

The target remains an obstruction study, so the expected classification is

\[
(\mathrm{A1\_WEAK},\mathrm{A2\_FAIL},
  \mathrm{A3\_FAIL},\mathrm{A4\_FORMAL\_HINT}),
\qquad \mathrm{ROUTE\_A\_REJECTED}.
\]

The useful advance is a larger closure class, not an improved RH score.
