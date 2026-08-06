# Legacy Annular Residual 001

## Status

```text
formal candidate: false
Route A: (A1_WEAK, A2_FAIL, A3_FAIL, A4_FAIL)
verdict: NOT_TESTABLE
Route B: not authorized
```

This stage freezes the direct annular logarithmic residual

\[
g_\sigma(z)=\sum_{n\ge2}\frac{\tau_{\sigma,n}-a_n}{n}z^n
=\log G_H(z)-\log\det_2(I-zC_\sigma).
\]

It is an A3 diagnostic for the existing noisy quadratic-map family, not a
standalone dynamical candidate or determinant. The frozen radii are

\[
R=1.4,\qquad \rho=1.41,
\qquad \rho_*=1.426787483864074\ldots.
\]

RH-300 proves that vanishing `H∞(1.41)` or `H2(1.41)` norm closes the full
weighted coefficient budget, and RH-302 reduces that statement to a moving
head. The current repositories do not contain the compatible physical-clock,
`q=1/2`-selected complementary spectrum/trace stream with frozen cutoff and
precision controls. Earlier fixed-noise spectra do not pay this moving-order
obligation.

## Reopening condition

Provide an actual same-ledger complementary spectrum or
`tau_(sigma_k,n)=Tr(C_(sigma_k)^n)` stream on the frozen baseline
`sigma_k=lambda^(-2k)`, together with discretization, spectral cutoff,
precision, and stopping controls. Then test the signed/complex moving-head
`H2(1.41)` norm without parameter refitting. A proof of the corresponding
all-order limit reopens the route directly.

No paper directory is created at this checkpoint: the source lock is useful,
but the stage adds no new theorem or physical obstruction beyond the audited
legacy frontier.

## Files

- `source_lock.yaml` freezes the object, data type, clocks, normalization,
  determinant convention, data firewall, and reopening condition.
- `route_a_evaluation.yaml` records the versioned Route-A diagnostic.

## Verification

At the source checkpoint, the focused legacy suites passed `39/39` tests:

```text
RH-300: 4/4
RH-302: 3/3
RH-309: 5/5
RH-311: 3/3
RH-361: 20/20
RH-VOL4: 4/4
```

The HP-Dynamics outer suite passed `225/225` tests in `63.548 s`, and all 43
source-lock/evaluation YAML files parsed. These tests reproduce the existing
conditional criteria and status ledgers; they do not supply the missing
physical moving-order spectrum.

Integrated from HP-Dynamics commit
`0e6152d8b477cb7c75cc3648e62ce18ed094031c` and legacy RH-371 commit
`2d01633de0bcf0ecd1310291e2547cff417e13a0`.
