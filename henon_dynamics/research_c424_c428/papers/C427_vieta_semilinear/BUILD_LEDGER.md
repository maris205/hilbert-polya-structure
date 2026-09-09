# C427 genuine initial builds and author handoff

2026-09-09 UTC. These are initial manuscript builds, not the required
post-review final independent-directory pair. No mathematical program
or old certificate was rerun. No nonauthor manuscript review is claimed.

## Environment and commands

The actual toolchain was latexmk 4.76, pdfTeX 1.40.22 / TeX Live
2022/dev/Debian, with the installed article/lmodern/AMS/natbib packages.
Every build used `SOURCE_DATE_EPOCH=1788912000`, `FORCE_SOURCE_DATE=1`,
`TZ=UTC`, `LC_ALL=C`, and the source disables PDF dates, pTeX metadata
and the variable trailer ID. The shell command, from this directory, was

```sh
env SOURCE_DATE_EPOCH=1788912000 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C \
  latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
  -outdir=builds/initial_01 main.tex
```

The other two runs used the same command with `initial_02` and
`initial_03` respectively. All three were fresh directories and exited
0. Each actual latexmk run invoked pdflatex three times and BibTeX twice.
The complete engine `.log`, BibTeX `.blg`, recorder `.fls`, dependency
`.fdb_latexmk`, `.bbl` and other generated files remain in each build
directory. Tool-console output was truncated in the interactive record;
no independent full console capture is claimed. The retained engine
and bibliography logs are the warning evidence.

## Real revisions, without invented review rounds

| Build | Outcome | Actual changes after/before this build |
| --- | --- | --- |
| `initial_01` | 12 pages, 346518 bytes | Successful original build; one underfull table label and one 3.49463 pt overfull inline example. Its original source archive was saved before editing. |
| `initial_02` | 12 pages, 346549 bytes | Table label shortened to `n=3 cycles`, polynomial-shear example displayed separately; `real` changed to `genuine` in one prose sentence. No warning remained. Two documentation links were also corrected. |
| `initial_03` | 13 pages, 346767 bytes | Added `\clearpage` before the appendix, following the selected compilation skill's appendix separation check. No mathematical or bibliographic content changed. This is the frozen initial review input. |

All earlier PDF/source archives are preserved. Archives contain the
actual nine TeX files and one BibTeX file, with directories retained;
the current exact input list is [INPUT_MANIFEST.sha256](INPUT_MANIFEST.sha256).

| File | SHA256 |
| --- | --- |
| `builds/initial_01/source.tar` | `782403ccda821ad5e840aa52d205c4a5ab9da0a9210cac63010805fa65a2d149` |
| `builds/initial_01/main.pdf` | `d787a42857d373e388e75c01442b9167b1480bc907ff7cfca7bdb0b3c415f97e` |
| `builds/initial_02/source.tar` | `93a36c57982a64a44152522d6502878fa23a3292cbf39a4f0c71427e86fd1ccb` |
| `builds/initial_02/main.pdf` | `b172a72255350f1631c44ba80be302a8b48333388bd6d355f482aeb2d77e0159` |
| `builds/initial_03/source.tar` | `35e78c9503e6f08c3f9ce2e3a2877a71d840f6636cc64344c2df507340862f83` |
| `builds/initial_03/main.pdf`, `main.pdf` | `ff63cdac04d87d212e7c902ce61c56695587e3b12379e180bd6f9c3c3e4dd021` |

## Actual initial-PDF checks

The coordinator read the entire 12-page `initial_02` extracted text,
viewed all its 12 separately rendered pages, and found no clipping,
missing characters, overlaps or broken equations. After the appendix
break in `initial_03`, pages 1–10 rendered byte-identically to the
already viewed pages (`cmp` on each PNG); the coordinator freshly
viewed pages 11–13, covering the now separate final reference page and
the two-page appendix. Page 11 is intentionally short, not missing text.
The renders use `pdftoppm -r 85 -png`; the full extracted text is saved
as `builds/initial_03/main.txt`.

`pdfinfo`: 13 letter-sized pages, 346767 bytes, PDF 1.5, unencrypted,
no JavaScript. Body concludes on page 10, references occupy the rest
of page 10 and page 11, and Appendix A is on pages 12–13. No target
venue or page quota has been selected. `pdffonts` lists 19 font rows,
all Type 1, embedded/subset, with Unicode mappings; no Type 3 font.
The final `.log`/`.blg` have no `Warning`, `Overfull`, `Underfull`,
`undefined` or TeX-error matches. The extracted text has no TODO,
FIXME, VERIFY, `??` or `[?]` match. `rg` returns 1 for these zero-hit
queries; it is not a compilation failure.

The source includes every section; no image is required. Both tables
are exact proof/ownership summaries, not experimental graphics.
The two actual nonauthor manuscript passes, any resulting repairs,
formal evaluation, final fresh-build pair and release sealing remain
pending at this initial handoff.
