#!/usr/bin/env python3
"""Independent standard-library checker for the C130 evidence.

This module deliberately does not import the producer or SymPy.
"""
from __future__ import annotations

import hashlib
import itertools
import json
import math
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results" / "c130_suspension_evidence.json"
PREFIX = 10
Poly = dict[tuple[int, int], int]


def canonical_payload(data: dict) -> bytes:
    body = dict(data)
    body.pop("payload_sha256", None)
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def padd(left: Poly, right: Poly) -> Poly:
    out = dict(left)
    for monomial, coefficient in right.items():
        out[monomial] = out.get(monomial, 0) + coefficient
        if out[monomial] == 0:
            del out[monomial]
    return out


def pscale(poly: Poly, scalar: int) -> Poly:
    return {monomial: scalar * value for monomial, value in poly.items() if scalar * value}


def pmul(left: Poly, right: Poly, cutoff: int | None = None) -> Poly:
    out: Poly = {}
    for (a, b), x in left.items():
        for (c, d), y in right.items():
            if cutoff is not None and a + b + c + d > cutoff:
                continue
            key = (a + c, b + d)
            out[key] = out.get(key, 0) + x * y
            if out[key] == 0:
                del out[key]
    return out


def mmul(left: list[list[Poly]], right: list[list[Poly]]) -> list[list[Poly]]:
    return [[
        sum_polys(pmul(left[i][k], right[k][j]) for k in range(len(right)))
        for j in range(len(right[0]))
    ] for i in range(len(left))]


def sum_polys(polys) -> Poly:
    out: Poly = {}
    for poly in polys:
        out = padd(out, poly)
    return out


def eye(n: int) -> list[list[Poly]]:
    return [[{(0, 0): 1} if i == j else {} for j in range(n)] for i in range(n)]


def mpow(matrix: list[list[Poly]], n: int) -> list[list[Poly]]:
    out = eye(len(matrix))
    base = matrix
    while n:
        if n & 1:
            out = mmul(out, base)
        base = mmul(base, base)
        n //= 2
    return out


def trace(matrix: list[list[Poly]]) -> Poly:
    return sum_polys(matrix[i][i] for i in range(len(matrix)))


