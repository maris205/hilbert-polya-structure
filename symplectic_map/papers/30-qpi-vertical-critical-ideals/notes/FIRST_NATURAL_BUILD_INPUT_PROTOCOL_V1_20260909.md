# Paper30 first natural production input and protocol

Date: 2026-09-09. State: `COMPLETE_SOURCE_AND_BUILD_PROTOCOL_FROZEN`.
This is a pre-execution record, not a compilation, page-count, reproducibility or PDF acceptance.
The complete source is `paper/v2/`; V1 remains the immutable complete static-review input.
V2 only clarifies the abstract's smooth-fiber scope, the anticanonical-power/section
referent, and the precise henselian section citation. It changes no theorem, proof or layout.
The independent V1 report and actual V1-to-V2 delta disposition must be closed before execution.

## 1. Complete production source

Paths below are relative to `paper/v2/`. The whole 11-file set is copied to each empty build root.
The checksum input [SOURCE_V2_20260909.sha256](SOURCE_V2_20260909.sha256) has SHA-256
`343900f00d8f47acc087d99f4e3b45c688227b7e02685568740e69c24d11552e`. Execute its check from the source and again from each copied work directory.

| File | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| `macros.tex` | 9 | 327 | `b4831759010e67ff47811ba1346c0a8aea47d0e2fc1bfa6e3f8312828b6b5dc3` |
| `main.tex` | 62 | 2533 | `1d1a47776586fc72aa7041eaaf1098615b4bb1adc373f62546cbf71d6b6679b4` |
| `references.bib` | 183 | 5779 | `418530c0bc71f2fbbf5aa0e65b8d2c984c5c68f7fca9dcbb65c2fa84550ab0ba` |
| `sections/01-introduction.tex` | 300 | 13903 | `9b2876f36052d545ccf03a8309c4119f66ea06c3a9bbffa002e6228aa7610c0e` |
| `sections/02-surface-pencil.tex` | 446 | 20456 | `573a521e07117dc43b9291417469fa429701c67d711ec150a578b22c54205f8f` |
| `sections/03-spectral-jacobian.tex` | 435 | 19215 | `011c5415ac5d109c56cea3263ea9cad64db79a7f6102f12676c744bacb065b9b` |
| `sections/04-closed-hasse.tex` | 271 | 12079 | `68efcc6780280d7e06c107bc993fe4c431d8131b59f1f4f9e6b874dd96c6000e` |
| `sections/05-integral-trace.tex` | 244 | 10015 | `d25e401b8b14d56ce1eb8d0eb91c56bac8849dd9be933c6dcf19ac47a254f190` |
| `sections/06-first-layer.tex` | 394 | 16381 | `f4232d918c4d78bacfc7c7a9dea2fbbe0aa60e634fbf27354d1708e02d84792d` |
| `sections/07-odd-jets.tex` | 468 | 18431 | `8a5d216f27ca6b9c41a6c911f1d572b6728682138a3d96874c82f33b60eff690` |
| `sections/08-two-jets.tex` | 666 | 26100 | `5cfee2a607e6ff1ab52192bb5c9b1a73cef6635c3e5dcfe26aa73fe1192b42a9` |

## 2. Locked upstream production inputs

Paths are relative to the project; V2 source scope and the existing outline disposition
interpret the retained original source/publication locks without overwriting them.

