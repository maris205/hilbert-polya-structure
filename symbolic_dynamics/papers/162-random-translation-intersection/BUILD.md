# P162 build and exact-control record

**Artifact:** Random Translation Intersection  
**Format:** anonymous `amsart`, A4, 10 pt, 27 mm margins  
**Lifecycle:** `HOLD_EXTERNAL`  
**Review state:** `ROUND-2 INTERNAL ACCEPT`; both independent hostile-review
rounds are complete and the artifact remains `HOLD_EXTERNAL`.

## Exact verifier

Command:

```bash
python3 code/verify.py
```

| Check | Result |
|---|---|
| Standard-library / external imports | standard library only / none |
| Assertion count | 1,712,974 |
| Status | `PASS` |
| Row digest printed by verifier | `c70d262c1d3752d23ee680a653c2e475ac5a57f6bd6491bf088bb7a9934cf02f` |
| Canonical transcript SHA-256 | `c31ec0a098bab52241eb2765bd6fef0669fdacdb4486ca69bea9dfc56fbab62b` |
| Fresh replay comparison | byte-identical, 2/2; a later direct replay also matched `CANONICAL.txt` |

The exact atlas compares literal iteration with independently evaluated span
erosion for all source/history pairs in the following boxes:

```text
d=0, t=0..6
d=1, t=0..8
d=2, t=0..6
d=3, t=0..4
```

It compares every target and source-size coefficient with the theorem.  It
also brute-counts ranks through `d=4,t=5`, checks all 2,825 subspaces at
`d=6` for the sharp witness, classifies universal fixed states through
`d=4`, and exercises 32,907 odd-cardinality targets with trivial stabilizer.
This is finite falsification evidence, not an all-parameter proof.

## Settled paper build

Toolchain:

```text
pdfTeX 3.141592653-2.6-1.40.22 (TeX Live 2022/dev/Debian)
BibTeX 0.99d (TeX Live 2022/dev/Debian)
```

Settled sequence:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The retained logs are `build_pdflatex_1.log`, `build_bibtex.log`,
`build_pdflatex_2.log`, and `build_pdflatex_3.log`.  The settled log contains
zero LaTeX/package warnings, errors, undefined citations or references, rerun
requests, overfull boxes, or underfull boxes.  BibTeX resolves 4/4 entries and
reports no warning or error.

Two fresh temporary directories received only `main.tex` and
`references.bib`.  Both completed the settled sequence and produced a PDF
byte-identical to the paper-local `main.pdf`.  Their final-pass logs are
retained as `build_cold1_settled.log` and `build_cold2_settled.log`.

Final-batch integrity audit on 2026-09-03 found that the two filenames had
still contained pre-repair final-pass logs reporting a 399,817-byte PDF.
The builds were rerun independently from the Round-2 source and the stale
logs were replaced with the two current final-pass logs.  Both now report
399,828 bytes and their PDFs match the Round-2/current SHA-256 below byte for
byte.  This repair changes build evidence only, not source or mathematics.

## PDF record and inspection

| Check | Value |
|---|---|
| File | `main.pdf` |
| Pages / format | 4 / A4 (`595.276 x 841.89 pt`) |
| Size | 399,828 bytes |
| SHA-256 | `730c4a57cb1c3f787c0cc8b142d4dbf62da4d2b06bc1c42d5c30d00eb8e20b62` |
| Fonts | 30 rows; all embedded, subsetted, and Unicode mapped |
| Encryption / forms / JavaScript | none / none / none |
| Metadata title / author / subject / keywords | blank / blank / blank / blank |

All four pages were rendered at 120 dpi and visually inspected.  No clipping,
overlap, broken glyph, bad equation break, illegible reference, or running-head
collision was found.  Text extraction contains the anonymous byline and the
visible `HOLD_EXTERNAL` sentences, with no email, affiliation, personal name,
local path, or editorial marker.

## Frozen source hashes

```text
6e04aa91ac0befb9bfa06567be8cfbdb068a7bcbd2d46502a1030e053848cf04  main.tex
db620e6954f54081fe8a2fa59045251e5ee16c8858b2c92fdcf031dd549d04e8  references.bib
3b05be5e204503365e4cbb88c0fc7e580fe4a460966e5b1714ecbb8a4f8ea8de  code/verify.py
c31ec0a098bab52241eb2765bd6fef0669fdacdb4486ca69bea9dfc56fbab62b  code/CANONICAL.txt
```

The source hash above describes the pre-review author draft.  The current
Round-2 source SHA-256 is
`98b54a3052dccb6168655e8f337921eef76547c73005d847338eb69fd5454e1d`;
the only review repair was the Review-A abstract qualifier recorded in
`IMPROVEMENT_LOG.md`.  Review B requested no further change.  Its independent
verifier executed 2,275,862 assertions, and two source-only cold builds
reproduced the Round-1/2 PDF byte for byte.  This is not an external release
manifest.

## Preserved review artifacts

| round | PDF SHA-256 | disposition |
|---|---|---|
| Round 0 | `e496ce1be3084e61616494cab2ca405238adfa575a6484db93029f8dae01de46` | author artifact preserved |
| Round 1 | `730c4a57cb1c3f787c0cc8b142d4dbf62da4d2b06bc1c42d5c30d00eb8e20b62` | Review-A minor repaired |
| Round 2 / current | `730c4a57cb1c3f787c0cc8b142d4dbf62da4d2b06bc1c42d5c30d00eb8e20b62` | Review B accepted 0/0/0 |

`main.pdf` and `main_round2.pdf` are byte-identical.  Review-B proof, owner,
verifier, and PDF-QA evidence is frozen under
`docs/papers162_166_sequence/reviews/p162_b/`.
