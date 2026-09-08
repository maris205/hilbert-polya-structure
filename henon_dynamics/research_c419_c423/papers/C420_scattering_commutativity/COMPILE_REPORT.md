# C420 baseline compile and author visual report

Date: 2026-09-08 UTC. Scope: the actual initial manuscript build and a
typesetting-only repair build. This is an author receipt, not an
independent mathematical manuscript review, acceptance decision or final
release certification.

## Actual build history

| Build | Actual latexmk exit | PDF | Final-log issues |
| --- | --- | --- | --- |
| `baseline` | 0 | 18 pages; 428825 bytes | One underfull table cell, badness 1831; two hyperref warnings about math-shift tokens in the Section 7 bookmark |
| `baseline_polished` | 0 | 18 pages; 428469 bytes | No matches for `Warning`, `Overfull`, `Underfull`, `undefined` or `Error` |

The initial completed build used normal latexmk convergence, including
BibTeX and repeated pdfLaTeX passes. The later build changed only the first
column of the boundary-level table to ragged-right and removed math mode
from the two numerals in the Section 7 title. No theorem, formula,
quantifier or citation changed in that repair. Initial transient
undefined citations before BibTeX are retained in raw output; the table
above reports the final LaTeX log after normal convergence.

An initial JavaScript quoting error occurred while constructing the build
script. It stopped before writing the script or running any compiler.
The corrected script was then created and syntax-checked. This is not a
third build, a mathematical test or a successful check.

All existing receipts are preserved under each build directory:

- `compile.stdout.log`: raw output of the actual latexmk invocation;
- `main.log`, `main.blg` and normal TeX auxiliaries: actual compiler files;
- `latexmk_exit_code.txt` and `environment.txt`;
- `source_inputs.sha256` and complete `source_snapshot/`;
- `main.pdf`, `pdf.sha256`, `pdfinfo.txt`, `pdffonts.txt`, `main.txt`.

The polished build began at 09:35:22 UTC. Selected environment:
Linux 5.15.0-78-generic x86_64; pdfTeX 1.40.22 (TeX Live
2022/dev/Debian); latexmk 4.76; BibTeX 0.99d.
`SOURCE_DATE_EPOCH=1788825600`, `FORCE_SOURCE_DATE=1`, `TZ=UTC` and
`LC_ALL=C` were fixed by the script. The TeX source suppresses volatile
PDF dates and trailer IDs. These measures prepare reproducible builds;
they do not themselves establish byte-for-byte reproducibility.

## Artifact identity and source binding

| Item | SHA256 |
| --- | --- |
| First PDF | `02155b14e6496bd9d9f64876ea2295d5e380cda9a5e0fc8f464d8ae8c8c391c6` |
| Current polished PDF | `08967fffb8542a60bdedc4142f2efd7149d26fb9057276bb6ab27fbcce5f10ff` |
| Current input manifest | `9d94846bd6fe52a6a9c30e5a7385bd369c3aa8a767e5cd85a5a404a7d1003994` |
| Current master `paper/main.tex` | `44f5150ce545c5a6b801e848c9f85393eb6f5122608c6d74206bdb8d0415050f` |

`sha256sum -c builds/baseline_polished/source_inputs.sha256` reported
OK for all 13 current TeX/Bib inputs. The review artifact is
`builds/baseline_polished/main.pdf`, not the earlier PDF.

## Final-log and PDF inspection

The final polished `main.log` was searched for warnings, box diagnostics,
undefined material and errors; there were no matches. The extracted text
was checked for unresolved-reference markers and verification placeholders;
none were found. The output is an unencrypted, 18-page US-letter PDF 1.5,
with no JavaScript. All 27 font rows in `pdffonts.txt` report embedded,
subset, Unicode-mapped Type 1 fonts; there are no Type 3 fonts.

The polished PDF was rendered by `pdftoppm` at scale-to 1500. All 18
retained images under `builds/baseline_polished/pages/` were actually opened
and inspected by the author, in batches 01–04, 05–08, 09–12, 13–16 and
17–18. This was a page-by-page visual check, not an inference from a
successful compiler exit.

| Pages | Inspected material | Observation |
| --- | --- | --- |
| 1–2 | Title, abstract, two main theorems, source-ownership table | Readable; theorem statements and table do not overlap |
| 3–5 | Fixed cusp transform, local incoming factors, paired blocks | No clipped formula or missing mathematical glyph |
| 5–8 | All-exponent principal basis, including both central parity cases | Display equations and indices remain within margins |
| 8–11 | Complete imprimitive scalar identity and outside-level determinant obstruction | Long products and aligned formulas remain readable |
| 11–14 | Tensor lemma, fixed phases, odd central obstruction and converse | No overflow; local phase table legible |
| 14–15 | Unit-group derivation of the explicit level conditions | Exponent table is readable and correctly placed |
| 15–16 | Exact levels 50 and 100 | Boundary table and explicit commutator readable |
| 17–18 | Scope, AI/preparation disclosure and seven-entry bibliography | No clipping or unresolved citation; last page contains the final Young entry |

The short last bibliography page is an optional later layout-polish item,
not a missing-proof issue or a violation of a page limit. No hard page
limit was imposed by the approved mathematical-article plan.

## Proof coverage and integrity boundary

The manuscript includes the full fixed-coordinate transform and
width-one normalization; the all-exponent principal basis proof in both
central cases; all missing Euler factors for an imprimitive character
square; nonreal-square necessity at arbitrary containing levels; tensor
noncancellation; the exact fixed-phase/odd-exponent obstruction; the
converse including regular removable parameters; the elementary character
and level equivalence; and the exact level-50/100 controls.

Every central new proof is typeset in the article. Local Markdown
derivations are provenance, not a substitute for a manuscript proof.
The classical Eisenstein reconstruction and functional equations and
Dirichlet identities are explicitly cited imported inputs.

The author readback found no outstanding mathematical transcription gap.
That assessment is provisional until the separately routed full-text
reviews. Seven cited bibliography records and the exact limits of new
primary-source access are recorded in `BIBLIOGRAPHY_VERIFICATION.md`.
No old mathematical probe was rerun, and no mathematical PASS result was
created by this typesetting work.

## Outstanding gates

Two actual independent full-manuscript review/fix/recompile rounds remain
pending. Final same-input builds in two fresh directories have not been
run: the two builds above deliberately have different source inputs.
Final bytewise reproducibility, source freeze, release documentation,
whole-batch checks and formal evaluation belong to the later coordinator
workflow. No Git mutation, external manuscript upload or paid review API
call was performed by this author subtask.
