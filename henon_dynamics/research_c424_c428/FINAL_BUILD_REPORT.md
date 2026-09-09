# C424–C428: final deterministic builds and coordinator checks

2026-09-09 UTC. **FIVE_FINAL_BUILD_PAIRS_COMPLETE; 72_FINAL_PAGES_VIEWED**.
The five final papers are actual PDFs, not plans, source-only scaffolds
or five aliases of one result. The coordinator read all five complete
paper-local final build reports and accepts their document-quality
receipts. [Manuscript review closure](REVIEW_ADJUDICATION.md) is separate
from these builds; [evaluation closure](EVALUATION_ADJUDICATION.md)
does not infer target success from successful typesetting.

## Actual final pairs

Every row used two previously nonexistent directories and unchanged
reviewed inputs. Each actual latexmk invocation exited 0 and made
three pdfLaTeX and two BibTeX passes. The ten final invocations thus
made 30 engine and 20 bibliography passes, with no failed final build,
retry or third final directory. Earlier genuine initial-build failures
and layout changes remain preserved and are not included in this count.

| Paper / final PDF | Fresh directories relative to paper | Pages / bytes | Reproducibility inputs | Embedded font resources | Full final report |
| --- | --- | --- | ---: | ---: | --- |
| [C424](papers/C424_integer_valued_quadratic/main.pdf) | build/final_frozen_01, build/final_frozen_02 | 21 / 463423 | 29 | 22 | [Report](papers/C424_integer_valued_quadratic/FINAL_BUILD_REPORT.md) |
| [C425](papers/C425_fricke_return/main.pdf) | build_final_01, build_final_02 | 12 / 378223 | 13 | 23 | [Report](papers/C425_fricke_return/FINAL_BUILD_REPORT.md) |
| [C426](papers/C426_affine_good_models/main.pdf) | builds/final_01, builds/final_02 | 10 / 343725 | 10 | 20 | [Report](papers/C426_affine_good_models/FINAL_BUILD_REPORT.md) |
| [C427](papers/C427_vieta_semilinear/main.pdf) | builds/final_01, builds/final_02 | 13 / 346694 | 10 | 19 | [Report](papers/C427_vieta_semilinear/FINAL_BUILD_REPORT.md) |
| [C428](papers/C428_integer_period_spectrum/main.pdf) | builds/final_01, builds/final_02 | 16 / 389314 | 15 | 19 | [Report](papers/C428_integer_period_spectrum/FINAL_BUILD_REPORT.md) |

Total: 72 pages and 1,921,379 bytes across the five selected PDFs.
The 77 manifest entries are reproducibility inputs, not 77 TeX files:
C424 also pins its source evidence/programs and C425 its build script.
No mathematical program or table renderer was rerun during final builds.

All builds use SOURCE_DATE_EPOCH=1788912000, FORCE_SOURCE_DATE=1,
TZ=UTC and LC_ALL=C, with unchanged deterministic pdfTeX metadata
controls. Observed tool versions are latexmk 4.76, pdfTeX 1.40.22,
BibTeX 0.99d, TeX Live 2022/dev/Debian and Poppler 22.02.0.
Each local report gives the actual command, archive/snapshot policy,
logs, inputs and version details. This is reproducibility on the
observed toolchain, not an all-platform byte-equivalence guarantee.

## Independent coordinator integration check

A read-only standard-library aggregation, run from the repository root,
rehashes all 77 listed inputs and verifies each known final PDF digest
and length. It compares main.pdf, main_round1.pdf, main_round2.pdf
and the two actual final PDFs for every paper; all five sets match.
It runs pdfinfo/pdffonts on both final copies and checks the 20 converged
engine/BibTeX logs. The successful invocation exited 0 and reported
five PASS rows, 77 inputs, 72 pages and 1921379 final PDF bytes.

An initial diagnostic mistakenly read the encoding field as the font
embedding field (sixth instead of fifth token from the right), raising
an “unembedded” parser error before any paper PASS was emitted.
The raw font output shows embedding=yes; correcting the read-only
column index produced the complete successful check. This was a
diagnostic implementation error, not a missing font, PDF rebuild or
mathematical execution. No manuscript or evidence changed.

The coordinator also separately compared C427's ten members in both
final archives and its reviewed revision archive against active source.
Each other builder's complete report records equivalent archive or
snapshot comparisons, and the coordinator checked the active manifests
and matching final/reviewed PDF identities. No extra proof-certificate
rerun is inferred from integrity checks.

## Final visual and text evidence

The final builders actually read the complete extracted final texts:
1107, 614, 520, 645 and 788 lines respectively. They freshly rendered and
viewed all 21, 12, 10, 13 and 16 final pages. C424/C425 were checked by
as3h_source_spotcheck, C426/C428 by lyness_round5, and C427 by /root.
This is 72 final-page views of the chosen PDFs; byte-identical paired
copies do not imply 144 separately viewed images.

All final resources are embedded Type 1 fonts. The 20 final engine/BibTeX
logs contain no substantive warning, undefined citation/reference,
Overfull or Underfull diagnostic. Initial unconverged warnings remain
in full console logs; C424's transient 0.57625pt box and C425's earlier
failed initial build are not hidden. Every article includes its required
proof or explicit imported theorem dependency. No final layout defect
required another source change or build. No venue was selected and no
journal acceptance or venue-compliance certificate is claimed.

## Final identities

| Paper | Final PDF SHA256 | Final build-report SHA256 |
| --- | --- | --- |
| C424 | `3a1eadac84dd7fe9b730cde464bbc31a80469963aa984ac3a7117936e7bdf98b` | `c6d3912f9d07dc2d1d9adb00cca3fef10b3ff91334a3f3cf8113fdaec315357a` |
| C425 | `e7330f65920c40c566b01ee0d864d9f5a023c70010954e8af633c325f92c1dcb` | `a5c121ae9d4108a9ec7671bcb9d02d38cde0566b2eb370494d4dd15e564cb6bb` |
| C426 | `d0b4e14e8ed42002bf0ad454ee004c817403e9662ae92b25306a94adf4d582db` | `6fee551e5265a4da181689104cd46a3027b9e756bb36f5e51676fd5610149698` |
| C427 | `cae339b829dd8a4ca0c57accc75b3a9a3ced62173f49402e853e6d63c2d91bd1` | `8fd54f3ce12360e15ed4ad92cefbcc98c357f2a0c0d34f27b695351d520694a0` |
| C428 | `cf02bdd886584949847f2583904601bb2734010a5f9d9cafbcbe749ddb0553af` | `b085f757c78d3e6780411de7a284749da6e7bb32150592032c727a647ad3e4ef` |

All paper writers are stopped. Exact tree inventory, sealing, independent
membership verification and Git integration remain separate, actual
operations under [release policy](release/README.md); this report
does not preclaim their success. Stop at C428; no Route B or external upload.
