# Paper 25 Stage 4.5 Phase C internal-consistency audit

Audit time: **2026-08-30T12:27:09Z**  
Mode: **Stage 4.5 / final-check / current revised draft**  
Target: `notes/stage4_revision_round1.tex`  
Target SHA-256: `39a643c05b4820b782e45a5ec240caa7223ad444229e8a89bdcc98791ce23835`

## Result

**PASS for the checked Phase-C populations.** Two tables, the six registered
experiment-backed ClaimIntent surfaces, the current reproducibility lock, the
exact two-witness proof, and the route statements agree with their bound
sources. This result does not close the separately audited bibliography
metadata findings and is not a guarantee of mathematical correctness beyond
the recorded checks.

## C1. Data and numerical surfaces

The audit re-read the committed CSV/JSON carriers rather than copying numbers
from the prose.

| Checked family | Manuscript value | Independent carrier/recount | Result |
|---|---:|---:|---|
| Physical replay rows | 2,241 | CSV has 2,241 data rows | PASS |
| Rows per geometry | 747 | 747 for each of `29/5`, `6`, `31/5` | PASS |
| Scalar-clock matches | 3 per geometry | CSV boolean field gives 3 per geometry | PASS |
| Disagreements | 744 per geometry | CSV boolean field gives 744 per geometry | PASS |
| Exact witness rows | 6 | witness CSV has 6 data rows | PASS |
| Round-8 result digests | three declared hashes | all three current bytes match the Stage-4 receipt | PASS |
| Stage-4 inventory | 68 files | lock and replay receipt both report 68 checked files | PASS |
| Direct/historical tests | 75/75 | fresh `bash experiments/reproduce_stage4.sh` replay | PASS |

Stable result bindings:

- `results/round8_physical_roof_replay.csv`:
  `fa82c62ff34b8e674e78e37e800a5f31fdcbe3b986b37344a36719e30fa53e63`
- `results/round8_exact_roof_witnesses.csv`:
  `53acd2d60db18909e36ad0ad7c1ee505874117d5fbb32eeda1fc374d15530ad5`
- `results/round8_roof_nontransfer_summary.json`:
  `39bb90334d57eee2e9fa3678cb5079b2d8f087d60c607a052955bb0303cd4295`
- `experiments/stage4_reproducibility_lock.json`:
  `8848177095735a88437d7f335835f5ff6b200e701dbd75cb15370200522cb198`

The values are deterministic finite-cutoff validation surfaces. They are not
treated as independent statistical samples, asymptotic evidence, or an
additional proof of roof noncohomology.

## C2. Mathematical and documentary consistency

Eighteen named consistency families were checked:

1. title--abstract--conclusion claim boundary;
2. no-eclipse initial restriction and three frozen geometry labels;
3. period-two mean roof `d-2a`;
4. period-three mean roof `d-sqrt(3)a`;
5. exact gap `(2-sqrt(3))a`;
6. minimax lower bound `(2-sqrt(3))a/2`;
7. the telescoping necessary direction of the cohomology obstruction;
8. the owner- and repetition-preserving scope of the scalar-transfer no-go;
9. the finite no-repeat adjacency determinant;
10. the `q=3` primitive-owner count under the frozen orientation convention;
11. the local symplectic half-density identity and its non-arithmetic scope;
12. the four-object ownership map;
13. separation of exact proof from numerical replay;
14. registered ClaimIntent byte preservation;
15. Stage-4 lock/receipt/environment statements;
16. declarations, author identity, funding, and conflict statements;
17. symbolic-calibrator Route-A tuple versus physical-flow `UNASSIGNED`;
18. explicit non-invocation of Route B.

All eighteen are internally aligned on the frozen target. The Stage-4 bundle
validator passed. Token-conservation replay returned four expected advisory
families for authorized new numbers/citations/layout dimensions; semantic
review found no unregistered strengthening caused by those advisories.

## C3. Figure and table fidelity

Current population: **0 figures, 2 tables, 2 captions**.

| Table | Type | Trace | Result |
|---|---|---|---|
| `tab:object-map` | conceptual taxonomy | rows replayed against the surrounding object definitions and Route-A owner boundary; no data source is implied | PASS |
| `tab:replay` | deterministic result table | all 12 displayed cells rechecked against the committed replay CSV/summary | PASS |

There is no Figure Package because the figure denominator is zero. The
conceptual table is explicitly marked as a manuscript-level taxonomy, while
the replay table has a complete result trace.

## C4. Experiment provenance and reproducibility

- Scholar declaration: `status=experiments_declared`, `declared_by=scholar`,
  `declared_at=2026-08-29T05:52:42Z`.
- Registered current population: **6/6 experiment-backed ClaimIntent
  surfaces**; Stage-4 replay records each byte-exactly once.
- Historical provenance: seven Round-2--8 entries remain explicitly labelled
  retrospective transcriptions, not preregistrations.
- Fresh Stage-4 replay: **PASS**, 68 locked artifacts, 75/75 tests, two
  isolated Round-8 rebuilds matching each other and the canonical results,
  no canonical refresh, and no scientific-value change.
- The replay's evidentiary role remains
  `SOLVER_AND_REPRODUCIBILITY_VALIDATION_ONLY`.

## Build check

A marker-stripped isolated build using the current bibliography produced 13
A4 pages with zero undefined citations, undefined references, missing
characters, fatal errors, or overfull boxes. Consecutive PDFs were not
byte-identical because the build embeds volatile metadata, so this audit does
not claim byte-reproducible PDFs. No project PDF or canonical source was
overwritten.

## Boundary

This Phase-C PASS cannot override a Phase-A bibliography correction hold. It
does not promote `paper/manuscript.tex`, refresh canonical results, enter Stage
5, or award any Route gate credit.

