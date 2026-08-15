#!/usr/bin/env python3
"""Independent full-leaf checker for the HCS-C57 PREFREEZE certificate."""

from __future__ import annotations

import argparse
import ast
from copy import deepcopy
from fractions import Fraction
import hashlib
import itertools
import json
import math
from math import comb
import os
from pathlib import Path
import re
import subprocess
import sys
from typing import Any

from flint import fmpq, fmpq_poly

from c57_exact import (
    StrictDataError,
    atomic_write,
    canonical_json_bytes,
    canonical_leaf_bytes,
    deterministic_gzip,
    deep_exact,
    prepare_output_targets,
    read_stable,
    regular_file,
    reject_optimized_python,
    require_exact_keys,
    require_canonical_compact_json,
    safe_relative_path,
    sha256_bytes,
    strict_gzip_json,
    strict_json_loads,
)
from c57_pipeline import (
    clean_environment,
    python_preflight,
    singular_preflight,
)


REPO = Path(__file__).resolve().parents[3]
PROJECT = Path(__file__).resolve().parents[1]
CODE = PROJECT / "code"
C56 = REPO / "henon_dynamics/henon_mu3_yukawa_line_field"
C56_CERTIFICATE = C56 / "results/c56_certificate.json"
C56_SCHEMA = C56 / "results/c56_schema.json"
C56_CHECK_REPORT = C56 / "results/c56_check_report.json"
IMPLEMENTATION_COMMIT = "b32402f1dd276a2684d3e849dae26150ebb595e1"
PROVENANCE_COMMIT = "6594400c577c4f59090174dc79b981ffbe8a50ac"
FINAL_REPAIR_COMMIT = "883cb727e57135a0b098a882d9995dd000df2bc0"
C56_CERTIFICATE_SHA256 = "26739ce5aedb4a3467645f9c1b2036d4d3eec9ce4d0dbce23d67ea7b67e5fbc4"
C56_PAYLOAD_SHA256 = "5b17c9ed7bea60680556af70297199b653d51188bb30ce59f7c2c6bfbc94f661"
C56_SCOPED_MANIFEST_SHA256 = "20d29af97128e766bb5e59bf6f82f8401c6ed62f279371b031febcefd5d99b4a"
C56_CHECK_REPORT_SHA256 = "4ccfb09139a4bfa812ea9c57ff8b65a6a8e603dbdb00e245355a4563386489a9"
BRIDGE_PRIMES = (
    7,
    37,
    100000000000000000000000000000000000000000000012477,
)
ARTIFACTS = {
    "a12_crt_transcript.json.gz": (
        18_797_009,
        "5171ed975096c1cffed221e7eeec7a87d3afd2970ccd91c431b5283587f7a22f",
        40_146_042,
        "1189d4b015b2024fede11fbc4361575eccbddeed9c3ff6043cd34d16ec311fb2",
        25_000_000,
        50_000_000,
    ),
    "a12_table.json.gz": (
        15_817_606,
        "1034828fcfaad5262ea0388762947e78bf51f3986be642643dfdf5f66711e3f6",
        33_700_083,
        "9dd43ebbdd61873dae3f6437c160a0dfbc389934a62a38057b915955c117c3cc",
        40_000_000,
        40_000_000,
    ),
    "delta_crt.json.gz": (
        97_372,
        "4deead9914f31b0012afd91088339793330874a3b5156ceaeb1371fcb495f685",
        288_384,
        "61ead9febb5ee8295c75980b81ba1c73c2d9cdaebf9e87dd0d0e76da899999a9",
        1_000_000,
        1_000_000,
    ),
    "incidence_char0_witness.json.gz": (
        1_697_390,
        "4853641b143d3d7d0c2086fbee13f9d1f191bac960a989e8e85aede117cf8060",
        4_297_007,
        "2c42ac21f43e54870b030c71facff31b0b0b5a05da544b7455f960e47448a392",
        3_000_000,
        6_000_000,
    ),
    "theta_crt.json.gz": (
        50_282,
        "91181a525e0acb17e73d2e96fd4e7d5d7a25913784ef8ad9d3be59c430a4fadd",
        132_705,
        "5760dd3f4a1e07834f974e340f6cd488d9b793dab8efa0864505903cf9e1bcb3",
        1_000_000,
        1_000_000,
    ),
}

CODE_SOURCE_FILES = (
    "README.md",
    "c57_a12_reconstruction.py",
    "c57_atomic_promote.py",
    "c57_checker.py",
    "c57_exact.py",
    "c57_flint_carrier_identity.py",
    "c57_group.py",
    "c57_hash_manifest.py",
    "c57_incidence_bridge.py",
    "c57_incidence_char0_verify.py",
    "c57_irreducibility.py",
    "c57_modular_resolvent.py",
    "c57_pipeline.py",
    "c57_producer.py",
    "c57_quartic_pivot.py",
    "c57_resolver_replay.py",
    "run_all.sh",
    "test_c57.py",
)


def rebuild_c57_source_contract() -> dict[str, Any]:
    if len(CODE_SOURCE_FILES) != 18 or len(set(CODE_SOURCE_FILES)) != 18:
        raise StrictDataError("C57 source allowlist must contain 18 distinct names")
    children = list(CODE.iterdir())
    observed = {path.name for path in children}
    if len(observed) != len(children) or observed != set(CODE_SOURCE_FILES):
        raise StrictDataError(
            f"C57 code inventory mismatch; missing={sorted(set(CODE_SOURCE_FILES)-observed)}; "
            f"extra={sorted(observed-set(CODE_SOURCE_FILES))}"
        )
    entries = []
    for name in CODE_SOURCE_FILES:
        raw, fingerprint = read_stable(CODE / name, max_bytes=2_000_000)
        entries.append(
            {
                "path": f"code/{name}",
                "sha256": fingerprint.sha256,
                "size_bytes": len(raw),
            }
        )
    return {
        "schema_id": "hcs-c57-exact-source-contract-v1",
        "entry_count": len(entries),
        "exact_code_inventory": True,
        "entries": entries,
        "self_reference_policy": "final certificate/schema/check/manifest digests are not embedded; immutable evidence inputs may be source-locked",
        "scoped_manifest_must_rebind_all_code_and_results_artifacts": True,
    }


def git(*arguments: str, check: bool = True) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["/usr/bin/git", *arguments],
        cwd=REPO,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=clean_environment(),
        check=check,
        timeout=60,
    )


def rebuild_g0() -> dict[str, Any]:
    expected_files = {
        "henon_dynamics/henon_mu3_yukawa_line_field/code/c56_checker.py": (
            "05eaa9001c9138c4429c1d369d14dade96e9d09c",
            "83923b42662bb1368380271bf83476966dbd6c0522a78d7b0b86cafb1e1bfd63",
        ),
        "henon_dynamics/henon_mu3_yukawa_line_field/results/c56_certificate.json": (
            "d8c9faa272682bf9403605c59fcef09fcccbe000",
            C56_CERTIFICATE_SHA256,
        ),
        "henon_dynamics/henon_mu3_yukawa_line_field/results/c56_check_report.json": (
            "e902189d1c66e33bdd5283389b1d512c909b67c1",
            C56_CHECK_REPORT_SHA256,
        ),
        "henon_dynamics/henon_mu3_yukawa_line_field/results/c56_schema.json": (
            "01717e84a0efdb204d38ecd881a7827a7af01958",
            "adab34998a944c8a4af8db774e511f0453839ea6a6e14e9437ffc259be3da504",
        ),
        "henon_dynamics/henon_mu3_yukawa_line_field/results/scoped_hash_manifest.json": (
            "e287006599be564b617ba92bf948b253a695bddd",
            C56_SCOPED_MANIFEST_SHA256,
        ),
    }
    ancestry = []
    for left, right, label in (
        (IMPLEMENTATION_COMMIT, PROVENANCE_COMMIT, "implementation_to_provenance"),
        (PROVENANCE_COMMIT, FINAL_REPAIR_COMMIT, "provenance_to_final_repair"),
        (FINAL_REPAIR_COMMIT, "HEAD", "final_repair_to_current_HEAD"),
    ):
        completed = git("merge-base", "--is-ancestor", left, right, check=False)
        if completed.returncode or completed.stderr:
            raise StrictDataError(f"C56 ancestry failed: {label}")
        ancestry.append({"relation": label, "verified": True})
    scope = "henon_dynamics/henon_mu3_yukawa_line_field"
    if git("diff", "--quiet", FINAL_REPAIR_COMMIT, "HEAD", "--", scope, check=False).returncode:
        raise StrictDataError("a descendant commit changed C56")
    if git("diff", "--quiet", FINAL_REPAIR_COMMIT, "--", scope, check=False).returncode:
        raise StrictDataError("live/index C56 differs from final repair")

    committed = []
    for relative, (blob, expected_sha) in sorted(expected_files.items()):
        raw, fingerprint = read_stable(REPO / relative, max_bytes=2_000_000)
        if fingerprint.sha256 != expected_sha:
            raise StrictDataError(f"C56 live lock mismatch: {relative}")
        for commit in (IMPLEMENTATION_COMMIT, PROVENANCE_COMMIT, FINAL_REPAIR_COMMIT):
            tokens = git("ls-tree", commit, "--", relative).stdout.decode().strip().split()
            if len(tokens) != 4 or tokens[2] != blob or tokens[3] != relative:
                raise StrictDataError("C56 committed blob mismatch")
        committed.append(
            {
                "path": relative,
                "git_blob_id": blob,
                "sha256": expected_sha,
                "size_bytes": len(raw),
                "identical_at_all_three_frozen_commits": True,
            }
        )

    manifest_raw, _ = read_stable(C56 / "results/scoped_hash_manifest.json", max_bytes=100_000)
    manifest = strict_json_loads(manifest_raw, max_bytes=100_000)
    require_exact_keys(
        manifest,
        {"entries", "entry_count", "manifest_self_included", "schema", "scope", "status"},
        "C56 scoped manifest",
    )
    if (
        manifest["schema"] != "hcs-c56-scoped-hash-manifest-v1"
        or manifest["status"] != "PREFREEZE_CODE_RESULTS_PASS"
        or manifest["manifest_self_included"] is not False
        or manifest["entry_count"] != 12
        or len(manifest["entries"]) != 12
    ):
        raise StrictDataError("C56 scoped manifest header mismatch")
    declared = set()
    for entry in manifest["entries"]:
        require_exact_keys(entry, {"path", "sha256", "size_bytes"}, "C56 manifest entry")
        relative = entry["path"]
        if not safe_relative_path(relative) or relative in declared:
            raise StrictDataError("unsafe/duplicate C56 scoped path")
        declared.add(relative)
        raw, fingerprint = read_stable(C56 / relative, max_bytes=2_000_000)
        if len(raw) != entry["size_bytes"] or fingerprint.sha256 != entry["sha256"]:
            raise StrictDataError("C56 scoped entry digest mismatch")
    live = set()
    for root_name in ("code", "results"):
        for path in (C56 / root_name).rglob("*"):
            if path.is_symlink():
                raise StrictDataError("C56 scoped symlink forbidden")
            if path.is_dir():
                continue
            if not regular_file(path):
                raise StrictDataError("C56 scoped nonregular entry forbidden")
            live.add(path.relative_to(C56).as_posix())
    if live != declared | {"results/scoped_hash_manifest.json"}:
        raise StrictDataError("C56 scoped exact inventory mismatch")

    certificate_raw, _ = read_stable(C56_CERTIFICATE, max_bytes=2_000_000)
    c56_envelope = strict_json_loads(certificate_raw, max_bytes=2_000_000)
    if (
        c56_envelope.get("payload_sha256") != C56_PAYLOAD_SHA256
        or sha256_bytes(canonical_leaf_bytes(c56_envelope["payload"])) != C56_PAYLOAD_SHA256
    ):
        raise StrictDataError("C56 payload digest mismatch")
    # This is deliberately a different G0 call graph from the producer.  The
    # producer freshly executes the committed C56 checker; this checker instead
    # rebinds the already frozen report, certificate, route and exact manifest
    # bytes without invoking the C56 program again.
    committed_report, committed_fingerprint = read_stable(
        C56_CHECK_REPORT, max_bytes=10_000
    )
    if committed_fingerprint.sha256 != C56_CHECK_REPORT_SHA256:
        raise StrictDataError("C56 committed checker report bytes changed")
    report = strict_json_loads(committed_report, max_bytes=10_000)
    if (
        report.get("result") != "PASS_PREFREEZE_CODE_RESULTS"
        or report.get("semantic_gate_count") != 10
        or report.get("scalar_leaf_rebound", {}).get("rebound_mutations_rejected") != 2684
    ):
        raise StrictDataError("C56 checker semantic counts mismatch")

    route_relative = "henon_dynamics/henon_mu3_yukawa_line_field/route_a_evaluation.yaml"
    route_raw, route_fingerprint = read_stable(REPO / route_relative, max_bytes=100_000)
    if route_fingerprint.sha256 != "cc17a14a3565165de2249bc5219f209b6546ffd91b583e75ac07bbba7730ca73":
        raise StrictDataError("C56 final route bytes changed")
    route_blobs = []
    for commit, blob in (
        (IMPLEMENTATION_COMMIT, "993ce55e4b4b29d9c5470cf1c5a4dde90c3959e7"),
        (PROVENANCE_COMMIT, "fe569eb606451efb92bffcede93f3025070ed58d"),
        (FINAL_REPAIR_COMMIT, "cfdbc21b1613ade960570aec7eebd15c2da5ab8a"),
    ):
        tokens = git("ls-tree", commit, "--", route_relative).stdout.decode().strip().split()
        if len(tokens) != 4 or tokens[2] != blob:
            raise StrictDataError("C56 route blob chain mismatch")
        route_blobs.append({"commit": commit, "git_blob_id": blob})
    required_statuses = {
        "documentation_status: DOCS_FINAL_NO_MORE_EDITS",
        "code_results_status: PREFREEZE_CODE_RESULTS_PASS",
        "release_status: RELEASE_FROZEN",
    }
    if not required_statuses.issubset(set(route_raw.decode().splitlines())):
        raise StrictDataError("C56 route layered status mismatch")
    archive_relative = (
        "henon_dynamics/henon_mu3_yukawa_line_field/evaluations/route_a/"
        "HCS-C56/20260815T000000Z.yaml"
    )
    archive_raw, archive_fingerprint = read_stable(REPO / archive_relative, max_bytes=100_000)
    archive_tokens = git("ls-tree", FINAL_REPAIR_COMMIT, "--", archive_relative).stdout.decode().strip().split()
    if (
        archive_raw != route_raw
        or archive_fingerprint.sha256 != route_fingerprint.sha256
        or len(archive_tokens) != 4
        or archive_tokens[2] != "cfdbc21b1613ade960570aec7eebd15c2da5ab8a"
    ):
        raise StrictDataError("C56 archived route mismatch")
    return {
        "implementation_commit": IMPLEMENTATION_COMMIT,
        "provenance_commit": PROVENANCE_COMMIT,
        "final_repair_commit": FINAL_REPAIR_COMMIT,
        "ancestry": ancestry,
        "certificate_sha256": C56_CERTIFICATE_SHA256,
        "payload_sha256": C56_PAYLOAD_SHA256,
        "scoped_manifest_sha256": C56_SCOPED_MANIFEST_SHA256,
        "committed_checker_report_sha256": C56_CHECK_REPORT_SHA256,
        "committed_checker_report_status": report["result"],
        "committed_checker_semantic_gates": report["semantic_gate_count"],
        "committed_checker_rebound_mutations": report["scalar_leaf_rebound"]["rebound_mutations_rejected"],
        "committed_files": committed,
        "fresh_committed_checker_replayed_by_producer": True,
        "fresh_committed_checker_report_sha256": committed_fingerprint.sha256,
        "final_route": {
            "path": route_relative,
            "sha256": route_fingerprint.sha256,
            "size_bytes": len(route_raw),
            "provenance_blob_chain": route_blobs,
            "documentation_status": "DOCS_FINAL_NO_MORE_EDITS",
            "code_results_status": "PREFREEZE_CODE_RESULTS_PASS",
            "release_status": "RELEASE_FROZEN",
            "archived_copy_path": archive_relative,
            "archived_copy_byte_identical": True,
        },
        "current_HEAD_policy": "final repair is an ancestor and every imported C56 machine byte is independently rebound; later C57-only commits are permitted",
        "tracked_C56_subtree_unchanged_since_final_repair": True,
        "C56_code_and_results_exact_live_inventory_rebound": True,
        "C56_line_field_E_not_equal_splitting_field_K": True,
        "C56_line_field_E_non_Galois": True,
        "ordinary_S27_sign_argument_used": False,
    }


def rebuild_artifacts(result_dir: Path) -> dict[str, Any]:
    result = {}
    for name, expected in sorted(ARTIFACTS.items()):
        csize, csha, dsize, dsha, clim, dlim = expected
        path = result_dir / name
        if path.is_symlink() or not path.is_file():
            raise StrictDataError(f"missing/nonregular evidence artifact: {name}")
        value, raw, fingerprint = strict_gzip_json(
            path, max_compressed_bytes=clim, max_decompressed_bytes=dlim
        )
        if (
            fingerprint.size_bytes,
            fingerprint.sha256,
            len(raw),
            sha256_bytes(raw),
        ) != (csize, csha, dsize, dsha):
            raise StrictDataError(f"evidence source-lock mismatch: {name}")
        require_canonical_compact_json(raw)
        compressed, _ = read_stable(path, max_bytes=clim)
        if compressed != deterministic_gzip(raw):
            raise StrictDataError(f"nondeterministic gzip evidence: {name}")
        result[name] = {
            "path": f"results/{name}",
            "compressed_size_bytes": csize,
            "compressed_sha256": csha,
            "decompressed_size_bytes": dsize,
            "decompressed_sha256": dsha,
            "gzip_mtime": 0,
            "semantic_replay_required": True,
        }
    return result


def normalized_backends(pari_python: Path, flint_python: Path, singular: Path):
    python = python_preflight(pari_python, flint_python)
    singular_value = singular_preflight(singular)
    return {
        "PARI": {
            "path_contract": "USR_BIN_PYTHON3",
            "executable_sha256": python["pari"]["executable_sha256"],
            "executable_size_bytes": python["pari"]["executable_size_bytes"],
            "versions": python["pari"]["versions"],
        },
        "FLINT_SYMPY": {
            "path_contract": "MINICONDA3_BIN_PYTHON3",
            "executable_sha256": python["flint_group"]["executable_sha256"],
            "executable_size_bytes": python["flint_group"]["executable_size_bytes"],
            "versions": python["flint_group"]["versions"],
        },
        "SINGULAR": {
            "path_contract": "USR_BIN_SINGULAR",
            **{key: value for key, value in singular_value.items() if key != "resolved_executable"},
        },
    }


