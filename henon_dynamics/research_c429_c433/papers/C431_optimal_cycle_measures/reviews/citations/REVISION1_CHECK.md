# C431 citation revision-1 check

Article: *Haar limits of optimal wild cycles*.
Checked 2026-09-09 UTC against the frozen revision-1 source and PDF.
Result: C431-CIT-1, C431-CIT-2, and C431-CIT-3 are closed on these bytes.
C431-CIT-4 remains **UNCHECKED**, not cleared.

## Bounded read and verification extent

This is a targeted follow-up to the immutable 266-line
[original citation report](REPORT.md), not a second full manuscript review.
The ARS citation-compliance role alone was used, retaining the specified
plain numbered alphabetical mathematics format and the prohibition on
editing author files. Its router, workflow, citation role and format
reference were read in full for this check. No other persona was activated.

The complete actual baseline-to-current unified diffs were read for the
only three changed source files: `sections/1_introduction.tex` (26 diff
lines), `sections/2_coefficients.tex` (12), and `references.bib` (45).
The 83 diff lines include headers/context. The full author improvement
log (153 lines), state JSON (73), and generated `main.bbl` (49) were
read. The log/state are declarations; closure below is based on actual
source, generated bibliography, extracted PDF text and link objects.

New PDF text extraction was inspected only at the affected background/
source-citation passage and bibliography, using the reader's selections
3 and 11–12. The corresponding existing revision-1 renders
`page-03.png`, `page-11.png`, and `page-12.png` were actually opened and
visually checked. There was no new full-source or whole-manuscript read.
Mechanical hashing and citation-key scanning covered all nine current
TeX/BibTeX files, without claiming a renewed semantic reading of them.

`pdfinfo -url` was used to inspect the PDF's actual URI annotations.
Fresh extraction of the complete PDF for identifier matching was
byte-identical to `revision1/main.txt`; this is a mechanical text-output
comparison, not a claim to have read all 647 extracted lines anew.
No compilation, render generation, mathematical program, preflight,
external API, new agent, or Git operation was performed.

No primary page needed revisiting: the changed wording and repeated
source citation are resolved by the primary passages already inspected
in the original audit. Online source availability was not freshly
retested. “URL destination checked” below means exact embedded target
bytes agree with the already identified source/DOI, not that a publisher
page previously inaccessible has become accessible.

## Finding-by-finding closure

| Finding | Actual revised evidence | Disposition |
| --- | --- | --- |
| C431-CIT-1: four journal DOIs absent from PDF | `references.bib:10`, `:21`, `:33`, `:45` add the correct DOI URLs to `note` while keeping the original DOI fields and all five version URLs. All four are in the generated BBL, extracted PDF, visible bibliography and URI annotations. Alphabetical labels [1]–[5] are unchanged. | CLOSED: four source identifiers now render and point to their exact intended DOI URLs. |
| C431-CIT-2: unqualified compact-system background | `sections/1_introduction.tex:111` now introduces the “finite-quotient inverse-limit” description for “minimal equicontinuous Cantor systems”; the Hurder–Lukina author-version citation remains at line 114. The next sentence still supplies the manuscript's own proof, including the finite alternative. Both sentences render correctly. | CLOSED: the attribution now matches the previously checked Cantor-action source scope. |
| C431-CIT-3: Baker lecture/version date ambiguity | `references.bib:53` retains the 2007 lecture-notes entry and explicitly distinguishes the 2007 AWS lectures from first publication in University Lecture Series 45 (2008), as recorded in the linked PDF. The same clarification appears in the BBL and visible [1]. No chapter DOI or PDF revision date was invented. | CLOSED: the two dates now have separate, accurate roles. |
| C431-CIT-4: inaccessible complete retraction/update screening | Improvement log and state explicitly retain UNCHECKED; no new status survey was run. | UNCHECKED: no “zero retractions” or complete article-update clearance is implied. |

The repeated citation after equation (2.2), at
`sections/2_coefficients.tex:18`, is actually `[4, Theorem C and the q=1
discussion]`; it does **not** claim to cite LRL §2.2. It reuses the
already checked LRL v3 source binding and renders beside the unchanged
source-owned minimal-ramification identity. The optional introductory
definitions are visible in the source diff but receive no mathematical
assessment in this citation-only check.

## Citation and identifier consistency

| Entry | Current citation locations | Count |
| --- | --- | ---: |
| [1] Baker | Introduction:111; compact-limit section:143 | 2 |
| [2] Hurder–Lukina | Introduction:114 | 1 |
| [3] Jacobs | Introduction:103 | 1 |
| [4] Lindahl–Rivera-Letelier | Introduction:32 and :84; coefficients section:18 | 3 |
| [5] Nordqvist–Rivera-Letelier | Introduction:108 | 1 |

There are 8 citation occurrences, 5 distinct keys and 5 generated
bibliography entries: 0 in-text orphans, 0 uncited entries and 0 duplicate
keys. All unchanged reference metadata/version bindings retain their
original audit disposition; no new reference was introduced.

Every URL below is present exactly in the BBL, in PDF text after removal
of layout whitespace, and among the PDF's URI destinations:

