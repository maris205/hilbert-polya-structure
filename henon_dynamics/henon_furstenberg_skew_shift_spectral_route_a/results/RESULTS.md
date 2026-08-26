# C169 results

Status: all symbolic and finite regression gates pass.

- All irrational \(\alpha\): exact iterate formula and no fixed point for any positive iterate (`PROVED`).
- Artin--Mazur zeta: exactly \(1\) (`PROVED`).
- Koopman: exact Fourier action; \(k=0\) pure point and \(k\ne0\) bilateral-shift sectors (`PROVED`).
- Reversal: explicit involutive \(R\) and antiunitary \(\Theta\) (`PROVED`).
- Operator boundary: noncompact, no finite Schatten membership, no ordinary Fredholm determinant for \(z\ne0\) (`PROVED`).
- Finite sentinels: 32 iterate rows, 425 Fourier rows, and 24 nonzero-sector rows.
- Independent checker: 1,574 assertions.
- SymPy: 940 checks.
- Mutation suite: 16/16 repaired-hash and 1/1 stale-hash mutations rejected.
- Citation and reference registries: 0 entries.

Route-A v0.2 decision: `(A0_FAIL, A1_FAIL, A2_FAIL, A3_FAIL, A4_NATURAL_QUANTIZATION)`, overall `ROUTE_A_REJECTED`, Route B false. The strong A4 result is retained as reusable structural knowledge; it does not promote the empty orbit ledger.
