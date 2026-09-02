#!/usr/bin/env python3
"""Producer-independent strict checker for the HCS-C295 certificate."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Any

import mpmath as mp
import yaml
from yaml.constructor import ConstructorError
from yaml.tokens import AliasToken, AnchorToken

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c295_isochrone_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C295/2026-09-02.yaml"
SOURCE = "f8d3ad9a8940b54e82854b2924be353575ed8fcb"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788307200
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
TUPLE = ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"]

MODEL = {
    "hamiltonian": "H=p_r^2/2+L^2/(2r^2)-mu/(b+sqrt(b^2+r^2))",
    "parameters": "mu>0, b>0, signed angular momentum L; ell=abs(L)",
    "phase_space": "planar central motion; polar chart for ell>0 and Cartesian continuation for ell=0",
    "clock": "physical Hamiltonian time",
    "radial_action_convention": "J_r=(1/pi) integral from periapsis to apoapsis; at ell=0 use the continuous half-line limit",
}
THEOREM = {
    "energy_domain": "bound motion exists exactly for E_c(ell)<=E<0, where E_c=-2 mu^2/(ell+sqrt(ell^2+4 mu b))^2",
    "action": "J_r=mu/sqrt(-2E)-(ell+sqrt(ell^2+4 mu b))/2",
    "period": "T_r=2 pi mu/(-2E)^(3/2), independent of ell",
    "frequency_ratio": "for ell>0, Omega_phi/Omega_r=(1+ell/sqrt(ell^2+4 mu b))/2; this is the L>=0 convention",
    "closure": "a noncircular bound orbit with ell>0 is phase-space periodic iff the frequency ratio is rational",
    "degenerate_boundaries": "circular orbits are closed independently of the ratio; ell=0 noncentral bound motions cross the smooth center and return after 2 T_r",
    "escape": "E=0 is the marginal escape threshold and E>0 is unbound; J_r and T_r diverge as E increases to zero",
    "kepler_limit": "for fixed ell>0, b decreases to zero gives J_r=mu/sqrt(-2E)-ell and frequency ratio one",
}
PROOF = {
    "substitution": "x=b+sqrt(b^2+r^2), so r^2=x(x-2b) and dt=(x-b) dx/sqrt(Q(x))",
    "quadratic": "Q(x)=2E x^2+(2mu-4bE)x-(4mu b+ell^2)",
    "period_integral": "the root sum and the arcsine integral give the exact angular-momentum-independent radial period",
    "action_integration": "partial_E J_r=T_r/(2pi), with J_r=0 at the unique circular energy",
    "apsidal_integral": "partial fractions of (x-b)/(x(x-2b)) and both root products give Delta_phi=pi(1+ell/sqrt(ell^2+4mu b))",
    "closure_logic": "return of the nonconstant radial phase forces an integer number of radial cycles; angular return is then equivalent to rational frequency ratio",
    "finite_role": "finite algebraic cells and quadrature controls are regression evidence only, not the all-parameter proof",
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
BOUNDARIES = [
    {
        "face": "below_circular_minimum",
        "statement": "E<E_c(ell) has no real radial motion",
        "status": "forbidden",
    },
    {
        "face": "circular_energy",
        "statement": "E=E_c has J_r=0 and a closed circular orbit, or the center equilibrium when ell=0",
        "status": "included",
    },
    {
        "face": "bound_open_energy",
        "statement": "E_c<E<0 gives radial oscillation",
        "status": "included",
    },
    {
        "face": "escape_threshold",
        "statement": "E=0 is marginal escape and T_r,J_r diverge",
        "status": "excluded_from_action_chart",
    },
    {
        "face": "positive_energy",
        "statement": "E>0 gives escape/scattering motion",
        "status": "unbound",
    },
    {
        "face": "zero_angular_momentum",
        "statement": "noncentral bound trajectories cross the smooth center and their full Cartesian period is 2T_r",
        "status": "separate",
    },
    {
        "face": "signed_angular_momentum",
        "statement": "the displayed positive ratio uses L>=0; negative L reverses its sign while ell=abs(L) controls the geometry",
        "status": "separate",
    },
    {
        "face": "kepler_limit",
        "statement": "b to zero at fixed ell>0 gives ratio one; ell=0 reaches the Kepler collision singularity and is not a smooth commuting corner",
        "status": "singular_corner",
    },
]
REFERENCES = [
    {
        "authors": "Michel Henon",
        "id": "Henon1959I",
        "identifier": "1959AnAp...22..126H",
        "ownership": "original isochrone-cluster construction",
        "title": "L'amas isochrone I",
        "url": "https://ui.adsabs.harvard.edu/abs/1959AnAp...22..126H/abstract",
        "venue": "Annales d'Astrophysique 22 (1959), 126-139",
    },
    {
        "authors": "Michel Henon",
        "id": "Henon1959II",
        "identifier": "1959AnAp...22..491H",
        "ownership": "original orbit calculation",
        "title": "L'amas isochrone II: Le calcul des orbites",
        "url": "https://ui.adsabs.harvard.edu/abs/1959AnAp...22..491H/abstract",
        "venue": "Annales d'Astrophysique 22 (1959), 491-498",
    },
    {
        "authors": "Paul Ramond and Jerome Perez",
        "id": "RamondPerez2021",
        "identifier": "10.1063/5.0056957",
        "ownership": "modern action-angle and Hamiltonian treatment",
        "title": "New Methods of Isochrone Mechanics",
        "url": "https://arxiv.org/abs/2104.05643",
        "venue": "Journal of Mathematical Physics 62 (2021), 112704",
    },
    {
        "authors": "Jean-Baptiste Fouvry and Simon Prunet",
        "id": "FouvryPrunet2022",
        "identifier": "10.1093/mnras/stab3020",
        "ownership": "official appendix recording the isochrone frequency map",
        "title": "Linear response theory and damped modes of stellar clusters",
        "url": "https://academic.oup.com/mnras/article/509/2/2443/6407532",
        "venue": "Monthly Notices of the Royal Astronomical Society 509 (2022), 2443-2456",
    },
]
NONCLAIMS = [
    "the isochrone potential, its action formula, and its frequency map are classical and are not claimed as literature originality",
    "finite algebraic cells and numerical quadratures do not prove the all-parameter theorem",
    "closed resonant tori are continuous families rather than isolated arithmetic primitive owners",
    "the natural Schroedinger quantization is not identified with a target Hilbert-Polya operator",
]
TOP_KEYS = {
    "schema", "candidate_id", "obstruction_id", "evaluation_date", "source_commit",
    "fixed_epoch", "scope_literal", "evaluator", "model", "theorem_contract",
    "proof_contract", "route_a", "scope_flags", "enumeration", "orbit_cells",
    "boundary_cells", "references", "nonclaims", "payload_sha256",
}
ROW_KEYS = {
    "mu", "b", "ell", "action_multiplier", "radicand", "radicand_square",
    "sqrt_radicand_decimal", "invariant_I", "radial_action", "circular_energy",
    "energy", "circular_s", "circular_radius_squared", "omega_r",
    "frequency_ratio", "period_over_2pi", "x_peri_decimal", "x_apo_decimal",
    "orbit_class", "closure_class", "primitive_radial_cycles",
}
YAML_KEYS = {
    "schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch",
    "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256",
    "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics",
    "parameters", "parameter_provenance", "arithmetic_origin", "clock", "normalization",
    "determinant_convention", "orbit_cutoff", "precision", "training_data", "forbidden_data",
    "artifact_paths", "a0", "a1", "a2", "a3", "a4", "tuple", "overall_verdict",
    "route_b_invocation_allowed", "route_b_lock_reason", "scope_flags", "theorem_status",
    "finite_evidence_role", "source_owner_tokens",
}
YAML_GATE_KEYS = {"verdict", "evidence_status", "strongest_evidence", "strongest_failure"}
YAML_SEMANTIC_SHA = "371a0e27dcd17ba950b06ab7ece415469ea998b244ba1eb6e208851182ec365d"


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
        if type(key) is not str or key in result:
            raise ValueError(f"duplicate or non-string JSON key: {key!r}")
        result[key] = value
    return result


def strict_json(path: Path) -> dict[str, Any]:
    def reject_constant(token: str) -> None:
        raise ValueError(f"nonfinite JSON constant: {token}")
    value = json.loads(path.read_text(), object_pairs_hook=reject_duplicates, parse_constant=reject_constant)
    if type(value) is not dict:
        raise TypeError("top-level JSON object required")
    return value


class UniqueYAMLLoader(yaml.SafeLoader):
    """Safe loader with recursive duplicate, merge, and non-string-key rejection."""


UniqueYAMLLoader.yaml_implicit_resolvers = {
    key: [(tag, pattern) for tag, pattern in resolvers if tag != "tag:yaml.org,2002:timestamp"]
    for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def unique_yaml_mapping(loader: UniqueYAMLLoader, node: yaml.nodes.MappingNode, deep: bool = False) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge" or key_node.value == "<<":
            raise ConstructorError("mapping", node.start_mark, "YAML merge keys forbidden", key_node.start_mark)
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in result:
            raise ConstructorError("mapping", node.start_mark, f"duplicate or non-string YAML key: {key!r}", key_node.start_mark)
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueYAMLLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_yaml_mapping)


def strict_yaml(path: Path) -> dict[str, Any]:
    text = path.read_text()
    if any(isinstance(token, (AnchorToken, AliasToken)) for token in yaml.scan(text)):
        raise ValueError("YAML anchors and aliases forbidden")
    value = yaml.load(text, Loader=UniqueYAMLLoader)
    if type(value) is not dict:
        raise TypeError("top-level YAML object required")
    return value


def payload_hash(data: dict[str, Any]) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def exact_keys(c: Checks, value: Any, expected: set[str], label: str) -> None:
    c.ok(type(value) is dict, f"{label} object")
    c.ok(set(value) == expected, f"{label} exact keys")


def exact_tree(c: Checks, value: Any, expected: Any, label: str) -> None:
    """Recursively lock both values and JSON scalar types."""
    c.ok(type(value) is type(expected), f"{label} exact type")
    if type(expected) is dict:
        c.ok(set(value) == set(expected), f"{label} exact keys")
        for key in expected:
            exact_tree(c, value[key], expected[key], f"{label}.{key}")
    elif type(expected) is list:
        c.ok(len(value) == len(expected), f"{label} exact length")
        for index, item in enumerate(expected):
            exact_tree(c, value[index], item, f"{label}[{index}]")
    else:
        c.ok(value == expected, f"{label} exact value")


def frac(c: Checks, value: Any, label: str) -> Fraction:
    c.ok(type(value) is str, f"{label} string")
    try:
        result = Fraction(value)
    except (ValueError, ZeroDivisionError) as error:
        raise AssertionError(f"{label} rational") from error
    c.ok(str(result) == value, f"{label} canonical")
    return result


def parse_quad(c: Checks, value: Any, d: int, label: str) -> tuple[Fraction, Fraction]:
    exact_keys(c, value, {"a", "c", "d"}, label)
    c.ok(type(value["d"]) is int and value["d"] == d, f"{label} radicand")
    return frac(c, value["a"], f"{label} a"), frac(c, value["c"], f"{label} c")


def qmul(x: tuple[Fraction, Fraction], y: tuple[Fraction, Fraction], d: int) -> tuple[Fraction, Fraction]:
    return x[0] * y[0] + x[1] * y[1] * d, x[0] * y[1] + x[1] * y[0]


def qval(x: tuple[Fraction, Fraction], d: int) -> mp.mpf:
    return mp.mpf(x[0].numerator) / x[0].denominator + mp.mpf(x[1].numerator) / x[1].denominator * mp.sqrt(d)


def close(c: Checks, x: mp.mpf, y: mp.mpf, label: str, tol: mp.mpf = mp.mpf("1e-48")) -> None:
    c.ok(abs(x - y) <= tol * max(mp.mpf(1), abs(x), abs(y)), label)


def validate_yaml(c: Checks, path: Path) -> dict[str, Any]:
    route = strict_yaml(path)
    exact_keys(c, route, YAML_KEYS, "route YAML")
    c.ok(route["schema"] == "route-a-evaluation-v0.2.0", "YAML schema")
    c.ok(route["candidate_id"] == "HCS-C295" and route["obstruction_id"] == "HEN-O279", "YAML ids")
    c.ok(route["evaluation_date"] == "2026-09-02" and type(route["evaluation_date"]) is str, "YAML date")
    c.ok(route["source_commit"] == SOURCE, "YAML source")
    c.ok(type(route["fixed_epoch"]) is int and route["fixed_epoch"] == EPOCH, "YAML epoch")
    c.ok(route["scope_literal"] == SCOPE, "YAML scope")
    c.ok(route["evaluator_version"] == "0.2.0" and route["evaluator_authority_sha256"] == EVALUATOR, "YAML evaluator")
    c.ok(route["artifact_paths"] == ["THEOREM_PACKAGE.md", "results/c295_isochrone_evidence.json", "paper/main.pdf"], "YAML artifacts")
    c.ok(type(route["tuple"]) is list and route["tuple"] == TUPLE and all(type(x) is str for x in route["tuple"]), "YAML tuple")
    c.ok(route["overall_verdict"] == "ROUTE_A_REJECTED", "YAML verdict")
    c.ok(type(route["route_b_invocation_allowed"]) is bool and route["route_b_invocation_allowed"] is False, "YAML Route B")
    for axis, verdict in zip(("a0", "a1", "a2", "a3", "a4"), TUPLE):
        exact_keys(c, route[axis], YAML_GATE_KEYS, f"YAML {axis}")
        c.ok(all(type(item) is str for item in route[axis].values()), f"YAML {axis} types")
        c.ok(route[axis]["verdict"] == verdict, f"YAML {axis} verdict")
    exact_keys(c, route["scope_flags"], set(FLAGS), "YAML flags")
    c.ok(route["scope_flags"] == FLAGS and all(type(v) is bool and v is False for v in route["scope_flags"].values()), "YAML flag values")
    c.ok(route["theorem_status"] == "PROVABLE_AS_STATED", "YAML theorem status")
    c.ok(route["finite_evidence_role"] == "regression_only_not_all_parameter_proof", "YAML finite role")
    c.ok(route["source_owner_tokens"] == ["1959AnAp...22..126H", "1959AnAp...22..491H", "10.1063/5.0056957", "10.1093/mnras/stab3020"], "YAML owners")
    semantic = json.dumps(route, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    c.ok(hashlib.sha256(semantic.encode()).hexdigest() == YAML_SEMANTIC_SHA, "YAML semantic hash")
    return route


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", type=Path, default=DEFAULT)
    parser.add_argument("--yaml", type=Path, default=DEFAULT_YAML)
    args = parser.parse_args()
    c = Checks()
    data = strict_json(args.input)
    exact_keys(c, data, TOP_KEYS, "top")
    c.ok(data["schema"] == "hcs-c295-henon-isochrone-action-frequency-v1", "schema")
    c.ok(data["candidate_id"] == "HCS-C295" and data["obstruction_id"] == "HEN-O279", "ids")
    c.ok(data["evaluation_date"] == "2026-09-02" and data["source_commit"] == SOURCE, "date/source")
    c.ok(type(data["fixed_epoch"]) is int and data["fixed_epoch"] == EPOCH, "epoch")
    c.ok(data["scope_literal"] == SCOPE, "scope")
    exact_keys(c, data["evaluator"], {"version", "sha256"}, "evaluator")
    c.ok(data["evaluator"] == {"version": "0.2.0", "sha256": EVALUATOR}, "evaluator value")
    for name, expected in (("model", MODEL), ("theorem_contract", THEOREM), ("proof_contract", PROOF), ("route_a", ROUTE), ("scope_flags", FLAGS)):
        exact_keys(c, data[name], set(expected), name)
        c.ok(data[name] == expected, f"{name} value")
    c.ok(type(data["route_a"]["route_b_invocation_allowed"]) is bool, "Route B bool")
    c.ok(all(type(value) is bool and value is False for value in data["scope_flags"].values()), "scope flags false")
    c.ok(type(data["payload_sha256"]) is str and len(data["payload_sha256"]) == 64, "payload syntax")
    c.ok(data["payload_sha256"] == payload_hash(data), "payload hash")
    # Validate the small evaluation contract before expensive orbit quadratures;
    # this keeps hostile YAML testing fast without weakening the canonical run.
    validate_yaml(c, args.yaml)

    enumeration = data["enumeration"]
    exact_keys(c, enumeration, {"mu_values", "b_values", "ell_values", "action_multipliers", "orbit_cells", "boundary_cells", "closure_counts"}, "enumeration")
    c.ok(enumeration["mu_values"] == [1, 2, 3] and all(type(x) is int for x in enumeration["mu_values"]), "mu grid")
    c.ok(enumeration["b_values"] == [1, 2, 3] and all(type(x) is int for x in enumeration["b_values"]), "b grid")
    c.ok(enumeration["ell_values"] == [0, 1, 2, 3] and all(type(x) is int for x in enumeration["ell_values"]), "ell grid")
    c.ok(enumeration["action_multipliers"] == [1, 2, 3] and all(type(x) is int for x in enumeration["action_multipliers"]), "multiplier grid")
    expected_grid = {(mu, scale_b, ell, k) for mu in (1, 2, 3) for scale_b in (1, 2, 3) for ell in (0, 1, 2, 3) for k in (1, 2, 3)}
    c.ok(type(data["orbit_cells"]) is list and len(data["orbit_cells"]) == enumeration["orbit_cells"] == 108, "row count")

    mp.mp.dps = 90
    seen: set[tuple[int, int, int, int]] = set()
    closure_counts: dict[str, int] = {}
    for index, row in enumerate(data["orbit_cells"]):
        exact_keys(c, row, ROW_KEYS, f"row {index}")
        for key in ("mu", "b", "ell", "action_multiplier", "radicand"):
            c.ok(type(row[key]) is int, f"row {index} {key} type")
        mu, scale_b, ell, k = row["mu"], row["b"], row["ell"], row["action_multiplier"]
        key = (mu, scale_b, ell, k)
        c.ok(key in expected_grid and key not in seen, f"row {index} grid/unique")
        seen.add(key)
        d = ell * ell + 4 * mu * scale_b
        c.ok(row["radicand"] == d, f"row {index} radicand")
        root = math.isqrt(d)
        square = root * root == d
        c.ok(type(row["radicand_square"]) is bool and row["radicand_square"] is square, f"row {index} square")
        c.ok(type(row["sqrt_radicand_decimal"]) is str, f"row {index} root decimal type")
        close(c, mp.mpf(row["sqrt_radicand_decimal"]), mp.sqrt(d), f"row {index} root decimal")

        values = {name: parse_quad(c, row[name], d, f"row {index} {name}") for name in (
            "invariant_I", "radial_action", "circular_energy", "energy", "circular_s",
            "circular_radius_squared", "omega_r", "frequency_ratio", "period_over_2pi",
        )}
        big_b = (Fraction(ell), Fraction(1))
        expected_i = (Fraction(k * ell, 2), Fraction(k, 2))
        expected_j = (Fraction((k - 1) * ell, 2), Fraction(k - 1, 2))
        expected_ec = (-Fraction(ell * ell + 2 * mu * scale_b, 4 * scale_b * scale_b), Fraction(ell, 4 * scale_b * scale_b))
        expected_e = (expected_ec[0] / (k * k), expected_ec[1] / (k * k))
        expected_sc = (Fraction(scale_b) + Fraction(ell * ell, 2 * mu), Fraction(ell, 2 * mu))
        expected_rc2_tmp = qmul(expected_sc, expected_sc, d)
        expected_rc2 = (expected_rc2_tmp[0] - scale_b * scale_b, expected_rc2_tmp[1])
        expected_omega = (-Fraction(ell * (ell * ell + 3 * mu * scale_b), 2 * k**3 * mu * scale_b**3), Fraction(ell * ell + mu * scale_b, 2 * k**3 * mu * scale_b**3))
        expected_beta = (Fraction(1, 2), Fraction(ell, 2 * d))
        expected_tr = (Fraction(k**3 * ell * (ell * ell + 3 * mu * scale_b), 2 * mu * mu), Fraction(k**3 * (ell * ell + mu * scale_b), 2 * mu * mu))
        for name, expected in (("invariant_I", expected_i), ("radial_action", expected_j), ("circular_energy", expected_ec), ("energy", expected_e), ("circular_s", expected_sc), ("circular_radius_squared", expected_rc2), ("omega_r", expected_omega), ("frequency_ratio", expected_beta), ("period_over_2pi", expected_tr)):
            c.ok(values[name] == expected, f"row {index} {name} exact")

        num = {name: qval(value, d) for name, value in values.items()}
        c.ok(num["invariant_I"] > 0 and num["radial_action"] >= 0, f"row {index} action domain")
        c.ok(num["circular_energy"] <= num["energy"] < 0, f"row {index} energy domain")
        c.ok((num["radial_action"] == 0) is (k == 1), f"row {index} circular boundary")
        close(c, num["energy"], -mp.mpf(mu) ** 2 / (2 * num["invariant_I"] ** 2), f"row {index} action inversion")
        close(c, num["omega_r"], mp.mpf(mu) ** 2 / num["invariant_I"] ** 3, f"row {index} radial frequency")
        close(c, num["period_over_2pi"] * num["omega_r"], mp.mpf(1), f"row {index} period reciprocal")
        close(c, num["frequency_ratio"], (1 + mp.mpf(ell) / mp.sqrt(d)) / 2, f"row {index} beta")
        c.ok(mp.mpf("0.5") <= num["frequency_ratio"] < 1, f"row {index} beta range")
        close(c, num["circular_radius_squared"], num["circular_s"] ** 2 - scale_b**2, f"row {index} circular radius")
        if ell > 0:
            close(c, mp.mpf(ell) ** 2, mp.mpf(mu) * (num["circular_s"] - scale_b) ** 2 / num["circular_s"], f"row {index} circular condition")
        else:
            close(c, num["circular_s"], mp.mpf(scale_b), f"row {index} center s")

        x_p = mp.mpf(row["x_peri_decimal"])
        x_a = mp.mpf(row["x_apo_decimal"])
        c.ok(type(row["x_peri_decimal"]) is str and type(row["x_apo_decimal"]) is str, f"row {index} turning types")
        c.ok(x_p >= 2 * scale_b - mp.mpf("1e-48") and x_a >= x_p, f"row {index} turning order")
        e_num = num["energy"]
        def polynomial(x: mp.mpf) -> mp.mpf:
            return 2 * e_num * x * x + (2 * mu - 4 * scale_b * e_num) * x - (4 * mu * scale_b + ell * ell)
        close(c, polynomial(x_p), mp.mpf(0), f"row {index} peri root", mp.mpf("1e-45"))
        close(c, polynomial(x_a), mp.mpf(0), f"row {index} apo root", mp.mpf("1e-45"))

        c.ok(type(row["orbit_class"]) is str and type(row["closure_class"]) is str, f"row {index} class types")
        if k == 1:
            c.ok(row["orbit_class"] == ("center_equilibrium" if ell == 0 else "circular"), f"row {index} circular class")
            c.ok(row["closure_class"] == "closed_degenerate" and row["primitive_radial_cycles"] is None, f"row {index} circular closure")
        elif ell == 0:
            c.ok(row["orbit_class"] == "radial_through_center", f"row {index} radial class")
            c.ok(row["closure_class"] == "closed_radial" and type(row["primitive_radial_cycles"]) is int and row["primitive_radial_cycles"] == 2, f"row {index} radial period")
        elif square:
            beta_q = Fraction(1, 2) * (1 + Fraction(ell, root))
            c.ok(row["closure_class"] == "closed_resonant", f"row {index} resonant class")
            c.ok(type(row["primitive_radial_cycles"]) is int and row["primitive_radial_cycles"] == beta_q.denominator, f"row {index} primitive cycles")
        else:
            c.ok(row["closure_class"] == "nonclosed_irrational" and row["primitive_radial_cycles"] is None, f"row {index} irrational class")

        if k > 1:
            q_num = -2 * e_num
            midpoint = (x_p + x_a) / 2
            halfwidth = (x_a - x_p) / 2
            half_time = mp.quad(lambda theta: (midpoint + halfwidth * mp.cos(theta) - scale_b) / mp.sqrt(q_num), [0, mp.pi])
            close(c, half_time / mp.pi, num["period_over_2pi"], f"row {index} direct period quadrature", mp.mpf("1e-42"))
            if ell > 0:
                half_angle = mp.quad(
                    lambda theta: ell * (midpoint + halfwidth * mp.cos(theta) - scale_b)
                    / ((midpoint + halfwidth * mp.cos(theta)) * (midpoint + halfwidth * mp.cos(theta) - 2 * scale_b) * mp.sqrt(q_num)),
                    [0, mp.pi],
                )
                close(c, half_angle / mp.pi, num["frequency_ratio"], f"row {index} direct apsidal quadrature", mp.mpf("1e-40"))
        closure_counts[row["closure_class"]] = closure_counts.get(row["closure_class"], 0) + 1

    c.ok(seen == expected_grid, "complete grid")
    c.ok(enumeration["closure_counts"] == closure_counts == {"closed_degenerate": 36, "closed_radial": 18, "closed_resonant": 14, "nonclosed_irrational": 40}, "closure counts")
    c.ok(type(data["boundary_cells"]) is list and len(data["boundary_cells"]) == enumeration["boundary_cells"] == 8, "boundary count")
    expected_faces = ["below_circular_minimum", "circular_energy", "bound_open_energy", "escape_threshold", "positive_energy", "zero_angular_momentum", "signed_angular_momentum", "kepler_limit"]
    c.ok([row["face"] for row in data["boundary_cells"]] == expected_faces, "boundary faces")
    for index, row in enumerate(data["boundary_cells"]):
        exact_keys(c, row, {"face", "status", "statement"}, f"boundary {index}")
        c.ok(all(type(value) is str for value in row.values()), f"boundary {index} types")
    exact_tree(c, data["boundary_cells"], BOUNDARIES, "canonical boundaries")
    c.ok(type(data["references"]) is list and len(data["references"]) == 4, "reference count")
    identifiers = []
    for index, ref in enumerate(data["references"]):
        exact_keys(c, ref, {"id", "authors", "title", "venue", "identifier", "url", "ownership"}, f"reference {index}")
        c.ok(all(type(value) is str and value for value in ref.values()), f"reference {index} values")
        identifiers.append(ref["identifier"])
    c.ok(identifiers == ["1959AnAp...22..126H", "1959AnAp...22..491H", "10.1063/5.0056957", "10.1093/mnras/stab3020"], "reference identifiers")
    exact_tree(c, data["references"], REFERENCES, "canonical references")
    exact_tree(c, data["nonclaims"], NONCLAIMS, "canonical nonclaims")
    print(f"C295 independent checker: PASS ({c.n} assertions; strict duplicate-rejecting JSON/YAML, exact algebraic reconstruction, direct quadratures)")


if __name__ == "__main__":
    main()
