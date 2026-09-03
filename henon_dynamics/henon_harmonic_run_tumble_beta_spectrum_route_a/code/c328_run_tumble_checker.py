#!/usr/bin/env python3
"""Producer-independent checker for HCS-C328."""
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
DEFAULT = ROOT / "results/c328_run_tumble_evidence.json"
DEFAULT_EVAL = ROOT / "evaluations/route_a/HCS-C328/2026-09-03.yaml"
SOURCE = "1aba1f6fd0cf81baa7c137a2ce7ce3d097ba63fc"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EVAL_RAW = "d95689db325195f9c14bb38f739c66003d53eb3e53a08bf98de78ad7b045787f"
EVAL_SEMANTIC = "64a9be4c652799d46ed59bbfb91e8835e0ff20726d3b00f38d33019a1d6963b8"
N = 8
PARAMETERS = (
    (Fraction(1), Fraction(1), Fraction(1, 2)),
    (Fraction(1), Fraction(2), Fraction(1)),
    (Fraction(2), Fraction(3), Fraction(3)),
    (Fraction(2), Fraction(5), Fraction(4)),
    (Fraction(3), Fraction(4), Fraction(15, 2)),
    (Fraction(4), Fraction(7), Fraction(12)),
    (Fraction(1), Fraction(3), Fraction(1, 3)),
    (Fraction(2), Fraction(1), Fraction(1, 2)),
    (Fraction(3), Fraction(5), Fraction(2)),
    (Fraction(5), Fraction(2), Fraction(7, 2)),
    (Fraction(6), Fraction(11), Fraction(5, 2)),
    (Fraction(7), Fraction(13), Fraction(9, 2)),
)
TIMES = (Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(1), Fraction(2))
mp.mp.dps = 100


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
    expected = mp.nstr(value, 72, strip_zeros=False, min_fixed=-90, max_fixed=90)
    if text != expected:
        raise AssertionError("noncanonical decimal")
    return value


def close_decimal(text: str, expected: mp.mpf, tol=mp.mpf("3e-70")) -> None:
    value = canonical_decimal(text)
    if abs(value - expected) > tol * max(1, abs(expected)):
        raise AssertionError("decimal mismatch")


def mpq(value: Fraction) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def rising(value: Fraction, n: int) -> Fraction:
    out = Fraction(1)
    for j in range(n):
        out *= value + j
    return out


def rank(matrix: list[list[Fraction]]) -> int:
    work = [row[:] for row in matrix]
    rows = len(work)
    cols = len(work[0]) if rows else 0
    pivot_row = 0
    for col in range(cols):
        pivot = next((r for r in range(pivot_row, rows) if work[r][col]), None)
        if pivot is None:
            continue
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        scale = work[pivot_row][col]
        work[pivot_row] = [x / scale for x in work[pivot_row]]
        for r in range(rows):
            if r != pivot_row and work[r][col]:
                factor = work[r][col]
                work[r] = [a - factor * b for a, b in zip(work[r], work[pivot_row])]
        pivot_row += 1
        if pivot_row == rows:
            break
    return pivot_row


def generator(mu: Fraction, speed: Fraction, lam: Fraction) -> list[list[Fraction]]:
    """Columns are L applied to A_0,B_0,A_1,B_1,...,A_N,B_N."""
    size = 2 * (N + 1)
    out = [[Fraction(0) for _ in range(size)] for _ in range(size)]
    for n in range(N + 1):
        a, b = 2*n, 2*n + 1
        out[a][a] = -n * mu
        out[b][b] = -n * mu - 2 * lam
        if n:
            out[2*(n-1)+1][a] = n * speed
            out[2*(n-1)][b] = n * speed
    return out


