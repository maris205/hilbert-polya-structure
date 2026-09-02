# P158 improvement log

**Current state:** `ROUND-2 INTERNAL ACCEPT / HOLD_EXTERNAL`.

## Immutable baseline

`main_round0_original.pdf` remains the byte-exact pre-review freeze:

- 4 A4 pages, 352,360 bytes;
- SHA-256 `bbe961298aa62adc54d34f15cc546ff3f14d7d4d29fd90dee2dcc6e2fff2e892`.

## Hostile Review A disposition

Review A returned `REVISE — 0 Critical / 0 Major / 2 Minor`.

1. **m1, multiplication separator — fixed.**  The mandatory `n=5,t=2`
   display now reads `(2)_2 2^2 A_0(1)=0` with an explicit TeX multiplication
   space rather than a comma.  The formula and conclusion are unchanged.
2. **m2, pathwise verifier independence — fixed by expansion.**  The author
   verifier now implements a literal epoch-by-epoch intersection beginning at
   `K_n` and compares it with a separately coded complement-word graph for
   every one of the 42,252 histories in the frozen cases before forming the
   fibre dictionary.  This adds 42,252 exact assertions and raises the total
   from 35,278 to 77,530.

The frozen transcript is now SHA-256
`3e69dfb7d0653c140f2945a6fe4888afc569756a25acf20c1e7eaf2d9f432f0d`;
two fresh runs reproduce it byte for byte.  No theorem statement, proof
argument, target formula, or parameter range changed.

## Round-1 build hygiene and artifact

Microtype protrusion is retained while expansion is disabled, removing the
previously disclosed font-expansion ordering notice.  This is a typesetting
repair only.  The settled Round-1 build has zero warnings, bad boxes,
undefined references, and rerun requests.

- `main.pdf` and `main_round1.pdf` are byte-identical;
- 4 A4 pages, 371,703 bytes;
- SHA-256 `2ec5779cb4b1c2f8515104c6114431df89155e8e3dfde7749a48ab113b9bb0d5`;
- all 28 reported font rows are embedded, subsetted, and Unicode mapped;
- all four pages were raster inspected after repair.

## Hostile Review B and Round 2

Review B returned `ACCEPT_INTERNAL — 0 Critical / 0 Major / 0 Minor`.  It
independently rederived every theorem interface, checked the `n=5,t=2`
sentinel by literal enumeration, verified both Review-A repairs in source and
PDF, replayed the 77,530-assertion verifier twice, and reproduced the PDF in
two source-only directories.  No further source change was required.

`main_round2.pdf` is therefore a no-change freeze of accepted Round 1 and is
byte-identical to both `main.pdf` and `main_round1.pdf`: 4 A4 pages, 371,703
bytes, SHA-256
`2ec5779cb4b1c2f8515104c6114431df89155e8e3dfde7749a48ab113b9bb0d5`.
Surviving severity is zero Critical, zero Major, and zero Minor.