def primitive(word: tuple[int, ...]) -> bool:
    n = len(word)
    return not any(n % d == 0 and word == word[:d] * (n // d) for d in range(1, n))


def least_rotation(word: tuple[int, ...]) -> tuple[int, ...]:
    return min(word[k:] + word[:k] for k in range(len(word)))


def reps(n: int) -> list[str]:
    words = {
        least_rotation(word)
        for word in itertools.product(range(2), repeat=n)
        if primitive(word)
    }
    return ["".join(str(bit) for bit in word) for word in sorted(words)]


def validate(data: dict) -> int:
    checks = 0

    def ck(condition: bool, label: str) -> None:
        nonlocal checks
        if not condition:
            raise AssertionError(label)
        checks += 1

    ck(set(data) == {
        "all_period_identity", "candidate_id", "clock_sector_separation",
        "date_utc", "frozen_model", "nonclaims", "payload_sha256",
        "progress_and_boundary", "rational_roof_control", "replay_prefix",
        "route_a", "schema", "scope_flags", "scope_literal", "source_lock",
    }, "top-level key schema")
    ck(data["payload_sha256"] == hashlib.sha256(canonical_payload(data)).hexdigest(), "payload hash")
    ck(data["schema"] == "HCS-C130-v1", "schema")
    ck(data["candidate_id"] == "HCS-C130", "candidate")
    ck(data["date_utc"] == "2026-08-24", "date")
    ck(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")

    source = data["source_lock"]
    ck(set(source) == {
        "allowed_data", "base", "clock", "determinant_convention",
        "forbidden_data", "mixing_certificate", "normalization", "precision",
        "prefix", "roof", "suspension",
    }, "source-lock key schema")
    ck(source["base"] == "two-sided full binary shift Sigma_B with B=[[1,1],[1,1]]", "base")
    ck(source["roof"] == "tau(x)=1 on symbol 0 and sqrt(2) on symbol 1", "roof")
    ck(source["clock"] == "continuous suspension time; base return count remains explicit", "clock")
    ck(source["normalization"] == "unweighted full-shift transitions and the literal roof pair (1,sqrt(2))", "normalization")
    ck(source["determinant_convention"] == "d_tau(s)=det(I-M(exp(-s),exp(-sqrt(2)*s)))", "determinant convention")
    ck("external zero tables" in source["forbidden_data"], "forbidden data")

    model = data["frozen_model"]
    ck(model["adjacency_B"] == [[1, 1], [1, 1]], "B")
    ck(model["roof_values"] == ["1", "sqrt(2)"], "roof values")
    ck(model["bivariate_transfer_matrix"] == [["u", "v"], ["u", "v"]], "M")
    ck(model["bivariate_determinant"] == "Delta(u,v)=det(I-M(u,v))=1-u-v", "det")
    ck(model["exponential_polynomial"] == "d_tau(s)=1-exp(-s)-exp(-sqrt(2)*s)", "specialization")

    one: Poly = {(0, 0): 1}
    u: Poly = {(1, 0): 1}
    v: Poly = {(0, 1): 1}
    matrix = [[u, v], [u, v]]
    det_i_minus_m = padd(pmul(padd(one, pscale(u, -1)), padd(one, pscale(v, -1))), pscale(pmul(v, u), -1))
    ck(det_i_minus_m == {(0, 0): 1, (1, 0): -1, (0, 1): -1}, "independent determinant")

    identity = data["all_period_identity"]
    ck(set(identity) == {
        "all_period", "convergence_domain", "log_determinant",
        "primitive_euler_identity", "primitive_length",
        "replay_cutoff_is_not_theorem_cutoff", "suspension_euler_identity",
        "trace_formula_bivariate", "trace_formula_specialized",
    }, "all-period key schema")
    ck(identity["all_period"] is True, "all period")
    ck(identity["replay_cutoff_is_not_theorem_cutoff"] is True, "cutoff boundary")
    ck(identity["trace_formula_bivariate"] == "Tr(M(u,v)^n)=(u+v)^n=sum_{k=0}^n binom(n,k)u^(n-k)v^k", "bivariate trace headline")
    ck(identity["trace_formula_specialized"] == "Tr(M(s)^n)=sum_{k=0}^n binom(n,k)exp(-s*((n-k)+k*sqrt(2)))", "specialized trace headline")
    ck(identity["primitive_euler_identity"] == "Delta(u,v)=product_[gamma primitive](1-u^N0(gamma)*v^N1(gamma))", "Euler identity")
    ck(identity["convergence_domain"].startswith("absolute for Re(s)>h"), "convergence")

    prefix = data["replay_prefix"]
    ck(prefix["period_limit"] == PREFIX, "prefix limit")
    rooted_total = 0
    primitive_total = 0
    all_reps: list[str] = []
    for n, row in enumerate(prefix["rows"], 1):
        expected_reps = reps(n)
        expected_trace = {(n - k, k): math.comb(n, k) for k in range(n + 1)}
        ck(row["period"] == n, f"row period {n}")
        ck(row["rooted_closed_words"] == 2**n, f"rooted {n}")
        ck(row["primitive_cycles"] == len(expected_reps), f"primitive count {n}")
        ck(row["clock_sector_count"] == n + 1, f"sector count {n}")
        ck(prefix["primitive_representatives"][str(n)] == expected_reps, f"representatives {n}")
        ck(trace(mpow(matrix, n)) == expected_trace, f"matrix trace {n}")
        evidence_sectors = {
            (sector["N0"], sector["N1"]): sector["multiplicity"]
            for sector in row["trace_sectors"]
        }
        ck(evidence_sectors == expected_trace, f"evidence trace sectors {n}")
        ck(all(sector["roof"] == f'{sector["N0"]}+{sector["N1"]}*sqrt(2)' for sector in row["trace_sectors"]), f"roof labels {n}")
        rooted_total += 2**n
        primitive_total += len(expected_reps)
        all_reps.extend(expected_reps)
    ck(prefix["rooted_closed_words_total"] == rooted_total == 2046, "rooted total")
    ck(prefix["primitive_cycles_total"] == primitive_total == 226, "primitive total")
    ck(prefix["clock_sectors_total"] == 65, "sector total")

    euler_product: Poly = {(0, 0): 1}
    for word in all_reps:
        factor = {(0, 0): 1, (word.count("0"), word.count("1")): -1}
        euler_product = pmul(euler_product, factor, PREFIX)
    ck(euler_product == {(0, 0): 1, (1, 0): -1, (0, 1): -1}, "Euler product through degree 10")

    separation = data["clock_sector_separation"]
    ck(set(separation) == {
        "basis", "consequence", "imaginary_period_proof",
        "imaginary_period_statement", "not_orbit_injectivity",
        "q_linear_independence", "same_sector_counts",
        "same_sector_primitive_example_period_6", "same_sector_roof",
        "sector_injectivity",
    }, "clock-sector key schema")
    ck(separation["q_linear_independence"] is True, "Q independence")
    ck(separation["sector_injectivity"] == "a+b*sqrt(2)=c+d*sqrt(2) for integers implies (a,b)=(c,d)", "sector injectivity")
    ck(separation["same_sector_primitive_example_period_6"] == ["000111", "001011"], "same sector pair")
    ck(all(word in prefix["primitive_representatives"]["6"] for word in separation["same_sector_primitive_example_period_6"]), "same sector primitive")
    ck(separation["same_sector_counts"] == {"N0": 3, "N1": 3}, "same counts")
    ck(separation["same_sector_roof"] == "3+3*sqrt(2)", "same roof")
    ck(separation["imaginary_period_statement"] == "d_tau(s+iT)=d_tau(s) for all s forces T=0", "nonperiodicity")

    control = data["rational_roof_control"]
    ck(control["roof_values"] == ["1", "2"], "control roof")
    ck(control["lattice_polynomial"] == "d_rat=1-q-q^2", "control polynomial")
    collision = control["cross_sector_collision"]
    ck(collision["counts_a"] == {"N0": 2, "N1": 0}, "collision a")
    ck(collision["counts_b"] == {"N0": 0, "N1": 1}, "collision b")
    ck(collision["counts_a"]["N0"] + 2 * collision["counts_a"]["N1"] == collision["common_roof_time"] == 2, "collision time a")
    ck(collision["counts_b"]["N0"] + 2 * collision["counts_b"]["N1"] == collision["common_roof_time"], "collision time b")
    ck(control["periodicity"] == "d_rat(s+2*pi*i)=d_rat(s)", "periodicity")
    ck(control["periodicity_recovered"] is True, "periodicity recovered")

    progress = data["progress_and_boundary"]
    ck(set(progress) == {"internal_obstruction", "progress", "target_obstruction"}, "progress key schema")
    ck(progress["progress"] == "an all-period primitive-orbit determinant now carries an intrinsically nonlattice continuous clock with exact sector separation", "progress headline")
    ck(progress["internal_obstruction"] == "the determinant aggregates distinct primitive necklaces that have the same symbol counts", "internal obstruction")
    ck(progress["target_obstruction"] == "no frozen external divisor, functional equation, counting law, or arithmetic interpretation is compared", "target obstruction")

    route = data["route_a"]
    ck(set(route) == {
        "A1_qualification", "A2_qualification", "A3_qualification",
        "A4_qualification", "overall", "route_b_invocation_allowed", "tuple",
    }, "Route-A key schema")
    ck(route["tuple"] == ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "tuple")
    ck(route["overall"] == "ROUTE_A_EXPLORATORY", "Route-A overall")
    ck(route["route_b_invocation_allowed"] is False, "route B")
    flags = data["scope_flags"]
    ck(flags["scope"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope flag")
    ck(not any(value for key, value in flags.items() if key != "scope"), "all scope flags false")
    ck(len(data["nonclaims"]) == 6, "nonclaims")
    ck("orbit-level injectivity inside a fixed population sector" in data["nonclaims"], "orbit nonclaim")
    return checks


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_EVIDENCE
    checks = validate(json.loads(path.read_text()))
    print(json.dumps({"status": "C130_INDEPENDENT_CHECK_PASS", "assertions": checks, "imports_producer": False, "imports_sympy": False}, sort_keys=True))


if __name__ == "__main__":
    main()
