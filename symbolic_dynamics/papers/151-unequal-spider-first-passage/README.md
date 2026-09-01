# P151 — leaf-marked first passage on unequal finite spiders

Status: **ROUND-2 INTERNAL REVIEW ACCEPTED / HOLD_EXTERNAL**.

Hostile Review A returned 0 Critical / 1 Major / 3 Minor.  The generic
Sericola/Chen owner boundary, de la Iglesia--Juarez version of record,
exact-versus-independent wording, and `Q(0)/Q(1)/D(1)` bridge were repaired.
Independent Hostile Review B accepted the repaired package with 0 / 0 / 0
findings.

This short paper studies simple random walk started at the centre of a finite
spider with arbitrary positive integer arm lengths and absorbing labelled
leaves.  Its residual package is deliberately narrow: an explicit
unequal-spider continuant factorization of the generic leaf-marked law, a
compact scalar variance formula, sharp
fixed-total-length mean extremizers, and the precise coarse-data inverse
boundary.  General-tree endpoint/mean results, the published unequal-arm
endpoint exercise, equal-arm star laws, generic finite-chain time/place and
moment formulas, general-tree PGF algorithms, spider spectral methods, and
network tomography are explicitly subtracted.

## Reproduce the exact control

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p151.py
PYTHONDONTWRITEBYTECODE=1 python3 verify_p151.py > /tmp/p151_replay.txt
cmp -s /tmp/p151_replay.txt verification_output.txt
```

The frozen run contains 1,446,432 exact integer/rational assertions and ends
in `PASS`.  Enumeration is a falsifier, not a proof or novelty certificate.

## Rebuild the paper

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

`main_round0_original.pdf` freezes the first successful compiled draft.
The accepted current `main.pdf` and `main_round1.pdf` are byte-identical,
6 pages and 356,664 bytes, at SHA-256
`24fddbfb896510cf2712a8ade2a3ac37d04712676f635e39f1170c4cc334e8d9`.
Root will later archive the same accepted artifact as `main_round2.pdf`.
`PROOF_PACKAGE.md` records the derivation spine, `CLAIMS_EVIDENCE.md` separates
proof, exact pressure, and owner subtraction, and `HOSTILE_REVIEW.md` plus
`IMPROVEMENT_LOG.md` record the consolidated closure.

No file in this directory authorizes posting, submission, circulation, author
contact, or any other external action.
