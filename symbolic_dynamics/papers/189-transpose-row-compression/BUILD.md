# P189 build and artifact ledger

**State:** `ROUND2_DUAL_REVIEW_FREEZE`  
**Lifecycle:** `OWNER_AMBER / HOLD_EXTERNAL`

## Independent exact verifier

```text
command: PYTHONDONTWRITEBYTECODE=1 python3 code/verify_p189.py
result: PASS_INTERNAL
exact assertions: 5,336,613
complete matrix carriers: all 2^(n^2) matrices for n=1,...,4
largest complete box: 65,536 matrices; every target at times one and two
partition/depth transfer: n=1,...,12
conjugation and inverse-mass transfer: n=1,...,9
counterexample attack: PASS (F^2 != F and F^3 != F witnesses found)
canonical lines/bytes: 35 / 2,224
canonical SHA-256: 9474855682c21a356876b12aef70d8cc12af929bb5846b3c259a4f037048ef25
two fresh verifier processes: byte-identical to canonical
```

## Deterministic PDF build

```text
SOURCE_DATE_EPOCH=1704067200
TZ=UTC
FORCE_SOURCE_DATE=1
pdflatex; bibtex; pdflatex; pdflatex
result: PASS
pages: 4
bytes: 363,099
page box: A4, 595.276 x 841.89 pt
PDF version: 1.5
PDF SHA-256: 6ba00f6b542fdbefd4789e8f23f2d683c642132e989ff7af828436da063d6a81
Round-0 copy byte-identical: yes
two source-only cold builds byte-identical: yes
font rows embedded/subsetted/Unicode: 29/29/29
encrypted: no
forms: none
JavaScript: no
identifying metadata fields: blank
warnings/bad boxes/unresolved references or citations: 0
```

Frozen core hashes:

```text
c9c4417012fcc9663ac3c3ac3fe9f5113fdf4fe4213846d2a6815b7657724457  main.tex
fbed4d833c2855548bc721b793ad74da2e5fcf994fccbc35e2fdbae74bb1ac4c  references.bib
b87fde66e16b164544eb6bc0463e4b4d4e82fae8531b43c322cbb96df0db7a5c  code/verify_p189.py
9474855682c21a356876b12aef70d8cc12af929bb5846b3c259a4f037048ef25  code/CANONICAL.txt
6ba00f6b542fdbefd4789e8f23f2d683c642132e989ff7af828436da063d6a81  main_round0_original.pdf
```

## Review closure

Review A used row-support sets, indegree peeling, reverse BFS, and direct
one-step/two-step target reconstruction to make 1,493,113 exact assertions and
closed with zero findings. Fresh Review B instead represented matrices as
column-bit tuples, reconstructed the literal map from row sums, and used
memoized orbit-repeat detection plus independent partition and mass controls.
It made 1,493,195 exact assertions and also closed with zero findings.

No source or PDF change was requested in either review. `main_round1.pdf`,
`main_round2.pdf`, and the live `main.pdf` all retain the Round-0 SHA-256
`6ba00f6b542fdbefd4789e8f23f2d683c642132e989ff7af828436da063d6a81`.
Terminal QA on 2026-09-04 completed two physical source-only cold builds,
final manifests, and byte-identical author/reviewer replays. External
lifecycle remains `OWNER_AMBER / HOLD_EXTERNAL`.
