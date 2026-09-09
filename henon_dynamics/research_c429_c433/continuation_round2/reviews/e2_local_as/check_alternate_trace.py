#!/usr/bin/env python3
"""One authorized independent check: p=3, period 9, precision s^64.

Only input is the coefficient certificate emitted in execution_n1024.log.
No producer import, Hensel lifting, derivative matrix, Cramer determinants,
or Bareiss determinant is used. Canonical factor membership is tested by a
divided-difference identity. The alternative trace-one element is alpha /
Tr_native(alpha). There is one fixed precision and no retry.
"""

from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import resource
import sys
import time

from flint import nmod_poly


PREC = 64
DIM = 9
MODULUS = 3
START = time.monotonic()
Z = nmod_poly([], MODULUS)
O = nmod_poly([1], MODULUS)
S = nmod_poly([0, 1], MODULUS)
LAMBDA = O + S
HERE = Path(__file__).resolve().parent
INPUT = HERE.parent.parent / "a3_wild_local_tower" / "execution_n1024.log"


def emit(event, **fields):
    print(json.dumps({
        "event": event,
        "utc": datetime.now(timezone.utc).isoformat(),
        "wall_s": round(time.monotonic() - START, 6),
        "cpu_s": round(time.process_time(), 6),
        **fields,
    }, sort_keys=True), flush=True)


def constant(c):
    return [c] + [Z] * (DIM - 1)


def plus(a, b, precision=PREC):
    return [(a[i] + b[i]).truncate(precision) for i in range(DIM)]


def minus(a, b, precision=PREC):
    return [(a[i] - b[i]).truncate(precision) for i in range(DIM)]


def scalar(c, a, precision=PREC):
    return [c.mul_low(v, precision) for v in a]


def product(a, b, factor, precision=PREC):
    # Straight convolution, then reduction in descending z-degree.
    tmp = [Z] * (2 * DIM - 1)
    for i in range(DIM):
        for j in range(DIM):
            tmp[i + j] = tmp[i + j] + a[i].mul_low(b[j], precision)
    for degree in range(2 * DIM - 2, DIM - 1, -1):
        high = tmp[degree]
        for j in range(DIM):
            k = degree - DIM + j
            tmp[k] = tmp[k] - high.mul_low(factor[j], precision)
    return [v.truncate(precision) for v in tmp[:DIM]]


def apply_p(a, factor, precision=PREC):
    return plus(product(a, a, factor, precision),
                scalar(LAMBDA, a, precision), precision)


def evaluate(coeffs, a, factor, precision=PREC):
    out = constant(Z)
    for coeff in reversed(coeffs):
        out = plus(product(out, a, factor, precision),
                   constant(coeff), precision)
    return out


def powers(a, largest, factor, precision=PREC):
    out = [constant(O)]
    for _ in range(largest):
        out.append(product(out[-1], a, factor, precision))
    return out


def divided_difference(coeffs, a, b, factor):
    # D_R(a,b)=sum_j c_j sum_{r=0}^{j-1} a^(j-1-r) b^r.
    ap = powers(a, len(coeffs) - 2, factor)
    bp = powers(b, len(coeffs) - 2, factor)
    out = constant(Z)
    for j in range(1, len(coeffs)):
        for r in range(j):
            term = product(ap[j - 1 - r], bp[r], factor)
            out = plus(out, scalar(coeffs[j], term))
    return out


def is_zero(a):
    return all(not v for v in a)


def order(poly):
    return next((i for i in range(len(poly)) if int(poly[i])), None)


