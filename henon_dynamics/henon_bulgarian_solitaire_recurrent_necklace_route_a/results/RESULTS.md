# C190 results

## Exact evidence

- Evidence payload SHA-256:
  `52e6fd775ea565fa86eaf0c4fa1dae1c1e793c9ad4e565be89c14092842b94d3`.
- Evidence file SHA-256:
  `78d1ab6aa74d47adb23c8bbcfe1f5ba04125a4aaa152e3d834be4c7f6dde03a4`.
- Evidence bytes: 772,424.
- Systems: all 40 deck sizes `1<=N<=40`.
- Direct integer partitions: 215,307.
- Recurrent word/partition pairs: 757.
- Direct cycles: 114.
- Positive-iterate residue rows: 248.
- Least-period rows: 117.
- Spectral rows: 248.

The `N=8` sentinel has 22 total partitions, six recurrent states, one
2-cycle, one 4-cycle, fixed ledger `(F_1,F_2,F_3,F_4)=(0,2,0,6)`, full
Koopman zero multiplicity 16, and fourth-root multiplicities `(2,1,2,1)`.

## Verification

- Independent checker: 658,664 assertions.
- Direct partition/independent word agreement: 40/40 systems.
- Separate SymPy reconstruction: 2,210 checks.
- Byte replay: 772,424 bytes, exact.
- Mutation suite: 118 repaired-hash rejections and one stale-hash rejection.
- Final PDF: 2 pages, SHA-256
  `aca83c129125d10ed7a797c51494630c14953f7b63beeea14f8821dc09db2c1d`.

## Verdict

The all-parameter periodic and algebraic spectral structure is exact and
source native.  Complete transient geometry is deliberately not claimed.
Route verdict:

`A0_FAIL / A1_WEAK / A2_FAIL / A3_FAIL / A4_FORMAL_HINT`, overall
`ROUTE_A_REJECTED`, Route B false.
