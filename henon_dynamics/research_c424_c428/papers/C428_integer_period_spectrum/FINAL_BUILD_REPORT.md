# C428 final deterministic build report

2026-09-09 UTC. **FINAL_BUILD_COMPLETE_PENDING_SEAL — writer stop.**
Both actual nonauthor manuscript passes were completed and adjudicated
before these builds. This is the final typesetting/build gate, not a
new manuscript review, mathematical execution, formal evaluation or
release seal.

## Result

Two previously nonexistent output directories, `builds/final_01/` and
`builds/final_02/`, were independently built from the same frozen fifteen
editable inputs. Both latexmk invocations exited 0. Their complete
PDFs compare byte-identical with `cmp` and have SHA-256
`cf02bdd886584949847f2583904601bb2734010a5f9d9cafbcbe749ddb0553af`.
Each has 16 pages and 389314 bytes. The selected final PDF is
`builds/final_02/main.pdf`; `main.pdf` was explicitly copied from that
actual build. It also compares byte-identical with the already reviewed
`main_round1.pdf`, no-change `main_round2.pdf` and the final first-review
revision build. Equality with an earlier PDF does not substitute for
the two real fresh builds recorded here.

No TeX, bibliography, table, theorem, proof or mathematical program was
changed. No build failed, no retry was needed, and no third final build
was launched. All prior initial/revision outputs and source archives
remain preserved. Main-round aliases retain their historical identities.

## Frozen inputs and actual review closure

The complete second manuscript review was read before building. Its
unchanged full copy is `reviews/round2/REVIEW.md`, from
`../../manuscript_reviews/round2/C428_REVIEW.md`, SHA-256
`724dc2ba066ba48d25822664e12f2a36a727e30ccd43b3a45595c6f1b1178042`.
It closes P1/P2/T1 with zero remaining must-fix and zero new optional
findings. The coordinator adopted it and requested no source change.
The improvement log/state were updated to this actual closure before
the final pair; `main_round2.pdf` was saved as a no-change round alias.

`FINAL_INPUTS.sha256` lists all fifteen active editable TeX/Bib inputs,
SHA-256 `afa96126117e48bc266cc82406cdd7a55473d799596e36c9334cabe3157e7e0c`.
The list contains main, bibliography, nine sections and four exact
tables; all are included by the actual source tree. The checksum
manifest was checked before each build, after both builds and again
after the final-page inspection. Every entry passed every check.

Each new build independently archived these inputs before compilation
as `input_source.tar`. The two archives compare byte-identical,
SHA-256 `30aba8ebb244b00f1c5001f3e9a741d70fd1b7ba9302ee68242723dc1c16033d`.
Every member was streamed separately from each archive and compared
byte-for-byte with its active source. All fifteen were also separately
stream-compared with the already reviewed
`builds/round1_revised_03/source.tar`. All forty-five member comparisons
passed. That historical archive was not regenerated here and retains
SHA-256 `aa8d95083804dc7f226be3b72eb901aede362c5f347959e01ca4b5ec131c6171`,
including its original review-stage documentation.

## Exact execution and fixed settings

Both invocations were launched independently, in parallel, from the
manuscript directory, with disjoint fresh output directories. Each
directory was checked absent and then created. No cleaning command
was run, and no previously built auxiliary file was copied in. Each
build used the following command, with its own literal output suffix:

```bash
env SOURCE_DATE_EPOCH=1788912000 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C \
  latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=builds/final_01 main.tex 2>&1 | tee builds/final_01/compile.log
env SOURCE_DATE_EPOCH=1788912000 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C \
  latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=builds/final_02 main.tex 2>&1 | tee builds/final_02/compile.log
```

The shell enabled pipefail and captured the latexmk status through
`PIPESTATUS[0]`, printing `latexmk_exit_code=0` and returning that
status in both actual tool results. The complete stdout/stderr stream
of each latexmk invocation remains in its `compile.log`; terminal
display truncation did not truncate either file.

The unchanged preamble sets `pdfinfoomitdate=1`, an empty PDF trailer
ID, and `pdfsuppressptexinfo=15`. The local configuration read was
`/etc/LatexMk`. All generated dependency records, engine logs, `.blg`,
`.bbl`, `.aux`, `.fls` and `.fdb_latexmk` files remain in their own
build directories.

| Actual invocation | Exit | pdfLaTeX passes | BibTeX passes | Final output |
| --- | --- | --- | --- | --- |
| `final_01` | 0 | 3 | 2 | 16 pages; 389314 bytes |
| `final_02` | 0 | 3 | 2 | 16 pages; 389314 bytes |

Each transcript records three actual engine outputs: first 15 pages
and 379093 bytes, then 16 pages and 388703 bytes, finally 16 pages and
389314 bytes. Early-pass citation/reference warnings resolve in the
final pass. The two final builds add six engine and four BibTeX passes.
Together with the three initial builds and three changed-input review
revision builds, the manuscript has eight successful latexmk invocations,
zero failed invocations, twenty-four engine passes and sixteen BibTeX
passes. None is counted as another manuscript review or mathematical test.

Actual installed tools, checked before building:

