# Build and Verification Record

Build date: 2026-09-04 UTC.

Gate: `OWNER_RED_AMBER/HOLD_EXTERNAL`.

## Environment

```text
Linux 5.15.0-78-generic x86_64 GNU/Linux
Python 3.12.3
g++ (Ubuntu 11.4.0-1ubuntu1~22.04) 11.4.0
pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian)
BibTeX 0.99d (TeX Live 2022/dev/Debian)
```

`latexmk` and `qpdf` were not installed. The build therefore used explicit `pdflatex`/`bibtex` passes. PDF structure/readability checks used `pdfinfo`, `pdffonts`, `pdftotext`, and `pdftoppm`.

## Canonical finite checks

The principal verifier was replayed repeatedly with the exact contract requested:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 code/verify.py | cmp - code/CANONICAL.txt
```

Final replay status: exit 0, no diff. A representative shell timing was 10.268 s wall, 10.214 s user, and 0.056 s system; timing is informational, not a benchmark.

Canonical Python summary:

```text
transitions=280392
assertions=1962920
record_digest=67cc231e1e1ad859aca4c6de30f7a3dd76f81358ff2753b48bbdac06662cad24
theorem_status=history_law_verified_n_le_8_not_claimed_all_n
status=PASS
```

The independent (n=9) stream was compiled and replayed as:

```bash
g++ -std=c++17 -O3 -Wall -Wextra -pedantic code/verify_n9.cpp -o /tmp/p192_verify_n9
/tmp/p192_verify_n9 | cmp - code/CANONICAL_N9.txt
```

Final replay status: exit 0, no compiler warnings, no transcript diff. It streamed all 4,782,969 Prüfer words and checked all 128 history masks. Two raw-output runs were byte-identical. Representative timings were 3.403 s and 3.399 s wall for the raw runs; the final `cmp` replay was 3.420 s wall. The transcript explicitly says `conjecture_status=n9_verified_not_claimed_all_n`. This is finite conjecture evidence, not part of the all-(n) theorem proof.

## Deterministic cold compile

Two fresh directories made by `mktemp -d` received only `main.tex` and `references.bib`. Each ran:

```bash
export TZ=UTC
export SOURCE_DATE_EPOCH=1788480000
export FORCE_SOURCE_DATE=1
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

`SOURCE_DATE_EPOCH=1788480000` is 2026-09-04 00:00:00 UTC. The two Round-0 cold PDFs compared byte-for-byte equal with `cmp`. After the accepted Review-A repair, a fresh source-only build and an independent reviewer cold build again produced the same current PDF byte-for-byte. The generated final log contains no LaTeX warning, overfull/underfull box, undefined citation/reference, or multiply-defined-label match.

Immutable Round-0 PDF data:

```text
file: main_round0_original.pdf
pages: 3
page size: 595.276 x 841.89 pt (A4)
PDF version: 1.5
bytes: 321493
SHA-256: aa0ade6d64cb2cbd87545bde50ed15ba2b9729e3235aa7395b4be892b1cb76f1
fonts: 25 listed fonts, all embedded; all listed fonts subsetted
encrypted: no
JavaScript: no
```

Those data describe the immutable `main_round0_original.pdf` baseline. The
current repaired `main.pdf` has the following data:

```text
pages: 4
page size: 595.276 x 841.89 pt (A4)
PDF version: 1.5
bytes: 323972
SHA-256: e06aac2579f0d90a15c1a7a2c8fa09ce57286f15818a10c2466cd06d210d6b57
fonts: 25 listed fonts, all embedded, subsetted, and Unicode-mapped
encrypted: no
JavaScript: no
```

All three Round-0 pages and all four repaired pages were rasterized and
visually inspected. No clipping, overlap, blank page, malformed equation, or
bibliography overflow was observed.

## Frozen input and transcript hashes

```text
30cd2c9bc853d9b195f89527db4794681e4d3dcacd8c45f5aea0b49a98ab12f9  main.tex
70d17104f92450aaca7c1322f96b5343d975fef7f6becef726c514642768cdd5  references.bib
c8bc72dd399cc57dd8cc6f153975853d2fb53cf0005c25b7dc283a6fe2e05cce  SOURCE_VERIFICATION.md
6cedec783fe521867eba84dbaa7c636b1239bc60199b3a958c91ac2edf1409b3  code/verify.py
1368a122f0ee04e0ea7211e7fb9841ce6d55ba380780651186ce0d1953216d3c  code/verify_n9.cpp
d84874a28136b812aa87ea630c4453b259501cb8c698d3c1c388a88501d77f36  code/CANONICAL.txt
be04390b272bccefdaca143c49172bf005c685d8f9335400da496dacd78650d6  code/CANONICAL_N9.txt
e06aac2579f0d90a15c1a7a2c8fa09ce57286f15818a10c2466cd06d210d6b57  main.pdf
aa0ade6d64cb2cbd87545bde50ed15ba2b9729e3235aa7395b4be892b1cb76f1  main_round0_original.pdf
220b3e2f5111f83c23bc29608472eab858e6369dbbdf13dbbef85b1c542098e0  main_pre_metadata_audit.pdf
```

The current `main.tex`, bibliography, source audit, and `main.pdf` incorporate
the accepted Review-A source/domain repair. `main_round0_original.pdf` remains
the immutable Round-0 pin and is intentionally not byte-identical to current
`main.pdf`. The PDF present before the initial metadata cleanup was renamed
`main_pre_metadata_audit.pdf`; it is noncanonical because its rendered
bibliography contains superseded metadata.

## Round-0 bibliography delta

Only `references.bib` was corrected:

- Stanley 1997 DOI corrected to `10.37236/1335`;
- Irving--Rattan corrected to European Journal of Combinatorics 93 (2021), article 103257, DOI `10.1016/j.ejc.2020.103257`;
- Stanley, *Enumerative Combinatorics*, Volume 2 DOI corrected to `10.1017/9781009262538`;
- Gorsky--Gorsky changed from unsupported Moscow Mathematical Journal coordinates to the verified arXiv:1112.0381v2 preprint record.

The first three cold-build attempts exposed and then resolved the Gorsky metadata/line-breaking issue; the final two fresh Round-0 builds are the recorded baseline pair. No mathematical source line changed in that metadata pass.

## Review-A repair delta

The repaired manuscript adds the Campion Loth--Rattan 2025 source and
zero-credits its deterministic conditional Hurwitz/string-reordering
mechanism, while distinguishing its convention, scheduler, objective, and
theorem output. It also makes the domain `n>=2` explicit and separates the
`n>=3` sharp witness from the sole `n=2` fixed state and its indegree-one
self-fibre. These repairs do not change the four proved axes, promote the
history conjecture, or relax `OWNER_RED_AMBER/HOLD_EXTERNAL`.

## Rebuild acceptance criteria

A future rebuild passes only if:

1. both `cmp` commands exit zero;
2. the Python transcript still says `history_law_verified_n_le_8_not_claimed_all_n`;
3. the C++ transcript still says `n9_verified_not_claimed_all_n`;
4. the final TeX pass has no fatal error or unresolved citation/reference;
5. current `main.pdf` opens as four nonblank A4 pages and the immutable Round-0 pin remains three pages;
6. no document promotes the history law or the owner status.
