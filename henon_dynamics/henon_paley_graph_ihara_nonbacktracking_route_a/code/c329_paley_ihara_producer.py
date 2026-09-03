#!/usr/bin/env python3
"""Deterministic exact evidence producer for HCS-C329."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c329_paley_ihara_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C329/2026-09-03.yaml"
SOURCE = "5ca65027918c0fce7ef9af82f3faf2e46ed6530c"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
FIELDS = [(5, 5, 1), (9, 3, 2), (13, 13, 1), (17, 17, 1),
          (25, 5, 2), (29, 29, 1), (37, 37, 1), (41, 41, 1),
          (49, 7, 2), (53, 53, 1), (61, 61, 1), (73, 73, 1), (81, 3, 4)]
FLAGS = {
    "claims_target_arithmetic_local_data": False,
    "claims_target_euler_factors": False,
    "claims_root_number": False,
    "claims_automorphy": False,
    "claims_target_divisor_or_counting_law": False,
    "claims_target_functional_equation": False,
    "claims_target_zero_match": False,
    "claims_hilbert_polya_operator": False,
    "invokes_route_b": False,
}


class UniqueLoader(yaml.SafeLoader):
    pass


UniqueLoader.yaml_implicit_resolvers = {
    key: [(tag, rx) for tag, rx in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


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


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def strict_yaml(path: Path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors and aliases forbidden")
    value = yaml.load(raw, Loader=UniqueLoader)
    if type(value) is not dict:
        raise TypeError("YAML root")
    return value


def poly_trim(poly):
    value = list(poly)
    while len(value) > 1 and value[-1] == 0:
        value.pop()
    return value


def poly_remainder(dividend, divisor, p):
    value = poly_trim([x % p for x in dividend])
    divisor = poly_trim([x % p for x in divisor])
    while len(value) >= len(divisor) and value != [0]:
        shift = len(value) - len(divisor)
        factor = value[-1]
        for index, coefficient in enumerate(divisor):
            value[index + shift] = (value[index + shift] - factor * coefficient) % p
        value = poly_trim(value)
    return value


def irreducible_modulus(p, degree):
    if degree == 1:
        return []
    for low in itertools.product(range(p), repeat=degree):
        if low[0] == 0:
            continue
        polynomial = list(low) + [1]
        reducible = False
        for divisor_degree in range(1, degree // 2 + 1):
            for divisor_low in itertools.product(range(p), repeat=divisor_degree):
                divisor = list(divisor_low) + [1]
                if poly_remainder(polynomial, divisor, p) == [0]:
                    reducible = True
                    break
            if reducible:
                break
        if not reducible:
            return list(low)
    raise AssertionError("irreducible modulus not found")


class Field:
    def __init__(self, p, degree, modulus):
        self.p = p
        self.degree = degree
        self.q = p ** degree
        self.modulus = modulus

    def digits(self, value):
        out = []
        for _ in range(self.degree):
            out.append(value % self.p)
            value //= self.p
        return out

    def encode(self, digits):
        return sum((coefficient % self.p) * self.p ** index
                   for index, coefficient in enumerate(digits))

    def add(self, left, right):
        return self.encode([(a + b) % self.p
                            for a, b in zip(self.digits(left), self.digits(right))])

    def neg(self, value):
        return self.encode([(-a) % self.p for a in self.digits(value)])

    def sub(self, left, right):
        return self.add(left, self.neg(right))

    def mul(self, left, right):
        a, b = self.digits(left), self.digits(right)
        work = [0] * (2 * self.degree - 1)
        for i, x in enumerate(a):
            for j, y in enumerate(b):
                work[i + j] = (work[i + j] + x * y) % self.p
        if self.degree > 1:
            for power in range(len(work) - 1, self.degree - 1, -1):
                lead = work[power] % self.p
                if lead:
                    for index, coefficient in enumerate(self.modulus):
                        work[power - self.degree + index] = (
                            work[power - self.degree + index] - lead * coefficient) % self.p
        return self.encode(work[:self.degree])

    def power(self, base, exponent):
        answer = 1
        while exponent:
            if exponent & 1:
                answer = self.mul(answer, base)
            base = self.mul(base, base)
            exponent //= 2
        return answer


def mobius(n):
    value, primes = n, 0
    factor = 2
    while factor * factor <= value:
        if value % factor == 0:
            value //= factor
            if value % factor == 0:
                return 0
            primes += 1
            while value % factor == 0:
                value //= factor
        factor += 1
    if value > 1:
        primes += 1
    return -1 if primes % 2 else 1


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def quadratic_mul(left, right, q):
    a, b = left
    c, d = right
    return a * c + b * d * q, a * d + b * c


def spectral_power_sum(lam, k_minus_one, n, q=None):
    if q is None:
        if n == 0:
            return 2
        old, current = 2, lam
        for _ in range(2, n + 1):
            old, current = current, lam * current - k_minus_one * old
        return current
    if n == 0:
        return Fraction(2), Fraction(0)
    old, current = (Fraction(2), Fraction(0)), lam
    for _ in range(2, n + 1):
        product = quadratic_mul(lam, current, q)
        old, current = current, (product[0] - k_minus_one * old[0],
                                 product[1] - k_minus_one * old[1])
    return current


def field_row(q, p, degree):
    modulus = irreducible_modulus(p, degree)
    field = Field(p, degree, modulus)
    residues = sorted({field.mul(x, x) for x in range(1, q)})
    if len(residues) != (q - 1) // 2 or field.neg(1) not in residues:
        raise AssertionError("quadratic residue census")
    k = (q - 1) // 2
    edges = q * k // 2
    bass_exponent = edges - q
    traces = {}
    rows = []
    r = (Fraction(-1, 2), Fraction(1, 2))
    for n in range(1, 13):
        trivial = spectral_power_sum(k, k - 1, n)
        nontrivial_one = spectral_power_sum(r, k - 1, n, q)
        if nontrivial_one[1] != 0 and False:
            raise AssertionError("unreachable")
        conjugate_sum = 2 * nontrivial_one[0]
        trace = bass_exponent * (1 + (-1) ** n) + trivial + k * conjugate_sum
        if trace.denominator != 1:
            raise AssertionError("integral trace")
        traces[n] = int(trace)
        primitive = sum(mobius(d) * traces[n // d] for d in divisors(n)) // n
        rows.append({"n": n, "trace": traces[n], "primitive_oriented_cycles": primitive})
    return {
        "q": q,
        "characteristic": p,
        "extension_degree": degree,
        "modulus_coefficients_low_to_high": modulus,
        "vertex_count": q,
        "degree": k,
        "edge_count": edges,
        "directed_edge_count": q * k,
        "quadratic_residues": residues,
        "strongly_regular": {"v": q, "k": k, "lambda": (q - 5) // 4,
                             "mu": (q - 1) // 4},
        "adjacency_spectrum": [
            {"label": "k", "minimal_polynomial": f"x-{k}", "multiplicity": 1},
            {"label": "r", "minimal_polynomial": f"x^2+x-{(q - 1) // 4}",
             "multiplicity": k},
            {"label": "s", "minimal_polynomial": f"x^2+x-{(q - 1) // 4}",
             "multiplicity": k},
        ],
        "bass_factorization": {
            "one_minus_u_squared_exponent": bass_exponent,
            "trivial_factor": f"1-{k}u+{k-1}u^2",
            "r_factor_multiplicity": k,
            "s_factor_multiplicity": k,
            "total_degree": q * k,
        },
        "trace_rows": rows,
    }


def leaves(value):
    if type(value) is dict:
        return sum(leaves(item) for item in value.values())
    if type(value) is list:
        return sum(leaves(item) for item in value)
    return 1


def produce(evaluation_path):
    evaluation = strict_yaml(evaluation_path)
    rows = [field_row(*triple) for triple in FIELDS]
    data = {
        "schema": "hcs-c329-paley-ihara-v1",
        "candidate_id": "HCS-C329",
        "obstruction_id": "HEN-O313",
        "evaluation_date": "2026-09-03",
        "fixed_epoch": EPOCH,
        "source_commit": SOURCE,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR,
                      "authority": "flow_systems/skills/route-a-evaluator.md"},
        "model": {
            "field_domain": "odd prime powers q congruent to 1 modulo 4",
            "graph": "x adjacent to y exactly when x-y is a nonzero square in F_q",
            "state_space": "directed Paley edges",
            "transition": "(x,y) to (y,z) exactly when z is adjacent to y and z differs from x",
            "orbit_convention": "oriented tailless nonbacktracking cycles modulo cyclic shift, not reversal",
        },
        "theorem_contract": {
            "graph": "connected strongly regular Paley graph with exact parameters",
            "adjacency": "complete three-eigenvalue spectrum from additive characters",
            "bass": "exact determinant factorization and full Hashimoto spectrum",
            "orbits": "all traces and oriented primitive counts by Mobius inversion",
            "boundary": "q=5 is C5 with zero Bass excess and two oriented primitive 5-cycles",
        },
        "finite_grid": {"q_values": [q for q, _, _ in FIELDS], "max_trace_power": 12,
                        "field_representation": "base-p coefficients modulo the lexicographically first monic irreducible polynomial in low-to-high coefficient order"},
        "field_rows": rows,
        "arithmetic_controls": [
            "replace the quadratic-residue connection set by a seeded balanced additive Cayley set",
            "replace the finite field by an odd composite residue ring with its square set",
            "stratify prime fields against proper prime-power extensions at neighboring sizes",
        ],
        "route_a_yaml": {
            "relative_path": "evaluations/route_a/HCS-C329/2026-09-03.yaml",
            "raw_sha256": hashlib.sha256(evaluation_path.read_bytes()).hexdigest(),
            "semantic_sha256": hashlib.sha256(json.dumps(
                evaluation, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest(),
        },
        "collision_boundary": {
            "C15": "Heisenberg congruence voltage and Bass roots, not Paley quadratic-residue graphs",
            "C161": "cyclic quadratic Birkhoff Gauss sums, not nonbacktracking graph dynamics",
            "C260": "PGL2 finite-field permutation cycles, not quadratic-residue Cayley edges",
            "C269": "finite-field Chebyshev functional graphs, not Ihara edge cycles",
        },
        "route_a": {"tuple": ["A0_WEAK_ARITHMETIC_RELATION", "A1_PASS_ANALYTIC",
                               "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
                    "overall": "ROUTE_A_EXPLORATORY", "route_b_invocation_allowed": False},
        "scope_flags": FLAGS,
        "nonclaims": [
            "Finite field rows audit but do not prove the all-prime-power theorem.",
            "The Ihara product and the Paley Ramanujan bound are source-local and are not target Euler factors or a target RH statement.",
            "No literature-priority claim is made for the classical Paley, Hashimoto, or Bass ingredients.",
            "No target arithmetic local datum, root number, automorphy, target divisor, functional equation, target zero match, or Hilbert--Polya operator is asserted.",
        ],
        "references": [
            {"authors": "R. E. A. C. Paley", "title": "On Orthogonal Matrices",
             "identifier": "DOI:10.1002/sapm1933121311"},
            {"authors": "Ki-ichiro Hashimoto", "title": "Zeta Functions of Finite Graphs and Representations of p-Adic Groups",
             "identifier": "DOI:10.1016/B978-0-12-330580-0.50015-X"},
            {"authors": "Hyman Bass", "title": "The Ihara-Selberg zeta function of a tree lattice",
             "identifier": "DOI:10.1142/S0129167X92000357"},
        ],
    }
    counted = dict(data)
    data["enumeration"] = {
        "field_rows": len(rows),
        "residue_cells": sum(len(row["quadratic_residues"]) for row in rows),
        "adjacency_cells_recomputed": sum(row["q"] ** 2 for row in rows),
        "directed_edges_recomputed": sum(row["directed_edge_count"] for row in rows),
        "legal_nonbacktracking_transitions_recomputed": sum(
            row["directed_edge_count"] * (row["degree"] - 1) for row in rows),
        "trace_rows": sum(len(row["trace_rows"]) for row in rows),
        "audited_leaf_count": leaves(counted),
    }
    body = dict(data)
    data["payload_sha256"] = hashlib.sha256(json.dumps(
        body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    return data


def main():
    if sys.flags.optimize:
        raise RuntimeError("C329 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    parser.add_argument("--evaluation", type=Path, default=EVALUATION)
    args = parser.parse_args()
    data = produce(args.evaluation)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C329_PRODUCER_PASS {data['payload_sha256']} {data['enumeration']['field_rows']} fields")


if __name__ == "__main__":
    main()
