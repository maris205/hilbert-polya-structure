#!/usr/bin/env python3
"""Producer-independent strict checker for HCS-C357."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction as Q
from pathlib import Path

import yaml
from yaml.tokens import AliasToken, AnchorToken

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT/"results/c357_bilinear_oscillator_evidence.json"
EVALUATION = ROOT/"evaluations/route_a/HCS-C357/2026-09-03.yaml"
SOURCE = "140c8714b74de666d56f441ddfb712026955901a"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EVAL_RAW = "da4bf6ccbc6bb5cdeb60df9c4b215d0a2b6e0fae670cdc0e7c1dfd6c804f74c3"
EVAL_SEMANTIC = "83361e1520848f7a132a1b9b008be1f0bed6844449f4fb99b10871149238f4e4"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
CHECKS = 0

FLAGS = {
    "claims_target_arithmetic_local_data": False, "claims_target_euler_factors": False,
    "claims_root_number": False, "claims_automorphy": False,
    "claims_target_divisor_or_counting_law": False, "claims_target_functional_equation": False,
    "claims_target_zero_match": False, "claims_hilbert_polya_operator": False,
    "invokes_route_b": False,
}
MODEL = {
    "classical_hamiltonian": "H=p^2/2+omega_plus^2*(max(x,0))^2/2+omega_minus^2*(min(x,0))^2/2",
    "classical_equation": "x_dot=p; p_dot=-omega_plus^2*x for x>=0 and -omega_minus^2*x for x<=0",
    "action_angle_regularness": "globally C1 and piecewise analytic on the punctured plane, but not C2 across the seam unless the frequencies agree",
    "quantum_operator": "-one_half*d2_dx2+V on L2(R), defined by its Friedrichs quadratic form",
    "wronskian": "F(lambda)=sqrt(omega_plus)*D_nu_plus'(0)*D_nu_minus(0)+sqrt(omega_minus)*D_nu_minus'(0)*D_nu_plus(0), nu_sign=lambda/omega_sign-1/2",
}
THEOREM = {
    "classical_iff": "all nonzero trajectories are bounded periodic with a common least period iff omega_plus and omega_minus are both positive",
    "period_action": "T=pi*(1/omega_plus+1/omega_minus), J=E*(1/omega_plus+1/omega_minus)/2, and Omega=dE/dJ=2/(1/omega_plus+1/omega_minus)",
    "seam_monodromy": "the two seam-to-seam half-flow matrices are minus identity, so the common-period map and its derivative are identity",
    "action_angle": "the punctured plane has a global C1 piecewise-analytic action-angle chart with dx wedge dp=dtheta wedge dJ and theta_dot=Omega; it is not C2 across the seam unless the frequencies agree",
    "quantum": "for positive frequencies the Friedrichs operator is self-adjoint with compact resolvent and simple spectrum, and lambda is an eigenvalue iff the parabolic-cylinder interface Wronskian vanishes",
    "boundaries": "equal frequency, zero energy, one-sided zero stiffness, and the free particle are stated separately",
}
BOUNDARIES = {
    "zero_energy": "for positive frequencies E=0 is only the origin equilibrium",
    "equal_frequency": "omega_plus=omega_minus is the ordinary harmonic oscillator; the Wronskian zeros recover lambda_n=omega*(n+1/2)",
    "one_sided_zero": "a flat half-axis is a continuum of rest equilibria and every other orbit reaching it escapes linearly; quantum compact resolvent is lost and essential spectrum begins at zero",
    "free": "both frequencies zero give the free particle, all p=0 states are equilibria, and nonzero momentum is unbounded",
    "seam": "the force is continuous and globally Lipschitz, while its derivative jumps unless the frequencies agree",
    "smoothness": "the action-angle map is not claimed globally C-infinity across the seam",
}
REFERENCES = [
    {"identifier": "10.1088/0305-4470/38/27/007", "role": "primary study of quantum spectra of isochronous potentials including the asymmetric parabolic well"},
    {"identifier": "https://dlmf.nist.gov/12.2", "role": "NIST authority for the parabolic-cylinder equation, values, derivatives, and Wronskians"},
    {"identifier": "10.1090/gsm/157", "role": "authoritative self-adjoint one-dimensional Schrodinger-operator framework"},
]
COLLISIONS = {
    "C212": "affine impact dynamics resets velocity and has a separate flight-time roof",
    "C232": "Duffing is smooth, amplitude-dependent, and has separatrix chambers",
    "C238": "Coulomb friction is dissipative Filippov dynamics with finite capture",
    "C252": "the relay oscillator changes a discrete guard state and owns an attracting hybrid cycle",
}
NONCLAIMS = [
    "No priority claim is made for asymmetric parabolic isochrony or parabolic-cylinder matching.",
    "Classical isochrony does not imply an equally spaced asymmetric quantum spectrum.",
    "The interface Wronskian is a source spectral equation, not a target determinant.",
    "No target arithmetic datum, Euler factor, root number, automorphy, target divisor, functional equation, target-zero match, Hilbert-Polya operator, or Route-B input is claimed.",
]
FREQUENCIES = [
    (Q(1), Q(1)), (Q(1), Q(2)), (Q(2), Q(3)), (Q(1, 2), Q(3, 2)),
    (Q(3), Q(5)), (Q(2, 3), Q(4, 3)), (Q(5, 2), Q(7, 2)),
    (Q(4), Q(1)), (Q(3, 4), Q(5, 4)), (Q(7), Q(2)),
]
ENERGIES = (Q(1, 8), Q(1, 2), Q(1), Q(3, 2), Q(2), Q(5))
QFREQ = (Q(1, 2), Q(1), Q(2), Q(5, 2), Q(3))

TOP_KEYS = {"schema", "candidate_id", "obstruction_id", "evaluation_date", "source_commit", "fixed_epoch", "scope_literal", "evaluator", "evaluation_lock", "model", "theorem_contract", "boundary_atlas", "references", "collision_boundary", "nonclaims", "route_a", "scope_flags", "frequency_grid", "energy_grid", "classical_rows", "quantum_equal_frequency_rows", "zero_stiffness_rows", "enumeration", "payload_sha256"}
CLASSICAL_KEYS = {"frequency_index", "energy_index", "omega_plus", "omega_minus", "energy", "k_plus", "k_minus", "amplitude_plus_squared", "amplitude_minus_squared", "seam_speed_squared", "right_time_over_pi", "left_time_over_pi", "period_over_pi", "action", "action_over_energy", "loop_area_over_pi", "Omega", "Omega_times_period_over_pi", "right_half_matrix", "left_half_matrix", "full_monodromy", "right_time_fraction", "left_time_fraction"}
QUANTUM_KEYS = {"frequency_index", "level", "omega", "lambda", "nu_plus", "nu_minus", "parity", "vanishing_interface_factor", "wronskian_zero"}
BOUNDARY_KEYS = {"omega_plus", "omega_minus", "flat_side", "classical", "quantum_compact_resolvent", "essential_lower_edge"}


def need(condition, label):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def unique(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError("duplicate JSON key")
        out[key] = value
    return out


class UniqueLoader(yaml.SafeLoader):
    pass


def construct_mapping(loader, node, deep=False):
    out = {}
    for kn, vn in node.value:
        key = loader.construct_object(kn, deep=deep)
        if type(key) is not str or key in out:
            raise ValueError("non-string or duplicate YAML key")
        out[key] = loader.construct_object(vn, deep=deep)
    return out


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, construct_mapping)


def parse_yaml(raw):
    for token in yaml.scan(raw):
        if isinstance(token, (AliasToken, AnchorToken)):
            raise ValueError("YAML alias")
    value = yaml.load(raw, Loader=UniqueLoader)
    if type(value) is not dict:
        raise ValueError("YAML root")
    return value


def q(value):
    need(type(value) is str, "rational type")
    out = Q(value)
    canonical = str(out.numerator) if out.denominator == 1 else f"{out.numerator}/{out.denominator}"
    need(value == canonical, "canonical rational")
    return out


def leaves(value):
    if type(value) is dict:
        return sum(leaves(v) for v in value.values())
    if type(value) is list:
        return sum(leaves(v) for v in value)
    return 1


def multiply(a, b):
    return [[sum(Q(a[i][k])*Q(b[k][j]) for k in range(2)) for j in range(2)] for i in range(2)]


def check_evaluation(raw):
    need(sha(raw) == EVAL_RAW, "evaluation raw")
    value = parse_yaml(raw)
    need(sha(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()) == EVAL_SEMANTIC, "evaluation semantic")
    keys = {"schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch", "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256", "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters", "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention", "orbit_cutoff", "precision", "training_data", "forbidden_data", "artifact_paths", "a0", "a1", "a2", "a3", "a4", "tuple", "overall_verdict", "route_b_invocation_allowed", "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role", "source_owner_tokens"}
    need(set(value) == keys, "evaluation keys")
    need((value["candidate_id"], value["obstruction_id"], value["evaluation_date"]) == ("HCS-C357", "HEN-O341", "2026-09-03"), "evaluation identity")
    need(value["source_commit"] == SOURCE and value["fixed_epoch"] == EPOCH and value["scope_literal"] == SCOPE, "evaluation provenance")
    need(value["evaluator_authority"] == "flow_systems/skills/route-a-evaluator.md" and value["evaluator_version"] == "0.2.0" and value["evaluator_authority_sha256"] == EVALUATOR, "evaluation authority")
    need(value["artifact_paths"] == ["results/c357_bilinear_oscillator_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"], "paths")
    verdicts = ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"]
    statuses = ["PROVED", "PROVED", "STOP_SCOPED", "STOP_SCOPED", "PROVED"]
    for i, key in enumerate(("a0", "a1", "a2", "a3", "a4")):
        need(set(value[key]) == {"verdict", "evidence_status", "strongest_evidence", "strongest_failure"}, f"{key} keys")
        need(value[key]["verdict"] == verdicts[i] and value[key]["evidence_status"] == statuses[i], f"{key} lock")
    need(value["tuple"] == verdicts and value["overall_verdict"] == "ROUTE_A_REJECTED", "tuple")
    need(value["route_b_invocation_allowed"] is False and value["scope_flags"] == FLAGS, "firewall")
    need(value["theorem_status"] == "PROVABLE_AS_STATED" and len(value["finite_evidence_role"]) > 80, "status")
    need(value["source_owner_tokens"] == ["10.1088/0305-4470/38/27/007", "https://dlmf.nist.gov/12.2", "10.1090/gsm/157"], "sources")


def check(path, evaluation):
    check_evaluation(evaluation.read_bytes())
    data = json.loads(path.read_text(), object_pairs_hook=unique,
                      parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))
    need(set(data) == TOP_KEYS, "top keys")
    claimed = data["payload_sha256"]; need(type(claimed) is str and len(claimed) == 64, "hash type")
    payload = dict(data); payload.pop("payload_sha256")
    need(claimed == sha(json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()), "payload hash")
    need(data["schema"] == "hcs-c357-bilinear-oscillator-evidence-v1", "schema")
    need((data["candidate_id"], data["obstruction_id"], data["evaluation_date"]) == ("HCS-C357", "HEN-O341", "2026-09-03"), "identity")
    need(data["source_commit"] == SOURCE and data["fixed_epoch"] == EPOCH and data["scope_literal"] == SCOPE, "provenance")
    need(data["evaluator"] == {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR}, "evaluator")
    need(data["evaluation_lock"] == {"relative_path": "evaluations/route_a/HCS-C357/2026-09-03.yaml", "raw_sha256": EVAL_RAW, "semantic_sha256": EVAL_SEMANTIC}, "evaluation lock")
    need(data["model"] == MODEL and data["theorem_contract"] == THEOREM, "model theorem")
    need(data["boundary_atlas"] == BOUNDARIES and data["references"] == REFERENCES, "boundary refs")
    need(data["collision_boundary"] == COLLISIONS and data["nonclaims"] == NONCLAIMS, "collisions")
    need(data["route_a"] == {"tuple": ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"], "overall": "ROUTE_A_REJECTED", "route_b": False}, "route")
    need(data["scope_flags"] == FLAGS, "flags")
    need(data["frequency_grid"] == [[str(a.numerator) if a.denominator == 1 else f"{a.numerator}/{a.denominator}", str(b.numerator) if b.denominator == 1 else f"{b.numerator}/{b.denominator}"] for a, b in FREQUENCIES], "frequency grid")
    need([q(x) for x in data["energy_grid"]] == list(ENERGIES), "energy grid")
    rows = data["classical_rows"]; need(type(rows) is list and len(rows) == len(FREQUENCIES)*len(ENERGIES), "classical count")
    coordinates = []
    for row in rows:
        need(set(row) == CLASSICAL_KEYS, "classical keys")
        fi, ei = row["frequency_index"], row["energy_index"]
        need(type(fi) is int and type(ei) is int and 0 <= fi < len(FREQUENCIES) and 0 <= ei < len(ENERGIES), "coordinates")
        coordinates.append((fi, ei))
        wp, wm = FREQUENCIES[fi]; E = ENERGIES[ei]
        need([q(row[k]) for k in ("omega_plus", "omega_minus", "energy")] == [wp, wm, E], "values")
        total = 1/wp+1/wm; Omega = 2/total; J = E/Omega
        expected = {
            "k_plus": wp*wp, "k_minus": wm*wm,
            "amplitude_plus_squared": 2*E/(wp*wp), "amplitude_minus_squared": 2*E/(wm*wm),
            "seam_speed_squared": 2*E, "right_time_over_pi": 1/wp, "left_time_over_pi": 1/wm,
            "period_over_pi": total, "action": J, "action_over_energy": 1/Omega,
            "loop_area_over_pi": 2*J, "Omega": Omega, "Omega_times_period_over_pi": Q(2),
            "right_time_fraction": (1/wp)/total, "left_time_fraction": (1/wm)/total,
        }
        for key, value in expected.items():
            need(q(row[key]) == value, f"classical {key}")
        for key in ("right_half_matrix", "left_half_matrix", "full_monodromy"):
            need(type(row[key]) is list and len(row[key]) == 2 and all(type(x) is list and len(x) == 2 for x in row[key]), "matrix shape")
            for r in row[key]:
                for value in r:
                    q(value)
        need([[q(v) for v in r] for r in row["right_half_matrix"]] == [[-1, 0], [0, -1]], "right half")
        need([[q(v) for v in r] for r in row["left_half_matrix"]] == [[-1, 0], [0, -1]], "left half")
        need([[q(v) for v in r] for r in row["full_monodromy"]] == multiply(row["left_half_matrix"], row["right_half_matrix"]) == [[1, 0], [0, 1]], "monodromy")
        need(q(row["right_time_fraction"])+q(row["left_time_fraction"]) == 1, "time fractions")
    need(coordinates == [(i, j) for i in range(len(FREQUENCIES)) for j in range(len(ENERGIES))], "classical enumeration")
    qrows = data["quantum_equal_frequency_rows"]; need(type(qrows) is list and len(qrows) == len(QFREQ)*17, "quantum count")
    qcoords = []
    for row in qrows:
        need(set(row) == QUANTUM_KEYS, "quantum keys")
        fi, n = row["frequency_index"], row["level"]; need(type(fi) is int and type(n) is int and 0 <= fi < len(QFREQ) and 0 <= n < 17, "quantum coordinate")
        qcoords.append((fi, n)); omega = QFREQ[fi]
        need(q(row["omega"]) == omega and q(row["lambda"]) == omega*(Q(n)+Q(1, 2)), "quantum energy")
        need(q(row["nu_plus"]) == n and q(row["nu_minus"]) == n, "quantum nu")
        need(row["parity"] == ("even" if n%2 == 0 else "odd"), "parity")
        need(row["vanishing_interface_factor"] == ("D_prime" if n%2 == 0 else "D_value"), "zero factor")
        need(row["wronskian_zero"] is True, "wronskian zero")
    need(qcoords == [(i, n) for i in range(len(QFREQ)) for n in range(17)], "quantum enumeration")
    brows = data["zero_stiffness_rows"]; need(type(brows) is list and len(brows) == 3, "boundary count")
    expected_b = [("0", "1", "right", "rest continuum on x>=0 plus linear escape"), ("1", "0", "left", "rest continuum on x<=0 plus linear escape"), ("0", "0", "both", "free particle")]
    for row, expected in zip(brows, expected_b):
        need(set(row) == BOUNDARY_KEYS, "boundary keys")
        need((row["omega_plus"], row["omega_minus"], row["flat_side"], row["classical"]) == expected, "boundary values")
        need(row["quantum_compact_resolvent"] is False and q(row["essential_lower_edge"]) == 0, "boundary quantum")
    enum = data["enumeration"]
    need(set(enum) == {"frequency_pairs", "energies", "classical_rows", "quantum_equal_frequency_rows", "zero_stiffness_rows", "leaf_count_without_payload_hash"}, "enumeration keys")
    expected_enum = {"frequency_pairs": len(FREQUENCIES), "energies": len(ENERGIES), "classical_rows": len(rows), "quantum_equal_frequency_rows": len(qrows), "zero_stiffness_rows": len(brows), "leaf_count_without_payload_hash": leaves(payload)-6}
    need(enum == expected_enum, "enumeration")
    print(f"C357 independent bilinear-oscillator checker: PASS ({CHECKS} checks)")


def main():
    if sys.flags.optimize:
        raise RuntimeError("C357 checker refuses optimized Python")
    parser = argparse.ArgumentParser(); parser.add_argument("--evidence", type=Path, default=EVIDENCE); parser.add_argument("--evaluation", type=Path, default=EVALUATION)
    args = parser.parse_args(); check(args.evidence, args.evaluation)


if __name__ == "__main__":
    main()