def run_inline_json_backend(
    python: Path,
    source: str,
    request: dict[str, Any],
    *,
    timeout: int,
    max_stdout_bytes: int = 5_000_000,
) -> dict[str, Any]:
    """Run checker-owned source under a locked backend and parse one JSON line."""
    resolved_python = python.resolve(strict=True)
    completed = subprocess.run(
        [str(resolved_python), "-s", "-B", "-c", source],
        input=canonical_leaf_bytes(request),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=clean_environment(),
        # A fixed root cwd contains no project sources; unlike -I, this
        # preserves the locked PYTHONHASHSEED=0.
        cwd="/",
        check=True,
        timeout=timeout,
    )
    if completed.stderr:
        raise StrictDataError("independent backend emitted stderr")
    if len(completed.stdout) > max_stdout_bytes:
        raise StrictDataError("independent backend stdout exceeds limit")
    if not completed.stdout.endswith(b"\n") or completed.stdout.count(b"\n") != 1:
        raise StrictDataError("independent backend must emit exactly one JSON line")
    raw = completed.stdout[:-1]
    value = strict_json_loads(raw, max_bytes=max_stdout_bytes)
    if type(value) is not dict or raw != canonical_leaf_bytes(value):
        raise StrictDataError("independent backend JSON is not canonical")
    return value


PARI_PRIME_FACTOR_SOURCE = r'''
import json,sys
sys.set_int_max_str_digits(0)
from cypari2 import Pari
data=json.loads(sys.stdin.buffer.read())
p=Pari()
prime_flags=[int(p.isprime(value))==1 for value in data["primes"]]
factor_records=[]
for coefficients in data["polynomials"]:
    poly=p.Polrev(coefficients)
    per_poly=[]
    for modulus in data["factor_primes"]:
        rows=p.factormod(poly,modulus)
        factors=[]
        for row in range(int(rows.nrows())):
            factor=rows[row,0]
            multiplicity=int(rows[row,1])
            values=[int(p.lift(value))%modulus for value in reversed(list(p.Vec(factor)))]
            factors.append({"coefficients":values,"irreducible":int(p.polisirreducible(factor))==1,"multiplicity":multiplicity})
        per_poly.append({"prime":modulus,"factors":factors})
    factor_records.append(per_poly)
out={"all_primes_proven":all(prime_flags),"prime_flags":prime_flags,"factor_records":factor_records}
print(json.dumps(out,sort_keys=True,separators=(",",":")))
'''


PARI_RESOLVER_PRODUCTS_SOURCE = r'''
import itertools,json,math,sys
sys.set_int_max_str_digits(0)
from cypari2 import Pari
data=json.loads(sys.stdin.buffer.read()); pari=Pari(); z=pari("z")
shape={row["leading_variable"]:row for row in data["lex_shape"]}; g_coefficients=shape["d"]["tail_coefficients_d_0_up"]
theta_primes=set(data["theta_primes"]); delta_primes=set(data["delta_primes"])
def horner(coefficients,value):
    result=value*0
    for coefficient in reversed(coefficients): result=result*value+coefficient
    return result
def line_restriction(surface,line):
    a,b,c,d=(line[key] for key in ("a","b","c","d")); zero=d*0; result=[zero]*4
    for row in surface:
        coefficient=row["coefficient"]; e0,e1,e2,e3=row["exponents_u0_to_u3"]
        for i in range(e2+1):
            left=math.comb(e2,i)*a**(e2-i)*c**i
            for j in range(e3+1): result[e1+i+j]+=coefficient*left*math.comb(e3,j)*b**(e3-j)*d**j
    return result
def orbit_product(values,generator,prime):
    coefficients=[generator**0]
    for root in values:
        updated=[generator*0]*(len(coefficients)+1)
        for i,coefficient in enumerate(coefficients):
            updated[i]-=root*coefficient; updated[i+1]+=coefficient
        coefficients=updated
    lifted=[]
    for coefficient in coefficients:
        value=pari.lift(coefficient)
        if value!=0 and int(pari.poldegree(value))>0: raise ValueError("orbit product did not descend")
        lifted.append(0 if value==0 else int(str(value))%prime)
    return lifted
checked_theta=0; checked_delta=0; processed=0
for prime in sorted(theta_primes|delta_primes):
    if int(pari.isprime(prime))!=1 or prime<=3: raise ValueError("unproven prime")
    if g_coefficients[-1]%prime==0: raise ValueError("g degree drop")
    factor_degrees=pari.factormod(pari.Polrev(g_coefficients),prime,1).python(); extension=1
    for degree,multiplicity in factor_degrees:
        if int(multiplicity)!=1: raise ValueError("inseparable g")
        extension=math.lcm(extension,int(degree))
    generator=pari.ffgen(pari.ffinit(prime,extension,z),z)
    roots=list(pari.polrootsmod(pari.Polrev(g_coefficients),generator))
    if len(roots)!=27 or not all(roots[i]!=roots[j] for i,j in itertools.combinations(range(27),2)): raise ValueError("wrong roots")
    lines=[]
    for d in roots:
        line={"d":d}
        for variable in ("a","b","c"):
            row=shape[variable]; denominator=row["leading_coefficient"]%prime
            if denominator==0: raise ValueError("shape denominator")
            line[variable]=-horner(row["tail_coefficients_d_0_up"],d)/denominator
        lines.append(line)
    zero=roots[0]*0
    if any(line_restriction(data["surface"],line)!=[zero]*4 for line in lines): raise ValueError("line restriction")
    meeting=set()
    for i,j in itertools.combinations(range(27),2):
        left,right=lines[i],lines[j]
        if (left["a"]-right["a"])*(left["d"]-right["d"])-(left["b"]-right["b"])*(left["c"]-right["c"])==0: meeting.add(frozenset((i,j)))
    if len(meeting)!=135: raise ValueError("meeting count")
    sixers=[frozenset(subset) for subset in itertools.combinations(range(27),6) if all(frozenset((i,j)) not in meeting for i,j in itertools.combinations(subset,2))]
    if len(sixers)!=72: raise ValueError("sixer count")
    doubles=set()
    for first in sixers:
        second=frozenset(i for i in range(27) if i not in first and sum(frozenset((i,j)) in meeting for j in first)==5)
        if len(second)!=6: raise ValueError("double-six complement")
        doubles.add(frozenset((first,second)))
    if len(doubles)!=36: raise ValueError("double-six count")
    scale=g_coefficients[-1]
    theta_values=[sum((scale*roots[i] for i in set().union(*double)),zero) for double in doubles]
    delta_values=[]
    for double in doubles:
        first,second=tuple(double)
        beta=sum((scale*roots[i] for i in first),zero)-sum((scale*roots[i] for i in second),zero)
        delta_values.append(beta**2)
    if not all(theta_values[i]!=theta_values[j] for i,j in itertools.combinations(range(36),2)): raise ValueError("theta collision")
    if not all(delta_values[i]!=delta_values[j] for i,j in itertools.combinations(range(36),2)): raise ValueError("delta collision")
    if prime in theta_primes:
        observed=orbit_product(theta_values,generator,prime)
        if observed!=[value%prime for value in data["theta_coefficients"]]: raise ValueError("theta orbit product mismatch")
        checked_theta+=1
    if prime in delta_primes:
        observed=orbit_product(delta_values,generator,prime)
        if observed!=[value%prime for value in data["delta_coefficients"]]: raise ValueError("delta orbit product mismatch")
        checked_delta+=1
    processed+=1
print(json.dumps({"all_line_restrictions_zero":True,"all_orbit_products_match_final_coefficients_mod_p":True,"delta_products_checked":checked_delta,"theta_products_checked":checked_theta,"unique_primes_processed":processed},sort_keys=True,separators=(",",":")))
'''


def multiply_mod(left: list[int], right: list[int], prime: int) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] = (result[i + j] + a * b) % prime
    return result


def proper_subset_degrees(degrees: list[int]) -> set[int]:
    return {
        sum(subset)
        for count in range(1, len(degrees))
        for subset in itertools.combinations(degrees, count)
    }


def independent_resolver_replay(result_dir: Path, pari_python: Path) -> dict[str, Any]:
    """Second-lane resolver audit: transcript, heights, primes, full factors."""
    c56_raw, _ = read_stable(C56_CERTIFICATE, max_bytes=2_000_000)
    c56 = strict_json_loads(c56_raw, max_bytes=2_000_000)
    rows = {
        row["leading_variable"]: row
        for row in c56["payload"]["grassmann_main_chart"]["lex_shape"]
    }
    g = rows["d"]["tail_coefficients_d_0_up"]
    alpha_bound = abs(g[-1]) + max(abs(value) for value in g[:-1])
    transcript_values: dict[str, dict[str, Any]] = {}
    all_primes: list[int] = []
    expected = {
        "theta": {
            "file": "theta_crt.json.gz",
            "schema": "hcs-c57-theta-crt-v1",
            "method": "EXACT_FINITE_FIELD_DOUBLE_SIX_ORBIT_PRODUCTS_PLUS_CRT",
            "prime_count": 99,
            "coefficient_sha": "845a0cd703b3d5d7c8814f7339010601cc2a25293b6b1bfe792aff2c728e23ea",
            "source": "4b0e5e899b4d431765000ed76e46405b0e54e960a684b3250bfec12ffdefd2dd",
        },
        "delta": {
            "file": "delta_crt.json.gz",
            "schema": "hcs-c57-delta-crt-v1",
            "method": "EXACT_FINITE_FIELD_ORBIT_PRODUCTS_PLUS_CRT",
            "prime_count": 198,
            "coefficient_sha": "d0d90e4513feab467abbf948e39296f4a6cf01569890a55081494258058fecfb",
            "source": "9890dd6400a65684639e9f7c06933bac0425ff69e359f898254ab16df06e859c",
        },
    }
    for kind in ("theta", "delta"):
        value, _, _ = strict_gzip_json(
            result_dir / expected[kind]["file"],
            max_compressed_bytes=1_000_000,
            max_decompressed_bytes=1_000_000,
        )
        if (
            value.get("schema_id") != expected[kind]["schema"]
            or value.get("method") != expected[kind]["method"]
            or value.get("original_source_sha256") != expected[kind]["source"]
            or value.get("candidate_input_used") is not False
            or value.get("degree") != 36
            or value.get("prime_count") != expected[kind]["prime_count"]
            or len(value.get("coefficients", [])) != 37
            or value["coefficients"][-1] != 1
            or math.gcd(*value["coefficients"]) != 1
        ):
            raise StrictDataError(f"independent {kind} resolver transcript header failed")
        if sha256_bytes(canonical_leaf_bytes(value["coefficients"])) != expected[kind]["coefficient_sha"]:
            raise StrictDataError(f"independent {kind} coefficient digest failed")
        if sha256_bytes(canonical_leaf_bytes(value["primes"])) != value["primes_sha256"]:
            raise StrictDataError(f"independent {kind} prime-list digest failed")
        if len(value["primes"]) != len(set(value["primes"])):
            raise StrictDataError(f"independent {kind} primes are not distinct")
        records = value["records"] if kind == "theta" else value["prime_records"]
        if len(records) != len(value["primes"]):
            raise StrictDataError(f"independent {kind} record count failed")
        for prime, record in zip(value["primes"], records):
            if record.get("prime") != prime:
                raise StrictDataError(f"independent {kind} record/prime alignment failed")
            for key, expected_value in {
                "proven_prime": True,
                "g_squarefree": True,
                "shape_denominators_nonzero": True,
                "line_carrier_good_specialization": True,
                "meeting_count": 135,
                "sixer_count": 72,
                "double_six_count": 36,
            }.items():
                if not deep_exact(record.get(key), expected_value):
                    raise StrictDataError(f"independent {kind} modular record failed: {key}")
            if kind == "delta" and (
                record.get("orientation_square_distinct_values") != 36
                or sum(degree * multiplicity for degree, multiplicity in record["factor_degrees"]) != 27
            ):
                raise StrictDataError("independent delta modular record shape failed")
        modulus = math.prod(value["primes"])
        if modulus != value["modulus"]:
            raise StrictDataError(f"independent {kind} prime product/modulus failed")
        root_bound = 12 * alpha_bound if kind == "theta" else (12 * alpha_bound) ** 2
        coefficient_bounds = [
            math.comb(36, 36 - power) * root_bound ** (36 - power)
            for power in range(37)
        ]
        if max(coefficient_bounds) != value["uniform_coefficient_bound"]:
            raise StrictDataError(f"independent {kind} height bound failed")
        if not (modulus > 2 * max(coefficient_bounds)):
            raise StrictDataError(f"independent {kind} CRT uniqueness failed")
        if any(
            abs(coefficient) > coefficient_bounds[index]
            for index, coefficient in enumerate(value["coefficients"])
        ):
            raise StrictDataError(f"independent {kind} coefficient height failed")
        if kind == "theta" and value.get("theta_bound") != root_bound:
            raise StrictDataError("independent theta root bound failed")
        if kind == "delta" and (
            value.get("alpha_bound") != alpha_bound
            or value.get("delta_bound") != root_bound
            or value.get("all_primes_proven_prime") is not True
            or value.get("all_line_carrier_specializations_good") is not True
        ):
            raise StrictDataError("independent delta bound/header failed")
        transcript_values[kind] = value
        all_primes.extend(value["primes"])

    products = run_inline_json_backend(
        pari_python,
        PARI_RESOLVER_PRODUCTS_SOURCE,
        {
            "lex_shape": c56["payload"]["grassmann_main_chart"]["lex_shape"],
            "surface": c56["payload"]["surface"]["primitive_coefficients"],
            "theta_primes": transcript_values["theta"]["primes"],
            "delta_primes": transcript_values["delta"]["primes"],
            "theta_coefficients": transcript_values["theta"]["coefficients"],
            "delta_coefficients": transcript_values["delta"]["coefficients"],
        },
        timeout=3_600,
    )
    expected_unique_primes = len(
        set(transcript_values["theta"]["primes"])
        | set(transcript_values["delta"]["primes"])
    )
    if not deep_exact(
        products,
        {
            "all_line_restrictions_zero": True,
            "all_orbit_products_match_final_coefficients_mod_p": True,
            "delta_products_checked": 198,
            "theta_products_checked": 99,
            "unique_primes_processed": expected_unique_primes,
        },
    ):
        raise StrictDataError("independent all-prime resolver orbit-product replay failed")

    factor_primes = [
        100000000000000000000000000000000000000000000012537,
        100000000000000000000000000000000000000000000014181,
    ]
    pari = run_inline_json_backend(
        pari_python,
        PARI_PRIME_FACTOR_SOURCE,
        {
            "primes": all_primes + factor_primes,
            "polynomials": [
                transcript_values["theta"]["coefficients"],
                transcript_values["delta"]["coefficients"],
            ],
            "factor_primes": factor_primes,
        },
        timeout=900,
    )
    if pari.get("all_primes_proven") is not True or pari.get("prime_flags") != [True] * (len(all_primes) + 2):
        raise StrictDataError("independent PARI primality replay failed")
    for polynomial_index, kind in enumerate(("theta", "delta")):
        coefficient_modulus = transcript_values[kind]["coefficients"]
        subset_sets = []
        patterns = []
        for record in pari["factor_records"][polynomial_index]:
            prime = record["prime"]
            product = [1]
            degrees = []
            for factor in record["factors"]:
                coefficients = factor["coefficients"]
                if (
                    factor["multiplicity"] != 1
                    or factor["irreducible"] is not True
                    or coefficients[-1] != 1
                ):
                    raise StrictDataError("independent PARI full factor gate failed")
                degrees.append(len(coefficients) - 1)
                product = multiply_mod(product, coefficients, prime)
            if product != [value % prime for value in coefficient_modulus]:
                raise StrictDataError("independent PARI factor multiply-back failed")
            patterns.append(degrees)
            subset_sets.append(proper_subset_degrees(degrees))
        if patterns != [[1, 5, 5, 5, 10, 10], [9, 9, 9, 9]] or subset_sets[0] & subset_sets[1]:
            raise StrictDataError(f"independent {kind} irreducibility subset gate failed")
    return {
        "theta_prime_count": 99,
        "theta_modulus_digits": len(str(transcript_values["theta"]["modulus"])),
        "theta_coefficients_sha256": expected["theta"]["coefficient_sha"],
        "delta_prime_count": 198,
        "delta_modulus_digits": len(str(transcript_values["delta"]["modulus"])),
        "delta_required_height_digits": len(str(2 * transcript_values["delta"]["uniform_coefficient_bound"])),
        "delta_coefficients_sha256": expected["delta"]["coefficient_sha"],
        "factor_patterns": [[1, 5, 5, 5, 10, 10], [9, 9, 9, 9]],
        "proper_factor_degree_intersection": [],
        "all_primes_proven": True,
        "all_297_orbit_product_congruences_replayed": True,
    }


def qpoly_from_fraction_pairs(row: list[list[int]]) -> fmpq_poly:
    return fmpq_poly([fmpq(pair[0], pair[1]) for pair in row])


def canonical_field_vector(value: fmpq_poly, degree: int) -> list[list[int]]:
    coefficients = list(value.coeffs())
    coefficients.extend([Fraction(0)] * (degree - len(coefficients)))
    if len(coefficients) != degree:
        raise StrictDataError("field element did not reduce below theta degree")
    result = []
    for coefficient in coefficients:
        # python-flint fmpq exposes p/q; Fraction exposes numerator/denominator.
        if hasattr(coefficient, "p"):
            result.append([int(coefficient.p), int(coefficient.q)])
        else:
            fraction = Fraction(coefficient)
            result.append([fraction.numerator, fraction.denominator])
    return result


