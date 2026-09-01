# Round-1 build and artifact audit

**Date:** 2026-09-01 UTC
**External status:** `HOLD_EXTERNAL`

## Canonical verifier replay

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p145.py | \
  cmp - verification_output.txt
```

Result: `cmp=0`.  The frozen transcript ends with

```text
exact_assertions=155901
status=PASS
external_status=HOLD_EXTERNAL
```

The recovery routine receives only `(n,Q)`.  The canonical run covers 28,628
input-only recoveries, 624,834 exact candidate division attempts, and 144,024
successful factor peels.

## Settled manuscript build

`latexmk` is unavailable, so the equivalent explicit protocol was used:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

All four stages exited zero.  The settled `main.log` and `main.blg` contain no
LaTeX/package warning, overfull or underfull box, undefined citation or
reference, multiply defined label, or actionable rerun request.  All six
bibliography entries are cited.

## Isolated reproducibility build

Only `main.tex` and `references.bib` were copied to the fresh directory
`/tmp/p145-round1-isolated.OxKSB5` and rebuilt with the same four commands.
The isolated build exited zero, its settled warning scan was empty, and its
PDF compared byte for byte with the paper-local `main.pdf` (`cmp=0`).

## PDF and visual audit

```text
pages=5
page_size=A4 (595.276 x 841.89 pt)
file_size=394974 bytes
pdf_version=1.5
encrypted=no
forms=none
javascript=no
pdf_author_metadata=blank
pdf_title_metadata=blank
visible_author=Anonymous
font_rows=30
nonembedded_fonts=0
```

All five pages were rendered at 120 dpi and inspected.  There is no clipping,
collision, malformed display, unreadable table, orphaned heading, or broken
reference.  Page five contains the six verified references and intentional
residual whitespace.  No figure is present; `PAPER_PLAN.md` records the
formula-only decision.

## Round preservation

- `main_round0_original.pdf` remains byte-identical to the original author
  artifact and was not overwritten.
- the round-1 build is preserved as `main_round1.pdf`;
- current `main.pdf` is the distinct accepted round-2 build recorded below.

## Frozen hashes

```text
ebd0606e9650eb363511387c0954c084cb41a8587049cca63706de5672bd3949  main.tex
6e261188f0784f18bc1bb1f9c40efa873e4272bb9412e34e40801119d57aa7b7  references.bib
8ddc8bda503147a72778fc501dc3d6aa535ce7503edd5b72df6d0d21cd81f65a  verify_p145.py
89aaeddaa2cfc8c66a1d05681e3ef3115f7b13bca665a894b1a48aa2f5df92d9  verification_output.txt
aed3fcd367940666cc2b5489f83ac1d54a72a60e6351ccd4b9d34c73117eeb14  round1 build (then main.pdf)
abf75d832a1bd874ce31155d8c71e55e8cf3bb23f17029b82b6a88e645a49dea  main_round0_original.pdf
aed3fcd367940666cc2b5489f83ac1d54a72a60e6351ccd4b9d34c73117eeb14  main_round1.pdf
```

These hashes establish artifact identity only.  They do not provide novelty,
priority, owner clearance, or external-release authority.

## Accepted round-2 freeze

- Hostile review B: `ACCEPT`, with 0 critical, 0 major, and 1 nonblocking
  bibliographic minor; the minor was closed before freeze.
- Result: 5 A4 pages, 395,143 bytes, with 6/6 cited references.
- Current and `main_round2.pdf` SHA-256:
  `39b806e687bcd223fb4182f7c0bbe9b16cdeb270595db1925279f04b6e024569`.
- Historical `main_round0_original.pdf` and `main_round1.pdf` remain distinct
  at their recorded hashes.
- Canonical replay: 155,901 assertions and byte-identical transcript.
- Source-only isolated build in `/tmp/p145-round2-9YbxQk` is byte-identical to
  current `main.pdf`; the settled logs contain no substantive warning,
  undefined citation/reference, bad box, or rerun request.
- The primary journal author spelling/locator and the exact-integral-division
  proof sentence are present in the final source and PDF.
- No paper-local Git operation was performed; external status remains
  `HOLD_EXTERNAL`.
