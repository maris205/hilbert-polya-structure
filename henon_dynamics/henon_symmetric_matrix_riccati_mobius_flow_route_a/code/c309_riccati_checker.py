#!/usr/bin/env python3
"""Producer-independent structural and numerical checker for HCS-C309."""
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
DEFAULT = ROOT / "results/c309_riccati_evidence.json"
DEFAULT_EVALUATION = ROOT / "evaluations/route_a/HCS-C309/2026-09-03.yaml"
SOURCE = "b3e2f3f7207b85d7be942ff72b1f49e754615c76"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
SPECS = [
    ("scalar-minus-two", ["-2"]), ("scalar-minus-one", ["-1"]), ("scalar-zero", ["0"]),
    ("scalar-one", ["1"]), ("scalar-three", ["3"]), ("two-global", ["-1", "2"]),
    ("two-heteroclinic", ["-1/2", "1/3"]), ("two-forward-pole", ["-3", "1/2"]),
    ("two-both-poles", ["-4", "5"]), ("three-mixed-global", ["-1", "0", "7/3"]),
    ("three-two-forward-poles", ["-5", "-2", "4"]), ("three-repeated", ["-1/3", "-1/3", "2"]),
    ("four-global-boundary", ["-1", "-1", "1", "3"]), ("four-interior", ["-3/4", "-1/4", "1/4", "3/4"]),
    ("four-pole-tie", ["-2", "-2", "0", "2"]), ("five-spectrum", ["-1", "-2/3", "0", "3/2", "4"]),
]


