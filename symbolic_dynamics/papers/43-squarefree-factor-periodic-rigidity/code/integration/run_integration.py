#!/usr/bin/env python3
"""Transactional parent for the exact Paper 43 integration namespace.

All computation and validation occur in disposable staging roots.  The
declared 53 files are installed only after two byte-identical complete stage
builds, a cold relocated build, the adversarial suite, and the read-only
integrity audit succeed.  ``--force-late-failure`` stops after validation and
before the first target write.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path, PurePosixPath
from typing import Any


PYTHON = sys.executable
PENDING = "PENDING_FIRST_ARTIFACT_COMMIT"


def canonical(value: Any) -> bytes:
    return (json.dumps(value, sort_keys=True, indent=2, ensure_ascii=True,
                       separators=(",", ": ")) + "\n").encode("ascii")


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for key, value in pairs:
        if key in output:
            raise ValueError(f"duplicate key: {key}")
        output[key] = value
    return output


def decode(raw: bytes) -> Any:
    value = json.loads(raw.decode("ascii"), object_pairs_hook=unique)
    if canonical(value) != raw:
        raise ValueError("subprocess emitted noncanonical JSON")
    return value


def safe(relative: str) -> bool:
    pure = PurePosixPath(relative)
    return type(relative) is str and bool(relative) and "\\" not in relative \
        and not pure.is_absolute() and all(part not in {".", ".."} for part in pure.parts)


def invoke(script: Path, arguments: list[str], cwd: Path) -> bytes:
    hostile = cwd / "hostile_modules"
    hostile.mkdir(parents=True, exist_ok=True)
    (hostile / "sitecustomize.py").write_text(
        "raise RuntimeError('hostile sitecustomize loaded')\n", encoding="ascii")
    (hostile / "json.py").write_text(
        "raise RuntimeError('hostile json shadow loaded')\n", encoding="ascii")
    env = {
        "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
        "PYTHONPATH": str(hostile),
        "PYTHONDONTWRITEBYTECODE": "1",
    }
    process = subprocess.run(
        [PYTHON, "-I", "-B", str(script), *arguments], cwd=cwd, env=env,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
    )
    if process.returncode != 0:
        detail = process.stderr.decode("utf-8", errors="replace").splitlines()[-3:]
        raise ValueError(f"isolated subprocess failed ({script.name}): {detail}")
    return process.stdout


def static_rows(root: Path) -> list[tuple[str, str]]:
    path = root / "STATIC_INPUT_SHA256SUMS.txt"
    rows = []
    for line in path.read_text(encoding="ascii").splitlines():
        if len(line) < 67 or line[64:66] != "  " or not safe(line[66:]):
            raise ValueError("static manifest row failure")
        rows.append((line[:64], line[66:]))
    paths = [relative for _, relative in rows]
    if paths != sorted(paths) or len(paths) != len(set(paths)):
        raise ValueError("static manifest order/uniqueness failure")
    return rows


def copy_static(root: Path, destination: Path) -> None:
    destination.mkdir(parents=True, exist_ok=False)
    for expected, relative in static_rows(root):
        source = root / relative
        target = destination / relative
        if source.is_symlink() or sha(source.read_bytes()) != expected:
            raise ValueError(f"static byte drift: {relative}")
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
    shutil.copyfile(root / "STATIC_INPUT_SHA256SUMS.txt",
                    destination / "STATIC_INPUT_SHA256SUMS.txt")


def write(path: Path, raw: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw)


def scientific_pipeline(root: Path, scratch: Path) -> dict[str, bytes]:
    unrelated = scratch / "unrelated_cwd"
    unrelated.mkdir(parents=True, exist_ok=True)
    hostile = unrelated / "hostile_modules"
    hostile.mkdir()
    (hostile / "sitecustomize.py").write_text(
        "raise RuntimeError('hostile sitecustomize loaded')\n", encoding="ascii")
    (hostile / "json.py").write_text(
        "raise RuntimeError('hostile json shadow loaded')\n", encoding="ascii")
    naive = subprocess.run(
        [PYTHON, "-c", "import json"], cwd=unrelated,
        env={"PATH": os.environ.get("PATH", "/usr/bin:/bin"),
             "PYTHONPATH": str(hostile)},
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
    )
    isolated = subprocess.run(
        [PYTHON, "-I", "-B", "-c", "import json"], cwd=unrelated,
        env={"PATH": os.environ.get("PATH", "/usr/bin:/bin"),
             "PYTHONPATH": str(hostile)},
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
    )
    if naive.returncode == 0 or isolated.returncode != 0:
        raise ValueError("hostile module-shadow isolation control failed")
    code = root / "code"
    packet = invoke(code / "source/emit_packet.py", [], unrelated)
    packet_path = scratch / "source_packet.json"
    write(packet_path, packet)
    lint = invoke(code / "source/lint_packet.py", [str(packet_path)], unrelated)
    lint_value = decode(lint)
    if lint_value["status"] != "PASS":
        raise ValueError("raw packet linter failed")
    main = invoke(code / "evaluator/evaluate_packet.py", [str(packet_path)], unrelated)
    independent = invoke(code / "evaluator/independent_evaluator.py", [str(packet_path)], unrelated)
    main_value, independent_value = decode(main), decode(independent)
    if main_value["science"] != independent_value["science"]:
        raise ValueError("scientific evaluator object disagreement")
    science = canonical(main_value["science"])
    if sha(science) != main_value["science_sha256"] \
            or sha(science) != independent_value["science_sha256"]:
        raise ValueError("scientific evaluator byte disagreement")
    science_path = scratch / "scientific_results.json"
    write(science_path, science)
    route = invoke(code / "evaluator/evaluate_route_a.py", [str(science_path)], unrelated)
    route_path = scratch / "route.yaml"
    write(route_path, route)
    route_main = invoke(code / "route/validate_route_a.py",
                        [str(route_path), str(science_path)], unrelated)
    route_independent = invoke(code / "route/audit_route_a.py",
                               [str(route_path), str(science_path)], unrelated)
    route_main_value, route_independent_value = decode(route_main), decode(route_independent)
    if route_main_value["status"] != "PASS" or route_independent_value["status"] != "PASS" \
            or route_main_value["normalized_route_sha256"] \
            != route_independent_value["normalized_route_sha256"]:
        raise ValueError("Route validator disagreement")
    return {
        "independent": independent,
        "lint": lint,
        "main": main,
        "packet": packet,
        "route": route,
        "route_independent": route_independent,
        "route_main": route_main,
        "science": science,
    }


def projection(schema: str, payload: Any) -> bytes:
    return canonical({"payload": payload, "schema": schema, "status": "PASS"})


def manifest_bytes(root: Path, paths: list[str]) -> bytes:
    lines = []
    for relative in sorted(paths):
        path = root / relative
        if not path.is_file() or path.is_symlink():
            raise ValueError(f"ledger target missing: {relative}")
        lines.append(f"{sha(path.read_bytes())}  {relative}\n")
    return "".join(lines).encode("ascii")


def complete_tree_manifest(root: Path) -> bytes:
    paths = sorted(path.relative_to(root).as_posix() for path in root.rglob("*")
                   if path.is_file() and not path.is_symlink()
                   and path.relative_to(root).as_posix() != "PAPER_MANIFEST.sha256")
    return manifest_bytes(root, paths)


def verify_paired_states(static_root: Path, stage_root: Path,
                         state_a_route: dict[str, Any], state_a_main: dict[str, Any],
                         state_a_independent: dict[str, Any]) -> None:
    commit = "1" * 40
    science_path = stage_root / "results/scientific_results.json"
    with tempfile.TemporaryDirectory(prefix="paper43_state_pair_") as temporary_name:
        temporary = Path(temporary_name)
        unrelated = temporary / "unrelated_cwd"
        unrelated.mkdir()
        route_b_raw = invoke(static_root / "code/evaluator/evaluate_route_a.py", [
            str(science_path), "--state-b", commit
        ], unrelated)
        route_b = decode(route_b_raw)
        route_b_path = temporary / "route_b.yaml"
        write(route_b_path, route_b_raw)
        main_b = decode(invoke(static_root / "code/route/validate_route_a.py", [
            str(route_b_path), str(science_path)
        ], unrelated))
        independent_b = decode(invoke(static_root / "code/route/audit_route_a.py", [
            str(route_b_path), str(science_path)
        ], unrelated))
        expected_normalized = state_a_main["normalized_route_sha256"]
        if main_b["status"] != "PASS" or independent_b["status"] != "PASS" \
                or main_b["normalized_route_sha256"] != expected_normalized \
                or independent_b["normalized_route_sha256"] != expected_normalized \
                or state_a_independent["normalized_route_sha256"] != expected_normalized:
            raise ValueError("legal paired State-B Route validation failure")
        state_b_root = temporary / "state_B_root"
        shutil.copytree(stage_root, state_b_root)
        write(state_b_root / "evaluations/route_a/SD-C45/2026-08-17.yaml", route_b_raw)
        write(state_b_root / "PAPER_MANIFEST.sha256", complete_tree_manifest(state_b_root))
        state_b_audit = invoke(static_root / "code/integration/audit_integrity.py", [
            str(state_b_root), "--state", "B"
        ], unrelated)
        if state_b_audit != (stage_root / "results/integrity_audit.json").read_bytes():
            raise ValueError("legal State-B integrity audit differs")

        invalid_routes = []
        variants: list[tuple[str, Any]] = []
        unequal = json.loads(json.dumps(route_b))
        unequal["code_commit"] = "2" * 40
        variants.append(("unequal_commit", unequal))
        zero = json.loads(json.dumps(route_b))
        zero["source_commit"] = zero["code_commit"] = zero["source_lock"]["code_commit"] = "0" * 40
        variants.append(("zero_commit", zero))
        nonhex = json.loads(json.dumps(route_b))
        nonhex["source_commit"] = nonhex["code_commit"] = nonhex["source_lock"]["code_commit"] = "g" * 40
        variants.append(("nonhex_commit", nonhex))
        absent = json.loads(json.dumps(route_b))
        absent["authority_integration"]["paper_manifest_present"] = False
        variants.append(("manifest_flag_false", absent))
        stale = json.loads(json.dumps(route_b))
        stale["freeze_note"] = "stale freeze text"
        variants.append(("stale_freeze_note", stale))
        for identifier, value in variants:
            invalid_routes.append({"id": f"provenance_state_b__{identifier}", "route": value})
        batch_path = temporary / "invalid_state_b_routes.json"
        write(batch_path, canonical(invalid_routes))
        for script in (static_root / "code/route/validate_route_a.py",
                       static_root / "code/route/audit_route_a.py"):
            result = decode(invoke(script, ["--batch", str(batch_path), str(science_path)],
                                   unrelated))
            if result["status"] != "PASS" or result["accepted_ids"] \
                    or result["rejected_count"] != len(invalid_routes):
                raise ValueError("mixed State-B Route survived")

        mixed_a_root = temporary / "mixed_A_manifest_root"
        shutil.copytree(stage_root, mixed_a_root)
        write(mixed_a_root / "PAPER_MANIFEST.sha256", complete_tree_manifest(mixed_a_root))
        process = subprocess.run([
            PYTHON, "-I", "-B", str(static_root / "code/integration/audit_integrity.py"),
            str(mixed_a_root), "--state", "A"
        ], cwd=unrelated, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
        if process.returncode == 0:
            raise ValueError("State A with paper manifest survived")
        state_a_bytes = canonical(state_a_route)
        changed = {
            "evaluations/route_a/SD-C45/2026-08-17.yaml"
            if state_a_bytes != route_b_raw else "",
            "PAPER_MANIFEST.sha256",
        } - {""}
        if changed != {"evaluations/route_a/SD-C45/2026-08-17.yaml",
                       "PAPER_MANIFEST.sha256"}:
            raise ValueError("Stage-2 changed-path scope failure")


def build_report(science: dict[str, Any], main: dict[str, Any], independent: dict[str, Any],
                 route_main: dict[str, Any], route_independent: dict[str, Any],
                 adversarial: dict[str, Any], ledger_raw: bytes,
                 exact_output_count: int) -> bytes:
    crt_rows = len(science["crt_proximality"]["control_rows"])
    finite_rows = len(science["finite_p0_sharpness"]["rows"])
    fixed_rows = len(science["periodic_ledger"]["fixed_count_rows"])
    terminal = science["terminal_codes"]
    lines = [
        "# Paper 43 exact integration report",
        "",
        "## Scope and chronology",
        "",
        "This is an independent executable replay of already-known mathematics. "
        "The selector, theorem, literature disposition, and witnesses were known before "
        "the final canonical run. The run is retrospective, nonblind, nonprospective, "
        "and supplies no novelty, priority, predecessor-ranking, or authorization credit.",
        "",
        "## Theorem replay",
        "",
        f"Algorithm C passed {main['checks_passed']}/{main['checks_total']} checks and "
        f"Algorithm F passed {independent['checks_passed']}/{independent['checks_total']} checks. "
        f"They emitted byte-identical science `{sha(canonical(science))}`. The replay checked "
        f"{crt_rows} exact CRT control rows, {finite_rows} finite-P0 rows, and {fixed_rows} "
        "fixed-count coefficients. The universal statements remain proof-schema replays, "
        "not inferences from the finite grid.",
        "",
        "The two implementations use trial-division plus incremental extended-Euclidean CRT "
        "versus a sieve plus simultaneous product-form CRT. Their factor-periodic arguments "
        "use epsilon--delta adjacent-orbit separation versus contradiction with a fixed-anchor "
        "orbit separation. Both preserve the arbitrary compact metrizable factor quantifier.",
        "",
        "The nonempty finite-P0 constructor and the separate empty-P0 two-fixed-point control "
        "both pass. The factor primitive ledger remains a singleton fixed orbit; temporal "
        "traversals are repetitions, not rational-prime primitive species. The one-dimensional "
        "owner `[1]` yields the inverse determinant `1-z` and owns neither the full source nor "
        "the rational-prime comparator.",
        "",
        "## Strict Route disposition",
        "",
        f"The strict Route tuple is `{science['route']['tuple']}` with overall verdict "
        f"`{science['route']['overall_verdict']}` and Route B allowed = "
        f"`{str(science['route']['route_b_invocation_allowed']).lower()}`. Main Route validation "
        f"passed {route_main['checks_passed']}/{route_main['checks_total']}; independent Route "
        f"audit passed {route_independent['checks_passed']}/{route_independent['checks_total']}.",
        "",
        "The exact four-field terminal mapping is:",
        "",
        f"- determinant_comparison: `{terminal['determinant_comparison']}`",
        f"- factor_cycle_creation: `{terminal['factor_cycle_creation']}`",
        f"- literature: `{terminal['literature']}`",
        f"- rational_prime_identification: `{terminal['rational_prime_identification']}`",
        "",
        "`STOP_DUPLICATE` remains a separate conditional literature/claim-boundary control and "
        "is not a strict Route terminal.",
        "",
        "## Adversarial, portability, and seal evidence",
        "",
        f"The frozen mutation registry contains {adversarial['classes_registered']} classes; "
        f"{adversarial['instance_count']} generated instances had "
        f"{adversarial['survivor_count']} survivors. Runs A, B, and relocated cold Run C are "
        "byte-identical for canonical packet, science, evaluator, and Route artifacts. A full "
        "parent rerun regenerates identical bytes, so its changed-path set is empty. State A "
        "and a disposable legal State B normalize to the same scientific Route payload; mixed "
        "states reject.",
        "",
        f"The exact canonical output namespace has {exact_output_count} paths. The self-excluding "
        f"result ledger has {len(ledger_raw.decode('ascii').splitlines())} entries and SHA-256 "
        f"`{sha(ledger_raw)}`.",
        "",
        "## Claim boundary",
        "",
        "Standalone novelty remains 1/10 and internal typed-closure value remains 2/10. "
        "No new proximality mechanism, universal aperiodic-factor theorem, rational-prime owner, "
        "or priority claim is made. If the same typed closure is found in a primary source, "
        "`STOP_DUPLICATE` closes the standalone route and assigns no novelty credit.",
    ]
    return ("\n".join(lines) + "\n").encode("ascii")


def assemble_outputs(static_root: Path, stage_root: Path, first: dict[str, bytes],
                     second: dict[str, bytes], cold: dict[str, bytes]) -> dict[str, bytes]:
    contract = json.loads((static_root / "code/contracts/INTEGRATION_CONTRACT.json").read_text(
        encoding="ascii"))
    expected = contract["exact_output_paths"]
    if len(expected) != 53 or expected != sorted(expected) or len(expected) != len(set(expected)):
        raise ValueError("exact output contract failure")
    canonical_keys = ("packet", "main", "independent", "science", "route", "route_main",
                      "route_independent")
    for key in canonical_keys:
        if first[key] != second[key] or first[key] != cold[key]:
            raise ValueError(f"A/B/C canonical byte mismatch: {key}")
    science = decode(first["science"])
    packet = decode(first["packet"])
    main = decode(first["main"])
    independent = decode(first["independent"])
    route = decode(first["route"])
    route_main = decode(first["route_main"])
    route_independent = decode(first["route_independent"])
    source_index = json.loads((static_root / "inputs/source_snapshot/SOURCE_INDEX.json").read_text(
        encoding="ascii"))
    files: dict[str, bytes] = {}

    def put(relative: str, raw: bytes) -> None:
        if relative in files:
            raise ValueError(f"duplicate output assignment: {relative}")
        files[relative] = raw

    put("evaluations/route_a/SD-C45/2026-08-17.yaml", first["route"])
    put("evaluations/route_a/SD-C45/independent_evaluation.json", first["route_independent"])
    put("results/source_packet.json", first["packet"])
    put("results/main_evaluation.json", first["main"])
    put("results/independent_evaluation.json", first["independent"])
    put("results/scientific_results.json", first["science"])
    put("results/route_evaluation.json", first["route_main"])
    for label, run in (("A", first), ("B", second), ("C", cold)):
        put(f"results/runs/{label}/source_packet.json", run["packet"])
        put(f"results/runs/{label}/main_evaluation.json", run["main"])
        put(f"results/runs/{label}/independent_evaluation.json", run["independent"])
        put(f"results/runs/{label}/scientific_results.json", run["science"])
        put(f"results/runs/{label}/route_evaluation.json", run["route_main"])
    put("results/source_topology_certificate.json",
        projection("paper43-source-topology-certificate-v1", science["source_topology"]))
    put("results/crt_proximality_certificate.json",
        projection("paper43-crt-proximality-certificate-v1", science["crt_proximality"]))
    put("results/factor_contract_certificate.json",
        projection("paper43-factor-contract-certificate-v1", {
            "claim_scope": science["claim_scope"],
            "factor_axioms": science["factor_periodic_rigidity"]["factor_axioms"],
            "universal_aperiodic_factor_theorem_claimed": False,
        }))
    put("results/factor_periodic_rigidity_certificate.json",
        projection("paper43-factor-periodic-rigidity-certificate-v1",
                   science["factor_periodic_rigidity"]))
    put("results/finite_p0_sharpness_certificate.json",
        projection("paper43-finite-p0-sharpness-certificate-v1",
                   science["finite_p0_sharpness"]))
    put("results/source_periodic_collapse_certificate.json",
        projection("paper43-source-periodic-collapse-certificate-v1",
                   science["source_periodic_collapse"]))
    put("results/periodic_ledger_certificate.json",
        projection("paper43-periodic-ledger-certificate-v1", science["periodic_ledger"]))
    put("results/operator_ownership_certificate.json",
        projection("paper43-operator-ownership-certificate-v1", {
            "marker_ledger": science["marker_ledger"],
            "operator_ledger": science["operator_ledger"],
            "type_ledger": science["type_ledger"],
        }))
    put("results/type_contract_certificate.json",
        projection("paper43-type-contract-certificate-v1", {
            "marker_ledger": science["marker_ledger"],
            "type_ledger": science["type_ledger"],
        }))
    put("results/witness_certificate.json",
        projection("paper43-witness-certificate-v1", science["witness_ledger"]))
    put("results/selection_resolver.json",
        projection("paper43-selection-resolver-v1", science["selection"]))
    put("results/source_resolver.json", projection("paper43-source-resolver-v1", {
        "entries": source_index["entries"],
        "external_tree_status": "NOT_QUERIED",
        "matches": len(source_index["entries"]),
        "total": 40,
    }))
    put("results/algorithm_independence.json", projection(
        "paper43-algorithm-independence-v1", {
            "algorithm_C": main["implementation"],
            "algorithm_F": independent["implementation"],
            "canonical_science_byte_identical": True,
            "project_local_import_edges": [],
            "separate_processes": True,
        }))
    put("results/dependency_controls.json", projection("paper43-dependency-controls-v1", {
        "bytecode_disabled": True,
        "external_dependencies": [],
        "hostile_pythonpath_ignored": True,
        "isolated_python": True,
        "live_external_tree": "NOT_QUERIED",
        "network": "NOT_USED",
    }))
    put("results/source_evaluator_boundary.json", projection(
        "paper43-source-evaluator-boundary-v1", {
            "evaluator_reads": ["canonical_raw_packet"],
            "packet_forbidden_derived_answers": True,
            "producer_reads": ["sealed_static_inputs"],
            "shared_project_helpers": [],
        }))
    put("results/external_provenance_stability.json", projection(
        "paper43-external-provenance-stability-v1", {
            "source_count": 40,
            "source_index_sha256": sha(canonical(source_index)),
            "status": "PORTABLE_SNAPSHOT_ONLY_LIVE_TREE_NOT_QUERIED",
        }))
    put("results/immutable_inputs.json", projection("paper43-immutable-inputs-v1", {
        "bindings": contract["immutable_inputs"],
        "mutation_registry_sha256": contract["mutation_registry"]["sha256"],
        "static_manifest_sha256": sha((static_root / "STATIC_INPUT_SHA256SUMS.txt").read_bytes()),
    }))
    put("results/research_reproduction.json", projection("paper43-research-reproduction-v1", {
        "chronology": science["integration_chronology"],
        "claim_scope": science["claim_scope"],
        "theorems": science["theorems"],
    }))
    put("results/route_schema_certificate.json", projection(
        "paper43-route-schema-certificate-v1", {
            "independent_audit": route_independent,
            "renderer_schema": "route-a-evaluator-v0.2.0",
            "strict_validation": route_main,
        }))
    put("results/reproducibility_certificate.json", projection(
        "paper43-reproducibility-certificate-v1", {
            "canonical_artifacts_byte_identical": sorted(canonical_keys),
            "run_labels_serialized_in_science": False,
            "runs": ["A", "B", "C"],
        }))
    put("results/cold_copy_certificate.json", projection("paper43-cold-copy-certificate-v1", {
        "cold_run_C_equals_run_A": True,
        "external_tree_status": "NOT_QUERIED",
        "host_paths_serialized": False,
        "invocation_cwd": "UNRELATED_NONPROJECT_DIRECTORY",
        "relocated_static_copy": True,
    }))
    put("results/idempotence_certificate.json", projection("paper43-idempotence-certificate-v1", {
        "changed_paths_on_complete_parent_rerun": [],
        "internal_complete_stage_builds_compared": 2,
        "physical_writes_on_complete_second_parent_run": 0,
    }))
    put("results/sealed_state_compatibility.json", projection(
        "paper43-sealed-state-compatibility-v1", {
            "legal_states": ["A", "B"],
            "mixed_states_rejected": True,
            "normalized_scientific_route_byte_identical": True,
            "state_b_changed_paths": contract["provenance_states"]["state_b"]["changed_paths"],
        }))
    put("results/integrity_contract.json", projection("paper43-integrity-contract-v1", {
        "exact_output_paths": expected,
        "paper_manifest_forbidden_in_state_a": True,
        "result_ledger_self_excluding": True,
        "static_manifest_sha256": sha((static_root / "STATIC_INPUT_SHA256SUMS.txt").read_bytes()),
    }))
    result_paths = sorted(path for path in expected if path.startswith("results/"))
    put("results/exact_result_set.json", canonical({
        "count": len(result_paths), "paths": result_paths,
        "schema": "paper43-exact-result-set-v1", "status": "PASS",
    }))
    static_paths = [relative for _, relative in static_rows(static_root)] \
        + ["STATIC_INPUT_SHA256SUMS.txt"]
    put("results/exact_text_set.json", canonical({
        "integrator_managed_paths": sorted(static_paths + expected),
        "schema": "paper43-exact-text-set-v1",
        "status": "PASS",
        "writer_owned_authority_paths_excluded": True,
    }))
    put("results/integrity_audit.json", canonical({
        "checks": {
            "authority_overlay_state_valid": True,
            "cache_and_symlink_hygiene": True,
            "canonical_json_types_and_bytes_exact": True,
            "canonical_output_payloads_portable": True,
            "da_binding_exact": True,
            "exact_output_namespace": True,
            "exact_result_ledger": True,
            "exact_result_set_certificate": True,
            "frozen_package_exact": True,
            "immutable_source_snapshot_exact": True,
            "integration_contract_exact": True,
            "packet_science_route_bindings_exact": True,
            "paired_provenance_state_legal": True,
            "route_and_independent_audit_clean": True,
            "static_input_manifest_exact": True,
            "writer_pointer_exact": True,
        },
        "checks_passed": 16,
        "checks_total": 16,
        "schema": "paper43-read-only-integrity-audit-v1",
        "status": "PASS",
    }))
    put("results/analysis_summary.json", b"{}\n")
    put("results/adversarial_tests.json", b"{}\n")
    put("results/SHA256SUMS.txt", b"PLACEHOLDER\n")
    put("EXPERIMENT_REPORT.md", b"# PLACEHOLDER\n")
    if set(files) != set(expected):
        raise ValueError(f"pre-adversarial output assignment mismatch: {sorted(set(expected)-set(files))}")
    for relative, raw in files.items():
        write(stage_root / relative, raw)

    result_ledger_paths = sorted(
        path for path in expected if path.startswith("results/")
        and path != "results/SHA256SUMS.txt"
    )
    mutation_path = stage_root / "results/adversarial_tests.json"
    packet_path = stage_root / "results/source_packet.json"
    science_path = stage_root / "results/scientific_results.json"
    route_path = stage_root / "evaluations/route_a/SD-C45/2026-08-17.yaml"

    def analysis_summary(adversarial_value: dict[str, Any]) -> dict[str, Any]:
        return {
            "canonical_science_sha256": sha(first["science"]),
            "crt_control_failures": 0,
            "crt_control_rows_checked": len(science["crt_proximality"]["control_rows"]),
            "exact_output_path_count": len(expected),
            "finite_p0_failures": 0,
            "finite_p0_rows_checked": len(science["finite_p0_sharpness"]["rows"]),
            "integration_chronology_status": science["integration_chronology"]["status"],
            "mutation_instances": adversarial_value["instance_count"],
            "mutation_survivors": adversarial_value["survivor_count"],
            "route_b_invocation_allowed": False,
            "route_tuple": science["route"]["tuple"],
            "schema": "paper43-analysis-summary-v1",
            "selection_survivors": science["selection"]["survivors"],
            "status": "PASS",
            "theorem_failures": science["theorems"]["failure_count"],
        }

    # Phase one produces a structurally complete, noncanonical baseline result
    # without output-tree mutations.  It lets every phase-two mutation start
    # from an auditor-clean exact namespace instead of a self-certifying
    # placeholder.  These bytes are replaced before the staged tree can leave
    # this function.
    with tempfile.TemporaryDirectory(prefix="paper43_mutation_preflight_") as preflight_name:
        preliminary_raw = invoke(static_root / "code/tests/run_mutations.py", [
            str(packet_path), str(science_path), str(route_path)
        ], Path(preflight_name))
    preliminary = decode(preliminary_raw)
    if preliminary["status"] != "PASS" or preliminary["survivor_count"] != 0:
        raise ValueError("preflight adversarial suite failure")
    write(mutation_path, preliminary_raw)
    write(stage_root / "results/analysis_summary.json",
          canonical(analysis_summary(preliminary)))
    preliminary_ledger = manifest_bytes(stage_root, result_ledger_paths)
    write(stage_root / "results/SHA256SUMS.txt", preliminary_ledger)
    write(stage_root / "EXPERIMENT_REPORT.md",
          build_report(science, main, independent, route_main, route_independent,
                       preliminary, preliminary_ledger, len(expected)))

    # Phase two executes literal disposable-tree mutations and requires the
    # independent read-only auditor to reject each mutated copy.
    with tempfile.TemporaryDirectory(prefix="paper43_mutation_parent_") as mutation_cwd_name:
        unrelated = Path(mutation_cwd_name)
        mutation_raw = invoke(static_root / "code/tests/run_mutations.py", [
            str(packet_path), str(science_path), str(route_path), "--output-root", str(stage_root)
        ], unrelated)
    adversarial = decode(mutation_raw)
    if adversarial["status"] != "PASS" or adversarial["survivor_count"] != 0:
        raise ValueError("adversarial suite failure")
    write(mutation_path, mutation_raw)
    write(stage_root / "results/analysis_summary.json",
          canonical(analysis_summary(adversarial)))
    ledger_raw = manifest_bytes(stage_root, result_ledger_paths)
    write(stage_root / "results/SHA256SUMS.txt", ledger_raw)
    report = build_report(science, main, independent, route_main, route_independent,
                          adversarial, ledger_raw, len(expected))
    write(stage_root / "EXPERIMENT_REPORT.md", report)
    verify_paired_states(static_root, stage_root, route, route_main, route_independent)
    return {relative: (stage_root / relative).read_bytes() for relative in expected}


def generate(root: Path, workspace: Path) -> dict[str, bytes]:
    audit = invoke(root / "code/integration/audit_integrity.py",
                   [str(root), "--static-only"], workspace)
    if decode(audit)["status"] != "PASS":
        raise ValueError("static integrity audit failure")
    run_a_root = workspace / "run_A"
    run_b_root = workspace / "run_B"
    run_c_root = workspace / "relocated_installation_C"
    copy_static(root, run_a_root)
    copy_static(root, run_b_root)
    copy_static(root, run_c_root)
    run_a = scientific_pipeline(run_a_root, workspace / "scratch_A")
    run_b = scientific_pipeline(run_b_root, workspace / "scratch_B")
    run_c = scientific_pipeline(run_c_root, workspace / "scratch_C")
    assembled = workspace / "assembled"
    copy_static(root, assembled)
    outputs = assemble_outputs(root, assembled, run_a, run_b, run_c)
    final_audit = invoke(root / "code/integration/audit_integrity.py",
                         [str(assembled), "--state", "A"], workspace)
    if final_audit != outputs["results/integrity_audit.json"]:
        raise ValueError("read-only integrity stdout differs from canonical certificate")
    return outputs


def existing_output_set(root: Path) -> set[str]:
    output = set()
    if (root / "EXPERIMENT_REPORT.md").is_file():
        output.add("EXPERIMENT_REPORT.md")
    for base_name in ("results", "evaluations"):
        base = root / base_name
        if base.exists():
            for path in base.rglob("*"):
                if path.is_file() or path.is_symlink():
                    output.add(path.relative_to(root).as_posix())
    return output


def main(argv: list[str]) -> int:
    if not sys.flags.isolated or not sys.dont_write_bytecode:
        raise RuntimeError("run_integration.py requires python3 -I -B")
    if not argv or len(argv) > 2 or (len(argv) == 2 and argv[1] != "--force-late-failure"):
        raise SystemExit("usage: run_integration.py ROOT [--force-late-failure]")
    root = Path(argv[0]).resolve()
    force_failure = len(argv) == 2
    contract = json.loads((root / "code/contracts/INTEGRATION_CONTRACT.json").read_text(
        encoding="ascii"))
    expected = set(contract["exact_output_paths"])
    existing = existing_output_set(root)
    if existing and existing != expected:
        raise ValueError("target has a partial or extra output namespace")
    before = {relative: sha((root / relative).read_bytes()) for relative in existing}
    with tempfile.TemporaryDirectory(prefix="paper43_transaction_") as first_name:
        first_outputs = generate(root, Path(first_name))
        with tempfile.TemporaryDirectory(prefix="paper43_transaction_replay_") as second_name:
            second_outputs = generate(root, Path(second_name))
    if first_outputs != second_outputs or set(first_outputs) != expected:
        raise ValueError("two complete staged parents are not byte-identical")
    if force_failure:
        after = {relative: sha((root / relative).read_bytes()) for relative in existing}
        if before != after or existing_output_set(root) != existing:
            raise ValueError("late-failure path changed target")
        sys.stdout.buffer.write(canonical({
            "exact_output_path_count": len(expected),
            "failure_point": "AFTER_FULL_STAGE_VALIDATION_BEFORE_TARGET_WRITE",
            "physical_writes": 0,
            "schema": "paper43-transaction-parent-status-v1",
            "status": "FORCED_LATE_FAILURE_TARGET_UNCHANGED",
            "target_changed_paths": [],
        }))
        return 23
    changed = []
    for relative in sorted(expected):
        path = root / relative
        raw = first_outputs[relative]
        if path.is_file() and path.read_bytes() == raw:
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = path.with_name(path.name + ".paper43-new")
        temporary.write_bytes(raw)
        os.replace(temporary, path)
        changed.append(relative)
    if existing_output_set(root) != expected:
        raise ValueError("post-install output exact-set failure")
    stdout = {
        "exact_output_path_count": len(expected),
        "physical_writes": len(changed),
        "schema": "paper43-transaction-parent-status-v1",
        "status": "FINAL" if changed else "IDEMPOTENT_NO_WRITES",
        "target_changed_paths": changed,
    }
    sys.stdout.buffer.write(canonical(stdout))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
