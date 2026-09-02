#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C316."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c316_elephant_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C316/2026-09-03.yaml"
SOURCE = "1938bae19e5a92f9ce2411aafdc68323bd641bd0"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EXPECTED_EVALUATION_SHA256 = "c9681f64de85e4a175a5880aede32a9ffad5a48bc03f5de081be2947b7f48808"
EXPECTED_EVALUATION_SEMANTIC_SHA256 = "16e3ac72536a8d8e20c7a1324a6587c1c43a2f2bb1c95e6d3e4775de2048d52d"
P_VALUES = [Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(2, 3),
            Fraction(3, 4), Fraction(4, 5), Fraction(1)]
Q_VALUES = [Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1)]
HISTORY_SPECS = [(Fraction(0), Fraction(1)), (Fraction(1, 2), Fraction(1, 4)),
                 (Fraction(3, 4), Fraction(1, 2)), (Fraction(4, 5), Fraction(1))]
SUPER_SPECS = [(p, q) for p in (Fraction(4, 5), Fraction(7, 8), Fraction(1))
               for q in (Fraction(0), Fraction(1, 2), Fraction(1))]


def duplicate(items):
    out = {}
    for key, value in items:
        if key in out:
            raise ValueError(f"duplicate JSON key {key}")
        out[key] = value
    return out


def nonfinite(value):
    raise ValueError(f"nonfinite JSON value {value}")


def strict_json(path: Path):
    value = json.loads(path.read_text(), object_pairs_hook=duplicate, parse_constant=nonfinite)
    if type(value) is not dict:
        raise TypeError("JSON root must be an object")
    return value


class UniqueLoader(yaml.SafeLoader):
    pass


