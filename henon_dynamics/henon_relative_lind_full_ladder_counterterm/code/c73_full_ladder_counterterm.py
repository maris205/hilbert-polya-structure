#!/usr/bin/env python3
"""Exact full-ladder counterterm certificate for HCS-P73."""

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
DEFAULT_OUTPUT = PROJECT / "results/c73_certificate.json"
FORMAL_ORDER = 96
REGULARIZATION_ORDER = 24
ROOT_ORDER = 12

DEPENDENCIES = {
    "p71_proof": (
        TRACK / "henon_relative_lind_counterterm/PROOF_PACKAGE.md",
        "d0a85f29652a80bc6286f4cebe1949b8892daa8f768d4349e082aaf5ad640dc7",
    ),
    "p71_certificate": (
        TRACK / "henon_relative_lind_counterterm/results/c71_certificate.json",
        "b765fa8a04a552289f5672a1d590e3d84a9ab0e8616a5844b431a5b01c7c3866",
    ),
    "p71_paper": (
        TRACK / "henon_relative_lind_counterterm/paper/paper.pdf",
        "930d21108cfd88a3607ac62146e00d25e220382c704a4d04111b575c1d608fde",
    ),
    "p72_proof": (
        TRACK / "henon_relative_lind_essential_ladder/PROOF_PACKAGE.md",
        "b0390d8b8a10160ea0958a4594b54a320566f9f7e0c26138aca11112f33bf018",
    ),
    "p72_certificate": (
        TRACK / "henon_relative_lind_essential_ladder/results/c72_certificate.json",
        "a311c84c88a2cf798767c35e200f3f77de8424f63fa1827472b3f2f81fb772f8",
    ),
    "p72_paper": (
        TRACK / "henon_relative_lind_essential_ladder/paper/paper.pdf",
        "4c89c65983c0d867bd8bb3130c5176705d8e1d05876d7cc67f8b26c77433a5b1",
    ),
}

EXPECTED_STRINGS = {
    "candidate_id": "HCS-P73",
    "tail_definition": "L(t)=sum_(m>=2)c_m Phi(t^m), Phi(x)=2x/(1-2x^2)",
    "complex_roots": "alpha_(m,k)=2^(-1/(2m))*exp(pi*i*k/m), 0<=k<2m",
    "partial_fraction_identity": "c_m Phi(t^m)=sum_(k=0)^(2m-1)b_(m,k)/(1-t/alpha_(m,k)), b_(m,k)=c_m*(-1)^k/(sqrt(2)*m)",
    "regularized_pole": "R_(m,k)=b_(m,k)*((1-t/alpha)^(-1)-sum_(j=0)^(m-1)(t/alpha)^j)",
    "regularized_channel_identity": "sum_k R_(m,k)=c_m Phi(t^m)",
    "raw_divergence": "sum_k |b_(m,k)|=sqrt(2)|c_m| and |c_p|>=2/3 on every odd prime level",
    "normal_convergence": "sum_k |R_(m,k)|<=sqrt(2)|c_m|q^m/(1-q) on compact tails",
    "order_independence": "absolute normal convergence permits every enumeration of individual complex pole factors",
    "source_rewrite": "H_rel(1-sqrt(2)t)=3/(4w)-(1/2)log(w)-3/2, w=1+sqrt(2)t",
    "counterterm": "K_all=exp(3/2)w^(1/2)exp(-3/(4w))*exp(L(t))",
    "renormalization_identity": "K_all(t)*C_rel(t)=1 on compatible branches",
    "strongest_positive_result": "the full positive and complex ladder has an exact normalized order-independent counterterm",
    "strongest_obstruction": "the raw pole family is not absolutely summable and cannot be multiplied in arbitrary pole order",
    "open_theorem": "construct an independent punctured-domain transfer operator whose traces produce the channel ledger",
    "round2_clue": "test operator ownership only with a predeclared kernel and trace iteration law, not a determinant reverse-engineered from K_all",
}

EXPECTED_STATUS = {
    "complex_divisor": "PROVED",
    "partial_fractions": "PROVED",
    "raw_unordered_pole_product": "REFUTED",
    "weierstrass_regularization": "PROVED",
    "transfer_operator_ownership": "NOT_CLAIMED",
    "arithmetic_advance": "NO",
    "route_b_authorized": False,
}


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    value = n
    factors = 0
    p = 2
    while p * p <= value:
        if value % p == 0:
            value //= p
            factors += 1
            if value % p == 0:
                return 0
        p += 1
    if value > 1:
        factors += 1
    return -1 if factors % 2 else 1


def odd_prime_divisors(n: int) -> list[int]:
    value = n
    while value % 2 == 0:
        value //= 2
    out = []
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


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    p = 3
    while p * p <= n:
        if n % p == 0:
            return False
        p += 2
    return True


