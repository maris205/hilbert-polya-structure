#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C171."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from math import comb
from pathlib import Path


D_MAX, N_MAX = 18, 24
EXPECTED_TOP = {
    "schema", "candidate_id", "evaluation_date", "scope_literal", "source_commit", "source_lock",
    "walsh_spectral_theorem", "trace_determinant_theorem", "return_theorem", "lumping_theorem",
    "arithmetic_controls", "finite_ledgers", "route_a", "claim_boundary", "integrity", "payload_sha256",
}


def frac(text: str) -> Fraction:
    return Fraction(text)


def qtext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def digest(data: dict) -> str:
    work = dict(data)
    work.pop("payload_sha256", None)
    raw = json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def krawtchouk(d: int, j: int, k: int) -> int:
    lo, hi = max(0, j - d + k), min(j, k)
    return sum((-1) ** r * comb(k, r) * comb(d - k, j - r) for r in range(lo, hi + 1))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence", nargs="?", type=Path,
                        default=Path(__file__).resolve().parents[1] / "results/c171_ehrenfest_evidence.json")
    parser.add_argument("--mutation-fast", action="store_true")
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    assertions = 0

    def check(condition: bool, label: str) -> None:
        nonlocal assertions
        assertions += 1
        if not condition:
            raise AssertionError(label)

    check(set(data) == EXPECTED_TOP, "top-level keys")
    check(data["payload_sha256"] == digest(data), "canonical payload hash")
    check(data["schema"] == "hcs-c171-ehrenfest-hypercube-trace-v1", "schema")
    check(data["candidate_id"] == "HCS-C171", "candidate")
    check(data["evaluation_date"] == "2026-08-26", "date")
    check(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    check(data["source_commit"] == "ee8af7b8e265fa4f901d5ed2d1c2edd51475b06f", "commit")
    lock = data["source_lock"]
    check(set(lock) == {"object", "parameters", "arithmetic_origin", "clock", "normalization",
                        "determinant_convention", "cutoff", "precision", "allowed_data", "forbidden_data"}, "lock keys")
    check(lock["object"].startswith("P_d f(x)=d^(-1)"), "object")
    check(lock["parameters"] == "integer d>=1; no fitted parameter", "parameters")
    check(lock["arithmetic_origin"].startswith("none:"), "arithmetic origin")
    check(lock["clock"] == "one uniformly chosen coordinate flip is one Markov step", "clock")
    check(lock["determinant_convention"] == "D_d(z)=det(I-z P_d)", "determinant")
    check(lock["cutoff"] == {"d_max": D_MAX, "n_max": N_MAX}, "cutoff")
    check(lock["precision"] == "exact integers and rational arithmetic", "precision")
    check("target zeros" in lock["forbidden_data"] and "Route B" in lock["forbidden_data"], "forbidden")

    ws = data["walsh_spectral_theorem"]
    check(set(ws) == {"characters", "eigenvalue", "multiplicity", "complete_orthogonal_basis", "all_d"}, "Walsh keys")
    check(ws["eigenvalue"] == "P_d chi_S=(1-2|S|/d) chi_S", "Walsh law")
    check(ws["multiplicity"] == "binom(d,j) at lambda_j=1-2j/d", "multiplicity law")
    check(ws["complete_orthogonal_basis"] is True and ws["all_d"] is True, "Walsh completeness")
    td = data["trace_determinant_theorem"]
    check(set(td) == {"trace", "determinant", "trace_log", "family_uniform_artin_mazur_interpretation", "reason", "d1_boundary"}, "trace keys")
    check(td["family_uniform_artin_mazur_interpretation"] is False and "for every d>1" in td["reason"] and "deterministic two-cycle" in td["d1_boundary"], "not uniformly AM with d=1 boundary")
    rt = data["return_theorem"]
    check(rt == {"formula": "P_d^n(x,x)=2^(-d) Tr(P_d^n), independently of x",
                 "odd_times_zero": True,
                 "reason": "the hypercube is bipartite and every step changes parity"}, "return theorem")
    lump = data["lumping_theorem"]
    check(set(lump) == {"weight_coordinate", "kernel", "stationary_measure", "reversibility",
                        "symmetric_similarity", "krawtchouk_eigenvectors", "simple_spectrum", "spectral_compression"}, "lump keys")
    check(lump["kernel"] == "Q(k,k+1)=(d-k)/d and Q(k,k-1)=k/d", "kernel")
    check("2^d to d+1" in lump["spectral_compression"], "compression")
    controls = data["arithmetic_controls"]
    check(len(controls) == 4, "control count")
    check([x["name"] for x in controls] == ["randomized arithmetic labels", "composite-only dimension labels",
                                               "neighboring dimensions", "lazy-kernel parent"], "control names")

    rows = data["finite_ledgers"]
    check(len(rows) == D_MAX, "ledger count")
    for d, row in enumerate(rows, 1):
        expected_keys = {"d", "dimension", "distinct_eigenvalues", "multiplicities", "multiplicity_sum",
                         "trace_n_0_to_24", "return_probability_n_0_to_24", "odd_return_probabilities_zero",
                         "determinant_factors", "lumped_stationary_weights", "lumped_upper_probabilities",
                         "lumped_lower_probabilities", "detailed_balance_edge_weights",
                         "symmetric_offdiagonal_squared", "krawtchouk_endpoint_checksum"}
        check(set(row) == expected_keys, f"row {d} keys")
        check(row["d"] == d and row["dimension"] == 2**d, f"row {d} id/dimension")
        lambdas = [Fraction(d - 2*j, d) for j in range(d + 1)]
        mult = [comb(d, j) for j in range(d + 1)]
        check(row["distinct_eigenvalues"] == [qtext(x) for x in lambdas], f"row {d} eigenvalues")
        check(row["multiplicities"] == mult and row["multiplicity_sum"] == 2**d, f"row {d} multiplicities")
        traces = [sum(Fraction(m)*lam**n for lam, m in zip(lambdas, mult)) for n in range(N_MAX+1)]
        check(row["trace_n_0_to_24"] == [qtext(x) for x in traces], f"row {d} traces")
        check(row["return_probability_n_0_to_24"] == [qtext(x/(2**d)) for x in traces], f"row {d} returns")
        check(row["odd_return_probabilities_zero"] is True, f"row {d} odd")
        check(row["determinant_factors"] == [{"eigenvalue": qtext(x), "exponent": mult[j]}
                                                for j, x in enumerate(lambdas)], f"row {d} factors")
        pi = [Fraction(comb(d,k), 2**d) for k in range(d+1)]
        check(row["lumped_stationary_weights"] == [qtext(x) for x in pi], f"row {d} pi")
        check(row["lumped_upper_probabilities"] == [qtext(Fraction(d-k,d)) for k in range(d)] + ["0"], f"row {d} upper")
        check(row["lumped_lower_probabilities"] == ["0"] + [qtext(Fraction(k,d)) for k in range(1,d+1)], f"row {d} lower")
        edges = [pi[k]*Fraction(d-k,d) for k in range(d)]
        check(row["detailed_balance_edge_weights"] == [qtext(x) for x in edges], f"row {d} balance")
        for k in range(d):
            check(edges[k] == pi[k+1]*Fraction(k+1,d), f"row {d} balance identity {k}")
        check(row["symmetric_offdiagonal_squared"] == [qtext(Fraction((k+1)*(d-k),d*d)) for k in range(d)], f"row {d} similarity")
        checksums = [krawtchouk(d,j,0)+krawtchouk(d,j,d) for j in range(d+1)]
        check(row["krawtchouk_endpoint_checksum"] == checksums, f"row {d} K checksum")
        for j in range(d+1):
            lam = lambdas[j]
            for k in range(d+1):
                lhs = Fraction(0)
                if k < d:
                    lhs += Fraction(d-k,d)*krawtchouk(d,j,k+1)
                if k > 0:
                    lhs += Fraction(k,d)*krawtchouk(d,j,k-1)
                check(lhs == lam*krawtchouk(d,j,k), f"K eigen d={d},j={j},k={k}")

    route = data["route_a"]
    check(route == {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
                    "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}, "route")
    boundary = data["claim_boundary"]
    check(set(boundary) == {"all_parameter_spectral_theorem", "all_parameter_lumping_theorem", "finite_ledgers_are_proof",
                            "uniform_all_d_artin_mazur_zeta", "prime_or_prime_power_correspondence", "target_divisor_matching",
                            "target_functional_equation_or_counting_law", "arithmetic_local_data", "euler_factors",
                            "root_numbers", "automorphy", "hilbert_polya_operator"}, "boundary keys")
    check(boundary["all_parameter_spectral_theorem"] and boundary["all_parameter_lumping_theorem"], "positive boundary")
    check(not any(boundary[k] for k in boundary if k not in {"all_parameter_spectral_theorem", "all_parameter_lumping_theorem"}), "negative boundary")
    integrity = data["integrity"]
    check(integrity["hard_gate_status"] == "PASS" and integrity["pivot_required"] is False, "hard gate")
    check(integrity["registered_citation_population"] == 0 and integrity["external_reviewer_simulated"] is False, "integrity")

    if not args.mutation_fast:
        # Independent closed-walk enumeration for small cubes.
        for d in range(1, 8):
            size = 2**d
            current = [[1 if x == y else 0 for y in range(size)] for x in range(size)]
            adjacency = [[x ^ (1 << i) for i in range(d)] for x in range(size)]
            for n in range(0, 9):
                if n:
                    nxt = [[0]*size for _ in range(size)]
                    for x in range(size):
                        for mid in adjacency[x]:
                            source_row = current[mid]
                            target_row = nxt[x]
                            for y, value in enumerate(source_row):
                                target_row[y] += value
                    current = nxt
                loop_count = sum(current[x][x] for x in range(size))
                formula = sum(comb(d,j)*(d-2*j)**n for j in range(d+1))
                check(loop_count == formula, f"brute loops d={d},n={n}")

    print(json.dumps({"status": "C171_CHECKER_PASS", "assertions": assertions}, sort_keys=True))


if __name__ == "__main__":
    main()
