# Round-1 build and artifact audit

## Environment and sequence

- Document class: `amsart`, 10pt, A4.
- Engine: pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/Debian).
- Bibliography: BibTeX 0.99d with `plainnat`.
- `latexmk` is unavailable, so the equivalent settled sequence was run from
  this directory:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The final `pdflatex` pass was repeated and compared byte for byte with the
preceding settled PDF; `cmp` returned 0.

## Preserved and round-1 artifacts

| Artifact | Role | SHA-256 |
|---|---|---|
| `main_round0_original.pdf` | frozen author-stage PDF, unchanged | `f30d0145385d226ac66b75c280db956672f714d27e1e3c65169e37273c8baf26` |
| `main_round1.pdf` | frozen post-owner-remediation round-1 snapshot | `24a483f852b5c2fd29e5acf8ccc19aafe218928d7b5efb247a640444e1ef050c` |
| `main.pdf` / `main_round2.pdf` | accepted current manuscript | `606a564462eb2d19ea48d00d5ade232fb7963133c422597a0d5b1f446eefc655` |

## Compilation result

| Check | Result |
|---|---|
| Build exit status | PASS |
| Total pages | 6 |
| PDF size | 328,154 bytes |
| Bibliography entries | 7 |
| Cited bibliography entries | 7 |
| Undefined references | 0 |
| Undefined citations | 0 |
| Multiply defined labels | 0 |
| Overfull boxes | 0 |
| Underfull boxes | 0 |
| Remaining LaTeX/BibTeX warnings | 0 |
| Fonts embedded | all |
| PDF author/title metadata | blank |
| Volatile PDF dates/trailer ID | suppressed |
| Encrypted/forms/JavaScript | no/no/no |

All six pages were rendered and inspected.  The new Pallo/Chapoton comparison,
plane-tree graft equation, suffix-lift paragraph, ownership subtraction, table,
and seven references are legible with no clipping or collision.  No figure is
required: the literal factor equation and its one-line ordered-tree conjugacy
display the complete move and inverse operation without an additional visual
claim.

## Exact control replay

```bash
PYTHONDWRITEBYTECODE=1 python3 verify_p144.py | cmp - verification_output.txt
```

`cmp` returned 0.  The canonical run remains unchanged and terminates with:

```text
TOTAL_STATES=290511
TOTAL_FIXED_TARGETS=82500
TOTAL_ASSERTIONS=6005502
STATUS=PASS
```

The round-1 changes concern sources, ownership allocation, explanatory carrier,
and planning only; the verified theorem formulas and verifier were not changed.

## Release boundary

Successful compilation, source verification, and exact replay establish
artifact integrity only.  The bounded owner search did not establish an owner
of the remaining temporal/target-fibre conjunction, but that non-hit is not
novelty or priority evidence.  The package remains **OWNER-THIN /
HOLD_EXTERNAL**.

## Accepted round-2 freeze

- Hostile review B: `ACCEPT`, with 0 critical, 0 major, and 1 nonblocking
  minor finding; the abstract-range wording was closed before freeze.
- Result: 6 A4 pages, 328,424 bytes, with 7/7 cited references.
- Current and `main_round2.pdf` SHA-256:
  `606a564462eb2d19ea48d00d5ade232fb7963133c422597a0d5b1f446eefc655`.
- Historical `main_round0_original.pdf` and `main_round1.pdf` retain their
  recorded, distinct hashes.
- Canonical replay: 6,005,502 assertions, transcript byte match.
- Source-only isolated build in `/tmp/p144-final-zDPch5` is byte-identical to
  current `main.pdf`; the settled log has no substantive warning, unresolved
  citation/reference, bad box, or rerun request.
- External status remains **OWNER-THIN / HOLD_EXTERNAL**.
