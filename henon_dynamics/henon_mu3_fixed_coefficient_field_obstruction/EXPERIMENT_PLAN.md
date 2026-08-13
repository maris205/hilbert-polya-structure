# HCS-C44 exact experiment plan

## Objective

Certify the all-prime field-generation theorem and independently replay exact
finite-prime controls without using floating point, fitted phases, or Riemann
zero data.

## Producer tasks

1. Lock the HCS-C43 certificate and mathematical normalization.
2. Enumerate all primes \(p\equiv1\pmod3\) up to the frozen cutoff.
3. Construct \(\rho\), the histogram \(N_p\), and the paired histogram \(H_p\).
4. Compute the scaling stabilizer of \(H_p\).
5. Compute \(M_{2m}\), and \(M_{2m+2}\) for \(p\ge13\), both directly and
   from the closed formulas.
6. Verify \(N_p(0)=p-3\) and the rational trace \(-6\).
7. Record the exact field degree \((p-1)/2\).
8. Emit the symbolic all-prime proof contract and conservative Route-A verdict.

## Independent checker

The checker must not import producer code.  It reconstructs every histogram
and moment, validates strict JSON types and exact key sets, verifies the source
hashes, and rejects any altered theorem, stabilizer, degree, normalization,
scope, or Route-A field.

## Stop/go gate

- `STOP_FIXED_COEFFICIENT_FIELD` if the all-prime stabilizer theorem is proved.
- `GO_UNIFORM_HANKEL_RANK` only if a fixed field survives.
- `GO_C45_GALOIS_NORM_DESCENT` after the fixed-field stop, because trace and
  norm are the first minimal rational descents to test.  This is a successor
  choice, not a classification of all invariant descents.

## Forbidden moves

- prime-dependent coefficient fields marketed as one compatible system;
- averaging split and inert clocks;
- post hoc choice of embeddings or phases;
- inference from the finite ledger in place of the symbolic theorem;
- Riemann-zero fitting.
