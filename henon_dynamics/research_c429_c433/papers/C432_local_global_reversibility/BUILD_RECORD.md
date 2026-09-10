# C432 first-draft build and author readback

Freeze checkpoint: 2026-09-09 20:49 UTC.
Status: **AUTHOR_BASELINE_READY_FOR_TWO_NONAUTHOR_MANUSCRIPT_REVIEWS**.
This is an actual first manuscript/PDF, not a completed-paper, formal
evaluation, release, external review, or publication claim.

## Deliverables and baseline

- Current article: [main.pdf](main.pdf), 8 pages, 341,782 bytes.
- Modular source: [main.tex](main.tex), seven included section files,
  one included exact local-place table, and [references.bib](references.bib).
- Source verification: [SOURCES.md](SOURCES.md).
- Claim/proof placement: [PAPER_PLAN.md](PAPER_PLAN.md).
- The actual pre-review source/PDF snapshot is in [baseline/](baseline/).
  Its source and PDF are byte-identical to the current author baseline.
- The first and only latexmk build attempt, its source inputs, all-pass
  console log, final engine/BibTeX logs, auxiliary files, extracted text,
  font/metadata receipts, and all eight page renderings remain in
  [build/attempt_01/](build/attempt_01/).

No second source version or improved review score is invented.
The ordinary TeX/BibTeX passes inside one successful latexmk invocation
are not separate manuscript revisions.

## Actual compilation

Working directory: this manuscript's build/attempt_01, populated with
copies of the author-read source, table, bibliography, plan, and source record.
The existing directory did not contain an earlier build. Nothing was deleted.

Command executed:

    set -o pipefail
    env SOURCE_DATE_EPOCH=1788912000 TZ=UTC LC_ALL=C latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error main.tex 2>&1 | tee compile.log

Result: exit status **0**. The log records three pdflatex passes and
two BibTeX passes, all within this one invocation. The first passes'
normal unresolved-citation/reference messages are preserved in compile.log;
they disappear from the final engine log. No failed LaTeX build or
post-build source repair occurred.

The environment was already installed:

- pdfTeX 3.141592653-2.6-1.40.22, TeX Live 2022/dev/Debian;
- LaTeX2e 2021-11-15 patch level 1;
- latexmk 4.76, 20 November 2021;
- BibTeX 0.99d;
- standard article class, 11pt, letter paper, one-inch geometry margins,
  Latin Modern fonts, amsmath/amsthm, mathtools, microtype, booktabs,
  array, and hyperref; amsplain bibliography style.

No package or font was installed. The pre-existing /etc/LatexMk contains
only its PDF-mode default; the explicit -pdf option selected pdflatex.
The source suppresses only the variable PDF trailer ID. The actual PDF
CreationDate and ModDate strings are both D:20260909000000Z, matching
the requested epoch. The local pdfinfo renderer displays the equivalent
08:00 CST; the raw PDF strings were inspected to distinguish that
presentation from the document's UTC metadata.

## Final engine and PDF checks

Actual checks used the completed first PDF and its final logs:

| Check | Result |
| --- | --- |
| Final main.log and main.blg scan for warnings, overfull/underfull boxes, undefined entries, missing characters, or TeX errors | No matches |
| PDF existence, size, and page count | 341,782 bytes; 8 pages; valid PDF 1.5 |
| Fonts | All 20 font entries are Type 1, embedded, subsetted, and Unicode-mapped |
| PDF text | All eight pages extracted and read; no unresolved-reference/citation or VERIFY/TODO/FIXME/XXX markers |
| Source inclusion | All seven section files and the sole table are included; no orphaned section or figure file |
| Bibliography | Four entries, all cited; generated main.bbl read and compared with the checked records |
| Anonymous metadata | Anonymous Authors; no fabricated identity, affiliation, funding, or venue |
| Current/build/baseline PDF comparison | Byte-identical |
| Current/baseline source comparison | main.tex and bibliography identical; recursive section/table comparisons identical |

Commands used included pdfinfo, pdffonts, pdftotext -layout,
rg scans of the final logs and extracted text, direct main.bbl readback,
cmp, and read-only directory diffs. The full compile log is not relabelled
warning-free: it retains the expected preliminary-pass warnings.
No warning-suppression setting was added.

## Actual page-by-page visual inspection

All eight page images were generated from the actual PDF using
pdftoppm -png -r 110 and individually opened at readable resolution.
This author inspection does not substitute for the later final-release
all-page check on whatever reviewed bytes are ultimately released.

