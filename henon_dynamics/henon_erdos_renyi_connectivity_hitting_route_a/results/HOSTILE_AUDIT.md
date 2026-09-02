# Hostile audit

## False model substitution

The finite law is the fixed-size slice `G(n,m)` generated without replacement.
A mutation to independent Bernoulli edges is rejected.  The asymptotic proof
uses the exact hypergeometric probability of required/forbidden edges.

## Insufficient connectivity proof

Poisson isolated vertices alone do not prove connectivity.  A no-cross-edge
bound alone is also too coarse at small component sizes.  The repaired proof
requires one of `s^(s-2)` spanning trees inside each proposed component and
all crossing edges absent, then splits at `n/log n`.  Both ranges are shown
summable.

## Distributional overclaim

The window result is weak convergence.  It does not imply convergence of
unbounded moments and is not promoted to finite-n equality with the
last-isolated stopping time.  These negative boundaries appear in evidence,
paper, theorem package, and mutation targets.

## Count and serialization attacks

Mutations cover recurrence counts, support, endpoints, CDF/PMF/tails, moments,
window coordinates, appended rows, and bool/float integer aliases.  Semantic
mutations are rehashed; a stale-hash control is separate.  Duplicate JSON,
NaN, trailing data, compact bytes, invalid UTF-8, top-level type, duplicate
YAML, aliases, merges, and non-string YAML keys are rejected.  The checker
explicitly rejects `python -O`.

## Collision-map attacks

The exact C301 partition-refinement, C291 dimer-RSA, and C276 uniform-random-
mapping distinctions are part of the evidence tree and independent checker.
Three repaired-payload-hash mutations alter them individually and must fail.

## Scope

All five Route-A entries fail, overall Route A is rejected, Route B is false,
and every target-arithmetic claim flag is false.
