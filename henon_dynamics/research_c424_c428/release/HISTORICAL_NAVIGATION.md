# Historical Markdown navigation without altering evidence

2026-09-09 UTC. This is a coordinator-authorized navigation overlay,
not a rewritten source, mathematical review, release manifest or seal.
The original snapshots and copied review reports retain their bytes.

The initial Markdown scan at 07:41:43 UTC covered 227 files and 640
local-link occurrences. It found 40 literal destination misses:
36 in six C424 provenance copies, two in source-only baseline READMEs,
one in a relocated C428 review copy, and one renderer-dependent line
suffix in the outline review. No active README navigation was missing.
Later coordinator documents are handled by the separately recorded
delta in [PREFLIGHT_TREE.md](PREFLIGHT_TREE.md), not presumed present
at this initial scan. The coordinator-triggered document delta is now
completed in that report: all 47 local links in this overlay, including
the forty row-specific working routes, resolve. This checks the new
routes and does not relabel the forty original literal misses as fixed.

Each row below names one actual parsed link occurrence. Original
filenames are batch-relative; line numbers identify the inspected
unchanged source. Literal destinations are quoted as data, not offered
as working links. The working links are relative to this new file.
External-to-batch targets remain inside the same repository and need
the repository checkout; their existence does not make them members
of the batch-only payload.

## C424 copied provenance: all 36 occurrences

The paper [citation audit](../papers/C424_integer_valued_quadratic/CITATION_AUDIT.md)
identifies the source-copy policy. The original
[scout](../arithmetic_maps/SCOUT_REPORT.md) and
[proof](../arithmetic_maps/PROOF_PACKAGE.md) retain the correct relative
base. All three scout copies and all three proof copies were individually
compared byte-identical to those originals, first by the delegated link
auditor and again by the preflight author. The copies were not changed.
For the PDF-preflight link, the original companion JSON exists in
`arithmetic_maps/`; it was not copied beside these prose snapshots.

