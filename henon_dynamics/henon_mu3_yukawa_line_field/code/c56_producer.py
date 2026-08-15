#!/usr/bin/env python3
"""Exact producer for the HCS-C56 Yukawa-surface line-field certificate.

The only mathematical input imported from HCS-C55 is the primitive ordered
twenty-term cubic.  Before that array is read, this program binds the final
C55 implementation/provenance commits with ``git show``, checks live bytes
against the committed blobs, and runs the committed C55 checker.  All C56
line-scheme, finite-field, and Weyl-group data are then recomputed exactly.
"""

from __future__ import annotations

import argparse
from collections import Counter, deque
from fractions import Fraction
import hashlib
from itertools import combinations
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import stat
import tempfile
from typing import Any, Iterable


PROJECT = Path(__file__).resolve().parents[1]
REPOSITORY = Path(__file__).resolve().parents[3]
C55_PROJECT = "henon_dynamics/henon_mu3_rational_yukawa_surface"
C55_IMPLEMENTATION = "e5661e80da6f7de53f574f97f768744095ba8ae0"
C55_PROVENANCE = "0b0a48db257a4b8bd4af905ab9c9cafba4a4d8be"
C55_PAYLOAD_SHA256 = "6afc529d2ab9e849592d9eba7b76324cc7a840670f50c669f90fdd079c0b4323"
C55_SCHEMA_SHA256 = "2961eb6b5b4aefa0e12ffcb59c9e1095b14f0309e2045fd6d8a7f636dc6dca53"
C55_COEFFICIENT_SHA256 = "1c7065d5644c44bba80658dee5d0704c371e9f446c8c3c6ac29f9590d0831b9e"
ELIMINANT_TEXT_SHA256 = "290b1182209491576070b8fa06b5b73b179738a790b9ca258242a3e9152ca48a"
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
                raise OSError("short write to result artifact")
            view = view[written:]
        os.fsync(descriptor)
    finally:
        os.close(descriptor)


def run(command: list[str], *, cwd: Path = REPOSITORY, input_text: str | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=cwd,
        input=input_text,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )


def git_bytes(commit: str, repository_relative: str) -> bytes:
    result = subprocess.run(
        ["git", "show", f"{commit}:{repository_relative}"],
        cwd=REPOSITORY,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
    )
    return result.stdout


def git_blob(commit: str, repository_relative: str) -> str:
    return run(["git", "rev-parse", f"{commit}:{repository_relative}"]).stdout.strip()


def strict_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise AssertionError(f"duplicate JSON key {key!r}")
        result[key] = value
    return result


def strict_json(raw: bytes) -> Any:
    text = raw.decode("utf-8", errors="strict")
    return json.loads(text, object_pairs_hook=strict_pairs)


def expected_degree_three_exponents() -> list[list[int]]:
    rows: list[list[int]] = []
    for e0 in range(3, -1, -1):
        for e1 in range(3 - e0, -1, -1):
            for e2 in range(3 - e0 - e1, -1, -1):
                e3 = 3 - e0 - e1 - e2
                rows.append([e0, e1, e2, e3])
    return rows


