# Initial manuscript compilation receipt

Date: 2026-09-05. Status: **INITIAL DRAFT BUILD SUCCESS**, not a
deterministic release or admission receipt. The unnumbered manuscript
contains complete proofs of the fixed finite-coupling claims and the
singular endpoint. No C number or five-paper completion is asserted.

## Actual build

Working directory:
`/root/autodl-tmp/hilbert-polya-structure/henon_dynamics/research_c399_c403/delta_comb/paper`.
An empty directory was obtained with
`mktemp -d /tmp/delta-comb-initial-build.XXXXXX`; the actual result was
`/tmp/delta-comb-initial-build.kfeCU0`.

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=/tmp/delta-comb-initial-build.kfeCU0 main.tex
```

The first invocation exited 0 and produced a 13-page PDF after the
normal BibTeX/reference passes. It needed no compile-error repair.
A wording-only precision edit changed the two squared-form expressions
called norms into their square-root norms in Section 2. The same
command was then rerun for that changed input and exited 0.
The resulting PDF has **13 pages, 405,764 bytes**.

Tools observed: latexmk 4.76, pdfTeX 1.40.22, TeX Live
2022/dev/Debian, BibTeX 0.99d. No packages were installed. This was
an ordinary initial build; no SOURCE_DATE_EPOCH or deterministic
settings were asserted. PDF timestamps reflect the environment's
CST rendering (19:43:36 CST = 11:43:36 UTC on the recorded date).

The generated final PDF and final engine log were copied to
[main.pdf](main.pdf) and [initial_pdflatex.log](initial_pdflatex.log).
The log is the final **pdflatex** pass, not a fabricated complete
latexmk console transcript. Earlier transient missing-citation
messages resolved through latexmk's normal passes.

## Initial checks actually performed

- The final engine log has zero occurrences of Warning, Overfull,
  Underfull, undefined, multiply defined, or a leading TeX error.
- PDF text extraction succeeded with 13 page breaks and no `??`,
  `[?]`, `[VERIFY]`, TODO, or FIXME marker.
- `pdfinfo` reports A4, 13 pages, no encryption and no JavaScript.
- All 21 font rows from `pdffonts` are embedded Type 1 fonts;
  their subset and Unicode flags are also yes.
- All eight natural section files are included by main.tex. All
  five bibliography entries are cited; there are no placeholder
  entries or orphaned section files.
- The source-to-proof mapping was checked against PAPER_PLAN.md:
  original proof steps 1--5 are in Section 2, step 6 in Section 3,
  steps 7--10 in Section 4, and steps 11--13 in Section 5.
  Section 6 uses actual SANITY_OUTPUT.json values, preserves the
  coarse-grid failure, and does not certify infinite counts.
- An author clarity/claim-coverage pass found no missing claim.
  This is self-checking, not an independent manuscript review.
- **No page image was visually inspected in this initial lane.**
  The coordinator explicitly owns the final all-page visual pass
  and two fresh deterministic builds, to avoid duplicating them.

Independent current-team manuscript review is being coordinated
separately. The existing independent proof review is not relabelled
as a review of this new PDF. No unavailable external GPT-5.4 review,
Route A evaluation, final manifest verification, or journal
submission-readiness pass is claimed here.

## Bound artifact identity

These hashes bind this initial receipt only; they are not a release
manifest. Later reviewed PDF changes must receive their own checks.

| File | SHA256 |
| --- | --- |
| main.pdf | 06f7dd31f97a02a267e69b34821dfdd5acc56f76e159ecb5c54151443e714b18 |
| initial_pdflatex.log | b0e0d5e397a65c14d1df7b17a3b4b16bed2563675cab549ed6e0351ed6b4527a |
| main.tex | e85f39d3ab773794bc768335b6a5719648180648ef3cde6cac1a158b786fdf69 |
| math_commands.tex | 0877c2538604b06108164619fff7d5ddad90db431b78dd34d1ae99880053c300 |
| references.bib | a99f9fe25a836b0c3c64957df4057eff7424680e0802c686af26d53de61d3853 |
| sections/0_abstract.tex | 01bc361cf7ed4fedccae43d92a8a556cbcb4cca65d5dade59c35d9ce89712433 |
| sections/1_introduction.tex | 1643c128d4c8822236e8f599c7809b4eda78ae6ecda0240bfc49f6720588afae |
| sections/2_forms.tex | 205bb36168a5391193c9337e99d3be3a26cae04bbd826a7bfb2da9c4947eb52a |
| sections/3_comparator.tex | 3f9b699040d7a26eae1430461d41d2c2d02706a6d635b68a6f2135e65c410982 |
| sections/4_asymptotics.tex | 404e95e350d5d3ab5c36076c50ee0546e6f13eef7ec045ccc75657b0c223ff83 |
| sections/5_strong_coupling.tex | 9e28f66ceb97ba250d9774cfa141d7d03bb5117b8093ce85f3d8516d90b54771 |
| sections/6_checks.tex | a6f92368734cc4b39b767c4ea9516030e2041b2f898e3d27087a43b46dfcd22f |
| sections/7_discussion.tex | dfb8ef3137bd1b3f85145f1b7de7a282a5596a34aca91ed33a122521466d36a9 |

The original PROOF_PACKAGE.md, sanity.py, and existing independent
proof review were not changed by this drafting task.

## Historical locator after final production

The 13-page PDF bound above was preserved, with exactly the stated hash, at
[../build/initial-main.pdf](../build/initial-main.pdf) before the reviewed
14-page PDF replaced `main.pdf`. This receipt's original TeX/PDF hashes describe
the initial snapshot, not the later production files. The final state and its
own checks are in [../BUILD_REPORT.md](../BUILD_REPORT.md). The original engine
log remains unchanged at the link above.
