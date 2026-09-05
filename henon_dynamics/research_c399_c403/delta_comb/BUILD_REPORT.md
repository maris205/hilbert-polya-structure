# Reviewed research-draft build receipt

Date: 2026-09-05. Output: [paper/main.pdf](paper/main.pdf), **14 pages**, 406,100
bytes. This is a complete unnumbered mathematical research manuscript, not a
C-numbered release, formal Route-A evaluation, five-paper completion, global
novelty certificate, human peer review, or journal submission.

## Review and actual revisions

The complete proof received the independent current-team review in
[REVIEW_OF_DELTA_COMB.md](../boole/REVIEW_OF_DELTA_COMB.md). The actual manuscript,
primary citation passages, and finite-output reporting were subsequently checked
in [DELTA_MANUSCRIPT_REVIEW.md](../reviews/DELTA_MANUSCRIPT_REVIEW.md).
That review found no blocking mathematical or citation issue. All five actual
bibliography entries and nine citation contexts were checked against primary
metadata/text/formulas; all nine numerical rows were reconciled with the saved
JSON. These are bounded internal checks, not exhaustive literature validation.

The only editorial finding, D-MINOR-1, was addressed by replacing the broad
abstract sentence about interval decoupling with the precise statement that
Dirichlet-wall replacement changes the leading high-energy coefficient. The
main preamble also suppresses PDF date and trailer-ID fields. No theorem,
proof, citation, numerical method, or table value changed. The original proof
and sanity-check script were therefore not rerun for these two production edits.
The independent review's appended targeted receipt binds the changed inputs.

Final amended manuscript-review SHA256:
`6089b17c74d494982bc8bd27230fe8ca5d5539f507d61f83d8ac8c4e3556103e`.

## Two fresh deterministic builds

Working directory:
`henon_dynamics/research_c399_c403/delta_comb/paper/` under the repository root.
Each output directory was separately created by `mktemp -d` and was empty.

```sh
env SOURCE_DATE_EPOCH=1788566400 FORCE_SOURCE_DATE=1 TZ=UTC \
  latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=/tmp/delta-comb-final-a.imtLY7 main.tex
env SOURCE_DATE_EPOCH=1788566400 FORCE_SOURCE_DATE=1 TZ=UTC \
  latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=/tmp/delta-comb-final-b.hCuZ1A main.tex
cmp /tmp/delta-comb-final-a.imtLY7/main.pdf /tmp/delta-comb-final-b.hCuZ1A/main.pdf
```

Both actual `latexmk` processes exited **0**; `cmp` exited **0**. Normal
fresh-build bibliography/reference passes resolved the early transient
warnings. The document has a fixed explicit date. Byte identity is established
for these inputs and this environment, not for every TeX distribution.

Observed environment: Latexmk 4.76; pdfTeX 3.141592653-2.6-1.40.22;
TeX Live 2022/dev/Debian; LaTeX2e 2021-11-15 patch level 1; BibTeX 0.99d.
No package installation or system-setting change was needed.

| Generated artifact | SHA256 |
|---|---|
| Both fresh PDFs and saved `paper/main.pdf` | `ed580df6ca898434951fbad6aa0c91130af77e58537e5900fc634f4eaf4279b5` |
| [build/compile-a.log](build/compile-a.log), final engine pass | `5ea177399326a8a25acaed067db6494ea011178f9c5f1347935385cc9a2859ee` |
| [build/compile-b.log](build/compile-b.log), final engine pass | `03786201ea9be125a2fdd332d806c861083b8d918749482c35f48d4242a8247c` |

The actual final engine logs differ because their temporary paths differ.
They are not represented as complete archived latexmk console transcripts.
The earlier ordinary 13-page build remains separately available at
[build/initial-main.pdf](build/initial-main.pdf), SHA256
`06f7dd31f97a02a267e69b34821dfdd5acc56f76e159ecb5c54151443e714b18`.
Its [initial receipt](paper/INITIAL_COMPILE_REPORT.md) binds the earlier inputs,
not the later final PDF. The extra final page is a bibliography continuation
after the clarified abstract changed pagination; no page quota was imposed.

## Final output checks actually performed

- `pdfinfo`: A4, 14 pages, 406,100 bytes, unencrypted PDF 1.5, no JavaScript.
- Both final engine logs were searched for `Warning`, `Overfull`, `Underfull`,
  `undefined`, `multiply defined`, and a leading TeX error. No matches were
  found; the expected `rg` exit code was 1.
- `pdffonts`: all 21 font rows are embedded, subsetted, and have Unicode maps.
- `pdftotext` succeeded. The full extracted-text marker search found no `??`,
  `[?]`, `[VERIFY]`, `TODO`, or `FIXME`.
- `pdftoppm -r 105 -png` rendered all final pages and exited 0. The coordinator
  viewed **every page, 1–14 individually**, including the nine-row table,
  theorem/equation numbering, cross-page arguments, and bibliography. No
  overlap, missing glyph, clipped content, or empty-content page was observed.
  Page 14 contains the last three bibliography entries and is intentional.
- All eight section files are included. All five bibliography entries are
  used; the independent review records their nine actual citation contexts.
- Saved PDF/log hashes were checked against the corresponding generated files
  after copying. The initial PDF was preserved before the final PDF replaced
  its delivery path; no user artifact was deleted.

## Exact final manuscript inputs

Paths are relative to `paper/`. These eleven authored TeX/BibTeX files are the
complete manuscript input set; installed class/package/font files are provided
by the environment recorded above.

| Input | SHA256 |
|---|---|
| `main.tex` | `ad78a74abfc5f9d7a62a8b5ed8c7db094a453f55da85f398a4f4af84113e2b5f` |
| `math_commands.tex` | `0877c2538604b06108164619fff7d5ddad90db431b78dd34d1ae99880053c300` |
| `references.bib` | `a99f9fe25a836b0c3c64957df4057eff7424680e0802c686af26d53de61d3853` |
| `sections/0_abstract.tex` | `95c63f61da43d369b99a6f2f98d1604d723135e85ec86cb20b34aff89c3e9f69` |
| `sections/1_introduction.tex` | `1643c128d4c8822236e8f599c7809b4eda78ae6ecda0240bfc49f6720588afae` |
| `sections/2_forms.tex` | `205bb36168a5391193c9337e99d3be3a26cae04bbd826a7bfb2da9c4947eb52a` |
| `sections/3_comparator.tex` | `3f9b699040d7a26eae1430461d41d2c2d02706a6d635b68a6f2135e65c410982` |
| `sections/4_asymptotics.tex` | `404e95e350d5d3ab5c36076c50ee0546e6f13eef7ec045ccc75657b0c223ff83` |
| `sections/5_strong_coupling.tex` | `9e28f66ceb97ba250d9774cfa141d7d03bb5117b8093ce85f3d8516d90b54771` |
| `sections/6_checks.tex` | `a6f92368734cc4b39b767c4ea9516030e2041b2f898e3d27087a43b46dfcd22f` |
| `sections/7_discussion.tex` | `dfb8ef3137bd1b3f85145f1b7de7a282a5596a34aca91ed33a122521466d36a9` |

The unchanged complete proof has SHA256
`7a63727caee39ba2926e2fe93dd249df17ea9ec4ba5ddf7b760432f02898b0af`.
The numerical execution record remains [CHECK_REPORT.md](CHECK_REPORT.md),
with raw [SANITY_OUTPUT.json](SANITY_OUTPUT.json). Its coarse-grid 311/312
discrepancy is retained. Neither PDF success nor finite agreement establishes
the all-energy theorem, interval-certified counts, or target arithmetic.
