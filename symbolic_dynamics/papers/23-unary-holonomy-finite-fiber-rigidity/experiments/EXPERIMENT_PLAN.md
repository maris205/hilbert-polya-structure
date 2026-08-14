# Exact Experiment Plan — SD-C25

All runs audit theorem consequences inside Symbolic Dynamics. They use no
Riemann-zero data and do not promote finite prefixes to proofs.

| ID | Frozen audit | Exact success condition | Primary artifact |
|---|---|---|---|
| E1 | canonical cycles through (k=4096), ordered word, no-oracle scan | every word is (1^{k-1}2); candidate source has no target call | `canonical_word_certificates.csv` |
| E2 | all unary maps through four states; full two-state Boolean relations | every response repeats after certified ((\mu,\lambda)) | `finite_state_periodicity.csv` |
| E3 | post-freeze composite witnesses | (p(1+\lambda)) is composite with the same response | `composite_witnesses.csv` |
| E4 | 48 rational matrix fixtures, (d=1,\ldots,8) | Cayley–Hamilton, LRS residuals, and rational series agree exactly | `recurrence_certificates.csv` |
| E5 | two nilpotent realizations, seven targets, four cutoffs | exact prefix and exact zero tail for every matched target | `nilpotent_memorizer_controls.csv` |
| E6 | same-object finite blocks through period 32 | exact traces and determinants agree; full local factor retained | `canonical_block_traces.csv` |
| E7 | directed-rounding edge prefixes | ordered intervals for all sigma/cutoff/A–B controls | `trace_class_diagnostics.csv` |
| E8 | licensed Paper19/20 wrappers on five supports | transient pruning, clock bound, and marker change all certify | `wrapper_import_certificates.json` |
| E9 | exact roof/marker ledger through (k=4096) | (\prod nd=M_k^2), while (z^k,M_k^{-2s}) differ from the diagonal target | `roof_marker_mismatch.csv` |
| E10 | two runs, tests, schema, SHA | byte-identical outputs, 32/32 tests, integrity and SHA checks pass | `double_run_certificate.json` |

The E6 local-factor convention is

\[
  \det(I-w_kBA^{k-1}).
\]

The frozen (2\times2) control (A=I), (B=\operatorname{diag}(1,-1))
must return first trace zero, second repetition trace two, and local factor
(1-w_k^2). A scalar oracle filter is a separate one-dimensional
orbit-level control.

