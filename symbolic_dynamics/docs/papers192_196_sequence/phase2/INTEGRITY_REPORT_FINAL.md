# Final internal integrity report — P192–P196

Decision: `PASS_INTERNAL / OPEN FINDINGS 0 CRITICAL / 0 MAJOR / 0 MINOR /
HOLD_EXTERNAL`.

This report closes the Round-2 review-integrity surface. It does not certify
external ownership, novelty, priority, or freedom to operate.

## Canonical replay accounting

| evidence layer | frozen assertions/checks | accepted packages | replay condition |
|---|---:|---:|---|
| author controls | 15,387,752 | 5 | each canonical output reproduced byte for byte |
| hostile Review A | 9,347,475 | 5 | each process-separated canonical output reproduced byte for byte |
| hostile Review B | 31,782,429 | 5 | replay 1 and replay 2 are fresh-process, byte-identical, and equal the canonical |
| **grand total** | **56,517,656** | **15 controls / 10 review packages** | **PASS** |

The counters measure executed deterministic assertions, not proof strength.
The deductive proof packages remain the authority for all-parameter results.
P192's independent `n=9` stream is additional bounded evidence and is not
included in the grand total.

## Review-package integrity

All ten Review-A/Review-B package manifests verify from their own package
directories. They are non-self manifests with package-relative paths and full
coverage of every other regular payload: eight payloads in each Review-A
package and nine in each Review-B package. All ten `PINNED_INPUTS.sha256`
files verify from the workspace root, use root-relative paths, and contain no
parent traversal. Reviewer verifiers import neither author code nor the other
reviewer's implementation.

Each review package contains the required independent proof rederivation,
source/owner audit, exact delta, build/PDF QA, pinned-input manifest, verifier,
canonical transcript, and finding census. Each Review-B package additionally
contains an explicit replay log naming replay 1 and replay 2 and recording
byte identity.

## Round-2 PDF and cold-build integrity

| paper | pages | bytes | bibliography records | current/Round-2 PDF SHA-256 |
|---:|---:|---:|---:|---|
| P192 | 4 | 323,972 | 6 | `e06aac2579f0d90a15c1a7a2c8fa09ce57286f15818a10c2466cd06d210d6b57` |
| P193 | 5 | 390,196 | 4 | `b5b2f4e77bada6229a0716d9780a871f95b8e6ba75fa2c9e6794b5bf524ad0d9` |
| P194 | 5 | 372,121 | 6 | `682eeced97037b899f91dc2b93afaaf514b6dcbf8f95d1225ddb87f4cce6203b` |
| P195 | 3 | 318,096 | 4 | `d5dbac8ed78f1f3eccc3c7aeccda852e6f44f77a513091032120254119ff9c0a` |
| P196 | 3 | 345,811 | 5 | `bb0ee2d7e155bd515a250fe1c84146fcea3d2586b903fd5a71ecedb1a3d34948` |
| **total** | **20** | **1,750,196** | **25** | — |

For every paper, two source-only cold builds are byte-identical to each other
and to the current/Round-2 PDF. Final LaTeX/BibTeX logs contain no warning,
undefined citation/reference, overfull/underfull box, or fatal diagnostic.
The PDFs are nonempty A4 documents with blank identifying metadata and
embedded/subsetted/Unicode-mapped fonts. The visual corpus contains exactly
20 page rasters, one for every Round-2 page, and the accepted review QA found
no clipping, collision, broken formula, unintended blank page, or identifying
artifact.

P194's current PDF is intentionally different from its four-page Round-1
snapshot because the accepted Defant–Williams source subtraction reflowed the
manuscript to five pages. The repair changed no theorem statement, numbered
equation, proof, example, author verifier, or canonical output. P192, P193,
P195, and P196 retain byte-identical Round-1 and Round-2 PDFs.

## Historical versus open findings

| finding | original severity | accepted resolution | current state |
|---|---|---|---|
| P192-A1 | Major | added and zero-credited Campion Loth–Rattan's conditional Hurwitz/string-reordering neighbour | closed |
| P192-A2 | Minor | made `n>=2`, the `n>=3` sharp witness, and the `n=2` zero-tail/self-fibre case explicit | closed |
| P192-A3 | Minor | synchronized companion QA with the repaired source/PDF while preserving immutable Round 0 | closed |
| P192-A4 | Minor | corrected stale page/status descriptions in the two planning records | closed |
| P193-A1 | Major | cited and subtracted Schipper–Zhang's stochastic sequential mutual-best process | closed |
| P194-B1 | Major | cited and zero-credited Defant–Williams crystal pop-stack dynamics; Review B accepted and Review A passed nonregression | closed |
| P195-A1 | Major | added the P123/P159 historical subtraction and exact literal distinctions | closed |
| P195-A2 | Minor | restored the full `OWNER_AMBER / HOLD_EXTERNAL` release-state string | closed |

Historical total: `0 Critical / 4 Major / 4 Minor`, all closed. Current open
total: `0 Critical / 0 Major / 0 Minor`. No historical finding has been
dropped from the provenance ledger, and no resolved finding is misreported as
open.

## Claim-integrity firewalls

- P192's history-set law `#Hist=I=(n-1)^(n-2-|I|)`, its binomial depth law,
  and the general unique-deepest consequence remain conjectural. Checks
  through `n=8` plus the separate `n=9` stream do not promote them.
- P194's Defant–Williams repair is a source subtraction, not a theorem
  amendment or a novelty argument. Existing crystal pop-stack convergence
  and sharp orbit results receive zero contribution credit.
- P195 does not assert one attracting two-cycle per connected `H` component;
  the six-vertex multiple-mutual-edge witness remains a regression control.
- P196 uses `lambda^q-(lambda+1)^(q-1)` as the characteristic polynomial. The
  falsified q-bonacci alternative remains excluded.
- Exact enumeration, byte replay, clean compilation, and bounded source
  non-hits are integrity evidence only. None establishes a uniform proof or
  an external owner clearance.

## Final integrity disposition

The five Round-2 artifacts and ten hostile-review packages are internally
consistent with their canonical controls, accepted deltas, source
subtractions, and zero-open-finding censuses. The terminal internal review
decision is `PASS_INTERNAL`. The binding lifecycle remains
`OWNER_RED_AMBER / HOLD_EXTERNAL` for P192 and
`OWNER_AMBER / HOLD_EXTERNAL` for P193–P196.
