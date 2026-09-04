# HCS-C354 — Lagrange heavy-top elliptic closure

This package proves the complete regular-chart reduction and reconstruction theorem for the Lagrange symmetric heavy top: cubic root chambers, Jacobi nutation, exact period, two complete third-kind phase increments, and full \(SO(3)\) closure iff both normalized increments are rational. Pole, steady, separatrix, sleeping, free and spherical boundaries are separated.

## Reproduce

    python3 -B code/c354_lagrange_top_producer.py
    python3 -B code/c354_lagrange_top_checker.py
    python3 -B code/c354_lagrange_top_sympy_crosscheck.py
    python3 -B code/c354_lagrange_top_replay.py
    python3 -B code/c354_lagrange_top_mutation.py
    python3 -B code/c354_release_manifest.py

The package contains 27 manifest payloads plus the self-excluded release manifest. Scope is NO_BAD_EULER_OR_ROOT_NUMBER; Route B is false.
