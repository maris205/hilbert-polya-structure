#!/usr/bin/env python3
"""Independent fail-closed checker for HCS-C377; imports no producer code."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("c377 checker refuses optimized Python")

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c377_periodic_clm_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C377/2026-09-04.yaml"
PAPER = ROOT / "paper/main.tex"
SOURCE = "f58422d8f03235329863f946654981ecb5d4dc97"
AUTHORITY_SHA = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
YAML_RAW_SHA = "f7a15957460d7ebdf3b18c51044e31899d66fb4d4fba3a7f280c50e2355e8920"
YAML_SEMANTIC_SHA = "9645872c74a85036a2aa42bb9221ab20a7295731034dcd624f8599150424e2d8"
TUPLE = ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"]
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
    "multiplier_rows", "tricomi_rows", "zero_mean_rows", "nonzero_mean_rows", "one_mode_rows",
    "arithmetic_control_rows", "nonzero_profile_rows", "zero_profile_rows", "boundary_rows",
    "section_sha256", "payload_sha256",
}
YAML_TOP_KEYS = {
    "schema", "skill", "skill_version", "candidate_id", "title", "evaluation_date",
    "source_commit", "code_commit", "fixed_epoch", "scope_literal", "evaluator_authority",
    "evaluator_version", "evaluator_authority_sha256", "obstruction_id", "candidate_definition",
    "family", "phase_space", "dynamics", "parameters", "parameter_provenance",
    "arithmetic_origin", "clock", "normalization", "determinant_convention", "orbit_cutoff",
    "precision", "training_data", "forbidden_data", "source_lock", "artifact_paths", "a0", "a1",
    "a2", "a3", "a4", "tuple", "overall_verdict", "adversarial_controls", "claim_boundary",
    "blocking_conditions", "next_smallest_test", "round2_clues", "route_b_invocation_allowed",
    "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role",
    "source_owner_tokens",
}


def unique_object(pairs):
    out = {}
    for key, value in pairs:
        if key in out:
            raise ValueError(f"duplicate JSON key {key}")
        out[key] = value
    return out


def load_json(path: Path):
    return json.loads(path.read_text(), object_pairs_hook=unique_object,
                      parse_constant=lambda token: (_ for _ in ()).throw(ValueError(token)))


class StrictLoader(yaml.SafeLoader):
    pass


StrictLoader.yaml_implicit_resolvers = {
    key: [(tag, regex) for tag, regex in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def strict_mapping(loader, node, deep=False):
    out = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in out:
            raise ValueError("duplicate or non-string YAML key")
        out[key] = loader.construct_object(value_node, deep=deep)
    return out


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, strict_mapping)


def load_yaml(path: Path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors forbidden")
    value = yaml.load(raw, Loader=StrictLoader)
    assert type(value) is dict
    return value


def canonical(value) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def digest(value) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def typed_equal(a, b):
    if type(a) is not type(b):
        return False
    if type(a) is dict:
        return set(a) == set(b) and all(typed_equal(a[k], b[k]) for k in b)
    if type(a) is list:
        return len(a) == len(b) and all(typed_equal(x, y) for x, y in zip(a, b))
    return a == b


def exact(a, b, label):
    if not typed_equal(a, b):
        raise AssertionError(f"typed mismatch at {label}: {a!r} != {b!r}")


def frac(x: Fraction):
    return {"numerator": x.numerator, "denominator": x.denominator}


Z = (Fraction(0), Fraction(0))
O = (Fraction(1), Fraction(0))
I = (Fraction(0), Fraction(1))


def add(a, b): return (a[0] + b[0], a[1] + b[1])
def sub(a, b): return (a[0] - b[0], a[1] - b[1])
def mul(a, b): return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])
def scale(a, c): return (a[0] * c, a[1] * c)
def norm(a): return a[0] * a[0] + a[1] * a[1]


def divide(a, b):
    d = norm(b)
    assert d
    return ((a[0] * b[0] + a[1] * b[1]) / d, (a[1] * b[0] - a[0] * b[1]) / d)


def enc(a): return {"re": frac(a[0]), "im": frac(a[1])}


def polynomial_add(a, b, sign=Fraction(1)):
    out = {k: add(a.get(k, Z), scale(b.get(k, Z), sign)) for k in set(a) | set(b)}
    return {k: v for k, v in out.items() if v != Z}


def convolution(a, b):
    out = {}
    for j, x in a.items():
        for k, y in b.items():
            out[j + k] = add(out.get(j + k, Z), mul(x, y))
    return {k: v for k, v in out.items() if v != Z}


def H(poly):
    out = {}
    for k, value in poly.items():
        out[k] = mul((Fraction(0), Fraction(-1 if k > 0 else 1 if k < 0 else 0)), value)
    return {k: v for k, v in out.items() if v != Z}


def poly_encoding(poly): return [[k, enc(poly[k])] for k in sorted(poly)]


def validate_yaml(path):
    raw = path.read_bytes()
    y = load_yaml(path)
    assert hashlib.sha256(raw).hexdigest() == YAML_RAW_SHA
    assert digest(y) == YAML_SEMANTIC_SHA
    exact(set(y), YAML_TOP_KEYS, "yaml.top keys")
    frozen = {
        "schema": "route-a-evaluation-v0.2.0", "skill": "route-a-evaluator",
        "skill_version": "0.2.0", "candidate_id": "HCS-C377",
        "evaluation_date": "2026-09-04", "source_commit": SOURCE, "fixed_epoch": 1788480000,
        "code_commit": SOURCE,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "evaluator_authority": "flow_systems/skills/route-a-evaluator.md", "evaluator_version": "0.2.0",
        "evaluator_authority_sha256": AUTHORITY_SHA, "obstruction_id": "HEN-O361",
        "artifact_paths": ["results/c377_periodic_clm_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"],
        "tuple": TUPLE, "overall_verdict": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
        "theorem_status": "PROVABLE_AS_STATED_WITH_SIMPLE_POLE_CONDITION_FOR_PROFILE",
        "finite_evidence_role": "exact algebraic regression for formulas proved from the periodic Tricomi identity, never proof by finite sampling",
        "scope_flags": FLAGS,
        "source_owner_tokens": ["DOI:10.1002/cpa.3160380605", "arXiv:2010.01201", "DOI:10.1007/s00332-021-09737-x", "theorem:periodic-CLM-arbitrary-mean-first-pole-clock"],
    }
    for key, expected in frozen.items(): exact(y[key], expected, "yaml." + key)
    exact(y["source_lock"], {
        "object": "inviscid nonadvective periodic CLM with arbitrary conserved mean",
        "arithmetic_origin": "none; Fourier integers are harmonic labels only",
        "clock": "physical PDE time in omega_t=omega*Homega",
        "normalization": "H(e^{ikx})=-i*sign(k)e^{ikx} and z=H(omega-mu)+i*(omega-mu)",
        "determinant_convention": "none",
        "cutoff": "no theorem cutoff; the exact finite ledger sizes are frozen below",
        "precision": "exact Gaussian rationals with no floating-point theorem decision",
        "allowed_data": "source formulas, exact Fourier algebra, exact rational grids, and cited bibliographic metadata",
        "forbidden_data": "prime tables, Riemann-zero tables, target local factors, target divisors, fitted target parameters, and Route B",
    }, "yaml.source_lock")
    statuses = ("PROVED", "PROVED", "STOP_SCOPED", "STOP_SCOPED", "STOP_SCOPED")
    gate_keys = {
        "a0": {"verdict", "evidence_status", "strongest_evidence", "strongest_failure", "arithmetic_controls", "artifacts"},
        "a1": {"verdict", "evidence_status", "strongest_evidence", "strongest_failure", "metrics", "artifacts"},
        "a2": {"verdict", "evidence_status", "strongest_evidence", "strongest_failure", "metrics", "artifacts"},
        "a3": {"verdict", "evidence_status", "strongest_evidence", "strongest_failure", "analytic_structure", "weil_compression", "artifacts"},
        "a4": {"verdict", "evidence_status", "strongest_evidence", "strongest_failure", "metrics", "artifacts"},
    }
    for gate, verdict, status in zip(("a0", "a1", "a2", "a3", "a4"), TUPLE, statuses):
        exact(set(y[gate]), gate_keys[gate], f"yaml.{gate}.keys")
        exact(y[gate]["verdict"], verdict, f"yaml.{gate}.verdict")
        exact(y[gate]["evidence_status"], status, f"yaml.{gate}.status")
        assert type(y[gate]["artifacts"]) is list and y[gate]["artifacts"], f"yaml.{gate}.artifacts"
    controls = y["a0"]["arithmetic_controls"]
    assert type(controls) is list and len(controls) == 4
    exact([row["name"] for row in controls], [
        "composite Fourier modes", "deterministic randomized mode labels",
        "neighboring mean-amplitude parameters", "simpler zero-mean parent",
    ], "yaml.a0.arithmetic_controls.names")
    for index, row in enumerate(controls):
        exact(set(row), {"name", "status", "result", "artifact"}, f"yaml.a0.control[{index}].keys")
        exact(row["status"], "EXECUTED_EXACT", f"yaml.a0.control[{index}].status")
        assert row["result"] and row["artifact"].startswith("results/c377_periodic_clm_evidence.json#")
    exact(set(y["a1"]["metrics"]), {
        "isolated_primitive_orbit_count", "repeated_orbit_ledger_count", "zero_free_solution_period",
        "monodromy_or_stability_multiplier_ledger", "completeness_status",
    }, "yaml.a1.metrics")
    exact(y["a1"]["metrics"]["isolated_primitive_orbit_count"], 0, "yaml.a1.orbit count")
    exact(y["a1"]["metrics"]["repeated_orbit_ledger_count"], 0, "yaml.a1.repeat count")
    exact(set(y["a2"]["metrics"]), {
        "zero_error_train", "zero_error_validation", "zero_error_test", "extra_zero_count",
        "missing_zero_count", "root_count_discrepancy", "cutoff_drift", "precision_drift",
        "control_margin",
    }, "yaml.a2.metrics")
    for key, value in y["a2"]["metrics"].items():
        assert type(value) is str and ("not applicable" in value or key == "precision_drift"), f"yaml.a2.metrics.{key}"
    exact(set(y["a3"]["analytic_structure"]), {
        "conjugation_symmetry", "functional_equation", "gamma_trivial_zero_pole_data",
        "counting_law", "continuation_domain",
    }, "yaml.a3.analytic_structure")
    exact(set(y["a3"]["weil_compression"]), {
        "status", "trace_second_moment_inertia", "common_prime_dynamical_reading",
    }, "yaml.a3.weil_compression")
    exact(set(y["a4"]["metrics"]), {
        "coherent_symplectic_contact_scattering_phase_space", "time_reversal_or_antiunitary_test",
        "same_clock_quantum_lift", "orbit_phase_retention", "hilbert_space_and_operator_domain",
    }, "yaml.a4.metrics")
    adversarial = y["adversarial_controls"]
    exact(set(adversarial), {"controls_used", "proves_too_much_risk", "verdict"}, "yaml.adversarial.keys")
    assert type(adversarial["controls_used"]) is list and len(adversarial["controls_used"]) == 5
    exact(adversarial["verdict"], "PASS_DOES_NOT_CERTIFY_TARGET", "yaml.adversarial.verdict")
    exact(y["claim_boundary"], [
        "exact periodic CLM arbitrary-mean solution and first forward denominator-pole classification only",
        "local vorticity profiles only at simple first poles and a global inverse-time rate only when every simultaneous first pole is simple",
        "no claim after the first pole, for three-dimensional Euler, for target arithmetic, or for global literature novelty",
    ], "yaml.claim_boundary")
    assert type(y["blocking_conditions"]) is list and len(y["blocking_conditions"]) == 4
    assert all(type(item) is str and item for item in y["blocking_conditions"])
    assert type(y["next_smallest_test"]) is str and "independently sourced arithmetic carrier" in y["next_smallest_test"]
    assert type(y["round2_clues"]) is list and len(y["round2_clues"]) == 3
    assert all(type(item) is str and item for item in y["round2_clues"])
    exact(y["route_b_invocation_allowed"], False, "yaml.route_b_invocation_allowed")


def validate_paper(path):
    text = path.read_text()
    title_contract = """\\ifcase\\CRevisionRound
