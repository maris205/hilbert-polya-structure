#!/usr/bin/env python3
"""Producer-independent double-precision checker for HCS-C275."""
from __future__ import annotations

import hashlib
import json
import math
import os
from fractions import Fraction as Q
from pathlib import Path

from scipy import special

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = Path(os.environ.get("C275_EVIDENCE_PATH", ROOT / "results/c275_poncelet_evidence.json"))
SOURCE = "418bcec5afb1f9e5905cc6e2ba7f9e099fef2e02"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788220800
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
ASSERTIONS = 0


def ck(condition: bool, label: str) -> None:
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(label)


def payload_hash(data: dict) -> str:
    copy = dict(data)
    copy.pop("payload_sha256", None)
    raw = json.dumps(copy, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def fq(text: str) -> float:
    return float(Q(text))


def close(a: float, b: float, tolerance: float = 3e-12) -> bool:
    return math.isclose(a, b, rel_tol=tolerance, abs_tol=tolerance)


def rotation(e: float, f: float) -> tuple[float, float, float, float]:
    complete = float(special.ellipk(e * e))
    omega = math.asin(math.sqrt((e * e - f * f) / (e * e * (1 - f * f))))
    incomplete = float(special.ellipkinc(omega, e * e))
    return incomplete / (2 * complete), omega, incomplete, complete


def point(e: float, f: float, theta: float) -> tuple[float, float]:
    complete = float(special.ellipk(e * e))
    sn, cn, _dn, _phase = special.ellipj(4 * complete * theta, e * e)
    return -float(sn) / f, math.sqrt(1 - f * f) * float(cn) / f


def outer_residual(f: float, z: tuple[float, float]) -> float:
    x, y = z
    return f * f * x * x + f * f * y * y / (1 - f * f) - 1


def tangent_residual(e: float, z0: tuple[float, float], z1: tuple[float, float]) -> float:
    x0, y0 = z0
    x1, y1 = z1
    aa, bb, cc = y0 - y1, x1 - x0, x0 * y1 - x1 * y0
    raw = cc * cc - aa * aa / (e * e) - bb * bb * (1 - e * e) / (e * e)
    scale = max(1.0, abs(cc * cc), abs(aa * aa / (e * e)),
                abs(bb * bb * (1 - e * e) / (e * e)))
    return raw / scale


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    expected_top = {
        "a4_liftability", "candidate_id", "evaluation_date", "evaluator", "fixed_epoch", "nonclaims",
        "owner", "payload_sha256", "proof_obligations", "regression", "route_a",
        "schema", "scope_flags", "scope_literal", "source_commit", "sources",
        "theorem_contract",
    }
    ck(set(data) == expected_top, "top-level schema")
    ck(data["schema"] == "hcs-c275-elliptic-billiard-poncelet-v1", "schema")
    ck(data["candidate_id"] == "HCS-C275", "candidate")
    ck(data["evaluation_date"] == "2026-09-01", "date")
    ck(data["source_commit"] == SOURCE, "source")
    ck(data["fixed_epoch"] == EPOCH, "epoch")
    ck(data["scope_literal"] == SCOPE, "scope")
    ck(data["evaluator"] == {
        "path": "flow_systems/skills/route-a-evaluator.md",
        "version": "0.2.0", "sha256": EVALUATOR,
    }, "evaluator")
    ck(data["payload_sha256"] == payload_hash(data), "payload hash")
    ck(data["owner"]["parameter_domain"] == "0<f<e<1", "domain")
    ck(data["owner"]["clock"] == "one billiard reflection", "clock")
    ck("elliptic-caustic" in data["owner"]["phase_space"], "sector")
    ck("hyperbolic caustics" in data["owner"]["excluded_sector"], "excluded sector")

    theorem = data["theorem_contract"]
    ck("F(omega,e)/(2K(e))" in theorem["rotation_number"], "rotation contract")
    ck(theorem["strict_monotonicity"] == "partial_e rho>0 and partial_f rho<0 on 0<f<e<1",
       "monotonicity contract")
    ck("minimal period q" in theorem["porism"], "minimal period contract")
    ck("unit tangent derivative" in theorem["clean_family"], "derivative contract")
    ck("ambient Jordan type" in theorem["sector_firewall"], "ambient firewall")
    ck(len(data["proof_obligations"]) == 7, "proof obligations")

    a4 = data["a4_liftability"]
    ck(set(a4) == {
        "ambient_quantum_owner", "classical_owner_clock", "classification",
        "coherent_ambient_quantization", "fixed_caustic_orbit_phases_weights_preserved",
        "gate_reason", "same_clock_quantum_return_constructed", "target_identification",
    }, "A4 schema")
    ck(a4["classification"] == "A4_FORMAL_HINT", "A4 classification")
    quantum = a4["ambient_quantum_owner"]
    ck(set(quantum) == {
        "antiunitary_time_reversal", "compact_resolvent", "domain_geometry",
        "hilbert_space", "operator", "operator_domain", "self_adjoint",
        "time_parameter", "unitary_group",
    }, "ambient quantum schema")
    ck(quantum["domain_geometry"] == "Omega_f is the smooth bounded interior of E(f)",
       "quantum domain geometry")
    ck(quantum["hilbert_space"] == "L^2(Omega_f)", "quantum Hilbert space")
    ck(quantum["operator"] == "-Delta_D", "quantum operator")
    ck(quantum["operator_domain"] == "H^2(Omega_f) cap H_0^1(Omega_f)",
       "quantum operator domain")
    ck(quantum["self_adjoint"] is True and quantum["compact_resolvent"] is True,
       "self-adjoint compact-resolvent facts")
    ck(quantum["unitary_group"] == "U(t)=exp(-it(-Delta_D))", "unitary group")
    ck(quantum["time_parameter"] == "continuous physical flight time", "quantum clock")
    ck(quantum["antiunitary_time_reversal"] ==
       "C is complex conjugation; C U(t) C=U(-t)", "antiunitary time reversal")
    ck(a4["classical_owner_clock"] == "one billiard reflection", "classical A4 clock")
    ck(a4["coherent_ambient_quantization"] is True, "ambient quantization coherence")
    ck(a4["same_clock_quantum_return_constructed"] is False, "same-clock gate")
    ck(a4["fixed_caustic_orbit_phases_weights_preserved"] is False,
       "fixed-caustic phase/weight gate")
    ck(a4["target_identification"] is False, "A4 target nonclaim")
    ck("one-reflection Poincare map" in a4["gate_reason"] and
       "same-clock quantum return" in a4["gate_reason"] and
       "phase/weight bridge" in a4["gate_reason"], "A4 gate reason")

    route = data["route_a"]
    ck(route["tuple"] == [
        "A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"
    ], "route tuple")
    ck(route["overall"] == "ROUTE_A_REJECTED", "overall")
    ck(route["route_b_invocation_allowed"] is False, "route B")
    expected_flags = {
        "arithmetic_local_data", "automorphy", "euler_factors", "functional_equation",
        "hilbert_polya_operator", "root_numbers", "target_divisor",
    }
    ck(set(data["scope_flags"]) == expected_flags, "scope flag keys")
    for key, value in data["scope_flags"].items():
        ck(value is False, f"scope flag {key}")
    ck(len(data["nonclaims"]) == 5, "nonclaims length")
    ck(any("not an ambient unipotent" in item for item in data["nonclaims"]), "unipotent firewall")
    ck(any("only positive-orientation elliptic caustics" in item for item in data["nonclaims"]),
       "hyperbolic firewall")
    ck(any("only an A4 formal hint" in item and "same-clock quantum return" in item
           for item in data["nonclaims"]), "A4 nonclaim")
    ck(len(data["sources"]) == 3, "source count")
    ck(data["sources"][0]["identifier"] == "arXiv:2309.08013v1", "primary arxiv")
    ck(data["sources"][0]["doi"] == "10.48550/arXiv.2309.08013", "arxiv doi")
    ck(data["sources"][1]["doi"] == "10.1063/1.527900", "closure source")
    ck(data["sources"][2]["doi"] == "10.4064/sm-81-3-293-302", "rotation source")

    regression = data["regression"]
    ck(set(regression) == {
        "counts", "covering_cells", "endpoint_paths", "formula_cells",
        "monotonicity_in_e", "monotonicity_in_f", "porism_cases",
    }, "regression schema")
    counts = regression["counts"]
    ck(counts == {
        "formula_cells": 32, "covering_cells": 192, "monotonicity_values": 117,
        "endpoint_values": 96, "porism_cases": 24, "porism_vertex_cells": 128,
        "return_derivative_cells": 24,
    }, "counts")

    formula_lookup: dict[tuple[str, str], float] = {}
    for index, cell in enumerate(regression["formula_cells"]):
        ck(set(cell) == {"e", "f", "f_over_e", "omega", "F_omega_e", "K_e", "rho"},
           f"formula schema {index}")
        e, f = fq(cell["e"]), fq(cell["f"])
        ck(0 < f < e < 1, f"formula domain {index}")
        ck(close(f / e, fq(cell["f_over_e"])), f"formula ratio {index}")
        rho, omega, incomplete, complete = rotation(e, f)
        ck(close(float(cell["omega"]), omega), f"omega {index}")
        ck(close(float(cell["F_omega_e"]), incomplete), f"F {index}")
        ck(close(float(cell["K_e"]), complete), f"K {index}")
        ck(close(float(cell["rho"]), rho), f"rho {index}")
        ck(0 < rho < 0.5, f"rho range {index}")
        formula_lookup[(cell["e"], cell["f"])] = rho
    ck(len(formula_lookup) == 32, "formula uniqueness")

    for index, cell in enumerate(regression["covering_cells"]):
        ck(set(cell) == {
            "e", "f", "theta", "next_theta", "point", "next_point",
            "outer_residual", "next_outer_residual", "caustic_tangency_relative_residual",
            "deck_period_error",
        }, f"covering schema {index}")
        e, f, theta = fq(cell["e"]), fq(cell["f"]), fq(cell["theta"])
        rho = formula_lookup[(cell["e"], cell["f"])]
        ck(close(float(cell["next_theta"]), theta + rho), f"next theta {index}")
        z0, z1 = point(e, f, theta), point(e, f, theta + rho)
        ck(all(close(float(cell["point"][j]), z0[j]) for j in range(2)), f"point {index}")
        ck(all(close(float(cell["next_point"][j]), z1[j]) for j in range(2)), f"next point {index}")
        r0, r1 = outer_residual(f, z0), outer_residual(f, z1)
        tangent = tangent_residual(e, z0, z1)
        deck = point(e, f, theta + 1)
        deck_error = max(abs(deck[j] - z0[j]) for j in range(2))
        ck(abs(r0) < 4e-12 and abs(r1) < 4e-12, f"outer geometry {index}")
        ck(abs(tangent) < 2e-11, f"tangency {index}")
        ck(deck_error < 2e-11, f"deck {index}")
        ck(abs(float(cell["outer_residual"])) < 1e-65, f"stored outer {index}")
        ck(abs(float(cell["next_outer_residual"])) < 1e-65, f"stored next outer {index}")
        ck(abs(float(cell["caustic_tangency_relative_residual"])) < 1e-65,
           f"stored tangent {index}")
        ck(abs(float(cell["deck_period_error"])) < 1e-65, f"stored deck {index}")

    monotone_value_count = 0
    for row_index, row in enumerate(regression["monotonicity_in_f"]):
        ck(row["direction"] == "strictly_decreasing_in_f", f"f direction {row_index}")
        e = fq(row["fixed_e"])
        prior_f, prior_rho = 0.0, 1.0
        for item_index, item in enumerate(row["values"]):
            f = fq(item["f"])
            rho = rotation(e, f)[0]
            ck(prior_f < f < e, f"f order {row_index}:{item_index}")
            ck(rho < prior_rho, f"rho decreases {row_index}:{item_index}")
            ck(close(float(item["rho"]), rho), f"f rho value {row_index}:{item_index}")
            prior_f, prior_rho = f, rho
            monotone_value_count += 1
    for row_index, row in enumerate(regression["monotonicity_in_e"]):
        ck(row["direction"] == "strictly_increasing_in_e", f"e direction {row_index}")
        f = fq(row["fixed_f"])
        prior_e, prior_rho = f, -1.0
        for item_index, item in enumerate(row["values"]):
            e = fq(item["e"])
            rho = rotation(e, f)[0]
            ck(prior_e < e < 1, f"e order {row_index}:{item_index}")
            ck(rho > prior_rho, f"rho increases {row_index}:{item_index}")
            ck(close(float(item["rho"]), rho), f"e rho value {row_index}:{item_index}")
            prior_e, prior_rho = e, rho
            monotone_value_count += 1
    ck(monotone_value_count == counts["monotonicity_values"], "monotone count")

    endpoint_value_count = 0
    valid_paths = {
        "f_to_e_minus": 0.0, "e_to_f_plus": 0.0,
        "f_to_zero_plus": 0.5, "e_to_one_minus": 0.5,
    }
    for path_index, row in enumerate(regression["endpoint_paths"]):
        ck(row["path"] in valid_paths, f"endpoint path {path_index}")
        limit = valid_paths[row["path"]]
        ck(close(float(Q(row["limit"])), limit), f"endpoint limit {path_index}")
        prior_error = 1.0
        for item_index, item in enumerate(row["values"]):
            e, f = fq(item["e"]), fq(item["f"])
            rho = rotation(e, f)[0]
            error = abs(rho - limit)
            ck(0 < f < e < 1, f"endpoint domain {path_index}:{item_index}")
            ck(close(float(item["rho"]), rho), f"endpoint rho {path_index}:{item_index}")
            ck(close(float(item["error_to_limit"]), error), f"endpoint error {path_index}:{item_index}")
            ck(error < prior_error, f"endpoint convergence {path_index}:{item_index}")
            prior_error = error
            endpoint_value_count += 1
    ck(endpoint_value_count == counts["endpoint_values"], "endpoint count")

    porism_vertices = 0
    for case_index, case in enumerate(regression["porism_cases"]):
        p, q = int(case["p"]), int(case["q"])
        e, f = fq(case["e"]), float(case["f"])
        ck(math.gcd(p, q) == 1 and 0 < 2 * p < q, f"reduced rotation {case_index}")
        complete = float(special.ellipk(e * e))
        sn, cn, dn, _phase = special.ellipj(2 * complete * p / q, e * e)
        expected_f = e * float(cn) / float(dn)
        ck(close(f, expected_f, 2e-11), f"inverse f {case_index}")
        rho = rotation(e, f)[0]
        ck(close(rho, p / q, 2e-11), f"porism rho {case_index}")
        ck(close(float(case["rho_recovered"]), rho, 2e-11), f"stored porism rho {case_index}")
        ck(close(float(case["q_rho"]), p, 2e-11), f"q rho {case_index}")
        ck(case["minimal_period"] == q, f"minimal period field {case_index}")
        for k in range(1, q):
            ck((k * p) % q != 0, f"no shorter period {case_index}:{k}")
        ck(case["tangent_q_return_derivative"] == "1", f"return derivative {case_index}")
        ck(case["restricted_q_return"] == "identity_on_the_entire_elliptic_caustic_curve",
           f"restricted return {case_index}")
        ck(case["periodic_orbit_family"] == "one_parameter_circle_quotient",
           f"family {case_index}")
        ck(case["isolated_orbit_product_applicable"] is False, f"A2 obstruction {case_index}")
        ck(case["ambient_unipotent_conclusion"] is False, f"ambient guard {case_index}")
        ck(len(case["vertices"]) == q, f"vertex count {case_index}")
        theta0 = float(case["vertices"][0]["theta"])
        max_outer, max_tangent = 0.0, 0.0
        for j, vertex in enumerate(case["vertices"]):
            theta = theta0 + j * p / q
            z0, z1 = point(e, f, theta), point(e, f, theta + p / q)
            ck(vertex["j"] == j, f"vertex index {case_index}:{j}")
            ck(close(float(vertex["theta"]), theta, 2e-11), f"vertex theta {case_index}:{j}")
            ck(close(float(vertex["x"]), z0[0], 2e-11), f"vertex x {case_index}:{j}")
            ck(close(float(vertex["y"]), z0[1], 2e-11), f"vertex y {case_index}:{j}")
            max_outer = max(max_outer, abs(outer_residual(f, z0)))
            max_tangent = max(max_tangent, abs(tangent_residual(e, z0, z1)))
            porism_vertices += 1
        closure = point(e, f, theta0 + p)
        start = point(e, f, theta0)
        closure_error = max(abs(closure[j] - start[j]) for j in range(2))
        ck(max_outer < 5e-12, f"porism outer {case_index}")
        ck(max_tangent < 3e-11, f"porism tangent {case_index}")
        ck(closure_error < 3e-11, f"porism closure {case_index}")
        ck(abs(float(case["max_outer_residual"])) < 1e-64, f"stored max outer {case_index}")
        ck(abs(float(case["max_caustic_tangency_relative_residual"])) < 1e-64,
           f"stored max tangent {case_index}")
        ck(abs(float(case["closure_error"])) < 1e-64, f"stored closure {case_index}")
    ck(len(regression["porism_cases"]) == counts["porism_cases"], "porism count")
    ck(porism_vertices == counts["porism_vertex_cells"], "porism vertex count")

    print(
        f"C275 independent checker: PASS ({ASSERTIONS} assertions; "
        "Jacobi covering, monotonicity, porism, and sector audit)"
    )


if __name__ == "__main__":
    main()
