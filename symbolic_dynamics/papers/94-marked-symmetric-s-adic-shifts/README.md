# P94 — Marked symmetric S-adic shifts

Status: **internal Stage 2 frozen package / external HOLD**.

For positive integers `a_n`, the paper studies the binary constant-length
directive morphisms

```text
sigma_n(0) = 0^(a_n+1) 1
sigma_n(1) = 0 1^(a_n+1).
```

The concrete theorem package is:

1. `10` occurs exactly across every image boundary, giving unique
   desubstitution and a two-tower clopen partition at every level;
2. the resulting shift is minimal and aperiodic for every positive
   directive sequence;
3. invariant probabilities are exactly the compatible normalized incidence
   vectors, and the physical symbol bias fills
   `[-R,R]`, where `R = product a_n/(a_n+2)`;
4. the actual zero-frequency interval has radius `R/2`, not `R`;
5. divergence of `sum 1/a_n` gives unique ergodicity, while convergence
   gives exactly two ergodic endpoints;
6. `a_n=n` has finite-prefix bias radius
   `R_N=2/((N+1)(N+2))`, and `a_n=n^2` has limiting bias radius
   `pi*sqrt(2)/sinh(pi*sqrt(2))`.

The reciprocal-sum unique-ergodicity criterion and the general
recognizability/measure-transfer mechanisms have prior owners.  The paper
explicitly subtracts those results.  Its residual result is the complete
closed solution for this specific marked symbolic realization, not a new
general phase-transition theorem.

Run the exact control with:

```bash
python3 code/verify_marked_s_adic.py
```

Build the manuscript with the four-stage command in [BUILD.md](BUILD.md).

The frozen package passed 90,509 registered assertions and a four-stage
production build.  The retained PDF has 7 pages and 352,417 bytes.  The two
internal review rounds are recorded in [HOSTILE_REVIEW.md](HOSTILE_REVIEW.md),
and the final mechanical checks are recorded in [FINAL_QA.md](FINAL_QA.md).
Verify the ten-file frozen manifest with:

```bash
sha256sum -c SHA256SUMS
```

No public release, submission, author contact, specialist-clearance claim, or
priority claim is authorized.
