"""Exact two-by-two integer algebra and the frozen determinant ledger."""

from __future__ import annotations

from typing import Any


Matrix2 = tuple[tuple[int, int], tuple[int, int]]
CAT_MATRIX: Matrix2 = ((2, 1), (1, 1))
IDENTITY: Matrix2 = ((1, 0), (0, 1))
REGISTERED_PERIODS = tuple(range(1, 13))

LOCKED_LEDGER = (
    (1, -1, {}, None),
    (2, -5, {5: 1}, 5),
    (3, -16, {2: 4}, 2),
    (4, -45, {3: 2, 5: 1}, 3),
    (5, -121, {11: 2}, 11),
    (6, -320, {2: 6, 5: 1}, None),
    (7, -841, {29: 2}, 29),
    (8, -2205, {3: 2, 5: 1, 7: 2}, 7),
    (9, -5776, {2: 4, 19: 2}, 19),
    (10, -15125, {5: 3, 11: 2}, None),
    (11, -39601, {199: 2}, 199),
    (12, -103680, {2: 8, 3: 4, 5: 1}, None),
)
LOCKED_ABSOLUTE_DELTAS = frozenset(abs(item[1]) for item in LOCKED_LEDGER)
LOCKED_SUPPORT = (2, 3, 5, 7, 11, 19, 29, 199)


def _exact_int(value: Any, *, label: str) -> int:
    if type(value) is not int:
        raise TypeError(f"{label} must be an exact integer")
    return value


def matrix2(value: Any) -> Matrix2:
    """Normalize an exact 2-by-2 integer matrix without coercion."""

    if type(value) not in {tuple, list} or len(value) != 2:
        raise TypeError("matrix must have exactly two rows")
    rows: list[tuple[int, int]] = []
    for row in value:
        if type(row) not in {tuple, list} or len(row) != 2:
            raise TypeError("matrix rows must have exactly two entries")
        rows.append(
            (
                _exact_int(row[0], label="matrix entry"),
                _exact_int(row[1], label="matrix entry"),
            )
        )
    return (rows[0], rows[1])


def determinant(matrix: Matrix2) -> int:
    a, b = matrix[0]
    c, d = matrix[1]
    return a * d - b * c


def trace(matrix: Matrix2) -> int:
    return matrix[0][0] + matrix[1][1]


def matrix_multiply(left: Matrix2, right: Matrix2) -> Matrix2:
    return (
        (
            left[0][0] * right[0][0] + left[0][1] * right[1][0],
            left[0][0] * right[0][1] + left[0][1] * right[1][1],
        ),
        (
            left[1][0] * right[0][0] + left[1][1] * right[1][0],
            left[1][0] * right[0][1] + left[1][1] * right[1][1],
        ),
    )


def matrix_power(matrix: Matrix2, exponent: int) -> Matrix2:
    exponent = _exact_int(exponent, label="exponent")
    if exponent < 0:
        raise ValueError("matrix exponent must be nonnegative")
    result = IDENTITY
    base = matrix
    remaining = exponent
    while remaining:
        if remaining % 2:
            result = matrix_multiply(result, base)
        base = matrix_multiply(base, base)
        remaining //= 2
    return result


def subtract_identity(matrix: Matrix2) -> Matrix2:
    return ((matrix[0][0] - 1, matrix[0][1]), (matrix[1][0], matrix[1][1] - 1))


def delta_direct(matrix: Matrix2, period: int) -> int:
    period = _exact_int(period, label="period")
    if period not in REGISTERED_PERIODS:
        raise ValueError("candidate determinant periods are frozen to 1 through 12")
    return determinant(subtract_identity(matrix_power(matrix, period)))


