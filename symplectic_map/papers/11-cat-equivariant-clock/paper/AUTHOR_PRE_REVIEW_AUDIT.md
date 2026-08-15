# Author Pre-Review Audit

Date: 2026-08-15 UTC  
Candidate: `cat_equivariant_retention_tradeoff_v1`  
State: `READY_FOR_FRESH_INDEPENDENT_MANUSCRIPT_REVIEW`

This record is an author-side production audit. It is not an independent
manuscript review, an acceptance decision, or authorization to finalize the
paper. No `paper_final.pdf` exists.

## Frozen package

| Artifact | SHA-256 |
|---|---|
| `paper/manuscript.tex` | `88e81b0c91f57eb6b66c81d2c10af6b6ce4f611113383051a50f4e74e7fb67a5` |
| `paper/math_commands.tex` | `1a057269cb071f5ba026430174b0d1b9c9651932ff2c8de286f4a8b6164e9a39` |
| `paper/build.sh` | `3526ec2fad377a51620d18318dafdd43b59620ce1b9b95fb8c3e41c544fbd27a` |
| `paper/references.bib` | `d88a3de08479c46174831a7d562405835800822850505f455831925ff06691d7` |
| `paper/manuscript.pdf` | `f0c27ce18c5f20b5192fb341a4960e2ccfbb7fd08727680912e5c1fb853b8e2e` |
| `paper/paper_pre_review.pdf` | `f0c27ce18c5f20b5192fb341a4960e2ccfbb7fd08727680912e5c1fb853b8e2e` |

The two PDF paths are byte-identical. The document has 19 pages, with the
three frozen vector figures appearing as Figures 1--3 on pages 4, 12, and 13.

## Bound authorities and gates

- Source lock v2:
  `331a1f9004f83c7979daf8eacddd6844072c6b5b7068293c1276985cf6aaa87b`.
- Independent source rereview:
  `2f75d6934e3d61bdc941ee6689102a1cb08a959270a7cd87965579f1ec5cc622`,
  verdict `SOURCE_LOCK_PASS`.
- Frozen proof/formula package:
  `3d723fdb02c89f9b2f281da807bcd745c5991393d25e223f95d6673961c20948`.
- Claims/evidence matrix:
  `0ea191ebb1f6f0f915db096a68606099d4a315d80d333adadd3e396b11885490`.
- Raw result and strict result manifest:
  `bef8aa5d632ed11b1ca58a123bbfe967a5426e2049d862118a373e4c1dc005fe`
  and
  `a0b409061c34eff0d68fdc326fe4ec6ff9295895444b857ee161fd77e417292c`.
- Independent result review:
  `c91737c8bf860bd559eebebe08420fc5d095800c47d132381f584e918e714a20`,
  verdict `RESULT_PASS`.
- Independent analyzer review:
  `ba63afc8c88903f15ec6ac5d82f0cd65430710ca9c132b489a7cd4f70e7660a8`,
  verdict `ANALYZER_PASS`.
- Independent theorem-scope audit:
  `f7b365c9e6c8933cf3cbcaf3c96692cbacdaabcc84400bdc629f1d482cb243e4`,
  verdict `PASS_WITH_SCOPE_CORRECTION`.
- Independent plan/figure review:
  `ebf1644dc03da4c1ccc03972b545688d595ed6da125de2ec831ffcf82e4e69cf`,
  verdict `ASSET_PASS`.
- Frozen figure manifest and asset tree:
  `e3a8d1d36ba8c4959b080a9661b242c40195ea08d27690fc8ee899b487cfd6dc`
  and
  `95bb23519a427ef6a73a6a04b1aef6861aa4c5e4f6b844e7866bf9c43e52b28c`.

No source, candidate code, registered claim, raw result, analyzer result, or
independent-review artifact was edited during manuscript production.

## Theorem-scope correction

The publication layer explicitly supersedes the overstrong scalar quantifier
in the frozen prose while preserving all frozen formulas and exact results.
The following checks pass:

- the locked `q=2` row is stated as `(n,r,m)=(3,3,1)`;
- its point-cardinality factor is stated as `(1-t^3)^(-1)`;
- it is identified as the unique locked source-support/unit-exponent pair;
- the negative statement is only that no one scalar-reduction type works
  uniformly across all nine locked rows;
- `r_2=r_4=3` is used to show that the exception is not modulus-specific;
- the A0 conclusion concerns absence of a common intrinsic modulus/prime
  clock, not absence of every local one-cycle factor.

The correction is present in the abstract, opening scope statement, corrected
tradeoff proposition, C21 discussion, exact ledger, all relevant frozen figure
captions, K011 family-level control, A0 disposition, and conclusion. A scan for
the forbidden stronger per-row statement returned zero hits.

## Scientific coverage and boundaries

