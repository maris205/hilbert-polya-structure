# Exact authority experiment plan — SD-C37

**Freeze status:** frozen after both Paper 35 preregistrations and before
authority output generation.

## Claim-to-certificate matrix

| ID | Frozen audit | Exact success condition | Primary artifact |
|---|---|---|---|
| E1 | authority height / positive DAG | every U/V edge has the source-locked increment; independent Kahn audit finds no cycle | `height_dag_ledger.csv` |
| E2 | symmetric backtracks | one primitive two-step immediate reversal per positive edge, excluded by Hashimoto semantics | `backtrack_ledger.csv` |
| E3 | reduced affine cycles | exhaustive words and eight explicit witnesses retain primitive length-`r+3` relation cycles | `admissible_word_census.csv`, `relation_witnesses.json` |
| E4 | generic controls | dilation commutators and arbitrary one-relator mutations retain relation polygons without acceptance labels | `commutation_witnesses.json`, `monoid_relation_controls.json` |
| E5 | operator boundary | exact unweighted norm bounds and disjoint nonzero image-support witnesses; full infinite-outdegree graph stays theorem-only | `operator_certificates.json`, `full_monoid_boundary.json` |
| E6 | finite quotients | all relation words persist, all `U_q^q` cycles appear, and small-modulus degenerations remain visible | `quotient_ledger.csv` |
| E7 | diagonal object firewall | determinant product, Newton coefficients, and trace-log coefficients agree exactly without object conflation | `bc_diagonal_fixtures.json`, `bc_firewall.json` |
| E8 | marker / cancellation boundary | prime-Fock labels occur only after source freeze; signed/matrix/groupoid limits stay scoped | `fock_marker_firewall.json`, `boundary_controls.json` |
| E9 | strict Route evaluation | v0.2 keys/enums, exact NA strings, paired PENDING provenance, rejected tuple, and Route B false | `evaluations/route_a/SD-C37/2026-08-15.yaml` |
| E10 | reproducibility | A=B=C, independent evaluator, exact tests, metadata stability, hygiene, idempotence, and SHA all pass | reproducibility and integrity metadata |

## Run order

1. Freeze this file and `experiments/PREREGISTRATION.md`.
2. Adapt the `/tmp` implementation to authority height and unweighted operator
   conventions; scan physical source/evaluator separation.
3. Run source generation, independent evaluation, tests, and analysis in fresh
   A and B directories.
4. Remove caches and repeat the full pipeline in a third initially empty cold
   start C directory.
5. Publish A only after all scientific artifact hashes agree across A/B/C.
6. Write `EXPERIMENT_REPORT.md`, strict Route-A YAML, registries, schema, and
   tracker without modifying the published scientific payloads.
7. Certify metadata-seal stability, exact inventory, Route schema, hygiene,
   source separation, research hashes, and non-self-referential SHA ledger.
8. Run freeze and integrity twice; certify byte/stdout idempotence and recheck
   the ledger.

## Analysis format

The authority analysis contains an exact raw-data table. Each numbered
finding contains Observation, Interpretation, Implication, and Next step. No
mean, standard deviation, confidence interval, or multiple-seed statistic is
reported because the protocol is a deterministic exact census.

## Stop rules

- stop on any authority-height mismatch;
- stop if an immediate backtrack is Hashimoto-admissible;
- stop if the affine relation disappears or a generic control is silently
  discarded;
- stop if quotient cycles are presented as infinite-ledger descent;
- stop if a BC/Fock scalar is presented as the same graph-step determinant;
- stop if a finite operator witness is promoted to an infinite numerical
  proof;
- stop if any Route target/root metric is numeric or null;
- stop on any mixed provenance token, Route B true, cache, symlink, inventory
  surplus, schema drift, hygiene failure, or scientific-byte change after
  metadata.

## Authorized write boundary

Writes are confined to `code/`, `results/`, `experiments/`,
`EXPERIMENT_REPORT.md`, `docs/`, and `evaluations/route_a/SD-C37/` within the
Paper 35 scaffold. Root README/source/writer documents, sections, figures,
LaTeX/PDF/compilation files, manifests, repository root files, Git, and mirror
are read-only and outside this plan.
