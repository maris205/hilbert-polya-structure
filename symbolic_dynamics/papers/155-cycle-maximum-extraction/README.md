# P155 — cycle-maximum extraction

Status: **ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL**.

The paper studies the rank-changing map that orders the disjoint-cycle
supports of a permutation by their minima, reads their maxima, and
standardizes.  Its frozen contribution ceiling has three exact axes:

1. the target threshold `mu(sigma)=2m-rlmin(sigma)` and a constructive right
   section at every admissible source rank;
2. every-target fibres as ordered-support sums weighted by
   `prod_i (|B_i|-1)!`; and
3. identity-only recurrence with strict rank drop off the identities.

The observed power-of-two absorption clock is explicitly **not claimed**.
Static cycle maxima, cycles ordered by minima, and opener/closer endpoint
technology are cited and fully subtracted.

## Reproduce the exact control

```bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_p155.py
PYTHONDONTWRITEBYTECODE=1 python3 verify_p155.py > /tmp/p155_replay.txt
cmp -s /tmp/p155_replay.txt verification_output.txt
```

The frozen run checks 4,037,913 literal states through rank ten and executes
16,473,121 exact assertions.  Enumeration is counterexample pressure, not an
all-parameter proof or a novelty/ownership certificate.

## Rebuild

```bash
pdflatex -interaction=nonstopmode -halt-on-error main.tex
bibtex main
pdflatex -interaction=nonstopmode -halt-on-error main.tex
pdflatex -interaction=nonstopmode -halt-on-error main.tex
```

`main_round0_original.pdf` preserves the author freeze, and
`main_round1.pdf` preserves the Review-A repair freeze. Hostile Review B
returned `ACCEPT_INTERNAL — 0 Critical / 0 Major / 0 Minor`; it requested no
manuscript change. `main.pdf`, `main_round1.pdf`, and `main_round2.pdf` are
byte-identical, 4 A4 pages and 345,390 bytes, at SHA-256
`54fb1fb0a2519950d3b5725ea5e02c09eb89de13048bf7a97c62d41a9f99ebd1`.
Hostile Review A's two Minor findings are closed in `IMPROVEMENT_LOG.md`;
Round 2 is the accepted byte-identical freeze. Nothing in this directory
authorizes posting, submission, circulation, specialist contact, or any other
external action.