def verify_c55_source_lock() -> tuple[dict[str, Any], list[dict[str, Any]]]:
    ancestry = subprocess.run(
        ["git", "merge-base", "--is-ancestor", C55_IMPLEMENTATION, C55_PROVENANCE],
        cwd=REPOSITORY,
    )
    if ancestry.returncode != 0:
        raise AssertionError("C55 implementation is not an ancestor of provenance")
    released_ancestry = subprocess.run(
        ["git", "merge-base", "--is-ancestor", C55_PROVENANCE, "HEAD"],
        cwd=REPOSITORY,
    )
    if released_ancestry.returncode != 0:
        raise AssertionError("C55 provenance is not an ancestor of current released HEAD")

    artifact_rows: list[dict[str, Any]] = []
    committed: dict[str, bytes] = {}
    for relative, expected_sha in C55_ARTIFACTS.items():
        repository_relative = f"{C55_PROJECT}/{relative}"
        raw = git_bytes(C55_PROVENANCE, repository_relative)
        actual_sha = sha256_bytes(raw)
        if actual_sha != expected_sha:
            raise AssertionError(f"C55 committed hash mismatch: {relative}")
        live = REPOSITORY / repository_relative
        if not live.is_file() or live.read_bytes() != raw:
            raise AssertionError(f"C55 live bytes differ from provenance blob: {relative}")
        committed[relative] = raw
        artifact_rows.append(
            {
                "path": repository_relative,
                "sha256": actual_sha,
                "git_blob_id": git_blob(C55_PROVENANCE, repository_relative),
                "live_equals_committed": True,
            }
        )

    route = committed["route_a_evaluation.yaml"].decode("utf-8")
    archived_route = committed["evaluations/route_a/HCS-C55/20260815T000000Z.yaml"]
    if committed["route_a_evaluation.yaml"] != archived_route:
        raise AssertionError("C55 Route root/archive mismatch")
    required_route_lines = (
        "documentation_status: DOCS_FINAL_NO_MORE_EDITS",
        "code_results_status: RELEASE_CANDIDATE",
        "release_status: RELEASE_FROZEN",
        f"code_commit: {C55_IMPLEMENTATION}",
        'full_project_manifest_status: VERIFIED_47_ENTRIES_CURRENT',
    )
    if any(line not in route for line in required_route_lines):
        raise AssertionError("C55 layered frozen status contract mismatch")
    for relative in ("README.md", "INTEGRITY_REPORT.md", "IMPLEMENTATION_CHECKLIST.md"):
        text = committed[relative].decode("utf-8")
        if "RELEASE_FROZEN" not in text or C55_IMPLEMENTATION not in text:
            raise AssertionError(f"C55 final documentation status mismatch: {relative}")

    manifest_lines = committed["results/ARTIFACT_HASHES.sha256"].decode("utf-8").splitlines()
    if len(manifest_lines) != 47 or manifest_lines != sorted(manifest_lines, key=lambda line: line.split("  ", 1)[1]):
        raise AssertionError("C55 full manifest count/order mismatch")
    manifest_entries = []
    seen_paths: set[str] = set()
    for line in manifest_lines:
        match = re.fullmatch(r"([0-9a-f]{64})  ([^\n]+)", line)
        if match is None or match.group(2) in seen_paths:
            raise AssertionError("C55 full manifest syntax/uniqueness mismatch")
        expected_sha, relative = match.groups()
        pure = PurePosixPath(relative)
        if (
            pure.is_absolute() or str(pure) != relative or "\\" in relative
            or any(part in ("", ".", "..") for part in pure.parts)
            or pure.name == "ARTIFACT_HASHES.sha256"
        ):
            raise AssertionError("C55 full manifest unsafe/noncanonical path")
        seen_paths.add(relative)
        repository_relative = f"{C55_PROJECT}/{relative}"
        raw = git_bytes(C55_PROVENANCE, repository_relative)
        if sha256_bytes(raw) != expected_sha:
            raise AssertionError(f"C55 full manifest committed rebound failed: {relative}")
        live = REPOSITORY / repository_relative
        if not live.is_file() or live.read_bytes() != raw:
            raise AssertionError(f"C55 full manifest live rebound failed: {relative}")
        manifest_entries.append({"path": relative, "sha256": expected_sha})
    tracked_output = run(["git", "ls-tree", "-r", "--name-only", C55_PROVENANCE, "--", C55_PROJECT]).stdout.splitlines()
    tracked_relative = {
        str(PurePosixPath(path).relative_to(C55_PROJECT))
        for path in tracked_output
        if PurePosixPath(path).name not in FULL_MANIFEST_EXCLUDED_NAMES
        and not any(part in {"__pycache__", ".pytest_cache", ".ipynb_checkpoints"} for part in PurePosixPath(path).parts)
    }
    if seen_paths != tracked_relative:
        raise AssertionError("C55 full manifest is not the exact committed inventory")

    # The machine payload deliberately remains RELEASE_CANDIDATE inside the
    # frozen project.  Run its provenance-bound checker before importing rows.
    checker = REPOSITORY / C55_PROJECT / "code/c55_checker.py"
    certificate_path = REPOSITORY / C55_PROJECT / "results/c55_certificate.json"
    with tempfile.TemporaryDirectory(prefix="c56-c55-check-") as directory:
        output = Path(directory) / "independent_check.json"
        completed = run([sys.executable, str(checker), str(certificate_path), "--output", str(output)])
        if "C55 CHECK PASS" not in completed.stdout:
            raise AssertionError("committed C55 checker did not report PASS")
        check_raw = output.read_bytes()
        if sha256_bytes(check_raw) != C55_ARTIFACTS["results/independent_check.json"]:
            raise AssertionError("replayed C55 check report hash mismatch")

    certificate_raw = committed["results/c55_certificate.json"]
    certificate = strict_json(certificate_raw)
    if set(certificate) != {"schema", "payload_sha256", "payload"}:
        raise AssertionError("C55 certificate envelope mismatch")
    if certificate["schema"] != "hcs-c55-certificate-v1":
        raise AssertionError("C55 certificate schema mismatch")
    if certificate["payload_sha256"] != C55_PAYLOAD_SHA256:
        raise AssertionError("C55 payload lock mismatch")
    if sha256_bytes(canonical_json(certificate["payload"])) != C55_PAYLOAD_SHA256:
        raise AssertionError("C55 canonical payload hash mismatch")
    if certificate["payload"].get("artifact_status") != "RELEASE_CANDIDATE":
        raise AssertionError("C55 immutable machine-payload status mismatch")

    cubic = certificate["payload"]["rational_cubic_surface"]
    rows = cubic["primitive_integral_coefficients"]
    if sha256_bytes(canonical_json(rows)) != C55_COEFFICIENT_SHA256:
        raise AssertionError("C55 primitive coefficient canonical digest mismatch")
    if cubic["primitive_coefficients_sha256"] != C55_COEFFICIENT_SHA256:
        raise AssertionError("C55 coefficient digest leaf mismatch")
    if len(rows) != 20 or [row["exponents_u0_to_u3"] for row in rows] != expected_degree_three_exponents():
        raise AssertionError("C55 coefficient exponent order/content mismatch")
    if any(set(row) != {"exponents_u0_to_u3", "coefficient"} for row in rows):
        raise AssertionError("C55 coefficient row schema mismatch")
    if any(type(row["coefficient"]) is not int for row in rows):
        raise AssertionError("C55 noninteger coefficient")
    if math.gcd(*(abs(row["coefficient"]) for row in rows)) != 1 or rows[0]["coefficient"] <= 0:
        raise AssertionError("C55 primitive sign/content mismatch")
    certificate["_c56_full_manifest_entries"] = manifest_entries
    return certificate, artifact_rows


# Sparse polynomials use exponent tuples (a,b,c,d,s,t).
Sparse = dict[tuple[int, ...], int]


def sparse_add(left: Sparse, right: Sparse) -> Sparse:
    result = dict(left)
    for exponent, coefficient in right.items():
        result[exponent] = result.get(exponent, 0) + coefficient
        if result[exponent] == 0:
            del result[exponent]
    return result


def sparse_scale(poly: Sparse, scalar: int) -> Sparse:
    return {exponent: coefficient * scalar for exponent, coefficient in poly.items() if coefficient * scalar}


def sparse_multiply(left: Sparse, right: Sparse) -> Sparse:
    result: Sparse = {}
    for le, lc in left.items():
        for re_, rc in right.items():
            exponent = tuple(a + b for a, b in zip(le, re_))
            result[exponent] = result.get(exponent, 0) + lc * rc
    return {exponent: coefficient for exponent, coefficient in result.items() if coefficient}


