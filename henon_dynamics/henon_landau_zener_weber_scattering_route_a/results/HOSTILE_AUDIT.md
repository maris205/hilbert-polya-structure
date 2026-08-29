# Hostile audit

The main failure modes were tested explicitly:

1. Changing the Hamiltonian, Weber signs, probability, phase, route tuple,
   scope flags, or source/evaluator locks is rejected even after repairing the
   payload hash.
2. Unknown top-level and nested row keys are rejected by exact schema closure.
3. A stale payload hash is rejected before numerical rows are trusted.
4. The `g↦−g` gauge, `g=0`, sudden/adiabatic limits, and finite-window status
   are represented as separate boundary rows.
5. The finite RK4 ledger is deliberately bounded (`<1e-3` Gram residual in the
   checker) and never promoted to an exact finite-time formula.

The audit therefore supports only the source-local scattering theorem and its
reproducibility controls.  It does not support an arithmetic interpretation,
a target operator, or Route B.