| Label | Exact URI destination(s) | Result |
| --- | --- | --- |
| [1] | `https://swc-math.github.io/aws/2007/BakerNotesMarch21.pdf` | MATCH |
| [2] | `https://doi.org/10.2969/jmsj/90779077`; `https://arxiv.org/abs/2205.06285v2` | BOTH MATCH |
| [3] | `https://doi.org/10.1016/j.jnt.2017.02.018`; `https://arxiv.org/pdf/1409.4808v2` | BOTH MATCH |
| [4] | `https://doi.org/10.1112/S0010437X15007575`; `https://arxiv.org/abs/1311.4478v3` | BOTH MATCH |
| [5] | `https://doi.org/10.1112/jlms.12325`; `https://arxiv.org/abs/1904.04494v3` | BOTH MATCH |

There are 12 URI annotations representing 9 unique destinations:
wrapping splits three links into repeated annotations with identical
targets. None includes the surrounding sentence's terminal period in
the URI. The inspected bibliography renders show complete, readable
links without clipping; ordinary line wrapping is not a citation defect.

## Preserved limits and version identity

All four journal entries retain the original report's retraction and
complete-update **UNCHECKED** status, including its publisher-access
limits (indexed rather than directly opened Jacobs publisher metadata;
unavailable substantive Project Euclid article/status text). The
original database-interface/CSV access failures are not retested or
silently cleared. Anonymous self-citation remains UNKNOWN and external
similarity screening UNCHECKED. The informative classic-source/currency
disposition is unchanged; no venue-age quota is imposed.

The original preflight's missing-dependency advisory is retained as
historical evidence only. No structural preflight was run on this new
PDF, so no structural PASS or certified page-anchor claim is made.
Reader selections and render filenames above identify inspection scope,
not a structural certificate. This check is neither manuscript pass 2,
a proof review, a publication verdict, nor a release/build certificate.

Only `REVISION1_CHECK.md` was written. Independently computed identities
are below; paired/current-snapshot files were compared byte for byte.
All nine current source files equal their `revision1/` counterparts;
only the three diff-listed files differ from `baseline/src/`. All ten
baseline source/record hashes still match the original audit's bindings.

| Input(s), relative to article directory | SHA256 |
| --- | --- |
| `main.tex` and `revision1/main.tex` | `665ecb1d163a5345d5871bb5c8155ca99eb0a30f5e367840d600d52c65ab1c81` |
| `references.bib` and revision-1 copy | `67164b9f8489c3d99cc3219ae13372659dd2aac1b618d2f572e1950375e00da5` |
| `sections/1_introduction.tex` and revision-1 copy | `40d85d94398f31bb838c5a9779f7533f22523b7de141763b4e73506b524e1308` |
| `sections/2_coefficients.tex` and revision-1 copy | `8359d9a98f5bd1da20fca07e2ab4c59074e9b36dcab7e29f04a8b99701468432` |
| `sections/3_displacements.tex` and revision-1 copy | `6f63fde2fc55ab4fda11d55e1952306cfc7dca0b9caed1781e3e5a1abae9aad4` |
| `sections/4_contacts.tex` and revision-1 copy | `c6203fdd3985c273cc6211f536887e9273a94be5e92cfe7e2d2464ccd0d03873` |
| `sections/5_compact_limit.tex` and revision-1 copy | `3eaf9f89737f7d62791a4ec83a95afccd470afcc77cf914dfdc781f58b8e938c` |
| `sections/6_adding_machine.tex` and revision-1 copy | `a665bb19ca294784768d01353c35b83f92db3be4def838bb67b7818a75be3c8b` |
| `sections/7_scope.tex` and revision-1 copy | `eeed8f29f17238f77f265cc43bf179af32abbe52184b1ff9d03ef5c8a537c174` |
| `main.bbl` and `revision1/main.bbl` (49 lines) | `f04a9a70697f9cf25d0d27bf626d1bd680bcc7c606915aa0a2d542753b3d532d` |
| `main.pdf`, `main_round1.pdf`, `revision1/main.pdf` (384227 bytes each) | `dba1f729d54b44b12cd800273041e3a514846613a4cdad0cd2454d9aa28a0915` |
| `baseline/main.pdf`, `main_round0_original.pdf` | `989f18747d96648d7ebbeaed4b8e1bba7002e3cb407a21748d60a4b64107a4e6` |
| `reviews/citations/REPORT.md` (266 lines; unchanged) | `289e6d4e48726877f6231b0c49f11ca2902d4eb1579c916f9ab3bfaed27723e4` |
| `PAPER_IMPROVEMENT_LOG.md` (153 lines) | `f8308863e66d1cfa05c112633ba365814961efb8d600133f53a9421949b79ce2` |
| `PAPER_IMPROVEMENT_STATE.json` (73 lines) | `2fe85e74ff1f94994c1656a846e6573ddc2586461ad3f2cd6d2cc6bde79a366c` |
| `revision1/main.txt` | `dd24807e31a05470e0ad35d1dd3f08b39694b1af5b5bbb6985c20478b59ab417` |
| `revision1/inspection/page-03.png` | `9f82968b61bc1ca20c015a8d49663b402ba6f0c0868c7942f4904d3966deb54d` |
| `revision1/inspection/page-11.png` | `e2d855e503d1c0750a9b5592d7026ad84356dc204d3730395013de0d60e857f5` |
| `revision1/inspection/page-12.png` | `afac245e42173209c6e5843b1a54b9124c45ac9bc88fe7c9d6a3a8cf779a111f` |

These inspected input hashes were rechecked unchanged before handoff.
This report is frozen for coordinator disposition; no further citation
source edit is required by CIT-1 through CIT-3 on this revision.