def sparse_power(poly: Sparse, exponent: int) -> Sparse:
    result: Sparse = {(0,) * 6: 1}
    for _ in range(exponent):
        result = sparse_multiply(result, poly)
    return result


def line_equations_sparse(rows: list[dict[str, Any]]) -> list[list[dict[str, Any]]]:
    zero = (0,) * 6
    coordinate_polys: list[Sparse] = [
        {(0, 0, 0, 0, 1, 0): 1},
        {(0, 0, 0, 0, 0, 1): 1},
        {(1, 0, 0, 0, 1, 0): 1, (0, 0, 1, 0, 0, 1): 1},
        {(0, 1, 0, 0, 1, 0): 1, (0, 0, 0, 1, 0, 1): 1},
    ]
    expanded: Sparse = {}
    for row in rows:
        term: Sparse = {zero: row["coefficient"]}
        for poly, exponent in zip(coordinate_polys, row["exponents_u0_to_u3"]):
            term = sparse_multiply(term, sparse_power(poly, exponent))
        expanded = sparse_add(expanded, term)
    output: list[list[dict[str, Any]]] = []
    for t_degree in range(4):
        s_degree = 3 - t_degree
        terms = [
            {"exponents_abcd": list(exponent[:4]), "coefficient": coefficient}
            for exponent, coefficient in sorted(expanded.items(), reverse=True)
            if exponent[4:] == (s_degree, t_degree)
        ]
        output.append(terms)
    return output


def singular_surface_expression(rows: list[dict[str, Any]], variables: list[str]) -> str:
    terms: list[str] = []
    for row in rows:
        coefficient = row["coefficient"]
        monomial_parts = [
            variable if exponent == 1 else f"{variable}^{exponent}"
            for variable, exponent in zip(variables, row["exponents_u0_to_u3"])
            if exponent
        ]
        monomial = "*".join(monomial_parts) or "1"
        terms.append(f"{coefficient:+d}*{monomial}")
    return "".join(terms).lstrip("+")


def run_singular_script(script: str) -> list[str]:
    with tempfile.TemporaryDirectory(prefix="c56-singular-") as directory:
        path = Path(directory) / "replay.sing"
        path.write_text(script, encoding="utf-8")
        completed = run(["Singular", "-q", str(path)])
    transcript = completed.stdout + "\n" + completed.stderr
    lowered = transcript.lower()
    if "?" in transcript or any(token in lowered for token in ("error", "not found", "halt")):
        raise AssertionError("Singular emitted a syntax/runtime diagnostic despite its exit status")
    markers = [line.strip() for line in completed.stdout.splitlines() if line.startswith("C56_")]
    if not markers:
        raise AssertionError("Singular emitted no C56 markers")
    return markers


def parse_monomial(text: str, variables: str = "abcd") -> list[int]:
    if text == "1" or text == "gen(1)":
        return [0] * len(variables)
    text = text.replace("*gen(1)", "").replace("gen(1)", "1")
    if text == "1":
        return [0] * len(variables)
    cursor = 0
    exponents = [0] * len(variables)
    while cursor < len(text):
        variable = text[cursor]
        if variable not in variables:
            raise AssertionError(f"unparsed monomial {text!r}")
        cursor += 1
        start = cursor
        while cursor < len(text) and text[cursor].isdigit():
            cursor += 1
        exponent = int(text[start:cursor] or "1")
        exponents[variables.index(variable)] += exponent
    return exponents


def split_polynomial_terms(text: str) -> list[str]:
    if not text or any(character.isspace() for character in text):
        raise AssertionError("noncanonical polynomial text")
    starts = [0] + [index for index in range(1, len(text)) if text[index] in "+-"]
    ends = starts[1:] + [len(text)]
    return [text[start:end] for start, end in zip(starts, ends)]


def parse_shape_polynomial(text: str, leading_variable: str) -> dict[str, Any]:
    lambda_coefficient = 0
    max_degree = 27 if leading_variable == "d" else 26
    tail = [0] * (max_degree + 1)
    for token in split_polynomial_terms(text):
        match = re.fullmatch(r"([+-]?)(\d*)([abcd]?)(\d*)", token)
        if match is None:
            raise AssertionError(f"cannot parse Singular shape term {token!r}")
        sign = -1 if match.group(1) == "-" else 1
        digits, variable, exponent_digits = match.group(2), match.group(3), match.group(4)
        coefficient = sign * int(digits or "1")
        exponent = int(exponent_digits or "1") if variable else 0
        if variable == leading_variable and (leading_variable == "d" or exponent == 1):
            if leading_variable == "d":
                tail[exponent] += coefficient
            else:
                lambda_coefficient += coefficient
        elif variable == "d" or not variable:
            tail[exponent] += coefficient
        else:
            raise AssertionError("unexpected lex-shape variable")
    if leading_variable == "d":
        lambda_coefficient = tail[27]
    content_values = [lambda_coefficient] + tail
    content = math.gcd(*(abs(value) for value in content_values))
    if content != 1 or lambda_coefficient <= 0:
        raise AssertionError("shape polynomial primitive/sign normalization mismatch")
    return {
        "leading_variable": leading_variable,
        "leading_coefficient": lambda_coefficient,
        "tail_coefficients_d_0_up": tail,
        "primitive_content": content,
        "canonical_text_sha256": sha256_bytes((text + "\n").encode("utf-8")),
    }


