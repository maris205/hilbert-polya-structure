# C130 hostile audit

## Threat model

An evidence file may preserve valid JSON and even carry a newly repaired
payload hash while changing a mathematical claim.  The suite therefore
mutates the receipt, recomputes its internal hash, and invokes the independent
checker in a fresh process.

## Coverage

Forty-three repaired-hash semantic mutations cover:

- schema, candidate, date, scope, base, roof, clock, normalization, and
  determinant convention;
- adjacency, transfer matrix, determinant, and exponential specialization;
- both all-period trace headlines, primitive identity, and convergence flags;
- replay periods, rooted/primitive counts, sector multiplicities, and words;
- sector injectivity, same-sector limitation, and imaginary nonperiodicity;
- rational control roof, collision time, and recovered period;
- progress headline, strict Route-A tuple and overall verdict, Route-B flag,
  scope flags, and nonclaims;
- injected keys at the top level and in each newly closed critical dictionary.

One additional mutation leaves a forged stale hash.  All 44 are rejected,
with the repaired/stale split reported separately by the mutation runner.

## Independence result

The checker does not import the producer or SymPy.  It represents a bivariate
polynomial as a dictionary keyed by `(N0,N1)`, rebuilds matrix powers, enumerates
primitive necklaces, and multiplies primitive factors with an explicit degree
cutoff.  The producer's symbolic representation is therefore not the oracle
for the hostile audit.

## Residual boundary

The audit establishes internal consistency and mutation sensitivity.  It does
not validate any target divisor or arithmetic interpretation, neither of which
is present in the frozen source.
