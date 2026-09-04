# P189 process-separated hostile Review B

## Verdict

`PASS / ZERO FINDINGS / ACCEPTED_NO_CHANGE / HOLD_EXTERNAL`

The frozen Round-1 package survives a fresh Review B.  No file in
`papers/189-transpose-row-compression/` was modified.  Round 0, Round 1, and
the live PDF remain byte-identical throughout this review.

## Frozen binding

- `main.tex`: `c9c4417012fcc9663ac3c3ac3fe9f5113fdf4fe4213846d2a6815b7657724457`
- `main_round1.pdf`: `6ba00f6b542fdbefd4789e8f23f2d683c642132e989ff7af828436da063d6a81`
- author verifier: `b87fde66e16b164544eb6bc0463e4b4d4e82fae8531b43c322cbb96df0db7a5c`
- author canonical: `9474855682c21a356876b12aef70d8cc12af929bb5846b3c259a4f037048ef25`
- Review-A canonical: `7fed29f8dd04c2493772596e788a9763222dc5a31d7be70ecdbef28e8d717139`
- reviewer verifier: `16dd9c0500bc350dec14cfe8c265ebc87b5182f621fb7796b9bb9ea102595a23`
- reviewer canonical: `95aa42c0b31c3d13fc9d893a92b45b0f1613929bb3beb6b6fc6b524539e8564d`

## Independent attack route

The reviewer replaces Review A's row-support graph analysis by labelled
row-bitmask degree-sequence calculus.  The dynamics are rebuilt through the
identities `F(A)=D(r)`, `F^2(A)=D(r^*)`, `F^3(A)=D(r^\downarrow)`, and
`F^4(A)=F^2(A)`, while time-one and time-two fibres are recomputed by
Ferrers-column and degree-multiset counting rather than full reverse-graph
search.

The control exhausts every `n x n` binary matrix through `n=4` and extends
the partition/coefficient checks through `n=12`.  It records
`exact_assertions=660870`, reopens the `F^2!=F`, `F^3!=F` witnesses, and
finds zero open finding.

## Finding ledger

- Critical: `0`
- Major: `0`
- Minor: `0`

Review B requests no manuscript change.  `main_round2.pdf` is therefore a
byte-identical Round-2 receipt, and `HOLD_EXTERNAL` remains active.
