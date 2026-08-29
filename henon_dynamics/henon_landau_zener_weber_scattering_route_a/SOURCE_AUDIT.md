# Source audit

The manuscript uses three pre-registered primary/review sources.  DOI links
were checked and are reproduced verbatim in the evidence ledger.

| Key | Source-local claim | Persistent DOI |
|---|---|---|
| Zener1932 | Original nonadiabatic level-crossing law | [10.1098/rspa.1932.0165](https://doi.org/10.1098/rspa.1932.0165) |
| VitanovGarraway1996 | Parabolic-cylinder treatment and finite-duration effects | [10.1103/PhysRevA.53.4288](https://doi.org/10.1103/PhysRevA.53.4288) |
| Shevchenko2010 | Stokes-phase conventions and interferometric review | [10.1016/j.physrep.2010.03.002](https://doi.org/10.1016/j.physrep.2010.03.002) |

The sources support the standard physical model and its Weber connection
formula; they are not used as evidence for arithmetic correspondences or
priority claims.  The exact probability and phase are independently encoded
in the producer and reconstructed by the checker.  Finite-window entries are
new source-local controls generated from the displayed ODE, with fixed rational
parameters and deterministic step count.

No prime/zero table, local arithmetic datum, Euler factor, root number,
automorphy assertion, target divisor, or Route-B input is read by any script.
The package does not claim an exact finite-time closed form: only the
infinite-time scattering law is theorem-level, while RK4 data delimit the
finite-window approximation explicitly.
