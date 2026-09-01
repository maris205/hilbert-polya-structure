# P147 — Adjacent-Run Consolidation

Status: **ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL**.

This is an anonymous internal theorem note.  Hostile Review A returned
0 Critical / 1 Major / 3 Minor; the ancestry proof, target typing, explicit
all-size witnesses, and closest-source subtraction were repaired.  Independent
Hostile Review B accepted the repaired package with 0 / 0 / 0 findings.

The literal self-map acts on positive compositions of a fixed total and
replaces every maximal run `s^r` simultaneously by `rs`.  The paper proves:

- the exact sharp clock `max tau=floor(log2 n)` for every `n`, with an
  explicit equality witness;
- absorption at adjacent-unequal (Carlitz) compositions; and
- the complete source-length-refined one-step fibre polynomial over
  adjacent-unequal divisor choices.

Classical Carlitz enumeration and static run statistics receive zero
contribution credit.  Random composition evolution, static adjacent-
restriction families, and the literal equal-run rule alone are also
subtracted.  The residual is the simultaneous self-map together with its sharp
all-size clock and complete target-resolved length-refined inverse.

## Reproduce

```bash
python3 verify_p147.py
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

The frozen exact transcript is `verification_output.txt`: its cold replay
passes 2,690,869 integer assertions byte for byte.  The initial pre-hostile-
review artifact is `main_round0_original.pdf`; the accepted current
`main.pdf` and proof/owner-repaired `main_round1.pdf` are byte-identical,
4 pages and 338,052 bytes, at SHA-256
`1d9c5ceb72891e1c509ebeb8adfdb23d110958f129ea7ae32d3c9d427253ce20`.
Root will later archive the same accepted artifact as `main_round2.pdf`.

`HOSTILE_REVIEW.md` and `IMPROVEMENT_LOG.md` give the consolidated closure.
No file in this directory authorizes posting, submission, circulation, author
contact, or any other external action.
