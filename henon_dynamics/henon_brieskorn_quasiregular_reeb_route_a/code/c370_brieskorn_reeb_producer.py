#!/usr/bin/env python3
"""Canonical exact evidence producer for HCS-C370."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("c370 producer refuses optimized Python")

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results/c370_brieskorn_reeb_evidence.json"
EVAL = ROOT / "evaluations/route_a/HCS-C370/2026-09-04.yaml"
SOURCE = "c6553f02d928c6aa05400ded57746869a85f0238"
EVALUATOR_SHA = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
YAML_RAW_SHA = "d452c49bc188141a22e60a5f3e5b7dacd59ecea99de39ce6e33d1f492d90ade1"
YAML_SEMANTIC_SHA = "5af9e8955b35292f87189a87fa1cf7a6ca15aa97d339cba822da940f6a3c3eda"


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


def update_cell(hasher, p: int, q: int, time: int, label: str, dimension: int) -> None:
    hasher.update(f"{p}|{q}|{time}|{label}|{dimension}\n".encode("ascii"))


def fixed_class(p: int, q: int, time: int):
    principal = 2 * p * q
    if time % principal == 0:
        return "principal_link", 3
    if time % (2 * p) == 0:
        return "exceptional_01", 1
    if time % (2 * q) == 0:
        return "exceptional_02", 1
    if time % (p * q) == 0:
        return "exceptional_12", 1
    return "empty", -1


def fraction_record(value: Fraction):
    return {"numerator": value.numerator, "denominator": value.denominator}


def sequence_sha(values) -> str:
    return digest(list(values))


def build(evaluation_path: Path):
    raw = evaluation_path.read_bytes()
    semantic = load_yaml(evaluation_path)
    assert hashlib.sha256(raw).hexdigest() == YAML_RAW_SHA
    assert digest(semantic) == YAML_SEMANTIC_SHA

    pairs = [
        (p, q)
        for p in range(3, 102, 2)
        for q in range(p + 2, 102, 2)
        if math.gcd(p, q) == 1
    ]
    pair_rows = []
    orbit_type_rows = []
    rotation_rows = []
    invariant_rows = []
    global_fixed_digest = hashlib.sha256()
    fixed_cells = 0
    cz_cells = 0

    for p, q in pairs:
        principal = 2 * p * q
        pair_digest = hashlib.sha256()
        counts = {
            "empty": 0,
            "exceptional_01": 0,
            "exceptional_02": 0,
            "exceptional_12": 0,
            "principal_link": 0,
        }
        for time in range(1, principal + 1):
            label, dimension = fixed_class(p, q, time)
            counts[label] += 1
            update_cell(pair_digest, p, q, time, label, dimension)
            update_cell(global_fixed_digest, p, q, time, label, dimension)
            fixed_cells += 1

        expected_counts = {
            "empty": 2 * p * q - p - q,
            "exceptional_01": q - 1,
            "exceptional_02": p - 1,
            "exceptional_12": 1,
            "principal_link": 1,
        }
        assert counts == expected_counts
        pair_rows.append(
            {
                "p": p,
                "q": q,
                "principal_period": principal,
                "fixed_time_cell_count": principal,
                "fixed_class_counts": counts,
                "fixed_time_sha256": pair_digest.hexdigest(),
            }
        )

        orbit_type_rows.extend(
            [
                {
                    "p": p,
                    "q": q,
                    "label": "exceptional_01",
                    "support": [0, 1],
                    "primitive_period": 2 * p,
                    "isotropy_order": q,
                    "morse_bott_dimension": 1,
                    "orbit_quotient_dimension": 0,
                },
                {
                    "p": p,
                    "q": q,
                    "label": "exceptional_02",
                    "support": [0, 2],
                    "primitive_period": 2 * q,
                    "isotropy_order": p,
                    "morse_bott_dimension": 1,
                    "orbit_quotient_dimension": 0,
                },
                {
                    "p": p,
                    "q": q,
                    "label": "exceptional_12",
                    "support": [1, 2],
                    "primitive_period": p * q,
                    "isotropy_order": 2,
                    "morse_bott_dimension": 1,
                    "orbit_quotient_dimension": 0,
                },
                {
                    "p": p,
                    "q": q,
                    "label": "principal",
                    "support": [0, 1, 2],
                    "primitive_period": principal,
                    "isotropy_order": 1,
                    "morse_bott_dimension": 3,
                    "orbit_quotient_dimension": 2,
                },
            ]
        )

        rotation_specs = [
            ("exceptional_01", 2 * p, q),
            ("exceptional_02", 2 * q, p),
            ("exceptional_12", p * q, 2),
        ]
        for label, numerator, denominator in rotation_specs:
            rho = Fraction(numerator, denominator)
            assert rho.denominator == denominator
            cz_values = [
                2 * ((cover * rho.numerator) // rho.denominator) + 1
                for cover in range(1, rho.denominator)
            ]
            cz_cells += len(cz_values)
            rotation_rows.append(
                {
                    "p": p,
                    "q": q,
                    "label": label,
                    "rotation_number": fraction_record(rho),
                    "return_determinant": "4*sin(pi*rho)^2",
                    "return_determinant_argument": fraction_record(rho),
                    "first_degenerate_cover": rho.denominator,
                    "nondegenerate_cover_count": rho.denominator - 1,
                    "cz_formula": "2*floor(cover*rho)+1 for 1<=cover<first_degenerate_cover",
                    "cz_sequence_sha256": sequence_sha(cz_values),
                    "trivialization": "ambient missing-coordinate complex-line trivialization",
                }
            )

        chi = Fraction(-p * q + 2 * p + 2 * q, 2 * p * q)
        rs_index = -2 * p * q + 4 * p + 4 * q
        sign = "positive" if rs_index > 0 else "negative" if rs_index < 0 else "zero"
        invariant_rows.append(
            {
                "p": p,
                "q": q,
                "base_orbifold_orders": [2, p, q],
                "orbifold_euler_characteristic": fraction_record(chi),
                "orbifold_geometry_sign": sign,
                "principal_robbin_salamon_index": rs_index,
                "index_identity": "mu_RS=2*(2*p*q)*chi_orb",
                "principal_trivialization": "standard Milnor-fiber capping trivialization",
            }
        )

    sections = {
        "pair_rows": pair_rows,
        "orbit_type_rows": orbit_type_rows,
        "rotation_rows": rotation_rows,
        "invariant_rows": invariant_rows,
    }
    flags = {
        key: False
        for key in (
            "claims_target_arithmetic_local_data",
            "claims_target_euler_factors",
            "claims_root_number",
            "claims_automorphy",
            "claims_target_divisor_or_counting_law",
            "claims_target_functional_equation",
            "claims_target_zero_match",
            "claims_hilbert_polya_operator",
            "invokes_route_b",
        )
    }
    body = {
        "schema": "hcs-c370-brieskorn-quasiregular-reeb-evidence-v1",
        "candidate_id": "HCS-C370",
        "obstruction_id": "HEN-O354",
        "evaluation_date": "2026-09-04",
        "source_commit": SOURCE,
        "fixed_epoch": 1788480000,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "evaluator": {
            "authority": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": EVALUATOR_SHA,
        },
        "route_a_yaml": {
            "relative_path": "evaluations/route_a/HCS-C370/2026-09-04.yaml",
            "raw_sha256": YAML_RAW_SHA,
            "semantic_sha256": YAML_SEMANTIC_SHA,
        },
        "parameter_domain": {
            "p_min": 3,
            "q_max": 101,
            "p_q_odd": True,
            "p_less_than_q": True,
            "gcd_p_q": 1,
        },
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
        "finite_grid": {
            "pair_count": len(pairs),
            "fixed_time_cell_count": fixed_cells,
            "orbit_type_row_count": len(orbit_type_rows),
            "rotation_row_count": len(rotation_rows),
            "nondegenerate_cz_cell_count": cz_cells,
            "invariant_row_count": len(invariant_rows),
            "fixed_time_storage": "all cells recomputed; canonical streaming digest plus exact per-pair class counts and digests stored",
            "fixed_time_encoding": "ASCII p|q|time|class|dimension followed by newline in lexicographic pair and increasing-time order",
            "fixed_time_sha256": global_fixed_digest.hexdigest(),
        },
        "collision_boundary": {
            "C242": "irrational ellipsoid Reeb flow with two isolated coordinate orbits, not a weighted-homogeneous link with three exceptional fibers and a principal Morse-Bott family",
            "C313": "round-sphere geodesic clean flow, not a contact link and Seifert orbifold action",
            "C339": "Katok-Zermelo Finsler geodesics, not weighted singularity-link Reeb dynamics",
            "C349": "Neumann integrable dynamics on a sphere, not a quasiregular contact circle action",
        },
        "nonclaims": [
            "no rational-prime or prime-power orbit taxonomy",
            "no target arithmetic local data",
            "no target Euler factor or root number",
            "no automorphy, target divisor, target functional equation, or target zero match",
            "no Hilbert-Polya operator and no Route B",
            "no contact-homology computation or extrapolation",
            "no ordinary discrete primitive product for the principal orbit continuum",
        ],
        "references": [
            {
                "doi": "10.1112/blms/bdv088",
                "role": "Brieskorn contact manifolds and periodic Reeb-flow background",
            },
            {
                "doi": "10.1515/FORUM.2008.016",
                "role": "standard Brieskorn orbit-stratum and index conventions",
            },
        ],
        "scope_flags": flags,
        "route_a": {
            "tuple": [
                "A0_WEAK_ARITHMETIC_RELATION",
                "A1_WEAK",
                "A2_FAIL",
                "A3_FAIL",
                "A4_FORMAL_HINT",
            ],
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
            "theorem_status": "PROVABLE_AS_STATED",
        },
        "finite_evidence_role": "the exhaustive finite ledger is regression evidence only; analytic divisibility, transversality, Seifert, and index arguments prove the uniform theorem",
        **sections,
        "section_sha256": {name: digest(value) for name, value in sections.items()},
    }
    body["payload_sha256"] = digest(body)
    return body


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUT)
    parser.add_argument("--evaluation", type=Path, default=EVAL)
    args = parser.parse_args()
    obj = build(args.evaluation)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(
        json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False).encode() + b"\n"
    )
    grid = obj["finite_grid"]
    print(
        "C370 producer PASS: "
        f"pairs={grid['pair_count']} fixed_cells={grid['fixed_time_cell_count']} "
        f"orbit_types={grid['orbit_type_row_count']} rotations={grid['rotation_row_count']} "
        f"cz_cells={grid['nondegenerate_cz_cell_count']} payload={obj['payload_sha256']}"
    )


if __name__ == "__main__":
    main()