| No. | Original file | Line | Original literal destination | Working navigation | Reason |
| --- | --- | ---: | --- | --- | --- |
| 1 | `papers/C424_integer_valued_quadratic/evidence/SCOUT_REPORT.md` | 4 | `../SCOUT_PLAN.md` | [Batch scout plan](../SCOUT_PLAN.md) | Byte-identical copy retains its original relative base. |
| 2 | `papers/C424_integer_valued_quadratic/evidence/SCOUT_REPORT.md` | 56 | `../../continuation_c409_c413_round2/papers/C412_integer_henon/sections/2_normalization.tex` | [C412 normalization source](../../continuation_c409_c413_round2/papers/C412_integer_henon/sections/2_normalization.tex) | Byte-identical copy retains its original relative base. |
| 3 | `papers/C424_integer_valued_quadratic/evidence/SCOUT_REPORT.md` | 61 | `../../research_c419_c423/papers/C421_integral_return/sections/02_classification.tex` | [C421 classification source](../../research_c419_c423/papers/C421_integral_return/sections/02_classification.tex) | Byte-identical copy retains its original relative base. |
| 4 | `papers/C424_integer_valued_quadratic/evidence/SCOUT_REPORT.md` | 65 | `../../henon_padic_symplectic_analytic_interpolation_route_a/THEOREM_PACKAGE.md` | [p-adic interpolation package](../../henon_padic_symplectic_analytic_interpolation_route_a/THEOREM_PACKAGE.md) | Byte-identical copy retains its original relative base. |
| 5 | `papers/C424_integer_valued_quadratic/evidence/SCOUT_REPORT.md` | 68 | `../../research_c419_c423/arithmetic/SCOUT_REPORT.md` | [Prior arithmetic scout](../../research_c419_c423/arithmetic/SCOUT_REPORT.md) | Byte-identical copy retains its original relative base. |
| 6 | `papers/C424_integer_valued_quadratic/evidence/SCOUT_REPORT.md` | 72 | `../../research_c419_c423/continuation_round7/arithmetic_scout/SCOUT_REPORT.md` | [Prior round-seven arithmetic scout](../../research_c419_c423/continuation_round7/arithmetic_scout/SCOUT_REPORT.md) | Byte-identical copy retains its original relative base. |
| 7 | `papers/C424_integer_valued_quadratic/evidence/SCOUT_REPORT.md` | 77 | `../../research_c419_c423/continuation_round3/birational_arithmetic/FROZEN_CONTRACTS.md` | [Prior birational contracts](../../research_c419_c423/continuation_round3/birational_arithmetic/FROZEN_CONTRACTS.md) | Byte-identical copy retains its original relative base. |
| 8 | `papers/C424_integer_valued_quadratic/evidence/SCOUT_REPORT.md` | 80 | `../../research_c419_c423/continuation_round3/cubic_recurrence/FROZEN_CONTRACTS.md` | [Prior cubic-recurrence contracts](../../research_c419_c423/continuation_round3/cubic_recurrence/FROZEN_CONTRACTS.md) | Byte-identical copy retains its original relative base. |
| 9 | `papers/C424_integer_valued_quadratic/evidence/SCOUT_REPORT.md` | 83 | `../../research_c419_c423/continuation_round7/nonlinear_scout/SCOUT_REPORT.md` | [Prior nonlinear scout](../../research_c419_c423/continuation_round7/nonlinear_scout/SCOUT_REPORT.md) | Byte-identical copy retains its original relative base. |
| 10 | `papers/C424_integer_valued_quadratic/evidence/SCOUT_REPORT.md` | 85 | `../../henon_mcmillan_rational_route_a/THEOREM_PACKAGE.md` | [McMillan theorem package](../../henon_mcmillan_rational_route_a/THEOREM_PACKAGE.md) | Byte-identical copy retains its original relative base. |
| 11 | `papers/C424_integer_valued_quadratic/evidence/SCOUT_REPORT.md` | 94 | `LOCAL_PDF_PREFLIGHT.json` | [Original PDF-preflight receipt](../arithmetic_maps/LOCAL_PDF_PREFLIGHT.json) | Original companion is not beside relocated copy. |
| 12 | `papers/C424_integer_valued_quadratic/evidence/PROOF_PACKAGE.md` | 236 | `../../continuation_c409_c413_round2/papers/C412_integer_henon/sections/4_local_classification.tex` | [C412 local-classification source](../../continuation_c409_c413_round2/papers/C412_integer_henon/sections/4_local_classification.tex) | Byte-identical copy retains its original relative base. |
| 13 | `papers/C424_integer_valued_quadratic/baseline/round0/evidence/SCOUT_REPORT.md` | 4 | `../SCOUT_PLAN.md` | [Batch scout plan](../SCOUT_PLAN.md) | Byte-identical copy retains its original relative base. |
| 14 | `papers/C424_integer_valued_quadratic/baseline/round0/evidence/SCOUT_REPORT.md` | 56 | `../../continuation_c409_c413_round2/papers/C412_integer_henon/sections/2_normalization.tex` | [C412 normalization source](../../continuation_c409_c413_round2/papers/C412_integer_henon/sections/2_normalization.tex) | Byte-identical copy retains its original relative base. |
| 15 | `papers/C424_integer_valued_quadratic/baseline/round0/evidence/SCOUT_REPORT.md` | 61 | `../../research_c419_c423/papers/C421_integral_return/sections/02_classification.tex` | [C421 classification source](../../research_c419_c423/papers/C421_integral_return/sections/02_classification.tex) | Byte-identical copy retains its original relative base. |
| 16 | `papers/C424_integer_valued_quadratic/baseline/round0/evidence/SCOUT_REPORT.md` | 65 | `../../henon_padic_symplectic_analytic_interpolation_route_a/THEOREM_PACKAGE.md` | [p-adic interpolation package](../../henon_padic_symplectic_analytic_interpolation_route_a/THEOREM_PACKAGE.md) | Byte-identical copy retains its original relative base. |
| 17 | `papers/C424_integer_valued_quadratic/baseline/round0/evidence/SCOUT_REPORT.md` | 68 | `../../research_c419_c423/arithmetic/SCOUT_REPORT.md` | [Prior arithmetic scout](../../research_c419_c423/arithmetic/SCOUT_REPORT.md) | Byte-identical copy retains its original relative base. |
| 18 | `papers/C424_integer_valued_quadratic/baseline/round0/evidence/SCOUT_REPORT.md` | 72 | `../../research_c419_c423/continuation_round7/arithmetic_scout/SCOUT_REPORT.md` | [Prior round-seven arithmetic scout](../../research_c419_c423/continuation_round7/arithmetic_scout/SCOUT_REPORT.md) | Byte-identical copy retains its original relative base. |
| 19 | `papers/C424_integer_valued_quadratic/baseline/round0/evidence/SCOUT_REPORT.md` | 77 | `../../research_c419_c423/continuation_round3/birational_arithmetic/FROZEN_CONTRACTS.md` | [Prior birational contracts](../../research_c419_c423/continuation_round3/birational_arithmetic/FROZEN_CONTRACTS.md) | Byte-identical copy retains its original relative base. |
| 20 | `papers/C424_integer_valued_quadratic/baseline/round0/evidence/SCOUT_REPORT.md` | 80 | `../../research_c419_c423/continuation_round3/cubic_recurrence/FROZEN_CONTRACTS.md` | [Prior cubic-recurrence contracts](../../research_c419_c423/continuation_round3/cubic_recurrence/FROZEN_CONTRACTS.md) | Byte-identical copy retains its original relative base. |
| 21 | `papers/C424_integer_valued_quadratic/baseline/round0/evidence/SCOUT_REPORT.md` | 83 | `../../research_c419_c423/continuation_round7/nonlinear_scout/SCOUT_REPORT.md` | [Prior nonlinear scout](../../research_c419_c423/continuation_round7/nonlinear_scout/SCOUT_REPORT.md) | Byte-identical copy retains its original relative base. |
| 22 | `papers/C424_integer_valued_quadratic/baseline/round0/evidence/SCOUT_REPORT.md` | 85 | `../../henon_mcmillan_rational_route_a/THEOREM_PACKAGE.md` | [McMillan theorem package](../../henon_mcmillan_rational_route_a/THEOREM_PACKAGE.md) | Byte-identical copy retains its original relative base. |
| 23 | `papers/C424_integer_valued_quadratic/baseline/round0/evidence/SCOUT_REPORT.md` | 94 | `LOCAL_PDF_PREFLIGHT.json` | [Original PDF-preflight receipt](../arithmetic_maps/LOCAL_PDF_PREFLIGHT.json) | Original companion is not beside relocated copy. |
| 24 | `papers/C424_integer_valued_quadratic/baseline/round0/evidence/PROOF_PACKAGE.md` | 236 | `../../continuation_c409_c413_round2/papers/C412_integer_henon/sections/4_local_classification.tex` | [C412 local-classification source](../../continuation_c409_c413_round2/papers/C412_integer_henon/sections/4_local_classification.tex) | Byte-identical copy retains its original relative base. |
| 25 | `papers/C424_integer_valued_quadratic/baseline/round0_layout1/evidence/SCOUT_REPORT.md` | 4 | `../SCOUT_PLAN.md` | [Batch scout plan](../SCOUT_PLAN.md) | Byte-identical copy retains its original relative base. |
| 26 | `papers/C424_integer_valued_quadratic/baseline/round0_layout1/evidence/SCOUT_REPORT.md` | 56 | `../../continuation_c409_c413_round2/papers/C412_integer_henon/sections/2_normalization.tex` | [C412 normalization source](../../continuation_c409_c413_round2/papers/C412_integer_henon/sections/2_normalization.tex) | Byte-identical copy retains its original relative base. |
| 27 | `papers/C424_integer_valued_quadratic/baseline/round0_layout1/evidence/SCOUT_REPORT.md` | 61 | `../../research_c419_c423/papers/C421_integral_return/sections/02_classification.tex` | [C421 classification source](../../research_c419_c423/papers/C421_integral_return/sections/02_classification.tex) | Byte-identical copy retains its original relative base. |
| 28 | `papers/C424_integer_valued_quadratic/baseline/round0_layout1/evidence/SCOUT_REPORT.md` | 65 | `../../henon_padic_symplectic_analytic_interpolation_route_a/THEOREM_PACKAGE.md` | [p-adic interpolation package](../../henon_padic_symplectic_analytic_interpolation_route_a/THEOREM_PACKAGE.md) | Byte-identical copy retains its original relative base. |
| 29 | `papers/C424_integer_valued_quadratic/baseline/round0_layout1/evidence/SCOUT_REPORT.md` | 68 | `../../research_c419_c423/arithmetic/SCOUT_REPORT.md` | [Prior arithmetic scout](../../research_c419_c423/arithmetic/SCOUT_REPORT.md) | Byte-identical copy retains its original relative base. |
| 30 | `papers/C424_integer_valued_quadratic/baseline/round0_layout1/evidence/SCOUT_REPORT.md` | 72 | `../../research_c419_c423/continuation_round7/arithmetic_scout/SCOUT_REPORT.md` | [Prior round-seven arithmetic scout](../../research_c419_c423/continuation_round7/arithmetic_scout/SCOUT_REPORT.md) | Byte-identical copy retains its original relative base. |
| 31 | `papers/C424_integer_valued_quadratic/baseline/round0_layout1/evidence/SCOUT_REPORT.md` | 77 | `../../research_c419_c423/continuation_round3/birational_arithmetic/FROZEN_CONTRACTS.md` | [Prior birational contracts](../../research_c419_c423/continuation_round3/birational_arithmetic/FROZEN_CONTRACTS.md) | Byte-identical copy retains its original relative base. |
| 32 | `papers/C424_integer_valued_quadratic/baseline/round0_layout1/evidence/SCOUT_REPORT.md` | 80 | `../../research_c419_c423/continuation_round3/cubic_recurrence/FROZEN_CONTRACTS.md` | [Prior cubic-recurrence contracts](../../research_c419_c423/continuation_round3/cubic_recurrence/FROZEN_CONTRACTS.md) | Byte-identical copy retains its original relative base. |
| 33 | `papers/C424_integer_valued_quadratic/baseline/round0_layout1/evidence/SCOUT_REPORT.md` | 83 | `../../research_c419_c423/continuation_round7/nonlinear_scout/SCOUT_REPORT.md` | [Prior nonlinear scout](../../research_c419_c423/continuation_round7/nonlinear_scout/SCOUT_REPORT.md) | Byte-identical copy retains its original relative base. |
| 34 | `papers/C424_integer_valued_quadratic/baseline/round0_layout1/evidence/SCOUT_REPORT.md` | 85 | `../../henon_mcmillan_rational_route_a/THEOREM_PACKAGE.md` | [McMillan theorem package](../../henon_mcmillan_rational_route_a/THEOREM_PACKAGE.md) | Byte-identical copy retains its original relative base. |
| 35 | `papers/C424_integer_valued_quadratic/baseline/round0_layout1/evidence/SCOUT_REPORT.md` | 94 | `LOCAL_PDF_PREFLIGHT.json` | [Original PDF-preflight receipt](../arithmetic_maps/LOCAL_PDF_PREFLIGHT.json) | Original companion is not beside relocated copy. |
| 36 | `papers/C424_integer_valued_quadratic/baseline/round0_layout1/evidence/PROOF_PACKAGE.md` | 236 | `../../continuation_c409_c413_round2/papers/C412_integer_henon/sections/4_local_classification.tex` | [C412 local-classification source](../../continuation_c409_c413_round2/papers/C412_integer_henon/sections/4_local_classification.tex) | Byte-identical copy retains its original relative base. |

