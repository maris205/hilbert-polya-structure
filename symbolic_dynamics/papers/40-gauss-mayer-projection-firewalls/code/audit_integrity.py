#!/usr/bin/env python3
"""Read-only, State-A/State-B-stable integrity audit for Paper 40."""

from __future__ import annotations

import ast
from base64 import b64decode
from hashlib import sha256
from importlib.metadata import version as distribution_version
import importlib.util
import json
from pathlib import Path
import re
import sys
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_REL = "code/contracts/INTEGRATION_CONTRACT.json"
CONTRACT_SHA256 = "d03079f89cda8ce3b92c8ff2e961df99fcbb20e9d132cb8b1b51199b81aaf06f"
ROUTE_REL = "evaluations/route_a/SD-C42/2026-08-17.yaml"
MANIFEST_REL = "PAPER_MANIFEST.sha256"
SCIENCE_SHA256 = "340aff6f08e7cf9360d57d34ff9c66e99f9322343b3069fe37e5acc2f55aa7c5"
MUTATION_REGISTRY_SHA256 = "cdacd81a8817845cfe68e464d333fbff5c45e8fa8fb4208a72f00debc494b7f4"
ROUTE_SCHEMA_FIXTURE_SHA256 = "15e47752d6134ec7ddc8f36329a3f7139031122ead7a90af6b876840c1ac5bfa"
ROUTE_SKILL_SHA256 = "29bd6275aa0c80ecce9cca898f06687208475c0a9a40cf3b9592fde45951458a"
ROUTE_SKILL_REL = "docs/inputs/route-a-evaluator-v0.2.0.md.b64"
RESEARCH_MANIFEST_SHA256 = "530f8a989d1e0f29e4ca51342d121a4e358d60692e659b18d136b9236e95c55e"
RESEARCH_POINTER_SHA256 = "e985b438395225f454fc60e6e913e1e2b6f1fd6781c24bb3f703778e415fb4e5"
RESEARCH_FILES = {
    "COUNTEREXAMPLES.md": "b86a431c61ed11c409090c81bbb6660f16343cc9ee1ecbadd902e92d86b8fb5f",
    "DERIVATION_PACKAGE.md": "7f1f80637b8dbadf95461245419529180243faec08637e306b79da76389229ea",
    "LITERATURE_BOUNDARY_ADDENDUM.md": "fb2cdae0e4b1aa662a3426d7d569a926d94b5bf7b2b36b5de0e8bc77f6ffb9fb",
    "LITERATURE_NOVELTY_AUDIT.md": "79982d110318ca29a9f579d8498a4b110da742450f6e0011f2164067ac20a3e8",
    "MAYER_SOURCE_BOUNDARY.md": "a9dcbc922f8c47b0b845e7c6e76422aad3a0e744940a6529c2172176f5725bc5",
    "OBJECT_OWNERSHIP.md": "7cda0257d99547b8dd28f8c7e5fc0c315e34fcb0e2724f10d75a40dfd3553e7f",
    "PRIMITIVITY_TYPE_FIREWALL.md": "5280a3ef22fcfef0078ed4e162246aa6cc516135aece0a53f78ce8fad2ca18a8",
    "PROOF_PACKAGE.md": "9ae5b6220ba1fde93b4592e6ec1b1dd78289248f376b7ef395b96dc815e9aa8e",
    "ROUTE_STATUS_AUDIT.md": "4fb51559b79420f5515698b0f3b069d94c46736c9ef8e4f999041f2ed81a3c07",
    "SELECTION_AUDIT.md": "0739263b6da1795bfa693ba2600e92a87fd973d9af08398d505a8fa4afa3190c",
    "SOURCE_LOCK.md": "2269e06576dd20c513c5ca9482cb49d36678e07358aaf80f2f08b33806b87041",
}
PLAN_HASHES = {
    "experiments/EXPERIMENT_PLAN.md": "dbae7e5317bea10e623f957ee75389392de7cfd8d55b17965ce710ff78364b2d",
    "experiments/PREREGISTRATION.md": "f1643899ea7ac62e916b24fc265a4ee2ce1d042e2e078d7b336662ab2a065908",
}
KNOWN_OUTPUT_HASHES = {
    "results/control_reference.json": "d0be9630e4f0710c1f602e14e517939f6eef21c582934d79f795a9871f45a30f",
    "results/control_independent.json": "729287849f36046b8aa21d8dba615650f4289dd1d3202c1783cc41af207c4d92",
    "results/prototype_reference.json": "2fee7701a08ec4f7e019863c6e86bf6fb884bf0323e5593e4bf946ef35e7a995",
    "results/prototype_independent.json": "78a1846b19cffde3c21642e6220b893a82690adaee5314ff6be2b19e7265fe38",
}
EXPECTED_STATIC_SEAL_IDS = {
    "main_forbidden_source_import", "independent_forbidden_source_import",
    "undeclared_third_party_import", "result_missing_path", "result_extra_path",
    "wrong_pyyaml_runtime_version",
    "result_duplicate_path", "managed_text_missing_path", "managed_text_extra_path",
    "managed_text_duplicate_path",
    "host_absolute_runtime_token",
    "manifest_present_with_pending_triple", "sealed_triple_without_manifest",
    "sealed_manifest_mismatched_triple", "sealed_manifest_inaccurate_note",
    "sealed_manifest_wrong_hash", "sealed_manifest_unsorted",
    "sealed_manifest_duplicate_path", "sealed_manifest_self_included",
    "sealed_manifest_missing_path", "sealed_uppercase_commit", "sealed_zero_commit",
}


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=True) + "\n").encode("ascii")


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def parse_json(relative: str) -> Any:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def python_imports(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    output: set[str] = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            output.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            output.add(node.module.split(".")[0])
    return output


def text_hygiene(path: Path) -> bool:
    raw = path.read_bytes()
    try:
        raw.decode("utf-8")
    except UnicodeDecodeError:
        return False
    if raw.startswith(b"\xef\xbb\xbf") or b"\r" in raw:
        return False
    if not raw.endswith(b"\n") or raw.endswith(b"\n\n"):
        return False
    if any(line.rstrip(b" \t") != line for line in raw.splitlines()):
        return False
    return not any(byte < 32 and byte not in (9, 10) for byte in raw)


def files_below(relative: str) -> list[str]:
    base = ROOT / relative
    return sorted(path.relative_to(ROOT).as_posix() for path in base.rglob("*") if path.is_file())


def whole_authority_text_inventory() -> list[str]:
    """Dynamically enumerate every non-PDF authority file except the Stage-2 manifest.

    The immutable integration ledger deliberately has a narrower ownership scope.
    This inventory is recomputed on every audit so mutable writer prose, TeX,
    bibliography, and figure sources are nevertheless covered by the hygiene gate.
    The root manifest is excluded so legal State A and State B audit bytes agree.
    """
    return sorted(
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.is_file()
        and path.relative_to(ROOT).as_posix() != MANIFEST_REL
        and path.suffix.lower() != ".pdf"
    )


def load_route_module() -> Any:
    path = ROOT / "code/evaluator/evaluate_route_a.py"
    spec = importlib.util.spec_from_file_location("paper40_route_audit", path)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load Route validator")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def manifest_state() -> dict[str, bool]:
    route_module = load_route_module()
    manifest = ROOT / MANIFEST_REL
    present = manifest.exists() or manifest.is_symlink()
    regular = manifest.is_file() and not manifest.is_symlink()
    try:
        route = route_module.parse_route((ROOT / ROUTE_REL).read_bytes())
        route_checks = route_module.validate_semantics(route, manifest_present=present)
    except Exception:
        route_checks = {"route_parse": False}
    state_name = route_module.paired_state(route, present) if "route" in locals() else "INVALID"

    format_valid = True
    sorted_unique = True
    paths_safe = True
    self_excluded = True
    exact_set = True
    hashes_valid = True
    if present and not regular:
        format_valid = sorted_unique = paths_safe = self_excluded = exact_set = hashes_valid = False
    elif regular:
        raw = manifest.read_bytes()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            text = ""
            format_valid = False
        format_valid = (
            format_valid and not raw.startswith(b"\xef\xbb\xbf") and b"\r" not in raw
            and raw.endswith(b"\n") and not raw.endswith(b"\n\n")
            and all(line.rstrip(" \t") == line for line in text.splitlines())
        )
        rows: list[tuple[str, str]] = []
        for line in text.splitlines():
            match = re.fullmatch(r"([0-9a-f]{64})  ([^\n]+)", line)
            if match is None:
                format_valid = False
            else:
                rows.append((match.group(2), match.group(1)))
        declared = [relative for relative, _ in rows]
        sorted_unique = declared == sorted(set(declared))
        paths_safe = all(
            relative and relative.strip() == relative and not relative.startswith(("/", "./"))
            and ".." not in Path(relative).parts and Path(relative).as_posix() == relative
            for relative in declared
        )
        self_excluded = MANIFEST_REL not in declared
        actual = sorted(
            path.relative_to(ROOT).as_posix() for path in ROOT.rglob("*")
            if path.is_file() and path != manifest
        )
        exact_set = declared == actual
        hashes_valid = format_valid and paths_safe and self_excluded and all(
            (ROOT / relative).is_file() and digest(ROOT / relative) == expected
            for relative, expected in rows
        )

    valid_manifest = all((format_valid, sorted_unique, paths_safe, self_excluded, exact_set, hashes_valid))
    return {
        "paired_exactly_one_legal_state": state_name == "VALID_PAIRED_STATE" and ((not present) or regular),
        "paired_route_recursive_semantics": len(route_checks) == 18 and all(route_checks.values()),
        "paired_manifest_presence_matches_state": (not present) or regular,
        "paired_manifest_format": format_valid,
        "paired_manifest_sorted_unique": sorted_unique,
        "paired_manifest_safe_paths": paths_safe,
        "paired_manifest_self_excluded": self_excluded,
        "paired_manifest_exact_set": exact_set,
        "paired_manifest_hashes": hashes_valid,
        "paired_manifest_valid_for_state": valid_manifest,
    }


def main() -> int:
    checks: dict[str, bool] = {}

    def check(name: str, value: Any) -> None:
        checks[name] = bool(value)

    for name, value in manifest_state().items():
        check(name, value)

    contract_path = ROOT / CONTRACT_REL
    contract = parse_json(CONTRACT_REL)
    check("contract_hash", digest(contract_path) == CONTRACT_SHA256)
    result_paths = contract.get("result_paths", [])
    managed_paths = contract.get("managed_text_paths", [])
    ledger_paths = contract.get("ledger_paths", [])
    check("contract_counts", contract.get("counts") == {
        "code": 11, "docs": 21, "evaluations": 2, "experiments": 2,
        "ledger": 102, "managed_text": 104, "packet_mutations": 164,
        "results": 54, "route_distinct_payloads": 409,
        "route_explicit_mutations": 24, "route_recursive_mutations": 398,
        "static_and_seal_mutations": 22,
    })
    check("integration_managed_text_scope", contract.get("managed_text_scope") ==
          "INTEGRATION_OWNED_OUTPUTS_PLUS_IMMUTABLE_RESEARCH_INPUTS")
    check("writer_mutable_text_policy", contract.get("writer_mutable_text_policy") ==
          "EXCLUDED_FROM_IMMUTABLE_INTEGRATION_LEDGER; DYNAMICALLY_ENUMERATED_AND_HYGIENE_AUDITED_ACROSS_THE_WHOLE_AUTHORITY_TREE")
    check("exact_code_set", files_below("code") == contract.get("code_paths"))
    check("exact_doc_set", files_below("docs") == contract.get("doc_paths"))
    check("exact_experiment_set", files_below("experiments") == contract.get("experiment_paths"))
    check("exact_evaluation_set", files_below("evaluations") == contract.get("evaluation_paths"))
    check("exact_result_set", files_below("results") == result_paths)
    check("result_paths_sorted_unique", result_paths == sorted(set(result_paths)))
    check("result_set_certificate", parse_json("results/exact_result_set.json") == {
        "schema": "paper40-exact-result-set-v1", "count": len(result_paths), "paths": result_paths,
    })
    check("text_set_certificate", parse_json("results/exact_text_set.json") == {
        "schema": "paper40-exact-text-set-v1", "count": len(managed_paths), "paths": managed_paths,
    })
    check("integration_managed_text_all_present", all((ROOT / relative).is_file() for relative in managed_paths))
    check("integration_managed_text_sorted_unique", managed_paths == sorted(set(managed_paths)))

    for relative, expected in RESEARCH_FILES.items():
        check("research:" + relative, (ROOT / relative).is_file() and digest(ROOT / relative) == expected)
    check("research_manifest", digest(ROOT / "RESEARCH_LOCK.sha256") == RESEARCH_MANIFEST_SHA256)
    check("research_pointer", digest(ROOT / "RESEARCH_LOCK.json") == RESEARCH_POINTER_SHA256)
    for relative, expected in PLAN_HASHES.items():
        check("experiment:" + relative, digest(ROOT / relative) == expected)

    research_lock = parse_json("docs/RESEARCH_LOCK.json")
    check("integrator_research_lock", research_lock.get("immutable_files") == RESEARCH_FILES and research_lock.get("experiment_files") == PLAN_HASHES)
    prototype_lock = parse_json("docs/PROTOTYPE_LOCK.json")
    check("prototype_lock_exact", all((ROOT / relative).is_file() and digest(ROOT / relative) == expected for relative, expected in prototype_lock.get("vendored_files", {}).items()))
    dependency_lock = parse_json("docs/DEPENDENCY_LOCK.json")
    check("dependency_import_exact_sets", all(python_imports(ROOT / relative) == set(expected) for relative, expected in dependency_lock.get("python_imports", {}).items()))
    check("dependency_distribution_pin", dependency_lock.get("external_dependencies") == {"PyYAML": "6.0.2"})
    check("dependency_runtime_version", dependency_lock.get("runtime_import_versions") == {"yaml": "6.0.2"} and distribution_version("PyYAML") == "6.0.2")
    skill_encoded = (ROOT / ROUTE_SKILL_REL).read_bytes()
    try:
        skill_raw = b64decode(b"".join(skill_encoded.split()), validate=True)
    except ValueError:
        skill_raw = b""
    route_fixture_raw = (ROOT / "code/contracts/ROUTE_A_V0_2_SCHEMA.json").read_bytes()
    route_fixture = json.loads(route_fixture_raw)
    check("route_skill_decoded_byte_lock", sha256(skill_raw).hexdigest() == ROUTE_SKILL_SHA256)
    check("route_schema_fixture_byte_lock", sha256(route_fixture_raw).hexdigest() == ROUTE_SCHEMA_FIXTURE_SHA256)
    check("route_schema_skill_link", route_fixture.get("skill_sha256") == ROUTE_SKILL_SHA256)
    forbidden = {"source_core", "evaluate_packet", "independent_evaluator", "prototype_reference", "prototype_independent"}
    check("evaluator_import_firewall", all(not (python_imports(ROOT / relative) & forbidden) for relative in (
        "code/evaluator/evaluate_packet.py", "code/evaluator/independent_evaluator.py",
    )))

    ledger_raw = (ROOT / "results/SHA256SUMS.txt").read_bytes()
    try:
        ledger_text = ledger_raw.decode("utf-8")
    except UnicodeDecodeError:
        ledger_text = ""
    rows: list[tuple[str, str]] = []
    ledger_format = ledger_raw.endswith(b"\n") and not ledger_raw.endswith(b"\n\n") and b"\r" not in ledger_raw
    for line in ledger_text.splitlines():
        match = re.fullmatch(r"([0-9a-f]{64})  ([^\n]+)", line)
        if match is None:
            ledger_format = False
        else:
            rows.append((match.group(2), match.group(1)))
    declared = [relative for relative, _ in rows]
    check("ledger_format", ledger_format)
    check("ledger_exact_paths", declared == ledger_paths == sorted(set(declared)))
    check("ledger_exclusions", set(contract.get("ledger_exclusions", [])) == {"PAPER_MANIFEST.sha256", ROUTE_REL, "results/SHA256SUMS.txt"})
    check("ledger_hashes", ledger_format and all((ROOT / relative).is_file() and digest(ROOT / relative) == expected for relative, expected in rows))

    main_eval = parse_json("results/main_evaluation.json")
    independent = parse_json("results/independent_evaluation.json")
    science_raw = (ROOT / "results/scientific_results.json").read_bytes()
    check("main_evaluator", main_eval.get("all_pass") is True and main_eval.get("check_count") == 210 and main_eval.get("failure_count") == 0)
    check("independent_evaluator", independent.get("all_pass") is True and independent.get("check_count") == 208 and independent.get("failure_count") == 0)
    check("science_equal", main_eval.get("science_projection") == independent.get("science_projection"))
    check("science_hash", sha256(science_raw).hexdigest() == SCIENCE_SHA256 and canonical_bytes(main_eval.get("science_projection")) == science_raw)
    for relative, expected in KNOWN_OUTPUT_HASHES.items():
        check("prototype:" + relative, digest(ROOT / relative) == expected)

    tests = parse_json("results/adversarial_tests.json")
    check("mutation_counts", tests.get("counts") == {
        "packet_mutations": 164, "main_rejections": 164, "independent_rejections": 164,
        "route_mutations": 422, "route_explicit_mutations": 24,
        "route_recursive_mutations": 398, "route_distinct_payloads": 409,
        "route_rejections": 422,
    })
    check("mutation_all_rejected", tests.get("all_pass") is True and all(
        row["evaluators"][label]["rejected"] for row in tests.get("packet_results", []) for label in ("main", "independent")
    ) and all(row["rejected"] for row in tests.get("route_results", [])))
    packet_ids = [row["id"] for row in tests.get("packet_results", [])]
    route_ids = [row["id"] for row in tests.get("route_results", [])]
    check("mutation_ids_unique", len(packet_ids) == len(set(packet_ids)) == 164 and len(route_ids) == len(set(route_ids)) == 422)
    recursive_ids = [item for item in route_ids if item.startswith("route_recursive_")]
    check("route_recursive_id_lock", len(recursive_ids) == 398 and sha256(canonical_bytes(recursive_ids)).hexdigest() == "ea76a28ee16f23cbf9897e60c79be604bc093204d860a32a215e29ca8e499123")

    registry = parse_json("code/contracts/MUTATION_REGISTRY.json")
    expansion = registry.get("exhaustive_expansion_contract", {})
    expected_packet_ids = [item["id"] for item in registry.get("packet_mutations", [])]
    expected_packet_ids += [
        f"card_{card_id}_{kind}"
        for card_id in expansion.get("card_ids", [])
        for kind in expansion.get("card_case_kinds", [])
    ]
    expected_packet_ids += [
        f"inventory_{run_id}_{kind}"
        for run_id in expansion.get("inventory_run_ids", [])
        for kind in expansion.get("inventory_case_kinds", [])
    ]
    explicit_route_ids = [item["id"] for item in registry.get("route_mutations", [])]
    ordered_static_ids = [item["id"] for item in registry.get("static_and_seal_mutations", [])]
    expected_bindings = {
        "expanded_packet": {"count": len(expected_packet_ids), "ordered_id_sha256": sha256(canonical_bytes(expected_packet_ids)).hexdigest()},
        "route_explicit": {"count": len(explicit_route_ids), "ordered_id_sha256": sha256(canonical_bytes(explicit_route_ids)).hexdigest()},
        "route_recursive": {"count": len(recursive_ids), "ordered_id_sha256": sha256(canonical_bytes(recursive_ids)).hexdigest()},
        "route_full": {"count": len(explicit_route_ids + recursive_ids), "ordered_id_sha256": sha256(canonical_bytes(explicit_route_ids + recursive_ids)).hexdigest()},
        "static_and_seal": {"count": len(ordered_static_ids), "ordered_id_sha256": sha256(canonical_bytes(ordered_static_ids)).hexdigest()},
    }
    check("mutation_registry_sha256", digest(ROOT / "code/contracts/MUTATION_REGISTRY.json") == MUTATION_REGISTRY_SHA256 and tests.get("registry_sha256") == MUTATION_REGISTRY_SHA256)
    check("packet_result_ids_exact_registry_sequence", packet_ids == expected_packet_ids)
    check("route_result_ids_exact_registry_sequence", route_ids == explicit_route_ids + recursive_ids)
    check("mutation_result_id_bindings_exact", registry.get("result_id_bindings") == expected_bindings)
    static_ids = set(ordered_static_ids)
    check("static_seal_registry_exact", static_ids == EXPECTED_STATIC_SEAL_IDS and len(ordered_static_ids) == len(static_ids))
    dependency_controls = parse_json("results/dependency_controls.json")
    exact_controls = parse_json("results/exact_set_controls.json")
    seal_controls = parse_json("results/sealed_state_compatibility.json")
    dependency_negative_ids = set(dependency_controls.get("checks", {})) - {
        "all_declared_import_sets_exact", "pyyaml_distribution_pin_exact", "pyyaml_import_runtime_exact",
    }
    observed_static = dependency_negative_ids | set(exact_controls.get("checks", {})) | set(seal_controls.get("unsafe_controls_rejected", {}))
    check("dependency_positive_lock_check", all(dependency_controls.get("checks", {}).get(name) is True for name in (
        "all_declared_import_sets_exact", "pyyaml_distribution_pin_exact", "pyyaml_import_runtime_exact",
    )))
    check("static_seal_controls_executed", observed_static == EXPECTED_STATIC_SEAL_IDS and dependency_controls.get("all_pass") and exact_controls.get("all_pass") and seal_controls.get("all_pass") and all(seal_controls.get("unsafe_controls_rejected", {}).values()))

    check("route_card_stage_scope", parse_json("results/route_evaluation.json").get("all_pass") is True and parse_json("results/route_evaluation.json").get("check_count") == 18)
    route_certificate = parse_json("results/route_schema_certificate.json")
    stage1_route_sha256 = sha256(
        load_route_module().render_route(parse_json("results/scientific_results.json"))
    ).hexdigest()
    check("route_schema_certificate_semantics", route_certificate == {
        "schema": "paper40-route-schema-certificate-v1",
        "route_sha256": stage1_route_sha256,
        "route_evaluation_sha256": digest(ROOT / "results/route_evaluation.json"),
        "strict_checks": 18,
        "explicit_mutations": 24,
        "recursive_mutations": 398,
        "recursive_id_sha256": "ea76a28ee16f23cbf9897e60c79be604bc093204d860a32a215e29ca8e499123",
        "distinct_mutated_payloads": 409,
        "all_pass": True,
    })
    check("reproducibility", parse_json("results/reproducibility_certificate.json").get("all_pass") is True and all(parse_json("results/reproducibility_certificate.json").get("byte_identity", {}).values()))
    check("cold_certificate", parse_json("results/cold_copy_certificate.json").get("all_pass") is True)
    check("idempotence_certificate", parse_json("results/idempotence_certificate.json").get("all_pass") is True)
    check("boundary_certificate", parse_json("results/source_evaluator_boundary.json").get("all_pass") is True)

    all_files = [path for path in ROOT.rglob("*") if path.is_file()]
    authority_text_paths = whole_authority_text_inventory()
    authority_text_files = [ROOT / relative for relative in authority_text_paths]
    writer_core = {
        "README.md", "NARRATIVE_REPORT.md", "PAPER_PLAN.md", "PREREGISTRATION.md",
        "FIGURE_SPEC.md", "main.tex", "math_commands.tex", "references.bib",
    }
    writer_tree = {
        path.relative_to(ROOT).as_posix()
        for parent in (ROOT / "sections", ROOT / "figures")
        for path in parent.rglob("*") if path.is_file() and path.suffix.lower() != ".pdf"
    }
    check("whole_authority_text_inventory_covers_writer_surfaces",
          writer_core | writer_tree <= set(authority_text_paths))
    check("whole_authority_text_hygiene", all(text_hygiene(path) for path in authority_text_files))
    host_absolute_tokens = tuple(
        value.encode("ascii")
        for value in ("/" + "tmp" + "/", "/" + "root" + "/", "/" + "home" + "/", "file" + "://")
    )
    check("no_host_absolute_runtime_tokens", all(
        all(token not in path.read_bytes() for token in host_absolute_tokens)
        for path in authority_text_files
    ))
    manifest = ROOT / MANIFEST_REL
    check("stage2_manifest_text_hygiene_if_present", not manifest.exists() or text_hygiene(manifest))
    check("no_symlinks", not any(path.is_symlink() for path in ROOT.rglob("*")))
    forbidden_names = {"__pycache__", ".pytest_cache", ".mypy_cache"}
    forbidden_suffixes = (".pyc", ".pyo", ".aux", ".log", ".out", ".blg", ".bbl", ".fls", ".fdb_latexmk", ".synctex.gz")
    check("no_cache_aux_bytecode", not any(path.name in forbidden_names or path.name.endswith(forbidden_suffixes) for path in ROOT.rglob("*")))

    output = {
        "schema": "paper40-integrity-audit-v1",
        "checks": dict(sorted(checks.items())),
        "counts": {
            "checks_total": len(checks),
            "checks_passed": sum(checks.values()),
            "ledger_entries": len(rows),
            "managed_text": len(managed_paths),
            "results": len(result_paths),
            "whole_authority_text_excluding_manifest": len(authority_text_paths),
        },
        "whole_authority_text_inventory_sha256": sha256(canonical_bytes(authority_text_paths)).hexdigest(),
        "all_pass": all(checks.values()),
    }
    sys.stdout.buffer.write(canonical_bytes(output))
    return 0 if output["all_pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
