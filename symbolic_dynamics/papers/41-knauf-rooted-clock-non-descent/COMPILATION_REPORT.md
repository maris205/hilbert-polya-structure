# Paper 41 compilation report

Status: `FINAL_WRITER_COMPILE_CLEAN`.

Title: **The Rooted Knauf Clock Does Not Descend to Cycles**.

This report records the final writer-only build. The immutable research
pointer remains SHA-256
`3f03a09fe318f96b7573268f6126946d20c2b5287e3bd50e9a21a20ec98616b6`.
No code, result, experiment, evaluation, Route provenance, paper manifest,
root README, Git, or mirror byte was changed by the writer.

## Deterministic build

Two independent empty out-of-tree directories were populated from the same
final source bytes and built with:

```text
SOURCE_DATE_EPOCH=1786924800
FORCE_SOURCE_DATE=1
TZ=UTC
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error main.tex
```

The two PDFs compare byte-for-byte equal.

- pdfTeX: `3.141592653-2.6-1.40.22` (TeX Live 2022/dev/Debian);
- BibTeX: `0.99d` (TeX Live 2022/dev/Debian);
- fixed epoch: `1786924800`;
- PDF SHA-256:
  `adfe4de4470ed744b71f26ec27233242acd430539ae3dfbb7ae26ccf1abe37ec`;
- byte size: `448353`;
- format: PDF 1.5, 13 A4 pages;
- metadata: title exact, author `Anonymous Authors`, no host path.

## Final log, citation, font, and text QA

The final logs from both builds have:

- 0 TeX/BibTeX errors;
- 0 package or LaTeX warnings;
- 0 undefined citations or references;
- 0 multiply defined labels;
- 0 overfull boxes;
- 0 underfull boxes.

The bibliography has 12 unique keys, all 12 are genuinely cited, and there
are no missing, uncited, or duplicate keys. The PDF reports 26 font rows;
all 26 are embedded and subset.

Extracted text has no `??`, `[?]`, `TODO`, `VERIFY`, unfilled
`{{...}}` token, old canonical-placeholder marker, absolute host path, or
temporary path. The sole rendered `PENDING_FIRST_ARTIFACT_COMMIT` token is
the required Stage-A sentinel for exactly the three fields
`source_commit`, `code_commit`, and `source_lock.code_commit`; it is
not an unresolved placeholder. There is no other or bare `PENDING` token,
and the same sentence records that `PAPER_MANIFEST.sha256` is absent.

## Page-by-page visual QA

All 13 final pages were rasterized and inspected.

| Pages | Content checked | Verdict |
|---|---|---|
| 1--4 | title, abstract, claim boundary, prior ownership, source definitions, Tables 1--2 | clean |
| 5 | Figure 1 and rooted-state theorem | clean |
| 6 | Figure 2 and scalar-phase theorem | clean |
| 7 | inventory determinant statement and proof | clean |
| 8 | Figure 3, ownership prose, Route opening | clean |
| 9 | Route table, canonical integration block, conclusion opening | clean |
| 10 | conclusion and all 12 bibliography entries | clean; no isolated entry |
| 11 | Appendix A recurrence, witness table, and exact proofs | clean |
| 12 | Appendix A completion, Appendix B domain and literature tables | clean |
| 13 | literature metadata, chronology, and lock boundary | clean |

No page has clipping, overlap, missing graphics, illegible labels, table
spill, footer collision, orphan heading, or isolated bibliography row. The
three figures are pure TikZ and appear on pages 5, 6, and 8.

## Writer scientific QA

The final reverse outline is:
source question and boundary; prior ownership and retrospective selector;
typed rooted object; exact non-descent theorems; state-inventory determinant;
strict Route/reproducibility record; limitations; exact proofs; analytic,
literature, and lock boundaries. Five formal statements have five proofs.
The claims--evidence matrix closes without importing object ownership from a
changed Farey, Gauss, Selberg, adelic, trace-clock, or eigenvalue-clock model.

The canonical block is unique and records only final CLEAN fields:
main/independent `24/24` and `25/25`, science SHA-256
`f9cbcde9a757896b976ad81a66f235d670029f727b6fda9b4e851846bac50bec`,
resolver `22/22`, zero theorem failures, Route `51/51` and `24/24`,
`1168/0` mutations, integrity `51/51`, first materialization/idempotence
`42 -> 0`, and the exact result-ledger anchors. The text retains
`results_unseen=false`, `blind=false`, and
`fully_prospective=false`; no prospective, novelty, discovery, or priority
credit is added.

## Final 19-source publication map

The map is C-sorted by relative path and excludes this report and the
generated PDF.

```text
df03263750f754aa10fb8cf2636deb4660db3d0989bad8f28b00897acf4dbaeb  NARRATIVE_REPORT.md
5d008ff8dd16e7293253f0d10665918f06f9b8942ec5fc9fd215c34a77319398  PAPER_PLAN.md
31fbcda72cac474b906be09547e999940733e250738efbcf07fd8d2691a143ae  README.md
3373e38a281eabcddfed6e0206f906f1bd8e823935404729cae3c72372bd8354  figures/clock_phase_non_descent.tex
5ff3316bc9454f1e6bd5c13bfd6772691f492158c60b510a3fbd10ff96821ae4  figures/inventory_ownership.tex
1ee7bf4abd2c534cdc99a1efe53c7cac0600413fdb9afc923d293bad0cbb3aa8  figures/rooted_state_non_descent.tex
876d2d41c0417ba5c2691a45fb644b9a06ae671c54f0139dea50476130b777e5  main.tex
b72ae1635ceadad9f3ed22ea1e8285dfa471045f0a752b8308d43165eea1ae78  math_commands.tex
52b4de2a3150e35c92f846e79e2b1e99be3aeb75a8b466b02181ae48b15a7ac0  references.bib
f86b09536ad14bd4eb50b94544fe2c8fa0b9e1340055d3cfb398a9e380da7ecf  sections/0_abstract.tex
e58e567d15a04f22a9b950e6d7cf76e96542bd346572ee2604ab8e959dd57b46  sections/1_introduction.tex
f5ce74064ef73bea9dd17f5f535a6ec3ccfb2b5f246f49a337a1729e32401458  sections/2_prior_scope.tex
3900140254e6776729072c14143c33237b0b137d956dd332247c0cb8fa4d9901  sections/3_source_types.tex
5f9b66f3935858c13b2f56e8d12106d648f95ad1fa14ad8f2662cccdde2ec290  sections/4_non_descent.tex
25c93c001cb34d2016c1c35873258c054bdec797684e44841c88e8de260e90dd  sections/5_inventory_determinant.tex
a42c15f1818363895350e5c5e70480d1b364e63f560ff551d645041df68629bb  sections/6_route_audit.tex
5bb2bf1bbd05ec99614941d7daad223a6954c12442f808072e29b1894d0d7f0d  sections/7_conclusion.tex
584f4e5e3fdc275b02fcb8f0744726156e26c4cfe5b3873896cd6a48b36b8394  sections/A_exact_proofs.tex
d160d32e3e5e3732bf8a38116062898c97d1d340e5691738f3135fbbefa28649  sections/B_boundaries_and_locks.tex
```

## Authority installation boundary

Only `main.pdf` and this `COMPILATION_REPORT.md` are installed from the
writer build. No `.aux`, `.bbl`, `.blg`, `.log`, `.out`, cache,
raster, or build-directory artifact is installed.
