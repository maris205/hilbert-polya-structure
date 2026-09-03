#!/usr/bin/env python3
"""Producer-independent structural and mathematical checker for HCS-C331."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c331_dirac_monopole_evidence.json"
DEFAULT_EVAL = ROOT / "evaluations/route_a/HCS-C331/2026-09-03.yaml"
SOURCE = "5ca65027918c0fce7ef9af82f3faf2e46ed6530c"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EVAL_RAW = "02af8e9102ec43a62b69b5131952ff6e49f83e0ab1826b9a916ed32a953abd4a"
EVAL_SEMANTIC = "03ca40b5c17fa8858846885ae2c4a48375c114b71594550f3896ab4b69779a21"
SPEEDS = (Fraction(1, 2), Fraction(1), Fraction(3, 2))
TIMES = (Fraction(1, 4), Fraction(1, 2), Fraction(1), Fraction(2))
HEAT_CUTOFF = 80
mp.mp.dps = 110


def object_pairs(items):
    out = {}
    for key, value in items:
        if key in out:
            raise ValueError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def strict_json(path: Path):
    return json.loads(path.read_text(), object_pairs_hook=object_pairs,
                      parse_constant=lambda value: (_ for _ in ()).throw(ValueError(value)))


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
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in out:
            raise ValueError("duplicate/non-string YAML key")
        out[key] = loader.construct_object(value_node, deep=deep)
    return out


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def strict_yaml(path: Path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors/aliases forbidden")
    return yaml.load(raw, Loader=UniqueLoader)


def semantic_hash(value) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return semantic_hash(body)


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(v) for v in value.values())
    if type(value) is list:
        return sum(leaves(v) for v in value)
    return 1


def canonical_fraction(text: str) -> Fraction:
    if type(text) is not str or not re.fullmatch(r"-?(?:0|[1-9][0-9]*)(?:/[1-9][0-9]*)?", text):
        raise AssertionError("noncanonical rational syntax")
    value = Fraction(text)
    expected = str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"
    if text != expected:
        raise AssertionError("non-reduced rational")
    return value


def canonical_decimal(text: str) -> mp.mpf:
    if type(text) is not str:
        raise AssertionError("decimal is not a string")
    value = mp.mpf(text)
    if not mp.isfinite(value):
        raise AssertionError("nonfinite decimal")
    expected = mp.nstr(value, 80, strip_zeros=False, min_fixed=-120, max_fixed=120)
    if text != expected:
        raise AssertionError("noncanonical decimal")
    return value


def close_decimal(text: str, expected: mp.mpf) -> None:
    value = canonical_decimal(text)
    if abs(value-expected) > mp.mpf("4e-78")*max(1, abs(expected)):
        raise AssertionError("decimal mismatch")


def mpq(value: Fraction) -> mp.mpf:
    return mp.mpf(value.numerator)/value.denominator


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C331 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_EVAL)
    args = parser.parse_args()
    data = strict_json(args.evidence)
    evaluation = strict_yaml(args.evaluation)
    checks = 0

    if hashlib.sha256(args.evaluation.read_bytes()).hexdigest() != EVAL_RAW:
        raise AssertionError("evaluation raw digest")
    if semantic_hash(evaluation) != EVAL_SEMANTIC:
        raise AssertionError("evaluation semantic digest")
    if payload_hash(data) != data.get("payload_sha256"):
        raise AssertionError("payload digest")
    checks += 3

    top = {"schema", "candidate_id", "obstruction_id", "evaluation_date", "fixed_epoch", "source_commit",
           "scope_literal", "evaluator", "evaluation_lock", "model", "theorem_contract", "classical_rows",
           "spectral_rows", "heat_rows", "chern_rows", "time_reversal_rows", "boundary_atlas", "collision_boundary", "route_a",
           "scope_flags", "nonclaims", "references", "enumeration", "payload_sha256"}
    if type(data) is not dict or set(data) != top:
        raise AssertionError("top-level schema")
    identity = ("hcs-c331-dirac-monopole-v1", "HCS-C331", "HEN-O315", "2026-09-03", 1788393600, SOURCE, SCOPE)
    if tuple(data[key] for key in ("schema", "candidate_id", "obstruction_id", "evaluation_date", "fixed_epoch", "source_commit", "scope_literal")) != identity:
        raise AssertionError("identity")
    expected_evaluator = {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR}
    expected_lock = {"relative_path": "evaluations/route_a/HCS-C331/2026-09-03.yaml", "raw_sha256": EVAL_RAW, "semantic_sha256": EVAL_SEMANTIC}
    if data["evaluator"] != expected_evaluator or data["evaluation_lock"] != expected_lock:
        raise AssertionError("evaluator lock")
    expected_model = {
        "manifold": "unit oriented two-sphere",
        "connection_curvature": "i*(q/2)*dA on the degree-q Hermitian line bundle",
        "classical_equation": "nabla_t xdot=(q/2)*J*xdot with speed squared 2E",
        "quantum_operator": "Friedrichs realization of the nonnegative covariant-Laplacian form on smooth sections",
        "parameters": "q integral and E nonnegative",
    }
    expected_contract = {
        "poincare_vector": "K=x cross xdot+(q/2)x is conserved with K dot x=q/2 and norm squared 2E+q^2/4",
        "positive_energy_orbits": "every E>0 trajectory is a primitive oriented small circle of period 2pi/sqrt(2E+q^2/4)",
        "bundle_connection_bridge": "degree-q line bundles on S^2 are classified by c1 and every unitary connection with curvature i*(q/2)*dA is unitary-gauge equivalent to the standard homogeneous monopole connection because H^1_dR(S^2)=0",
        "operator_realization": "Delta_q is the Friedrichs realization of the nonnegative form integral |nabla s|^2 dA on smooth sections and equals the unique self-adjoint closure of the compact boundaryless elliptic covariant Laplacian",
        "spectrum": "lambda_nq=n(n+abs(q)+1)+abs(q)/2 with multiplicity 2n+abs(q)+1 for every n>=0",
        "heat_trace": "Tr exp(-t Delta_q)=sum_n>=0 (2n+abs(q)+1) exp(-t lambda_nq) for t>0",
        "sign_reversal": "x_q(-t) with reversed initial velocity solves charge -q and traverses the same geometric circle oppositely; bundle conjugation preserves spectrum",
        "boundaries": "q=0 is the round geodesic and spherical-harmonic case; E=0 is stationary; nonintegral q has no frozen global line bundle",
    }
    expected_boundary = [
        {"face": "q=0", "status": "great-circle geodesic flow and ordinary spherical harmonics"},
        {"face": "E=0", "status": "stationary classical points; no primitive orbit is counted"},
        {"face": "q changes sign", "status": "time reversal pairs charge q with charge -q after reversing initial velocity on the same geometric circle; the conjugate bundle has identical spectrum"},
        {"face": "q nonintegral", "status": "the classical equation is local but the frozen global degree-q line bundle does not exist"},
        {"face": "positive energy", "status": "orbits occur in clean continuous circle families and are not isolated hyperbolic cycles"},
        {"face": "n=0", "status": "lowest monopole level has eigenvalue abs(q)/2 and multiplicity abs(q)+1"},
        {"face": "connection gauge class", "status": "fixed curvature on the unique degree-q line bundle determines one unitary gauge class because H^1_dR(S^2)=0; the spectrum is gauge invariant"},
        {"face": "operator domain", "status": "the smooth-section energy form has the Friedrichs realization, equal to the unique self-adjoint elliptic closure on compact boundaryless S^2"},
    ]
    expected_collision = {
        "C313": "round-sphere geodesic and Laplacian dynamics is exactly the q=0 boundary only",
        "C289": "hyperbolic magnetic flow is noncompact and has no monopole line-bundle spectrum",
        "C293": "magnetic Grushin dynamics has a singular cylinder geometry and flux channels",
        "C274": "the Euclidean Penning trap has no Chern-degree quantization on a sphere",
    }
    expected_nonclaims = [
        "No priority is claimed for monopole harmonics, Dirac quantization, or magnetic small circles.",
        "Chern integrality is not a rational-prime or prime-power carrier.",
        "Clean circle families are not an isolated hyperbolic primitive-orbit ledger.",
        "The covariant Laplacian is not asserted to be a Hilbert--Polya operator.",
        "Finite grids are regression receipts and do not prove the all-q and all-n theorem.",
        "No target arithmetic local data, Euler factors, root numbers, automorphy, divisor, functional equation, or zero match is asserted.",
    ]
    expected_refs = [
        {"doi": "10.1098/rspa.1931.0130", "role": "Dirac quantization and integral magnetic charge source"},
        {"doi": "10.1016/0550-3213(76)90143-7", "role": "Wu--Yang global monopole-harmonic construction"},
        {"doi": "10.1103/PhysRevD.14.437", "role": "Wu--Yang classical global monopole dynamics source"},
        {"doi": "10.1103/PhysRevD.16.1018", "role": "further monopole-harmonic properties source"},
    ]
    if (data["model"], data["theorem_contract"], data["boundary_atlas"], data["collision_boundary"], data["nonclaims"], data["references"]) != (
            expected_model, expected_contract, expected_boundary, expected_collision, expected_nonclaims, expected_refs):
        raise AssertionError("static theorem/source boundary")
    if ("classified by c1" not in data["theorem_contract"]["bundle_connection_bridge"] or
            "H^1_dR(S^2)=0" not in data["theorem_contract"]["bundle_connection_bridge"]):
        raise AssertionError("bundle and gauge bridge")
    if ("Friedrichs realization" not in data["theorem_contract"]["operator_realization"] or
            "unique self-adjoint closure" not in data["theorem_contract"]["operator_realization"]):
        raise AssertionError("operator realization bridge")
    if [row["face"] for row in data["boundary_atlas"][-2:]] != ["connection gauge class", "operator domain"]:
        raise AssertionError("bridge boundary coordinates")
    if "Friedrichs realization" not in data["model"]["quantum_operator"]:
        raise AssertionError("model operator domain")
    expected_route = {"tuple": ["A0_WEAK_ARITHMETIC_RELATION", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
                      "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}
    if data["route_a"] != expected_route:
        raise AssertionError("Route-A evidence")
    flag_keys = {"claims_target_arithmetic_local_data", "claims_target_euler_factors", "claims_root_number", "claims_automorphy",
                 "claims_target_divisor_or_counting_law", "claims_target_functional_equation", "claims_target_zero_match",
                 "claims_hilbert_polya_operator", "invokes_route_b"}
    if set(data["scope_flags"]) != flag_keys or any(type(v) is not bool or v for v in data["scope_flags"].values()):
        raise AssertionError("scope flags")
    checks += 19

    eval_top = {"schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch", "scope_literal",
                "evaluator_authority", "evaluator_version", "evaluator_authority_sha256", "obstruction_id", "candidate_definition",
                "family", "phase_space", "dynamics", "parameters", "parameter_provenance", "arithmetic_origin", "clock",
                "normalization", "determinant_convention", "orbit_cutoff", "precision", "training_data", "forbidden_data",
                "artifact_paths", "a0", "a1", "a2", "a3", "a4", "tuple", "overall_verdict", "route_b_invocation_allowed",
                "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role", "source_owner_tokens"}
    if type(evaluation) is not dict or set(evaluation) != eval_top:
        raise AssertionError("evaluation schema")
    layer_keys = {"verdict", "evidence_status", "strongest_evidence", "strongest_failure"}
    if any(type(evaluation[k]) is not dict or set(evaluation[k]) != layer_keys for k in ("a0", "a1", "a2", "a3", "a4")):
        raise AssertionError("evaluation layer schema")
    expected_layers = {
        "a0": {"verdict": "A0_WEAK_ARITHMETIC_RELATION", "evidence_status": "PROVED", "strongest_evidence": "the magnetic charge is half an integral first Chern number", "strongest_failure": "Chern integrality does not intrinsically label rational primes or prime powers"},
        "a1": {"verdict": "A1_WEAK", "evidence_status": "PROVED", "strongest_evidence": "every positive-energy orbit is a primitive small circle with an exact common period", "strongest_failure": "the circles form clean continuous families rather than an isolated hyperbolic primitive ledger"},
        "a2": {"verdict": "A2_FAIL", "evidence_status": "STOP_SCOPED", "strongest_evidence": "an exact heat-trace series exists for the covariant Laplacian", "strongest_failure": "no primitive-orbit Euler product or target determinant is defined"},
        "a3": {"verdict": "A3_FAIL", "evidence_status": "STOP_SCOPED", "strongest_evidence": "the spectrum and heat trace are entire source-local spectral data", "strongest_failure": "no target meromorphic continuation, functional equation, Weil form, or explicit formula is produced"},
        "a4": {"verdict": "A4_NATURAL_QUANTIZATION", "evidence_status": "PROVED", "strongest_evidence": "the degree-q connection has a natural positive self-adjoint covariant Laplacian", "strongest_failure": "its monopole-harmonic spectrum is not a Hilbert-Polya realization of target zeros"},
    }
    if any(evaluation[k] != expected_layers[k] for k in expected_layers):
        raise AssertionError("evaluation layers")
    if (evaluation["schema"], evaluation["candidate_id"], evaluation["obstruction_id"], evaluation["evaluation_date"],
            evaluation["source_commit"], evaluation["fixed_epoch"], evaluation["scope_literal"], evaluation["evaluator_authority"],
            evaluation["evaluator_version"], evaluation["evaluator_authority_sha256"], evaluation["artifact_paths"], evaluation["tuple"],
            evaluation["overall_verdict"], evaluation["route_b_invocation_allowed"], evaluation["scope_flags"], evaluation["theorem_status"],
            evaluation["finite_evidence_role"], evaluation["source_owner_tokens"]) != (
            "route-a-evaluation-v0.2.0", "HCS-C331", "HEN-O315", "2026-09-03", SOURCE, 1788393600, SCOPE,
            "flow_systems/skills/route-a-evaluator.md", "0.2.0", EVALUATOR,
            ["results/c331_dirac_monopole_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"], expected_route["tuple"],
            "ROUTE_A_REJECTED", False, data["scope_flags"], "PROVABLE_AS_STATED", "convention and implementation receipt, not proof",
            ["10.1098/rspa.1931.0130", "10.1016/0550-3213(76)90143-7", "10.1103/PhysRevD.14.437", "10.1103/PhysRevD.16.1018"]):
        raise AssertionError("evaluation semantics")
    checks += 42

    classical = data["classical_rows"]
    expected_coords = [(q, s) for q in range(-6, 7) for s in SPEEDS]
    row_keys = {"row_id", "q", "speed", "energy", "magnetic_charge", "angular_norm_squared", "period", "plane_height", "orbit_radius_squared", "quarter_positions"}
    sample_keys = {"quarter_phase", "x", "y", "z"}
    if type(classical) is not list or len(classical) != len(expected_coords):
        raise AssertionError("classical row count")
    for index, (row, (q, speed)) in enumerate(zip(classical, expected_coords), 1):
        if type(row) is not dict or set(row) != row_keys:
            raise AssertionError("classical row schema")
        b = Fraction(q, 2); energy = speed*speed/2; w2 = speed*speed+b*b
        if (row["row_id"], row["q"], canonical_fraction(row["speed"]), canonical_fraction(row["energy"]),
                canonical_fraction(row["magnetic_charge"]), canonical_fraction(row["angular_norm_squared"]),
                canonical_fraction(row["orbit_radius_squared"])) != (
                f"mag-{index:03d}", q, speed, energy, b, w2, speed*speed/w2):
            raise AssertionError("classical exact fields")
        ss, bb, w = mpq(speed), mpq(b), mp.sqrt(mpq(w2))
        close_decimal(row["period"], 2*mp.pi/w); close_decimal(row["plane_height"], bb/w)
        if type(row["quarter_positions"]) is not list or len(row["quarter_positions"]) != 5:
            raise AssertionError("quarter sample count")
        for phase, sample in enumerate(row["quarter_positions"]):
            if type(sample) is not dict or set(sample) != sample_keys or sample["quarter_phase"] != phase:
                raise AssertionError("quarter sample schema")
            cosine, sine = ((1,0),(0,1),(-1,0),(0,-1),(1,0))[phase]
            c, s = mp.mpf(cosine), mp.mpf(sine)
            expected = (ss*s/w, ss*bb*(1-c)/(w*w), c+bb*bb*(1-c)/(w*w))
            for key, value in zip(("x", "y", "z"), expected):
                close_decimal(sample[key], value)
            vector = [canonical_decimal(sample[key]) for key in ("x", "y", "z")]
            if abs(sum(v*v for v in vector)-1) > mp.mpf("2e-78"):
                raise AssertionError("sphere closure")
            if abs((ss*vector[1]+bb*vector[2])/w-bb/w) > mp.mpf("2e-78"):
                raise AssertionError("Poincare plane closure")
            checks += 8
        checks += 11

    spectral = data["spectral_rows"]
    coords = [(q, n) for q in range(-10, 11) for n in range(17)]
    if type(spectral) is not list or len(spectral) != len(coords):
        raise AssertionError("spectral row count")
    for row, (q, n) in zip(spectral, coords):
        if type(row) is not dict or set(row) != {"q", "n", "eigenvalue", "multiplicity"}:
            raise AssertionError("spectral row schema")
        aq = abs(q); eigenvalue = Fraction(n*(n+aq+1), 1)+Fraction(aq, 2)
        if (row["q"], row["n"], canonical_fraction(row["eigenvalue"]), row["multiplicity"]) != (q, n, eigenvalue, 2*n+aq+1):
            raise AssertionError("spectral identity")
        checks += 5

    heat = data["heat_rows"]
    heat_coords = [(q,t) for q in range(9) for t in TIMES]
    if type(heat) is not list or len(heat) != len(heat_coords):
        raise AssertionError("heat row count")
    for row, (aq, time) in zip(heat, heat_coords):
        if type(row) is not dict or set(row) != {"abs_q", "time", "cutoff", "partial_heat_trace", "first_omitted_eigenvalue"}:
            raise AssertionError("heat schema")
        if (row["abs_q"], canonical_fraction(row["time"]), row["cutoff"]) != (aq, time, HEAT_CUTOFF):
            raise AssertionError("heat coordinate")
        tt = mpq(time); total = mp.mpf("0")
        for n in range(HEAT_CUTOFF+1):
            lam = n*(n+aq+1)+mp.mpf(aq)/2
            total += (2*n+aq+1)*mp.exp(-tt*lam)
        next_lam = (HEAT_CUTOFF+1)*(HEAT_CUTOFF+aq+2)+mp.mpf(aq)/2
        close_decimal(row["partial_heat_trace"], total); close_decimal(row["first_omitted_eigenvalue"], next_lam)
        checks += 6

    chern = data["chern_rows"]
    if type(chern) is not list or len(chern) != 25:
        raise AssertionError("Chern row count")
    for row, q in zip(chern, range(-12, 13)):
        if type(row) is not dict or set(row) != {"q", "flux_over_two_pi", "charge"}:
            raise AssertionError("Chern schema")
        if (row["q"], row["flux_over_two_pi"], canonical_fraction(row["charge"])) != (q, q, Fraction(q,2)):
            raise AssertionError("Chern identity")
        checks += 4

    time_reversal = data["time_reversal_rows"]
    reversal_coords = [(q, speed) for q in range(1, 7) for speed in SPEEDS]
    reversal_keys = {"q", "speed", "original_charge", "paired_charge", "original_tangent_x", "paired_tangent_x", "original_K", "paired_K", "same_geometric_plane", "opposite_traversal", "period_equal"}
    if type(time_reversal) is not list or len(time_reversal) != len(reversal_coords):
        raise AssertionError("time-reversal row count")
    for row, (q, speed) in zip(time_reversal, reversal_coords):
        if type(row) is not dict or set(row) != reversal_keys:
            raise AssertionError("time-reversal schema")
        b = Fraction(q, 2)
        original_k = [Fraction(0), speed, b]
        paired_k = [Fraction(0), -speed, -b]
        if (row["q"], canonical_fraction(row["speed"]), canonical_fraction(row["original_charge"]), canonical_fraction(row["paired_charge"]),
                canonical_fraction(row["original_tangent_x"]), canonical_fraction(row["paired_tangent_x"]),
                [canonical_fraction(x) for x in row["original_K"]], [canonical_fraction(x) for x in row["paired_K"]],
                row["same_geometric_plane"], row["opposite_traversal"], row["period_equal"]) != (
                q, speed, b, -b, speed, -speed, original_k, paired_k, True, True, True):
            raise AssertionError("time-reversal pairing")
        if paired_k != [-x for x in original_k]:
            raise AssertionError("time-reversal plane equivalence")
        checks += 14

    expected_enum = {"classical_rows": 39, "quarter_samples": 195, "spectral_rows": 357, "heat_rows": 36, "chern_rows": 25, "time_reversal_rows": 18}
    if type(data["enumeration"]) is not dict or set(data["enumeration"]) != set(expected_enum)|{"audited_leaf_count"}:
        raise AssertionError("enumeration schema")
    if any(data["enumeration"][k] != v for k,v in expected_enum.items()):
        raise AssertionError("enumeration values")
    leaf_body = dict(data)
    leaf_body.pop("payload_sha256")
    if data["enumeration"]["audited_leaf_count"] != leaves(leaf_body):
        raise AssertionError("leaf count")
    checks += 8
    print(f"C331 independent checker: PASS ({checks} checks)")


if __name__ == "__main__":
    main()
