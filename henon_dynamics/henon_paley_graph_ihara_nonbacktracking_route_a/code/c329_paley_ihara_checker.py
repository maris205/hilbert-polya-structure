#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C329."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c329_paley_ihara_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C329/2026-09-03.yaml"
SOURCE = "5ca65027918c0fce7ef9af82f3faf2e46ed6530c"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
YAML_RAW = "c6fda35b2c995e0aeea2e6387e85081fbdf5aa1ba7556f3f38218558599c6e96"
YAML_SEMANTIC = "a93e188801729210831752e124dd40857375059ebe4d0b8038dd5015a150646e"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIELDS = [(5, 5, 1), (9, 3, 2), (13, 13, 1), (17, 17, 1),
          (25, 5, 2), (29, 29, 1), (37, 37, 1), (41, 41, 1),
          (49, 7, 2), (53, 53, 1), (61, 61, 1), (73, 73, 1), (81, 3, 4)]
FLAGS = {"claims_target_arithmetic_local_data": False,
         "claims_target_euler_factors": False, "claims_root_number": False,
         "claims_automorphy": False, "claims_target_divisor_or_counting_law": False,
         "claims_target_functional_equation": False, "claims_target_zero_match": False,
         "claims_hilbert_polya_operator": False, "invokes_route_b": False}