def main_singular(rows: list[dict[str, Any]]) -> dict[str, Any]:
    form = singular_surface_expression(rows, ["q0", "q1", "q2", "q3"])
    script = f"""
option(redSB);
ring r0=0,(a,b,c,d,s,t),dp;
poly q0=s; poly q1=t; poly q2=a*s+c*t; poly q3=b*s+d*t;
poly F={form};
poly f0=subst(subst(F,t,0),s,1);
poly f1=subst(subst(diff(F,t),t,0),s,1);
poly f2=(1/2)*subst(subst(diff(diff(F,t),t),t,0),s,1);
poly f3=(1/6)*subst(subst(diff(diff(diff(F,t),t),t),t,0),s,1);
ideal I0=f0,f1,f2,f3;
ring rdp=0,(a,b,c,d),dp;
ideal I=imap(r0,I0); ideal G=std(I); module KB=kbase(G);
print("C56_DP_SIZE="+string(size(G)));
print("C56_DP_VDIM="+string(vdim(G)));
print("C56_DP_KBASE="+string(KB));
int i;
for(i=1;i<=size(G);i++) {{
  print("C56_DP_ROW="+string(leadmonom(G[i]))+"|"+string(deg(G[i]))+"|"+string(size(G[i])));
}}
ring rlex=0,(a,b,c,d),lp;
ideal L=fglm(rdp,G); ideal IL=imap(rdp,I);
print("C56_LEX_SIZE="+string(size(L)));
print("C56_LEX_VDIM="+string(vdim(L)));
for(i=1;i<=size(L);i++) {{
  print("C56_LEX_ROW="+string(cleardenom(L[i])));
  print("C56_LEX_ORIGINAL_REDUCE="+string(reduce(IL[i],L)==0));
}}
quit;
"""
    lines = run_singular_script(script)
    expected_marker_counts = {
        "C56_DP_SIZE=": 1,
        "C56_DP_VDIM=": 1,
        "C56_DP_KBASE=": 1,
        "C56_DP_ROW=": 21,
        "C56_LEX_SIZE=": 1,
        "C56_LEX_VDIM=": 1,
        "C56_LEX_ROW=": 4,
        "C56_LEX_ORIGINAL_REDUCE=": 4,
    }
    for prefix, count in expected_marker_counts.items():
        if sum(line.startswith(prefix) for line in lines) != count:
            raise AssertionError(f"Singular main marker count mismatch: {prefix}")
    if len(lines) != sum(expected_marker_counts.values()):
        raise AssertionError("unexpected Singular main marker")
    singleton = {line.split("=", 1)[0]: line.split("=", 1)[1] for line in lines if line.count("=") == 1 and not line.startswith(("C56_DP_ROW=", "C56_LEX_ROW=", "C56_LEX_ORIGINAL_REDUCE="))}
    if singleton.get("C56_DP_SIZE") != "21" or singleton.get("C56_DP_VDIM") != "27":
        raise AssertionError("Singular dp line-scheme dimensions mismatch")
    if singleton.get("C56_LEX_SIZE") != "4" or singleton.get("C56_LEX_VDIM") != "27":
        raise AssertionError("Singular FGLM shape dimensions mismatch")
    kbase_line = next(line for line in lines if line.startswith("C56_DP_KBASE="))
    standard = [parse_monomial(item) for item in kbase_line.split("=", 1)[1].split(",")]
    if len(standard) != 27:
        raise AssertionError("Singular standard-monomial count mismatch")
    standard.sort()
    standard_degree_counts = [sum(sum(row) == degree for row in standard) for degree in range(5)]
    if standard_degree_counts != [1, 4, 10, 12, 0] or any(sum(row) >= 4 for row in standard):
        raise AssertionError("Singular standard-monomial Hilbert counts mismatch")
    dp_rows = []
    for line in lines:
        if line.startswith("C56_DP_ROW="):
            monomial, degree, terms = line.split("=", 1)[1].split("|")
            dp_rows.append({"leading_monomial_abcd": parse_monomial(monomial), "degree": int(degree), "term_count": int(terms)})
    dp_rows.sort(key=lambda row: row["leading_monomial_abcd"])
    lex_text = [line.split("=", 1)[1] for line in lines if line.startswith("C56_LEX_ROW=")]
    reductions = [line.endswith("=1") for line in lines if line.startswith("C56_LEX_ORIGINAL_REDUCE=")]
    if len(dp_rows) != 21 or len(lex_text) != 4 or reductions != [True] * 4:
        raise AssertionError("Singular basis/remainder marker mismatch")
    shapes = [parse_shape_polynomial(text, variable) for text, variable in zip(lex_text, ("d", "c", "b", "a"))]
    if shapes[0]["canonical_text_sha256"] != ELIMINANT_TEXT_SHA256:
        raise AssertionError("fresh committed-input eliminant hash mismatch")
    return {
        "dp_basis_size": 21,
        "dp_quotient_dimension": 27,
        "dp_basis_rows": dp_rows,
        "standard_monomials_abcd": standard,
        "standard_monomial_degree_counts_0_to_4": standard_degree_counts,
        "lex_basis_size": 4,
        "lex_quotient_dimension": 27,
        "lex_shape": shapes,
        "singular_original_equation_reductions_zero": reductions,
    }


def univariate_text(coefficients: list[int], variable: str = "d") -> str:
    terms: list[str] = []
    for exponent in range(len(coefficients) - 1, -1, -1):
        coefficient = coefficients[exponent]
        if coefficient == 0:
            continue
        sign = "-" if coefficient < 0 else ("+" if terms else "")
        absolute = abs(coefficient)
        if exponent == 0:
            body = str(absolute)
        elif exponent == 1:
            body = f"{absolute}{variable}"
        else:
            body = f"{absolute}{variable}{exponent}"
        terms.append(sign + body)
    return "".join(terms) or "0"


def parse_univariate_mod(text: str, prime: int) -> list[int]:
    coefficients: dict[int, int] = {}
    for token in split_polynomial_terms(text):
        match = re.fullmatch(r"([+-]?)(\d*)(d?)(\d*)", token)
        if match is None:
            raise AssertionError(f"cannot parse modular factor {token!r}")
        sign = -1 if match.group(1) == "-" else 1
        digits, variable, exponent_digits = match.group(2), match.group(3), match.group(4)
        coefficient = sign * int(digits or "1")
        exponent = int(exponent_digits or "1") if variable else 0
        coefficients[exponent] = (coefficients.get(exponent, 0) + coefficient) % prime
    degree = max((degree for degree, value in coefficients.items() if value), default=0)
    return [coefficients.get(index, 0) for index in range(degree + 1)]


