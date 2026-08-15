# Implementation notes — SD-C36

## Physical source/evaluator firewall

`code/source_core.py` and `code/generate_artifacts.py` contain neutral graph,
word, rational weight, code, roof, and determinant logic only. They do not
classify trial-division atoms, squares, Fibonacci numbers, modular supports,
or SHA-selected inventories.

`code/independent_evaluator.py` does not import the source implementation. It
reconstructs SCCs by transitive closure, cycles by vertex permutations,
primitive roots by coordinate periods, connectors by independent path
enumeration, and determinants by recurrent-SCC products. Source generation
instead uses Tarjan SCCs, DFS cycles, divisor roots, and Newton identities.

## Frozen C2 repair

The strict normal form requiring both connector interiors to avoid both cycles
is deliberately retained and fails 18,272 times. The repaired evaluator uses
arbitrary mutual paths in one SCC and has zero failures. The proxy failure and
the theorem-level result are separate fields and artifacts.

## Exact arithmetic and evidence boundary

- Counts, masks, words, and powered clock inequalities are integers.
- Weights, Kraft sums, roof shares, and polynomial coefficients are exact
  fractions serialized as `numerator/denominator`.
- Floating point decides no gate.
- The 1--4 vertex census is complete for the frozen class.
- Larger graphs, code cutoffs, inventories, and marker rows are deterministic
  finite controls and are never described as an infinite proof.

## Canonical execution and provenance

The authority runner creates three empty result directories. Runs A and B are
the required fresh double-run; run C is a cache-free cold start. Only A is
published, and only after all 19 hashes agree. A later metadata seal adds the
report, Route-A card, registries, and audit metadata while proving that none of
the 19 scientific bytes changed.

The first artifact stage keeps `source_commit`, `code_commit`, and
`source_lock.code_commit` equal to `PENDING_FIRST_ARTIFACT_COMMIT`. A future
root-owned metadata-only stage may replace all three simultaneously with the
same lowercase 40-hex artifact commit and regenerate the manifest. Mixed,
partial, or self-referential provenance is forbidden.
