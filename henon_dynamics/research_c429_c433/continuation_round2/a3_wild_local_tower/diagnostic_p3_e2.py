#!/usr/bin/env python3
"""One allocated exact AS diagnostic: p=3,e=2; no parameter loop.

Arithmetic is F_3[s]/s^N and polynomials in z represented by coefficient
lists. The only precision stages are N=128 and, if required, N=512.
Run with the externally recorded CPU/address-space/wall limits.
"""

import hashlib
import json
import resource
import sys
import time

from flint import nmod_poly

P, E, NATIVE, PREV = 3, 2, 9, 3
START = time.monotonic()
ZERO = nmod_poly([], P)
ONE = nmod_poly([1], P)
S = nmod_poly([0, 1], P)
LAM = ONE + S


def emit(event, **data):
    print(json.dumps({"event": event, "wall_s": round(time.monotonic()-START, 3),
                      "cpu_s": round(time.process_time(), 3), **data}, sort_keys=True),
          flush=True)


def trim(a):
    while a and not a[-1]:
        a.pop()
    return a


def trunc(a, prec):
    return trim([x.truncate(prec) for x in a])


def add(a, b, prec, sign=1):
    return trim([((a[i] if i < len(a) else ZERO)
                  + sign*(b[i] if i < len(b) else ZERO)).truncate(prec)
                 for i in range(max(len(a), len(b)))])


def scale(a, b, prec):
    return trim([x.mul_low(b, prec) for x in a])


def mul(a, b, prec):
    if not a or not b:
        return []
    out = [ZERO for _ in range(len(a)+len(b)-1)]
    if a is b:
        for i, x in enumerate(a):
            if not x:
                continue
            for j in range(i, len(a)):
                if b[j]:
                    term = x.mul_low(b[j], prec)
                    out[i+j] += term if i == j else 2*term
    else:
        for i, x in enumerate(a):
            if not x:
                continue
            for j, y in enumerate(b):
                if y:
                    out[i+j] += x.mul_low(y, prec)
    return trim(out)


def divmonic(a, b, prec):
    assert b and b[-1] == ONE
    rem = trunc(a, prec)
    if len(rem) < len(b):
        return [], rem
    quotient = [ZERO for _ in range(len(rem)-len(b)+1)]
    for pos in range(len(rem)-len(b), -1, -1):
        coeff = rem[pos+len(b)-1]
        quotient[pos] = coeff
        if coeff:
            for j in range(len(b)-1):
                rem[pos+j] -= coeff.mul_low(b[j], prec)
        rem[pos+len(b)-1] = ZERO
    return trim(quotient), trim(rem[:len(b)-1])


def mod(a, modulus, prec):
    return divmonic(a, modulus, prec)[1]


def ringmul(a, b, modulus, prec):
    return mod(mul(a, b, prec), modulus, prec)


def multmatrix(a, modulus, prec):
    dim = len(modulus)-1
    cols = []
    curr = mod(a, modulus, prec)
    for _ in range(dim):
        cols.append(curr + [ZERO]*(dim-len(curr)))
        curr = mod([ZERO] + curr, modulus, prec)
    return [[cols[j][i] for j in range(dim)] for i in range(dim)]


def solve_unit(matrix, rhs, prec):
    dim = len(matrix)
    a = [list(row) + [rhs[i] if i < len(rhs) else ZERO]
         for i, row in enumerate(matrix)]
    for j in range(dim):
        pivot = next((i for i in range(j, dim) if int(a[i][j][0]) != 0), None)
        assert pivot is not None, "Hensel unit matrix lost invertibility"
        a[j], a[pivot] = a[pivot], a[j]
        inv = a[j][j].inverse_series_trunc(prec)
        a[j] = [x.mul_low(inv, prec) for x in a[j]]
        for i in range(dim):
            if i == j or not a[i][j]:
                continue
            factor = a[i][j]
            a[i] = [x-factor.mul_low(y, prec) for x, y in zip(a[i], a[j])]
    return trim([a[i][-1] for i in range(dim)])