## Two source-only snapshots, copied review, and renderer suffix

For rows 37--38 the working target is the preserved **historical
initial handoff PDF**, not today's revised final PDF. Actual `cmp`
confirmed C426's `main_round0_original.pdf` equals
`builds/initial_02/main.pdf` and C428's equals
`builds/initial_03/main.pdf`. Neither source-only `baseline_source/`
directory contains its own `main.pdf`; no fake local PDF was added.

| No. | Original file | Line | Original literal destination | Working navigation | Reason |
| --- | --- | ---: | --- | --- | --- |
| 37 | `papers/C426_affine_good_models/builds/round1_revised/baseline_source/README.md` | 7 | `main.pdf` | [C426 historical initial handoff](../papers/C426_affine_good_models/main_round0_original.pdf) | Source-only archive extraction did not contain its adjacent historical PDF; the actual initial PDF is preserved separately. |
| 38 | `papers/C428_integer_period_spectrum/builds/round1_revised/baseline_source/README.md` | 7 | `main.pdf` | [C428 historical initial handoff](../papers/C428_integer_period_spectrum/main_round0_original.pdf) | Source-only archive extraction did not contain its adjacent historical PDF; the actual initial PDF is preserved separately. |
| 39 | `papers/C428_integer_period_spectrum/reviews/round2/REVIEW.md` | 17 | `../round1/C428_REVIEW.md` | [C428 canonical first manuscript review](../manuscript_reviews/round1/C428_REVIEW.md) | Unchanged copy of the canonical second report retains the canonical review-directory base; the paper-local first report has basename `REVIEW.md`. |
| 40 | `REVIEW_OUTLINE.md` | 84 | `BATCH_PLAN.md:150` | [Batch plan; historical review cites line 150](../BATCH_PLAN.md) | Plain CommonMark/GitHub navigation treats `:150` as part of the filename; an IDE-style renderer may instead interpret it as a line suffix. The plan itself exists. |

