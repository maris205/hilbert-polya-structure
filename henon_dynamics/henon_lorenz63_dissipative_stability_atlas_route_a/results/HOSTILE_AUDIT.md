# Hostile audit

The mutation harness must reject every altered artifact, including a stale
payload hash, a repaired bad divergence, unknown top-level and nested keys,
an altered source commit or evaluator hash, an inflated A4 verdict, a true
forbidden-claim flag, shifted Hopf input and threshold, a corrupted cubic,
a corrupted Lyapunov ledger, false counts, a renamed identity, a changed DOI,
and a truncated row ledger.

Result: **PASS 17/17**.  The checker validates exact schema closure before
semantic reconstruction, so repairing the payload hash does not make a false
claim admissible.

Adversarial scientific controls also pass:

- volume contraction is not used as the sole dissipativity proof;
- the linear Hopf boundary is not promoted to nonlinear criticality;
- instability above \(\rho_H\) is not called universal chaos;
- zero-rate equilibrium curves are not hidden inside the positive-domain
  theorem;
- finite rows are not represented as a proof of the parameter continuum.
