# HCS-C202: all-speed Fisher--KPP traveling-wave atlas

This package gives one complete paper for

\[
u_t=D u_{xx}+r u(1-u),\qquad D,r>0.
\]

It proves that positive decreasing fronts exist uniquely up to translation
exactly for `c>=2sqrt(Dr)`, obtains the `c<=-2sqrt(Dr)` family by reflection,
rules out `[0,1]` fronts at every subcritical or stationary speed, derives all
three leading-edge regimes, and verifies the Ablowitz--Zeppetella solution.

## Reproduce

Run from the repository root:

```bash
python henon_dynamics/henon_fisher_kpp_traveling_wave_atlas_route_a/code/c202_fisher_kpp_producer.py
python henon_dynamics/henon_fisher_kpp_traveling_wave_atlas_route_a/code/c202_fisher_kpp_checker.py
python henon_dynamics/henon_fisher_kpp_traveling_wave_atlas_route_a/code/c202_fisher_kpp_sympy_crosscheck.py
python henon_dynamics/henon_fisher_kpp_traveling_wave_atlas_route_a/code/c202_fisher_kpp_replay.py
python henon_dynamics/henon_fisher_kpp_traveling_wave_atlas_route_a/code/c202_fisher_kpp_mutation.py
python henon_dynamics/henon_fisher_kpp_traveling_wave_atlas_route_a/code/c202_release_manifest.py
```

The finite ledger is explicitly a regression certificate.  It does not prove
the all-speed heteroclinic theorem.  The Route-A verdict is
`(A0_FAIL,A1_FAIL,A2_FAIL,A3_FAIL,A4_FAIL)`, overall rejected, Route B false,
under `NO_BAD_EULER_OR_ROOT_NUMBER`.
