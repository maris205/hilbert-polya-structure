# Deterministic build profile (internal control record)

## Profile identity

This profile is bound to the immutable anonymous source trio for candidate
`positive_newton_translation_reciprocity_v5`.  It defines a standard TeX
build only; it is not a build receipt and it does not create a build root,
auxiliary file, PDF, release copy, or external effect.  The source manifest
at profile opening has 35 rows, framing digest
`8a7643372a808ace900b86666143abddedd76a152145f0dfaadd8fa53a966b6d`, and
the three source bytes are:

| Source | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| `paper/main.tex` | 33,811 | 829 | `ba9879a7084821b18c3e76166706d90d99bc4cb8e0bb1cb09d04a23f3a007f18` |
| `paper/math_commands.tex` | 601 | 17 | `34fdee026ed49adf9d7ad2d3b3c2d397549f29fd9f896fe5d54e046456e30957` |
| `paper/references.bib` | 6,607 | 217 | `4ec09da4d7be513d2cf11811515975e1f3c35b53ae9d84cbda6748cb39cbd23b` |

The article is expected to render as a proof-content document in the locked
24--28 page range.  Page count, PDF bytes, fonts, streams, and metadata are
build-stage observations and cannot be inferred from this profile.

## Pinned toolchain and environment

The commands must resolve through the following absolute executable targets,
which are checked immediately before the first build command:

| Tool | Invocation target | Resolved regular-file identity |
|---|---|---|
| pdfLaTeX | `/usr/bin/pdflatex` -> `/usr/bin/pdftex` | 1,802,504 bytes, mode 0755, SHA-256 `01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9` |
| BibTeX | `/usr/bin/bibtex` -> `/usr/bin/bibtex.original` | 117,128 bytes, mode 0755, SHA-256 `c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f` |

The standard packages are resolved from the system TeX tree and their
profile-time hashes are recorded here:

| Package | Path | SHA-256 |
|---|---|---|
| amsmath | `/usr/share/texlive/texmf-dist/tex/latex/amsmath/amsmath.sty` | `027b292408d989f370f160c9b5f5b89641f69cd19027b0342beb022dd74d7c83` |
| amssymb | `/usr/share/texlive/texmf-dist/tex/latex/amsfonts/amssymb.sty` | `70838b061b56569dd3ed9f339b1bdd1c78ba185de49f27ceae331c97f48b5986` |
| amsthm | `/usr/share/texlive/texmf-dist/tex/latex/amscls/amsthm.sty` | `8d5e2bdb117297385971927b14fe4804314133dc0027b3171249a08280894626` |
| mathtools | `/usr/share/texlive/texmf-dist/tex/latex/mathtools/mathtools.sty` | `e6bb70c66ffccc39e0ce8786d3dfca962a473339008a5a51ffae09075b74f5a7` |
| booktabs | `/usr/share/texlive/texmf-dist/tex/latex/booktabs/booktabs.sty` | `3fe694a5406f84847143e56ba1841385364277cfe7694a9f4bc0072ca8656abc` |
| array | `/usr/share/texlive/texmf-dist/tex/latex/tools/array.sty` | `1518422cc09b174c47105e41e3606260714b8f99049e3005a87f3c2ce034d157` |
| longtable | `/usr/share/texlive/texmf-dist/tex/latex/tools/longtable.sty` | `196f2a7038e1727c4088a015bf11cac88abfedc5b7ee5eca65f44ab91dbac415` |
| enumitem | `/usr/share/texlive/texmf-dist/tex/latex/enumitem/enumitem.sty` | `a217353d233e54e8c0944d87ea2924ec1f20d849a35b749698df03884856e5e3` |

Each root uses the following fixed environment, with no inherited locale or
time setting:

```text
PATH=/usr/bin:/bin
SOURCE_DATE_EPOCH=0
FORCE_SOURCE_DATE=1
TZ=UTC
LC_ALL=C
LANG=C
TEXMFVAR=<root>/texmf-var
TEXMFCONFIG=<root>/texmf-config
TEXMFHOME=<root>/texmf-home
XDG_CACHE_HOME=<root>/xdg-cache
```

The placeholders are expanded separately for each root.  The profile does
not repurpose a home-directory variable and does not permit writes outside
the selected root.

## Fresh roots and exact command sequence

Two roots are reserved by name but are not created by this profile:

* `papers/27-positive-newton-translation-reciprocity/build/r0-20260829`
* `papers/27-positive-newton-translation-reciprocity/build/r1-20260829`

Immediately before creating each one, its exact nonexistence and its parent
state must be checked.  The root is then created with mode `0700`; no root
may be reused, nested in the other root, or pre-created.  The `build/`
directory and both roots remain absent until a later build authorization.

For each root, the one and only permitted sequence is:

```text
mkdir -m 0700 <root>
mkdir -p <root>/texmf-var <root>/texmf-config <root>/texmf-home <root>/xdg-cache
install -m 0644 paper/main.tex <root>/main.tex
install -m 0644 paper/math_commands.tex <root>/math_commands.tex
install -m 0644 paper/references.bib <root>/references.bib
cd <root>
/usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape -recorder main.tex
/usr/bin/bibtex main
/usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape -recorder main.tex
/usr/bin/pdflatex -interaction=nonstopmode -halt-on-error -file-line-error -no-shell-escape -recorder main.tex
```

The three source copies must be byte-identical to the frozen hashes before
the first command.  No retry, alternate compiler, package installation,
network access, shell escape, compiler, `py_compile`, or post-command repair
is allowed.  Generated `.aux`, `.bbl`, `.blg`, `.fls`, `.log`, `.out`, and
`.pdf` files may exist only inside the authorized root.  Any unexpected file,
cache byte, command, status, or root permission is a hard build failure.

## Evidence obligations and handoff

The later build author must capture, before each first command, the raw source
hashes, executable identities, environment, root identity, and cache census.
It must record every command's raw exit status, logs, opening/closing root
manifests, PDF hash and byte count, page count, and cross-root comparisons.
The independent build reviewer must receive those time-indexed records and
must not infer a missing pre-command fact from a later PDF equality.  PDF
inspection includes raw bytes, decoded streams, dates, fonts, security
settings, page count, theorem text, citations, and the anonymous firewall.

This standard profile is sufficient; no custom harness is authorized.  A
failed build or a needed source repair requires a separately named ledger
revision and fresh source review.  This record itself does not authorize any
build action.

BATCH07_PAPER27_BUILD_PROFILE_FROZEN
