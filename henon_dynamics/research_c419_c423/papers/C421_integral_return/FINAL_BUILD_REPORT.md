# C421 final release build report

Date: 8 September 2026. Status: **PASS — two fresh final builds are byte-identical; all 18 final pages inspected.**

This is a release-production check after the accepted round-two manuscript review, not a new mathematical experiment or a substitute for that review. The release PDF is `main.pdf`, copied from `build_final_stable1/main.pdf` only after exact comparison and final checks. No production TeX, bibliography, mathematical program, accepted receipt, or supplement was changed during this task.

## 1. Reviewed inputs and preserved versions

The 17 production TeX/Bib files remain those in `ROUND1_SOURCE_SHA256SUMS.txt`. A complete `sha256sum -c ROUND1_SOURCE_SHA256SUMS.txt` check passed before building and again after both final builds: **17/17 OK**, exit 0. The manifest SHA-256 is:

```text
d25c04662e738dae4e753f5c9f33cc11cadbc3c09a9195e1c12d2a118591dfef
```

The complete round-two review was accepted by the coordinating author before this task. The approved reviewed PDF, `main_round1.pdf`, remains unchanged:

```text
c497c8f2efc4d6a22f28153ef27178040c3af8d099fa610ea564d1e1a7df575b
```

The old root alias was first confirmed identical to the preserved baseline `main_round0_original.pdf`. That baseline remains unchanged, as do `build_baseline/`, `build_round1/`, both initial final-build attempts, and both successful stable-build directories. Its SHA-256 is:

```text
7fcfe7c00da4590cc44565d2343a5d3e37f233c5ece4798971891e9f145b5e1d
```

The listing input `supplement/integral_return/certify_ir1_core.py` was also checked unchanged, SHA-256:

```text
750b4dbb54cacd1df11cc3929ed436cf8de9877048545f212cecc9bc03b75330
```

No mathematical certifier or symbolic checker was executed. All numerical evidence in the manuscript remains historical proof-stage evidence.

## 2. Actual environment

All commands below ran from this paper directory on Linux 5.15.0-78-generic, x86_64 GNU/Linux, using the installed toolchain without installation or upgrades:

- latexmk 4.76;
- pdfTeX 3.141592653-2.6-1.40.22, TeX Live 2022/dev/Debian, kpathsea 6.3.4/dev;
- LaTeX2e 2021-11-15, patch level 1;
- BibTeX 0.99d;
- Poppler `pdfinfo`, `pdffonts`, `pdftotext`, and `pdftoppm` 22.02.0.

Every build command set `SOURCE_DATE_EPOCH=1788825600 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C`. This fixes the PDF creation/modification date to `D:20260908000000Z`. The local `pdfinfo` display renders that instant as 08:00 CST, even when invoked with `TZ=UTC`; direct inspection of the PDF confirms the stored UTC timestamp. This display behavior is not a build discrepancy.

Tool/configuration byte identifiers:

```text
/etc/LatexMk   276b04cd6052a7574fecfc7acad3295d67c4bcf99b2f544b82a6157abe8340aa
/usr/bin/latexmk 22e2164fea826ee19ff234503ef807d2728541e10eb3563912169977a650c951
pdftex        01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9
bibtex        c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f
```

The paper uses the established 11-point article fallback with one-inch margins. No named venue template or venue page-limit compliance is asserted.

## 3. Initial fresh pair: successful compilation, failed byte comparison

Both directory names were checked absent before `mkdir build_final1 build_final2`. They were genuinely new and did not inherit auxiliary files. Two separate commands were executed with Bash `pipefail`:

```bash
set -o pipefail
env SOURCE_DATE_EPOCH=1788825600 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C \
  latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=build_final1 main.tex 2>&1 | tee build_final1/compile_console.log

set -o pipefail
env SOURCE_DATE_EPOCH=1788825600 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C \
  latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=build_final2 main.tex 2>&1 | tee build_final2/compile_console.log
```

Both latexmk commands exited **0**, each performing three pdflatex passes and two BibTeX passes. These are normal dependency/convergence passes within one build. Each produced an 18-page, 473670-byte PDF. The first exact `cmp` exited **1**, reporting the first difference at byte 472055, line 2467. The hashes were:

```text
build_final1/main.pdf de38dbd7bd40841a6508e94fa46b43b806d562283e148f62948c3156a5cf5f1d
build_final2/main.pdf 425fec48310d525ec705fb716d961c59ed95f0ff4d43b5a37c1b7fade44b4bd4
```

