# Deterministic build-profile revision (internal control record)

## Binding and scope

This record supersedes BUILD_PROFILE.md only because its source bibliography
was corrected in the single authorized revision window after the preserved R0
BibTeX failure.  It is an internal control record and has no publication,
upload, submission, hosting, identity, or other external effect.  The
source/control manifest immediately before this record contains 40 rows,
5,833 framing bytes, and aggregate
e7d0796d716078481f01dba85ff87cb12700267942918fa74fab3ae44e647b67 under
path<TAB>bytes<TAB>LF<TAB>644<TAB>1<TAB>sha256<LF>.  The controlled ledger
and the entire authorized build subtree are excluded from that aggregate.

The revised anonymous source trio is:

| Source | Bytes | LF | SHA-256 |
|---|---:|---:|---|
| paper/main.tex | 33,811 | 829 | ba9879a7084821b18c3e76166706d90d99bc4cb8e0bb1cb09d04a23f3a007f18 |
| paper/math_commands.tex | 601 | 17 | 34fdee026ed49adf9d7ad2d3b3c2d397549f29fd9f896fe5d54e046456e30957 |
| paper/references.bib | 6,610 | 217 | a77d814de144852c760c9c6e894ad92ea567dd03be188e2786662aaf7cb521e5 |

The source-revision review is
notes/INDEPENDENT_SOURCE_REVISION_REVIEW.md, 5,858 bytes, 112 LF, SHA-256
769c21cf8d6c9b42b044cd3546020ad1ea07b1e9fdcdb1e20bc2215f62f98309.  The
old failed root papers/27-positive-newton-translation-reciprocity/build/
r0-20260829 is immutable evidence and is never a source or build input.

## Fixed toolchain

The exact executable targets and resolved regular-file identities are:

| Invocation | Resolved target | Bytes | Mode | SHA-256 |
|---|---|---:|---:|---|
| /usr/bin/pdflatex | /usr/bin/pdftex | 1,802,504 | 0755 | 01a7ab54ebf2fd89865aa0743ae9eaeec37ba4be75ca7cd254631cba6fb76cf9 |
| /usr/bin/bibtex | /usr/bin/bibtex.original | 117,128 | 0755 | c9ecb71856a3e6a597fceaaa22d624efe9ba46506c90a6609149abf9f22ad18f |

The eight package files are resolved from the system tree and must match
these SHA-256 values before each first compiler command:

amsmath 027b292408d989f370f160c9b5f5b89641f69cd19027b0342beb022dd74d7c83
amssymb 70838b061b56569dd3ed9f339b1bdd1c78ba185de49f27ceae331c97f48b5986
amsthm 8d5e2bdb117297385971927b14fe4804314133dc0027b3171249a08280894626
mathtools e6bb70c66ffccc39e0ce8786d3dfca962a473339008a5a51ffae09075b74f5a7
booktabs 3fe694a5406f84847143e56ba1841385364277cfe7694a9f4bc0072ca8656abc
array 1518422cc09b174c47105e41e3606260714b8f99049e3005a87f3c2ce034d157
longtable 196f2a7038e1727c4088a015bf11cac88abfedc5b7ee5eca65f44ab91dbac415
enumitem a217353d233e54e8c0944d87ea2924ec1f20d849a35b749698df03884856e5e3

## Environment and fresh roots

Each child process receives exactly:

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

The existing build parent is the controlled mode-0755 directory
papers/27-positive-newton-translation-reciprocity/build.  Two new roots are
reserved but are not created or inspected by this record:

papers/27-positive-newton-translation-reciprocity/build/r0-rev1-20260830
papers/27-positive-newton-translation-reciprocity/build/r1-rev1-20260830

Immediately before each root mkdir, the exact path must be checked absent and
the parent identity checked.  Each root is created mode 0700 and is never
reused, nested, or copied from the failed root.

## Exact one-shot sequence per root

From the project directory, after the immediate nonexistence check:

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

The source copies must be byte-identical to the revised trio before the first
compiler command.  Auxiliary files, logs, recorder files, PDFs, and any cache
bytes may exist only inside the selected root.  No retry, alternate builder,
package installation, network, shell escape, post-command repair, source
mutation, or cleanup is allowed under this profile.

## Evidence handoff

The build author must record time-indexed source-copy, executable, package,
environment, root, and cache identities before each first command; every raw
command status; opening and closing root manifests; log and PDF hashes and
byte counts; page count; and normalized cross-root comparisons.  The
independent build reviewer must inspect the preserved failed-root boundary
and both new roots directly.  Missing pre-command facts cannot be inferred
from later equality.  PDF inspection must cover raw bytes, decoded streams,
dates, fonts, security flags, pages, theorem text, citations, and anonymous
metadata.  This profile authorizes no build by itself.

BATCH07_PAPER27_BUILD_PROFILE_REVISION_FROZEN