| Input | SHA-256 |
|---|---|
| `notes/SOURCE_SCOPE_LOCK_20260909.md` | `b146ef107bd1956c96909ad4499bf803acf223fbc0d569a3e72d6185f79afa44` |
| `notes/SOURCE_SCOPE_LOCK_V2_20260909.md` | `66afedb5efe87a29250d24aa2ba275fe79b1ec6eee727e362b0fc7b2c48df5b2` |
| `notes/PUBLICATION_LOCK_20260909.md` | `e07f4bcb20f8aa445b41a5ceccd3d680036700fb63f26b9fc1379870c94573fa` |
| `PAPER_PLAN.md` | `12c824ec4f2b198ad28237fa6972a3747e1be1cf7557ead5115ca4b0764c3187` |
| `notes/OUTLINE_SCOPE_DISPOSITION_V1_20260909.md` | `ed5134e43d928d009c51963b1023d86daf871c63eafc5c6d4ab8077c312d93a3` |
| `notes/CITATION_RECORDS_20260909.md` | `8c531f799e71f82f01039332b1d80eaa78ea15b20d6716ddb21924faf98cbf6e` |
| `notes/COMPLETE_DRAFT_INPUT_SNAPSHOT_V1_20260909.md` | `a8047771fa2f899aaf0fad3d369129e77dad301fe6caa2fea20d79b49601e958` |

The bibliography has 17 actual cited keys. The Vlasenko erratum-content gap remains
`CORRECTION_IMPACT_UNKNOWN`; its original author version is only related work, not
a necessary proof premise. The precise Stacks citation correction is documented
in the complete static review and its delta disposition; the original citation ledger is preserved.

## 3. Observed local tools and fixed inputs

Observed before execution on 2026-09-09:
`/usr/bin/pdflatex`: pdfTeX 3.141592653-2.6-1.40.22, TeX Live 2022/dev/Debian;
kpathsea 6.3.4/dev. `/usr/bin/bibtex`: BibTeX 0.99d, same TeX distribution.
pdfTeX reports libpng 1.6.37, zlib 1.2.11 and xpdf 4.03.
Available locale names were C, C.utf8 and POSIX; use `LC_ALL=C.utf8`.
PDF inspection utilities pdfinfo, pdftotext, pdffonts and pdftoppm are installed.
No installation, network dependency retrieval, GPU, external write or Git operation is needed.

The directly selected class/packages/style were resolved locally and hashed below.
This is not a claim to have enumerated every transitive TeX/font input;
`-recorder` will preserve actual loaded inputs in each `main.fls`.

| Selected input | Resolved local path | SHA-256 |
|---|---|---|
| `article.cls` | `/usr/share/texlive/texmf-dist/tex/latex/base/article.cls` | `988fb3e599df7e5b545e4253829dab11f0c7bd7827b79d32c2aaadfb52db6f6c` |
| `lmodern.sty` | `/usr/share/texmf/tex/latex/lm/lmodern.sty` | `e1cdd137ae86b4e860f0b0bcfc4c1a90cae3ff1f9c651cb21bd86c15bb83b916` |
| `fontenc.sty` | `/usr/share/texlive/texmf-dist/tex/latex/base/fontenc.sty` | `d088c75e16c3c9f6b979a59571b96e5dd9e487a720bc74591580878388b82918` |
| `inputenc.sty` | `/usr/share/texlive/texmf-dist/tex/latex/base/inputenc.sty` | `16dffe967174f21dbd52ef849bcb74741109f3ce5bc68b881f1ce4aef3133b2a` |
| `geometry.sty` | `/usr/share/texlive/texmf-dist/tex/latex/geometry/geometry.sty` | `d5d36ad74051ad36288242b51438e2d9a5db2bd6c063b9b5704d0931fbc9f439` |
| `amsmath.sty` | `/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty` | `027b292408d989f370f160c9b5f5b89641f69cd19027b0342beb022dd74d7c83` |
| `amssymb.sty` | `/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty` | `70838b061b56569dd3ed9f339b1bdd1c78ba185de49f27ceae331c97f48b5986` |
| `amsthm.sty` | `/usr/share/texlive/texmf-dist/tex/latex/amscls/amsthm.sty` | `8d5e2bdb117297385971927b14fe4804314133dc0027b3171249a08280894626` |
| `mathtools.sty` | `/usr/share/texlive/texmf-dist/tex/latex/mathtools/mathtools.sty` | `e6bb70c66ffccc39e0ce8786d3dfca962a473339008a5a51ffae09075b74f5a7` |
| `booktabs.sty` | `/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty` | `3fe694a5406f84847143e56ba1841385364277cfe7694a9f4bc0072ca8656abc` |
| `array.sty` | `/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty` | `1518422cc09b174c47105e41e3606260714b8f99049e3005a87f3c2ce034d157` |
| `natbib.sty` | `/usr/share/texlive/texmf-dist/tex/latex/natbib/natbib.sty` | `d2709be806dc7d5f54daa9a16022ba1451b1322954751b98e38cfad0cc107450` |
| `hyperref.sty` | `/usr/share/texlive/texmf-dist/tex/latex/hyperref/hyperref.sty` | `77e7c2421a06900f158416e090665069dd724a6e0c605cd2a1838c7d3b7944d2` |
| `plainnat.bst` | `/usr/share/texlive/texmf-dist/bibtex/bst/natbib/plainnat.bst` | `21eefa76f1c967f5074776fcef096c0f8f2b9e42347e84b62e1dbb121dcae486` |

