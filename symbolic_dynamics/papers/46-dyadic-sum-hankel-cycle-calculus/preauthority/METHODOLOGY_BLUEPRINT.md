# Methodology Blueprint — Paper 46

## Methodological principle

The theorem is analytic and exact. Computation has four narrower jobs:

1. verify that two independently implemented representations agree;
2. exercise every convention and endpoint falsifier;
3. make the finite witness ledger reproducible;
4. prevent a later report, Route record, or ledger edit from changing the
   scientific conclusion.

Finite cutoffs never prove an infinite endpoint.

## Typed pipeline

    frozen source packet
        -> evaluator M: cutoff matrix / exact closed-walk enumeration
        -> evaluator C: dyadic anti-diagonal / valuation / cyclic solver
        -> exact science projection
        -> adversarial mutation registry
        -> read-only integrity audit
        -> Route expectation comparison

Evaluator M and evaluator C may share only the frozen packet schema and
standard serialization utilities. They may not import each other's support,
cycle, endpoint, or trace routines.

## Evaluator M: matrix lane

- construct the cutoff support by the predicate that \(m+n\) is a positive
  power of two;
- retain diagonal entries;
- partition the matrix by directly computed \(v_2(m)\);
- compute exact support counts and exact rational weights when \(s\) is an
  even positive integer;
- enumerate based closed walks for small cutoff and length;
- compute deterministic high-precision singular values only as a finite
  diagnostic;
- derive finite trace powers by matrix multiplication.

## Evaluator C: arithmetic lane

- enumerate dyadic anti-diagonals \(m+(2^a-m)=2^a\);
- compute level sums and interval bounds without constructing a matrix;
- generate valuation blocks by odd representatives;
- solve every cyclic label tuple from the closing equation;
- impose positivity and odd-block parity explicitly;
- sum trace contributions from the solver;
- construct disjoint matching lower-bound certificates.

## Exact agreement surface

The lanes must agree exactly on:

- every support bit in all declared cutoffs;
- loop positions and valuation block IDs;
- based closed-walk counts and ordered vertex tuples;
- label tuples derived from each walk;
- the odd/even solver's compatibility and solution set;
- exact traces at integer \(s\) and declared small powers;
- all frozen witnesses and all declared failure classes.

High-precision values are compared only after their exact support and formula
owners have agreed.

## Proof-backed endpoint certificates

The executable package must serialize, rather than rediscover:

- the row-one divergent subseries for \(\sigma\le0\);
- central anti-diagonal lower bounds at \(\sigma=1/2\);
- the exact harmonic identity at \(\sigma=1\);
- finite partial sums of the disjoint matching lower bound at
  \(\sigma=1\);
- summable upper envelopes in the strict legal domains.

Each certificate contains its quantifier, legal domain, formula, and source
proof anchor. A fit to a slope is diagnostic only and cannot be the sole
value of a Boolean theorem check.

## Determinant policy

The ordinary determinant is evaluated only at \(\sigma>1\).
The Hilbert–Carleman determinant is evaluated only at \(\sigma>1/2\).
Finite determinants outside these domains may be computed as controls but
must be labeled cutoff-only and cannot be projected into the infinite
science record.

## Reproducibility and transaction policy

- all paths are package relative;
- inputs and expected outputs are C-sorted and uniquely named;
- raw JSON duplicate keys, nonfinite numbers, bool/int equality, key order,
  and path containment are checked before use;
- the workflow materializes outputs in an isolated stage;
- exact output bytes and every audit must pass before installation;
- a forced late failure must leave the target byte-for-byte unchanged;
- a second complete top-level run must perform zero physical replacements;
- reports and ledgers are mechanically reconstructed from sealed science.

## Scope boundary

This blueprint authorizes no authority run, Git operation, README edit,
mirror operation, novelty claim, or publication decision.

