#!/usr/bin/env python3
"""Exact certificate for HCS-P74 all-channel gauge rigidity."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from fractions import Fraction
from pathlib import Path


PROJECT = Path(__file__).resolve().parents[1]
TRACK = PROJECT.parent
DEFAULT_OUTPUT = PROJECT / "results/c74_certificate.json"
CHANNEL_ORDER = 32
SERIES_ORDER = 96

DEPENDENCIES = {
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
    "p73_proof": (
        TRACK / "henon_relative_lind_full_ladder_counterterm/PROOF_PACKAGE.md",
        "248806829666f45d07e29784cba7594b97fbe4734d09d4bf1774a8c213bdbd6e",
    ),
    "p73_certificate": (
        TRACK / "henon_relative_lind_full_ladder_counterterm/results/c73_certificate.json",
        "35f03baf04ae62ed1088288d7cf259d9cfde63acc17aa14bf069b7479dd43ebe",
    ),
    "p73_paper": (
        TRACK / "henon_relative_lind_full_ladder_counterterm/paper/paper.pdf",
        "b54804f45bd10f47429eb2cd43f76ff02bf6b6628aaabfdccf7f8643a9200a26",
    ),
}


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    if n < 1:
        raise ValueError("positive integer required")
    value = n
    prime_count = 0
    p = 2
    while p * p <= value:
        if value % p == 0:
            value //= p
            prime_count += 1
            if value % p == 0:
                return 0
        p += 1
    if value > 1:
        prime_count += 1
    return -1 if prime_count % 2 else 1


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
    return sum(
        (Fraction(k * mobius(k), m) for k in divisors(m) if k % 2),
        Fraction(0),
    )


def c_euler(m: int) -> Fraction:
    numerator = 1
    for p in odd_prime_divisors(m):
        numerator *= 1 - p
    return Fraction(numerator, m)


def weighted_root_filter(m: int, degree: int) -> int:
    """Exact DFT value after reducing exponents modulo 2m."""
    return 2 * m if degree % (2 * m) == m else 0


def channel_log_coefficient(m: int, degree: int) -> Fraction:
    """[t^degree] c_m Phi(t^m)."""
    if degree % m:
        return Fraction(0)
    quotient = degree // m
    if quotient < 1 or quotient % 2 == 0:
        return Fraction(0)
    return c_euler(m) * (2 ** ((quotient + 1) // 2))


def primary_multiplier_coefficient(m: int, genus: int, degree: int) -> Fraction:
    """Orbit-summed coefficient of the positive relative multiplier.

    Each local logarithm is b*z^(genus+1)/(1-z).  The root filter removes
    every coefficient except degrees congruent to m modulo 2m.
    """
    if degree <= genus:
        return Fraction(0)
    return channel_log_coefficient(m, degree)


def relative_channel_coefficient(degree: int) -> Fraction:
    """Coefficient of -sum_(m>=2)c_m Phi(t^m)."""
    return -sum(
        (channel_log_coefficient(m, degree) for m in divisors(degree) if m >= 2),
        Fraction(0),
    )


def genus_minus_one_multiplier_coefficient(degree: int) -> Fraction:
    return sum(
        (
            primary_multiplier_coefficient(m, m - 1, degree)
            for m in divisors(degree)
            if m >= 2
        ),
        Fraction(0),
    )


def genus_m_multiplier_coefficient(degree: int) -> Fraction:
    return sum(
        (
            primary_multiplier_coefficient(m, m, degree)
            for m in divisors(degree)
            if m >= 2
        ),
        Fraction(0),
    )


def source_residual(a: Fraction, beta: Fraction) -> dict[str, str]:
    return {
        "pole_coefficient": str(Fraction(3, 4) - a),
        "log_coefficient": str(beta - Fraction(1, 2)),
        "constant": "-3/2",
    }


def product_residual_log_coefficient(degree: int) -> Fraction:
    """Coefficient from 2t+2 sum_(d odd) mu(d) log(1-t^d)."""
    value = Fraction(2 if degree == 1 else 0)
    value -= Fraction(2, degree) * sum(
        d * mobius(d) for d in divisors(degree) if d % 2
    )
    return value


def exp_series(log_coefficients: list[Fraction], order: int) -> list[Fraction]:
    """Return exp(L(t)) through order using n a_n=sum k l_k a_(n-k)."""
    if len(log_coefficients) <= order:
        raise ValueError("insufficient log coefficients")
    out = [Fraction(0)] * (order + 1)
    out[0] = Fraction(1)
    for n in range(1, order + 1):
        out[n] = sum(
            (Fraction(k) * log_coefficients[k] * out[n - k] for k in range(1, n + 1)),
            Fraction(0),
        ) / n
    return out


def finite_jet_example(order: int, lam: Fraction = Fraction(1)) -> list[Fraction]:
    log_coeffs = [Fraction(0)] * (2 * order + 4)
    log_coeffs[order + 1] = lam
    return exp_series(log_coeffs, 2 * order + 2)


def dependency_locks() -> dict[str, dict[str, str]]:
    out: dict[str, dict[str, str]] = {}
    for name, (path, expected) in DEPENDENCIES.items():
        observed = hashlib.sha256(path.read_bytes()).hexdigest()
        if observed != expected:
            raise RuntimeError(f"dependency changed: {name}")
        out[name] = {
            "path": str(path.relative_to(TRACK)),
            "sha256": observed,
        }
    return out


def canonical_sha(value: object) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def channel_row(m: int) -> dict[str, object]:
    c_m = c_euler(m)
    if c_m != c_divisor(m) or c_m == 0:
        raise ArithmeticError("P72 coefficient replay failed")
    filter_values = {
        str(j): weighted_root_filter(m, j)
        for j in range(0, 4 * m + 1)
        if weighted_root_filter(m, j)
    }
    return {
        "m": m,
        "c_m": str(c_m),
        "pole_count": 2 * m,
        "rho_m": f"2^(-1/{2*m})",
        "relative_principal_coefficient": "-c_m*(-1)^k/(sqrt(2)*m)",
        "multiplier_principal_coefficient": "+d_m*(-1)^k/(sqrt(2)*m)",
        "forced_d_m": str(c_m),
        "nonzero_root_filters_through_4m": filter_values,
        "genus_m_minus_1_residual_log": "0",
        "genus_m_residual_log": f"{-2*c_m}*t^{m}",
    }


def core_payload() -> dict[str, object]:
    rows = [channel_row(m) for m in range(2, CHANNEL_ORDER + 1)]
    coefficient_checks = []
    for degree in range(1, SERIES_ORDER + 1):
        relative = relative_channel_coefficient(degree)
        g_minus = genus_minus_one_multiplier_coefficient(degree)
        g_source = genus_m_multiplier_coefficient(degree)
        annihilated = relative + g_minus
        preserved = relative + g_source
        expected_preserved = Fraction(0) if degree == 1 else -2 * c_euler(degree)
        product_form = product_residual_log_coefficient(degree)
        if annihilated != 0:
            raise ArithmeticError(f"genus m-1 sign failure at {degree}")
        if preserved != expected_preserved or product_form != expected_preserved:
            raise ArithmeticError(f"genus m residual failure at {degree}")
        coefficient_checks.append({
            "degree": degree,
            "relative_channel_log": str(relative),
            "genus_m_minus_1_multiplier_log": str(g_minus),
            "annihilated_residual_log": str(annihilated),
            "genus_m_multiplier_log": str(g_source),
            "source_preserving_residual_log": str(preserved),
            "product_form_residual_log": str(product_form),
        })

    jet_checks = []
    for order in range(0, 13):
        series = finite_jet_example(order)
        if series[:order + 1] != [Fraction(1)] + [Fraction(0)] * order:
            raise ArithmeticError("finite jet mutation")
        if series[order + 1] != 1:
            raise ArithmeticError("finite jet witness missing")
        jet_checks.append({
            "jet_order": order,
            "gauge": f"exp(t^{order+1})",
            "coefficients_through_jet": [str(v) for v in series[:order + 1]],
            "first_different_coefficient": str(series[order + 1]),
        })

    return {
        "candidate_id": "HCS-P74",
        "relative_sign_lock": "log C_rel=H_rel-sum_(m>=2)c_m Phi(t^m)",
        "multiplier_class": "W_(d,G)=exp(sum_(m>=2)d_m Phi(t^m)+G(t))",
        "normal_convergence_hypothesis": "sum_(m>=2)|d_m|r^m<infinity for every 0<r<1; G holomorphic on unit disk",
        "channel_rigidity": "all channel singularities removable implies d_m=c_m for every m>=2",
        "source_coordinate": "w=1+sqrt(2)t",
        "source_exact_ledger": "H_rel(2-w)=3/(4w)-(1/2)log(w)-3/2",
        "source_multiplier": "w^beta exp(-a/w)",
        "source_forced_pair": {"a": "3/4", "beta": "1/2"},
        "source_forced_residual": source_residual(Fraction(3, 4), Fraction(1, 2)),
        "gauge_torsor": "remaining multipliers are a torsor under nowhere-zero holomorphic functions on the unit disk",
        "genus_m_minus_1_multiplier": "exp(sum_(m>=2)c_m Phi(t^m)); G=0",
        "genus_m_minus_1_channel_residual": "1",
        "normalized_full_residual": "exp(3/2)*w^(1/2)*exp(-3/(4w))*W_-*C_rel=1",
        "genus_m_multiplier": "exp(sum_(m>=2)c_m Phi(t^m)-2sum_(m>=2)c_m t^m)",
        "genus_m_channel_residual": "exp(-2sum_(m>=2)c_m t^m)",
        "genus_m_product_form": "exp(2t)*product_(d>=1,d odd)(1-t^d)^(2mu(d))",
        "finite_jet_conclusion": "for every N, exp(lambda*(t-t0)^(N+1)) preserves the N-jet and changes the gauge when lambda is nonzero",
        "monodromy": "primary exponential factors are single-valued; nontrivial slit logarithms are extra data",
        "channel_ledger": rows,
        "coefficient_crosscheck": coefficient_checks,
        "finite_jet_witnesses": jet_checks,
        "strongest_positive_result": "singular coefficients and the negative source pair are rigid, and both primary products converge normally and independently of pole order",
        "strongest_obstruction": "removability leaves an arbitrary nowhere-zero holomorphic gauge, so cancellation and every finite jet fail to define an absolute canonical determinant",
        "open_theorem": "supply an independent source-native normalization or operator that selects and owns one holomorphic gauge",
        "claim_status": {
            "channel_coefficient_rigidity": "PROVED_IN_DECLARED_CLASS",
            "negative_source_pair_rigidity": "PROVED_FOR_NONZERO_HOLOMORPHIC_EXTENSION",
            "holomorphic_gauge_torsor": "PROVED",
            "genus_m_minus_1_trivialization": "PROVED_AFTER_STATED_SCALAR_NORMALIZATION",
            "genus_m_source_residual": "PROVED",
            "finite_jet_uniqueness": "REFUTED",
            "absolute_canonical_gauge": "OPEN",
            "operator_ownership": "OPEN",
            "arithmetic_advance": "NO",
            "route_b_authorized": False,
        },
    }


EXPECTED_STATUS = {
    "channel_coefficient_rigidity": "PROVED_IN_DECLARED_CLASS",
    "negative_source_pair_rigidity": "PROVED_FOR_NONZERO_HOLOMORPHIC_EXTENSION",
    "holomorphic_gauge_torsor": "PROVED",
    "genus_m_minus_1_trivialization": "PROVED_AFTER_STATED_SCALAR_NORMALIZATION",
    "genus_m_source_residual": "PROVED",
    "finite_jet_uniqueness": "REFUTED",
    "absolute_canonical_gauge": "OPEN",
    "operator_ownership": "OPEN",
    "arithmetic_advance": "NO",
    "route_b_authorized": False,
}


PROTECTED_SCALARS = {
    "candidate_id": "HCS-P74",
    "relative_sign_lock": "log C_rel=H_rel-sum_(m>=2)c_m Phi(t^m)",
    "multiplier_class": "W_(d,G)=exp(sum_(m>=2)d_m Phi(t^m)+G(t))",
    "channel_rigidity": "all channel singularities removable implies d_m=c_m for every m>=2",
    "source_coordinate": "w=1+sqrt(2)t",
    "source_exact_ledger": "H_rel(2-w)=3/(4w)-(1/2)log(w)-3/2",
    "source_multiplier": "w^beta exp(-a/w)",
    "gauge_torsor": "remaining multipliers are a torsor under nowhere-zero holomorphic functions on the unit disk",
    "genus_m_minus_1_multiplier": "exp(sum_(m>=2)c_m Phi(t^m)); G=0",
    "genus_m_minus_1_channel_residual": "1",
    "normalized_full_residual": "exp(3/2)*w^(1/2)*exp(-3/(4w))*W_-*C_rel=1",
    "genus_m_multiplier": "exp(sum_(m>=2)c_m Phi(t^m)-2sum_(m>=2)c_m t^m)",
    "genus_m_channel_residual": "exp(-2sum_(m>=2)c_m t^m)",
}


def validate(core: dict[str, object]) -> None:
    if type(core) is not dict:
        raise ValueError("schema")
    for key, expected in PROTECTED_SCALARS.items():
        if core.get(key) != expected:
            raise ValueError(key)
    if core.get("source_forced_pair") != {"a": "3/4", "beta": "1/2"}:
        raise ValueError("source pair")
    if core.get("source_forced_residual") != {
        "pole_coefficient": "0", "log_coefficient": "0", "constant": "-3/2"
    }:
        raise ValueError("source residual")
    if core.get("claim_status") != EXPECTED_STATUS:
        raise ValueError("claim status")

    rows = core.get("channel_ledger")
    if type(rows) is not list or len(rows) != CHANNEL_ORDER - 1:
        raise ValueError("channel ledger")
    for expected_m, row in enumerate(rows, start=2):
        if row.get("m") != expected_m:
            raise ValueError("channel order")
        if Fraction(row.get("c_m")) != c_euler(expected_m):
            raise ValueError("channel coefficient")
        if Fraction(row.get("forced_d_m")) != c_euler(expected_m):
            raise ValueError("forced sign")
        if row.get("genus_m_minus_1_residual_log") != "0":
            raise ValueError("annihilation")
        if row.get("genus_m_residual_log") != f"{-2*c_euler(expected_m)}*t^{expected_m}":
            raise ValueError("source residual sign")

    checks = core.get("coefficient_crosscheck")
    if type(checks) is not list or len(checks) != SERIES_ORDER:
        raise ValueError("coefficient crosscheck")
    for expected_degree, row in enumerate(checks, start=1):
        if row.get("degree") != expected_degree:
            raise ValueError("coefficient degree")
        if Fraction(row.get("annihilated_residual_log")) != 0:
            raise ValueError("coefficient annihilation")
        expected = Fraction(0) if expected_degree == 1 else -2 * c_euler(expected_degree)
        if Fraction(row.get("source_preserving_residual_log")) != expected:
            raise ValueError("coefficient source residual")
        if row.get("source_preserving_residual_log") != row.get("product_form_residual_log"):
            raise ValueError("product form")

    jets = core.get("finite_jet_witnesses")
    if type(jets) is not list or len(jets) != 13:
        raise ValueError("jet witnesses")
    for order, row in enumerate(jets):
        if row.get("jet_order") != order or row.get("first_different_coefficient") != "1":
            raise ValueError("jet witness")


def mutation_audit(core: dict[str, object]) -> dict[str, object]:
    mutations: list[tuple[str, callable]] = []
    for key in PROTECTED_SCALARS:
        mutations.append((key, lambda trial, k=key: trial.__setitem__(k, "FORGED")))
    mutations.extend([
        ("source-a-sign", lambda trial: trial["source_forced_pair"].__setitem__("a", "-3/4")),
        ("source-beta", lambda trial: trial["source_forced_pair"].__setitem__("beta", "-1/2")),
        ("source-constant", lambda trial: trial["source_forced_residual"].__setitem__("constant", "0")),
        ("forced-d-sign", lambda trial: trial["channel_ledger"][0].__setitem__("forced_d_m", str(-c_euler(2)))),
        ("zero-channel", lambda trial: trial["channel_ledger"][1].__setitem__("c_m", "0")),
        ("annihilation-nonzero", lambda trial: trial["channel_ledger"][2].__setitem__("genus_m_minus_1_residual_log", "1")),
        ("genus-m-sign", lambda trial: trial["channel_ledger"][3].__setitem__("genus_m_residual_log", "FORGED")),
        ("crosscheck-drop", lambda trial: trial["coefficient_crosscheck"].pop()),
        ("residual-flip", lambda trial: trial["coefficient_crosscheck"][7].__setitem__("source_preserving_residual_log", str(2*c_euler(8)))),
        ("product-disagree", lambda trial: trial["coefficient_crosscheck"][10].__setitem__("product_form_residual_log", "999")),
        ("jet-delete", lambda trial: trial["finite_jet_witnesses"].pop()),
        ("jet-fake", lambda trial: trial["finite_jet_witnesses"][5].__setitem__("first_different_coefficient", "0")),
    ])
    for key, forged in (
        ("channel_coefficient_rigidity", "OPEN"),
        ("negative_source_pair_rigidity", "HEURISTIC"),
        ("holomorphic_gauge_torsor", "OPEN"),
        ("genus_m_minus_1_trivialization", "ABSOLUTELY_CANONICAL"),
        ("genus_m_source_residual", "OPEN"),
        ("finite_jet_uniqueness", "PROVED"),
        ("absolute_canonical_gauge", "PROVED"),
        ("operator_ownership", "PROVED"),
        ("arithmetic_advance", "YES"),
        ("route_b_authorized", True),
    ):
        mutations.append((f"status-{key}", lambda trial, k=key, v=forged: trial["claim_status"].__setitem__(k, v)))

    rejected: list[str] = []
    for name, mutate in mutations:
        trial = copy.deepcopy(core)
        mutate(trial)
        try:
            validate(trial)
        except (ValueError, TypeError, ZeroDivisionError):
            rejected.append(name)
    return {
        "attempted": len(mutations),
        "rejected": rejected,
        "all_rejected": len(rejected) == len(mutations),
    }


def build() -> dict[str, object]:
    core = core_payload()
    validate(core)
    audit = mutation_audit(core)
    if not audit["all_rejected"]:
        raise RuntimeError("mutation audit failed")
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
    payload = build()
    args.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps({
        "candidate_id": "HCS-P74",
        "channels": len(payload["channel_ledger"]),
        "series_order": len(payload["coefficient_crosscheck"]),
        "finite_jet_witnesses": len(payload["finite_jet_witnesses"]),
        "mutations": payload["mutation_audit"]["attempted"],
        "core_sha256": payload["core_sha256"],
        "check": True,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
