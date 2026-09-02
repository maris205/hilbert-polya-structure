# P166 paper build status

`ROUND2_INTERNAL_ACCEPT / REVIEWS A-B 0C-0M-0m / HOLD_EXTERNAL`

| Check | Result |
|---|---|
| Anonymous `amsart` source | PASS |
| Complete proofs in body | PASS |
| Required author-side files | PASS |
| Author verifier | 17,017,929 assertions, PASS |
| Canonical replay | 2/2 byte-identical |
| Primary build | PASS |
| Source-only cold builds | 2/2 PASS; both byte-identical to canonical PDF |
| Settled warning/error/badbox scan | 0 |
| Page budget | 4 pages, inside 4--6 target |
| Fonts | 24/24 embedded, subsetted, Unicode mapped |
| Metadata/anonymity | PASS |
| Visible lifecycle marker | `HOLD_EXTERNAL` |
| Hostile Review A | ACCEPT, 11,795,304 assertions, 0C/0M/0m |
| Hostile Review B | ACCEPT_INTERNAL, 14,005,344 assertions, 0C/0M/0m |
| Round-1/2 transitions | both no-change; all frozen mathematical artifacts unchanged |
| Git | intentionally untouched |

Canonical Round-1 PDF:

```text
bytes: 294,007
SHA-256: f8cafffe180ce73764057e26435c3abd36602dc392a151388531ab003da5496c
Round-0 copy: main_round0_original.pdf (byte-identical)
Round-1 copy: main_round1.pdf (byte-identical)
Round-2 copy: main_round2.pdf (byte-identical)
```

Paper-local `SHA256SUMS` is deliberately pending final consistency notice.
