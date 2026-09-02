# HCS-C285 — Gordon–Newell bottleneck condensation

This source-local package closes a complete theorem for arbitrary finite
irreducible, possibly nonreversible Gordon–Newell routing. It proves the
canonical product form `Z_N=h_N(w)`, all occupancy moment/covariance
derivatives, station and directed edge event flows, exact routing reversal and
the positive-population reversibility criterion, and the unique/tied
bottleneck thermodynamic limit with independent geometric nonbottlenecks and
`Dirichlet(1,...,1)` bottleneck shares.

The classical product-form and bottleneck lineage belongs to Gordon and
Newell (1967). This package makes no originality claim. Its deliverable is a
self-contained exact synthesis, explicit boundary atlas, independent
Fraction/SymPy reconstruction, byte replay, hostile mutation suite, three
substantive deterministic manuscript rounds, and a content-addressed release.

## Frozen identity

- Candidate: `HCS-C285`
- Source commit: `3878fa5282ca89f75700b3ef9d623f54dcb7bcf9`
- Evaluation date: `2026-09-02`
- `SOURCE_DATE_EPOCH=1788307200`
- Evaluator v0.2.0 SHA-256:
  `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`
- Scope literal: `NO_BAD_EULER_OR_ROOT_NUMBER`
- Route-A tuple:
  `(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`
- Overall: `ROUTE_A_REJECTED`
- Route B: `false`

## Package map

- `THEOREM_PACKAGE.md`: full theorem, proofs, asymptotic and boundary atlas.
- `SOURCE_AUDIT.md`: verified authoritative metadata and full-registry
  collision distinctions.
- `results/c285_gordon_newell_evidence.json`: canonical exact receipt.
- `code/c285_gordon_newell_producer.py`: deterministic producer.
- `code/c285_gordon_newell_checker.py`: producer-independent Fraction
  generator/left-nullspace/global-balance and semantic checker.
- `code/c285_gordon_newell_sympy_crosscheck.py`: independent symbolic layer.
- `code/c285_gordon_newell_replay.py`: two fresh-path byte replay.
- `code/c285_gordon_newell_mutation.py`: repaired-hash, duplicate/drop-replace,
  boundary, truncation, duplicate-key, and stale-hash attacks.
- `paper/main.tex` and three archived PDFs: two substantive paper-improvement
  rounds under deterministic LuaLaTeX.
- `C285_RELEASE_MANIFEST.json`: self-excluded 27-payload closure.

## Reproduce

Run from this directory:

```bash
PYTHONDONTWRITEBYTECODE=1 python -B code/c285_gordon_newell_producer.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c285_gordon_newell_checker.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c285_gordon_newell_sympy_crosscheck.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c285_gordon_newell_replay.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c285_gordon_newell_mutation.py
PYTHONDONTWRITEBYTECODE=1 python -B code/c285_release_manifest.py
```

Finite receipt rows are regression evidence. The all-parameter finite theorem
and `N->infinity` limit are carried by the written proofs.
