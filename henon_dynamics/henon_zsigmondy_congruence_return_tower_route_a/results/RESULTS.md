# C179 exact results

## Claim-bearing results

- For every coprime \(a>b\geq1\), a prime is primitive for
  \(a^n-b^n\) exactly when \(1\) first returns at time \(n\) under
  multiplication by \(ab^{-1}\) on \(U_p\).
- The exact primitive-return existence exceptions are the attributed
  classical Zsigmondy exceptions: \((2,1,6)\), and \(n=2\) with \(a+b\) a
  power of two.
- If \(e=v_p(a^n-b^n)\), then the least return on every \(p^k\)-fiber is
  \(np^{\max(0,k-e)}\).
- Every admissible \(N\)-fiber is \(\varphi(N)/L_N\) equal cycles of length
  \(L_N\), with exact fixed counts, reciprocal zeta/determinant factors, and
  inversion time reversal.
- The disjoint union has fixed ledger \(a^n-b^n\), source zeta
  \((1-bz)/(1-az)\), and an exact Möbius primitive-cycle formula.
- The profinite inverse-limit translation has no positive-time fixed point
  and source zeta 1.
- These incompatible global ledgers prove owner nonselection from finite
  fibers alone, not absolute nonexistence after extra structure.

## Deterministic validation

- Canonical evidence payload SHA-256:
  `22b08c44f51e4bf063a2fc608d570a3584462d3efbaf3e2acb47d0f9b083b34f`.
- Released evidence-file SHA-256:
  `0a756181a775171a6c7de06afced94a75d835cd265d14f38ab825c1119525066`.
- Producer-independent checker: 320,291 assertions.
- Separate SymPy path: 6,674 exact checks.
- Hostile mutations: 64 repaired-hash and one stale-hash mutation, all
  rejected.
- The original 60 repaired-hash cases are retained.  Four additional exact-
  contract attacks cover attribution novelty status, appended A0 log-p clock
  semantics, appended A4 target-operator semantics, and absolute enlarged-
  owner impossibility; all four are rejected after rehashing.
- Byte replay: exact at 2,219,358 bytes.
- Finite sentinels: 63 parameter pairs, 31 finite-fiber pairs, 567
  primitive-divisor rows, 630 globalization rows, 1,650 finite-fiber rows,
  2,080 prime-power lift rows, and exactly seven exception rows.

The PDF and manifest hashes are recorded after deterministic build closure in
`paper/COMPILE_REPORT.md` and `C179_RELEASE_MANIFEST.json`.

The evidence payload contains no changed mathematical claim in this validator
hardening pass and remains byte-identical.  The paper's validation count is
refreshed from 60 to 64 without changing its theorem or scope.

## Route decision

`(A0_WEAK_ARITHMETIC_RELATION, A1_WEAK, A2_FAIL, A3_FAIL,
A4_NATURAL_QUANTIZATION)`; overall `ROUTE_A_EXPLORATORY`; Route B false.
