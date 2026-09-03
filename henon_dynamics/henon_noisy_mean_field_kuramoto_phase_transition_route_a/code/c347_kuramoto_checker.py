#!/usr/bin/env python3
"""Producer-independent exact and semantic checker for HCS-C347."""
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
DEFAULT = ROOT / "results/c347_kuramoto_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C347/2026-09-03.yaml"
SOURCE = "1af63b945e19b5f94ac1cb76f93af5ac66d3d562"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
YAML_RAW = "032d92adfe7e5ceff5727dce250f06ddf5e24516c6f616982327a621b2503f5b"
YAML_SEMANTIC = "62ecfa44268ab9d87c05956f4a9e8639beb065a17aab7d2f0a7dee35c647babf"
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
    result = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in result:
            raise ValueError("duplicate/non-string YAML key")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, strict_mapping)


def strict_yaml(path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors/aliases forbidden")
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


def term0(x, m):
    return x ** (2 * m) / (4 ** m * math.factorial(m) ** 2)


def term1(x, m):
    return x ** (2 * m + 1) / (2 * 4 ** m * math.factorial(m) * math.factorial(m + 1))


def independent_bounds(x, stop=20):
    low0 = sum((term0(x, j) for j in range(stop + 1)), Fraction())
    low1 = sum((term1(x, j) for j in range(stop + 1)), Fraction())
    q0 = x * x / (4 * (stop + 2) ** 2)
    q1 = x * x / (4 * (stop + 2) * (stop + 3))
    high0 = low0 + term0(x, stop + 1) / (1 - q0)
    high1 = low1 + term1(x, stop + 1) / (1 - q1)
    return low0, high0, low1, high1


def expected_coefficients():
    result = []
    for j in range(17):
        left = Fraction(1, 4 ** j * math.factorial(j) ** 2)
        right = Fraction(1, 2 * 4 ** j * math.factorial(j) * math.factorial(j + 1))
        result.append({"m": j, "i0_coefficient": fstr(left),
            "i1_over_kappa_coefficient": fstr(right),
            "coefficient_ratio": fstr(right / left)})
    return result


def expected_quotient():
    denominator = [Fraction(1, 4 ** j * math.factorial(j) ** 2) for j in range(9)]
    numerator = [Fraction(1, 2 * 4 ** j * math.factorial(j) * math.factorial(j + 1))
                 for j in range(9)]
    coefficients = []
    for n in range(9):
        coefficients.append(numerator[n] - sum(
            denominator[j] * coefficients[n - j] for j in range(1, n + 1)))
    return [{"power_of_kappa_squared": j, "coefficient": fstr(value)}
            for j, value in enumerate(coefficients)]


def expected_tails():
    result = []
    for x in map(Fraction, ("1/4", "1/2", "1", "3/2", "2", "3", "4")):
        low0, high0, low1, high1 = independent_bounds(x)
        lowr, highr = low1 / high0, high1 / low0
        result.append({"kappa": fstr(x), "cutoff": 20,
            "i0_lower": fstr(low0), "i0_upper": fstr(high0),
            "i1_lower": fstr(low1), "i1_upper": fstr(high1),
            "ratio_lower": fstr(lowr), "ratio_upper": fstr(highr),
            "strict_interval": lowr < highr})
    return result


def expected_roots():
    result = []
    mesh = Fraction(1, 64)
    for a in map(Fraction, ("5/2", "3", "4", "6")):
        positive = negative = None
        for index in range(1, int(a / mesh) + 1):
            x = index * mesh
            low0, high0, low1, high1 = independent_bounds(x)
            lower, upper = low1 / high0, high1 / low0
            if a * lower - x > 0:
                positive = (x, a * lower - x)
            if negative is None and a * upper - x < 0:
                negative = (x, a * upper - x)
        need(positive is not None and negative is not None and positive[0] < negative[0], "root bracket")
        result.append({"K_over_D": fstr(a), "mesh_denominator": 64,
            "kappa_left": fstr(positive[0]), "certified_f_left_lower": fstr(positive[1]),
            "kappa_right": fstr(negative[0]), "certified_f_right_upper": fstr(negative[1]),
            "root_count_analytic": 1})
    return result


def expected_fourier():
    result = []
    for d in map(Fraction, ("1/2", "1", "2")):
        for a in map(Fraction, ("0", "1", "2", "5/2", "3", "4")):
            k = a * d
            for n in range(9):
                eigen = Fraction() if n == 0 else (k / 2 - d if n == 1 else -d * n * n)
                result.append({"D": fstr(d), "K": fstr(k), "mode": n,
                    "real_multiplicity": 1 if n == 0 else 2,
                    "linearized_eigenvalue": fstr(eigen)})
    return result


def digest(rows):
    return hashlib.sha256(canonical(rows)).hexdigest()


def check_yaml(value):
    top = ["schema", "candidate_id", "title", "evaluation_date", "source_commit",
        "fixed_epoch", "scope_literal", "evaluator_authority", "evaluator_version",
        "evaluator_authority_sha256", "obstruction_id", "candidate_definition", "family",
        "phase_space", "dynamics", "parameters", "parameter_provenance", "arithmetic_origin",
        "clock", "normalization", "determinant_convention", "orbit_cutoff", "precision",
        "training_data", "forbidden_data", "artifact_paths", "a0", "a1", "a2", "a3", "a4",
        "tuple", "overall_verdict", "route_b_invocation_allowed", "route_b_lock_reason",
        "scope_flags", "theorem_status", "finite_evidence_role", "source_owner_tokens"]
    exact_keys(value, top, "YAML top")
    need((value["schema"], value["candidate_id"], value["obstruction_id"],
          value["evaluation_date"], value["source_commit"], value["fixed_epoch"],
          value["scope_literal"]) == ("route-a-evaluation-v0.2.0", "HCS-C347", "HEN-O331",
          "2026-09-03", SOURCE, 1788393600, SCOPE), "YAML identity")
    need(value["evaluator_authority"] == "flow_systems/skills/route-a-evaluator.md", "YAML authority")
    need(value["evaluator_version"] == "0.2.0" and value["evaluator_authority_sha256"] == EVALUATOR, "YAML evaluator")
    need(value["artifact_paths"] == ["results/c347_kuramoto_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"], "YAML artifacts")
    verdicts = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
    for i, name in enumerate(("a0", "a1", "a2", "a3", "a4")):
        exact_keys(value[name], ["verdict", "evidence_status", "strongest_evidence", "strongest_failure"], f"YAML {name}")
        need(value[name]["verdict"] == verdicts[i], f"YAML {name} verdict")
        need(value[name]["evidence_status"] == ("PROVED" if i < 2 else "STOP_SCOPED"), f"YAML {name} status")
    need(value["tuple"] == verdicts and value["overall_verdict"] == "ROUTE_A_REJECTED", "YAML outcome")
    need(value["route_b_invocation_allowed"] is False, "YAML Route B")
    need(value["route_b_lock_reason"] == "no arithmetic source, prime clock, target Euler factor, target divisor, or natural target-zero quantization exists", "YAML route lock")
    need(value["scope_flags"] == FLAGS, "YAML flags")
    need(value["theorem_status"] == "PROVABLE_AS_STATED", "YAML theorem")
    need(value["finite_evidence_role"] == "Bessel series, certified root bracket, Fourier, parser, and implementation receipt only; analytic arguments prove the continuum stationary theorem", "YAML evidence role")
    need(value["source_owner_tokens"] == ["10.1143/PTP.79.39", "10.1007/s10955-009-9908-9"], "YAML sources")


def main():
    if sys.flags.optimize:
        raise RuntimeError("C347 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_YAML)
    args = parser.parse_args()
    data = strict_json(args.evidence)
    raw_yaml = args.evaluation.read_bytes()
    evaluation = strict_yaml(args.evaluation)
    need(hashlib.sha256(raw_yaml).hexdigest() == YAML_RAW, "YAML raw digest")
    need(hashlib.sha256(canonical(evaluation)).hexdigest() == YAML_SEMANTIC, "YAML semantic digest")
    check_yaml(evaluation)
    top = ["schema", "candidate_id", "obstruction_id", "evaluation_date", "source_commit",
        "fixed_epoch", "scope_literal", "evaluator", "route_a_yaml", "model", "theorem_contract",
        "finite_grid", "collision_boundary", "nonclaims", "references", "route_a", "scope_flags",
        "bessel_coefficient_rows", "formal_quotient_rows", "tail_bracket_rows",
        "self_consistency_root_rows", "fourier_rows", "critical_expansion", "enumeration",
        "payload_sha256"]
    exact_keys(data, top, "top")
    body = dict(data)
    claimed = body.pop("payload_sha256")
    need(type(claimed) is str and claimed == hashlib.sha256(canonical(body)).hexdigest(), "payload hash")
    need(data["schema"] == "hcs-c347-kuramoto-evidence-v1", "schema")
    need((data["candidate_id"], data["obstruction_id"], data["evaluation_date"], data["source_commit"], data["fixed_epoch"], data["scope_literal"]) ==
         ("HCS-C347", "HEN-O331", "2026-09-03", SOURCE, 1788393600, SCOPE), "identity")
    need(data["evaluator"] == {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR}, "evaluator")
    need(data["route_a_yaml"] == {"relative_path": "evaluations/route_a/HCS-C347/2026-09-03.yaml", "raw_sha256": YAML_RAW, "semantic_sha256": YAML_SEMANTIC}, "YAML binding")
    need(data["model"] == {"phase_space": "nonnegative unit-mass circle densities; classical theorem starts from C^{2+gamma}", "parameters": "D>0 and K>=0", "order_parameter": "z[p]=integral exp(i theta)p(theta)dtheta=r exp(i psi)", "pde": "p_t=D p_thetatheta-d_theta(K r sin(psi-theta)p)", "uniform_density": "1/(2 pi)", "stationary_family": "exp(kappa cos(theta-psi))/(2 pi I0(kappa))"}, "model")
    need(data["theorem_contract"] == {"flow": "unique global classical mass-preserving positive probability flow", "free_energy": "F=D integral p log p-(K/2)|z[p]|^2 with exact dissipation", "stationary": "all positive C2 stationary densities are uniform or the self-consistent von Mises circle", "transition": "uniform only for K<=2D; one nonzero concentration modulo phase for K>2D", "linearization": "mass mode zero, first harmonic K/2-D, higher harmonics -D n^2", "critical": "kappa^2=4 delta+(2/3)delta^2+O(delta^3), r^2=delta-(5/6)delta^2+O(delta^3)"}, "contract")
    need(data["collision_boundary"] == {"C322": "linear Kac collision spectrum, not a nonlinear nonlocal parabolic phase transition", "C339": "finite-dimensional Hamiltonian navigation, not a dissipative probability PDE", "C340": "periodic Schrodinger finite-gap operator, not Kuramoto mean-field synchronization"}, "collision")
    need(data["nonclaims"] == ["no general-initial-data convergence rate or global convergence theorem", "no Hopf bifurcation, time-periodic branch, disorder, delay, inertia, or finite-N theorem", "no D=0 atomic-state extension", "no target arithmetic local data, Euler factors, root number, automorphy, target zero match, Hilbert-Polya operator, or Route B"], "nonclaims")
    need(data["references"] == [{"authors": "Hidetsugu Sakaguchi", "year": 1988, "identifier": "DOI:10.1143/PTP.79.39", "url": "https://academic.oup.com/ptp/article/79/1/39/1855689", "role": "primary noisy globally coupled oscillator source"}, {"authors": "Lorenzo Bertini; Giambattista Giacomin; Khashayar Pakdaman", "year": 2010, "identifier": "DOI:10.1007/s10955-009-9908-9", "url": "https://arxiv.org/abs/0911.1499", "role": "authoritative reversible mean-field rotator dynamics and free-energy source"}], "references")
    need(data["route_a"] == {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}, "Route A")
    need(data["scope_flags"] == FLAGS, "flags")
    coefficients, quotient = expected_coefficients(), expected_quotient()
    tails, roots, fourier = expected_tails(), expected_roots(), expected_fourier()
    need(data["bessel_coefficient_rows"] == coefficients, "coefficient ledger")
    need(data["formal_quotient_rows"] == quotient, "quotient ledger")
    need(data["tail_bracket_rows"] == tails, "tail ledger")
    need(data["self_consistency_root_rows"] == roots, "root ledger")
    need(data["fourier_rows"] == fourier, "Fourier ledger")
    need(data["finite_grid"] == {"bessel_coefficient_rows": 17, "formal_quotient_rows": 9,
        "tail_bracket_rows": 7, "self_consistency_root_rows": 4, "fourier_rows": 162,
        "bessel_cutoff": 20, "root_mesh_denominator": 64}, "grid")
    need(data["critical_expansion"] == {"delta": "K/D-2", "kappa_squared": ["4", "2/3"], "r_squared": ["1", "-5/6"], "analytic_remainder_order": 3}, "critical")
    need(data["enumeration"] == {"all_arithmetic_exact": True, "floating_point_used": False,
        "finite_evidence_proves_continuum_theorem": False,
        "bessel_coefficient_sha256": digest(coefficients),
        "formal_quotient_sha256": digest(quotient), "tail_bracket_sha256": digest(tails),
        "root_bracket_sha256": digest(roots), "fourier_sha256": digest(fourier)}, "enumeration")
    checks = 17 + 9 + 7 + 4 + 162
    print(f"C347 independent Kuramoto checker: PASS {checks} exact ledger rows")


if __name__ == "__main__":
    main()
