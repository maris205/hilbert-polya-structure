# Paper 38 claim-driven exact experiment plan — SD-C40

Date frozen: 2026-08-15

Version: `SD-C40-stage1-plan-v1`

## Material passport

- Origin skills: `experiment-bridge`, `analyze-results`, and ARS experiment-agent
- Origin mode: implementation plan
- Verification status at freeze: `UNVERIFIED`
- Experiment type: deterministic exact analysis/simulation

## Objective and hypothesis

The experiment audits whether the presentation-canonical Bass--Serre tree
candidate owns a nonempty source-selective primitive ledger and ordinary
Fredholm determinant under the canonical modular cocycle. The preregistered
hypothesis is the terminal no-go tuple

`(A0_STRUCTURAL_ARITHMETIC_RELATION, A1_FAIL, A2_FAIL, A3_FAIL, A4_FAIL)`.

The implementation may confirm or falsify frozen statements but may not tune
the object, marker, cocycle, controls, or route after observing output.

## Claim map

| Claim | Minimum convincing evidence | Block |
|---|---|---|
| C1: full-tree ledger empty | theorem boundary plus finite rooted-tree edge/vertex and reduced-walk certificates | B1 |
| C2: full-tree Hashimoto owns no ordinary Fredholm determinant | theorem boundary plus orthogonal-column constant-norm and growing partial Hilbert--Schmidt mass | B1 |
| C3: orbital replacement is generic/divergent | exact residue, Burnside, Möbius, repetition, Euler-product, prime/composite and GBS controls | B2--B3 |
| C4: old marker cannot be inherited | elliptic-collapse, many-to-one and defining-relator witnesses | B4 |
| C5: implementation and provenance are reproducible | source/evaluator firewall, A/B/cold-C identity, metadata and integrity audits | B5 |

Anti-claim: a finite quotient, orbital trace, formal zero trace, or reciprocal-
infinite-stabilizer weight is the same ordinary full-tree Fredholm object.

## Setup

- Language: Python 3 standard library only.
- Arithmetic: integers and `fractions.Fraction` only.
- Entry command from the paper directory:
  `PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 python3 -I -B code/run_exact_integration.py`
- Independent audit command:
  `PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 python3 -I -B code/audit_integrity.py`
- Hardware: CPU only; no GPU.
- Network and external datasets: none.
- Expected wall time: under one minute on the current host.
- Timeout: five minutes; an overrun is a failure, not permission to broaden
  search.

## Inputs

| Input | Path | Role |
|---|---|---|
| frozen source fixtures | `code/source/source_core.py` | generates parameter, GBS, random-presentation and marker rows only |
| source emitter | `code/source/emit_packet.py` | canonical JSON transport |
| independent scientific evaluator | `code/evaluator/independent_evaluator.py` | independently parses and evaluates exact claims |
| packet adapter | `code/evaluator/evaluate_packet.py` | accepts raw or metadata-enveloped fixtures |
| Route evaluator | `code/evaluator/evaluate_route_a.py` | derives strict gate tuple solely from scientific output |
| stable research lock | `docs/RESEARCH_LOCK.json` | five immutable writer research files plus prototype provenance |

The integrated code contains all scientific logic. `/tmp/paper38_*` files are
never runtime dependencies.

## Experiment blocks

### B1 — Full-tree ownership sanity audit

For three finite rooted-tree controls, verify `|E|=|V|-1` and absence of a
reduced closed walk within the frozen ranges. For `r=1,2,4,5,6`, emit
orthogonal-column norms and partial Hilbert--Schmidt masses for 1, 2, 4, 8,
16, and 32 columns. These are finite consistency checks, not proofs of the
infinite statements.

### B2 — Exact conjugacy and Euler-product boundary

For each `r>=2` row and `1<=k<=12`, compute total positive-height classes by
Burnside and primitive counts by Möbius inversion. Check repetition for every
row. Independently enumerate multiplication-by-`r` residue orbits for
`r<=5`, `k<=6`. Compare the two Euler products coefficientwise through degree
12 with `(1-z)/(1-r*z)` and `(1-z/r)/(1-z)`. Keep `r=1` explicitly divergent.

### B3 — Generic-presentation firewall

Independently parse eighteen deliberate `BS(p,q)` relators and verify that
ascending, reversed, balanced, and non-ascending GBS controls share the full-
tree empty/non-Fredholm obstruction. Parse all 64 seeded random relators;
preserve ineligible status rather than assigning an unowned splitting.

### B4 — Marker and PROVES_TOO_MUCH firewalls

Compare old word length and absolute HNN height on stable letters, elliptic
base words, equal-tree/different-old-length pairs, defining relators, and
stable powers. Record that treating reciprocal infinite stabilizer size as
zero annihilates all GBS controls and is forbidden.

### B5 — Separation, reproducibility, and integrity

1. Parse Python imports and forbid source-to-evaluator or evaluator-to-source
   imports.
2. Run the source and evaluator in disjoint subprocesses for fresh A and B.
3. Copy only `code/source` and `code/evaluator` to an isolated temporary
   directory for cold C, run there, and remove it.
4. Require byte identity for source, science, and Route outputs across A/B/C.
5. Require stability under absent/null/empty/populated metadata and simulated
   future root-manifest absence/presence.
6. Materialize every canonical result twice and require no second-pass change.
7. Independently audit the closed result set, research lock, Route pending
   triple, ledger, UTF-8/LF/EOF hygiene, no caches, and Stage-1 manifest
   absence.

## Expected outputs and success criteria

| Output class | Path | Format | Criterion |
|---|---|---|---|
| canonical science | `results/scientific_results.json` and `results/runs/{A,B,C}/` | canonical JSON | 277/277 exact assertions and A/B/C byte identity |
| independent Route result | `results/route_evaluation.json` | canonical JSON | frozen five-gate tuple and Route-A rejection |
| exact tables | `results/*.csv` | UTF-8 CSV | row counts match frozen controls |
| reproducibility/boundary/metadata | `results/*certificate.json`, `results/*stability.json`, `results/source_evaluator_boundary.json` | canonical JSON | all stated booleans true |
| analysis | `results/analysis_summary.json` | canonical JSON | exact counts only, with no inferential overclaim |
| integrity evidence | `results/integrity_audit.json`, `results/exact_result_set.json`, `results/SHA256SUMS.txt` | canonical JSON / checksum ledger | full pass and closed path set |
| Route card | `evaluations/route_a/SD-C40/2026-08-15.yaml` | strict Route-A v0.2 YAML | literal pending provenance triple; separate hash |
| report | `EXPERIMENT_REPORT.md` | Markdown | claim/evidence boundary and terminal verdict stated |

## Run order and stopping

1. Verify stable research and plan locks and assert no root manifest.
2. Check source/evaluator physical and import separation.
3. Run B1 sanity checks first, then B2, B3, and B4.
4. Complete fresh A/B and isolated cold C.
5. Run four-state metadata, manifest-stability, idempotence, exact-set, and
   independent integrity checks.
6. Freeze the immutable ledger and fixed Route card.

Any failed exact assertion stops the run. A terminal scientific failure closes
the affine branch; it does not trigger hyperparameter search, representation
search, Route B, or a review loop.
