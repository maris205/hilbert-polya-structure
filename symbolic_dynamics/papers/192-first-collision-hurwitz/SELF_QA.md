# Round-0 Self-QA and accepted-repair addendum

Date: 2026-09-04 UTC.

Disposition: immutable Round-0 baseline retained; Review-A repair incorporated
in the current manuscript; `OWNER_RED_AMBER/HOLD_EXTERNAL` remains binding.

## Manuscript integrity

- [x] The immutable Round-0 `main.tex` had hash `5171a6dcacce38068b04a6c2a3fe8a7332068c5b320dca99ad3607f5a9c1f7c5`; its PDF is retained as `main_round0_original.pdf`.
- [x] The current repaired `main.tex` has hash `30cd2c9bc853d9b195f89527db4794681e4d3dcacd8c45f5aea0b49a98ab12f9`.
- [x] Carrier, product order, long-cycle orientation, right Hurwitz move, lower endpoint, and least-index scheduler are explicit.
- [x] Theorem-level claims are limited to strict histories/fixed recurrence, sharp tail, fixed count, every-target fibre atlas, and unique maximum indegree.
- [x] The history-set law is labelled `Conjecture 5.1`.
- [x] The manuscript explicitly withholds theorem status from the binomial depth law, unique deepest-state consequence, and derived basin formula.
- [x] The abstract and limitations state `OWNER_RED_AMBER/HOLD_EXTERNAL` / `HOLD_EXTERNAL` and deny novelty inference.
- [x] Classical Hurwitz, parking-function, tree, and Prüfer ingredients receive zero contribution credit.

## Proof QA

- [x] The equal-transposition degeneracy is excluded using minimal transposition length.
- [x] The local collision proof checks the comparison at (i-1), not only positions strictly before it.
- [x] The sharp witness is linked to the canonical factorization by product-preserving Hurwitz moves.
- [x] Pollak's orbit division includes freeness, adjacent-inequality invariance, and unique empty-spot normalization.
- [x] The inverse formula (H_i^{-1}(u,v)=(uvu,u)) is checked algebraically.
- [x] Reverse admissibility includes both (i<j(y)) and the endpoint inequality (c>a).
- [x] Maximum-fibre uniqueness uses both strict increase and the parking inequalities.
- [x] The (n=2) boundary case is consistent.
- [x] The conjectural history formula is not used by any proved axis.

## Computation QA

- [x] `PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py | cmp - code/CANONICAL.txt` exits zero.
- [x] A repeated Python replay exits zero against the same canonical transcript.
- [x] `code/verify_n9.cpp` compiles under C++17 with `-O3 -Wall -Wextra -pedantic` and no warning.
- [x] The C++ stream traverses all (9^7=4,782,969) Prüfer words and emits all 128 masks.
- [x] Two independent raw n=9 runs are byte-identical.
- [x] `/tmp/p192_verify_n9 | cmp - code/CANONICAL_N9.txt` exits zero.
- [x] Both transcripts explicitly deny an all-(n) theorem for the history law.
- [x] No Python bytecode cache was produced by the recorded command.

## Source QA

- [x] All five Round-0 cited keys occurred in the Round-0 bibliography.
- [x] The repaired manuscript has six matched citation/BibTeX keys, adding Campion Loth--Rattan (2025) and explicitly zero-crediting its conditional Hurwitz-string construction.
- [x] Dénes metadata was checked against the Hungarian Academy repository.
- [x] Stanley 1997 metadata/DOI was checked against the journal page.
- [x] Irving--Rattan metadata/DOI was checked against Elsevier and arXiv records.
- [x] Stanley Volume 2 metadata/DOI was checked against Cambridge University Press.
- [x] Gorsky--Gorsky is cited as the verified arXiv preprint, not with unsupported journal coordinates.
- [x] Four bibliography corrections are disclosed in `SOURCE_VERIFICATION.md` and `BUILD.md`.
- [ ] A complete external search for exact or equivalent adaptive schedulers has not been performed/frozen.

## Build and visual QA

- [x] Two builds started from separate fresh temporary directories containing only source inputs.
- [x] Both used the same explicit UTC source epoch and four-pass `pdflatex`/`bibtex` recipe.
- [x] Their PDFs are byte-identical.
- [x] Final log scan finds no warning, overfull/underfull box, undefined citation/reference, or multiply-defined label.
- [x] The immutable Round-0 pin has three A4 pages; `pdfinfo` reports four A4 pages for the repaired current PDF, PDF 1.5, no encryption, and no JavaScript.
- [x] `pdffonts` reports every listed font embedded and subsetted.
- [x] `pdftotext` extracts all sections and bibliography.
- [x] All three Round-0 pages and all four repaired pages were rasterized and visually inspected with no clipping, collision, or blank-page defect.

## Open defects and holds

1. **History proof gap:** no all-(n) bijection explains the mask formula. The law remains a conjecture despite exact (n\le8) exhaustion and independent (n=9) streaming.
2. **Owner gap:** there is no frozen, query-by-query external exact-scheduler search sufficient for novelty or priority assessment. External circulation remains prohibited.
3. **Convention sensitivity:** reverse-cycle or inverse-Hurwitz variants are outside the proved contract and can behave differently.
4. **Higher fibres:** the one-step atlas iterates algorithmically, but no uniform higher-fibre or basin formula is proved.
5. **Tooling limitation:** `latexmk` and `qpdf` are unavailable in this environment; explicit TeX passes and Poppler tools were used instead.
6. **Repository limitation:** the workspace is not a Git worktree, so no Git diff/commit hash can be supplied. File-level SHA-256 hashes are the freeze mechanism.
7. **Snapshot caveat:** `main_round0_original.pdf` is the immutable three-page hostile-review pin with SHA-256 `aa0ade6d64cb2cbd87545bde50ed15ba2b9729e3235aa7395b4be892b1cb76f1`; it is no longer byte-identical to repaired `main.pdf`, whose four-page SHA-256 is `e06aac2579f0d90a15c1a7a2c8fa09ce57286f15818a10c2466cd06d210d6b57`. The superseded pre-audit PDF remains `main_pre_metadata_audit.pdf` with SHA-256 `220b3e2f5111f83c23bc29608472eab858e6369dbbdf13dbbef85b1c542098e0`.

No defect above changes the four proved mathematical axes. Defects 1 and 2 block promotion beyond the present internal gate.
