#!/usr/bin/env python3
"""Build the P28 Round-8 exact control-systole certificate.

The proof uses Gaussian-integer polynomials in u=exp(-1/10), exact PSU(1,1)
normal forms, and rational interval signs.  A compact-fundamental-polygon
lemma converts the geometric cutoff 21/10 into a finite tile-ball traversal.
No floating-point value is used for a proof decision.
"""

from __future__ import annotations

import argparse
import csv
from collections import deque
from fractions import Fraction
import hashlib
import json
from pathlib import Path
from typing import Iterable, Sequence

import mpmath as mp


SCHEMA = "p28_round8_exact_control_systole_certificate/1.0"
ACCESS_DATE = "2026-08-28"
SURFACE_ID = "NAZARENKO-EXP-OCTAGON-G2"
CUTOFF = Fraction(21, 10)
CENTER_GUARD = 20_000
MAX_STATES = 100_000
FREEZE_PATH = (
    Path(__file__).resolve().parents[1]
    / "notes"
    / "round8_control_systole_completeness_freeze.md"
)
EXPECTED_FREEZE_SHA256 = (
    "b2655431dcc27c471e8da3c092435dbe30c6a483e2244f78543adcd2a3141528"
)

UPSTREAM_LOCKS = {
    "notes/round7_nonarithmetic_source_package_freeze.md": (
        "efdbeca3611b92863e1e8b8b1769a7d18c2ac4d839001275afb5b8db09c9255a"
    ),
    "results/round7_nonarithmetic_control_matrices.json": (
        "a900749b6905a5f324c2e2670363ec1bc9480481f3f5aa1240ed0ebbee55e6ca"
    ),
    "results/round7_nonarithmetic_source_package_gate.json": (
        "0e192fefeb88ffd891b9c20964ddf1f4430bc990ba637d5709b990a2658218cb"
    ),
    "results/round7_nonarithmetic_control_validation.json": (
        "7a9843cf8d472c0968ade948a99a63d840537c6c188f92bbc403275c134034ef"
    ),
    "experiments/round7_reproducibility_receipt.json": (
        "6a6143adfd14b17a167af9a07c983cf22c50f06596d99ab37e64322d4fb05b13"
    ),
}

REMOTE_SOURCE_SHA256 = {
    "nazarenko_arxiv_source_tar_v1": (
        "9d19d6408c1f6a38374b1d9085382213bf4285acaea09cb3657743eb4f44e38b"
    ),
    "voight_numdam_pdf": (
        "2cc4e0cc11e05f17c23cf6e27117968fc2cda31abf4db184ee6d0486bff88ec3"
    ),
    "despre_kolbe_parlier_teillaud_drops_pdf": (
        "edcd2ed17558fba5698a21552796d2b6e92b4d5ec8143be788e1c739abfbda5a"
    ),
}

SOURCE_FIELDS = (
    "source_id",
    "citation",
    "publication_type",
    "peer_review_status",
    "source_tier",
    "overall_grade",
    "identifier",
    "primary_locator",
    "verification_locator",
    "existence_verdict",
    "original_content_accessed",
    "content_sha256",
    "claim_support",
    "claim_boundary",
    "access_date",
    "decision",
    "decision_reason",
)

# A polynomial is a little-endian tuple of Gaussian-integer coefficients.
Gaussian = tuple[int, int]
Polynomial = tuple[Gaussian, ...]
Matrix = tuple[Polynomial, Polynomial, Polynomial, Polynomial]
State = tuple[int, int, Matrix]  # sqrt(Delta) parity, Delta exponent, numerator

