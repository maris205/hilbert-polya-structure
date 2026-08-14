#!/usr/bin/env python3
"""Produce the exact HCS-C55 tangent, projector, and Yukawa certificate.

The machine certificate deliberately separates finite algebra from the
deformation-theoretic implications that belong to the written proof.  In
particular, a CAS replay does not prove Rim's theorem, smoothness of a Hilbert
fixed germ, algebraization of the germ, or existence of a relative VHS.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
from functools import reduce
import hashlib
import importlib.util
from itertools import combinations_with_replacement
import json
import math
from pathlib import Path
import re
import subprocess
import sys
import tempfile
from typing import Any, Iterable

import sympy as sp


SCHEMA = "hcs-c55-certificate-v1"
CANDIDATE_ID = "HCS-C55"
PROJECT_SLUG = "henon_mu3_rational_yukawa_surface"
PROJECT = Path(__file__).resolve().parents[1]
REPOSITORY = Path(__file__).resolve().parents[3]

SOURCE_LOCKS = {
    "C52_certificate": (
        "henon_dynamics/henon_mu3_d12_calabi_yau_core_projector/results/c52_certificate.json",
        "a2b0b281bfb311f979c7ed65e441a184ebe338b05f5fec8a60768610965c9c94",
        "78d362e62efacc78dac511d9607d93f21f065a86f1d41c62c10c101b652558f1",
    ),
    "C52_theorem": (
        "henon_dynamics/henon_mu3_d12_calabi_yau_core_projector/THEOREM_PACKAGE.md",
        "376c6444481b5766d05a4f23757217496402de12507e2303d2c1a25ced8e469a",
        None,
    ),
    "C52_exact_backend": (
        "henon_dynamics/henon_mu3_d12_calabi_yau_core_projector/code/c52_producer.py",
        "69cf4d7571bf6a8ca6dfc972c57c5f0fa6b2b06f02ac8d583c56d233e81a3eed",
        None,
    ),
    "C53_certificate": (
        "henon_dynamics/henon_mu3_dihedral_core_rational_descent/results/c53_certificate.json",
        "f4325a5987933e2acf81656389d46701d82d38912c546d1e5996123f617f6e79",
        "8064224eda63fa9d890efd26ec9aa167c7cd9458662620be3135196a09494d41",
    ),
    "C53_theorem": (
        "henon_dynamics/henon_mu3_dihedral_core_rational_descent/THEOREM_PACKAGE.md",
        "e474d938c02d1d9e39e510dfd77ffcdd6383e5dcc8a8442b5b19465be82dbebe",
        None,
    ),
    "C54_certificate": (
        "henon_dynamics/henon_mu3_universal_dihedral_denominator_rigidity/results/c54_certificate.json",
        "780cc9f249e836d3fa5b51a00fd2cdb9af0eac595d929cd1be4d728df1921846",
        "f068d5e11ea8e6245e04bd3a30e77140267f835c4e07412ce2009c7fb04ceae1",
    ),
    "C54_theorem": (
        "henon_dynamics/henon_mu3_universal_dihedral_denominator_rigidity/THEOREM_PACKAGE.md",
        "d234f078cb415db8394fdcece124068cad90dbdf12b82941207105ecd24088b4",
        None,
    ),
}

RELEASE_PROVENANCE = {
    "C52": {
        "project": "henon_dynamics/henon_mu3_d12_calabi_yau_core_projector",
        "implementation_commit": "208feef86365cd92ace8dad02904acff6623eeec",
        "provenance_commit": "a411b8d2626190a9ca941e55d15826db0dedc417",
        "files": {
            "results/c52_certificate.json": "a2b0b281bfb311f979c7ed65e441a184ebe338b05f5fec8a60768610965c9c94",
            "results/independent_check.json": "a4a0180a3e40a8eb82159fcea474221dafabddd728ebf1c2112435b21ad5c6f1",
            "results/ARTIFACT_HASHES.sha256": "3e0b3d1fa0f371ddffe5eba9a379018d72ee1f2059863245a741da899ec9fd30",
            "THEOREM_PACKAGE.md": "376c6444481b5766d05a4f23757217496402de12507e2303d2c1a25ced8e469a",
            "route_a_evaluation.yaml": "312d4701adb82e30224749ba682474ab66a921222f584d8e6e1d9743a4d64653",
            "evaluations/route_a/HCS-C52/20260814T100000Z.yaml": "312d4701adb82e30224749ba682474ab66a921222f584d8e6e1d9743a4d64653",
            "INTEGRITY_REPORT.md": "e7224410769e3e5dfb66a3ecacb64a6d061d28394cefd2e5ac446027729125db",
            "code/c52_producer.py": "69cf4d7571bf6a8ca6dfc972c57c5f0fa6b2b06f02ac8d583c56d233e81a3eed",
        },
        "payload_sha256": "78d362e62efacc78dac511d9607d93f21f065a86f1d41c62c10c101b652558f1",
        "historical_code_results_manifest_sha256": None,
    },
    "C53": {
        "project": "henon_dynamics/henon_mu3_dihedral_core_rational_descent",
        "implementation_commit": "0a7f0fdb8290eab4aa92ed5ade432401c40c22cf",
        "provenance_commit": "9d509d3b3826b7bfbdb38ed9fe4dac9297f5dbdf",
        "files": {
            "results/c53_certificate.json": "f4325a5987933e2acf81656389d46701d82d38912c546d1e5996123f617f6e79",
            "results/independent_check.json": "0d38643ded626c2a5e1536c8a4df9c56ae98c4fda01e1d15660996ea8c495e67",
            "results/ARTIFACT_HASHES.sha256": "2b4fc3e3bf3dedba175d40756421ae3433eddc2b7c7272983cf644d6034091b3",
            "THEOREM_PACKAGE.md": "e474d938c02d1d9e39e510dfd77ffcdd6383e5dcc8a8442b5b19465be82dbebe",
            "route_a_evaluation.yaml": "ae508e6e41523559f014f6fbcd0c4c199229f221fe6ac915a75cd27b02e73719",
            "evaluations/route_a/HCS-C53/20260814T150000Z.yaml": "ae508e6e41523559f014f6fbcd0c4c199229f221fe6ac915a75cd27b02e73719",
            "INTEGRITY_REPORT.md": "da3f6caec587b56871ac01cc7db1364cc45f3ec99e684dc263332fb9f2585ae2",
        },
        "payload_sha256": "8064224eda63fa9d890efd26ec9aa167c7cd9458662620be3135196a09494d41",
        "historical_code_results_manifest_sha256": "b62f353d119d6c8565f513dad771a047a5e6343411d08ad2e91562fe84923480",
    },
    "C54": {
        "project": "henon_dynamics/henon_mu3_universal_dihedral_denominator_rigidity",
        "implementation_commit": "f2fee2f9844b84aa31e076aabe9d4bb88fbd3618",
        "provenance_commit": "eba8a1e76c0486b72e595f4baddd00d11ae81309",
        "files": {
            "results/c54_certificate.json": "780cc9f249e836d3fa5b51a00fd2cdb9af0eac595d929cd1be4d728df1921846",
            "results/independent_check.json": "160b3a9d11354b41404642a3dd22d6e43f2ce576126acb21eb0133e552fc0c0a",
            "results/CODE_RESULTS_HASHES.sha256": "62f67e6d4929496974020febab3bc0e2cff45ed153b0cef51937031863d866ba",
            "results/ARTIFACT_HASHES.sha256": "92e1950c787ac1625ad9edaf448e54a1fe63162344c79748970bbcfa3dcf7065",
            "THEOREM_PACKAGE.md": "d234f078cb415db8394fdcece124068cad90dbdf12b82941207105ecd24088b4",
            "route_a_evaluation.yaml": "bcc5609b0131444f9321b8c2a79f8480508af84c20cd9933dc993a804fc8c5ed",
            "evaluations/route_a/HCS-C54/20260814T134920Z.yaml": "bcc5609b0131444f9321b8c2a79f8480508af84c20cd9933dc993a804fc8c5ed",
            "INTEGRITY_REPORT.md": "e4683fd0fe5e7529f196c7eb8fbeaa859e1ccd1a46f78d6de447251d7d7cba4f",
        },
        "payload_sha256": "f068d5e11ea8e6245e04bd3a30e77140267f835c4e07412ce2009c7fb04ceae1",
        "historical_code_results_manifest_sha256": "62f67e6d4929496974020febab3bc0e2cff45ed153b0cef51937031863d866ba",
    },
}

ARCHITECTURE_REPORT_SHA256 = (
    "21c5fcfdbc4387b141388103c896cf33a32b29cbf2c7cde09d1d04c85b7c49bd"
)

SEED_X_EXPONENTS = (
    (0, 0, 0, 1, 0, 1, 0, 1),  # x3*x5*x7
    (0, 0, 0, 2, 0, 1, 0, 0),  # x3^2*x5
    (0, 0, 2, 0, 0, 0, 1, 0),  # x2^2*x6
    (0, 0, 2, 0, 1, 0, 0, 0),  # x2^2*x4
)

DIRECT_CUBE_POINTS = (
    (1, 0, 0, 0),
    (0, 1, 0, 0),
    (0, 0, 1, 0),
    (0, 0, 0, 1),
    (0, 0, 1, 1),
    (0, 0, 1, 2),
    (0, 1, 0, 1),
    (0, 1, 0, 2),
    (0, 1, 1, 0),
    (0, 1, 1, 1),
    (0, 1, 2, 0),
    (1, 0, 0, 1),
    (1, 0, 0, 2),
    (1, 0, 1, 0),
    (1, 0, 1, 1),
    (1, 0, 2, 0),
    (1, 1, 0, 0),
    (1, 1, 0, 1),
    (1, 1, 1, 0),
    (1, 2, 0, 0),
)

EXPECTED_PRIMITIVE = {
    (3, 0, 0, 0): 75081586157,
    (2, 1, 0, 0): -28576620789,
    (1, 2, 0, 0): 164150208636,
    (0, 3, 0, 0): 6898957820,
    (2, 0, 1, 0): -122000922135,
    (1, 1, 1, 0): -415458334296,
    (0, 2, 1, 0): 1132596902196,
    (1, 0, 2, 0): 1158143874300,
    (0, 1, 2, 0): -2054867641020,
    (0, 0, 3, 0): 2646295985484,
    (2, 0, 0, 1): -5364921951,
    (1, 1, 0, 1): 151070718312,
    (0, 2, 0, 1): -30413540316,
    (1, 0, 1, 1): 114691988016,
    (0, 1, 1, 1): 151980984216,
    (0, 0, 2, 1): 560186573940,
    (1, 0, 0, 2): 113572676646,
    (0, 1, 0, 2): 36794420832,
    (0, 0, 1, 2): 706181383584,
    (0, 0, 0, 3): 1884468968,
}


def canonical_json(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def load_c52_backend():
    path = REPOSITORY / SOURCE_LOCKS["C52_exact_backend"][0]
    specification = importlib.util.spec_from_file_location("c55_c52_backend", path)
    module = importlib.util.module_from_spec(specification)
    if specification.loader is None:
        raise AssertionError("C52 backend loader unavailable")
    specification.loader.exec_module(module)
    return module


def source_bundle() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    rows = []
    certificates = {}
    for name, (relative, expected_sha, expected_payload) in SOURCE_LOCKS.items():
        path = REPOSITORY / relative
        actual = sha256_file(path)
        if actual != expected_sha:
            raise AssertionError(f"source-lock mismatch for {name}: {actual}")
        row: dict[str, Any] = {
            "name": name,
            "path": relative,
            "sha256": actual,
        }
        if expected_payload is not None:
            certificate = json.loads(path.read_text(encoding="utf-8"))
            if certificate.get("payload_sha256") != expected_payload:
                raise AssertionError(f"payload-lock mismatch for {name}")
            row["payload_sha256"] = expected_payload
            row["schema"] = certificate["schema"]
            certificates[name] = certificate
        rows.append(row)
    return rows, certificates


def git_blob(commit: str, relative: str) -> bytes:
    process = subprocess.run(
        ["git", "show", f"{commit}:{relative}"],
        cwd=REPOSITORY,
        capture_output=True,
        timeout=60,
        check=False,
    )
    if process.returncode != 0:
        raise AssertionError(
            f"committed blob unavailable {commit}:{relative}: "
            + process.stderr.decode(errors="replace")[-1000:]
        )
    return process.stdout


def verify_release_provenance() -> list[dict[str, Any]]:
    rows = []
    for label, release in RELEASE_PROVENANCE.items():
        implementation = release["implementation_commit"]
        provenance = release["provenance_commit"]
        ancestry = subprocess.run(
            ["git", "merge-base", "--is-ancestor", implementation, provenance],
            cwd=REPOSITORY,
            capture_output=True,
            timeout=30,
            check=False,
        )
        if ancestry.returncode != 0:
            raise AssertionError(f"{label} implementation is not an ancestor of provenance")
        committed_files = []
        for project_relative, expected_sha in release["files"].items():
            repository_relative = f"{release['project']}/{project_relative}"
            live_path = REPOSITORY / repository_relative
            live = live_path.read_bytes()
            committed = git_blob(provenance, repository_relative)
            if live != committed:
                raise AssertionError(f"{label} live bytes differ from provenance blob: {project_relative}")
            actual_sha = hashlib.sha256(committed).hexdigest()
            if actual_sha != expected_sha:
                raise AssertionError(f"{label} committed hash drifted: {project_relative}")
            committed_files.append({
                "path": repository_relative,
                "sha256": actual_sha,
                "live_equals_provenance_blob": True,
            })

        route_path = f"{release['project']}/route_a_evaluation.yaml"
        route_text = git_blob(provenance, route_path).decode("utf-8")
        if f"code_commit: {implementation}" not in route_text:
            raise AssertionError(f"{label} Route-A implementation tuple mismatch")
        certificate_path = next(
            path for path in release["files"] if path.endswith("_certificate.json")
        )
        certificate = json.loads(
            git_blob(provenance, f"{release['project']}/{certificate_path}")
        )
        if certificate["payload_sha256"] != release["payload_sha256"]:
            raise AssertionError(f"{label} committed payload hash mismatch")
        certificate_sha = release["files"][certificate_path]
        check_path = "results/independent_check.json"
        check_sha = release["files"][check_path]
        if label in {"C53", "C54"}:
            required_route_tokens = [certificate_sha, release["payload_sha256"], check_sha]
            historical_manifest = release["historical_code_results_manifest_sha256"]
            if historical_manifest is not None:
                required_route_tokens.append(historical_manifest)
            if any(token not in route_text for token in required_route_tokens):
                raise AssertionError(f"{label} committed Route-A release tuple incomplete")
            tuple_authority = "committed Route-A release tuple"
        else:
            integrity_text = git_blob(
                provenance, f"{release['project']}/INTEGRITY_REPORT.md"
            ).decode("utf-8")
            if any(
                token not in integrity_text
                for token in [certificate_sha, release["payload_sha256"], check_sha]
            ):
                raise AssertionError("C52 committed Route-A/integrity release tuple incomplete")
            tuple_authority = "committed Route-A code commit plus committed integrity hash tuple"
        rows.append({
            "source": label,
            "implementation_commit": implementation,
            "provenance_commit": provenance,
            "implementation_is_ancestor_of_provenance": True,
            "tuple_authority": tuple_authority,
            "certificate_sha256": certificate_sha,
            "payload_sha256": release["payload_sha256"],
            "independent_check_sha256": check_sha,
            "historical_code_results_manifest_sha256": release[
                "historical_code_results_manifest_sha256"
            ],
            "committed_files": committed_files,
            "commit_lock_status": "VERIFIED_GIT_OBJECTS_AND_LIVE_BYTE_IDENTITY",
        })
    return rows


def hilbert_h0(degree: int) -> int:
    def ambient(value: int) -> int:
        return math.comb(value + 7, 7) if value >= 0 else 0

    return (
        ambient(degree)
        - ambient(degree - 2)
        - ambient(degree - 3)
        + ambient(degree - 5)
    )


def complete_intersection_controls() -> dict[str, Any]:
    h0 = {str(degree): hilbert_h0(degree) for degree in range(4)}
    if h0 != {"0": 1, "1": 8, "2": 35, "3": 111}:
        raise AssertionError("Hilbert coefficients drifted")
    normal_sections = h0["2"] + h0["3"]
    ambient_vector_fields = 8 * h0["1"] - h0["0"]
    dimension_balance = normal_sections - ambient_vector_fields
    if (normal_sections, ambient_vector_fields, dimension_balance) != (146, 63, 83):
        raise AssertionError("embedded deformation dimensions drifted")
    return {
        "ambient": "P^7_Q(rho)",
        "complete_intersection_degrees": [2, 3],
        "dimension": 5,
        "canonical_bundle": "O_X(-3)",
        "normal_bundle": "O_X(2) direct_sum O_X(3)",
        "hilbert_series": "(1-t^2)(1-t^3)/(1-t)^8",
        "hilbert_numerator_coefficients_degrees_0_to_5": [1, 0, -1, -1, 0, 1],
        "h0_OX_degrees_0_to_3": h0,
        "h0_normal_bundle": normal_sections,
        "h0_TP7_restricted": ambient_vector_fields,
        "normal_minus_ambient_vector_field_dimension_balance": dimension_balance,
        "dimension_balance_is_not_by_itself_an_injectivity_proof": True,
        "koszul_twists_used": {
            "O_X(2)": [2, 0, -1, -3],
            "O_X(3)": [3, 1, 0, -2],
            "O_X(1)": [1, -1, -2, -4],
            "O_X": [0, -2, -3, -5],
        },
        "cohomology_values_locked_for_written_proof": {
            "H1_normal_bundle_dimension": 0,
            "H1_TP7_restricted_dimension": 0,
            "embedded_Kodaira_Spencer_surjective": True,
        },
        "machine_scope": (
            "the Hilbert coefficients and finite dimensions are recomputed; "
            "Koszul/Euler/Hilbert implications are written-proof obligations"
        ),
        "written_proof_dependencies": [
            "Koszul and projective-space line-bundle cohomology give H1(N_X/P7)=0",
            "the restricted Euler sequence gives H1(T_P7|X)=0",
            "the Hilbert germ is smooth and its embedded Kodaira-Spencer map is surjective",
            "CY-type contraction identifies H1(T_X) with the independently computed 83-dimensional R_(2,-3); the resulting dimension balance gives the zero Lie-algebra stabilizer",
            "the fixed Hilbert germ of a characteristic-zero finite-etale group action is smooth with tangent H0(N_X/P7)^G",
            "an equivariant transverse slice to the kernel of Kodaira-Spencer has quotient tangent H1(T_X)^G of dimension four",
            "the transverse fixed slice and universal complete intersection are algebraized over a rational etale/analytic germ",
        ],
        "fixed_Hilbert_tangent_dimension_claimed_to_be_four": False,
        "full_PGL_stabilizer_discreteness_inferred_from_C54_monomial_result": False,
        "general_8_by_8_Lie_stabilizer_directly_computed_by_exact_linear_algebra": True,
        "four_dimensional_object": "equivariant transverse moduli slice with tangent H1(T_X)^G",
        "CAS_proves_Rim_or_Hilbert_theorems": False,
    }


def k_serial(value) -> dict[str, list[int]]:
    return {
        "a": [value[0].numerator, value[0].denominator],
        "b": [value[1].numerator, value[1].denominator],
    }


def fraction_text(value: Fraction) -> str:
    if value.denominator == 1:
        return str(value.numerator)
    return f"({value.numerator}/{value.denominator})"


def k_singular(value) -> str:
    a, b = value
    if not b:
        return fraction_text(a)
    if not a:
        return f"({fraction_text(b)})*rho"
    return f"({fraction_text(a)}+({fraction_text(b)})*rho)"


def matrix_rank_k(c52, rows: list[list[Any]]) -> int:
    matrix = [row[:] for row in rows]
    rank = 0
    for column in range(len(matrix[0])):
        pivot = next(
            (i for i in range(rank, len(matrix)) if not c52.k_is_zero(matrix[i][column])),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = c52.k_inverse(matrix[rank][column])
        matrix[rank] = [c52.k_mul(entry, inverse) for entry in matrix[rank]]
        for i in range(len(matrix)):
            if i == rank or c52.k_is_zero(matrix[i][column]):
                continue
            scalar = matrix[i][column]
            matrix[i] = [
                c52.k_sub(left, c52.k_mul(scalar, right))
                for left, right in zip(matrix[i], matrix[rank])
            ]
        rank += 1
        if rank == len(matrix):
            break
    return rank


def infinitesimal_ideal_stabilizer(c52) -> dict[str, Any]:
    """Solve the full linearized PGL8 ideal-stabilizer equations over K."""

    quadratic_monomials = list(combinations_with_replacement(range(8), 2))
    cubic_monomials = list(combinations_with_replacement(range(8), 3))
    quadratic_index = {monomial: index for index, monomial in enumerate(quadratic_monomials)}
    cubic_index = {monomial: index for index, monomial in enumerate(cubic_monomials)}
    unknown_count = 64 + 1 + 1 + 8
    nu_index = 64
    mu_index = 65
    l_start = 66
    q_terms = [
        (tuple(sorted((index, index + 1))), c52.K_ONE) for index in range(7)
    ] + [((0, 7), c52.k_rho_power(1))]

    quadratic_rows = [
        [c52.K_ZERO] * unknown_count for _ in quadratic_monomials
    ]
    for (left, right), q_coefficient in q_terms:
        for variable in range(8):
            # dQ/dx_left times (A*x)_left.
            row = quadratic_rows[
                quadratic_index[tuple(sorted((right, variable)))]
            ]
            a_index = 8 * left + variable
            row[a_index] = c52.k_add(row[a_index], q_coefficient)
            # dQ/dx_right times (A*x)_right.
            row = quadratic_rows[
                quadratic_index[tuple(sorted((left, variable)))]
            ]
            a_index = 8 * right + variable
            row[a_index] = c52.k_add(row[a_index], q_coefficient)
        source_row = quadratic_rows[quadratic_index[(left, right)]]
        source_row[nu_index] = c52.k_sub(source_row[nu_index], q_coefficient)

    cubic_rows = [[c52.K_ZERO] * unknown_count for _ in cubic_monomials]
    for index in range(8):
        for variable in range(8):
            monomial = tuple(sorted((index, index, variable)))
            row = cubic_rows[cubic_index[monomial]]
            a_index = 8 * index + variable
            row[a_index] = c52.k_add(row[a_index], c52.k_int(3))
        row = cubic_rows[cubic_index[(index, index, index)]]
        row[mu_index] = c52.k_sub(row[mu_index], c52.K_ONE)
    for l_index in range(8):
        for (left, right), q_coefficient in q_terms:
            monomial = tuple(sorted((l_index, left, right)))
            row = cubic_rows[cubic_index[monomial]]
            row[l_start + l_index] = c52.k_sub(
                row[l_start + l_index], q_coefficient
            )

    rows = quadratic_rows + cubic_rows
    rank = matrix_rank_k(c52, rows)
    if rank != 73 or unknown_count - rank != 1:
        raise AssertionError("infinitesimal ideal stabilizer is larger than scalars")
    scalar_solution = [c52.K_ZERO] * unknown_count
    for index in range(8):
        scalar_solution[8 * index + index] = c52.K_ONE
    scalar_solution[nu_index] = c52.k_int(2)
    scalar_solution[mu_index] = c52.k_int(3)
    for row in rows:
        dot = c52.K_ZERO
        for coefficient, value in zip(row, scalar_solution):
            dot = c52.k_add(dot, c52.k_mul(coefficient, value))
        if not c52.k_is_zero(dot):
            raise AssertionError("scalar coordinate solution failed")
    return {
        "equations": [
            "delta_A(Q)=nu*Q",
            "delta_A(C)=mu*C+L*Q",
        ],
        "A_entries": 64,
        "equation_mixing_unknowns": {"nu": 1, "mu": 1, "linear_form_L": 8},
        "total_unknowns": unknown_count,
        "quadratic_coefficient_equations": len(quadratic_rows),
        "cubic_coefficient_equations": len(cubic_rows),
        "exact_Qrho_matrix_rank": rank,
        "kernel_dimension_in_GL8_with_equation_mixing": unknown_count - rank,
        "kernel_generator": "A=I8, nu=2, mu=3, L=0",
        "projective_Lie_stabilizer_dimension": 0,
        "H0_T_X_dimension": 0,
        "full_linearized_ideal_stabilizer_used": True,
        "full_PGL_group_classification_claimed": False,
    }


def tangent_computation(c52) -> dict[str, Any]:
    group, table, inverses = c52.enumerate_projective_group()
    character = c52.character_data(group)
    if character["H32_character"]["trivial_multiplicity"] != 4:
        raise AssertionError("invariant tangent multiplicity drifted")
    monomials = c52.target_monomials()
    relations = c52.jacobian_relations(monomials)
    rref, pivots = c52.exact_rref(relations)
    pivot_row = {pivot: row for row, pivot in enumerate(pivots)}
    quotient_basis = [index for index in range(len(monomials)) if index not in pivot_row]
    monomial_index = {monomial: index for index, monomial in enumerate(monomials)}

    def reduce_vector(vector):
        result = vector[:]
        for pivot in pivots:
            coefficient = result[pivot]
            if c52.k_is_zero(coefficient):
                continue
            row = rref[pivot_row[pivot]]
            result = [
                c52.k_sub(left, c52.k_mul(coefficient, right))
                for left, right in zip(result, row)
            ]
        return result

    def action(element, vector):
        q_scale = group[element]
        permutation, phases = element
        determinant = c52.k_mul(
            c52.k_int(c52.permutation_sign(permutation)),
            c52.k_rho_power(sum(phases)),
        )
        residue_twist = c52.k_div(determinant, c52.k_rho_power(q_scale))
        result = [c52.K_ZERO] * len(monomials)
        for position, coefficient in enumerate(vector):
            if c52.k_is_zero(coefficient):
                continue
            y_exponent, z_exponent, x_exponents = monomials[position]
            transformed = [0] * c52.N
            phase = -q_scale * z_exponent
            for index, exponent in enumerate(x_exponents):
                transformed[permutation[index]] += exponent
                phase += phases[index] * exponent
            image = monomial_index[(y_exponent, z_exponent, tuple(transformed))]
            scalar = c52.k_mul(residue_twist, c52.k_rho_power(phase))
            result[image] = c52.k_add(
                result[image], c52.k_mul(coefficient, scalar)
            )
        return reduce_vector(result)

    basis = []
    for x_exponents in SEED_X_EXPONENTS:
        seed = (2, 0, x_exponents)
        unit = [c52.K_ZERO] * len(monomials)
        unit[monomial_index[seed]] = c52.K_ONE
        total = [c52.K_ZERO] * len(monomials)
        for element in sorted(group):
            image = action(element, unit)
            total = [c52.k_add(left, right) for left, right in zip(total, image)]
        reynolds = [c52.k_div(entry, c52.k_int(24)) for entry in total]
        if reduce_vector(reynolds) != reynolds:
            raise AssertionError("Reynolds basis is not reduced")
        basis.append(reynolds)

    invariance_tests = 0
    for element in sorted(group):
        for vector in basis:
            if action(element, vector) != vector:
                raise AssertionError("Reynolds seed failed invariance")
            invariance_tests += 1
    coordinate_rows = [
        [vector[position] for position in quotient_basis] for vector in basis
    ]
    if matrix_rank_k(c52, coordinate_rows) != 4:
        raise AssertionError("Reynolds basis is dependent")

    def tau(value):
        return value[0] - value[1], -value[1]

    sigma = tuple((-index) % c52.N for index in range(c52.N))
    descent_phase = tuple(
        1 if index != 0 and index % 2 == 0 else 0 for index in range(c52.N)
    )

    def descent(vector):
        result = [c52.K_ZERO] * len(monomials)
        for position, coefficient in enumerate(vector):
            if c52.k_is_zero(coefficient):
                continue
            y_exponent, z_exponent, x_exponents = monomials[position]
            if z_exponent != 0:
                raise AssertionError("descent basis left the cubic-only slice")
            transformed = [0] * c52.N
            phase = 0
            for index, exponent in enumerate(x_exponents):
                transformed[sigma[index]] += exponent
                phase += 2 * descent_phase[index] * exponent
            image = monomial_index[(y_exponent, z_exponent, tuple(transformed))]
            scalar = c52.k_mul(tau(coefficient), c52.k_rho_power(phase))
            result[image] = c52.k_add(result[image], scalar)
        return reduce_vector(result)

    def solve_in_basis(target):
        rows = [
            [basis[column][coordinate] for column in range(4)]
            + [target[coordinate]]
            for coordinate in quotient_basis
        ]
        matrix = [row[:] for row in rows]
        rank = 0
        pivot_columns = []
        pivot_rows = []
        for column in range(4):
            pivot = next(
                i
                for i in range(rank, len(matrix))
                if not c52.k_is_zero(matrix[i][column])
            )
            matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
            inverse = c52.k_inverse(matrix[rank][column])
            matrix[rank] = [c52.k_mul(entry, inverse) for entry in matrix[rank]]
            for i in range(len(matrix)):
                if i == rank or c52.k_is_zero(matrix[i][column]):
                    continue
                scalar = matrix[i][column]
                matrix[i] = [
                    c52.k_sub(left, c52.k_mul(scalar, right))
                    for left, right in zip(matrix[i], matrix[rank])
                ]
            pivot_columns.append(column)
            pivot_rows.append(rank)
            rank += 1
        answer = [c52.K_ZERO] * 4
        for row, column in zip(pivot_rows, pivot_columns):
            answer[column] = matrix[row][4]
        reconstruction = [c52.K_ZERO] * len(monomials)
        for coefficient, vector in zip(answer, basis):
            reconstruction = [
                c52.k_add(left, c52.k_mul(coefficient, right))
                for left, right in zip(reconstruction, vector)
            ]
        if reconstruction != target:
            raise AssertionError("semilinear image not in invariant basis")
        return answer

    descent_columns = [solve_in_basis(descent(vector)) for vector in basis]
    expected_columns = [
        [c52.K_ONE, c52.K_ZERO, c52.K_ZERO, c52.K_ZERO],
        [c52.K_ZERO, c52.K_ZERO, c52.K_ZERO, c52.K_ONE],
        [c52.K_ZERO, c52.K_ZERO, c52.k_rho_power(2), c52.K_ZERO],
        [c52.K_ZERO, c52.K_ONE, c52.K_ZERO, c52.K_ZERO],
    ]
    if descent_columns != expected_columns:
        raise AssertionError("semilinear descent matrix drifted")
    for i in range(4):
        for j in range(4):
            value = c52.K_ZERO
            for k in range(4):
                value = c52.k_add(
                    value,
                    c52.k_mul(descent_columns[k][i], tau(descent_columns[j][k])),
                )
            expected = c52.K_ONE if i == j else c52.K_ZERO
            if value != expected:
                raise AssertionError("A*tau(A) is not identity")

    theta = (Fraction(1), Fraction(2))
    q_basis = [
        [c52.K_ONE, c52.K_ZERO, c52.K_ZERO, c52.K_ZERO],
        [c52.K_ZERO, c52.K_ONE, c52.K_ZERO, c52.K_ONE],
        [c52.K_ZERO, theta, c52.K_ZERO, c52.k_neg(theta)],
        [c52.K_ZERO, c52.K_ZERO, c52.k_neg(c52.k_rho_power(1)), c52.K_ZERO],
    ]
    for vector in q_basis:
        image = [c52.K_ZERO] * 4
        for coefficient, column in zip(vector, descent_columns):
            for row in range(4):
                image[row] = c52.k_add(
                    image[row], c52.k_mul(tau(coefficient), column[row])
                )
        if image != vector:
            raise AssertionError("claimed rational basis is not semilinearly fixed")
    if matrix_rank_k(c52, [[q_basis[column][row] for column in range(4)] for row in range(4)]) != 4:
        raise AssertionError("rational basis is not a K-basis after extension")

    sparse_basis = []
    for vector in basis:
        terms = []
        for position, coefficient in enumerate(vector):
            if c52.k_is_zero(coefficient):
                continue
            terms.append({
                "monomial": [monomials[position][0], monomials[position][1], list(monomials[position][2])],
                "coefficient": k_serial(coefficient),
            })
        sparse_basis.append(terms)

    return {
        "group": group,
        "multiplication_table": table,
        "inverse_ids": inverses,
        "character": character,
        "monomials": monomials,
        "quotient_basis": quotient_basis,
        "basis": basis,
        "sparse_basis": sparse_basis,
        "descent_columns": descent_columns,
        "q_basis": q_basis,
        "invariance_tests": invariance_tests,
        "relation_rank": len(pivots),
    }


def tangent_operator_component(c52, tangent: dict[str, Any]) -> dict[str, Any]:
    """Construct R_(1,0) and verify multiplication by y is an isomorphism."""

    source_monomials = []
    source_monomials.extend(
        (1, 0, exponent) for exponent in c52.compositions(3, c52.N)
    )
    source_monomials.extend(
        (0, 1, exponent) for exponent in c52.compositions(2, c52.N)
    )
    if len(source_monomials) != 156:
        raise AssertionError("R_(1,0) ambient dimension drifted")
    source_index = {
        monomial: position for position, monomial in enumerate(source_monomials)
    }
    edge_weights = {
        edge: c52.k_rho_power(exponent)
        for edge, exponent in c52.edge_weight_exponents().items()
    }

    def source_vector(terms):
        result = [c52.K_ZERO] * len(source_monomials)
        for coefficient, monomial in terms:
            result[source_index[monomial]] = c52.k_add(
                result[source_index[monomial]], coefficient
            )
        return result

    def derivative_q(variable):
        terms = []
        for edge, coefficient in edge_weights.items():
            if variable in edge:
                neighbor = edge[0] if edge[1] == variable else edge[1]
                exponent = [0] * c52.N
                exponent[neighbor] = 1
                terms.append((coefficient, tuple(exponent)))
        return terms

    source_relations = []
    for variable in range(c52.N):
        for multiplier in range(c52.N):
            exponent = [0] * c52.N
            exponent[variable] += 2
            exponent[multiplier] += 1
            terms = [(c52.k_int(3), (1, 0, tuple(exponent)))]
            for coefficient, x_exponent in derivative_q(variable):
                shifted = list(x_exponent)
                shifted[multiplier] += 1
                terms.append((coefficient, (0, 1, tuple(shifted))))
            source_relations.append(source_vector(terms))
    source_relations.append(source_vector([
        (c52.K_ONE, (1, 0, tuple(3 if i == j else 0 for i in range(c52.N))))
        for j in range(c52.N)
    ]))
    source_relations.append(source_vector([
        (
            coefficient,
            (0, 1, tuple(1 if i in edge else 0 for i in range(c52.N))),
        )
        for edge, coefficient in edge_weights.items()
    ]))
    for multiplier in range(c52.N):
        terms = []
        for edge, coefficient in edge_weights.items():
            exponent = [0] * c52.N
            exponent[edge[0]] += 1
            exponent[edge[1]] += 1
            exponent[multiplier] += 1
            terms.append((coefficient, (1, 0, tuple(exponent))))
        source_relations.append(source_vector(terms))
    if len(source_relations) != 74:
        raise AssertionError("R_(1,0) relation row count drifted")
    source_rref, source_pivots = c52.exact_rref(source_relations)
    if len(source_pivots) != 73:
        raise AssertionError("R_(1,0) relation rank drifted")
    source_pivot_row = {
        pivot: row for row, pivot in enumerate(source_pivots)
    }
    source_basis = [
        index for index in range(len(source_monomials)) if index not in source_pivot_row
    ]

    target_monomials = tangent["monomials"]
    target_relations = c52.jacobian_relations(target_monomials)
    target_rref, target_pivots = c52.exact_rref(target_relations)
    target_pivot_row = {
        pivot: row for row, pivot in enumerate(target_pivots)
    }
    target_basis = [
        index for index in range(len(target_monomials)) if index not in target_pivot_row
    ]
    target_index = {
        monomial: position for position, monomial in enumerate(target_monomials)
    }

    def reduce_target(vector):
        result = vector[:]
        for pivot in target_pivots:
            coefficient = result[pivot]
            if c52.k_is_zero(coefficient):
                continue
            result = [
                c52.k_sub(left, c52.k_mul(coefficient, right))
                for left, right in zip(result, target_rref[target_pivot_row[pivot]])
            ]
        return result

    def multiply_by_y(source_vector_value):
        result = [c52.K_ZERO] * len(target_monomials)
        for position, coefficient in enumerate(source_vector_value):
            if c52.k_is_zero(coefficient):
                continue
            y_exponent, z_exponent, x_exponents = source_monomials[position]
            target = (y_exponent + 1, z_exponent, x_exponents)
            result[target_index[target]] = c52.k_add(
                result[target_index[target]], coefficient
            )
        return reduce_target(result)

    relation_map_tests = 0
    for relation in source_relations:
        if any(not c52.k_is_zero(entry) for entry in multiply_by_y(relation)):
            raise AssertionError("multiplication by y is not well defined on R_(1,0)")
        relation_map_tests += 1
    map_rows = []
    for source_position in source_basis:
        unit = [c52.K_ZERO] * len(source_monomials)
        unit[source_position] = c52.K_ONE
        image = multiply_by_y(unit)
        map_rows.append([image[position] for position in target_basis])
    map_rank = matrix_rank_k(c52, map_rows)
    if len(source_basis) != 83 or len(target_basis) != 83 or map_rank != 83:
        raise AssertionError("multiplication by y is not an 83-dimensional isomorphism")

    lift_tests = 0
    for target_vector in tangent["basis"]:
        source_vector_value = [c52.K_ZERO] * len(source_monomials)
        for position, coefficient in enumerate(target_vector):
            if c52.k_is_zero(coefficient):
                continue
            y_exponent, z_exponent, x_exponents = target_monomials[position]
            if (y_exponent, z_exponent) != (2, 0):
                raise AssertionError("frozen invariant class is not cubic-only")
            source_vector_value[source_index[(1, 0, x_exponents)]] = coefficient
        if multiply_by_y(source_vector_value) != target_vector:
            raise AssertionError("[y*p_i] does not map to [y^2*p_i]")
        lift_tests += 1
    return {
        "ambient_piece": "S_(1,0)",
        "ambient_dimension": len(source_monomials),
        "ambient_decomposition": {"y_times_cubics": 120, "z_times_quadrics": 36},
        "Jacobian_relation_rows": len(source_relations),
        "Jacobian_relation_rank": len(source_pivots),
        "quotient_piece": "R_(1,0)",
        "quotient_dimension": len(source_basis),
        "relation_images_under_multiply_y_tested": relation_map_tests,
        "multiplication_map": "times y: R_(1,0) -> R_(2,-3)",
        "multiplication_matrix_shape": [len(source_basis), len(target_basis)],
        "multiplication_matrix_rank": map_rank,
        "multiplication_isomorphism": True,
        "frozen_operator_lift_tests": lift_tests,
        "operator_classes": "[y*p_i]",
        "first_variation_images": "[y^2*p_i]",
    }


def ambient_descent_controls(c52, tangent: dict[str, Any], c53_payload: dict[str, Any]) -> dict[str, Any]:
    """Reconstruct the semilinear descent datum on the ambient PGL action."""

    elements = sorted(tangent["group"])
    element_index = {element: index for index, element in enumerate(elements)}
    identity = c52.IDENTITY
    m_element = (
        tuple((-index) % c52.N for index in range(c52.N)),
        tuple(1 if index != 0 and index % 2 == 0 else 0 for index in range(c52.N)),
    )

    def inverse(element):
        permutation, phases = element
        inverse_permutation = [0] * c52.N
        for index, image in enumerate(permutation):
            inverse_permutation[image] = index
        inverse_phases = [0] * c52.N
        for image in range(c52.N):
            inverse_phases[image] = (-phases[inverse_permutation[image]]) % 3
        return c52.canonical_element(tuple(inverse_permutation), tuple(inverse_phases))

    def tau_element(element):
        return c52.canonical_element(
            element[0], tuple((-phase) % 3 for phase in element[1])
        )

    m_inverse = inverse(m_element)
    if c52.multiply(m_element, tau_element(m_element)) != identity:
        raise AssertionError("ambient coordinate cocycle M*tau(M) failed")
    if c52.multiply(m_element, m_inverse) != identity:
        raise AssertionError("ambient coordinate inverse failed")

    # Replay both defining equation lines for every geometric group element;
    # the C52 certificate remains provenance, not a substitute for this C55
    # calculation.  The group dictionary records the exact Q scaling.
    cubic_source = {
        tuple(3 if index == variable else 0 for index in range(c52.N)): c52.K_ONE
        for variable in range(c52.N)
    }
    quadratic_source = {}
    for edge, rho_exponent in c52.edge_weight_exponents().items():
        exponent = tuple(1 if index in edge else 0 for index in range(c52.N))
        quadratic_source[exponent] = c52.k_rho_power(rho_exponent)

    def linear_pullback(terms, element):
        permutation, phases = element
        result = {}
        for exponent, coefficient in terms.items():
            transformed = [0] * c52.N
            phase = 0
            for index, power in enumerate(exponent):
                transformed[permutation[index]] += power
                phase += phases[index] * power
            key = tuple(transformed)
            value = c52.k_mul(coefficient, c52.k_rho_power(phase))
            result[key] = c52.k_add(result.get(key, c52.K_ZERO), value)
        return {key: value for key, value in result.items() if not c52.k_is_zero(value)}

    equation_covariance_tests = 0
    for element, q_scale in tangent["group"].items():
        if linear_pullback(cubic_source, element) != cubic_source:
            raise AssertionError("split group element failed C covariance")
        equation_covariance_tests += 1
        expected_q = {
            exponent: c52.k_mul(c52.k_rho_power(q_scale), coefficient)
            for exponent, coefficient in quadratic_source.items()
        }
        if linear_pullback(quadratic_source, element) != expected_q:
            raise AssertionError("split group element failed Q covariance")
        equation_covariance_tests += 1

    # The coefficient-semilinear pullback used throughout the certificate is
    # D(f)(x)=tau(f)(M^(-1)x).  Replay its effect on the two equations rather
    # than inferring the Cayley-variable action from the final top trace.
    # (The independent Wp top gauge contains z^3 and therefore cannot by
    # itself distinguish z -> rho*z from the erroneous z -> rho^2*z.)
    inverse_permutation, inverse_phases = m_inverse

    def descend_x_polynomial(terms):
        result = {}
        for exponent, coefficient in terms.items():
            transformed = [0] * c52.N
            phase = 0
            for index, power in enumerate(exponent):
                transformed[inverse_permutation[index]] += power
                phase += inverse_phases[index] * power
            key = tuple(transformed)
            descended = c52.k_mul(
                (coefficient[0] - coefficient[1], -coefficient[1]),
                c52.k_rho_power(phase),
            )
            result[key] = c52.k_add(result.get(key, c52.K_ZERO), descended)
        return {key: value for key, value in result.items() if not c52.k_is_zero(value)}

    if descend_x_polynomial(cubic_source) != cubic_source:
        raise AssertionError("D(C)=C failed")
    expected_dq = {
        exponent: c52.k_mul(c52.k_rho_power(2), coefficient)
        for exponent, coefficient in quadratic_source.items()
    }
    if descend_x_polynomial(quadratic_source) != expected_dq:
        raise AssertionError("D(Q)=rho^2*Q failed")
    # D(y)=y and D(z)=rho*z now give D(F)=y*C+rho*z*rho^2*Q=F.
    if c52.k_mul(c52.k_rho_power(1), c52.k_rho_power(2)) != c52.K_ONE:
        raise AssertionError("D(F)=F Cayley auxiliary compatibility failed")

    alpha = []
    compatibility_tests = 0
    for element in elements:
        image = c52.multiply(
            c52.multiply(m_element, tau_element(element)), m_inverse
        )
        if image not in element_index:
            raise AssertionError("semilinear transport left Dih(C12)")
        alpha.append(element_index[image])
        compatibility_tests += 1
    expected = c53_payload["B2_twisted_dihedral_Chow_descent"]["group_scheme"][
        "Galois_alpha_id_map"
    ]
    if alpha != expected:
        raise AssertionError("ambient action descent differs from C53")
    table = tangent["multiplication_table"]
    automorphism_tests = 0
    for left in range(24):
        for right in range(24):
            if alpha[table[left][right]] != table[alpha[left]][alpha[right]]:
                raise AssertionError("semilinear transport is not a group automorphism")
            automorphism_tests += 1
    if [index for index, image in enumerate(alpha) if index == image] != [0, 13]:
        raise AssertionError("rational geometric-point locus drifted")
    scheme = c53_payload["B2_twisted_dihedral_Chow_descent"]["group_scheme"]
    rotation = scheme["generator_r_id"]
    reflection = scheme["generator_s_id"]
    if alpha[rotation] != tangent["inverse_ids"][rotation]:
        raise AssertionError("alpha(r) is not r inverse")
    if alpha[reflection] != table[rotation][reflection]:
        raise AssertionError("alpha(s) is not r*s")
    return {
        "coordinate_descent_matrix_projective_monomial": {
            "permutation_output_to_input": list(m_element[0]),
            "rho_phase_exponents": list(m_element[1]),
            "formula": "M(x)_i=rho^(m_i)*x_(-i)",
        },
        "coordinate_cocycle": "M*tau(M)=I8",
        "coordinate_cocycle_exact": True,
        "Cayley_extension": {
            "D_formula": "D(f)(x)=tau(f)(M^(-1)x)",
            "D_C_equals_C": True,
            "D_Q_equals_rho2_Q": True,
            "D_y": "y",
            "D_z": "rho*z",
            "D_F_equals_F": True,
            "quadratic_monomials_compared": len(quadratic_source),
            "cubic_monomials_compared": len(cubic_source),
        },
        "transport_formula": "alpha(g)=M*tau(g)*M^(-1) in PGL8(K)",
        "transported_element_ids": alpha,
        "exact_semilinear_compatibility_tests": compatibility_tests,
        "split_equation_line_covariance_tests": equation_covariance_tests,
        "group_table_automorphism_tests": automorphism_tests,
        "alpha_rotation": "r^(-1)",
        "alpha_reflection": "r*s=s*r^(-1)",
        "fixed_geometric_element_ids": [0, 13],
        "finite_etale_Q_form_rank": 24,
        "Q_rational_geometric_point_count": 2,
        "projective_action_descent_datum_verified": True,
        "descended_morphism": "mathscrG -> PGL8_Q",
        "effective_finite-etale_and_projective_descent_is_written_theorem": True,
        "all_24_geometric_matrices_Q_rational": False,
    }


def x_monomial(exponents: Iterable[int]) -> str:
    factors = []
    for index, exponent in enumerate(exponents):
        if exponent == 1:
            factors.append(f"x{index}")
        elif exponent:
            factors.append(f"x{index}^{exponent}")
    return "*".join(factors) if factors else "1"


def p_singular(c52, vector, monomials) -> str:
    terms = []
    for position, coefficient in enumerate(vector):
        if c52.k_is_zero(coefficient):
            continue
        y_exponent, z_exponent, x_exponents = monomials[position]
        if (y_exponent, z_exponent, sum(x_exponents)) != (2, 0, 3):
            raise AssertionError("basis is not represented by y^2 times a cubic")
        terms.append(f"({k_singular(coefficient)})*{x_monomial(x_exponents)}")
    return "+".join(terms).replace("+-", "-")


def semilinear_raw_top_image(c52, ordering: str) -> dict[str, Any]:
    """Derive D(top gauge) from M^-1 and D(z)=rho*z, before reduction."""
    if ordering == "wp":
        source_x = (0, 0, 0, 0, 0, 0, 2, 2)
        y_exponent, z_exponent = 0, 5
    elif ordering == "Wp":
        source_x = (0, 0, 0, 0, 0, 0, 0, 6)
        y_exponent, z_exponent = 2, 3
    else:
        raise ValueError(ordering)
    inverse_permutation = tuple((-index) % c52.N for index in range(c52.N))
    m_phases = tuple(
        1 if index != 0 and index % 2 == 0 else 0 for index in range(c52.N)
    )
    inverse_phases = tuple((2 * phase) % 3 for phase in m_phases)
    transformed_x = [0] * c52.N
    x_phase_exponent = 0
    for index, power in enumerate(source_x):
        transformed_x[inverse_permutation[index]] += power
        x_phase_exponent += inverse_phases[index] * power
    z_phase_exponent = z_exponent  # D(z)=rho*z.
    x_prefactor = c52.k_rho_power(x_phase_exponent)
    z_prefactor = c52.k_rho_power(z_phase_exponent)
    total_prefactor = c52.k_mul(x_prefactor, z_prefactor)
    result = {
        "source_x": source_x,
        "source_y": y_exponent,
        "source_z": z_exponent,
        "image_x": tuple(transformed_x),
        "image_y": y_exponent,
        "image_z": z_exponent,
        "x_prefactor": x_prefactor,
        "z_prefactor": z_prefactor,
        "total_prefactor": total_prefactor,
    }
    if ordering == "wp" and result != {
        "source_x": (0, 0, 0, 0, 0, 0, 2, 2),
        "source_y": 0,
        "source_z": 5,
        "image_x": (0, 2, 2, 0, 0, 0, 0, 0),
        "image_y": 0,
        "image_z": 5,
        "x_prefactor": c52.k_rho_power(1),
        "z_prefactor": c52.k_rho_power(2),
        "total_prefactor": c52.K_ONE,
    }:
        raise AssertionError("programmatic wp raw top descent drifted")
    return result


def raw_top_singular(c52, raw: dict[str, Any]) -> str:
    factors = [x_monomial(raw["image_x"])]
    if raw["image_y"]:
        factors.append("y" if raw["image_y"] == 1 else f"y^{raw['image_y']}")
    if raw["image_z"]:
        factors.append("z" if raw["image_z"] == 1 else f"z^{raw['image_z']}")
    return f"({k_singular(raw['total_prefactor'])})*" + "*".join(factors)


def yukawa_script(c52, tangent: dict[str, Any], ordering: str) -> str:
    if ordering not in {"wp", "Wp"}:
        raise ValueError(ordering)
    lines = [
        f"ring r=(0,rho),(x0,x1,x2,x3,x4,x5,x6,x7,y,z),{ordering}(1,1,1,1,1,1,1,1,1,2);",
        "minpoly=rho^2+rho+1;",
        "option(redSB);",
        "poly C=x0^3+x1^3+x2^3+x3^3+x4^3+x5^3+x6^3+x7^3;",
        "poly Q=x0*x1+x1*x2+x2*x3+x3*x4+x4*x5+x5*x6+x6*x7+rho*x7*x0;",
        "poly F=y*C+z*Q;",
        "ideal G=std(jacob(F));",
        '"GSIZE",size(G);',
        "int le_index;",
        "for (le_index=1;le_index<=size(G);le_index++)",
        "{",
        '  "LE",leadexp(G[le_index]);',
        "}",
    ]
    for index, vector in enumerate(tangent["basis"]):
        lines.append(f"poly p{index}={p_singular(c52, vector, tangent['monomials'])};")
    raw_top = semilinear_raw_top_image(c52, ordering)
    lines.extend([
        f"poly DTOP=reduce({raw_top_singular(c52, raw_top)},G);",
        '"DTOPC",leadcoef(DTOP);',
        '"DTOPE",leadexp(DTOP);',
    ])
    for point_index, point in enumerate(DIRECT_CUBE_POINTS):
        linear = "+".join(
            f"({coefficient})*p{index}"
            for index, coefficient in enumerate(point)
            if coefficient
        )
        label = f"{point_index:02d}"
        lines.extend([
            f"poly V{label}=reduce(y^5*({linear})^3,G);",
            f'"V{label}",leadcoef(V{label});',
            f'"W{label}",leadexp(V{label});',
        ])
    lines.append("quit;")
    return "\n".join(lines) + "\n"


def parse_k_number(text: str):
    rho = sp.Symbol("rho")
    expression = sp.expand(sp.sympify(text.replace("^", "**"), locals={"rho": rho}))
    polynomial = sp.Poly(expression, rho, domain=sp.QQ)
    if polynomial.degree() > 1:
        raise AssertionError(f"unreduced Q(rho) number: {text}")
    a = polynomial.coeff_monomial(1)
    b = polynomial.coeff_monomial(rho)
    return Fraction(int(a.p), int(a.q)), Fraction(int(b.p), int(b.q))


def parse_exponent(text: str) -> tuple[int, ...]:
    entries = tuple(int(part.strip()) for part in text.split(","))
    if len(entries) != 10:
        raise AssertionError(f"bad exponent vector: {text}")
    return entries


def run_yukawa_backend(c52, tangent: dict[str, Any], ordering: str) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="c55-yukawa-") as temporary:
        script = Path(temporary) / f"yukawa_{ordering}.sing"
        script.write_text(yukawa_script(c52, tangent, ordering), encoding="utf-8")
        process = subprocess.run(
            ["Singular", "-q", str(script)],
            capture_output=True,
            text=True,
            timeout=180,
            check=False,
        )
    if process.returncode != 0 or re.search(r"^\s*\?", process.stdout, re.MULTILINE):
        raise AssertionError(f"Singular Yukawa backend failed: {process.stderr[-2000:]}")
    size_match = re.search(r"^GSIZE\s+(\d+)\s*$", process.stdout, re.MULTILINE)
    if size_match is None:
        raise AssertionError("missing Singular GSIZE")
    leads = [
        parse_exponent(match.group(1))
        for match in re.finditer(r"^LE\s+([0-9,]+)\s*$", process.stdout, re.MULTILINE)
    ]
    if len(leads) != int(size_match.group(1)):
        raise AssertionError("Singular leading-exponent count mismatch")
    descent_coefficient = re.search(
        r"^DTOPC\s+(.+?)\s*$", process.stdout, re.MULTILINE
    )
    descent_exponent = re.search(
        r"^DTOPE\s+([0-9,]+)\s*$", process.stdout, re.MULTILINE
    )
    if descent_coefficient is None or descent_exponent is None:
        raise AssertionError("missing top-line descent output")
    evaluation_values = []
    evaluation_exponents = []
    for point_index, _ in enumerate(DIRECT_CUBE_POINTS):
        label = f"{point_index:02d}"
        coefficient = re.search(
            rf"^V{label}\s+(.+?)\s*$", process.stdout, re.MULTILINE
        )
        exponent = re.search(
            rf"^W{label}\s+([0-9,]+)\s*$", process.stdout, re.MULTILINE
        )
        if coefficient is None or exponent is None:
            raise AssertionError(f"missing direct cube evaluation {label}")
        evaluation_values.append(parse_k_number(coefficient.group(1)))
        evaluation_exponents.append(parse_exponent(exponent.group(1)))
    if len(set(evaluation_exponents)) != 1:
        raise AssertionError("direct cube evaluations do not share a top coordinate")
    return {
        "ordering": ordering,
        "groebner_size": len(leads),
        "leads": leads,
        "direct_cube_points": DIRECT_CUBE_POINTS,
        "direct_cube_values": evaluation_values,
        "trace_exponent": evaluation_exponents[0],
        "top_descent_coefficient": parse_k_number(descent_coefficient.group(1)),
        "top_descent_exponent": parse_exponent(descent_exponent.group(1)),
        "stdout_sha256": hashlib.sha256(process.stdout.encode()).hexdigest(),
    }


def compositions(total: int, slots: int, prefix: tuple[int, ...] = ()):
    if slots == 1:
        yield prefix + (total,)
        return
    for entry in range(total + 1):
        yield from compositions(total - entry, slots - 1, prefix + (entry,))


def top_component(leads: list[tuple[int, ...]]) -> dict[str, Any]:
    ambient = 0
    standard = []
    for z_exponent in range(6):
        y_exponent = 5 - z_exponent
        x_degree = 9 - z_exponent
        for x_exponents in compositions(x_degree, 8):
            ambient += 1
            exponent = x_exponents + (y_exponent, z_exponent)
            if not any(
                all(left >= right for left, right in zip(exponent, leading))
                for leading in leads
            ):
                standard.append(exponent)
    if ambient != 24145 or standard != [(0, 0, 0, 0, 0, 0, 2, 2, 0, 5)]:
        raise AssertionError("top Cayley component drifted")
    return {
        "ambient_monomial_count": ambient,
        "quotient_dimension": len(standard),
        "standard_monomial_exponents_x0_to_x7_y_z": list(standard[0]),
        "standard_monomial": "x6^2*x7^2*z^5",
    }


def multinomial_for_triple(triple: tuple[int, int, int]) -> int:
    counts = Counter(triple)
    return math.factorial(3) // reduce(lambda a, b: a * math.factorial(b), counts.values(), 1)


def degree_three_exponents() -> list[tuple[int, int, int, int]]:
    return sorted(
        (
            (a, b, c, 3 - a - b - c)
            for a in range(4)
            for b in range(4 - a)
            for c in range(4 - a - b)
        ),
        reverse=True,
    )


def interpolate_direct_cubes(c52, points, values) -> tuple[dict[tuple[int, ...], Any], int]:
    monomials = degree_three_exponents()
    matrix = []
    for point, value in zip(points, values):
        matrix.append([
            c52.k_int(math.prod(point[index] ** exponent for index, exponent in enumerate(monomial)))
            for monomial in monomials
        ] + [value])
    rank = 0
    for column in range(len(monomials)):
        pivot = next(
            (row for row in range(rank, len(matrix)) if not c52.k_is_zero(matrix[row][column])),
            None,
        )
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        inverse = c52.k_inverse(matrix[rank][column])
        matrix[rank] = [c52.k_mul(entry, inverse) for entry in matrix[rank]]
        for row in range(len(matrix)):
            if row == rank or c52.k_is_zero(matrix[row][column]):
                continue
            scalar = matrix[row][column]
            matrix[row] = [
                c52.k_sub(left, c52.k_mul(scalar, right))
                for left, right in zip(matrix[row], matrix[rank])
            ]
        rank += 1
    if rank != 20:
        raise AssertionError("direct-cube evaluation points are not unisolvent")
    coefficients = {monomial: matrix[row][-1] for row, monomial in enumerate(monomials)}
    if any(c52.k_is_zero(value) for value in coefficients.values()):
        raise AssertionError("unexpected zero coefficient after direct-cube interpolation")
    return coefficients, rank


def traces_from_direct_cubic(c52, coefficients):
    traces = {}
    for triple in combinations_with_replacement(range(4), 3):
        exponent = tuple(triple.count(index) for index in range(4))
        traces[triple] = c52.k_div(
            coefficients[exponent], c52.k_int(multinomial_for_triple(triple))
        )
    return traces


def rational_cubic(c52, traces: dict[tuple[int, int, int], Any], q_basis):
    coefficients = {
        exponent: c52.K_ZERO
        for exponent in EXPECTED_PRIMITIVE
    }
    for triple, trace in traces.items():
        scalar = c52.k_mul(c52.k_int(multinomial_for_triple(triple)), trace)
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    change = c52.k_mul(
                        q_basis[a][triple[0]],
                        c52.k_mul(q_basis[b][triple[1]], q_basis[c][triple[2]]),
                    )
                    if c52.k_is_zero(change):
                        continue
                    exponent = [0, 0, 0, 0]
                    exponent[a] += 1
                    exponent[b] += 1
                    exponent[c] += 1
                    key = tuple(exponent)
                    coefficients[key] = c52.k_add(
                        coefficients[key], c52.k_mul(scalar, change)
                    )
    base = coefficients[(3, 0, 0, 0)]
    if c52.k_is_zero(base):
        raise AssertionError("Yukawa base coefficient vanished")
    rational_ratios = {}
    for exponent, coefficient in coefficients.items():
        ratio = c52.k_div(coefficient, base)
        if ratio[1] != 0:
            raise AssertionError(f"Q descent failed at {exponent}")
        rational_ratios[exponent] = ratio[0]
    denominator_lcm = math.lcm(*(value.denominator for value in rational_ratios.values()))
    integers = {
        exponent: int(value * denominator_lcm)
        for exponent, value in rational_ratios.items()
    }
    coefficient_gcd = math.gcd(*(abs(value) for value in integers.values()))
    primitive = {key: value // coefficient_gcd for key, value in integers.items()}
    if primitive[(3, 0, 0, 0)] < 0:
        primitive = {key: -value for key, value in primitive.items()}
    if primitive != EXPECTED_PRIMITIVE:
        raise AssertionError("primitive rational Yukawa cubic drifted")
    return {
        "_raw_common_scale": base,
        "common_K_trace_scale": k_serial(base),
        "ratios_to_u0_cubed_are_rational": True,
        "denominator_lcm_before_primitive_reduction": denominator_lcm,
        "coefficient_gcd_after_clearing_denominators": coefficient_gcd,
        "primitive": primitive,
    }


def primitive_entries(primitive: dict[tuple[int, ...], int]) -> list[dict[str, Any]]:
    return [
        {"exponents_u0_to_u3": list(exponent), "coefficient": primitive[exponent]}
        for exponent in sorted(primitive, reverse=True)
    ]


def cubic_singular_text(primitive: dict[tuple[int, ...], int]) -> str:
    terms = []
    for exponent in sorted(primitive, reverse=True):
        coefficient = primitive[exponent]
        monomial = []
        for index, power in enumerate(exponent):
            if power == 1:
                monomial.append(f"u{index}")
            elif power:
                monomial.append(f"u{index}^{power}")
        terms.append(f"({coefficient})*{'*'.join(monomial)}")
    return "+".join(terms).replace("+-", "-")


def smoothness_backend(primitive: dict[tuple[int, ...], int], ordering: str) -> dict[str, Any]:
    if ordering not in {"dp", "Dp"}:
        raise ValueError(ordering)
    script_text = "\n".join([
        f"ring q=0,(u0,u1,u2,u3),{ordering};",
        f"poly Y={cubic_singular_text(primitive)};",
        "ideal D=jacob(Y);",
        "ideal G=std(D);",
        '"VDIM",vdim(G);',
        '"GSIZE",size(G);',
        '"HILB";',
        "hilb(G,1);",
        "quit;",
    ]) + "\n"
    with tempfile.TemporaryDirectory(prefix="c55-smooth-") as temporary:
        script = Path(temporary) / "smooth.sing"
        script.write_text(script_text, encoding="utf-8")
        process = subprocess.run(
            ["Singular", "-q", str(script)],
            capture_output=True,
            text=True,
            timeout=90,
            check=False,
        )
    if process.returncode != 0:
        raise AssertionError(f"Singular smoothness backend failed: {process.stderr[-2000:]}")
    vdim = re.search(r"^VDIM\s+(\d+)\s*$", process.stdout, re.MULTILINE)
    size = re.search(r"^GSIZE\s+(\d+)\s*$", process.stdout, re.MULTILINE)
    hilbert = re.search(r"^HILB\s*\n([^\n]+)", process.stdout, re.MULTILINE)
    if vdim is None or size is None or hilbert is None:
        raise AssertionError("smoothness backend output missing")
    numerator = [int(value) for value in hilbert.group(1).split(",")]
    if int(vdim.group(1)) != 16 or numerator != [1, 0, -4, 0, 6, 0, -4, 0, 1, 0]:
        raise AssertionError("Jacobian complete-intersection certificate failed")
    return {
        "ordering": ordering,
        "jacobian_quotient_length": int(vdim.group(1)),
        "jacobian_groebner_size": int(size.group(1)),
        "hilbert_numerator": numerator,
        "expected_complete_intersection_length": 2**4,
        "projective_singular_locus_empty": True,
    }


def factorization_over_q(primitive: dict[tuple[int, ...], int]) -> list[dict[str, int]]:
    variables = sp.symbols("u0:4")
    expression = 0
    for exponent, coefficient in primitive.items():
        monomial = coefficient
        for variable, power in zip(variables, exponent):
            monomial *= variable**power
        expression += monomial
    content, factors = sp.factor_list(expression, *variables)
    if abs(int(content)) != 1 or len(factors) != 1 or factors[0][1] != 1:
        raise AssertionError("primitive cubic factors over Q")
    polynomial = sp.Poly(factors[0][0], *variables)
    if polynomial.total_degree() != 3:
        raise AssertionError("unexpected Q factor degree")
    return [{"degree": polynomial.total_degree(), "multiplicity": factors[0][1]}]


def build_payload() -> dict[str, Any]:
    source_locks, source_certificates = source_bundle()
    release_provenance = verify_release_provenance()
    c52 = load_c52_backend()
    tangent = tangent_computation(c52)
    tangent_operators = tangent_operator_component(c52, tangent)
    infinitesimal_stabilizer = infinitesimal_ideal_stabilizer(c52)
    producer_yukawa = run_yukawa_backend(c52, tangent, "wp")
    if producer_yukawa["groebner_size"] != 604:
        raise AssertionError("producer Groebner size drifted")
    top = top_component(producer_yukawa["leads"])
    if tuple(top["standard_monomial_exponents_x0_to_x7_y_z"]) != producer_yukawa["trace_exponent"]:
        raise AssertionError("Yukawa products do not land in the certified top monomial")
    direct_coefficients, interpolation_rank = interpolate_direct_cubes(
        c52,
        producer_yukawa["direct_cube_points"],
        producer_yukawa["direct_cube_values"],
    )
    producer_traces = traces_from_direct_cubic(c52, direct_coefficients)
    cubic = rational_cubic(c52, producer_traces, tangent["q_basis"])
    top_descent = producer_yukawa["top_descent_coefficient"]
    top_scale = cubic["_raw_common_scale"]
    top_scale_tau = (top_scale[0] - top_scale[1], -top_scale[1])
    if top_descent != c52.k_div(top_scale, top_scale_tau):
        raise AssertionError("top-line descent is incompatible with the rational Yukawa scale")
    top_descent_tau = (top_descent[0] - top_descent[1], -top_descent[1])
    if c52.k_mul(top_descent, top_descent_tau) != c52.K_ONE:
        raise AssertionError("top-line semilinear cocycle failed")
    if producer_yukawa["top_descent_exponent"] != producer_yukawa["trace_exponent"]:
        raise AssertionError("top-line descent left the certified top gauge")
    entries = primitive_entries(cubic["primitive"])
    smoothness = smoothness_backend(cubic["primitive"], "dp")
    factors = factorization_over_q(cubic["primitive"])

    c52_payload = source_certificates["C52_certificate"]["payload"]
    c53_payload = source_certificates["C53_certificate"]["payload"]
    c54_payload = source_certificates["C54_certificate"]["payload"]
    ambient_descent = ambient_descent_controls(c52, tangent, c53_payload)
    h32 = tangent["character"]["H32_character"]
    h41 = tangent["character"]["H41_character"]
    if c52_payload["cayley_jacobian_representation"]["H32_character"]["trivial_multiplicity"] != 4:
        raise AssertionError("C52 invariant multiplicity source mismatch")
    if c53_payload["B1_explicit_n4_Q_model"]["dimension"] != 5 or len(
        c53_payload["B1_explicit_n4_Q_model"]["descent_M"][
            "permutation_output_to_input"
        ]
    ) != 8:
        raise AssertionError("C53 n=4 source mismatch")
    if c54_payload["rational_group_form"]["Q_rational_point_count"] != 2:
        raise AssertionError("C54 rational group-form source mismatch")

    triple_rows = []
    for triple in combinations_with_replacement(range(4), 3):
        triple_rows.append({
            "indices": list(triple),
            "trace_coefficient": k_serial(producer_traces[triple]),
            "polynomial_multiplicity": multinomial_for_triple(triple),
        })
    basis_rows = [
        [k_serial(entry) for entry in column] for column in tangent["q_basis"]
    ]
    descent_rows = [
        [k_serial(entry) for entry in column] for column in tangent["descent_columns"]
    ]

    primitive_sha = hashlib.sha256(canonical_json(entries)).hexdigest()
    return {
        "material_passport": {
            "candidate_id": CANDIDATE_ID,
            "project_slug": PROJECT_SLUG,
            "date_utc": "2026-08-14",
            "artifact_kind": "exact finite-algebra certificate",
            "verification_status": "REPRODUCIBLE_EXACT_COMPUTATION",
        },
        "source_lock": {
            "frozen_upstream_artifacts": source_locks,
            "committed_release_provenance": release_provenance,
            "base_field": "K=Q(rho), rho^2+rho+1=0",
            "action_convention": "x_i maps to rho^(e_i) x_(sigma(i)); output-to-input permutation convention",
            "residue_orientation_multiplier": "det(M_g)/det(diag(1,rho^lambda_g))",
            "descent_convention": "D(p)(x)=tau(p)(M_4^(-1)x), tau(rho)=rho^2",
            "Tate_twist_convention": "Q(1) sends (p,q) to (p-1,q-1)",
            "geometric_Frobenius_used": False,
        },
        "pre_release_chronology": {
            "architecture_report_sha256": ARCHITECTURE_REPORT_SHA256,
            "status": "UNPACKAGED_NOT_REPLAYED_NOT_THEOREM_INPUT",
            "counts_as_source_control_or_gate_evidence": False,
            "absolute_temporary_path_recorded": False,
        },
        "claim_scope": {
            "title": "The rational Yukawa surface of the fourth Henon dihedral core",
            "computed_gates": ["G0 source lock", "G3 ring replay", "G5 rational cubic"],
            "finite_controls_for_written_gates": ["G1 deformation", "G2 relative projector", "G4 Yukawa identification"],
            "purely_written_gate": "G6 functorial polarized-VHS realization criterion",
            "CAS_proves_relative_family_or_VHS": False,
            "CAS_proves_motivic_realization": False,
            "candidate_comparison_performed": False,
        },
        "complete_intersection_controls": {
            **complete_intersection_controls(),
            "infinitesimal_ideal_stabilizer": infinitesimal_stabilizer,
        },
        "ambient_group_action_descent": ambient_descent,
        "equivariant_tangent": {
            "Cayley_piece": "R_(2,-3)",
            "ambient_monomial_dimension": len(tangent["monomials"]),
            "Jacobian_relation_rank": tangent["relation_rank"],
            "quotient_dimension": len(tangent["quotient_basis"]),
            "group_name": "Dih(C12)",
            "geometric_group_order": len(tangent["group"]),
            "H32_character_trivial_multiplicity": h32["trivial_multiplicity"],
            "H41_character": h41["representation"],
            "Reynolds_seed_x_exponents": [list(row) for row in SEED_X_EXPONENTS],
            "Reynolds_basis_sparse_y2_p_i": tangent["sparse_basis"],
            "all_group_basis_invariance_tests": tangent["invariance_tests"],
            "semilinear_descent_matrix_columns": descent_rows,
            "semilinear_cocycle_A_tau_A": "identity",
            "fixed_Q_basis_columns_in_e_basis": basis_rows,
            "fixed_Q_basis_formula": [
                "q0=e0",
                "q1=e1+e3",
                "q2=(1+2rho)(e1-e3)",
                "q3=-rho*e2",
            ],
            "Q_form_dimension": 4,
            "tangent_operator_component": tangent_operators,
            "class_role_firewall": {
                "H41_generator": "[y] in R_(1,-3)",
                "tangent_deformation_operators": "[y*p_i] in R_(1,0)",
                "first_variation_H32_classes": "[y^2*p_i] in R_(2,-3)",
                "third_variation_classes": "[y^4*p_i*p_j*p_k] in R_(4,-3)",
                "paired_top_trace_classes": "[y^5*p_i*p_j*p_k] in R_(5,-6)",
                "four_y_degree_layers_are_distinct": True,
                "direct_multiplication_of_contracted_R_2_minus3_classes_used": False,
                "allowed_multiplication_route": "apply three R_(1,0) tangent operators successively to the R_(1,-3) generator, then pair with that generator",
                "not_a_literal_linear_equivariant_family": True,
            },
        },
        "relative_projector_controls": {
            "geometric_graphs_in_Reynolds_sum": 24,
            "Reynolds_denominator": 24,
            "group_table_order": len(tangent["multiplication_table"]),
            "group_inverse_count": len(tangent["inverse_ids"]),
            "group_average_convolution_coefficient": "24/24^2=1/24",
            "base_fiber_projector_idempotent": True,
            "untwisted_invariant_Hodge_multiplicities_high_to_low": [1, 4, 4, 1],
            "base_fiber_projected_rank": 10,
            "C53_nonconstant_Q_group_form": True,
            "Q_rational_geometric_group_points": 2,
            "all_24_geometric_automorphisms_individually_Q_rational": False,
            "written_proof_dependencies": [
                "relative graph sum descends for the nonconstant finite-etale Q group form",
                "relative Reynolds correspondence is horizontal and idempotent",
                "rank and Hodge numbers are locally constant on the connected germ",
            ],
            "machine_claims_relative_VHS": False,
        },
        "twist_and_Hodge": {
            "untwisted_weight": 5,
            "untwisted_types_high_to_low": [[4, 1], [3, 2], [2, 3], [1, 4]],
            "Tate_twist": "Q(1)",
            "twisted_weight": 3,
            "twisted_types_high_to_low": [[3, 0], [2, 1], [1, 2], [0, 3]],
            "twisted_multiplicities_high_to_low": [1, 4, 4, 1],
            "Q2_twist_used": False,
            "CY3_type_variation_not_honest_CY3": True,
        },
        "cayley_Yukawa": {
            "Cayley_polynomial": "F=y*C+z*Q",
            "bigrading": {
                "deg_x_i": [0, 1],
                "deg_y": [1, -3],
                "deg_z": [1, -2],
                "top_piece": "R_(5,-6)",
            },
            "formula": "Tr_R_(5,-6)(y^5*p_i*p_j*p_k)",
            "formula_role": "finite multiplication tensor; its Gauss-Manin/polarization identification is a written-proof obligation",
            "derivative_operator_applications": 3,
            "tangent_operator_basis_count": 4,
            "third_variation_before_pairing": "y^4*p_i*p_j*p_k in R_(4,-3)",
            "pairing_extra_H41_generator": "y",
            "producer_monomial_order": "wp(1,1,1,1,1,1,1,1,1,2)",
            "producer_Groebner_basis_size": producer_yukawa["groebner_size"],
            "top_component": top,
            "top_line_semilinear_descent": {
                "ring_descent": "tau on K, x maps by M^(-1), y maps to y, z maps to rho*z",
                "compatibility_identity": "Q_(rho^2)(M^(-1)x)=rho^2*Q_rho(x), hence D(z)=rho*z; raw x6^2*x7^2 -> rho*x1^2*x2^2, z^5 -> rho^2*z^5, total prefactor 1 before quotient",
                "producer_top_gauge": "x6^2*x7^2*z^5",
                "raw_image_quotient_reduction_scalar": k_serial(top_descent),
                "scalar_cocycle_d_tau_d": "1",
                "fixed_Q_generator": "common_K_trace_scale * x6^2*x7^2*z^5",
                "fixed_Q_generator_coefficient": k_serial(top_scale),
                "exact_direct_reduction_verified": True,
            },
            "symmetric_triple_count": len(triple_rows),
            "symmetric_traces_in_e_basis": triple_rows,
            "producer_direct_cube": {
                "expression": "y^5*(a0*p0+a1*p1+a2*p2+a3*p3)^3",
                "evaluation_points": [list(point) for point in DIRECT_CUBE_POINTS],
                "evaluation_values_in_producer_top_gauge": [
                    k_serial(value) for value in producer_yukawa["direct_cube_values"]
                ],
                "direct_reductions": len(DIRECT_CUBE_POINTS),
                "evaluation_matrix_rank": interpolation_rank,
                "interpolation_monomial_count": len(direct_coefficients),
                "unordered_traces_derived_by_dividing_mixed_coefficients_by_1_3_6": True,
                "generic_parameter_Groebner_backend_used": False,
            },
            "only_common_nonzero_trace_normalization_intrinsic": True,
        },
        "rational_cubic_surface": {
            "Q_basis_variables": ["u0", "u1", "u2", "u3"],
            "primitive_integral_coefficients": entries,
            "primitive_coefficients_sha256": primitive_sha,
            "coefficient_count": len(entries),
            "coefficient_gcd": math.gcd(*(abs(row["coefficient"]) for row in entries)),
            "common_K_trace_scale": cubic["common_K_trace_scale"],
            "all_projective_coefficient_ratios_rational": cubic["ratios_to_u0_cubed_are_rational"],
            "factorization_over_Q": factors,
            "producer_smoothness_backend": smoothness,
            "smooth_over_Qbar": True,
            "geometrically_irreducible": True,
            "geometric_irreducibility_reason": "a reducible projective cubic surface over an algebraic closure has intersecting positive-degree components and is singular",
            "intrinsic_object": "projective GL4-class up to one nonzero common scalar",
            "canonical_certificate_model": "the 20-term primitive integral cubic; any reduced display model requires an exact invertible change-of-basis certificate",
        },
        "realization_firewalls": {
            "equal_Hodge_numbers_imply_VHS": False,
            "projective_Yukawa_match_sufficient_for_VHS": False,
            "projective_Yukawa_mismatch_obstructs_pointed_polarized_VHS_isomorphism": "written theorem, not CAS output",
            "finite_prime_matches_prove_motive": False,
            "algebraic_correspondence_constructed": False,
            "honest_CY3_realization_claimed": False,
            "motive_isomorphism_claimed": False,
        },
        "artifact_status": "RELEASE_CANDIDATE",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    arguments = parser.parse_args()
    if arguments.output.exists():
        arguments.output.unlink()
    if sys.flags.optimize:
        raise SystemExit("optimized Python is forbidden for certificate production")
    payload = build_payload()
    certificate = {
        "schema": SCHEMA,
        "payload_sha256": hashlib.sha256(canonical_json(payload)).hexdigest(),
        "payload": payload,
    }
    arguments.output.parent.mkdir(parents=True, exist_ok=True)
    arguments.output.write_text(
        json.dumps(certificate, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"wrote {arguments.output}")
    print(f"payload_sha256={certificate['payload_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
