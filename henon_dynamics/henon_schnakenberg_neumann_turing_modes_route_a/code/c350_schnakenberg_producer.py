#!/usr/bin/env python3
"""Canonical exact finite-evidence producer for HCS-C350."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c350_schnakenberg_evidence.json"
DEFAULT_YAML = ROOT / "evaluations/route_a/HCS-C350/2026-09-03.yaml"
SOURCE = "327fc1172cebcdeb17adfd2d8ad12636fbb94f52"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
YAML_RAW = "392e9d205af7e0e7f765bc34889f23cd094434335d68e9ab1cf4853bf32e0d21"
YAML_SEMANTIC = "ed762fcd6f342b51d83c2445e5d862407317fec49d961a73bc1cf20830cc7cda"

CASES = (
    ("kinetic_unstable", "1/100", "9/100", "1", "20", "16"),
    ("kinetic_neutral", "3/16", "5/16", "1", "10", "4"),
    ("equal_diffusion", "1/10", "9/10", "1", "1", "16"),
    ("window_no_mode", "1/10", "9/10", "1", "20", "1"),
    ("one_unstable_mode", "1/10", "9/10", "1", "20", "4"),
    ("two_unstable_modes", "1/10", "9/10", "1", "20", "16"),
    ("lower_endpoint_neutral", "1/10", "9/10", "1", "100/11", "4"),
    ("upper_endpoint_neutral", "1/10", "9/10", "1", "100/11", "25/11"),
    ("double_wall_neutral", "1/9", "8/9", "1", "9", "3"),
)


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


def strict_yaml(path: Path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("anchors forbidden")
    value = yaml.load(raw, Loader=StrictLoader)
    if type(value) is not dict:
        raise TypeError("YAML root")
    return value


def canonical(value) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def fs(value) -> str:
    value = Fraction(value)
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def digest(value) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def invariants(a, b, du, dv):
    s = a + b
    fu, fv, gu, gv = (b - a) / s, s * s, -2 * b / s, -s * s
    tau = fu + gv
    determinant = fu * gv - fv * gu
    B = dv * fu + du * gv
    Q = B * B - 4 * du * dv * determinant
    return s, fu, fv, gu, gv, tau, determinant, B, Q


def mode_state(trace, determinant):
    if determinant < 0:
        return "saddle_unstable"
    if determinant == 0:
        return "neutral_zero"
    if trace < 0:
        return "stable"
    if trace == 0:
        return "neutral_imaginary"
    return "positive_spectral_abscissa"


def strict_count_formula(detj, B, Q, du, dv, ell2):
    """Evaluate the strict floor/ceiling formula using exact root-side tests."""
    if not (B > 0 and Q > 0):
        return None
    vertex = B / (2 * du * dv)
    lower_floor = 0
    while True:
        candidate = lower_floor + 1
        mu = Fraction(candidate * candidate, 1) / ell2
        determinant = du * dv * mu * mu - B * mu + detj
        if mu <= vertex and determinant >= 0:
            lower_floor = candidate
        else:
            break
    upper_ceil = 0
    while True:
        mu = Fraction(upper_ceil * upper_ceil, 1) / ell2
        determinant = du * dv * mu * mu - B * mu + detj
        if mu >= vertex and determinant >= 0:
            break
        upper_ceil += 1
    return max(0, upper_ceil - lower_floor - 1)


def case_rows():
    summaries, modes, walls = [], [], []
    for name, aa, bb, u0, v0, length0 in CASES:
        a, b, du, dv, ell2 = map(Fraction, (aa, bb, u0, v0, length0))
        s, fu, fv, gu, gv, tau, detj, B, Q = invariants(a, b, du, dv)
        kinetic = "stable" if tau < 0 else ("neutral" if tau == 0 else "unstable")
        continuous_window = tau < 0 and B > 0 and Q > 0
        double_wall = tau < 0 and B > 0 and Q == 0
        count_formula_value = (
            strict_count_formula(detj, B, Q, du, dv, ell2)
            if continuous_window else None
        )
        cutoff = 6
        if B > 0:
            while Fraction(cutoff * cutoff, 1) / ell2 <= B / (du * dv):
                cutoff += 1
        unstable, neutral = [], []
        local_modes = []
        for n in range(cutoff + 1):
            mu = Fraction(n * n, 1) / ell2
            trace = tau - (du + dv) * mu
            det = du * dv * mu * mu - B * mu + detj
            state = mode_state(trace, det)
            if tau < 0 and n >= 1 and det < 0:
                unstable.append(n)
            if tau < 0 and n >= 1 and det == 0:
                neutral.append(n)
            local_modes.append({"case": name, "n": n, "mu": fs(mu),
                "trace": fs(trace), "determinant": fs(det), "state": state})
        modes.extend(local_modes)
        summaries.append({
            "case": name, "a": fs(a), "b": fs(b), "d_u": fs(du),
            "d_v": fs(dv), "ell_squared": fs(ell2), "s": fs(s),
            "f_u": fs(fu), "f_v": fs(fv), "g_u": fs(gu), "g_v": fs(gv),
            "tau": fs(tau), "det_J": fs(detj), "B": fs(B), "Q": fs(Q),
            "kinetic_state": kinetic, "continuous_window": continuous_window,
            "double_wall": double_wall, "complete_mode_cutoff": cutoff,
            "unstable_indices": unstable, "neutral_indices": neutral,
            "finite_domain_turing": bool(unstable),
            "count_formula_value": count_formula_value,
        })
        if continuous_window:
            for n in range(1, 5):
                # D(n^2/ell^2)=0 after multiplication by ell^4.
                walls.append({"case": name, "n": n,
                    "ell2_polynomial": [fs(detj), fs(-B * n * n), fs(du * dv * n ** 4)],
                    "discriminant": fs(n ** 4 * Q),
                    "strict_between_roots_is_unstable": True})
    return summaries, modes, walls


def build(evaluation: Path):
    raw = evaluation.read_bytes()
    semantic = strict_yaml(evaluation)
    if hashlib.sha256(raw).hexdigest() != YAML_RAW:
        raise AssertionError("evaluation raw hash")
    if hashlib.sha256(canonical(semantic)).hexdigest() != YAML_SEMANTIC:
        raise AssertionError("evaluation semantic hash")
    summaries, modes, walls = case_rows()
    body = {
        "schema": "hcs-c350-schnakenberg-evidence-v1",
        "candidate_id": "HCS-C350", "obstruction_id": "HEN-O334",
        "evaluation_date": "2026-09-03", "source_commit": SOURCE,
        "fixed_epoch": 1788393600, "scope_literal": SCOPE,
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0", "sha256": EVALUATOR},
        "route_a_yaml": {"relative_path": "evaluations/route_a/HCS-C350/2026-09-03.yaml",
            "raw_sha256": YAML_RAW, "semantic_sha256": YAML_SEMANTIC},
        "model": {
            "domain": "(0,L) with homogeneous Neumann boundary conditions",
            "parameters": "a,b,d_u,d_v,L>0",
            "pde": "u_t=d_u u_xx+a-u+u^2 v; v_t=d_v v_xx+b-u^2 v",
            "equilibrium": "s=a+b; (u_*,v_*)=(s,b/s^2)",
            "neumann_modes": "mu_n=(n*pi/L)^2"},
        "theorem_contract": {
            "equilibrium": "unique positive spatially homogeneous equilibrium only",
            "kinetic": "det J=s^2 and kinetic asymptotic stability iff tau=(b-a)/s-s^2<0",
            "modal": "after complexification, the complete compact-resolvent spectrum is the union of the two eigenvalues of M(mu_n)",
            "continuous_window": "under tau<0, an open unstable wavenumber window exists iff B>0 and Q=B^2-4d_u d_v s^2>0",
            "finite_domain": "linear Turing instability iff some n>=1 satisfies mu_-<mu_n<mu_+",
            "count": "N_unst=max(0,ceil((L/pi)sqrt(mu_+))-floor((L/pi)sqrt(mu_-))-1)",
            "boundaries": "endpoint modes are neutral; equal diffusion has no window; Q=0 is neutral contact; zero diffusion is excluded"},
        "finite_grid": {"case_rows": len(summaries), "mode_rows": len(modes),
            "length_wall_rows": len(walls), "uses_ell_squared": True,
            "records_count_formula": True},
        "collision_boundary": {
            "C311": "Brusselator ODE Hopf normal form, not a spatial two-species Turing spectrum",
            "C304": "scalar fourth-order Cahn-Hilliard shells, not unequal two-species diffusion",
            "C347": "nonlocal Kuramoto probability PDE, not local Schnakenberg kinetics",
            "C202": "scalar Fisher-KPP traveling fronts, not stationary modal instability"},
        "nonclaims": [
            "no nonlinear patterned branch or bifurcation theorem",
            "no nonlinear global well-posedness, attractor, or pattern-selection theorem",
            "no zero-diffusion extension of the uniformly parabolic theorem",
            "no priority claim for Schnakenberg kinetics, Turing instability, or modal analysis",
            "no target arithmetic local data, Euler factors, root number, automorphy, target zero match, Hilbert-Polya operator, or Route B"],
        "references": [
            {"authors": "J. Schnakenberg", "year": 1979,
             "identifier": "DOI:10.1016/0022-5193(79)90042-0",
             "url": "https://www.sciencedirect.com/science/article/pii/0022519379900420",
             "role": "primary source for the named reaction kinetics"},
            {"authors": "A. M. Turing", "year": 1952,
             "identifier": "DOI:10.1098/rstb.1952.0012",
             "url": "https://royalsocietypublishing.org/doi/10.1098/rstb.1952.0012",
             "role": "original reaction-diffusion instability lineage"}],
        "route_a": {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": {
            "claims_target_arithmetic_local_data": False,
            "claims_target_euler_factors": False, "claims_root_number": False,
            "claims_automorphy": False,
            "claims_target_divisor_or_counting_law": False,
            "claims_target_functional_equation": False,
            "claims_target_zero_match": False,
            "claims_hilbert_polya_operator": False, "invokes_route_b": False},
        "case_rows": summaries, "mode_rows": modes, "length_wall_rows": walls,
        "enumeration": {"all_arithmetic_exact": True, "floating_point_used": False,
            "finite_evidence_proves_continuum_theorem": False,
            "case_sha256": digest(summaries), "mode_sha256": digest(modes),
            "length_wall_sha256": digest(walls)},
    }
    body["payload_sha256"] = hashlib.sha256(canonical(body)).hexdigest()
    return body


def main():
    if sys.flags.optimize:
        raise RuntimeError("C350 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_YAML)
    args = parser.parse_args()
    result = build(args.evaluation)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(f"C350_PRODUCER_PASS cases={len(result['case_rows'])} modes={len(result['mode_rows'])} "
          f"walls={len(result['length_wall_rows'])} payload={result['payload_sha256']}")


if __name__ == "__main__":
    main()
