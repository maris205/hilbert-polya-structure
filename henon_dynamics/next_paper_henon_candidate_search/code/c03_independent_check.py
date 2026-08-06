#!/usr/bin/env python3
"""Independent tuple-based check of the C03 raw cycle ledger.

This checker intentionally does not import c03_finite_field.  It recomputes
the prime list and cycles using tuple states and Python sets, then compares the
result with the frozen JSON artifact.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import time
from collections import Counter
from pathlib import Path


def is_prime(value: int) -> bool:
    if value < 2:
        return False
    for divisor in range(2, math.isqrt(value) + 1):
        if value % divisor == 0:
            return False
    return True


def tuple_cycle_counts(prime: int) -> Counter[int]:
    seen: set[tuple[int, int]] = set()
    counts: Counter[int] = Counter()
    for q in range(prime):
        for r in range(prime):
            start = (q, r)
            if start in seen:
                continue
            current = start
            length = 0
            while current not in seen:
                seen.add(current)
                q_now, r_now = current
                current = ((1 - 6 * q_now * q_now - r_now) % prime, q_now)
                length += 1
            if current != start:
                raise AssertionError(f"p={prime}: tuple orbit did not close")
            counts[length] += 1
    if sum(length * count for length, count in counts.items()) != prime * prime:
        raise AssertionError(f"p={prime}: tuple point total failed")
    return counts


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    default_results = Path(__file__).resolve().parents[1] / "results" / "c03_finite_field"
    parser.add_argument("--census", type=Path, default=default_results / "c03_census.json")
    parser.add_argument(
        "--output", type=Path, default=default_results / "c03_independent_check.json"
    )
    args = parser.parse_args()
    started = time.perf_counter()
    census = json.loads(args.census.read_text())
    expected_primes = [p for p in range(2, census["frozen_configuration"]["max_prime"] + 1) if is_prime(p)]
    recorded_primes = [record["p"] for record in census["primes"]]
    if expected_primes != recorded_primes:
        raise AssertionError("independent prime list mismatch")

    checked = []
    for record in census["primes"]:
        prime = record["p"]
        observed = tuple_cycle_counts(prime)
        expected = Counter(
            {
                item["length"]: item["multiplicity"]
                for item in record["zeta"]["raw_denominator_factors"]
            }
        )
        if observed != expected:
            raise AssertionError(f"p={prime}: independent cycle ledger mismatch")
        checked.append(
            {
                "p": prime,
                "cycles": sum(observed.values()),
                "points": sum(length * count for length, count in observed.items()),
                "pass": True,
            }
        )

    payload = {
        "checker": "independent tuple-state cycle enumeration",
        "imports_primary_implementation": False,
        "census_sha256": sha256(args.census),
        "prime_count": len(checked),
        "all_pass": True,
        "elapsed_seconds": time.perf_counter() - started,
        "checks": checked,
    }
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        f"independent cycle ledgers PASS for {len(checked)} primes; "
        f"elapsed={payload['elapsed_seconds']:.3f}s; wrote {args.output}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