def mod_multiply(left: list[int], right: list[int], prime: int) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, lc in enumerate(left):
        for j, rc in enumerate(right):
            result[i + j] = (result[i + j] + lc * rc) % prime
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def subset_sums(degrees: Iterable[int]) -> list[int]:
    values = {0}
    for degree in degrees:
        values |= {value + degree for value in tuple(values)}
    return sorted(values)


def factor_singular(g_coefficients: list[int]) -> dict[str, Any]:
    blocks: list[str] = []
    g_text = univariate_text(g_coefficients)
    for prime in WITNESS_PATTERNS:
        blocks.append(
            f"""
ring r{prime}={prime},(d),lp;
poly g={g_text}; list ff=factorize(g); int j;
print("C56_MOD_META={prime}|"+string(deg(g))+"|"+string(leadcoef(g))+"|"+string(deg(gcd(g,diff(g,d))))+"|"+string(ff[1][1]));
for(j=2;j<=size(ff[1]);j++) {{
  print("C56_MOD_FACTOR={prime}|"+string(ff[2][j])+"|"+string(ff[1][j]));
}}
"""
        )
    lines = run_singular_script("\n".join(blocks) + "\nquit;\n")
    if sum(line.startswith("C56_MOD_META=") for line in lines) != 4:
        raise AssertionError("Singular modular meta marker count mismatch")
    if sum(line.startswith("C56_MOD_FACTOR=") for line in lines) != sum(len(pattern) for pattern in WITNESS_PATTERNS.values()):
        raise AssertionError("Singular modular factor marker count mismatch")
    if len(lines) != 4 + sum(len(pattern) for pattern in WITNESS_PATTERNS.values()):
        raise AssertionError("unexpected Singular modular marker")
    records: dict[int, dict[str, Any]] = {}
    for prime in WITNESS_PATTERNS:
        meta = next(line for line in lines if line.startswith(f"C56_MOD_META={prime}|"))
        _, degree, leading, gcd_degree, unit = meta.split("=", 1)[1].split("|")
        factors = []
        for line in lines:
            if line.startswith(f"C56_MOD_FACTOR={prime}|"):
                _, multiplicity, text = line.split("=", 1)[1].split("|", 2)
                coefficients = parse_univariate_mod(text, prime)
                if coefficients[-1] % prime != 1:
                    raise AssertionError("Singular modular factor is not monic")
                factors.append({"multiplicity": int(multiplicity), "coefficients_mod_p_0_up": coefficients})
        factors.sort(key=lambda row: (len(row["coefficients_mod_p_0_up"]), row["coefficients_mod_p_0_up"]))
        unit_mod = int(unit) % prime
        product = [unit_mod]
        degrees: list[int] = []
        for factor in factors:
            for _ in range(factor["multiplicity"]):
                product = mod_multiply(product, factor["coefficients_mod_p_0_up"], prime)
                degrees.append(len(factor["coefficients_mod_p_0_up"]) - 1)
        reduced_g = [coefficient % prime for coefficient in g_coefficients]
        while len(reduced_g) > 1 and reduced_g[-1] == 0:
            reduced_g.pop()
        degrees.sort()
        if int(degree) != 27 or int(leading) % prime == 0 or int(gcd_degree) != 0:
            raise AssertionError(f"bad eliminant reduction at {prime}")
        if product != reduced_g or tuple(degrees) != WITNESS_PATTERNS[prime]:
            raise AssertionError(f"Singular modular factor rebound mismatch at {prime}")
        records[prime] = {
            "prime": prime,
            "eliminant_degree_preserved": True,
            "leading_coefficient_mod_p": g_coefficients[-1] % prime,
            "derivative_gcd_degree": 0,
            "squarefree": True,
            "factorization_unit_mod_p": unit_mod,
            "factors": factors,
            "factor_degrees": degrees,
            "factor_multiplication_rebound": True,
            "subset_sums": subset_sums(degrees),
        }
    return {str(prime): records[prime] for prime in sorted(records)}


