# HCS-C323 exact-evidence plan

## Analytic claims under test

1. Orthogonal marked-dark, unmarked-dark, and bright decomposition.
2. Complete spectrum and multiplicities in every interior case.
3. Exact success probability and off-resonance maximum.
4. Perfect success iff `g=1` for `0<M<N`.
5. Critical `g=1+c sqrt(a)` detuning window.
6. Complete-graph adjacency/global-phase equivalence.
7. `M=0`, `M=N`, `N=1`, and `g=0` faces.

## Deterministic lanes

- The producer writes canonical JSON with exact rationals and 72-digit decimal
  receipts over all `2<=N<=32`, all interior `M`, and seven frozen driver
  strengths.
- A separate checker reconstructs every formula without importing the
  producer, strictly parses JSON/YAML, and locks both evaluator bytes and
  semantics.
- SymPy independently proves the bright characteristic polynomial,
  trace-free square, success/max-defect identities, graph shift, and critical
  window before running exact parameter substitutions.
- Replay requires two isolated producer runs to equal the checked-in bytes.
- Hostile mutation uses repaired payload hashes and parser/schema attacks; all
  attacks must be rejected.
- Every executable lane must explicitly reject optimized Python.

## Paper gates

Round 0 contains the spectral and search theorem.  Round 1 adds the critical
window, all boundary faces, and graph normalization.  Round 2 adds evidence,
collision, and Route-A/nonclaim audits.  Each revision is compiled twice from
a fresh directory under the fixed epoch using LuaLaTeX.  Logs must contain no
warning, overfull/underfull box, undefined reference/citation, rerun request,
or missing glyph; every font must be embedded and subset.
