# C193 results

## Exact evidence

- Evidence payload SHA-256:
  `80c9bffcb3d520fe760af9fd682c1d8c05743cd8a4f8f8252fd459d45da2b4b6`.
- Evidence file SHA-256:
  `39a46bbfd4375c7e01571f18551f69b256f8d09c9b2fc522ba1c4ebd58f53e25`.
- Evidence bytes: 402,099.
- Quotient-tree rows: 513 through depth ten, with all 512 one-step
  frontier children retained in their depth-ten parent rows.
- Vieta-invariance tests: 1,539; largest stored coordinate: 56 digits.
- Independent bounded solutions: all 15 normalized solutions with largest
  coordinate at most 2,000.
- Complete descent traces: 19, containing 107 strict descent steps.

The level population is
`1,1,1,2,4,8,16,32,64,128,256` from depths zero through ten.  The
finite table is a regression oracle with an open depth-eleven frontier, not a
finite truncation proof of the all-solution theorem.

## Verification

- Independent checker: 8,417 assertions.
- Separate SymPy reconstruction: 8,418 checks.
- Canonical replay: 402,099 bytes, exact.
- Mutation suite: 156 repaired-hash rejections and one stale-hash rejection.
- Final PDF: 2 pages, 130,852 bytes, SHA-256
  `7dd5274a024a51df47bbcb67e57e8efbae0b672ee76c3a1ddf73ce96e1f42b06`.

## Verdict

The all-positive permutation-quotient graph has a source-attributed global
generation theorem and a derived unique terminating parent orientation.
Strict descent excludes every non-root periodic orbit.  The Frobenius
uniqueness conjecture and all mod-prime dynamics remain outside the claim.
Route verdict:

`A0_WEAK_ARITHMETIC_RELATION / A1_FAIL / A2_FAIL / A3_FAIL /
A4_FORMAL_HINT`, overall `ROUTE_A_REJECTED`, Route B false.
