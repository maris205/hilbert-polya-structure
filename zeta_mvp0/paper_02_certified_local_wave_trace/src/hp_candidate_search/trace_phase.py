"""Phase-convention oracle for the Route A4 fixed-energy trace.

This module is separate from the immutable R400 orbit engine.  It records the
sign selected by the exact anisotropic-harmonic-oscillator trace in the
Combescure--Ralston--Robert convention.
"""

from __future__ import annotations

from dataclasses import dataclass

from .local_periodic_orbits import normal_mode_data
from .warped_henon import TWO_PI


@dataclass(frozen=True)
class FastCRRPhaseData:
    """CRR phase convention for the once-traversed fast orbit."""

    transverse_angle: float
    transverse_stability_determinant: float
    crr_candidate_indices: tuple[int, int]
    positive_time_index_mod_four: int
    negative_time_index_mod_four: int
    positive_time_phase: complex
    negative_time_phase: complex


def fast_crr_phase_data(a: float) -> FastCRRPhaseData:
    """Return the trace-relevant CRR phase of the near-bottom fast branch.

    In two configuration dimensions with elliptic transverse multipliers,
    CRR equations (58) leave the representatives 1 and 3.  The exact
    anisotropic-oscillator trace selects positive imaginary phase at the
    positive one-fold return, hence index 1 modulo four.  The negative-time
    contribution is its complex conjugate.
    """

    mode = normal_mode_data(a)
    angle = mode.fast_transverse_angle
    if not 0.0 < angle < TWO_PI:
        raise ValueError("the fast transverse angle must lie in (0, 2*pi)")
    return FastCRRPhaseData(
        transverse_angle=angle,
        transverse_stability_determinant=mode.fast_stability_determinant,
        crr_candidate_indices=(1, 3),
        positive_time_index_mod_four=1,
        negative_time_index_mod_four=3,
        positive_time_phase=1.0j,
        negative_time_phase=-1.0j,
    )
