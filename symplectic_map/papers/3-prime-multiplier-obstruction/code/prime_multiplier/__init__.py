"""Exact arithmetic tools for the frozen PCF multiplier audit.

The public API is deliberately small and has no network or external-data
dependency.  All candidate computations are orchestrated by the source-lock
aware CLI; the pure algebra functions remain independently testable.
"""

from .algebra import (
    CandidateField,
    candidate_field,
    candidate_parameter_polynomial,
    exact_equal,
    iterate_polynomial,
    serialize_polynomial,
)
from .controls import CONTROL_SPECS, audit_controls
from .dynatomic import DynatomicComponent, exact_period_component, formal_dynatomic
from .resultant import MultiplierCertificate, multiplier_certificate

__all__ = [
    "CONTROL_SPECS",
    "CandidateField",
    "DynatomicComponent",
    "MultiplierCertificate",
    "audit_controls",
    "candidate_field",
    "candidate_parameter_polynomial",
    "exact_equal",
    "exact_period_component",
    "formal_dynatomic",
    "iterate_polynomial",
    "multiplier_certificate",
    "serialize_polynomial",
]

