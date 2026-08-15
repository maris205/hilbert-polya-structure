#!/usr/bin/env python3
"""Independent fail-closed checker for the HCS-C56 exact certificate.

This file deliberately does not import the producer.  It rebuilds the C55
commit lock, line equations, Gröbner quotient, complement and smoothness
ideals, modular factorizations, irreducibility sieve, and W(E6) action by
separate Python/SymPy code.  The lex shape is treated as a compact witness:
every stored coefficient is bound by a canonical hash and its three
back-substitutions are verified by independent Fraction arithmetic.
"""

from __future__ import annotations

import os
os.environ["SYMPY_GROUND_TYPES"] = "python"

import argparse
from collections import Counter, deque
import copy
from fractions import Fraction
import hashlib
from itertools import combinations, product
import json
import math
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import stat
import tempfile
from typing import Any, Iterable
import warnings

import sympy as sp
from sympy.utilities.exceptions import SymPyDeprecationWarning

warnings.filterwarnings("ignore", category=SymPyDeprecationWarning)


PROJECT = Path(__file__).resolve().parents[1]
REPOSITORY = Path(__file__).resolve().parents[3]
C55_PROJECT = "henon_dynamics/henon_mu3_rational_yukawa_surface"
C55_IMPLEMENTATION = "e5661e80da6f7de53f574f97f768744095ba8ae0"
C55_PROVENANCE = "0b0a48db257a4b8bd4af905ab9c9cafba4a4d8be"
C55_PAYLOAD_SHA256 = "6afc529d2ab9e849592d9eba7b76324cc7a840670f50c669f90fdd079c0b4323"
C55_SCHEMA_SHA256 = "2961eb6b5b4aefa0e12ffcb59c9e1095b14f0309e2045fd6d8a7f636dc6dca53"
C55_COEFFICIENT_SHA256 = "1c7065d5644c44bba80658dee5d0704c371e9f446c8c3c6ac29f9590d0831b9e"
LEX_SHAPE_HASHES = {
    "d": "290b1182209491576070b8fa06b5b73b179738a790b9ca258242a3e9152ca48a",
    "c": "4bda88396c5cd784fdc7dc187a36337ad146156993b3187f56365d3c5261a8c7",
    "b": "1a8d7b42a337e6dc31c894dd40d4d1ce071b8b08f948c2d51fd5fefdeed67285",
    "a": "43f22edc37c7e828e75c1abde9c7cef5576e7dcafc854a35f845986d58777b9a",
}
WITNESS_PATTERNS = {
    7: (3, 3, 3, 3, 3, 6, 6),
    19: (1, 4, 4, 6, 12),
    29: (1, 2, 8, 8, 8),
    37: (2, 5, 5, 5, 10),
}
FULL_MANIFEST_EXCLUDED_NAMES = {
    "ARTIFACT_HASHES.sha256", "compile.log", "main.aux", "main.bbl",
    "main.blg", "main.fdb_latexmk", "main.fls", "main.log", "main.out", "main.txt",
}
C55_ARTIFACTS = {
    "route_a_evaluation.yaml": "320b561d1a6fd9a23daafefc3bfdd75d5cf41d6e1eaee6c353bec6f956e7c4a2",
    "evaluations/route_a/HCS-C55/20260815T000000Z.yaml": "320b561d1a6fd9a23daafefc3bfdd75d5cf41d6e1eaee6c353bec6f956e7c4a2",
    "README.md": "7165f8b181d244232bec8ce1a8aa490645a4f5a129b32af1e715d977c94a76ac",
    "INTEGRITY_REPORT.md": "8513ac443a9328fce6c5e681e6efdd112e5da7917d55c7cf8a201b7d65e0389f",
    "IMPLEMENTATION_CHECKLIST.md": "7b99fde66df8ad4f8de3f43442adfeb7f60d5b2d0e71cc9c9ff8d1970eb0340d",
    "THEOREM_PACKAGE.md": "5f843b24094991902f1335054dc8d7f2b0d5ef9753c3a5b756fa964f9af62400",
    "results/ARTIFACT_HASHES.sha256": "8b9a935bddb4aee04561860491eb982311b6776e250b41c8598336fe6bfc2fc9",
    "results/CODE_RESULTS_HASHES.sha256": "7f1fa8bc6f22dd89b6b9a41ae2353129853f39430ba932f048ff295e56ba30e6",
    "results/c55_certificate.json": "aa6a57bc496d78afd5728640083179bb0dd24963deb44e31459c59edc71c381f",
    "results/independent_check.json": "e24c90fac1b222ed161eec677c06209c901f0decc335e769dc7df4ce53c68469",
    "code/c55_producer.py": "3975ad77301939f23754920643b3baa205d67f1451791db3643df693d99c27ba",
    "code/c55_checker.py": "38d7c144389ba116fc9f6d52bb4327cbe4479f7b7ac71f447c406e69c633834b",
    "code/test_c55.py": "ccff76d883b2511a2f7491ed28a3f0af2384af2777c402829ef72de6cdf82281",
    "code/run_c55.sh": "8cce25318f34eb36f3347fce8111074845c98277c89489d9e686dc10a64dba35",
}
MAX_CERTIFICATE_BYTES = 2_000_000


def canonical_json(value: Any) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def sha256_bytes(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def remove_stale_regular_output(path: Path) -> None:
    if not os.path.lexists(path):
        return
    metadata = path.lstat()
    if stat.S_ISLNK(metadata.st_mode) or not stat.S_ISREG(metadata.st_mode):
        raise SystemExit(f"output exists and is not a non-symlink regular file: {path}")
    path.unlink()


def write_new_regular(path: Path, raw: bytes) -> None:
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    if hasattr(os, "O_CLOEXEC"):
        flags |= os.O_CLOEXEC
    if hasattr(os, "O_NOFOLLOW"):
        flags |= os.O_NOFOLLOW
    descriptor = os.open(path, flags, 0o644)
    try:
        view = memoryview(raw)
        while view:
            written = os.write(descriptor, view)
            if written <= 0:
                raise OSError("short write to checker output")
            view = view[written:]
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def strict_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise AssertionError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def parse_integer(token: str) -> int:
    if not re.fullmatch(r"0|-?[1-9][0-9]*", token):
        raise AssertionError("noncanonical JSON integer")
    return int(token)


def reject_float(token: str) -> Any:
    raise AssertionError(f"floating-point JSON value forbidden: {token}")


def strict_load(raw: bytes, *, maximum: int = MAX_CERTIFICATE_BYTES) -> Any:
    if len(raw) > maximum:
        raise AssertionError("oversized JSON input")
    text = raw.decode("utf-8", errors="strict")
    if text.startswith("\ufeff"):
        raise AssertionError("UTF-8 BOM forbidden")
    return json.loads(
        text,
        object_pairs_hook=strict_pairs,
        parse_int=parse_integer,
        parse_float=reject_float,
        parse_constant=reject_float,
    )


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=REPOSITORY,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )


