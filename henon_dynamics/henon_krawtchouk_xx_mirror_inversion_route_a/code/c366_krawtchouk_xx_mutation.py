#!/usr/bin/env python3
"""Repaired-hash JSON and strict-YAML hostile mutations for HCS-C366."""
from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c366_krawtchouk_xx_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C366/2026-09-04.yaml"
CHECKER = ROOT / "code/c366_krawtchouk_xx_checker.py"


def refuse_optimized() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C366 mutation lane refuses optimized Python")


def repair(data: dict) -> None:
    payload = dict(data)
    payload.pop("payload_sha256", None)
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    data["payload_sha256"] = hashlib.sha256(encoded).hexdigest()


def reject(evidence: bytes, evaluation: bytes, label: str, directory: Path) -> None:
    evidence_path = directory / f"{label}.json"
    evaluation_path = directory / f"{label}.yaml"
    evidence_path.write_bytes(evidence)
    evaluation_path.write_bytes(evaluation)
    environment = dict(os.environ, PYTHONDONTWRITEBYTECODE="1", TZ="UTC")
    process = subprocess.run(
        [sys.executable, "-B", str(CHECKER), "--input", str(evidence_path),
         "--evaluation", str(evaluation_path)],
        env=environment, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
    )
    if process.returncode == 0:
        raise AssertionError(f"mutation survived: {label}")


