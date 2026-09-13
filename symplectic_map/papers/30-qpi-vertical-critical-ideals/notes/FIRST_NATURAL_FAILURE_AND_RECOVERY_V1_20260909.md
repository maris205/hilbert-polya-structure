# Paper30 first natural build failure and minimal recovery

Date: 2026-09-09. The complete V2 source was actually copied to the absent
`build/natural-20260909-r0/work/`, and all eleven copied-source checksums passed.
The [frozen first-build protocol](FIRST_NATURAL_BUILD_INPUT_PROTOCOL_V1_20260909.md)
and [complete-static disposition](COMPLETE_DRAFT_STATIC_DISPOSITION_V1_20260909.md)
preceded this execution. No partial manuscript or measurement probe was used.

## 1. Actual r0 result, preserved

- pdfLaTeX pass 1: exit status 1, fatal at `sections/07-odd-jets.tex:338`.
- BibTeX and pdfLaTeX passes 2/3: NOT_RUN, because the first process failed.
- `main.pdf`: absent. Physical body/reference counts: NOT_MEASURED.
- `main.log`, `main.fls`, `main.aux`, `main.out`, the copied source and
  `pdflatex-1.stdout.log` remain in the original r0 root; nothing was cleaned or rerun there.
- Undefined citations/references in this aborted first pass are unconverged first-pass
  diagnostics, not evidence of missing final bibliography entries.

| Preserved evidence | SHA-256 |
|---|---|
| `build/natural-20260909-r0/pdflatex-1.stdout.log` | `efe3e9439a892432a52e4d1da8fe7566fdf74b46eb157a5bbb6cef960a74deeb` |
| `build/natural-20260909-r0/work/main.log` | `c65328c029f3d14dc2134c3f16ef7a46bd7b3eecf6298c5ed388455be4d8cef8` |
| `build/natural-20260909-r0/work/main.fls` | `c92d77a1033ad0b3a41387360432548958e66adad1cbfbaa3666ee4502b5f4a6` |

## 2. Diagnosed cause and exact successor changes

The cases row separator immediately precedes the interval `[1,5]`.
TeX reads that bracket group as the optional dimension of the row separator,
giving “Illegal unit of measure (pt inserted)”. The interval is mathematically valid.
V3 adds an empty group between the row separator and interval to terminate that
optional-argument scan. No interval endpoint, hypothesis or mathematical symbol changes.

The same actual log identifies a 50.51622pt overfull paragraph in §5:69–77,
containing the original reduced-insertion equation. V3 puts that identical equation
in ordinary display math, without resizing it or changing its tokens.
Two minor pre-convergence warnings (9.96825pt in §3, 4.74084pt in §6) are retained
for assessment after successful convergence; their paragraphs are not changed speculatively.

The root read the entire actual V2→V3 recursive diff and both changed contexts.
Only §5 and §7 change; the other nine sources are byte-identical. The complete source
remains eleven files, with no scientific, coefficient-ring, scope, font, margin,
spacing, numbering, reference or bibliography change. V1 and V2 remain intact.
A targeted non-author check of these two actual edits has been assigned; it is not
a re-review of unchanged scientific inputs or a pre-grant of PDF acceptance.

## 3. V3 production input freeze before recovery

The [source checksum list](SOURCE_V3_20260909.sha256) is checked before execution
and again on the copy. Paths below are relative to `paper/v3/`.

| File | Lines | Bytes | SHA-256 |
|---|---:|---:|---|
| `macros.tex` | 9 | 327 | `b4831759010e67ff47811ba1346c0a8aea47d0e2fc1bfa6e3f8312828b6b5dc3` |
| `main.tex` | 62 | 2533 | `1d1a47776586fc72aa7041eaaf1098615b4bb1adc373f62546cbf71d6b6679b4` |
| `references.bib` | 183 | 5779 | `418530c0bc71f2fbbf5aa0e65b8d2c984c5c68f7fca9dcbb65c2fa84550ab0ba` |
| `sections/01-introduction.tex` | 300 | 13903 | `9b2876f36052d545ccf03a8309c4119f66ea06c3a9bbffa002e6228aa7610c0e` |
| `sections/02-surface-pencil.tex` | 446 | 20456 | `573a521e07117dc43b9291417469fa429701c67d711ec150a578b22c54205f8f` |
| `sections/03-spectral-jacobian.tex` | 435 | 19215 | `011c5415ac5d109c56cea3263ea9cad64db79a7f6102f12676c744bacb065b9b` |
| `sections/04-closed-hasse.tex` | 271 | 12079 | `68efcc6780280d7e06c107bc993fe4c431d8131b59f1f4f9e6b874dd96c6000e` |
| `sections/05-integral-trace.tex` | 246 | 10020 | `925b2bedcc8e942fb92797d9080b983f53010de97bc1676053390f8a5fc70ab0` |
| `sections/06-first-layer.tex` | 394 | 16381 | `f4232d918c4d78bacfc7c7a9dea2fbbe0aa60e634fbf27354d1708e02d84792d` |
| `sections/07-odd-jets.tex` | 468 | 18433 | `046f8cf808cc64de570605b316bcb5b0c6970f52492a585f97f97597ae2d74f5` |
| `sections/08-two-jets.tex` | 666 | 26100 | `5cfee2a607e6ff1ab52192bb5c9b1a73cef6635c3e5dcfe26aa73fe1192b42a9` |

All source/publication/citation controls, actual tools, package identities, PDF metadata
controls, process flags and environment are the unchanged ones bound by the original
pre-execution protocol (SHA-256
`24a734ad9b6b8116f54cf9969cd3dbcb81844a21eddd6a14b5fdc1986c0c9223`).

## 4. Exact recovery-root protocol, not yet an outcome

From the project directory, with bash fail-fast execution:

```bash
test ! -e build/natural-20260909-r2
mkdir build/natural-20260909-r2
cp -a paper/v3 build/natural-20260909-r2/work
```

From that new `work/` directory, check:

```bash
sha256sum -c ../../../notes/SOURCE_V3_20260909.sha256
```

Run the same four command lines printed in the first-build protocol, in the same order,
with `set -o pipefail`, the exact fixed environment and the same root-relative stdout
log filenames. Only the work directory and complete source successor differ.
The source is not edited during execution. Stop at any actual failed process and retain it.

This is the permitted ordinary compiler/overflow recovery in a fresh r2 root,
not a repeat of the frozen failed r0 run. r1 is still absent and no deterministic second
build is pre-authorized by an aborted first pass. After the first successful complete
natural build, obtain actual body/reference counts. The 22–30-page contract and its
under/over-window stop remain unchanged; no page count has been inferred from the aborted log.