def git_bytes(commit: str, repository_relative: str) -> bytes:
    completed = subprocess.run(
        ["git", "show", f"{commit}:{repository_relative}"],
        cwd=REPOSITORY,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    return completed.stdout


def git_blob(commit: str, repository_relative: str) -> str:
    return run(["git", "rev-parse", f"{commit}:{repository_relative}"]).stdout.strip()


def degree_three_exponents() -> list[list[int]]:
    rows = []
    for e0 in range(3, -1, -1):
        for e1 in range(3 - e0, -1, -1):
            for e2 in range(3 - e0 - e1, -1, -1):
                rows.append([e0, e1, e2, 3 - e0 - e1 - e2])
    return rows


def independent_c55_source_lock() -> tuple[list[dict[str, Any]], dict[str, Any]]:
    for older, newer, label in (
        (C55_IMPLEMENTATION, C55_PROVENANCE, "implementation/provenance"),
        (C55_PROVENANCE, "HEAD", "provenance/released HEAD"),
    ):
        if subprocess.run(["git", "merge-base", "--is-ancestor", older, newer], cwd=REPOSITORY).returncode:
            raise AssertionError(f"C55 {label} ancestry mismatch")
    committed: dict[str, bytes] = {}
    artifact_rows = []
    for relative, digest in C55_ARTIFACTS.items():
        repository_relative = f"{C55_PROJECT}/{relative}"
        raw = git_bytes(C55_PROVENANCE, repository_relative)
        if sha256_bytes(raw) != digest:
            raise AssertionError(f"C55 committed source mismatch: {relative}")
        live = REPOSITORY / repository_relative
        if not live.is_file() or live.read_bytes() != raw:
            raise AssertionError(f"C55 live source mismatch: {relative}")
        committed[relative] = raw
        artifact_rows.append({
            "path": repository_relative,
            "sha256": digest,
            "git_blob_id": git_blob(C55_PROVENANCE, repository_relative),
            "live_equals_committed": True,
        })
    if committed["route_a_evaluation.yaml"] != committed["evaluations/route_a/HCS-C55/20260815T000000Z.yaml"]:
        raise AssertionError("C55 Route copies differ")
    route = committed["route_a_evaluation.yaml"].decode("utf-8")
    for line in (
        "documentation_status: DOCS_FINAL_NO_MORE_EDITS",
        "code_results_status: RELEASE_CANDIDATE",
        "release_status: RELEASE_FROZEN",
        f"code_commit: {C55_IMPLEMENTATION}",
        "full_project_manifest_status: VERIFIED_47_ENTRIES_CURRENT",
    ):
        if line not in route:
            raise AssertionError("C55 layered status mismatch")
    for relative in ("README.md", "INTEGRITY_REPORT.md", "IMPLEMENTATION_CHECKLIST.md"):
        text = committed[relative].decode("utf-8")
        if "RELEASE_FROZEN" not in text or C55_IMPLEMENTATION not in text:
            raise AssertionError(f"C55 frozen root artifact mismatch: {relative}")

    full_entries = []
    manifest_lines = committed["results/ARTIFACT_HASHES.sha256"].decode("utf-8").splitlines()
    if len(manifest_lines) != 47:
        raise AssertionError("C55 full manifest count")
    seen: set[str] = set()
    for line in manifest_lines:
        match = re.fullmatch(r"([0-9a-f]{64})  ([^\n]+)", line)
        if match is None or match.group(2) in seen:
            raise AssertionError("C55 full manifest syntax/duplicate")
        digest, relative = match.groups()
        pure = PurePosixPath(relative)
        if (
            pure.is_absolute() or str(pure) != relative or "\\" in relative
            or any(part in ("", ".", "..") for part in pure.parts)
            or pure.name == "ARTIFACT_HASHES.sha256"
        ):
            raise AssertionError("C55 full manifest unsafe/noncanonical path")
        seen.add(relative)
        repository_relative = f"{C55_PROJECT}/{relative}"
        raw = git_bytes(C55_PROVENANCE, repository_relative)
        if sha256_bytes(raw) != digest or (REPOSITORY / repository_relative).read_bytes() != raw:
            raise AssertionError(f"C55 full manifest rebound: {relative}")
        full_entries.append({"path": relative, "sha256": digest})
    if [row["path"] for row in full_entries] != sorted(row["path"] for row in full_entries):
        raise AssertionError("C55 full manifest order")
    tracked_output = run(["git", "ls-tree", "-r", "--name-only", C55_PROVENANCE, "--", C55_PROJECT]).stdout.splitlines()
    tracked_relative = {
        str(PurePosixPath(path).relative_to(C55_PROJECT))
        for path in tracked_output
        if PurePosixPath(path).name not in FULL_MANIFEST_EXCLUDED_NAMES
        and not any(part in {"__pycache__", ".pytest_cache", ".ipynb_checkpoints"} for part in PurePosixPath(path).parts)
    }
    if seen != tracked_relative:
        raise AssertionError("C55 full manifest exact committed inventory")

    checker = REPOSITORY / C55_PROJECT / "code/c55_checker.py"
    certificate_path = REPOSITORY / C55_PROJECT / "results/c55_certificate.json"
    with tempfile.TemporaryDirectory(prefix="c56-independent-c55-") as directory:
        output = Path(directory) / "check.json"
        completed = run([sys.executable, str(checker), str(certificate_path), "--output", str(output)])
        if "C55 CHECK PASS" not in completed.stdout or sha256_bytes(output.read_bytes()) != C55_ARTIFACTS["results/independent_check.json"]:
            raise AssertionError("committed C55 checker replay mismatch")

    c55 = strict_load(committed["results/c55_certificate.json"])
    if set(c55) != {"schema", "payload_sha256", "payload"} or c55["schema"] != "hcs-c55-certificate-v1":
        raise AssertionError("C55 envelope")
    if c55["payload_sha256"] != C55_PAYLOAD_SHA256 or sha256_bytes(canonical_json(c55["payload"])) != C55_PAYLOAD_SHA256:
        raise AssertionError("C55 payload")
    if c55["payload"]["artifact_status"] != "RELEASE_CANDIDATE":
        raise AssertionError("C55 immutable machine payload status")
    rows = c55["payload"]["rational_cubic_surface"]["primitive_integral_coefficients"]
    if sha256_bytes(canonical_json(rows)) != C55_COEFFICIENT_SHA256:
        raise AssertionError("C55 coefficient hash")
    if [row["exponents_u0_to_u3"] for row in rows] != degree_three_exponents():
        raise AssertionError("C55 coefficient order")
    if math.gcd(*(abs(row["coefficient"]) for row in rows)) != 1 or rows[0]["coefficient"] <= 0:
        raise AssertionError("C55 primitive normalization")
    source_lock = {
        "implementation_commit": C55_IMPLEMENTATION,
        "provenance_commit": C55_PROVENANCE,
        "implementation_is_ancestor_of_provenance": True,
        "provenance_is_ancestor_of_current_released_HEAD": True,
        "layered_status_contract": {
            "project_release_status": "RELEASE_FROZEN",
            "documentation_status": "DOCS_FINAL_NO_MORE_EDITS",
            "machine_code_results_status": "RELEASE_CANDIDATE",
            "certificate_artifact_status": "RELEASE_CANDIDATE",
            "machine_release_candidate_is_immutable_payload_contract_not_unreleased_project": True,
        },
        "committed_artifacts": artifact_rows,
        "full_manifest_entry_count": 47,
        "full_manifest_entries": full_entries,
        "full_manifest_all_committed_and_live_entries_rebound": True,
        "full_manifest_path_safety_and_exact_inventory_verified": True,
        "certificate_sha256": C55_ARTIFACTS["results/c55_certificate.json"],
        "payload_sha256": C55_PAYLOAD_SHA256,
        "schema_descriptor_sha256": C55_SCHEMA_SHA256,
        "independent_check_sha256": C55_ARTIFACTS["results/independent_check.json"],
        "scoped_manifest_sha256": C55_ARTIFACTS["results/CODE_RESULTS_HASHES.sha256"],
        "full_manifest_sha256": C55_ARTIFACTS["results/ARTIFACT_HASHES.sha256"],
        "route_sha256": C55_ARTIFACTS["route_a_evaluation.yaml"],
        "primitive_coefficients_sha256": C55_COEFFICIENT_SHA256,
        "primitive_coefficients": rows,
        "committed_checker_replay_passed_before_coefficient_import": True,
    }
    return rows, source_lock


def cubic_and_lines(rows: list[dict[str, Any]]) -> tuple[tuple[sp.Symbol, ...], sp.Expr, tuple[sp.Symbol, ...], list[sp.Expr]]:
    u = sp.symbols("u0:4")
    a, b, c, d, s, t = sp.symbols("a b c d s t")
    form = sum(
        row["coefficient"] * sp.prod(variable ** exponent for variable, exponent in zip(u, row["exponents_u0_to_u3"]))
        for row in rows
    )
    restricted = sp.Poly(sp.expand(form.subs({u[0]: s, u[1]: t, u[2]: a * s + c * t, u[3]: b * s + d * t})), s, t)
    equations = [restricted.coeff_monomial(s ** (3 - index) * t ** index) for index in range(4)]
    return u, form, (a, b, c, d, s, t), equations


def serialize_line_equations(equations: list[sp.Expr], variables: tuple[sp.Symbol, ...]) -> list[list[dict[str, Any]]]:
    output = []
    for equation in equations:
        poly = sp.Poly(equation, *variables, domain=sp.ZZ)
        output.append([
            {"exponents_abcd": list(exponents), "coefficient": int(coefficient)}
            for exponents, coefficient in poly.terms()
        ])
    return output


def standard_monomials(leading: list[tuple[int, ...]]) -> tuple[list[list[int]], list[int]]:
    """Enumerate the complete finite monomial box determined by pure powers."""

    bounds: list[int] = []
    for variable in range(4):
        pure_powers = [
            lead[variable]
            for lead in leading
            if lead[variable] > 0 and all(lead[index] == 0 for index in range(4) if index != variable)
        ]
        if len(pure_powers) != 1:
            raise AssertionError("independent leading ideal lacks unique pure-power bound")
        bounds.append(pure_powers[0])
    if bounds != [3, 3, 3, 4]:
        raise AssertionError("independent leading-ideal box bounds")
    values = [
        list(exponents)
        for exponents in product(*(range(bound) for bound in bounds))
        if not any(all(exponents[index] >= lead[index] for index in range(4)) for lead in leading)
    ]
    values.sort()
    degree_counts = [sum(sum(value) == degree for value in values) for degree in range(5)]
    if len(values) != 27 or degree_counts != [1, 4, 10, 12, 0] or any(sum(value) >= 4 for value in values):
        raise AssertionError("independent complete standard-monomial box/count")
    return values, degree_counts


def univariate_text(coefficients: list[int], variable: str = "d") -> str:
    terms = []
    for exponent in range(len(coefficients) - 1, -1, -1):
        coefficient = coefficients[exponent]
        if coefficient == 0:
            continue
        sign = "-" if coefficient < 0 else ("+" if terms else "")
        absolute = abs(coefficient)
        suffix = "" if exponent == 0 else (variable if exponent == 1 else f"{variable}{exponent}")
        terms.append(sign + str(absolute) + suffix)
    return "".join(terms) or "0"


def imul(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, lv in enumerate(left):
        for j, rv in enumerate(right):
            result[i + j] += lv * rv
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def ipow(poly: list[int], exponent: int) -> list[int]:
    result = [1]
    for _ in range(exponent):
        result = imul(result, poly)
    return result


def fraction_remainder_zero(dividend: list[int], divisor: list[int]) -> bool:
    """Check divisibility in Q[d] by custom exact long division.

    Substitution expansion is first performed over Z with one common
    denominator.  This small Fraction loop is intentionally independent of
    SymPy's polynomial-remainder implementation; the producer uses Singular.
    """

    if not divisor or divisor[-1] == 0:
        raise AssertionError("zero/noncanonical polynomial divisor")
    remainder = [Fraction(value) for value in dividend]
    divisor_q = [Fraction(value) for value in divisor]
    while remainder and remainder[-1] == 0:
        remainder.pop()
    while len(remainder) >= len(divisor_q):
        shift = len(remainder) - len(divisor_q)
        quotient_term = remainder[-1] / divisor_q[-1]
        for index, coefficient in enumerate(divisor_q):
            remainder[index + shift] -= quotient_term * coefficient
        while remainder and remainder[-1] == 0:
            remainder.pop()
    return not remainder


def bind_lex_shapes(shapes: Any) -> list[dict[str, Any]]:
    """Type-check and bind all four shape arrays to fixed canonical hashes."""

    if type(shapes) is not list or len(shapes) != 4:
        raise AssertionError("lex shape container")
    if [shape.get("leading_variable") if type(shape) is dict else None for shape in shapes] != ["d", "c", "b", "a"]:
        raise AssertionError("lex shape labels")
    rebound_shapes: list[dict[str, Any]] = []
    for shape, expected_variable in zip(shapes, ("d", "c", "b", "a")):
        if set(shape) != {"leading_variable", "leading_coefficient", "tail_coefficients_d_0_up", "primitive_content", "canonical_text_sha256"}:
            raise AssertionError("lex shape unknown/missing field")
        variable = shape["leading_variable"]
        tail = shape["tail_coefficients_d_0_up"]
        expected_length = 28 if variable == "d" else 27
        if (
            type(variable) is not str or variable != expected_variable
            or type(shape["leading_coefficient"]) is not int
            or type(shape["primitive_content"]) is not int
            or type(shape["canonical_text_sha256"]) is not str
            or type(tail) is not list or len(tail) != expected_length
            or any(type(value) is not int for value in tail)
        ):
            raise AssertionError("lex shape coefficient schema")
        values = [shape["leading_coefficient"]] + tail
        if math.gcd(*(abs(value) for value in values)) != 1 or shape["primitive_content"] != 1:
            raise AssertionError("lex shape content")
        if shape["leading_coefficient"] <= 0:
            raise AssertionError("lex shape sign")
        if variable == "d":
            if shape["leading_coefficient"] != tail[27]:
                raise AssertionError("d leading coefficient is not d^27 coefficient")
            text = univariate_text(tail)
        else:
            lambda_coefficient = shape["leading_coefficient"]
            d_text = univariate_text(tail)
            if d_text == "0":
                text = f"{lambda_coefficient}{variable}"
            else:
                prefix = f"{lambda_coefficient}{variable}"
                text = prefix + (d_text if d_text.startswith("-") else "+" + d_text)
        digest = sha256_bytes((text + "\n").encode("utf-8"))
        if digest != LEX_SHAPE_HASHES[variable] or shape["canonical_text_sha256"] != digest:
            raise AssertionError("lex shape canonical hash")
        rebound_shapes.append({
            "leading_variable": expected_variable,
            "leading_coefficient": shape["leading_coefficient"],
            "tail_coefficients_d_0_up": list(tail),
            "primitive_content": 1,
            "canonical_text_sha256": LEX_SHAPE_HASHES[expected_variable],
        })
    return rebound_shapes


def validate_lex_witness(
    main: dict[str, Any], line_equations: list[list[dict[str, Any]]]
) -> list[dict[str, Any]]:
    expected_main_keys = {
        "chart", "coordinates", "line_equations_sparse", "dp_basis_size",
        "dp_quotient_dimension", "dp_basis_rows", "standard_monomials_abcd",
        "standard_monomial_degree_counts_0_to_4",
        "lex_basis_size", "lex_quotient_dimension", "lex_shape",
        "singular_original_equation_reductions_zero", "all_four_back_substitution_remainders_zero",
    }
    if set(main) != expected_main_keys or main["chart"] != "U01" or main["coordinates"] != ["s", "t", "a*s+c*t", "b*s+d*t"]:
        raise AssertionError("main chart schema/coordinates")
    rebound_shapes = bind_lex_shapes(main["lex_shape"])
    g_coefficients = rebound_shapes[0]["tail_coefficients_d_0_up"]
    numerators = {
        2: [-value for value in rebound_shapes[1]["tail_coefficients_d_0_up"]],
        1: [-value for value in rebound_shapes[2]["tail_coefficients_d_0_up"]],
        0: [-value for value in rebound_shapes[3]["tail_coefficients_d_0_up"]],
        3: [0, 1],
    }
    denominators = {
        2: rebound_shapes[1]["leading_coefficient"],
        1: rebound_shapes[2]["leading_coefficient"],
        0: rebound_shapes[3]["leading_coefficient"],
        3: 1,
    }
    common_denominator = denominators[0] ** 3 * denominators[1] ** 3 * denominators[2] ** 3
    for equation in line_equations:
        result = [0]
        for term in equation:
            contribution = [1]
            denominator = 1
            for position, exponent in enumerate(term["exponents_abcd"]):
                contribution = imul(contribution, ipow(numerators[position], exponent))
                denominator *= denominators[position] ** exponent
            scale = term["coefficient"] * (common_denominator // denominator)
            if len(result) < len(contribution):
                result.extend([0] * (len(contribution) - len(result)))
            for index, value in enumerate(contribution):
                result[index] += scale * value
        if not fraction_remainder_zero(result, g_coefficients):
            raise AssertionError("lex back-substitution remainder nonzero")
    return rebound_shapes


def sympy_geometry(rows: list[dict[str, Any]], form: sp.Expr, u: tuple[sp.Symbol, ...], symbols: tuple[sp.Symbol, ...]) -> tuple[dict[str, Any], dict[str, Any]]:
    a, b, c, d, s, t = symbols
    charts = {
        "U02": ((s, a * s + c * t, t, b * s + d * t), c, ["s", "a*s+c*t", "t", "b*s+d*t"], "c"),
        "U03": ((s, a * s + c * t, b * s + d * t, t), c, ["s", "a*s+c*t", "b*s+d*t", "t"], "c"),
        "U12": ((a * s + c * t, s, t, b * s + d * t), c, ["a*s+c*t", "s", "t", "b*s+d*t"], "c"),
        "U13": ((a * s + c * t, s, b * s + d * t, t), c, ["a*s+c*t", "s", "b*s+d*t", "t"], "c"),
        "U23": ((a * s + c * t, b * s + d * t, s, t), a * d - b * c, ["a*s+c*t", "b*s+d*t", "s", "t"], "a*d-b*c"),
    }
    complement_rows = []
    for name, (coordinates, p01, coordinate_text, p01_text) in charts.items():
        restricted = sp.Poly(sp.expand(form.subs(dict(zip(u, coordinates)))), s, t)
        equations = [restricted.coeff_monomial(s ** (3 - index) * t ** index) for index in range(4)]
        basis = sp.groebner(equations + [p01], a, b, c, d, order="grevlex")
        if len(basis.polys) != 1 or basis.polys[0].as_expr() != 1:
            raise AssertionError(f"independent complement nonunit {name}")
        complement_rows.append({"chart": name, "coordinates": coordinate_text, "p01_zero_equation": p01_text, "singular_unit_ideal": True, "groebner_basis_size": 1})
    complement = {"charts": complement_rows, "all_five_unit_ideals": True}
    smoothness = {}
    for label, modulus in (("Q", None), ("7", 7), ("19", 19), ("29", 29), ("37", 37)):
        units = []
        for chart_index in range(4):
            equations = [form] + [sp.diff(form, variable) for variable in u] + [u[chart_index] - 1]
            kwargs = {} if modulus is None else {"modulus": modulus}
            basis = sp.groebner(equations, *u, order="grevlex", **kwargs)
            units.append(len(basis.polys) == 1 and basis.polys[0].as_expr() == 1)
        if units != [True] * 4:
            raise AssertionError(f"independent surface singular at {label}")
        smoothness[label] = {"four_affine_projective_chart_unit_ideals": units, "surface_smooth": True}
    return complement, smoothness


def subset_sums(degrees: Iterable[int]) -> list[int]:
    values = {0}
    for degree in degrees:
        values |= {value + degree for value in tuple(values)}
    return sorted(values)


def mod_multiply(left: list[int], right: list[int], prime: int) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, left_value in enumerate(left):
        for j, right_value in enumerate(right):
            result[i + j] = (result[i + j] + left_value * right_value) % prime
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def mod_coefficients(poly: sp.Poly, prime: int) -> list[int]:
    coefficients = [0] * (poly.degree() + 1)
    for (exponent,), coefficient in poly.terms():
        coefficients[exponent] = int(coefficient) % prime
    inverse = pow(coefficients[-1], -1, prime)
    return [(value * inverse) % prime for value in coefficients]


def validate_modular(candidate: dict[str, Any], g_coefficients: list[int], smoothness: dict[str, Any]) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    d = sp.symbols("d")
    expected_records = {}
    chain = []
    current: set[int] | None = None
    for prime in sorted(WITNESS_PATTERNS):
        stored = candidate[str(prime)]
        if type(stored["factorization_unit_mod_p"]) is not int:
            raise AssertionError("stored modular unit type")
        stored_product = [stored["factorization_unit_mod_p"] % prime]
        for stored_factor in stored["factors"]:
            if type(stored_factor["multiplicity"]) is not int or stored_factor["multiplicity"] < 1:
                raise AssertionError("stored modular multiplicity type/value")
            coefficients = stored_factor["coefficients_mod_p_0_up"]
            if not coefficients or any(type(value) is not int or not (0 <= value < prime) for value in coefficients) or coefficients[-1] != 1:
                raise AssertionError("stored modular coefficient canonicality")
            for _ in range(stored_factor["multiplicity"]):
                stored_product = mod_multiply(stored_product, coefficients, prime)
        reduced_coefficients = [coefficient % prime for coefficient in g_coefficients]
        while len(reduced_coefficients) > 1 and reduced_coefficients[-1] == 0:
            reduced_coefficients.pop()
        if stored_product != reduced_coefficients:
            raise AssertionError(f"stored factor multiplication rebound failed at {prime}")
        reduced = sp.Poly(sum(coefficient * d ** index for index, coefficient in enumerate(g_coefficients)), d, modulus=prime)
        if reduced.degree() != 27 or int(reduced.LC()) % prime == 0 or sp.gcd(reduced, reduced.diff()).degree() != 0:
            raise AssertionError(f"independent bad eliminant prime {prime}")
        unit, factors_raw = sp.factor_list(reduced)
        factors = []
        degree_list = []
        for factor, multiplicity in factors_raw:
            coefficients = mod_coefficients(factor, prime)
            factors.append({"multiplicity": int(multiplicity), "coefficients_mod_p_0_up": coefficients})
            degree_list.extend([factor.degree()] * multiplicity)
        factors.sort(key=lambda row: (len(row["coefficients_mod_p_0_up"]), row["coefficients_mod_p_0_up"]))
        degree_list.sort()
        if tuple(degree_list) != WITNESS_PATTERNS[prime]:
            raise AssertionError(f"independent factor pattern {prime}")
        sums = subset_sums(degree_list)
        current = set(sums) if current is None else current & set(sums)
        expected_records[str(prime)] = {
            "prime": prime,
            "eliminant_degree_preserved": True,
            "leading_coefficient_mod_p": g_coefficients[-1] % prime,
            "derivative_gcd_degree": 0,
            "squarefree": True,
            "factorization_unit_mod_p": int(unit) % prime,
            "factors": factors,
            "factor_degrees": degree_list,
            "factor_multiplication_rebound": True,
            "subset_sums": sums,
            "surface_good_reduction": smoothness[str(prime)]["surface_smooth"] is True,
        }
        chain.append({"through_prime": prime, "intersection": sorted(current)})
    if sorted(current or ()) != [0, 27]:
        raise AssertionError("independent subset-sum intersection")
    deep_exact(candidate, expected_records, ("irreducibility", "modular_witnesses"))
    return expected_records, chain


def lattice_dot(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return left[0] * right[0] - sum(a * b for a, b in zip(left[1:], right[1:]))


def reflection_matrix(root: tuple[int, ...]) -> sp.Matrix:
    columns = []
    for column in range(7):
        basis = tuple(int(i == column) for i in range(7))
        pairing = lattice_dot(basis, root)
        columns.append(sp.Matrix([basis[i] + pairing * root[i] for i in range(7)]))
    return sp.Matrix.hstack(*columns)


def compose_right(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(right[left[index]] for index in range(27))


def cycles(permutation: tuple[int, ...]) -> tuple[int, ...]:
    unseen = set(range(27))
    lengths = []
    while unseen:
        current = min(unseen)
        length = 0
        while current in unseen:
            unseen.remove(current)
            length += 1
            current = permutation[current]
        lengths.append(length)
    return tuple(sorted(lengths))


def s27_sign(permutation: tuple[int, ...]) -> int:
    return -1 if sum(permutation[i] > permutation[j] for i in range(27) for j in range(i + 1, 27)) % 2 else 1


def independent_we6() -> dict[str, Any]:
    h = (1, 0, 0, 0, 0, 0, 0)
    exceptional = [tuple([0] + [int(i == j) for i in range(6)]) for j in range(6)]
    lines = list(exceptional)
    for i, j in combinations(range(6), 2):
        vector = list(h); vector[i + 1] = vector[j + 1] = -1; lines.append(tuple(vector))
    for omitted in range(6):
        vector = [2] + [-1] * 6; vector[omitted + 1] = 0; lines.append(tuple(vector))
    if len(lines) != 27 or len(set(lines)) != 27:
        raise AssertionError("independent line classes")
    roots = [tuple(exceptional[i][k] - exceptional[i + 1][k] for k in range(7)) for i in range(5)]
    roots.append((1, -1, -1, -1, 0, 0, 0))
    matrices = [reflection_matrix(root) for root in roots]
    root_squares = [lattice_dot(root, root) for root in roots]
    if root_squares != [-2] * 6:
        raise AssertionError("independent root squares")
    form_matrix = sp.diag(1, -1, -1, -1, -1, -1, -1)
    preserve_form = [matrix.T * form_matrix * matrix == form_matrix for matrix in matrices]
    reflection_determinants = [int(matrix.det()) for matrix in matrices]
    if preserve_form != [True] * 6 or reflection_determinants != [-1] * 6:
        raise AssertionError("independent reflection form/determinant")
    anticanonical = sp.Matrix([3, -1, -1, -1, -1, -1, -1])
    if any(matrix * anticanonical != anticanonical for matrix in matrices):
        raise AssertionError("independent anticanonical fixed gate")
    line_index = {line: index for index, line in enumerate(lines)}
    generators = []
    for matrix in matrices:
        generator = []
        for line in lines:
            image = tuple(int(value) for value in matrix * sp.Matrix(line))
            generator.append(line_index[image])
        generators.append(tuple(generator))
    identity = tuple(range(27))
    parity = {identity: 0}
    queue = deque([identity])
    while queue:
        current = queue.popleft()
        for generator in generators:
            successor = compose_right(current, generator)
            expected = parity[current] ^ 1
            if successor not in parity:
                parity[successor] = expected; queue.append(successor)
            elif parity[successor] != expected:
                raise AssertionError("independent Coxeter parity")
    target = (2, 5, 5, 5, 10)
    target_elements = [element for element in parity if cycles(element) == target]
    target_counts = Counter(parity[element] for element in target_elements)
    target_s27_signs = {s27_sign(element) for element in target_elements}
    if target_s27_signs != {1}:
        raise AssertionError("independent target S27 sign")
    fixed_matrix = sp.Matrix.vstack(*(matrix - sp.eye(7) for matrix in matrices))
    line_intersections = [[lattice_dot(left, right) for right in lines] for left in lines]
    preserve_incidence = [
        all(line_intersections[generator[i]][generator[j]] == line_intersections[i][j] for i in range(27) for j in range(27))
        for generator in generators
    ]
    if preserve_incidence != [True] * 6:
        raise AssertionError("independent line incidence")
    result = {
        "picard_basis": ["H", "E1", "E2", "E3", "E4", "E5", "E6"],
        "intersection_form_diagonal": [1, -1, -1, -1, -1, -1, -1],
        "canonical_class_negative": [3, -1, -1, -1, -1, -1, -1],
        "simple_roots": [list(root) for root in roots],
        "simple_root_self_intersections": root_squares,
        "line_classes": [list(line) for line in lines],
        "line_class_intersection_matrix": line_intersections,
        "line_class_intersection_matrix_sha256": sha256_bytes(canonical_json(line_intersections)),
        "simple_reflection_line_permutations": [list(generator) for generator in generators],
        "simple_reflections_preserve_picard_intersection": preserve_form,
        "simple_reflections_preserve_line_incidence": preserve_incidence,
        "group_order": len(parity),
        "line_orbit_size": len({element[0] for element in parity}),
        "index_two_kernel_definition": "kernel_of_E6_reflection_determinant_equivalently_Coxeter_word_parity_not_S27_sign",
        "index_two_kernel_order": sum(value == 0 for value in parity.values()),
        "all_W_E6_line_permutations_have_even_S27_sign": all(s27_sign(element) == 1 for element in parity),
        "S27_odd_element_count": sum(s27_sign(element) == -1 for element in parity),
        "target_cycle_type": list(target),
        "target_cycle_type_S27_sign": next(iter(target_s27_signs)),
        "target_cycle_count": target_counts[0] + target_counts[1],
        "target_in_index_two_kernel_count": target_counts[0],
        "target_outside_index_two_kernel_count": target_counts[1],
        "simple_reflection_determinants_on_E6": reflection_determinants,
        "anticanonical_fixed_by_all_simple_reflections": [True] * 6,
        "picard_fixed_rank": 7 - fixed_matrix.rank(),
    }
    required = (51840, 27, 25920, 0, 5184, 0, 1)
    actual = (result["group_order"], result["line_orbit_size"], result["index_two_kernel_order"], result["target_in_index_two_kernel_count"], result["target_outside_index_two_kernel_count"], result["S27_odd_element_count"], result["picard_fixed_rank"])
    if actual != required:
        raise AssertionError("independent W(E6) invariants")
    return result


def scalar_leaf_count(value: Any) -> int:
    if isinstance(value, dict):
        return sum(scalar_leaf_count(child) for child in value.values())
    if isinstance(value, list):
        return sum(scalar_leaf_count(child) for child in value)
    return 1


def shape_descriptor(value: Any) -> Any:
    if isinstance(value, dict):
        return {key: shape_descriptor(child) for key, child in sorted(value.items())}
    if isinstance(value, list):
        return [shape_descriptor(child) for child in value]
    if type(value) is bool: return "bool"
    if type(value) is int: return "int"
    if type(value) is str: return "str"
    if value is None: return "null"
    raise AssertionError("forbidden scalar type")


def expected_schema(payload: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_id": "hcs-c56-certificate-schema-v1",
        "payload_top_level_keys": sorted(payload),
        "payload_shape_sha256": sha256_bytes(canonical_json(shape_descriptor(payload))),
        "payload_scalar_leaf_count": scalar_leaf_count(payload),
        "unknown_fields_rejected": True,
        "duplicate_keys_rejected": True,
        "floats_rejected": True,
        "booleans_rejected_in_integer_slots": True,
        "noncanonical_integers_rejected": True,
        "non_UTF8_rejected": True,
        "oversized_input_rejected": True,
        "optimized_python_rejected": True,
        "max_certificate_bytes": MAX_CERTIFICATE_BYTES,
    }


def theorem_gates() -> dict[str, Any]:
    return {
        "surface_smooth_over_Q": True,
        "surface_good_at_all_four_witness_primes": True,
        "classical_total_27_lines_external_input": "Cayley-Salmon_smooth_cubic_surface_line_count",
        "line_section_rank_external_input": "Kass-Wickelgren_Theorem_2_rank_4_bundle_section",
        "simple_zero_external_input": "Kass-Wickelgren_Corollary_53",
        "separability_external_input": "Kass-Wickelgren_Corollary_54",
        "main_chart_closed_etale_subscheme_degree": 27,
        "all_27_lines_in_U01": True,
        "line_scheme_is_Spec_E_connected_etale_degree_27": True,
        "E_degree": 27,
        "E_is_Galois_claimed": False,
        "no_Q_rational_line": True,
        "finite_L_line_defines_injective_conjugate_E_embedding": True,
        "finite_L_line_field_degree_divisible_by_27": True,
        "eliminant_irreducible_over_Q": True,
        "p37_surface_good_reduction_gate": True,
        "p37_eliminant_leading_coefficient_nonzero_and_squarefree_unramified_gate": True,
        "p37_complete_factor_multiply_back_cycle_type_gate": True,
        "p37_target_class_outside_index_two_Coxeter_kernel_gate": True,
        "p37_cycle_type": [2, 5, 5, 5, 10],
        "transitive_plus_order5_subgroup_gate": True,
        "index_two_kernel_excluded_by_Coxeter_parity_not_S27_sign": True,
        "galois_closure_group": "W(E6)",
        "galois_closure_degree": 51840,
        "geometric_picard_rank": 7,
        "rational_picard_rank_uses_Hochschild_Serre_torsion_rank_bridge": True,
        "rational_picard_rank": 1,
        "no_rational_point_or_motive_consequence_claimed": True,
        "final_status": "PREFREEZE_CODE_RESULTS_PASS",
    }


def deep_exact(actual: Any, expected: Any, path: tuple[Any, ...] = ()) -> None:
    if type(actual) is not type(expected):
        raise AssertionError(f"type mismatch at {path}")
    if isinstance(expected, dict):
        if set(actual) != set(expected):
            raise AssertionError(f"object keys mismatch at {path}")
        for key in expected:
            deep_exact(actual[key], expected[key], path + (key,))
    elif isinstance(expected, list):
        if len(actual) != len(expected):
            raise AssertionError(f"list length mismatch at {path}")
        for index, (left, right) in enumerate(zip(actual, expected)):
            deep_exact(left, right, path + (index,))
    elif actual != expected:
        raise AssertionError(f"scalar mismatch at {path}")


def semantic_preflight(payload: dict[str, Any]) -> None:
    """Reject central rebound forgeries before expensive algebra contexts."""

    deep_exact(payload["material_passport"], {
        "candidate_id": "HCS-C56",
        "slug": "henon_mu3_yukawa_line_field",
        "artifact_status": "PREFREEZE_CODE_RESULTS_PASS",
        "arithmetic_mode": "exact_Q_and_finite_fields_no_floating_point",
        "tmp_reconnaissance_is_theorem_evidence": False,
    }, ("material_passport",))
    source = payload["c55_source_lock"]
    deep_exact(source["implementation_commit"], C55_IMPLEMENTATION, ("c55_source_lock", "implementation_commit"))
    deep_exact(source["provenance_commit"], C55_PROVENANCE, ("c55_source_lock", "provenance_commit"))
    deep_exact(source["full_manifest_entry_count"], 47, ("c55_source_lock", "full_manifest_entry_count"))
    deep_exact(source["layered_status_contract"], {
        "project_release_status": "RELEASE_FROZEN",
        "documentation_status": "DOCS_FINAL_NO_MORE_EDITS",
        "machine_code_results_status": "RELEASE_CANDIDATE",
        "certificate_artifact_status": "RELEASE_CANDIDATE",
        "machine_release_candidate_is_immutable_payload_contract_not_unreleased_project": True,
    }, ("c55_source_lock", "layered_status_contract"))

    surface = payload["surface"]
    rows = surface["primitive_coefficients"]
    if sha256_bytes(canonical_json(rows)) != C55_COEFFICIENT_SHA256:
        raise AssertionError("central coefficient mutation")
    for key, expected in (
        ("primitive_coefficients_sha256", C55_COEFFICIENT_SHA256),
        ("coefficient_count", 20),
        ("coefficient_gcd", 1),
        ("first_coefficient_positive", True),
    ):
        deep_exact(surface[key], expected, ("surface", key))

    main = payload["grassmann_main_chart"]
    deep_exact(main["chart"], "U01", ("grassmann_main_chart", "chart"))
    deep_exact(main["coordinates"], ["s", "t", "a*s+c*t", "b*s+d*t"], ("grassmann_main_chart", "coordinates"))
    for key, expected in (
        ("dp_basis_size", 21),
        ("dp_quotient_dimension", 27),
        ("standard_monomial_degree_counts_0_to_4", [1, 4, 10, 12, 0]),
        ("lex_basis_size", 4),
        ("lex_quotient_dimension", 27),
        ("all_four_back_substitution_remainders_zero", True),
    ):
        deep_exact(main[key], expected, ("grassmann_main_chart", key))
    bind_lex_shapes(main["lex_shape"])

    expected_complement = {
        "charts": [
            {"chart": "U02", "coordinates": ["s", "a*s+c*t", "t", "b*s+d*t"], "p01_zero_equation": "c", "singular_unit_ideal": True, "groebner_basis_size": 1},
            {"chart": "U03", "coordinates": ["s", "a*s+c*t", "b*s+d*t", "t"], "p01_zero_equation": "c", "singular_unit_ideal": True, "groebner_basis_size": 1},
            {"chart": "U12", "coordinates": ["a*s+c*t", "s", "t", "b*s+d*t"], "p01_zero_equation": "c", "singular_unit_ideal": True, "groebner_basis_size": 1},
            {"chart": "U13", "coordinates": ["a*s+c*t", "s", "b*s+d*t", "t"], "p01_zero_equation": "c", "singular_unit_ideal": True, "groebner_basis_size": 1},
            {"chart": "U23", "coordinates": ["a*s+c*t", "b*s+d*t", "s", "t"], "p01_zero_equation": "a*d-b*c", "singular_unit_ideal": True, "groebner_basis_size": 1},
        ],
        "all_five_unit_ideals": True,
    }
    deep_exact(payload["grassmann_complement"], expected_complement, ("grassmann_complement",))

    irreducible = payload["irreducibility"]
    for key, expected in (
        ("eliminant_degree", 27),
        ("eliminant_primitive_content", 1),
        ("eliminant_canonical_singular_text_sha256", LEX_SHAPE_HASHES["d"]),
        ("final_subset_sum_intersection", [0, 27]),
        ("gauss_lemma_irreducibility_gate", True),
    ):
        deep_exact(irreducible[key], expected, ("irreducibility", key))
    witnesses = irreducible["modular_witnesses"]
    if type(witnesses) is not dict or set(witnesses) != {str(prime) for prime in WITNESS_PATTERNS}:
        raise AssertionError("modular witness prime keys")
    for prime, degrees in WITNESS_PATTERNS.items():
        witness = witnesses[str(prime)]
        deep_exact(witness["prime"], prime, ("irreducibility", "modular_witnesses", str(prime), "prime"))
        deep_exact(witness["factor_degrees"], list(degrees), ("irreducibility", "modular_witnesses", str(prime), "factor_degrees"))

    we6 = payload["we6"]
    for key, expected in (
        ("group_order", 51840),
        ("line_orbit_size", 27),
        ("index_two_kernel_definition", "kernel_of_E6_reflection_determinant_equivalently_Coxeter_word_parity_not_S27_sign"),
        ("index_two_kernel_order", 25920),
        ("all_W_E6_line_permutations_have_even_S27_sign", True),
        ("S27_odd_element_count", 0),
        ("target_cycle_type", [2, 5, 5, 5, 10]),
        ("target_cycle_type_S27_sign", 1),
        ("target_cycle_count", 5184),
        ("target_in_index_two_kernel_count", 0),
        ("target_outside_index_two_kernel_count", 5184),
        ("simple_reflection_determinants_on_E6", [-1] * 6),
        ("picard_fixed_rank", 1),
    ):
        deep_exact(we6[key], expected, ("we6", key))
    deep_exact(payload["theorem_gates"], theorem_gates(), ("theorem_gates",))


def build_expected(candidate_payload: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    gates: list[str] = []
    rows, source_lock = independent_c55_source_lock(); gates.append("G01_C55_COMMITTED_SOURCE_LOCK")
    u, form, symbols, equations = cubic_and_lines(rows)
    line_serialized = serialize_line_equations(equations, symbols[:4])
    gates.append("G02_SURFACE_AND_LINE_EQUATIONS")

    candidate_main = candidate_payload["grassmann_main_chart"]
    deep_exact(candidate_main["line_equations_sparse"], line_serialized, ("grassmann_main_chart", "line_equations_sparse"))
    a, b, c, d, _, _ = symbols
    groebner = sp.groebner(equations, a, b, c, d, order="grevlex")
    if len(groebner.polys) != 21 or not groebner.is_zero_dimensional:
        raise AssertionError("independent dp basis")
    dp_rows = sorted([
        {"leading_monomial_abcd": list(poly.LM(order=groebner.order).exponents), "degree": int(poly.total_degree()), "term_count": len(poly.terms())}
        for poly in groebner.polys
    ], key=lambda row: row["leading_monomial_abcd"])
    leading = [tuple(row["leading_monomial_abcd"]) for row in dp_rows]
    standards, standard_degree_counts = standard_monomials(leading)
    lex_shape = validate_lex_witness(candidate_main, line_serialized)
    expected_main = {
        "chart": "U01",
        "coordinates": ["s", "t", "a*s+c*t", "b*s+d*t"],
        "line_equations_sparse": line_serialized,
        "dp_basis_size": 21,
        "dp_quotient_dimension": 27,
        "dp_basis_rows": dp_rows,
        "standard_monomials_abcd": standards,
        "standard_monomial_degree_counts_0_to_4": standard_degree_counts,
        "lex_basis_size": 4,
        "lex_quotient_dimension": 27,
        "lex_shape": lex_shape,
        "singular_original_equation_reductions_zero": [True] * 4,
        "all_four_back_substitution_remainders_zero": True,
    }
    deep_exact(candidate_main, expected_main, ("grassmann_main_chart",))
    gates.append("G03_DEGREE27_LEX_BACKSUBSTITUTION")

    complement, smoothness = sympy_geometry(rows, form, u, symbols)
    deep_exact(candidate_payload["grassmann_complement"], complement, ("grassmann_complement",))
    gates.append("G04_FIVE_COMPLEMENT_CHARTS")
    surface = {
        "variables": ["u0", "u1", "u2", "u3"],
        "primitive_coefficients": rows,
        "primitive_coefficients_sha256": C55_COEFFICIENT_SHA256,
        "coefficient_count": 20,
        "coefficient_gcd": 1,
        "first_coefficient_positive": True,
        "projective_GL4_Q_and_common_nonzero_Q_scalar_invariance": True,
        "smoothness": smoothness,
    }
    deep_exact(candidate_payload["surface"], surface, ("surface",))
    gates.append("G05_Q_AND_FOUR_PRIME_SMOOTHNESS")

    irreducible = candidate_payload["irreducibility"]
    g_coefficients = candidate_main["lex_shape"][0]["tail_coefficients_d_0_up"]
    if type(irreducible["eliminant_coefficients_d_0_to_27"]) is not list or len(g_coefficients) != 28:
        raise AssertionError("eliminant duplicate array mismatch")
    deep_exact(irreducible["eliminant_coefficients_d_0_to_27"], g_coefficients, ("irreducibility", "eliminant_coefficients"))
    if sha256_bytes((univariate_text(g_coefficients) + "\n").encode("utf-8")) != LEX_SHAPE_HASHES["d"]:
        raise AssertionError("eliminant text hash")
    modular, chain = validate_modular(irreducible["modular_witnesses"], g_coefficients, smoothness)
    expected_irreducible = {
        "eliminant_coefficients_d_0_to_27": g_coefficients,
        "eliminant_degree": 27,
        "eliminant_primitive_content": 1,
        "eliminant_canonical_singular_text_sha256": LEX_SHAPE_HASHES["d"],
        "modular_witnesses": modular,
        "subset_sum_intersection_chain": chain,
        "final_subset_sum_intersection": [0, 27],
        "gauss_lemma_irreducibility_gate": True,
    }
    deep_exact(irreducible, expected_irreducible, ("irreducibility",))
    gates.extend(["G06_FOUR_PRIME_FACTORS_AND_IRREDUCIBILITY", "G07_P37_FULL_GOOD_FROBENIUS"])

    we6 = independent_we6()
    deep_exact(candidate_payload["we6"], we6, ("we6",))
    gates.extend(["G08_FULL_WE6_NOT_INDEX_TWO_KERNEL", "G09_PICARD_FIXED_RANK_ONE"])
    expected = dict(sorted({
        "material_passport": {
            "candidate_id": "HCS-C56",
            "slug": "henon_mu3_yukawa_line_field",
            "artifact_status": "PREFREEZE_CODE_RESULTS_PASS",
            "arithmetic_mode": "exact_Q_and_finite_fields_no_floating_point",
            "tmp_reconnaissance_is_theorem_evidence": False,
        },
        "c55_source_lock": source_lock,
        "surface": surface,
        "grassmann_main_chart": expected_main,
        "grassmann_complement": complement,
        "irreducibility": expected_irreducible,
        "we6": we6,
        "theorem_gates": theorem_gates(),
    }.items()))
    deep_exact(candidate_payload["theorem_gates"], expected["theorem_gates"], ("theorem_gates",))
    gates.append("G10_SCOPE_AND_FINITE_L_FIREWALLS")
    return expected, gates


def envelope_exact(certificate: dict[str, Any], expected_payload: dict[str, Any], expected_schema_object: dict[str, Any]) -> None:
    if list(certificate) != ["payload", "payload_sha256", "schema", "schema_sha256"]:
        # Files are dumped with sort_keys=True, and strict key order is part of
        # the byte-level schema.
        raise AssertionError("certificate envelope keys/order")
    if certificate["payload_sha256"] != sha256_bytes(canonical_json(certificate["payload"])):
        raise AssertionError("payload envelope hash")
    if certificate["schema_sha256"] != sha256_bytes(canonical_json(certificate["schema"])):
        raise AssertionError("schema envelope hash")
    deep_exact(certificate["payload"], expected_payload, ("payload",))
    deep_exact(certificate["schema"], expected_schema_object, ("schema",))


def scalar_paths(value: Any, prefix: tuple[Any, ...] = ()) -> list[tuple[Any, ...]]:
    if isinstance(value, dict):
        return [path for key, child in value.items() for path in scalar_paths(child, prefix + (key,))]
    if isinstance(value, list):
        return [path for index, child in enumerate(value) for path in scalar_paths(child, prefix + (index,))]
    return [prefix]


def get_path(value: Any, path: tuple[Any, ...]) -> Any:
    for item in path:
        value = value[item]
    return value


def set_path(value: Any, path: tuple[Any, ...], replacement: Any) -> None:
    parent = value
    for item in path[:-1]:
        parent = parent[item]
    parent[path[-1]] = replacement


def mutate_scalar(value: Any) -> Any:
    if type(value) is bool: return not value
    if type(value) is int: return value + 1 if value != -1 else 1
    if type(value) is str: return value + "__MUTATED"
    if value is None: return "__MUTATED_NULL"
    raise AssertionError("unhandled scalar mutation")


def all_leaf_rebound(certificate: dict[str, Any], expected_payload: dict[str, Any], schema: dict[str, Any]) -> dict[str, int]:
    payload_paths = scalar_paths(certificate["payload"])
    schema_paths = scalar_paths(certificate["schema"])
    passed = 0
    for subtree, path in [("payload", path) for path in payload_paths] + [("schema", path) for path in schema_paths]:
        mutant = copy.deepcopy(certificate)
        target = mutant[subtree]
        set_path(target, path, mutate_scalar(get_path(target, path)))
        mutant["payload_sha256"] = sha256_bytes(canonical_json(mutant["payload"]))
        mutant["schema_sha256"] = sha256_bytes(canonical_json(mutant["schema"]))
        try:
            envelope_exact(mutant, expected_payload, schema)
        except AssertionError:
            passed += 1
        else:
            raise AssertionError(f"rebound scalar mutation survived: {subtree}/{path}")
    digest_passed = 0
    for digest_key in ("payload_sha256", "schema_sha256"):
        mutant = copy.deepcopy(certificate)
        mutant[digest_key] = "0" * 64 if mutant[digest_key] != "0" * 64 else "1" * 64
        try:
            envelope_exact(mutant, expected_payload, schema)
        except AssertionError:
            digest_passed += 1
        else:
            raise AssertionError(f"envelope digest mutation survived: {digest_key}")
    if digest_passed != 2:
        raise AssertionError("envelope digest rebound count")
    return {
        "payload_scalar_leaves": len(payload_paths),
        "schema_scalar_leaves": len(schema_paths),
        "envelope_digest_leaves": 2,
        "rebound_mutations_rejected": passed + digest_passed,
    }


def verify(raw: bytes, schema_raw: bytes | None) -> dict[str, Any]:
    certificate = strict_load(raw)
    if type(certificate) is not dict:
        raise AssertionError("certificate root")
    if list(certificate) != ["payload", "payload_sha256", "schema", "schema_sha256"]:
        raise AssertionError("certificate envelope")
    # Fast semantic preflight closes central fail-open paths before expensive
    # Gröbner/group contexts are built.
    payload = certificate["payload"]
    if list(payload) != ["c55_source_lock", "grassmann_complement", "grassmann_main_chart", "irreducibility", "material_passport", "surface", "theorem_gates", "we6"]:
        raise AssertionError("payload top-level schema/order")
    semantic_preflight(payload)

    expected_payload, gates = build_expected(payload)
    schema = expected_schema(expected_payload)
    if schema_raw is not None:
        schema_file = strict_load(schema_raw, maximum=100_000)
        deep_exact(schema_file, schema, ("schema_file",))
    envelope_exact(certificate, expected_payload, schema)
    mutation = all_leaf_rebound(certificate, expected_payload, schema)
    return {
        "schema": "hcs-c56-independent-check-v1",
        "result": "PASS_PREFREEZE_CODE_RESULTS",
        "certificate_sha256": sha256_bytes(raw),
        "payload_sha256": certificate["payload_sha256"],
        "schema_sha256": certificate["schema_sha256"],
        "semantic_gate_count": len(gates),
        "executed_gates": gates,
        "scalar_leaf_rebound": mutation,
        "line_scheme_degree": 27,
        "four_prime_irreducibility": True,
        "W_E6_order": 51840,
        "index_two_kernel_order": 25920,
        "target_cycle_count_outside_kernel": 5184,
        "picard_fixed_rank": 1,
        "written_Hochschild_Serre_rank_bridge_required": True,
        "derived_rational_picard_rank": 1,
        "finite_L_degree_divisibility_gate": True,
        "tmp_hash_used_as_theorem_evidence": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--schema", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    arguments = parser.parse_args()
    remove_stale_regular_output(arguments.output)
    if sys.flags.optimize or os.environ.get("PYTHONOPTIMIZE") not in (None, "", "0"):
        raise SystemExit("optimized Python is forbidden")
    try:
        raw = arguments.certificate.read_bytes()
        schema_raw = arguments.schema.read_bytes() if arguments.schema else None
        report = verify(raw, schema_raw)
        write_new_regular(arguments.output, json.dumps(report, sort_keys=True, indent=2).encode("utf-8") + b"\n")
    except BaseException:
        arguments.output.unlink(missing_ok=True)
        raise
    print("C56 CHECK PASS PREFREEZE")
    print(f"semantic_gates={report['semantic_gate_count']}")
    print(f"rebound_mutations={report['scalar_leaf_rebound']['rebound_mutations_rejected']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
