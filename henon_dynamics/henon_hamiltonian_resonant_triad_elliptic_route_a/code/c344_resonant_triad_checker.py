#!/usr/bin/env python3
"""Producer-independent strict theorem/evidence checker for HCS-C344."""
from __future__ import annotations

import argparse
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
EVIDENCE = ROOT / "results/c344_resonant_triad_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C344/2026-09-03.yaml"
SOURCE = "1af63b945e19b5f94ac1cb76f93af5ac66d3d562"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EVAL_RAW = "6cad36134e348ea562025fc6a8dd91003962fe5c50944b4b52d2611d8526ff7b"
EVAL_SEMANTIC = "65c82147824ba8cfdbf1f4dea119bfab26ab6c1df5f36939087e244fc2161ac0"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
CHECKS = 0

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
PAIRS = [
    (Fraction(1), Fraction(2)), (Fraction(1), Fraction(3)),
    (Fraction(2), Fraction(3)), (Fraction(2), Fraction(5)),
    (Fraction(3), Fraction(5)), (Fraction(3, 2), Fraction(7, 2)),
    (Fraction(4, 3), Fraction(5, 2)), (Fraction(5, 4), Fraction(9, 4)),
    (Fraction(2), Fraction(2)), (Fraction(3), Fraction(3)),
    (Fraction(5), Fraction(8)), (Fraction(8), Fraction(5)),
]
LEVELS = [Fraction(1), Fraction(2), Fraction(3)]
TOP_KEYS = {
    "schema", "candidate_id", "obstruction_id", "source_commit", "fixed_epoch",
    "scope_literal", "evaluator", "evaluation", "model", "theorem_contract",
    "references", "collision_boundary", "nonclaims", "route_a", "scope_flags",
    "parameter_grid", "regular_rows", "zero_hamiltonian_rows",
    "relative_equilibrium_rows", "boundary_atlas", "enumeration", "payload_sha256",
}
REGULAR_KEYS = {
    "n1", "n2", "level", "h_sign", "h_squared", "witness_x", "root_intervals",
    "roots_decimal", "root_sum", "root_pair_sum", "root_product",
    "jacobi_modulus_squared", "intensity_period", "phase_increment_1",
    "phase_increment_2", "closure_rule",
}
ZERO_KEYS = {
    "n1", "n2", "face", "modulus_squared", "intensity_formula",
    "amplitude_formula", "intensity_period", "full_state_period", "endpoint",
}
RELATIVE_KEYS = {
    "n1", "n2", "h_sign", "critical_x", "maximum_abs_h", "omega1", "omega2",
    "omega3", "critical_equation", "phase_lock", "closure_classification",
}
MODEL = {
    "hamiltonian": "H=z1*z2*conjugate(z3)+conjugate(z1)*conjugate(z2)*z3",
    "poisson_bracket": "{f,g}=-i*sum(df_dzj*dg_dconjugatezj-df_dconjugatezj*dg_dzj)",
    "equations": "i*z1'=conjugate(z2)*z3; i*z2'=conjugate(z1)*z3; i*z3'=z1*z2",
    "invariants": "N1=abs(z1)^2+abs(z3)^2; N2=abs(z2)^2+abs(z3)^2; H",
    "reduction": "x=abs(z3)^2; x'^2=4*x*(N1-x)*(N2-x)-H^2",
    "domain": "all z in complex three-space with source interaction time",
}
THEOREM = {
    "global_integrability": "the flow is global and H,N1,N2 are generically independent commuting integrals",
    "regular_solution": "every nonzero-H regular intensity is an sn-squared oscillation between the two accessible roots",
    "phase_return": "two complete third-kind integrals reconstruct the torus phases and both rationality conditions are necessary and sufficient for full-state closure",
    "zero_h_boundary": "unequal invariants give full period twice the intensity period; equal invariants give a heteroclinic separatrix",
    "double_root_boundary": "maximal absolute H gives a relative equilibrium whose full state closes exactly at rational frequency ratio",
    "scope_boundary": "no quantized domain theorem, full quantum spectrum, arithmetic orbit ledger, target determinant, or Route-B result is claimed",
}
REFERENCES = [
    {"identifier": "10.1103/PhysRev.127.1918", "role": "primary coupled optical three-wave amplitude source"},
    {"identifier": "10.1109/JRPROC.1956.275145", "role": "primary Manley-Rowe energy-relation source"},
    {"identifier": "10.1103/RevModPhys.51.275", "role": "authoritative primary resonant three-wave treatment"},
]
COLLISIONS = {
    "C211": "Hamiltonian Lotka-Volterra period annulus, not a complex resonant wave triad with two phase returns",
    "C230": "open Toda Lax scattering, not a cubic three-mode wave interaction",
    "C235": "cyclic population dynamics with mutation, not a canonical complex Hamiltonian triad",
    "C256": "KdV traveling-wave cnoidal profiles, not full finite-dimensional complex-amplitude dynamics",
}
NONCLAIMS = [
    "No priority claim is made for three-wave equations, Manley-Rowe relations, or elliptic integration.",
    "Intensity recurrence alone is not claimed to imply recurrence of the full complex state.",
    "The formal bosonic analogy is not a proved self-adjoint quantization or a complete quantum spectrum.",
    "No target arithmetic datum, Euler factor, root number, automorphy, target divisor, functional equation, target-zero match, Hilbert-Polya operator, or Route-B input is claimed.",
]
BOUNDARIES = {
    "origin_and_axes": "the origin and each complex coordinate axis are equilibrium families",
    "n1_or_n2_zero": "if either Manley-Rowe invariant vanishes the state lies on an equilibrium axis",
    "h_zero_unequal": "smooth chart crossings; intensity period is half the full complex-state period",
    "h_zero_equal": "sech/sech/tanh heteroclinic with infinite period",
    "maximal_abs_h": "double accessible root and two-frequency relative equilibrium",
    "coupling_zero": "identity flow; every nonzero real coupling is reduced by time rescaling and sign reversal",
    "complex_conjugation": "complex conjugation paired with time reversal preserves the geometric intensity orbit",
    "formal_quantization": "bosonic cubic interaction is only a formal hint; no operator-domain or spectral theorem is asserted",
}


