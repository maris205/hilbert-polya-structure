# Paper 9 independent release audit

**Audit date:** 2026-08-14 (Asia/Shanghai)  
**Audit role:** independent ARS integrity, formatting, and release reviewer  
**Verdict:** **PASS**

The exact candidate identified below is fit for repository release.  This is a
read-only audit of the locked manuscript, bibliography, figures, PDF, project
READMEs, controls, citation audit, evidence records, and retained source
material.  The only project file written by this audit is this report.

The PASS is not a journal-submission authorization.  The human author must
still confirm the provisional CRediT, competing-interest, funding,
acknowledgement, and final AI-disclosure wording before submission.  That
human-confirmation boundary is already stated in the release package and does
not block repository release.

## 1. Exact release lock

| Artifact | SHA-256 | Result |
|---|---|---|
| `paper/manuscript.tex` | `24dfcc168c140c77cfe413f9ca3b7fe7f59d9927bd2c4343159c5139b1ce31bb` | PASS |
| `paper/references.bib` | `0e4054e00ea1d09ce71d8f16fa2a051216d34f76aa437663012e726caf950f35` | PASS |
| `paper/figures/constant_class_convergence.tex` | `abece8b050760a3a85afb88f12875f5eed6a39a7ccbc51e92d4e9adade4f9cb7` | PASS |
| `paper/figures/topology_owner_split.tex` | `53b4c678011d90d9cc20cba5e6b37720c14b1f9462cf2e9e1a2e2e81f8b7f1dc` | PASS |
| `paper/paper.pdf` | `c55e4f45fe5f58841864e9af695c4664bdb1a77cff6e087fd2869d4ecd385e02` | PASS |
| `README.md` | `ddad7b1a7a474e7393dec66d60065e9f8ea7fd77af3c7c853b67225404328f2f` | PASS |
| `paper/README.md` | `5ac7a34024672d01ce2e8d9cac24036c0e7be9f2516b79da7603a5dfaf04eb34` | PASS |
| `results/packet_separation_manifest.json` | `52e7a4242f91fcff1b622c9455e90ad3380ae40e742e15bf5b922a3dd4415668` | PASS |
| `notes/citation_audit.md` | `bdba712848cb0872f9d8979858656384963930d6482c519cfa6485c9d5597f49` | PASS |

No locked byte changed during the audit.

## 2. Independent clean build

The release instructions were executed in a fresh temporary directory with
XeTeX 3.141592653-2.6-0.999993 (TeX Live 2022/dev/Debian) and BibTeX 0.99d:

```text
xelatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex
bibtex paper
xelatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex
xelatex -jobname=paper -interaction=nonstopmode -halt-on-error manuscript.tex
```

The clean build completed successfully and produced 21 A4 pages.  The final
pass contains:

- compilation errors: 0;
- undefined citations: 0;
- undefined references: 0;
- BibTeX warnings: 0;
- overfull boxes: 0;
- missing-character or missing-glyph diagnostics: 0; and
- underfull boxes: 6, all harmless paragraph-spacing notices.

The rebuilt PDF has SHA-256
`f8ebeaa18f14e1cdc0828702e010aecff386621845f39ec5e518acc248d230ff`.
Container bytes differ from the locked PDF because the rebuild carries a new
creation timestamp and regenerated PDF object/font subset identifiers.  This
does not conceal a layout change: the following two stronger content checks
pass.

- `pdftotext -layout` output is byte-identical between the release and rebuild,
  SHA-256
  `fb94d76d0b9be5649a836cd8d3f46dbdb8a5c6a7d0e69143d4eda9aee391755d`.
- All 21 pages rendered independently at 144 dpi to PPM are byte-identical
  between the release and rebuild; mismatching pages: 0.

Ghostscript processed the full release PDF through the `nullpage` device with
no error.  Every page has nonempty extractable text.

## 3. Full-page visual and structural inspection

All pages 1--21 were independently rasterized at 120 dpi and inspected, not
sampled.  The inspection covered the title and bilingual abstracts, contents,
the theorem ledger, all proofs and displayed equations, seven tables, both
native TikZ figures, the Paper-8 corrigendum, Route-A table, evidence hashes,
declarations, and all seven bibliography entries.

No clipping, collision, truncated formula, broken rule, misplaced caption,
malformed table, missing page number, unreadable CJK text, or figure overflow
was found.  The two TikZ figures remain sharp and within the text block.  The
large blank area after the final bibliography entry on page 21 is ordinary
end-of-document whitespace, not missing content.  `pdfimages -list` reports no
embedded raster images, consistent with the declared native-vector figure
package.

Static source checks also pass:

- balanced braces, with no negative intermediate balance;
- 43 `begin` and 43 `end` environments;
- duplicate labels: 0;
- unresolved static `ref`/`pageref`/`eqref` targets: 0;
- both figure inputs exist; and
- unresolved ARS markers, `anchor:none`, or `severity=HIGH-BLOCK` tokens: 0.

## 4. PDF metadata, fonts, and links