def main():
    blob = INPUT.read_bytes()
    records = [json.loads(line) for line in blob.splitlines() if line.strip()]
    certificates = [row for row in records if row.get("event") == "M_COEFFICIENTS"]
    assert len(certificates) == 1
    certificate = certificates[0]
    assert certificate["precision"] == 1024
    coefficients = certificate["coefficients_low_s_first"]
    assert len(coefficients) == DIM + 1 and coefficients[-1] == [1]
    assert all(len(row) <= 1024 and all(c in (0, 1, 2) for c in row)
               for row in coefficients)
    factor = [nmod_poly(row[:PREC], MODULUS) for row in coefficients]
    assert all(int(factor[j][0]) == 0 for j in range(DIM))
    emit("START_INDEPENDENT_CHECK", p=3, e=2, precision=PREC,
         input_path=str(INPUT), input_sha256=hashlib.sha256(blob).hexdigest(),
         checker_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         algorithm="divided_difference_and_alternate_coordinate_trace",
         cpu_limit_s=30, wall_limit_s=60, address_space_limit_bytes=536870912)

    alpha = [Z, O] + [Z] * (DIM - 2)
    # Hand-derived coefficient formula for R=P_s composed three times.
    l2, l3, l4 = LAMBDA**2, LAMBDA**3, LAMBDA**4
    rpoly = [Z, l3, l4 + l3 + l2, 2*(l4 + l3 + l2),
             l4 + l2 + LAMBDA, l3, 2*LAMBDA, LAMBDA, O]
    ralpha = evaluate(rpoly, alpha, factor)
    direct = apply_p(apply_p(apply_p(alpha, factor), factor), factor)
    assert is_zero(minus(ralpha, direct))
    r2alpha = evaluate(rpoly, ralpha, factor)
    d1 = divided_difference(rpoly, ralpha, alpha, factor)
    d2 = divided_difference(rpoly, r2alpha, ralpha, factor)
    qrem = plus(plus(constant(O), d1), product(d1, d2, factor))
    assert is_zero(qrem), "Claimed factor fails the exact dynatomic remainder test"
    emit("CANONICAL_FACTOR_CERTIFICATE_PASSED", precision=PREC,
         reduction="z^9", identity="Q9=1+D1+D1*D2",
         uses_accepted_coprime_special_factor_uniqueness=True)

    orbit = []
    current = alpha
    for _ in range(DIM):
        orbit.append(current)
        current = apply_p(current, factor)
    assert is_zero(minus(current, alpha))
    tr = constant(Z)
    weighted = constant(Z)
    for i, point in enumerate(orbit):
        tr = plus(tr, point)
        weighted = plus(weighted, scalar(nmod_poly([-(i % 3)], 3), point))
    assert all(not v for v in tr[1:])
    trace_scalar = tr[0]
    assert trace_scalar == -factor[DIM - 1]
    trace_order = order(trace_scalar)
    assert trace_order == 10
    inner = PREC - trace_order
    error_exponent = PREC - 4 * trace_order
    assert error_exponent > 0
    emit("ALTERNATE_TRACE_CERTIFIED", trace_valuation=trace_order,
         trace_leading_coefficient=int(trace_scalar[trace_order]),
         trace_matches_minus_z8_coefficient=True,
         integral_scaled_precision=inner, AS_error_exponent=error_exponent)

    trace_unit = trace_scalar.right_shift(trace_order)
    inv = trace_unit.inverse_series_trunc(inner)
    scaled_y = scalar(inv, weighted, inner)
    # Native action is substitution on the polynomial scaled_y(alpha),
    # not evaluation of P_s at its value.
    sigma_y = evaluate(scaled_y, orbit[1], factor, inner)
    target = constant(O.left_shift(trace_order))
    assert is_zero(minus(minus(sigma_y, scaled_y, inner), target, inner))
    scaled_as = minus(product(product(scaled_y, scaled_y, factor, inner),
                              scaled_y, factor, inner),
                      scalar(O.left_shift(2*trace_order), scaled_y, inner), inner)
    assert all(not v for v in scaled_as[1:]), "AS numerator is not scalar"
    pole_bound = 3 * trace_order
    raw = {pole_bound - i: int(scaled_as[0][i])
           for i in range(pole_bound) if int(scaled_as[0][i])}
    reduced = dict(raw)
    # Frobenius is the identity on F_3 coefficients; all terms are handled.
    for exponent in range(pole_bound, 0, -1):
        coeff = reduced.pop(exponent, 0) % 3 if exponent % 3 == 0 else 0
        if coeff:
            reduced[exponent//3] = (reduced.get(exponent//3, 0) + coeff) % 3
    reduced = {j: c % 3 for j, c in reduced.items() if c % 3}
    assert all(j % 3 for j in reduced)
    emit("INDEPENDENT_AS_RESULT", raw_polar_terms=sorted(raw.items(), reverse=True),
         reduced_AS_polar_terms=sorted(reduced.items(), reverse=True),
         class_nonzero=bool(reduced), pole_bound=pole_bound,
         all_negative_coefficients_certified=True, AS_error_exponent=error_exponent)
    assert reduced == {4: 2, 2: 1}, "Reduced AS class differs from the stated target"
    emit("END_INDEPENDENT_CHECK", status="PASS_ONE_PAIR_ONLY",
         parameter_pairs=1, precision_attempts=1,
         maxrss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as error:
        emit("END_INDEPENDENT_CHECK", status="FAILED_NO_VERIFICATION",
             exception=repr(error))
        raise