| Page | Inspected content and disposition |
| --- | --- |
| 1 | Anonymous title, abstract, full original local-global question and Hénon definitions. Text, delimiters, and native-map conventions render legibly. |
| 2 | Both main theorems, nonzero scalar domain, all integer components, and classical source subtraction. No clipping or missing citations. |
| 3 | Full-group amalgam, coset tree, prefix axis, centralizer notation, and displacement proof. Long displayed definitions fit within the margins. |
| 4 | Intrinsic turn-label proof, primitive native translation argument, and centralizer theorem. Equations and the proof continuation are intact. |
| 5 | Complete diagonal-affine calculation, four scalar equations, reversing coset, and scalar-twist identities. All coefficient signs and exponents are visible. |
| 6 | Every-component original-field descent, construction over arbitrary characteristic-zero local fields, and the start of the Wang proof. No claim of an embedding of a completion into C is introduced. |
| 7 | Dyadic and real places, global non-root, exact place table, main counterexample proof, and the displayed nonlinear two-factor involutions. Table columns/caption fit and do not obscure the proof. |
| 8 | Explicit two-factor affine-ansatz failure versus its nonlinear reversor, limitations, AI/internal-review disclosure, and all four references/URLs. No text or link is clipped. |

No visual defect requiring a source change was identified.

## Author mathematical and source readback

Every typeset source section and the complete extracted PDF text were read.
The proof retains the admitted statement without new hypotheses:

1. The tree is built from the entire polynomial automorphism group.
   All turn-label representative changes, the signed native translation
   image, and the exclusion of a shorter centralizer translation are proved.
2. Both translations in every diagonal-affine axis fixer are retained until
   coefficient comparison removes them. The full centralizer is exactly
   mu_8 times the original native cyclic group, not only a subgroup.
3. All polynomial reversors form the computed coset. The twist retains
   all eight roots of t^8=a^2, including t^4=-a, and all j in Z.
4. Removing a field-defined native power treats every integer component
   and excludes coefficient-cancellation escape over the original number field.
5. The local construction is an algebraic identity over each original
   completion. Odd places, the unique dyadic place, both real places,
   and the absence of complex places are explicitly handled.
6. The two-factor control contains both globally defined nonlinear
   involutions and their reversal identity. A two-coordinate readback
   also gives the displayed necessary t^8=16 equation for the selected
   affine family, making the failure of that ansatz explicit.

The proof-writer checks shaped the assumption and component audit;
paper-plan/paper-write supplied the claim/proof structure and complete
modular article; paper-figure supplied only the exact LaTeX table;
paper-compile supplied actual build, log, text/font, and page checks.
The current anonymous mathematical/current-team contract overrides legacy
ML venue, minimum-length, numerical-figure, and external-model examples.

All four included bibliographic records are resolved, with actual access
boundaries in SOURCES.md. The failed BR DOI and published Wang PDF retrievals
do not become claimed full-text accesses. No direct reading of the original
1948/1950 Wang papers is asserted. A dedicated retraction/Crossmark audit
was not performed. The classical arithmetic, group structure, reversing
coset, and Cantat–Dujardin twist/centralizer mechanism are explicitly credited.

No mathematical program, external model/API upload, new agent, Git action,
shared-state change, old-proof edit, formal evaluation, manifest, seal,
or publication action was performed. Only this allocated manuscript
directory was written.

## Bound byte identities

These are integrity locators for this author handoff, not a release manifest
or a mathematical correctness certificate.

| Artifact | SHA256 |
| --- | --- |
| main.pdf, also baseline/main.pdf and build/attempt_01/main.pdf | d1f0c9bcab429d955b8700c2ce5bcc811f40f1f77f9bf7655ab8a4af0942a9aa |
| main.tex | e83ee44b45b9a4be1e98a150ec05514a3f47fcbc3f87342da90cfed55d3201c8 |
| references.bib | a4ce6daf2a069c51bece1a08c45ad8f241c8cfca74b20fede1d6e5cac8b564b7 |
| PAPER_PLAN.md | 30f3364801b0b7dbab2bd56c94eb45b7d93f62e45558452332011246618856ae |
| SOURCES.md | 04813dc535c7d6fc4d10140f7bd5f3a4483db05dbd240c2609422239128ef5d1 |
| build/attempt_01/compile.log | 3976bd51289c1347ee5a1791203169f4873b7fe831a14b80741a2ee0300605ab |
| build/attempt_01/main.log | c43eb822031592ad45f7bc3cdb675530354c76196b583426e7d774d41a90c3c8 |

The frozen research inputs were rehashed and remain unchanged:

| R5 input | SHA256 |
| --- | --- |
| C4 PROOF_PACKAGE.md | 99bf7efa1486df5a685347aac3bfa6d2c79ab45f241dc1b94c6a5a69b181143e |
| C4 REPORT.md | 2710692dc3c30c5a58a5d448c36ed900ba6aa93b0bc62bbaa8f5ffc958a019de |
| E5 full mathematical review | bb369ff50bac71a548207466c5b89e9fa93b2944d06a6fe767863e64792b81a2 |
| B1 source/substantiality review | 5cafc9a0f0e315e1959fb4db2a5ebf49a0379ca5fd31a5495010c8eb9dd5631b |

Root now owns assignment of the two actual nonauthor manuscript reviews.
Those reviews, any required revisions and affected readbacks, the formal
evaluation, two fresh deterministic final builds, release membership
verification, and integration remain pending. The author baseline is frozen
for that next gate; none of those later outcomes is inferred from this build.