ZERO_G: Gaussian = (0, 0)
ZERO: Polynomial = (ZERO_G,)
ONE: Polynomial = ((1, 0),)
U: Polynomial = (ZERO_G, (1, 0))
U2: Polynomial = (ZERO_G, ZERO_G, (1, 0))
I_POLY: Polynomial = ((0, 1),)
DELTA: Polynomial = ((-1, 0), ZERO_G, (3, 0), ZERO_G, (-2, 0))


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_rows() -> list[dict[str, str]]:
    return [
        {
            "source_id": "S1-NAZARENKO-2013",
            "citation": (
                "Nazarenko, A. V. (2013). Two-parametric hyperbolic octagons "
                "and reduced Teichmuller space in genus two. arXiv:1301.5446v1."
            ),
            "publication_type": "PRIMARY_AUTHOR_PREPRINT",
            "peer_review_status": "NOT_CONFIRMED",
            "source_tier": "tier_3_academic_not_peer_reviewed",
            "overall_grade": "B_USE_WITH_PREPRINT_CAVEAT",
            "identifier": "arXiv:1301.5446v1",
            "primary_locator": "https://arxiv.org/abs/1301.5446v1",
            "verification_locator": (
                "https://export.arxiv.org/api/query?id_list=1301.5446"
            ),
            "existence_verdict": "VERIFIED_OFFICIAL_RECORD_AND_TEX_SOURCE",
            "original_content_accessed": "YES_TEX_SOURCE",
            "content_sha256": REMOTE_SOURCE_SHA256[
                "nazarenko_arxiv_source_tar_v1"
            ],
            "claim_support": (
                "Equations (10)-(16) give the compact genus-two fundamental "
                "octagon, opposite-side pairing, presentation, and exact "
                "SU(1,1) generators; the later alternative pants formulas "
                "corroborate the equality-witness length."
            ),
            "claim_boundary": (
                "Does not state or prove the Round-8 systole, finite tile-ball "
                "bound, exact polynomial normal form, or cutoff completeness."
            ),
            "access_date": ACCESS_DATE,
            "decision": "INCLUDE_PRIMARY_GEOMETRY",
            "decision_reason": "Only primary source for the exact chosen representation.",
        },
        {
            "source_id": "S2-VOIGHT-2009",
            "citation": (
                "Voight, J. (2009). Computing fundamental domains for "
                "Fuchsian groups. Journal de Theorie des Nombres de Bordeaux, "
                "21(2), 467-489."
            ),
            "publication_type": "JOURNAL_ARTICLE",
            "peer_review_status": "PEER_REVIEWED",
            "source_tier": "tier_2_peer_reviewed",
            "overall_grade": "A_PEER_REVIEWED_ALGORITHMIC_CONTEXT",
            "identifier": "10.5802/jtnb.683",
            "primary_locator": "https://doi.org/10.5802/jtnb.683",
            "verification_locator": "https://numdam.org/articles/10.5802/jtnb.683/",
            "existence_verdict": "VERIFIED_PUBLISHER_RECORD_AND_PDF",
            "original_content_accessed": "YES_PUBLISHER_PDF",
            "content_sha256": REMOTE_SOURCE_SHA256["voight_numdam_pdf"],
            "claim_support": (
                "The main theorem and Sections 1-4 support the exact-algorithm "
                "setting for finite Fuchsian fundamental domains, side "
                "pairings, presentations, reduction, and word problems."
            ),
            "claim_boundary": (
                "Its exact input class is algebraic; it is contextual and is "
                "not a turnkey certificate for the transcendental control."
            ),
            "access_date": ACCESS_DATE,
            "decision": "INCLUDE_METHOD_CONTEXT",
            "decision_reason": "Authoritative peer-reviewed exact-domain algorithm context.",
        },
        {
            "source_id": "S3-DESPRE-ET-AL-2023",
            "citation": (
                "Despre, V., Kolbe, B., Parlier, H., & Teillaud, M. (2023). "
                "Computing a Dirichlet Domain for a Hyperbolic Surface. SoCG "
                "2023, LIPIcs 258, 27:1-27:15."
            ),
            "publication_type": "PEER_REVIEWED_CONFERENCE_PAPER",
            "peer_review_status": "PEER_REVIEWED",
            "source_tier": "tier_2_peer_reviewed",
            "overall_grade": "A_PEER_REVIEWED_SURFACE_ALGORITHM_CONTEXT",
            "identifier": "10.4230/LIPIcs.SoCG.2023.27",
            "primary_locator": "https://doi.org/10.4230/LIPIcs.SoCG.2023.27",
            "verification_locator": (
                "https://drops.dagstuhl.de/entities/document/"
                "10.4230/LIPIcs.SoCG.2023.27"
            ),
            "existence_verdict": "VERIFIED_OFFICIAL_RECORD_AND_PDF",
            "original_content_accessed": "YES_OFFICIAL_PDF",
            "content_sha256": REMOTE_SOURCE_SHA256[
                "despre_kolbe_parlier_teillaud_drops_pdf"
            ],
            "claim_support": (
                "Abstract and Sections 2-3 support the algorithmic input model "
                "of a closed hyperbolic surface represented by a fundamental "
                "polygon and side pairings."
            ),
            "claim_boundary": (
                "The real-RAM analysis does not supply rational interval signs, "
                "the Round-8 radius lemma, or this systole result."
            ),
            "access_date": ACCESS_DATE,
            "decision": "INCLUDE_METHOD_CONTEXT",
            "decision_reason": "Peer-reviewed polygon-and-side-pairing algorithm context.",
        },
        {
            "source_id": "E1-DELECROIX-ET-AL-2026",
            "citation": (
                "Delecroix, Despre, Lanuel, Parlier, & Teillaud (2026). "
                "Computing an e-net of a closed hyperbolic surface. arXiv:2608.24497."
            ),
            "publication_type": "RECENT_PREPRINT",
            "peer_review_status": "NOT_CONFIRMED",
            "source_tier": "tier_3_academic_not_peer_reviewed",
            "overall_grade": "C_EXCLUDED_RECENT_PREPRINT",
            "identifier": "arXiv:2608.24497",
            "primary_locator": "https://arxiv.org/abs/2608.24497",
            "verification_locator": "https://arxiv.org/abs/2608.24497",
            "existence_verdict": "VERIFIED_OFFICIAL_ARXIV_RECORD",
            "original_content_accessed": "ABSTRACT_AND_RECORD_ONLY",
            "content_sha256": "NOT_RETRIEVED",
            "claim_support": "Potentially relevant algorithms for nets and short geodesics.",
            "claim_boundary": "Posted days before the audit and not independently peer reviewed.",
            "access_date": ACCESS_DATE,
            "decision": "EXCLUDE_FROM_PROOF",
            "decision_reason": "Not needed and review status unavailable.",
        },
        {
            "source_id": "E2-BUSER-1992",
            "citation": (
                "Buser, P. (1992). Geometry and Spectra of Compact Riemann "
                "Surfaces. Birkhauser."
            ),
            "publication_type": "AUTHORITATIVE_MONOGRAPH",
            "peer_review_status": "BOOK_REVIEW_PROCESS_NOT_AUDITED",
            "source_tier": "tier_2_authoritative_secondary",
            "overall_grade": "B_EXCLUDED_CONTENT_NOT_DIRECTLY_AUDITED",
            "identifier": "ISBN:978-0-8176-3406-8",
            "primary_locator": "https://link.springer.com/book/10.1007/978-1-4612-4438-9",
            "verification_locator": "https://doi.org/10.1007/978-1-4612-4438-9",
            "existence_verdict": "VERIFIED_PUBLISHER_METADATA",
            "original_content_accessed": "NO_FULL_TEXT_IN_THIS_AUDIT",
            "content_sha256": "NOT_APPLICABLE_METADATA_ONLY",
            "claim_support": "Standard background cited by the primary octagon source.",
            "claim_boundary": "No page-level content was used for a Round-8 proof step.",
            "access_date": ACCESS_DATE,
            "decision": "EXCLUDE_FROM_PROOF",
            "decision_reason": "Avoid unsupported page-level attribution.",
        },
        {
            "source_id": "E3-PAIR-OF-PANTS-WEB-RESULTS",
            "citation": "Search-result set for hyperbolic pants seams and self-orthogeodesics.",
            "publication_type": "MIXED_WEB_AND_SECONDARY_RESULTS",
            "peer_review_status": "MIXED_OR_UNCONFIRMED",
            "source_tier": "tier_4_unverified_or_secondary",
            "overall_grade": "D_EXCLUDED",
            "identifier": "SEARCH-CLUSTER-2026-08-28",
            "primary_locator": "NOT_APPLICABLE_SEARCH_CLUSTER",
            "verification_locator": "NOT_APPLICABLE_SEARCH_CLUSTER",
            "existence_verdict": "MULTIPLE_RESULTS_INSPECTED",
            "original_content_accessed": "PARTIAL",
            "content_sha256": "NOT_APPLICABLE",
            "claim_support": "Exploratory seam and returning-arc formulas.",
            "claim_boundary": "No source package closed the global gluing/completeness step.",
            "access_date": ACCESS_DATE,
            "decision": "EXCLUDE_FROM_PROOF",
            "decision_reason": "Replaced by the exact finite tile-ball theorem.",
        },
    ]


