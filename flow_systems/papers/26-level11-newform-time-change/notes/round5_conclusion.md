# P26 Round-5 conclusion

## Paper-level advance

Round 5 derives the first variation of two frozen primitive-orbit products
without merging Hecke branch degree with zeta repetition.  Under the explicit
reciprocal convention,

```text
d log Z_R / d epsilon |_0
  = -s sum_(gamma#) I(gamma#)
      sum_(r>=1) exp(-s r ell(gamma#)),
```

and the frozen-stability Selberg-type formula inserts the factor
`(1-exp(-r ell(gamma#)))^(-1)`.  In both cases the period `rI` of a repeated
orbit cancels the log-series coefficient `1/r`.

The decisive result is exact: a canonical oriented primitive-orbit family
contains both `gamma#` and `gamma#^(-1)`.  They have equal length and opposite
one-form period, so both log-zeta first variations vanish pairwise.  Retaining
only the positive-word orientation avoids the zero only by defining a
noncanonical half-ledger.

## Missing-obligation theorem

For a Round-4 source owner `M`, write

```text
P_d = sum_(O: cycle_degree(O)=d) I(delta_O).
```

The Hecke theorem gives only `sum_d P_d=a_p I(M)`.  A naive first-variation
recurrence for either frozen zeta kernel holds for every `s` exactly when

```text
P_1=a_p I(M),
P_d=0 for every d>1.
```

This follows by expanding in `q=exp(-s ell(M))` and applying Mobius inversion
to the divisor sums.  Therefore the unweighted Hecke period relation does not
imply a primitive Euler recurrence.

## Finite result

The source-locked audit consumes 138 primitive-certified Round-4 Hecke
cycle-owner instances in the finite output multiset and produces:

- 1,104 explicit inverse-orientation/repetition rows (`138 x 2 x 4`);
- 110 degree-moment rows, including an explicit zero-owner degree-one bin
  whenever the Hecke permutation has no degree-one cycle;
- 165 one-sided Hecke-zeta rows (`55 x 3`);
- 38 mixed-degree and 17 uniform-nonunit-degree source groups;
- 55/55 passing unweighted Hecke period sums;
- 51/55 alpha-period groups violating the all-`s` degree moments;
- 153/165 failures of the naive finite Ruelle recurrence;
- 153/165 failures of the naive frozen Selberg-type recurrence; and
- 53/55 degree-moment failures for the genus-one closed-form control.

All 11 tests pass.  Two complete result trees are byte-identical with SHA-256

```text
7b21a0c25ee269d28b53cd8c0551c8b2a977307641c2d07be78810be2e975731.
```

## Verdict and route boundary

```text
CANONICAL_INVERSE_PAIRED_FIRST_VARIATION=PROVED_EXACT_ZERO
HECKE_DEGREE_MOMENT_CRITERION=PROVED
HECKE_PERIOD_RELATION_IMPLIES_ZETA_RECURRENCE=false
DISCRIMINATIVE_HECKE_EULER_EVIDENCE=STOP_SCOPED
PRIMITIVE_EULER_FACTORIZATION=NOT_ESTABLISHED
```

P26 remains at ARS Stage 1 and Proposal Stage 1 / Route A A0--A1.  The finite
product algebra is not a Route-A A2 evaluation: no complete primitive-class
enumeration, global convergence/continuation theorem, target-prime table,
spectral-zero data, formal Route tuple, or Route-B invocation is present.
