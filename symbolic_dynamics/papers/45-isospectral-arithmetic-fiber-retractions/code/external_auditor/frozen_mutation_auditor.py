#!/usr/bin/env python3
"""Frozen external physical auditor; independent of the internal runner."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import signal
import stat
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml


TOOLS = {
    "A": ("code/evaluator_a/evaluator_a.py", "--inputs"),
    "B": ("code/evaluator_b/evaluator_b.py", "--inputs"),
    "P": ("code/proof_auditor/proof_auditor_p.py", "--inputs"),
    "X": ("code/comparator/comparator_x.py", "--inputs"),
    "T": ("code/auditors/type_auditor.py", "--root"),
    "S": ("code/auditors/source_auditor.py", "--root"),
    "I": ("code/auditors/independence_auditor.py", "--root"),
    "G": ("code/auditors/integrity_auditor.py", "--root"),
    "R_MAIN": ("code/route_main/validate_route_main.py", "--root"),
    "R_INDEPENDENT": ("code/route_independent/validate_route_independent.py", "--root"),
}
MARKER = ".paper45-disposable-root.json"
MARKER_BYTES = b'{"purpose":"paper45-disposable-clone-v1"}\n'
EXPECTED_REGISTRY_SHA256 = "e212120010437f95996d3ff502d38ea527a3bd971bb7baa4f318d26d19ba1540"
PROOF_SOURCE_MUTATIONS = {
    "Q_MAIN_ALL_H": (r"Let \(h\ge2\), \(s\in\mathbb C\)", r"Let \(h=2\), \(s\in\mathbb C\)"),
    "P3_S_ENDPOINT": (r"Hence no bounded extension exists. Suppose \(\sigma>0\).", r"Hence no bounded extension exists. Suppose \(\sigma\ge0\)."),
    "P3_M_ENDPOINT": (r"is finite exactly when \(\sigma>1/h\). On that domain,", r"is finite exactly when \(\sigma\ge1/h\). On that domain,"),
    "P4_POWER_IFF": (r"S^k\in\mathcal S_q\iff k\sigma q>2,", r"S^k\in\mathcal S_q\iff k\sigma q\le2,"),
    "P5_TRACE_ENDPOINT": (r"On the common bounded domain and for \(k\sigma>2\),", r"On the common bounded domain and for \(k\sigma\ge2\),"),
    "P5_DET_ENDPOINT": (r"if \(\sigma>1/h\) and \(r\sigma>2\), both", r"if \(\sigma\ge1/h\) and \(r\sigma\ge2\), both"),
    "P6_SIMILARITY_ENDPOINT": (r"S\sim_{\mathrm{bd}}\text{ normal}\iff\sigma>1,", r"S\sim_{\mathrm{bd}}\text{ normal}\iff\sigma\ge1,"),
    "P7_COEFFICIENT": (r"\frac{(h-1)^{\sigma-1}(\log x)^{1-\sigma}}", r"\frac{(h-1)^{1-\sigma}(\log x)^{1-\sigma}}"),
    "P8_STRIP_OPERATOR": (r"=\max\left(\frac1h,\frac{1-\sigma}{h-1}\right).", r"=\min\left(\frac1h,\frac{1-\sigma}{h-1}\right)."),
    "P9_CROSSOVER_VALUE": (r"Hence \(C_{h,1}=D_{h,1}=1\), with no claimed ordering away from one.", r"Hence \(C_{h,1}=D_{h,1}=2\), with no claimed ordering away from one."),
    "P11_COMM_ENDPOINT": (r"[S^*,S]\in\mathcal S_q\iff\sigma q>1.", r"[S^*,S]\in\mathcal S_q\iff\sigma q\ge1."),
    "P11_H2_WITNESS": (r"For \(h=2\), exponent one is saturated. Fix \(p_0\) and instead take", r"For \(h=2\), use one nonsaturated exponent-one prime. Fix \(p_0\) and instead take"),
    "P12_ENDPOINT": (r"For \(\sigma>1/2\), the two positive sums below converge separately, and", r"For \(\sigma\ge1/2\), the two positive sums below converge separately, and"),
    "P12_PRODUCT_SIGN": ("=2\\left\\{\n\\prod_p\\left[1+(p^\\sigma-1)^{-2}\\right]\n-\\prod_p", "=2\\left\\{\n\\prod_p\\left[1+(p^\\sigma-1)^{-2}\\right]\n+\\prod_p"),
    "FREE_UFD_POLARITY": (r"oblique-projection, and free-UFD methods, the exact", r"oblique-projection, and rational-prime-specific free-UFD methods, the exact"),
}


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def clone_tree(source: Path, target: Path):
    def ignore(_path, names):
        return {n for n in names if n in {"results", "results.__stage__", "__pycache__", ".p45_harness"} or n.endswith((".pyc", ".pyo"))}
    shutil.copytree(source, target, symlinks=True, ignore=ignore)
    marker = target / MARKER
    marker.write_bytes(MARKER_BYTES)
    marker.chmod(0o444)


def clean_env(extra=None):
    env = {k: v for k, v in os.environ.items() if k not in {"PYTHONPATH", "PYTHONHOME", "TMPDIR", "TMP", "TEMP",
                                                               "P45_EXPECTED_OVERRIDE", "P45_CACHE_OVERRIDE"}}
    env.update({"PYTHONDONTWRITEBYTECODE": "1", "PYTHONHASHSEED": "0", "TMPDIR": "/tmp", "TMP": "/tmp", "TEMP": "/tmp"})
    if extra:
        env.update(extra)
    return env


def total_call(command, timeout=300, env=None):
    process = subprocess.Popen(command, cwd="/", env=env or clean_env(), stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               text=True, start_new_session=True)
    try:
        stdout, stderr = process.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        os.killpg(process.pid, signal.SIGKILL)
        process.communicate()
        raise RuntimeError("external timeout")
    return process.returncode, stdout, stderr


def replace_pointer(document, pointer, old, new):
    pieces = [x.replace("~1", "/").replace("~0", "~") for x in pointer.lstrip("/").split("/")]
    node = document
    for piece in pieces[:-1]:
        node = node[int(piece)] if isinstance(node, list) else node[piece]
    tail = pieces[-1]
    present = node[int(tail)] if isinstance(node, list) else node[tail]
    if type(present) is not type(old) or present != old:
        raise ValueError("precondition")
    if isinstance(node, list):
        node[int(tail)] = new
    else:
        node[tail] = new


def metadata(target: Path):
    if not target.exists() and not target.is_symlink():
        return []
    nodes = [target]
    if target.is_dir() and not target.is_symlink():
        nodes += sorted(target.rglob("*"))
    result = []
    for node in nodes:
        info = os.lstat(node)
        kind = "regular" if stat.S_ISREG(info.st_mode) else "directory" if stat.S_ISDIR(info.st_mode) else "symlink" if stat.S_ISLNK(info.st_mode) else "other"
        raw = node.read_bytes() if kind == "regular" else os.readlink(node).encode() if kind == "symlink" else b""
        result.append((node.relative_to(target.parent).as_posix(), kind, hashlib.sha256(raw).hexdigest(), info.st_size,
                       stat.S_IMODE(info.st_mode), info.st_mtime_ns))
    return result


def forced_probe(root: Path, operation: dict):
    target, stage = root / "results", root / "results.__stage__"
    before = metadata(target)
    stage.mkdir()
    names = ["comparator_x.json", "evaluation_report.json", "evaluator_a.json", "evaluator_b.json",
             "integrity_audit.json", "mutation_outcomes.json", "proof_auditor_p.json"]
    for name in names:
        (stage / name).write_text("{}\n")
    manifest_lines = [hashlib.sha256((stage / n).read_bytes()).hexdigest() + "  " + n for n in sorted(names)]
    (stage / "SHA256SUMS.txt").write_text("\n".join(manifest_lines) + "\n")
    if len(list(stage.iterdir())) != 8:
        raise ValueError("stage")
    shutil.rmtree(stage)
    payload = {"checkpoint": operation["checkpoint"], "stage_removed": not stage.exists(),
               "target_metadata_unchanged": before == metadata(target), "physical_probe": True}
    mark = root / ".p45_harness"
    mark.mkdir()
    (mark / "M048.json").write_text(json.dumps(payload, sort_keys=True, separators=(",", ":")) + "\n")


def apply_row(root: Path, row: dict, outer: Path):
    op = row["operation"]
    if op["kind"] == "replace_json_pointer":
        target = root / "inputs" / "preauthority" / op["target_artifact"]
        document = load(target)
        replace_pointer(document, op["pointer"], op["value_from"], op["value_to"])
        target.chmod(0o644)
        target.write_text(json.dumps(document, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
        target.chmod(0o444)
        if row["id"] in {"M043", "M049"}:
            route_path = root / "inputs/preauthority/ROUTE_EXPECTATION.yaml"
            route = yaml.safe_load(route_path.read_text(encoding="utf-8"))
            if row["id"] == "M043":
                route["evaluation_state"] = "EVALUATED"
            else:
                route["overall_expectation"] = "GO_EVALUATED"
                route["branch_status"] = "GO_EVALUATED"
            route_path.chmod(0o644)
            route_path.write_text(yaml.safe_dump(route, sort_keys=False, allow_unicode=True), encoding="utf-8")
            route_path.chmod(0o444)
    elif op["kind"] == "filesystem_symlink_swap":
        destination = root / op["path"]
        destination.mkdir()
        destination.rmdir()
        sentinel = outer / "external_sentinel"
        sentinel.mkdir(exist_ok=True)
        destination.symlink_to(sentinel, target_is_directory=True)
    elif op["kind"] == "filesystem_create_forbidden_artifact":
        destination = root / op["path"]
        destination.parent.mkdir(parents=True)
        destination.write_text(op["content_utf8"])
    elif op["kind"] == "force_late_failure":
        return
    else:
        raise ValueError("operation")


def build_science_views(source: Path, parent: Path):
    inputs = source / "inputs/preauthority"
    outputs = {}
    for lane in ("A", "B"):
        target = parent / ("external-baseline-" + lane.lower() + ".json")
        rel, _ = TOOLS[lane]
        code, stdout, _ = total_call([sys.executable, "-B", str(source / rel), "--inputs", str(inputs), "--emit", str(target)])
        if code != 0 or stdout.strip():
            raise RuntimeError("external baseline lane")
        outputs[lane] = target
    for lane in ("A", "B"):
        projection = load(outputs[lane])
        target = parent / ("external-view-" + lane.lower() + ".json")
        target.write_text(json.dumps({"producer": projection["producer"], "contract_sha256": projection["contract_sha256"],
                                      "finite_records": projection["finite_records"]}, sort_keys=True, separators=(",", ":")) + "\n")
        outputs[lane + "_VIEW"] = target
    p_target = parent / "external-baseline-p.json"
    p_code, p_stdout, _ = total_call([sys.executable, "-B", str(source / TOOLS["P"][0]), "--inputs", str(inputs),
                                      "--b", str(outputs["B"]), "--emit", str(p_target)])
    if p_code != 0 or p_stdout.strip():
        raise RuntimeError("external baseline P")
    outputs["P"] = p_target
    x_target = parent / "external-baseline-x.json"
    x_code, x_stdout, _ = total_call([sys.executable, "-B", str(source / TOOLS["X"][0]), "--inputs", str(inputs),
                                      "--a-finite", str(outputs["A_VIEW"]), "--b-finite", str(outputs["B_VIEW"]),
                                      "--emit", str(x_target)])
    if x_code != 0 or x_stdout.strip():
        raise RuntimeError("external baseline X")
    outputs["X"] = x_target
    return outputs


def prepared_bundle(source: Path, registry: dict, target: Path):
    outcomes = []
    for row in registry["mutations"]:
        for consumer in row["consumers"]:
            material = f"external-prepared\n{row['id']}\n{consumer}\n{row['code']}\n".encode()
            outcomes.append({"mutation_id": row["id"], "consumer_key": consumer, "outcome": "REJECT", "exit_code": 2,
                             "rejection_code": row["code"], "result_digest": hashlib.sha256(material).hexdigest()})
    inputs = source / "inputs/preauthority"
    value = {"schema_version": "paper45.mutation-outcomes.v1",
             "contract_sha256": hashlib.sha256((inputs / "EXPERIMENT_CONTRACT.json").read_bytes()).hexdigest(),
             "registry_sha256": hashlib.sha256((inputs / "MUTATION_REGISTRY.json").read_bytes()).hexdigest(),
             "outcomes": outcomes}
    target.write_text(json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n")


def call_consumer(root: Path, consumer: str, row: dict, baseline: dict, prepared: Path):
    rel, option = TOOLS[consumer]
    inputs = root / "inputs/preauthority"
    if row["id"] == "M048" and consumer == "G":
        command = [sys.executable, "-B", str(root / "code/integration/run_integration.py"), "--root", str(root),
                   "--phase", "FINAL", "--force-late-failure", "--prepared-mutation-bundle", str(prepared)]
        timeout = 900
    elif consumer in {"A", "B"}:
        command, timeout = [sys.executable, "-B", str(root / rel), "--inputs", str(inputs)], 300
    elif consumer == "P":
        command, timeout = [sys.executable, "-B", str(root / rel), "--inputs", str(inputs), "--b", str(baseline["B"])], 300
    elif consumer == "X":
        command = [sys.executable, "-B", str(root / rel), "--inputs", str(inputs),
                   "--a-finite", str(baseline["A_VIEW"]), "--b-finite", str(baseline["B_VIEW"])]
        timeout = 300
    else:
        command, timeout = [sys.executable, "-B", str(root / rel), "--root", str(root)], 300
    exit_code, stdout, _ = total_call(command, timeout)
    lines = [x for x in stdout.splitlines() if x.strip()]
    if len(lines) != 1:
        return False
    try:
        answer = json.loads(lines[0])
    except json.JSONDecodeError:
        return False
    return (exit_code == 2 and answer.get("outcome") == "REJECT" and answer.get("exit_code") == 2 and
            answer.get("rejection_code") == row["code"])


def schema_attacks(source: Path, parent: Path):
    attacks = {
        "BOOL_AS_INTEGER": lambda c: c["mutation_baseline"]["case"].__setitem__("h", True),
        "FLOAT_AS_INTEGER": lambda c: c["mutation_baseline"]["case"].__setitem__("h", 2.0),
        "STRING_AS_BOOLEAN": lambda c: c["mutation_baseline"]["scope"].__setitem__("all_h", "true"),
        "UNKNOWN_TOP_KEY": lambda c: c.__setitem__("unexpected", 1),
        "MISSING_REQUIRED_KEY": lambda c: c.pop("schema_version"),
        "OUTPUT_ORDER_CHANGED": lambda c: c["output_artifacts"].reverse(),
        "COMMON_FINITE_ORDER_CHANGED": lambda c: c["common_finite_case_ids"].reverse(),
        "DUPLICATE_CASE_ID": lambda c: c["case_registry"].append(dict(c["case_registry"][0])),
    }
    passed = []
    for name, operation in attacks.items():
        root = parent / ("schema-" + name)
        clone_tree(source, root)
        contract_path = root / "inputs" / "preauthority" / "EXPERIMENT_CONTRACT.json"
        contract = load(contract_path)
        operation(contract)
        contract_path.chmod(0o644)
        contract_path.write_text(json.dumps(contract, sort_keys=True, separators=(",", ":")) + "\n")
        command = [sys.executable, "-B", str(root / "code/auditors/type_auditor.py"), "--root", str(root)]
        return_code, _stdout, _stderr = total_call(command, 180)
        if return_code == 0:
            raise RuntimeError("schema attack survived:" + name)
        passed.append(name)
    return passed


def remanifest_input(root: Path, changed_name: str):
    inputs = root / "inputs/preauthority"
    manifest = inputs / "SHA256SUMS.txt"
    rows = []
    for line in manifest.read_text(encoding="utf-8").splitlines():
        _old, name = line.split("  ", 1)
        checksum = hashlib.sha256((inputs / name).read_bytes()).hexdigest()
        rows.append(checksum + "  " + name)
    manifest.chmod(0o644)
    manifest.write_text("\n".join(sorted(rows, key=lambda row: row.split("  ", 1)[1])) + "\n", encoding="utf-8")
    manifest.chmod(0o444)


def reclose_certificate(certificate: dict, payload: dict):
    encoded = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)
    certificate["certificate_value"] = encoded
    material = ("paper45-analytic-derivation-v3\n" + certificate["case_id"] + "\n" +
                certificate["strict_domain_expression"] + "\n" + certificate["endpoint_witness_type"] + "\n" +
                encoded + "\n").encode()
    certificate["analytic_derivation_hash"] = hashlib.sha256(material).hexdigest()
    stripped = {key: value for key, value in certificate.items() if key != "certificate_payload_sha256"}
    certificate["certificate_payload_sha256"] = hashlib.sha256(
        json.dumps(stripped, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()).hexdigest()


def expect_p_hold(source: Path, inputs: Path, b_path: Path, label: str):
    code, stdout, _err = total_call([sys.executable, "-B", str(source / TOOLS["P"][0]),
                                     "--inputs", str(inputs), "--b", str(b_path)], 300)
    lines = [line for line in stdout.splitlines() if line.strip()]
    if code != 0 or len(lines) != 1:
        raise RuntimeError("P physical negative execution:" + label)
    value = json.loads(lines[0])
    if value.get("verdict") != "HOLD" or not value.get("findings"):
        raise RuntimeError("P physical negative survived:" + label)


def physical_reproductions(source: Path, parent: Path, baseline: dict):
    killed = []

    # Frozen-source attack even after the attacker recomputes the member list.
    tau_root = parent / "repro-tau-remanifest"
    clone_tree(source, tau_root)
    source_lock = tau_root / "inputs/preauthority/SOURCE_LOCK.md"
    text_value = source_lock.read_text(encoding="utf-8")
    if "\\tau_h" not in text_value:
        raise RuntimeError("tau repro precondition")
    source_lock.chmod(0o644)
    source_lock.write_text(text_value.replace("\\tau_h", "\\tau_{999999}", 1), encoding="utf-8")
    source_lock.chmod(0o444)
    remanifest_input(tau_root, "SOURCE_LOCK.md")
    code, _out, _err = total_call([sys.executable, "-B", str(tau_root / TOOLS["S"][0]), "--root", str(tau_root)])
    if code == 0:
        raise RuntimeError("tau999999+remanifest survived")
    killed.append("TAU999999_REMANIFEST")

    # X must reject both a Boolean count and a dishonest PASS disposition.
    x_bad = parent / "repro-x-false-count-pass.json"
    x_value = load(baseline["X"])
    x_value["exact_mismatch_count"] = False
    x_value["verdict"] = "PASS"
    x_bad.write_text(json.dumps(x_value, sort_keys=True, separators=(",", ":")) + "\n")
    code, _out, _err = total_call([sys.executable, "-B", str(source / TOOLS["X"][0]), "--inputs",
                                   str(source / "inputs/preauthority"), "--validate-report", str(x_bad)])
    if code != 2:
        raise RuntimeError("X false count/PASS survived")
    killed.append("X_FALSE_COUNT_PASS")

    # A missing required eigen enclosure is passed through X's ordinary
    # finite-view validator, not a synthetic mutation hook.
    missing_view = parent / "repro-missing-eigen-interval.json"
    a_view = load(baseline["A_VIEW"])
    a_view["finite_records"][0].pop("finite_nonzero_eigenvalue_interval")
    missing_view.write_text(json.dumps(a_view, sort_keys=True, separators=(",", ":")) + "\n")
    code, _out, _err = total_call([sys.executable, "-B", str(source / TOOLS["X"][0]), "--inputs",
                                   str(source / "inputs/preauthority"), "--a-finite", str(missing_view),
                                   "--b-finite", str(baseline["B_VIEW"])])
    if code != 2:
        raise RuntimeError("missing eigen interval survived")
    killed.append("MISSING_EIGEN_INTERVAL")

    # Endpoint enclosure drift is independently recomputed by P at 250 dps.
    endpoint_b = parent / "repro-endpoint-drift-b.json"
    b_value = load(baseline["B"])
    certificate = b_value["infinite_records"][0]
    analytic = json.loads(certificate["certificate_value"])
    analytic["partial_product_certified_interval"]["lower"] = "0"
    analytic["partial_product_certified_interval"]["upper"] = "0"
    certificate["certificate_value"] = json.dumps(analytic, sort_keys=True, separators=(",", ":"))
    endpoint_b.write_text(json.dumps(b_value, sort_keys=True, separators=(",", ":")) + "\n")
    code, stdout, _err = total_call([sys.executable, "-B", str(source / TOOLS["P"][0]), "--inputs",
                                     str(source / "inputs/preauthority"), "--b", str(endpoint_b)])
    lines = [line for line in stdout.splitlines() if line.strip()]
    if code != 0 or len(lines) != 1 or json.loads(lines[0]).get("verdict") != "HOLD":
        raise RuntimeError("analytic endpoint drift survived")
    killed.append("ANALYTIC_ENDPOINT_DRIFT")

    # A rendered audit cannot claim PASS when one exact case is HOLD.
    p_bad = parent / "repro-hold-rerender.json"
    p_value = load(baseline["P"])
    p_value["per_case_audits"][0]["verdict"] = "HOLD"
    p_value["findings"] = ["physical HOLD rerender"]
    p_value["verdict"] = "PASS"
    p_bad.write_text(json.dumps(p_value, sort_keys=True, separators=(",", ":")) + "\n")
    code, _out, _err = total_call([sys.executable, "-B", str(source / TOOLS["P"][0]), "--inputs",
                                   str(source / "inputs/preauthority"), "--validate-audit", str(p_bad)])
    if code != 2:
        raise RuntimeError("HOLD rerender survived")
    killed.append("HOLD_RERENDER")

    # Integrity booleans are strict booleans and the final verdict is their iff.
    integrity_bad = parent / "repro-false-integrity.json"
    integrity_bad.write_text(json.dumps({"manifest_verified": True, "path_policy_verified": True,
                                         "late_failure_identity_verified": False,
                                         "second_run_zero_replacements": True,
                                         "pre_io_containment_verified": True,
                                         "recursive_namespace_verified": True, "verdict": "PASS"},
                                        sort_keys=True, separators=(",", ":")) + "\n")
    code, _out, _err = total_call([sys.executable, "-B", str(source / TOOLS["G"][0]), "--root", str(source),
                                   "--validate-integrity-report", str(integrity_bad)])
    if code != 2:
        raise RuntimeError("false integrity boolean survived")
    killed.append("FALSE_INTEGRITY_BOOLEAN")

    # Registry digest is immutable even if the attacker remanifests inputs.
    registry_root = parent / "repro-forged-registry"
    clone_tree(source, registry_root)
    registry_path = registry_root / "inputs/preauthority/MUTATION_REGISTRY.json"
    registry_value = load(registry_path)
    registry_value["schema_version"] = "paper45.mutation-registry.forged"
    registry_path.chmod(0o644)
    registry_path.write_text(json.dumps(registry_value, sort_keys=True, separators=(",", ":")) + "\n")
    registry_path.chmod(0o444)
    remanifest_input(registry_root, "MUTATION_REGISTRY.json")
    code, _out, _err = total_call([sys.executable, "-B", str(registry_root / TOOLS["T"][0]), "--root", str(registry_root)])
    if code == 0:
        raise RuntimeError("forged registry/digest survived")
    killed.append("FORGED_REGISTRY_DIGEST")

    # Both Route validators see an actual zero source hash plus an extra
    # nested member in the v0.2 object.
    route_root = parent / "repro-route-zero-extra"
    clone_tree(source, route_root)
    route_path = route_root / "inputs/preauthority/ROUTE_EXPECTATION.yaml"
    route_value = yaml.safe_load(route_path.read_text(encoding="utf-8"))
    route_value["source_commit"] = "0" * 40
    route_value["source_lock"]["unexpected_nested"] = "forbidden"
    route_path.chmod(0o644)
    route_path.write_text(yaml.safe_dump(route_value, sort_keys=False, allow_unicode=True), encoding="utf-8")
    route_path.chmod(0o444)
    for consumer in ("R_MAIN", "R_INDEPENDENT"):
        code, _out, _err = total_call([sys.executable, "-B", str(route_root / TOOLS[consumer][0]), "--root", str(route_root)])
        if code == 0:
            raise RuntimeError("Route zero+extra survived:" + consumer)
    killed.append("ROUTE_ZERO_SOURCE_EXTRA")

    # Hostile TMPDIR must remain untouched; the production driver chooses
    # /tmp explicitly and PRE_CERT emits no result/cache files.
    hostile_root = parent / "repro-hostile-tmpdir"
    clone_tree(source, hostile_root)
    sentinel = parent / "hostile-tmpdir-sentinel"
    sentinel.mkdir()
    sentinel_file = sentinel / "DO_NOT_TOUCH"
    sentinel_file.write_text("paper45-hostile-tmpdir-sentinel\n")
    before = metadata(sentinel)
    driver = hostile_root / "code/integration/run_integration.py"
    code, _out, _err = total_call([sys.executable, "-B", str(driver), "--root", str(hostile_root), "--phase", "PRE_CERT"],
                                  300, clean_env({"TMPDIR": str(sentinel), "TMP": str(sentinel), "TEMP": str(sentinel)}))
    if code != 0 or metadata(sentinel) != before or (hostile_root / "results").exists():
        raise RuntimeError("hostile TMPDIR containment")
    killed.append("HOSTILE_TMPDIR_SENTINEL")

    # Fifteen physical edits of the frozen proof corpus must make the normal
    # proof lane render HOLD.  No mutation identifier is passed to P.
    proof_baseline = (source / "inputs/preauthority/PROOF_PACKAGE.md").read_text(encoding="utf-8")
    for label, (before_text, after_text) in PROOF_SOURCE_MUTATIONS.items():
        if proof_baseline.count(before_text) != 1:
            raise RuntimeError("proof mutation precondition:" + label)
        proof_root = parent / ("repro-proof-" + label.lower())
        clone_tree(source, proof_root)
        proof_file = proof_root / "inputs/preauthority/PROOF_PACKAGE.md"
        proof_file.chmod(0o644)
        proof_file.write_text(proof_baseline.replace(before_text, after_text), encoding="utf-8")
        proof_file.chmod(0o444)
        expect_p_hold(proof_root, proof_root / "inputs/preauthority", baseline["B"], label)
        killed.append("PROOF_SOURCE_" + label)

    # Formula/output negatives are reclosed at the outer hash layers so the
    # independent mathematical AST and high-precision checks must do the work.
    for label in ("FORMULA_DOMAIN", "WITNESS_FABRICATED", "CONCLUSION_OPPOSITE", "TRACE_ENDPOINT_NONSTRICT",
                  "POWER_LOCAL_AST", "COMMUTATOR_SIGN", "WEYL_D_INTERVAL", "FREE_UFD_SEMANTICS"):
        b_value = load(baseline["B"])
        if label == "FORMULA_DOMAIN":
            certificate = next(row for row in b_value["infinite_records"] if row["case_id"] == "INF-S-EXIST-H2")
            analytic = json.loads(certificate["certificate_value"])
            certificate["strict_domain_expression"] = "sigma<=0"
            analytic["formula_ast"]["domain_ast"]["op"] = "LESS_EQUAL"
        elif label == "WITNESS_FABRICATED":
            certificate = next(row for row in b_value["infinite_records"] if row["case_id"] == "INF-S-EXIST-H2")
            analytic = json.loads(certificate["certificate_value"])
            certificate["endpoint_witness_type"] = "fabricated_endpoint_witness"
            analytic["endpoint_witness"] = "fabricated_endpoint_witness"
        elif label == "CONCLUSION_OPPOSITE":
            certificate = next(row for row in b_value["infinite_records"] if row["case_id"] == "INF-S-EXIST-H2")
            analytic = json.loads(certificate["certificate_value"])
            analytic["conclusion_label"] = "bounded_and_compact_not_iff"
        elif label == "TRACE_ENDPOINT_NONSTRICT":
            certificate = next(row for row in b_value["infinite_records"] if row["case_id"] == "INF-TRACE-H3-K2")
            analytic = json.loads(certificate["certificate_value"])
            certificate["strict_domain_expression"] = "sigma>1/h and k*sigma>=2"
            analytic["formula_ast"]["domain_ast"]["operands"][1]["op"] = "GREATER_EQUAL"
        elif label == "POWER_LOCAL_AST":
            certificate = next(row for row in b_value["infinite_records"] if row["case_id"] == "INF-POWER-H2-K1-Q2")
            analytic = json.loads(certificate["certificate_value"])
            factor = analytic["analytic_families"][0]["local_factors"][0]
            factor["operation_ast"]["op"] = "MULTIPLY"
            factor["operation_ast_sha256"] = hashlib.sha256(
                json.dumps(factor["operation_ast"], sort_keys=True, separators=(",", ":")).encode()).hexdigest()
        elif label == "COMMUTATOR_SIGN":
            certificate = next(row for row in b_value["infinite_records"] if row["case_id"] == "INF-COMM-H2-EULER")
            analytic = json.loads(certificate["certificate_value"])
            analytic["commutator_product_difference"]["operation_ast"]["operands"][1]["op"] = "ADD"
            analytic["commutator_product_difference"]["operation_ast_sha256"] = hashlib.sha256(
                json.dumps(analytic["commutator_product_difference"]["operation_ast"], sort_keys=True,
                           separators=(",", ":")).encode()).hexdigest()
        elif label == "WEYL_D_INTERVAL":
            certificate = next(row for row in b_value["infinite_records"] if row["case_id"] == "INF-WEYL-H3-NONCROSSOVER")
            analytic = json.loads(certificate["certificate_value"])
            family = next(row for row in analytic["analytic_families"] if row["family_id"].startswith("WEYL_D:"))
            family["local_factors"][0]["lower"] = "0"
            family["local_factors"][0]["upper"] = "0"
        else:
            certificate = next(row for row in b_value["infinite_records"] if row["case_id"] == "INF-FREE-UFD-CONTROL-H3")
            analytic = json.loads(certificate["certificate_value"])
            analytic["modulo_formula"]["rational_prime_semantics"] = True
        reclose_certificate(certificate, analytic)
        b_path = parent / ("repro-analytic-" + label.lower() + ".json")
        b_path.write_text(json.dumps(b_value, sort_keys=True, separators=(",", ":")) + "\n", encoding="utf-8")
        expect_p_hold(source, source / "inputs/preauthority", b_path, label)
        killed.append("ANALYTIC_" + label)
    return killed


def audit(source: Path):
    source = source.resolve(strict=True)
    registry_path = source / "inputs" / "preauthority" / "MUTATION_REGISTRY.json"
    if hashlib.sha256(registry_path.read_bytes()).hexdigest() != EXPECTED_REGISTRY_SHA256:
        raise ValueError("immutable registry digest")
    registry = load(registry_path)
    if [x["id"] for x in registry["mutations"]] != [f"M{i:03d}" for i in range(1, 76)]:
        raise ValueError("registry")
    calls = 0
    with tempfile.TemporaryDirectory(prefix="paper45-external-audit-", dir="/tmp") as raw:
        parent = Path(raw)
        baseline = build_science_views(source, parent)
        prepared = parent / "external-prepared-mutations.json"
        prepared_bundle(source, registry, prepared)
        for row in registry["mutations"]:
            root = parent / row["id"] / "candidate"
            root.parent.mkdir()
            clone_tree(source, root)
            apply_row(root, row, root.parent)
            observed = []
            for consumer in row["consumers"]:
                if not call_consumer(root, consumer, row, baseline, prepared):
                    raise RuntimeError("survivor:" + row["id"] + ":" + consumer)
                observed.append(consumer)
                calls += 1
            if observed != row["consumers"] or len(set(observed)) != len(observed):
                raise RuntimeError("consumer set")
        attacks = schema_attacks(source, parent)
        reproductions = physical_reproductions(source, parent, baseline)
    return {"schema_version": "paper45.external-frozen-audit.v1", "registry_rows": 75,
            "physical_consumer_calls": calls, "all_registered_mutations_killed": True,
            "schema_attacks": attacks, "schema_attack_count": len(attacks),
            "physical_reproductions": reproductions, "physical_reproduction_count": len(reproductions),
            "verdict": "PASS"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", type=Path, required=True)
    ns = ap.parse_args()
    try:
        print(json.dumps(audit(ns.root), sort_keys=True, separators=(",", ":")))
        return 0
    except Exception:
        print('{"error":{"code":"EXTERNAL_AUDIT_ERROR","detail":"redacted","stage":"EXTERNAL"},"exit_code":3,"outcome":"HARNESS_ERROR"}')
        return 3


if __name__ == "__main__":
    raise SystemExit(main())