The manuscript contains the planned general finite abelian `C`-set
translation theorem and proof; source and coarse zetas; point-order versus
orbit-order Burnside sequences; additive-only orbifold reductions with an
explicit nonmultiplicativity witness; the labelled `Z x C` stabilizer and
recovery modulo the action kernel; quotient-stack, inertia, effectivity, and
rigidification boundaries; the regular Paper-10 centralizer-torsor
specialization; the separately typed effective `C6` structural control; the
exact nine-row audit; and dual-tree provenance.

The prior-art and nonclaim boundaries are explicit. In particular, the paper
does not define a new zeta construction, claim priority, assert a universal
no-go theorem, compare varying coefficient categories canonically, or open
Route B. It uses no reader-facing numeric novelty score.

## Exact data and figure integration

- All 9 frozen arithmetic triples match the strict result ledger.
- All 36 scalar support/exponent cells match the frozen contract.
- The sole positive locked cell is `q=2` point-cardinality.
- The two independent execution/analyzer trees are bound by SHA-256.
- The three figure environments are exact copies of the frozen
  `paper/figures/latex_includes.tex` blocks, in the approved order.
- The integrated labels are `fig:retention-hierarchy`,
  `fig:nine-row-retention`, and `fig:effectivity-counterexamples`.
- Original-resolution asset inspection and integrated 19-page inspection both
  pass; no clipping, collision, missing glyph, or illegible table was found.

## Deterministic build and document QA

The build fixes `SOURCE_DATE_EPOCH`, `FORCE_SOURCE_DATE`, `TZ`, and `LC_ALL`,
then runs `pdflatex`, `bibtex`, and three final `pdflatex` passes. The workspace
and two isolated clean build trees produced byte-identical PDF, log, BLG, BBL,
AUX, and outline files.

| Build artifact | SHA-256 |
|---|---|
| `manuscript.log` | `89adf923399cb2257d58470c8e2e08514205d0b8389833fa2e8e6c99799a2b1c` |
| `manuscript.blg` | `13d7d6e141ace109be09bce9bee17212ac6ecccac082a14ca8ae2d71200b3ef5` |
| `manuscript.bbl` | `617845025a84100f82a10e7c4e5d8068e7493e8f3779f37c32da555b2ace56ca` |
| `manuscript.aux` | `d7b528a949b8b97707d6af793d9c370929b5c731e36bd579b9a714f8a5b807a6` |
| `manuscript.out` | `cd36533f9b25495005a0d2c92a38093d909fe5c9c0d5a4b23d2b353e55a75ec6` |

Terminal QA returned zero LaTeX/package, BibTeX, citation, reference,
overfull-box, or underfull-box warnings. All 65 labels and 40 referenced
targets close, and all 14 cited keys match the 14-entry bibliography with no
unused entry. The PDF has 39 embedded, subset, Unicode-mapped fonts, no Type-3
font, and no raster image object. Title and anonymous-author metadata are
correct.

The Walton record uses DOI-authoritative publication metadata: *Journal of
Number Theory* 192 (2018), 386--405, DOI
`10.1016/j.jnt.2018.03.023`. The frozen design-side typo was not modified; the
paper discloses this publication-layer correction and makes no scientific
change from it.

## Originality screen and metadata closure

The local heuristic 12-word-shingle screen reports zero overlap between the
normalized abstract-through-conclusion text and Papers 1--10 or the project
proposal. This is explicitly not an external plagiarism certificate.

The following author-side manifests validate and are bound here:

| Metadata artifact | SHA-256 |
|---|---|
| `paper/PAPER_CONFIGURATION.md` | `82a9402967537fe61ad49d081e02be5803207bb42bd4a0f6387f9d2c4f27d90c` |
| `paper/CLAIM_MANIFEST.json` | `c452d77404bd78482ed0be54d1f6a3f4736ca5220cf22c8a52c4e98143ea4bc9` |
| `paper/EXPERIMENT_PASSPORT.json` | `631b1102894d72cf608d53a7b96a7e7baf41fe0d5f638225ebe7876d52604f36` |
| `paper/FIGURE_PACKAGE.json` | `f310441a3df42cc70583ee09ab5b971b332f0c873f685e17e2c69bb143e39131` |
| `paper/PLAGIARISM_MANIFEST.json` | `a5e44ea401d1e3c52e9489dc0b2738b1d4cbbc89ea2073f90515ed53a58ba5dc` |
| `paper/PIPELINE_STATE.json` | `8f55bd719f12c2a9cf1dcd83669a6972f80f2f279a58137c9df26100aee86af0` |

The metadata graph is acyclic: base manifests bind the frozen manuscript and
authorities; `PIPELINE_STATE.json` binds those base manifests; this audit binds
the pipeline state; the downstream integrity record binds this audit. No node
hashes itself.

## Stop condition

The author-side pre-review package is frozen at
`READY_FOR_FRESH_INDEPENDENT_MANUSCRIPT_REVIEW`. The next authorized action is
a fresh independent manuscript review. This audit does not perform that
review, does not issue a manuscript verdict, and does not authorize
finalization.