\\title{The Periodic Constantin--Lax--Majda Equation:\\
Exact Arbitrary-Mean Riccati Flow}
\\or
\\title{The Periodic Constantin--Lax--Majda Equation:\\
Exact Arbitrary-Mean Flow and Complete First-Pole Clock}
\\else
\\title{The Periodic Constantin--Lax--Majda Equation:\\
Exact Arbitrary-Mean Flow, First-Pole Clock, and Transverse Profiles}
\\fi"""
    exact(text.count(title_contract), 1, "paper round-title contract")
    exact(text.count("\\ifdefined\\CRevisionRound\\else\\def\\CRevisionRound{2}\\fi"), 1, "paper default round")


def validate_multipliers(rows):
    modes = tuple(range(-128, 0)) + tuple(range(1, 129))
    assert len(rows) == 256
    for index, k in enumerate(modes):
        expected = {"k": k, "multiplier": enc((Fraction(0), Fraction(-1 if k > 0 else 1))), "square_on_nonzero_mode": -1}
        exact(rows[index], expected, f"multiplier[{index}]")


def validate_tricomi(rows):
    assert len(rows) == 1024
    index = 0
    for k in range(1, 33):
        for ell in range(1, 33):
            a = Fraction(k % 5 + 1, ell % 7 + 2)
            b = Fraction(ell % 3 + 1, k % 6 + 2)
            f = {}
            for mode, coefficient in ((k, (0, -a / 2)), (-k, (0, a / 2)), (ell, (b / 2, 0)), (-ell, (b / 2, 0))):
                coefficient = (Fraction(coefficient[0]), Fraction(coefficient[1]))
                f[mode] = add(f.get(mode, Z), coefficient)
            f = {mode: coefficient for mode, coefficient in f.items() if coefficient != Z}
            h = H(f)
            lhs = H(convolution(f, h))
            rhs = polynomial_add(convolution(h, h), convolution(f, f), Fraction(-1))
            rhs = {mode: scale(coefficient, Fraction(1, 2)) for mode, coefficient in rhs.items()}
            assert lhs == rhs
            expected = {
                "k": k, "ell": ell, "sin_coefficient": frac(a), "cos_coefficient": frac(b),
                "mode_count_f": len(f), "mode_count_identity": len(lhs),
                "identity_coefficient_sha256": digest(poly_encoding(lhs)), "residual_nonzero_count": 0,
            }
            exact(rows[index], expected, f"tricomi[{index}]")
            index += 1


def validate_zero_mean(rows):
    values = [Fraction(-2), Fraction(-3, 2), Fraction(-1), Fraction(-1, 2), Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(2)]
    times = [Fraction(1, 4), Fraction(1, 3), Fraction(1, 2), Fraction(2, 3), Fraction(3, 4), Fraction(1), Fraction(4, 3), Fraction(3, 2)]
    assert len(rows) == 512
    index = 0
    for h in values:
        for w in values:
            for t in times:
                denominator = sub((Fraction(2), Fraction(0)), scale((h, w), t))
                z = divide(scale((h, w), 2), denominator)
                d = (2 - t * h) ** 2 + (t * w) ** 2
                expected = {"h0": frac(h), "omega0": frac(w), "t": frac(t), "denominator_abs_squared": frac(d), "z": enc(z), "omega_formula": frac(4 * w / d)}
                exact(rows[index], expected, f"zero_mean[{index}]")
                index += 1


def validate_nonzero(rows):
    values = [Fraction(-2), Fraction(-3, 2), Fraction(-1), Fraction(-1, 2), Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(2)]
    r_values = [Fraction(1, 4), Fraction(1, 2), Fraction(1), Fraction(2)]
    assert len(rows) == 2048
    index = 0
    for mu in values:
        for h in values:
            for f in values:
                z0 = (h, f)
                for r in r_values:
                    e = scale((1 - r * r, 2 * r), Fraction(1, 1) / (1 + r * r))
                    delta = sub(scale(I, 2 * mu), mul(sub(e, O), z0))
                    d = norm(delta)
                    singular = d == 0
                    if singular:
                        z, omega = None, None
                    else:
                        zz = divide(mul(scale(I, 2 * mu), mul(e, z0)), delta)
                        z, omega = enc(zz), frac(mu + zz[1])
                        assert mu + zz[1] == 4 * mu * mu * (mu + f) / d
                    expected = {"mu": frac(mu), "h0": frac(h), "f0": frac(f), "tan_half_angle": frac(r), "e_i_mu_t": enc(e), "delta": enc(delta), "delta_abs_squared": frac(d), "singular": singular, "z": z, "omega": omega}
                    exact(rows[index], expected, f"nonzero[{index}]")
                    index += 1


def validate_one_mode(rows):
    amplitudes = [Fraction(j, 2) for j in tuple(range(-8, 0)) + tuple(range(1, 9))]
    assert len(rows) == 2304
    index = 0
    for integer in range(-4, 5):
        mu = Fraction(integer)
        for amplitude in amplitudes:
            for mode in range(1, 17):
                if mu == 0:
                    regime, hsq = "zero_mean_crossing", amplitude * amplitude
                    time = {"kind": "rational", "value": frac(Fraction(2) / abs(amplitude))}
                elif abs(mu) > abs(amplitude):
                    regime, hsq, time = "zero_free_global_periodic", None, None
                else:
                    hsq = amplitude * amplitude - mu * mu
                    regime = "tangent_zero" if hsq == 0 else "simple_crossing_zeros"
                    time = {"kind": "two_over_abs_mu_times_arccot", "arccot_argument_squared": frac(hsq / (mu * mu)), "arccot_branch": "(0,pi)"}
                expected = {"mu": frac(mu), "amplitude": frac(amplitude), "mode": mode, "regime": regime, "zero_exists": abs(mu) <= abs(amplitude), "maximum_H_on_zero_set_squared": None if hsq is None else frac(hsq), "first_forward_time": time}
                exact(rows[index], expected, f"one_mode[{index}]")
                index += 1


def validate_arithmetic_controls(rows, one_mode, zero_mean):
    """Recompute every A0 control without importing or executing the producer."""
    exact(len(rows), 4, "arithmetic controls count")
    stripped_hashes = {}
    for mode in range(1, 17):
        stripped = [
            {key: value for key, value in row.items() if key != "mode"}
            for row in one_mode if row["mode"] == mode
        ]
        exact(len(stripped), 144, f"control mode {mode} row count")
        stripped_hashes[mode] = digest(stripped)
    exact(len(set(stripped_hashes.values())), 1, "mode-independent stripped clocks")
    permutation = {mode: 1 + ((5 * (mode - 1) + 3) % 16) for mode in range(1, 17)}
    exact(sorted(permutation.values()), list(range(1, 17)), "affine permutation image")
    assert all(stripped_hashes[mode] == stripped_hashes[permutation[mode]] for mode in permutation)
    regime_counts = {}
    for row in one_mode:
        regime_counts[row["regime"]] = regime_counts.get(row["regime"], 0) + 1
        mu = Fraction(row["mu"]["numerator"], row["mu"]["denominator"])
        amplitude = Fraction(row["amplitude"]["numerator"], row["amplitude"]["denominator"])
        exact(row["zero_exists"], abs(mu) <= abs(amplitude), "neighbor threshold")
    expected = [
        {
            "control": "composite_vs_prime_fourier_modes", "status": "PASS_EXACT",
            "prime_modes": [2, 3, 5, 7, 11, 13],
            "composite_modes": [4, 6, 8, 9, 10, 12, 14, 15, 16], "unit_mode": 1,
            "common_stripped_clock_sha256": stripped_hashes[1],
        },
        {
            "control": "deterministic_affine_mode_relabeling", "status": "PASS_EXACT",
            "mapping": [[mode, permutation[mode]] for mode in range(1, 17)],
            "all_stripped_clock_hashes_preserved": True,
        },
        {
            "control": "neighboring_mean_amplitude_grid", "status": "PASS_EXACT",
            "cell_count": len(one_mode), "regime_counts": regime_counts,
            "only_threshold": "abs(mu)=abs(amplitude)",
        },
        {
            "control": "simpler_zero_mean_parent", "status": "PASS_EXACT",
            "cell_count": len(zero_mean), "section_sha256": digest(zero_mean),
            "arithmetic_labels_used": False,
        },
    ]
    exact(rows, expected, "arithmetic controls")


def validate_profiles(nonzero_rows, zero_rows):
    values = [Fraction(-2), Fraction(-1), Fraction(1), Fraction(2)]
    assert len(nonzero_rows) == 1024
    index = 0
    for mu in values:
        for cot in values:
            e = divide((cot, Fraction(1)), (cot, Fraction(-1)))
            zstar = (mu * cot, -mu)
            for hp in values:
                for wp in values:
                    for y in values:
                        lead = sub(mul(scale(I, mu), mul(e, zstar)), scale(mul(sub(e, O), (hp, wp)), y))
                        profile = 4 * mu * mu * wp * y / norm(lead)
                        expected = {"mu": frac(mu), "cot_half_angle": frac(cot), "h_prime": frac(hp), "omega_prime": frac(wp), "y": frac(y), "leading_denominator": enc(lead), "profile": frac(profile), "transverse": True}
                        exact(nonzero_rows[index], expected, f"nonzero_profile[{index}]")
                        index += 1
    assert len(zero_rows) == 256
    index = 0
    for hstar in (Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3)):
        T = Fraction(2) / hstar
        for hp in values:
            for wp in values:
                for y in values:
                    lead = sub((hstar, Fraction(0)), scale((hp, wp), T * y))
                    profile = 4 * wp * y / norm(lead)
                    expected = {"h_star": frac(hstar), "blowup_time": frac(T), "h_prime": frac(hp), "omega_prime": frac(wp), "y": frac(y), "leading_denominator": enc(lead), "profile": frac(profile), "transverse": True}
                    exact(zero_rows[index], expected, f"zero_profile[{index}]")
                    index += 1


def validate(path, evaluation, paper):
    validate_yaml(evaluation)
    validate_paper(paper)
    x = load_json(path)
    exact(set(x), TOP_KEYS, "top keys")
    frozen = {
        "schema": "hcs-c377-evidence-v1", "candidate_id": "HCS-C377", "obstruction_id": "HEN-O361",
        "evaluation_date": "2026-09-04", "source_commit": SOURCE, "fixed_epoch": 1788480000,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": AUTHORITY_SHA},
        "route_a_yaml": {"relative_path": "evaluations/route_a/HCS-C377/2026-09-04.yaml", "raw_sha256": YAML_RAW_SHA, "semantic_sha256": YAML_SEMANTIC_SHA},
        "scope_flags": FLAGS,
        "route_a": {"tuple": TUPLE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False, "theorem_status": "PROVABLE_AS_STATED_WITH_SIMPLE_POLE_CONDITION_FOR_PROFILE"},
        "finite_evidence_role": "exact algebraic regression only; the periodic Hilbert and Riccati proofs establish the infinite theorem",
    }
    for key, expected in frozen.items(): exact(x[key], expected, key)
    exact(x["conventions"], {
        "equation": "omega_t=omega*H(omega) on R/(2*pi*Z)",
        "hilbert": "H(e^(i*k*x))=-i*sign(k)*e^(i*k*x), H(1)=0",
        "decomposition": "mu=mean(omega0), f=omega-mu, h=Hf, z=h+i*f",
        "tricomi": "H(f*Hf)=((Hf)^2-f^2)/2 for real mean-zero f",
        "riccati": "z_t=i*mu*z+z^2/2", "arccot_branch": "arccot:R->(0,pi), strictly decreasing",
    }, "conventions")
    contract_keys = {"mean", "zero_mean", "nonzero_mean", "nonzero_omega", "nonzero_criterion", "zero_criterion", "one_mode", "profile", "boundaries"}
    exact(set(x["theorem_contract"]), contract_keys, "contract keys")
    required_contract_fragments = {
        "mean": "conserved", "zero_mean": "z=2*z0", "nonzero_mean": "e^(i*mu*t)",
        "nonzero_omega": "4*mu^2", "nonzero_criterion": "arccot", "zero_criterion": "Homega0 positive",
        "one_mode": "zero-free", "profile": "simple first pole", "boundaries": "tangent",
    }
    for key, fragment in required_contract_fragments.items(): assert fragment in x["theorem_contract"][key]
    exact(x["finite_grid"], {"hilbert_multiplier_count": 256, "tricomi_polynomial_count": 1024, "zero_mean_mobius_count": 512, "nonzero_mean_mobius_count": 2048, "one_mode_regime_count": 2304, "nonzero_mean_profile_count": 1024, "zero_mean_profile_count": 256, "arithmetic_control_count": 4, "boundary_case_count": 7}, "grid")
    exact(set(x["collision_boundary"]), {"C309", "C324", "C278", "C363"}, "collisions")
    assert len(x["nonclaims"]) == 5 and "no unconditional self-similar rate at tangent or higher-order zeros" in x["nonclaims"]
    assert x["references"][0]["doi"] == "10.1002/cpa.3160380605"
    assert x["references"][1]["arxiv"] == "2010.01201"
    validate_multipliers(x["multiplier_rows"])
    validate_tricomi(x["tricomi_rows"])
    validate_zero_mean(x["zero_mean_rows"])
    validate_nonzero(x["nonzero_mean_rows"])
    validate_one_mode(x["one_mode_rows"])
    validate_arithmetic_controls(x["arithmetic_control_rows"], x["one_mode_rows"], x["zero_mean_rows"])
    validate_profiles(x["nonzero_profile_rows"], x["zero_profile_rows"])
    assert len(x["boundary_rows"]) == 7 and x["boundary_rows"][2]["case"] == "mu_nonzero_tangent_zero"
    sections = ("multiplier_rows", "tricomi_rows", "zero_mean_rows", "nonzero_mean_rows", "one_mode_rows", "arithmetic_control_rows", "nonzero_profile_rows", "zero_profile_rows", "boundary_rows")
    exact(set(x["section_sha256"]), set(sections), "section hashes")
    for section in sections: exact(x["section_sha256"][section], digest(x[section]), "hash." + section)
    payload = x.pop("payload_sha256")
    exact(payload, digest(x), "payload hash")
    return payload


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=EVIDENCE)
    parser.add_argument("--evaluation", type=Path, default=EVALUATION)
    parser.add_argument("--paper", type=Path, default=PAPER)
    args = parser.parse_args()
    try:
        payload = validate(args.input, args.evaluation, args.paper)
    except Exception as exc:
        print(f"C377 checker FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
    print("C377 independent checker PASS: exact Hilbert/Riccati/clock/profile ledgers payload=" + payload)


if __name__ == "__main__":
    main()
