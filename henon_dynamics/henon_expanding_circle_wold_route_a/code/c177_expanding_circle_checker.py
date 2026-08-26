#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C177."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c177_expanding_circle_evidence.json"
checks = 0


def require(condition: bool, message: str) -> None:
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def factors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mu(n: int) -> int:
    count = 0
    divisor = 2
    remaining = n
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            remaining //= divisor
            count += 1
            if remaining % divisor == 0:
                return 0
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        count += 1
    return -1 if count & 1 else 1


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    data = json.loads(path.read_text())
    body = dict(data)
    claimed = body.pop("payload_sha256")
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    require(sha256(raw).hexdigest() == claimed, "payload hash")
    require(set(data) == {
        "schema", "candidate_id", "date_utc", "source_commit", "scope_literal",
        "evaluator", "source_lock", "periodic_theorem", "operator_theorem",
        "correlation_theorem", "finite_replay", "progress_and_boundary",
        "route_a", "scope_flags", "nonclaims", "payload_sha256",
    }, "top-level closure")
    require(data["schema"] == "HCS-C177-v1", "schema")
    require(data["candidate_id"] == "HCS-C177", "candidate")
    require(data["date_utc"] == "2026-08-26", "date")
    require(data["source_commit"] == "100e5f601a0196710d53784bdeef40d2bff89fa8", "source commit")
    require(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")

    evaluator = data["evaluator"]
    require(set(evaluator) == {"path", "version", "sha256"}, "evaluator closure")
    require(evaluator["path"] == "flow_systems/skills/route-a-evaluator.md", "evaluator path")
    require(evaluator["version"] == "0.2.0", "evaluator version")
    require(evaluator["sha256"] == "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c", "evaluator hash")

    lock = data["source_lock"]
    require(set(lock) == {"object", "family", "clock", "measure", "fourier_convention", "zeta_convention", "cutoff", "allowed_data", "forbidden_data"}, "lock closure")
    require("T_b(x)=b*x" in lock["object"], "object")
    require(lock["family"] == "every integer b>=2 on R/Z", "family")
    require(lock["clock"] == "one application of T_b", "clock")
    require(lock["measure"] == "normalized Haar measure", "measure")
    require("U_b f=f after T_b" in lock["fourier_convention"], "Fourier convention")
    require("Artin--Mazur" in lock["zeta_convention"], "zeta convention")
    require("2<=b<=12" in lock["cutoff"] and "|m|<=72" in lock["cutoff"], "cutoff")
    require("target zero or prime tables" in lock["forbidden_data"], "forbidden")

    periodic = data["periodic_theorem"]
    require(set(periodic) == {"fixed_points", "exact_period_points", "primitive_cycles", "artin_mazur_zeta", "euler_product"}, "periodic closure")
    require(periodic["fixed_points"] == "#Fix(T_b^n)=b^n-1 for every b>=2 and n>=1", "fixed theorem")
    require("mu(n/d)" in periodic["exact_period_points"], "Mobius theorem")
    require(periodic["primitive_cycles"] == "C_b(n)=P_b(n)/n", "cycle theorem")
    require(periodic["artin_mazur_zeta"] == "zeta_AM,b(z)=(1-z)/(1-b*z)", "zeta theorem")
    require("coefficientwise" in periodic["euler_product"], "Euler product convention")

    operator = data["operator_theorem"]
    require(set(operator) == {"basis_action", "wold_decomposition", "shift_multiplicity", "spectrum", "adjoint", "ownership"}, "operator closure")
    require(operator["basis_action"] == "U_b e_m=e_(b*m)", "basis action")
    require("b not dividing r" in operator["wold_decomposition"] and "j>=0" in operator["wold_decomposition"], "Wold decomposition")
    require(operator["shift_multiplicity"] == "countably infinite copies of the unilateral shift", "multiplicity")
    require("closed unit disk" in operator["spectrum"] and "only Koopman eigenvalue is 1" in operator["spectrum"], "spectrum")
    require("when b divides m" in operator["adjoint"], "adjoint")
    require("proper isometry" in operator["ownership"] and "not unitary" in operator["ownership"] and "no ordinary Fredholm determinant" in operator["ownership"], "ownership")

    correlation = data["correlation_theorem"]
    require(set(correlation) == {"homogeneous_norm", "bound", "sharpness", "transfer"}, "correlation closure")
    require("m!=0" in correlation["homogeneous_norm"], "homogeneous norm")
    require("b^(-n*s)" in correlation["bound"] and "mean-zero" in correlation["bound"], "correlation bound")
    require("attains" in correlation["sharpness"], "sharpness")
    require(correlation["transfer"] == "the Perron operator is U_b^* and erases modes not divisible by b", "transfer")

    replay = data["finite_replay"]
    require(set(replay) == {
        "b_min", "b_max", "n_max", "mode_max", "correlation_n_max",
        "sobolev_s_max", "periodic_rows", "wold_rows", "correlation_rows",
        "periodic_row_count", "wold_row_count", "correlation_row_count",
    }, "replay closure")
    require((replay["b_min"], replay["b_max"], replay["n_max"], replay["mode_max"], replay["correlation_n_max"], replay["sobolev_s_max"]) == (2, 12, 12, 72, 8, 4), "bounds")

    expected_periodic = []
    for b in range(2, 13):
        for n in range(1, 13):
            fixed = b**n - 1
            exact = sum(mu(n // d) * (b**d - 1) for d in factors(n))
            require(exact >= 0, f"nonnegative exact count {b},{n}")
            require(exact % n == 0, f"cycle integrality {b},{n}")
            recovered = sum(
                sum(mu(d // e) * (b**e - 1) for e in factors(d))
                for d in factors(n)
            )
            require(recovered == fixed, f"Mobius inversion {b},{n}")
            expected_periodic.append({"b": b, "n": n, "fixed_points": fixed, "exact_period_points": exact, "primitive_cycles": exact // n})
    require(replay["periodic_rows"] == expected_periodic, "periodic rows")
    require(replay["periodic_row_count"] == 132, "periodic row count")

    expected_wold = []
    for b in range(2, 13):
        for m in range(-72, 73):
            if m == 0:
                root, level, sector = 0, 0, "constant"
            else:
                root, level = m, 0
                while root % b == 0:
                    root //= b
                    level += 1
                sector = "unilateral_shift"
                require(root % b != 0, f"primitive root {b},{m}")
                require(root * b**level == m, f"chain reconstruction {b},{m}")
            expected_wold.append({
                "b": b, "input_mode": m, "output_mode": b * m,
                "chain_root": root, "chain_level": level,
                "output_chain_level": 0 if m == 0 else level + 1,
                "adjoint_output": m // b if m % b == 0 else None,
                "sector": sector,
            })
    require(replay["wold_rows"] == expected_wold, "Wold rows")
    require(replay["wold_row_count"] == 1595, "Wold row count")

    expected_correlations = []
    for b in range(2, 13):
        for n in range(1, 9):
            for s in range(1, 5):
                denominator = b ** (n * s)
                require(denominator >= b, f"contraction {b},{n},{s}")
                expected_correlations.append({
                    "b": b, "n": n, "s": s,
                    "sharp_test_f_mode": b**n, "sharp_test_g_mode": 1,
                    "normalized_correlation_numerator": 1,
                    "normalized_correlation_denominator": denominator,
                })
    require(replay["correlation_rows"] == expected_correlations, "correlation rows")
    require(replay["correlation_row_count"] == 352, "correlation row count")

    progress = data["progress_and_boundary"]
    require(set(progress) == {"progress", "parameter_blindness", "natural_extension", "evidence_boundary"}, "progress closure")
    require("all-b" in progress["progress"] and "Wold" in progress["progress"] and "Sobolev" in progress["progress"], "progress")
    require("prime and composite b" in progress["parameter_blindness"], "parameter blindness")
    require("changed phase space" in progress["natural_extension"], "extension boundary")
    require("regression-test" in progress["evidence_boundary"], "evidence boundary")

    route = data["route_a"]
    require(set(route) == {"tuple", "overall", "A0_qualification", "A1_qualification", "A2_qualification", "A3_qualification", "A4_qualification", "route_b_invocation_allowed"}, "route closure")
    require(route["tuple"] == ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "route tuple")
    require(route["overall"] == "ROUTE_A_REJECTED", "overall")
    require(route["A0_qualification"] == "DEGREE_PARAMETER_HAS_NO_INTRINSIC_PRIME_OR_ARITHMETIC_ORIGIN", "A0")
    require(route["A1_qualification"] == "COMPLETE_PRIMITIVE_ORBIT_LEDGER_BUT_ONLY_GENERIC_DEGREE_DATA", "A1")
    require(route["A2_qualification"] == "RATIONAL_SOURCE_ZETA_HAS_NO_TARGET_DIVISOR_MATCH", "A2")
    require(route["A3_qualification"] == "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_CONTINUATION_COMPARISON", "A3")
    require("CHANGING_PHASE_SPACE" in route["A4_qualification"], "A4")
    require(route["route_b_invocation_allowed"] is False, "Route B")

    flags = data["scope_flags"]
    require(set(flags) == {"used_target_zero_table", "used_target_prime_table", "used_arithmetic_local_data", "claimed_target_divisor_match", "claimed_target_functional_equation", "claimed_hilbert_polya", "route_b_invocation_allowed"}, "flags closure")
    require(not any(flags.values()), "all scope flags false")
    require(len(data["nonclaims"]) == 5, "nonclaim count")
    joined = " ".join(data["nonclaims"])
    require("novelty" in joined and "Hilbert--Polya" in joined and "external peer review" in joined, "nonclaim boundary")
    print(json.dumps({"status": "C177_INDEPENDENT_CHECK_PASS", "assertions": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