UniqueLoader.yaml_implicit_resolvers = {
    key: [(tag, pattern) for tag, pattern in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def unique_mapping(loader, node, deep=False):
    out = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge is forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in out:
            raise ValueError("duplicate or non-string YAML key")
        out[key] = loader.construct_object(value_node, deep=deep)
    return out


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def strict_yaml(path: Path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors and aliases are forbidden")
    value = yaml.load(raw, Loader=UniqueLoader)
    if type(value) is not dict:
        raise TypeError("YAML root must be a mapping")
    return value


def digest(data):
    body = dict(data); body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def semantic_digest(data):
    """Canonical digest used to lock every parsed YAML value, independent of layout."""
    raw = json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def fs(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def product(n, c):
    out = Fraction(1)
    for j in range(1, n):
        out *= 1 + c / j
    return out


def harmonic(n):
    return sum((Fraction(1, j) for j in range(1, n + 1)), Fraction(0))


def second_formula(n, a):
    return n * harmonic(n) if a == Fraction(1, 2) else (2 * a * product(n, 2 * a) - n) / (2 * a - 1)


def advance(dist, n, a):
    nxt = {}
    for s, mass in dist.items():
        plus = (1 + a * Fraction(s, n)) / 2
        nxt[s + 1] = nxt.get(s + 1, Fraction(0)) + mass * plus
        nxt[s - 1] = nxt.get(s - 1, Fraction(0)) + mass * (1 - plus)
    return {s: mass for s, mass in nxt.items() if mass}


def parse_pmf(rows):
    if type(rows) is not list:
        raise TypeError("PMF rows must be a list")
    out = {}
    for row in rows:
        if type(row) is not dict or set(row) != {"position", "probability"}:
            raise AssertionError("PMF schema")
        s = row["position"]
        if type(s) is not int or s in out:
            raise AssertionError("PMF position")
        mass = Fraction(row["probability"])
        if mass < 0:
            raise AssertionError("negative PMF")
        out[s] = mass
    if list(out) != sorted(out):
        raise AssertionError("PMF order")
    return out


def leaf_count(value):
    if type(value) is dict:
        return sum(leaf_count(v) for v in value.values())
    if type(value) is list:
        return sum(leaf_count(v) for v in value)
    return 1


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C316 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT)
    parser.add_argument("--evaluation", type=Path, default=EVALUATION)
    args = parser.parse_args()
    data = strict_json(args.evidence); evaluation = strict_yaml(args.evaluation); checks = 0
    if hashlib.sha256(args.evaluation.read_bytes()).hexdigest() != EXPECTED_EVALUATION_SHA256:
        raise AssertionError("evaluation byte contract mismatch")
    if semantic_digest(evaluation) != EXPECTED_EVALUATION_SEMANTIC_SHA256:
        raise AssertionError("evaluation semantic contract mismatch")
    if digest(data) != data.get("payload_sha256"):
        raise AssertionError("payload hash mismatch")
    checks += 1
    expected_top = {"schema", "candidate_id", "obstruction_id", "evaluation_date", "fixed_epoch",
                    "source_commit", "scope_literal", "evaluator", "model", "theorem_contract",
                    "cases", "martingale_rows", "history_crosschecks", "superdiffusive_moment_rows",
                    "collision_boundary", "route_a", "scope_flags", "nonclaims", "references",
                    "enumeration", "payload_sha256"}
    if set(data) != expected_top:
        raise AssertionError("top-level schema mismatch")
    if (data["schema"], data["candidate_id"], data["obstruction_id"], data["evaluation_date"], data["fixed_epoch"], data["source_commit"], data["scope_literal"]) != (
            "hcs-c316-elephant-random-walk-v1", "HCS-C316", "HEN-O300", "2026-09-03", 1788393600, SOURCE, SCOPE):
        raise AssertionError("identity or provenance mismatch")
    checks += 5
    expected_model = {"increments": "+/-1", "initial_probability_plus": "q",
        "memory_rule": "uniformly recall one past increment; copy with p and reverse with 1-p",
        "position": "S_n=sum_{j<=n} X_j"}
    expected_theorem = {
        "finite_laws": "exact conditional kernel and all-n first two moments",
        "martingale": "S_n/G_n(2p-1) for p>0; (n-1)S_n from n=2 when p=0",
        "phase_transition": "diffusive p<3/4, critical p=3/4, superdiffusive p>3/4",
        "endpoint": "at p=1, S_n=nX_1 and q=0 or 1 gives a deterministic limit",
        "evidence_boundary": "finite exact enumeration is regression evidence and does not prove a CLT",
    }
    if data["model"] != expected_model or data["theorem_contract"] != expected_theorem:
        raise AssertionError("model/theorem contract mismatch")
    checks += 9
    if data["evaluator"] != {"version": "0.2.0", "sha256": "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"}:
        raise AssertionError("evaluator authority mismatch")
    expected_collision = {
        "C263": "the classical Polya urn is exchangeable with a Dirichlet limit; elephant increments have signed copying and a 3/4 scaling transition",
        "C273": "Sparre--Andersen treats iid symmetric increments; elephant increments retain full memory",
        "C302": "Quicksort has a recursive contraction limit rather than a memory-driven walk",
    }
    expected_nonclaims = [
        "No finite enumeration is presented as a proof of an asymptotic limit theorem.",
        "The stochastic memory clock has no rational-prime ownership or target determinant.",
        "No target arithmetic datum, Euler factor, root number, automorphy, target divisor, functional equation, zero match, or Hilbert--Polya operator is asserted.",
        "The package does not assert literature priority for the elephant-walk theorems.",
    ]
    expected_references = [
        {"identifier": "10.1103/PhysRevE.70.045101", "role": "original elephant random walk and finite moments"},
        {"identifier": "10.1088/1751-8121/aa95a6", "role": "martingale and three-regime limit theorems"},
    ]
    if data["collision_boundary"] != expected_collision or data["nonclaims"] != expected_nonclaims or data["references"] != expected_references:
        raise AssertionError("collision/nonclaim/reference contract mismatch")
    checks += 20
    if data["route_a"] != {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
                            "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}:
        raise AssertionError("route tuple mismatch")
    if set(data["scope_flags"]) != {"claims_target_arithmetic_local_data", "claims_target_euler_factors",
        "claims_root_number", "claims_automorphy", "claims_target_divisor_or_counting_law",
        "claims_target_functional_equation", "claims_target_zero_match", "claims_hilbert_polya_operator",
        "invokes_route_b"} or any(type(v) is not bool or v for v in data["scope_flags"].values()):
        raise AssertionError("scope firewall mismatch")
    checks += 12
    eval_keys = {"schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch",
        "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256",
        "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters",
        "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention",
        "orbit_cutoff", "precision", "training_data", "forbidden_data", "artifact_paths", "a0", "a1",
        "a2", "a3", "a4", "tuple", "overall_verdict", "route_b_invocation_allowed",
        "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role", "source_owner_tokens"}
    if set(evaluation) != eval_keys:
        raise AssertionError("evaluation schema mismatch")
    if (evaluation["schema"], evaluation["candidate_id"], evaluation["obstruction_id"],
        evaluation["source_commit"], evaluation["fixed_epoch"], evaluation["scope_literal"]) != (
        "route-a-evaluation-v0.2.0", "HCS-C316", "HEN-O300", SOURCE, 1788393600, SCOPE):
        raise AssertionError("evaluation provenance mismatch")
    if evaluation["tuple"] != data["route_a"]["tuple"] or evaluation["overall_verdict"] != "ROUTE_A_REJECTED" or evaluation["route_b_invocation_allowed"] is not False:
        raise AssertionError("evaluation verdict mismatch")
    for key, verdict in zip(("a0", "a1", "a2", "a3", "a4"), data["route_a"]["tuple"]):
        if type(evaluation[key]) is not dict or evaluation[key].get("verdict") != verdict:
            raise AssertionError("evaluation branch mismatch")
    if evaluation["scope_flags"] != data["scope_flags"] or evaluation["theorem_status"] != "PROVABLE_AFTER_EXPLICIT_BOUNDARY_SPLIT":
        raise AssertionError("evaluation scope/status mismatch")
    checks += 20
    if len(data["cases"]) != len(P_VALUES) * len(Q_VALUES):
        raise AssertionError("parameter case count")
    for row, p, q in zip(data["cases"], (p for p in P_VALUES for _ in Q_VALUES), Q_VALUES * len(P_VALUES)):
        if set(row) != {"case_id", "p", "q", "a", "initial_bias", "phase", "normalization", "limit_law", "times"}:
            raise AssertionError("case schema")
        a, b = 2 * p - 1, 2 * q - 1
        if (Fraction(row["p"]), Fraction(row["q"]), Fraction(row["a"]), Fraction(row["initial_bias"])) != (p, q, a, b):
            raise AssertionError("case parameters")
        expected_phase = "diffusive" if p < Fraction(3, 4) else "critical" if p == Fraction(3, 4) else "superdiffusive"
        expected_id = f"p-{p.numerator}-{p.denominator}-q-{q.numerator}-{q.denominator}"
        if p < Fraction(3, 4):
            expected_norm, expected_law = "sqrt(n)", f"Normal(0,{fs(1/(3-4*p))})"
        elif p == Fraction(3, 4):
            expected_norm, expected_law = "sqrt(n log n)", "Normal(0,1)"
        else:
            expected_norm, expected_law = f"n^{fs(2*p-1)}", "L with almost-sure and L4 convergence"
        if (row["case_id"], row["phase"], row["normalization"], row["limit_law"]) != (expected_id, expected_phase, expected_norm, expected_law) or len(row["times"]) != 14:
            raise AssertionError("phase/time coverage")
        dist = {1: q, -1: 1 - q}; dist = {s: m for s, m in dist.items() if m}
        for n, time in enumerate(row["times"], 1):
            if set(time) != {"n", "pmf", "total_mass", "mean", "second_moment", "variance",
                              "mean_formula", "second_formula", "mean_product", "second_product"} or time["n"] != n:
                raise AssertionError("time schema")
            got = parse_pmf(time["pmf"])
            if got != dist:
                raise AssertionError("exact DP mismatch")
            total = sum(dist.values(), Fraction(0))
            mean = sum((s * m for s, m in dist.items()), Fraction(0))
            second = sum((s * s * m for s, m in dist.items()), Fraction(0))
            expected = {"total_mass": total, "mean": mean, "second_moment": second,
                        "variance": second - mean * mean, "mean_formula": b * product(n, a),
                        "second_formula": second_formula(n, a), "mean_product": product(n, a),
                        "second_product": product(n, 2 * a)}
            for key, value in expected.items():
                if Fraction(time[key]) != value:
                    raise AssertionError(f"{key} mismatch")
                checks += 1
            if total != 1 or mean != expected["mean_formula"] or second != expected["second_formula"]:
                raise AssertionError("moment theorem mismatch")
            for s, mass in dist.items():
                if (s - n) % 2 or abs(s) > n or mass <= 0:
                    raise AssertionError("support/parity/positivity")
                checks += 1
            if n < 14:
                dist = advance(dist, n, a)
        checks += 8
    expected_martingales = []
    for p in P_VALUES:
        a = 2 * p - 1
        for n in range(2 if p == 0 else 1, 11):
            for s in range(-n, n + 1, 2):
                drift = (1 + a / n) * s
                if p == 0:
                    before, after, label = Fraction((n - 1) * s), Fraction(n) * drift, "(n-1)S_n from n=2"
                else:
                    before, after, label = Fraction(s) / product(n, a), drift / product(n + 1, a), "S_n/G_n(a)"
                expected_martingales.append({"p": fs(p), "n": n, "position": s,
                    "conditional_position_mean": fs(drift), "normalized_before": fs(before),
                    "normalized_after_mean": fs(after), "normalization": label})
                if before != after:
                    raise AssertionError("martingale identity failure")
    if data["martingale_rows"] != expected_martingales:
        raise AssertionError("martingale ledger mismatch")
    checks += len(expected_martingales) * 4
    if len(data["history_crosschecks"]) != len(HISTORY_SPECS):
        raise AssertionError("history coverage")
    for receipt, (p, q) in zip(data["history_crosschecks"], HISTORY_SPECS):
        if set(receipt) != {"p", "q", "terminal_n", "positive_history_count", "terminal_pmf"}:
            raise AssertionError("history schema")
        histories = {}
        if q: histories[(1,)] = q
        if q != 1: histories[(-1,)] = 1 - q
        a = 2 * p - 1
        for n in range(1, 8):
            nxt = {}
            for history, mass in histories.items():
                plus = (1 + a * Fraction(sum(history), n)) / 2
                if plus: nxt[history + (1,)] = mass * plus
                if plus != 1: nxt[history + (-1,)] = mass * (1 - plus)
            histories = nxt
        terminal = {}
        for history, mass in histories.items(): terminal[sum(history)] = terminal.get(sum(history), Fraction(0)) + mass
        if (Fraction(receipt["p"]), Fraction(receipt["q"]), receipt["terminal_n"], receipt["positive_history_count"]) != (p, q, 8, len(histories)):
            raise AssertionError("history identity")
        if parse_pmf(receipt["terminal_pmf"]) != terminal:
            raise AssertionError("history terminal mismatch")
        checks += len(histories) + len(terminal)
    super_rows = data["superdiffusive_moment_rows"]
    if len(super_rows) != 9:
        raise AssertionError("superdiffusive row count")
    for row, (expected_p, expected_q) in zip(super_rows, SUPER_SPECS):
        if set(row) != {"p", "q", "moment_1", "moment_2", "moment_3", "moment_4", "endpoint_class"}:
            raise AssertionError("super row schema")
        p, q = Fraction(row["p"]), Fraction(row["q"]); b = 2 * q - 1
        if (p, q) != (expected_p, expected_q):
            raise AssertionError("superdiffusive parameter ledger mismatch")
        expected = [(b, 2*p), (1/(4*p-3), 4*p-2),
                    (2*p*b/((2*p-1)*(4*p-3)), 6*p-3),
                    (6*(8*p*p-4*p-1)/((8*p-5)*(4*p-3)**2), 8*p-4)]
        for index, (prefactor, gamma_arg) in enumerate(expected, 1):
            cell = row[f"moment_{index}"]
            if set(cell) != {"prefactor", "gamma_argument"} or Fraction(cell["prefactor"]) != prefactor or Fraction(cell["gamma_argument"]) != gamma_arg:
                raise AssertionError("super moment mismatch")
            checks += 2
        label = "deterministic-sign" if p == 1 and q in (0, 1) else "two-point-sign" if p == 1 else "nondegenerate"
        if row["endpoint_class"] != label:
            raise AssertionError("endpoint classification")
        checks += 1
    enum = data["enumeration"]
    if set(enum) != {"parameter_case_count", "time_slice_count", "pmf_cell_count", "martingale_cell_count", "history_case_count", "superdiffusive_moment_case_count", "audited_leaf_count"}:
        raise AssertionError("enumeration schema")
    if enum["parameter_case_count"] != 35 or enum["time_slice_count"] != 490 or enum["martingale_cell_count"] != len(expected_martingales) or enum["history_case_count"] != 4 or enum["superdiffusive_moment_case_count"] != 9:
        raise AssertionError("enumeration accounting")
    if enum["pmf_cell_count"] != sum(len(t["pmf"]) for row in data["cases"] for t in row["times"]):
        raise AssertionError("PMF accounting")
    body_for_count = dict(data); body_for_count.pop("payload_sha256")
    if enum["audited_leaf_count"] != leaf_count(body_for_count):
        raise AssertionError("leaf accounting")
    checks += 8
    print(f"C316 independent checker: PASS ({checks} checks)")


if __name__ == "__main__":
    main()