def independent_carrier_replay(result_dir: Path, pari_python: Path) -> dict[str, Any]:
    """Checker-owned rational reconstruction and Q(theta) factor identity."""
    candidate, _, _ = strict_gzip_json(
        result_dir / "a12_table.json.gz",
        max_compressed_bytes=40_000_000,
        max_decompressed_bytes=40_000_000,
    )
    transcript, _, _ = strict_gzip_json(
        result_dir / "a12_crt_transcript.json.gz",
        max_compressed_bytes=25_000_000,
        max_decompressed_bytes=50_000_000,
    )
    theta, _, _ = strict_gzip_json(
        result_dir / "theta_crt.json.gz",
        max_compressed_bytes=1_000_000,
        max_decompressed_bytes=1_000_000,
    )
    candidate_keys = {
        "all_congruences_replayed",
        "all_denominators_units_mod_modulus",
        "all_entries_nonempty",
        "all_entries_within_symmetric_bound",
        "coefficient_table_fractions",
        "coefficient_table_sha256",
        "max_denominator_digits",
        "max_numerator_digits",
        "method",
        "modulus_digits",
        "original_source_sha256",
        "parameter",
        "prime_count",
        "reconstruction_bound_digits",
        "schema_id",
        "state_sha256",
        "table_kind",
    }
    transcript_keys = {
        "accepted_primes",
        "candidate_input_used",
        "collector_source_sha256",
        "failures",
        "method",
        "modular_generator_source_sha256",
        "modulus",
        "next_candidate",
        "original_trusted_pickle_sha256",
        "parameter",
        "prime_count",
        "prior_hash",
        "residues",
        "schema_id",
        "source_acceptance_contract",
        "stability_counter",
        "table_kind",
    }
    require_exact_keys(candidate, candidate_keys, "independent A12 table")
    require_exact_keys(transcript, transcript_keys, "independent A12 transcript")
    if (
        candidate["schema_id"] != "hcs-c57-a12-table-v1"
        or candidate["method"]
        != "PARI_BESTAPPR_FROM_EXACT_MODULAR_CRT_THEN_EXACT_IDENTITY_REQUIRED"
        or candidate["original_source_sha256"]
        != "810ca69f08dae07b2978f6cc9d441638e6c79a8bcfd6a771c4a895f6b0d1b17d"
        or transcript["schema_id"] != "hcs-c57-a12-crt-transcript-v1"
        or transcript["method"]
        != "CANDIDATE_BLIND_FINITE_FIELD_CARRIER_TABLE_PLUS_CRT"
        or transcript["candidate_input_used"] is not False
        or transcript["failures"] != []
        or transcript["prior_hash"] is not None
        or transcript["stability_counter"] != 0
        or candidate["parameter"] != transcript["parameter"]
        or candidate["parameter"] != "theta"
        or candidate["table_kind"] != transcript["table_kind"]
        or candidate["table_kind"] != "carrier"
        or candidate["state_sha256"] != transcript["original_trusted_pickle_sha256"]
        or transcript["modular_generator_source_sha256"]
        != "8832df1e0041b41b84e872fb717895f11da55f80247d112918ab07de08eea99d"
        or transcript["collector_source_sha256"]
        != "b2f0a12c0ffb0431e93e6e3f35cfa51d2f8638bf6417ae0c508163a8b7f79282"
    ):
        raise StrictDataError("independent A12 lineage/method gate failed")
    primes = transcript["accepted_primes"]
    if (
        len(primes) != 1048
        or len(primes) != transcript["prime_count"]
        or len(primes) != candidate["prime_count"]
        or primes != sorted(set(primes))
        or transcript["next_candidate"] <= primes[-1]
    ):
        raise StrictDataError("independent A12 prime sequence failed")
    primality = run_inline_json_backend(
        pari_python,
        PARI_PRIME_FACTOR_SOURCE,
        {"primes": primes, "polynomials": [], "factor_primes": []},
        timeout=900,
    )
    if primality.get("all_primes_proven") is not True or primality.get("prime_flags") != [True] * 1048:
        raise StrictDataError("independent A12 primality replay failed")
    modulus = math.prod(primes)
    if modulus != transcript["modulus"] or len(str(modulus)) != 100609:
        raise StrictDataError("independent A12 modulus replay failed")
    bound = math.isqrt(modulus // 2)
    if len(str(bound)) != candidate["reconstruction_bound_digits"]:
        raise StrictDataError("independent A12 rational bound failed")
    residues = transcript["residues"]
    table = candidate["coefficient_table_fractions"]
    if (
        len(residues) != 13
        or len(table) != 13
        or any(len(row) != 36 for row in residues)
        or any(len(row) != 36 for row in table)
    ):
        raise StrictDataError("independent A12 table shape failed")
    max_num_digits = 0
    max_den_digits = 0
    for residue_row, table_row in zip(residues, table):
        for residue, pair in zip(residue_row, table_row):
            if type(residue) is not int or type(pair) is not list or len(pair) != 2:
                raise StrictDataError("independent A12 cell type failed")
            numerator, denominator = pair
            if type(numerator) is not int or type(denominator) is not int:
                raise StrictDataError("independent A12 rational type failed")
            if not (abs(numerator) < bound and 0 < denominator < bound):
                raise StrictDataError("independent A12 height gate failed")
            if math.gcd(denominator, modulus) != 1:
                raise StrictDataError("independent A12 denominator unit gate failed")
            if (residue * denominator - numerator) % modulus:
                raise StrictDataError("independent A12 congruence failed")
            max_num_digits = max(max_num_digits, len(str(abs(numerator))))
            max_den_digits = max(max_den_digits, len(str(denominator)))
    table_sha = sha256_bytes(canonical_leaf_bytes(table))
    if (
        table_sha != "72d4aef5120926ec09904b08219cba7cf2b49323bd085d05274e5c17e1ed90a1"
        or table_sha != candidate["coefficient_table_sha256"]
        or max_num_digits != candidate["max_numerator_digits"]
        or max_den_digits != candidate["max_denominator_digits"]
    ):
        raise StrictDataError("independent A12 canonical table gate failed")

    theta_coefficients = theta["coefficients"]
    theta_sha = sha256_bytes(canonical_leaf_bytes(theta_coefficients))
    if theta_sha != "845a0cd703b3d5d7c8814f7339010601cc2a25293b6b1bfe792aff2c728e23ea":
        raise StrictDataError("independent A12 theta modulus digest failed")
    theta_modulus = fmpq_poly(theta_coefficients)
    c56_raw, _ = read_stable(C56_CERTIFICATE, max_bytes=2_000_000)
    c56 = strict_json_loads(c56_raw, max_bytes=2_000_000)
    g_coefficients = next(
        row["tail_coefficients_d_0_up"]
        for row in c56["payload"]["grassmann_main_chart"]["lex_shape"]
        if row["leading_variable"] == "d"
    )
    scale = g_coefficients[-1]
    carrier = [qpoly_from_fraction_pairs(row) % theta_modulus for row in table]
    zero = fmpq_poly()
    one = fmpq_poly([1])
    theta_element = fmpq_poly([0, 1])
    if carrier[-1] != one or carrier[-2] != (-theta_element / scale):
        raise StrictDataError("independent A12 monic/subtop gate failed")

    # Derive B15 by a checker-owned top-down recurrence, reducing after every
    # multiplication.  Then perform a fresh B*A convolution in the opposite
    # nesting order from the producer implementation.
    target = [fmpq_poly([fmpq(value, scale)]) for value in g_coefficients]
    residual = list(target)
    complement = [zero for _ in range(16)]
    division_count = 0
    for quotient_degree in range(15, -1, -1):
        top = quotient_degree + 12
        coefficient = residual[top]
        complement[quotient_degree] = coefficient
        for carrier_degree in range(12, -1, -1):
            residual[quotient_degree + carrier_degree] -= (
                coefficient * carrier[carrier_degree]
            ) % theta_modulus
            residual[quotient_degree + carrier_degree] %= theta_modulus
            division_count += 1
        if residual[top] != zero:
            raise StrictDataError("independent A12 division top failed")
    if any(value != zero for value in residual) or complement[-1] != one:
        raise StrictDataError("independent A12 remainder/complement failed")
    product = [zero for _ in range(28)]
    forward_count = 0
    for right_degree, right in enumerate(complement):
        for left_degree, left in enumerate(carrier):
            product[left_degree + right_degree] += (right * left) % theta_modulus
            product[left_degree + right_degree] %= theta_modulus
            forward_count += 1
    if product != target:
        raise StrictDataError("independent A12 forward convolution failed")
    complement_table = [canonical_field_vector(value, 36) for value in complement]
    complement_sha = sha256_bytes(canonical_leaf_bytes(complement_table))
    if complement_sha != "b922484d59786a850fc8d13283366e2536c21eae56c5aaae1908b91bc7edbc0f":
        raise StrictDataError("independent A12 complement digest failed")
    return {
        "carrier_table_sha256": table_sha,
        "prime_count": 1048,
        "modulus_digits": 100609,
        "all_468_congruences_bounds_units": True,
        "carrier_degree": 12,
        "complement_degree": 15,
        "division_field_multiplication_count": division_count,
        "forward_convolution_field_multiplication_count": forward_count,
        "all_28_coefficients_exact": True,
        "complement_table_sha256": complement_sha,
    }


PARI_INDEPENDENT_INCIDENCE_SOURCE = r'''
import hashlib,itertools,json,math,re,sys
sys.set_int_max_str_digits(0)
from cypari2 import Pari
request=json.loads(sys.stdin.buffer.read())
shape={row["leading_variable"]:row for row in request["lex_shape"]}
g_coefficients=shape["d"]["tail_coefficients_d_0_up"]
term_re=re.compile(r"([+-]?)([0-9]+)(?:/([0-9]+))?(?:x([0-9]+)?)?")
def parse_x(source):
    position=0; terms={}
    while position<len(source):
        match=term_re.match(source,position)
        if match is None: raise ValueError("bad H x coefficient")
        sign,num,den,exp=match.groups(); token=match.group(0)
        numerator=int(num)*(-1 if sign=="-" else 1); denominator=int(den or "1")
        exponent=int(exp or "1") if "x" in token else 0
        if denominator==0 or exponent in terms or exponent>26: raise ValueError("bad H term")
        terms[exponent]=(numerator,denominator); position=match.end()
    if not terms: raise ValueError("empty H coefficient")
    return [terms.get(i,(0,1)) for i in range(max(terms)+1)]
def parse_poly(text,top_degree):
    prefix="y"+str(top_degree)+"+"
    if not text.endswith("\n") or not text.startswith(prefix): raise ValueError("bad polynomial shell")
    source=text[:-1]; position=len(prefix); rows={top_degree:[(1,1)]}
    for degree in range(top_degree-1,0,-1):
        marker=")*"+("y" if degree==1 else "y"+str(degree))+"+"
        if source[position]!="(": raise ValueError("bad H open")
        end=source.find(marker,position)
        if end<0: raise ValueError("bad H delimiter")
        rows[degree]=parse_x(source[position+1:end]); position=end+len(marker)
    if source[position]!="(" or not source.endswith(")"): raise ValueError("bad H constant")
    rows[0]=parse_x(source[position+1:-1])
    return [rows[i] for i in range(top_degree+1)]
h=parse_poly(request["H_text"],10)
q=parse_poly(request["Q_text"],17)
if len(h)!=11 or len(q)!=18: raise ValueError("H/Q degrees")
def horner(values,x):
    total=x*0
    for value in reversed(values): total=total*x+value
    return total
def quotient_at(values,x):
    result=[x*0]*(len(values)-1); result[-1]=values[-1]
    for i in range(len(result)-2,-1,-1): result[i]=values[i+1]+x*result[i+1]
    return result
def add(a,b):
    zero=(a or b)[0]*0; result=[zero]*max(len(a),len(b))
    for i,v in enumerate(a): result[i]+=v
    for i,v in enumerate(b): result[i]+=v
    return result
def scale(a,s): return [s*v for v in a]
def multiply(a,b):
    result=[a[0]*0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): result[i+j]+=x*y
    return result
def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()
pari=Pari(); T=pari("T"); z=pari("z"); results=[]
for prime in request["primes"]:
    if int(pari.isprime(prime))!=1: raise ValueError("unproven prime")
    if g_coefficients[-1]%prime==0: raise ValueError("g degree dropped")
    if any(shape[name]["leading_coefficient"]%prime==0 for name in ("a","b","c")): raise ValueError("shape denominator")
    factors=pari.factormod(pari.Polrev(g_coefficients),prime,1).python()
    if any(int(m)!=1 for d,m in factors): raise ValueError("g not squarefree")
    extension=1
    for degree,multiplicity in factors: extension=math.lcm(extension,int(degree))
    generator=pari.ffgen(pari.ffinit(prime,extension,z),z)
    roots=list(pari.polrootsmod(pari.Polrev(g_coefficients),generator))
    if len(roots)!=27 or not all(roots[i]!=roots[j] for i,j in itertools.combinations(range(27),2)): raise ValueError("wrong roots")
    parameters=[]
    for root in roots:
        row={"d":root}
        for name in ("a","b","c"):
            row[name]=-horner(shape[name]["tail_coefficients_d_0_up"],root)/(shape[name]["leading_coefficient"]%prime)
        parameters.append(row)
    determinant_edges=set(); j_edges=set()
    for i,j in itertools.combinations(range(27),2):
        left,right=parameters[i],parameters[j]
        det=(right["a"]-left["a"])*(right["d"]-left["d"])-(right["b"]-left["b"])*(right["c"]-left["c"])
        if det==0: determinant_edges.add((i,j))
        x,y=roots[i],roots[j]
        da=(horner(shape["a"]["tail_coefficients_d_0_up"],y)-horner(shape["a"]["tail_coefficients_d_0_up"],x))/(y-x)
        db=(horner(shape["b"]["tail_coefficients_d_0_up"],y)-horner(shape["b"]["tail_coefficients_d_0_up"],x))/(y-x)
        dc=(horner(shape["c"]["tail_coefficients_d_0_up"],y)-horner(shape["c"]["tail_coefficients_d_0_up"],x))/(y-x)
        value=-da*(shape["b"]["leading_coefficient"]%prime)*(shape["c"]["leading_coefficient"]%prime)-db*dc*(shape["a"]["leading_coefficient"]%prime)
        if value==0: j_edges.add((i,j))
    if determinant_edges!=j_edges: raise ValueError("det/J mismatch")
    gff=pari.Polrev([generator*0+c for c in g_coefficients],T)
    gcd_degrees=[]; h_equal=[]; diagonal=[]; denominator_units=True
    for i,x in enumerate(roots):
        da=quotient_at(shape["a"]["tail_coefficients_d_0_up"],x)
        db=quotient_at(shape["b"]["tail_coefficients_d_0_up"],x)
        dc=quotient_at(shape["c"]["tail_coefficients_d_0_up"],x)
        jc=add(scale(da,-(shape["b"]["leading_coefficient"]%prime)*(shape["c"]["leading_coefficient"]%prime)),scale(multiply(db,dc),-(shape["a"]["leading_coefficient"]%prime)))
        gcd=pari.gcd(gff,pari.Polrev(jc,T)); gcd_degrees.append(int(pari.poldegree(gcd))); gcd/=pari.pollead(gcd)
        hc=[]
        for x_terms in h:
            reduced=[]
            for numerator,denominator in x_terms:
                if denominator%prime==0: denominator_units=False; raise ValueError("H denominator")
                reduced.append(numerator%prime*pow(denominator%prime,-1,prime)%prime)
            hc.append(horner(reduced,x))
        hp=pari.Polrev(hc,T); h_equal.append(hp==gcd); diagonal.append(pari.subst(gcd,T,x)!=0)
    degrees=[0]*27
    for i,j in j_edges: degrees[i]+=1; degrees[j]+=1
    if len(j_edges)!=135 or degrees!=[10]*27 or gcd_degrees!=[10]*27 or h_equal!=[True]*27 or diagonal!=[True]*27: raise ValueError("incidence/gcd gate")
    meeting={frozenset(edge) for edge in j_edges}
    sixers=[frozenset(s) for s in itertools.combinations(range(27),6) if all(frozenset((i,j)) not in meeting for i,j in itertools.combinations(s,2))]
    doubles=set()
    for first in sixers:
        second=frozenset(i for i in range(27) if i not in first and sum(frozenset((i,j)) in meeting for j in first)==5)
        if len(second)!=6: raise ValueError("double-six complement")
        doubles.add(frozenset((first,second)))
    if len(sixers)!=72 or len(doubles)!=36: raise ValueError("configuration counts")
    zero=roots[0]*0; scale_alpha=g_coefficients[-1]
    oriented=[sum((scale_alpha*roots[i] for i in sixer),zero) for sixer in sixers]
    deltas=[]
    for double in doubles:
        first,second=tuple(double)
        beta=sum((scale_alpha*roots[i] for i in first),zero)-sum((scale_alpha*roots[i] for i in second),zero)
        deltas.append(beta*beta)
    oriented_unique=[]
    for value in oriented:
        if all(value!=prior for prior in oriented_unique): oriented_unique.append(value)
    delta_distinct=all(deltas[i]!=deltas[j] for i,j in itertools.combinations(range(36),2))
    results.append({"prime":prime,"prime_proven":True,"eliminant_leading_coefficient_nonzero":True,"all_shape_denominators_units":True,"g_squarefree_27_roots":True,"all_H_coefficient_denominators_units":denominator_units,"determinant_formula_equals_J":True,"H_mod_p_equals_monic_gcd_all_27":all(h_equal),"gcd_degrees":gcd_degrees,"line_degrees":degrees,"meeting_count":len(j_edges),"sixer_count":len(sixers),"double_six_count":len(doubles),"oriented_sixer_distinct_values":len(oriented_unique),"double_six_delta_distinct_values":36 if delta_distinct else 0,"all_36_beta_nonzero":all(value!=0 for value in deltas),"meeting_graph_sha256":digest(sorted(j_edges))})
print(json.dumps({"reports":results},sort_keys=True,separators=(",",":")))
'''


CHAR0_TERM = re.compile(r"([+-]?)([0-9]+)/([0-9]+)(?:x([0-9]*))?")


def parse_char0_x_coefficient(source: str) -> fmpq_poly:
    terms: dict[int, fmpq] = {}
    cursor = 0
    while cursor < len(source):
        match = CHAR0_TERM.match(source, cursor)
        if match is None:
            raise StrictDataError("independent char0 parser rejected x coefficient")
        sign, numerator, denominator, exponent = match.groups()
        degree = 0 if exponent is None else (1 if exponent == "" else int(exponent))
        if degree in terms:
            raise StrictDataError("independent char0 parser found duplicate x degree")
        value = fmpq(int(numerator), int(denominator))
        terms[degree] = -value if sign == "-" else value
        cursor = match.end()
    if not terms:
        return fmpq_poly()
    coefficients = [fmpq(0)] * (max(terms) + 1)
    for degree, value in terms.items():
        coefficients[degree] = value
    return fmpq_poly(coefficients)


def parse_char0_y_polynomial(source: str, degree: int) -> list[fmpq_poly]:
    if not source.endswith("\n") or "\n" in source[:-1]:
        raise StrictDataError("independent char0 polynomial terminal newline failed")
    text = source[:-1]
    leading = "y" + (str(degree) if degree != 1 else "")
    if not text.startswith(leading):
        raise StrictDataError("independent char0 polynomial is not monic")
    cursor = len(leading)
    coefficients = [fmpq_poly() for _ in range(degree + 1)]
    coefficients[degree] = fmpq_poly([1])
    seen = {degree}
    while cursor < len(text):
        if not text.startswith("+(", cursor):
            raise StrictDataError("independent char0 y coefficient delimiter failed")
        end = text.find(")", cursor + 2)
        if end < 0:
            raise StrictDataError("independent char0 y coefficient is unterminated")
        coefficient = parse_char0_x_coefficient(text[cursor + 2 : end])
        cursor = end + 1
        if text.startswith("*y", cursor):
            cursor += 2
            start = cursor
            while cursor < len(text) and text[cursor].isdigit():
                cursor += 1
            y_degree = 1 if start == cursor else int(text[start:cursor])
        else:
            y_degree = 0
        if y_degree in seen or not 0 <= y_degree < degree:
            raise StrictDataError("independent char0 y degree failed")
        coefficients[y_degree] = coefficient
        seen.add(y_degree)
    if seen != set(range(degree + 1)):
        raise StrictDataError("independent char0 polynomial has missing coefficient slots")
    return coefficients


def independent_char0_incidence_identity(
    c56: dict[str, Any], witness: dict[str, Any]
) -> dict[str, Any]:
    rows = {
        row["leading_variable"]: row
        for row in c56["payload"]["grassmann_main_chart"]["lex_shape"]
    }
    if set(rows) != {"a", "b", "c", "d"}:
        raise StrictDataError("independent char0 lex shape failed")
    if c56["payload"].get("theorem_gates", {}).get("eliminant_irreducible_over_Q") is not True:
        raise StrictDataError("independent char0 field irreducibility premise failed")
    g = rows["d"]["tail_coefficients_d_0_up"]
    leading = g[-1]
    modulus = fmpq_poly([fmpq(value, leading) for value in g])
    if modulus.degree() != 27 or modulus.leading_coefficient() != 1:
        raise StrictDataError("independent char0 field modulus failed")
    H = parse_char0_y_polynomial(witness["H_text"], 10)
    Q = parse_char0_y_polynomial(witness["Q_text"], 17)
    if any(coefficient.degree() >= 27 for coefficient in H + Q):
        raise StrictDataError("independent char0 H/Q coefficients are unreduced")
    zero = fmpq_poly()
    one = fmpq_poly([1])

    def reduce_field(value: fmpq_poly) -> fmpq_poly:
        return value % modulus

    def multiply_field(left: fmpq_poly, right: fmpq_poly) -> fmpq_poly:
        return zero if left == 0 or right == 0 else (left * right) % modulus

    def trim_y(value: list[fmpq_poly]) -> list[fmpq_poly]:
        result = list(value)
        while len(result) > 1 and result[-1] == zero:
            result.pop()
        return result

    def multiply_y(left: list[fmpq_poly], right: list[fmpq_poly]) -> list[fmpq_poly]:
        result = [zero for _ in range(len(left) + len(right) - 1)]
        for right_degree, right_value in enumerate(right):
            if right_value == zero:
                continue
            for left_degree, left_value in enumerate(left):
                if left_value != zero:
                    index = left_degree + right_degree
                    result[index] = reduce_field(
                        result[index] + multiply_field(right_value, left_value)
                    )
        return trim_y(result)

    def divide_monic_y(dividend: list[fmpq_poly], divisor: list[fmpq_poly]):
        if divisor[-1] != one:
            raise StrictDataError("independent char0 division divisor is not monic")
        remainder = trim_y(dividend)
        quotient = [zero for _ in range(max(1, len(remainder) - len(divisor) + 1))]
        while len(remainder) >= len(divisor) and remainder != [zero]:
            shift = len(remainder) - len(divisor)
            coefficient = remainder[-1]
            quotient[shift] = coefficient
            for index in range(len(divisor)):
                target = shift + index
                remainder[target] = reduce_field(
                    remainder[target] - multiply_field(coefficient, divisor[index])
                )
            remainder = trim_y(remainder)
        return trim_y(quotient), trim_y(remainder)

    gy = [fmpq_poly([fmpq(value, leading)]) for value in g]
    if multiply_y(Q, H) != gy:
        raise StrictDataError("independent char0 forward Q*H identity failed")
    quotient, remainder = divide_monic_y(gy, H)
    if remainder != [zero] or quotient != Q:
        raise StrictDataError("independent char0 monic division failed")
    x = fmpq_poly([0, 1])
    x_powers = [one]
    for _ in range(25):
        x_powers.append(multiply_field(x_powers[-1], x))

    def divided_difference(coefficients: list[int]) -> list[fmpq_poly]:
        if len(coefficients) != 27:
            raise StrictDataError("independent divided-difference vector failed")
        result = []
        for y_degree in range(26):
            value = zero
            for source_degree in range(y_degree + 1, 27):
                value += x_powers[source_degree - 1 - y_degree] * coefficients[source_degree]
            result.append(reduce_field(value))
        return trim_y(result)

    Da = divided_difference(rows["a"]["tail_coefficients_d_0_up"])
    Db = divided_difference(rows["b"]["tail_coefficients_d_0_up"])
    Dc = divided_difference(rows["c"]["tail_coefficients_d_0_up"])
    DbDc = multiply_y(Db, Dc)
    J = [zero for _ in range(max(len(Da), len(DbDc)))]
    for index in range(len(J)):
        left = Da[index] * (-rows["b"]["leading_coefficient"] * rows["c"]["leading_coefficient"]) if index < len(Da) else zero
        right = DbDc[index] * (-rows["a"]["leading_coefficient"]) if index < len(DbDc) else zero
        J[index] = reduce_field(left + right)
    J = trim_y(J)
    _, remainder = divide_monic_y(J, H)
    if remainder != [zero]:
        raise StrictDataError("independent char0 H does not divide J")
    diagonal = zero
    power = one
    for coefficient in H:
        diagonal = reduce_field(diagonal + multiply_field(coefficient, power))
        power = multiply_field(power, x)
    if diagonal == zero:
        raise StrictDataError("independent char0 diagonal survived")
    return {
        "H_degree": 10,
        "Q_degree": 17,
        "H_Q_monic": True,
        "g_equals_H_times_Q": True,
        "monic_division_recovers_Q": True,
        "H_divides_J": True,
        "H_diagonal_nonzero_in_Qx_mod_g": True,
        "char0_common_factor_lower_bound": 10,
    }


def independent_incidence_replay(result_dir: Path, pari_python: Path) -> dict[str, Any]:
    witness, _, _ = strict_gzip_json(
        result_dir / "incidence_char0_witness.json.gz",
        max_compressed_bytes=3_000_000,
        max_decompressed_bytes=6_000_000,
    )
    if (
        witness.get("schema_id") != "hcs-c57-char0-incidence-witness-v1"
        or witness.get("H_text_sha256")
        != "b0f02a13ae60b01f1ec3d781896c5393853a75ff5fb0be517ae4c337c5f7007f"
        or witness.get("Q_text_sha256")
        != "ebf57460f2349972e99ecd6a4739a1c0e11521a65201c72a0be6665d91038a47"
        or sha256_bytes(witness["H_text"].encode()) != witness["H_text_sha256"]
        or sha256_bytes(witness["Q_text"].encode()) != witness["Q_text_sha256"]
    ):
        raise StrictDataError("independent incidence H/Q witness parser lock failed")
    c56 = strict_json_loads(
        read_stable(C56_CERTIFICATE, max_bytes=2_000_000)[0],
        max_bytes=2_000_000,
    )
    char0 = independent_char0_incidence_identity(c56, witness)
    backend = run_inline_json_backend(
        pari_python,
        PARI_INDEPENDENT_INCIDENCE_SOURCE,
        {
            "lex_shape": c56["payload"]["grassmann_main_chart"]["lex_shape"],
            "H_text": witness["H_text"],
            "Q_text": witness["Q_text"],
            "primes": list(BRIDGE_PRIMES),
        },
        timeout=1_800,
    )
    reports = backend.get("reports")
    if type(reports) is not list or len(reports) != 3:
        raise StrictDataError("independent incidence report count failed")
    if [report.get("prime") for report in reports] != list(BRIDGE_PRIMES):
        raise StrictDataError("independent incidence prime sequence/distinctness failed")
    report_keys = {
        "prime",
        "prime_proven",
        "eliminant_leading_coefficient_nonzero",
        "all_shape_denominators_units",
        "g_squarefree_27_roots",
        "all_H_coefficient_denominators_units",
        "determinant_formula_equals_J",
        "H_mod_p_equals_monic_gcd_all_27",
        "gcd_degrees",
        "line_degrees",
        "meeting_count",
        "sixer_count",
        "double_six_count",
        "oriented_sixer_distinct_values",
        "double_six_delta_distinct_values",
        "all_36_beta_nonzero",
        "meeting_graph_sha256",
    }
    expected_graphs = {
        7: "aaea1ca9c2fa5e0976583f3b8ae13d35b344623e637730ac3f85526ea7f3df38",
        37: "72939b3118f6cc1d149340363bdbcbded623d3a900ab6c326dd6e72700bfe347",
        BRIDGE_PRIMES[2]: "bf482b36a1f066939319b072d56d78bd511b1967b94550c8d709374ad1367bb8",
    }
    for report in reports:
        require_exact_keys(report, report_keys, "independent incidence prime report")
        prime = report.get("prime")
        required = {
            "prime_proven": True,
            "eliminant_leading_coefficient_nonzero": True,
            "all_shape_denominators_units": True,
            "g_squarefree_27_roots": True,
            "all_H_coefficient_denominators_units": True,
            "determinant_formula_equals_J": True,
            "H_mod_p_equals_monic_gcd_all_27": True,
            "gcd_degrees": [10] * 27,
            "line_degrees": [10] * 27,
            "meeting_count": 135,
            "sixer_count": 72,
            "double_six_count": 36,
            "double_six_delta_distinct_values": 36,
            "all_36_beta_nonzero": True,
            "meeting_graph_sha256": expected_graphs.get(prime),
        }
        for key, expected_value in required.items():
            if not deep_exact(report.get(key), expected_value):
                raise StrictDataError(f"independent incidence failed at p={prime}:{key}")
        if report.get("oriented_sixer_distinct_values") != (66 if prime == 7 else 72):
            raise StrictDataError("independent orientation separator count failed")
    return {
        "H_text_sha256": witness["H_text_sha256"],
        "Q_text_sha256": witness["Q_text_sha256"],
        "char0_identity": char0,
        "good_specialization_primes": list(BRIDGE_PRIMES),
        "graph_sha256_by_prime": {str(row["prime"]): row["meeting_graph_sha256"] for row in reports},
        "all_27_H_specializations_equal_monic_modular_gcd": True,
        "rank_specialization_upper_bound": 10,
        "orientation_separator_prime": 37,
        "oriented_sixer_distinct_values": 72,
        "all_36_beta_nonzero": True,
    }


PARI_H1_SOURCE = r'''
import json,sys
sys.set_int_max_str_digits(0)
from cypari2 import Pari
data=json.loads(sys.stdin.buffer.read()); pari=Pari()
def identity(n): return [[int(i==j) for j in range(n)] for i in range(n)]
def add(a,b): return [[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
def mul(a,b): return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def power(a,n):
    out=identity(len(a))
    while n:
        if n&1: out=mul(out,a)
        a=mul(a,a); n//=2
    return out
def pari_matrix(rows): return pari.matrix(len(rows),len(rows[0]),sum(rows,[]))
def relation(gens,coxeter):
    n=len(gens); I=identity(7); blocks=[]
    def word_block(word):
        block=[[0]*(7*n) for _ in range(7)]; prefix=I
        for index in word:
            for i in range(7):
                for j in range(7): block[i][7*index+j]+=prefix[i][j]
            prefix=mul(prefix,gens[index])
        if prefix!=I: raise ValueError("nonrelation")
        blocks.extend(block)
    for i in range(n): word_block([i,i])
    if coxeter:
        for i in range(6):
            for j in range(i+1,6):
                product=mul(gens[i],gens[j])
                order=3 if power(product,3)==I else 2
                if power(product,order)!=I: raise ValueError("bad Coxeter pair")
                word_block([i,j]*order)
    else:
        for i in range(5):
            for j in range(i+1,5): word_block([i,j]*(3 if j==i+1 else 2))
        for i in range(5): word_block([5,i,5,i])
    equations=pari_matrix(blocks)
    principal=[]
    for generator in gens:
        principal.extend([[generator[i][j]-I[i][j] for j in range(7)] for i in range(7)])
    P=pari_matrix(principal)
    if equations*P!=0: raise ValueError("principal is not cocycle")
    U,V,D=pari.matsnf(equations,1)
    zero_columns=[]; nonzero_columns=[]
    for j in range(int(D.ncols())):
        if all(D[i,j]==0 for i in range(int(D.nrows()))): zero_columns.append(j)
        else: nonzero_columns.append(j)
    coordinates=(V**-1)*P
    if any(coordinates[i,j]!=0 for i in nonzero_columns for j in range(7)): raise ValueError("principal outside kernel")
    rows=[[int(coordinates[i,j]) for j in range(7)] for i in zero_columns]
    K=pari_matrix(rows)
    diagonal=sorted(abs(int(x)) for x in pari.matsnf(K) if int(x)!=0)
    return {"smith_diagonal":diagonal,"cocycle_kernel_rank":len(zero_columns),"relation_rank":len(nonzero_columns)}
W=relation(data["W_generators"],True); U=relation(data["U_generators"],False)
invariant=[]; I=identity(7)
for generator in data["U_generators"][:5]:
    invariant.extend([[generator[i][j]-I[i][j] for j in range(7)] for i in range(7)])
S=pari.matsnf(pari_matrix(invariant)); invariant_nonzero=sorted(abs(int(x)) for x in S if int(x)!=0)
print(json.dumps({"W":W,"U":U,"S6_invariant_smith_nonzero":invariant_nonzero},sort_keys=True,separators=(",",":")))
'''


def vector_dot(left: tuple[int, ...], right: tuple[int, ...]) -> int:
    return left[0] * right[0] - sum(a * b for a, b in zip(left[1:], right[1:]))


def vector_add(
    left: tuple[int, ...], right: tuple[int, ...], scale: int = 1
) -> tuple[int, ...]:
    return tuple(a + scale * b for a, b in zip(left, right))


def vector_reflect(vector: tuple[int, ...], root: tuple[int, ...]) -> tuple[int, ...]:
    return vector_add(vector, root, vector_dot(vector, root))


def matrix_apply(matrix: list[list[int]], vector: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(sum(matrix[i][j] * vector[j] for j in range(7)) for i in range(7))


def permutation_compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[index]] for index in range(len(left)))