def poly_trim(poly: Iterable[Gaussian]) -> Polynomial:
    values = list(poly)
    while len(values) > 1 and values[-1] == ZERO_G:
        values.pop()
    return tuple(values) if values else ZERO


def poly_add(left: Polynomial, right: Polynomial) -> Polynomial:
    result: list[Gaussian] = []
    for index in range(max(len(left), len(right))):
        ar, ai = left[index] if index < len(left) else ZERO_G
        br, bi = right[index] if index < len(right) else ZERO_G
        result.append((ar + br, ai + bi))
    return poly_trim(result)


def poly_neg(poly: Polynomial) -> Polynomial:
    return tuple((-real, -imag) for real, imag in poly)


def poly_sub(left: Polynomial, right: Polynomial) -> Polynomial:
    return poly_add(left, poly_neg(right))


def poly_mul(left: Polynomial, right: Polynomial) -> Polynomial:
    result = [[0, 0] for _ in range(len(left) + len(right) - 1)]
    for left_index, (ar, ai) in enumerate(left):
        for right_index, (br, bi) in enumerate(right):
            result[left_index + right_index][0] += ar * br - ai * bi
            result[left_index + right_index][1] += ar * bi + ai * br
    return poly_trim(tuple((real, imag) for real, imag in result))


def poly_conjugate(poly: Polynomial) -> Polynomial:
    return tuple((real, -imag) for real, imag in poly)


def poly_scale(poly: Polynomial, factor: int) -> Polynomial:
    return poly_trim((real * factor, imag * factor) for real, imag in poly)


def poly_pow(poly: Polynomial, exponent: int) -> Polynomial:
    result = ONE
    base = poly
    power = exponent
    while power:
        if power & 1:
            result = poly_mul(result, base)
        base = poly_mul(base, base)
        power //= 2
    return result