def need(condition: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def unique(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


class UniqueLoader(yaml.SafeLoader):
    pass


def construct_mapping(loader, node, deep=False):
    mapping = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in mapping:
            raise ValueError("non-string or duplicate YAML key")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping)


def parse_yaml(raw: bytes):
    for token in yaml.scan(raw):
        if isinstance(token, (AliasToken, AnchorToken)):
            raise ValueError("YAML aliases and anchors forbidden")
    value = yaml.load(raw, Loader=UniqueLoader)
    if type(value) is not dict:
        raise ValueError("YAML root must be mapping")
    return value


def canonical_yaml_hash(value) -> str:
    return sha(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(child) for child in value.values())
    if type(value) is list:
        return sum(leaves(child) for child in value)
    return 1


def q(value: str) -> Fraction:
    need(type(value) is str, "rational is not a string")
    result = Fraction(value)
    canonical = str(result.numerator) if result.denominator == 1 else f"{result.numerator}/{result.denominator}"
    need(value == canonical, "noncanonical rational string")
    return result


def qmp(value: Fraction) -> mp.mpf:
    return mp.mpf(value.numerator)/value.denominator


def dec(value: mp.mpf) -> str:
    return mp.nstr(value, 60, strip_zeros=False, min_fixed=0, max_fixed=0)


def decimal_value(value: str) -> mp.mpf:
    need(type(value) is str and len(value) >= 20, "decimal type/precision")
    got = mp.mpf(value)
    need(mp.isfinite(got), "nonfinite decimal")
    need(dec(got) == value, "noncanonical decimal")
    return got


def close_decimal(stored: str, expected: mp.mpf, label: str) -> None:
    got = decimal_value(stored)
    need(abs(got-expected) <= mp.mpf("2e-58")*max(1, abs(expected)), label)


def cubic(x: Fraction, n1: Fraction, n2: Fraction, h2: Fraction) -> Fraction:
    return 4*x*(n1-x)*(n2-x)-h2


def bisect_root(n1: Fraction, n2: Fraction, h2: Fraction,
                left: Fraction, right: Fraction) -> mp.mpf:
    lo, hi = qmp(left), qmp(right)
    hh = qmp(h2)
    f = lambda x: 4*x*(qmp(n1)-x)*(qmp(n2)-x)-hh
    flo, fhi = f(lo), f(hi)
    need(flo*fhi < 0, "decimal bisection signs")
    for _ in range(320):
        middle = (lo+hi)/2
        fm = f(middle)
        if flo*fm < 0:
            hi, fhi = middle, fm
        else:
            lo, flo = middle, fm
    return (lo+hi)/2


EVAL_KEYS = {
    "schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch",
    "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256",
    "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters",
    "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention",
    "orbit_cutoff", "precision", "training_data", "forbidden_data", "artifact_paths", "a0", "a1",
    "a2", "a3", "a4", "tuple", "overall_verdict", "route_b_invocation_allowed",
    "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role", "source_owner_tokens",
}
EVAL_FIXED = {
    "schema": "route-a-evaluation-v0.2.0",
    "candidate_id": "HCS-C344",
    "title": "Hamiltonian resonant-triad elliptic reduction and phase-return theorem",
    "evaluation_date": "2026-09-03", "source_commit": SOURCE, "fixed_epoch": EPOCH,
    "scope_literal": SCOPE, "evaluator_authority": "flow_systems/skills/route-a-evaluator.md",
    "evaluator_version": "0.2.0", "evaluator_authority_sha256": EVALUATOR,
    "obstruction_id": "HEN-O328",
    "candidate_definition": "the autonomous complex three-wave Hamiltonian with cubic interaction z1 z2 conjugate-z3 plus its conjugate",
    "family": "finite-dimensional resonant wave interaction and elliptic integrable Hamiltonian dynamics",
    "phase_space": "complex three-space with its canonical real symplectic structure",
    "dynamics": "i z1-dot equals conjugate-z2 z3, i z2-dot equals conjugate-z1 z3, and i z3-dot equals z1 z2",
    "parameters": "initial complex amplitudes only; a nonzero real coupling is removed by source-time rescaling",
    "parameter_provenance": "source wave amplitudes and coupling only, never target-fitted",
    "arithmetic_origin": "none", "clock": "source physical interaction time",
    "normalization": "the cubic Hamiltonian has coefficient one and H equals two times the real part of z1 z2 conjugate-z3",
    "determinant_convention": "no orbit Euler product, transfer determinant, or target determinant is defined",
    "orbit_cutoff": "all-time analytic theorem on every initial state; finite invariant grids are implementation receipts only",
    "precision": "exact rational polynomial identities plus deterministic high-precision elliptic-integral regression",
    "training_data": "none",
    "forbidden_data": "target arithmetic local data, Euler factors, root numbers, automorphy, target divisor or functional equation, target zeros, Hilbert-Polya operators, and Route B",
    "artifact_paths": ["results/c344_resonant_triad_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"],
    "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
    "overall_verdict": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
    "route_b_lock_reason": "the missing arithmetic carrier, primitive orbit dictionary, and target determinant cannot be supplied by elliptic integrability or a formal bosonic analogy",
    "scope_flags": FLAGS, "theorem_status": "PROVABLE_AS_STATED",
    "finite_evidence_role": "invariant, cubic-root, elliptic-period, phase-integral, zero-Hamiltonian, relative-equilibrium, and implementation receipt only; analytic arguments prove the continuum theorem",
    "source_owner_tokens": ["10.1103/PhysRev.127.1918", "10.1109/JRPROC.1956.275145", "10.1103/RevModPhys.51.275"],
}
GATES = {
    "a0": {"verdict": "A0_FAIL", "evidence_status": "PROVED",
           "strongest_evidence": "the Hamiltonian and both Manley-Rowe invariants are exact source-local quantities",
           "strongest_failure": "the model has no intrinsic rational-prime, prime-power, logarithmic-prime, or local arithmetic carrier"},
    "a1": {"verdict": "A1_WEAK", "evidence_status": "PROVED",
           "strongest_evidence": "every regular reduced intensity orbit is an explicit Jacobi elliptic oscillation and full-state closure has two exact phase-return conditions",
           "strongest_failure": "the closed states occur on continuously selected resonance loci rather than forming a canonical isolated primitive-orbit ledger"},
    "a2": {"verdict": "A2_FAIL", "evidence_status": "STOP_SCOPED",
           "strongest_evidence": "the reduced cubic curve and its real root chamber are completely explicit",
           "strongest_failure": "no primitive-orbit Euler product or Fredholm determinant with arithmetic repetition weights is constructed"},
    "a3": {"verdict": "A3_FAIL", "evidence_status": "STOP_SCOPED",
           "strongest_evidence": "all regular and degenerate source dynamics are controlled analytically",
           "strongest_failure": "there is no target analytic continuation, functional equation, divisor, counting law, or Weil-form compression"},
    "a4": {"verdict": "A4_FORMAL_HINT", "evidence_status": "PROVED",
           "strongest_evidence": "the source system is Hamiltonian and admits a formal three-boson cubic interaction quantization with finite number-sector reductions",
           "strongest_failure": "no self-adjoint domain theorem or same-clock unitary spectral identification is proved, and no Hilbert-Polya operator is claimed"},
}


def check_evaluation(raw: bytes, value) -> None:
    need(sha(raw) == EVAL_RAW, "evaluation raw hash")
    need(canonical_yaml_hash(value) == EVAL_SEMANTIC, "evaluation semantic hash")
    need(set(value) == EVAL_KEYS, "evaluation exact keys")
    for key, expected in EVAL_FIXED.items():
        need(value.get(key) == expected, f"evaluation fixed field {key}")
    for key, expected in GATES.items():
        need(value.get(key) == expected, f"evaluation gate {key}")


def check_regular(rows) -> None:
    need(type(rows) is list and len(rows) == len(PAIRS)*len(LEVELS)*2, "regular row count")
    expected_coords = [(a, b, level, sign) for a, b in PAIRS for level in LEVELS for sign in (-1, 1)]
    mp.mp.dps = 100
    for row, (n1, n2, level, sign) in zip(rows, expected_coords):
        need(type(row) is dict and set(row) == REGULAR_KEYS, "regular exact row keys")
        need((q(row["n1"]), q(row["n2"]), q(row["level"]), row["h_sign"]) ==
             (n1, n2, level, sign), "regular coordinates/order")
        need(type(row["h_sign"]) is int and row["h_sign"] in (-1, 1), "Hamiltonian sign")
        nminus, nplus = min(n1, n2), max(n1, n2)
        xw = nminus/2
        h2 = level*xw*(n1-xw)*(n2-xw)
        need(q(row["h_squared"]) == h2 and q(row["witness_x"]) == xw, "regular level construction")
        need(q(row["root_sum"]) == n1+n2, "Vieta sum")
        need(q(row["root_pair_sum"]) == n1*n2, "Vieta pair sum")
        need(q(row["root_product"]) == h2/4, "Vieta product")
        intervals = row["root_intervals"]
        need(type(intervals) is list and len(intervals) == 3, "three root intervals")
        rational_intervals = []
        for interval in intervals:
            need(type(interval) is list and len(interval) == 2, "root interval shape")
            left, right = q(interval[0]), q(interval[1])
            need(left < right and cubic(left, n1, n2, h2)*cubic(right, n1, n2, h2) < 0,
                 "exact root bracket")
            need(right-left < max(Fraction(1), nplus)/2**80, "root bracket precision")
            rational_intervals.append((left, right))
        need(Fraction(0) < rational_intervals[0][0] < rational_intervals[0][1] < xw,
             "first root chamber")
        need(xw < rational_intervals[1][0] < rational_intervals[1][1] < nminus,
             "second root chamber")
        need(nplus < rational_intervals[2][0] < rational_intervals[2][1], "third root chamber")
        roots = [bisect_root(n1, n2, h2, *interval) for interval in rational_intervals]
        for stored, expected in zip(row["roots_decimal"], roots):
            close_decimal(stored, expected, "root decimal")
        r1, r2, r3 = roots
        modulus = (r2-r1)/(r3-r1)
        period = 2*mp.ellipk(modulus)/mp.sqrt(r3-r1)
        close_decimal(row["jacobi_modulus_squared"], modulus, "Jacobi modulus")
        close_decimal(row["intensity_period"], period, "intensity period")
        h = sign*mp.sqrt(qmp(h2))
        expected_deltas = []
        for invariant in (n1, n2):
            n = (r2-r1)/(qmp(invariant)-r1)
            expected_deltas.append(-h*mp.ellippi(n, modulus)/(
                mp.sqrt(r3-r1)*(qmp(invariant)-r1)))
        close_decimal(row["phase_increment_1"], expected_deltas[0], "first phase increment")
        close_decimal(row["phase_increment_2"], expected_deltas[1], "second phase increment")
        need(row["closure_rule"] ==
             "full state closes iff both phase increments divided by 2*pi are rational",
             "two-phase closure rule")


def check_zero(rows) -> None:
    need(type(rows) is list and len(rows) == len(PAIRS), "zero-H row count")
    mp.mp.dps = 100
    for row, (n1, n2) in zip(rows, PAIRS):
        need(type(row) is dict and set(row) == ZERO_KEYS, "zero-H exact row keys")
        need((q(row["n1"]), q(row["n2"])) == (n1, n2), "zero-H coordinates/order")
        if n1 == n2:
            need(row == {
                "n1": row["n1"], "n2": row["n2"], "face": "equal_invariant_separatrix",
                "modulus_squared": "1", "intensity_formula": "N*tanh(sqrt(N)*(t-t0))^2",
                "amplitude_formula": "sqrt(N)*(sech,sech,-i*tanh) up to the two torus phases",
                "intensity_period": None, "full_state_period": None,
                "endpoint": "heteroclinic between opposite points of the z3-axis equilibrium family",
            }, "equal-invariant separatrix row")
        else:
            nminus, nplus = min(n1, n2), max(n1, n2)
            need(row["face"] == "unequal_invariant_periodic_transfer", "unequal H-zero face")
            need(q(row["modulus_squared"]) == nminus/nplus, "H-zero modulus")
            need(row["intensity_formula"] ==
                 "Nminus*sn(sqrt(Nplus)*(t-t0)|Nminus/Nplus)^2", "H-zero intensity formula")
            need(row["amplitude_formula"] ==
                 "cn/dn/(-i sn) with the smaller invariant assigned to cn and sn", "H-zero amplitude formula")
            period = 2*mp.ellipk(qmp(nminus/nplus))/mp.sqrt(qmp(nplus))
            close_decimal(row["intensity_period"], period, "H-zero intensity period")
            close_decimal(row["full_state_period"], 2*period, "H-zero full period")
            need(row["endpoint"] == "both zero-amplitude chart crossings are smooth in the complex variables",
                 "H-zero chart crossing")


def check_relative(rows) -> None:
    need(type(rows) is list and len(rows) == 2*len(PAIRS), "relative row count")
    mp.mp.dps = 100
    coordinates = [(n1, n2, sign) for n1, n2 in PAIRS for sign in (-1, 1)]
    for row, (n1, n2, sign) in zip(rows, coordinates):
        need(type(row) is dict and set(row) == RELATIVE_KEYS, "relative exact row keys")
        need((q(row["n1"]), q(row["n2"]), row["h_sign"]) == (n1, n2, sign),
             "relative coordinates/order")
        s, product = qmp(n1+n2), qmp(n1*n2)
        xstar = (s-mp.sqrt(s*s-3*product))/3
        hmax = 2*mp.sqrt(xstar*(qmp(n1)-xstar)*(qmp(n2)-xstar))
        h = sign*hmax
        omega1 = -h/(2*(qmp(n1)-xstar))
        omega2 = -h/(2*(qmp(n2)-xstar))
        omega3 = -h/(2*xstar)
        close_decimal(row["critical_x"], xstar, "critical intensity")
        close_decimal(row["maximum_abs_h"], hmax, "maximal H")
        close_decimal(row["omega1"], omega1, "relative omega1")
        close_decimal(row["omega2"], omega2, "relative omega2")
        close_decimal(row["omega3"], omega3, "relative omega3")
        need(abs(omega3-omega1-omega2) < mp.mpf("1e-80"), "phase-lock identity")
        need(row["critical_equation"] == "3*x^2-2*(N1+N2)*x+N1*N2=0", "critical equation")
        need(row["phase_lock"] == "omega3=omega1+omega2", "phase lock text")
        if n1 == n2:
            expected = "periodic symmetric relative equilibrium with omega1=omega2 and omega3=omega1+omega2"
        elif (n1, n2) in ((Fraction(5), Fraction(8)), (Fraction(8), Fraction(5))):
            expected = "periodic rational-frequency witness with absolute omega1/omega2 equal to 2 or 1/2"
            need(abs(abs(omega1/omega2) - (2 if n1 < n2 else mp.mpf("0.5"))) < mp.mpf("1e-80"),
                 "rational relative-frequency witness")
        else:
            expected = "full state closes iff omega1/omega2 is rational; no generic closure is asserted"
        need(row["closure_classification"] == expected, "relative closure classification")


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C344 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    parser.add_argument("--evaluation", type=Path, default=EVALUATION)
    args = parser.parse_args()
    raw = args.evidence.read_bytes()
    data = json.loads(raw, object_pairs_hook=unique,
                      parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    need(type(data) is dict and set(data) == TOP_KEYS, "evidence exact top keys")
    payload = dict(data)
    claimed_hash = payload.pop("payload_sha256")
    need(type(claimed_hash) is str and len(claimed_hash) == 64, "payload hash type")
    need(claimed_hash == sha(json.dumps(payload, sort_keys=True, separators=(",", ":"),
                                        ensure_ascii=False).encode()), "payload hash")
    evaluation_raw = args.evaluation.read_bytes()
    evaluation_value = parse_yaml(evaluation_raw)
    check_evaluation(evaluation_raw, evaluation_value)
    fixed = {
        "schema": "hcs-c344-resonant-triad-v1", "candidate_id": "HCS-C344",
        "obstruction_id": "HEN-O328", "source_commit": SOURCE, "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR},
        "evaluation": {"path": "evaluations/route_a/HCS-C344/2026-09-03.yaml",
                       "raw_sha256": EVAL_RAW, "semantic_sha256": EVAL_SEMANTIC},
        "model": MODEL, "theorem_contract": THEOREM, "references": REFERENCES,
        "collision_boundary": COLLISIONS, "nonclaims": NONCLAIMS,
        "route_a": {"tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
                    "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": FLAGS,
        "parameter_grid": {"pairs": [[str(a.numerator) if a.denominator == 1 else f"{a.numerator}/{a.denominator}",
                                         str(b.numerator) if b.denominator == 1 else f"{b.numerator}/{b.denominator}"] for a, b in PAIRS],
                           "regular_levels": ["1", "2", "3"], "hamiltonian_signs": [-1, 1],
                           "root_bracket_iterations": 84, "decimal_digits": 60,
                           "evidence_role": "exact and high-precision finite receipt, not proof by sampling"},
        "boundary_atlas": BOUNDARIES,
    }
    for key, expected in fixed.items():
        need(data[key] == expected, f"fixed evidence field {key}")
    check_regular(data["regular_rows"])
    check_zero(data["zero_hamiltonian_rows"])
    check_relative(data["relative_equilibrium_rows"])
    need(data["enumeration"] == {
        "regular_rows": 72, "zero_hamiltonian_rows": 12,
        "relative_equilibrium_rows": 24, "audited_leaf_count": 2126,
    }, "enumeration exact values")
    need(leaves(payload) == data["enumeration"]["audited_leaf_count"], "audited leaf count")
    need(all(value is False for value in data["scope_flags"].values()), "scope flags")
    print(f"C344 independent resonant-triad checker: PASS {CHECKS} assertions")


if __name__ == "__main__":
    main()
