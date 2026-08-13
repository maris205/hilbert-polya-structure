"""Numerical primitives for the conformally symplectic Hénon homotopy.

The package deliberately contains no prime tables or spectral data.  It is the
geometry-only layer used by the Stage-1 falsification experiments.
"""

from .model import HenonHomotopy
from .audit import audit_ledger_payload, audit_orbit, audit_run
from .cycles import (
    binary_primitive_orbit_count,
    build_orbit_ledger,
    cyclic_jacobian,
    cyclic_residual,
    primitive_binary_necklaces,
)

__all__ = [
    "HenonHomotopy",
    "audit_ledger_payload",
    "audit_orbit",
    "audit_run",
    "binary_primitive_orbit_count",
    "build_orbit_ledger",
    "cyclic_jacobian",
    "cyclic_residual",
    "primitive_binary_necklaces",
]
