# HCS-C206 — Couette shear enhanced dissipation

This package proves the complete Fourier-semigroup theorem for
`partial_t f + a y partial_x f = nu Delta f` on `T x R` for every real shear
`a`, viscosity `nu>=0`, Fourier sector, and physical time. It includes the
exact and sharp sector norm with its nonattainment/unitary-attainment boundary,
exact semigroup composition, cubic enhanced-dissipation scale, inviscid
unitary/mixing boundary, every degenerate parameter boundary, the complete
`L2` periodic-state classification, and the non-trace-class stop.

Run from the repository root:

```text
python3 henon_dynamics/henon_couette_shear_enhanced_dissipation_route_a/code/c206_couette_producer.py
python3 henon_dynamics/henon_couette_shear_enhanced_dissipation_route_a/code/c206_couette_checker.py
python3 henon_dynamics/henon_couette_shear_enhanced_dissipation_route_a/code/c206_couette_sympy_crosscheck.py
python3 henon_dynamics/henon_couette_shear_enhanced_dissipation_route_a/code/c206_couette_replay.py
python3 henon_dynamics/henon_couette_shear_enhanced_dissipation_route_a/code/c206_couette_mutation.py
python3 henon_dynamics/henon_couette_shear_enhanced_dissipation_route_a/code/c206_release_manifest.py
```

The release contains 27 content-addressed payloads and one self-excluded
manifest. Exponentials are evaluated at 100 working decimal digits and the
1,350 multiplier/norm fields are serialized to 82 significant digits. Scope
is `NO_BAD_EULER_OR_ROOT_NUMBER`; Route B is false.
