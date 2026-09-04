#!/usr/bin/env python3
"""Independent fail-closed checker for HCS-C373; imports no producer code."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("c373 checker refuses optimized Python")

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c373_higgs_oscillator_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C373/2026-09-04.yaml"
SOURCE = "c6553f02d928c6aa05400ded57746869a85f0238"
AUTHORITY_SHA = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
YAML_RAW_SHA = "e093905d686c2d32e46cbaa8d711f61c460f21c35f79106be778d222fa85a541"
YAML_SEMANTIC_SHA = "daae2b83c7c1e7cdbc54ec7751e699d04dd9781854403de19364305fc63c13f5"
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
    "classical_rows", "quantum_state_rows", "quantum_level_rows", "rational_revival_rows",
    "irrational_revival_rows", "boundary_rows", "section_sha256", "payload_sha256",
}
YAML_KEYS = {
    "schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch",
    "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256",
    "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters",
    "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention",
    "orbit_cutoff", "precision", "training_data", "forbidden_data", "artifact_paths", "a0", "a1",
    "a2", "a3", "a4", "tuple", "overall_verdict", "route_b_invocation_allowed",
    "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role", "source_owner_tokens",
}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key {key}")
        result[key] = value
    return result


def load_json(path: Path):
    return json.loads(
        path.read_text(), object_pairs_hook=unique_object,
        parse_constant=lambda token: (_ for _ in ()).throw(ValueError(f"nonfinite {token}")),
    )


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
        raise AssertionError(f"typed value mismatch at {label}")


def exact_keys(actual, expected, label):
    if type(actual) is not dict or set(actual) != set(expected):
        raise AssertionError(f"key set mismatch at {label}")


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


def validate_yaml(path: Path):
    raw = path.read_bytes()
    value = load_yaml(path)
    assert hashlib.sha256(raw).hexdigest() == YAML_RAW_SHA
    assert digest(value) == YAML_SEMANTIC_SHA
    exact_keys(value, YAML_KEYS, "evaluation YAML")
    frozen = {
        "schema": "route-a-evaluation-v0.2.0", "candidate_id": "HCS-C373",
        "title": "Hemispherical Higgs oscillator classical action, quantum spectrum, and exact revival criterion",
        "evaluation_date": "2026-09-04", "source_commit": SOURCE, "fixed_epoch": 1788480000,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "evaluator_authority": "flow_systems/skills/route-a-evaluator.md", "evaluator_version": "0.2.0",
        "evaluator_authority_sha256": AUTHORITY_SHA, "obstruction_id": "HEN-O357",
        "artifact_paths": ["results/c373_higgs_oscillator_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"],
        "tuple": TUPLE, "overall_verdict": "ROUTE_A_REJECTED",
        "route_b_invocation_allowed": False,
        "route_b_lock_reason": "natural source quantization and periodicity do not clear arithmetic, isolated-orbit, determinant, or analytic-target gates",
        "scope_flags": FLAGS, "theorem_status": "PROVABLE_AS_STATED",
        "finite_evidence_role": "exact action, label, differential-equation, and revival regression only, not proof by finite sampling; the classical periodic-flow theorem excludes omega zero while the Friedrichs quantum boundary includes it",
        "source_owner_tokens": [
            "DOI:10.1088/0305-4470/12/3/006", "DOI:10.1088/0305-4470/12/4/009",
            "arXiv:1008.3865", "arXiv:quant-ph/9803085",
            "theorem:hemisphere-Friedrichs-revival-criterion",
        ],
    }
    for key, expected in frozen.items():
        exact(value[key], expected, f"yaml.{key}")
    statuses = ("PROVED", "PROVED", "STOP_SCOPED", "STOP_SCOPED", "PROVED")
    for key, verdict, status in zip(("a0", "a1", "a2", "a3", "a4"), TUPLE, statuses):
        exact_keys(value[key], {"verdict", "evidence_status", "strongest_evidence", "strongest_failure"}, f"yaml.{key}")
        exact(value[key]["verdict"], verdict, f"yaml.{key}.verdict")
        exact(value[key]["evidence_status"], status, f"yaml.{key}.status")
    for key in (
        "candidate_definition", "family", "phase_space", "dynamics", "parameters", "parameter_provenance",
        "arithmetic_origin", "clock", "normalization", "determinant_convention", "orbit_cutoff",
        "precision", "training_data", "forbidden_data",
    ):
        assert type(value[key]) is str and value[key]
    assert "classically R and omega are strictly positive" in value["parameters"]
    assert "quantum mechanically" in value["parameters"] and "omega is nonnegative" in value["parameters"]


def frac(value: Fraction):
    return {"numerator": value.numerator, "denominator": value.denominator}


def expected_classical_rows():
    r2s = [Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3)]
    omegas = [Fraction(1, 4), Fraction(1, 2), Fraction(1), Fraction(3, 2)]
    actions = [Fraction(1, 8), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1), Fraction(3, 2), Fraction(2), Fraction(5, 2)]
    momenta = [Fraction(1, 7), Fraction(1, 5), Fraction(1, 3), Fraction(1, 2), Fraction(2, 3), Fraction(1), Fraction(3, 2), Fraction(2)]
    rows = []
    for r2 in r2s:
        for omega in omegas:
            scale = omega * r2
            for action in actions:
                for ell in momenta:
                    for sign in (-1, 1):
                        J = 2 * action + ell + scale
                        energy = (J * J - scale * scale) / (2 * r2)
                        threshold = omega * ell + ell * ell / (2 * r2)
                        A = J * J
                        B = 2 * r2 * energy + ell * ell
                        C = ell * ell
                        discriminant = B * B - 4 * A * C
                        vertex = B / (2 * A)
                        value_at_one = A - B + C
                        recovered = J * (1 - ell / J - scale / J) / 2
                        rows.append({
                            "radius_sq": frac(r2), "omega": frac(omega), "radial_action": frac(action),
                            "angular_momentum": frac(sign * ell), "J": frac(J), "energy": frac(energy),
                            "circular_threshold": frac(threshold),
                            "turning_polynomial": {
                                "A": frac(A), "B": frac(B), "C": frac(C), "form": "A*x^2-B*x+C",
                                "discriminant": frac(discriminant), "root_sum": frac(B / A),
                                "root_product": frac(C / A), "complement_product": frac(value_at_one / A),
                                "vertex": frac(vertex), "value_at_one": frac(value_at_one),
                                "roots": ["(B-sqrt(discriminant))/(2*A)", "(B+sqrt(discriminant))/(2*A)"],
                            },
                            "action_recovered": frac(recovered), "omega_r": frac(2 * J / r2),
                            "omega_phi": frac(sign * J / r2), "radial_period_over_pi": frac(r2 / J),
                            "phase_period_over_pi": frac(2 * r2 / J),
                            "frequency_lock_abs": "Omega_r=2*abs(Omega_phi)",
                        })
    return rows


def expected_quantum_rows():
    states, levels = [], []
    for N in range(129):
        labels = []
        k = N + 1
        for m in range(-N, N + 1):
            if (N - abs(m)) % 2:
                continue
            nr = (N - abs(m)) // 2
            states.append({
                "N": N, "n_r": nr, "m": m, "abs_m": abs(m), "k": k,
                "jacobi_degree": nr, "jacobi_alpha": abs(m), "jacobi_beta": "nu",
                "energy_scaled_2R2_over_hbar2": {"constant": k * k, "nu_coefficient": 2 * k},
                "level_multiplicity": N + 1,
            })
            labels.append([nr, m])
        levels.append({
            "N": N, "k": k, "multiplicity": N + 1, "state_label_sha256": digest(labels),
            "omega_zero_dirichlet_l": N + 1,
            "omega_zero_energy_scaled_2R2_over_hbar2": (N + 1) * (N + 2),
            "flat_limit_energy_over_hbar_omega": N + 1,
        })
    return states, levels


def expected_revivals():
    values = sorted({Fraction(n, d) for d in range(1, 33) for n in range(d, 4 * d + 1)})[:256]
    rational = []
    for index, two_nu in enumerate(values):
        gap = 3 + two_nu
        M = gap.denominator if gap.numerator % 2 == 0 else 2 * gap.denominator
        first = M * gap
        global_phase = M * (1 + two_nu)
        phases = [(M * (k * k + two_nu * k)).numerator for k in range(1, 130)]
        rational.append({
            "case": index, "kind": "rational_two_nu", "two_nu": frac(two_nu),
            "three_plus_two_nu": frac(gap), "minimum_M": M,
            "first_gap_exponent": first.numerator, "global_k1_exponent": global_phase.numerator,
            "phase_exponents_k1_to_k129_sha256": digest(phases), "all_phase_residues_mod_2": 0,
        })
    nonsquares = []
    candidate = 2
    while len(nonsquares) < 256:
        root = math.isqrt(candidate)
        if root * root != candidate:
            nonsquares.append(candidate)
        candidate += 1
    irrational = [{
        "case": index, "kind": "irrational_two_nu", "two_nu": f"sqrt({d})",
        "radicand": d, "integer_square_root": math.isqrt(d), "identity_revival_exists": False,
        "obstruction": "M*(3+sqrt(radicand)) cannot be an even integer for positive integer M",
    } for index, d in enumerate(nonsquares)]
    return rational, irrational


BOUNDARIES = [
    {"case": "regular", "classical_omega": "positive", "I_r": "positive", "L": "nonzero", "turning_roots": "two distinct roots in (0,1)", "phase_period": "2*pi*R^2/J", "radial_period": "pi*R^2/J"},
    {"case": "circular", "classical_omega": "positive", "I_r": "zero", "L": "nonzero", "turning_roots": "double root abs(L)/(abs(L)+omega*R^2)", "phase_period": "2*pi*R^2/(abs(L)+omega*R^2)", "radial_period": "linearized only"},
    {"case": "meridional", "classical_omega": "positive", "I_r": "positive", "L": "zero", "turning_roots": "zero and 1-(omega*R^2/J)^2", "phase_period": "2*pi*R^2/J after polar-chart continuation", "radial_period": "pi*R^2/J"},
    {"case": "north_equilibrium", "classical_omega": "positive", "I_r": "zero", "L": "zero", "turning_roots": "north pole", "phase_period": "not applicable", "radial_period": "not applicable"},
    {"case": "classical_omega_zero", "classical_omega": "zero", "I_r": "not frozen", "L": "any", "turning_roots": "equator is no longer a confining barrier", "phase_period": "excluded from the open-hemisphere complete-flow theorem", "radial_period": "excluded"},
    {"case": "quantum_omega_zero", "classical_omega": "not applicable", "I_r": "not applicable", "L": "m*hbar", "turning_roots": "not applicable", "phase_period": "Friedrichs Dirichlet-hemisphere spectrum with l=N+1", "radial_period": "not applicable"},
]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=EVIDENCE)
    parser.add_argument("--evaluation", type=Path, default=EVALUATION)
    args = parser.parse_args()
    validate_yaml(args.evaluation)
    obj = load_json(args.input)
    exact_keys(obj, TOP_KEYS, "evidence root")
    frozen = {
        "schema": "hcs-c373-hemispherical-higgs-evidence-v1", "candidate_id": "HCS-C373",
        "obstruction_id": "HEN-O357", "evaluation_date": "2026-09-04", "source_commit": SOURCE,
        "fixed_epoch": 1788480000, "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": AUTHORITY_SHA},
        "route_a_yaml": {"relative_path": "evaluations/route_a/HCS-C373/2026-09-04.yaml", "raw_sha256": YAML_RAW_SHA, "semantic_sha256": YAML_SEMANTIC_SHA},
        "conventions": {
            "hemisphere": "0<=theta<pi/2 with radius R>0", "classical_domain": "omega>0; regular theorem has I_r>0 and L!=0",
            "hamiltonian": "p_theta^2/(2*R^2)+L^2/(2*R^2*sin(theta)^2)+omega^2*R^2*tan(theta)^2/2",
            "radial_action": "I_r=(1/(2*pi))*closed integral p_theta dtheta", "J": "sqrt(2*R^2*E+omega^2*R^4)",
            "quantum_domain": "omega>=0, R>0, hbar>0, Friedrichs realization on one hemisphere",
            "nu": "sqrt((omega*R^2/hbar)^2+1/4)", "revival_tau": "tau=hbar*t/(2*R^2)",
            "identity_revival": "the full propagator equals the identity, not merely a scalar phase",
        },
        "theorem_contract": {
            "turning_polynomial": "J^2*x^2-(2*R^2*E+L^2)*x+L^2=0 for x=sin(theta)^2",
            "action": "I_r=(J-abs(L)-omega*R^2)/2 and H=((2*I_r+abs(L)+omega*R^2)^2-omega^2*R^4)/(2*R^2)",
            "frequencies": "Omega_r=2*J/R^2 and Omega_phi=sign(L)*J/R^2; regular phase period 2*pi*R^2/J and radial period pi*R^2/J",
            "faces": "circular, meridional, equilibrium, and classical omega-zero faces are separate; omega zero is not a complete open-hemisphere classical periodic-flow claim",
            "quantum": "eigenfunctions exp(i*m*phi)*sin(theta)^abs(m)*cos(theta)^(nu+1/2)*P_nr^(abs(m),nu)(cos(2*theta)); E_N=hbar^2*(N+1)*(N+1+2*nu)/(2*R^2), N=2*n_r+abs(m), multiplicity N+1",
            "limits": "flat limit is hbar*omega*(N+1); omega down to zero gives Dirichlet hemisphere l=N+1 levels, not the full-sphere multiplicity",
            "revival": "identity iff tau=pi*M and M*(3+2*nu) is even; existence iff 2*nu is rational; for reduced 3+2*nu=a/b, M_min=b for even a and 2*b for odd a",
        },
        "finite_grid": {
            "classical_cell_count": 2048, "quantum_level_max": 128, "quantum_state_label_count": 8385,
            "quantum_level_count": 129, "rational_revival_case_count": 256,
            "irrational_revival_case_count": 256, "total_revival_case_count": 512,
            "boundary_row_count": 6,
            "classical_grid": "4 radius-squared * 4 omega * 8 positive radial actions * 8 positive angular magnitudes * 2 signs",
        },
        "collision_boundary": {
            "C349": "Neumann oscillator on the full sphere with Uhlenbeck integrals, not the equator-singular isotropic Higgs potential and its hemisphere Friedrichs spectrum",
            "C244": "spherical pendulum focus-focus monodromy, not maximally resonant Higgs superintegrability",
            "C313": "free round-sphere geodesic and Laplacian dynamics, not a tan-squared barrier with a Dirichlet hemisphere boundary",
            "C221": "nonlinear Schrodinger PDE dynamics, not the linear one-particle Friedrichs Higgs Hamiltonian",
        },
        "nonclaims": [
            "no classical omega-zero complete periodic flow on the open hemisphere",
            "no full-sphere multiplicity at the omega-zero Friedrichs boundary",
            "no rational-prime or prime-power carrier and no arithmetic clock",
            "no target Euler factor, root number, automorphy, target divisor, target functional equation, or target zero match",
            "no Hilbert-Polya operator and no Route B",
        ],
        "references": [
            {"doi": "10.1088/0305-4470/12/3/006", "role": "Higgs spherical oscillator and dynamical symmetry"},
            {"doi": "10.1088/0305-4470/12/4/009", "role": "Leemon curved-space oscillator symmetry"},
            {"arxiv": "1008.3865", "role": "classical action-angle formulation"},
            {"arxiv": "quant-ph/9803085", "role": "two-dimensional spherical oscillator separation and Jacobi spectrum"},
        ],
        "scope_flags": FLAGS,
        "route_a": {"tuple": TUPLE, "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False, "theorem_status": "PROVABLE_AS_STATED"},
        "finite_evidence_role": "finite exact action, state-label, Jacobi, and revival checks are regression evidence only; analytic calculation proves the general classical, quantum, limit, and revival theorems",
    }
    for key, expected in frozen.items():
        exact(obj[key], expected, key)
    temporary = dict(obj)
    claimed = temporary.pop("payload_sha256")
    assert type(claimed) is str and claimed == digest(temporary)

    classical = expected_classical_rows()
    states, levels = expected_quantum_rows()
    rational, irrational = expected_revivals()
    exact(obj["classical_rows"], classical, "classical_rows")
    exact(obj["quantum_state_rows"], states, "quantum_state_rows")
    exact(obj["quantum_level_rows"], levels, "quantum_level_rows")
    exact(obj["rational_revival_rows"], rational, "rational_revival_rows")
    exact(obj["irrational_revival_rows"], irrational, "irrational_revival_rows")
    exact(obj["boundary_rows"], BOUNDARIES, "boundary_rows")
    sections = {
        "classical_rows": classical, "quantum_state_rows": states, "quantum_level_rows": levels,
        "rational_revival_rows": rational, "irrational_revival_rows": irrational,
        "boundary_rows": BOUNDARIES,
    }
    exact(obj["section_sha256"], {key: digest(value) for key, value in sections.items()}, "section_sha256")
    assert sum(row["multiplicity"] for row in levels) == 8385
    assert all(row["global_k1_exponent"] % 2 == 0 for row in rational)
    assert all(not row["identity_revival_exists"] for row in irrational)
    print(
        f"C373 checker PASS: classical={len(classical)} states={len(states)} levels={len(levels)} "
        f"revivals={len(rational)+len(irrational)} payload={claimed}"
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"C373 checker FAIL: {type(exc).__name__}: {exc}", file=sys.stderr)
        sys.exit(1)