def main() -> None:
    refuse_optimized()
    base = json.loads(EVIDENCE.read_text())
    base_bytes = EVIDENCE.read_bytes()
    yaml_bytes = EVALUATION.read_bytes()
    yaml_text = yaml_bytes.decode()

    changes = []
    def add(label, change):
        changes.append((label, change))

    add("candidate", lambda x: x.__setitem__("candidate_id", "HCS-C365"))
    add("obstruction", lambda x: x.__setitem__("obstruction_id", "HEN-O349"))
    add("date", lambda x: x.__setitem__("evaluation_date", "2026-09-03"))
    add("source", lambda x: x.__setitem__("source_commit", "0" * 40))
    add("epoch", lambda x: x.__setitem__("fixed_epoch", 0))
    add("scope", lambda x: x.__setitem__("scope_literal", "BAD_SCOPE"))
    add("top_extra", lambda x: x.__setitem__("unexpected", True))
    add("top_missing", lambda x: x.pop("nonclaims"))
    add("evaluator_authority", lambda x: x["evaluator"].__setitem__("authority", "wrong"))
    add("evaluator_version", lambda x: x["evaluator"].__setitem__("version", "9.9"))
    add("evaluator_sha", lambda x: x["evaluator"].__setitem__("sha256", "0" * 64))
    add("evaluator_extra", lambda x: x["evaluator"].__setitem__("extra", 1))
    add("yaml_path", lambda x: x["route_a_yaml"].__setitem__("relative_path", "other.yaml"))
    add("yaml_raw", lambda x: x["route_a_yaml"].__setitem__("raw_sha256", "0" * 64))
    add("yaml_semantic", lambda x: x["route_a_yaml"].__setitem__("semantic_sha256", "0" * 64))
    add("model_propagator", lambda x: x["model"].__setitem__("propagator", "exp(+itH)"))
    add("model_field", lambda x: x["model"].__setitem__("uniform_field", "B times identity"))
    add("model_extra", lambda x: x["model"].__setitem__("extra", 1))
    add("model_missing", lambda x: x["model"].pop("fermion_order"))
    add("theorem_status", lambda x: x.__setitem__("theorem_status", "OPEN"))
    add("route_tuple", lambda x: x["route_tuple"].__setitem__(1, "A1_PASS_ANALYTIC"))
    add("overall", lambda x: x.__setitem__("overall_verdict", "ROUTE_A_PROMISING"))
    add("route_b", lambda x: x.__setitem__("route_b_invocation_allowed", True))
    add("route_b_bool_int", lambda x: x.__setitem__("route_b_invocation_allowed", 0))
    add("forbidden", lambda x: x["scope_flags"].__setitem__("claims_target_zero_match", True))
    add("flag_bool_int", lambda x: x["scope_flags"].__setitem__("claims_root_number", 0))
    add("flag_missing", lambda x: x["scope_flags"].pop("claims_root_number"))
    add("claim_mirror", lambda x: x["exact_claims"].__setitem__("mirror_phase", "wrong"))
    add("claim_endpoint", lambda x: x["exact_claims"].__setitem__("endpoint_law", "probability only"))
    add("claim_qbinomial", lambda x: x["exact_claims"].__setitem__("gaussian_q_binomial", "wrong recurrence"))
    add("claim_field", lambda x: x["exact_claims"].__setitem__("uniform_field_revival", "always identity"))
    add("claim_identity", lambda x: x["exact_claims"].__setitem__("full_identity_conditions", "all B"))
    add("claim_extra", lambda x: x["exact_claims"].__setitem__("extra", 1))
    add("claim_missing", lambda x: x["exact_claims"].pop("spectrum"))
    add("boundary_zero", lambda x: x["boundary_atlas"].__setitem__("omega_zero", "transfer exists"))
    add("boundary_field", lambda x: x["boundary_atlas"].__setitem__("uniform_field", "global phase"))
    add("boundary_revival", lambda x: x["boundary_atlas"].__setitem__("full_fock_revival", "always identity"))
    add("boundary_extra", lambda x: x["boundary_atlas"].__setitem__("extra", 1))
    add("finite_role", lambda x: x.__setitem__("finite_evidence_role", "proof by enumeration"))
    add("collision", lambda x: x.__setitem__("collision_boundary", "none"))
    add("collision_old_wrong_ids", lambda x: x.__setitem__(
        "collision_boundary",
        "C253 owns a different finite quantum walk, C263 owns a different orthogonal-polynomial "
        "chain, and C285 owns a different fermionic model; C366 uniquely owns the engineered "
        "Krawtchouk XX mirror chain and its full exterior-power phase law"))
    add("nonclaims", lambda x: x.__setitem__("nonclaims", "claims everything"))
    add("reference", lambda x: x["references"][0].__setitem__("doi", "wrong"))
    add("reference_extra", lambda x: x["references"][0].__setitem__("extra", True))
    add("counts", lambda x: x["counts"].__setitem__("spectral_rows", 65))
    add("counts_extra", lambda x: x["counts"].__setitem__("extra", 0))
    add("spectral_value", lambda x: x["spectral_rows"][10].__setitem__("twice_energy_over_omega", 99))
    add("spectral_coordinate_bool", lambda x: x["spectral_rows"][0].__setitem__("N", False))
    add("spectral_coordinate_float", lambda x: x["spectral_rows"][10].__setitem__("r", float(x["spectral_rows"][10]["r"])))
    add("spectral_vector", lambda x: x["spectral_rows"][20]["krawtchouk_values"].__setitem__(0, 999))
    add("spectral_norm", lambda x: x["spectral_rows"][30].__setitem__("weighted_norm", 1))
    add("spectral_extra", lambda x: x["spectral_rows"][0].__setitem__("extra", 1))
    add("spectral_omit", lambda x: x["spectral_rows"].pop())
    add("spectral_duplicate_coordinate", lambda x: x["spectral_rows"].__setitem__(1, copy.deepcopy(x["spectral_rows"][0])))
    add("subset_particle", lambda x: x["subset_rows"][100].__setitem__("particles", 99))
    add("subset_count_bool", lambda x: x["subset_rows"][100].__setitem__("particles", True))
    add("subset_exponent_float", lambda x: x["subset_rows"][100].__setitem__("mirror_phase_minus_i_exponent_mod4", float(x["subset_rows"][100]["mirror_phase_minus_i_exponent_mod4"])))
    add("subset_energy", lambda x: x["subset_rows"][1000].__setitem__("twice_energy_over_omega", 99))
    add("subset_phase", lambda x: x["subset_rows"][6000].__setitem__("mirror_phase_minus_i_exponent_mod4", 99))
    add("subset_extra", lambda x: x["subset_rows"][0].__setitem__("extra", 1))
    add("subset_omit", lambda x: x["subset_rows"].pop())
    add("subset_duplicate_coordinate", lambda x: x["subset_rows"].__setitem__(10, copy.deepcopy(x["subset_rows"][9])))
    add("energy_value", lambda x: x["energy_multiplicity_rows"][5].__setitem__("multiplicity", 99))
    add("energy_extra", lambda x: x["energy_multiplicity_rows"][0].__setitem__("extra", 1))
    add("energy_omit", lambda x: x["energy_multiplicity_rows"].pop())
    add("energy_duplicate", lambda x: x["energy_multiplicity_rows"].__setitem__(1, copy.deepcopy(x["energy_multiplicity_rows"][0])))
    add("endpoint_phase", lambda x: x["endpoint_rows"][20].__setitem__("amplitude_phase_minus_i_exponent_mod4", 3))
    add("endpoint_phase_bool", lambda x: x["endpoint_rows"][0].__setitem__("amplitude_phase_minus_i_exponent_mod4", False))
    add("endpoint_count_float", lambda x: x["endpoint_rows"][40].__setitem__("half_transfer_probability_numerator", float(x["endpoint_rows"][40]["half_transfer_probability_numerator"])))
    add("endpoint_radicand", lambda x: x["endpoint_rows"][40].__setitem__("amplitude_binomial_radicand", 99))
    add("endpoint_sine", lambda x: x["endpoint_rows"][60].__setitem__("amplitude_sine_power", 99))
    add("endpoint_cosine", lambda x: x["endpoint_rows"][80].__setitem__("amplitude_cosine_power", 99))
    add("endpoint_extra", lambda x: x["endpoint_rows"][0].__setitem__("extra", 1))
    add("endpoint_omit", lambda x: x["endpoint_rows"].pop())
    add("endpoint_duplicate", lambda x: x["endpoint_rows"].__setitem__(1, copy.deepcopy(x["endpoint_rows"][0])))
    add("gaussian_coefficient", lambda x: x["gaussian_q_binomial_rows"][30]["coefficients"].__setitem__(0, 99))
    add("gaussian_coefficient_bool", lambda x: x["gaussian_q_binomial_rows"][0]["coefficients"].__setitem__(0, True))
    add("count_float", lambda x: x["counts"].__setitem__("spectral_rows", 66.0))
    add("gaussian_extra", lambda x: x["gaussian_q_binomial_rows"][0].__setitem__("extra", 1))
    add("gaussian_omit", lambda x: x["gaussian_q_binomial_rows"].pop())
    add("gaussian_duplicate", lambda x: x["gaussian_q_binomial_rows"].__setitem__(2, copy.deepcopy(x["gaussian_q_binomial_rows"][1])))

    yaml_mutations = [
        ("yaml_duplicate", yaml_text + "\ncandidate_id: HCS-C366\n"),
        ("yaml_merge", yaml_text + "\nmerge_target:\n  <<: {bad: value}\n"),
        ("yaml_nonstring", yaml_text + "\n7: seven\n"),
        ("yaml_anchor", yaml_text.replace("title: ", "title: &owned ", 1)),
        ("yaml_alias", yaml_text + "\nalias_field: *missing\n"),
        ("yaml_implicit_timestamp", yaml_text.replace("evaluation_date: '2026-09-04'", "evaluation_date: 2026-09-04")),
        ("yaml_unknown", yaml_text + "\nunexpected_field: true\n"),
        ("yaml_type", yaml_text.replace("fixed_epoch: 1788480000", "fixed_epoch: '1788480000'")),
        ("yaml_authority", yaml_text.replace("evaluator_authority: flow_systems", "evaluator_authority: wrong")),
        ("yaml_artifacts", yaml_text.replace("artifact_paths:\n", "artifact_paths: wrong\n", 1)),
        ("yaml_gate_status", yaml_text.replace("evidence_status: PROVED", "evidence_status: STOP_SCOPED", 1)),
        ("yaml_gate_verdict", yaml_text.replace("verdict: A1_WEAK", "verdict: A1_PASS_ANALYTIC", 1)),
        ("yaml_route_b", yaml_text.replace("route_b_invocation_allowed: false", "route_b_invocation_allowed: true")),
        ("yaml_scope_flag", yaml_text.replace("claims_target_zero_match: false", "claims_target_zero_match: true")),
        ("yaml_finite_role", yaml_text.replace("finite_evidence_role: exact spectrum", "finite_evidence_role: finite proof of exact spectrum")),
        ("yaml_nested_duplicate", yaml_text.replace("  evidence_status: PROVED\n", "  evidence_status: PROVED\n  evidence_status: PROVED\n", 1)),
    ]

    rejected = 0
    with tempfile.TemporaryDirectory(prefix="c366-mutations-") as directory_name:
        directory = Path(directory_name)
        for label, change in changes:
            item = copy.deepcopy(base)
            change(item)
            repair(item)
            encoded = (json.dumps(item, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode()
            reject(encoded, yaml_bytes, label, directory)
            rejected += 1
        stale = copy.deepcopy(base)
        stale["scope_literal"] = "STALE_HASH_CONTROL"
        reject((json.dumps(stale, sort_keys=True) + "\n").encode(), yaml_bytes,
               "stale_hash_control", directory)
        rejected += 1
        duplicate_json = base_bytes.replace(b'  "candidate_id": "HCS-C366",',
                                            b'  "candidate_id": "HCS-C366",\n  "candidate_id": "HCS-C366",', 1)
        reject(duplicate_json, yaml_bytes, "json_duplicate", directory); rejected += 1
        nonfinite_json = base_bytes.replace(b'  "fixed_epoch": 1788480000,',
                                            b'  "fixed_epoch": NaN,', 1)
        reject(nonfinite_json, yaml_bytes, "json_nonfinite", directory); rejected += 1
        for label, mutated in yaml_mutations:
            reject(base_bytes, mutated.encode(), label, directory)
            rejected += 1
    expected = len(changes) + 3 + len(yaml_mutations)
    assert rejected == expected
    print(f"C366 hostile mutation suite: PASS ({rejected}/{expected} rejected; "
          f"repaired_hash={len(changes)} strict_yaml={len(yaml_mutations)})")


if __name__ == "__main__":
    main()
