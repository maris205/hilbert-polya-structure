#!/usr/bin/env python3
"""Six fixed high-precision algebraic diagnostics. No file writes, no global claim.

The recursive derivative separation is a floating-point diagnostic, not a Sturm
or directed-interval certificate. Repeat precision detects instability only.
"""

import json
import platform
import time
from mpmath import mp
import mpmath

CASES = ((1, 24), (5, 24), (11, 24), (1, 30), (7, 30), (13, 30))
PRECISIONS = (100, 180)


def add(p, q):
    n = max(len(p), len(q))
    return [(p[j] if j < len(p) else mp.mpf(0)) +
            (q[j] if j < len(q) else mp.mpf(0)) for j in range(n)]


def mul(p, q):
    out = [mp.mpf(0)] * (len(p) + len(q) - 1)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            out[i + j] += x * y
    return out


def scale(p, c):
    return [c * x for x in p]


def psum(polys):
    out = [mp.mpf(0)]
    for p in polys:
        out = add(out, p)
    return out


def coefficient(r, s):
    v = [[mp.mpf(0)]]
    e = [[mp.mpf(1)]]
    for n in range(1, s):
        f = psum(mul(e[j], e[n - 2 - j]) for j in range(n - 1))
        numerator = add(scale(e[n - 1], mp.mpf(1) / 2), [mp.mpf(0)] + f)
        denominator = 4 * mp.sin(mp.pi * r * n / s) ** 2
        v.append(scale(numerator, -1 / denominator))
        e.append(scale(psum(scale(mul(v[k], e[n - k]), k)
                            for k in range(1, n + 1)), mp.mpf(1) / n))
    f = psum(mul(e[j], e[s - 2 - j]) for j in range(s - 1))
    out = scale(add(e[s - 1], [mp.mpf(0)] + scale(f, 2)), -1)
    while out[-1] == 0:
        out.pop()
    return out


def value(p, x):
    ans = p[-1]
    for c in p[-2::-1]:
        ans = ans * x + c
    return ans


def abs_value_scale(p, x):
    return value([abs(c) for c in p], abs(x))


def derivative(p):
    return [j * p[j] for j in range(1, len(p))]


def positive_roots(p, issues, level=0):
    """Separate simple positive roots by recursively estimated critical points.

    Every accepted root has a computed sign-changing bracket. Critical values
    close to numerical zero are flagged instead of being called multiple roots.
    This only uses rounded coefficients and is intentionally not a proof.
    """
    degree = len(p) - 1
    if degree == 1:
        root = -p[0] / p[1]
        return [(root, root)] if root > 0 else []
    critical_brackets = positive_roots(derivative(p), issues, level + 1)
    critical = [(a + b) / 2 for a, b in critical_brackets]
    bound = 1 + max(abs(c / p[-1]) for c in p[:-1])
    partition = [mp.mpf(0)] + [x for x in critical if 0 < x < bound] + [bound]
    tol = mp.power(10, -mp.dps + 20)
    close = mp.power(10, -mp.dps // 2)
    vals = [value(p, x) for x in partition]
    for x, y in zip(partition[1:-1], vals[1:-1]):
        normalized = abs(y) / abs_value_scale(p, x)
        if normalized < close:
            issues.append({"kind": "near_zero_critical_value", "level": level,
                           "degree": degree, "x": mp.nstr(x, mp.dps),
                           "normalized": mp.nstr(normalized, mp.dps)})
    brackets = []
    for left, right, fl, fr in zip(partition, partition[1:], vals, vals[1:]):
        if fl == 0 or fr == 0:
            issues.append({"kind": "rounded_zero_endpoint", "degree": degree})
            continue
        if mp.sign(fl) == mp.sign(fr):
            continue
        for _ in range(2000):
            middle = (left + right) / 2
            fm = value(p, middle)
            if fm == 0:
                # A rounded exact zero is not an exact-root certificate.
                left = middle - tol * max(1, abs(middle)) / 4
                right = middle + tol * max(1, abs(middle)) / 4
                break
            if mp.sign(fm) == mp.sign(fl):
                left, fl = middle, fm
            else:
                right, fr = middle, fm
            if right - left < tol * max(1, abs(middle)):
                break
        else:
            issues.append({"kind": "bisection_limit", "degree": degree})
        if mp.sign(value(p, left)) == mp.sign(value(p, right)):
            issues.append({"kind": "lost_endpoint_sign_change", "degree": degree})
        brackets.append((left, right))
    return brackets


def run_case(r, s, dps):
    mp.dps = dps
    started = time.monotonic()
    p = coefficient(r, s)
    issues = []
    brackets = positive_roots(p, issues)
    roots = [(lo + hi) / 2 for lo, hi in brackets]
    dp = derivative(p)
    items = []
    for root, (lo, hi) in zip(roots, brackets):
        norm_resid = abs(value(p, root)) / abs_value_scale(p, root)
        condition = abs_value_scale(p, root) / abs(root * value(dp, root))
        items.append({
            "root_estimate": mp.nstr(root, dps - 15),
            "rounded_coefficient_bracket": [mp.nstr(lo, dps - 5), mp.nstr(hi, dps - 5)],
            "endpoint_signs": [int(mp.sign(value(p, lo))), int(mp.sign(value(p, hi)))],
            "normalized_residual": mp.nstr(norm_resid, 15),
            "coefficientwise_relative_condition_estimate": mp.nstr(condition, 15),
        })
    return {
        "r": r, "s": s, "decimal_precision": dps, "degree": len(p) - 1,
        "real_positive_signchange_brackets": len(brackets),
        "issues": issues,
        "minimum_separation_estimate": mp.nstr(min(roots[j + 1] - roots[j]
                                                   for j in range(len(roots) - 1)), 30)
            if len(roots) > 1 else None,
        "coefficients_ascending": [mp.nstr(x, dps - 5) for x in p],
        "roots": items,
        "seconds": time.monotonic() - started,
        "rigorous_interval_or_sturm_certificate": False,
    }


def main():
    results = []
    for r, s in CASES:
        runs = [run_case(r, s, dps) for dps in PRECISIONS]
        low, high = runs
        mp.dps = 180
        if len(low["roots"]) == len(high["roots"]):
            relative = [abs(mp.mpf(x["root_estimate"]) - mp.mpf(y["root_estimate"]))
                        / max(1, abs(mp.mpf(y["root_estimate"])))
                        for x, y in zip(low["roots"], high["roots"])]
            change = mp.nstr(max(relative), 30) if relative else None
        else:
            change = None
        results.append({"r": r, "s": s, "runs": runs,
                        "max_root_change_100_to_180_scaled_by_max_1_abs": change})
    print(json.dumps({
        "scope": [list(case) for case in CASES], "precisions": list(PRECISIONS),
        "python": platform.python_version(), "mpmath": mpmath.__version__,
        "kind": "targeted algebraic numerical diagnostic, not proof or experiment acceptance",
        "coefficient_recurrence": "v_n=-(E_(n-1)/2+lambda*F_(n-2))/D_n; C=-E_(s-1)-2lambdaF_(s-2)",
        "real_root_method": "recursive derivative separation with positive Cauchy bounds and sign-changing brackets",
        "all_denominator_claim_proved": False,
        "actual_family_counterexample_certified": False,
        "results": results,
    }, indent=2))


if __name__ == "__main__":
    main()
