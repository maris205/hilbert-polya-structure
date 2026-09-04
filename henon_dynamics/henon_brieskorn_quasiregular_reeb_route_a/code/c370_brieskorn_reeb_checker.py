#!/usr/bin/env python3
"""Independent fail-closed checker for HCS-C370; imports no producer code."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("c370 checker refuses optimized Python")

import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c370_brieskorn_reeb_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C370/2026-09-04.yaml"
SOURCE = "c6553f02d928c6aa05400ded57746869a85f0238"
AUTHORITY_SHA = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
YAML_RAW_SHA = "d452c49bc188141a22e60a5f3e5b7dacd59ecea99de39ce6e33d1f492d90ade1"
YAML_SEMANTIC_SHA = "5af9e8955b35292f87189a87fa1cf7a6ca15aa97d339cba822da940f6a3c3eda"

TOP_KEYS = {
    "schema", "candidate_id", "obstruction_id", "evaluation_date", "source_commit",
    "fixed_epoch", "scope_literal", "evaluator", "route_a_yaml", "parameter_domain",
    "conventions", "theorem_contract", "finite_grid", "collision_boundary", "nonclaims",
    "references", "scope_flags", "route_a", "finite_evidence_role", "pair_rows",
    "orbit_type_rows", "rotation_rows", "invariant_rows", "section_sha256", "payload_sha256",
}
YAML_KEYS = {
    "schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch",
    "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256",
    "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters",
    "parameter_provenance", "arithmetic_origin", "clock", "normalization",
    "determinant_convention", "orbit_cutoff", "precision", "training_data", "forbidden_data",
    "artifact_paths", "a0", "a1", "a2", "a3", "a4", "tuple", "overall_verdict",
    "route_b_invocation_allowed", "route_b_lock_reason", "scope_flags", "theorem_status",
    "finite_evidence_role", "source_owner_tokens",
}
TUPLE = [
    "A0_WEAK_ARITHMETIC_RELATION", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"
]
FLAGS = {
    key: False
    for key in (
        "claims_target_arithmetic_local_data", "claims_target_euler_factors", "claims_root_number",
        "claims_automorphy", "claims_target_divisor_or_counting_law",
        "claims_target_functional_equation", "claims_target_zero_match",
        "claims_hilbert_polya_operator", "invokes_route_b",
    )
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
        path.read_text(),
        object_pairs_hook=unique_object,
        parse_constant=lambda token: (_ for _ in ()).throw(ValueError(f"nonfinite {token}")),
    )


def canonical(value) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def digest(value) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def typed_equal(actual, expected) -> bool:
    if type(actual) is not type(expected):
        return False
    if type(actual) is dict:
        return set(actual) == set(expected) and all(
            typed_equal(actual[key], expected[key]) for key in expected
        )
    if type(actual) is list:
        return len(actual) == len(expected) and all(
            typed_equal(left, right) for left, right in zip(actual, expected)
        )
    return actual == expected


def exact(actual, expected, label: str) -> None:
    if not typed_equal(actual, expected):
        raise AssertionError(f"typed value mismatch at {label}")


def exact_keys(value, expected, label: str) -> None:
    if type(value) is not dict or set(value) != set(expected):
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


def validate_yaml(path: Path) -> None:
    raw = path.read_bytes()
    value = load_yaml(path)
    assert hashlib.sha256(raw).hexdigest() == YAML_RAW_SHA
    assert digest(value) == YAML_SEMANTIC_SHA
    exact_keys(value, YAML_KEYS, "evaluation YAML")
    frozen = {
        "schema": "route-a-evaluation-v0.2.0",
        "candidate_id": "HCS-C370",
        "title": "Quasiregular Reeb dynamics on the Brieskorn links Sigma(2,p,q)",
        "evaluation_date": "2026-09-04",
        "source_commit": SOURCE,
        "fixed_epoch": 1788480000,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "evaluator_authority": "flow_systems/skills/route-a-evaluator.md",
        "evaluator_version": "0.2.0",
        "evaluator_authority_sha256": AUTHORITY_SHA,
        "obstruction_id": "HEN-O354",
        "artifact_paths": [
            "results/c370_brieskorn_reeb_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"
        ],
        "tuple": TUPLE,
        "overall_verdict": "ROUTE_A_EXPLORATORY",
        "route_b_invocation_allowed": False,
        "route_b_lock_reason": "no target Euler factor, root number, divisor, functional equation, or target-zero identification is present",
        "scope_flags": FLAGS,
        "theorem_status": "PROVABLE_AS_STATED",
        "finite_evidence_role": "exhaustive finite divisibility ledgers, exact rotation and index rows, and hostile tests are regression evidence only; analytic arguments prove the all-parameter statements",
        "source_owner_tokens": ["10.1112/blms/bdv088", "10.1515/FORUM.2008.016"],
    }
    for key, expected in frozen.items():
        exact(value[key], expected, f"yaml.{key}")
    statuses = ("PROVED", "PROVED", "STOP_SCOPED", "STOP_SCOPED", "FORMAL_ONLY")
    for key, verdict, status in zip(("a0", "a1", "a2", "a3", "a4"), TUPLE, statuses):
        exact_keys(
            value[key],
            {"verdict", "evidence_status", "strongest_evidence", "strongest_failure"},
            f"yaml.{key}",
        )
        exact(value[key]["verdict"], verdict, f"yaml.{key}.verdict")
        exact(value[key]["evidence_status"], status, f"yaml.{key}.evidence_status")
    for key in (
        "candidate_definition", "family", "phase_space", "dynamics", "parameters",
        "parameter_provenance", "arithmetic_origin", "clock", "normalization",
        "determinant_convention", "orbit_cutoff", "precision", "training_data", "forbidden_data",
    ):
        assert type(value[key]) is str and value[key], key


def update_cell(hasher, p: int, q: int, time: int, label: str, dimension: int) -> None:
    hasher.update(f"{p}|{q}|{time}|{label}|{dimension}\n".encode("ascii"))


def classify(p: int, q: int, time: int):
    if time % (2 * p * q) == 0:
        return "principal_link", 3
    if time % (2 * p) == 0:
        return "exceptional_01", 1
    if time % (2 * q) == 0:
        return "exceptional_02", 1
    if time % (p * q) == 0:
        return "exceptional_12", 1
    return "empty", -1


def frac(value: Fraction):
    return {"numerator": value.numerator, "denominator": value.denominator}


def sequence_digest(values) -> str:
    return digest(list(values))


def expected_rows():
    pairs = [
        (p, q)
        for p in range(3, 102, 2)
        for q in range(p + 2, 102, 2)
        if math.gcd(p, q) == 1
    ]
    pair_rows, orbit_rows, rotation_rows, invariant_rows = [], [], [], []
    global_hasher = hashlib.sha256()
    fixed_cells = 0
    cz_cells = 0
    for p, q in pairs:
        principal = 2 * p * q
        local = hashlib.sha256()
        counts = {key: 0 for key in (
            "empty", "exceptional_01", "exceptional_02", "exceptional_12", "principal_link"
        )}
        for time in range(1, principal + 1):
            label, dim = classify(p, q, time)
            counts[label] += 1
            update_cell(local, p, q, time, label, dim)
            update_cell(global_hasher, p, q, time, label, dim)
            fixed_cells += 1
        pair_rows.append({
            "p": p, "q": q, "principal_period": principal,
            "fixed_time_cell_count": principal, "fixed_class_counts": counts,
            "fixed_time_sha256": local.hexdigest(),
        })
        for label, support, period, isotropy, dimension, quotient_dimension in (
            ("exceptional_01", [0, 1], 2 * p, q, 1, 0),
            ("exceptional_02", [0, 2], 2 * q, p, 1, 0),
            ("exceptional_12", [1, 2], p * q, 2, 1, 0),
            ("principal", [0, 1, 2], principal, 1, 3, 2),
        ):
            orbit_rows.append({
                "p": p, "q": q, "label": label, "support": support,
                "primitive_period": period, "isotropy_order": isotropy,
                "morse_bott_dimension": dimension,
                "orbit_quotient_dimension": quotient_dimension,
            })
        for label, numerator, denominator in (
            ("exceptional_01", 2 * p, q),
            ("exceptional_02", 2 * q, p),
            ("exceptional_12", p * q, 2),
        ):
            rho = Fraction(numerator, denominator)
            values = [
                2 * ((cover * rho.numerator) // rho.denominator) + 1
                for cover in range(1, rho.denominator)
            ]
            cz_cells += len(values)
            rotation_rows.append({
                "p": p, "q": q, "label": label,
                "rotation_number": frac(rho),
                "return_determinant": "4*sin(pi*rho)^2",
                "return_determinant_argument": frac(rho),
                "first_degenerate_cover": rho.denominator,
                "nondegenerate_cover_count": rho.denominator - 1,
                "cz_formula": "2*floor(cover*rho)+1 for 1<=cover<first_degenerate_cover",
                "cz_sequence_sha256": sequence_digest(values),
                "trivialization": "ambient missing-coordinate complex-line trivialization",
            })
        chi = Fraction(-p * q + 2 * p + 2 * q, 2 * p * q)
        rs = -2 * p * q + 4 * p + 4 * q
        sign = "positive" if rs > 0 else "negative" if rs < 0 else "zero"
        invariant_rows.append({
            "p": p, "q": q, "base_orbifold_orders": [2, p, q],
            "orbifold_euler_characteristic": frac(chi), "orbifold_geometry_sign": sign,
            "principal_robbin_salamon_index": rs,
            "index_identity": "mu_RS=2*(2*p*q)*chi_orb",
            "principal_trivialization": "standard Milnor-fiber capping trivialization",
        })
    grid = {
        "pair_count": len(pairs), "fixed_time_cell_count": fixed_cells,
        "orbit_type_row_count": len(orbit_rows), "rotation_row_count": len(rotation_rows),
        "nondegenerate_cz_cell_count": cz_cells, "invariant_row_count": len(invariant_rows),
        "fixed_time_storage": "all cells recomputed; canonical streaming digest plus exact per-pair class counts and digests stored",
        "fixed_time_encoding": "ASCII p|q|time|class|dimension followed by newline in lexicographic pair and increasing-time order",
        "fixed_time_sha256": global_hasher.hexdigest(),
    }
    return pair_rows, orbit_rows, rotation_rows, invariant_rows, grid


def quick_semantic_gate(obj) -> None:
    """Reject common repaired-hash attacks before the exhaustive digest pass."""
    pairs = [
        (p, q)
        for p in range(3, 102, 2)
        for q in range(p + 2, 102, 2)
        if math.gcd(p, q) == 1
    ]
    grid = obj["finite_grid"]
    exact(grid["pair_count"], 1003, "quick.grid.pairs")
    exact(grid["fixed_time_cell_count"], 5_469_178, "quick.grid.fixed")
    exact(grid["orbit_type_row_count"], 4_012, "quick.grid.orbits")
    exact(grid["rotation_row_count"], 3_009, "quick.grid.rotations")
    exact(grid["nondegenerate_cz_cell_count"], 103_749, "quick.grid.cz")
    exact(grid["invariant_row_count"], 1_003, "quick.grid.invariants")
    exact(
        grid["fixed_time_sha256"],
        "25a48cc23c1cd7a6003f9dd44f0caaee44205fa65f8da56c20b759d776a3df35",
        "quick.grid.fixed_digest",
    )
    assert len(obj["pair_rows"]) == len(pairs)
    assert len(obj["orbit_type_rows"]) == 4 * len(pairs)
    assert len(obj["rotation_rows"]) == 3 * len(pairs)
    assert len(obj["invariant_rows"]) == len(pairs)
    for index, (p, q) in enumerate(pairs):
        period = 2 * p * q
        pair_row = obj["pair_rows"][index]
        exact(pair_row["p"], p, "quick.pair.p")
        exact(pair_row["q"], q, "quick.pair.q")
        exact(pair_row["principal_period"], period, "quick.pair.period")
        exact(pair_row["fixed_time_cell_count"], period, "quick.pair.cells")
        exact(pair_row["fixed_class_counts"], {
            "empty": period - p - q, "exceptional_01": q - 1,
            "exceptional_02": p - 1, "exceptional_12": 1, "principal_link": 1,
        }, "quick.pair.counts")
        orbit_expected = (
            ("exceptional_01", [0, 1], 2 * p, q, 1, 0),
            ("exceptional_02", [0, 2], 2 * q, p, 1, 0),
            ("exceptional_12", [1, 2], p * q, 2, 1, 0),
            ("principal", [0, 1, 2], period, 1, 3, 2),
        )
        for offset, expected in enumerate(orbit_expected):
            row = obj["orbit_type_rows"][4 * index + offset]
            label, support, primitive, isotropy, dim, quotient = expected
            exact(
                {key: row[key] for key in (
                    "p", "q", "label", "support", "primitive_period", "isotropy_order",
                    "morse_bott_dimension", "orbit_quotient_dimension",
                )},
                {"p": p, "q": q, "label": label, "support": support,
                 "primitive_period": primitive, "isotropy_order": isotropy,
                 "morse_bott_dimension": dim, "orbit_quotient_dimension": quotient},
                "quick.orbit",
            )
        for offset, (label, numerator, denominator) in enumerate((
            ("exceptional_01", 2 * p, q),
            ("exceptional_02", 2 * q, p),
            ("exceptional_12", p * q, 2),
        )):
            row = obj["rotation_rows"][3 * index + offset]
            rho = Fraction(numerator, denominator)
            exact(row["p"], p, "quick.rotation.p")
            exact(row["q"], q, "quick.rotation.q")
            exact(row["label"], label, "quick.rotation.label")
            exact(row["rotation_number"], frac(rho), "quick.rotation.rho")
            exact(row["first_degenerate_cover"], rho.denominator, "quick.rotation.degeneracy")
            exact(row["nondegenerate_cover_count"], rho.denominator - 1, "quick.rotation.count")
        invariant = obj["invariant_rows"][index]
        chi = Fraction(-p * q + 2 * p + 2 * q, 2 * p * q)
        rs = -2 * p * q + 4 * p + 4 * q
        sign = "positive" if rs > 0 else "negative" if rs < 0 else "zero"
        exact(invariant["p"], p, "quick.invariant.p")
        exact(invariant["q"], q, "quick.invariant.q")
        exact(invariant["orbifold_euler_characteristic"], frac(chi), "quick.invariant.chi")
        exact(invariant["orbifold_geometry_sign"], sign, "quick.invariant.sign")
        exact(invariant["principal_robbin_salamon_index"], rs, "quick.invariant.rs")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=EVIDENCE)
    parser.add_argument("--evaluation", type=Path, default=EVALUATION)
    args = parser.parse_args()
    validate_yaml(args.evaluation)
    obj = load_json(args.input)
    exact_keys(obj, TOP_KEYS, "evidence root")

    frozen = {
        "schema": "hcs-c370-brieskorn-quasiregular-reeb-evidence-v1",
        "candidate_id": "HCS-C370", "obstruction_id": "HEN-O354",
        "evaluation_date": "2026-09-04", "source_commit": SOURCE,
        "fixed_epoch": 1788480000, "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": AUTHORITY_SHA},
        "route_a_yaml": {"relative_path": "evaluations/route_a/HCS-C370/2026-09-04.yaml", "raw_sha256": YAML_RAW_SHA, "semantic_sha256": YAML_SEMANTIC_SHA},
        "parameter_domain": {"p_min": 3, "q_max": 101, "p_q_odd": True, "p_less_than_q": True, "gcd_p_q": 1},
        "conventions": {
            "link": "z0^2+z1^p+z2^q=0 intersect unit S5",
            "contact_form": "alpha=(i/(4*pi))*sum_j a_j*(z_j*dbar(z_j)-bar(z_j)*dz_j), a=(2,p,q)",
            "reeb_flow": "Phi_t(z_j)=exp(2*pi*i*t/a_j)*z_j",
            "fixed_time_window": "integer times 1<=T<=2*p*q for every pair",
            "fixed_empty_dimension": -1,
            "exceptional_cz_trivialization": "ambient missing-coordinate complex-line trivialization",
            "principal_rs_trivialization": "standard Milnor-fiber capping trivialization",
            "return_determinant": "det_R(I-P)=4*sin(pi*rho)^2",
        },
        "theorem_contract": {
            "periods": "principal period 2*p*q; exceptional periods 2*p, 2*q, and p*q",
            "fixed_atlas": "J_T={j:T/a_j integer}; empty for |J_T|<2, the corresponding circle for |J_T|=2, and the whole link for |J_T|=3; every nonempty component is Morse-Bott",
            "rotations": "rho_01=2*p/q, rho_02=2*q/p, rho_12=p*q/2 in the declared trivializations; first degeneracy at q, p, and 2 covers",
            "indices": "mu_CZ(gamma^r)=2*floor(r*rho)+1 before first degeneracy; principal mu_RS=-2*p*q+4*p+4*q",
            "quotient": "the orbit quotient is the Seifert orbifold S2(2,p,q) with chi_orb=1/2+1/p+1/q-1",
            "sign": "chi_orb and mu_RS are positive only for (p,q)=(3,5), negative otherwise, and never zero",
        },
        "collision_boundary": {
            "C242": "irrational ellipsoid Reeb flow with two isolated coordinate orbits, not a weighted-homogeneous link with three exceptional fibers and a principal Morse-Bott family",
            "C313": "round-sphere geodesic clean flow, not a contact link and Seifert orbifold action",
            "C339": "Katok-Zermelo Finsler geodesics, not weighted singularity-link Reeb dynamics",
            "C349": "Neumann integrable dynamics on a sphere, not a quasiregular contact circle action",
        },
        "nonclaims": [
            "no rational-prime or prime-power orbit taxonomy", "no target arithmetic local data",
            "no target Euler factor or root number",
            "no automorphy, target divisor, target functional equation, or target zero match",
            "no Hilbert-Polya operator and no Route B", "no contact-homology computation or extrapolation",
            "no ordinary discrete primitive product for the principal orbit continuum",
        ],
        "references": [
            {"doi": "10.1112/blms/bdv088", "role": "Brieskorn contact manifolds and periodic Reeb-flow background"},
            {"doi": "10.1515/FORUM.2008.016", "role": "standard Brieskorn orbit-stratum and index conventions"},
        ],
        "scope_flags": FLAGS,
        "route_a": {"tuple": TUPLE, "overall": "ROUTE_A_EXPLORATORY", "route_b_invocation_allowed": False, "theorem_status": "PROVABLE_AS_STATED"},
        "finite_evidence_role": "the exhaustive finite ledger is regression evidence only; analytic divisibility, transversality, Seifert, and index arguments prove the uniform theorem",
    }
    for key, expected in frozen.items():
        exact(obj[key], expected, key)

    temporary = dict(obj)
    claimed_payload = temporary.pop("payload_sha256")
    assert type(claimed_payload) is str and claimed_payload == digest(temporary)

    quick_semantic_gate(obj)

    pair_rows, orbit_rows, rotation_rows, invariant_rows, grid = expected_rows()
    exact(obj["pair_rows"], pair_rows, "pair_rows")
    exact(obj["orbit_type_rows"], orbit_rows, "orbit_type_rows")
    exact(obj["rotation_rows"], rotation_rows, "rotation_rows")
    exact(obj["invariant_rows"], invariant_rows, "invariant_rows")
    exact(obj["finite_grid"], grid, "finite_grid")
    sections = {
        "pair_rows": pair_rows, "orbit_type_rows": orbit_rows,
        "rotation_rows": rotation_rows, "invariant_rows": invariant_rows,
    }
    exact(obj["section_sha256"], {key: digest(value) for key, value in sections.items()}, "section_sha256")

    assert grid["pair_count"] == 1003
    assert grid["fixed_time_cell_count"] == 5_469_178
    assert grid["orbit_type_row_count"] == 4_012
    assert grid["rotation_row_count"] == 3_009
    assert grid["nondegenerate_cz_cell_count"] == 103_749
    assert grid["invariant_row_count"] == 1_003
    assert sum(row["orbifold_geometry_sign"] == "positive" for row in invariant_rows) == 1
    assert sum(row["orbifold_geometry_sign"] == "zero" for row in invariant_rows) == 0
    assert next(row for row in invariant_rows if row["p"] == 3 and row["q"] == 5)["principal_robbin_salamon_index"] == 2
    print(
        "C370 checker PASS: "
        f"pairs={grid['pair_count']} fixed_cells={grid['fixed_time_cell_count']} "
        f"orbit_types={grid['orbit_type_row_count']} rotations={grid['rotation_row_count']} "
        f"cz_cells={grid['nondegenerate_cz_cell_count']} payload={claimed_payload}"
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"C370 checker FAIL: {type(exc).__name__}: {exc}", file=sys.stderr)
        sys.exit(1)