def poly_divide_delta(poly: Polynomial) -> Polynomial | None:
    """Return poly/Delta if exact, otherwise None."""

    if poly == ZERO:
        return ZERO
    if len(poly) < len(DELTA):
        return None
    work = [list(coefficient) for coefficient in poly]
    quotient = [[0, 0] for _ in range(len(poly) - 4)]
    for offset in range(len(poly) - 5, -1, -1):
        leading_real, leading_imag = work[offset + 4]
        if leading_real % 2 or leading_imag % 2:
            return None
        coefficient_real = -leading_real // 2
        coefficient_imag = -leading_imag // 2
        quotient[offset] = [coefficient_real, coefficient_imag]
        work[offset][0] += coefficient_real
        work[offset][1] += coefficient_imag
        work[offset + 2][0] -= 3 * coefficient_real
        work[offset + 2][1] -= 3 * coefficient_imag
        work[offset + 4][0] += 2 * coefficient_real
        work[offset + 4][1] += 2 * coefficient_imag
    if any(tuple(coefficient) != ZERO_G for coefficient in work):
        return None
    return poly_trim((real, imag) for real, imag in quotient)


def poly_real_coefficients(poly: Polynomial) -> tuple[int, ...]:
    if any(imag != 0 for _, imag in poly):
        raise ValueError("expected a real polynomial")
    return tuple(real for real, _ in poly)


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    return (
        poly_add(poly_mul(left[0], right[0]), poly_mul(left[1], right[2])),
        poly_add(poly_mul(left[0], right[1]), poly_mul(left[1], right[3])),
        poly_add(poly_mul(left[2], right[0]), poly_mul(left[3], right[2])),
        poly_add(poly_mul(left[2], right[1]), poly_mul(left[3], right[3])),
    )


def matrix_inverse_numerator(matrix: Matrix) -> Matrix:
    return (matrix[3], poly_neg(matrix[1]), poly_neg(matrix[2]), matrix[0])


def canonical_state(parity: int, exponent: int, matrix: Matrix) -> State:
    if parity not in (0, 1) or exponent < 0:
        raise ValueError("invalid denominator state")
    while exponent:
        divided = tuple(poly_divide_delta(entry) for entry in matrix)
        if any(entry is None for entry in divided):
            break
        matrix = tuple(entry for entry in divided if entry is not None)  # type: ignore[assignment]
        exponent -= 1
    first: Gaussian | None = None
    for entry in matrix:
        for coefficient in entry:
            if coefficient != ZERO_G:
                first = coefficient
                break
        if first is not None:
            break
    if first is None:
        raise ValueError("zero matrix has no PSU normal form")
    if first[0] < 0 or (first[0] == 0 and first[1] < 0):
        matrix = tuple(poly_neg(entry) for entry in matrix)  # type: ignore[assignment]
    return parity, exponent, matrix


def multiply_state(state: State, generator: Matrix) -> State:
    parity, exponent, matrix = state
    return canonical_state(
        1 - parity,
        exponent + (1 if parity else 0),
        matrix_multiply(matrix, generator),
    )


def generator_numerators() -> tuple[Matrix, ...]:
    beta0 = poly_add(U2, poly_mul(I_POLY, poly_sub(ONE, U2)))
    beta1 = poly_add(poly_sub(ONE, U2), poly_mul(I_POLY, U2))
    beta2 = poly_mul(I_POLY, beta0)
    beta3 = poly_mul(I_POLY, beta1)

    def generator(beta: Polynomial) -> Matrix:
        return U, beta, poly_conjugate(beta), U

    positive = tuple(generator(beta) for beta in (beta0, beta1, beta2, beta3))
    return positive + tuple(matrix_inverse_numerator(matrix) for matrix in positive)


IDENTITY = canonical_state(0, 0, (ONE, ZERO, ZERO, ONE))
STEP_NAMES = ("g0", "g1", "g2", "g3", "g0^-1", "g1^-1", "g2^-1", "g3^-1")


Interval = tuple[Fraction, Fraction]
_U_INTERVALS: dict[int, Interval] = {}


def interval_add(left: Interval, right: Interval) -> Interval:
    return left[0] + right[0], left[1] + right[1]


def interval_mul(left: Interval, right: Interval) -> Interval:
    products = (
        left[0] * right[0],
        left[0] * right[1],
        left[1] * right[0],
        left[1] * right[1],
    )
    return min(products), max(products)


def interval_reciprocal(interval: Interval) -> Interval:
    if interval[0] <= 0 <= interval[1]:
        raise ZeroDivisionError("interval contains zero")
    return min(1 / interval[0], 1 / interval[1]), max(1 / interval[0], 1 / interval[1])


def interval_divide(left: Interval, right: Interval) -> Interval:
    return interval_mul(left, interval_reciprocal(right))


def interval_pow(interval: Interval, exponent: int) -> Interval:
    result: Interval = (Fraction(1), Fraction(1))
    base = interval
    power = exponent
    while power:
        if power & 1:
            result = interval_mul(result, base)
        base = interval_mul(base, base)
        power //= 2
    return result


def u_interval(order: int) -> Interval:
    """Alternating-series enclosure for exp(-1/10)."""

    even_order = order if order % 2 == 0 else order + 1
    if even_order not in _U_INTERVALS:
        term = Fraction(1)
        partial = Fraction(1)
        values = {0: partial}
        for index in range(1, even_order + 2):
            term *= Fraction(-1, 10 * index)
            partial += term
            values[index] = partial
        _U_INTERVALS[even_order] = (values[even_order + 1], values[even_order])
    return _U_INTERVALS[even_order]


