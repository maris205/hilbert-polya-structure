# Paper Configuration

- Candidate: `cat_equivariant_retention_tradeoff_v1`.
- Title: *An Equivariant-Zeta Audit of Cat-Map Centralizer Quotients*.
- Format: anonymous specialist theory-and-exact-audit note, 11 pt, single
  column; no venue, page-limit, acceptance, priority, or historical-first
  claim is made.
- Document date: 2026-08-15 pre-review freeze.
- Length: 19 pages including appendices, three frozen vector figures, three
  tables, and 14 references.
- Manuscript source: `paper/manuscript.tex`, SHA-256
  `88e81b0c91f57eb6b66c81d2c10af6b6ce4f611113383051a50f4e74e7fb67a5`.
- Shared notation: `paper/math_commands.tex`, SHA-256
  `1a057269cb071f5ba026430174b0d1b9c9651932ff2c8de286f4a8b6164e9a39`.
- Deterministic build script: `paper/build.sh`, SHA-256
  `3526ec2fad377a51620d18318dafdd43b59620ce1b9b95fb8c3e41c544fbd27a`.
- Bibliography: `paper/references.bib`, SHA-256
  `d88a3de08479c46174831a7d562405835800822850505f455831925ff06691d7`.
- Review PDF: `paper/paper_pre_review.pdf`, SHA-256
  `f0c27ce18c5f20b5192fb341a4960e2ccfbb7fd08727680912e5c1fb853b8e2e`;
  it is byte-identical to `paper/manuscript.pdf`.
- Build method: fixed `SOURCE_DATE_EPOCH`, `FORCE_SOURCE_DATE`, `TZ`, and
  `LC_ALL`, followed by `pdflatex -> bibtex -> pdflatex x3`. Two disposable
  isolated clean trees and the workspace produced byte-identical PDF, LaTeX
  log, BibTeX log, BBL, AUX, and outline artifacts.
- Terminal build QA: zero LaTeX/package, BibTeX, citation, reference,
  overfull-box, and underfull-box warnings; 65 labels and 40 referenced
  targets with no missing target; 14 cited keys against exactly 14 BibTeX
  entries with no missing or unused key.
- PDF QA: all 19 pages inspected; 39 fonts are embedded, subset, and
  Unicode-mapped; Type-3 fonts 0; raster image objects 0; anonymous title,
  author, subject, and keyword metadata verified.
- Figure integration: the three manuscript figure environments are exact
  copies of the independently approved `latex_includes.tex` blocks, in
  frozen order, and appear as Figures 1--3 on pages 4, 12, and 13.
- Reader-facing novelty policy: the note is described only as a deliberately
  modest, low-novelty boundary audit. No numeric novelty score appears in the
  manuscript or this pre-review release metadata.
- Review state: `READY_FOR_FRESH_INDEPENDENT_MANUSCRIPT_REVIEW`. This is an
  author-side production state, not an independent manuscript verdict.
  `paper_final.pdf` has not been created and finalization is not authorized.

## Scientific and theorem-scope boundary

For a finite abelian group acting on a disjoint union of orbit types, the note
derives source/coarse zetas, separates point-order and orbit-order Burnside
classes, applies orbifold maps only additively to exact-period classes,
computes the labelled `Z x C` stabilizer and action-kernel quotient, and
records effectivization, rigidification, quotient-stack, and static-inertia
boundaries. It then specializes these established constructions to the
frozen Paper-10 regular cat-map centralizer torsor.

The post-run scope audit is binding. The point-cardinality reduction at the
locked row `q=2` is `(1-t^3)^(-1)` and is the unique one of the 36 locked
row/type pairs with source support and unit exponent. The authorized negative
statement is only family-uniform: no single scalar-reduction type has both
properties over all nine locked rows. The collision `r_2=r_4=3` prevents the
exception from identifying the modulus. The A0 disposition therefore means
failure of a common intrinsic modulus/prime clock, not absence of every local
one-cycle factor.

No new equivariant, Burnside, orbifold, enhanced, group-action, groupoid, or
stacky zeta is defined. No universal no-go theorem, canonical comparison of
the varying coefficient categories, analytic continuation, transfer,
Fredholm, Hecke, quantum, prime--zero, Riemann-hypothesis, or Route-B claim is
made.

Scientific disposition:
`EQUIVARIANT_RETENTION_COMPRESSION_TRADEOFF_CERTIFIED /
A0_FAIL_MODULUS_GLOBAL_NON_SPECIFIC / ROUTE_B_NOT_OPENED`.

## Frozen authorities and publication assets

- Source lock v2:
  `331a1f9004f83c7979daf8eacddd6844072c6b5b7068293c1276985cf6aaa87b`.
- Frozen proof/formula package:
  `3d723fdb02c89f9b2f281da807bcd745c5991393d25e223f95d6673961c20948`;
  its overstrong scalar quantifier is superseded at publication layer.
- Raw result and strict result manifest:
  `bef8aa5d632ed11b1ca58a123bbfe967a5426e2049d862118a373e4c1dc005fe`
  and
  `a0b409061c34eff0d68fdc326fe4ec6ff9295895444b857ee161fd77e417292c`.
- Independent result and analyzer reviews:
  `c91737c8bf860bd559eebebe08420fc5d095800c47d132381f584e918e714a20`
  (`RESULT_PASS`) and
  `ba63afc8c88903f15ec6ac5d82f0cd65430710ca9c132b489a7cd4f70e7660a8`
  (`ANALYZER_PASS`).
- Independent theorem-scope audit:
  `f7b365c9e6c8933cf3cbcaf3c96692cbacdaabcc84400bdc629f1d482cb243e4`
  (`PASS_WITH_SCOPE_CORRECTION`).
- Paper plan, citation verification, figure manifest, and 25-path asset tree:
  `9a6ebb212e175775673e97bfc8b5eb18a2e8f760c756cdfc21583b0fb296124c`,
  `29681de3379801d1f376ecaa3b3cfc0d366964666852bff8b08faaf3cd67d3ca`,
  `e3a8d1d36ba8c4959b080a9661b242c40195ea08d27690fc8ee899b487cfd6dc`,
  and
  `95bb23519a427ef6a73a6a04b1aef6861aa4c5e4f6b844e7866bf9c43e52b28c`.
- Independent plan/figure review:
  `ebf1644dc03da4c1ccc03972b545688d595ed6da125de2ec831ffcf82e4e69cf`
  (`ASSET_PASS`).
- Walton publication-layer metadata are DOI-authoritative: *Journal of
  Number Theory* 192 (2018), 386--405. The frozen design-side volume/page
  typo remains unchanged as provenance and causes no scientific change.

