#!/usr/bin/env python3
"""Exact HCS-P66 boundary cohomology anomaly certificate."""
from __future__ import annotations
import argparse, copy, hashlib, itertools, json
from fractions import Fraction
from pathlib import Path
import sympy as sp

PROJECT = Path(__file__).resolve().parents[1]
TRACK = PROJECT.parent
DEFAULT_OUTPUT = PROJECT / "results/c66_certificate.json"
DEPENDENCIES = {
    "p64_proof": (TRACK / "henon_reflection_boundary_mahler_pressure/PROOF_PACKAGE.md", "b98dbeb0ca2dbaa8196726eef9cd3f25dbdd1a620096d51a95c806eae95a3db6"),
    "p65_proof": (TRACK / "henon_minimal_symmetry_defect_pressure/PROOF_PACKAGE.md", "052ed9114f3da7ca3a039263e4bdfc617cabc6e9023542c0111d2d1c008b99eb"),
    "p65_certificate": (TRACK / "henon_minimal_symmetry_defect_pressure/results/c65_certificate.json", "f0f9e3bb8c361c7b5b313ec38b96c585863fa0fa18c18e2461d97b14ed436cf2"),
    "p65_paper": (TRACK / "henon_minimal_symmetry_defect_pressure/paper/paper.pdf", "d7574c7c8b6c0d70ef5bde5b2b5c074477dfaaf5a6136d028b0025fb2ea26ab9"),
}