def all_reflection_count(n: int) -> int:
    if n < 1 or n % 2 == 0:
        raise ValueError("positive odd period required")
    return 2 ** ((n + 1) // 2)


def primitive_reflection_count(n: int) -> int:
    if n < 1 or n % 2 == 0:
        raise ValueError("positive odd period required")
    return sum(mobius(k) * all_reflection_count(n // k) for k in divisors(n))


def direct_log_coefficient(degree: int) -> Fraction:
    return sum(
        Fraction(n * primitive_reflection_count(n), degree)
        for n in divisors(degree)
        if n % 2
    )


def phi_coefficient(degree: int) -> Fraction:
    if degree < 1 or degree % 2 == 0:
        return Fraction(0)
    return Fraction(2 ** ((degree + 1) // 2))


def channel_coefficient(m: int, degree: int) -> Fraction:
    if degree < m or (degree - m) % (2 * m):
        return Fraction(0)
    ell = (degree - m) // (2 * m)
    return c_euler(m) * (2 ** (ell + 1))


def tail_direct_coefficient(degree: int) -> Fraction:
    return direct_log_coefficient(degree) - phi_coefficient(degree)


def tail_channel_coefficient(degree: int) -> Fraction:
    return sum(channel_coefficient(m, degree) for m in range(2, degree + 1))


def rho(m: int) -> float:
    return 2 ** (-1 / (2 * m))


def alpha(m: int, k: int) -> complex:
    return rho(m) * cmath.exp(1j * math.pi * k / m)


def principal_multiplier(m: int, k: int) -> Fraction:
    """Multiplier of 1/sqrt(2) in b_(m,k)."""
    return c_euler(m) * ((-1) ** k) / m


def root_sum_is_zero(m: int, degree: int) -> bool:
    """Exact 2m-th-root orthogonality for sum (-1)^k alpha^(-degree)."""
    return (m - degree) % (2 * m) != 0


def normalized_level_bound(m: int, q: Fraction) -> Fraction:
    """Level bound after removing the common sqrt(2) factor."""
    if not 0 < q < 1:
        raise ValueError("q must lie in (0,1)")
    return abs(c_euler(m)) * q**m / (1 - q)


def normalized_tail_bound(first_m: int, q: Fraction) -> Fraction:
    """Geometric bound after removing the common sqrt(2) factor."""
    if first_m < 1 or not 0 < q < 1:
        raise ValueError("invalid tail bound input")
    return q**first_m / (1 - q) ** 2


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


def root_ledger() -> list[dict[str, object]]:
    rows = []
    for m in range(2, ROOT_ORDER + 1):
        for k in range(2 * m):
            root = alpha(m, k)
            residual = abs(1 - 2 * root ** (2 * m))
            rows.append({
                "m": m,
                "k": k,
                "alpha_exact": f"2^(-1/{2*m})*exp(pi*i*{k}/{m})",
                "alpha_real": format(root.real, ".17g"),
                "alpha_imag": format(root.imag, ".17g"),
                "root_residual": format(residual, ".3e"),
                "b_multiplier_of_1_over_sqrt2": str(principal_multiplier(m, k)),
            })
    return rows


def regularization_ledger() -> list[dict[str, object]]:
    q = Fraction(4, 5)
    rows = []
    for m in range(2, REGULARIZATION_ORDER + 1):
        coefficient = c_euler(m)
        if coefficient != c_divisor(m) or coefficient == 0:
            raise ArithmeticError(f"channel coefficient failure at {m}")
        cancellations = [root_sum_is_zero(m, j) for j in range(m)]
        if not all(cancellations):
            raise ArithmeticError(f"Taylor cancellation failure at {m}")
        rows.append({
            "m": m,
            "c_m": str(coefficient),
            "rho_m": format(rho(m), ".17g"),
            "pole_count": 2 * m,
            "weierstrass_genus": m - 1,
            "cancelled_taylor_degrees": list(range(m)),
            "raw_absolute_mass_over_sqrt2": str(abs(coefficient)),
            "regularized_level_bound_over_sqrt2_at_q_4_5": str(normalized_level_bound(m, q)),
        })
    return rows


def coefficient_crosscheck() -> list[dict[str, object]]:
    rows = []
    for degree in range(1, FORMAL_ORDER + 1):
        direct = tail_direct_coefficient(degree)
        regrouped = tail_channel_coefficient(degree)
        if direct != regrouped:
            raise ArithmeticError(f"tail coefficient mismatch at {degree}")
        rows.append({"degree": degree, "tail_coefficient": str(direct)})
    return rows


def prime_divergence_ledger() -> list[dict[str, object]]:
    rows = []
    lower_sum = Fraction(0)
    for p in range(3, 80, 2):
        if not is_prime(p):
            continue
        mass = abs(c_euler(p))
        if mass < Fraction(2, 3):
            raise ArithmeticError("prime lower bound")
        lower_sum += mass
        rows.append({
            "prime_level": p,
            "raw_absolute_mass_over_sqrt2": str(mass),
            "partial_mass_over_sqrt2": str(lower_sum),
        })
    return rows


def core_payload() -> dict[str, object]:
    core = dict(EXPECTED_STRINGS)
    core.update({
        "coefficient_formula": "c_m=(1/m)sum_(d|m,d odd)d*mu(d)=(1/m)product_(p|m,p odd)(1-p)",
        "counterterm_basepoint": "K_all(0)=exp(3/4), C_rel(0)=exp(-3/4)",
        "root_ledger": root_ledger(),
        "regularization_ledger": regularization_ledger(),
        "coefficient_crosscheck": coefficient_crosscheck(),
        "prime_divergence_ledger": prime_divergence_ledger(),
        "tail_majorant_over_sqrt2_from_m_25_at_q_4_5": str(
            normalized_tail_bound(25, Fraction(4, 5))
        ),
        "reusable_structure": "root-of-unity Taylor cancellation converts conditionally grouped rational channels into an absolutely normal pole family",
        "claim_status": dict(EXPECTED_STATUS),
    })
    return core


def validate(core: dict[str, object]) -> None:
    if type(core) is not dict:
        raise ValueError("schema")
    for key, expected in EXPECTED_STRINGS.items():
        if core.get(key) != expected:
            raise ValueError(key)
    if core.get("claim_status") != EXPECTED_STATUS:
        raise ValueError("claim status")
    roots = core.get("root_ledger")
    expected_roots = sum(2 * m for m in range(2, ROOT_ORDER + 1))
    if type(roots) is not list or len(roots) != expected_roots:
        raise ValueError("root ledger")
    for row in roots:
        if Fraction(row["b_multiplier_of_1_over_sqrt2"]) != principal_multiplier(row["m"], row["k"]):
            raise ValueError("root multiplier")
    regularization = core.get("regularization_ledger")
    if type(regularization) is not list or len(regularization) != REGULARIZATION_ORDER - 1:
        raise ValueError("regularization ledger")
    for row in regularization:
        m = row["m"]
        if Fraction(row["c_m"]) != c_euler(m):
            raise ValueError("regularization coefficient")
        if row["weierstrass_genus"] != m - 1:
            raise ValueError("genus")
        if row["cancelled_taylor_degrees"] != list(range(m)):
            raise ValueError("Taylor degrees")
    crosscheck = core.get("coefficient_crosscheck")
    if type(crosscheck) is not list or len(crosscheck) != FORMAL_ORDER:
        raise ValueError("coefficient crosscheck")
    for row in crosscheck:
        if Fraction(row["tail_coefficient"]) != tail_channel_coefficient(row["degree"]):
            raise ValueError("formal coefficient")
    primes = core.get("prime_divergence_ledger")
    if type(primes) is not list or len(primes) < 10:
        raise ValueError("prime ledger")
    if any(Fraction(row["raw_absolute_mass_over_sqrt2"]) < Fraction(2, 3) for row in primes):
        raise ValueError("raw mass lower bound")


def mutation_audit(core: dict[str, object]) -> dict[str, object]:
    rejected = []
    for key in EXPECTED_STRINGS:
        trial = copy.deepcopy(core)
        trial[key] = "FORGED"
        try:
            validate(trial)
        except ValueError:
            rejected.append(key)
    for key, forged in (
        ("complex_divisor", "HEURISTIC"),
        ("partial_fractions", "OPEN"),
        ("raw_unordered_pole_product", "PROVED"),
        ("weierstrass_regularization", "NUMERICAL"),
        ("transfer_operator_ownership", "PROVED"),
        ("arithmetic_advance", "YES"),
        ("route_b_authorized", True),
    ):
        trial = copy.deepcopy(core)
        trial["claim_status"][key] = forged
        try:
            validate(trial)
        except ValueError:
            rejected.append("status-" + key)
    trial = copy.deepcopy(core)
    trial["coefficient_crosscheck"].pop()
    try:
        validate(trial)
    except ValueError:
        rejected.append("short-coefficient-ledger")
    trial = copy.deepcopy(core)
    trial["regularization_ledger"][0]["weierstrass_genus"] = 0
    try:
        validate(trial)
    except ValueError:
        rejected.append("wrong-genus")
    attempted = len(EXPECTED_STRINGS) + 7 + 2
    return {
        "attempted": attempted,
        "rejected": rejected,
        "all_rejected": len(rejected) == attempted,
    }


def build() -> dict[str, object]:
    core = core_payload()
    validate(core)
    audit = mutation_audit(core)
    if audit["attempted"] != 25 or not audit["all_rejected"]:
        raise RuntimeError("mutation audit")
    out = dict(core)
    out["dependency_locks"] = dependency_locks()
    out["mutation_audit"] = audit
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
        "candidate_id": "HCS-P73",
        "complex_roots": len(out["root_ledger"]),
        "regularized_levels": len(out["regularization_ledger"]),
        "mutations": out["mutation_audit"]["attempted"],
        "core_sha256": out["core_sha256"],
        "check": True,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
