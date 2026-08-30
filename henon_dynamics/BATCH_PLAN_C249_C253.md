# Route-A batch plan C249--C253

**Status:** frozen for implementation (2026-08-30)
**Baseline:** `3ff451e904f8f063e88c40ef87f4697a6586b1a5` (updated only if the
remote advances before release)
**Evaluator:** `flow_systems/skills/route-a-evaluator.md` v0.2.0,
SHA-256 `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
**Scope:** `NO_BAD_EULER_OR_ROOT_NUMBER`
**Fixed build epoch:** `1788048000`, `FORCE_SOURCE_DATE=1`, `TZ=UTC`

This round follows the Route-A roadmap's A1/A2-first policy. Every slot has a
different dynamical owner and one theorem-scale advance; the five manuscripts
are independent papers, not five slices of one calculation. All finite
receipts are source-local regression evidence. No candidate is allowed to
ingest target primes/zeros, arithmetic local data, Euler factors, root
numbers, automorphy, a target divisor/counting law, a functional equation, a
Hilbert--Pólya operator, or Route-B input.

## Frozen owners and advances

| ID | owner / subtype | theorem-scale advance | planned tuple |
|---|---|---|---|
| C249 | van der Pol--Liénard smooth dissipative ODE | global forward well-posedness, a Liénard trapping/existence argument with an implicit compact absorbing annulus, uniqueness and stability of the limit cycle in the frozen parameter regime, plus the Hopf/zero-damping boundary ledger and certified Poincaré receipts | `(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` |
| C250 | Ermakov--Pinney (isotonic) integrable Hamiltonian ODE | explicit quadratic Ermakov invariant, all positive solutions through the linear oscillator pair, exact turning radii/period/action, and the singular κ=0/equilibrium faces | `(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_NATURAL_QUANTIZATION)` |
| C251 | radius-1 synchronous majority cellular automaton (rule 232) | all-n fixed configurations and the unique nontrivial 2-cycle, domain-wall Lyapunov descent, sharp transient bound, and transfer-matrix basin/depth counts | `(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` |
| C252 | two-threshold hysteretic relay oscillator | exact event map on the switching section, a continuum of periodic cycles, finite-time entry from the interior, grazing boundary, and a no-Zeno theorem under the declared hybrid convention | `(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` |
| C253 | finite Moran birth--death population process | exact fixation probability for every selection ratio, rational Green/absorption-time solution, reversible killed-chain symmetrization, and neutral/zero-rate/singleton faces | `(A0_FAIL,A1_PASS_ANALYTIC,A2_FAIL,A3_FAIL,A4_FORMAL_HINT)` |

The only deliberately shared item is the evaluator and scope contract. C249
is the smooth dissipative owner; C250 is integrable singular Hamiltonian; C251
is discrete nonlinear symbolic; C252 is nonsmooth hybrid; C253 is stochastic
finite-state. Collision screening found no existing owner for these precise
models in C1--C248; this is a workspace collision statement, not a literature
priority claim.

## Evidence and release gates

Each package must contain the 27-file payload plus self-excluded release
manifest, independent producer/checker, exact or symbolic cross-check, byte
replay, hostile mutation suite, evaluator YAML, theorem/report documents, and
three deterministic manuscript PDFs (round 0, two substantive revisions).
The release script must verify payload hashes, fixed epoch, embedded fonts,
text extraction, no LaTeX/Python sidecars, and `paper/main.pdf ==
paper/main_round2.pdf`. The final batch review will aggregate checker,
symbolic, hostile, page, font, and hash counts and will stop before C254 until
the user confirms.

## Route-A stopping boundary

These candidates can establish source-local dynamics only. A0 is mandatory
for any arithmetic bridge, and no candidate has a source-derived arithmetic
origin. Therefore every strict tuple is expected to remain
`ROUTE_A_REJECTED` with `route_b_invocation_allowed: false`, even when A1 is a
genuine analytic pass. A failed or unstable implementation is to be pivoted
to a different owner rather than split into a fifth installment.