Read-only comparison isolated the entire difference to the two hexadecimal values in the PDF trailer `/ID` entry. The first build used `204EB76180CFEC163D505BDB8AF0CF8E`; the second used `CB08148D2A88AE8B8755648A37CF4246`. Replacing only these values in comparison streams made the PDFs identical to each other and to the reviewed PDF. No PDF was modified by that diagnostic.

The coordinating author was informed before any correction and explicitly approved a build-only change to omit the volatile automatic trailer ID, while preserving the failed comparison pair and without forcing the old PDF identity.

## 4. Successful fresh final pair

Two additional absent directory names were checked and then created: `build_final_stable1` and `build_final_stable2`. Neither inherited auxiliary files. The approved correction was supplied only as a compiler command override; the reviewed source files were not edited. The actual commands were:

```bash
set -o pipefail
env SOURCE_DATE_EPOCH=1788825600 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C \
  latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=build_final_stable1 \
  -pdflatex='pdflatex %O -jobname=main "\pdftrailerid{}\input{main.tex}"' \
  main.tex 2>&1 | tee build_final_stable1/compile_console.log

set -o pipefail
env SOURCE_DATE_EPOCH=1788825600 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C \
  latexmk -pdf -interaction=nonstopmode -halt-on-error \
  -outdir=build_final_stable2 \
  -pdflatex='pdflatex %O -jobname=main "\pdftrailerid{}\input{main.tex}"' \
  main.tex 2>&1 | tee build_final_stable2/compile_console.log

cmp build_final_stable1/main.pdf build_final_stable2/main.pdf
cmp build_final_stable1/main.bbl build_final_stable2/main.bbl
```

Both build commands exited **0**, each again performing three pdflatex and two BibTeX passes. Both comparisons exited **0**. There were four actual fresh builds in total: the first pair had a disclosed metadata-only comparison failure; the second pair is the successful release pair. No hidden retry or PDF post-processing is involved.

Both final PDFs are **18 pages, 473595 bytes**, with identical SHA-256:

```text
13fece76ec21d56eacbdcb43303f3acef017e9f9b7f1e0e228f5438cd6761d0c
```

The `/ID` entry is absent from the final pair. The following read-only stream comparison exited 0:

```bash
cmp build_final_stable1/main.pdf \
  <(sed -E 's@^/ID \[<[^>]+> <[^>]+>\]$@@' main_round1.pdf)
```

Thus the final PDF is byte-for-byte the approved reviewed PDF except that the 75 characters of the automatic `/ID` entry were omitted, leaving the existing line ending. No content stream, layout, reference, font, formula, or other metadata changed. A preliminary diagnostic that deleted the entire line also deleted its newline and correctly failed comparison; keeping the line ending resolved that diagnostic, without writing to either PDF.

## 5. Final log, bibliography, font, and text checks

The complete final `main.log` and `main.blg` files for both successful builds were scanned for `Warning`, `Overfull`, `Underfull`, `undefined`, `LaTeX Error`, and `Package Error`: **0 matches**. BibTeX resolved all six bibliography entries; both generated `.bbl` files are byte-identical. No missing citation, unresolved label, rerun request, fatal compiler error, or box warning remains.

The final inspections used:

```bash
pdftotext -layout build_final_stable1/main.pdf build_final_stable1/main.txt
pdfinfo build_final_stable1/main.pdf
pdffonts build_final_stable1/main.pdf
cmp build_final_stable1/main.txt <(pdftotext -layout main_round1.pdf -)
```

All exited **0**. The final extracted text is 864 lines and was read in full, including the references and listing through source line 139. The same-layout comparison with the approved review PDF passed exactly. An earlier comparison against the old non-layout text export failed because extraction options differed; regenerating only the comparison stream with the same `-layout` option passed. No content discrepancy was found.

The extracted-text marker scan for `??`, `TODO`, `FIXME`, `PLACEHOLDER`, and `TBD` found **0 matches**. Text extraction naturally rearranges some mathematical accents/superscripts; those formulas were additionally checked in rendered page images.

`pdfinfo` reports PDF 1.5, 18 letter-size pages (612 by 792 points), no encryption, zero page rotation, no JavaScript or form. `pdffonts` reports **24 fonts, all embedded, all subset, all with Unicode mappings**, with no Type 3 fonts. Empty optional title/author metadata fields are unchanged from the reviewed PDF; the visible title, anonymous author line, and date are present.

## 6. Actual all-page visual inspection

The final first-build PDF was rendered with:

```bash
mkdir build_final_stable1/visual
pdftoppm -png -r 110 build_final_stable1/main.pdf \
  build_final_stable1/visual/page
```

