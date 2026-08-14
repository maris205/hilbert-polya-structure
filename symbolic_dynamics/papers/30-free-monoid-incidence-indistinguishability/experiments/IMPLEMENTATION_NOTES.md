# SD-C32 implementation notes

## Provenance locks

- Research package: `/tmp/paper30_research_package.md`, SHA-256
  `98b58fd77ac6bd3fd7aa5c1f662d2203a34fa2891c631fad36ed8c9a19f45b1d`.
- Exact prototype ledger: `/tmp/paper30_global_coherence_prototype/SHA256SUMS.txt`,
  SHA-256 `a7df78b607500c687981e731764ca0c7adc21489c36d4be29ffa36a802b46472`.
- Prototype report: SHA-256
  `9d107b3919bd327f4c56f4f7577a49f8d8d4630baba9b83ad756ae2977b61e8a`.

The authority code is a path-only mechanical integration of the prototype
candidate, generator, independent evaluator, tests, and analysis.  Authority
wrappers add isolated double-run, Route-A, integrity, and SHA checks without
altering the frozen selector.

## Source separation

`code/independent_evaluator.py` imports neither `coherence_core` nor
`generate_results`.  It reads only serialized JSON/CSV artifacts and
recomputes the decisive counts, rational identities, clone equalities, marker
relations, route locks, and no-target-zero declarations.

The candidate compiler derives atoms only as bottom covers.  Numeric roof
marks are transported data used after source selection; candidate code does
not call primality, factorization, zeta-zero, or target-coefficient oracles.

## Run order

`experiments/run_exact_suite.py` performs, for each of two isolated temporary
directories:

1. exact generation (sanity, baseline, finite controls, masks, UFD clone,
   analytic and marker ledgers);
2. independent serialized-artifact evaluation;
3. deterministic unit tests; and
4. bounded Observation–Interpretation–Implication–Next-step analysis.

Only after all 17 artifacts are byte-identical is the first fresh directory
published to `results/`.  Deterministic metadata, integrity audit, and a
31-entry code/result SHA ledger are then created.

## Theorem boundary

The source isomorphism theorem covers every local or nonlocal invariant natural
in the frozen decorated multiplicative data.  It does not cover an enrichment
by independently derived addition, congruence, Archimedean order, or another
nontransportable operation.  The prototype illustrates the theorem and proves
the finite ledgers; it does not numerically establish the infinite theorem.
