# Hostile audit

The adversarial suite rejects `141/141` mutations.  The attacks are designed to survive a shallow top-level hash check: semantic evidence mutations receive repaired canonical payload hashes, and YAML mutations are accompanied by repaired raw and semantic hash carriers whenever parsing permits.

The suite owns the theorem-critical failure modes: Hamiltonian/Poisson sign drift, wrong cubic, one-phase-for-two substitution, intensity/full-period conflation, missing equal-invariant separatrix, generic-periodic relative-equilibrium overclaim, noncanonical but equivalent rational strings, nonfinite decimal strings, coordinate duplication/omission/reordering, and Route-A/evaluator/scope expansion.

Strict parsing also rejects duplicate or nonfinite JSON, YAML anchors, aliases, merge keys, non-string keys, implicit date typing, unknown fields, and optimized Python.  A stale-hash-only mutation is retained as a control.
