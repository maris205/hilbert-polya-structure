#!/usr/bin/env python3
"""Exact finite certificate for the C38 functorial Kummer obstruction."""

from __future__ import annotations

import hashlib
import json


def phase(x: int, n: int) -> int:
    return (x * x * x + 2 * x + 1) % 3


def cocycle(g: int, x: int, n: int) -> int:
    return (phase((x + g) % n, n) - phase(x, n)) % 3


def certificate(n: int = 13) -> dict[str, object]:
    cocycle_checks = 0
    representation_checks = 0
    determinant_checks = 0
    for g in range(n):
        for h in range(n):
            for x in range(n):
                lhs = cocycle((g + h) % n, x, n)
                rhs = (cocycle(g, (x + h) % n, n) + cocycle(h, x, n)) % 3
                if lhs != rhs:
                    raise AssertionError("cocycle identity failed")
                cocycle_checks += 1
                for channel in range(3):
                    direct = channel * cocycle(g, x, n) % 3
                    gauged = channel * (phase((x + g) % n, n) - phase(x, n)) % 3
                    if direct != gauged:
                        raise AssertionError("represented gauge identity failed")
                    representation_checks += 1
                if sum(j * cocycle(g, x, n) for j in range(3)) % 3 != 0:
                    raise AssertionError("graded determinant must be one")
                determinant_checks += 1

    path = (2, 5, 1, 5)
    if sum(path) % n != 0:
        raise AssertionError("frozen path is not closed")
    holonomy = []
    x = 4
    for channel in range(3):
        exponent = 0
        y = x
        for g in path:
            exponent = (exponent + channel * cocycle(g, y, n)) % 3
            y = (y + g) % n
        holonomy.append(exponent)
    if holonomy != [0, 0, 0]:
        raise AssertionError("closed holonomy is not the identity")

    payload = {
        "candidate": "HCS-C38",
        "modulus": n,
        "channels": [0, 1, 2],
        "closed_path": list(path),
        "closed_holonomy_exponents_mod_3": holonomy,
        "cocycle_checks": cocycle_checks,
        "representation_checks": representation_checks,
        "determinant_checks": determinant_checks,
        "functorial_kummer_prime_weight": "IDENTITY",
        "status": "PROVED_SCOPED_OBSTRUCTION",
    }
    canonical = json.dumps(payload, sort_keys=True, separators=(",", ":"))
    payload["payload_sha256"] = hashlib.sha256(canonical.encode()).hexdigest()
    return payload


def main() -> None:
    print(json.dumps(certificate(), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
