# C428 initial manuscript build ledger

2026-09-09 UTC. These three actual drafting builds are not manuscript
review rounds and not the coordinator's two future fresh final-release
builds. No mathematical certificate program was executed or modified
while preparing this manuscript.

## Fixed settings

Each invocation used `SOURCE_DATE_EPOCH=1788912000`,
`FORCE_SOURCE_DATE=1`, `TZ=UTC`, `LC_ALL=C`, and `latexmk -pdf
-interaction=nonstopmode -halt-on-error -outdir=... main.tex`.
The preamble sets `pdfinfoomitdate=1`, an empty `pdftrailerid`, and
`pdfsuppressptexinfo=15`. Engine: pdfTeX 1.40.22, TeX Live
2022/dev/Debian; latexmk 4.76; BibTeX 0.99d. The format is an anonymous
English 11pt article, letter paper, one-inch margins, without a
venue-specific page cap.

## Actual compile attempts

| Attempt | Actual result | Persistent output and subsequent correction |
| --- | --- | --- |
| `initial_01` | Exit 0; 16 pages, 387737 bytes; three pdfLaTeX passes and two BibTeX passes. Two final overfull hboxes: 27.61766pt for the independent command and 1.31245pt for a long artifact path. | Transcript, engine log, PDF and original `source.tar` retained. The command was moved to a quote environment; the artifact-path wording was shortened. |
| `initial_02` | Exit 0; 16 pages, 387746 bytes; three pdfLaTeX passes and two BibTeX passes. Final log clean. | Full transcript, final log, PDF, extracted text and all 16 rendered page images retained. All pages were viewed. The extracted shell option used an en dash; its source was changed from `--diameter` to `-{}-diameter` to preserve two literal hyphens. Pre-change `source.tar` retained. |
| `initial_03` | Exit 0; 16 pages, 387701 bytes; three pdfLaTeX passes and two BibTeX passes. Final log clean. | Full transcript, final log, PDF, extracted text and all 16 rendered page images retained. The shell command extracts with ASCII `--diameter`; all 16 final page renderings were viewed. |

There were three successful latexmk invocations, zero failed
invocations, nine engine passes and six BibTeX passes. The cumulative
transcripts preserve expected early-pass reference/citation warnings;
these were resolved by latexmk. Final `initial_03/main.log` has no
Warning, Overfull, Underfull or undefined matches. A diagnostic `rg`
with no matches returns exit 1; this is not a failed compilation.

## Actual PDF checks

- `pdfinfo`: 16 pages, 387701 bytes, 612 by 792 pt, empty author,
  unencrypted, no JavaScript and no CreationDate/ModDate reported.
- `pdffonts`: all 19 resources embedded; all Type 1, no Type 3.
- `pdftotext -layout`: actual text extracted. The two-hyphen command
  is correct; no `??`, `[?]`, `VERIFY`, `TODO` or `FIXME` marker was
  found. No unresolved-reference marker appears in the sources.
- All 16 renderings were actually viewed. The four exact tables,
  displayed formulas, source hashes, pseudocode and references have
  no clipping or collisions. Proof continuations remain readable.
- The main text ends on page 11; Appendix A begins on page 12;
  Appendix B begins on page 14; references span pages 15--16.
  The final page is lightly filled by the end of the bibliography;
  no artificial page cap or compression was applied.

## Preserved baseline hashes

| Artifact | SHA-256 |
| --- | --- |
| `initial_01/main.pdf` | `8c06ce870c7b7d96da858e150baf7bbd70a01905a261b880ebdd3b7182375520` |
| `initial_02/main.pdf` | `10b5fd6120cff93fb6bc57a0bb2594159a68478de0ad914bd207201559f0a47e` |
| `initial_03/main.pdf` | `d5aeb4ae86009dc9f229a54c50083ccb03eba1f3bdc562d13a12400140dd8cde` |
| `initial_01/source.tar` | `d408384ef2bf3bbb040c179d6deaf711700c6eeca8271508abbcdec7a4c6d3bb` |
| `initial_02/source.tar` | `8c72e59e5abd2b29e8dd55af5fae511961ad56c2839c8cbb1051a76da6615b7a` |

The handoff `main.pdf` is a byte copy of `initial_03/main.pdf`.
`initial_03/source.tar` preserves the editable source, bibliography,
source audit, this ledger and README; its hash is checked at handoff.
No mathematical execution is hidden among these PDF builds: the
manuscript reports only the two historical author certificate runs
and the one historical independent reconstruction, with their
different evidence scopes stated in Section 7.

The author stops writing at handoff. Two actual nonauthor manuscript
reviews, adjudicated revisions, formal evaluation and the fresh
deterministic final build pair remain for coordinator scheduling.
