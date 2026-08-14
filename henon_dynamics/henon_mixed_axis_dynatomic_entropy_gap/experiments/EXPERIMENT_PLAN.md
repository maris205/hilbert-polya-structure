# Experiment plan

1. Generate every odd mixed-axis closure through period 15 exactly.
2. Check all divisor remainders in `Q[X]`.
3. Recursively remove lower-period quotients and compare their degrees with
   the M\"obius formula.
4. Compute `gcd(F_n,F_n')` and factor each new quotient over `Q`.
5. Match the period-nine coefficient digest to P58.
6. Reconstruct degrees and coefficient hashes in a second implementation.
7. Reject mutations that promote finite reducedness to an all-period theorem
   or formal degree to Galois height.

The experiment is exact. Timing and decimal entropy values are diagnostics,
not proof inputs.
