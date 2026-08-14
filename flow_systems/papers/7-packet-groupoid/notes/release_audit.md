# Paper 7 independent release audit

Audit date: **2026-08-14 (Asia/Shanghai)**  
Audit mode: **independent, read-only release and visual audit**  
Decision: **PASS**  
Blocking findings: **0**

## 1. Scope and write boundary

This audit examined the final Paper-7 release bytes, rebuilt the manuscript in
an isolated `mktemp` directory, reran the deterministic package from a complete
temporary copy, and inspected the released PDF.  It did not edit any existing
Paper-7 file.  The only workspace output of the audit is this report.

The SHA-256 inventory of the 73 Paper-7 files present at the final release
snapshot was captured before the audit and remained unchanged through the
isolated build, control, text, font, and visual checks.  Its audit-sidecar
digest was
`576ada315e0ae21a1277273f361112157cc1c4066f0ede3d243d3ad6835490bb`.
During report write, separate orchestrator tasks appended the citation-audit
closure and created a Chinese stage summary.  Those concurrent note changes
are not outputs of this auditor and do not alter any protected release object
in Section 2; the protected locks were rechecked after that activity.

## 2. Final byte lock

| Release object | Observed SHA-256 | Result |
|---|---|---|
| `paper/manuscript.tex` | `5fd2f30d072b5c629a67c2be95b8fcc95a917e694f7e6be13a45f347f0e0c384` | PASS |
| `paper/references.bib` | `68d96e5857dafd0594acd5d465637487c9281e06a178faed3e2998c231d3b48f` | PASS |
| `paper/paper.pdf` | `4f0f9fbebf705e6b73c34fb66b01d4dda9d6ac37b7409f587bbefd8fecdcbd8d` | PASS |
| `paper/fig_owner_map.tex` | `684bb3e83de9f12c92651580797d72c0b528051549b80f8239dc083dfcde03f3` | PASS |
| `paper/fig_ef_collapse.tex` | `fca764ba3ee291961c7b9c013544ea5751cc03f6ce8d4168fbd4ddfff9e86959` | PASS |
| `notes/sources/paper7_source_manifest.md` | `d99a0e9c9ddcfb4ab5ca3f7a57284dd1a405567664ce3dcc1d7abd1602fd4d0e` | PASS |
| `results/packet_trace_manifest.json` | `fe12ec4c6b0a950d35d267c830119945652acafb9a5ddae2aa6b86db92943b26` | PASS |
| `notes/route_audit.md` | `79261a2e6e70350a22d1fc81336c24c7c86fc1baafaa5ed8acbbebea404a6091` | PASS |
| `paper/README.md` | `523e3d5bccf36054783e793eb2c6b35ea1dcc0b00d6e9d468cb0fee3ae6a15d0` | PASS |

The paper README names the current TeX, BibTeX, figures, PDF, canonical source
manifest, control manifest, and Route-audit locks.  Its release hashes agree
with the bytes observed independently here.

## 3. Clean XeLaTeX/BibTeX build

The four manuscript inputs were copied to a new temporary directory.  The
following sequence was then executed without using any workspace build
artifact:

```text
xelatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex
bibtex paper
xelatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex
xelatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex
xelatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex
```

Final-log results:

| Gate | Observed result |
|---|---|
| XeLaTeX exit status | PASS |
| BibTeX exit status | PASS |
| Undefined citations | 0 |
| Undefined references | 0 |
| Overfull boxes | 0 |
| Missing-character or missing-glyph diagnostics | 0 |
| LaTeX/package warnings in the final pass | 0 |
| BibTeX warnings or missing entries | 0 |
| Nonfatal underfull boxes | 35 |

The underfull diagnostics are concentrated in narrow audit-table cells and
long typed identifiers.  They do not cross a release gate; the affected pages
were included in the visual inspection below.

The clean build produced a 22-page A4 PDF with the same title and author
metadata as the release.  Its SHA-256 was
`14024f5954fe18f698e2b342767716d188b3ede35628a86d1b0b2f5086efa9bd`,
which differs from the locked release PDF.  No bit-reproducible PDF claim is
made.  The differing fresh-build hash is recorded rather than silently
equated with the release.  Content equivalence was checked more strongly at
the rendered and extracted-text levels: all 22 pages were pixel-identical at
100 dpi, and `pdftotext -layout` outputs were byte-identical.

## 4. Released PDF integrity and metadata

`pdfinfo` on the locked release reported:

```text
Title:      Prime Packets without a Packet Trace
Author:     Liang Wang
Pages:      22
Page size:  595.28 x 841.89 pts (A4)
File size:  224879 bytes
PDF version: 1.5
```

Additional checks:

- `pdftotext -layout` completed and yielded the full 22-page text;
- `pdffonts` enumerated 22 fonts, all with embedding status `yes`;
- Ghostscript parsed every page with the `nullpage` device without error;
- `pdfimages -list` found no raster image objects, consistent with the two
  figures being native TikZ/vector content; and
- the clean-build and release text extractions were identical.

## 5. Citation and canonical-source integrity