def singular_geometry(rows: list[dict[str, Any]]) -> tuple[dict[str, Any], dict[str, Any]]:
    form = singular_surface_expression(rows, ["q0", "q1", "q2", "q3"])
    complement_script = f"""
option(redSB); ring r=0,(a,b,c,d,s,t),dp;
proc lineideal(poly q0,poly q1,poly q2,poly q3) {{
  poly F={form};
  poly f0=subst(subst(F,t,0),s,1);
  poly f1=subst(subst(diff(F,t),t,0),s,1);
  poly f2=(1/2)*subst(subst(diff(diff(F,t),t),t,0),s,1);
  poly f3=(1/6)*subst(subst(diff(diff(diff(F,t),t),t),t,0),s,1);
  return(ideal(f0,f1,f2,f3));
}}
proc emptycheck(ideal I,string tag) {{ ideal G=std(I); print("C56_COMPLEMENT="+tag+"|"+string(reduce(1,G)==0)+"|"+string(size(G))); }}
ideal I02=lineideal(s,a*s+c*t,t,b*s+d*t),c; emptycheck(I02,"U02");
ideal I03=lineideal(s,a*s+c*t,b*s+d*t,t),c; emptycheck(I03,"U03");
ideal I12=lineideal(a*s+c*t,s,t,b*s+d*t),c; emptycheck(I12,"U12");
ideal I13=lineideal(a*s+c*t,s,b*s+d*t,t),c; emptycheck(I13,"U13");
ideal I23=lineideal(a*s+c*t,b*s+d*t,s,t),a*d-b*c; emptycheck(I23,"U23");
quit;
"""
    complement_lines = run_singular_script(complement_script)
    if len(complement_lines) != 5 or any(not line.startswith("C56_COMPLEMENT=") for line in complement_lines):
        raise AssertionError("Singular complement marker inventory mismatch")
    definitions = {
        "U02": (["s", "a*s+c*t", "t", "b*s+d*t"], "c"),
        "U03": (["s", "a*s+c*t", "b*s+d*t", "t"], "c"),
        "U12": (["a*s+c*t", "s", "t", "b*s+d*t"], "c"),
        "U13": (["a*s+c*t", "s", "b*s+d*t", "t"], "c"),
        "U23": (["a*s+c*t", "b*s+d*t", "s", "t"], "a*d-b*c"),
    }
    complement = []
    for name, (coordinates, p01) in definitions.items():
        line = next(item for item in complement_lines if item.startswith(f"C56_COMPLEMENT={name}|"))
        _, unit, size = line.split("=", 1)[1].split("|")
        if unit != "1" or size != "1":
            raise AssertionError(f"nonempty Grassmann complement in {name}")
        complement.append({"chart": name, "coordinates": coordinates, "p01_zero_equation": p01, "singular_unit_ideal": True, "groebner_basis_size": 1})

    smooth_blocks = []
    for label, characteristic in (("Q", 0), ("7", 7), ("19", 19), ("29", 29), ("37", 37)):
        smooth_form = singular_surface_expression(rows, ["x0", "x1", "x2", "x3"])
        smooth_blocks.append(
            f"""
ring rs{label}={characteristic},(x0,x1,x2,x3),dp;
poly F={smooth_form}; ideal J=F,diff(F,x0),diff(F,x1),diff(F,x2),diff(F,x3); int ok=1; int i;
for(i=1;i<=4;i++) {{ ideal A=J,var(i)-1; ideal B=std(A); if(reduce(1,B)!=0) {{ ok=0; }} }}
print("C56_SMOOTH={label}|"+string(ok));
"""
        )
    smooth_lines = run_singular_script("\n".join(smooth_blocks) + "\nquit;\n")
    if len(smooth_lines) != 5 or any(not line.startswith("C56_SMOOTH=") for line in smooth_lines):
        raise AssertionError("Singular smoothness marker inventory mismatch")
    smoothness = {}
    for label in ("Q", "7", "19", "29", "37"):
        line = next(item for item in smooth_lines if item.startswith(f"C56_SMOOTH={label}|"))
        if not line.endswith("|1"):
            raise AssertionError(f"surface singular in characteristic {label}")
        smoothness[label] = {"four_affine_projective_chart_unit_ideals": [True] * 4, "surface_smooth": True}
    return {"charts": complement, "all_five_unit_ideals": True}, smoothness


def lattice_dot(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return left[0] * right[0] - sum(a * b for a, b in zip(left[1:], right[1:]))


def vector_add(left: tuple[int, ...], right: tuple[int, ...], scale: int = 1) -> tuple[int, ...]:
    return tuple(a + scale * b for a, b in zip(left, right))


def reflect(vector: tuple[int, ...], root: tuple[int, ...]) -> tuple[int, ...]:
    return vector_add(vector, root, lattice_dot(vector, root))


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[index]] for index in range(len(right)))


def cycle_type(permutation: tuple[int, ...]) -> tuple[int, ...]:
    seen = [False] * len(permutation)
    output = []
    for start in range(len(permutation)):
        if seen[start]:
            continue
        current = start
        length = 0
        while not seen[current]:
            seen[current] = True
            length += 1
            current = permutation[current]
        output.append(length)
    return tuple(sorted(output))


def permutation_sign(permutation: tuple[int, ...]) -> int:
    inversions = sum(permutation[i] > permutation[j] for i in range(len(permutation)) for j in range(i + 1, len(permutation)))
    return -1 if inversions % 2 else 1


def integer_rank(rows: list[list[int]]) -> int:
    matrix = [[Fraction(value) for value in row] for row in rows]
    rank = 0
    columns = len(matrix[0]) if matrix else 0
    for column in range(columns):
        pivot = next((index for index in range(rank, len(matrix)) if matrix[index][column]), None)
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        scale = matrix[rank][column]
        matrix[rank] = [value / scale for value in matrix[rank]]
        for index in range(len(matrix)):
            if index != rank and matrix[index][column]:
                factor = matrix[index][column]
                matrix[index] = [a - factor * b for a, b in zip(matrix[index], matrix[rank])]
        rank += 1
    return rank


def integer_determinant(rows: list[list[int]]) -> int:
    matrix = [[Fraction(value) for value in row] for row in rows]
    determinant = Fraction(1)
    for column in range(len(matrix)):
        pivot = next((index for index in range(column, len(matrix)) if matrix[index][column]), None)
        if pivot is None:
            return 0
        if pivot != column:
            matrix[column], matrix[pivot] = matrix[pivot], matrix[column]
            determinant *= -1
        pivot_value = matrix[column][column]
        determinant *= pivot_value
        matrix[column] = [value / pivot_value for value in matrix[column]]
        for row in range(column + 1, len(matrix)):
            factor = matrix[row][column]
            if factor:
                matrix[row] = [a - factor * b for a, b in zip(matrix[row], matrix[column])]
    if determinant.denominator != 1:
        raise AssertionError("nonintegral reflection determinant")
    return determinant.numerator


