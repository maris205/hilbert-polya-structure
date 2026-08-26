# C188 exact-regression plan

## Purpose

Regression-test the source-owned all-irreducible theorems and the package's
derived boundary statements without treating finite enumeration as proof.

## Frozen census

- all 144 strongly connected `2 x 2` matrices over
  `{-inf,-1,0,1}`;
- one dimension-one shifted matrix;
- pure critical cycles of lengths three through six;
- an irreducible five-node matrix with critical SCC cyclicities two and three;
- the fixed-support transient family through `m=24`;
- four rational-weight three-cycles with nonintegral cycle means.

This gives 177 matrices, 441 simple cycles, 189 critical SCCs, and 901 declared
vector/projective rows.

## Producer path

1. Enumerate elementary directed cycles.
2. Compute exact `Fraction` cycle means and `lambda`.
3. Build the critical graph from maximizing cycles and compute SCC cyclicities.
4. Form normalized powers sequentially and locate the first period equality.
5. Construct `K,C,S,R` and locate the first full CSR phase window.
6. Classify raw and projective test-vector periods and attraction divisors.
7. Verify the closed `B_m` transient family and reducible boundary.

## Independent checker path

The checker imports no producer code.  It reconstructs:

- `lambda` with Karp's dynamic-programming cycle-mean formula;
- critical edges from a truncated max-plus Kleene closure;
- SCCs with Tarjan's algorithm;
- component cyclicity with the directed-distance gcd formula;
- powers with binary exponentiation;
- cycles by permutation enumeration;
- CSR matrices, transients, vector periods and all exact metadata.

## Third path and adversarial tests

SymPy rationals reconstruct every cycle mean, normalization, period cell, CSR
cell and vector period, plus the symbolic `max(-t,-m)` family boundary.
Canonical replay runs the producer in a temporary directory.  Repaired-hash
mutations attack source ownership, normalization, cyclicity, every theorem and
Route qualification, matrix/vector cells, transient family and reducible
boundary; a stale-hash mutation tests the digest gate.

## Release gates

- all five executable checks pass;
- evidence replay is byte exact;
- three PDF rounds are text-distinct and final equals round two;
- two fresh fixed-epoch builds equal the release PDF;
- fonts are embedded, logs clean, pages visually inspected;
- manifest contains exactly 27 payload files and excludes itself.