def geometric_multiplicity(matrix: list[list[Fraction]], eigenvalue: Fraction) -> int:
    shifted = [row[:] for row in matrix]
    for j in range(len(shifted)):
        shifted[j][j] -= eigenvalue
    return len(shifted) - rank(shifted)


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C328 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_EVAL)
    args = parser.parse_args()
    data = strict_json(args.evidence)
    evaluation = strict_yaml(args.evaluation)
    checks = 0

    if hashlib.sha256(args.evaluation.read_bytes()).hexdigest() != EVAL_RAW or semantic_hash(evaluation) != EVAL_SEMANTIC:
        raise AssertionError("evaluation digest")
    if payload_hash(data) != data.get("payload_sha256"):
        raise AssertionError("payload digest")
    checks += 3

    top = {
        "schema", "candidate_id", "obstruction_id", "evaluation_date", "fixed_epoch",
        "source_commit", "scope_literal", "evaluator", "evaluation_lock", "model",
        "theorem_contract", "parameter_rows", "boundary_atlas", "collision_boundary", "route_a",
        "scope_flags", "nonclaims", "references", "enumeration", "payload_sha256",
    }
    if set(data) != top:
        raise AssertionError("top-level schema")
    if (data["schema"], data["candidate_id"], data["obstruction_id"], data["evaluation_date"],
            data["fixed_epoch"], data["source_commit"], data["scope_literal"]) != (
            "hcs-c328-harmonic-run-tumble-v1", "HCS-C328", "HEN-O312", "2026-09-03",
            1788393600, SOURCE, SCOPE):
        raise AssertionError("identity")
    if data["evaluator"] != {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR}:
        raise AssertionError("evaluator")
    if data["evaluation_lock"] != {
            "relative_path": "evaluations/route_a/HCS-C328/2026-09-03.yaml",
            "raw_sha256": EVAL_RAW, "semantic_sha256": EVAL_SEMANTIC}:
        raise AssertionError("evaluation lock")
    expected_model = {
        "state": "(x,sigma) in [-v/mu,v/mu] times {-1,+1}",
        "deterministic_motion": "dx/dt=v*sigma-mu*x",
        "jump_rule": "sigma flips sign at rate lambda",
        "generator": "L f_sigma=(v*sigma-mu*x)*partial_x f_sigma+lambda*(f_-sigma-f_sigma)",
        "parameters": "mu,v,lambda strictly positive",
    }
    expected_contract = {
        "stationary_marginal": "scaled y=mu*x/v has density Gamma(alpha+1/2)/(sqrt(pi)Gamma(alpha))*(1-y^2)^(alpha-1)",
        "stationary_components": "p_+=(1+y)p/2 and p_-=(1-y)p/2",
        "moments": "all odd x moments and all E[sigma*x^(2n)] vanish; E[x^(2n)]=(v/mu)^(2n)*(1/2)_n/(alpha+1/2)_n",
        "correlation": "for t>=0 the complete stationary (x,sigma) correlation matrix is R(t)=exp(A t)Sigma, with a Jordan limit at mu=2lambda; R(-t)=R(t)^T",
        "polynomial_filter": "P_N=span{x^n,sigma*x^n:0<=n<=N} is invariant with two triangular eigenvalue ladders",
        "resonance": "for v>0 and 2lambda/mu=k integer, repeated eigenvalues are size-two Jordan blocks iff k is odd and are semisimple iff k is even",
        "spectrum_boundary": "the claim concerns every finite polynomial filter and not the full L2 spectrum",
    }
    expected_boundary = [
        {"face": "mu=0", "status": "unconfined integrated telegraph motion; no compact stationary probability on the line"},
        {"face": "lambda=0", "status": "orientation sectors do not communicate and arbitrary mixtures of the two attracting endpoint atoms are stationary"},
        {"face": "v=0 with lambda>0", "status": "the joint stationary law is delta_0 tensor the uniform orientation law and all repeated polynomial eigenvalues are semisimple because couplings vanish"},
        {"face": "v=lambda=0", "status": "position contracts to zero while orientation is frozen, so every orientation mixture over delta_0 is stationary"},
        {"face": "mu=2lambda", "status": "first odd resonance with t exp(-mu t) in stationary correlations"},
        {"face": "alpha<1, alpha=1, alpha>1", "status": "marginal density respectively diverges, is uniform, or vanishes at the support endpoints"},
        {"face": "support endpoints", "status": "open-interval densities may be integrably singular but carry no atoms for positive rates"},
        {"face": "full L2 generator", "status": "not classified; only invariant finite polynomial filters are claimed"},
    ]
    expected_collision = {
        "C213": "the circular telegraph process is unconfined in position and closes Fourier blocks rather than a harmonic beta law",
        "C237": "harmonic Kramers--Langevin has Gaussian Mehler dynamics rather than compact beta support",
        "C265": "exponential Hawkes dynamics is a self-exciting affine jump process rather than a symmetric two-velocity PDMP",
    }
    expected_nonclaims = [
        "No priority is claimed for harmonic run-and-tumble stationary laws or telegraph-noise calculations.",
        "No full L2 spectrum, completeness theorem, or spectral expansion of arbitrary observables is claimed.",
        "Finite parameter and degree-eight receipts do not prove the all-parameter finite-filter theorem.",
        "The Markov generator is not self-adjoint here and is not a Hilbert--Polya operator.",
        "No target arithmetic local data, Euler factors, root numbers, automorphy, target divisor, functional equation, or target-zero match is asserted.",
    ]
    expected_references = [
        {"doi": "10.1103/PhysRevE.99.032132", "role": "one-dimensional confined run-and-tumble stationary and relaxation source"},
        {"doi": "10.1088/1742-5468/ac014d", "role": "harmonic run-and-tumble field-theory and stationary component source"},
    ]
    if (data["model"], data["theorem_contract"], data["boundary_atlas"], data["collision_boundary"],
            data["nonclaims"], data["references"]) != (expected_model, expected_contract, expected_boundary,
                                                        expected_collision, expected_nonclaims, expected_references):
        raise AssertionError("static theorem/source boundary")
    expected_route = {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
                      "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}
    if data["route_a"] != expected_route:
        raise AssertionError("Route-A")
    flag_keys = {
        "claims_target_arithmetic_local_data", "claims_target_euler_factors", "claims_root_number",
        "claims_automorphy", "claims_target_divisor_or_counting_law", "claims_target_functional_equation",
        "claims_target_zero_match", "claims_hilbert_polya_operator", "invokes_route_b",
    }
    if set(data["scope_flags"]) != flag_keys or any(type(x) is not bool or x for x in data["scope_flags"].values()):
        raise AssertionError("scope flags")
    checks += 14

    eval_top = {
        "schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch",
        "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256",
        "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters",
        "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention",
        "orbit_cutoff", "precision", "training_data", "forbidden_data", "artifact_paths", "a0", "a1",
        "a2", "a3", "a4", "tuple", "overall_verdict", "route_b_invocation_allowed",
        "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role", "source_owner_tokens",
    }
    if set(evaluation) != eval_top:
        raise AssertionError("evaluation schema")
    layer_keys = {"verdict", "evidence_status", "strongest_evidence", "strongest_failure"}
    if any(type(evaluation[name]) is not dict or set(evaluation[name]) != layer_keys for name in ("a0", "a1", "a2", "a3", "a4")):
        raise AssertionError("evaluation layer schema")
    if evaluation["artifact_paths"] != ["results/c328_run_tumble_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"]:
        raise AssertionError("artifact paths")
    expected_layers = {
        "a0": {"verdict": "A0_FAIL", "evidence_status": "PROVED",
               "strongest_evidence": "no arithmetic source exists",
               "strongest_failure": "drift and flip parameters do not intrinsically encode rational primes or prime powers"},
        "a1": {"verdict": "A1_FAIL", "evidence_status": "PROVED",
               "strongest_evidence": "the source Markov generator and invariant law are exact",
               "strongest_failure": "stochastic flips do not define a natural primitive deterministic orbit ledger carrying arithmetic labels"},
        "a2": {"verdict": "A2_FAIL", "evidence_status": "STOP_SCOPED",
               "strongest_evidence": "none",
               "strongest_failure": "no primitive-orbit zeta or target determinant is defined"},
        "a3": {"verdict": "A3_FAIL", "evidence_status": "STOP_SCOPED",
               "strongest_evidence": "a finite-degree polynomial filtration is invariant",
               "strongest_failure": "filtered generator eigenvalues are not a target analytic continuation or Weil compression"},
        "a4": {"verdict": "A4_FAIL", "evidence_status": "STOP_SCOPED",
               "strongest_evidence": "a non-self-adjoint Markov generator exists",
               "strongest_failure": "no natural unitary, scattering, or Hamiltonian lift preserving a prime clock is available"},
    }
    if any(evaluation[name] != expected_layers[name] for name in expected_layers):
        raise AssertionError("evaluation layer semantics")
    if (evaluation["schema"], evaluation["candidate_id"], evaluation["obstruction_id"],
            evaluation["evaluation_date"], evaluation["source_commit"], evaluation["fixed_epoch"],
            evaluation["scope_literal"], evaluation["evaluator_authority"], evaluation["evaluator_version"],
            evaluation["evaluator_authority_sha256"], evaluation["tuple"], evaluation["overall_verdict"],
            evaluation["route_b_invocation_allowed"], evaluation["scope_flags"], evaluation["theorem_status"],
            evaluation["finite_evidence_role"], evaluation["source_owner_tokens"]) != (
            "route-a-evaluation-v0.2.0", "HCS-C328", "HEN-O312", "2026-09-03", SOURCE, 1788393600,
            SCOPE, "flow_systems/skills/route-a-evaluator.md", "0.2.0", EVALUATOR,
            expected_route["tuple"], "ROUTE_A_REJECTED", False, data["scope_flags"], "PROVABLE_AS_STATED",
            "convention and implementation receipt, not proof",
            ["10.1103/PhysRevE.99.032132", "10.1088/1742-5468/ac014d"]):
        raise AssertionError("evaluation semantics")
    checks += 39

    rows = data["parameter_rows"]
    if type(rows) is not list or len(rows) != len(PARAMETERS):
        raise AssertionError("parameter row count")
    row_keys = {
        "parameter_id", "mu", "speed_v", "lambda", "alpha_lambda_over_mu", "support_half_width",
        "beta_normalization_y", "beta_normalization_x", "endpoint_exponent_marginal",
        "endpoint_exponent_suppressed_component", "component_masses", "moments", "stationary_covariance",
        "correlations", "filter_degree", "spectral_cells", "resonance_integer", "resonance_class", "resonances",
    }
    moment_keys = {"n", "even_position_moment", "odd_position_moment", "sigma_even_position_moment", "sigma_odd_position_moment"}
    covariance_keys = {"xx", "x_sigma", "sigma_x", "sigma_sigma"}
    correlation_keys = {"time", "xx", "x_sigma", "sigma_x", "sigma_sigma"}
    spectral_keys = {"sector", "degree", "diagonal_eigenvalue"}
    resonance_keys = {"a_degree", "b_degree", "eigenvalue", "algebraic_multiplicity", "geometric_multiplicity", "jordan_class"}
    moment_total = correlation_total = spectral_total = resonance_total = 0
    for index, (row, params) in enumerate(zip(rows, PARAMETERS), 1):
        mu, speed, lam = params
        alpha, scale = lam / mu, speed / mu
        if type(row) is not dict or set(row) != row_keys:
            raise AssertionError("parameter row schema")
        if (row["parameter_id"], canonical_fraction(row["mu"]), canonical_fraction(row["speed_v"]),
                canonical_fraction(row["lambda"]), canonical_fraction(row["alpha_lambda_over_mu"]),
                canonical_fraction(row["support_half_width"]), row["filter_degree"]) != (
                f"rt-{index:02d}", mu, speed, lam, alpha, scale, N):
            raise AssertionError("parameter identity")
        alpha_mp, scale_mp = mpq(alpha), mpq(scale)
        normal = mp.gamma(alpha_mp + mp.mpf("0.5")) / (mp.sqrt(mp.pi) * mp.gamma(alpha_mp))
        close_decimal(row["beta_normalization_y"], normal)
        close_decimal(row["beta_normalization_x"], normal / scale_mp)
        if (canonical_fraction(row["endpoint_exponent_marginal"]),
                canonical_fraction(row["endpoint_exponent_suppressed_component"]), row["component_masses"]) != (
                alpha - 1, alpha, ["1/2", "1/2"]):
            raise AssertionError("stationary beta metadata")

        if type(row["moments"]) is not list or len(row["moments"]) != N + 1:
            raise AssertionError("moment count")
        for n, cell in enumerate(row["moments"]):
            if type(cell) is not dict or set(cell) != moment_keys or cell["n"] != n:
                raise AssertionError("moment schema/coordinate")
            unit_even = rising(Fraction(1, 2), n) / rising(alpha + Fraction(1, 2), n)
            sigma_odd = scale ** (2*n + 1) * rising(Fraction(1, 2), n + 1) / rising(alpha + Fraction(1, 2), n + 1)
            if (canonical_fraction(cell["even_position_moment"]), canonical_fraction(cell["odd_position_moment"]),
                    canonical_fraction(cell["sigma_even_position_moment"]),
                    canonical_fraction(cell["sigma_odd_position_moment"])) != (
                    scale ** (2*n) * unit_even, Fraction(0), Fraction(0), sigma_odd):
                raise AssertionError("moment value")
            checks += 9
        moment_total += len(row["moments"])

        if type(row["stationary_covariance"]) is not dict or set(row["stationary_covariance"]) != covariance_keys:
            raise AssertionError("covariance schema")
        mu_m, speed_m, lam_m = mpq(mu), mpq(speed), mpq(lam)
        covariance = {
            "xx": speed_m**2 / (mu_m * (mu_m + 2*lam_m)),
            "x_sigma": speed_m / (mu_m + 2*lam_m),
            "sigma_x": speed_m / (mu_m + 2*lam_m),
            "sigma_sigma": mp.mpf(1),
        }
        for key in sorted(covariance):
            close_decimal(row["stationary_covariance"][key], covariance[key])
        if type(row["correlations"]) is not list or len(row["correlations"]) != len(TIMES):
            raise AssertionError("correlation count")
        jordan = mu == 2*lam
        for cell, time in zip(row["correlations"], TIMES):
            if type(cell) is not dict or set(cell) != correlation_keys or canonical_fraction(cell["time"]) != time:
                raise AssertionError("correlation schema/coordinate")
            tt = mpq(time)
            e_mu, e_lam = mp.exp(-mu_m*tt), mp.exp(-2*lam_m*tt)
            off = speed_m*tt*e_mu if jordan else speed_m*(e_lam-e_mu)/(mu_m-2*lam_m)
            expected = {
                "xx": e_mu*covariance["xx"] + off*covariance["x_sigma"],
                "x_sigma": e_mu*covariance["x_sigma"] + off,
                "sigma_x": e_lam*covariance["sigma_x"],
                "sigma_sigma": e_lam,
            }
            for key in sorted(expected):
                close_decimal(cell[key], expected[key])
            checks += 11
        correlation_total += len(row["correlations"])

        expected_spectral = []
        for n in range(N + 1):
            expected_spectral.extend((
                {"sector": "A", "degree": n, "diagonal_eigenvalue": str(-n*mu) if (-n*mu).denominator == 1 else f"{(-n*mu).numerator}/{(-n*mu).denominator}"},
                {"sector": "B", "degree": n, "diagonal_eigenvalue": str(-n*mu-2*lam) if (-n*mu-2*lam).denominator == 1 else f"{(-n*mu-2*lam).numerator}/{(-n*mu-2*lam).denominator}"},
            ))
        if type(row["spectral_cells"]) is not list or row["spectral_cells"] != expected_spectral:
            raise AssertionError("spectral cells")
        if any(type(cell) is not dict or set(cell) != spectral_keys for cell in row["spectral_cells"]):
            raise AssertionError("spectral schema")
        spectral_total += len(row["spectral_cells"])

        ratio = 2*lam/mu
        expected_resonances = []
        if ratio.denominator == 1:
            k = ratio.numerator
            expected_class = "odd_integer_jordan" if k % 2 else "even_integer_semisimple"
            matrix = generator(mu, speed, lam)
            for n in range(k, N + 1):
                eigenvalue = -n*mu
                geometric = geometric_multiplicity(matrix, eigenvalue)
                if geometric != (1 if k % 2 else 2):
                    raise AssertionError("independent resonance rank")
                expected_resonances.append({
                    "a_degree": n, "b_degree": n-k,
                    "eigenvalue": str(eigenvalue) if eigenvalue.denominator == 1 else f"{eigenvalue.numerator}/{eigenvalue.denominator}",
                    "algebraic_multiplicity": 2, "geometric_multiplicity": geometric,
                    "jordan_class": "one_size_2_block" if k % 2 else "two_size_1_blocks",
                })
            expected_integer = k
        else:
            expected_integer, expected_class = None, "noninteger_nonresonant"
        if (row["resonance_integer"], row["resonance_class"], row["resonances"]) != (
                expected_integer, expected_class, expected_resonances):
            raise AssertionError("resonance classification")
        if any(type(cell) is not dict or set(cell) != resonance_keys for cell in row["resonances"]):
            raise AssertionError("resonance schema")
        resonance_total += len(row["resonances"])
        checks += 36 + 3*len(expected_resonances)

    enumeration = data["enumeration"]
    enum_keys = {"parameter_rows", "moment_rows", "correlation_rows", "spectral_cells", "resonance_rows", "audited_leaf_count"}
    if set(enumeration) != enum_keys:
        raise AssertionError("enumeration schema")
    if (enumeration["parameter_rows"], enumeration["moment_rows"], enumeration["correlation_rows"],
            enumeration["spectral_cells"], enumeration["resonance_rows"]) != (
            12, moment_total, correlation_total, spectral_total, resonance_total):
        raise AssertionError("enumeration")
    body = dict(data)
    body.pop("payload_sha256")
    if enumeration["audited_leaf_count"] != leaves(body):
        raise AssertionError("leaf count")
    checks += 7
    print(f"C328 independent checker: PASS ({checks} checks)")


if __name__ == "__main__":
    main()
