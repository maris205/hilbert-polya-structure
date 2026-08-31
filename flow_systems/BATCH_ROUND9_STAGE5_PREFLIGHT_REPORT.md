# Round 9 Papers 24--28 — Stage 5 content-proof preflight

Date: **2026-08-31 UTC**  
Pipeline state: **Stage 5 in progress; five preflights PASS; one scholar content confirmation pending**  
Final PDFs: **0/5 emitted**

## Decision and scope

The scholar's exact response was:

> 确认

It answers the immediately preceding mandatory Stage-5 entry prompt.  The
already selected citation profile remains
`natbib[numbers,sort&compress] + \bibliographystyle{plainnat}`.  This entry
decision is distinct from the in-stage confirmation that the five content
proofs are correct.

Stage 5 is format-only.  It has not changed scientific prose, formulas,
citations, declarations, frozen dynamical objects, initial subtype
restrictions, results, canonical `paper/` trees, Route tuples, or claim
strength.  It has not submitted, released, or contacted anyone about a paper.

## Batch result

All five accepted Stage-4.5 manuscripts were transferred into isolated
finalization workspaces.  The formatter removed 599 standalone
`<!--block:B####-->` transport markers in total.  Paper 25 additionally
removed four inline `ref` and four inline `anchor` audit comments.  No other
source byte was changed.  The accepted bibliographies and Stage-4.5 preview
PDFs were copied byte-for-byte.

| Paper | Stage-5 source SHA-256 | Content proof | Pages | Citation/Bib closure | Explicit paper result carried into Stage 5 |
|---|---|---:|---:|---:|---|
| [P24](papers/24-bianchi-holonomy-flow/README.md) | `153e80d360b35c25cac8f0ad2fc1cea14ba43afed07ce7fbb59b9f48c7baeb4e` | [PDF](papers/24-bianchi-holonomy-flow/stage5_finalization/content_proof.pdf) | 15 | 9 commands / 7 keys / 7 entries | Ring-general first-congruence-jet trace universality and a distinct-owner witness are retained; the loxodromic joint descriptor reduces the largest observed bucket from 208 to 84 but yields zero singletons. |
| [P25](papers/25-three-disk-scattering-flow/README.md) | `9c7782ebf6a90f0e33ab86f2e77d7ce78ecfb2ad0ddb9413e4829cfe33f776e1` | [PDF](papers/25-three-disk-scattering-flow/stage5_finalization/content_proof.pdf) | 13 | 13 commands / 8 keys / 8 entries | The exact roof-nontransfer theorem and the 2,241-row validation-only estimand remain the paper's clear negative transfer result; the physical flow is not credited with the unit-roof determinant. |
| [P26](papers/26-level11-newform-time-change/README.md) | `fca2b382c3d64273ccb6c17d63330ecfad20ff02087b001175c1003bb4006fd3` | [PDF](papers/26-level11-newform-time-change/stage5_finalization/content_proof.pdf) | 16 | 9 commands / 7 keys / 7 entries | The exact 138-instance/55-group owner taxonomy, two negative controls, and zero both-controls-pass residue retain the scoped nonfactorization result without promotion to a global Euler owner. |
| [P27](papers/27-congruence-inverse-limit-no-go/README.md) | `bbac2f5dd43149348c33da883e2b7fe0d342abdf932723ea859edf70d46d5e48` | [PDF](papers/27-congruence-inverse-limit-no-go/stage5_finalization/content_proof.pdf) | 13 | 5 commands / 5 keys / 5 entries | The congruence residual renormalization no-go and the homology-cover four-quadrant calibration remain two explicitly separated negative candidate results. |
| [P28](papers/28-bolza-magnetic-flow/README.md) | `14ad8eeaa7cdd55bc889adc250630a7b18a9e20e316d4fb6becddb9e05922d22` | [PDF](papers/28-bolza-magnetic-flow/stage5_finalization/content_proof.pdf) | 14 | 9 commands / 6 keys / 6 entries | Exact nonarithmeticity, the finite completeness certificate, and the exact systole chain remain the positive control result; the magnetic/arithmetical transfer remains unclaimed. |

