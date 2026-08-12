# Experiment tracker

## Final core status

- M0 three-representation discovery: completed.
- M1 Arb/Rouché local certificate: passed.
- M2 mirror/odd no-cancellation: passed.
- M3 linear-parent control: passed.
- M4 global strip census: intentionally skipped; one certified extra divisor
  already rejects the candidate.

Independent replay: 9/9 gates. Mutation suite: 25/25 tests.

Decision: `STOP_UNRENORMALIZED_ROUTE`; pivot to homogeneous-cubic
Poisson-boundary anomaly/index.

| Run ID | Milestone | Purpose | Priority | Status | Notes |
|---|---|---|---|---|---|
| C36-R001 | M0 | three-formula replay of \(z_0\) | MUST | PASS_NUMERICAL | 60--80 digit agreement |
| C36-R002 | M1 | certified simple-zero disc | MUST | PASS_CERTIFIED | Arb plus Rouché |
| C36-R003 | M2 | companion-factor nonvanishing | MUST | PASS_CERTIFIED | full input balls |
| C36-R004 | M3 | linear-parent and completed-\(\xi\) exclusion | MUST | PASS_CERTIFIED | both nonzero on disc |
| C36-R005 | M4 | strip argument-principle census | NICE | SKIPPED | not needed for local kill |