def determinant(matrix):
    """Exact fraction-free determinant in F_3[s], no series division."""
    a = [list(row) for row in matrix]
    dim, sign, previous = len(a), 1, ONE
    for j in range(dim-1):
        pivotrow = next((i for i in range(j, dim) if a[i][j]), None)
        if pivotrow is None:
            return ZERO
        if pivotrow != j:
            a[j], a[pivotrow] = a[pivotrow], a[j]
            sign = -sign
        pivot = a[j][j]
        for i in range(j+1, dim):
            for k in range(j+1, dim):
                numerator = a[i][k]*pivot-a[i][j]*a[j][k]
                quotient, rem = divmod(numerator, previous)
                assert not rem, "Bareiss exact division failed"
                a[i][k] = quotient
            a[i][j] = ZERO
        previous = pivot
    return sign*a[-1][-1]


def valuation(a):
    return next((i for i in range(len(a)) if int(a[i]) != 0), None)


def build_q(prec):
    current = [ZERO, ONE]
    previous = None
    for i in range(1, NATIVE+1):
        current = add(mul(current, current, prec), scale(current, LAM, prec), prec)
        if i == PREV:
            previous = add(current, [ZERO, ONE], prec, -1)
    numerator = add(current, [ZERO, ONE], prec, -1)
    q, rem = divmonic(numerator, previous, prec)
    assert not rem and len(q)-1 == 504
    emit("Q_constructed", precision=prec, z_degree=len(q)-1)
    return q


def hensel(q, target, current_m=None, current_n=None, known=1):
    if current_m is None:
        q0 = trunc(q, 1)
        assert all(not x for x in q0[:NATIVE]) and q0[NATIVE]
        current_m = [ZERO]*NATIVE+[ONE]
        current_n = q0[NATIVE:]
        assert not add(q0, mul(current_m, current_n, 1), 1, -1)
    while known < target:
        nxt = min(2*known, target)
        err = add(trunc(q, nxt), mul(current_m, current_n, nxt), nxt, -1)
        assert all(x.truncate(known) == ZERO for x in err)
        remerr = mod(err, current_m, nxt)
        a = solve_unit(multmatrix(current_n, current_m, nxt), remerr, nxt)
        assert all(x.truncate(known) == ZERO for x in a)
        b, rem = divmonic(add(err, mul(a, current_n, nxt), nxt, -1), current_m, nxt)
        assert not rem and all(x.truncate(known) == ZERO for x in b)
        current_m = add(current_m, a, nxt)
        current_n = add(current_n, b, nxt)
        assert not add(trunc(q, nxt), mul(current_m, current_n, nxt), nxt, -1)
        assert len(current_m)-1 == NATIVE and current_m[-1] == ONE
        known = nxt
        emit("Hensel_verified", precision=known)
    return current_m, current_n


def native_apply(a, modulus, prec):
    out = []
    native = [ZERO, LAM, ONE]
    for coeff in reversed(a):
        out = add(ringmul(out, native, modulus, prec), [coeff], prec)
    return out


