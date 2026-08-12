# Stage 01 — Session 4 Symbolic-Dynamics Scope Screening

Status: **COMPLETE / FROZEN**

Parent index: [Hilbert–Pólya Symbolic-Dynamics Subproject](../../README.md)

Shared rules: [proposal](../../../propose-symbolic-dynamics.md),
[Route A](../../../skills/route-a-evaluator.md), and
[Route B](../../../skills/route-b-evaluator.md)

This directory is the Session 4 research package for the Hilbert–Pólya
structure program.  The only primary system family in this package is
**symbolic dynamics**.

The research question is:

> Which parts of a Riemann-type arithmetic dynamical model can be supplied by
> a symbolic grammar, and which parts cannot be obtained without a separate
> geometric carrier?

The session is deliberately falsification-first.  A symbolic model is not
credited for reproducing a target after primes, \(\log p\), von Mangoldt
weights, phases, or Riemann zeros have been inserted into its definition.
Route A begins at the arithmetic-origin gate.  Route B is unavailable unless
one *single frozen construction* reaches `A4_ROUTE_B_READY`.

## Frozen research lines

| ID | Symbolic object | Purpose |
|---|---|---|
| `SD-C01` | full \(q\)-shift over \(\mathbb F_q\), plus the finite-memory weighted class | Exact function-field prime/repetition ledger and finite-state divisor-growth gate |
| `SD-C02` | squarefree \(\mathscr B\)-admissible subshift | Test whether direct rational-prime arithmetic in the grammar produces periodic prime orbits |
| `SD-C03` | weighted loop/renewal shift | Test countable-state flexibility, positivity, and inverse-design non-identifiability |
| `SD-C04` | Gauss continued-fraction shift with the Mayer transfer operator | Strongest natural arithmetic/analytic symbolic benchmark; audit the missing rational-prime ledger and geometry interface |
| `SD-C05` | recursive wheel-sieve level shift | Strongest endogenous rational-prime generator found in the session; test whether it has any periodic-orbit dynamics |
| `SD-C06` | Knauf number-theoretical spin-chain recursion | Prior-art collision test for an exact zeta quotient and a proposed Liouville-signed refinement |

The objects, forbidden data, controls, and stop rules are frozen in
[`SESSION4_PREREGISTRATION.md`](SESSION4_PREREGISTRATION.md) before the
experiments are run.

## Navigation

- [`paper/main.pdf`](paper/main.pdf) — shareable Stage-01 paper; its LaTeX,
  figures, claims–evidence plan, and improvement record are in [`paper/`](paper/).
- [`SESSION4_SUMMARY.md`](SESSION4_SUMMARY.md) — final ten-question synthesis,
  Route-A matrix, strongest surviving lead, and strongest negative theorem.
- [`SESSION4_PREREGISTRATION.md`](SESSION4_PREREGISTRATION.md) — source locks,
  data separation, controls, and stop rules.
- [`EXPERIMENT_REPORT.md`](EXPERIMENT_REPORT.md) — numerical results, exact
  certificates, failures, and reproduction commands.
- `finite_state_arithmetic_skeleton/` — `SD-C01`.
- `squarefree_admissible_shift/` — `SD-C02`.
- `renewal_inverse_design_obstruction/` — `SD-C03`.
- `farey_gauss_transfer/` — `SD-C04`.
- `wheel_sieve_level_shift/` — `SD-C05`.
- `knauf_spin_chain_audit/` — `SD-C06`.
- `evaluations/route_a/` — append-only Route-A records.
- `evaluations/route_b/` — intentionally empty; no candidate passed the
  same-object Route-B gate.
- [`docs/candidate_registry.md`](docs/candidate_registry.md) — session candidate
  ledger.
- [`docs/obstruction_registry.md`](docs/obstruction_registry.md) — reusable
  symbolic no-go results.
- [`docs/operator_obligations.md`](docs/operator_obligations.md) — obligations
  recorded without prematurely invoking Route B.
- [`ROUND2_CLUES.md`](ROUND2_CLUES.md) — ideas that would leave symbolic
  dynamics and therefore are not developed here.
- [`STAGE_MANIFEST.sha256`](STAGE_MANIFEST.sha256) — self-contained artifact
  checksums, verified from this directory.

## Claim discipline

Every substantive item is labelled with one of the Route-A evidence labels:

`PROVED`, `CONDITIONAL_THEOREM`, `NUMERICALLY_CERTIFIED`,
`NUMERICAL_OBSERVATION`, `HEURISTIC`, `MODELING_CHOICE`,
`FITTED_PARAMETER`, `OPEN`, `REFUTED`, `NOT_TESTABLE`, or `STOP_SCOPED`.

No Riemann-zero table is an input to this package.

All paths stored in the Route-A YAML records are relative to this Stage-01
root; each record declares the umbrella-relative `artifact_path_base` that
selects this directory.  Historical absolute paths in run metadata remain
provenance from the original run and are not rewritten during relocation.

## Final outcome

No frozen candidate passes A0 through A4 as one object, and no Route-B
evaluation is authorized.  `SD-C05` is the strongest endogenous
rational-prime lead but is acyclic; `SD-C04` is the strongest natural
Fredholm determinant but has the wrong primitive arithmetic species; `SD-C06`
is the strongest exact zeta-quotient collision but has no primitive-orbit
Fredholm ledger.  These strengths are not combined.

The most reusable result is a proved obstruction: every finite-state,
finite-memory weighted determinant with a finite-dimensional cocycle has
divisor count $O(R)$, incompatible with the completed Riemann
$\Theta(R\log R)$ divisor.  Its finite-memory scope boundary is explicit.
