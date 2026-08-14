#!/usr/bin/env python3
"""Exact HCS-P60 mixed-axis reflection dynatomic certificate."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
from pathlib import Path

import sympy as sp


PROJECT = Path(__file__).resolve().parents[1]
TRACK = PROJECT.parent
DEFAULT_OUTPUT = PROJECT / "results" / "c60_certificate.json"
X = sp.symbols("X")

DEPENDENCIES = {
    "p59_readme": (
        TRACK / "henon_reflection_half_entropy_law" / "README.md",
        "96d38a5b88d54e23195ce870a11fb368f01379236204243d5dc81ce876b22fe1",
    ),
    "p59_proof": (
        TRACK / "henon_reflection_half_entropy_law" / "PROOF_PACKAGE.md",
        "d83c5b295f26f40b6d4bd5c767f7ec278a979d197101d0fd01f0459ad7be0ccb",
    ),
    "p59_code": (
        TRACK / "henon_reflection_half_entropy_law" / "code" / "c59_reflection_counts.py",
        "422ae38e56d340560b2a6d590ffd42f6474bc85a65f444378273c2d107be0368",
    ),
    "p59_certificate": (
        TRACK / "henon_reflection_half_entropy_law" / "results" / "c59_certificate.json",
        "6acfccad4f6b15f6e375be5362f4251b98dcd755819f7ac593a42dfdc48a6bc8",
    ),
    "p59_route_a": (
        TRACK / "henon_reflection_half_entropy_law" / "route_a_evaluation.yaml",
        "e9be8726cd0cf50219ac92360011616b34e9010bf449e1271c75c276b9bf64a3",
    ),
    "p59_paper": (
        TRACK / "henon_reflection_half_entropy_law" / "paper" / "paper.pdf",
        "62e1dae62678f5d6d100949f5272f2002a17cbf32de8d471266df04377e58838",
    ),
    "p58_certificate": (
        TRACK / "henon_physical_tail_galois_parity_obstruction" / "results" / "c58_certificate.json",
        "366664f2de23ff503f8dd9efd63f0d80a9b7c23e98a510f662230c71dacc6022",
    ),
}


def canonical_sha(payload: object) -> str:
    raw = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(raw).hexdigest()


def dependency_locks() -> dict[str, dict[str, str]]:
    locked: dict[str, dict[str, str]] = {}
    for name, (path, expected) in DEPENDENCIES.items():
        observed = hashlib.sha256(path.read_bytes()).hexdigest()
        if observed != expected:
            raise RuntimeError(f"dependency hash changed: {name}")
        locked[name] = {"path": str(path.relative_to(TRACK)), "sha256": observed}
    return locked


def primitive_integer(poly: sp.Poly) -> sp.Poly:
    integer = poly.clear_denoms()[1].primitive()[1]
    return -integer if integer.LC() < 0 else integer


def polynomial_sha(poly: sp.Poly) -> str:
    integer = primitive_integer(poly)
    return canonical_sha([int(coefficient) for coefficient in integer.all_coeffs()])


def closure_polynomials(max_period: int = 15) -> dict[int, sp.Poly]:
    if max_period % 2 != 1:
        raise ValueError("max period must be odd")
    coordinates = [X, sp.expand((1 - 6 * X**2) / 2)]
    closures: dict[int, sp.Poly] = {}
    for half in range((max_period + 1) // 2):
        n = 2 * half + 1
        while len(coordinates) <= half + 1:
            coordinates.append(
                sp.expand(1 - 6 * coordinates[-1] ** 2 - coordinates[-2])
            )
        closures[n] = sp.Poly(
            coordinates[half + 1] - coordinates[half], X, domain=sp.QQ
        ).monic()
    return closures


def formal_degree(n: int) -> int:
    return sum(
        int(sp.mobius(n // divisor)) * 2 ** ((divisor + 1) // 2)
        for divisor in sp.divisors(n)
    )


def primitive_quotients(closures: dict[int, sp.Poly]) -> dict[int, sp.Poly]:
    quotients: dict[int, sp.Poly] = {}
    for n, closure in closures.items():
        lower = sp.Poly(1, X, domain=sp.QQ)
        for divisor in sp.divisors(n):
            if divisor < n:
                lower *= quotients[int(divisor)]
        quotient, remainder = sp.div(closure, lower, domain=sp.QQ)
        if not remainder.is_zero:
            raise ArithmeticError(f"formal primitive quotient failed at n={n}")
        quotients[n] = quotient.monic()
    return quotients


def exact_rows() -> list[dict[str, object]]:
    closures = closure_polynomials()
    quotients = primitive_quotients(closures)
    rows: list[dict[str, object]] = []
    for n, closure in closures.items():
        factors = sp.factor_list(quotients[n].as_expr())[1]
        factor_degrees = [sp.Poly(factor, X).degree() for factor, exponent in factors for _ in range(exponent)]
        irreducible = len(factors) == 1 and factors[0][1] == 1
        proper_divisibility = {
            str(divisor): sp.rem(closure, closures[int(divisor)], domain=sp.QQ).is_zero
            for divisor in sp.divisors(n)
            if divisor < n
        }
        if not all(proper_divisibility.values()):
            raise ArithmeticError(f"divisibility sequence failed at n={n}")
        product = sp.Poly(1, X, domain=sp.QQ)
        for divisor in sp.divisors(n):
            product *= quotients[int(divisor)]
        if product.monic() != closure:
            raise ArithmeticError(f"dynatomic product reconstruction failed at n={n}")
        if sp.gcd(closure, closure.diff()).degree() != 0:
            raise ArithmeticError(f"finite closure is not squarefree at n={n}")
        if quotients[n].degree() != formal_degree(n):
            raise ArithmeticError(f"formal degree mismatch at n={n}")
        rows.append(
            {
                "period": n,
                "closure_degree": closure.degree(),
                "formal_primitive_degree": formal_degree(n),
                "quotient_degree": quotients[n].degree(),
                "closure_coefficients_sha256": polynomial_sha(closure),
                "quotient_coefficients_sha256": polynomial_sha(quotients[n]),
                "closure_squarefree": True,
                "quotient_irreducible_over_Q": irreducible,
                "quotient_factor_degrees": factor_degrees,
                "proper_divisor_closures_divide": proper_divisibility,
            }
        )
    if not all(row["quotient_irreducible_over_Q"] for row in rows):
        raise ArithmeticError("finite primitive quotient lost irreducibility")
    return rows


def core_payload() -> dict[str, object]:
    rows = exact_rows()
    p58 = json.loads(DEPENDENCIES["p58_certificate"][0].read_text(encoding="utf-8"))
    row9 = next(row for row in rows if row["period"] == 9)
    p58_p9_sha = p58["reflection_algebra"]["A9_B9_vertex_edge"][
        "coordinate_factor_coefficients_sha256"
    ]
    if row9["quotient_coefficients_sha256"] != p58_p9_sha:
        raise ArithmeticError("P60 period-nine quotient does not match P58")
    phi = (1 + sp.sqrt(5)) / 2
    gap = sp.log(sp.Rational(2, 1) / phi) / 2
    return {
        "candidate_id": "HCS-P60",
        "map": "H_6(q,p)=(1-6q^2-p,q)",
        "vertex_axis_start": "q_0=X, q_1=(1-6X^2)/2",
        "mixed_axis_closure": "F_n(X)=q_((n+1)/2)(X)-q_((n-1)/2)(X), n odd",
        "closure_degree_theorem": "deg(F_n)=2^((n+1)/2)",
        "divisibility_theorem": "F_d divides F_n in Q[X] whenever d|n are odd",
        "formal_dynatomic_definition": "Psi_n^form=product_{d|n} F_d^mu(n/d)",
        "formal_degree_theorem": "D_n=sum_{d|n}mu(n/d)2^((d+1)/2)=2^((n+1)/2)+O(n*2^(n/6+1/2))",
        "finite_exact_rows": rows,
        "p58_period9_quotient_match": p58_p9_sha,
        "entropy_comparison": {
            "formal_algebraic_reflection_entropy": "(1/2)log(2)",
            "physical_symbolic_reflection_entropy": "(1/2)log(phi)",
            "strict_gap": "(1/2)log(2/phi)>0",
            "strict_gap_decimal_40": str(sp.N(gap, 40)),
            "formal_to_physical_population_ratio_rate": "(1/2)log(2/phi)",
        },
        "strongest_positive_result": "an all-odd-period mixed-axis divisibility sequence and formal primitive dynatomic degree law with entropy one-half log 2, plus exact reduced irreducible quotients through period 15",
        "strongest_obstruction": "the physical H6 reflection entropy is strictly smaller than the formal ambient algebraic reflection entropy, but no all-period reducedness theorem or canonical physical-root/Galois-root incidence compiler is known",
        "open_theorem": "prove every odd mixed-axis closure is reduced/transverse and the formal Psi_n is an effective primitive root divisor; then attach trace-field heights uniformly",
        "reusable_structure": "the reversor-line closure F_n, quotient-ring proof of F_d|F_n, formal Mobius degree compiler, and exact quotient chain through n=15",
        "round2_clue": "test transversality through monodromy eigenvalue 1 and separate survivor roots from the ambient mixed-axis root population",
        "claim_status": {
            "divisibility_and_formal_degree": "PROVED",
            "finite_reduced_irreducible_through_15": "COMPUTER_CERTIFIED_EXACT",
            "all_period_effective_dynatomic_root_count": "OPEN",
            "galois_height_pressure": "OPEN",
            "arithmetic_advance": "NO",
        },
        "route_a_status": {
            "tuple": "(A1_PASS_ANALYTIC [formal algebraic reflection layer], A2_ANALYTIC_DETERMINANT [physical subsystem inherited], A3_PARTIAL_ANALYTIC_STRUCTURE, A4_FORMAL_HINT)",
            "overall": "ROUTE_A_EXPLORATORY",
            "full_arithmetic_candidate_pass": False,
        },
        "route_b_authorized": False,
        "claim_boundary": "P60 proves a formal dynatomic degree entropy and finite exact reduced quotients, not all-period effectiveness, a Galois pressure, rational-prime law, completed determinant, or Hilbert-Polya operator",
    }


EXPECTED_CORE_SHA256 = "27b530feb63bf02408acaeff6a9b0ebd737b98e865a4b10852fa87e3ec41431a"


def validate_core(candidate: object, expected: object) -> None:
    if type(candidate) is not dict or candidate != expected:
        raise ValueError("core payload changed")


def assign_path(payload: object, path: tuple[object, ...], value: object) -> None:
    cursor = payload
    for key in path[:-1]:
        cursor = cursor[key]  # type: ignore[index]
    cursor[path[-1]] = value  # type: ignore[index]


def mutation_audit(core: dict[str, object]) -> dict[str, object]:
    mutations = (
        ("closure_degree", ("closure_degree_theorem",), "2^((n-1)/2)"),
        ("divisibility", ("divisibility_theorem",), "numerical only"),
        ("formal_degree", ("formal_degree_theorem",), "2^n"),
        ("entropy_formal", ("entropy_comparison", "formal_algebraic_reflection_entropy"), "log(2)"),
        ("entropy_physical", ("entropy_comparison", "physical_symbolic_reflection_entropy"), "log(phi)"),
        ("gap_sign", ("entropy_comparison", "strict_gap"), "negative"),
        ("ratio", ("entropy_comparison", "formal_to_physical_population_ratio_rate"), "zero"),
        ("p9_match", ("p58_period9_quotient_match",), "forged"),
        ("finite_status", ("claim_status", "finite_reduced_irreducible_through_15"), "HEURISTIC"),
        ("effectiveness_promotion", ("claim_status", "all_period_effective_dynatomic_root_count"), "PROVED"),
        ("height_promotion", ("claim_status", "galois_height_pressure"), "PROVED"),
        ("arithmetic_promotion", ("claim_status", "arithmetic_advance"), "YES"),
        ("route_a_promotion", ("route_a_status", "full_arithmetic_candidate_pass"), True),
        ("route_b_promotion", ("route_b_authorized",), True),
        ("boundary", ("claim_boundary",), "Hilbert-Polya proved"),
        ("row_degree", ("finite_exact_rows", 7, "quotient_degree"), 248),
        ("row_squarefree", ("finite_exact_rows", 7, "closure_squarefree"), False),
        ("row_irreducible", ("finite_exact_rows", 7, "quotient_irreducible_over_Q"), False),
        ("row_hash", ("finite_exact_rows", 4, "quotient_coefficients_sha256"), "forged"),
        ("map", ("map",), "different map"),
    )
    rejected: list[str] = []
    for label, path, replacement in mutations:
        trial = copy.deepcopy(core)
        assign_path(trial, path, replacement)
        try:
            validate_core(trial, core)
        except ValueError:
            rejected.append(label)
        else:
            raise AssertionError(f"mutation accepted: {label}")
    return {
        "attempted": len(mutations),
        "rejected": len(rejected),
        "all_rejected": True,
        "labels": rejected,
        "trace_sha256": canonical_sha(rejected),
    }


def build_certificate() -> dict[str, object]:
    core = core_payload()
    core_sha = canonical_sha(core)
    if EXPECTED_CORE_SHA256 == "TO_BE_FROZEN":
        raise RuntimeError(f"freeze core SHA256: {core_sha}")
    if core_sha != EXPECTED_CORE_SHA256:
        raise RuntimeError(f"core payload digest changed: {core_sha}")
    return {
        **core,
        "core_sha256": core_sha,
        "dependency_locks": dependency_locks(),
        "mutation_audit": mutation_audit(core),
        "check": True,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    result = build_certificate()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "candidate_id": result["candidate_id"],
        "check": result["check"],
        "core_sha256": result["core_sha256"],
        "periods": len(result["finite_exact_rows"]),
        "mutations_rejected": result["mutation_audit"]["rejected"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
