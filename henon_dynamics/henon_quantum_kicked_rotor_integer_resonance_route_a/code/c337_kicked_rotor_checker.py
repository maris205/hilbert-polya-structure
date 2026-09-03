#!/usr/bin/env python3
"""Producer-independent strict checker for HCS-C337."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import yaml
from yaml.tokens import AliasToken, AnchorToken


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c337_kicked_rotor_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C337/2026-09-03.yaml"
SOURCE = "db2c816b7b6bd450f51f79b91842cb882b0bd773"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EVAL_RAW = "1844e53da7f5d2c498518b4b1941ec50358505fe37ec959692bb11b57b1475a2"
EVAL_SEMANTIC = "9a378976e7e821c71e87428a969ec3fb20eaa4861837b28b91ed8fece15d5b56"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600

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
MODEL = {
    "hilbert_space": "L2(T,dtheta/(2pi)) with basis |n>=exp(i n theta)",
    "momentum": "n_hat=-i d/dtheta with integer spectrum",
    "floquet_order": "U_tau=exp(-i tau n_hat^2/2) exp(-i kappa cos(theta))",
    "resonance_sheet": "tau=2pi ell with ell a positive integer",
    "parameter_domain": "kappa real, m integer, t nonnegative integer",
    "kinetic_energy": "n_hat^2/2",
}
THEOREM = {
    "parity": "even ell gives identity free factor; odd ell gives half-turn R",
    "even_kernel": "<n|U^t|m>=(-i)^(n-m) J_(n-m)(kappa t)",
    "characteristic": "E exp(iu(n-m))=J_0(2 kappa t sin(u/2)) on the even sheet",
    "moments": "centered moments through six and exact ballistic variance are explicit",
    "odd_involution": "for odd ell, U=R K_kappa and U^2=I",
    "boundaries": "all m, kappa=0, t=0, parity, vector phase, and operator order are explicit",
}
REFERENCES = [
    {"identifier": "10.1103/PhysRevE.54.5948", "role": "primary antiresonance history"},
    {"identifier": "10.1103/PhysRevE.73.026206", "role": "primary general resonance history"},
    {"identifier": "10.1103/PhysRevLett.96.160403", "role": "primary experimental ballistic-resonance context"},
]
COLLISIONS = {
    "C110": "classical nonautonomous Henon Floquet dynamics, not a quantum rotor",
    "C143": "coined quantum walk, not a cosine-kicked momentum lattice",
    "C148": "open Walsh quantum baker, not a closed rotor unitary",
    "C178": "harmonic metaplectic strobe, not the kicked-rotor parity sheet",
    "C224": "two-level Landau--Zener scattering, not a kicked rotor",
    "C318": "static SSH lattice, not a time-periodic rotor",
    "C323": "finite continuous-time quantum search, not Floquet momentum transport",
}
NONCLAIMS = [
    "No literature-priority claim is made for resonance, antiresonance, or Bessel transport.",
    "No general rational resonance, detuning, localization, or quasienergy theorem is claimed.",
    "No target arithmetic datum, Euler factor, root number, automorphy, target divisor, functional equation, target-zero match, Hilbert--Polya operator, or Route-B input is claimed.",
]
GRID = {
    "ell": "1..12", "momentum": "-16..16 for parity and -3..3 for moments",
    "time": "0..8 for moments and 0..9 for operator words",
    "formal_degree": "0..14", "formal_shift": "-14..14",
    "numeric_cutoff": 120, "numeric_precision_digits": 90,
}
BOUNDARIES = {
    "kappa_zero": "even ell gives I; odd ell gives R; momentum probabilities are stationary",
    "t_zero": "J_q(0)=delta_(q,0) and U^0=I",
    "odd_vector_phase": "at kappa=0, |m> acquires (-1)^m under one odd-sheet kick although its ray and probability law are fixed",
    "odd_period": "U^2=I as an operator; individual states may already be one-step eigenstates",
    "even_nonzero": "for kappa nonzero, the even-sheet variance is kappa^2 t^2/2",
    "operator_order": "free-after-kick is frozen; the reversed product is not silently substituted",
}
TOP_KEYS = {
    "schema", "candidate_id", "obstruction_id", "source_commit", "fixed_epoch",
    "scope_literal", "evaluator", "evaluation", "model", "theorem_contract",
    "references", "collision_boundary", "nonclaims", "route_a", "scope_flags",
    "parameter_grid", "parity_rows", "formal_kernel_coefficients", "moment_rows",
    "operator_rows", "numeric_rows", "boundary_rows", "enumeration", "payload_sha256",
}
EVAL_KEYS = {
    "schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch",
    "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256",
    "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters",
    "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention",
    "orbit_cutoff", "precision", "training_data", "forbidden_data", "artifact_paths",
    "a0", "a1", "a2", "a3", "a4", "tuple", "overall_verdict",
    "route_b_invocation_allowed", "route_b_lock_reason", "scope_flags", "theorem_status",
    "finite_evidence_role", "source_owner_tokens",
}
EVAL_FIXED = {
    "schema": "route-a-evaluation-v0.2.0",
    "candidate_id": "HCS-C337",
    "title": "Integer-resonant quantum kicked rotor parity sheet",
    "evaluation_date": "2026-09-03",
    "source_commit": SOURCE,
    "fixed_epoch": EPOCH,
    "scope_literal": SCOPE,
    "evaluator_authority": "flow_systems/skills/route-a-evaluator.md",
    "evaluator_version": "0.2.0",
    "evaluator_authority_sha256": EVALUATOR,
    "obstruction_id": "HEN-O321",
    "candidate_definition": "the quantum kicked rotor Floquet unitary exp(-i tau n_hat squared/2) exp(-i kappa cos theta) at tau=2 pi ell",
    "family": "periodically kicked quantum rotor and infinite momentum-lattice Floquet dynamics",
    "phase_space": "L2 of the circle with normalized Haar measure and integer momentum basis",
    "dynamics": "one source kick followed by free rotation in the frozen Floquet ordering",
    "parameters": "positive integer ell, real kick strength kappa, integer momentum seed m, and nonnegative integer kick count t",
    "parameter_provenance": "source rotor period and kick strength only, never target-fitted",
    "arithmetic_origin": "none",
    "clock": "source integer kick count",
    "normalization": "n_hat=-i d/dtheta; normalized Haar measure dtheta/(2 pi); kinetic energy n_hat squared/2",
    "determinant_convention": "no dynamical Euler product, Fredholm determinant, or target determinant is defined",
    "orbit_cutoff": "all-time analytic theorem on the integer parity sheet; finite grids and formal coefficients are receipts only",
    "precision": "exact integer, rational, Gaussian-rational, and symbolic polynomial identities with high-precision Bessel spot checks",
    "training_data": "none",
    "forbidden_data": "target arithmetic local data, Euler factors, root numbers, automorphy, target divisor or functional equation, target zeros, Hilbert-Polya operators, and Route B",
    "artifact_paths": ["results/c337_kicked_rotor_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"],
    "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
    "overall_verdict": "ROUTE_A_REJECTED",
    "route_b_invocation_allowed": False,
    "route_b_lock_reason": "no arithmetic source, target Euler factor, target divisor, or same-clock arithmetic lift exists",
    "scope_flags": FLAGS,
    "theorem_status": "PROVABLE_AS_STATED",
    "finite_evidence_role": "convention, coefficient, moment, and implementation receipt only; parity reduction and Fourier analysis prove the all-time theorem",
    "source_owner_tokens": ["10.1103/PhysRevE.54.5948", "10.1103/PhysRevE.73.026206", "10.1103/PhysRevLett.96.160403"],
}
GATES = {
    "a0": {"verdict": "A0_FAIL", "evidence_status": "PROVED",
           "strongest_evidence": "the integer resonance and antiresonance sheet is derived exactly from the source Floquet unitary",
           "strongest_failure": "ell, kappa, momentum labels, and kick count contain no intrinsic rational-prime or prime-power payload"},
    "a1": {"verdict": "A1_FAIL", "evidence_status": "PROVED",
           "strongest_evidence": "the odd-parity operator is an exact involution and the even-parity propagator is explicit",
           "strongest_failure": "Floquet recurrences and Bessel spreading are not an isolated arithmetic primitive-orbit ledger with repetition weights"},
    "a2": {"verdict": "A2_FAIL", "evidence_status": "STOP_SCOPED",
           "strongest_evidence": "the exact unitary kernel and characteristic function are source-local",
           "strongest_failure": "no primitive-orbit Euler product or target divisor is defined"},
    "a3": {"verdict": "A3_FAIL", "evidence_status": "STOP_SCOPED",
           "strongest_evidence": "all integer-resonance times and parity faces are covered by one analytic theorem",
           "strongest_failure": "the theorem supplies no target functional equation, continuation, counting law, or Weil compression"},
    "a4": {"verdict": "A4_NATURAL_QUANTIZATION", "evidence_status": "PROVED",
           "strongest_evidence": "the self-adjoint rotor momentum and bounded cosine kick give a source-native unitary Floquet quantization with the physical kick clock",
           "strongest_failure": "the quasienergy structure is not identified with target zeros and is not a Hilbert-Polya operator"},
}


class UniqueLoader(yaml.SafeLoader):
    pass


UniqueLoader.yaml_implicit_resolvers = {
    key: [(tag, regexp) for tag, regexp in values if tag != "tag:yaml.org,2002:timestamp"]
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


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def duplicate_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def strict_json(path: Path):
    value = json.loads(path.read_text(), object_pairs_hook=duplicate_pairs,
                       parse_constant=lambda token: (_ for _ in ()).throw(ValueError(f"nonfinite {token}")))
    if type(value) is not dict:
        raise ValueError("evidence root must be an object")
    return value


def strict_yaml(path: Path):
    raw = path.read_bytes()
    tokens = list(yaml.scan(raw.decode()))
    if any(isinstance(token, (AliasToken, AnchorToken)) for token in tokens):
        raise ValueError("YAML anchors and aliases forbidden")
    value = yaml.load(raw.decode(), Loader=UniqueLoader)
    if type(value) is not dict:
        raise ValueError("evaluation root must be a mapping")
    return raw, value


def canonical_hash(value) -> str:
    return sha(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())


def qstr(x: Fraction) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def parse_q(x: str) -> Fraction:
    if type(x) is not str:
        raise ValueError("rational encoding is not a string")
    return Fraction(x)


def phase(power: int) -> tuple[Fraction, Fraction]:
    return ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(-1)),
            (Fraction(-1), Fraction(0)), (Fraction(0), Fraction(1)))[power % 4]


def bessel_coefficient(q: int, degree: int) -> tuple[Fraction, Fraction]:
    order = abs(q)
    if degree < order or (degree - order) % 2:
        return Fraction(0), Fraction(0)
    j = (degree - order) // 2
    scalar = Fraction((-1 if j % 2 else 1), 2**degree * math.factorial(j) * math.factorial(order + j))
    if q < 0 and order % 2:
        scalar = -scalar
    re, im = phase(q)
    return scalar * re, scalar * im


def central(x: Fraction) -> list[Fraction]:
    return [Fraction(1), Fraction(0), x**2 / 2, Fraction(0),
            x**2 / 2 + 3*x**4 / 8, Fraction(0),
            x**2 / 2 + 15*x**4 / 8 + 5*x**6 / 16]


def raw_from_center(m: int, values: list[Fraction]) -> list[Fraction]:
    answer = []
    for order in range(7):
        answer.append(sum(Fraction(math.comb(order, j)) * Fraction(m) ** (order-j) * values[j]
                          for j in range(order + 1)))
    return answer


def leaf_count(value) -> int:
    if type(value) is dict:
        return sum(leaf_count(child) for child in value.values())
    if type(value) is list:
        return sum(leaf_count(child) for child in value)
    return 1


def check_evaluation(path: Path, evidence: dict) -> int:
    raw, value = strict_yaml(path)
    if sha(raw) != EVAL_RAW or canonical_hash(value) != EVAL_SEMANTIC:
        raise AssertionError("evaluation raw/semantic lock mismatch")
    if set(value) != EVAL_KEYS:
        raise AssertionError("evaluation key schema mismatch")
    for key, expected in EVAL_FIXED.items():
        if value.get(key) != expected:
            raise AssertionError(f"evaluation field mismatch: {key}")
    for key, expected in GATES.items():
        if value.get(key) != expected:
            raise AssertionError(f"evaluation gate mismatch: {key}")
    if evidence["evaluation"] != {
        "path": "evaluations/route_a/HCS-C337/2026-09-03.yaml",
        "raw_sha256": EVAL_RAW, "semantic_sha256": EVAL_SEMANTIC,
    }:
        raise AssertionError("nested evaluation carrier mismatch")
    return leaf_count(value)


def check_payload(data: dict) -> int:
    if set(data) != TOP_KEYS:
        raise AssertionError("top-level evidence schema mismatch")
    body = dict(data)
    claimed = body.pop("payload_sha256")
    if type(claimed) is not str or len(claimed) != 64 or canonical_hash(body) != claimed:
        raise AssertionError("evidence payload hash mismatch")
    fixed = {
        "schema": "hcs-c337-integer-kicked-rotor-v1", "candidate_id": "HCS-C337",
        "obstruction_id": "HEN-O321", "source_commit": SOURCE, "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR},
        "model": MODEL, "theorem_contract": THEOREM, "references": REFERENCES,
        "collision_boundary": COLLISIONS, "nonclaims": NONCLAIMS,
        "route_a": {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
                    "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": FLAGS, "parameter_grid": GRID, "boundary_rows": BOUNDARIES,
    }
    for key, expected in fixed.items():
        if data[key] != expected:
            raise AssertionError(f"fixed evidence field mismatch: {key}")
    return 1


def check_parity(rows: list) -> int:
    if type(rows) is not list or len(rows) != 396:
        raise AssertionError("parity row count")
    checks = 0
    index = 0
    for ell in range(1, 13):
        for n in range(-16, 17):
            expected = {"ell": ell, "n": n,
                        "free_phase": 1 if ell % 2 == 0 or n % 2 == 0 else -1,
                        "operator_face": "identity" if ell % 2 == 0 else "half_turn"}
            if rows[index] != expected:
                raise AssertionError(f"parity row {index}")
            index += 1
            checks += 4
    return checks


def check_formal(rows: list) -> int:
    if type(rows) is not list or len(rows) != 435:
        raise AssertionError("formal row count")
    checks = 0
    index = 0
    for q in range(-14, 15):
        for degree in range(15):
            coefficient = bessel_coefficient(q, degree)
            encoded = [qstr(coefficient[0]), qstr(coefficient[1])]
            expected = {"q": q, "degree": degree,
                        "direct_exponential": encoded, "bessel_formula": encoded}
            if rows[index] != expected:
                raise AssertionError(f"formal row {index}")
            index += 1
            checks += 6
    return checks


def check_moments(rows: list) -> int:
    kappas = [Fraction(-3, 2), Fraction(-1), Fraction(-1, 3), Fraction(0),
              Fraction(2, 5), Fraction(1), Fraction(5, 3)]
    if type(rows) is not list or len(rows) != 882:
        raise AssertionError("moment row count")
    checks = 0
    index = 0
    for face in ("even_resonance", "odd_antiresonance"):
        for kappa in kappas:
            for m in range(-3, 4):
                for time in range(9):
                    x = kappa*time if face == "even_resonance" else (kappa if time % 2 else Fraction(0))
                    centered = central(x)
                    raw = raw_from_center(m, centered)
                    expected = {"face": face, "kappa": qstr(kappa), "m": m, "time": time,
                                "effective_bessel_argument": qstr(x),
                                "central_moments_0_to_6": [qstr(v) for v in centered],
                                "raw_moments_0_to_6": [qstr(v) for v in raw],
                                "kinetic_energy": qstr(raw[2]/2)}
                    if rows[index] != expected:
                        raise AssertionError(f"moment row {index}")
                    if parse_q(rows[index]["central_moments_0_to_6"][2]) != x*x/2:
                        raise AssertionError("variance formula")
                    index += 1
                    checks += 23
    return checks


def check_operators(rows: list) -> int:
    if type(rows) is not list or len(rows) != 120:
        raise AssertionError("operator row count")
    checks = 0
    index = 0
    for ell in range(1, 13):
        for time in range(10):
            expected = {
                "ell": ell, "time": time,
                "power_reduction": "K_(t*kappa)" if ell % 2 == 0 else ("I" if time % 2 == 0 else "R K_kappa"),
                "amplitude_phase": "(-i)^(n-m) J_(n-m)(kappa*t)" if ell % 2 == 0 else
                                   ("delta_(n,m)" if time % 2 == 0 else "(-1)^n (-i)^(n-m) J_(n-m)(kappa)"),
            }
            if rows[index] != expected:
                raise AssertionError(f"operator row {index}")
            index += 1
            checks += 4
    return checks


def check_numeric(rows: list) -> int:
    pairs = [("-5/2", "1/7"), ("-1", "2/5"), ("-1/3", "3/7"),
             ("0", "1/2"), ("2/5", "2/3"), ("1", "3/4"), ("7/3", "4/5")]
    if type(rows) is not list or len(rows) != len(pairs):
        raise AssertionError("numeric row count")
    mp.mp.dps = 90
    checks = 0
    for row, (xs, us) in zip(rows, pairs):
        xq, uq = Fraction(xs), Fraction(us)
        x, u = mp.mpf(xq.numerator)/xq.denominator, mp.mpf(uq.numerator)/uq.denominator
        weights = [(q, mp.besselj(q, x)**2) for q in range(-120, 121)]
        norm = mp.fsum(w for _, w in weights)
        char = mp.fsum(w*mp.e**(1j*q*u) for q, w in weights)
        target = mp.besselj(0, 2*x*mp.sin(u/2))
        second = mp.fsum(q*q*w for q, w in weights)
        expected = {"x": xs, "u": us, "cutoff": 120, "precision_digits": 90,
                    "normalization_error": mp.nstr(abs(norm-1), 65),
                    "characteristic_error": mp.nstr(abs(char-target), 65),
                    "second_moment_error": mp.nstr(abs(second-x*x/2), 65),
                    "evidence_status": "NUMERICAL_OBSERVATION"}
        if row != expected:
            raise AssertionError(f"numeric row {xs},{us}")
        checks += 8
    return checks


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C337 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    parser.add_argument("--evaluation", type=Path, default=EVALUATION)
    args = parser.parse_args()
    data = strict_json(args.evidence)
    checks = check_payload(data)
    yaml_leaves = check_evaluation(args.evaluation, data)
    checks += check_parity(data["parity_rows"])
    checks += check_formal(data["formal_kernel_coefficients"])
    checks += check_moments(data["moment_rows"])
    checks += check_operators(data["operator_rows"])
    checks += check_numeric(data["numeric_rows"])
    expected_enumeration = {"parity_rows": 396, "formal_coefficient_rows": 435,
                            "moment_rows": 882, "operator_rows": 120, "numeric_rows": 7,
                            "audited_leaf_count": 22444}
    if data["enumeration"] != expected_enumeration:
        raise AssertionError("enumeration mismatch")
    count_body = copy.deepcopy(data)
    count_body.pop("payload_sha256")
    count_body["enumeration"].pop("audited_leaf_count")
    if leaf_count(count_body) != data["enumeration"]["audited_leaf_count"]:
        raise AssertionError("audited leaf count mismatch")
    checks += data["enumeration"]["audited_leaf_count"] + yaml_leaves
    print(f"C337 independent kicked-rotor checker: PASS {checks} assertions {yaml_leaves} evaluator leaves")


if __name__ == "__main__":
    main()
