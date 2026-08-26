# Pre-loop internal Stage-2 review

This file preserves the package author's internal pre-loop review verbatim before
the mandatory independent cross-agent improvement loop replaced
`ROUND1_HOSTILE_REVIEW.md`.

## Questions forced

1. Is local degree computed at `x_-1`, with all indices consistent under iteration?
2. Does pressure use all invariant measures rather than only Bernoulli measures?
3. Does the spectrum count future symbols while controlling the negative tail's contribution?
4. Can the pressure curve recover repeated fibre sizes, not only the set of sizes?
5. Are the Martins--Mattos--Varão entropy formulae visibly owner-subtracted?

## Findings and repairs

- Equation (5.2) displays the single boundary term and the exact future index range.
- The natural-extension variational proof begins with arbitrary invariant measures and uses entropy-rate inequality; equality forces Bernoulli.
- A Bowen-cylinder comparison isolates `O(1)` past coordinates.
- The recovery uses coefficients `m_k`, with largest-base coefficient extraction followed by finite recursion.
- The abstract, introduction, pressure corollary, and scope section all name the direct owner and distinguish input from derived bridge.

Verdict: theorem package closes internally; active-neighbour/source status remains HOLD.