The locked PDF reports the expected title, author `Liang Wang`, subject, and
five keyword groups.  It is an unencrypted, unrotated, 21-page A4 PDF 1.5
produced by `xdvipdfmx`; it contains no JavaScript, form, attachment, metadata
stream, or custom metadata.  Filtered `pdfinfo` fields agree exactly between
the release and rebuild after excluding only creation time and file size.

All eight font records report `emb=yes`, `sub=yes`, and `uni=yes`.  The font
families are TeX Gyre Termes, TeX Gyre Termes Math, Noto Serif CJK,
TeX Gyre Heros, and TeX Gyre Cursor, matching the build declaration.

The PDF carries 141 link annotations:

- 19 unique internal page targets, all within pages 2--21 and none out of
  range;
- seven unique external source URLs; and
- one syntactically valid author `mailto:` link.

All seven external URLs returned HTTP 200 on the audit date.  The two relative
links in the project README resolve to `paper/README.md` and `paper/paper.pdf`;
missing README targets: 0.

## 5. Citation, source, and evidence closure

The source contains 20 citation commands and exactly seven unique citation
keys.  `references.bib` contains exactly those seven entries:

```text
ConnesConsani2016  ConnesConsani2026  Deninger2024  Deninger2026
Justel2018         LeBruyn2016        Morishita2026
```

Cited-but-absent keys, uncited bibliography entries, and duplicate BibTeX
keys are all zero.  The clean final build confirms the same closure.

The retained-source checksum ledger, SHA-256
`6413af8f2d0afec7158aec123f32a641776edcef0a9a9e747fd0ebc5c5f697e4`,
was independently run from repository root: all 14 entries pass.  These are
seven exact PDFs and their seven preflight sidecars, including three
byte-reused Paper-8 manifestations.  Each preflight sidecar has verdict PASS,
equal declared/enumerated/reader page counts, and an empty warning list.

The following evidence hashes also agree with the manuscript appendix and the
independent citation audit:

| Artifact | SHA-256 |
|---|---|
| `notes/proof_audit.md` | `c38c24296e5519862eb671dba1644c8005788ac15dffcac48dfdaa1ac3afdde8` |
| `notes/phase3_peer_review.md` | `447a6d575a27c87e3874591dfa3eae5f71ea1714819ada43263ffac44c53a678` |
| `notes/route_audit.md` | `f6e3c0ef065fb675d1f6408a411dba14de1581c5dfe4800dbddb532adaf8e730` |
| `notes/composition_blueprint.md` | `9258fa741ad8cb60d7b5de4f9220ab64a7aa44a5490ed88c185094c4418a41f5` |
| `notes/sources/paper9_source_manifest.md` | `8dd678dc33fa7396484c8c8d63a91943f6755da24eedefa0471860fa94e42906` |

All eight Stage-9 Route-A YAML hashes reproduce the appendix list in its stated
row order.  No Route-B record is introduced.

## 6. Deterministic controls

The control workflow was re-executed without writing to the locked result
directory.  This read-only equivalent of `experiments/reproduce.sh` ran the
unit tests, verified the existing result directory, and generated two fresh
result sets in independent temporary directories.

- unit tests: 20/20 PASS;
- existing-result `--verify-only`: PASS;
- CSV artifacts: 8;
- generated CSV data rows: 240;
- locked results versus temporary generation one: byte-identical;
- temporary generation one versus generation two: byte-identical;
- manifest hash in all three locations:
  `52e7a4242f91fcff1b622c9455e90ad3380ae40e742e15bf5b922a3dd4415668`;
  and
- Python cache/bytecode artifacts in code, experiments, and results: 0.

The controls remain finite regression witnesses and are not treated as proofs
of the infinite topological statements.

## 7. Public-release staging boundary

Two fresh temporary Git repositories were initialized and staged with
`git add .`.

1. The Paper-9 tree alone staged 46 files.  Its four local
   `notes/sources/*.pdf` files were ignored, and zero source PDFs were staged.
   The release `paper/paper.pdf` was staged as intended.
2. A support-tree test containing the Paper-8 retained sources plus the full
   Paper-9 tree placed 23 source PDFs on disk.  All 23 were ignored by their
   local `.gitignore` rules; staged `papers/*/notes/sources/*.pdf`: **0**.

The distributable source manifests, checksum ledgers, URLs, locators, and
preflight JSON sidecars remain staged.  The repository-release boundary is
therefore both auditable and conservative with respect to source-PDF
redistribution.

## 8. ARS release decision

| Gate | Result |
|---|---|
| Exact candidate lock | PASS |
| Independent clean build | PASS |
| Text and full-page raster equivalence | PASS |
| 21/21-page visual inspection | PASS |
| Fonts, metadata, PDF syntax, and links | PASS |
| Citation and source closure | PASS |
| Controls and double-temporary reproducibility | PASS |
| Public staging excludes retained source PDFs | PASS |
| Journal-facing human declarations | OPEN, explicitly non-blocking for repository release |

**Final decision: PASS.**  No release-blocking defect or unreported format
degradation was found.  The decision applies only to the exact hashes in
Section 1; any later change to a locked artifact requires a fresh release
audit.
