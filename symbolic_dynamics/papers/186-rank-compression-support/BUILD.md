# P186 build and immutable-round ledger

**State:** `ROUND2_DUAL_REVIEW_FREEZE`  
**Lifecycle:** `OWNER_AMBER / HOLD_EXTERNAL`

## Exact verifier

```text
command: PYTHONDONTWRITEBYTECODE=1 python3 verify_p186.py
result: PASS
exact assertions: 12,104,596
complete carriers: every subset through n=18
largest box: 262,144 states; all times 0,...,18
canonical lines/bytes: 22 / 2,757
canonical SHA-256: e73a433e8dae091a04b743ee2b27a039964797d296dd1dc9b8cec2e767ba57dd
second fresh replay: byte-identical
```

## Deterministic PDF build

```text
SOURCE_DATE_EPOCH=1704067200
TZ=UTC
pdflatex; bibtex; pdflatex; pdflatex
result: PASS
pages: 3
bytes: 306,253
page box: A4, 595.276 x 841.89 pt
PDF version: 1.5
PDF SHA-256: 6c85285c7c2f5fb96b9558de3b77e784a079bde08cc9ad23ec3139f17c676431
Round-0 copy byte-identical: yes
font rows embedded/subsetted/Unicode: 24/24/24
encrypted: no
forms: none
JavaScript: no
identifying metadata fields: blank
warnings/bad boxes/unresolved references or citations: 0
```

Frozen source hashes:

```text
f44a1fa0119ff853991d737b72a345e0a60266bf7438c947bf5b61bb61a525aa  main.tex
63066317db03a7e7ad89c11cbe1883d290c3bb7d9769a68931c629a18e5d9c58  references.bib
dc437bcc6f48caa3a9c1f03702770f3c0bbbdae0501a7fa400f1488b48dd9bbc  verify_p186.py
e73a433e8dae091a04b743ee2b27a039964797d296dd1dc9b8cec2e767ba57dd  CANONICAL.txt
6c85285c7c2f5fb96b9558de3b77e784a079bde08cc9ad23ec3139f17c676431  main_round0_original.pdf
```

The corrected fibre upper limit was compiled before the Round-0 copy was
frozen.  This is an artifact/build receipt, not an independent paper review.

## Terminal receipt

Review A requested two abstract repairs: say that a gap contributes `g-t`
exactly when `g>t`, and restrict the unique depth-`n-1` state to `n>=2`.
The repaired source has SHA-256
`e7f407c5200e2e308885d61bd1328c8e3d20f57e50f219ab5ad104609cee0394`;
Round 1, Round 2, and live PDF share SHA-256
`449ddc9983cec9618e8a7cead63730d3ed29e1dbb5f36a630948eac3618f2b48`.
Review B found no further issue.  Two physical source-only builds reproduce
the final bytes.
