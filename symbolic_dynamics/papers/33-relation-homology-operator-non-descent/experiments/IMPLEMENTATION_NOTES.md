# Implementation Notes — Paper 33

## Source separation

`cycle_quotient_core.py` retains the exact research SHA
`3843f0871278c0c2544494be3fff1bca1def98bfb6b870141812fd90b8897168`.
`generate_results.py` retains the exact research-runner SHA
`03e840f8941e69220a467fa106a55939529bd1adbe1b2fe2d2e67d2fb1887335`
as a bridge witness only and is not run canonically.

The canonical source-only process is `source_generator.py`; it writes
`modulus_source_census.csv` before any prime/composite class is computed.
`post_census_classifier.py` reads that completed table, preserves every raw
column byte value, and appends the evaluator fields.  The AST separation audit
finds zero banned arithmetic identifiers in the core and source generator.

## Independent evaluation

`independent_evaluator.py` deliberately duplicates the finite mathematics and
imports no project module.  It independently rebuilds:

- all 191 projective state sets and `S/R` actions;
- all relation and adjacency-augmented ranks;
- all cusp counts, cusp returns, and arithmetic labels;
- all 191 seeded relabel controls;
- all 64 seeded random actions;
- all 21 twist rows;
- the cross graph and 31 diamond boundaries.

It performs 8349/8349 low-level checks.  Candidate-aware unit and integration
tests perform a further 1932/1932 assertions.

## Exact arithmetic

Sparse ranks use `F_1000003`, avoiding characteristics two and three.  This
validates finite certificates; theorem statements remain over `Q`.

The generator sequence is `R` then `S`; under right-to-left operator
composition its operator word is `SR`.

## Reproducibility

`run_exact_suite.py` executes the complete six-stage pipeline twice in new
temporary directories with `PYTHONDONTWRITEBYTECODE=1` and compares 20
payloads and each stage stdout against the authority freeze.

The SHA ledger uses paper-root-relative paths and includes every canonical
Python source plus experiment controls/reports and all non-meta result
payloads.  The final audit separately verifies Route-A v0.2 enums, paired
pending provenance, target-zero absence, source separation, byte identity,
cache absence, LF line endings, no trailing whitespace, and exact one-LF EOF.
The idempotence stage also rebuilds all five meta-integrity files from a fresh
directory containing only the 21 primary payloads, so the freeze has no hidden
dependency on stale metadata.
