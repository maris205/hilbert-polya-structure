# Exact control results — P94

Command:

```text
python3 code/verify_marked_s_adic.py
```

Result on 2026-08-28 UTC:

```text
marked symmetric S-adic exact control: PASS
assertions=90509
literal_marker_words=2286
cyclic_phase_words=2286
incidence_bias_cases=28050
inverse_limit_cases=170
a_n=n: R_N=2/((N+1)(N+2)) verified exactly for N<=200
a_n=n^2: R_20=10636990873600000000/92311345892374520571
a_n=n^2: exact partial-product recurrence verified for N<=100
a_n=n^2: R_250000=0.104529502407964
a_n=n^2: pi*sqrt(2)/sinh(pi*sqrt(2))=0.104528666176957
```

## Lane separation

- The marker lane constructs literal words.  It checks internal marker
  absence, boundary marker completeness, cyclic marker spacing, and exact
  decoding.  It does not call the incidence routines.
- The incidence lane uses `fractions.Fraction`.  It verifies normalized
  matrices, their symmetric and antisymmetric directions, all directives of
  depths `1..6` over `a in {1,2,3,4}`, and compatible finite tower biases.
- The linear and quadratic examples have exact rational checks.  Only the
  displayed comparison of the `N=250000` quadratic partial product with the
  sinh constant uses floating point; it is a non-evidence-bearing sanity
  check of the analytic Euler-product proof.

The 90,509 assertions are finite falsification controls.  Compactness,
uniform recurrence, Borel measure extension, and infinite-product convergence
are established in the manuscript.