The clean `.aux` contained 15 unique citation keys.  The BibTeX database
contained 15 entries, the generated `.bbl` contained 15 `bibitem` records,
and the symmetric difference between cited keys and bibliography keys was
empty.

The canonical Paper-7 source manifest has 15 data rows.  For every row, this
audit independently checked:

- the exact PDF filename and PDF SHA-256;
- the same-stem preflight-sidecar SHA-256;
- preflight verdict `PASS`;
- equality of declared, enumerated, reader, and manifest page counts; and
- an empty sidecar warning array.

All 15 rows passed.  The manifest's redistribution boundary remains in
force: a read-integrity pass and lawful retrieval endpoint do not themselves
grant permission to redistribute a retained source PDF.

The final bibliography visibly includes the corrected Bornemann issue as
*Mathematics of Computation* **79(270)**, 871--915, and the current DOI and
manifestation metadata required by the preceding citation audit.

## 6. Author, bilingual abstract, declarations, and scope language

The source, rendered title page, and PDF metadata consistently identify:

```text
Liang Wang
School of Artificial Intelligence and Automation
Huazhong University of Science and Technology, Wuhan 430074, P.R. China
wangliang.f@gmail.com
```

The Chinese abstract and keywords use simplified-Chinese forms.  The English
and Chinese abstracts state the same object boundary, trace-domain split,
branch-fixed Euler product domain, and restricted-intertwiner conclusion.

The final declarations include all of the following:

- source and citation integrity;
- data and code availability;
- ethics;
- named-author CRediT contributions;
- competing interests;
- funding;
- AI-use disclosure; and
- acknowledgments.

No blind-author placeholder, TODO/TBD marker, undefined-reference marker, or
adjacent mechanical duplicate was found.  The two previously flagged prose
fragments each occur exactly once.  No positive attribution of a
flow-generated or packet-groupoid algebra was found, and the manuscript does
not make a spectral or critical-line promotion.

## 7. Route table and same-object boundary

The final Route-A v0.2.0 table agrees with the independent Route audit:

| Candidate | Final tuple | Overall | Route B |
|---|---|---|---|
| Published source | `(A0_ANALYTIC_ARITHMETIC_ORIGIN, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `EXPLORATORY` | `false` |
| Mass-family proxy | `(A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)` | `EXPLORATORY` | `false` |
| Return record | `(A0_WEAK_ARITHMETIC_RELATION, A1_PASS_ANALYTIC, A2_FAIL, A3_FAIL, A4_FAIL)` | `EXPLORATORY` | `false` |
| Zero-mode record | `(A0_WEAK_ARITHMETIC_RELATION, A1_FAIL, A2_ANALYTIC_DETERMINANT, A3_FAIL, A4_FAIL)` | `EXPLORATORY` | `false` |

The table and surrounding prose explicitly prohibit coordinatewise splicing.
Source arithmetic-origin credit, the return-record analytic ledger, and the
zero-mode analytic determinant remain attached to different typed owners.

## 8. Deterministic controls

The complete Paper-7 directory was copied to a second temporary tree before
running `./experiments/reproduce.sh`.  Thus regeneration did not overwrite
the checked-in results.  The receipt was:

```text
21/21 unit tests: PASS
manifest and implementation verification: PASS
generated artifacts: 9 CSV files
generated data rows: 407
max_prime: 5000 (669 primes)
two fresh regenerations: byte-for-byte identical
manifest SHA-256:
fe12ec4c6b0a950d35d267c830119945652acafb9a5ddae2aa6b86db92943b26
```

These are finite implementation and convention witnesses.  The controls are
not treated as proofs of the infinite analytic theorems, source transport,
trace provenance, determinant provenance, or a Route verdict.

## 9. Visual audit

Representative release pages were rasterized and inspected at 150 dpi:

| Page | Inspected content | Result |
|---:|---|---|
| 1 | title, Liang Wang/HUST metadata, English abstract, start of simplified-Chinese abstract | PASS |
| 2 | remainder of simplified-Chinese abstract, Chinese keywords, contents | PASS |
| 4 | native owner diagram and source/proxy separation | PASS |
| 16 | native `E_f` collapse/non-surjectivity/no-bridge diagram and P7-9 boundary | PASS |
| 17 | T0--T7 table and four-row Route table | PASS |
| 21 | declarations and first bibliography page, including Bornemann 79(270) | PASS |
| 22 | remaining bibliography and versioned arXiv locators | PASS |

No overlap, clipping, missing glyph, broken rule, unreadable identifier, or
figure/caption collision was observed.  As an additional mechanical visual
check, every clean-build page and its released counterpart was rasterized at
100 dpi; all 22 image pairs were byte-identical.

## 10. Decision

**PASS.**  The locked TeX, BibTeX, PDF, README, canonical 15-source manifest,
Route audit, and deterministic-control manifest are mutually consistent.
The manuscript clean-builds, the released PDF is textually and visually
equivalent to the clean build, all required declarations and ownership
boundaries are present, and no blocking release diagnostic remains.

The 35 underfull-box messages and the absence of a bit-reproducible PDF claim
are disclosed above as nonblocking facts; neither changes the release
decision.
