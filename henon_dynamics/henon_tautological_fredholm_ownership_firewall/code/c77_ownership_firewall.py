#!/usr/bin/env python3
"""Trace-class realization and source-block firewall certificate for HCS-P77."""

from __future__ import annotations

import argparse
import cmath
import copy
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
TRACK = PROJECT.parent
DEFAULT_OUTPUT = PROJECT / "results/c77_certificate.json"
CHANNEL_CUTOFF = 256
SINGLETON_ORDER = 49

DEPENDENCIES = {
    "p75_proof": (
        TRACK / "henon_weighted_reflection_channel_divisor/PROOF_PACKAGE.md",
        "f2ee916354ef0c4e7ecd9693826d33752510faf9e7892faf690a56333771ddd4",
    ),
    "p75_certificate": (
        TRACK / "henon_weighted_reflection_channel_divisor/results/c75_certificate.json",
        "2bcae20706f6061636ee9d327810eaf9501e30e8c1583cbc7af860938cc98464",
    ),
    "p75_paper": (
        TRACK / "henon_weighted_reflection_channel_divisor/paper/paper.pdf",
        "da68d4cfea785e121ffff960bebf10a5c0ee5b2ace20f0b81bc81c0c9aa3aa8f",
    ),
    "p76_proof": (
        TRACK / "henon_weighted_reflection_natural_boundary/PROOF_PACKAGE.md",
        "e171c701b78b7fd41b28a6c105eb46cafbfb5ff4812db7008e34f7fb49098cfd",
    ),
    "p76_certificate": (
        TRACK / "henon_weighted_reflection_natural_boundary/results/c76_certificate.json",
        "5d8557ce670b66ba55deab6e38b97b3ffecd85259b3be02c4329725dffff64e2",
    ),
    "p76_paper": (
        TRACK / "henon_weighted_reflection_natural_boundary/paper/paper.pdf",
        "60361548504e4b7297525399469a7e25f8b064883cd763535d5ac0d0a4456ce3",
    ),
}


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    count = 0
    value = n
    p = 2
    while p * p <= value:
        if value % p == 0:
            value //= p
            count += 1
            if value % p == 0:
                return 0
        p += 1
    if value > 1:
        count += 1
    return -1 if count % 2 else 1


def odd_prime_divisors(n: int) -> list[int]:
    value = n
    while value % 2 == 0:
        value //= 2
    out: list[int] = []
    p = 3
    while p * p <= value:
        if value % p == 0:
            out.append(p)
            while value % p == 0:
                value //= p
        p += 2
    if value > 1:
        out.append(value)
    return out


def c_divisor(m: int) -> Fraction:
    return sum(Fraction(k * mobius(k), m) for k in divisors(m) if k % 2)


def c_euler(m: int) -> Fraction:
    numerator = 1
    for p in odd_prime_divisors(m):
        numerator *= 1 - p
    return Fraction(numerator, m)


def psi(m: int, z: complex, q: float) -> complex:
    return 2 * (q * z) ** m / (1 - (1 + q ** (2 * m)) * z ** (2 * m))


def h_channel(m: int, z: complex, q: float) -> complex:
    return float(c_euler(m)) * psi(m, z, q)


def channel_entries(z: complex, q: float, cutoff: int = CHANNEL_CUTOFF) -> list[complex]:
    return [h_channel(m, z, q) for m in range(1, cutoff + 1)]


def universal_rank_one_determinant(f_value: complex) -> complex:
    """det(I+(F-1)P) for a rank-one projection P."""
    return 1 + (f_value - 1)


def singleton_word(n: int) -> tuple[int, ...]:
    if n < 3 or n % 2 == 0:
        raise ValueError("odd n>=3 required")
    return (1,) + (0,) * (n - 1)


def is_reflection_fixed(word: tuple[int, ...]) -> bool:
    n = len(word)
    return all(word[j] == word[-j % n] for j in range(n))


def least_period(word: tuple[int, ...]) -> int:
    n = len(word)
    for d in divisors(n):
        if all(word[j] == word[j % d] for j in range(n)):
            return d
    raise ArithmeticError("least period")


def chi_values(word: tuple[int, ...]) -> tuple[int, ...]:
    n = len(word)
    return tuple(int(word[(j - 1) % n] == word[(j + 1) % n]) for j in range(n))


def symmetry_energy(word: tuple[int, ...]) -> int:
    return sum(chi_values(word))