def trace_recurrence(matrix_trace: int, maximum_period: int = 12) -> list[int]:
    matrix_trace = _exact_int(matrix_trace, label="matrix trace")
    maximum_period = _exact_int(maximum_period, label="maximum period")
    if maximum_period < 1 or maximum_period > 12:
        raise ValueError("trace recurrence cutoff must lie in 1 through 12")
    values = [2, matrix_trace]
    while len(values) <= maximum_period:
        values.append(matrix_trace * values[-1] - values[-2])
    return values


def delta_recurrence(matrix: Matrix2, period: int) -> int:
    period = _exact_int(period, label="period")
    if period not in REGISTERED_PERIODS:
        raise ValueError("candidate determinant periods are frozen to 1 through 12")
    return 2 - trace_recurrence(trace(matrix), period)[period]


def factor_locked_integer(value: int) -> dict[int, int]:
    """Trial-factor one of the twelve locked determinant magnitudes only."""

    value = _exact_int(value, label="locked determinant")
    remaining = abs(value)
    if remaining not in LOCKED_ABSOLUTE_DELTAS:
        raise ValueError("factorization input is not a frozen determinant")
    if remaining == 1:
        return {}
    factors: dict[int, int] = {}
    divisor = 2
    while divisor * divisor <= remaining:
        exponent = 0
        while remaining % divisor == 0:
            exponent += 1
            remaining //= divisor
        if exponent:
            factors[divisor] = exponent
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        factors[remaining] = factors.get(remaining, 0) + 1
    return factors


def factorization_text(delta: int, factors: dict[int, int]) -> str:
    if delta == -1:
        return "-1"
    pieces: list[str] = []
    for divisor in sorted(factors):
        exponent = factors[divisor]
        pieces.append(str(divisor) if exponent == 1 else f"{divisor}^{exponent}")
    sign = "-" if delta < 0 else ""
    return sign + "*".join(pieces)


def selected_primitive_divisor(
    period: int, factors: dict[int, int], earlier_support: set[int]
) -> int | None:
    new_support = sorted(set(factors).difference(earlier_support))
    if len(new_support) > 1:
        raise RuntimeError("frozen ledger unexpectedly has multiple first-appearance factors")
    selected = new_support[0] if new_support else None
    locked = LOCKED_LEDGER[period - 1][3]
    if selected != locked:
        raise RuntimeError("primitive first-appearance divisor disagrees with source lock")
    return selected


def frozen_ledger_records() -> list[dict[str, Any]]:
    """Recompute the full locked ledger with two independent exact engines."""

    records: list[dict[str, Any]] = []
    earlier_support: set[int] = set()
    for period, expected_delta, expected_factors, expected_selected in LOCKED_LEDGER:
        direct = delta_direct(CAT_MATRIX, period)
        recurrence = delta_recurrence(CAT_MATRIX, period)
        factors = factor_locked_integer(direct)
        selected = selected_primitive_divisor(period, factors, earlier_support)
        record = {
            "period": period,
            "delta_direct": direct,
            "delta_recurrence": recurrence,
            "factorization": {str(key): value for key, value in sorted(factors.items())},
            "factorization_text": factorization_text(direct, factors),
            "support": sorted(factors),
            "selected_primitive_prime": selected,
            "engines_agree": direct == recurrence,
            "locked_record_matches": (
                direct == expected_delta
                and factors == expected_factors
                and selected == expected_selected
            ),
        }
        records.append(record)
        earlier_support.update(factors)
    return records


def validate_hyperbolic_sl2(matrix: Any) -> dict[str, Any]:
    """Accept exactly hyperbolic determinant-one integer matrices."""

    try:
        normalized = matrix2(matrix)
    except (TypeError, ValueError) as error:
        return {"accepted": False, "reason": type(error).__name__}
    det = determinant(normalized)
    tr = trace(normalized)
    accepted = det == 1 and abs(tr) > 2
    reason = "HYPERBOLIC_SL2" if accepted else "DETERMINANT_OR_HYPERBOLICITY_REJECT"
    return {"accepted": accepted, "determinant": det, "trace": tr, "reason": reason}