def generated_permutations(generators: list[tuple[int, ...]]) -> set[tuple[int, ...]]:
    identity = tuple(range(len(generators[0])))
    group = {identity}
    queue = [identity]
    cursor = 0
    while cursor < len(queue):
        value = queue[cursor]
        cursor += 1
        for generator in generators:
            new = permutation_compose(generator, value)
            if new not in group:
                group.add(new)
                queue.append(new)
    return group


def act_set(permutation: tuple[int, ...], value: frozenset[Any]) -> frozenset[Any]:
    return frozenset(
        permutation[item] if type(item) is int else act_set(permutation, item)
        for item in value
    )


def independent_group_replay(pari_python: Path) -> dict[str, Any]:
    exceptional = []
    for index in range(6):
        value = [0] * 7
        value[index + 1] = 1
        exceptional.append(tuple(value))
    roots = [vector_add(exceptional[i], exceptional[i + 1], -1) for i in range(5)]
    roots.append((1, -1, -1, -1, 0, 0, 0))
    lines = list(exceptional)
    for left, right in itertools.combinations(range(6), 2):
        value = [1] + [0] * 6
        value[left + 1] = value[right + 1] = -1
        lines.append(tuple(value))
    for omitted in range(6):
        value = [2] + [-1] * 6
        value[omitted + 1] = 0
        lines.append(tuple(value))
    line_index = {line: index for index, line in enumerate(lines)}
    reflection_permutations = [
        tuple(line_index[vector_reflect(line, root)] for line in lines)
        for root in roots
    ]
    incidence = [[vector_dot(left, right) for right in lines] for left in lines]
    sixers = [
        frozenset(subset)
        for subset in itertools.combinations(range(27), 6)
        if all(incidence[i][j] == 0 for i, j in itertools.combinations(subset, 2))
    ]
    doubles = set()
    for first in sixers:
        second = frozenset(
            line
            for line in range(27)
            if line not in first
            and sum(incidence[line][other] for other in first) == 5
        )
        if len(second) != 6:
            raise StrictDataError("independent group double-six complement failed")
        doubles.add(frozenset((first, second)))
    if len(sixers) != 72 or len(doubles) != 36:
        raise StrictDataError("independent group configuration counts failed")
    weyl = generated_permutations(reflection_permutations)
    if len(weyl) != 51840:
        raise StrictDataError("independent W(E6) order failed")
    standard_first = frozenset(range(6))
    standard_second = frozenset(range(21, 27))
    chosen = frozenset((standard_first, standard_second))
    stabilizer = {element for element in weyl if act_set(element, chosen) == chosen}
    oriented = {element for element in stabilizer if act_set(element, standard_first) == standard_first}
    swaps = {element for element in stabilizer if act_set(element, standard_first) == standard_second}
    if len(stabilizer) != 1440 or len(oriented) != 720 or len(swaps) != 720:
        raise StrictDataError("independent double-six stabilizers failed")
    core = {
        element
        for element in weyl
        if all(act_set(element, double) == double for double in doubles)
    }
    fixed_doubles = {
        double
        for double in doubles
        if all(act_set(element, double) == double for element in stabilizer)
    }
    if len(core) != 1 or len(fixed_doubles) != 1:
        raise StrictDataError("independent core/self-normalizer gate failed")
    orbit_sizes = []
    remaining = set(range(27))
    while remaining:
        seed = min(remaining)
        orbit = {element[seed] for element in stabilizer}
        orbit_sizes.append(len(orbit))
        remaining -= orbit
    if sorted(orbit_sizes) != [12, 15]:
        raise StrictDataError("independent stabilizer line orbits failed")

    picard_generators = []
    for root in roots:
        columns = [
            vector_reflect(tuple(int(i == j) for i in range(7)), root)
            for j in range(7)
        ]
        picard_generators.append(
            [[columns[column][row] for column in range(7)] for row in range(7)]
        )
    switch_columns = [(5, -2, -2, -2, -2, -2, -2)]
    for index in range(6):
        column = [2] + [-1] * 6
        column[index + 1] = 0
        switch_columns.append(tuple(column))
    switch = [[switch_columns[column][row] for column in range(7)] for row in range(7)]
    switch_permutation = tuple(line_index[matrix_apply(switch, line)] for line in lines)
    s6 = generated_permutations(reflection_permutations[:5])
    full = generated_permutations(reflection_permutations[:5] + [switch_permutation])
    if (
        len(s6) != 720
        or len(full) != 1440
        or switch_permutation in s6
        or switch_permutation == tuple(range(27))
        or permutation_compose(switch_permutation, switch_permutation) != tuple(range(27))
        or any(
            permutation_compose(switch_permutation, generator)
            != permutation_compose(generator, switch_permutation)
            for generator in reflection_permutations[:5]
        )
        or full != stabilizer
        or s6 != oriented
        or act_set(switch_permutation, standard_first) != standard_second
        or act_set(switch_permutation, standard_second) != standard_first
    ):
        raise StrictDataError("independent S6 x C2 presentation failed")

    h1 = run_inline_json_backend(
        pari_python,
        PARI_H1_SOURCE,
        {
            "W_generators": picard_generators,
            "U_generators": picard_generators[:5] + [switch],
        },
        timeout=900,
    )
    if (
        h1.get("W", {}).get("smith_diagonal") != [1, 1, 1, 1, 1, 1]
        or h1.get("U", {}).get("smith_diagonal") != [1, 1, 1, 1, 1, 2]
        or h1.get("W", {}).get("cocycle_kernel_rank") != 6
        or h1.get("W", {}).get("relation_rank") != 36
        or h1.get("U", {}).get("cocycle_kernel_rank") != 6
        or h1.get("U", {}).get("relation_rank") != 36
        or h1.get("S6_invariant_smith_nonzero") != [1, 1, 1, 1, 1]
    ):
        raise StrictDataError("independent PARI H1/S6 invariant SNF failed")
    h = (1, 0, 0, 0, 0, 0, 0)
    e_sum = (0, 1, 1, 1, 1, 1, 1)
    if any(matrix_apply(generator, h) != h or matrix_apply(generator, e_sum) != e_sum for generator in picard_generators[:5]):
        raise StrictDataError("independent Pic^S6 basis failed")
    if matrix_apply(switch, h) != vector_add(tuple(5 * x for x in h), e_sum, -2):
        raise StrictDataError("independent central action on h failed")
    if matrix_apply(switch, e_sum) != vector_add(tuple(12 * x for x in h), e_sum, -5):
        raise StrictDataError("independent central action on eSigma failed")
    d0 = vector_add(e_sum, h, -2)
    H0 = vector_add(tuple(3 * x for x in h), e_sum, -1)
    D = vector_add(e_sum, H0, -2)
    if matrix_apply(switch, d0) != tuple(-x for x in d0) or D != tuple(3 * x for x in d0):
        raise StrictDataError("independent oriented divisor lattice identity failed")
    central_coordinates = [[5, 12], [-2, -5]]
    sigma_minus_identity_columns = [
        [central_coordinates[row][column] - int(row == column) for row in range(2)]
        for column in range(2)
    ]
    d0_coordinates = [-2, 1]
    coboundary_multiples = []
    for column in sigma_minus_identity_columns:
        multiple = column[1]
        if column != [multiple * value for value in d0_coordinates]:
            raise StrictDataError("independent central coboundary image is not on d0")
        coboundary_multiples.append(multiple)
    if math.gcd(*coboundary_multiples) != 2 or 3 % 2 != 1:
        raise StrictDataError("independent coboundary parity failed")
    return {
        "W_E6_order": 51840,
        "stabilizer_order": 1440,
        "stabilizer_index": 36,
        "core_order": 1,
        "normalizer_order": 1440,
        "U_fixed_double_six_count": 1,
        "S6_order": 720,
        "central_swap_order": 2,
        "generated_order": 1440,
        "line_orbit_sizes": [12, 15],
        "H1_W_Pic_torsion": [],
        "H1_U_Pic_torsion": [2],
        "H1_W_Pic_smith_diagonal": [1, 1, 1, 1, 1, 1],
        "H1_U_Pic_smith_diagonal": [1, 1, 1, 1, 1, 2],
        "W_cocycle_kernel_rank": 6,
        "W_relation_rank": 36,
        "U_cocycle_kernel_rank": 6,
        "U_relation_rank": 36,
        "Pic_S6_invariant_basis": [list(h), list(e_sum)],
        "central_swap_on_h_E_columns": [[5, -2], [12, -5]],
        "anti_invariant_d0_in_h_E": [-2, 1],
        "central_swap_minus_identity_d0_multiples": coboundary_multiples,
        "Pic_S6_coboundary_lattice": "2 Z*d0",
        "oriented_divisor_class_D_multiple_of_d0": 3,
        "oriented_divisor_class_D_nonzero_mod_coboundaries": True,
    }