def block_weights(word: tuple[int, ...], q: Fraction) -> tuple[Fraction, ...]:
    return tuple(q ** value for value in chi_values(word))


def weighted_cyclic_matrix(weights: tuple[Fraction, ...]) -> list[list[Fraction]]:
    n = len(weights)
    matrix = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for j, weight in enumerate(weights):
        matrix[(j + 1) % n][j] = weight
    return matrix


def identity_minus_scaled(
    matrix: list[list[Fraction]], scale: Fraction
) -> list[list[Fraction]]:
    n = len(matrix)
    return [
        [Fraction(int(i == j)) - scale * matrix[i][j] for j in range(n)]
        for i in range(n)
    ]


def determinant_fraction(matrix: list[list[Fraction]]) -> Fraction:
    data = [row[:] for row in matrix]
    n = len(data)
    determinant = Fraction(1)
    for column in range(n):
        pivot = next((row for row in range(column, n) if data[row][column]), None)
        if pivot is None:
            return Fraction(0)
        if pivot != column:
            data[column], data[pivot] = data[pivot], data[column]
            determinant = -determinant
        value = data[column][column]
        determinant *= value
        for row in range(column + 1, n):
            if data[row][column] == 0:
                continue
            ratio = data[row][column] / value
            for j in range(column, n):
                data[row][j] -= ratio * data[column][j]
    return determinant


def matrix_multiply(
    left: list[list[Fraction]], right: list[list[Fraction]]
) -> list[list[Fraction]]:
    n = len(left)
    return [
        [sum((left[i][k] * right[k][j] for k in range(n)), Fraction(0)) for j in range(n)]
        for i in range(n)
    ]


def matrix_power(matrix: list[list[Fraction]], exponent: int) -> list[list[Fraction]]:
    n = len(matrix)
    result = [[Fraction(int(i == j)) for j in range(n)] for i in range(n)]
    base = [row[:] for row in matrix]
    power = exponent
    while power:
        if power & 1:
            result = matrix_multiply(result, base)
        base = matrix_multiply(base, base)
        power //= 2
    return result


def scalar_identity(n: int, scalar: Fraction) -> list[list[Fraction]]:
    return [[scalar if i == j else Fraction(0) for j in range(n)] for i in range(n)]