- `/usr/bin/pdflatex`: pdfTeX 3.141592653-2.6-1.40.22, TeX Live
  2022/dev/Debian; kpathsea 6.3.4/dev. The actual log uses LaTeX2e
  2021-11-15 patch level 1 and article class 2021/10/04 v1.4n.
- `/usr/bin/latexmk`: 4.76, dated 20 November 2021.
- `/usr/bin/bibtex`: 0.99d, TeX Live 2022/dev/Debian.
- `/usr/bin/pdfinfo`, `pdftotext`, `pdffonts`, `pdftoppm`: Poppler
  22.02.0, each queried separately.
- `uname -srmo`: Linux 5.15.0-78-generic x86_64 GNU/Linux.

## Actual final quality checks

Both final engine and BibTeX logs were searched for Warning, Error,
Overfull, Underfull and undefined; there were zero matches in all four
files. The normal unresolved early-pass messages remain visible in
the full compile transcripts. A no-match `rg` returns exit 1 and is
not a failed build. The preliminary absence checks similarly reported
that the two final output directories did not yet exist, as required.
A later read-only diagnostic initially guessed the wrong C426 directory
when looking for the completed sibling build-report format; it failed
to start a process there, then read the correct directory from the batch
plan. No file changed, no build failed, and C426 remained frozen.

Both PDFs were inspected with `pdfinfo` and `pdffonts`: 16 pages,
612 by 792 pt letter paper, PDF 1.5, 389314 bytes, empty author,
unencrypted, no JavaScript, and no CreationDate/ModDate fields.
All 19 font resources in each PDF are embedded and subset Type 1
fonts with Unicode maps; there are no Type 3 or unembedded resources.
The anonymous English 11pt article has one-inch margins. No venue
or artificial page cap was selected, so no venue-compliance claim
is made.

Actual `pdftotext -layout` outputs were retained for both fresh PDFs.
They compare byte-identical to one another and to the reviewed revision
text. Their SHA-256 is
`87acdc8595ba8ba09541ed68b4a943b7f973a4a5ee7eefd2b9ee94163206b428`.
The complete 788-line final text was read. No `??`, `[?]`, VERIFY,
TODO or FIXME marker was found. Both actual auxiliary files contain
eighteen citation commands and the same seven resolved bibliography
keys. The full references are visible across pages 15--16; both IH6
records print their date year only once. The recorded mathematical
command extracts with the two ASCII hyphens in `--diameter` intact.

The selected final PDF was newly rendered with
`pdftoppm -scale-to 1400 -png` to `builds/final_02/pages/page-01.png`
through `page-16.png`. Every one of the sixteen final page images was
actually viewed after building. Inspection covered the exact family-
union theorem and source deductions; integer secant remainder and
all-diameter endpoint reduction; interpolation and full-support graph
proof; all four exact tables and eleven witnesses; identity/exceptional
graphs and pruning; historical execution boundaries; complete numerical
and affine pseudocode; alternative reconstruction equivalence; and all
seven bibliography records. Coordinate-keyed dictionaries, the explicit
target loop, exceptional-diameter evaluation and right-hand `D-b` values
remain unambiguous in the actual rendered Appendix A continuations.

No clipped formula, missing glyph, overlap, broken table row or illegible
proof continuation was found. The main text ends on page 11; Appendix A
begins on page 12 and Appendix B on page 14; references span pages
15--16. Because both complete PDFs compare byte-identical, these page
views apply to the shared final artifact; they are not claimed as
thirty-two separate image views. The final builder's all-sixteen-page
inspection is distinct from the second reviewer's six affected-page
inspection and does not relabel that review's actual scope.

## Persistent evidence hashes

| File | SHA-256 |
| --- | --- |
| `builds/final_01/compile.log` | `e3bcc35731477febd4b5147e72b26dec6a6566ef6de59dc80fe5227c1410bafb` |
| `builds/final_02/compile.log` | `81382564b56f22d237f5bd0c9d855b6cbf1a0876464b60022e81d9307d45672a` |
| `builds/final_01/main.log` | `3b5cea6c06eed30931162943853e107fb64636ae79b49e8d2f9b87d65f103d24` |
| `builds/final_02/main.log` | `a925a94e3e1546725ee42a121221c424470703ddfd8f262fd77a0cc7b27c01af` |
| Both `main.blg` files | `0b36e337d1de641c1b36e42e976f7c6e74928457ca335c0778f9b5e30e84df41` |

These hashes identify bytes and are not substitutes for the reviewed
mathematical proof or the actual comparisons and page checks.

## Handoff boundary

The `paper-compile` skill supplied the real build, logs, font/text and
every-page quality checks. The batch contract overrides its cleaning,
automatic source-fix and ML-venue defaults: old evidence was preserved,
no manuscript source was changed, and only the authorized two final
builds ran. No mathematical program, old certificate, external model,
external upload or GPU job was invoked. No other manuscript, shared
evaluation/registry/seal or Git object was written.

The improvement log/state and README record actual final-build
completion. `BUILD_LEDGER.md` and historical archived documentation
retain their earlier-stage wording; this report is the later final-build
receipt. Formal evaluation, final payload seal, independent membership
verification and integration remain coordinator-owned and are not
certified by this report. The writer stops now.