_IG6_P = 7
_IG6_N = 6
_IG6_Q = _IG6_P**_IG6_N
_IG6_EXPECTED_PAYLOAD_SHA256 = (
    "5b17c9ed7bea60680556af70297199b653d51188bb30ce59f7c2c6bfbc94f661"
)
_IG6_EXPECTED_A12_TABLE_SHA256 = (
    "72d4aef5120926ec09904b08219cba7cf2b49323bd085d05274e5c17e1ed90a1"
)
_IG6_EXPECTED_THETA_COEFFICIENTS_SHA256 = (
    "845a0cd703b3d5d7c8814f7339010601cc2a25293b6b1bfe792aff2c728e23ea"
)


def _ig6_canonical(value):
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def _ig6_hash(value):
    return hashlib.sha256(_ig6_canonical(value)).hexdigest()


# Scalar polynomials over F_7, coefficients low to high.
def _ig6_sp_trim(poly):
    result = [value % _IG6_P for value in poly]
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def _ig6_sp_sub(left, right):
    result = [0] * max(len(left), len(right))
    for i in range(len(result)):
        result[i] = (
            (left[i] if i < len(left) else 0)
            - (right[i] if i < len(right) else 0)
        ) % _IG6_P
    return _ig6_sp_trim(result)


def _ig6_sp_mul(left, right):
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        if a:
            for j, b in enumerate(right):
                if b:
                    result[i + j] = (result[i + j] + a * b) % _IG6_P
    return _ig6_sp_trim(result)


def _ig6_sp_divmod(numerator, denominator):
    num = _ig6_sp_trim(numerator)
    den = _ig6_sp_trim(denominator)
    if den == [0]:
        raise ZeroDivisionError
    if len(num) < len(den):
        return [0], num
    quotient = [0] * (len(num) - len(den) + 1)
    inverse = pow(den[-1], -1, _IG6_P)
    while num != [0] and len(num) >= len(den):
        shift = len(num) - len(den)
        coefficient = num[-1] * inverse % _IG6_P
        quotient[shift] = coefficient
        for i, value in enumerate(den):
            num[i + shift] = (
                num[i + shift] - coefficient * value
            ) % _IG6_P
        num = _ig6_sp_trim(num)
    return _ig6_sp_trim(quotient), num


def _ig6_sp_mod(poly, modulus):
    return _ig6_sp_divmod(poly, modulus)[1]


def _ig6_sp_mulmod(left, right, modulus):
    return _ig6_sp_mod(_ig6_sp_mul(left, right), modulus)


def _ig6_sp_powmod(base, exponent, modulus):
    result = [1]
    power = _ig6_sp_mod(base, modulus)
    while exponent:
        if exponent & 1:
            result = _ig6_sp_mulmod(result, power, modulus)
        power = _ig6_sp_mulmod(power, power, modulus)
        exponent >>= 1
    return result


def _ig6_sp_gcd(left, right):
    a, b = _ig6_sp_trim(left), _ig6_sp_trim(right)
    while b != [0]:
        _, remainder = _ig6_sp_divmod(a, b)
        a, b = b, remainder
    inverse = pow(a[-1], -1, _IG6_P)
    return [(value * inverse) % _IG6_P for value in a]


def _ig6_irreducible(modulus):
    modulus = _ig6_sp_trim(modulus)
    if len(modulus) != _IG6_N + 1 or modulus[-1] != 1:
        return False
    x = [0, 1]
    for exponent_degree in (2, 3):
        frobenius = _ig6_sp_powmod(
            x, _IG6_P**exponent_degree, modulus
        )
        if _ig6_sp_gcd(modulus, _ig6_sp_sub(frobenius, x)) != [1]:
            return False
    return _ig6_sp_sub(
        _ig6_sp_powmod(x, _IG6_P**_IG6_N, modulus), x
    ) == [0]


def _ig6_select_modulus():
    for constant in range(1, _IG6_P):
        for middle in itertools.product(
            range(_IG6_P), repeat=_IG6_N - 1
        ):
            candidate = (constant, *middle, 1)
            if _ig6_irreducible(candidate):
                return candidate
    raise AssertionError("no irreducible degree-six polynomial")


_IG6_MODULUS = _ig6_select_modulus()
_IG6_ZERO = (0,) * _IG6_N
_IG6_ONE = (1,) + (0,) * (_IG6_N - 1)


# F_(7^6) in the polynomial basis 1,z,...,z^5.
def _ig6_ff(value):
    return (value % _IG6_P,) + (0,) * (_IG6_N - 1)


def _ig6_ff_add(left, right):
    return tuple(
        (left[i] + right[i]) % _IG6_P for i in range(_IG6_N)
    )


def _ig6_ff_sub(left, right):
    return tuple(
        (left[i] - right[i]) % _IG6_P for i in range(_IG6_N)
    )


def _ig6_ff_neg(value):
    return tuple((-value[i]) % _IG6_P for i in range(_IG6_N))


def _ig6_ff_scale(value, scalar):
    scalar %= _IG6_P
    return tuple(
        scalar * value[i] % _IG6_P for i in range(_IG6_N)
    )


def _ig6_ff_mul(left, right):
    temporary = [0] * (2 * _IG6_N - 1)
    for i, a in enumerate(left):
        if a:
            for j, b in enumerate(right):
                if b:
                    temporary[i + j] += a * b
    for degree in range(2 * _IG6_N - 2, _IG6_N - 1, -1):
        coefficient = temporary[degree] % _IG6_P
        if coefficient:
            offset = degree - _IG6_N
            for i in range(_IG6_N):
                temporary[offset + i] -= coefficient * _IG6_MODULUS[i]
        temporary[degree] = 0
    return tuple(value % _IG6_P for value in temporary[:_IG6_N])


def _ig6_ff_pow(base, exponent):
    result = _IG6_ONE
    power = base
    while exponent:
        if exponent & 1:
            result = _ig6_ff_mul(result, power)
        power = _ig6_ff_mul(power, power)
        exponent >>= 1
    return result


def _ig6_ff_inv(value):
    if value == _IG6_ZERO:
        raise ZeroDivisionError
    return _ig6_ff_pow(value, _IG6_Q - 2)


def _ig6_ff_from_index(index):
    coefficients = []
    for _ in range(_IG6_N):
        coefficients.append(index % _IG6_P)
        index //= _IG6_P
    return tuple(coefficients)


def _ig6_ff_eval_scalar_polynomial(coefficients, value):
    result = _IG6_ZERO
    for coefficient in reversed(coefficients):
        result = _ig6_ff_mul(result, value)
        if coefficient % _IG6_P:
            result = (
                (result[0] + coefficient) % _IG6_P,
                result[1],
                result[2],
                result[3],
                result[4],
                result[5],
            )
    return result


# Polynomials in d over F_(7^6), coefficients low to high.
def _ig6_fp_trim(poly):
    result = list(poly)
    while len(result) > 1 and result[-1] == _IG6_ZERO:
        result.pop()
    return result


def _ig6_fp_add(left, right):
    result = [_IG6_ZERO] * max(len(left), len(right))
    for i in range(len(result)):
        result[i] = _ig6_ff_add(
            left[i] if i < len(left) else _IG6_ZERO,
            right[i] if i < len(right) else _IG6_ZERO,
        )
    return _ig6_fp_trim(result)


def _ig6_fp_scale(poly, scalar):
    return _ig6_fp_trim([_ig6_ff_scale(value, scalar) for value in poly])


def _ig6_fp_mul(left, right):
    result = [_IG6_ZERO] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        if a != _IG6_ZERO:
            for j, b in enumerate(right):
                if b != _IG6_ZERO:
                    result[i + j] = _ig6_ff_add(
                        result[i + j], _ig6_ff_mul(a, b)
                    )
    return _ig6_fp_trim(result)


def _ig6_fp_mod_monic(poly, modulus):
    result = list(poly)
    degree = len(modulus) - 1
    if modulus[-1] != _IG6_ONE:
        raise ValueError("carrier is not monic")
    while len(result) > degree:
        top_degree = len(result) - 1
        coefficient = result[-1]
        if coefficient != _IG6_ZERO:
            offset = top_degree - degree
            for i in range(degree):
                result[offset + i] = _ig6_ff_sub(
                    result[offset + i],
                    _ig6_ff_mul(coefficient, modulus[i]),
                )
        result.pop()
    return _ig6_fp_trim(result or [_IG6_ZERO])


def _ig6_fp_mulmod(left, right, modulus):
    return _ig6_fp_mod_monic(_ig6_fp_mul(left, right), modulus)


def _ig6_fp_orbit_product(roots):
    coefficients = [_IG6_ONE]
    for root in roots:
        updated = [_IG6_ZERO] * (len(coefficients) + 1)
        for i, coefficient in enumerate(coefficients):
            updated[i] = _ig6_ff_sub(
                updated[i], _ig6_ff_mul(root, coefficient)
            )
            updated[i + 1] = _ig6_ff_add(
                updated[i + 1], coefficient
            )
        coefficients = updated
    return _ig6_fp_trim(coefficients)


def _ig6_fp_coefficient(poly, index):
    return poly[index] if index < len(poly) else _IG6_ZERO


def _ig6_degree_four_monomials():
    rows = []
    for e0 in range(4, -1, -1):
        for e1 in range(4 - e0, -1, -1):
            for e2 in range(4 - e0 - e1, -1, -1):
                rows.append((e0, e1, e2, 4 - e0 - e1 - e2))
    return rows


_IG6_GAUGE = {
    (4, 0, 0, 0),
    (3, 1, 0, 0),
    (3, 0, 1, 0),
    (3, 0, 0, 1),
}
_IG6_MONOMIALS = [
    row for row in _ig6_degree_four_monomials() if row not in _IG6_GAUGE
]
_IG6_PIVOT_ROWS = [
    *range(0, 11),
    *range(12, 21),
    *range(24, 30),
    36,
    37,
    38,
    48,
]


def _ig6_solve_and_determinant(matrix, right):
    size = len(matrix)
    work = [list(row) for row in matrix]
    vector = list(right)
    determinant = _IG6_ONE
    sign = 1
    for column in range(size):
        pivot_row = next(
            (
                row
                for row in range(column, size)
                if work[row][column] != _IG6_ZERO
            ),
            None,
        )
        if pivot_row is None:
            return _IG6_ZERO, None
        if pivot_row != column:
            work[column], work[pivot_row] = work[pivot_row], work[column]
            vector[column], vector[pivot_row] = (
                vector[pivot_row],
                vector[column],
            )
            sign = -sign
        pivot = work[column][column]
        determinant = _ig6_ff_mul(determinant, pivot)
        inverse = _ig6_ff_inv(pivot)
        for i in range(column + 1, size):
            work[column][i] = _ig6_ff_mul(work[column][i], inverse)
        vector[column] = _ig6_ff_mul(vector[column], inverse)
        work[column][column] = _IG6_ONE
        for row in range(column + 1, size):
            factor = work[row][column]
            if factor == _IG6_ZERO:
                continue
            work[row][column] = _IG6_ZERO
            for i in range(column + 1, size):
                work[row][i] = _ig6_ff_sub(
                    work[row][i],
                    _ig6_ff_mul(factor, work[column][i]),
                )
            vector[row] = _ig6_ff_sub(
                vector[row], _ig6_ff_mul(factor, vector[column])
            )
    solution = [_IG6_ZERO] * size
    for row in range(size - 1, -1, -1):
        value = vector[row]
        for column in range(row + 1, size):
            value = _ig6_ff_sub(
                value, _ig6_ff_mul(work[row][column], solution[column])
            )
        solution[row] = value
    if sign < 0:
        determinant = _ig6_ff_neg(determinant)
    return determinant, solution


