#!/usr/bin/env python3
"""Hostile repaired-hash and stale-hash rejection audit for HCS-C207."""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c207_barenblatt_evidence.json"
CHECKER = Path(__file__).with_name("c207_barenblatt_checker.py")
WRONG_DECIMAL_82 = "1." + "0" * 81


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    blob = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(blob).hexdigest()


def must_reject(candidate: dict, label: str, repair_hash: bool) -> None:
    if repair_hash:
        candidate["payload_sha256"] = payload_hash(candidate)
    with tempfile.TemporaryDirectory(prefix="c207-mutation-") as directory:
        path = Path(directory) / "evidence.json"
        path.write_text(json.dumps(candidate, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        process = subprocess.run(
            [sys.executable, str(CHECKER), "--evidence", str(path)],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True,
        )
    if process.returncode == 0:
        raise AssertionError(f"checker accepted hostile mutation: {label}")


def main() -> None:
    canonical = json.loads(EVIDENCE.read_text())
    repaired: list[tuple[str, object]] = []

    def add(name: str, mutator) -> None:
        repaired.append((name, mutator))

    add("source_commit_corruption", lambda d: d.__setitem__("source_commit", "0" * 40))
    add("evaluator_hash_corruption", lambda d: d["evaluator"].__setitem__("sha256", "0" * 64))
    add("scope_literal_corruption", lambda d: d.__setitem__("scope_literal", "EXPANDED_SCOPE"))
    add("unknown_top_key", lambda d: d.__setitem__("unsafe_extra", True))
    add("unknown_nested_theorem_key", lambda d: d["theorem"].__setitem__("unsafe_extra", True))
    add("frozen_profile_class_expansion", lambda d: d["frozen_object"].__setitem__("profile_class", "arbitrary Cauchy solutions"))
    add("theorem_porous_corruption", lambda d: d["theorem"].__setitem__("porous", "corrupted"))
    add("theorem_pressure_corruption", lambda d: d["theorem"].__setitem__("pressure", "corrupted"))
    add("theorem_rescaled_corruption", lambda d: d["theorem"].__setitem__("rescaled", "corrupted"))
    add("theorem_free_energy_corruption", lambda d: d["theorem"].__setitem__("free_energy", "corrupted"))
    add("theorem_dissipation_expansion", lambda d: d["theorem"].__setitem__("dissipation", "unconditional for all Cauchy solutions"))
    add("theorem_uniqueness_expansion", lambda d: d["theorem"].__setitem__("uniqueness", "all solutions are unique"))
    add("mass_beta_zero", lambda d: d["regression"]["profiles"][0]["derived"].__setitem__("mass_beta", "0.0"))

    def corrupt_chemical_joint(data: dict) -> None:
        row = data["regression"]["profiles"][0]
        row["derived"]["chemical_constant"] = WRONG_DECIMAL_82
        for sample in row["samples"]:
            if sample["chemical_potential"] is not None:
                sample["chemical_potential"] = WRONG_DECIMAL_82

    add("chemical_constant_and_samples_joint_corruption", corrupt_chemical_joint)
    add("duplicate_case_grid", lambda d: d["regression"]["profiles"].__setitem__(1, deepcopy(d["regression"]["profiles"][0])))
    add("missing_case_grid", lambda d: d["regression"]["profiles"].pop())
    add("corrupted_case_id", lambda d: d["regression"]["profiles"][0].__setitem__("case_id", "duplicate-looking-id"))
    add("expanded_m_grid", lambda d: d["regression"]["profiles"][0].__setitem__("m", "1/5"))
    add("duplicate_sample_z", lambda d: d["regression"]["profiles"][0]["samples"].__setitem__(1, deepcopy(d["regression"]["profiles"][0]["samples"][0])))
    add("duplicate_moment_r", lambda d: d["regression"]["profiles"][0]["moments"].__setitem__(1, deepcopy(d["regression"]["profiles"][0]["moments"][0])))
    add("working_precision_corruption", lambda d: d["summary"].__setitem__("working_decimal_digits", 82))
    add("serialized_precision_corruption", lambda d: d["summary"].__setitem__("serialized_significant_digits", 100))
    add("shortened_decimal_serialization", lambda d: d["regression"]["profiles"][0]["derived"].__setitem__("C", "1.0"))
    add("fast_support_null_rule_corruption", lambda d: d["regression"]["profiles"][0]["derived"].__setitem__("support_radius_at_t1", WRONG_DECIMAL_82))
    add("heat_mass_beta_null_rule_corruption", lambda d: d["regression"]["profiles"][8]["derived"].__setitem__("mass_beta", WRONG_DECIMAL_82))
    add("porous_exterior_chemical_null_rule_corruption", lambda d: d["regression"]["profiles"][10]["samples"][3].__setitem__("chemical_potential", d["regression"]["profiles"][10]["derived"]["chemical_constant"]))
    add("moment_status_corruption", lambda d: d["regression"]["profiles"][2]["moments"][2].__setitem__("status", "finite"))
    add("finite_moment_coefficient_null", lambda d: d["regression"]["profiles"][0]["moments"][0].__setitem__("coefficient", None))
    add("route_tuple_promotion", lambda d: d["route_a"].__setitem__("tuple", ["A0_PASS", "A1_PASS", "A2_PASS", "A3_PASS", "A4_PASS"]))
    add("route_strongest_positive_hp_promotion", lambda d: d["route_a"].__setitem__("strongest_positive", "A Hilbert--Polya operator is constructed."))
    add("forbidden_scope_flag", lambda d: d["scope_flags"].__setitem__("claims_root_numbers", True))
    add("citation_corruption", lambda d: d["citations"][0].__setitem__("claim", "priority and novelty certification"))
    add("nonclaims_cleared", lambda d: d.__setitem__("nonclaims", []))

    repaired_names = []
    for name, mutator in repaired:
        candidate = deepcopy(canonical)
        mutator(candidate)
        must_reject(candidate, name, repair_hash=True)
        repaired_names.append(name)

    stale = deepcopy(canonical)
    stale["headline"] = "stale hash mutation"
    must_reject(stale, "stale_payload_hash", repair_hash=False)
    print(json.dumps({
        "status": "C207_MUTATION_PASS",
        "repaired_hash_rejections": len(repaired_names),
        "stale_hash_rejections": 1,
        "total_rejections": len(repaired_names) + 1,
        "repaired_attack_names": repaired_names,
        "stale_attack_names": ["stale_payload_hash"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
