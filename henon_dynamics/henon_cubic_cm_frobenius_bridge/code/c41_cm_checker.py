#!/usr/bin/env python3
"""Exact F_p and F_{p^2} checks for E: y^2=x^3+1."""

from __future__ import annotations

import hashlib
import json


def primes_below(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * limit
    sieve[:2] = b"\x00\x00"
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            sieve[p * p : limit : p] = b"\x00" * (((limit - 1 - p * p) // p) + 1)
    return [p for p in range(limit) if sieve[p]]


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    value = pow(a, (p - 1) // 2, p)
    return 1 if value == 1 else -1


def trace_fp(p: int) -> int:
    return -sum(legendre(x * x * x + 1, p) for x in range(p))


def nonsquare(p: int) -> int:
    return next(d for d in range(2, p) if legendre(d, p) == -1)


def mul(x: tuple[int, int], y: tuple[int, int], p: int, d: int) -> tuple[int, int]:
    return ((x[0] * y[0] + d * x[1] * y[1]) % p,
            (x[0] * y[1] + x[1] * y[0]) % p)


def power(x: tuple[int, int], n: int, p: int, d: int) -> tuple[int, int]:
    result = (1, 0)
    base = x
    while n:
        if n & 1:
            result = mul(result, base, p, d)
        base = mul(base, base, p, d)
        n //= 2
    return result


def count_fp2(p: int) -> int:
    d = nonsquare(p)
    q = p * p
    total = 1
    one = (1, 0)
    zero = (0, 0)
    for a in range(p):
        for b in range(p):
            x = (a, b)
            rhs = mul(mul(x, x, p, d), x, p, d)
            rhs = ((rhs[0] + 1) % p, rhs[1])
            if rhs == zero:
                total += 1
            elif power(rhs, (q - 1) // 2, p, d) == one:
                total += 2
    return total


def certificate(limit: int = 2000) -> dict[str, object]:
    ps = [p for p in primes_below(limit) if p > 3]
    traces = {p: trace_fp(p) for p in ps}
    inert = [p for p in ps if p % 3 == 2]
    if any(traces[p] != 0 for p in inert):
        raise AssertionError("inert-prime trace did not vanish")
    if any(traces[p] * traces[p] > 4 * p for p in ps):
        raise AssertionError("Hasse bound failed")

    extension_checks: dict[str, dict[str, int]] = {}
    for p in (5, 7, 11, 13):
        a = traces[p]
        predicted = p * p + 1 - (a * a - 2 * p)
        direct = count_fp2(p)
        if predicted != direct:
            raise AssertionError("F_p2 recurrence failed")
        extension_checks[str(p)] = {"direct": direct, "predicted": predicted}

    samples = {str(p): traces[p] for p in (5, 7, 11, 13, 19)}
    payload = {
        "candidate": "HCS-C41",
        "curve": "y^2=x^3+1",
        "prime_limit": limit,
        "good_prime_count": len(ps),
        "inert_prime_count": len(inert),
        "inert_trace_failures": 0,
        "hasse_failures": 0,
        "sample_traces": samples,
        "fp2_checks": extension_checks,
        "local_factor": "1-a_p*T+p*T^2",
        "status": "PROVED_ARITHMETIC_CONNECTION_NOT_HENON_DETERMINANT",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    return payload


if __name__ == "__main__":
    print(json.dumps(certificate(), indent=2, sort_keys=True))
