#!/usr/bin/env python3
"""Producer-independent exact and semantic checker for HCS-C352."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c352_jackiw_rebbi_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C352/2026-09-03.yaml"
SOURCE = "327fc1172cebcdeb17adfd2d8ad12636fbb94f52"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
YAML_RAW = "232e3fce6d9acd33d2700f461be42d3ca4f2491e76df298ecbcbfb0f3a56c827"
YAML_SEMANTIC = "64d65968f25f0a7d94a681de29c7e3ffd5e2291013921e9ca2e52266b2c08d4b"
N_MAX = 24
K_PANEL = tuple(map(Fraction, ("1/3", "1/2", "1", "3/2", "2", "5/2")))
FLAGS = {
    "claims_target_arithmetic_local_data": False, "claims_target_euler_factors": False,
    "claims_root_number": False, "claims_automorphy": False,
    "claims_target_divisor_or_counting_law": False,
    "claims_target_functional_equation": False, "claims_target_zero_match": False,
    "claims_hilbert_polya_operator": False, "invokes_route_b": False,
}


def duplicate_pairs(items):
    result = {}
    for key, value in items:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def strict_json(path):
    value = json.loads(path.read_text(), object_pairs_hook=duplicate_pairs,
        parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    if type(value) is not dict:
        raise TypeError("JSON root")
    return value


class StrictLoader(yaml.SafeLoader):
    pass


StrictLoader.yaml_implicit_resolvers = {
    key: [(tag, rx) for tag, rx in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def strict_mapping(loader, node, deep=False):
    answer = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in answer:
            raise ValueError("duplicate/non-string YAML key")
        answer[key] = loader.construct_object(value_node, deep=deep)
    return answer


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, strict_mapping)


def strict_yaml(path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors forbidden")
    value = yaml.load(raw, Loader=StrictLoader)
    if type(value) is not dict:
        raise TypeError("YAML root")
    return value


def need(condition, label):
    if not condition:
        raise AssertionError(label)


def exact_keys(value, keys, label):
    need(type(value) is dict and set(value) == set(keys), f"{label} keys")


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def fstr(value):
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def cmul(z, w):
    return z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0]


def independent_transmission(m, k):
    value = Fraction(1), Fraction(0)
    for r in range(1, m + 1):
        value = cmul(value, ((k * k - r * r) / (k * k + r * r),
                            2 * k * r / (k * k + r * r)))
    return value


def expected_spectra():
    rows = []
    for n in range(N_MAX + 1):
        pairs = [{"j": j, "energy_squared": j * (2 * n - j),
                  "positive_energy": f"sqrt({j * (2 * n - j)})",
                  "negative_energy": f"-sqrt({j * (2 * n - j)})"}
                 for j in range(1, n)]
        rows.append({"n": n,
            "upper_channel": {"constant": n * n, "sech_squared_coefficient": -n * (n + 1)},
            "lower_channel": {"constant": n * n, "sech_squared_coefficient": -n * (n - 1)},
            "upper_scalar_energy_squares": [j * (2 * n - j) for j in range(n)],
            "lower_scalar_energy_squares": [j * (2 * n - j) for j in range(1, n)],
            "dirac_nonzero_bound_pairs": pairs,
            "zero_mode_multiplicity": int(n >= 1),
            "zero_mode_component": "upper" if n else "none",
            "zero_mode_profile": f"sech(x)^{n}" if n else "none",
            "essential_spectrum": "R" if n == 0 else f"(-inf,-{n}] union [{n},inf)",
            "threshold_energy_squares": [] if n == 0 else [n * n],
            "threshold_resonances_non_L2": bool(n), "threshold_eigenvalues": False,
            "free_boundary": n == 0})
    return rows


def expected_factors():
    rows = []
    for n in range(1, N_MAX + 1):
        norm = Fraction(4 ** n * math.factorial(n) * math.factorial(n - 1), math.factorial(2 * n))
        rows.append({"n": n, "AstarA_constant": n * n,
            "AstarA_sech_squared_coefficient": -n * (n + 1),
            "AAstar_constant": n * n,
            "AAstar_sech_squared_coefficient": -n * (n - 1),
            "shape_invariance_shift": 2 * n - 1,
            "zero_mode_norm_squared": fstr(norm),
            "zero_mode_normalization_squared": fstr(1 / norm)})
    return rows


def expected_scattering():
    rows = []
    for m in range(N_MAX + 1):
        for k in K_PANEL:
            real, imag = independent_transmission(m, k)
            rows.append({"scalar_order": m, "momentum": fstr(k),
                "transmission_real": fstr(real), "transmission_imag": fstr(imag),
                "transmission_modulus_squared": fstr(real * real + imag * imag),
                "reflection_real": "0", "reflection_imag": "0"})
    return rows


def digest(rows):
    return hashlib.sha256(canonical(rows)).hexdigest()


def check_yaml(value):
    keys = ["schema", "candidate_id", "title", "evaluation_date", "source_commit",
        "fixed_epoch", "scope_literal", "evaluator_authority", "evaluator_version",
        "evaluator_authority_sha256", "obstruction_id", "candidate_definition", "family",
        "phase_space", "dynamics", "parameters", "parameter_provenance", "arithmetic_origin",
        "clock", "normalization", "determinant_convention", "orbit_cutoff", "precision",
        "training_data", "forbidden_data", "artifact_paths", "a0", "a1", "a2", "a3", "a4",
        "tuple", "overall_verdict", "route_b_invocation_allowed", "route_b_lock_reason",
        "scope_flags", "theorem_status", "finite_evidence_role", "source_owner_tokens"]
    exact_keys(value, keys, "YAML top")
    need((value["schema"], value["candidate_id"], value["obstruction_id"],
          value["evaluation_date"], value["source_commit"], value["fixed_epoch"],
          value["scope_literal"]) == ("route-a-evaluation-v0.2.0", "HCS-C352", "HEN-O336",
          "2026-09-03", SOURCE, 1788393600, SCOPE), "YAML identity")
    need(value["evaluator_authority"] == "flow_systems/skills/route-a-evaluator.md", "YAML authority")
    need(value["evaluator_version"] == "0.2.0" and value["evaluator_authority_sha256"] == EVALUATOR, "YAML evaluator")
    need(value["artifact_paths"] == ["results/c352_jackiw_rebbi_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"], "YAML artifacts")
    verdicts = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"]
    statuses = ["PROVED", "PROVED", "STOP_SCOPED", "STOP_SCOPED", "PROVED"]
    for index, name in enumerate(("a0", "a1", "a2", "a3", "a4")):
        exact_keys(value[name], ["verdict", "evidence_status", "strongest_evidence", "strongest_failure"], f"YAML {name}")
        need(value[name]["verdict"] == verdicts[index] and value[name]["evidence_status"] == statuses[index], f"YAML {name} outcome")
    need(value["tuple"] == verdicts and value["overall_verdict"] == "ROUTE_A_REJECTED", "YAML outcome")
    need(value["route_b_invocation_allowed"] is False, "YAML Route B")
    need(value["scope_flags"] == FLAGS, "YAML scope flags")
    need(value["theorem_status"] == "PROVABLE_AS_STATED", "YAML theorem")
    need(value["source_owner_tokens"] == ["10.1103/PhysRevD.13.3398", "10.1103/PhysRevD.89.025002"], "YAML sources")


def main():
    if sys.flags.optimize:
        raise RuntimeError("C352 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_YAML)
    args = parser.parse_args()
    data = strict_json(args.evidence)
    raw = args.evaluation.read_bytes()
    evaluation = strict_yaml(args.evaluation)
    need(hashlib.sha256(raw).hexdigest() == YAML_RAW, "YAML raw hash")
    need(hashlib.sha256(canonical(evaluation)).hexdigest() == YAML_SEMANTIC, "YAML semantic hash")
    check_yaml(evaluation)
    top = ["schema", "candidate_id", "obstruction_id", "evaluation_date", "source_commit",
        "fixed_epoch", "scope_literal", "evaluator", "route_a_yaml", "model", "theorem_contract",
        "finite_grid", "collision_boundary", "nonclaims", "references", "route_a", "scope_flags",
        "spectrum_rows", "factorization_rows", "scattering_rows", "enumeration", "payload_sha256"]
    exact_keys(data, top, "evidence top")
    body = dict(data)
    claimed = body.pop("payload_sha256")
    need(claimed == hashlib.sha256(canonical(body)).hexdigest(), "payload hash")
    need((data["schema"], data["candidate_id"], data["obstruction_id"],
          data["evaluation_date"], data["source_commit"], data["fixed_epoch"],
          data["scope_literal"]) == ("hcs-c352-jackiw-rebbi-evidence-v1", "HCS-C352",
          "HEN-O336", "2026-09-03", SOURCE, 1788393600, SCOPE), "identity")
    need(data["evaluator"] == {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR}, "evaluator")
    need(data["route_a_yaml"] == {"relative_path": "evaluations/route_a/HCS-C352/2026-09-03.yaml", "raw_sha256": YAML_RAW, "semantic_sha256": YAML_SEMANTIC}, "YAML binding")
    need(data["model"] == {"A_n": "d/dx+n*tanh(x)", "A_n_star": "-d/dx+n*tanh(x)",
        "H_n": "[[0,A_n_star],[A_n,0]]", "domain": "H1(R;C2)",
        "integer_regime": "n>=1", "free_boundary": "n=0"}, "model")
    need(data["theorem_contract"] == {
        "self_adjointness": "H_n is self-adjoint on H1 and generates a unitary group",
        "factorization": "H_n^2=diag(A_n_star A_n,A_n A_n_star) with shape invariance",
        "essential_spectrum": "(-inf,-n] union [n,inf), purely absolutely continuous off the finite point spectrum",
        "point_spectrum": "one chiral zero mode and simple pairs +/-sqrt(j(2n-j)), j=1,...,n-1",
        "thresholds": "+/-n are resonant but not L2 eigenvalues",
        "scattering": "both scalar partners and the Dirac kink are reflectionless at integer n"}, "theorem contract")
    need(data["collision_boundary"] == {
        "C224": "finite-dimensional Landau-Zener crossing, not a spatial kink Dirac operator",
        "C340": "periodic scalar Schrodinger bands, not whole-line chiral Dirac scattering",
        "C345": "nonlinear Toda lattice scattering, not supersymmetric one-particle Dirac factorization"}, "collision boundary")
    need(data["nonclaims"] == [
        "no interacting quantum field theory, fermion-number renormalization, or many-body theorem",
        "no noninteger-height reflectionless claim and no arbitrary kink-profile classification",
        "no spectral determinant, zeta regularization, or target-zero identification",
        "no target arithmetic local data, Euler factors, root number, automorphy, target functional equation, Hilbert-Polya operator, or Route B"], "nonclaims")
    need(data["references"] == [
        {"authors": "Roman Jackiw; Claudio Rebbi", "year": 1976,
         "identifier": "DOI:10.1103/PhysRevD.13.3398",
         "url": "https://doi.org/10.1103/PhysRevD.13.3398",
         "role": "primary zero-mode and fractional-fermion-number lineage"},
        {"authors": "Farid Charmchi; Siamak S. Gousheh", "year": 2014,
         "identifier": "DOI:10.1103/PhysRevD.89.025002",
         "url": "https://arxiv.org/abs/1402.2444",
         "role": "exact 1+1 dimensional spectral and scattering analysis"}], "references")
    need(data["route_a"] == {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}, "Route A")
    need(data["scope_flags"] == FLAGS, "scope flags")
    spectra, factors, scattering = expected_spectra(), expected_factors(), expected_scattering()
    need(data["spectrum_rows"] == spectra, "spectrum ledger")
    need(data["factorization_rows"] == factors, "factorization ledger")
    need(data["scattering_rows"] == scattering, "scattering ledger")
    need(data["finite_grid"] == {"n_min": 0, "n_max": 24, "spectrum_rows": 25,
        "factorization_rows": 24, "momentum_values": 6, "scattering_rows": 150,
        "nonzero_dirac_bound_pairs": 276}, "finite grid")
    need(data["enumeration"] == {"all_arithmetic_exact": True, "floating_point_used": False,
        "finite_evidence_proves_operator_theorem": False,
        "spectrum_sha256": digest(spectra), "factorization_sha256": digest(factors),
        "scattering_sha256": digest(scattering)}, "enumeration")
    need(all(row["transmission_modulus_squared"] == "1" and row["reflection_real"] == "0"
             for row in scattering), "reflectionless samples")
    print(f"C352 independent Jackiw-Rebbi checker: PASS {len(spectra)+len(factors)+len(scattering)} exact rows")


if __name__ == "__main__":
    main()
