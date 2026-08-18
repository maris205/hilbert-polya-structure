# Compilation report

## Outcome

The release candidate compiles successfully to a 16-page A4 PDF.  Two
independent clean builds from separate copied source trees are byte-identical.
The final artifact is `main.pdf`, with SHA-256
`3ee4b7662f9d5f8fdd6a410461c7c8094cb5c2782fbbb486603f56b9841cb66d`.
`main_round2.pdf` is an exact byte copy of that artifact.  Earlier snapshots
`main_round0_original.pdf` and `main_round1.pdf` preserve the improvement
history.

## Source map

- `main.tex`, `abstract.tex`, and `math_commands.tex` define the document.
- `sections/1_introduction.tex` through `sections/7_scope_conclusion.tex`
  contain the theorem-first narrative; Section 6 is deliberately included as
  Appendix B rather than in the anonymous main body.
- `appendices/A_proof_details.tex` contains expanded proofs.
- `appendices/B_types_provenance.tex` contains the detachable type,
  provenance, Route, and chronology record as Appendix C.
- `figures/*.tex` contains three pure TikZ figures.  No raster figure is used.
- `references.bib` contains the six cited records.

## Deterministic build recipe

Both builds used fresh directories and the same environment:

```text
TZ=UTC
SOURCE_DATE_EPOCH=1700000000
FORCE_SOURCE_DATE=1
```

The direct toolchain was used because `latexmk` was unavailable:

```text
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

Build A and Build B each produced:

- PDF SHA-256:
  `3ee4b7662f9d5f8fdd6a410461c7c8094cb5c2782fbbb486603f56b9841cb66d`;
- final log SHA-256:
  `af637b72c538b885cfeedefb7449051183f1d28392c94bd159505fc4473e48c1`;
- BBL SHA-256:
  `6e93d309e313842a071d965af99c48de5431534a5f72d634d09a3ec31e0a52de`.

The final logs are preserved as `evidence/FINAL_BUILD_A.log` and
`evidence/FINAL_BUILD_B.log`; the bibliography product is
`evidence/FINAL_BUILD.bbl`.  Every pass wrote zero bytes to stderr.  The final
logs contain no TeX error, warning, undefined citation/reference, overfull box,
or underfull box diagnostic.

## Bibliography and document structure

The six cited keys equal the six generated bibliography items exactly:
`ban2019pattern`, `ban2023boundary`, `ban2025affine`, `fan2012level`,
`kenyon2012hausdorff`, and `madritsch2012summatory`.  The main theorem narrative
ends on page 9; proof details begin on page 9, exact computational replay begins
on page 13, types/provenance/reproducibility begins on page 14, and references
appear on page 16.  The replay table is anchored after its appendix heading.

The Ban--Hu--Lai bibliography title protects the math token with double
grouping in `references.bib`.  The generated BBL contains
`{{\(\mathbb{N}^d\)}}`, default/layout/raw text extraction retains uppercase
`N`, and original-resolution inspection of page 16 confirms a readable
blackboard-bold $\mathbb N^d$.  The exact check is recorded in
`evidence/BHL_TITLE_RENDER_QA.txt`.

## Font, text, bounding-box, and visual QA

`pdffonts` reports 25 font rows; all 25 are embedded, subset, and supplied with
Unicode maps.  `pdfimages -list` reports no raster images.  Default, layout, and
raw text extractions were checked independently, and the bounding-box XML was
validated with `xmllint`.  All four representations contain zero illegal
C0/DEL characters under the audit rule (page-separator form feeds are allowed),
zero unresolved cross-reference markers, and zero forbidden host/build-path
leaks.  Their counts and SHA-256 values are recorded in
`evidence/FINAL_QA_SUMMARY.txt`.

All 16 pages were visually inspected, with individual checks of the three
figures and the page-13 canonical table at original rasterization resolution.
No clipping, collision, unreadable label, blank page, or float-order defect
remains.  The final contact sheet has SHA-256
`0a38b339f856e6972e97bc98d1c01fb776f153d9d9178211ecb2a06177ee53ae`.

## Protected-input replay

The frozen 62-file authority snapshot has SHA-256
`a364048f5be1f9b88dedae5cde2f92d69295e4f403d92da310bdda301479539a`.
The final replay compared every recorded path across type, mode, uid, gid,
size, mtime, inode, link count, and file SHA-256: 62/62 regular files matched,
there were no symbolic links and no field differences.  The writer performed
no authority write and no Git operation.  The exact replay record is
`evidence/PROTECTED62_FINAL_REPLAY.txt`.

## Release gate

The LaTeX/PDF release remains byte-identical to the independently audited
writer candidate.  Publication-mode tooling was added afterward without a
rebuild: `main.pdf` is still
`3ee4b7662f9d5f8fdd6a410461c7c8094cb5c2782fbbb486603f56b9841cb66d`.

The exact publication protocol, two-state auditor, bounded installation
transaction, and physical smoke evidence live under
`evidence/publication_gate/`.  They make the legacy frozen auditor's expected
post-overlay `STATIC_TREE_MISMATCH` explicit instead of weakening that frozen
contract.  All publication audits and transactions require an externally
supplied SHA-256 of the raw publication-seal bytes before parsing the seal or
writer manifest.  The installed tooling is locally complete but externally
seal-anchored; after commit, the persistent anchor is the selected Git
blob/commit plus the self-excluding `PAPER_MANIFEST.sha256`.

This candidate is not a publication install and remains
`HOLD_FOR_INDEPENDENT_PUBLICATION_AUDIT` until an independent auditor accepts
the added publication layer.  The exact experimental block, Route record,
protected-input mapping, and theorem statements remain integration-sensitive.
