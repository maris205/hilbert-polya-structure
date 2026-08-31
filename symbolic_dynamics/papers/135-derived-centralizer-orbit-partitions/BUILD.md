# Build record

## Round-0 isolated build

Date: 2026-08-31 UTC.

Only `main.tex` and `references.bib` were copied into the fresh directory
`/tmp/p135-round0-26pXwk` and built in four stages:

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

| stage | status |
|---|---:|
| pdflatex 1 | 0 |
| bibtex | 0 |
| pdflatex 2 | 0 |
| pdflatex 3 | 0 |

The settled log and BLG contain no LaTeX/package warning, overfull or
underfull box, undefined citation/reference, multiply-defined label, or
actionable rerun request.  All four cited keys have matching `bibcite`
records.

## PDF audit

```text
pages=5
page_size=A4 (595.276 x 841.89 pt)
file_size=394566 bytes
fonts=31
nonembedded_fonts=0
pdf_sha256=7cd8a811a9d879e303c3d7a0b1bd6631aa24d9fc64704df62b4a369ce327505b
round0_sha256=7cd8a811a9d879e303c3d7a0b1bd6631aa24d9fc64704df62b4a369ce327505b
main_vs_round0_cmp=0
```

All five pages were rasterized and visually inspected.  No clipping,
collision, malformed formula, or orphan bibliography page was found.
The control table floats to the top of page 5 between the final ownership
paragraph's last two lines; this is readable and not a rendering failure,
but is retained as a low-severity editorial layout risk for a later review
round.  `pdfinfo` reports blank Title, Subject, Keywords, and Author
metadata.  The visible author is `Anonymous`.

## Frozen source and control hashes

```text
386b0cbca5cf812599687df39e3db43ee0edb47cb500f7718742b9badf0cb273  main.tex
515faec4ab071ecf7c68bf65c5bb721867eeea912ef30a57c7b41f9e4402baae  references.bib
26b87846c87dd671f709f90e9945f5724b3f6deac959f2619a73078721f0313a  code/verify.py
be50b73c6c3c17c6378d141bc6c594388512241b8acb9b6e7b877b470070ba90  code/verification_output.txt
7cd8a811a9d879e303c3d7a0b1bd6631aa24d9fc64704df62b4a369ce327505b  main_round0_original.pdf
```

Round 0 is frozen and must not be overwritten.  External status is
`HOLD_EXTERNAL`.

## Round-1 repaired build

Review A's three minor boundary/traceability/layout findings were implemented
in `main.tex`, `PAPER_PLAN.md`, and `CLAIMS_EVIDENCE.md`.  Fresh verifier
stdout remained byte-identical to the 7,130,840-assertion canonical
transcript.  A four-stage isolated build in `/tmp/p135r1iso.ClVjhD`
reproduced `main.pdf` byte for byte.

```text
pages=5
file_size=395335 bytes
main_round1_sha256=dbf3a7ff19d1ddd2bcde59b35287835ffa8dec3b4244c53e65e87fc14a2b1b94
main_tex_sha256=cd8ea8a0d077b9619adf8b8d7e172757a5262d2f24a9060c98c92f0ad87ae149
main_vs_round1_cmp=0
round0_preserved_sha256=7cd8a811a9d879e303c3d7a0b1bd6631aa24d9fc64704df62b4a369ce327505b
```

The settled log has no warning, bad box, undefined citation/reference, or
error.  All 31 font rows pass.  Page 5 now begins with the continuation and
completion of the ownership/control paragraph, followed by the control table
and references; the former table splice is closed.  All pages remain legible
and anonymous.  External status remains `HOLD_EXTERNAL`.

## Round-B provenance closure

Round B requested only a support-ledger hash relabel.  Direct current hashes
remain:

```text
cd8ea8a0d077b9619adf8b8d7e172757a5262d2f24a9060c98c92f0ad87ae149  main.tex
dbf3a7ff19d1ddd2bcde59b35287835ffa8dec3b4244c53e65e87fc14a2b1b94  main.pdf
dbf3a7ff19d1ddd2bcde59b35287835ffa8dec3b4244c53e65e87fc14a2b1b94  main_round1.pdf
7cd8a811a9d879e303c3d7a0b1bd6631aa24d9fc64704df62b4a369ce327505b  main_round0_original.pdf
```

No rebuild was necessary because no compilable input changed.