The source fixes article 11pt, letter, one column, one-inch margins and ordinary
spacing, with no necessary-proof appendix or artificial body page break.
It sets `pdfinfoomitdate=1`, `pdfsuppressptexinfo=15` and an empty `pdftrailerid`
when provided by this engine. Every TeX/BibTeX process uses
`SOURCE_DATE_EPOCH=0 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C.utf8`.

## 4. Exact planned commands

Run from the project directory, only after the complete static disposition is closed:

```bash
test ! -e build/natural-20260909-r0
mkdir -p build
mkdir build/natural-20260909-r0
cp -a paper/v2 build/natural-20260909-r0/work
```

The existence checks and mkdir/copy sequence use fail-fast shell execution.
From `build/natural-20260909-r0/work/`, first run:

```bash
sha256sum -c ../../../notes/SOURCE_V2_20260909.sha256
```

Then run the following four commands in order, with bash `set -o pipefail`;
stop on a nonzero command status and retain the entire root:

```bash
env SOURCE_DATE_EPOCH=0 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C.utf8 pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -recorder main.tex 2>&1 | tee ../pdflatex-1.stdout.log
env SOURCE_DATE_EPOCH=0 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C.utf8 bibtex main 2>&1 | tee ../bibtex.stdout.log
env SOURCE_DATE_EPOCH=0 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C.utf8 pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -recorder main.tex 2>&1 | tee ../pdflatex-2.stdout.log
env SOURCE_DATE_EPOCH=0 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C.utf8 pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -recorder main.tex 2>&1 | tee ../pdflatex-3.stdout.log
```

Only actual unresolved cross-references permit recorded additional same-source convergence.
The work directory retains all copied source, aux/bbl/blg/log/fls/out and PDF outputs;
root-level stdout logs are retained. No cleanup command is part of this protocol.

## 5. Measurements, second root and boundary

After successful convergence, inspect the actual `main.pdf` with pdfinfo and pdftotext,
and compare the `LastBodyPage` aux label with the PDF's actual reference-start page.
All necessary proofs remain before the explicit bibliography clearpage.
The locked body range is 22–30 pages; references are counted separately.

Only if the first successful complete natural build has body 22–30 may the same
source/protocol be built in the second absent root `build/natural-20260909-r1/`.
For it, change only r0 to r1 in the preparation/work-directory paths; use the same
four command lines, environment, checksums and filenames.
Compare the two resulting PDF SHA-256 values before claiming byte determinism.

Under/over-window output is preserved and cannot be made acceptable by padding,
shrinking, scope deletion, proof appendices or unapproved redefinition of the contract.
An ordinary actual compiler/transcription issue may be repaired in a fresh source
successor and fresh build root with a narrow change record; frozen inputs and
failed roots are never overwritten. Page or scientific-contract changes require
an explicit user decision. Actual PDF reading, independent manuscript/PDF review
and final integrity review remain separate subsequent obligations.