Total: **71 pages**, **45 LaTeX citation-command instances**, **33 unique
citation keys**, and **33 BibTeX entries**, with zero missing keys, zero
orphans, and zero duplicate keys.

## Independent format and build validation

For every paper an isolated temporary workspace ran:

```text
LuaLaTeX -> BibTeX -> LuaLaTeX -> LuaLaTeX
```

All 20 commands returned successfully.  The final logs contain zero fatal
errors, unresolved citations, unresolved references, overfull boxes, or
missing-glyph diagnostics.  Each replay has the expected page count, and its
`pdftotext -layout` stream is byte-identical to the corresponding accepted
content proof.  Required author, affiliation, email, funding, conflict,
contribution, availability, ethics, AI-disclosure, and limitation surfaces
are present.

The independent batch validator passes **283/283** checks across all five
papers and 10 frozen canonical/result trees.  Its machine receipt is
[BATCH_ROUND9_STAGE5_PREFLIGHT_RECEIPT.json](BATCH_ROUND9_STAGE5_PREFLIGHT_RECEIPT.json),
SHA-256
`87b99ed793690c245304e1e117bb09e3890152c4da2648801549f62fd1a8a952`.
The prior Stage-4.5 validator was also replayed after materialization and still
passes **397/397** checks.

Pandoc conversion is materially lossy for all five papers: theorem/cross-
reference structures, citation handling, mathematical constructs, or literal
artifact paths are weakened or omitted.  Therefore no DOCX or Pandoc-derived
manuscript is presented as equivalent.  LaTeX/BibTeX remain authoritative,
and the final PDFs will be compiled from LaTeX only after content
confirmation.

## Entry advisories

The mandatory advisory order was executed against each exact accepted draft:

1. `#660` has schema-valid carriers but reports
   `HEURISTIC-ADVISORY / UNMEASURED / not_checked /
   SNAPSHOT_NOT_PROVIDED`.  No phrase snapshot was supplied, so this is not a
   clean-draft certificate.
2. `#672` returned exactly
   `ADVISORY_UNAVAILABLE:NAMED_INPUT_UNREADABLE` for all five papers because
   no exact builder-produced preregistration artifact and source manifest were
   available.  No carrier or unavailable status was fabricated.

Both states are nonblocking advisories.  They do not assert clean wording,
cross-document agreement, inconsistency, or scientific correctness.

## Roadmap crosswalk and frozen dynamical scope

The governing files remain byte-locked:

- `skills/route-a-evaluator.md` —
  `6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c`;
- `skills/route-b-evaluator.md` —
  `170eca554350e6116c024619a204a3673eaa52ba2cff991952d6a88a7d7d9595`.

Stage-5 formatting gives no Route credit.  Papers 24--28 remain in Route A's
early A0--A1 / A1--A2 evidence layer; positive arithmetic A2 is **0/5** and
Route-B invocation is **0/5**.  Paper 25's
`A2_ANALYTIC_DETERMINANT` belongs only to its nonarithmetic unit-roof symbolic
calibrator and is not counted as a positive arithmetic A2 result.

The initial dynamical restrictions remain unchanged: the cusped Bianchi
3-flow proxy; the no-eclipse three-disk physical flow with a separate
unit-roof calibrator; the positive Level-11 newform time change; the residual
and homology-cover geodesic candidates; and the nonarithmetic genus-two
geodesic control/magnetic precursor.  The 12 frozen geometric/physical
instances plus seven `q`-symbol calibrators remain **19 bookkeeping model
instances**, not 19 statistically independent samples.

## Required next action

The scholar should review the five linked `content_proof.pdf` files.  One
explicit content confirmation authorizes the reproducible final LaTeX builds,
final package verification, and the Stage-5 FULL completion checkpoint for all
five papers.  Until then, each `stage5_finalization/paper.pdf` remains absent.
