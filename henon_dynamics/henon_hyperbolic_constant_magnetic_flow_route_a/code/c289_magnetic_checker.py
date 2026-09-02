#!/usr/bin/env python3
"""Strict producer-independent Lorentz-frame checker for HCS-C289."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from fractions import Fraction
from pathlib import Path
from typing import Any

import mpmath as mp
import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c289_magnetic_evidence.json"
YAML_PATH = ROOT / "evaluations/route_a/HCS-C289/2026-09-02.yaml"
SOURCE = "7fbe9db30cc460a82883533d7cfb2edd988c5b65"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788307200
TUPLE = ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]

MODEL = {
    "configuration": "the simply connected oriented surface H^2 of curvature -kappa^2",
    "equation": "D_t velocity=b J velocity with constant speed v",
    "parameters": "kappa>0, v>0, and b real",
    "ambient_frame": "e0=kappa X is unit timelike and (e0,T,JT) is Lorentz orthonormal",
    "frame_ode": "for the matrix F=(e0,T,JT) of frame columns, F'=F A with the displayed right-action generator",
    "clock": "physical trajectory time t",
}
THEOREM = {
    "classification": "every nonstationary orbit is exactly a circle, horocycle, hypercycle, or geodesic according to |b| versus kappa v",
    "circle": "if |b|>kappa v every orbit is a hyperbolic circle of primitive period 2 pi/sqrt(b^2-kappa^2 v^2)",
    "critical": "if |b|=kappa v every orbit is a nonclosed horocycle and the Lorentz generator is nonzero nilpotent",
    "subcritical": "if 0<|b|<kappa v every orbit is an unbounded hypercycle and if b=0 it is a geodesic",
    "generator": "the raw Lorentz-frame generator satisfies A^3=(kappa^2 v^2-b^2)A",
    "boundary": "orientation, zero field, zero speed, and the Euclidean curvature limit are kept separate",
}
PROOF = {
    "frenet": "constant speed turns the magnetic equation into signed geodesic curvature b/v",
    "geometry": "the complete classification of constant-geodesic-curvature curves on H^2 gives the four orbit types",
    "lorentz": "differentiate the ambient Lorentz frame and classify its one-parameter subgroup by the cubic identity",
    "period": "the circle relation kappa coth(kappa rho)=|b|/v and its circumference give the primitive period",
    "circle_primitivity": "the embedded circle at nonzero constant speed first returns after one circumference; equivalently its nonzero rotating basepoint component returns iff sqrt(delta)t lies in 2 pi Z",
    "critical_basepoint": "at equality exp(tA)e0 has T-coordinate kappa v t, so no nonzero time returns the base point",
    "completeness": "the frame ODE has a global exponential for every initial frame and exhausts all magnetic initial data",
    "finite_role": "finite cells audit signs, thresholds, and periods but do not prove the all-parameter theorem",
}
ROUTE = {"tuple": TUPLE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}
FLAGS = {
    "arithmetic_local_data": False,
    "euler_factors": False,
    "root_numbers": False,
    "automorphy": False,
    "target_divisor_or_counting_law": False,
    "target_functional_equation": False,
    "target_zero_match": False,
    "hilbert_polya_operator": False,
    "route_b_input": False,
}
REFERENCES = [
    {"id": "Comtet1987", "authors": "Alain Comtet", "title": "On the Landau Levels on the Hyperbolic Plane", "venue": "Annals of Physics 173 (1987), 185-209", "identifier": "10.1016/0003-4916(87)90098-4", "url": "https://doi.org/10.1016/0003-4916(87)90098-4", "ownership": "direct owner of the classical and quantum constant-field problem on the hyperbolic plane"},
    {"id": "Adachi1995", "authors": "Toshiaki Adachi", "title": "Kaehler Magnetic Flows for a Manifold of Constant Holomorphic Sectional Curvature", "venue": "Tokyo Journal of Mathematics 18 (1995), 473-483", "identifier": "10.3836/tjm/1270043477", "url": "https://doi.org/10.3836/tjm/1270043477", "ownership": "direct geometric owner for magnetic trajectories on constant-curvature Kaehler space forms"},
]
NONCLAIMS = [
    "the classical circle-horocycle-hypercycle classification is not claimed as literature originality",
    "finite rational cells are regression evidence and do not replace the all-parameter proof",
    "a magnetic Laplacian is only a formal quantization hint here; no self-adjoint operator or spectrum is constructed",
]
TOP_KEYS = {
    "schema", "candidate_id", "evaluation_date", "source_commit", "fixed_epoch",
    "scope_literal", "evaluator", "model", "theorem_contract", "proof_contract",
    "route_a", "scope_flags", "enumeration", "orbit_cells", "boundary_cells",
    "references", "nonclaims", "payload_sha256",
}
ROW_KEYS = {
    "kappa", "speed", "field", "geodesic_curvature", "discriminant",
    "orbit_type", "orientation", "closed", "period_over_2pi_squared", "shape_tanh",
}
YAML_KEYS = {
    "schema", "candidate_id", "title", "evaluation_date", "source_commit",
    "fixed_epoch", "scope_literal", "evaluator_authority", "evaluator_version",
    "evaluator_authority_sha256", "obstruction_id", "candidate_definition",
    "family", "phase_space", "dynamics", "parameters", "parameter_provenance",
    "arithmetic_origin", "clock", "normalization", "determinant_convention",
    "orbit_cutoff", "precision", "training_data", "forbidden_data",
    "artifact_paths", "a0", "a1", "a2", "a3", "a4", "tuple",
    "overall_verdict", "route_b_invocation_allowed", "route_b_lock_reason",
    "scope_flags", "theorem_status", "finite_evidence_role", "source_owner_tokens",
}
YAML_SEMANTIC_SHA = "0c1fb9d1e91cd69e18c2fa2ff074ce0f237341810a225d7c9798414307a31c86"


class Checks:
    def __init__(self) -> None:
        self.n = 0

    def ok(self, condition: bool, label: str) -> None:
        self.n += 1
        if not condition:
            raise AssertionError(label)


def reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def strict_load(path: Path) -> dict[str, Any]:
    result = json.loads(path.read_text(), object_pairs_hook=reject_duplicates, parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    if type(result) is not dict:
        raise TypeError("top-level object required")
    return result


class UniqueYAMLLoader(yaml.SafeLoader):
    """Safe YAML loader which rejects duplicate mapping keys."""


def construct_unique_mapping(loader: UniqueYAMLLoader, node: yaml.nodes.MappingNode, deep: bool = False) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in result:
            raise ValueError(f"duplicate YAML key: {key}")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueYAMLLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_unique_mapping)


def validate_route_yaml(c: Checks, path: Path) -> None:
    value = yaml.load(path.read_text(), Loader=UniqueYAMLLoader)
    exact_keys(c, value, YAML_KEYS, "route yaml")
    c.ok(value["schema"] == "route-a-evaluation-v0.2.0", "yaml schema")
    c.ok(value["candidate_id"] == "HCS-C289" and value["evaluation_date"] == "2026-09-02", "yaml identity")
    c.ok(value["source_commit"] == SOURCE and value["fixed_epoch"] == EPOCH and type(value["fixed_epoch"]) is int, "yaml source epoch")
    c.ok(value["scope_literal"] == SCOPE and value["evaluator_authority_sha256"] == EVALUATOR, "yaml scope evaluator")
    c.ok(value["obstruction_id"] == "HEN-O273" and value["orbit_cutoff"] == "not applicable", "yaml obstruction cutoff")
    c.ok(value["tuple"] == TUPLE and type(value["tuple"]) is list and all(type(item) is str for item in value["tuple"]), "yaml tuple")
    c.ok(value["overall_verdict"] == "ROUTE_A_REJECTED" and value["route_b_invocation_allowed"] is False, "yaml verdict route b")
    c.ok(value["a4"]["verdict"] == "A4_FORMAL_HINT" and value["a4"]["evidence_status"] == "BOUNDED_NONCLAIM", "yaml A4 bound")
    c.ok(value["scope_flags"] == FLAGS and all(type(item) is bool for item in value["scope_flags"].values()), "yaml flags")
    c.ok(value["source_owner_tokens"] == ["10.1016/0003-4916(87)90098-4", "10.3836/tjm/1270043477"], "yaml source owners")
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    c.ok(hashlib.sha256(raw.encode()).hexdigest() == YAML_SEMANTIC_SHA, "yaml exact semantic hash")


def phash(data: dict[str, Any]) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def exact_keys(c: Checks, value: Any, keys: set[str], label: str) -> None:
    c.ok(type(value) is dict, f"{label} object")
    c.ok(set(value) == keys, f"{label} keys")


def exact_type(c: Checks, value: Any, cls: type, label: str) -> None:
    c.ok(type(value) is cls, f"{label} type")


def rat(c: Checks, value: Any, label: str) -> Fraction:
    exact_type(c, value, str, label)
    try:
        result = Fraction(value)
    except (ValueError, ZeroDivisionError) as error:
        raise AssertionError(f"{label} rational") from error
    c.ok(str(result) == value, f"{label} canonical")
    return result


def matmul(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0]))] for i in range(len(left))]


def transpose(value: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*value)]


def add(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[left[i][j] + right[i][j] for j in range(len(left[0]))] for i in range(len(left))]


def scale(value: Fraction, matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    return [[value * entry for entry in row] for row in matrix]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", type=Path, default=DEFAULT)
    parser.add_argument("--yaml", type=Path, default=YAML_PATH)
    args = parser.parse_args()
    data = strict_load(args.input)
    c = Checks()
    exact_keys(c, data, TOP_KEYS, "top")
    exact_type(c, data["payload_sha256"], str, "hash")
    c.ok(re.fullmatch(r"[0-9a-f]{64}", data["payload_sha256"]) is not None, "hash syntax")
    c.ok(data["payload_sha256"] == phash(data), "payload hash")
    c.ok(data["schema"] == "hcs-c289-hyperbolic-magnetic-flow-v1", "schema")
    c.ok(data["candidate_id"] == "HCS-C289", "candidate")
    c.ok(data["evaluation_date"] == "2026-09-02", "date")
    c.ok(data["source_commit"] == SOURCE, "source")
    exact_type(c, data["fixed_epoch"], int, "epoch")
    c.ok(data["fixed_epoch"] == EPOCH, "epoch value")
    c.ok(data["scope_literal"] == SCOPE, "scope")
    exact_keys(c, data["evaluator"], {"version", "sha256"}, "evaluator")
    c.ok(data["evaluator"] == {"version": "0.2.0", "sha256": EVALUATOR}, "evaluator value")
    for name, expected in (("model", MODEL), ("theorem_contract", THEOREM), ("proof_contract", PROOF), ("route_a", ROUTE), ("scope_flags", FLAGS)):
        exact_keys(c, data[name], set(expected), name)
        c.ok(data[name] == expected, f"{name} value")
    exact_type(c, data["route_a"]["tuple"], list, "route tuple")
    c.ok(all(type(value) is str for value in data["route_a"]["tuple"]), "route tuple item types")
    exact_type(c, data["route_a"]["overall"], str, "route overall")
    exact_type(c, data["route_a"]["route_b_invocation_allowed"], bool, "route b")
    c.ok(all(type(value) is bool and value is False for value in data["scope_flags"].values()), "all flags false")

    kappas = (Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3))
    speeds = (Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3))
    fields = tuple(Fraction(x) for x in (-6, -3, -2, -1, 0, 1, 2, 3, 6))
    expected_grid = {(k, v, b) for k in kappas for v in speeds for b in fields}
    enumeration = data["enumeration"]
    exact_keys(c, enumeration, {"kappa_values", "speed_values", "field_values", "orbit_cells", "boundary_cells", "type_counts"}, "enumeration")
    c.ok(enumeration["kappa_values"] == [str(x) for x in kappas], "kappa list")
    c.ok(enumeration["speed_values"] == [str(x) for x in speeds], "speed list")
    c.ok(enumeration["field_values"] == [str(x) for x in fields], "field list")
    exact_type(c, enumeration["orbit_cells"], int, "orbit count")
    exact_type(c, enumeration["boundary_cells"], int, "boundary count")
    c.ok(enumeration["orbit_cells"] == len(expected_grid) == 144, "orbit count value")
    c.ok(enumeration["boundary_cells"] == 5, "boundary count value")

    rows = data["orbit_cells"]
    exact_type(c, rows, list, "orbit rows")
    c.ok(len(rows) == 144, "orbit rows count")
    seen: set[tuple[Fraction, Fraction, Fraction]] = set()
    type_counts = {name: 0 for name in ("circle", "horocycle", "hypercycle", "geodesic")}
    eta = [[Fraction(-1), Fraction(0), Fraction(0)], [Fraction(0), Fraction(1), Fraction(0)], [Fraction(0), Fraction(0), Fraction(1)]]
    zero = [[Fraction(0) for _ in range(3)] for _ in range(3)]
    mp.mp.dps = 70
    for index, row in enumerate(rows):
        exact_keys(c, row, ROW_KEYS, f"row {index}")
        k = rat(c, row["kappa"], f"row {index} kappa")
        v = rat(c, row["speed"], f"row {index} speed")
        b = rat(c, row["field"], f"row {index} field")
        key = (k, v, b)
        c.ok(key in expected_grid, f"row {index} key")
        c.ok(key not in seen, f"row {index} unique")
        seen.add(key)
        curvature = rat(c, row["geodesic_curvature"], f"row {index} curvature")
        delta = rat(c, row["discriminant"], f"row {index} discriminant")
        c.ok(curvature == b / v, f"row {index} curvature value")
        c.ok(delta == b * b - k * k * v * v, f"row {index} delta value")
        a = k * v
        A = [[Fraction(0), a, Fraction(0)], [a, Fraction(0), -b], [Fraction(0), b, Fraction(0)]]
        c.ok(add(matmul(matmul(transpose(A), eta), [[Fraction(1),0,0],[0,Fraction(1),0],[0,0,Fraction(1)]]), matmul(eta, A)) == zero, f"row {index} Lorentz algebra")
        A2 = matmul(A, A)
        A3 = matmul(A2, A)
        e0 = [[Fraction(1)], [Fraction(0)], [Fraction(0)]]
        Ae0 = matmul(A, e0)
        A2e0 = matmul(A2, e0)
        c.ok(A3 == scale(-delta, A), f"row {index} cubic")
        exact_type(c, row["orbit_type"], str, f"row {index} type")
        exact_type(c, row["orientation"], int, f"row {index} orientation")
        exact_type(c, row["closed"], bool, f"row {index} closed")
        c.ok(row["orientation"] == (0 if b == 0 else (1 if b > 0 else -1)), f"row {index} orientation value")
        if delta > 0:
            expected_type, expected_closed = "circle", True
            expected_shape, expected_period = a / abs(b), 1 / delta
            numerical = mp.matrix([[mp.mpf(x.numerator) / x.denominator for x in line] for line in A])
            period = 2 * mp.pi / mp.sqrt(mp.mpf(delta.numerator) / delta.denominator)
            monodromy = mp.expm(numerical * period)
            c.ok(max(abs(monodromy[i, j] - (1 if i == j else 0)) for i in range(3) for j in range(3)) < mp.mpf("1e-55"), f"row {index} full-period return")
            c.ok(Ae0[1][0] == a and A2e0 != [[Fraction(0)], [Fraction(0)], [Fraction(0)]], f"row {index} nonzero rotating basepoint component")
            c.ok(A2e0[0][0] == a * a and A2e0[1][0] == 0, f"row {index} basepoint return forces sin(theta)=0 and cos(theta)=1")
            half = mp.expm(numerical * (period / 2))
            c.ok(max(abs(half[i, 0] - (1 if i == 0 else 0)) for i in range(3)) > mp.mpf("1e-30"), f"row {index} half-turn basepoint nonreturn")
        elif delta == 0:
            expected_type, expected_closed = "horocycle", False
            expected_shape, expected_period = Fraction(1), None
            c.ok(A2 != zero and A3 == zero, f"row {index} nonzero nilpotent")
            c.ok(Ae0 == [[Fraction(0)], [a], [Fraction(0)]] and A2e0[1][0] == 0, f"row {index} critical basepoint T-coordinate equals kappa*v*t for every nonzero t")
        elif b == 0:
            expected_type, expected_closed = "geodesic", False
            expected_shape, expected_period = Fraction(0), None
        else:
            expected_type, expected_closed = "hypercycle", False
            expected_shape, expected_period = abs(b) / a, None
        c.ok(row["orbit_type"] == expected_type, f"row {index} classification")
        c.ok(row["closed"] is expected_closed, f"row {index} closure")
        type_counts[expected_type] += 1
        shape = rat(c, row["shape_tanh"], f"row {index} shape")
        c.ok(shape == expected_shape, f"row {index} shape value")
        if expected_period is None:
            c.ok(row["period_over_2pi_squared"] is None, f"row {index} no period")
        else:
            period_sq = rat(c, row["period_over_2pi_squared"], f"row {index} period")
            c.ok(period_sq == expected_period, f"row {index} period value")
            c.ok(0 < shape < 1, f"row {index} circle radius relation")
    c.ok(seen == expected_grid, "complete grid")
    exact_keys(c, enumeration["type_counts"], set(type_counts), "type counts")
    c.ok(enumeration["type_counts"] == type_counts, "type count values")

    expected_boundaries = [
        {"name": "zero_speed", "parameters": {"kappa": "1", "speed": "0", "field": "2"}, "conclusion": "stationary curve; the unit-frame theorem is not invoked"},
        {"name": "euclidean_circle", "parameters": {"kappa": "0", "speed": "3", "field": "2"}, "conclusion": "Euclidean circle with period_over_2pi_squared=1/4"},
        {"name": "euclidean_line", "parameters": {"kappa": "0", "speed": "3", "field": "0"}, "conclusion": "Euclidean straight line"},
        {"name": "field_reversal", "parameters": {"kappa": "2", "speed": "1", "field_pair": "-3,3"}, "conclusion": "same unoriented circle and period with opposite orientation"},
        {"name": "critical_nonclosure", "parameters": {"kappa": "2", "speed": "3", "field": "6"}, "conclusion": "horocycle, nonzero nilpotent generator, and no primitive period"},
    ]
    exact_type(c, data["boundary_cells"], list, "boundaries")
    c.ok(data["boundary_cells"] == expected_boundaries, "boundary values")
    exact_type(c, data["references"], list, "references")
    c.ok(data["references"] == REFERENCES, "reference values")
    exact_type(c, data["nonclaims"], list, "nonclaims")
    c.ok(data["nonclaims"] == NONCLAIMS, "nonclaim values")
    validate_route_yaml(c, args.yaml)
    print(f"C289 independent Lorentz-frame checker: PASS ({c.n} assertions; strict duplicate-rejecting schema)")


if __name__ == "__main__":
    main()
