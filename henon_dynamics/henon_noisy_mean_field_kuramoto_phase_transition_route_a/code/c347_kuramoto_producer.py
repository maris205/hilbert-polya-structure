#!/usr/bin/env python3
"""Canonical exact finite-evidence producer for HCS-C347."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c347_kuramoto_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C347/2026-09-03.yaml"
SOURCE = "1af63b945e19b5f94ac1cb76f93af5ac66d3d562"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
YAML_RAW = "032d92adfe7e5ceff5727dce250f06ddf5e24516c6f616982327a621b2503f5b"
YAML_SEMANTIC = "62ecfa44268ab9d87c05956f4a9e8639beb065a17aab7d2f0a7dee35c647babf"
KAPPA_PANEL = tuple(Fraction(x) for x in ("1/4", "1/2", "1", "3/2", "2", "3", "4"))
COUPLING_PANEL = tuple(Fraction(x) for x in ("5/2", "3", "4", "6"))


class StrictLoader(yaml.SafeLoader):
    pass


StrictLoader.yaml_implicit_resolvers = {
    key: [(tag, rx) for tag, rx in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def strict_mapping(loader, node, deep=False):
    answer = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("merge key")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in answer:
            raise ValueError("duplicate/non-string YAML key")
        answer[key] = loader.construct_object(value_node, deep=deep)
    return answer


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, strict_mapping)


def strict_yaml(path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("anchors forbidden")
    value = yaml.load(raw, Loader=StrictLoader)
    if type(value) is not dict:
        raise TypeError("YAML root")
    return value


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def fstr(value):
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def i0_term(kappa, m):
    return kappa ** (2 * m) / (4 ** m * math.factorial(m) ** 2)


def i1_term(kappa, m):
    return kappa ** (2 * m + 1) / (2 * 4 ** m * math.factorial(m) * math.factorial(m + 1))


def bessel_bounds(kappa, cutoff=20):
    """Positive-series lower bounds and geometric majorants for I0 and I1."""
    i0_lower = sum((i0_term(kappa, m) for m in range(cutoff + 1)), Fraction(0))
    i1_lower = sum((i1_term(kappa, m) for m in range(cutoff + 1)), Fraction(0))
    next0 = i0_term(kappa, cutoff + 1)
    next1 = i1_term(kappa, cutoff + 1)
    ratio0 = kappa * kappa / (4 * (cutoff + 2) ** 2)
    ratio1 = kappa * kappa / (4 * (cutoff + 2) * (cutoff + 3))
    if not (ratio0 < 1 and ratio1 < 1):
        raise AssertionError("tail ratio")
    i0_upper = i0_lower + next0 / (1 - ratio0)
    i1_upper = i1_lower + next1 / (1 - ratio1)
    return i0_lower, i0_upper, i1_lower, i1_upper


def ratio_bounds(kappa, cutoff=20):
    i0_lower, i0_upper, i1_lower, i1_upper = bessel_bounds(kappa, cutoff)
    return i1_lower / i0_upper, i1_upper / i0_lower


def coefficient_rows():
    rows = []
    for m in range(17):
        i0 = Fraction(1, 4 ** m * math.factorial(m) ** 2)
        i1_over_kappa = Fraction(1, 2 * 4 ** m * math.factorial(m) * math.factorial(m + 1))
        rows.append({"m": m, "i0_coefficient": fstr(i0),
                     "i1_over_kappa_coefficient": fstr(i1_over_kappa),
                     "coefficient_ratio": fstr(i1_over_kappa / i0)})
    return rows


def formal_quotient_rows(order=8):
    denominator = [Fraction(1, 4 ** m * math.factorial(m) ** 2) for m in range(order + 1)]
    numerator = [Fraction(1, 2 * 4 ** m * math.factorial(m) * math.factorial(m + 1))
                 for m in range(order + 1)]
    quotient = []
    for n in range(order + 1):
        value = numerator[n] - sum(denominator[j] * quotient[n - j] for j in range(1, n + 1))
        quotient.append(value)
    return [{"power_of_kappa_squared": n, "coefficient": fstr(value)}
            for n, value in enumerate(quotient)]


def tail_rows():
    rows = []
    for kappa in KAPPA_PANEL:
        low0, high0, low1, high1 = bessel_bounds(kappa)
        lowr, highr = low1 / high0, high1 / low0
        rows.append({"kappa": fstr(kappa), "cutoff": 20,
            "i0_lower": fstr(low0), "i0_upper": fstr(high0),
            "i1_lower": fstr(low1), "i1_upper": fstr(high1),
            "ratio_lower": fstr(lowr), "ratio_upper": fstr(highr),
            "strict_interval": lowr < highr})
    return rows


def root_rows():
    rows = []
    step = Fraction(1, 64)
    for coupling in COUPLING_PANEL:
        last_positive = None
        first_negative = None
        for index in range(1, int(coupling / step) + 1):
            kappa = index * step
            lower, upper = ratio_bounds(kappa)
            if coupling * lower - kappa > 0:
                last_positive = (kappa, coupling * lower - kappa)
            if first_negative is None and coupling * upper - kappa < 0:
                first_negative = (kappa, coupling * upper - kappa)
        if last_positive is None or first_negative is None or not last_positive[0] < first_negative[0]:
            raise AssertionError(f"uncertified bracket for {coupling}")
        rows.append({"K_over_D": fstr(coupling), "mesh_denominator": 64,
            "kappa_left": fstr(last_positive[0]), "certified_f_left_lower": fstr(last_positive[1]),
            "kappa_right": fstr(first_negative[0]), "certified_f_right_upper": fstr(first_negative[1]),
            "root_count_analytic": 1})
    return rows


def fourier_rows():
    rows = []
    for diffusion in (Fraction(1, 2), Fraction(1), Fraction(2)):
        for ratio in (Fraction(0), Fraction(1), Fraction(2), Fraction(5, 2), Fraction(3), Fraction(4)):
            coupling = diffusion * ratio
            for mode in range(9):
                if mode == 0:
                    eigenvalue, multiplicity = Fraction(0), 1
                elif mode == 1:
                    eigenvalue, multiplicity = coupling / 2 - diffusion, 2
                else:
                    eigenvalue, multiplicity = -diffusion * mode * mode, 2
                rows.append({"D": fstr(diffusion), "K": fstr(coupling),
                    "mode": mode, "real_multiplicity": multiplicity,
                    "linearized_eigenvalue": fstr(eigenvalue)})
    return rows


def digest(rows):
    return hashlib.sha256(canonical(rows)).hexdigest()


def build(evaluation):
    raw = evaluation.read_bytes()
    semantic = strict_yaml(evaluation)
    if hashlib.sha256(raw).hexdigest() != YAML_RAW:
        raise AssertionError("evaluation raw hash")
    if hashlib.sha256(canonical(semantic)).hexdigest() != YAML_SEMANTIC:
        raise AssertionError("evaluation semantic hash")
    coefficients = coefficient_rows()
    quotient = formal_quotient_rows()
    tails = tail_rows()
    roots = root_rows()
    fourier = fourier_rows()
    body = {
        "schema": "hcs-c347-kuramoto-evidence-v1",
        "candidate_id": "HCS-C347", "obstruction_id": "HEN-O331",
        "evaluation_date": "2026-09-03", "source_commit": SOURCE,
        "fixed_epoch": 1788393600, "scope_literal": SCOPE,
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md",
                      "version": "0.2.0", "sha256": EVALUATOR},
        "route_a_yaml": {"relative_path": "evaluations/route_a/HCS-C347/2026-09-03.yaml",
                         "raw_sha256": YAML_RAW, "semantic_sha256": YAML_SEMANTIC},
        "model": {
            "phase_space": "nonnegative unit-mass circle densities; classical theorem starts from C^{2+gamma}",
            "parameters": "D>0 and K>=0",
            "order_parameter": "z[p]=integral exp(i theta)p(theta)dtheta=r exp(i psi)",
            "pde": "p_t=D p_thetatheta-d_theta(K r sin(psi-theta)p)",
            "uniform_density": "1/(2 pi)",
            "stationary_family": "exp(kappa cos(theta-psi))/(2 pi I0(kappa))"},
        "theorem_contract": {
            "flow": "unique global classical mass-preserving positive probability flow",
            "free_energy": "F=D integral p log p-(K/2)|z[p]|^2 with exact dissipation",
            "stationary": "all positive C2 stationary densities are uniform or the self-consistent von Mises circle",
            "transition": "uniform only for K<=2D; one nonzero concentration modulo phase for K>2D",
            "linearization": "mass mode zero, first harmonic K/2-D, higher harmonics -D n^2",
            "critical": "kappa^2=4 delta+(2/3)delta^2+O(delta^3), r^2=delta-(5/6)delta^2+O(delta^3)"},
        "finite_grid": {"bessel_coefficient_rows": len(coefficients),
            "formal_quotient_rows": len(quotient), "tail_bracket_rows": len(tails),
            "self_consistency_root_rows": len(roots), "fourier_rows": len(fourier),
            "bessel_cutoff": 20, "root_mesh_denominator": 64},
        "collision_boundary": {
            "C322": "linear Kac collision spectrum, not a nonlinear nonlocal parabolic phase transition",
            "C339": "finite-dimensional Hamiltonian navigation, not a dissipative probability PDE",
            "C340": "periodic Schrodinger finite-gap operator, not Kuramoto mean-field synchronization"},
        "nonclaims": [
            "no general-initial-data convergence rate or global convergence theorem",
            "no Hopf bifurcation, time-periodic branch, disorder, delay, inertia, or finite-N theorem",
            "no D=0 atomic-state extension",
            "no target arithmetic local data, Euler factors, root number, automorphy, target zero match, Hilbert-Polya operator, or Route B"],
        "references": [
            {"authors": "Hidetsugu Sakaguchi", "year": 1988,
             "identifier": "DOI:10.1143/PTP.79.39",
             "url": "https://academic.oup.com/ptp/article/79/1/39/1855689",
             "role": "primary noisy globally coupled oscillator source"},
            {"authors": "Lorenzo Bertini; Giambattista Giacomin; Khashayar Pakdaman", "year": 2010,
             "identifier": "DOI:10.1007/s10955-009-9908-9",
             "url": "https://arxiv.org/abs/0911.1499",
             "role": "authoritative reversible mean-field rotator dynamics and free-energy source"}],
        "route_a": {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
                    "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": {
            "claims_target_arithmetic_local_data": False, "claims_target_euler_factors": False,
            "claims_root_number": False, "claims_automorphy": False,
            "claims_target_divisor_or_counting_law": False,
            "claims_target_functional_equation": False, "claims_target_zero_match": False,
            "claims_hilbert_polya_operator": False, "invokes_route_b": False},
        "bessel_coefficient_rows": coefficients,
        "formal_quotient_rows": quotient,
        "tail_bracket_rows": tails,
        "self_consistency_root_rows": roots,
        "fourier_rows": fourier,
        "critical_expansion": {"delta": "K/D-2", "kappa_squared": ["4", "2/3"],
                               "r_squared": ["1", "-5/6"],
                               "analytic_remainder_order": 3},
        "enumeration": {"all_arithmetic_exact": True, "floating_point_used": False,
            "finite_evidence_proves_continuum_theorem": False,
            "bessel_coefficient_sha256": digest(coefficients),
            "formal_quotient_sha256": digest(quotient),
            "tail_bracket_sha256": digest(tails), "root_bracket_sha256": digest(roots),
            "fourier_sha256": digest(fourier)},
    }
    body["payload_sha256"] = hashlib.sha256(canonical(body)).hexdigest()
    return body


def main():
    if sys.flags.optimize:
        raise RuntimeError("C347 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_YAML)
    args = parser.parse_args()
    result = build(args.evaluation)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C347_PRODUCER_PASS coefficients={len(result['bessel_coefficient_rows'])} "
          f"tails={len(result['tail_bracket_rows'])} roots={len(result['self_consistency_root_rows'])} "
          f"fourier={len(result['fourier_rows'])} payload={result['payload_sha256']}")


if __name__ == "__main__":
    main()