def evaluate_real_poly_interval(coefficients: Sequence[int], interval: Interval) -> Interval:
    result: Interval = (Fraction(0), Fraction(0))
    for coefficient in reversed(coefficients):
        result = interval_add(
            interval_mul(result, interval),
            (Fraction(coefficient), Fraction(coefficient)),
        )
    return result


SIGN_ORDERS = (24, 36, 54, 80, 120, 180)


def certified_poly_sign(poly: Polynomial) -> tuple[int, int, Interval]:
    """Return sign, Taylor order, and enclosing interval."""

    coefficients = poly_real_coefficients(poly)
    if all(coefficient == 0 for coefficient in coefficients):
        return 0, 0, (Fraction(0), Fraction(0))
    for order in SIGN_ORDERS:
        enclosure = evaluate_real_poly_interval(coefficients, u_interval(order))
        if enclosure[1] < 0:
            return -1, order, enclosure
        if enclosure[0] > 0:
            return 1, order, enclosure
    raise ArithmeticError("adaptive rational interval could not resolve polynomial sign")


def exp_positive_interval(argument: Fraction, terms: int = 120) -> Interval:
    if argument < 0:
        raise ValueError("argument must be nonnegative")
    term = Fraction(1)
    partial = Fraction(1)
    for index in range(1, terms + 1):
        term *= argument / index
        partial += term
    next_term = term * argument / (terms + 1)
    ratio = argument / (terms + 2)
    if ratio >= 1:
        raise ArithmeticError("Taylor tail ratio is not contractive")
    return partial, partial + next_term / (1 - ratio)


def exp_interval(argument: Fraction) -> Interval:
    if argument >= 0:
        return exp_positive_interval(argument)
    return interval_reciprocal(exp_positive_interval(-argument))


def cosh_interval(argument: Fraction) -> Interval:
    return (
        interval_add(exp_interval(argument), exp_interval(-argument))[0] / 2,
        interval_add(exp_interval(argument), exp_interval(-argument))[1] / 2,
    )


def fraction_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def decimal_interval(interval: Interval, digits: int = 28) -> list[str]:
    mp.mp.dps = digits + 10
    return [
        mp.nstr(mp.mpf(value.numerator) / value.denominator, digits)
        for value in interval
    ]


def proof_guards() -> dict[str, object]:
    ui = u_interval(80)
    u2i = interval_mul(ui, ui)
    u4i = interval_mul(u2i, u2i)

    alternating_vertex_is_inner = u4i[0] > Fraction(1, 2)

    exp3 = exp_interval(Fraction(3))
    tanh_three_halves = interval_divide(
        interval_add(exp3, (Fraction(-1), Fraction(-1))),
        interval_add(exp3, (Fraction(1), Fraction(1))),
    )
    diameter_pass = ui[1] < tanh_three_halves[0]

    candidate_cosh = interval_reciprocal(
        interval_add(
            (2 * u2i[0], 2 * u2i[1]),
            (Fraction(-1), Fraction(-1)),
        )
    )
    cutoff_cosh = cosh_interval(Fraction(21, 20))
    candidate_below_cutoff = candidate_cosh[1] < cutoff_cosh[0]

    center_cosh = cosh_interval(Fraction(111, 20))
    center_cosh_square = interval_mul(center_cosh, center_cosh)
    center_guard_pass = center_cosh_square[1] < CENTER_GUARD

    return {
        "all_pass": (
            alternating_vertex_is_inner
            and diameter_pass
            and candidate_below_cutoff
            and center_guard_pass
        ),
        "vertex_radius_order": {
            "claim": "b=1/(sqrt(2)*u)<u",
            "equivalent_check": "u^4>1/2",
            "u_fourth_power_interval": [fraction_text(value) for value in u4i],
            "decimal_interval": decimal_interval(u4i),
            "status": "PASS" if alternating_vertex_is_inner else "FAIL",
        },
        "fundamental_polygon_radius": {
            "claim": "2*atanh(u)<3",
            "equivalent_check": "u<tanh(3/2)=(exp(3)-1)/(exp(3)+1)",
            "u_interval": [fraction_text(value) for value in ui],
            "tanh_3_over_2_interval": [
                fraction_text(value) for value in tanh_three_halves
            ],
            "decimal_intervals": {
                "u": decimal_interval(ui),
                "tanh_3_over_2": decimal_interval(tanh_three_halves),
            },
            "status": "PASS" if diameter_pass else "FAIL",
        },
        "candidate_below_cutoff": {
            "claim": "ell_*=2*acosh(1/(2u^2-1))<21/10",
            "candidate_cosh_interval": [
                fraction_text(value) for value in candidate_cosh
            ],
            "cutoff_cosh_interval": [
                fraction_text(value) for value in cutoff_cosh
            ],
            "decimal_intervals": {
                "candidate_cosh": decimal_interval(candidate_cosh),
                "cosh_21_over_20": decimal_interval(cutoff_cosh),
            },
            "status": "PASS" if candidate_below_cutoff else "FAIL",
        },
        "center_radius_guard": {
            "claim": "cosh(111/20)^2<20000",
            "interval": [fraction_text(value) for value in center_cosh_square],
            "decimal_interval": decimal_interval(center_cosh_square),
            "status": "PASS" if center_guard_pass else "FAIL",
        },
        "method": (
            "Exact Fraction Taylor enclosures: alternating series for "
            "exp(-1/10), positive exponential with a geometric tail bound "
            "for all other exponential values."
        ),
    }


