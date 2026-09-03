#!/usr/bin/env python3
"""Producer-independent checker for HCS-C319."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c319_clifford_evidence.json"
DEFAULT_EVAL = ROOT / "evaluations/route_a/HCS-C319/2026-09-03.yaml"
SOURCE = "1ccbfe2d759fe007c6b53c9646e1ab031878b34a"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EVAL_RAW = "59d4dd4f971c7a91d48c31630e903009bb641dc90fd082835b46bd2d15225339"
EVAL_SEMANTIC = "b88d5bc5d78f9b917bfbabcc91d29748172f28b05922d2477570cabef542f49f"
mp.mp.dps = 90


def pairs(items):
    out = {}
    for key, value in items:
        if key in out:
            raise ValueError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def strict_json(path: Path):
    return json.loads(path.read_text(), object_pairs_hook=pairs, parse_constant=lambda x: (_ for _ in ()).throw(ValueError(x)))


class UniqueLoader(yaml.SafeLoader):
    pass


UniqueLoader.yaml_implicit_resolvers = {key: [(tag, pattern) for tag, pattern in values if tag != "tag:yaml.org,2002:timestamp"] for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()}


def mapping(loader, node, deep=False):
    out = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in out:
            raise ValueError("duplicate/non-string YAML key")
        out[key] = loader.construct_object(value_node, deep=deep)
    return out


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, mapping)


def strict_yaml(path: Path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML anchors/aliases forbidden")
    return yaml.load(raw, Loader=UniqueLoader)


def digest(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(v) for v in value.values())
    if type(value) is list:
        return sum(leaves(v) for v in value)
    return 1


def F(text: str) -> Fraction:
    return Fraction(text)


def harmonic_dimension(d: int, ell: int) -> int:
    return math.comb(d + ell, ell) - (math.comb(d + ell - 2, ell - 2) if ell >= 2 else 0)


def close(text: str, expected: mp.mpf, tol=mp.mpf("2e-66")):
    if type(text) is not str or not mp.isfinite(mp.mpf(text)) or abs(mp.mpf(text) - expected) > tol * max(1, abs(expected)):
        raise AssertionError("decimal mismatch")


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C319 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT)
    parser.add_argument("--evaluation", type=Path, default=DEFAULT_EVAL)
    args = parser.parse_args()
    data = strict_json(args.evidence)
    evaluation = strict_yaml(args.evaluation)
    checks = 0
    sem = hashlib.sha256(json.dumps(evaluation, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    if hashlib.sha256(args.evaluation.read_bytes()).hexdigest() != EVAL_RAW or sem != EVAL_SEMANTIC:
        raise AssertionError("evaluation digest")
    checks += 2
    if digest(data) != data.get("payload_sha256"):
        raise AssertionError("payload digest")
    checks += 1
    expected_top = {"schema", "candidate_id", "obstruction_id", "evaluation_date", "fixed_epoch", "source_commit", "scope_literal", "evaluator", "model", "theorem_contract", "pq_rows", "boundary_atlas", "collision_boundary", "route_a", "scope_flags", "nonclaims", "references", "enumeration", "payload_sha256"}
    if set(data) != expected_top:
        raise AssertionError("top-level schema")
    if (data["schema"], data["candidate_id"], data["obstruction_id"], data["evaluation_date"], data["source_commit"], data["scope_literal"], data["fixed_epoch"]) != ("hcs-c319-clifford-product-mcf-v1", "HCS-C319", "HEN-O303", "2026-09-03", SOURCE, SCOPE, 1788393600):
        raise AssertionError("identity")
    if data["evaluator"] != {"version": "0.2.0", "sha256": "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"}:
        raise AssertionError("evaluator")
    expected_model = {"family": "S^p(cos(theta)) x S^q(sin(theta)) in the unit S^(p+q+1)", "dimensions": "integers p,q>=1", "coordinate": "y=sin(theta)^2 in (0,1)", "flow_sign": "mean-curvature vector is the negative area gradient"}
    expected_contract = {"reduction": "y'=2*((p+q)*y-q), with the minimal leaf y=q/(p+q)", "lifespan": "every nonminimal leaf is ancient and collapses at the exact stated finite forward time", "singularity": "both focal collapses are Type I with the stated round-cylinder parabolic limits", "area": "area is strictly decreasing off the minimal leaf with logarithmic derivative -H^2", "minimal_spectrum": "Jacobi operator is Delta+2n, with index n+3 and nullity (p+1)(q+1)"}
    expected_boundary = [{"face": "p,q>=1", "status": "main smooth hypersurface family"}, {"face": "y=q/(p+q)", "status": "stationary minimal Clifford product"}, {"face": "y=0 or y=1", "status": "focal submanifold, not a regular product hypersurface"}, {"face": "p=0 or q=0", "status": "excluded degenerate sphere/double-cover geometry"}, {"face": "t=-infinity", "status": "minimal backward limit, not an added finite slice"}]
    expected_collision = {"C281": "intrinsic homogeneous Ricci flow, not extrinsic spherical mean-curvature flow", "C314": "planar curve shortening, not an isoparametric hypersurface flow"}
    expected_nonclaims = ["No priority is claimed for Clifford products, isoparametric mean-curvature flow, or their classical spectra.", "No classification beyond the declared two-factor product family is claimed.", "The Jacobi operator is source-local and is not a Hilbert--Polya operator.", "No target arithmetic local data, Euler factors, root numbers, automorphy, target divisor, functional equation, or target-zero match is asserted."]
    expected_references = [{"doi": "10.1090/proc/14178", "role": "parallel isoparametric mean-curvature-flow source"}, {"doi": "10.1215/00127094-2009-009", "role": "isoparametric submanifold flow source"}]
    if (data["model"], data["theorem_contract"], data["boundary_atlas"], data["collision_boundary"], data["nonclaims"], data["references"]) != (expected_model, expected_contract, expected_boundary, expected_collision, expected_nonclaims, expected_references):
        raise AssertionError("static theorem/source boundary")
    if data["route_a"] != {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False}:
        raise AssertionError("Route-A")
    if len(data["scope_flags"]) != 9 or any(type(v) is not bool or v for v in data["scope_flags"].values()):
        raise AssertionError("scope")
    checks += 18
    if set(evaluation) != {"schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch", "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256", "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters", "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention", "orbit_cutoff", "precision", "training_data", "forbidden_data", "artifact_paths", "a0", "a1", "a2", "a3", "a4", "tuple", "overall_verdict", "route_b_invocation_allowed", "route_b_lock_reason", "scope_flags", "theorem_status", "finite_evidence_role", "source_owner_tokens"}:
        raise AssertionError("evaluation schema")
    if (evaluation["candidate_id"], evaluation["source_commit"], evaluation["scope_literal"], evaluation["tuple"], evaluation["overall_verdict"], evaluation["route_b_invocation_allowed"], evaluation["scope_flags"]) != ("HCS-C319", SOURCE, SCOPE, data["route_a"]["tuple"], "ROUTE_A_REJECTED", False, data["scope_flags"]):
        raise AssertionError("evaluation semantics")
    if evaluation["artifact_paths"] != ["results/c319_clifford_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"]:
        raise AssertionError("artifact paths")
    checks += 13
    rows = data["pq_rows"]
    if len(rows) != 100 or [(r["p"], r["q"]) for r in rows] != [(p, q) for p in range(1, 11) for q in range(1, 11)]:
        raise AssertionError("p,q enumeration")
    for row in rows:
        if set(row) != {"p", "q", "n", "minimal_y", "principal_curvature_square_first", "principal_curvature_square_second", "minimal_A_squared", "jacobi_potential", "morse_index", "nullity", "enumerated_negative_count", "enumerated_nullity", "branches", "spectrum_cells"}:
            raise AssertionError("pq row schema")
        p, q, n = row["p"], row["q"], row["n"]
        if n != p + q or F(row["minimal_y"]) != Fraction(q, n):
            raise AssertionError("minimal leaf")
        if (F(row["principal_curvature_square_first"]), F(row["principal_curvature_square_second"]), row["minimal_A_squared"], row["jacobi_potential"]) != (Fraction(q, p), Fraction(p, q), n, 2 * n):
            raise AssertionError("minimal geometry")
        if (row["morse_index"], row["nullity"]) != (n + 3, (p + 1) * (q + 1)):
            raise AssertionError("index/nullity")
        checks += 7
        if len(row["branches"]) != 6 or [(r["side"], r["slot"]) for r in row["branches"]] != [(side, slot) for side in ("left", "right") for slot in (1, 2, 3)]:
            raise AssertionError("branch count")
        for rec in row["branches"]:
            if set(rec) != {"side", "slot", "y0", "exp_2nT", "collapse_time", "collapse_focal_submanifold", "parabolic_cylinder", "cylinder_radius_squared", "type_I_A2_residue", "initial_H_squared", "area_to_minimal_ratio"}:
                raise AssertionError("branch schema")
            side, slot, y0 = rec["side"], rec["slot"], F(rec["y0"])
            star = Fraction(q, n)
            expected_y = Fraction(slot, 4) * star if side == "left" else star + Fraction(slot, 4) * (1 - star)
            if y0 != expected_y:
                raise AssertionError("branch initial value")
            expv = Fraction(q, q - n * y0) if side == "left" else Fraction(p, n * y0 - q)
            if F(rec["exp_2nT"]) != expv or rec["type_I_A2_residue"] != "1/2":
                raise AssertionError("branch exact data")
            close(rec["collapse_time"], mp.log(mp.mpf(expv.numerator) / expv.denominator) / (2 * n))
            hsq = Fraction((n * y0 - q) ** 2, y0 * (1 - y0))
            if F(rec["initial_H_squared"]) != hsq:
                raise AssertionError("H squared")
            y0_mp = mp.mpf(y0.numerator) / y0.denominator
            star_mp = mp.mpf(q) / n
            area_ratio = (y0_mp / star_mp) ** (mp.mpf(q) / 2)
            area_ratio *= ((1 - y0_mp) / (1 - star_mp)) ** (mp.mpf(p) / 2)
            close(rec["area_to_minimal_ratio"], area_ratio)
            if not (mp.mpf(rec["area_to_minimal_ratio"]) < 1 and hsq > 0):
                raise AssertionError("strict off-minimal area dissipation")
            # The independently reconstructed vector field gives
            # d(log A)/dt=(q/(2y)-p/(2(1-y)))y'=-H^2.
            log_area_derivative = (Fraction(q, 2) / y0 - Fraction(p, 2) / (1 - y0)) * 2 * (n * y0 - q)
            if log_area_derivative != -hsq:
                raise AssertionError("area dissipation identity")
            if side == "left":
                expected = (f"S^{p}", f"S^{q}(sqrt(2*{q})) x R^{p}", 2 * q)
            else:
                expected = (f"S^{q}", f"S^{p}(sqrt(2*{p})) x R^{q}", 2 * p)
            if (rec["collapse_focal_submanifold"], rec["parabolic_cylinder"], rec["cylinder_radius_squared"]) != expected:
                raise AssertionError("collapse labels")
            checks += 12
        neg = null = 0
        if len(row["spectrum_cells"]) != 36 or [(r["ell"], r["m"]) for r in row["spectrum_cells"]] != [(ell, m) for ell in range(6) for m in range(6)]:
            raise AssertionError("spectrum count")
        for rec in row["spectrum_cells"]:
            if set(rec) != {"ell", "m", "minus_laplacian_eigenvalue", "multiplicity", "relation"}:
                raise AssertionError("spectrum schema")
            ell, m = rec["ell"], rec["m"]
            lam = Fraction(n * ell * (ell + p - 1), p) + Fraction(n * m * (m + q - 1), q)
            mult = harmonic_dimension(p, ell) * harmonic_dimension(q, m)
            relation = "below_2n" if lam < 2 * n else "equal_2n" if lam == 2 * n else "above_2n"
            if F(rec["minus_laplacian_eigenvalue"]) != lam or rec["multiplicity"] != mult or rec["relation"] != relation:
                raise AssertionError("spectrum cell")
            neg += mult if relation == "below_2n" else 0
            null += mult if relation == "equal_2n" else 0
            checks += 4
        if (neg, null, row["enumerated_negative_count"], row["enumerated_nullity"]) != (n + 3, (p + 1) * (q + 1), n + 3, (p + 1) * (q + 1)):
            raise AssertionError("enumerated spectral count")
        checks += 4
    enum = data["enumeration"]
    if set(enum) != {"pq_rows", "branch_rows", "spectrum_cells", "audited_leaf_count"}:
        raise AssertionError("enumeration schema")
    if (enum["pq_rows"], enum["branch_rows"], enum["spectrum_cells"]) != (100, 600, 3600):
        raise AssertionError("enumeration")
    body = dict(data)
    body.pop("payload_sha256")
    if enum["audited_leaf_count"] != leaves(body):
        raise AssertionError("leaf count")
    checks += 4
    print(f"C319 independent checker: PASS ({checks} checks)")


if __name__ == "__main__":
    main()