def independent_g6_replay(c56_payload, a12, theta) -> dict:
    """Replay C57 G6 using parsed inputs and return compact invariants.

    Raises ValueError or AssertionError on every failed semantic gate.  There
    is no file access, command execution, producer call, or result mutation.
    """

    payload_hash = _ig6_hash(c56_payload)
    if payload_hash != _IG6_EXPECTED_PAYLOAD_SHA256:
        raise ValueError("C56 payload source lock mismatch")
    if not isinstance(a12, dict) or a12.get("schema_id") != "hcs-c57-a12-table-v1":
        raise ValueError("wrong A12 schema")
    if not isinstance(theta, dict) or theta.get("schema_id") != "hcs-c57-theta-crt-v1":
        raise ValueError("wrong theta schema")
    if theta.get("candidate_input_used") is not False:
        raise ValueError("theta evidence depends on carrier candidate")
    if theta.get("degree") != 36:
        raise ValueError("wrong theta degree")

    candidate_table = a12.get("coefficient_table_fractions")
    if (
        not isinstance(candidate_table, list)
        or len(candidate_table) != 13
        or any(not isinstance(row, list) or len(row) != 36 for row in candidate_table)
    ):
        raise ValueError("wrong A12 coefficient table dimensions")
    table_hash = _ig6_hash(candidate_table)
    if (
        table_hash != _IG6_EXPECTED_A12_TABLE_SHA256
        or a12.get("coefficient_table_sha256") != table_hash
    ):
        raise ValueError("A12 coefficient table source lock mismatch")
    theta_coefficients = theta.get("coefficients")
    if not isinstance(theta_coefficients, list) or len(theta_coefficients) != 37:
        raise ValueError("wrong theta coefficient count")
    theta_hash = _ig6_hash(theta_coefficients)
    if (
        theta_hash != _IG6_EXPECTED_THETA_COEFFICIENTS_SHA256
        or theta.get("coefficients_sha256") != theta_hash
    ):
        raise ValueError("theta coefficient source lock mismatch")

    table_mod_p = []
    for row in candidate_table:
        reduced = []
        for fraction in row:
            if (
                not isinstance(fraction, list)
                or len(fraction) != 2
                or not all(isinstance(value, int) for value in fraction)
            ):
                raise ValueError("malformed A12 fraction")
            numerator, denominator = fraction
            denominator_mod = denominator % _IG6_P
            if denominator_mod == 0:
                raise ValueError("A12 denominator is zero modulo 7")
            reduced.append(
                numerator % _IG6_P
                * pow(denominator_mod, -1, _IG6_P)
                % _IG6_P
            )
        table_mod_p.append(reduced)

    primitive = c56_payload.get("surface", {}).get("primitive_coefficients")
    if not isinstance(primitive, list):
        raise ValueError("missing C56 surface coefficients")
    surface_coefficients = {
        tuple(row["exponents_u0_to_u3"]): row["coefficient"]
        for row in primitive
    }
    c = surface_coefficients.get((3, 0, 0, 0), 0)
    gauge_block = [
        [c, 0, 0, 0],
        [surface_coefficients.get((2, 1, 0, 0), 0), c, 0, 0],
        [surface_coefficients.get((2, 0, 1, 0), 0), 0, c, 0],
        [surface_coefficients.get((2, 0, 0, 1), 0), 0, 0, c],
    ]
    expected_gauge = [
        [75081586157, 0, 0, 0],
        [-28576620789, 75081586157, 0, 0],
        [-122000922135, 0, 75081586157, 0],
        [-5364921951, 0, 0, 75081586157],
    ]
    gauge_determinant = c**4
    if gauge_block != expected_gauge:
        raise ValueError("C56-derived gauge block mismatch")
    if gauge_determinant != 31778526453059635681033276764499400992765201:
        raise ValueError("gauge determinant mismatch")
    if gauge_determinant % _IG6_P == 0:
        raise ValueError("gauge degenerates modulo 7")

    chart = c56_payload.get("grassmann_main_chart")
    if not isinstance(chart, dict):
        raise ValueError("missing C56 line chart")
    if chart.get("chart") != "U01" or chart.get("coordinates") != [
        "s",
        "t",
        "a*s+c*t",
        "b*s+d*t",
    ]:
        raise ValueError("line-chart convention mismatch")
    lex_shape = chart.get("lex_shape")
    if not isinstance(lex_shape, list):
        raise ValueError("missing C56 lex shape")
    by_variable = {row["leading_variable"]: row for row in lex_shape}
    if set(by_variable) != {"a", "b", "c", "d"}:
        raise ValueError("wrong lex-shape variables")
    g_coefficients = [
        value % _IG6_P
        for value in by_variable["d"]["tail_coefficients_d_0_up"]
    ]
    if len(g_coefficients) != 28 or g_coefficients[-1] == 0:
        raise ValueError("bad degree-27 eliminant modulo 7")
    for variable in ("a", "b", "c"):
        if by_variable[variable]["leading_coefficient"] % _IG6_P == 0:
            raise ValueError("shape denominator vanishes modulo 7")

    roots = []
    for index in range(_IG6_Q):
        value = _ig6_ff_from_index(index)
        if _ig6_ff_eval_scalar_polynomial(g_coefficients, value) == _IG6_ZERO:
            roots.append(value)
    if len(roots) != 27 or len(set(roots)) != 27:
        raise ValueError("eliminant lacks 27 distinct roots in F_(7^6)")

    unseen = set(roots)
    frobenius_degrees = []
    while unseen:
        start = min(unseen)
        orbit = []
        value = start
        while value not in orbit:
            orbit.append(value)
            value = _ig6_ff_pow(value, _IG6_P)
        if value != start or any(item not in unseen for item in orbit):
            raise ValueError("bad Frobenius orbit among eliminant roots")
        for item in orbit:
            unseen.remove(item)
        frobenius_degrees.append(len(orbit))
    frobenius_degrees.sort()
    if frobenius_degrees != [3, 3, 3, 3, 3, 6, 6]:
        raise ValueError("unexpected Frobenius factor degrees")

    lines = []
    for d_value in roots:
        line = {"d": d_value}
        for variable in ("a", "b", "c"):
            row = by_variable[variable]
            numerator = _ig6_ff_eval_scalar_polynomial(
                [value % _IG6_P for value in row["tail_coefficients_d_0_up"]],
                d_value,
            )
            inverse = pow(
                row["leading_coefficient"] % _IG6_P, -1, _IG6_P
            )
            line[variable] = _ig6_ff_scale(numerator, -inverse)
        lines.append(line)

    meeting = set()
    for left_index, right_index in itertools.combinations(range(27), 2):
        left, right = lines[left_index], lines[right_index]
        residue = _ig6_ff_sub(
            _ig6_ff_mul(
                _ig6_ff_sub(left["a"], right["a"]),
                _ig6_ff_sub(left["d"], right["d"]),
            ),
            _ig6_ff_mul(
                _ig6_ff_sub(left["b"], right["b"]),
                _ig6_ff_sub(left["c"], right["c"]),
            ),
        )
        if residue == _IG6_ZERO:
            meeting.add((left_index, right_index))
    if len(meeting) != 135:
        raise ValueError("wrong incidence count")

    def meets(i, j):
        return (i, j) in meeting if i < j else (j, i) in meeting

    sixers = []
    for subset in itertools.combinations(range(27), 6):
        if all(
            not meets(i, j)
            for i, j in itertools.combinations(subset, 2)
        ):
            sixers.append(frozenset(subset))
    if len(sixers) != 72:
        raise ValueError("wrong sixer count")
    sixer_set = set(sixers)
    double_sixes = set()
    for first in sixers:
        second = frozenset(
            index
            for index in range(27)
            if index not in first
            and sum(meets(index, member) for member in first) == 5
        )
        if len(second) != 6 or second not in sixer_set:
            raise ValueError("opposite-sixer reconstruction failed")
        double_sixes.add(
            tuple(sorted((tuple(sorted(first)), tuple(sorted(second)))))
        )
    configurations = sorted(double_sixes)
    if len(configurations) != 36:
        raise ValueError("wrong double-six count")
    if any(
        len(set(first) | set(second)) != 12
        for first, second in configurations
    ):
        raise ValueError("carrier does not contain 12 distinct lines")

    if len(_IG6_MONOMIALS) != 31 or _IG6_MONOMIALS[0] != (2, 2, 0, 0):
        raise ValueError("quartic monomial convention mismatch")
    if len(_IG6_PIVOT_ROWS) != 30 or len(set(_IG6_PIVOT_ROWS)) != 30:
        raise ValueError("pivot-row convention mismatch")

    def build_matrix(configuration):
        indices = sorted(set(configuration[0]) | set(configuration[1]))
        carrier = _ig6_fp_orbit_product(roots[index] for index in indices)
        if len(carrier) != 13 or carrier[-1] != _IG6_ONE:
            raise ValueError("bad carrier degree or leading coefficient")
        theta_value = _IG6_ZERO
        for index in indices:
            theta_value = _ig6_ff_add(theta_value, roots[index])
        theta_value = _ig6_ff_scale(theta_value, g_coefficients[-1])
        expected_carrier = [
            _ig6_ff_eval_scalar_polynomial(row, theta_value)
            for row in table_mod_p
        ]
        if carrier != expected_carrier:
            raise ValueError("A12 carrier specialization mismatch")

        line_polynomials = {"d": [_IG6_ZERO, _IG6_ONE]}
        for variable in ("a", "b", "c"):
            row = by_variable[variable]
            inverse = pow(
                row["leading_coefficient"] % _IG6_P, -1, _IG6_P
            )
            polynomial = [
                _ig6_ff((-value % _IG6_P) * inverse)
                for value in row["tail_coefficients_d_0_up"]
            ]
            line_polynomials[variable] = _ig6_fp_mod_monic(
                polynomial, carrier
            )

        powers = {}
        for variable in ("a", "b", "c", "d"):
            powers[(variable, 0)] = [_IG6_ONE]
            for exponent in range(1, 5):
                powers[(variable, exponent)] = _ig6_fp_mulmod(
                    powers[(variable, exponent - 1)],
                    line_polynomials[variable],
                    carrier,
                )

        columns = []
        for _e0, e1, e2, e3 in _IG6_MONOMIALS:
            coefficients = [[_IG6_ZERO] for _ in range(5)]
            for i in range(e2 + 1):
                for j in range(e3 + 1):
                    term = [_IG6_ONE]
                    for factor in (
                        powers[("a", e2 - i)],
                        powers[("c", i)],
                        powers[("b", e3 - j)],
                        powers[("d", j)],
                    ):
                        term = _ig6_fp_mulmod(term, factor, carrier)
                    term = _ig6_fp_scale(
                        term, comb(e2, i) * comb(e3, j)
                    )
                    t_degree = e1 + i + j
                    coefficients[t_degree] = _ig6_fp_add(
                        coefficients[t_degree], term
                    )
            columns.append(coefficients)

        matrix = [
            [_IG6_ZERO] * len(_IG6_MONOMIALS) for _ in range(60)
        ]
        for column_index, coefficients in enumerate(columns):
            for t_degree in range(5):
                for d_degree in range(12):
                    matrix[12 * t_degree + d_degree][column_index] = (
                        _ig6_fp_coefficient(
                            coefficients[t_degree], d_degree
                        )
                    )
        return matrix, theta_value

    theta_values = []
    determinant_values = []
    residual_count = 0
    for configuration in configurations:
        matrix, theta_value = build_matrix(configuration)
        if len(matrix) != 60 or any(len(row) != 31 for row in matrix):
            raise AssertionError("wrong restriction-matrix shape")
        minor = [
            [matrix[row][column] for column in range(1, 31)]
            for row in _IG6_PIVOT_ROWS
        ]
        right = [_ig6_ff_neg(matrix[row][0]) for row in _IG6_PIVOT_ROWS]
        determinant, rest = _ig6_solve_and_determinant(minor, right)
        if determinant == _IG6_ZERO or rest is None:
            raise ValueError("fixed pivot determinant vanished")
        solution = [_IG6_ONE, *rest]
        if solution[0] != _IG6_ONE or len(solution) != 31:
            raise AssertionError("Cramer normalization failed")
        for row in matrix:
            residue = _IG6_ZERO
            for coefficient, value in zip(row, solution):
                residue = _ig6_ff_add(
                    residue, _ig6_ff_mul(coefficient, value)
                )
            if residue != _IG6_ZERO:
                raise ValueError("nonzero quartic restriction remainder")
            residual_count += 1
        theta_values.append(theta_value)
        determinant_values.append(determinant)

    if len(set(theta_values)) != 36:
        raise ValueError("theta does not separate the 36 double-sixes")
    theta_coefficients_mod_p = [
        value % _IG6_P for value in theta_coefficients
    ]
    if any(
        _ig6_ff_eval_scalar_polynomial(theta_coefficients_mod_p, value)
        != _IG6_ZERO
        for value in theta_values
    ):
        raise ValueError("R_theta(theta_D) is nonzero")
    theta_orbit_product = _ig6_fp_orbit_product(theta_values)
    expected_theta_polynomial = [
        _ig6_ff(value) for value in theta_coefficients_mod_p
    ]
    if theta_orbit_product != expected_theta_polynomial:
        raise ValueError("theta orbit product differs from R_theta modulo 7")

    determinant_norm = _IG6_ONE
    for determinant in determinant_values:
        determinant_norm = _ig6_ff_mul(determinant_norm, determinant)
    if determinant_norm != _ig6_ff(3):
        raise ValueError("fixed-minor determinant norm is not 3 modulo 7")
    if residual_count != 2160:
        raise AssertionError("wrong residual count")

    return {
        "checker_id": "hcs-c57-g6-alt-inline-pure-python-v1",
        "status": "PASS",
        "backend": "pure_python_polynomial_basis_F_7_power_6",
        "input_bindings": {
            "c56_payload_sha256": payload_hash,
            "a12_table_sha256": table_hash,
            "theta_coefficients_sha256": theta_hash,
        },
        "finite_field": {
            "prime": _IG6_P,
            "degree": _IG6_N,
            "order": _IG6_Q,
            "modulus_coefficients_low_to_high": list(_IG6_MODULUS),
            "modulus_irreducible": True,
        },
        "configuration": {
            "eliminant_root_count": len(roots),
            "frobenius_factor_degrees": frobenius_degrees,
            "meeting_pair_count": len(meeting),
            "sixer_count": len(sixers),
            "double_six_count": len(configurations),
            "carrier_line_count_each": 12,
            "all_carrier_lines_distinct": True,
            "all_carrier_specializations_match_A12": True,
            "u0_hyperplane_contains_no_carrier_line": True,
        },
        "theta": {
            "distinct_value_count": len(set(theta_values)),
            "all_R_theta_at_theta_D_zero": True,
            "orbit_product_equals_R_theta_mod_7": True,
        },
        "gauge": {
            "block": gauge_block,
            "determinant_over_Z": gauge_determinant,
            "determinant_nonzero_mod_7": True,
        },
        "matrix": {
            "count": len(configurations),
            "shape_each": [60, 31],
            "fixed_minor_shape": [30, 30],
            "fixed_pivot_rows_zero_based": list(_IG6_PIVOT_ROWS),
            "all_fixed_pivot_determinants_nonzero": True,
            "pivot_determinant_norm_mod_7": 3,
            "normalization_monomial": [2, 2, 0, 0],
            "all_cramer_q0_equal_1": True,
            "zero_restriction_residual_count": residual_count,
            "all_restriction_residuals_zero": True,
        },
    }


EXPECTED_PRODUCER_EXACT_REPORTS = {
    "G1": {
        "char0_report_sha256": "33a1bab2ff85ea5add1a3e3e5c9043dbaea9bf84adbed93698363d7450de4b9d",
        "bridge_report_sha256_by_prime": {
            "7": "5cc6a573c6c4f7ab608fd721a755060abf416469959d8a5fc7461eb58e07e167",
            "37": "aeaaeab0d661c9c7b313287fbfd5c3f0fc1832399660899cc470b51c4c21c5de",
            "100000000000000000000000000000000000000000000012477": "a45e769022977bb449ffb74adf6c9572a0cc23c865220ae90fcd1bbd702fcdb3",
        },
    },
    "G2": {"group_report_sha256": "6e7bf757567f5a84e848ef29ac59c288c7e9ab0cfbfd620c9a7e7daeb4647a23"},
    "G3": {
        "resolver_replay_report_sha256": {
            "theta": "354569475914adad9837489e042bfc6e37cd1a815760f380ab1346844d40a5a7",
            "delta": "21a78de8501877f42be381db2745aec1d5805087391e8f6dcabe329a5d3ed9a7",
        },
        "irreducibility_report_sha256": {
            "theta": "4b85704ea35e0ac668dce1a0dade7213a42c261e30d2d09d75ea30792a915b1e",
            "delta": "9e825bf3671755078d17c820b3ca8ffc9f36c58a99f30edb4d5f43617e3f30d0",
        },
    },
    "G4": {
        "orientation_separator_report_sha256": "aeaaeab0d661c9c7b313287fbfd5c3f0fc1832399660899cc470b51c4c21c5de",
        "group_action_report_sha256": "6e7bf757567f5a84e848ef29ac59c288c7e9ab0cfbfd620c9a7e7daeb4647a23",
    },
    "G5": {
        "reconstruction_report_sha256": "b8109057684249a519ffb04209af865608488faf0094b2b1303141367946f774",
        "identity_report_sha256": "4c6081355dc3c6b2f7f704072336ce643ab5d84e18eec527d5b5c99f26fc325a",
    },
    "G6": {"pivot_report_sha256": "5e1e561996f4cb3a1ba8bbbac6c473390d45b9356d546c0df5630cae463a3b7e"},
    "G7": {
        "divisor_input_report_sha256": "5e1e561996f4cb3a1ba8bbbac6c473390d45b9356d546c0df5630cae463a3b7e",
        "report_semantic_scope": [
            "carrier_line_count_per_double_six",
            "all_12_carrier_lines_distinct_per_double_six",
            "u0_hyperplane_contains_no_carrier_line",
            "normalization_q0_value",
            "normalization_q0_nonzero",
            "all_36_times_60_replay_zero",
        ],
        "machine_scope_is_divisor_inputs_not_class_map": True,
    },
}


def _require_observation(actual: Any, expected: Any, label: str) -> None:
    if not deep_exact(actual, expected):
        raise StrictDataError(f"independent {label} semantic replay mismatch")


def independent_replays(result_dir: Path, pari_python: Path) -> dict[str, Any]:
    incidence = independent_incidence_replay(result_dir, pari_python)
    group = independent_group_replay(pari_python)
    resolvers = independent_resolver_replay(result_dir, pari_python)
    carrier = independent_carrier_replay(result_dir, pari_python)

    c56_raw, _ = read_stable(C56_CERTIFICATE, max_bytes=2_000_000)
    c56 = strict_json_loads(c56_raw, max_bytes=2_000_000)
    a12, _, _ = strict_gzip_json(
        result_dir / "a12_table.json.gz",
        max_compressed_bytes=40_000_000,
        max_decompressed_bytes=40_000_000,
    )
    theta, _, _ = strict_gzip_json(
        result_dir / "theta_crt.json.gz",
        max_compressed_bytes=1_000_000,
        max_decompressed_bytes=1_000_000,
    )
    g6 = independent_g6_replay(c56["payload"], a12, theta)
    observations = {
        "G1": incidence,
        "G2": group,
        "G3": resolvers,
        "G4": {
            "orientation_separator_prime": incidence["orientation_separator_prime"],
            "oriented_sixer_distinct_values": incidence[
                "oriented_sixer_distinct_values"
            ],
            "all_36_beta_nonzero": incidence["all_36_beta_nonzero"],
            "oriented_stabilizer_order": group["S6_order"],
            "central_swap_order": group["central_swap_order"],
        },
        "G5": carrier,
        "G6": g6,
        "G7": {
            "carrier_line_count": g6["configuration"]["carrier_line_count_each"],
            "all_12_carrier_lines_distinct": g6["configuration"][
                "all_carrier_lines_distinct"
            ],
            "u0_hyperplane_contains_no_carrier_line": g6["configuration"][
                "u0_hyperplane_contains_no_carrier_line"
            ],
            "normalization_q0_value": 1
            if g6["matrix"]["all_cramer_q0_equal_1"]
            else 0,
            "all_restriction_residuals_zero": g6["matrix"][
                "all_restriction_residuals_zero"
            ],
            "oriented_divisor_class_D_multiple_of_d0": group[
                "oriented_divisor_class_D_multiple_of_d0"
            ],
            "oriented_divisor_class_D_nonzero_mod_coboundaries": group[
                "oriented_divisor_class_D_nonzero_mod_coboundaries"
            ],
        },
    }
    validate_independent_replays(observations)
    return observations