def certify(mpoly, prec):
    deriv = trim([(i+1)*mpoly[i+1] for i in range(len(mpoly)-1)])
    matrix = multmatrix(deriv, mpoly, prec)
    det = determinant(matrix)
    delta = valuation(det)
    if delta is None or delta >= prec:
        emit("precision_insufficient", precision=prec, reason="discriminant_not_visible")
        return False
    # det is the discriminant up to its irrelevant sign; coefficient changes
    # of order s^prec change this integral determinant by order at least prec.
    emit("discriminant_valuation_certified", precision=prec, delta=delta,
         required_strict_lower_bound=4*delta+8,
         leading_coefficient=int(det[delta]))
    if prec <= 4*delta+8:
        emit("precision_insufficient", precision=prec, reason="N_not_above_4delta_plus_8")
        return False
    inner = prec-delta
    unit_inv = det.right_shift(delta).truncate(inner).inverse_series_trunc(inner)
    numerators = []
    for j in range(NATIVE):
        replaced = [list(row) for row in matrix]
        for i in range(NATIVE):
            replaced[i][j] = ONE if i == NATIVE-1 else ZERO
        numerators.append(determinant(replaced))
    wscaled = trim([num.mul_low(unit_inv, inner) for num in numerators])
    sdelta = ONE.left_shift(delta)
    # Cramer's rule certifies M'(alpha)*W=s^delta*alpha^(n-1).
    assert not add(ringmul(deriv, wscaled, mpoly, inner),
                   [ZERO]*(NATIVE-1)+[sdelta], inner, -1)
    trace, yscaled, curr = [], [], wscaled
    for i in range(NATIVE):
        trace = add(trace, curr, inner)
        yscaled = add(yscaled, scale(curr, nmod_poly([-(i % P)], P), inner), inner)
        curr = native_apply(curr, mpoly, inner)
    assert not add(curr, wscaled, inner, -1)
    assert not add(trace, [sdelta], inner, -1)
    assert not add(add(native_apply(yscaled, mpoly, inner), yscaled, inner, -1),
                   [sdelta], inner, -1)
    emit("trace_one_and_native_resolvent_verified", precision=prec,
         integral_scaled_precision=inner, y_known_mod_exponent=prec-2*delta)
    square = ringmul(yscaled, yscaled, mpoly, inner)
    cube = ringmul(square, yscaled, mpoly, inner)
    shifted = [x.left_shift(2*delta).truncate(inner) for x in yscaled]
    as_num = add(cube, shifted, inner, -1)
    assert all(not x for x in as_num[1:]), "AS output is not scalar at certified precision"
    scalar = as_num[0] if as_num else ZERO
    raw = {3*delta-i: int(scalar[i]) for i in range(3*delta) if int(scalar[i])}
    reduced = dict(raw)
    for pole in range(3*delta, 0, -1):
        coeff = reduced.get(pole, 0) % P
        if pole % P == 0 and coeff:
            reduced.pop(pole, None)
            lower = pole//P
            reduced[lower] = (reduced.get(lower, 0)+coeff) % P
    reduced = {j: a for j, a in reduced.items() if a % P}
    assert all(j % P for j in reduced)
    mdata = [[int(x[i]) for i in range(len(x))] for x in mpoly]
    mdigest = hashlib.sha256(json.dumps(mdata, separators=(",", ":")).encode()).hexdigest()
    emit("CERTIFIED_PAIR_RESULT", p=P, e=E, precision=prec, delta=delta,
         pole_bound=3*delta, integral_scaled_precision=inner,
         raw_polar_terms=sorted(raw.items(), reverse=True),
         reduced_AS_polar_terms=sorted(reduced.items(), reverse=True),
         class_nonzero=bool(reduced), M_coefficients_sha256=mdigest,
         maxrss_kib=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
         scope="one_pair_only_not_uniform_tower")
    # The exact truncated factor is emitted for independent reconstruction.
    emit("M_COEFFICIENTS", precision=prec, coefficients_low_s_first=mdata)
    return True


def main():
    emit("START", p=P, e=E, native_period=NATIVE, prior_period=PREV,
         allowed_precisions=[128, 512], cpu_limit_s=1200, wall_limit_s=1500,
         address_space_limit_bytes=2147483648)
    current_m = current_n = None
    known = 1
    for prec in (128, 512):
        q = build_q(prec)
        current_m, current_n = hensel(q, prec, current_m, current_n, known)
        known = prec
        if certify(current_m, prec):
            emit("END", status="CERTIFIED", mathematical_parameter_pairs=1)
            return 0
    emit("END", status="INCONCLUSIVE_AT_ALLOCATED_CAP", mathematical_parameter_pairs=1)
    return 2


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as exc:
        emit("END", status="FAILED_NO_MATHEMATICAL_CONCLUSION", exception=repr(exc))
        raise