def enumerate_we6() -> dict[str, Any]:
    h = (1, 0, 0, 0, 0, 0, 0)
    exceptional = []
    for index in range(6):
        vector = [0] * 7
        vector[index + 1] = 1
        exceptional.append(tuple(vector))
    line_classes = list(exceptional)
    for left, right in combinations(range(6), 2):
        vector = list(h)
        vector[left + 1] = -1
        vector[right + 1] = -1
        line_classes.append(tuple(vector))
    for omitted in range(6):
        vector = [2] + [-1] * 6
        vector[omitted + 1] = 0
        line_classes.append(tuple(vector))
    if len(line_classes) != 27 or len(set(line_classes)) != 27:
        raise AssertionError("27 line class construction failed")
    index = {line: number for number, line in enumerate(line_classes)}
    roots = [vector_add(exceptional[i], exceptional[i + 1], -1) for i in range(5)]
    roots.append((1, -1, -1, -1, 0, 0, 0))
    root_squares = [lattice_dot(root, root) for root in roots]
    if root_squares != [-2] * 6:
        raise AssertionError("simple root square mismatch")
    generators = [tuple(index[reflect(line, root)] for line in line_classes) for root in roots]
    identity = tuple(range(27))
    coxeter_parity = {identity: 0}
    queue = deque([identity])
    while queue:
        current = queue.popleft()
        for generator in generators:
            successor = compose(generator, current)
            parity = coxeter_parity[current] ^ 1
            if successor not in coxeter_parity:
                coxeter_parity[successor] = parity
                queue.append(successor)
            elif coxeter_parity[successor] != parity:
                raise AssertionError("Coxeter parity is not well-defined")
    target = (2, 5, 5, 5, 10)
    target_counts = Counter()
    target_s27_signs: set[int] = set()
    s27_odd = 0
    for element, parity in coxeter_parity.items():
        if permutation_sign(element) == -1:
            s27_odd += 1
        if cycle_type(element) == target:
            target_counts[parity] += 1
            target_s27_signs.add(permutation_sign(element))
    fixed_rows: list[list[int]] = []
    anti_canonical = (3, -1, -1, -1, -1, -1, -1)
    anticanonical_fixed = []
    intersection_preserved = []
    reflection_determinants = []
    form_diagonal = [1, -1, -1, -1, -1, -1, -1]
    for root in roots:
        columns: list[tuple[int, ...]] = []
        for basis_index in range(7):
            basis = tuple(int(i == basis_index) for i in range(7))
            columns.append(reflect(basis, root))
        matrix_minus_identity = [
            [columns[column][row] - int(row == column) for column in range(7)]
            for row in range(7)
        ]
        if any(sum(matrix_minus_identity[row][column] * anti_canonical[column] for column in range(7)) != 0 for row in range(7)):
            raise AssertionError("anticanonical class is not fixed by simple reflection")
        anticanonical_fixed.append(True)
        matrix = [[columns[column][row] for column in range(7)] for row in range(7)]
        reflection_determinants.append(integer_determinant(matrix))
        preserves = True
        for left in range(7):
            for right in range(7):
                value = sum(matrix[k][left] * form_diagonal[k] * matrix[k][right] for k in range(7))
                if value != (form_diagonal[left] if left == right else 0):
                    preserves = False
        intersection_preserved.append(preserves)
        fixed_rows.extend(matrix_minus_identity)
    fixed_rank = 7 - integer_rank(fixed_rows)
    orbit_size = len({element[0] for element in coxeter_parity})
    if (len(coxeter_parity), sum(value == 0 for value in coxeter_parity.values()), orbit_size, target_counts[0], target_counts[1], s27_odd, fixed_rank) != (51840, 25920, 27, 0, 5184, 0, 1):
        raise AssertionError("W(E6) enumeration mismatch")
    if target_s27_signs != {1}:
        raise AssertionError("target cycle type S27 sign mismatch")
    if reflection_determinants != [-1] * 6 or intersection_preserved != [True] * 6:
        raise AssertionError("simple reflection lattice gate mismatch")
    line_intersections = [[lattice_dot(left, right) for right in line_classes] for left in line_classes]
    incidence_preserved = [
        all(line_intersections[generator[i]][generator[j]] == line_intersections[i][j] for i in range(27) for j in range(27))
        for generator in generators
    ]
    if incidence_preserved != [True] * 6:
        raise AssertionError("line incidence is not preserved")
    return {
        "picard_basis": ["H", "E1", "E2", "E3", "E4", "E5", "E6"],
        "intersection_form_diagonal": [1, -1, -1, -1, -1, -1, -1],
        "canonical_class_negative": [3, -1, -1, -1, -1, -1, -1],
        "simple_roots": [list(root) for root in roots],
        "simple_root_self_intersections": root_squares,
        "line_classes": [list(line) for line in line_classes],
        "line_class_intersection_matrix": line_intersections,
        "line_class_intersection_matrix_sha256": sha256_bytes(canonical_json(line_intersections)),
        "simple_reflection_line_permutations": [list(generator) for generator in generators],
        "simple_reflections_preserve_picard_intersection": intersection_preserved,
        "simple_reflections_preserve_line_incidence": incidence_preserved,
        "group_order": 51840,
        "line_orbit_size": orbit_size,
        "index_two_kernel_definition": "kernel_of_E6_reflection_determinant_equivalently_Coxeter_word_parity_not_S27_sign",
        "index_two_kernel_order": 25920,
        "all_W_E6_line_permutations_have_even_S27_sign": True,
        "S27_odd_element_count": s27_odd,
        "target_cycle_type": list(target),
        "target_cycle_type_S27_sign": next(iter(target_s27_signs)),
        "target_cycle_count": target_counts[0] + target_counts[1],
        "target_in_index_two_kernel_count": target_counts[0],
        "target_outside_index_two_kernel_count": target_counts[1],
        "simple_reflection_determinants_on_E6": reflection_determinants,
        "anticanonical_fixed_by_all_simple_reflections": anticanonical_fixed,
        "picard_fixed_rank": fixed_rank,
    }


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
    if type(value) is bool:
        return "bool"
    if type(value) is int:
        return "int"
    if type(value) is str:
        return "str"
    if value is None:
        return "null"
    raise AssertionError(f"forbidden payload scalar {type(value).__name__}")