def graded_block_diagonal_sum(weights: tuple[Fraction, ...], power: int) -> Fraction:
    n = len(weights)
    if power % n:
        return Fraction(0)
    return Fraction(n) * math.prod(weights) ** (power // n)


def channel_sample(q: float, z: float) -> dict[str, object]:
    entries = channel_entries(complex(z), q)
    trace_sum = sum(entries, 0j)
    determinant_product = 1 + 0j
    for value in entries:
        determinant_product *= cmath.exp(value)
    trace_exponential = cmath.exp(trace_sum)
    error = abs(trace_exponential - determinant_product)
    if not error < 2e-11:
        raise ArithmeticError("trace exponential determinant")
    return {
        "q": format(q, ".17g"),
        "z": format(z, ".17g"),
        "cutoff": CHANNEL_CUTOFF,
        "partial_trace_norm": format(sum(abs(value) for value in entries), ".17g"),
        "last_entry_absolute_value": format(abs(entries[-1]), ".6e"),
        "exp_trace_real": format(trace_exponential.real, ".17g"),
        "exp_trace_imag": format(trace_exponential.imag, ".17g"),
        "determinant_product_error": format(error, ".6e"),
    }


def singleton_row(n: int, q: Fraction = Fraction(2, 3), z: Fraction = Fraction(1, 5)) -> dict[str, object]:
    word = singleton_word(n)
    values = chi_values(word)
    weights = block_weights(word, q)
    block = weighted_cyclic_matrix(weights)
    determinant = determinant_fraction(identity_minus_scaled(block, z))
    expected = 1 - z ** n * q ** sum(values)
    # Check the exact product acquired in one weighted cycle for every row,
    # and retain direct matrix multiplication on representative small blocks.
    full_turn_scalar = math.prod(weights)
    full_turn_matches = full_turn_scalar == q ** sum(values)
    if n <= 11:
        full_turn_matches = full_turn_matches and matrix_power(
            block, n
        ) == scalar_identity(n, full_turn_scalar)
    if (
        not is_reflection_fixed(word)
        or least_period(word) != n
        or sum(values) != n - 2
        or values.count(0) != 2
        or determinant != expected
        or not full_turn_matches
    ):
        raise ArithmeticError(f"singleton block mismatch at n={n}")
    return {
        "n": n,
        "reflection_fixed": True,
        "least_period": n,
        "energy": n - 2,
        "zero_chi_edges": 2,
        "one_chi_edges": n - 2,
        "q": str(q),
        "z": str(z),
        "determinant": str(determinant),
        "expected_determinant": str(expected),
        "full_turn_scalar": str(full_turn_scalar),
        "singular_values": {"1": 2, str(q): n - 2},
        "minimum_singular_value": str(min(Fraction(1), q)),
        "maximum_singular_value": str(max(Fraction(1), q)),
    }


def dependency_locks() -> dict[str, dict[str, str]]:
    out = {}
    for name, (path, expected) in DEPENDENCIES.items():
        observed = hashlib.sha256(path.read_bytes()).hexdigest()
        if observed != expected:
            raise RuntimeError(f"dependency changed: {name}")
        out[name] = {"path": str(path.relative_to(TRACK)), "sha256": observed}
    return out


def canonical_sha(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def core_payload() -> dict[str, object]:
    universal_samples = []
    for z in (0.2 + 0.1j, -0.3 + 0.25j, 0.4 - 0.2j):
        for label, value in (
            ("exp(z+z^2)", cmath.exp(z + z * z)),
            ("exp(sin(z))", cmath.exp(cmath.sin(z))),
        ):
            determinant = universal_rank_one_determinant(value)
            if abs(determinant - value) > 1e-15:
                raise ArithmeticError("rank-one determinant")
            universal_samples.append({
                "function": label,
                "z_real": format(z.real, ".17g"),
                "z_imag": format(z.imag, ".17g"),
                "determinant_error": format(abs(determinant - value), ".6e"),
            })

    singleton_rows = [singleton_row(n) for n in range(3, SINGLETON_ORDER + 1, 2)]
    return {
        "candidate_id": "HCS-P77",
        "frozen_input": "P75 weighted channel divisor and P76 punctured natural-boundary continuation",
        "punctured_domain": "Omega_q={|z|<min(1,q^(-1))} minus all channel roots",
        "channel_generator": "A(z,q)=diag(h_m(z,q)), h_m=c_m*2(qz)^m/[1-(1+q^(2m))z^(2m)]",
        "channel_trace_class": "A is locally holomorphic with values in S_1 on Omega_q",
        "channel_fredholm_family": "K_ch=exp(A)-I is locally trace class",
        "channel_determinant": "det_F(I+K_ch)=exp(Tr A)=Z_ch",
        "universal_rank_one_lemma": "K_F=(F-1)P gives det_F(I+K_F)=F for every nonvanishing holomorphic F",
        "ownership_classification": "PUNCTURED_ANALYTIC_DETERMINANT_PROVED_TAUTOLOGICAL",
        "source_block": "B_omega e_j=q^(chi(sigma^j omega))*e_(j+1 mod n)",
        "source_block_power": "B_omega^n=q^(S_n chi(omega))*I",
        "source_block_determinant": "det(I-zB_omega)=1-z^n q^(S_n chi(omega))",
        "source_block_singular_values": "the multiset {q^(chi_j)} is contained in {1,q}",
        "singleton_family": "for every odd n>=3, the reflection-fixed one-1 word is primitive and has S_n chi=n-2",
        "direct_sum_bounds": "min(1,q)||x||<=||B_q x||<=max(1,q)||x||",
        "direct_sum_compactness": "B_q is bounded and noncompact",
        "direct_sum_schatten": "B_q is in no finite S_p; for z!=0 the standard trace-class determinant det_F(I-zB_q) is undefined",
        "graded_power_ledger": "the canonical-basis diagonal sum of B_omega^r is 0 unless n|r, then n*q^((r/n)S); it is not an operator trace",
        "channel_samples": [
            channel_sample(0.5, 0.5),
            channel_sample(0.5, 0.95),
            channel_sample(1.0, 0.5),
            channel_sample(1.0, 0.8),
            channel_sample(2.0, 0.3),
            channel_sample(2.0, 0.46),
        ],
        "universal_rank_one_samples": universal_samples,
        "singleton_rows": singleton_rows,
        "strongest_positive_result": "the weighted punctured continuation has an explicit locally trace-class channel-diagonal Fredholm realization, while every physical primitive orbit owns an exact finite cyclic determinant block",
        "strongest_obstruction": "universal rank-one compression makes parameter-dependent determinant ownership tautological, whereas the undamped source-native full orbit-block sum is noncompact and outside every Schatten ideal",
        "open_theorem": "construct a source-native operator whose dynamics independently produces the weighted channel traces while paying compactness or nuclearity",
        "reusable_structure": "compare any scalar-built determinant with the universal rank-one lemma and a literal undamped source-block direct sum before granting operator ownership",
        "round2_clue": "any genuine owner must add a source-derived compactness mechanism without replacing the physical edge weights or merely compressing the finished scalar function",
        "claim_status": {
            "punctured_analytic_determinant": "PROVED_TAUTOLOGICAL",
            "universal_rank_one_firewall": "PROVED",
            "finite_source_cyclic_blocks": "PROVED",
            "source_native_direct_sum_trace_class": "REFUTED",
            "source_native_direct_sum_compact": "REFUTED",
            "genuine_transfer_owner": "OPEN",
            "arithmetic_trace": "OPEN",
            "arithmetic_advance": "NO",
            "route_b_authorized": False,
        },
    }


_VALIDATION_REFERENCE: dict[str, object] | None = None


def validate(core: dict[str, object]) -> None:
    global _VALIDATION_REFERENCE
    if _VALIDATION_REFERENCE is None:
        _VALIDATION_REFERENCE = core_payload()
    if type(core) is not dict or core != _VALIDATION_REFERENCE:
        raise ValueError("exact HCS-P77 schema drift")


def mutation_audit(core: dict[str, object]) -> dict[str, object]:
    rejected: list[str] = []
    protected = [
        "candidate_id", "frozen_input", "punctured_domain", "channel_generator",
        "channel_trace_class", "channel_fredholm_family", "channel_determinant",
        "universal_rank_one_lemma", "ownership_classification", "source_block",
        "source_block_power", "source_block_determinant",
        "source_block_singular_values", "singleton_family", "direct_sum_bounds",
        "direct_sum_compactness", "direct_sum_schatten", "graded_power_ledger",
        "strongest_positive_result", "strongest_obstruction", "open_theorem",
        "reusable_structure", "round2_clue",
    ]
    for key in protected:
        trial = copy.deepcopy(core)
        trial[key] = "FORGED"
        try:
            validate(trial)
        except ValueError:
            rejected.append(key)

    status_mutations = {
        "punctured_analytic_determinant": "GENUINE_TRANSFER_PROVED",
        "universal_rank_one_firewall": "OPEN",
        "finite_source_cyclic_blocks": "OPEN",
        "source_native_direct_sum_trace_class": "PROVED",
        "source_native_direct_sum_compact": "PROVED",
        "genuine_transfer_owner": "PROVED",
        "arithmetic_trace": "PROVED",
        "arithmetic_advance": "YES",
        "route_b_authorized": True,
    }
    for key, forged in status_mutations.items():
        trial = copy.deepcopy(core)
        trial["claim_status"][key] = forged
        try:
            validate(trial)
        except ValueError:
            rejected.append("status-" + key)

    for label, mutate in (
        ("short-channel-samples", lambda x: x["channel_samples"].pop()),
        ("rank-one-error", lambda x: x["universal_rank_one_samples"][0].update({"determinant_error": "1"})),
        ("singleton-energy", lambda x: x["singleton_rows"][4].update({"energy": 0})),
        ("singleton-period", lambda x: x["singleton_rows"][5].update({"least_period": 1})),
        ("singular-floor", lambda x: x["singleton_rows"][6].update({"minimum_singular_value": "0"})),
        ("determinant-forgery", lambda x: x["singleton_rows"][2].update({"determinant": "0"})),
    ):
        trial = copy.deepcopy(core)
        mutate(trial)
        try:
            validate(trial)
        except ValueError:
            rejected.append(label)

    attempted = len(protected) + len(status_mutations) + 6
    return {"attempted": attempted, "rejected": rejected, "all_rejected": len(rejected) == attempted}


def build() -> dict[str, object]:
    core = core_payload()
    validate(core)
    out = dict(core)
    out["dependency_locks"] = dependency_locks()
    out["mutation_audit"] = mutation_audit(core)
    if not out["mutation_audit"]["all_rejected"]:
        raise RuntimeError("mutation audit")
    out["core_sha256"] = canonical_sha(core)
    out["check"] = True
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    out = build()
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "candidate_id": out["candidate_id"],
        "channel_samples": len(out["channel_samples"]),
        "singleton_blocks": len(out["singleton_rows"]),
        "mutations": out["mutation_audit"]["attempted"],
        "core_sha256": out["core_sha256"],
        "check": True,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
