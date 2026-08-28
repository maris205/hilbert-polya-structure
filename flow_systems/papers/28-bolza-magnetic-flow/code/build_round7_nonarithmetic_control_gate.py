#!/usr/bin/env python3
"""Build the P28 Round-7 non-arithmetic genus-two source package.

The mathematical object is the exact Nazarenko octagon specialization

    (a, alpha) = (exp(-1/10), pi/4).

The builder replays its analytic SU(1,1) generators at high precision, checks
the published relator, records a Takeuchi trace-field obstruction to
arithmeticity, and proves the four side-pairing owners primitive through the
surface-group abelianization.  Decimal matrices are verification surfaces, not
the definition.  No common cutoff, orbit census, magnetic comparison, target
data, determinant, or Route-B action is permitted here.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path
from typing import Sequence

import mpmath as mp


SCHEMA_VERSION = "p28_round7_nonarithmetic_control_source_package/1.0"
SURFACE_ID = "NAZARENKO-EXP-OCTAGON-G2"
SURFACE_NAME = "Nazarenko exponential octagon genus-two control"
ACCESS_DATE = "2026-08-28"
WORKING_DPS = 140
OUTPUT_DIGITS = 110
FREEZE_PATH = (
    Path(__file__).resolve().parents[1]
    / "notes"
    / "round7_nonarithmetic_source_package_freeze.md"
)
EXPECTED_FREEZE_SHA256 = (
    "efdbeca3611b92863e1e8b8b1769a7d18c2ac4d839001275afb5b8db09c9255a"
)

REMOTE_SOURCE_SHA256 = {
    "nazarenko_arxiv_source_tar_v1": (
        "9d19d6408c1f6a38374b1d9085382213bf4285acaea09cb3657743eb4f44e38b"
    ),
    "nazarenko_tex_v1": (
        "657cc5245a5c12c610f1c90f41c4b10df59b949f662301b3275ecd2823bc9af0"
    ),
    "takeuchi_jstage_pdf": (
        "6fe5afdf2c02846ee8113ea2cb6f125d6807d2fce07c77feae4d71d6d3b8c048"
    ),
    "popescu_arxiv_source_gzip_v2": (
        "f002fe96c0f4e80ce7ed7fd23a69b88536df831883cbb9152904b85c6e62289d"
    ),
    "popescu_tex_v2": (
        "f6f54e01739755614ea1a4b85c7f902a315911d1478119383b6dc65a0f136c03"
    ),
}

SOURCE_FIELDS = (
    "source_id",
    "citation",
    "year",
    "publication_type",
    "peer_review_status",
    "source_tier",
    "evidence_design_level",
    "overall_grade",
    "doi_or_identifier",
    "primary_locator",
    "verification_locator",
    "existence_verdict",
    "original_content_accessed",
    "content_sha256",
    "claim_support",
    "claim_boundary",
    "predatory_venue_alert",
    "conflict_of_interest_assessment",
    "access_date",
    "inclusion",
)

REQUIREMENT_NAMES = (
    "named_closed_genus2_constant_curvature_surface",
    "explicit_torsion_free_cocompact_fuchsian_matrices",
    "presentation_and_checked_group_relation",
    "primary_or_peer_reviewed_source_locator",
    "independent_nonarithmeticity_certificate",
    "rigorous_systole_or_per_owner_primitivity_certificate",
)

FORBIDDEN_TRUE_FIELDS = (
    "common_geometric_cutoff_frozen",
    "census_run",
    "comparison_run",
    "target_data_used",
    "arithmetic_labels_assigned",
    "dynamical_zeta_defined",
    "a2_evaluation_run",
    "route_b_invocation_allowed",
)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_rows() -> list[dict[str, str]]:
    """Return the frozen source-verification matrix."""

    return [
        {
            "source_id": "S1-NAZARENKO-2013",
            "citation": (
                "Nazarenko, A. V. (2013). Two-parametric hyperbolic octagons "
                "and reduced Teichmuller space in genus two. arXiv:1301.5446v1."
            ),
            "year": "2013",
            "publication_type": "PRIMARY_AUTHOR_PREPRINT",
            "peer_review_status": "NOT_CONFIRMED",
            "source_tier": "tier_3_academic_not_peer_reviewed",
            "evidence_design_level": "VI_SINGLE_THEORETICAL_PRIMARY_SOURCE",
            "overall_grade": "B_USE_WITH_PREPRINT_CAVEAT",
            "doi_or_identifier": "arXiv:1301.5446v1",
            "primary_locator": "https://arxiv.org/abs/1301.5446v1",
            "verification_locator": (
                "https://export.arxiv.org/api/query?id_list=1301.5446"
            ),
            "existence_verdict": "VERIFIED_OFFICIAL_ARXIV_RECORD_AND_SOURCE",
            "original_content_accessed": "YES_TEX_SOURCE",
            "content_sha256": REMOTE_SOURCE_SHA256[
                "nazarenko_arxiv_source_tar_v1"
            ],
            "claim_support": (
                "Equations (10)-(16): admissible two-parameter octagon, closed "
                "genus-two quotient, side-pairing presentation, and explicit "
                "SU(1,1) generators."
            ),
            "claim_boundary": (
                "Does not classify the chosen specialization as non-arithmetic "
                "and does not prove its systole."
            ),
            "predatory_venue_alert": "NONE_ARXIV_REPOSITORY_NOT_A_JOURNAL",
            "conflict_of_interest_assessment": (
                "NO_FINANCIAL_CONFLICT_FOUND;NORMAL_INTELLECTUAL_SELF_AUTHORSHIP"
            ),
            "access_date": ACCESS_DATE,
            "inclusion": "INCLUDED_PRIMARY_REPRESENTATION_SOURCE",
        },
        {
            "source_id": "S2-AIGON-DUPUY-ET-AL-2005",
            "citation": (
                "Aigon-Dupuy, A., Buser, P., Cibils, M., Künzle, A. F., & "
                "Steiner, F. (2005). Hyperbolic octagons and Teichmüller space "
                "in genus 2. Journal of Mathematical Physics, 46(3), 033513."
            ),
            "year": "2005",
            "publication_type": "JOURNAL_ARTICLE",
            "peer_review_status": "REVIEWED_EPFL_METADATA",
            "source_tier": "tier_2_peer_reviewed",
            "evidence_design_level": "VI_THEORETICAL_CONSTRUCTION",
            "overall_grade": "A_FIELD_STANDARD_PEER_REVIEWED",
            "doi_or_identifier": "10.1063/1.1850177",
            "primary_locator": "https://doi.org/10.1063/1.1850177",
            "verification_locator": (
                "https://infoscience.epfl.ch/entities/publication/"
                "eb38a039-e625-41a3-a9a6-4fb5a81f7d7d"
            ),
            "existence_verdict": "VERIFIED_CROSSREF_AND_EPFL_OFFICIAL_METADATA",
            "original_content_accessed": "NO_METADATA_ONLY",
            "content_sha256": "NOT_APPLICABLE_METADATA_ONLY",
            "claim_support": (
                "Independent peer-reviewed family-level corroboration that "
                "geodesic octagons and associated isometry-group generators "
                "model compact genus-two Teichmüller space."
            ),
            "claim_boundary": (
                "Metadata/abstract only in this audit; exact Round-7 matrices "
                "are sourced to S1 rather than inferred from this record."
            ),
            "predatory_venue_alert": "NONE_ESTABLISHED_AIP_JOURNAL",
            "conflict_of_interest_assessment": (
                "NO_FINANCIAL_CONFLICT_FOUND;NORMAL_INTELLECTUAL_SELF_AUTHORSHIP"
            ),
            "access_date": ACCESS_DATE,
            "inclusion": "INCLUDED_PEER_REVIEWED_FAMILY_CORROBORATION",
        },
        {
            "source_id": "S3-TAKEUCHI-1975",
            "citation": (
                "Takeuchi, K. (1975). A characterization of arithmetic Fuchsian "
                "groups. Journal of the Mathematical Society of Japan, 27(4), "
                "600-612."
            ),
            "year": "1975",
            "publication_type": "JOURNAL_ARTICLE",
            "peer_review_status": "PEER_REVIEWED",
            "source_tier": "tier_2_peer_reviewed_foundational",
            "evidence_design_level": "VI_PRIMARY_MATHEMATICAL_THEOREM",
            "overall_grade": "A_FOUNDATIONAL_PRIMARY_THEOREM",
            "doi_or_identifier": "10.2969/jmsj/02740600",
            "primary_locator": "https://doi.org/10.2969/jmsj/02740600",
            "verification_locator": (
                "https://www.jstage.jst.go.jp/article/jmath1948/27/4/"
                "27_4_600/_pdf/-char/en"
            ),
            "existence_verdict": "VERIFIED_PUBLISHER_METADATA_DOI_AND_FULL_PDF",
            "original_content_accessed": "YES_PUBLISHER_PDF",
            "content_sha256": REMOTE_SOURCE_SHA256["takeuchi_jstage_pdf"],
            "claim_support": (
                "Theorem 1: an arithmetic cofinite Fuchsian group must have an "
                "algebraic-number trace field with integral traces, plus the "
                "stated bounded-embedding condition."
            ),
            "claim_boundary": (
                "Supplies the arithmeticity criterion, not the octagon "
                "representation or the transcendence calculation."
            ),
            "predatory_venue_alert": (
                "NONE_MATHEMATICAL_SOCIETY_OF_JAPAN_PUBLISHER_RECORD"
            ),
            "conflict_of_interest_assessment": "NO_CONFLICT_FOUND",
            "access_date": ACCESS_DATE,
            "inclusion": "INCLUDED_INDEPENDENT_ARITHMETICITY_CRITERION",
        },
        {
            "source_id": "S4-POPESCU-2024",
            "citation": (
                "Popescu, S. A. (2024). A simple and self-contained proof for "
                "the Lindemann-Weierstrass theorem. In New Frontiers in Number "
                "Theory and Applications (pp. 349-366). Birkhäuser."
            ),
            "year": "2024",
            "publication_type": "PUBLISHED_BOOK_CHAPTER_WITH_AUTHOR_PREPRINT",
            "peer_review_status": "REVIEW_STATUS_NOT_INDEPENDENTLY_CONFIRMED",
            "source_tier": "tier_3_published_review_status_unconfirmed",
            "evidence_design_level": "VI_PRIMARY_MATHEMATICAL_PROOF",
            "overall_grade": "B_USE_WITH_REVIEW_STATUS_CAVEAT",
            "doi_or_identifier": "10.1007/978-3-031-51959-8_16",
            "primary_locator": "https://doi.org/10.1007/978-3-031-51959-8_16",
            "verification_locator": "https://arxiv.org/abs/2306.14352v2",
            "existence_verdict": "VERIFIED_CROSSREF_SPRINGER_AND_AUTHOR_SOURCE",
            "original_content_accessed": "YES_AUTHOR_TEX_SOURCE_V2",
            "content_sha256": REMOTE_SOURCE_SHA256[
                "popescu_arxiv_source_gzip_v2"
            ],
            "claim_support": (
                "Corollary 3.2: exp(alpha) is transcendental for every nonzero "
                "algebraic alpha; this supplies the exact transcendence input "
                "used at alpha=-1/5."
            ),
            "claim_boundary": (
                "Supplies only the Lindemann-Weierstrass input, not the octagon "
                "representation, trace algebra, or arithmeticity criterion."
            ),
            "predatory_venue_alert": "NONE_SPRINGER_BIRKHAUSER_BOOK_CHAPTER",
            "conflict_of_interest_assessment": "NO_CONFLICT_FOUND",
            "access_date": ACCESS_DATE,
            "inclusion": "INCLUDED_TRANSCENDENCE_THEOREM_SOURCE",
        },
    ]


def source_package_preflight(
    sources: Sequence[dict[str, str]],
) -> dict[str, object]:
    """Decide the six source-only requirements before constructing geometry."""

    by_id = {source["source_id"]: source for source in sources}
    nazarenko = by_id.get("S1-NAZARENKO-2013", {})
    corroboration = by_id.get("S2-AIGON-DUPUY-ET-AL-2005", {})
    takeuchi = by_id.get("S3-TAKEUCHI-1975", {})
    popescu = by_id.get("S4-POPESCU-2024", {})
    freeze_locked = (
        FREEZE_PATH.is_file()
        and sha256_file(FREEZE_PATH) == EXPECTED_FREEZE_SHA256
    )
    checks = {
        "named_closed_genus2_constant_curvature_surface": (
            nazarenko.get("existence_verdict")
            == "VERIFIED_OFFICIAL_ARXIV_RECORD_AND_SOURCE"
            and "closed genus-two quotient"
            in nazarenko.get("claim_support", "")
        ),
        "explicit_torsion_free_cocompact_fuchsian_matrices": (
            nazarenko.get("content_sha256")
            == REMOTE_SOURCE_SHA256["nazarenko_arxiv_source_tar_v1"]
            and "explicit SU(1,1) generators" in nazarenko.get("claim_support", "")
        ),
        "presentation_and_checked_group_relation": (
            freeze_locked
            and "side-pairing presentation" in nazarenko.get("claim_support", "")
        ),
        "primary_or_peer_reviewed_source_locator": (
            nazarenko.get("primary_locator") == "https://arxiv.org/abs/1301.5446v1"
            and corroboration.get("doi_or_identifier") == "10.1063/1.1850177"
            and corroboration.get("source_tier") == "tier_2_peer_reviewed"
        ),
        "independent_nonarithmeticity_certificate": (
            freeze_locked
            and takeuchi.get("doi_or_identifier") == "10.2969/jmsj/02740600"
            and takeuchi.get("original_content_accessed") == "YES_PUBLISHER_PDF"
            and popescu.get("doi_or_identifier")
            == "10.1007/978-3-031-51959-8_16"
            and popescu.get("original_content_accessed")
            == "YES_AUTHOR_TEX_SOURCE_V2"
        ),
        "rigorous_systole_or_per_owner_primitivity_certificate": (
            freeze_locked
            and "presentation" in nazarenko.get("claim_support", "")
        ),
    }
    satisfied = sum(checks.values())
    ready = satisfied == len(REQUIREMENT_NAMES)
    return {
        "schema": "p28_round7_source_only_pregeometry_gate/1.0",
        "status": "PASS_READY_6_OF_6" if ready else "FAIL_CLOSED_NOT_READY",
        "requirements": {
            name: {"status": "PASS" if checks[name] else "FAIL"}
            for name in REQUIREMENT_NAMES
        },
        "requirements_satisfied": satisfied,
        "requirements_total": len(REQUIREMENT_NAMES),
        "pre_geometry_authorization": ready,
        "geometry_selected": False,
        "matrices_loaded": False,
        "common_geometric_cutoff_frozen": False,
        "comparison_run": False,
    }


def matrix_multiply(left: mp.matrix, right: mp.matrix) -> mp.matrix:
    return left * right


def matrix_inverse_det_one(matrix: mp.matrix) -> mp.matrix:
    return mp.matrix(
        [
            [matrix[1, 1], -matrix[0, 1]],
            [-matrix[1, 0], matrix[0, 0]],
        ]
    )


def identity_matrix() -> mp.matrix:
    return mp.matrix([[1, 0], [0, 1]])


def max_matrix_residual(left: mp.matrix, right: mp.matrix) -> mp.mpf:
    return max(abs(left[row, col] - right[row, col]) for row in range(2) for col in range(2))


def number_text(value: mp.mpf | mp.mpc) -> str:
    if isinstance(value, mp.mpc):
        if abs(value.imag) > mp.mpf("1e-130"):
            raise ValueError("number_text expects a real value")
        value = value.real
    return mp.nstr(value, OUTPUT_DIGITS, strip_zeros=False)


def complex_payload(value: mp.mpf | mp.mpc) -> dict[str, str]:
    complex_value = mp.mpc(value)
    real = mp.mpf("0") if abs(complex_value.real) < mp.mpf("1e-130") else complex_value.real
    imag = mp.mpf("0") if abs(complex_value.imag) < mp.mpf("1e-130") else complex_value.imag
    return {"re": number_text(real), "im": number_text(imag)}


def matrix_payload(matrix: mp.matrix) -> list[list[dict[str, str]]]:
    return [
        [complex_payload(matrix[row, col]) for col in range(2)]
        for row in range(2)
    ]


def build_geometry() -> dict[str, object]:
    """Instantiate the exact formulas at high precision after the frozen gate."""

    mp.mp.dps = WORKING_DPS
    a = mp.exp(-mp.mpf(1) / 10)
    x = a * a
    alpha = mp.pi / 4
    alpha_tilde = mp.mpf(0)
    b = 1 / (mp.sqrt(2) * a)
    normalization = -1 / mp.sqrt((1 - x) * (2 * x - 1))
    imaginary = mp.j
    g0 = normalization * mp.matrix(
        [[a, x + imaginary * (1 - x)], [x - imaginary * (1 - x), a]]
    )
    g1 = normalization * mp.matrix(
        [[a, (1 - x) + imaginary * x], [(1 - x) - imaginary * x, a]]
    )
    rotation = mp.matrix(
        [[mp.exp(imaginary * mp.pi / 4), 0], [0, mp.exp(-imaginary * mp.pi / 4)]]
    )
    rotation_inverse = matrix_inverse_det_one(rotation)
    g2 = rotation * g0 * rotation_inverse
    g3 = rotation * g1 * rotation_inverse
    generators = [g0, g1, g2, g3]

    relation_factors = (
        g0,
        matrix_inverse_det_one(g1),
        g2,
        matrix_inverse_det_one(g3),
        matrix_inverse_det_one(g0),
        g1,
        matrix_inverse_det_one(g2),
        g3,
    )
    relation = identity_matrix()
    for factor in relation_factors:
        relation = matrix_multiply(relation, factor)

    beta = mp.atan((1 - x) * 2 * x / (2 * x - 1))
    angle_sum = 4 * beta + 4 * (mp.pi / 2 - beta)
    common_trace = g0[0, 0] + g0[1, 1]
    trace_square_formula = 4 * x / ((1 - x) * (2 * x - 1))
    trace_of_square = common_trace**2 - 2

    determinant_residuals = [abs(mp.det(generator) - 1) for generator in generators]
    su11_residuals = []
    for generator in generators:
        su11_residuals.append(
            max(
                abs(generator[1, 0] - mp.conj(generator[0, 1])),
                abs(generator[1, 1] - mp.conj(generator[0, 0])),
                abs(abs(generator[0, 0]) ** 2 - abs(generator[0, 1]) ** 2 - 1),
            )
        )

    return {
        "a": a,
        "x": x,
        "alpha": alpha,
        "alpha_tilde": alpha_tilde,
        "b": b,
        "normalization": normalization,
        "beta": beta,
        "angle_sum": angle_sum,
        "generators": generators,
        "relation": relation,
        "relation_residual": max_matrix_residual(relation, identity_matrix()),
        "determinant_residuals": determinant_residuals,
        "su11_residuals": su11_residuals,
        "common_trace": common_trace,
        "trace_square_formula": trace_square_formula,
        "trace_of_square": trace_of_square,
    }


def matrices_artifact(
    geometry: dict[str, object], preflight: dict[str, object]
) -> dict[str, object]:
    generators = geometry["generators"]
    if not isinstance(generators, list):
        raise TypeError("generators must be a list")
    return {
        "schema": "p28_round7_nonarithmetic_control_matrices/1.0",
        "surface_id": SURFACE_ID,
        "surface_name": SURFACE_NAME,
        "evidence_token": "PROVED",
        "definition": {
            "parameter_a": "exp(-1/10)",
            "parameter_alpha": "pi/4",
            "parameter_alpha_tilde": "0",
            "parameter_b": "1/(sqrt(2)*exp(-1/10))",
            "parameter_x": "exp(-1/5)",
            "normalization_N": "-1/sqrt((1-x)(2x-1))",
            "rotation_R": "diag(exp(i*pi/4),exp(-i*pi/4))",
            "g0": "N[[a,x+i(1-x)],[x-i(1-x),a]]",
            "g1": "N[[a,(1-x)+i*x],[(1-x)-i*x,a]]",
            "g2": "R*g0*R^-1",
            "g3": "R*g1*R^-1",
            "relator": "g0*g1^-1*g2*g3^-1*g0^-1*g1*g2^-1*g3",
        },
        "decimal_parameters": {
            "a": number_text(geometry["a"]),
            "b": number_text(geometry["b"]),
            "alpha": number_text(geometry["alpha"]),
            "beta": number_text(geometry["beta"]),
            "normalization_N": number_text(geometry["normalization"]),
        },
        "decimal_generators": {
            f"g{index}": matrix_payload(generator)
            for index, generator in enumerate(generators)
        },
        "replay": {
            "working_decimal_precision": WORKING_DPS,
            "display_digits": OUTPUT_DIGITS,
            "max_determinant_residual": number_text(
                max(geometry["determinant_residuals"])
            ),
            "max_su11_residual": number_text(max(geometry["su11_residuals"])),
            "relator_max_entry_residual": number_text(
                geometry["relation_residual"]
            ),
            "angle_sum_residual_from_2pi": number_text(
                abs(geometry["angle_sum"] - 2 * mp.pi)
            ),
            "common_generator_trace": number_text(geometry["common_trace"]),
            "trace_square": number_text(geometry["common_trace"] ** 2),
            "trace_of_g0_square": number_text(geometry["trace_of_square"]),
            "all_generators_hyperbolic": all(
                abs(generator[0, 0] + generator[1, 1]) > 2
                for generator in generators
            ),
        },
        "source_binding": {
            "primary_source": "arXiv:1301.5446v1_equations_10_through_16",
            "pre_geometry_gate_status": preflight["status"],
            "freeze_sha256": EXPECTED_FREEZE_SHA256,
            "remote_source_sha256": REMOTE_SOURCE_SHA256,
        },
        "claim_boundary": (
            "Exact analytic formulas define the matrices; decimal replay does "
            "not independently prove discreteness or faithfulness. Those "
            "properties enter through the source's admissible fundamental-"
            "octagon construction."
        ),
    }


def gate_artifact(
    geometry: dict[str, object], preflight: dict[str, object]
) -> dict[str, object]:
    numerical_pass = (
        max(geometry["determinant_residuals"]) < mp.mpf("1e-120")
        and max(geometry["su11_residuals"]) < mp.mpf("1e-120")
        and geometry["relation_residual"] < mp.mpf("1e-120")
        and abs(geometry["angle_sum"] - 2 * mp.pi) < mp.mpf("1e-130")
    )
    admissible = 1 / mp.sqrt(2) < geometry["a"] < 1 and 0 < geometry["b"] < 1
    hyperbolic = abs(geometry["common_trace"]) > 2
    requirements = {
        "named_closed_genus2_constant_curvature_surface": {
            "status": preflight["requirements"][
                "named_closed_genus2_constant_curvature_surface"
            ]["status"],
            "evidence": (
                "Stable project name plus exact Nazarenko admissible-octagon "
                "specialization; source equations (10)-(12) identify the closed "
                "curvature-minus-one genus-two quotient."
            ),
            "sources": ["S1-NAZARENKO-2013", "S2-AIGON-DUPUY-ET-AL-2005"],
        },
        "explicit_torsion_free_cocompact_fuchsian_matrices": {
            "status": (
                "PASS"
                if preflight["pre_geometry_authorization"]
                and admissible
                and hyperbolic
                and numerical_pass
                else "FAIL"
            ),
            "evidence": (
                "Exact equations (13)-(16) specialized at the admissible point; "
                "the source fundamental-octagon construction supplies discrete, "
                "faithful, torsion-free cocompact side pairings, while this "
                "builder independently replays SU(1,1) and hyperbolicity."
            ),
            "sources": ["S1-NAZARENKO-2013"],
        },
        "presentation_and_checked_group_relation": {
            "status": (
                "PASS"
                if preflight["pre_geometry_authorization"] and numerical_pass
                else "FAIL"
            ),
            "evidence": (
                "Source equation (12) presentation; 140-decimal independent "
                "matrix-product replay below the frozen 1e-120 threshold."
            ),
            "sources": ["S1-NAZARENKO-2013"],
        },
        "primary_or_peer_reviewed_source_locator": {
            "status": preflight["requirements"][
                "primary_or_peer_reviewed_source_locator"
            ]["status"],
            "evidence": (
                "Official arXiv v1 primary-source record and retrieved source "
                "bytes; independent peer-reviewed DOI and EPFL metadata for the "
                "hyperbolic-octagon representation family."
            ),
            "sources": ["S1-NAZARENKO-2013", "S2-AIGON-DUPUY-ET-AL-2005"],
        },
        "independent_nonarithmeticity_certificate": {
            "status": preflight["requirements"][
                "independent_nonarithmeticity_certificate"
            ]["status"],
            "evidence": (
                "For x=exp(-1/5), tr(g0)^2=4x/((1-x)(2x-1)) is "
                "transcendental: algebraicity would make x algebraic via the "
                "displayed nonzero quadratic. Hence tr(g0^2)=tr(g0)^2-2 is a "
                "transcendental trace in Gamma^(2). The square subgroup has "
                "finite index because Gamma is finitely generated, and "
                "arithmeticity is stable under finite-index commensurability. "
                "After Cayley conjugation to SL(2,R), Takeuchi Theorem 1 "
                "applied to Gamma^(2) requires its trace field to be an "
                "algebraic number field for arithmeticity."
            ),
            "sources": [
                "S1-NAZARENKO-2013",
                "S3-TAKEUCHI-1975",
                "S4-POPESCU-2024",
            ],
            "witness": {
                "x": "exp(-1/5)",
                "trace_square": "4x/((1-x)(2x-1))",
                "square_subgroup_trace": "tr(g0^2)=trace_square-2",
                "contradiction_polynomial": "-2*t2*x^2+(3*t2-4)*x-t2",
                "contradiction_polynomial_nonzero_reason": (
                    "if t2 is nonzero its constant coefficient is nonzero; "
                    "if t2=0 the polynomial is -4*x"
                ),
                "transcendence_input": (
                    "Lindemann-Weierstrass: exp(nonzero algebraic) is transcendental"
                ),
                "takeuchi_condition_failed": (
                    "Q(traces of the square subgroup) is an algebraic number "
                    "field of finite degree"
                ),
                "square_subgroup_definition": "Gamma^(2)=<gamma^2:gamma in Gamma>",
                "square_subgroup_finite_index_reason": (
                    "Gamma/Gamma^(2) is a finitely generated elementary "
                    "abelian 2-group"
                ),
                "arithmeticity_transfer": (
                    "arithmeticity is invariant under commensurability, so an "
                    "arithmetic Gamma would make finite-index Gamma^(2) arithmetic"
                ),
                "real_model_bridge": "Cayley-conjugate SU(1,1) to SL(2,R)",
                "takeuchi_application_owner": "FINITE_COVOLUME_GAMMA_SQUARE_SUBGROUP",
            },
        },
        "rigorous_systole_or_per_owner_primitivity_certificate": {
            "status": preflight["requirements"][
                "rigorous_systole_or_per_owner_primitivity_certificate"
            ]["status"],
            "evidence": (
                "The sole relator has zero exponent sums, so abelianization is "
                "Z^4 and [g_j]=e_j. A proper power would make e_j divisible by "
                "n>=2, impossible. If g_i were conjugate to g_j or g_j^-1, "
                "abelianization would give e_i=e_j or -e_j, impossible for "
                "i!=j. This proves four distinct inverse-paired primitive "
                "owners and does not assert a systole."
            ),
            "sources": ["S1-NAZARENKO-2013"],
            "owners": [
                {
                    "owner_id": f"NAEXP-G{index}",
                    "element": f"g{index}",
                    "abelianization": [1 if component == index else 0 for component in range(4)],
                    "certificate": "NOT_A_PROPER_POWER_BY_PRIMITIVE_Z4_CLASS",
                }
                for index in range(4)
            ],
            "pairwise_unoriented_owner_distinct": True,
            "owner_distinctness_certificate": (
                "E_I_NOT_EQUAL_TO_PLUS_OR_MINUS_E_J_IN_Z4_FOR_I_NOT_EQUAL_J"
            ),
            "systole_claimed": False,
        },
    }
    satisfied = sum(
        requirement["status"] == "PASS" for requirement in requirements.values()
    )
    ready = satisfied == len(REQUIREMENT_NAMES)
    return {
        "schema": "p28_round7_nonarithmetic_source_package_gate/1.0",
        "status": "PASS_READY_6_OF_6" if ready else "FAIL_CLOSED_NOT_READY",
        "evidence_token": "PROVED" if ready else "OPEN",
        "surface_id": SURFACE_ID,
        "surface_name": SURFACE_NAME,
        "pre_geometry_source_gate": preflight,
        "requirements": requirements,
        "requirements_satisfied": satisfied,
        "requirements_total": len(REQUIREMENT_NAMES),
        "source_package_supplied": ready,
        "geometry_selected": ready,
        "matrices_loaded": ready,
        "nonarithmeticity_verified": ready,
        "per_owner_primitivity_verified": ready,
        "systole_verified": False,
        "control_instantiation_authorized": ready,
        "execution": {
            "common_geometric_cutoff_frozen": False,
            "census_run": False,
            "comparison_run": False,
            "target_data_used": False,
            "arithmetic_labels_assigned": False,
            "dynamical_zeta_defined": False,
            "a2_evaluation_run": False,
            "route_b_invocation_allowed": False,
        },
        "formal_full_candidate_route_a_tuple": "UNASSIGNED",
        "bounded_proxy_tuple": ["A0_WEAK_ARITHMETIC_RELATION", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
        "bounded_proxy_overall": "ROUTE_A_EXPLORATORY",
        "next_authorized_step": (
            "Prove a control systole/lower-bound or finite word-to-length "
            "completeness certificate sufficient to choose one common geometric "
            "cutoff Lambda; only then freeze Lambda and run a target-blind census."
            if ready
            else "Repair every failed source-package requirement before geometry selection."
        ),
        "claim_boundary": (
            "The six-item source package is ready and the named control is "
            "proved non-arithmetic with four certified primitive side-pairing "
            "owners. No systole, common-cutoff census, magnetic comparison, "
            "arithmetic discrimination, determinant, full Route-A promotion, "
            "or Route-B readiness is claimed."
            if ready
            else "No control geometry or comparison is authorized."
        ),
    }


def validate(
    sources: Sequence[dict[str, str]],
    geometry: dict[str, object],
    matrices: dict[str, object],
    gate: dict[str, object],
) -> dict[str, object]:
    errors: list[str] = []
    freeze_sha256 = sha256_file(FREEZE_PATH)
    if freeze_sha256 != EXPECTED_FREEZE_SHA256:
        errors.append("Round-7 freeze digest mismatch")

    if len(sources) != 4 or len({row["source_id"] for row in sources}) != 4:
        errors.append("source matrix must contain four unique included sources")
    if {row["access_date"] for row in sources} != {ACCESS_DATE}:
        errors.append("source access dates changed")
    if any(row["inclusion"].startswith("INCLUDED") is False for row in sources):
        errors.append("source inclusion matrix contains a non-included row")
    if any(row["predatory_venue_alert"].startswith("NONE") is False for row in sources):
        errors.append("source matrix contains a predatory-venue alert")

    if not (1 / mp.sqrt(2) < geometry["a"] < 1):
        errors.append("parameter a is outside the source admissibility domain")
    if not (0 < geometry["b"] < 1):
        errors.append("parameter b is outside the unit disk")
    if geometry["alpha_tilde"] != 0:
        errors.append("alpha_tilde changed")
    if max(geometry["determinant_residuals"]) >= mp.mpf("1e-120"):
        errors.append("determinant replay failed")
    if max(geometry["su11_residuals"]) >= mp.mpf("1e-120"):
        errors.append("SU(1,1) replay failed")
    if geometry["relation_residual"] >= mp.mpf("1e-120"):
        errors.append("published group relator replay failed")
    if abs(geometry["angle_sum"] - 2 * mp.pi) >= mp.mpf("1e-130"):
        errors.append("octagon angle sum replay failed")
    if abs(geometry["common_trace"]) <= 2:
        errors.append("source generators are not hyperbolic")
    if abs(geometry["common_trace"] ** 2 - geometry["trace_square_formula"]) >= mp.mpf("1e-130"):
        errors.append("trace-square identity failed")

    requirements = gate.get("requirements")
    if not isinstance(requirements, dict) or tuple(requirements) != REQUIREMENT_NAMES:
        errors.append("six-item requirement schema changed")
    elif any(requirement.get("status") != "PASS" for requirement in requirements.values()):
        errors.append("one or more source-package requirements failed")
    if gate.get("requirements_satisfied") != 6 or gate.get("requirements_total") != 6:
        errors.append("six-item gate is not 6/6")
    preflight = gate.get("pre_geometry_source_gate")
    if not isinstance(preflight, dict):
        errors.append("pre-geometry source gate is missing")
    else:
        if preflight.get("status") != "PASS_READY_6_OF_6":
            errors.append("pre-geometry source gate was not 6/6")
        if preflight.get("pre_geometry_authorization") is not True:
            errors.append("pre-geometry source gate did not authorize instantiation")
        if preflight.get("geometry_selected") is not False:
            errors.append("pre-geometry gate selected geometry")
        if preflight.get("matrices_loaded") is not False:
            errors.append("pre-geometry gate loaded matrices")
    for field in (
        "source_package_supplied",
        "geometry_selected",
        "matrices_loaded",
        "nonarithmeticity_verified",
        "per_owner_primitivity_verified",
        "control_instantiation_authorized",
    ):
        if gate.get(field) is not True:
            errors.append(f"post-gate source-package field {field} is not true")
    if gate.get("systole_verified") is not False:
        errors.append("a control systole was fabricated")
    execution = gate.get("execution")
    if not isinstance(execution, dict):
        errors.append("execution firewall is missing")
    else:
        for field in FORBIDDEN_TRUE_FIELDS:
            if execution.get(field) is not False:
                errors.append(f"forbidden execution field {field} is not false")
    if gate.get("formal_full_candidate_route_a_tuple") != "UNASSIGNED":
        errors.append("full-candidate Route-A tuple was assigned")
    if gate.get("bounded_proxy_overall") != "ROUTE_A_EXPLORATORY":
        errors.append("bounded proxy was promoted")

    primitivity = requirements[
        "rigorous_systole_or_per_owner_primitivity_certificate"
    ]
    owners = primitivity.get("owners", [])
    if len(owners) != 4:
        errors.append("four primitive side-pairing owners were not certified")
    for index, owner in enumerate(owners):
        expected = [1 if component == index else 0 for component in range(4)]
        if owner.get("abelianization") != expected:
            errors.append(f"owner g{index} abelianization changed")
        if owner.get("certificate") != "NOT_A_PROPER_POWER_BY_PRIMITIVE_Z4_CLASS":
            errors.append(f"owner g{index} primitivity certificate changed")

    source_payload = json.dumps(list(sources), sort_keys=True, separators=(",", ":")).encode("utf-8")
    matrix_payload_bytes = json.dumps(matrices, sort_keys=True, separators=(",", ":")).encode("utf-8")
    gate_payload = json.dumps(gate, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return {
        "schema": "p28_round7_nonarithmetic_control_validation/1.0",
        "status": "PASS" if not errors else "FAIL",
        "freeze_sha256": freeze_sha256,
        "remote_source_sha256": REMOTE_SOURCE_SHA256,
        "source_count": len(sources),
        "source_matrix_sha256": hashlib.sha256(source_payload).hexdigest(),
        "matrix_payload_sha256": hashlib.sha256(matrix_payload_bytes).hexdigest(),
        "gate_payload_sha256": hashlib.sha256(gate_payload).hexdigest(),
        "source_package_gate": gate["status"],
        "pre_geometry_source_gate": gate["pre_geometry_source_gate"]["status"],
        "requirements_satisfied": gate["requirements_satisfied"],
        "requirements_total": gate["requirements_total"],
        "control_surface_id": SURFACE_ID,
        "matrix_count": len(geometry["generators"]),
        "primitive_owner_count": len(owners),
        "systole_claimed": False,
        "max_determinant_residual": number_text(max(geometry["determinant_residuals"])),
        "max_su11_residual": number_text(max(geometry["su11_residuals"])),
        "relator_max_entry_residual": number_text(geometry["relation_residual"]),
        "trace_square_transcendence_certificate": "PROVED_BY_QUADRATIC_CONTRADICTION_AND_LINDEMANN_WEIERSTRASS",
        "nonarithmeticity_certificate": "PROVED_BY_TAKEUCHI_TRACE_FIELD_NECESSITY",
        "per_owner_primitivity_certificate": "PROVED_FOR_G0_G1_G2_G3_BY_Z4_ABELIANIZATION",
        "common_geometric_cutoff_frozen": False,
        "census_run": False,
        "comparison_run": False,
        "target_data_used": False,
        "arithmetic_labels_assigned": False,
        "formal_full_candidate_route_a_tuple": "UNASSIGNED",
        "bounded_proxy_overall": "ROUTE_A_EXPLORATORY",
        "a2_evaluation": "NOT_RUN",
        "route_b_evaluation": "NOT_RUN",
        "route_b_invocation_allowed": False,
        "errors": errors,
    }


def write_csv(path: Path, rows: Sequence[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=SOURCE_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def write_json(path: Path, payload: dict[str, object]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-matrix-output", required=True, type=Path)
    parser.add_argument("--matrices-output", required=True, type=Path)
    parser.add_argument("--gate-output", required=True, type=Path)
    parser.add_argument("--validation-output", required=True, type=Path)
    arguments = parser.parse_args()

    sources = source_rows()
    preflight = source_package_preflight(sources)
    if preflight["status"] != "PASS_READY_6_OF_6":
        raise RuntimeError(
            "Round-7 source-only preflight failed before geometry construction"
        )
    geometry = build_geometry()
    matrices = matrices_artifact(geometry, preflight)
    gate = gate_artifact(geometry, preflight)
    validation = validate(sources, geometry, matrices, gate)
    if validation["status"] != "PASS":
        raise RuntimeError("Round-7 source-package validation failed: " + "; ".join(validation["errors"]))

    write_csv(arguments.source_matrix_output, sources)
    write_json(arguments.matrices_output, matrices)
    write_json(arguments.gate_output, gate)
    write_json(arguments.validation_output, validation)
    print(
        json.dumps(
            {
                "status": validation["status"],
                "source_package_gate": validation["source_package_gate"],
                "requirements": f"{validation['requirements_satisfied']}/{validation['requirements_total']}",
                "surface_id": validation["control_surface_id"],
                "primitive_owners": validation["primitive_owner_count"],
                "common_cutoff_frozen": validation["common_geometric_cutoff_frozen"],
                "comparison_run": validation["comparison_run"],
                "formal_full_candidate_route_a_tuple": validation["formal_full_candidate_route_a_tuple"],
                "route_b_invocation_allowed": validation["route_b_invocation_allowed"],
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
