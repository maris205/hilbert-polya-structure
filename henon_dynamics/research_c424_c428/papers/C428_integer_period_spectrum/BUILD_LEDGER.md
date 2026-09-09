# C428 manuscript build ledger

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

The initial handoff `main.pdf` was a byte copy of `initial_03/main.pdf`.
`initial_03/source.tar` preserves the editable source, bibliography,
source audit, this ledger and README; its hash is checked at handoff.
No mathematical execution is hidden among these PDF builds: the
manuscript reports only the two historical author certificate runs
and the one historical independent reconstruction, with their
different evidence scopes stated in Section 7.

## Actual first-review revision builds

The complete nonauthor review and exact adopted changes are recorded
in `PAPER_IMPROVEMENT_LOG.md`. No mathematical program was rerun.
All three revision invocations used the fixed settings above, exited
0, and each ran three pdfLaTeX and two BibTeX passes. They are genuine
changed-input revision builds, not a final identical-input build pair.

| Attempt | Actual output | Subsequent action |
| --- | --- | --- |
| `round1_revised` | 16 pages, 388973 bytes; PDF SHA-256 `fd47f08578fff78c26e98a4a91fa2824256c6e311cf185eb88ccaf1a1933538a`. | P1/P2 applied. Its `input_source.tar` preserves this intermediate input. Then made support comparison explicitly `set(E)` and bound the distinct `b,c` to `S`. |
| `round1_revised_02` | 16 pages, 389315 bytes; PDF SHA-256 `c1d047ea288f5d91362c2b9d32a1703c5fd7b2f202d40af502a1fe95660fd395`. | Intermediate input preserved in `input_source.tar`. Full-page/text inspection found the inherited `secant- affine` source-line-break typography in the introduction, corrected as an author self-check. |
| `round1_revised_03` | 16 pages, 389314 bytes; PDF SHA-256 `cf02bdd886584949847f2583904601bb2734010a5f9d9cafbcbe749ddb0553af`. | Final first-review revision. Full transcript, clean final engine/BibTeX logs, PDF, complete extracted text and all 16 rendered pages retained. All 16 final pages actually viewed. |

Cumulative actual drafting and revision executions: six successful
latexmk invocations, zero failed compilations, eighteen engine passes,
twelve BibTeX passes. Two rejected patch attempts made no change
(an accidental empty hunk and a nonmatching abbreviated source line).
A diagnostic read guessed a nonexistent companion-paper directory;
the correct path was resolved with `rg --files`. None is a mathematical
or compilation failure. No external model, GPU job or certificate run
was involved.

The final revision engine and BibTeX logs have no Warning, Error,
Overfull, Underfull or undefined match. All 19 font resources are
embedded Type 1 with Unicode maps. `pdfinfo` reports an anonymous,
unencrypted, undated 16-page letter PDF with no JavaScript. The entire
788-line extracted text was read and all 16 page renderings viewed;
no clipping, collision, unresolved citation or missing table row was
found. Appendix A begins on page 12, Appendix B on page 14, and the
references span pages 15--16. The longer explicit pseudocode remains
readable across page continuations.

`main_round0_original.pdf` and `initial_03/source.tar` preserve the
initial handoff. `main_round1.pdf` and current `main.pdf` are byte
copies of `round1_revised_03/main.pdf`. The final revised
`round1_revised_03/source.tar` contains all 15 editable inputs, the
audit, README, updated ledger, complete first review, exact source
diff, improvement log and state. Its SHA-256 is reported at handoff.
All 12 editable inputs outside the three-file diff were compared
byte-identical with the extracted original source. The old author
programs and independent checker/output were rehashed unchanged.

The author stops writing at this revision handoff. The separately
scheduled second actual nonauthor manuscript review, formal evaluation
and fresh deterministic final build pair remain for the coordinator.
