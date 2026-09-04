# HCS-C372: Kirchhoff ellipse and the complete Love threshold ladder

This package closes a theorem-scale spectral linear-mode atlas for a uniform
vorticity ellipse in the planar incompressible Euler equation.

The patch rotates as a rigid shape with

\[
\Omega=\frac{\omega ab}{(a+b)^2},
\]

and, when its Fourier label `m` is measured relative to the instantaneous
principal axes, the Love boundary mode has co-rotating-frame frequency
`lambda_m` with

\[
\lambda_m^2=\frac{\omega^2}{4}\left[
\left(\frac{2mab}{(a+b)^2}-1\right)^2-
\left(\frac{a-b}{a+b}\right)^{2m}\right].
\]

The package proves the `m=1` rotation identity, the `m=2` ellipse-family
zero mode, one and only one threshold for every `m>=3`, strict ordering of
the thresholds, the sharp first wall `a/b=3`, and the linear asymptotic
growth of the threshold ladder.  Circle, zero-vorticity, axis-swap, first
wall, and singular strip faces are separated.

The exact evidence contains 561 rational aspect ratios, 35,904 modal cells,
62 certified thresholds through mode 64, and 390 rigid-solution rows.  It is
a regression certificate; the analytic argument owns all aspect ratios and
all modes.

## Route decision

`(A0_FAIL, A1_WEAK, A2_FAIL, A3_FAIL, A4_FORMAL_HINT)` with overall verdict
`ROUTE_A_REJECTED`.  There is no arithmetic prime owner, primitive-orbit
ledger, dynamical zeta, target determinant, target zero match, or
Hilbert--Pólya operator.  Route B remains locked under
`NO_BAD_EULER_OR_ROOT_NUMBER`.

## Reproduce

```bash
python -B code/c372_release_manifest.py --write --build-pdfs
python -B code/c372_release_manifest.py
python -m unittest tests/test_c372_smoke.py
```

The final manuscript is [paper/main.pdf](paper/main.pdf).
