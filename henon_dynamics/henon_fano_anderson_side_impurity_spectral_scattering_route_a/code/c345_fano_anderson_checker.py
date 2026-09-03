#!/usr/bin/env python3
"""Producer-independent strict checker for HCS-C345."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

import yaml
from yaml.tokens import AliasToken, AnchorToken


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c345_fano_anderson_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C345/2026-09-03.yaml"
SOURCE = "1af63b945e19b5f94ac1cb76f93af5ac66d3d562"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EVAL_RAW = "ac793e0ba23eee9154ae2ebacb966aa53289247b5aa847ef8c35ca58588bb056"
EVAL_SEMANTIC = "07c7fb37d0b7452c7adafc64b36ca04fb0fe88104e124310da7aed764dfef490"
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
    "hilbert_space": "ell2(Z) direct_sum C|d>",
    "chain_action": "(Hu)_n=J(u_{n+1}+u_{n-1})+g*u_d*delta_{n0}",
    "impurity_action": "(Hu)_d=epsilon*u_d+g*u_0",
    "main_domain": "J>0, epsilon real, g real",
    "free_dispersion": "E=2*J*cos(k)",
    "resolvent_branch": "sqrt(z^2-4J^2) is analytic off [-2J,2J] and asymptotic to z",
    "free_origin_m_function": "m(z)=1/sqrt(z^2-4J^2)",
    "impurity_resolvent": "G_dd(z)=1/(z-epsilon-g^2*m(z))",
}

THEOREM = {
    "spectral_type": "for J>0 and g!=0 the band [-2J,2J] is purely absolutely continuous of multiplicity two almost everywhere, with no singular-continuous spectrum",
    "resolvent_sign": "G_dd(z)=<d,(z-H)^(-1)d> is anti-Herglotz on the upper half-plane, while M_dd(z)=-G_dd(z)=<d,(H-z)^(-1)d> is Herglotz",
    "measure_exclusion": "local-uniform boundary convergence plus Stone inversion gives the full open-band density; off-band meromorphy leaves only two simple atoms; the two edge atom limits vanish",
    "bound_states": "for J>0 and g!=0 there are exactly two simple eigenvalues, one below -2J and one above 2J",
    "physical_branch": "the lower state solves E-epsilon+g^2/sqrt(E^2-4J^2)=0 and the upper solves E-epsilon-g^2/sqrt(E^2-4J^2)=0",
    "quartic_filter": "squaring yields (E-epsilon)^2(E^2-4J^2)-g^4=0 but only branch-compatible roots are eigenvalues",
    "density": "rho_d(E)=g^2*sqrt(4J^2-E^2)/(pi*((E-epsilon)^2*(4J^2-E^2)+g^4)) in the open band",
    "residues": "the two impurity atom weights are 1/(1-g^2*m'(E_pm)) and density plus atoms has mass one",
    "scattering": "T=4J^2*sin(k)^2*(E-epsilon)^2/(g^4+4J^2*sin(k)^2*(E-epsilon)^2), R=1-T",
    "fano_zero": "for g!=0 an exact continuum zero occurs at E=epsilon iff abs(epsilon)<2J",
}

MEASURE_PROOF = {
    "cauchy_convention": "G_dd(z)=integral (z-E)^(-1) dmu_d(E) has negative imaginary part for Im(z)>0; M_dd=-G_dd is the standard Herglotz transform",
    "density_sign": "rho_d(E)=-pi^(-1)*Im(G_dd(E+i0)) on the open band",
    "open_band_measure": "on every compact K inside (-2J,2J), G_dd(E+i*eta) converges uniformly to its continuous nonpolar boundary value and Stone inversion gives mu_d restricted to K equals rho_d(E)dE",
    "off_band_measure": "on the real complement of [-2J,2J], G_dd is real analytic except at exactly the two simple physical poles, so the measure there consists exactly of their two atoms",
    "edge_atom_test": "for E0=plus_or_minus 2J, mu_d({E0})=limit eta->0+ of i*eta*G_dd(E0+i*eta)=0 because G_dd=S/((z-epsilon)S-g^2) tends to zero",
    "singular_continuous_exclusion": "compact exhaustion of the open band, the off-band pole classification, and the zero edge atoms leave no support for a singular-continuous remainder",
}

REFERENCES = [
    {"identifier": "10.1103/PhysRev.124.1866", "role": "primary Fano discrete-continuum interference source"},
    {"identifier": "10.1002/cpa.3160010404", "role": "primary continuous-spectrum perturbation source"},
    {"identifier": "10.1103/RevModPhys.82.2257", "role": "authoritative Fano-resonance review and discrete-model context"},
]

COLLISIONS = {
    "C267": "Wannier--Stark uses a uniform field and a pure-point ladder, not a side impurity or Fano zero",
    "C288": "the continuum delta point interaction has no discrete side level and no two-channel Fano interference",
    "C308": "Hatano--Nelson is non-self-adjoint boundary-sensitive transport, not a self-adjoint finite-rank impurity",
    "C318": "SSH is a dimerized topological finite chain, not a discrete state coupled to a continuum backbone",
}

NONCLAIMS = [
    "No priority claim is made for the Fano--Anderson model, its resolvent, or its scattering formula.",
    "Finite chains are not used to prove the infinite-volume spectrum or spectral type.",
    "No target arithmetic datum, Euler factor, root number, automorphy, target divisor, functional equation, target-zero match, Hilbert--Polya operator, or Route-B input is claimed.",
]

BOUNDARIES = {
    "g_zero": "free chain direct_sum isolated impurity; the impurity eigenvalue may be embedded, at a band edge, or outside the band",
    "J_zero": "a two-by-two origin-impurity block with eigenvalues (epsilon plus_or_minus sqrt(epsilon^2+4g^2))/2 plus an infinite-multiplicity zero eigenspace",
    "coupling_sign": "g and -g are unitarily equivalent by changing the impurity phase",
    "epsilon_band_edges": "epsilon=plus_or_minus 2J is not an open-channel Fano zero; for g!=0 neither band edge is an eigenvalue",
    "g_to_zero": "the two physical poles approach the appropriate band edges or the decoupled level non-uniformly; the theorem does not identify the g=0 spectral decomposition by continuity alone",
    "quartic_warning": "branch-rejected real roots of the squared quartic are never promoted to eigenvalues",
}

GRID = {
    "J_values": ["1/2", "1", "2"],
    "epsilon_values": ["-3", "-2", "-1", "0", "1", "2", "3"],
    "g_nonzero_values": ["-2", "-1", "-1/2", "1/2", "1", "2"],
    "cos_k_values": ["-3/4", "-1/2", "0", "1/2", "3/4"],
    "evidence_role": "exact finite implementation receipt, not proof by sampling or finite-volume approximation",
}

TOP_KEYS = {
    "schema", "candidate_id", "obstruction_id", "source_commit", "fixed_epoch",
    "scope_literal", "evaluator", "evaluation", "model", "theorem_contract",
    "spectral_measure_proof_lock",
    "references", "collision_boundary", "nonclaims", "route_a", "scope_flags",
    "parameter_grid", "spectral_rows", "scattering_rows", "fano_zero_rows",
    "resolvent_moment_rows", "boundary_rows", "enumeration", "payload_sha256",
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
    "candidate_id": "HCS-C345",
    "title": "Discrete Fano--Anderson side-impurity spectral and scattering atlas",
    "evaluation_date": "2026-09-03",
    "source_commit": SOURCE,
    "fixed_epoch": EPOCH,
    "scope_literal": SCOPE,
    "evaluator_authority": "flow_systems/skills/route-a-evaluator.md",
    "evaluator_version": "0.2.0",
    "evaluator_authority_sha256": EVALUATOR,
    "obstruction_id": "HEN-O329",
    "candidate_definition": "an infinite nearest-neighbour self-adjoint tight-binding chain with one discrete state side-coupled at the origin",
    "family": "finite-rank impurity Hamiltonians and one-dimensional lattice scattering",
    "phase_space": "the Hilbert space ell2 of the integer lattice direct-summed with one impurity amplitude",
    "dynamics": "the unitary group generated by the bounded self-adjoint Fano--Anderson Hamiltonian and its stationary scattering problem",
    "parameters": "hopping J positive in the main theorem, impurity energy epsilon real, and coupling g real",
    "parameter_provenance": "source-local hopping, level energy, and hybridization only, never target-fitted",
    "arithmetic_origin": "none",
    "clock": "source quantum time for the Hamiltonian group and source wave number for on-shell scattering",
    "normalization": "chain dispersion E equals 2 J cos k and the resolvent square root is fixed by sqrt(z squared minus 4 J squared) asymptotic to z",
    "determinant_convention": "only the Schur denominator and branch-filtered secular equation are used; no dynamical Euler product or target determinant is defined",
    "orbit_cutoff": "full infinite-volume analytic theorem; finite rational grids are implementation receipts and finite boxes are non-probative regressions",
    "precision": "exact rational polynomial, Sturm, scattering, and symbolic identities with no fitted or target-derived constants",
    "training_data": "none",
    "forbidden_data": "target arithmetic local data, Euler factors, root numbers, automorphy, target divisor or functional equation, target zeros, Hilbert-Polya operators, and Route B",
    "artifact_paths": ["results/c345_fano_anderson_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"],
    "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
    "overall_verdict": "ROUTE_A_REJECTED",
    "route_b_invocation_allowed": False,
    "route_b_lock_reason": "no arithmetic source, prime clock, target Euler factor, target divisor, or target-zero correspondence exists",
    "scope_flags": FLAGS,
    "theorem_status": "PROVABLE_AS_STATED",
    "finite_evidence_role": "branch conventions, polynomial coefficients, physical-root Sturm counts, scattering conservation, density factors, and implementation receipt only; analytic arguments prove the parameter-continuum theorem",
    "source_owner_tokens": [
        "10.1103/PhysRev.124.1866", "10.1002/cpa.3160010404", "10.1103/RevModPhys.82.2257",
    ],
}

GATES = {
    "a0": {
        "verdict": "A0_FAIL", "evidence_status": "PROVED",
        "strongest_evidence": "the Hamiltonian, branch-safe resolvent, spectrum, bound states, and scattering amplitudes are derived exactly from source parameters",
        "strongest_failure": "the model has no intrinsic rational-prime or prime-power payload and no arithmetic source",
    },
    "a1": {
        "verdict": "A1_FAIL", "evidence_status": "PROVED",
        "strongest_evidence": "the complete spectral and on-shell scattering dynamics are explicit",
        "strongest_failure": "lattice propagation and impurity scattering do not provide an arithmetic primitive-periodic-orbit ledger with repetition weights",
    },
    "a2": {
        "verdict": "A2_FAIL", "evidence_status": "STOP_SCOPED",
        "strongest_evidence": "the Schur denominator is an exact source-local analytic function on the free resolvent surface",
        "strongest_failure": "no primitive-orbit Euler product, target Fredholm determinant, or target divisor is defined",
    },
    "a3": {
        "verdict": "A3_FAIL", "evidence_status": "STOP_SCOPED",
        "strongest_evidence": "the physical-sheet poles, absolutely continuous density, and scattering conservation law are controlled exactly",
        "strongest_failure": "the theorem supplies no target functional equation, target counting law, or Weil compression",
    },
    "a4": {
        "verdict": "A4_NATURAL_QUANTIZATION", "evidence_status": "PROVED",
        "strongest_evidence": "the model is already a natural bounded self-adjoint Hamiltonian with a canonical unitary group and scattering problem",
        "strongest_failure": "natural quantization alone supplies no arithmetic clock, target divisor, or target-zero correspondence",
    },
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
    value = json.loads(
        path.read_text(), object_pairs_hook=duplicate_pairs,
        parse_constant=lambda token: (_ for _ in ()).throw(ValueError(f"nonfinite {token}")),
    )
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


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def q(value: str) -> Fraction:
    if type(value) is not str:
        raise ValueError("rational encoding is not a string")
    return Fraction(value)


def leaf_count(value) -> int:
    if type(value) is dict:
        return sum(leaf_count(child) for child in value.values())
    if type(value) is list:
        return sum(leaf_count(child) for child in value)
    return 1


def strip(poly):
    result = list(poly)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def slope(poly):
    return strip([Fraction(i) * poly[i] for i in range(1, len(poly))] or [Fraction(0)])


def remainder(left, right):
    work = strip(left)
    divisor = strip(right)
    while work != [0] and len(work) >= len(divisor):
        shift = len(work) - len(divisor)
        scale = work[-1] / divisor[-1]
        for index, value in enumerate(divisor):
            work[index + shift] -= scale * value
        work = strip(work)
    return work


def sturm_chain(poly):
    chain = [strip(poly), slope(poly)]
    while chain[-1] != [0]:
        residual = remainder(chain[-2], chain[-1])
        if residual == [0]:
            break
        chain.append([-value for value in residual])
    return chain


def sign(value):
    return (value > 0) - (value < 0)


def at(poly, point):
    value = Fraction(0)
    for coefficient in reversed(poly):
        value = value * point + coefficient
    return value


def changes(chain, point):
    signs = []
    for poly in chain:
        if point == "minus":
            signs.append(sign(poly[-1]) * (-1 if (len(poly)-1) % 2 else 1))
        elif point == "plus":
            signs.append(sign(poly[-1]))
        else:
            signs.append(sign(at(poly, point)))
    signs = [item for item in signs if item]
    return sum(left != right for left, right in zip(signs, signs[1:]))


def roots(chain, left, right):
    return changes(chain, left) - changes(chain, right)


def polynomial(J, epsilon, g):
    return [-4*epsilon*epsilon*J*J-g**4, 8*epsilon*J*J,
            epsilon*epsilon-4*J*J, -2*epsilon, Fraction(1)]


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
        "path": "evaluations/route_a/HCS-C345/2026-09-03.yaml",
        "raw_sha256": EVAL_RAW,
        "semantic_sha256": EVAL_SEMANTIC,
    }:
        raise AssertionError("nested evaluation carrier mismatch")
    return leaf_count(value)


def check_fixed(data: dict) -> int:
    if set(data) != TOP_KEYS:
        raise AssertionError("top-level evidence schema mismatch")
    body = copy.deepcopy(data)
    claimed = body.pop("payload_sha256")
    if type(claimed) is not str or len(claimed) != 64 or canonical_hash(body) != claimed:
        raise AssertionError("evidence payload hash mismatch")
    fixed = {
        "schema": "hcs-c345-fano-anderson-v2", "candidate_id": "HCS-C345",
        "obstruction_id": "HEN-O329", "source_commit": SOURCE,
        "fixed_epoch": EPOCH, "scope_literal": SCOPE,
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR},
        "model": MODEL, "theorem_contract": THEOREM,
        "spectral_measure_proof_lock": MEASURE_PROOF, "references": REFERENCES,
        "collision_boundary": COLLISIONS, "nonclaims": NONCLAIMS,
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
        },
        "scope_flags": FLAGS, "parameter_grid": GRID, "boundary_rows": BOUNDARIES,
    }
    for key, expected in fixed.items():
        if data[key] != expected:
            raise AssertionError(f"fixed evidence field mismatch: {key}")
    return 1


def check_spectral(rows: list) -> int:
    Js = [Fraction(1, 2), Fraction(1), Fraction(2)]
    epsilons = [Fraction(-3), Fraction(-2), Fraction(-1), Fraction(0), Fraction(1), Fraction(2), Fraction(3)]
    couplings = [Fraction(-2), Fraction(-1), Fraction(-1, 2), Fraction(1, 2), Fraction(1), Fraction(2)]
    if type(rows) is not list or len(rows) != 126:
        raise AssertionError("spectral row count")
    index = 0
    for J in Js:
        for epsilon in epsilons:
            for g in couplings:
                coefficients = polynomial(J, epsilon, g)
                chain = sturm_chain(coefficients)
                lower, upper = min(-2*J, epsilon), max(2*J, epsilon)
                low_count = roots(chain, "minus", lower)
                up_count = roots(chain, upper, "plus")
                total = roots(chain, "minus", "plus")
                expected = {
                    "J": qstr(J), "epsilon": qstr(epsilon), "g": qstr(g),
                    "quartic_coefficients_ascending": [qstr(x) for x in coefficients],
                    "physical_lower_interval": f"(-infinity,{qstr(lower)})",
                    "physical_upper_interval": f"({qstr(upper)},infinity)",
                    "physical_lower_root_count": low_count,
                    "physical_upper_root_count": up_count,
                    "quartic_real_root_count": total,
                    "branch_rejected_real_root_count": total-low_count-up_count,
                    "band_root_count": roots(chain, -2*J, 2*J),
                }
                if rows[index] != expected or low_count != 1 or up_count != 1:
                    raise AssertionError(f"spectral row mismatch: {index}")
                if expected["band_root_count"] != 0 or expected["branch_rejected_real_root_count"] not in {0, 2}:
                    raise AssertionError(f"branch ledger mismatch: {index}")
                index += 1
    return 14 * len(rows)


def check_scattering(rows: list) -> int:
    Js = [Fraction(1, 2), Fraction(1), Fraction(2)]
    epsilons = [Fraction(-3), Fraction(-2), Fraction(-1), Fraction(0), Fraction(1), Fraction(2), Fraction(3)]
    couplings = [Fraction(1, 2), Fraction(1), Fraction(2)]
    cosines = [Fraction(-3, 4), Fraction(-1, 2), Fraction(0), Fraction(1, 2), Fraction(3, 4)]
    if type(rows) is not list or len(rows) != 315:
        raise AssertionError("scattering row count")
    index = 0
    for J in Js:
        for epsilon in epsilons:
            for g in couplings:
                for cosine in cosines:
                    energy = 2*J*cosine
                    sine2 = 1-cosine*cosine
                    channel = 4*J*J*sine2*(energy-epsilon)**2
                    denominator = g**4+channel
                    radical2 = 4*J*J-energy*energy
                    density_denominator = (energy-epsilon)**2*radical2+g**4
                    expected = {
                        "J": qstr(J), "epsilon": qstr(epsilon), "abs_g": qstr(g),
                        "cos_k": qstr(cosine), "energy": qstr(energy),
                        "sin_squared_k": qstr(sine2),
                        "transmission": qstr(channel/denominator),
                        "reflection": qstr(g**4/denominator), "unitarity_sum": "1",
                        "density_radical_squared": qstr(radical2),
                        "density_denominator": qstr(density_denominator),
                        "pi_density_divided_by_radical": qstr(g*g/density_denominator),
                    }
                    if rows[index] != expected or q(expected["transmission"])+q(expected["reflection"]) != 1:
                        raise AssertionError(f"scattering row mismatch: {index}")
                    if radical2 <= 0 or density_denominator <= 0:
                        raise AssertionError(f"density positivity mismatch: {index}")
                    index += 1
    return 15 * len(rows)


def check_fano(rows: list) -> int:
    Js = [Fraction(1, 2), Fraction(1), Fraction(2)]
    epsilons = [Fraction(-3), Fraction(-2), Fraction(-1), Fraction(0), Fraction(1), Fraction(2), Fraction(3)]
    couplings = [Fraction(1, 2), Fraction(1), Fraction(2)]
    if type(rows) is not list or len(rows) != 63:
        raise AssertionError("Fano row count")
    index = 0
    for J in Js:
        for epsilon in epsilons:
            location = ("interior_exact_zero" if abs(epsilon) < 2*J else
                        "band_edge_not_open_channel" if abs(epsilon) == 2*J else
                        "outside_band_not_on_shell")
            for g in couplings:
                expected = {
                    "J": qstr(J), "epsilon": qstr(epsilon), "abs_g": qstr(g),
                    "location": location,
                    "on_shell_energy": qstr(epsilon) if location == "interior_exact_zero" else None,
                    "transmission_numerator_at_epsilon": "0",
                    "transmission_denominator_at_epsilon": qstr(g**4),
                    "is_continuum_fano_zero": location == "interior_exact_zero",
                }
                if rows[index] != expected:
                    raise AssertionError(f"Fano row mismatch: {index}")
                index += 1
    return 9 * len(rows)


def check_moments(rows: list) -> int:
    epsilons = [Fraction(-3), Fraction(-2), Fraction(-1), Fraction(0), Fraction(1), Fraction(2), Fraction(3)]
    couplings = [Fraction(1, 2), Fraction(1), Fraction(2)]
    if type(rows) is not list or len(rows) != 21:
        raise AssertionError("moment row count")
    index = 0
    for epsilon in epsilons:
        for g in couplings:
            expected = {
                "epsilon": qstr(epsilon), "abs_g": qstr(g),
                "coefficient_z_minus_1": "1", "coefficient_z_minus_2": qstr(epsilon),
                "coefficient_z_minus_3": qstr(epsilon*epsilon+g*g),
                "coefficient_z_minus_4": qstr(epsilon**3+2*epsilon*g*g),
                "mass_conclusion": "ac_density_plus_two_bound_atoms_has_total_mass_one",
            }
            if rows[index] != expected:
                raise AssertionError(f"moment row mismatch: {index}")
            index += 1
    return 9 * len(rows)


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C345 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    parser.add_argument("--evaluation", type=Path, default=EVALUATION)
    args = parser.parse_args()
    data = strict_json(args.evidence)
    checks = check_fixed(data)
    yaml_leaves = check_evaluation(args.evaluation, data)
    checks += check_spectral(data["spectral_rows"])
    checks += check_scattering(data["scattering_rows"])
    checks += check_fano(data["fano_zero_rows"])
    checks += check_moments(data["resolvent_moment_rows"])
    expected_enumeration = {
        "spectral_rows": 126, "scattering_rows": 315,
        "fano_zero_rows": 63, "resolvent_moment_rows": 21,
        "audited_leaf_count": 6418,
    }
    if data["enumeration"] != expected_enumeration:
        raise AssertionError("enumeration mismatch")
    counted = copy.deepcopy(data)
    counted.pop("payload_sha256")
    counted["enumeration"].pop("audited_leaf_count")
    if leaf_count(counted) != data["enumeration"]["audited_leaf_count"]:
        raise AssertionError("audited leaf count mismatch")
    checks += data["enumeration"]["audited_leaf_count"] + yaml_leaves
    print(f"C345 independent Fano--Anderson checker: PASS {checks} assertions {yaml_leaves} evaluator leaves")


if __name__ == "__main__":
    main()
