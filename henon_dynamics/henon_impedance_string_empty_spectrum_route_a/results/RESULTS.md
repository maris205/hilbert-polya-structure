# C396 finite results

Actual producer and independent checker completed successfully:
7 boundary + 588 transport exact rows; 126 spectrum + 27 pseudospectrum +
21 Green numerical rows. Evidence SHA-256:
`015000cea0cbb302ac272b6a935a7f1bcadad585af53f955f8883695854f9fa3`.
Canonical payload SHA-256:
`caa73f4f09e4c4f45e5bf299df22c467a99dd4ec0d836847ab85795c036ed616`.

Actual separate lane: 11 symbolic identities, 27 Rayleigh quotients,
81 Volterra actions, 81 complex-gauge actions and 12 singular modes.
Maximum tracked norm/action residual: 6.4405619e-60; tolerance 1e-55.
Working precision 100 digits. The 12 singular modes include two actual
integrals each, checked to 1e-90; these are not interval bounds.

Two unrelated cwd replays matched canonical bytes. Three smoke tests passed.
Actual attacks: 45 repaired-hash semantic, 4 serialization, 10 strict YAML
against checker plus those same 10 against actual release --write:
The final gate additionally tests a changed live evaluator at both entries
and hidden-extra/symlink trees at actual release --write: 62 distinct mutations,
73 refusals in total. These are engineering checks, not scientific findings.
Optimized-mode and final release receipts are generated
by the release runner in TEST_REPORT.md.
