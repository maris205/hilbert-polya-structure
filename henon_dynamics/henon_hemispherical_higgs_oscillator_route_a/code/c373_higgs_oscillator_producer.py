#!/usr/bin/env python3
"""Canonical exact evidence producer for HCS-C373."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("c373 producer refuses optimized Python")

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results/c373_higgs_oscillator_evidence.json"
EVAL = ROOT / "evaluations/route_a/HCS-C373/2026-09-04.yaml"
SOURCE = "c6553f02d928c6aa05400ded57746869a85f0238"
EVALUATOR_SHA = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
YAML_RAW_SHA = "e093905d686c2d32e46cbaa8d711f61c460f21c35f79106be778d222fa85a541"
YAML_SEMANTIC_SHA = "daae2b83c7c1e7cdbc54ec7751e699d04dd9781854403de19364305fc63c13f5"


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


def frac(value: Fraction):
    return {"numerator": value.numerator, "denominator": value.denominator}


def rational_grid():
    radius_sq_values = [Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3)]
    omega_values = [Fraction(1, 4), Fraction(1, 2), Fraction(1), Fraction(3, 2)]
    radial_actions = [
        Fraction(1, 8), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4),
        Fraction(1), Fraction(3, 2), Fraction(2), Fraction(5, 2),
    ]
    angular_magnitudes = [
        Fraction(1, 7), Fraction(1, 5), Fraction(1, 3), Fraction(1, 2),
        Fraction(2, 3), Fraction(1), Fraction(3, 2), Fraction(2),
    ]
    return radius_sq_values, omega_values, radial_actions, angular_magnitudes


def classical_rows():
    radius_sq_values, omega_values, radial_actions, angular_magnitudes = rational_grid()
    rows = []
    for radius_sq in radius_sq_values:
        for omega in omega_values:
            oscillator_scale = omega * radius_sq
            for radial_action in radial_actions:
                for angular_magnitude in angular_magnitudes:
                    for sign in (-1, 1):
                        angular_momentum = sign * angular_magnitude
                        J = 2 * radial_action + angular_magnitude + oscillator_scale
                        energy = (J * J - oscillator_scale * oscillator_scale) / (2 * radius_sq)
                        circular_threshold = (
                            omega * angular_magnitude
                            + angular_magnitude * angular_magnitude / (2 * radius_sq)
                        )
                        coefficient_a = J * J
                        coefficient_b = 2 * radius_sq * energy + angular_magnitude * angular_magnitude
                        coefficient_c = angular_magnitude * angular_magnitude
                        discriminant = coefficient_b * coefficient_b - 4 * coefficient_a * coefficient_c
                        vertex = coefficient_b / (2 * coefficient_a)
                        polynomial_at_one = coefficient_a - coefficient_b + coefficient_c
                        root_sum = coefficient_b / coefficient_a
                        root_product = coefficient_c / coefficient_a
                        complement_product = polynomial_at_one / coefficient_a
                        recovered_action = J * (
                            1 - angular_magnitude / J - oscillator_scale / J
                        ) / 2
                        assert energy > circular_threshold
                        assert discriminant > 0 and 0 < vertex < 1 and polynomial_at_one > 0
                        assert recovered_action == radial_action
                        rows.append(
                            {
                                "radius_sq": frac(radius_sq),
                                "omega": frac(omega),
                                "radial_action": frac(radial_action),
                                "angular_momentum": frac(angular_momentum),
                                "J": frac(J),
                                "energy": frac(energy),
                                "circular_threshold": frac(circular_threshold),
                                "turning_polynomial": {
                                    "A": frac(coefficient_a),
                                    "B": frac(coefficient_b),
                                    "C": frac(coefficient_c),
                                    "form": "A*x^2-B*x+C",
                                    "discriminant": frac(discriminant),
                                    "root_sum": frac(root_sum),
                                    "root_product": frac(root_product),
                                    "complement_product": frac(complement_product),
                                    "vertex": frac(vertex),
                                    "value_at_one": frac(polynomial_at_one),
                                    "roots": ["(B-sqrt(discriminant))/(2*A)", "(B+sqrt(discriminant))/(2*A)"],
                                },
                                "action_recovered": frac(recovered_action),
                                "omega_r": frac(2 * J / radius_sq),
                                "omega_phi": frac(sign * J / radius_sq),
                                "radial_period_over_pi": frac(radius_sq / J),
                                "phase_period_over_pi": frac(2 * radius_sq / J),
                                "frequency_lock_abs": "Omega_r=2*abs(Omega_phi)",
                            }
                        )
    assert len(rows) == 2048
    return rows


def quantum_rows():
    states = []
    levels = []
    for level in range(129):
        level_states = []
        k = level + 1
        for magnetic in range(-level, level + 1):
            if (level - abs(magnetic)) % 2:
                continue
            radial = (level - abs(magnetic)) // 2
            row = {
                "N": level,
                "n_r": radial,
                "m": magnetic,
                "abs_m": abs(magnetic),
                "k": k,
                "jacobi_degree": radial,
                "jacobi_alpha": abs(magnetic),
                "jacobi_beta": "nu",
                "energy_scaled_2R2_over_hbar2": {
                    "constant": k * k,
                    "nu_coefficient": 2 * k,
                },
                "level_multiplicity": level + 1,
            }
            states.append(row)
            level_states.append([radial, magnetic])
        assert len(level_states) == level + 1
        levels.append(
            {
                "N": level,
                "k": k,
                "multiplicity": level + 1,
                "state_label_sha256": digest(level_states),
                "omega_zero_dirichlet_l": level + 1,
                "omega_zero_energy_scaled_2R2_over_hbar2": (level + 1) * (level + 2),
                "flat_limit_energy_over_hbar_omega": level + 1,
            }
        )
    assert len(states) == 8385
    return states, levels


def revival_rows():
    rational_values = sorted(
        {Fraction(numerator, denominator)
         for denominator in range(1, 33)
         for numerator in range(denominator, 4 * denominator + 1)}
    )[:256]
    rational_rows = []
    for index, two_nu in enumerate(rational_values):
        gap = 3 + two_nu
        minimum_m = gap.denominator if gap.numerator % 2 == 0 else 2 * gap.denominator
        first_gap = minimum_m * gap
        global_phase = minimum_m * (1 + two_nu)
        assert first_gap.denominator == 1 and first_gap.numerator % 2 == 0
        assert global_phase.denominator == 1 and global_phase.numerator % 2 == 0
        assert all(
            not (
                (trial * gap).denominator == 1
                and (trial * gap).numerator % 2 == 0
            )
            for trial in range(1, minimum_m)
        )
        phase_exponents = []
        for k in range(1, 130):
            exponent = minimum_m * (k * k + two_nu * k)
            assert exponent.denominator == 1 and exponent.numerator % 2 == 0
            phase_exponents.append(exponent.numerator)
        rational_rows.append(
            {
                "case": index,
                "kind": "rational_two_nu",
                "two_nu": frac(two_nu),
                "three_plus_two_nu": frac(gap),
                "minimum_M": minimum_m,
                "first_gap_exponent": first_gap.numerator,
                "global_k1_exponent": global_phase.numerator,
                "phase_exponents_k1_to_k129_sha256": digest(phase_exponents),
                "all_phase_residues_mod_2": 0,
            }
        )

    nonsquares = []
    candidate = 2
    while len(nonsquares) < 256:
        root = math.isqrt(candidate)
        if root * root != candidate:
            nonsquares.append(candidate)
        candidate += 1
    irrational_rows = [
        {
            "case": index,
            "kind": "irrational_two_nu",
            "two_nu": f"sqrt({radicand})",
            "radicand": radicand,
            "integer_square_root": math.isqrt(radicand),
            "identity_revival_exists": False,
            "obstruction": "M*(3+sqrt(radicand)) cannot be an even integer for positive integer M",
        }
        for index, radicand in enumerate(nonsquares)
    ]
    return rational_rows, irrational_rows


BOUNDARY_ROWS = [
    {
        "case": "regular", "classical_omega": "positive", "I_r": "positive", "L": "nonzero",
        "turning_roots": "two distinct roots in (0,1)",
        "phase_period": "2*pi*R^2/J", "radial_period": "pi*R^2/J",
    },
    {
        "case": "circular", "classical_omega": "positive", "I_r": "zero", "L": "nonzero",
        "turning_roots": "double root abs(L)/(abs(L)+omega*R^2)",
        "phase_period": "2*pi*R^2/(abs(L)+omega*R^2)", "radial_period": "linearized only",
    },
    {
        "case": "meridional", "classical_omega": "positive", "I_r": "positive", "L": "zero",
        "turning_roots": "zero and 1-(omega*R^2/J)^2",
        "phase_period": "2*pi*R^2/J after polar-chart continuation", "radial_period": "pi*R^2/J",
    },
    {
        "case": "north_equilibrium", "classical_omega": "positive", "I_r": "zero", "L": "zero",
        "turning_roots": "north pole", "phase_period": "not applicable", "radial_period": "not applicable",
    },
    {
        "case": "classical_omega_zero", "classical_omega": "zero", "I_r": "not frozen", "L": "any",
        "turning_roots": "equator is no longer a confining barrier",
        "phase_period": "excluded from the open-hemisphere complete-flow theorem", "radial_period": "excluded",
    },
    {
        "case": "quantum_omega_zero", "classical_omega": "not applicable", "I_r": "not applicable", "L": "m*hbar",
        "turning_roots": "not applicable",
        "phase_period": "Friedrichs Dirichlet-hemisphere spectrum with l=N+1", "radial_period": "not applicable",
    },
]


def build(evaluation_path: Path):
    raw = evaluation_path.read_bytes()
    semantic = load_yaml(evaluation_path)
    assert hashlib.sha256(raw).hexdigest() == YAML_RAW_SHA
    assert digest(semantic) == YAML_SEMANTIC_SHA

    classical = classical_rows()
    quantum_states, quantum_levels = quantum_rows()
    rational_revivals, irrational_revivals = revival_rows()
    sections = {
        "classical_rows": classical,
        "quantum_state_rows": quantum_states,
        "quantum_level_rows": quantum_levels,
        "rational_revival_rows": rational_revivals,
        "irrational_revival_rows": irrational_revivals,
        "boundary_rows": BOUNDARY_ROWS,
    }
    flags = {
        key: False
        for key in (
            "claims_target_arithmetic_local_data", "claims_target_euler_factors",
            "claims_root_number", "claims_automorphy",
            "claims_target_divisor_or_counting_law", "claims_target_functional_equation",
            "claims_target_zero_match", "claims_hilbert_polya_operator", "invokes_route_b",
        )
    }
    body = {
        "schema": "hcs-c373-hemispherical-higgs-evidence-v1",
        "candidate_id": "HCS-C373", "obstruction_id": "HEN-O357",
        "evaluation_date": "2026-09-04", "source_commit": SOURCE,
        "fixed_epoch": 1788480000, "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "evaluator": {
            "authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0",
            "sha256": EVALUATOR_SHA,
        },
        "route_a_yaml": {
            "relative_path": "evaluations/route_a/HCS-C373/2026-09-04.yaml",
            "raw_sha256": YAML_RAW_SHA, "semantic_sha256": YAML_SEMANTIC_SHA,
        },
        "conventions": {
            "hemisphere": "0<=theta<pi/2 with radius R>0",
            "classical_domain": "omega>0; regular theorem has I_r>0 and L!=0",
            "hamiltonian": "p_theta^2/(2*R^2)+L^2/(2*R^2*sin(theta)^2)+omega^2*R^2*tan(theta)^2/2",
            "radial_action": "I_r=(1/(2*pi))*closed integral p_theta dtheta",
            "J": "sqrt(2*R^2*E+omega^2*R^4)",
            "quantum_domain": "omega>=0, R>0, hbar>0, Friedrichs realization on one hemisphere",
            "nu": "sqrt((omega*R^2/hbar)^2+1/4)",
            "revival_tau": "tau=hbar*t/(2*R^2)",
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
            "classical_cell_count": len(classical), "quantum_level_max": 128,
            "quantum_state_label_count": len(quantum_states),
            "quantum_level_count": len(quantum_levels),
            "rational_revival_case_count": len(rational_revivals),
            "irrational_revival_case_count": len(irrational_revivals),
            "total_revival_case_count": len(rational_revivals) + len(irrational_revivals),
            "boundary_row_count": len(BOUNDARY_ROWS),
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
        "scope_flags": flags,
        "route_a": {
            "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
            "theorem_status": "PROVABLE_AS_STATED",
        },
        "finite_evidence_role": "finite exact action, state-label, Jacobi, and revival checks are regression evidence only; analytic calculation proves the general classical, quantum, limit, and revival theorems",
        **sections,
        "section_sha256": {key: digest(value) for key, value in sections.items()},
    }
    body["payload_sha256"] = digest(body)
    return body


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUT)
    parser.add_argument("--evaluation", type=Path, default=EVAL)
    args = parser.parse_args()
    value = build(args.evaluation)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(
        json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False).encode() + b"\n"
    )
    grid = value["finite_grid"]
    print(
        "C373 producer PASS: "
        f"classical={grid['classical_cell_count']} states={grid['quantum_state_label_count']} "
        f"levels={grid['quantum_level_count']} revivals={grid['total_revival_case_count']} "
        f"payload={value['payload_sha256']}"
    )


if __name__ == "__main__":
    main()
