#!/usr/bin/env python3
"""Independent fail-closed checker for HCS-C376; imports no producer code."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("c376 checker refuses optimized Python")

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c376_flat_magnetic_torus_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C376/2026-09-04.yaml"
SOURCE = "f58422d8f03235329863f946654981ecb5d4dc97"
AUTHORITY_SHA = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
YAML_RAW_SHA = "f1a920fc208186a02d4a5cafcf5cefbb554825699e503b7061dc8b0b29306287"
YAML_SEMANTIC_SHA = "9580d0e0d6fc1664cb701964c8bf5c82db6faecb1ec69c044dd50797f4990915"
TUPLE = ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"]
FLAGS = {
    key: False
    for key in (
        "claims_target_arithmetic_local_data", "claims_target_euler_factors", "claims_root_number",
        "claims_automorphy", "claims_target_divisor_or_counting_law",
        "claims_target_functional_equation", "claims_target_zero_match",
        "claims_hilbert_polya_operator", "invokes_route_b",
    )
}
TOP_KEYS = {
    "schema", "candidate_id", "obstruction_id", "evaluation_date", "source_commit", "fixed_epoch",
    "scope_literal", "evaluator", "route_a_yaml", "conventions", "theorem_contract", "finite_grid",
    "collision_boundary", "nonclaims", "references", "scope_flags", "route_a", "finite_evidence_role",
    "classical_rows", "flux_rows", "landau_rows", "translation_rows", "heat_rows", "determinant_rows",
    "revival_rows", "boundary_rows", "section_sha256", "payload_sha256",
}
YAML_TOP_KEYS = {
    "schema", "skill", "skill_version", "candidate_id", "title", "evaluation_date", "source_commit", "code_commit",
    "fixed_epoch", "scope_literal", "evaluator_authority", "evaluator_version",
    "evaluator_authority_sha256", "obstruction_id", "candidate_definition", "family",
    "phase_space", "dynamics", "parameters", "parameter_provenance", "arithmetic_origin",
    "clock", "normalization", "determinant_convention", "orbit_cutoff", "precision",
    "training_data", "forbidden_data", "artifact_paths", "a0", "a1", "a2", "a3", "a4",
    "tuple", "overall_verdict", "adversarial_controls", "claim_boundary",
    "blocking_conditions", "next_smallest_test", "round2_clues",
    "route_b_invocation_allowed", "route_b_lock_reason", "scope_flags", "theorem_status",
    "finite_evidence_role", "source_owner_tokens",
}


def unique_object(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"duplicate JSON key {key}")
        out[key] = value
    return out


def load_json(path: Path):
    return json.loads(
        path.read_text(), object_pairs_hook=unique_object,
        parse_constant=lambda token: (_ for _ in ()).throw(ValueError(f"nonfinite {token}")),
    )


class StrictLoader(yaml.SafeLoader):
    pass


StrictLoader.yaml_implicit_resolvers = {
    key: [(tag, regex) for tag, regex in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def strict_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge key forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in result:
            raise ValueError("duplicate or non-string YAML key")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, strict_mapping)


def load_yaml(path: Path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors and aliases forbidden")
    value = yaml.load(raw, Loader=StrictLoader)
    if type(value) is not dict:
        raise TypeError("YAML root must be a mapping")
    return value


def canonical(value) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def digest(value) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def typed_equal(actual, expected):
    if type(actual) is not type(expected):
        return False
    if type(actual) is dict:
        return set(actual) == set(expected) and all(typed_equal(actual[k], expected[k]) for k in expected)
    if type(actual) is list:
        return len(actual) == len(expected) and all(typed_equal(a, b) for a, b in zip(actual, expected))
    return actual == expected


def exact(actual, expected, label):
    if not typed_equal(actual, expected):
        raise AssertionError(f"typed mismatch at {label}: {actual!r} != {expected!r}")


def frac(value: Fraction):
    return {"numerator": value.numerator, "denominator": value.denominator}


def validate_yaml(path: Path):
    raw = path.read_bytes()
    value = load_yaml(path)
    assert hashlib.sha256(raw).hexdigest() == YAML_RAW_SHA
    assert digest(value) == YAML_SEMANTIC_SHA
    exact(set(value), YAML_TOP_KEYS, "yaml.top_keys")
    frozen = {
        "schema": "route-a-evaluation-v0.2.0",
        "skill": "route-a-evaluator",
        "skill_version": "0.2.0",
        "candidate_id": "HCS-C376",
        "evaluation_date": "2026-09-04",
        "source_commit": SOURCE,
        "code_commit": SOURCE,
        "fixed_epoch": 1788480000,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "evaluator_authority": "flow_systems/skills/route-a-evaluator.md",
        "evaluator_version": "0.2.0",
        "evaluator_authority_sha256": AUTHORITY_SHA,
        "obstruction_id": "HEN-O360",
        "artifact_paths": ["results/c376_flat_magnetic_torus_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"],
        "tuple": TUPLE,
        "overall_verdict": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
        "theorem_status": "PROVABLE_AS_STATED",
        "finite_evidence_role": "exact regression and reproducibility receipt for formulas proved analytically, never proof by finite sampling",
        "source_owner_tokens": [
            "DOI:10.1016/j.aop.2008.07.006", "arXiv:0807.0630", "arXiv:quant-ph/0007055",
            "DOI:10.1007/s00220-025-05267-9", "theorem:flat-torus-Bochner-Landau-determinant-double-revival",
        ],
        "scope_flags": FLAGS,
    }
    for key, expected in frozen.items():
        exact(value[key], expected, f"yaml.{key}")
    expected_statuses = ("PROVED", "PROVED", "PROVED", "STOP_SCOPED", "PROVED")
    gates = ("a0", "a1", "a2", "a3", "a4")
    for gate, verdict, status in zip(gates, TUPLE, expected_statuses):
        expected_keys = {"verdict", "evidence_status", "strongest_evidence", "strongest_failure", "metrics", "artifacts"}
        if gate == "a0":
            expected_keys.add("arithmetic_controls")
        exact(set(value[gate]), expected_keys, f"yaml.{gate}.keys")
        exact(value[gate]["verdict"], verdict, f"yaml.{gate}.verdict")
        exact(value[gate]["evidence_status"], status, f"yaml.{gate}.status")
        assert type(value[gate]["metrics"]) is dict and value[gate]["metrics"]
        assert type(value[gate]["artifacts"]) is list and len(value[gate]["artifacts"]) >= 2
        assert all(type(item) is str and item for item in value[gate]["artifacts"])
    controls = value["a0"]["arithmetic_controls"]
    assert type(controls) is list and len(controls) >= 3 and len(set(controls)) == len(controls)
    assert all(type(item) is str and item for item in controls)
    exact(set(value["adversarial_controls"]), {"controls_used", "proves_too_much_risk", "verdict"}, "yaml.adversarial.keys")
    assert type(value["adversarial_controls"]["controls_used"]) is list and len(value["adversarial_controls"]["controls_used"]) >= 3
    exact(value["adversarial_controls"]["verdict"], "STOP_SCOPED", "yaml.adversarial.verdict")
    assert type(value["claim_boundary"]) is str and value["claim_boundary"]
    assert type(value["blocking_conditions"]) is list and len(value["blocking_conditions"]) >= 3
    assert type(value["next_smallest_test"]) is str and value["next_smallest_test"]
    assert type(value["round2_clues"]) is list and len(value["round2_clues"]) >= 2
    for key in (
        "title", "candidate_definition", "family", "phase_space", "dynamics", "parameters",
        "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention",
        "orbit_cutoff", "precision", "training_data", "forbidden_data", "route_b_lock_reason",
    ):
        assert type(value[key]) is str and value[key]


def validate_classical(rows):
    b_values = [Fraction(1, 2), Fraction(2, 3), Fraction(1), Fraction(3, 2)]
    q_values = [(Fraction(0), Fraction(0)), (Fraction(1, 5), Fraction(1, 7)), (Fraction(2, 5), Fraction(3, 7)), (Fraction(4, 5), Fraction(6, 7))]
    p_values = [(Fraction(x), Fraction(y)) for x in (-2, -1, 1, 2) for y in (-2, -1, 1, 2)]
    assert len(rows) == 256
    index = 0
    for b in b_values:
        for qx, qy in q_values:
            for px, py in p_values:
                row = rows[index]
                center = (qx - py / b, qy + px / b)
                exact(row["abs_B"], frac(b), f"classical[{index}].B")
                exact(row["q0_lift"], [frac(qx), frac(qy)], f"classical[{index}].q")
                exact(row["p0"], [frac(px), frac(py)], f"classical[{index}].p")
                exact(row["energy"], frac((px * px + py * py) / 2), f"classical[{index}].energy")
                exact(row["center"], [frac(center[0]), frac(center[1])], f"classical[{index}].center")
                exact(row["least_period_over_pi"], frac(2 / b), f"classical[{index}].period")
                exact(row["return_derivative"], "identity_on_T(T2xR2)", f"classical[{index}].return")
                states = ((px, py), (-py, px), (-px, -py), (py, -px), (px, py))
                assert len(row["quarter_states"]) == 5
                for k, (pkx, pky) in enumerate(states):
                    state = row["quarter_states"][k]
                    qkx, qky = center[0] + pky / b, center[1] - pkx / b
                    expected = {
                        "quarter": k,
                        "q_lift": [frac(qkx), frac(qky)],
                        "p": [frac(pkx), frac(pky)],
                        "center": [frac(qkx - pky / b), frac(qky + pkx / b)],
                    }
                    exact(state, expected, f"classical[{index}].quarter[{k}]")
                index += 1


def validate_flux(rows):
    areas = [Fraction(1), Fraction(3, 2), Fraction(2), Fraction(5, 2)]
    fluxes = tuple(range(-64, 0)) + tuple(range(1, 65))
    assert len(rows) == 128
    for index, (row, n) in enumerate(zip(rows, fluxes)):
        area = areas[index % 4]
        expected = {
            "N": n, "area": frac(area), "B_over_2pi": frac(Fraction(n, 1) / area),
            "chern_integral": n, "degree_abs": abs(n),
            "chirality": "positive" if n > 0 else "negative_conjugate",
            "landau_multiplicity": abs(n), "flat_holonomy_changes_spectrum": False,
        }
        exact(row, expected, f"flux[{index}]")


def validate_landau(rows):
    assert len(rows) == 16512
    index = 0
    for n_flux in tuple(range(-64, 0)) + tuple(range(1, 65)):
        for level in range(129):
            expected = {
                "N": n_flux, "level": level,
                "energy_over_abs_B": frac(Fraction(2 * level + 1, 2)),
                "multiplicity": abs(n_flux), "raising_gap_over_abs_B": 1,
            }
            exact(rows[index], expected, f"landau[{index}]")
            index += 1


def validate_translations(rows):
    assert len(rows) == 4160
    index = 0
    for flux_sign in (-1, 1):
        for order in range(1, 65):
            for j in range(order):
                expected = {
                    "flux_sign": flux_sign,
                    "ordered_positive_division_vectors": ["(Lx/M,0)", "(0,Ly/M)"],
                    "order": order, "basis_index": j, "U_image_index": (j + 1) % order,
                    "V_phase_exponent_mod_order": (-flux_sign * j) % order,
                    "UV_over_VU_phase_exponent_mod_order": flux_sign % order,
                    "U_power_order_is_identity": True, "V_power_order_is_identity": True,
                }
                exact(rows[index], expected, f"translation[{index}]")
                index += 1


def validate_boundaries(rows):
    expected = [
        {"case": "B_nonzero_E_positive", "classical": "common least period 2*pi/abs(B)", "quantum": "requires integral flux"},
        {"case": "B_nonzero_E_zero", "classical": "zero-section equilibria", "quantum": "positive lowest Landau energy"},
        {"case": "integral_flux_positive", "classical": "unchanged", "quantum": "degree N line bundle and positive chirality"},
        {"case": "integral_flux_negative", "classical": "opposite orientation", "quantum": "complex-conjugate chirality and abs(N) multiplicity"},
        {"case": "abs_N_one", "classical": "unchanged", "quantum": "one-dimensional magnetic-translation representation"},
        {"case": "nonintegral_flux", "classical": "well-defined twisted flow", "quantum": "no global Hermitian line bundle with stipulated curvature"},
        {
            "case": "B_zero",
            "classical": "q(t)=q0+t*p modulo (Lx*Z direct_sum Ly*Z)",
            "closure_criterion": "there exists t>0 with p_x*t in Lx*Z and p_y*t in Ly*Z",
            "nonaxial_criterion": "p_y*Lx/(p_x*Ly) is rational",
            "x_axis_nonzero": "closed with least period Lx/abs(p_x)",
            "y_axis_nonzero": "closed with least period Ly/abs(p_y)",
            "zero_velocity": "stationary with no positive least period",
            "nonaxial_irrational_normalized_slope": "dense orbit",
            "quantum": "flat-holonomy shifted torus Laplacian; Landau theorem not continued",
        },
    ]
    exact(rows, expected, "boundary rows")


def validate_heat(rows):
    assert len(rows) == 1024
    index = 0
    for order in range(1, 65):
        for denominator in range(2, 18):
            q = Fraction(1, denominator)
            expected = {
                "abs_N": order, "q": frac(q),
                "trace_divided_by_sqrt_q": frac(Fraction(order, 1) / (1 - q)),
                "tail_ratio": frac(q),
            }
            exact(rows[index], expected, f"heat[{index}]")
            index += 1


def validate_determinants(rows):
    assert len(rows) == 64
    for index, order in enumerate(range(1, 65)):
        expected = {
            "abs_N": order, "zeta_at_zero": 0,
            "zeta_prime_at_zero_log2_coefficient": frac(Fraction(-order, 2)),
            "determinant_base": 2, "determinant_exponent": frac(Fraction(order, 2)),
            "independent_of_abs_B": True,
        }
        exact(rows[index], expected, f"determinant[{index}]")


def validate_revivals(rows):
    assert len(rows) == 129
    for level, row in enumerate(rows):
        expected = {
            "level": level, "phase_at_classical_period": "-1", "phase_at_double_period": "+1",
            "relative_phase_exponent_at_scalar_period": level,
            "identity_exponent_at_double_period": 2 * level + 1,
        }
        exact(row, expected, f"revival[{level}]")


def validate(path: Path, evaluation: Path):
    validate_yaml(evaluation)
    evidence = load_json(path)
    exact(set(evidence), TOP_KEYS, "top keys")
    frozen = {
        "schema": "hcs-c376-evidence-v1", "candidate_id": "HCS-C376", "obstruction_id": "HEN-O360",
        "evaluation_date": "2026-09-04", "source_commit": SOURCE, "fixed_epoch": 1788480000,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": AUTHORITY_SHA},
        "route_a_yaml": {"relative_path": "evaluations/route_a/HCS-C376/2026-09-04.yaml", "raw_sha256": YAML_RAW_SHA, "semantic_sha256": YAML_SEMANTIC_SHA},
        "scope_flags": FLAGS,
        "route_a": {"tuple": TUPLE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False, "theorem_status": "PROVABLE_AS_STATED"},
        "finite_evidence_role": "exact regression receipt only; analytic proofs establish every theorem",
    }
    for key, expected in frozen.items():
        exact(evidence[key], expected, key)
    conventions = {
        "torus": "R2/(Lx*Z direct_sum Ly*Z), A=Lx*Ly",
        "classical_symplectic": "dx wedge dp_x + dy wedge dp_y + B dx wedge dy",
        "classical_hamiltonian": "(p_x^2+p_y^2)/2",
        "rotation": "J(px,py)=(-py,px), pdot=B*J*p, center=q+J*p/B",
        "quantum_curvature": "F_nabla=-i*B*dx wedge dy",
        "kinetic_commutator": "[Pi_x,Pi_y]=i*B",
        "quantum_hamiltonian": "H_B=(Pi_x^2+Pi_y^2)/2=(1/2)nabla_star_nabla",
        "magnetic_translation_orientation": "U,V lift the fixed ordered positive vectors (Lx/M,0),(0,Ly/M), so UV=zeta_M^sgn(N)*VU",
        "zeta_determinant": "exp(-zeta_H_prime(0)) over the full positive spectrum",
    }
    exact(evidence["conventions"], conventions, "conventions")
    contract = {
        "classical": "for B nonzero and E positive every orbit has least period 2*pi/abs(B); returns are maximally clean",
        "integrality": "a global curvature line bundle exists iff N=B*A/(2*pi) is an integer",
        "spectrum": "E_n=abs(B)*(n+1/2), each with multiplicity abs(N), independent of flat holonomy",
        "translations": "for fixed ordered positive division vectors each eigenspace carries UV=zeta_M^sgn(N)*VU and the signed order-abs(N) irreducible clock-shift representation",
        "heat": "Tr(exp(-beta*H_B))=abs(N)*exp(-beta*abs(B)/2)/(1-exp(-beta*abs(B)))",
        "zeta": "zeta_H(s)=abs(N)*abs(B)^(-s)*zeta(s,1/2)",
        "determinant": "det_zeta(H_B)=2^(abs(N)/2)",
        "revival": "least scalar time is 2*pi/abs(B) with propagator -I; least identity time is 4*pi/abs(B)",
        "boundaries": "E=0, sign B, abs(N)=1, nonintegral flux, and the exact lattice-normalized B=0 closure faces are separated",
    }
    exact(evidence["theorem_contract"], contract, "theorem_contract")
    exact(evidence["finite_grid"], {
        "classical_quarter_return_cell_count": 256, "flux_case_count": 128,
        "landau_label_cell_count": 16512, "translation_basis_cell_count": 4160,
        "heat_cell_count": 1024, "determinant_control_count": 64,
        "revival_level_count": 129, "boundary_case_count": 7,
    }, "finite_grid")
    assert set(evidence["collision_boundary"]) == {"C274", "C289", "C293", "C331", "C371", "C156"}
    assert len(evidence["nonclaims"]) == 5 and "no Hilbert-Polya operator and no Route B" in evidence["nonclaims"]
    assert [row.get("arxiv") for row in evidence["references"][:2]] == ["0807.0630", "quant-ph/0007055"]
    assert evidence["references"][0]["doi"] == "10.1016/j.aop.2008.07.006"
    assert evidence["references"][1]["doi"] == "10.1023/A:1004115827959"
    assert evidence["references"][2]["doi"] == "10.1007/s00220-025-05267-9"
    validate_classical(evidence["classical_rows"])
    validate_flux(evidence["flux_rows"])
    validate_landau(evidence["landau_rows"])
    validate_translations(evidence["translation_rows"])
    validate_heat(evidence["heat_rows"])
    validate_determinants(evidence["determinant_rows"])
    validate_revivals(evidence["revival_rows"])
    validate_boundaries(evidence["boundary_rows"])
    sections = (
        "classical_rows", "flux_rows", "landau_rows", "translation_rows", "heat_rows",
        "determinant_rows", "revival_rows", "boundary_rows",
    )
    exact(set(evidence["section_sha256"]), set(sections), "section hashes")
    for section in sections:
        exact(evidence["section_sha256"][section], digest(evidence[section]), f"hash.{section}")
    claimed = evidence.pop("payload_sha256")
    exact(claimed, digest(evidence), "payload hash")
    return claimed


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=EVIDENCE)
    parser.add_argument("--evaluation", type=Path, default=EVALUATION)
    args = parser.parse_args()
    try:
        payload = validate(args.input, args.evaluation)
    except Exception as exc:
        print(f"C376 checker FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
    print("C376 independent checker PASS: exact ledgers and frozen contracts payload=" + payload)


if __name__ == "__main__":
    main()