def validate_independent_replays(observations: dict[str, Any]) -> None:
    _require_observation(
        observations["G1"],
        {
            "H_text_sha256": "b0f02a13ae60b01f1ec3d781896c5393853a75ff5fb0be517ae4c337c5f7007f",
            "Q_text_sha256": "ebf57460f2349972e99ecd6a4739a1c0e11521a65201c72a0be6665d91038a47",
            "char0_identity": {
                "H_degree": 10,
                "Q_degree": 17,
                "H_Q_monic": True,
                "g_equals_H_times_Q": True,
                "monic_division_recovers_Q": True,
                "H_divides_J": True,
                "H_diagonal_nonzero_in_Qx_mod_g": True,
                "char0_common_factor_lower_bound": 10,
            },
            "good_specialization_primes": list(BRIDGE_PRIMES),
            "graph_sha256_by_prime": {
                "7": "aaea1ca9c2fa5e0976583f3b8ae13d35b344623e637730ac3f85526ea7f3df38",
                "37": "72939b3118f6cc1d149340363bdbcbded623d3a900ab6c326dd6e72700bfe347",
                "100000000000000000000000000000000000000000000012477": "bf482b36a1f066939319b072d56d78bd511b1967b94550c8d709374ad1367bb8",
            },
            "all_27_H_specializations_equal_monic_modular_gcd": True,
            "rank_specialization_upper_bound": 10,
            "orientation_separator_prime": 37,
            "oriented_sixer_distinct_values": 72,
            "all_36_beta_nonzero": True,
        },
        "G1",
    )
    _require_observation(
        observations["G2"],
        {
            "W_E6_order": 51840,
            "stabilizer_order": 1440,
            "stabilizer_index": 36,
            "core_order": 1,
            "normalizer_order": 1440,
            "U_fixed_double_six_count": 1,
            "S6_order": 720,
            "central_swap_order": 2,
            "generated_order": 1440,
            "line_orbit_sizes": [12, 15],
            "H1_W_Pic_torsion": [],
            "H1_U_Pic_torsion": [2],
            "H1_W_Pic_smith_diagonal": [1, 1, 1, 1, 1, 1],
            "H1_U_Pic_smith_diagonal": [1, 1, 1, 1, 1, 2],
            "W_cocycle_kernel_rank": 6,
            "W_relation_rank": 36,
            "U_cocycle_kernel_rank": 6,
            "U_relation_rank": 36,
            "Pic_S6_invariant_basis": [
                [1, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1],
            ],
            "central_swap_on_h_E_columns": [[5, -2], [12, -5]],
            "anti_invariant_d0_in_h_E": [-2, 1],
            "central_swap_minus_identity_d0_multiples": [-2, -6],
            "Pic_S6_coboundary_lattice": "2 Z*d0",
            "oriented_divisor_class_D_multiple_of_d0": 3,
            "oriented_divisor_class_D_nonzero_mod_coboundaries": True,
        },
        "G2",
    )
    _require_observation(
        observations["G3"],
        {
            "theta_prime_count": 99,
            "theta_modulus_digits": 4951,
            "theta_coefficients_sha256": "845a0cd703b3d5d7c8814f7339010601cc2a25293b6b1bfe792aff2c728e23ea",
            "delta_prime_count": 198,
            "delta_modulus_digits": 9901,
            "delta_required_height_digits": 9858,
            "delta_coefficients_sha256": "d0d90e4513feab467abbf948e39296f4a6cf01569890a55081494258058fecfb",
            "factor_patterns": [[1, 5, 5, 5, 10, 10], [9, 9, 9, 9]],
            "proper_factor_degree_intersection": [],
            "all_primes_proven": True,
            "all_297_orbit_product_congruences_replayed": True,
        },
        "G3",
    )
    _require_observation(
        observations["G4"],
        {
            "orientation_separator_prime": 37,
            "oriented_sixer_distinct_values": 72,
            "all_36_beta_nonzero": True,
            "oriented_stabilizer_order": 720,
            "central_swap_order": 2,
        },
        "G4",
    )
    _require_observation(
        observations["G5"],
        {
            "carrier_table_sha256": "72d4aef5120926ec09904b08219cba7cf2b49323bd085d05274e5c17e1ed90a1",
            "prime_count": 1048,
            "modulus_digits": 100609,
            "all_468_congruences_bounds_units": True,
            "carrier_degree": 12,
            "complement_degree": 15,
            "division_field_multiplication_count": 208,
            "forward_convolution_field_multiplication_count": 208,
            "all_28_coefficients_exact": True,
            "complement_table_sha256": "b922484d59786a850fc8d13283366e2536c21eae56c5aaae1908b91bc7edbc0f",
        },
        "G5",
    )
    g6 = observations["G6"]
    required_g6 = {
        ("checker_id",): "hcs-c57-g6-alt-inline-pure-python-v1",
        ("status",): "PASS",
        ("backend",): "pure_python_polynomial_basis_F_7_power_6",
        ("finite_field", "prime"): 7,
        ("finite_field", "degree"): 6,
        ("finite_field", "order"): 117649,
        ("finite_field", "modulus_irreducible"): True,
        ("configuration", "eliminant_root_count"): 27,
        ("configuration", "frobenius_factor_degrees"): [3, 3, 3, 3, 3, 6, 6],
        ("configuration", "meeting_pair_count"): 135,
        ("configuration", "sixer_count"): 72,
        ("configuration", "double_six_count"): 36,
        ("configuration", "carrier_line_count_each"): 12,
        ("configuration", "all_carrier_lines_distinct"): True,
        ("configuration", "all_carrier_specializations_match_A12"): True,
        ("configuration", "u0_hyperplane_contains_no_carrier_line"): True,
        ("theta", "distinct_value_count"): 36,
        ("theta", "all_R_theta_at_theta_D_zero"): True,
        ("theta", "orbit_product_equals_R_theta_mod_7"): True,
        ("gauge", "determinant_over_Z"): 31778526453059635681033276764499400992765201,
        ("gauge", "determinant_nonzero_mod_7"): True,
        ("matrix", "count"): 36,
        ("matrix", "shape_each"): [60, 31],
        ("matrix", "fixed_minor_shape"): [30, 30],
        ("matrix", "all_fixed_pivot_determinants_nonzero"): True,
        ("matrix", "pivot_determinant_norm_mod_7"): 3,
        ("matrix", "normalization_monomial"): [2, 2, 0, 0],
        ("matrix", "all_cramer_q0_equal_1"): True,
        ("matrix", "zero_restriction_residual_count"): 2160,
        ("matrix", "all_restriction_residuals_zero"): True,
    }
    for path, expected in required_g6.items():
        value = g6
        for component in path:
            if type(value) is not dict or component not in value:
                raise StrictDataError(f"independent G6 missing {path}")
            value = value[component]
        if not deep_exact(value, expected):
            raise StrictDataError(f"independent G6 mismatch at {path}")
    _require_observation(
        observations["G7"],
        {
            "carrier_line_count": 12,
            "all_12_carrier_lines_distinct": True,
            "u0_hyperplane_contains_no_carrier_line": True,
            "normalization_q0_value": 1,
            "all_restriction_residuals_zero": True,
            "oriented_divisor_class_D_multiple_of_d0": 3,
            "oriented_divisor_class_D_nonzero_mod_coboundaries": True,
        },
        "G7 machine inputs",
    )


def expected_payload(
    backends: dict[str, Any],
    source_contract: dict[str, Any],
    g0: dict[str, Any],
    artifact_contract: dict[str, Any],
) -> dict[str, Any]:
    exact_reports = EXPECTED_PRODUCER_EXACT_REPORTS
    return {
        "status_contract": {
            "machine_code_results_status": "PREFREEZE_CODE_RESULTS_PASS",
            "certificate_artifact_status": "PREFREEZE_CODE_RESULTS_PASS",
            "documentation_status": "PAPER_PENDING",
            "project_release_status": "PAPER_PENDING",
            "promotion_authorized": False,
        },
        "backends": backends,
        "C57_source_contract": source_contract,
        "G0_C56_source_lock": g0,
        "artifact_contract": artifact_contract,
        "G1_exact_incidence": {
            "producer_exact_reports": exact_reports["G1"],
            "proof_class": "MACHINE_EXACT_PLUS_RANK_SPECIALIZATION_LEMMA",
            "formula": "J=-Da*Ab*Ac-Db*Dc*Aa",
            "H_text_sha256": "b0f02a13ae60b01f1ec3d781896c5393853a75ff5fb0be517ae4c337c5f7007f",
            "Q_text_sha256": "ebf57460f2349972e99ecd6a4739a1c0e11521a65201c72a0be6665d91038a47",
            "H_degree": 10,
            "Q_degree": 17,
            "H_divides_J_and_g_char0": True,
            "g_equals_H_times_Q_char0": True,
            "diagonal_gcd_degree": 0,
            "good_specialization_primes": list(BRIDGE_PRIMES),
            "all_good_specialization_primes_proven": True,
            "all_eliminant_leading_coefficients_nonzero": True,
            "all_shape_and_H_denominators_units": True,
            "all_specialized_eliminants_squarefree_with_27_roots": True,
            "determinant_formula_equals_divided_J_at_all_good_primes": True,
            "all_27_H_specializations_equal_monic_modular_gcd": True,
            "lower_bound_degree": 10,
            "upper_bound_degree": 10,
            "specialization_direction": "degree_gcd_char0_le_degree_gcd_good_specialization",
            "neighbours_per_line": 10,
            "unordered_edge_count": 135,
            "sixer_count": 72,
            "double_six_count": 36,
            "bridge_graph_sha256": {
                "7": "aaea1ca9c2fa5e0976583f3b8ae13d35b344623e637730ac3f85526ea7f3df38",
                "37": "72939b3118f6cc1d149340363bdbcbded623d3a900ab6c326dd6e72700bfe347",
                "100000000000000000000000000000000000000000000012477": "bf482b36a1f066939319b072d56d78bd511b1967b94550c8d709374ad1367bb8",
            },
            "numeric_residual_sorting_used": False,
        },
        "G2_group_and_H1": {
            "producer_exact_reports": exact_reports["G2"],
            "W_E6_order": 51840,
            "double_six_stabilizer_order": 1440,
            "double_six_stabilizer_index": 36,
            "double_six_stabilizer_core_order": 1,
            "double_six_stabilizer_normalizer_order": 1440,
            "U_fixed_double_six_count": 1,
            "stabilizer_structure": "S6 x C2",
            "oriented_stabilizer_order": 720,
            "central_swap_order": 2,
            "central_swap_nontrivial_and_not_in_S6": True,
            "central_swap_exchanges_sixers": True,
            "line_orbit_sizes": [12, 15],
            "H1_W_Pic_torsion": [],
            "H1_U_Pic_torsion": [2],
            "H1_W_Pic_smith_diagonal": [1, 1, 1, 1, 1, 1],
            "H1_U_Pic_smith_diagonal": [1, 1, 1, 1, 1, 2],
            "W_relation_rank": 36,
            "W_cocycle_kernel_rank": 6,
            "U_relation_rank": 36,
            "U_cocycle_kernel_rank": 6,
            "Pic_S6_invariant_basis": [
                [1, 0, 0, 0, 0, 0, 0],
                [0, 1, 1, 1, 1, 1, 1],
            ],
            "central_swap_on_h_E_columns": [[5, -2], [12, -5]],
            "anti_invariant_d0_in_h_E": [-2, 1],
            "Pic_S6_coboundary_lattice": "2 Z*d0",
            "oriented_divisor_class_D_multiple_of_d0": 3,
            "oriented_divisor_class_D_nonzero_mod_coboundaries": True,
            "global_minimality_proof_class": "LITERATURE_CLASSIFICATION_BRIDGE",
            "locator_required": True,
            "two_primary_case_split": {
                "Z_over_2": "H is contained in a conjugate of U1; index 36",
                "Z_over_2_squared": "H is contained in a conjugate of U3; index 720=36*20",
                "common_consequence": "36 divides [K intersect L:Q], and [K intersect L:Q] divides [L:Q] for every finite L/Q with nonzero 2-primary quotient",
                "degree_36_equality_consequence": "the subgroup is conjugate to U1",
                "degree_36_equality_field_consequence": "L=K intersect L=K^U1 (up to conjugate embedding)",
            },
            "machine_does_not_classify_all_two_primary_subgroups": True,
        },
        "G3_resolvers_and_fixed_field": {
            "producer_exact_reports": exact_reports["G3"],
            "theta_CRT_prime_count": 99,
            "theta_CRT_modulus_digits": 4951,
            "theta_coefficients_sha256": "845a0cd703b3d5d7c8814f7339010601cc2a25293b6b1bfe792aff2c728e23ea",
            "delta_CRT_prime_count": 198,
            "delta_CRT_modulus_digits": 9901,
            "delta_required_height_digits": 9858,
            "delta_coefficients_sha256": "d0d90e4513feab467abbf948e39296f4a6cf01569890a55081494258058fecfb",
            "candidate_input_used": False,
            "all_CRT_primes_proven_and_orbit_products_replayed": True,
            "two_reduction_factor_patterns": [[1, 5, 5, 5, 10, 10], [9, 9, 9, 9]],
            "proper_factor_degree_intersection": [],
            "theta_and_delta_irreducible_degree": 36,
            "delta_is_primary_fixed_field_and_radicand_authority": True,
            "theta_is_auxiliary_primitive_for_G5": True,
            "same_D_fixed_field_bridge": "WRITTEN_STABILIZER_AND_SEPARATING_ORBIT_BRIDGE",
            "delta_equals_polynomial_in_theta_required": False,
            "ordinary_S27_sign_argument_used": False,
        },
        "G4_orientation_quadratic": {
            "producer_exact_reports": exact_reports["G4"],
            "beta_definition": "sum_A(alpha)-sum_B(alpha)",
            "delta_definition": "beta^2",
            "oriented_stabilizer_order": 720,
            "central_swap_beta_sign": -1,
            "oriented_sixer_separator_is_proven_good_prime": True,
            "oriented_sixer_separator_prime": 37,
            "oriented_sixer_distinct_values": 72,
            "double_six_delta_distinct_values": 36,
            "all_36_beta_nonzero": True,
            "quadratic_extension_bridge": "WRITTEN_STABILIZER_BRIDGE_K_S6_EQUALS_F_D_SQRT_DELTA",
        },
        "G5_degree_12_carrier": {
            "producer_exact_reports": exact_reports["G5"],
            "carrier_table_shape": [13, 36],
            "carrier_table_sha256": "72d4aef5120926ec09904b08219cba7cf2b49323bd085d05274e5c17e1ed90a1",
            "original_candidate_source_sha256": "810ca69f08dae07b2978f6cc9d441638e6c79a8bcfd6a771c4a895f6b0d1b17d",
            "candidate_blind_CRT_prime_count": 1048,
            "candidate_blind_CRT_modulus_digits": 100609,
            "all_468_congruences_bounds_and_units_replayed": True,
            "stability_heuristic_used": False,
            "A_degree": 12,
            "B_degree": 15,
            "A_monic_and_subtop_minus_theta_over_leading_g": True,
            "division_field_multiplication_count": 208,
            "forward_convolution_field_multiplication_count": 208,
            "all_28_remainders_zero_and_forward_coefficients_equal": True,
            "complement_table_sha256": "b922484d59786a850fc8d13283366e2536c21eae56c5aaae1908b91bc7edbc0f",
            "authority": "EXACT_A12_TIMES_B15_EQUALS_G_IN_Q_THETA",
        },
        "G6_determinant_quartic_and_rank": {
            "producer_exact_reports": exact_reports["G6"],
            "matrix_shape": [60, 31],
            "normalization_monomial": [2, 2, 0, 0],
            "normalization_q0_value": 1,
            "normalization_q0_nonzero": True,
            "gauge_block_from_C56_cubic": [
                [75081586157, 0, 0, 0],
                [-28576620789, 75081586157, 0, 0],
                [-122000922135, 0, 75081586157, 0],
                [-5364921951, 0, 0, 75081586157],
            ],
            "gauge_determinant": 31778526453059635681033276764499400992765201,
            "pivot_rows_zero_based": [
                0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14, 15,
                16, 17, 18, 19, 20, 24, 25, 26, 27, 28, 29, 36, 37, 38, 48,
            ],
            "pivot_determinant_theta_coefficients_sha256": "1af5bfdc9b2f945094835fd81281305fb84dfc8208cb542874f2803420cd3a9e",
            "pivot_determinant_norm_mod_7": 3,
            "canonical_q_solution_sha256": "eb9e803e16f5623647843dd7636fe3d511af60f8f31c453ea6826cd3e4d25573",
            "all_36_theta_values_distinct_and_orbit_product_equal": True,
            "all_36_times_60_restriction_equations_zero": True,
            "rank_at_least_30_machine": True,
            "rank_at_most_30_and_kernel_existence_proof_class": "WRITTEN_HILBERT90_O4_GEOMETRIC_BRIDGE",
            "determinant_defined_Q_authority": True,
            "expanded_Q_required": False,
        },
        "G7_divisor_and_quaternion": {
            "producer_exact_reports": exact_reports["G7"],
            "carrier_line_count": 12,
            "all_12_carrier_lines_distinct": True,
            "normalization_q0_crossref_G6_value": 1,
            "Q_nonzero_mod_F_times_linear": True,
            "u0_hyperplane_contains_no_carrier_line": True,
            "quartic_divisor_H_degree": 12,
            "carrier_union_H_degree": 12,
            "multiplicity_at_least_one_on_each_carrier_line": True,
            "degree_exhaustion_no_residual_or_extra_multiplicity": True,
            "divisor_Q": "E+G",
            "oriented_divisor_D": "E-2H0",
            "divisor_f_for_f_equals_Q_over_u0_fourth": "E+G-4H0",
            "norm_D_equals_divisor_f": True,
            "norm_divisor_bridge_proof_class": "WRITTEN_EXACT_RESTRICTION_AND_DEGREE_EXHAUSTION",
            "cyclic_algebra": "(F_D_prime/F_D,Q/u0^4)",
            "quaternion": "(delta,Q/u0^4)",
            "cyclic_and_quaternion_presentations_identified": True,
            "unramifiedness_proof_class": "WRITTEN_CYCLIC_NORM_DIVISOR_CRITERION",
            "unramified": True,
            "unramifiedness_does_not_imply_nonzero": True,
            "Pic_S6_coordinates": {
                "basis": ["h", "eSigma"],
                "hyperplane_H0": [3, -1],
                "anti_invariant_d0": [-2, 1],
                "oriented_divisor_D": [-6, 3],
            },
            "central_swap_d0_sign": -1,
            "kernel_one_plus_central_swap_on_Pic_S6": "Z*d0",
            "central_swap_minus_one_image_on_Pic_S6": "2 Z*d0",
            "oriented_divisor_class_D_multiple_of_d0": 3,
            "oriented_divisor_class_D_nonzero_mod_coboundaries": True,
            "Hochschild_Serre_Brbar_and_H3_hypotheses_required": True,
            "cyclic_class_nonzero_proof_class": "WRITTEN_CLASS_MAP_BRIDGE_REQUIRED",
            "machine_does_not_claim_Hochschild_Serre_class_map": True,
            "written_conclusion_Br_quotient": "Z/2 generated by (delta,Q/u0^4)",
        },
        "nonresults_firewall": {
            "pari_direct_incidence_factor_lane": {
                "status": "TIMEOUT_NON_RESULT",
                "certificate_dependency": False,
                "noninput": True,
            },
            "expanded_quartic_lane": {
                "status": "BOUNDED_NON_RESULT",
                "certificate_dependency": False,
                "noninput": True,
            },
            "delta_as_polynomial_in_theta_lane": {
                "status": "BOUNDED_NON_RESULT",
                "certificate_dependency": False,
                "noninput": True,
            },
        },
        "scope_firewall": {
            "general_degree_36_resolvent_novelty_claimed": False,
            "delta_equals_polynomial_in_theta_claimed": False,
            "expanded_quartic_coefficients_claimed": False,
            "local_quaternion_evaluation_claimed": False,
            "rational_points_claimed": False,
            "absence_of_rational_points_claimed": False,
            "Hasse_failure_claimed": False,
            "weak_approximation_claimed": False,
            "Brauer_Manin_obstruction_claimed": False,
            "full_local_inertia_claimed": False,
            "Artin_conductors_claimed": False,
            "bad_Euler_factors_claimed": False,
            "root_numbers_claimed": False,
            "stable_rationality_novelty_claimed": False,
            "stable_irrationality_claimed": False,
            "surface_rationality_claimed": False,
            "arbitrary_cubic_surfaces_theorem_claimed": False,
            "later_batch_theorem_claimed": False,
            "all_Yukawa_or_Henon_surfaces_theorem_claimed": False,
            "motives_claimed": False,
            "VHS_realization_claimed": False,
            "Calabi_Yau_realization_claimed": False,
            "automorphy_claimed": False,
            "dynamics_claimed": False,
            "Riemann_Hypothesis_claimed": False,
            "Hilbert_Polya_operator_claimed": False,
            "local_Picard_Artin_package_claimed": False,
            "temporary_digest_accepted_as_release_provenance": False,
            "paper_complete_claimed": False,
            "release_claimed": False,
        },
        "documentation_contract": {
            "status": "PAPER_PENDING",
            "root_document_bytes_are_machine_certificate_inputs": False,
            "paper_bytes_are_machine_certificate_inputs": False,
            "later_document_and_paper_freeze_requires_external_full_project_manifest": True,
        },
    }