The render command exited **0**, producing `page-01.png` through `page-18.png`. Every one of these 18 images was actually opened and inspected, not merely counted. Since the second PDF is byte-identical, these checks apply to both final builds and the released alias.

| Page | Material actually checked | Result |
|---|---|---|
| 1 | Title, anonymity, date, abstract, introductory equation and paragraphs | PASS; no clipping or missing glyphs |
| 2 | Related-work distinctions, scope table, organization, inverse and invariant | PASS; table and formulas fit |
| 3 | Theorem 2.1, complete ten-row classification table, least-period list | PASS; every row and range readable |
| 4 | Difference identity, both preliminary lemmas, uniform-reduction setup | PASS; statements and equations intact |
| 5 | Endpoint centers and both nontrivial `s=-1` branches | PASS; inequalities and indices readable |
| 6 | Signed normalization and both signed center cases | PASS; all branches and formulas readable |
| 7 | End of reduction, orientation restoration, residual core, algorithm start | PASS; ordinary algorithm page continuation |
| 8 | Algorithm continuation, coverage/termination proof, inverse seed intervals | PASS; no lost list item or formula |
| 9 | Independent traversal/matching, complete finite counts, disposition table | PASS; full table fits above footer |
| 10 | Exceptional words and least-period/orientation arguments | PASS; conventional paragraph continuation to page 11 |
| 11 | Remaining least-period proof and arithmetic tests 1–5 | PASS; no missing proposition content |
| 12 | Arithmetic tests 6–9, count proof, fixed-point and zeta formulas | PASS; formula (24) fully readable |
| 13 | Scope, limitations, computation boundary, AI/review disclosure | PASS; deliberate white space before references |
| 14 | All six references, journal metadata, preprint identifier and URLs | PASS; no overrun or unresolved reference |
| 15 | Appendix provenance, execution caveat, supplement instructions, hashes | PASS; long identifiers remain within text area |
| 16 | Final identifier and complete certifier listing lines 1–57 | PASS; legible fixed-width listing and numbering |
| 17 | Certifier listing lines 58–125 | PASS; continuation, numbering, frame and wrapped lines intact |
| 18 | Certifier listing lines 126–139 including final `run()` and closing frame | PASS; long output call wraps as configured, no truncation |

No new manuscript defect requiring source correction was identified.

## 7. Release placement and artifact hashes

After successful final PDF/BibTeX/text comparisons and all-page inspection, a Bash `set -e` sequence repeated those comparisons, verified the old root alias against `main_round0_original.pdf`, and performed:

```bash
cp build_final_stable1/main.pdf main.pdf
cmp main.pdf build_final_stable1/main.pdf
sha256sum main.pdf main_round0_original.pdf main_round1.pdf
```

The sequence exited **0**. Only the current `main.pdf` alias was replaced; its previous bytes remain recoverable in `main_round0_original.pdf` and the baseline build. The final root alias has the final-pair SHA-256 printed above, 473595 bytes and 18 pages.

Additional final artifact SHA-256 values:

```text
build_final_stable1/main.log
  e42ac875d26b04ab0e3a00d8ebc4ea33191d3650a05273fa7be1f1cf22adec04
build_final_stable2/main.log
  f0144762452e64a5e4dcfd34b9c4f693af4a64785e8b074c70fb4b74b7680350
build_final_stable1/main.blg and build_final_stable2/main.blg
  a94914ec47c8bddcf4cf558a03e879b426b83207826de237fa9d8d62894406c6
build_final_stable1/compile_console.log
  40f498e70bfb771060ecbef8d80525bbbbd43d1cbb0a2e6d89644105ea9b9f7e
build_final_stable2/compile_console.log
  9d1a89e1d1b138e723d7eb00ee6520d91f52e7f615b17c95f991675802d6a939
build_final_stable1/main.txt
  46c0ed34db3fa97f92f4192f575572553ae025c4f62324ff9b6f3fc1a103ff1a
build_final_stable1/pdfinfo.txt
  63c797a6f4e71635476ee6c410ebbf61d39eba27abdeff32624a0f30786a01d7
build_final_stable1/pdffonts.txt
  2912c6dab4ec2d05c28e50b6af27c9e0fc0eec886550ad6a00ac8b552a71441a
```

Logs differ between the two successful builds in directory/process bookkeeping, not in warnings or final output. The byte-identity requirement is met by the actual PDFs and bibliography outputs; log identity is not asserted.

The `paper-compile` workflow was used for convergence, bibliography/log/font checks, fresh deterministic comparison, and all-page visual validation. No Git operation, shared tracking-file edit, new proof computation, or authorial manuscript revision was performed. Final editorial release adjudication remains with the coordinating author.