The [canonical second C428 report](../manuscript_reviews/round2/C428_REVIEW.md)
was byte-compared with its paper-local copy. Its first-review link works
at that original location. The current
[C426 final PDF](../papers/C426_affine_good_models/main.pdf) and
[C428 final PDF](../papers/C428_integer_period_spectrum/main.pdf) are
separate navigation options; they are not substituted for historical
PDFs in rows 37--38. No application rendering test was performed for
the outline's `:150` convention. The portable link here targets the
existing plan file and states the historical line reference in prose.

## Byte-preservation identities checked while preparing this overlay

| Artifact | SHA-256 |
| --- | --- |
| Original C424 scout and all three copies | `1749d3ef289818dd0b80576ef236d9abaecbf08c0118098f1bce028b9dffce14` |
| Original C424 proof and all three copies | `a8cf9e7b3f9b9f570beed1fc4b39815b84c648fcfbe3d62959c061b01b6eb63a` |
| C426 archived baseline README | `f7cdce38c694b3b5f5bceb6c8ced97759091fdd63917004668c9629ed7c8c1c7` |
| C428 archived baseline README | `05ccda3c1b5d3911fb641a3e291fb6f70879776023b5b507f2545472b8c8af12` |
| C428 canonical and copied second review | `724dc2ba066ba48d25822664e12f2a36a727e30ccd43b3a45595c6f1b1178042` |
| Original outline review | `52885c212b4a47de96344f8dae30bb2ee8517a1ebd46eeec6ae0c3350150528b` |
| C426 historical initial handoff PDF | `85677da439f31f1c2faea804430c8f395a2aaa235a0d20696e0a97a8ca08ed38` |
| C428 historical initial handoff PDF | `d5aeb4ae86009dc9f229a54c50083ccb03eba1f3bdc562d13a12400140dd8cde` |

The forty original literal misses are deliberately retained, not erased
or represented as newly working at their original locations. This overlay
supplies navigable alternatives and preserves provenance. It does not
reopen completed mathematical checks, rewrite historical status lines,
or certify the eventual release membership.
