# C191 results

## Exact evidence

- Evidence payload SHA-256:
  `8a4286b4d97efee5d93403407594b1539723cf6bab41ea38168ac515bd27a142`.
- Evidence file SHA-256:
  `6950c217543c2e9c023db08ac406b3f8f116a393294d43ce9ec4da96cfef6f9e`.
- Evidence bytes: 154,517.
- Zero-pattern rows: 272.
- Positive exact scaling cases: 4.
- Boundary cases: 4.
- Exact iteration rows: 40.
- Stored cross-ratios: 28.

The zero-pattern census separates support, total support and full
indecomposability.  In dimension two it contains seven patterns without a zero
line, seven with support, three with total support and one fully indecomposable
pattern.  The corresponding dimension-three counts are 265, 247, 49 and 34.

## Verification

- Independent checker: 2,411 assertions; no producer import.
- Separate SymPy/Ryser reconstruction: 951 checks.
- Byte replay: 154,517 bytes, exact.
- Mutation suite: 242 repaired-hash rejections and one stale-hash rejection.
- Final PDF: 2 pages and 146,909 bytes, SHA-256
  `b578720d2c9ba9e0be06cf659cf3e15521bfdd9267082333fd3c0144223d8129`.

## Verdict

The all-matrix classification is source locked, while the finite census is a
regression oracle only.  Convergent Sinkhorn scaling has no nonconstant
primitive periodic-orbit owner and supplies no target arithmetic semantics or
source-native Hilbert-space quantization.  The exact verdict is

`A0_FAIL / A1_FAIL / A2_FAIL / A3_FAIL / A4_FAIL`, overall
`ROUTE_A_REJECTED`, Route B false, under scope
`NO_BAD_EULER_OR_ROOT_NUMBER`.