def duplicate(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def nonfinite(value):
    raise ValueError(f"nonfinite JSON constant: {value}")


def strict(path):
    value = json.loads(path.read_text(), object_pairs_hook=duplicate, parse_constant=nonfinite)
    if type(value) is not dict:
        raise TypeError("JSON root must be object")
    return value


class UniqueSafeLoader(yaml.SafeLoader):
    pass


UniqueSafeLoader.yaml_implicit_resolvers = {key: [(tag, pattern) for tag, pattern in values if tag != "tag:yaml.org,2002:timestamp"] for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()}


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in result:
            raise ValueError("duplicate or non-string YAML key")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueSafeLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def strict_yaml(path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors and aliases are forbidden")
    value = yaml.load(raw, Loader=UniqueSafeLoader)
    if type(value) is not dict:
        raise TypeError("YAML root must be mapping")
    return value


def digest(data):
    body = dict(data); body.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def close(text, expected, tolerance=2e-68):
    if type(text) is not str or not math.isfinite(float(text)) or abs(float(text) - expected) > tolerance * max(1.0, abs(expected)):
        raise AssertionError(f"decimal mismatch {text!r} != {expected}")


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C309 checker refuses optimized Python")
    parser = argparse.ArgumentParser(); parser.add_argument("--evidence", type=Path, default=DEFAULT); parser.add_argument("--evaluation", type=Path, default=DEFAULT_EVALUATION)
    args = parser.parse_args(); data = strict(args.evidence); evaluation = strict_yaml(args.evaluation); checks = 0
    if digest(data) != data.get("payload_sha256"):
        raise AssertionError("payload hash mismatch")
    checks += 1
    expected_top = {"schema", "candidate_id", "obstruction_id", "evaluation_date", "fixed_epoch", "source_commit", "scope_literal", "evaluator", "model", "theorem_contract", "cases", "equilibrium_strata", "collision_boundary", "route_a", "scope_flags", "nonclaims", "references", "enumeration", "payload_sha256"}
    if set(data) != expected_top:
        raise AssertionError("exact top-level key set failed")
    if (data["candidate_id"], data["obstruction_id"], data["source_commit"], data["scope_literal"]) != ("HCS-C309", "HEN-O293", SOURCE, SCOPE):
        raise AssertionError("identity/provenance mismatch")
    checks += 4
    expected_model = {
        "phase_space": "Sym(n,R) for every finite n>=1",
        "dynamics": "Xdot=I-X^2",
        "solution": "(X0 cosh(t)+I sinh(t))(I cosh(t)+X0 sinh(t))^{-1}",
    }
    expected_theorem = {
        "maximal_interval": "poles occur exactly when cosh(t)+lambda sinh(t)=0 for an initial eigenvalue lambda",
        "forward_atlas": "forward global iff lambda_min(X0)>=-1; its limit is I-2P_{lambda=-1}",
        "gradient": "Phi=tr(X^3/3-X) and Phi_dot=-norm(I-X^2)_F^2",
        "morse_bott": "symmetric involutions form Grassmann strata with exact stable, unstable, and center dimensions",
        "frechet": "the solution-map Loewner factor is the reciprocal product of the two scalar denominators",
        "linear_lift": "X=VU^{-1} lifts to Udot=V, Vdot=U until chart failure",
    }
    if data["model"] != expected_model or data["theorem_contract"] != expected_theorem:
        raise AssertionError("model/theorem contract mismatch")
    checks += 9
    if data["route_a"] != {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}:
        raise AssertionError("route tuple mismatch")
    if any(type(value) is not bool or value for value in data["scope_flags"].values()):
        raise AssertionError("scope firewall mismatch")
    checks += 10
    required_eval = {"schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch", "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256", "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters", "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention", "orbit_cutoff", "precision", "training_data", "forbidden_data", "artifact_paths", "a0", "a1", "a2", "a3", "a4", "tuple", "overall_verdict", "route_b_invocation_allowed", "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role", "source_owner_tokens"}
    if set(evaluation) != required_eval:
        raise AssertionError("evaluation exact key set mismatch")
    if (evaluation["schema"], evaluation["candidate_id"], evaluation["obstruction_id"], evaluation["source_commit"], evaluation["fixed_epoch"], evaluation["scope_literal"]) != ("route-a-evaluation-v0.2.0", "HCS-C309", "HEN-O293", SOURCE, 1788393600, SCOPE):
        raise AssertionError("evaluation identity mismatch")
    if evaluation["tuple"] != data["route_a"]["tuple"] or evaluation["overall_verdict"] != "ROUTE_A_REJECTED" or evaluation["route_b_invocation_allowed"] is not False:
        raise AssertionError("evaluation route mismatch")
    for key, verdict in zip(("a0", "a1", "a2", "a3", "a4"), data["route_a"]["tuple"]):
        if type(evaluation[key]) is not dict or evaluation[key].get("verdict") != verdict:
            raise AssertionError("evaluation branch mismatch")
    if evaluation["scope_flags"] != data["scope_flags"] or evaluation["theorem_status"] != "PROVABLE_AS_STATED":
        raise AssertionError("evaluation scope/status mismatch")
    checks += 20
    if len(data["cases"]) != len(SPECS) or [row["case_id"] for row in data["cases"]] != [row[0] for row in SPECS]:
        raise AssertionError("case order mismatch")
    for row, (case_id, raw) in zip(data["cases"], SPECS):
        expected_keys = {"case_id", "dimension", "eigenvalues", "forward_global", "forward_poles", "backward_poles", "forward_limit", "probe_rows", "loewner_time", "loewner_factors"}
        if set(row) != expected_keys:
            raise AssertionError("case key set mismatch")
        eig = [Fraction(item) for item in raw]
        if row["dimension"] != len(eig) or row["eigenvalues"] != raw:
            raise AssertionError("spectrum receipt mismatch")
        fp, bp = [], []
        for index, lam in enumerate(eig):
            value = float(lam)
            if abs(value) > 1:
                point = math.atanh(-1 / value)
                (fp if point > 0 else bp).append((index, point))
        if row["forward_global"] is not (not fp):
            raise AssertionError("global classification mismatch")
        if len(row["forward_poles"]) != len(fp) or len(row["backward_poles"]) != len(bp):
            raise AssertionError("pole multiplicity mismatch")
        for receipt, (index, point) in zip(row["forward_poles"], fp):
            if receipt["index"] != index: raise AssertionError("forward pole index")
            close(receipt["time"], point, 2e-15); checks += 2
        for receipt, (index, point) in zip(row["backward_poles"], bp):
            if receipt["index"] != index: raise AssertionError("backward pole index")
            close(receipt["time"], point, 2e-15); checks += 2
        limit = (["-1" if lam == -1 else "1" for lam in eig] if not fp else None)
        if row["forward_limit"] != limit:
            raise AssertionError("limit mismatch")
        tL = float(row["loewner_time"]); cL, sL = math.cosh(tL), math.sinh(tL)
        if len(row["loewner_factors"]) != len(eig): raise AssertionError("Loewner rows")
        for i, factors in enumerate(row["loewner_factors"]):
            if len(factors) != len(eig): raise AssertionError("Loewner columns")
            for j, receipt in enumerate(factors):
                expected = 1 / ((cL + float(eig[i]) * sL) * (cL + float(eig[j]) * sL))
                close(receipt, expected, 2e-15); checks += 1
        for probe in row["probe_rows"]:
            if set(probe) != {"time", "flow_eigenvalues", "denominators", "velocity_eigenvalues", "lyapunov_derivative"}:
                raise AssertionError("probe key set")
            t = float(Fraction(probe["time"])); velocities = []
            for k, lam in enumerate(eig):
                den = math.cosh(t) + float(lam) * math.sinh(t)
                val = (float(lam) * math.cosh(t) + math.sinh(t)) / den
                vel = 1 - val * val; velocities.append(vel)
                close(probe["denominators"][k], den, 2e-15)
                close(probe["flow_eigenvalues"][k], val, 2e-15)
                close(probe["velocity_eigenvalues"][k], vel, 3e-15)
                checks += 3
            close(probe["lyapunov_derivative"], -sum(value * value for value in velocities), 5e-15); checks += 1
        checks += 5
    strata = []
    for n in range(1, 9):
        for p in range(n + 1):
            q = n - p
            strata.append({"n": n, "plus_multiplicity": p, "minus_multiplicity": q, "stable_dimension": p*(p+1)//2, "unstable_dimension": q*(q+1)//2, "center_dimension": p*q, "ambient_dimension": n*(n+1)//2})
    if data["equilibrium_strata"] != strata:
        raise AssertionError("Morse--Bott ledger mismatch")
    checks += len(strata) * 7
    if data["enumeration"]["case_count"] != len(SPECS) or data["enumeration"]["stratum_count"] != len(strata):
        raise AssertionError("enumeration mismatch")
    print(f"C309 independent checker: PASS ({checks} checks)")


if __name__ == "__main__":
    main()
