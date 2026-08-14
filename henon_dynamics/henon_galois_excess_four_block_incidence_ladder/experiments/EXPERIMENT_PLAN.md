# Experiment plan

## Claims under test

1. The closed-form `A_m/B_m` incidence relation holds for every `m`.
2. The new `B6` word is a genuine exact H6 orbit with the stated field.
3. The width-four excess identity fails by an exact sign.
4. The seven-row witness is rank deficient at width four but unimodular at
   width five.

## Primary protocol

- enumerate primitive words through period six;
- verify the common insertion row for `3 <= m <= 64` as a code guard;
- substitute radical coordinates into all six recurrences;
- compute exact monodromy and minimal polynomials;
- isolate period-five and period-six conjugates;
- evaluate the exact logarithmic comparison;
- form incidence matrices and selected minors;
- reject 20 mutations of claims, fields, ranks and scope.

## Independent protocol

- use adjacency DFS rather than Cartesian-product enumeration;
- use `collections.Counter` rather than the producer's dictionary rows;
- reconstruct monodromy in the opposite multiplication convention;
- recompute Sturm counts, numerical excesses and both matrix ranks;
- compare only final invariants with the primary JSON.

## Acceptance conditions

- producer and independent checker exit zero;
- 15 unit tests pass;
- every dependency hash matches;
- the exact inequality, not decimal rounding, proves the obstruction;
- Route/Hölder promotion mutations are rejected.
