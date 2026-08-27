#!/usr/bin/env python3
"""Independent SymPy reconstruction for HCS-C190."""
from __future__ import annotations

from hashlib import sha256
from itertools import product
import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c190_bulgarian_necklace_evidence.json"


def canonical_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def word_list(length: int, weight: int) -> list[str]:
    return sorted("".join(str(bit) for bit in bits) for bits in product((0, 1), repeat=length) if sum(bits) == weight)


def rotate(word: str, amount: int = 1) -> str:
    amount %= len(word)
    return word[-amount:] + word[:-amount] if amount else word


def reflection(word: str) -> str:
    return word[0] + word[:0:-1]


def fixed(length: int, weight: int, iterate: int) -> int:
    common = int(sp.gcd(length, iterate))
    block = length // common
    return 0 if weight % block else int(sp.binomial(common, weight // block))


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    assert data["payload_sha256"] == canonical_hash(data)
    checks = 1
    z, lam = sp.symbols("z lambda")

    for row in data["finite_replay"]["rows"]:
        n, length, weight = row["N"], row["k"], row["r"]
        assert n == length * (length - 1) // 2 + weight
        checks += 1
        assert row["partition_number"] == int(sp.functions.combinatorial.numbers.partition(n))
        checks += 1
        assert row["recurrent_count"] == int(sp.binomial(length, weight))
        checks += 1
        assert row["full_koopman_zero_algebraic_multiplicity"] == row["partition_number"] - row["recurrent_count"]
        checks += 1

        fixed_by_residue = {}
        for fixed_row in row["fixed_rows"]:
            residue = fixed_row["iterate_mod_k"]
            iterate = fixed_row["positive_iterate_representative"]
            assert iterate == (length if residue == 0 else residue)
            checks += 1
            value = fixed(length, weight, iterate)
            assert fixed_row["fixed_count"] == value
            checks += 1
            fixed_by_residue[residue] = value

        cycles = {}
        exact_population = 0
        for period_row in row["period_rows"]:
            period = period_row["period"]
            exact = sum(
                int(sp.mobius(period // divisor)) * fixed(length, weight, divisor)
                for divisor in sp.divisors(period)
            )
            assert period_row["fixed_at_period"] == fixed(length, weight, period)
            checks += 1
            assert period_row["exact_period_count"] == exact
            checks += 1
            assert exact % period == 0
            checks += 1
            assert period_row["cycle_count"] == exact // period
            checks += 1
            cycles[period] = exact // period
            exact_population += exact
        assert exact_population == row["recurrent_count"]
        checks += 1

        determinant = sp.Poly(1, z, domain=sp.ZZ)
        for period, cycle_count in cycles.items():
            determinant *= sp.Poly((1 - z**period) ** cycle_count, z, domain=sp.ZZ)
        assert determinant.degree() == row["recurrent_count"]
        checks += 1
        assert determinant.nth(0) == 1
        checks += 1
        assert sum(period * cycle_count for period, cycle_count in cycles.items()) == row["recurrent_count"]
        checks += 1

        characteristic_degree = row["full_koopman_zero_algebraic_multiplicity"] + sum(
            period * cycle_count for period, cycle_count in cycles.items()
        )
        assert characteristic_degree == row["partition_number"]
        checks += 1

        # The logarithmic derivative of the cycle product gives every trace.
        for iterate in range(1, 2 * length + 1):
            trace = sum(period * cycle_count for period, cycle_count in cycles.items() if iterate % period == 0)
            assert trace == fixed(length, weight, iterate)
            checks += 1

        total_multiplicity = 0
        for spectral_row in row["spectral_rows"]:
            exponent = spectral_row["root_exponent_mod_k"]
            multiplicity = sum(
                cycle_count for period, cycle_count in cycles.items()
                if exponent * period % length == 0
            )
            assert spectral_row["multiplicity"] == multiplicity
            checks += 1
            total_multiplicity += multiplicity
        assert total_multiplicity == row["recurrent_count"]
        checks += 1

        burnside = sum(fixed_by_residue[residue] for residue in range(length))
        assert burnside % length == 0
        checks += 1
        assert burnside // length == len(row["cycles"])
        checks += 1

        if weight == 0:
            assert row["recurrent_count"] == 1
            checks += 1
            assert cycles[1] == 1 and sum(cycles.values()) == 1
            checks += 1

    # Matrix-level operator and reversor sentinel for N=8.
    n8 = data["finite_replay"]["rows"][7]
    words = word_list(4, 2)
    position = {word: index for index, word in enumerate(words)}
    size = len(words)
    u = sp.zeros(size)
    q = sp.zeros(size)
    for word, index in position.items():
        u[index, position[rotate(word)]] = 1
        q[index, position[reflection(word)]] = 1
    identity = sp.eye(size)
    assert q * q == identity
    checks += 1
    assert q * u * q == u.inv()
    checks += 1
    expected_det = sp.expand((1 - z**2) * (1 - z**4))
    assert sp.expand((identity - z * u).det()) == expected_det
    checks += 1
    expected_char = sp.expand(lam**16 * (lam**2 - 1) * (lam**4 - 1))
    assert sp.degree(expected_char, lam) == n8["partition_number"]
    checks += 1
    assert [row["multiplicity"] for row in n8["spectral_rows"]] == [2, 1, 2, 1]
    checks += 1

    print(json.dumps({"status": "C190_SYMPY_PASS", "checks": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
