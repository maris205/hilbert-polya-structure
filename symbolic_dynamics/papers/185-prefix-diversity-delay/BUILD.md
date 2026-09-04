# P185 build and immutable-round ledger

**State:** `ROUND2_DUAL_REVIEW_FREEZE`  
**Lifecycle:** `OWNER_AMBER / HOLD_EXTERNAL`

## Exact verifier

```text
command: PYTHONDONTWRITEBYTECODE=1 python3 verify_p185.py
result: PASS
exact assertions: 10,430,175
complete carriers: all n^n words for n=1,...,7
largest box: 823,543 states; all relevant times
canonical lines/bytes: 11 / 680
canonical SHA-256: 8caaa2ca1ff4329d0c5b03d84d127c6ef7e060cd6c19a3314a8cd879130975ac
second fresh replay: byte-identical
```

## Deterministic PDF build

```text
SOURCE_DATE_EPOCH=1704067200
TZ=UTC
pdflatex; bibtex; pdflatex; pdflatex
result: PASS
pages: 3
bytes: 272,526
page box: A4, 595.276 x 841.89 pt
PDF version: 1.5
PDF SHA-256: 45a2ce36879d17dafb42fd4a08c2afbc6213c8c140ffdee145f4e27f4c8a9129
Round-0 copy byte-identical: yes
font rows embedded/subsetted/Unicode: 22/22/22
encrypted: no
forms: none
JavaScript: no
identifying metadata fields: blank
warnings/bad boxes/unresolved references or citations: 0
```

Frozen source hashes:

```text
a1fa39c5e83bba76af2100fdf27209414fdfb1c56bd7da36e6397c0a33657185  main.tex
79eddaa65b328390d8e3b4c3a8522f38523a8aa6bf7f75bd95c38f287dc0fc19  references.bib
4df99a117b6b30e2fbe91dff263fb1d86e016fb7de1090b7f0492fcee0c79cb4  verify_p185.py
8caaa2ca1ff4329d0c5b03d84d127c6ef7e060cd6c19a3314a8cd879130975ac  CANONICAL.txt
45a2ce36879d17dafb42fd4a08c2afbc6213c8c140ffdee145f4e27f4c8a9129  main_round0_original.pdf
```

The metadata integrity gate caught and corrected the
Mansour--Vajnovszki issue number from 16 to 17 before this PDF and Round-0
copy were frozen.  This is an artifact/build receipt, not an independent
paper review.

## Terminal receipt

Review A requested one scope repair: restrict the transient image/CDF formulas
to `1<=t<=n-1` and state the `t=0` and stabilized fibre cases explicitly.
The repaired source has SHA-256
`e17e073a15d839a3178bc5ed922227bd24cea41d4c6ceff4e6066090651da6f6`;
Round 1, Round 2, and live PDF share SHA-256
`fcd6257debd3a3e8744571a390296fe02566cc6655957011778400582bea03c3`.
Review B found no further issue.  Two physical source-only builds reproduce
the final bytes.
