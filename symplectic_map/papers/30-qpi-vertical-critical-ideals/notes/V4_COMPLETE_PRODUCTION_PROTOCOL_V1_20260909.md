# Paper30 V4 complete production input and fixed protocol

Date: 2026-09-09. Status: `FROZEN_BEFORE_R4_PRODUCTION`.
This records inputs and commands, not outcomes or acceptance.

The [user-approved page addendum](PUBLICATION_PAGE_ADDENDUM_V2_20260909.md)
changes only Paper30's body window to 22–40 pages. V4 contains the two actual
residual-overflow repairs described there; V1/V2/V3 and r0/r2 remain unchanged.
The root read the complete V3→V4 diff. All eleven files are present, the other
nine are byte-identical, and main.tex/macros.tex/global layout are unchanged.
The targeted change check is separate from the required fresh complete PDF review.

## Complete source freeze

Paths are relative to `paper/v4/`. The [checksum list](SOURCE_V4_20260909.sha256)
is checked in the source and both independent copied work directories, before
and after production. No frozen source edits are permitted during a build.

| Source | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| `macros.tex` | 9 | 327 | `b4831759010e67ff47811ba1346c0a8aea47d0e2fc1bfa6e3f8312828b6b5dc3` |
| `main.tex` | 62 | 2533 | `1d1a47776586fc72aa7041eaaf1098615b4bb1adc373f62546cbf71d6b6679b4` |
| `references.bib` | 183 | 5779 | `418530c0bc71f2fbbf5aa0e65b8d2c984c5c68f7fca9dcbb65c2fa84550ab0ba` |
| `sections/01-introduction.tex` | 300 | 13903 | `9b2876f36052d545ccf03a8309c4119f66ea06c3a9bbffa002e6228aa7610c0e` |
| `sections/02-surface-pencil.tex` | 446 | 20456 | `573a521e07117dc43b9291417469fa429701c67d711ec150a578b22c54205f8f` |
| `sections/03-spectral-jacobian.tex` | 438 | 19219 | `38e52e45513c51e9365d9bd0453776d09351fb1ca48b5d86233581112f95434f` |
| `sections/04-closed-hasse.tex` | 271 | 12079 | `68efcc6780280d7e06c107bc993fe4c431d8131b59f1f4f9e6b874dd96c6000e` |
| `sections/05-integral-trace.tex` | 246 | 10020 | `925b2bedcc8e942fb92797d9080b983f53010de97bc1676053390f8a5fc70ab0` |
| `sections/06-first-layer.tex` | 397 | 16400 | `e5ba6462600b04aee4d42f6d3ef85729ee2b3e7f5e6dfead92e37008d36ce392` |
| `sections/07-odd-jets.tex` | 468 | 18433 | `046f8cf808cc64de570605b316bcb5b0c6970f52492a585f97f97597ae2d74f5` |
| `sections/08-two-jets.tex` | 666 | 26100 | `5cfee2a607e6ff1ab52192bb5c9b1a73cef6635c3e5dcfe26aa73fe1192b42a9` |

## Bound controls

All selected tools/dependencies and metadata controls are those already observed
and fixed in the first-build input protocol below; this ordinary layout successor
does not install, fetch, replace or modify them. Actual transitive inputs remain
recorded by each new main.fls. No old auxiliary or compiled file is copied.

| Control, project-relative | SHA-256 |
|---|---|
| `notes/PUBLICATION_LOCK_20260909.md` | `e07f4bcb20f8aa445b41a5ceccd3d680036700fb63f26b9fc1379870c94573fa` |
| `notes/PUBLICATION_PAGE_ADDENDUM_V2_20260909.md` | `9cc96e76d8bd22dc7b76a4bb35791279c06fd1b83e24c3a74fe136f895a76380` |
| `notes/SOURCE_SCOPE_LOCK_V2_20260909.md` | `66afedb5efe87a29250d24aa2ba275fe79b1ec6eee727e362b0fc7b2c48df5b2` |
| `notes/FIRST_NATURAL_BUILD_INPUT_PROTOCOL_V1_20260909.md` | `24a734ad9b6b8116f54cf9969cd3dbcb81844a21eddd6a14b5fdc1986c0c9223` |
| `notes/COMPLETE_DRAFT_STATIC_DISPOSITION_V1_20260909.md` | `ed7f8d9b04d7aa7516a9b0f6af4a924ab16064fd5b5869d93962adadd0bba95a` |
| `notes/FIRST_COMPLETE_NATURAL_BUILD_RESULT_V1_20260909.md` | `ac86625f44ed62741ceefe84d62c67276f3cb8be5ee71a6edc00492c2375ebf5` |

## Exact commands and order

The root checked that r4 and r5 do not exist before freezing this record.
Create r4 from the complete eleven-file source, from the project directory:

```bash
test ! -e build/natural-20260909-r4
mkdir build/natural-20260909-r4
cp -a paper/v4 build/natural-20260909-r4/work
```

From its work directory, first run
`sha256sum -c ../../../notes/SOURCE_V4_20260909.sha256`.
Each following command uses bash with `set -o pipefail`; stop at the first
nonzero status and preserve that root. The four processes are, in order:

```bash
env SOURCE_DATE_EPOCH=0 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C.utf8 pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -recorder main.tex 2>&1 | tee ../pdflatex-1.stdout.log
env SOURCE_DATE_EPOCH=0 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C.utf8 bibtex main 2>&1 | tee ../bibtex.stdout.log
env SOURCE_DATE_EPOCH=0 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C.utf8 pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -recorder main.tex 2>&1 | tee ../pdflatex-2.stdout.log
env SOURCE_DATE_EPOCH=0 FORCE_SOURCE_DATE=1 TZ=UTC LC_ALL=C.utf8 pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error -file-line-error -recorder main.tex 2>&1 | tee ../pdflatex-3.stdout.log
```

Normal first-pass missing citations/labels are not final outcomes. An extra
same-source convergence pass is allowed only for a recorded actual unresolved
rerun requirement. Otherwise do not rerun the fixed root. Recheck all eleven
copied and original source hashes after completion.

Measure actual PDF body/reference boundaries using main.aux, pdfinfo and
pdftotext, not source length or a prior PDF. A result outside 22–40 stops the
page-window acceptance without font changes, scope cuts, padding or silent
threshold changes. If r4 succeeds and passes that window, create absent r5
with the same commands above substituting only r5 for r4, and run the exact
same four processes from its fresh work directory. Compare final PDF bytes
and SHA-256, not just renderings. Preserve all stdout/stderr and build artifacts.

After same-source two-root byte determinism, perform whole actual PDF reading
and fresh non-author complete manuscript/PDF review, followed by an independent
final integrity check. No acceptance is pre-granted by this protocol.