def build_payload() -> dict[str, Any]:
    certificate, c55_artifacts = verify_c55_source_lock()
    full_manifest_entries = certificate.pop("_c56_full_manifest_entries")
    coefficient_rows = certificate["payload"]["rational_cubic_surface"]["primitive_integral_coefficients"]
    main_chart = main_singular(coefficient_rows)
    line_equations = line_equations_sparse(coefficient_rows)
    complement, smoothness = singular_geometry(coefficient_rows)
    g_coefficients = main_chart["lex_shape"][0]["tail_coefficients_d_0_up"]
    modular = factor_singular(g_coefficients)
    for prime in WITNESS_PATTERNS:
        good_reduction = (
            smoothness[str(prime)]["surface_smooth"] is True
            and smoothness[str(prime)]["four_affine_projective_chart_unit_ideals"] == [True] * 4
        )
        if not good_reduction:
            raise AssertionError(f"surface good-reduction cross-gate failed at {prime}")
        modular[str(prime)]["surface_good_reduction"] = good_reduction
    intersection_chain = []
    current: set[int] | None = None
    for prime in sorted(WITNESS_PATTERNS):
        sums = set(modular[str(prime)]["subset_sums"])
        current = sums if current is None else current & sums
        intersection_chain.append({"through_prime": prime, "intersection": sorted(current)})
    if sorted(current or ()) != [0, 27]:
        raise AssertionError("four-prime irreducibility sieve failed")
    we6 = enumerate_we6()
    payload = {
        "material_passport": {
            "candidate_id": "HCS-C56",
            "slug": "henon_mu3_yukawa_line_field",
            "artifact_status": "PREFREEZE_CODE_RESULTS_PASS",
            "arithmetic_mode": "exact_Q_and_finite_fields_no_floating_point",
            "tmp_reconnaissance_is_theorem_evidence": False,
        },
        "c55_source_lock": {
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
            "committed_artifacts": c55_artifacts,
            "full_manifest_entry_count": 47,
            "full_manifest_entries": full_manifest_entries,
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
            "primitive_coefficients": coefficient_rows,
            "committed_checker_replay_passed_before_coefficient_import": True,
        },
        "surface": {
            "variables": ["u0", "u1", "u2", "u3"],
            "primitive_coefficients": coefficient_rows,
            "primitive_coefficients_sha256": C55_COEFFICIENT_SHA256,
            "coefficient_count": 20,
            "coefficient_gcd": 1,
            "first_coefficient_positive": True,
            "projective_GL4_Q_and_common_nonzero_Q_scalar_invariance": True,
            "smoothness": smoothness,
        },
        "grassmann_main_chart": {
            "chart": "U01",
            "coordinates": ["s", "t", "a*s+c*t", "b*s+d*t"],
            "line_equations_sparse": line_equations,
            **main_chart,
            "all_four_back_substitution_remainders_zero": True,
        },
        "grassmann_complement": complement,
        "irreducibility": {
            "eliminant_coefficients_d_0_to_27": g_coefficients,
            "eliminant_degree": 27,
            "eliminant_primitive_content": 1,
            "eliminant_canonical_singular_text_sha256": ELIMINANT_TEXT_SHA256,
            "modular_witnesses": modular,
            "subset_sum_intersection_chain": intersection_chain,
            "final_subset_sum_intersection": [0, 27],
            "gauss_lemma_irreducibility_gate": True,
        },
        "we6": we6,
        "theorem_gates": {
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
        },
    }
    return payload


def build_schema(payload: dict[str, Any]) -> dict[str, Any]:
    descriptor = shape_descriptor(payload)
    return {
        "schema_id": "hcs-c56-certificate-schema-v1",
        "payload_top_level_keys": sorted(payload),
        "payload_shape_sha256": sha256_bytes(canonical_json(descriptor)),
        "payload_scalar_leaf_count": scalar_leaf_count(payload),
        "unknown_fields_rejected": True,
        "duplicate_keys_rejected": True,
        "floats_rejected": True,
        "booleans_rejected_in_integer_slots": True,
        "noncanonical_integers_rejected": True,
        "non_UTF8_rejected": True,
        "oversized_input_rejected": True,
        "optimized_python_rejected": True,
        "max_certificate_bytes": 2_000_000,
    }


def write_certificate(output: Path, schema_output: Path | None = None) -> dict[str, Any]:
    if sys.flags.optimize:
        raise SystemExit("optimized Python is forbidden")
    payload = build_payload()
    schema = build_schema(payload)
    envelope = {
        "schema": schema,
        "schema_sha256": sha256_bytes(canonical_json(schema)),
        "payload": payload,
        "payload_sha256": sha256_bytes(canonical_json(payload)),
    }
    raw = json.dumps(envelope, sort_keys=True, indent=2, ensure_ascii=False).encode("utf-8") + b"\n"
    if len(raw) > schema["max_certificate_bytes"]:
        raise AssertionError("certificate exceeds schema size budget")
    output.parent.mkdir(parents=True, exist_ok=True)
    write_new_regular(output, raw)
    if schema_output is not None:
        schema_raw = json.dumps(schema, sort_keys=True, indent=2, ensure_ascii=False).encode("utf-8") + b"\n"
        schema_output.parent.mkdir(parents=True, exist_ok=True)
        write_new_regular(schema_output, schema_raw)
    return envelope


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--schema-output", type=Path)
    arguments = parser.parse_args()
    outputs = [arguments.output] + ([arguments.schema_output] if arguments.schema_output is not None else [])
    resolved_outputs = [path.resolve() for path in outputs]
    if len(set(resolved_outputs)) != len(resolved_outputs):
        raise SystemExit("certificate and schema outputs must be distinct")
    for output in outputs:
        remove_stale_regular_output(output)
    if sys.flags.optimize or (os.environ.get("PYTHONOPTIMIZE") not in (None, "", "0")):
        raise SystemExit("optimized Python is forbidden")
    try:
        envelope = write_certificate(arguments.output, arguments.schema_output)
    except BaseException:
        for output in outputs:
            output.unlink(missing_ok=True)
        raise
    print(f"wrote {arguments.output}")
    print(f"payload_sha256={envelope['payload_sha256']}")
    print(f"schema_sha256={envelope['schema_sha256']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