def center_guard_polynomial(state: State) -> Polynomial:
    parity, exponent, matrix = state
    alpha_squared = poly_mul(matrix[0], poly_conjugate(matrix[0]))
    denominator_power = poly_pow(DELTA, 2 * exponent + parity)
    return poly_sub(alpha_squared, poly_scale(denominator_power, CENTER_GUARD))


def systole_difference_polynomial(state: State) -> Polynomial:
    parity, exponent, matrix = state
    trace = poly_add(matrix[0], matrix[3])
    trace_real = poly_real_coefficients(trace)
    trace = tuple((coefficient, 0) for coefficient in trace_real)
    two_u2_minus_one = poly_add(poly_scale(U2, 2), poly_scale(ONE, -1))
    left = poly_mul(poly_mul(trace, trace), poly_mul(two_u2_minus_one, two_u2_minus_one))
    right = poly_scale(poly_pow(DELTA, 2 * exponent + parity), 4)
    return poly_sub(left, right)


def state_bytes(state: State) -> bytes:
    parity, exponent, matrix = state
    entries = []
    for poly in matrix:
        entries.append(";".join(f"{real},{imag}" for real, imag in poly))
    return f"{parity}:{exponent}:".encode("ascii") + "|".join(entries).encode("ascii")


def word_text(word: tuple[int, ...]) -> str:
    return "*".join(STEP_NAMES[index] for index in word) if word else "identity"