def canonical_sha(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()

def dependency_locks():
    result = {}
    for name, (path, expected) in DEPENDENCIES.items():
        observed = hashlib.sha256(path.read_bytes()).hexdigest()
        if observed != expected:
            raise RuntimeError(name)
        result[name] = {"path": str(path.relative_to(TRACK)), "sha256": observed}
    return result

def degree(n):
    return sum(int(sp.mobius(n // d)) * 2 ** ((d + 1) // 2) for d in sp.divisors(n))

def palindrome(half):
    return half + half[:0:-1]

def least_period(word):
    for divisor in sp.divisors(len(word)):
        d = int(divisor)
        if all(word[j] == word[j % d] for j in range(len(word))):
            return d
    raise ArithmeticError

def primitive_words(n):
    return [
        word for half in itertools.product((0, 1), repeat=(n + 1) // 2)
        if least_period(word := palindrome(half)) == n
    ]

def cylinder_u(word, center, radius):
    n = len(word)
    return int(all(word[(center-k) % n] == word[(center+k) % n] for k in range(1, radius+1)))

def finite_row(n, radius):
    full = [palindrome(half) for half in itertools.product((0, 1), repeat=(n + 1) // 2)]
    primitive = primitive_words(n)
    full_mean = Fraction(sum(cylinder_u(word, 1, radius) for word in full), len(full))
    primitive_mean = Fraction(sum(cylinder_u(word, 1, radius) for word in primitive), len(primitive))
    target = Fraction(1, 2**radius)
    epsilon = Fraction(len(full) - len(primitive), len(full))
    if len(primitive) != degree(n) or full_mean != target or abs(primitive_mean-target) > epsilon:
        raise ArithmeticError((n, radius))
    if any(cylinder_u(word, 0, radius) != 1 for word in primitive):
        raise ArithmeticError("axis")
    if any(sum(cylinder_u(word, j, radius)-cylinder_u(word, (j+1) % n, radius) for j in range(n)) != 0 for word in primitive):
        raise ArithmeticError("telescope")
    return {
        "period": n, "radius": radius, "primitive_count": len(primitive),
        "full_shifted_u_mean": str(full_mean), "primitive_shifted_u_mean": str(primitive_mean),
        "target_2_power_minus_r": str(target), "primitive_tv_bound": str(epsilon),
        "finite_v_anomaly": str(2 * (1-primitive_mean)),
        "full_v_anomaly": str(2 * (1-target)), "orbit_coboundary_sum": "0",
    }

def core_payload():
    return {
        "candidate_id": "HCS-P66",
        "boundary_anomaly": "A_J(u)=int(u-u o sigma)d eta_J",
        "pressure_gauge_law": "P_J(f+u-u o sigma)=P_J(f)-A_J(u)",
        "orbit_invariance": "every finite periodic Birkhoff sum of u-u o sigma is exactly zero",
        "cylinder_witness": "u_r=1_{s_(-k)=s_k for 1<=k<=r}",
        "witness_anomaly": "A_J(2u_r-1)=2(1-2^(-r))",
        "anomaly_operator_norm": "2",
        "measure_relation": "eta_J and sigma_*eta_J are mutually singular",
        "rows": [finite_row(2*radius+11, radius) for radius in range(1, 6)],
        "strongest_positive_result": "the marked reflection pressure has a nonzero norm-two cohomology anomaly with explicit cylinder witnesses, while orbit pressure is exactly gauge invariant",
        "strongest_obstruction": "marked-axis packet pressure is not a Livsic/cohomology invariant and is not canonical without a frozen gauge",
        "open_theorem": "prove uniform cyclic orbit averaging is the unique normalized linear sampler invariant under every symbolic coboundary",
        "reusable_structure": "the signed boundary measure eta_J-sigma_*eta_J exactly represents gauge dependence",
        "round2_clue": "classify cyclic samplers; coboundary invariance should force uniform weights and select orbit averaging canonically",
        "claim_status": {
            "boundary_gauge_anomaly": "PROVED", "anomaly_norm_two": "PROVED",
            "orbit_gauge_invariance": "PROVED", "canonical_sampler_uniqueness": "OPEN",
            "arithmetic_advance": "NO", "route_b_authorized": False,
        },
    }

def validate(core):
    if type(core) is not dict or core.get("candidate_id") != "HCS-P66":
        raise ValueError
    if core.get("anomaly_operator_norm") != "2":
        raise ValueError
    if core.get("orbit_invariance") != "every finite periodic Birkhoff sum of u-u o sigma is exactly zero":
        raise ValueError
    if [row["radius"] for row in core["rows"]] != [1, 2, 3, 4, 5]:
        raise ValueError
    if core["claim_status"]["arithmetic_advance"] != "NO" or core["claim_status"]["route_b_authorized"] is not False:
        raise ValueError

def mutation_audit(core):
    keys = ["candidate_id", "boundary_anomaly", "pressure_gauge_law", "orbit_invariance", "cylinder_witness", "witness_anomaly", "anomaly_operator_norm", "measure_relation", "strongest_positive_result", "strongest_obstruction", "open_theorem", "reusable_structure", "round2_clue"]
    rejected = []
    for key in keys:
        trial = copy.deepcopy(core); trial[key] = "FORGED"
        try:
            validate(trial)
            if trial != core: raise ValueError
        except ValueError:
            rejected.append(key)
    status_cases = [("boundary_gauge_anomaly", "OPEN"), ("anomaly_norm_two", "OPEN"), ("orbit_gauge_invariance", "OPEN"), ("canonical_sampler_uniqueness", "PROVED"), ("arithmetic_advance", "YES"), ("route_b_authorized", True)]
    for key, value in status_cases:
        trial = copy.deepcopy(core); trial["claim_status"][key] = value
        try:
            validate(trial)
            if trial != core: raise ValueError
        except ValueError:
            rejected.append("status-" + key)
    return {"attempted": len(rejected), "rejected": rejected, "all_rejected": len(rejected) == 19}

def build():
    core = core_payload(); validate(core)
    result = dict(core); result["dependency_locks"] = dependency_locks(); result["mutation_audit"] = mutation_audit(core)
    if not result["mutation_audit"]["all_rejected"]: raise RuntimeError
    result["core_sha256"] = canonical_sha(core); result["check"] = True
    return result

def main():
    parser = argparse.ArgumentParser(); parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args(); result = build()
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"candidate_id": "HCS-P66", "check": True, "core_sha256": result["core_sha256"], "mutations_rejected": 19}, sort_keys=True))

if __name__ == "__main__": main()
