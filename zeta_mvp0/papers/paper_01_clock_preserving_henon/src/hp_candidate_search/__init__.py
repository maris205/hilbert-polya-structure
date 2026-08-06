"""Hilbert--Pólya candidate screening utilities with lazy public imports.

Lazy loading lets the independent R108 finite-element implementation be
imported without transitively importing either finite-difference module.
"""

from __future__ import annotations

from importlib import import_module
from typing import Any


_WARPED_NAMES = {
    "FTLEConfig",
    "centered_fixed_point",
    "hamiltonian_energy",
    "henon_inverse_iterate",
    "henon_iterate_jet",
    "microcanonical_initial_state",
    "potential_derivatives",
    "run_ftle_trajectory",
}
_QUANTUM_NAMES = {
    "GridSpec",
    "classical_smooth_count",
    "compute_eigenvalues",
}

__all__ = sorted(_WARPED_NAMES | _QUANTUM_NAMES)


def __getattr__(name: str) -> Any:
    if name in _WARPED_NAMES:
        module = import_module(".warped_henon", __name__)
    elif name in _QUANTUM_NAMES:
        module = import_module(".quantum_fd", __name__)
    else:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    value = getattr(module, name)
    globals()[name] = value
    return value

