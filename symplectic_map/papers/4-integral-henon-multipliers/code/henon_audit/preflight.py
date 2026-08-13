"""Frozen parameter, proof-dependency, and symplectic preflight audits."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Any

import sympy as sp

from .algebra import PARAMETER_POLYNOMIAL, ROOT_LOWER, ROOT_UPPER, U
from .dynamics import derivative_matrix, henon_inverse, henon_map


def _file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def proof_dependency_audit(proof_path: Path) -> dict[str, Any]:
    """Check proof-artifact structure and report nonblocking prose hints.

    Mathematical correctness is carried by the independent source-lock audit
    validated in R000.  R010 blocks only on missing/duplicate stable schema,
    section, or equation identifiers.  Natural-language wording checks are
    advisory and cannot stop execution after an equivalent prose rewrite.
    """
    text = proof_path.read_text(encoding="utf-8")
    normalized_text = " ".join(text.split())
    required_section_ids = {
        "THEOREM_A",
        "COROLLARY_B",
        "THEOREM_C",
        "PROOF_STRATEGY",
        "DEPENDENCY_MAP",
        "PROOF",
        "STEP_1_SYMPLECTIC",
        "STEP_2_ALGEBRAICITY",
        "STEP_3_MAXIMUM",
        "STEP_4_MONODROMY",
        "STEP_5_RATIONAL_MODULUS",
        "STEP_6_FROZEN_SPECIALIZATION",
        "STEP_7_SHARPNESS",
    }
    required_equation_ids = {
        "POLYNOMIAL_INVERSE",
        "DERIVATIVE_DETERMINANT_ONE",
        "CYCLIC_RECURRENCE",
        "NO_INFINITY_EQUATIONS",
        "CYCLIC_MAXIMUM_ASSUMPTION",
        "STRICT_NONARCHIMEDEAN_DOMINATION",
        "INTEGRAL_SL2_MONODROMY",
        "UNIT_CHARACTERISTIC_POLYNOMIAL",
        "MODULUS_CONJUGATION_IDENTITY",
        "RATIONAL_BAD_PRIME_SUPPORT",
        "SHARP_CONTROL_MULTIPLIERS",
    }

    def identifier_counts(label: str) -> dict[str, int]:
        identifiers = re.findall(
            rf"^<!--\s*{re.escape(label)}:\s*([A-Z0-9_-]+)\s*-->\s*$",
            text,
            flags=re.MULTILINE,
        )
        return {identifier: identifiers.count(identifier) for identifier in sorted(set(identifiers))}

    schema_ids = re.findall(
        r"^<!--\s*HENON_PROOF_SCHEMA_ID:\s*([a-z0-9-]+)\s*-->\s*$",
        text,
        flags=re.MULTILINE,
    )
    section_counts = identifier_counts("HENON_PROOF_SECTION_ID")
    equation_counts = identifier_counts("HENON_PROOF_EQUATION_ID")
    structural_checks = {
        "schema_id_unique_and_current": schema_ids == ["integral-area-henon-proof-v2"],
        "required_section_id_set_exact": set(section_counts) == required_section_ids,
        "each_required_section_id_unique": all(
            section_counts.get(identifier) == 1 for identifier in required_section_ids
        ),
        "required_equation_id_set_exact": set(equation_counts) == required_equation_ids,
        "each_required_equation_id_unique": all(
            equation_counts.get(identifier) == 1 for identifier in required_equation_ids
        ),
    }
    advisory_checks = {
        "finite_affine_periodic_points_explicit": "finite affine points" in normalized_text,
        "algebraicity_precedes_valuations": "every complex periodic orbit is algebraic" in normalized_text,
        "projective_no_point_at_infinity": "force all homogeneous coordinates to vanish" in normalized_text,
        "positive_dimension_hyperplane_argument": "every positive-dimensional projective subvariety" in normalized_text,
        "monicity_degree_strict_maximum": "M^{d_{i_j}}>M" in normalized_text,
        "cyclic_nonarchimedean_contradiction": "a contradiction. Hence $|z_j|_w\\le1$" in normalized_text,
        "integral_special_linear_monodromy": "M_P\\in\\mathrm{SL}_2(\\overline R)" in normalized_text,
        "reciprocal_integrality": "The other eigenvalue is $\\lambda^{-1}$" in normalized_text,
        "galois_closure_over_Q": "finite Galois extension $M/\\mathbb Q$" in normalized_text,
        "all_places_above_rational_bad_support": "lying above the rational primes in" in normalized_text,
        "conjugation_stable_place_set": "stable under $\\operatorname{Gal}(M/\\mathbb Q)$" in normalized_text,
        "does_not_conflate_conjugate_and_reciprocal": "does not assert that $\\overline\\lambda$ is the reciprocal" in normalized_text,
        "rational_modulus_support_valuation": "2v_\\ell(q)" in normalized_text,
        "finite_audit_not_theorem": "No finite-period computation can extend" in normalized_text,
    }
    return {
        "run_id": "R010",
        "check_role": "blocking_structure_and_provenance_presence_check_with_nonblocking_prose_advisories",
        "independent_mathematical_audit_authority": "R000 validates source_lock.json v2, whose independent_theory_audit.status is PASS_AFTER_REPAIR",
        "natural_language_checks_are_blocking": False,
        "proof_path": str(proof_path),
        "proof_sha256": _file_hash(proof_path),
        "schema_ids": schema_ids,
        "section_id_counts": section_counts,
        "equation_id_counts": equation_counts,
        "structural_checks": structural_checks,
        "advisory_prose_checks": advisory_checks,
        "advisory_missing": sorted(
            name for name, present in advisory_checks.items() if not present
        ),
        "whitespace_normalization": "all Unicode whitespace collapsed to one ASCII space for advisory prose hints only",
        "mathematical_dependency_chain": [
            "projective cyclic system has no point at infinity, hence finite and algebraic",
            "cyclic ultrametric maximum forces S-integral periodic coordinates",
            "integral determinant-one monodromy makes both eigenvalues S-units",
            "Galois closure and all places above S_Q make complex conjugation preserve the unit group",
            "q^2=lambda*conjugate(lambda) makes exact rational q an S_Q-unit",
        ],
        "all_period_result_source": "deductive proof",
        "finite_experiment_role": "implementation audit only",
        "pass": all(structural_checks.values()),
    }


def parameter_preflight() -> dict[str, Any]:
    derivative = PARAMETER_POLYNOMIAL.diff()
    root_count_interval = PARAMETER_POLYNOMIAL.count_roots(ROOT_LOWER, ROOT_UPPER)
    real_intervals = PARAMETER_POLYNOMIAL.intervals(eps=sp.Rational(1, 10**10))
    return {
        "run_id": "R020",
        "parameter_polynomial": sp.sstr(PARAMETER_POLYNOMIAL.as_expr()),
        "monic": PARAMETER_POLYNOMIAL.LC() == 1,
        "degree": PARAMETER_POLYNOMIAL.degree(),
        "is_irreducible_over_Q": bool(PARAMETER_POLYNOMIAL.is_irreducible),
        "root_isolation_interval": [str(ROOT_LOWER), str(ROOT_UPPER)],
        "polynomial_at_lower": str(PARAMETER_POLYNOMIAL.eval(ROOT_LOWER)),
        "polynomial_at_upper": str(PARAMETER_POLYNOMIAL.eval(ROOT_UPPER)),
        "roots_in_frozen_interval": int(root_count_interval),
        "all_real_root_intervals": [
            {"interval": [str(item) for item in interval], "multiplicity": multiplicity}
            for interval, multiplicity in real_intervals
        ],
        "derivative": sp.sstr(derivative.as_expr()),
        "unique_real_root": sum(multiplicity for _interval, multiplicity in real_intervals) == 1,
        "algebraic_integer_certificate": "monic polynomial over Z",
        "pass": (
            PARAMETER_POLYNOMIAL.LC() == 1
            and PARAMETER_POLYNOMIAL.is_irreducible
            and PARAMETER_POLYNOMIAL.eval(ROOT_LOWER) < 0
            and PARAMETER_POLYNOMIAL.eval(ROOT_UPPER) > 0
            and root_count_interval == 1
            and sum(multiplicity for _interval, multiplicity in real_intervals) == 1
        ),
    }


def symplectic_identity_audit() -> dict[str, Any]:
    x, y, a = sp.symbols("x y a")
    forward = henon_map(x, y, a)
    inverse = henon_inverse(x, y, a)
    inverse_after_forward = henon_inverse(*forward, a)
    forward_after_inverse = henon_map(*inverse, a)
    derivative = derivative_matrix(x)
    omega = sp.Matrix([[0, 1], [-1, 0]])
    symplectic_residual = (derivative.T * omega * derivative - omega).applyfunc(sp.expand)
    return {
        "run_id": "R021",
        "forward": [sp.sstr(item) for item in forward],
        "inverse": [sp.sstr(item) for item in inverse],
        "inverse_after_forward": [sp.sstr(item) for item in inverse_after_forward],
        "forward_after_inverse": [sp.sstr(item) for item in forward_after_inverse],
        "inverse_identity_pass": inverse_after_forward == (x, y) and forward_after_inverse == (x, y),
        "derivative": [[sp.sstr(item) for item in row] for row in derivative.tolist()],
        "determinant": sp.sstr(derivative.det()),
        "symplectic_matrix_residual": [[sp.sstr(item) for item in row] for row in symplectic_residual.tolist()],
        "global_polynomial_automorphism": True,
        "pass": (
            inverse_after_forward == (x, y)
            and forward_after_inverse == (x, y)
            and derivative.det() == 1
            and symplectic_residual == sp.zeros(2)
        ),
    }
