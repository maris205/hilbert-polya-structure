# C423 final same-input build and every-page inspection

2026-09-08 UTC. Both genuine full-manuscript reviews have been read completely
and accepted by the coordinator: [round 1](../../manuscript_reviews/round1/C423_REVIEW.md)
and [round 2](../../manuscript_reviews/round2/C423_REVIEW.md). The first is
335 lines, the second 290; both have zero mandatory findings. The two optional
precision edits are recorded in [REVISION_ROUND1.md](REVISION_ROUND1.md).
No manuscript source changed after the second reviewed inputs.

## Actual fresh builds

Two separate initially nonexistent directories, builds/final1 and
builds/final2, were built by two actual latexmk invocations. Both exited 0.
The common command, with the final digit changed only in the output path, was:

    env SOURCE_DATE_EPOCH=1788825600 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error '-usepretex=\pdftrailerid{}' -jobname=main -outdir=builds/final1 main.tex

The installed latexmk help was checked before using usepretex. Its actual
compiler command prepended the empty pdftrailerid instruction to inputting
main.tex. This is a build-only metadata setting, not a TeX/Bib revision.
It prevents the output directory from changing pdfTeX's default file ID.
It was adopted in response to the observed C421 comparison failure; no
fictitious C423 failed pair is claimed. The C423 final pair passed directly.

Environment actually observed: Linux 5.15.0-78-generic x86_64; pdfTeX
1.40.22, TeX Live 2022/dev/Debian; LaTeX2e 2021-11-15 patch 1;
latexmk 4.76; BibTeX 0.99d. The log records /etc/LatexMk and actual
package inputs. The command executions and their exit statuses were
observed directly; final engine and BibTeX logs/auxiliaries are retained.

Both PDFs: **6 pages, 317347 bytes**, SHA256
03ab70bcbcac190c9592c55337dba2d6a124fb8574039ff00e5f5b23ec86f9bb.
Byte comparison with cmp exited 0, as did comparison of the two generated
main.bbl files. [main.pdf](main.pdf) is a byte-preserving copy of final1.

Final engine-log hashes:

    final1: 29f00699edecdfa9303d87430f557162a51f0df2d0005587171a2d9b41c8417c
    final2: 85e113f75a17049c53acbe9f6d0f22a32b900af4d261e3466052bf74e31905ff

All ten production files were byte-compared with their reviewed
snapshots/round1 counterparts; all passed. Their generated final input
manifest, builds/final1/source_inputs.sha256, has SHA256
da9ac909d7f463a36ecb2fb0b84cf837be288e6845446cef63d6f8f5262a2e7a.
The full individual hashes are also in the second review. A read-only
binary diagnostic found exactly one ID field in the reviewed round1 PDF;
removing that 75-byte field in memory gives exactly the final PDF bytes.
Neither PDF was edited by this diagnostic. Thus the review-to-final change
is fully localized to the generated ID, not different text or pagination.

## Actual final PDF checks

Both final engine and BibTeX logs were searched for warning, overfull,
underfull, undefined and error diagnostics: zero matches (rg exit 1 for
no match). All twenty pdffonts rows are embedded, subsetted, Unicode-mapped
Type 1 fonts. The PDF is unencrypted, US letter, PDF 1.5, with no form
or JavaScript. It is not tagged for accessibility; no tagged-PDF claim is made.

The entire final1 PDF text was newly extracted and read, pages 1–3 then
4–6. All six final pages were newly rendered at 100 dpi under
builds/final1/page-1.png through page-6.png and actually visually inspected.

| Pages | Material inspected | Outcome |
| --- | --- | --- |
| 1–2 | Revised abstract, full classification, source table and reduction | Legible; quantifiers and superscripts preserved; no overlap or clipping |
| 3–4 | Universal local-height input, exact two-cycle/escape, prime-period infinitude | Complete displays, bars, limits and proof endings; no missing glyph |
| 5 | Arbitrary-field descent, revised algebraic-closure explanation, limitations | Complete and readable; no lost line at page boundary |
| 6 | Dependency/access disclosure and both bibliography entries | Complete URLs and source-version notes; short page accepted without padding |

No mathematical program, source search, external model, submission or Git
write was part of this build task. Formal evaluation and exact whole-batch
sealing/synchronization are separate records, not certified by a PDF hash.