def shape_value(value: Any) -> Any:
    if type(value) is dict:
        return {key: shape_value(value[key]) for key in sorted(value)}
    if type(value) is list:
        return [len(value), [shape_value(item) for item in value]]
    if value is None:
        return "null"
    if type(value) is bool:
        return "bool"
    if type(value) is int:
        return "int"
    if type(value) is str:
        return "str"
    raise StrictDataError("unsupported payload leaf type")


def scalar_leaf_count(value: Any) -> int:
    if type(value) is dict:
        return sum(scalar_leaf_count(item) for item in value.values())
    if type(value) is list:
        return sum(scalar_leaf_count(item) for item in value)
    if value is None or type(value) in (bool, int, str):
        return 1
    raise StrictDataError("unsupported payload leaf type")


def leaf_paths(value: Any, prefix: tuple[Any, ...] = ()):
    if type(value) is dict:
        for key in sorted(value):
            yield from leaf_paths(value[key], prefix + (key,))
    elif type(value) is list:
        for index, item in enumerate(value):
            yield from leaf_paths(item, prefix + (index,))
    elif value is None or type(value) in (bool, int, str):
        yield prefix
    else:
        raise StrictDataError("unsupported scalar during rebound sweep")


def mutate_leaf(value: Any) -> Any:
    if type(value) is bool:
        return not value
    if type(value) is int:
        return value + 1
    if type(value) is str:
        return value + "#"
    if value is None:
        # JSON null has no distinct same-type value.  This explicit
        # type-confusion mutation is counted separately by the caller.
        return 0
    raise StrictDataError("unsupported mutation leaf")


def set_path(value: Any, path: tuple[Any, ...], replacement: Any) -> None:
    parent = value
    for component in path[:-1]:
        parent = parent[component]
    parent[path[-1]] = replacement


def schema_descriptor(payload: dict[str, Any]) -> dict[str, Any]:
    return {
        "schema_id": "hcs-c57-certificate-schema-v1",
        "max_certificate_bytes": 2_000_000,
        "payload_top_level_keys": sorted(payload),
        "payload_shape_sha256": sha256_bytes(
            canonical_leaf_bytes(shape_value(payload))
        ),
        "payload_scalar_leaf_count": scalar_leaf_count(payload),
        "unknown_fields_rejected_by_full_leaf_rebuild": True,
        "duplicate_keys_rejected": True,
        "floats_rejected": True,
        "booleans_rejected_in_integer_slots": True,
        "noncanonical_integers_rejected": True,
        "non_UTF8_rejected": True,
        "oversized_input_rejected": True,
        "optimized_python_rejected": True,
        "gzip_mtime_zero_and_deterministic_recompression_required": True,
    }


def core_verify(
    envelope: Any,
    schema: Any,
    expected: dict[str, Any],
    expected_schema: dict[str, Any],
) -> None:
    require_exact_keys(
        envelope,
        {
            "schema_id",
            "schema_descriptor_id",
            "schema_sha256",
            "canonical_schema_sha256",
            "status",
            "paper_status",
            "payload_sha256",
            "payload",
        },
        "C57 certificate envelope",
    )
    require_exact_keys(schema, set(expected_schema), "C57 schema descriptor")
    if (
        type(envelope["schema_id"]) is not str
        or envelope["schema_id"] != "hcs-c57-certificate-v1"
        or type(envelope["schema_descriptor_id"]) is not str
        or envelope["schema_descriptor_id"] != schema["schema_id"]
        or envelope["schema_descriptor_id"] != "hcs-c57-certificate-schema-v1"
        or type(envelope["status"]) is not str
        or envelope["status"] != "PREFREEZE_CODE_RESULTS_PASS"
        or type(envelope["paper_status"]) is not str
        or envelope["paper_status"] != "PAPER_PENDING"
    ):
        raise StrictDataError("C57 envelope identity/status mismatch")
    schema_raw = canonical_json_bytes(schema, pretty=True)
    if (
        type(envelope["schema_sha256"]) is not str
        or envelope["schema_sha256"] != sha256_bytes(schema_raw)
        or type(envelope["canonical_schema_sha256"]) is not str
        or envelope["canonical_schema_sha256"]
        != sha256_bytes(canonical_leaf_bytes(schema))
    ):
        raise StrictDataError("C57 schema digest binding mismatch")
    if (
        type(envelope["payload_sha256"]) is not str
        or envelope["payload_sha256"]
        != sha256_bytes(canonical_leaf_bytes(envelope["payload"]))
    ):
        raise StrictDataError("C57 payload digest binding mismatch")
    if not deep_exact(envelope["payload"], expected):
        raise StrictDataError("C57 full semantic payload rebuild mismatch")
    if not deep_exact(schema, expected_schema):
        raise StrictDataError("C57 schema descriptor rebuild mismatch")


def expect_core_rejection(
    envelope: dict[str, Any],
    schema: dict[str, Any],
    expected: dict[str, Any],
    expected_schema: dict[str, Any],
    label: str,
) -> None:
    parsed_envelope = strict_json_loads(
        canonical_json_bytes(envelope, pretty=True), max_bytes=2_000_000
    )
    parsed_schema = strict_json_loads(
        canonical_json_bytes(schema, pretty=True), max_bytes=100_000
    )
    try:
        core_verify(parsed_envelope, parsed_schema, expected, expected_schema)
    except StrictDataError:
        return
    raise StrictDataError(f"actual verifier accepted mutation: {label}")


def actual_verifier_rebound(
    certificate: dict[str, Any],
    schema: dict[str, Any],
    expected: dict[str, Any],
    expected_schema: dict[str, Any],
) -> dict[str, int]:
    payload_count = 0
    for path in leaf_paths(expected):
        mutant = deepcopy(certificate)
        original = mutant["payload"]
        for component in path:
            original = original[component]
        set_path(mutant["payload"], path, mutate_leaf(original))
        mutant["payload_sha256"] = sha256_bytes(
            canonical_leaf_bytes(mutant["payload"])
        )
        expect_core_rejection(
            mutant, schema, expected, expected_schema, f"payload:{path}"
        )
        payload_count += 1

    schema_count = 0
    for path in leaf_paths(expected_schema):
        mutant_schema = deepcopy(schema)
        original = mutant_schema
        for component in path:
            original = original[component]
        set_path(mutant_schema, path, mutate_leaf(original))
        mutant_certificate = deepcopy(certificate)
        mutant_certificate["schema_sha256"] = sha256_bytes(
            canonical_json_bytes(mutant_schema, pretty=True)
        )
        mutant_certificate["canonical_schema_sha256"] = sha256_bytes(
            canonical_leaf_bytes(mutant_schema)
        )
        expect_core_rejection(
            mutant_certificate,
            mutant_schema,
            expected,
            expected_schema,
            f"schema:{path}",
        )
        schema_count += 1

    type_confusion_count = 0
    for path, replacement in (
        (("status_contract", "promotion_authorized"), 0),
        (("G1_exact_incidence", "H_degree"), True),
    ):
        mutant = deepcopy(certificate)
        set_path(mutant["payload"], path, replacement)
        mutant["payload_sha256"] = sha256_bytes(
            canonical_leaf_bytes(mutant["payload"])
        )
        expect_core_rejection(
            mutant, schema, expected, expected_schema, f"type-confusion:{path}"
        )
        type_confusion_count += 1

    envelope_count = 0
    for key in (
        "schema_id",
        "schema_descriptor_id",
        "schema_sha256",
        "canonical_schema_sha256",
        "status",
        "paper_status",
        "payload_sha256",
    ):
        mutant = deepcopy(certificate)
        mutant[key] = mutate_leaf(mutant[key])
        expect_core_rejection(
            mutant, schema, expected, expected_schema, f"envelope:{key}"
        )
        envelope_count += 1

    structural_count = 0
    structural_mutants = []

    extra = deepcopy(certificate)
    extra["unknown"] = False
    structural_mutants.append(("envelope-extra", extra, schema))
    missing = deepcopy(certificate)
    del missing["status"]
    structural_mutants.append(("envelope-missing", missing, schema))

    extra = deepcopy(certificate)
    extra["payload"]["unknown"] = False
    extra["payload_sha256"] = sha256_bytes(canonical_leaf_bytes(extra["payload"]))
    structural_mutants.append(("payload-extra", extra, schema))
    missing = deepcopy(certificate)
    del missing["payload"]["status_contract"]
    missing["payload_sha256"] = sha256_bytes(canonical_leaf_bytes(missing["payload"]))
    structural_mutants.append(("payload-missing", missing, schema))

    extra_schema = deepcopy(schema)
    extra_schema["unknown"] = False
    extra_certificate = deepcopy(certificate)
    extra_certificate["schema_sha256"] = sha256_bytes(
        canonical_json_bytes(extra_schema, pretty=True)
    )
    extra_certificate["canonical_schema_sha256"] = sha256_bytes(
        canonical_leaf_bytes(extra_schema)
    )
    structural_mutants.append(("schema-extra", extra_certificate, extra_schema))
    missing_schema = deepcopy(schema)
    del missing_schema["schema_id"]
    missing_certificate = deepcopy(certificate)
    missing_certificate["schema_sha256"] = sha256_bytes(
        canonical_json_bytes(missing_schema, pretty=True)
    )
    missing_certificate["canonical_schema_sha256"] = sha256_bytes(
        canonical_leaf_bytes(missing_schema)
    )
    structural_mutants.append(("schema-missing", missing_certificate, missing_schema))

    for label, mutant_certificate, mutant_schema in structural_mutants:
        expect_core_rejection(
            mutant_certificate, mutant_schema, expected, expected_schema, label
        )
        structural_count += 1
    return {
        "payload_scalar_leaves": payload_count,
        "schema_scalar_leaves": schema_count,
        "envelope_metadata_scalar_leaves": envelope_count,
        "explicit_bool_int_type_confusions": type_confusion_count,
        "structural_mutations": structural_count,
        "rebound_mutations_rejected": (
            payload_count
            + schema_count
            + envelope_count
            + type_confusion_count
            + structural_count
        ),
    }


def require_canonical_pretty_json(raw: bytes, *, max_bytes: int, label: str) -> Any:
    value = strict_json_loads(raw, max_bytes=max_bytes)
    if raw != canonical_json_bytes(value, pretty=True):
        raise StrictDataError(f"{label} bytes are not canonical pretty JSON")
    return value


def literal_dict_key_audit() -> int:
    checked = 0
    for name in CODE_SOURCE_FILES:
        if not name.endswith(".py"):
            continue
        raw, _ = read_stable(CODE / name, max_bytes=2_000_000)
        try:
            tree = ast.parse(raw.decode("utf-8", errors="strict"), filename=name)
        except (SyntaxError, UnicodeDecodeError) as exc:
            raise StrictDataError(f"C57 source parse failed: {name}") from exc
        for node in ast.walk(tree):
            if type(node) is not ast.Dict:
                continue
            keys = [
                key.value
                for key in node.keys
                if type(key) is ast.Constant and type(key.value) is str
            ]
            if len(keys) != len(set(keys)):
                raise StrictDataError(f"duplicate literal dictionary key in {name}")
            checked += 1
    return checked


def strict_parser_cases() -> dict[str, int]:
    rejected = 0
    invalid = (
        b'{"a":1,"a":2}',
        b'{"a":-0}',
        b'{"a":01}',
        b'{"a":1.0}',
        b'{"a":NaN}',
        b"\xef\xbb\xbf{}",
        b'{"a":"\xff"}',
    )
    for raw in invalid:
        try:
            strict_json_loads(raw, max_bytes=100)
        except StrictDataError:
            rejected += 1
        else:
            raise StrictDataError("strict parser accepted an invalid case")
    try:
        strict_json_loads(b'{"a":1}', max_bytes=3)
    except StrictDataError:
        rejected += 1
    else:
        raise StrictDataError("strict parser accepted oversized input")
    noncanonical = b' { "a": 1 }\n'
    try:
        require_canonical_pretty_json(
            noncanonical, max_bytes=100, label="hostile noncanonical fixture"
        )
    except StrictDataError:
        rejected += 1
    else:
        raise StrictDataError("file-level canonical gate accepted hostile bytes")
    huge = b'{"a":' + b"9" * 100_000 + b"}"
    parsed_huge = strict_json_loads(huge, max_bytes=len(huge))
    if type(parsed_huge.get("a")) is not int:
        raise StrictDataError("100k-digit canonical integer was not accepted")
    return {
        "invalid_or_noncanonical_cases_rejected": rejected,
        "canonical_100k_digit_integer_accepted": 1,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate", type=Path)
    parser.add_argument("--schema", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--pari-python", type=Path, default=Path("/usr/bin/python3"))
    parser.add_argument(
        "--flint-group-python",
        type=Path,
        default=Path("/root/miniconda3/bin/python3"),
    )
    parser.add_argument("--singular", type=Path, default=Path("/usr/bin/Singular"))
    arguments = parser.parse_args()
    if arguments.output.name != "c57_check_report.json":
        raise StrictDataError("checker output basename is fixed")
    protected = [arguments.certificate, arguments.schema]
    protected.extend(arguments.certificate.parent / name for name in ARTIFACTS)
    protected.extend(CODE.iterdir())
    protected.extend(
        (
            C56_CERTIFICATE,
            C56_SCHEMA,
            C56_CHECK_REPORT,
            C56 / "results/scoped_hash_manifest.json",
            C56 / "route_a_evaluation.yaml",
            C56 / "evaluations/route_a/HCS-C56/20260815T000000Z.yaml",
        )
    )
    (output,) = prepare_output_targets((arguments.output,), protected=protected)
    try:
        reject_optimized_python()
        sys.set_int_max_str_digits(0)
        certificate_raw, certificate_fingerprint = read_stable(
            arguments.certificate, max_bytes=2_000_000
        )
        schema_raw, schema_fingerprint = read_stable(
            arguments.schema, max_bytes=100_000
        )
        certificate = require_canonical_pretty_json(
            certificate_raw, max_bytes=2_000_000, label="certificate"
        )
        schema = require_canonical_pretty_json(
            schema_raw, max_bytes=100_000, label="schema"
        )

        backends = normalized_backends(
            arguments.pari_python,
            arguments.flint_group_python,
            arguments.singular,
        )
        source_before = rebuild_c57_source_contract()
        g0 = rebuild_g0()
        artifacts_before = rebuild_artifacts(arguments.certificate.parent)
        observations = independent_replays(
            arguments.certificate.parent,
            arguments.pari_python.resolve(strict=True),
        )
        expected = expected_payload(
            backends, source_before, g0, artifacts_before
        )
        expected_schema = schema_descriptor(expected)
        core_verify(certificate, schema, expected, expected_schema)
        rebound = actual_verifier_rebound(
            certificate, schema, expected, expected_schema
        )
        parser_report = strict_parser_cases()
        literal_dict_nodes_checked = literal_dict_key_audit()

        if not deep_exact(source_before, rebuild_c57_source_contract()):
            raise StrictDataError("C57 code changed during independent checker replay")
        if not deep_exact(
            artifacts_before, rebuild_artifacts(arguments.certificate.parent)
        ):
            raise StrictDataError("C57 evidence changed during independent checker replay")
        certificate_raw_after, certificate_after = read_stable(
            arguments.certificate, max_bytes=2_000_000
        )
        schema_raw_after, schema_after = read_stable(
            arguments.schema, max_bytes=100_000
        )
        if (
            certificate_raw_after != certificate_raw
            or certificate_after != certificate_fingerprint
            or schema_raw_after != schema_raw
            or schema_after != schema_fingerprint
        ):
            raise StrictDataError("certificate/schema changed during checker replay")

        executed_gates = [f"G{index}" for index in range(8)]
        gate_payload_keys = [
            "G0_C56_source_lock",
            "G1_exact_incidence",
            "G2_group_and_H1",
            "G3_resolvers_and_fixed_field",
            "G4_orientation_quadratic",
            "G5_degree_12_carrier",
            "G6_determinant_quartic_and_rank",
            "G7_divisor_and_quaternion",
        ]
        gate_hashes = {
            gate: sha256_bytes(canonical_leaf_bytes(expected[key]))
            for gate, key in zip(executed_gates, gate_payload_keys)
        }
        report = {
            "schema_id": "hcs-c57-independent-check-v1",
            "result": "PASS_PREFREEZE_CODE_RESULTS",
            "certificate_sha256": certificate_fingerprint.sha256,
            "schema_file_sha256": schema_fingerprint.sha256,
            "payload_sha256": certificate["payload_sha256"],
            "executed_gates": executed_gates,
            "theorem_gate_count": 8,
            "gate_payload_sha256": gate_hashes,
            "evidence_artifact_count": 5,
            "full_semantic_leaf_rebuild": True,
            "independent_checker_does_not_import_or_call_producer_theorem_helpers": True,
            "payload_scalar_leaf_count": scalar_leaf_count(expected),
            "scalar_leaf_rebound": rebound,
            "strict_parser_cases": parser_report,
            "literal_dictionary_nodes_duplicate_key_checked": literal_dict_nodes_checked,
            "scope_firewall_separate_from_theorem_gates": True,
            "machine_and_written_proof_classes_separated": True,
            "unramifiedness_separated_from_nonzero_class_bridge": True,
            "nonresults_excluded_from_dependencies": True,
            "independent_replay_summary_sha256": sha256_bytes(
                canonical_leaf_bytes(observations)
            ),
            "paper_status": "PAPER_PENDING",
            "release_status": "PAPER_PENDING",
        }
        atomic_write(output, canonical_json_bytes(report, pretty=True))
    except BaseException:
        if output.exists() and output.is_file() and not output.is_symlink():
            output.unlink()
        raise
    print("C57 CHECK PASS PREFREEZE")
    print(f"theorem_gates={len(executed_gates)}")
    print(f"rebound_mutations={rebound['rebound_mutations_rejected']}")


if __name__ == "__main__":
    main()
