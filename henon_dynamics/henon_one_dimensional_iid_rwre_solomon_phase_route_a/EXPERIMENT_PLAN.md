# Exact evidence plan

## Purpose

The computation is a deterministic regression receipt for the analytic RWRE
theorem.  It is not a simulation and is not evidence for an almost-sure limit.

## Lanes

1. Enumerate all integer Beta parameters \(1\leq\alpha,\beta\leq20\), using
   exact harmonic numbers for the sign of
   \(\psi(\beta)-\psi(\alpha)\) and exact rational first moments.
2. Enumerate 280 rational two-atom laws.  Replace numerical logarithms by the
   exact comparison
   \(\rho_1^r\rho_2^{m-r}\lessgtr1\).
3. Enumerate all 780 finite environment words of interior length at most four
   over \(\{1/4,1/3,1/2,2/3,3/4\}\), and all 2,930 interior starting points.
   Rebuild every scale weight and hitting probability as a `Fraction`.
4. Independently reconstruct every row without importing the producer.
5. Verify Beta moments, digamma reduction, the harmonic recurrence, crossing
   series, and constant-environment speed in SymPy.
6. Replay the producer in two isolated temporary directories and require byte
   identity.
7. Attack the checker with repaired payload hashes, omitted/duplicated/nested
   rows, strict-JSON failures, and strict-YAML failures.

## Acceptance gates

- All exact ledgers agree with the independent checker.
- The evidence self-excluding payload digest is valid.
- YAML raw and semantic digests are both locked.
- Producer, checker, SymPy, replay, mutation, and release scripts refuse
  optimized Python under both `-O` and `-OO`.
- Three revision PDFs are substantively distinct; `main.pdf` equals round 2.
- Two fresh LuaLaTeX builds per round are byte-identical at the fixed epoch.
- Settled logs contain no warnings or layout defects; fonts are embedded and
  subset; text extraction and per-page rasterization succeed.
