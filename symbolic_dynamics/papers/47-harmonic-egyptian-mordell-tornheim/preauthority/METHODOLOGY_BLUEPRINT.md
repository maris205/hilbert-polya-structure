# Methodology Blueprint — Paper 47

## Two independent evaluators

### Evaluator D: direct graph lane

- tests \(m+n\mid mn\) with exact integer arithmetic;
- constructs cutoff matrices with loops;
- enumerates rows, closed walks, diagonal entries, and exact rational traces;
- uses direct matrix products for small trace powers;
- never imports gcd-scale or divisor-row generation code.

### Evaluator P: parameter lane

- generates ordered coprime triples \((t,a,b)\);
- independently generates a fixed row from \(d\mid m^2,d<m\);
- reconstructs endpoints and harmonic quotients;
- computes primitive MT truncations and scale sums;
- enumerates mixed cycles through parameter-compatible edges;
- never tests the direct divisibility predicate used by Evaluator D.

The lanes may share only the frozen packet schema and serialization helpers.

## Exact agreement surface

- complete ordered edge sets in every declared cutoff;
- loop sets;
- row neighbor sets for every declared row;
- edge coordinates and harmonic quotients;
- based closed walks through declared lengths;
- exact first and second cutoff traces at integer \(s\);
- mixed-cycle witnesses;
- all falsifier failure classes.

## Analytic certificates

The executable evidence records:

1. divisor-row upper envelopes for \(\sigma>0\);
2. high-degree squarefree rows at \(\sigma=0\);
3. loop scale divergence at \(\sigma=1/2\);
4. absolute even-diagonal divergence at \(\sigma=1\);
5. entrywise summability above \(1\);
6. the exact gcd extraction relating primitive and full MT sums.

These are serializations of proved formulas. Numerical slopes are never the
sole proof of an endpoint.

## Trace and determinant policy

- first trace and ordinary determinant only for \(\Re s>1\);
- second trace and \(\det_2\) only for \(\Re s>1/2\);
- finite matrices outside these domains are labeled cutoff-only;
- the MT series is a comparison owner, not a substitute source;
- reports are rendered mechanically from the exact science object.

## Integrity and transaction policy

The later implementation must use strict recursive type/value comparison,
safe relative paths checked before I/O, two external evaluator invocations,
an external read-only auditor, actual mutations of disposable copies,
transactional preinstall validation, a forced late-failure unchanged-target
test, and a zero-physical-write second run.

## Scope

No authority, Git, README, mirror, Route-B, or publication action is
authorized by this blueprint.

