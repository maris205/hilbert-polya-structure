# Experiment plan — C107

## Claim under test

For the frozen four-state H6 symbolic interface, deleting state 3 before every
iterate should produce an exact finite survivor transfer and a reproducible
escape determinant.

## Frozen inputs

- adjacency (A) is fixed before counting;
- the hole is the geometric/state label `3`;
- all arithmetic is exact integer/rational arithmetic;
- the maximum reported period is 12.

## Measurements and gates

1. Build the principal survivor matrix (B).
2. Compute (det(I-zB)), traces, and primitive necklace counts.
3. Reconstruct all values in an independent checker and SymPy.
4. Replay the evidence byte-for-byte and reject six semantic mutations.
5. Compile the paper twice with a fixed `SOURCE_DATE_EPOCH`.

The result earns only a discrete symbolic A2 prefix.  A geometric hole theorem
and an analytic open transfer owner are explicitly out of scope.
