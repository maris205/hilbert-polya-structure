#!/usr/bin/env python3
"""Canonical exact evidence producer for HCS-C352."""
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
DEFAULT_OUTPUT = ROOT / "results/c352_jackiw_rebbi_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C352/2026-09-03.yaml"
SOURCE = "327fc1172cebcdeb17adfd2d8ad12636fbb94f52"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
YAML_RAW = "232e3fce6d9acd33d2700f461be42d3ca4f2491e76df298ecbcbfb0f3a56c827"
YAML_SEMANTIC = "64d65968f25f0a7d94a681de29c7e3ffd5e2291013921e9ca2e52266b2c08d4b"
N_MAX = 24
K_PANEL = tuple(map(Fraction, ("1/3", "1/2", "1", "3/2", "2", "5/2")))


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
            raise ValueError("merge key")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in answer:
            raise ValueError("duplicate/non-string YAML key")
        answer[key] = loader.construct_object(value_node, deep=deep)
    return answer


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, strict_mapping)


def strict_yaml(path: Path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("anchors forbidden")
    value = yaml.load(raw, Loader=StrictLoader)
    if type(value) is not dict:
        raise TypeError("YAML root")
    return value


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def fstr(value):
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def cmul(left, right):
    a, b = left
    c, d = right
    return a * c - b * d, a * d + b * c


def transmission(m, k):
    value = Fraction(1), Fraction(0)
    for r in range(1, m + 1):
        denominator = k * k + r * r
        factor = (k * k - r * r) / denominator, 2 * k * r / denominator
        value = cmul(value, factor)
    return value


def spectrum_rows():
    rows = []
    for n in range(N_MAX + 1):
        positive = [{"j": j, "energy_squared": j * (2 * n - j),
                     "positive_energy": f"sqrt({j * (2 * n - j)})",
                     "negative_energy": f"-sqrt({j * (2 * n - j)})"}
                    for j in range(1, n)]
        rows.append({
            "n": n,
            "upper_channel": {"constant": n * n, "sech_squared_coefficient": -n * (n + 1)},
            "lower_channel": {"constant": n * n, "sech_squared_coefficient": -n * (n - 1)},
            "upper_scalar_energy_squares": [j * (2 * n - j) for j in range(n)],
            "lower_scalar_energy_squares": [j * (2 * n - j) for j in range(1, n)],
            "dirac_nonzero_bound_pairs": positive,
            "zero_mode_multiplicity": 1 if n >= 1 else 0,
            "zero_mode_component": "upper" if n >= 1 else "none",
            "zero_mode_profile": f"sech(x)^{n}" if n >= 1 else "none",
            "essential_spectrum": "R" if n == 0 else f"(-inf,-{n}] union [{n},inf)",
            "threshold_energy_squares": [] if n == 0 else [n * n],
            "threshold_resonances_non_L2": n >= 1,
            "threshold_eigenvalues": False,
            "free_boundary": n == 0,
        })
    return rows


def factorization_rows():
    return [{"n": n,
             "AstarA_constant": n * n,
             "AstarA_sech_squared_coefficient": -n * (n + 1),
             "AAstar_constant": n * n,
             "AAstar_sech_squared_coefficient": -n * (n - 1),
             "shape_invariance_shift": 2 * n - 1,
             "zero_mode_norm_squared": fstr(Fraction(4 ** n * math.factorial(n) * math.factorial(n - 1), math.factorial(2 * n))),
             "zero_mode_normalization_squared": fstr(Fraction(math.factorial(2 * n), 4 ** n * math.factorial(n) * math.factorial(n - 1)))}
            for n in range(1, N_MAX + 1)]


def scattering_rows():
    rows = []
    for m in range(N_MAX + 1):
        for k in K_PANEL:
            real, imag = transmission(m, k)
            rows.append({"scalar_order": m, "momentum": fstr(k),
                         "transmission_real": fstr(real), "transmission_imag": fstr(imag),
                         "transmission_modulus_squared": fstr(real * real + imag * imag),
                         "reflection_real": "0", "reflection_imag": "0"})
    return rows


def digest(rows):
    return hashlib.sha256(canonical(rows)).hexdigest()


def build(evaluation: Path):
    raw = evaluation.read_bytes()
    semantic = strict_yaml(evaluation)
    if hashlib.sha256(raw).hexdigest() != YAML_RAW:
        raise AssertionError("evaluation raw hash")
    if hashlib.sha256(canonical(semantic)).hexdigest() != YAML_SEMANTIC:
        raise AssertionError("evaluation semantic hash")
    spectra = spectrum_rows()
    factors = factorization_rows()
    scattering = scattering_rows()
    body = {
        "schema": "hcs-c352-jackiw-rebbi-evidence-v1",
        "candidate_id": "HCS-C352", "obstruction_id": "HEN-O336",
        "evaluation_date": "2026-09-03", "source_commit": SOURCE,
        "fixed_epoch": 1788393600, "scope_literal": SCOPE,
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md",
                      "version": "0.2.0", "sha256": EVALUATOR},
        "route_a_yaml": {"relative_path": "evaluations/route_a/HCS-C352/2026-09-03.yaml",
                         "raw_sha256": YAML_RAW, "semantic_sha256": YAML_SEMANTIC},
        "model": {"A_n": "d/dx+n*tanh(x)", "A_n_star": "-d/dx+n*tanh(x)",
                  "H_n": "[[0,A_n_star],[A_n,0]]", "domain": "H1(R;C2)",
                  "integer_regime": "n>=1", "free_boundary": "n=0"},
        "theorem_contract": {
            "self_adjointness": "H_n is self-adjoint on H1 and generates a unitary group",
            "factorization": "H_n^2=diag(A_n_star A_n,A_n A_n_star) with shape invariance",
            "essential_spectrum": "(-inf,-n] union [n,inf), purely absolutely continuous off the finite point spectrum",
            "point_spectrum": "one chiral zero mode and simple pairs +/-sqrt(j(2n-j)), j=1,...,n-1",
            "thresholds": "+/-n are resonant but not L2 eigenvalues",
            "scattering": "both scalar partners and the Dirac kink are reflectionless at integer n"},
        "finite_grid": {"n_min": 0, "n_max": N_MAX, "spectrum_rows": len(spectra),
                        "factorization_rows": len(factors), "momentum_values": len(K_PANEL),
                        "scattering_rows": len(scattering),
                        "nonzero_dirac_bound_pairs": sum(max(n - 1, 0) for n in range(N_MAX + 1))},
        "collision_boundary": {
            "C224": "finite-dimensional Landau-Zener crossing, not a spatial kink Dirac operator",
            "C340": "periodic scalar Schrodinger bands, not whole-line chiral Dirac scattering",
            "C345": "nonlinear Toda lattice scattering, not supersymmetric one-particle Dirac factorization"},
        "nonclaims": [
            "no interacting quantum field theory, fermion-number renormalization, or many-body theorem",
            "no noninteger-height reflectionless claim and no arbitrary kink-profile classification",
            "no spectral determinant, zeta regularization, or target-zero identification",
            "no target arithmetic local data, Euler factors, root number, automorphy, target functional equation, Hilbert-Polya operator, or Route B"],
        "references": [
            {"authors": "Roman Jackiw; Claudio Rebbi", "year": 1976,
             "identifier": "DOI:10.1103/PhysRevD.13.3398",
             "url": "https://doi.org/10.1103/PhysRevD.13.3398",
             "role": "primary zero-mode and fractional-fermion-number lineage"},
            {"authors": "Farid Charmchi; Siamak S. Gousheh", "year": 2014,
             "identifier": "DOI:10.1103/PhysRevD.89.025002",
             "url": "https://arxiv.org/abs/1402.2444",
             "role": "exact 1+1 dimensional spectral and scattering analysis"}],
        "route_a": {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
                    "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": {
            "claims_target_arithmetic_local_data": False, "claims_target_euler_factors": False,
            "claims_root_number": False, "claims_automorphy": False,
            "claims_target_divisor_or_counting_law": False,
            "claims_target_functional_equation": False, "claims_target_zero_match": False,
            "claims_hilbert_polya_operator": False, "invokes_route_b": False},
        "spectrum_rows": spectra, "factorization_rows": factors,
        "scattering_rows": scattering,
        "enumeration": {"all_arithmetic_exact": True, "floating_point_used": False,
                        "finite_evidence_proves_operator_theorem": False,
                        "spectrum_sha256": digest(spectra),
                        "factorization_sha256": digest(factors),
                        "scattering_sha256": digest(scattering)},
    }
    body["payload_sha256"] = hashlib.sha256(canonical(body)).hexdigest()
    return body


def main():
    if sys.flags.optimize:
        raise RuntimeError("C352 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_YAML)
    args = parser.parse_args()
    data = build(args.evaluation)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C352_PRODUCER_PASS {len(data['spectrum_rows'])} spectra "
          f"{len(data['scattering_rows'])} scattering rows {data['payload_sha256']}")


if __name__ == "__main__":
    main()