def finite_traversal() -> dict[str, object]:
    generators = generator_numerators()

    for index in range(4):
        state = multiply_state(IDENTITY, generators[index])
        state = multiply_state(state, generators[index + 4])
        if state != IDENTITY:
            raise ArithmeticError(f"generator {index} inverse failed")

    relator = (0, 5, 2, 7, 4, 1, 6, 3)
    relator_state = IDENTITY
    for step in relator:
        relator_state = multiply_state(relator_state, generators[step])
    if relator_state != IDENTITY:
        raise ArithmeticError("published relator did not reduce exactly")

    witness = multiply_state(multiply_state(IDENTITY, generators[0]), generators[3])
    witness_difference = systole_difference_polynomial(witness)
    witness_sign, _, _ = certified_poly_sign(witness_difference)
    if witness_sign != 0:
        raise ArithmeticError("g0*g3 is not an exact systole equality witness")

    words: dict[State, tuple[int, ...]] = {IDENTITY: ()}
    queue: deque[State] = deque((IDENTITY,))
    rejected: set[State] = set()
    depth_histogram = {0: 1}
    inside_sign_orders: dict[int, int] = {}
    outside_sign_orders: dict[int, int] = {}

    while queue:
        state = queue.popleft()
        word = words[state]
        for step_index, generator in enumerate(generators):
            neighbor = multiply_state(state, generator)
            if neighbor in words or neighbor in rejected:
                continue
            sign, order, _ = certified_poly_sign(center_guard_polynomial(neighbor))
            histogram = inside_sign_orders if sign <= 0 else outside_sign_orders
            histogram[order] = histogram.get(order, 0) + 1
            if sign <= 0:
                next_word = word + (step_index,)
                words[neighbor] = next_word
                queue.append(neighbor)
                depth_histogram[len(next_word)] = depth_histogram.get(len(next_word), 0) + 1
                if len(words) > MAX_STATES:
                    raise ArithmeticError("finite traversal exceeded frozen state cap")
            else:
                rejected.add(neighbor)

    equality_states: list[tuple[State, tuple[int, ...]]] = []
    strict_count = 0
    systole_sign_orders: dict[int, int] = {}
    for state, word in words.items():
        if state == IDENTITY:
            continue
        sign, order, _ = certified_poly_sign(systole_difference_polynomial(state))
        systole_sign_orders[order] = systole_sign_orders.get(order, 0) + 1
        if sign < 0:
            raise ArithmeticError(
                f"found exact state below candidate systole: {word_text(word)}"
            )
        if sign == 0:
            equality_states.append((state, word))
        else:
            strict_count += 1

    included_stream = b"\n".join(sorted(state_bytes(state) for state in words)) + b"\n"
    rejected_stream = b"\n".join(sorted(state_bytes(state) for state in rejected)) + b"\n"
    all_stream = included_stream + b"--REJECTED--\n" + rejected_stream

    mp.mp.dps = 80
    u_decimal = mp.exp(-mp.mpf(1) / 10)
    systole_decimal = 2 * mp.acosh(1 / (2 * u_decimal**2 - 1))

    equality_states.sort(key=lambda item: (len(item[1]), item[1], state_bytes(item[0])))
    return {
        "schema": SCHEMA,
        "status": "PASS_EXACT_SYSTOLE_AND_FINITE_COMPLETENESS",
        "evidence_token": "PROVED",
        "surface_id": SURFACE_ID,
        "exact_systole": {
            "formula": "2*acosh(1/(2*exp(-1/5)-1))",
            "decimal": mp.nstr(systole_decimal, 70),
            "equality_witness": "g0*g3",
            "witness_state_sha256": hashlib.sha256(state_bytes(witness)).hexdigest(),
            "witness_difference_polynomial": "IDENTICALLY_ZERO",
            "all_nonidentity_states_at_least_candidate": True,
            "strictly_above_state_count": strict_count,
            "equality_state_count_in_finite_component": len(equality_states),
            "equality_representative_words": [
                word_text(word) for _, word in equality_states[:24]
            ],
            "witness_primitive": True,
            "primitivity_reason": (
                "A proper root would be a nontrivial closed geodesic of "
                "translation length strictly below the proved systole."
            ),
        },
        "finite_completeness": {
            "theorem": (
                "Every conjugacy class with translation length <=21/10 has "
                "a conjugate in the exact identity-connected center sublevel "
                "component replayed here."
            ),
            "geometric_cutoff": "21/10",
            "center_guard_alpha_squared": CENTER_GUARD,
            "included_state_count": len(words),
            "rejected_boundary_state_count": len(rejected),
            "maximum_shortest_discovery_word_length": max(map(len, words.values())),
            "discovery_depth_histogram": {
                str(depth): count for depth, count in sorted(depth_histogram.items())
            },
            "included_state_stream_sha256": hashlib.sha256(included_stream).hexdigest(),
            "rejected_boundary_stream_sha256": hashlib.sha256(rejected_stream).hexdigest(),
            "classified_state_stream_sha256": hashlib.sha256(all_stream).hexdigest(),
            "normal_form": (
                "GaussianIntegerPolynomialMatrix/(Delta^q*sqrt(Delta)^p), "
                "common Delta factors cancelled, global PSU sign canonical"
            ),
            "deduplication": "EXACT_PSU_NORMAL_FORM",
            "component_boundary_closed": True,
            "raw_word_length_cap_used": False,
            "resource_cap_reached": False,
            "inside_sign_taylor_order_histogram": {
                str(order): count for order, count in sorted(inside_sign_orders.items())
            },
            "outside_sign_taylor_order_histogram": {
                str(order): count for order, count in sorted(outside_sign_orders.items())
            },
            "systole_sign_taylor_order_histogram": {
                str(order): count for order, count in sorted(systole_sign_orders.items())
            },
        },
        "exact_identity_checks": {
            "four_generator_inverse_pairs": "PASS",
            "published_eight_factor_relator": "PASS",
            "relator_word": "g0*g1^-1*g2*g3^-1*g0^-1*g1*g2^-1*g3",
        },
        "execution": {
            "control_systole_verified": True,
            "finite_word_to_length_completeness_verified": True,
            "common_geometric_cutoff_frozen": True,
            "common_geometric_cutoff": "21/10",
            "control_census_run": False,
            "bolza_census_run": False,
            "comparison_run": False,
            "target_data_used": False,
            "arithmetic_labels_assigned": False,
            "a2_evaluation_run": False,
            "route_b_invocation_allowed": False,
        },
        "route_a": {
            "bounded_proxy_tuple": [
                "A0_WEAK_ARITHMETIC_RELATION",
                "A1_WEAK",
                "A2_FAIL",
                "A3_FAIL",
                "A4_FAIL",
            ],
            "bounded_proxy_overall": "ROUTE_A_EXPLORATORY",
            "formal_full_candidate_route_a_tuple": "UNASSIGNED",
        },
        "claim_boundary": (
            "This proves the exact control systole and a finite completeness "
            "certificate at Lambda=21/10. It freezes that target-blind common "
            "cutoff but does not run either surface census, a magnetic "
            "comparison, an arithmetic control, a determinant, A2, or Route B."
        ),
    }


