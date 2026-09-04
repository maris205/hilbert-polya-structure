# HCS-C357 — bilinear two-stiffness isochronous oscillator

This package proves all-energy classical isochrony for the asymmetric
piecewise-quadratic well, its exact action and seam-compatible action-angle
chart, identity common-period map, and the complete real quantum eigenvalue iff
through a parabolic-cylinder interface Wronskian. Equal-frequency,
zero-energy, one-sided-flat, and free boundaries are separate.

## Reproduce

    python3 -B code/c357_bilinear_oscillator_producer.py
    python3 -B code/c357_bilinear_oscillator_checker.py
    python3 -B code/c357_bilinear_oscillator_sympy_crosscheck.py
    python3 -B code/c357_bilinear_oscillator_replay.py
    python3 -B code/c357_bilinear_oscillator_mutation.py
    python3 -B code/c357_release_manifest.py

The package contains 27 manifest payloads plus one self-excluded manifest.
