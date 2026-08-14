# SD-C34 implementation notes

## Frozen provenance

- Research package:
  `b34dd0489fae5080c683bedcaed6ddcc56025ddad6854da6e786c50c36fa61fb`.
- Prototype candidate core:
  `e7ad9ff5f515973d4a0d9a991be912961f2b7492dcac7ecf0006bf490c6179cf`.
- Prototype evaluator/runner:
  `cb6b128b9b3ace9cd39cf11ffe4ff02ac077d2bc923470bb61dd41580877616a`.
- Prototype seven-payload ledger:
  `f7c2e0f1c1be4bdce325515feb83a80bebfaf36e5785c39b31bcb12d9481d5e6`.

## Physical source separation

`code/residue_core.py` and `code/generate_results.py` own only residue-ring
projective construction and prime-blind controls. The independent evaluator
imports neither file. It reconstructs every finite object from first
principles, applies arithmetic labels only after reading the candidate
census, and verifies all transported operation-table entries and graph edges.

## Reproducibility gates

The test module defaults to authority `results/` and the isolated runner
overrides that location for each fresh directory. Its source-oracle test also
contains the complete-tree audit regression. The inventory normalizer removes
`integrity_audit.json` and `SHA256SUMS.txt` symmetrically, so the same audit
command must pass before and after self-generated freeze files exist.

The canonical suite runs sanity first, creates two isolated result trees,
requires all 16 fresh artifacts to be byte-identical, publishes one tree,
writes metadata, audits the route/science/source/hygiene boundary, and finally
freezes exactly eight Python sources plus 23 result artifacts.

## Ownership firewall

Finite rational majorants are diagnostic witnesses for the separately proved
trace-class estimate. The ordinary determinant belongs to the original
uninduced graph on `Re(s)>2`; it is not a prime determinant because the same
graph contains every universal `S/R` return and every cusp diamond. The
static `n+1` equality is evaluator-only and never gates candidate recurrence.