def pairs(items):
    result = {}
    for key, value in items:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def strict_json(path):
    value = json.loads(path.read_text(), object_pairs_hook=pairs,
                       parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    if type(value) is not dict:
        raise TypeError("JSON root")
    return value


class Loader(yaml.SafeLoader):
    pass


Loader.yaml_implicit_resolvers = {
    key: [(tag, rx) for tag, rx in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in result:
            raise ValueError("duplicate or non-string YAML key")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


Loader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)


def strict_yaml(path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors or aliases forbidden")
    value = yaml.load(raw, Loader=Loader)
    if type(value) is not dict:
        raise TypeError("YAML root")
    return value


def need(condition, label):
    if not condition:
        raise AssertionError(label)


def exact_keys(value, keys, label):
    need(type(value) is dict and set(value) == set(keys), f"{label} keys")


def trim(poly):
    out = list(poly)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def remainder(numerator, denominator, p):
    work = trim([x % p for x in numerator])
    denominator = trim([x % p for x in denominator])
    while len(work) >= len(denominator) and work != [0]:
        offset = len(work) - len(denominator)
        scale = work[-1]
        for j, coefficient in enumerate(denominator):
            work[offset + j] = (work[offset + j] - scale * coefficient) % p
        work = trim(work)
    return work


def canonical_modulus(p, e):
    if e == 1:
        return []
    for coefficients in itertools.product(range(p), repeat=e):
        if coefficients[0] == 0:
            continue
        polynomial = list(coefficients) + [1]
        factors = []
        for degree in range(1, e // 2 + 1):
            factors.extend(list(low) + [1] for low in itertools.product(range(p), repeat=degree))
        if all(remainder(polynomial, factor, p) != [0] for factor in factors):
            return list(coefficients)
    raise AssertionError("modulus")


class AuditField:
    def __init__(self, p, e, modulus):
        self.p, self.e, self.modulus = p, e, list(modulus)

    def vector(self, x):
        vector = []
        for _ in range(self.e):
            vector.append(x % self.p)
            x //= self.p
        return vector

    def scalar(self, vector):
        return sum((entry % self.p) * self.p ** i for i, entry in enumerate(vector))

    def neg(self, x):
        return self.scalar([-entry for entry in self.vector(x)])

    def sub(self, x, y):
        return self.scalar([a - b for a, b in zip(self.vector(x), self.vector(y))])

    def product(self, x, y):
        left, right = self.vector(x), self.vector(y)
        coefficients = [0] * (2 * self.e - 1)
        for i in range(self.e):
            for j in range(self.e):
                coefficients[i + j] = (coefficients[i + j] + left[i] * right[j]) % self.p
        for power in range(2 * self.e - 2, self.e - 1, -1):
            lead = coefficients[power] % self.p
            for j, coefficient in enumerate(self.modulus):
                coefficients[power - self.e + j] = (
                    coefficients[power - self.e + j] - lead * coefficient) % self.p
        return self.scalar(coefficients[:self.e])


def mu(n):
    sign = 1
    prime = 2
    rest = n
    while prime * prime <= rest:
        if rest % prime == 0:
            rest //= prime
            sign = -sign
            if rest % prime == 0:
                return 0
            while rest % prime == 0:
                rest //= prime
        prime += 1
    return -sign if rest > 1 else sign


def divs(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def qmul(x, y, q):
    return x[0] * y[0] + q * x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def sums(lam, k1, n, radicand=None):
    if radicand is None:
        if n == 1:
            return lam
        a, b = 2, lam
        for _ in range(2, n + 1):
            a, b = b, lam * b - k1 * a
        return b
    if n == 1:
        return lam
    a, b = (Fraction(2), Fraction(0)), lam
    for _ in range(2, n + 1):
        product = qmul(lam, b, radicand)
        a, b = b, (product[0] - k1 * a[0], product[1] - k1 * a[1])
    return b


def leaves(value):
    if type(value) is dict:
        return sum(leaves(item) for item in value.values())
    if type(value) is list:
        return sum(leaves(item) for item in value)
    return 1


def main():
    if sys.flags.optimize:
        raise RuntimeError("C329 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_YAML)
    args = parser.parse_args()
    data = strict_json(args.evidence)
    root_keys = {"schema", "candidate_id", "obstruction_id", "evaluation_date", "fixed_epoch",
                 "source_commit", "scope_literal", "evaluator", "model", "theorem_contract",
                 "finite_grid", "field_rows", "arithmetic_controls", "route_a_yaml",
                 "collision_boundary", "route_a", "scope_flags", "nonclaims", "references",
                 "enumeration", "payload_sha256"}
    exact_keys(data, root_keys, "root")
    required = {"schema": "hcs-c329-paley-ihara-v1", "candidate_id": "HCS-C329",
                "obstruction_id": "HEN-O313", "evaluation_date": "2026-09-03",
                "fixed_epoch": 1788393600, "source_commit": SOURCE, "scope_literal": SCOPE}
    for key, value in required.items():
        need(data[key] == value, key)
    need(data["evaluator"] == {"version": "0.2.0", "sha256": EVALUATOR,
                               "authority": "flow_systems/skills/route-a-evaluator.md"}, "evaluator")
    body = dict(data)
    payload = body.pop("payload_sha256")
    need(payload == hashlib.sha256(json.dumps(
        body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest(), "payload")
    need(data["model"] == {
        "field_domain": "odd prime powers q congruent to 1 modulo 4",
        "graph": "x adjacent to y exactly when x-y is a nonzero square in F_q",
        "state_space": "directed Paley edges",
        "transition": "(x,y) to (y,z) exactly when z is adjacent to y and z differs from x",
        "orbit_convention": "oriented tailless nonbacktracking cycles modulo cyclic shift, not reversal"}, "model")
    need(data["theorem_contract"] == {
        "graph": "connected strongly regular Paley graph with exact parameters",
        "adjacency": "complete three-eigenvalue spectrum from additive characters",
        "bass": "exact determinant factorization and full Hashimoto spectrum",
        "orbits": "all traces and oriented primitive counts by Mobius inversion",
        "boundary": "q=5 is C5 with zero Bass excess and two oriented primitive 5-cycles"}, "contract")
    need(data["finite_grid"] == {
        "q_values": [q for q, _, _ in FIELDS], "max_trace_power": 12,
        "field_representation": "base-p coefficients modulo the lexicographically first monic irreducible polynomial in low-to-high coefficient order"}, "grid")
    need(len(data["field_rows"]) == len(FIELDS), "field row length")
    checks = 32
    for row, (q, p, e) in zip(data["field_rows"], FIELDS):
        exact_keys(row, {"q", "characteristic", "extension_degree", "modulus_coefficients_low_to_high",
                         "vertex_count", "degree", "edge_count", "directed_edge_count",
                         "quadratic_residues", "strongly_regular", "adjacency_spectrum",
                         "bass_factorization", "trace_rows"}, "field row")
        modulus = canonical_modulus(p, e)
        need((row["q"], row["characteristic"], row["extension_degree"]) == (q, p, e), "field coordinate")
        need(row["modulus_coefficients_low_to_high"] == modulus, "representation lock")
        field = AuditField(p, e, modulus)
        residues = sorted({field.product(x, x) for x in range(1, q)})
        k = (q - 1) // 2
        need(row["quadratic_residues"] == residues and len(residues) == k and field.neg(1) in residues,
             "residue set")
        adjacency = [[field.sub(y, x) in residues for y in range(q)] for x in range(q)]
        need(all(not adjacency[x][x] and sum(adjacency[x]) == k for x in range(q)), "simple regular")
        need(all(adjacency[x][y] == adjacency[y][x] for x in range(q) for y in range(q)), "symmetric")
        lam, nu = (q - 5) // 4, (q - 1) // 4
        for x in range(q):
            for y in range(x + 1, q):
                common = sum(adjacency[x][z] and adjacency[y][z] for z in range(q))
                need(common == (lam if adjacency[x][y] else nu), "strong regularity")
        edges = q * k // 2
        need(row["vertex_count"] == q and row["degree"] == k and row["edge_count"] == edges and
             row["directed_edge_count"] == q * k, "sizes")
        need(row["strongly_regular"] == {"v": q, "k": k, "lambda": lam, "mu": nu}, "srg")
        need(row["adjacency_spectrum"] == [
            {"label": "k", "minimal_polynomial": f"x-{k}", "multiplicity": 1},
            {"label": "r", "minimal_polynomial": f"x^2+x-{nu}", "multiplicity": k},
            {"label": "s", "minimal_polynomial": f"x^2+x-{nu}", "multiplicity": k}], "adjacency spectrum")
        excess = edges - q
        need(row["bass_factorization"] == {
            "one_minus_u_squared_exponent": excess,
            "trivial_factor": f"1-{k}u+{k-1}u^2",
            "r_factor_multiplicity": k, "s_factor_multiplicity": k,
            "total_degree": q * k}, "Bass data")
        need(len(row["trace_rows"]) == 12, "trace row length")
        known = {}
        for n, cell in enumerate(row["trace_rows"], 1):
            exact_keys(cell, {"n", "trace", "primitive_oriented_cycles"}, "trace cell")
            nontrivial = sums((Fraction(-1, 2), Fraction(1, 2)), k - 1, n, q)
            trace = excess * (1 + (-1) ** n) + sums(k, k - 1, n) + k * 2 * nontrivial[0]
            need(trace.denominator == 1, "trace integral")
            known[n] = int(trace)
            primitive_numerator = sum(mu(d) * known[n // d] for d in divs(n))
            need(primitive_numerator % n == 0, "primitive divisibility")
            need(cell == {"n": n, "trace": known[n],
                          "primitive_oriented_cycles": primitive_numerator // n}, "trace cell value")
        checks += q * (q - 1) // 2 + 24
    q5 = data["field_rows"][0]
    need(q5["bass_factorization"]["one_minus_u_squared_exponent"] == 0 and
         q5["trace_rows"][4]["primitive_oriented_cycles"] == 2, "q=5 boundary")
    need(data["arithmetic_controls"] == [
        "replace the quadratic-residue connection set by a seeded balanced additive Cayley set",
        "replace the finite field by an odd composite residue ring with its square set",
        "stratify prime fields against proper prime-power extensions at neighboring sizes"], "controls")
    need(data["collision_boundary"] == {
        "C15": "Heisenberg congruence voltage and Bass roots, not Paley quadratic-residue graphs",
        "C161": "cyclic quadratic Birkhoff Gauss sums, not nonbacktracking graph dynamics",
        "C260": "PGL2 finite-field permutation cycles, not quadratic-residue Cayley edges",
        "C269": "finite-field Chebyshev functional graphs, not Ihara edge cycles"}, "collisions")
    need(data["nonclaims"] == [
        "Finite field rows audit but do not prove the all-prime-power theorem.",
        "The Ihara product and the Paley Ramanujan bound are source-local and are not target Euler factors or a target RH statement.",
        "No literature-priority claim is made for the classical Paley, Hashimoto, or Bass ingredients.",
        "No target arithmetic local datum, root number, automorphy, target divisor, functional equation, target zero match, or Hilbert--Polya operator is asserted."], "nonclaims")
    need(data["references"] == [
        {"authors": "R. E. A. C. Paley", "title": "On Orthogonal Matrices",
         "identifier": "DOI:10.1002/sapm1933121311"},
        {"authors": "Ki-ichiro Hashimoto", "title": "Zeta Functions of Finite Graphs and Representations of p-Adic Groups",
         "identifier": "DOI:10.1016/B978-0-12-330580-0.50015-X"},
        {"authors": "Hyman Bass", "title": "The Ihara-Selberg zeta function of a tree lattice",
         "identifier": "DOI:10.1142/S0129167X92000357"}], "references")
    evaluation = strict_yaml(args.evaluation)
    yaml_keys = {"schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch",
                 "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256",
                 "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters",
                 "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention",
                 "orbit_cutoff", "precision", "training_data", "forbidden_data", "artifact_paths", "a0", "a1",
                 "a2", "a3", "a4", "tuple", "overall_verdict", "route_b_invocation_allowed",
                 "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role", "source_owner_tokens"}
    exact_keys(evaluation, yaml_keys, "evaluation")
    lock = data["route_a_yaml"]
    exact_keys(lock, {"relative_path", "raw_sha256", "semantic_sha256"}, "YAML lock")
    need(lock["relative_path"] == "evaluations/route_a/HCS-C329/2026-09-03.yaml", "YAML path")
    raw = hashlib.sha256(args.evaluation.read_bytes()).hexdigest()
    semantic = hashlib.sha256(json.dumps(evaluation, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    need(raw == lock["raw_sha256"] == YAML_RAW and semantic == lock["semantic_sha256"] == YAML_SEMANTIC, "YAML hashes")
    route = {"tuple": ["A0_WEAK_ARITHMETIC_RELATION", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
             "overall": "ROUTE_A_EXPLORATORY", "route_b_invocation_allowed": False}
    need(data["route_a"] == route and evaluation["tuple"] == route["tuple"] and
         evaluation["overall_verdict"] == route["overall"] and
         evaluation["route_b_invocation_allowed"] is False, "route")
    gate_status = ["PROVED", "PROVED", "STOP_SCOPED", "STOP_SCOPED", "PROVED"]
    need([evaluation[key]["verdict"] for key in ("a0", "a1", "a2", "a3", "a4")] == route["tuple"], "gate verdicts")
    need([evaluation[key]["evidence_status"] for key in ("a0", "a1", "a2", "a3", "a4")] == gate_status, "gate status")
    for key in ("a0", "a1", "a2", "a3", "a4"):
        exact_keys(evaluation[key], {"verdict", "evidence_status", "strongest_evidence", "strongest_failure"}, key)
    need(evaluation["schema"] == "route-a-evaluation-v0.2.0" and
         evaluation["candidate_id"] == "HCS-C329" and evaluation["obstruction_id"] == "HEN-O313" and
         evaluation["evaluation_date"] == "2026-09-03" and evaluation["source_commit"] == SOURCE and
         evaluation["fixed_epoch"] == 1788393600 and evaluation["scope_literal"] == SCOPE, "YAML identity")
    need(evaluation["evaluator_authority"] == "flow_systems/skills/route-a-evaluator.md" and
         evaluation["evaluator_version"] == "0.2.0" and
         evaluation["evaluator_authority_sha256"] == EVALUATOR, "YAML evaluator")
    need(evaluation["artifact_paths"] == ["results/c329_paley_ihara_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"], "artifacts")
    need(evaluation["scope_flags"] == FLAGS and data["scope_flags"] == FLAGS, "scope flags")
    need(evaluation["theorem_status"] == "PROVABLE_AS_STATED" and
         evaluation["finite_evidence_role"] == "exact finite-field regression audit only, never proof by finite extrapolation" and
         evaluation["route_b_lock_reason"] == "exploratory Route A status does not authorize Route B under the scope firewall", "YAML semantics")
    need(evaluation["source_owner_tokens"] == ["DOI:10.1002/sapm1933121311",
          "DOI:10.1016/B978-0-12-330580-0.50015-X", "DOI:10.1142/S0129167X92000357"], "source tokens")
    exact_keys(data["enumeration"], {"field_rows", "residue_cells", "adjacency_cells_recomputed",
               "directed_edges_recomputed", "legal_nonbacktracking_transitions_recomputed", "trace_rows",
               "audited_leaf_count"}, "enumeration")
    counted = dict(data)
    counted.pop("payload_sha256")
    enumeration = counted.pop("enumeration")
    need(enumeration == {"field_rows": 13, "residue_cells": 240,
                         "adjacency_cells_recomputed": 25901, "directed_edges_recomputed": 12704,
                         "legal_nonbacktracking_transitions_recomputed": 369848, "trace_rows": 156,
                         "audited_leaf_count": leaves(counted)}, "enumeration values")
    print(f"C329 independent checker: PASS ({checks} exact checks, 13 fields, 156 trace rows)")


if __name__ == "__main__":
    main()
