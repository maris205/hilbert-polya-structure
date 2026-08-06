# R401-SC Result Report

## Outcome

Overall status: **PASS**.

This is an A4.9-guided fixed-energy numerical audit at delta=0.01.  The
analytic threshold delta_tr remains nonquantitative, so the result is not a
proof that this cell lies in the theorem's sufficiently-small interval.

| hbar | nonlinear Z | |Z-1| | arg Z | harmonic Z | |Z-Z_har| | integrity |
|---:|---:|---:|---:|---:|---:|:---:|
| 4.00e-04 | 0.344728+0.367872i | 0.7515 | +0.8179 | 0.333411+0.363570i | 0.0121 | PASS |
| 3.00e-04 | 1.448682+0.095288i | 0.4587 | +0.0657 | 1.444396+0.111833i | 0.0171 | PASS |
| 2.00e-04 | 0.317529+0.242788i | 0.7244 | +0.6528 | 0.314303+0.225802i | 0.0173 | PASS |
| 1.50e-04 | 1.403014-0.489353i | 0.6339 | -0.3356 | 1.414802-0.474346i | 0.0191 | PASS |
| 1.00e-04 | 0.843838-0.354104i | 0.3870 | -0.3973 | 0.865887-0.359363i | 0.0227 | PASS |
| 7.50e-05 | 0.785322+0.054500i | 0.2215 | +0.0693 | 0.787809+0.036198i | 0.0185 | PASS |
| 5.00e-05 | 1.047705+0.011489i | 0.0491 | +0.0110 | 1.044363+0.016959i | 0.0064 | PASS |
| 4.00e-05 | 1.006523+0.013300i | 0.0148 | +0.0132 | 1.004595+0.013999i | 0.0021 | PASS |

The preregistered prediction used the absolute coefficient

\[
T/(2\pi\sqrt D)=0.053731520381747562
\]

and phase +i, with no fitted constants.  The exact harmonic column uses the
same finite energy and time windows and exposes the pre-asymptotic window
oscillations in the coarser cells.

## Scientific gates

```json
{
  "all_integrity_gates": true,
  "finest_complex_error_le_0p025": true,
  "finest_phase_error_le_0p025": true,
  "finest_matches_harmonic_baseline": true,
  "finest_improves_on_two_preceding": true
}
```

Arithmetic P remains open and gate Z remains unauthorized.