def write_source_matrix(path: Path, rows: Sequence[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=SOURCE_FIELDS, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def json_bytes(payload: object) -> bytes:
    return (json.dumps(payload, indent=2, sort_keys=True) + "\n").encode("utf-8")


def build_validation(
    rows: Sequence[dict[str, str]],
    guards: dict[str, object],
    certificate: dict[str, object],
    source_matrix_path: Path,
) -> dict[str, object]:
    project = Path(__file__).resolve().parents[1]
    errors: list[str] = []
    actual_freeze = sha256_file(FREEZE_PATH)
    if actual_freeze != EXPECTED_FREEZE_SHA256:
        errors.append("Round-8 freeze hash mismatch")
    for relative_path, expected_hash in UPSTREAM_LOCKS.items():
        path = project / relative_path
        if not path.is_file() or sha256_file(path) != expected_hash:
            errors.append(f"upstream lock mismatch: {relative_path}")
    included = [row for row in rows if row["decision"].startswith("INCLUDE")]
    excluded = [row for row in rows if row["decision"].startswith("EXCLUDE")]
    if len(included) != 3 or len(excluded) != 3:
        errors.append("source inclusion/exclusion counts changed")
    if {row["access_date"] for row in rows} != {ACCESS_DATE}:
        errors.append("source access date changed")
    if not guards.get("all_pass"):
        errors.append("one or more exact rational radius guards failed")
    execution = certificate.get("execution", {})
    if not isinstance(execution, dict):
        errors.append("execution block missing")
    else:
        required_true = (
            "control_systole_verified",
            "finite_word_to_length_completeness_verified",
            "common_geometric_cutoff_frozen",
        )
        required_false = (
            "control_census_run",
            "bolza_census_run",
            "comparison_run",
            "target_data_used",
            "arithmetic_labels_assigned",
            "a2_evaluation_run",
            "route_b_invocation_allowed",
        )
        for field in required_true:
            if execution.get(field) is not True:
                errors.append(f"required theorem field is not true: {field}")
        for field in required_false:
            if execution.get(field) is not False:
                errors.append(f"forbidden execution field is not false: {field}")
        if execution.get("common_geometric_cutoff") != "21/10":
            errors.append("common cutoff changed")
    finite = certificate.get("finite_completeness", {})
    if not isinstance(finite, dict):
        errors.append("finite completeness block missing")
    else:
        if finite.get("raw_word_length_cap_used") is not False:
            errors.append("raw word cap was substituted for geometric completeness")
        if finite.get("component_boundary_closed") is not True:
            errors.append("finite component boundary is not closed")
        if int(finite.get("included_state_count", MAX_STATES + 1)) > MAX_STATES:
            errors.append("state resource cap exceeded")
    exact_systole = certificate.get("exact_systole", {})
    if not isinstance(exact_systole, dict):
        errors.append("exact systole block missing")
    else:
        if exact_systole.get("witness_difference_polynomial") != "IDENTICALLY_ZERO":
            errors.append("systole equality witness failed")
        if exact_systole.get("all_nonidentity_states_at_least_candidate") is not True:
            errors.append("systole lower bound failed")

    return {
        "schema": "p28_round8_control_systole_validation/1.0",
        "status": "PASS" if not errors else "FAIL",
        "evidence_token": "PROVED" if not errors else "OPEN",
        "errors": errors,
        "freeze_sha256": actual_freeze,
        "upstream_locks": UPSTREAM_LOCKS,
        "remote_source_sha256": REMOTE_SOURCE_SHA256,
        "source_matrix_sha256": sha256_file(source_matrix_path),
        "certificate_payload_sha256": hashlib.sha256(json_bytes(certificate)).hexdigest(),
        "source_counts": {"included": len(included), "excluded": len(excluded)},
        "theorem_status": certificate["status"],
        "control_systole_formula": certificate["exact_systole"]["formula"],
        "finite_component_state_count": certificate["finite_completeness"][
            "included_state_count"
        ],
        "common_geometric_cutoff": "21/10",
        "common_geometric_cutoff_frozen": not errors,
        "census_run": False,
        "comparison_run": False,
        "a2_evaluation_run": False,
        "route_b_invocation_allowed": False,
    }


def parse_args() -> argparse.Namespace:
    project = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source-matrix-output",
        type=Path,
        default=project / "results" / "round8_control_systole_source_matrix.csv",
    )
    parser.add_argument(
        "--certificate-output",
        type=Path,
        default=project / "results" / "round8_control_finite_ball_certificate.json",
    )
    parser.add_argument(
        "--validation-output",
        type=Path,
        default=project / "results" / "round8_control_systole_validation.json",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    rows = source_rows()
    guards = proof_guards()
    if not guards["all_pass"]:
        raise ArithmeticError("frozen rational proof guards failed")
    certificate = finite_traversal()
    certificate["proof_guards"] = guards
    certificate["source_summary"] = {
        "included": sum(row["decision"].startswith("INCLUDE") for row in rows),
        "excluded": sum(row["decision"].startswith("EXCLUDE") for row in rows),
        "access_date": ACCESS_DATE,
    }
    certificate["source_binding"] = {
        "freeze_sha256": EXPECTED_FREEZE_SHA256,
        "upstream_locks": UPSTREAM_LOCKS,
        "remote_source_sha256": REMOTE_SOURCE_SHA256,
    }

    write_source_matrix(args.source_matrix_output, rows)
    args.certificate_output.parent.mkdir(parents=True, exist_ok=True)
    args.certificate_output.write_bytes(json_bytes(certificate))
    validation = build_validation(rows, guards, certificate, args.source_matrix_output)
    args.validation_output.parent.mkdir(parents=True, exist_ok=True)
    args.validation_output.write_bytes(json_bytes(validation))
    if validation["status"] != "PASS":
        raise ArithmeticError("validation failed: " + "; ".join(validation["errors"]))

    print(
        json.dumps(
            {
                "status": validation["status"],
                "theorem": certificate["status"],
                "systole": certificate["exact_systole"]["formula"],
                "finite_states": certificate["finite_completeness"][
                    "included_state_count"
                ],
                "common_cutoff": "21/10",
                "census_run": False,
                "comparison_run": False,
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
