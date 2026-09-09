# C426 final deterministic build report

2026-09-09 UTC. **FINAL_BUILD_COMPLETE_PENDING_SEAL — writer stop.**
Both actual nonauthor manuscript passes were completed and adjudicated
before these builds. This is the final typesetting/build gate, not a
new manuscript review, mathematical execution, formal evaluation or
release seal.

## Result

Two previously nonexistent output directories, `builds/final_01/` and
`builds/final_02/`, were independently built from the same frozen ten
editable inputs. Both latexmk invocations exited 0. Their complete
PDFs compare byte-identical with `cmp` and have SHA-256
`d0b4e14e8ed42002bf0ad454ee004c817403e9662ae92b25306a94adf4d582db`.
Each has 10 pages and 343725 bytes. The selected final PDF is
`builds/final_02/main.pdf`; `main.pdf` is copied from that actual build.
It also compares byte-identical with the already reviewed
`main_round1.pdf`, no-change `main_round2.pdf` and original revision
build PDF. Equality with an earlier PDF does not replace the two real
fresh builds recorded here.

No TeX, bibliography, table, theorem, proof or mathematical program was
changed. No build failed, no retry was needed, and no third final build
was launched. All prior initial/revision outputs and source archives
remain preserved. Main-round aliases retain their historical identities.

## Frozen inputs and review gate

The complete second review was read before building:
`../../manuscript_reviews/round2/C426_REVIEW.md`, SHA-256
`30db2f60462771ff47a3347ce0a02755e9fcd7d2d11c68f7287d681475afa605`.
It closes P1/P2/P3 with no new findings and no required source edit.

`FINAL_INPUTS.sha256` lists all ten active editable TeX/Bib inputs,
SHA-256 `97451e88c5b07516c7e855a494fe256c648e3787a9ff9c267c6b5e52e310cf74`.
The list contains main, bibliography, seven sections and one table;
all are included by the actual source tree. The checksum manifest
was checked before each build, after both builds and again after the
final-page inspection. Every entry passed every check.

Each new build independently archived these inputs before compilation
as `input_source.tar`. The two archives are themselves byte-identical,
SHA-256 `8d065aa6ebdae5836c8329142b5b0ecefbc9243ab4a71ecf92f75af4c7bdf0c1`.
Every member was streamed separately from each archive and compared
byte-for-byte with its active source. All ten were also separately
stream-compared with the already reviewed `builds/round1_revised/source.tar`.
All thirty member comparisons passed. The latter historical archive,
not regenerated here, retains its original hash and documentation.

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
| `final_01` | 0 | 3 | 2 | 10 pages; 343725 bytes |
| `final_02` | 0 | 3 | 2 | 10 pages; 343725 bytes |

Each transcript records three actual engine outputs, with sizes 309601,
343573 and 343725 bytes; early-pass citation/reference warnings resolve
in the final pass. The two final builds add six engine and four BibTeX
passes. Together with the two initial builds and one review revision,
the manuscript has five successful latexmk invocations, zero failed
invocations, fifteen engine passes and ten BibTeX passes. None of these
passes is counted as another manuscript review or mathematical test.

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

Both PDFs were inspected with `pdfinfo` and `pdffonts`: 10 pages,
612 by 792 pt letter paper, PDF 1.5, 343725 bytes, empty author,
unencrypted, no JavaScript, and no CreationDate/ModDate fields.
All 20 font resources in each PDF are embedded and subset Type 1
fonts with Unicode maps; there are no Type 3 or unembedded resources.
The anonymous English 11pt article has one-inch margins. No venue
or artificial page cap was selected, so no venue-compliance claim
is made.

Actual `pdftotext -layout` outputs were retained for both fresh PDFs.
They compare byte-identical to one another and to the reviewed revision
text. Their SHA-256 is
`afeac1609b8b0613b3bfa6181cbb2b17a8db8aaf8a1e180639a594205d86d62a`.
The complete 520-line final text was read. No `??`, `[?]`, VERIFY,
TODO or FIXME marker was found. Both actual auxiliary files contain
nine citation commands and the same five resolved bibliography keys;
the complete bibliography is visible on page 10.

The selected final PDF was newly rendered with
`pdftoppm -scale-to 1400 -png` to `builds/final_02/pages/page-01.png`
through `page-10.png`. Every one of the ten final page images was
actually viewed after building. Inspection covered the abstract and
source table, the multi-page classification theorem, all-affine
necessity, every characteristic's centre test, the wild-centre example,
global CRT and explicit basis, both ideal examples, scope and references.
No clipped formula, missing glyph, overlap, broken table row or illegible
proof continuation was found. The mathematical body and references
both finish on page 10; there is no external proof appendix.
Because the two complete PDFs compare byte-identical, these final
page views apply to the shared final artifact; they are not claimed
as twenty separate image views.

## Persistent evidence hashes

| File | SHA-256 |
| --- | --- |
| `builds/final_01/compile.log` | `2d463eb0b3b64f50a0b2aa5e1ec17b3660510baffddcfde7b0f28d4c1708815e` |
| `builds/final_02/compile.log` | `e7a6ffd03a44dc5de819252f36992304f828114516bc6c78b8c555e394e29242` |
| `builds/final_01/main.log` | `4fe8fca6a471315bd2765960882ba6ef2cdf34996478ccf636c62c89c25f865d` |
| `builds/final_02/main.log` | `4066b9d7a5677fbfe1c8e2ed71878f773b4e9f296624a93a2ea95a3a4cd175fa` |
| Both `main.blg` files | `182cd035f3e4a41b2f4e770c02a102eda7328054d8f5d39f11c54f0d0d30663b` |

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

The writer stops now. Final build completion is recorded in README;
formal evaluation, final payload seal, independent membership verification
and integration remain coordinator-owned and are not certified by this
report. The pre-build manuscript-improvement state records its historical
review completion; this report is the authoritative later build receipt.
