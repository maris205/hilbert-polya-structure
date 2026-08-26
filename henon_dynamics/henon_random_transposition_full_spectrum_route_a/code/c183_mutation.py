#!/usr/bin/env python3
"""Hostile repaired-hash and stale-hash mutations for HCS-C183."""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c183_random_transposition_evidence.json"
CHECKER = ROOT / "code/c183_random_transposition_checker.py"

def rehash(data: dict) -> None:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    data["payload_sha256"] = sha256(raw).hexdigest()

def rejected(data: dict) -> bool:
    with tempfile.TemporaryDirectory(prefix="c183-mutation-") as tmp:
        path = Path(tmp) / "mutated.json"
        path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        result = subprocess.run([sys.executable, str(CHECKER), str(path)], capture_output=True, text=True)
        return result.returncode != 0

def main() -> None:
    base = json.loads(EVIDENCE.read_text())
    mutations = []
    def add(name, fn):
        item = deepcopy(base)
        fn(item)
        rehash(item)
        mutations.append((name, item))

    add("candidate", lambda d: d.__setitem__("candidate_id", "HCS-C000"))
    add("date", lambda d: d.__setitem__("date_utc", "2026-08-25"))
    add("commit", lambda d: d.__setitem__("source_commit", "0" * 40))
    add("scope", lambda d: d.__setitem__("scope_literal", "BROKEN"))
    add("evaluator", lambda d: d["evaluator"].__setitem__("version", "9.9"))
    add("evaluator_path", lambda d: d["evaluator"].__setitem__("path", "wrong.md"))
    add("evaluator_hash", lambda d: d["evaluator"].__setitem__("sha256", "0" * 64))
    add("source_object", lambda d: d["source_lock"].__setitem__("object", "different chain"))
    add("source_family", lambda d: d["source_lock"].__setitem__("family", "n=7 only"))
    add("clock", lambda d: d["source_lock"].__setitem__("clock", "two steps"))
    add("source_measure", lambda d: d["source_lock"].__setitem__("measure", "nonuniform"))
    add("source_operator", lambda d: d["source_lock"].__setitem__("operator", "BROKEN"))
    add("source_determinant", lambda d: d["source_lock"].__setitem__("determinant_convention", "Artin--Mazur on frozen S_n"))
    add("source_cutoff", lambda d: d["source_lock"].__setitem__("cutoff", "fitted cutoff"))
    add("source_allowed", lambda d: d["source_lock"].__setitem__("allowed_data", "target tables"))
    add("source_forbidden", lambda d: d["source_lock"].__setitem__("forbidden_data", "none"))
    add("n_min", lambda d: d["finite_replay"].__setitem__("n_min", 1))
    add("n_max_999", lambda d: d["finite_replay"].__setitem__("n_max", 999))
    add("moment_max", lambda d: d["finite_replay"].__setitem__("moment_max", 999))
    add("partition_count_metadata", lambda d: d["finite_replay"].__setitem__("partition_row_count", 999))
    add("moment_count_metadata", lambda d: d["finite_replay"].__setitem__("moment_row_count", 999))
    add("factor_count_metadata", lambda d: d["finite_replay"].__setitem__("factor_row_count", 999))
    add("partition", lambda d: d["finite_replay"]["partition_rows"][3].__setitem__("partition", [99]))
    add("conjugate", lambda d: d["finite_replay"]["partition_rows"][7].__setitem__("conjugate_partition", [1]))
    add("dimension", lambda d: d["finite_replay"]["partition_rows"][10].__setitem__("hook_dimension", 999))
    add("content", lambda d: d["finite_replay"]["partition_rows"][20].__setitem__("content_numerator", 1))
    add("ratio", lambda d: d["finite_replay"]["partition_rows"][30]["transposition_character_ratio"].__setitem__("numerator", 91))
    add("eigenvalue", lambda d: d["finite_replay"]["partition_rows"][40]["lazy_eigenvalue"].__setitem__("denominator", 99))
    add("multiplicity", lambda d: d["finite_replay"]["partition_rows"][50].__setitem__("regular_multiplicity", 0))
    add("trace", lambda d: d["finite_replay"]["moment_rows"][15]["operator_trace"].__setitem__("numerator", 123))
    add("return", lambda d: d["finite_replay"]["moment_rows"][25].__setitem__("ordered_pair_word_return_count", 7))
    add("l2", lambda d: d["finite_replay"]["moment_rows"][35]["l2_density_distance_squared"].__setitem__("numerator", 88))
    add("factor", lambda d: d["finite_replay"]["factor_rows"][10].__setitem__("multiplicity", 4))
    add("broken_factor_string", lambda d: d["finite_replay"]["factor_rows"][0].__setitem__("determinant_factor", "BROKEN"))
    add("gap", lambda d: d["finite_replay"]["summaries"][5]["spectral_gap"].__setitem__("numerator", 7))
    add("A0", lambda d: d["route_a"]["tuple"].__setitem__(0, "A0_PASS"))
    add("A1", lambda d: d["route_a"]["tuple"].__setitem__(1, "A1_WEAK"))
    add("A0_qualification", lambda d: d["route_a"].__setitem__("A0_qualification", "A0_PASS_ARITHMETIC"))
    add("A1_pass_qualification", lambda d: d["route_a"].__setitem__("A1_qualification", "A1_PASS_CANONICAL_ORBITS"))
    add("A2_qualification", lambda d: d["route_a"].__setitem__("A2_qualification", "A2_PASS_TARGET"))
    add("A3_qualification", lambda d: d["route_a"].__setitem__("A3_qualification", "A3_PASS"))
    add("A4_qualification", lambda d: d["route_a"].__setitem__("A4_qualification", "A4_TARGET_OPERATOR"))
    add("overall", lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_SUCCESS"))
    add("route_b", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("target", lambda d: d["scope_flags"].__setitem__("used_target_prime_table", True))
    add("frozen_map", lambda d: d["mixing_and_operator_boundary"].__setitem__("frozen_phase_space_boundary", "P_n is a deterministic map on frozen S_n"))
    add("frozen_determinant", lambda d: d["mixing_and_operator_boundary"].__setitem__("frozen_determinant_boundary", "det(I-z P_n) is an unweighted Artin--Mazur determinant on frozen S_n"))
    add("weighted_product_denial", lambda d: d["mixing_and_operator_boundary"].__setitem__("weighted_path_cycle_product", "no canonical primitive product exists after any lift"))
    add("path_owner_equals_frozen_owner", lambda d: d["mixing_and_operator_boundary"].__setitem__("owner_change_boundary", "the weighted path owner is identical to the frozen S_n owner"))
    add("a1_boundary", lambda d: d["mixing_and_operator_boundary"].__setitem__("a1_failure_boundary", "A1 passes after the path lift"))
    add("source_key", lambda d: d["source_registry"][0].__setitem__("key", "fake"))
    add("source_title", lambda d: d["source_registry"][0].__setitem__("title", "Fake title"))
    add("source_authors", lambda d: d["source_registry"][0].__setitem__("authors", "Nobody"))
    add("source_year_1900", lambda d: d["source_registry"][0].__setitem__("year", 1900))
    add("doi", lambda d: d["source_registry"][0].__setitem__("doi", "fake"))
    add("source_role", lambda d: d["source_registry"][0].__setitem__("role", "new theorem claimed"))
    add("nonclaim", lambda d: d["nonclaims"].__setitem__(1, "weighted path cycles are frozen deterministic orbits"))

    repaired = 0
    for name, item in mutations:
        if not rejected(item):
            raise AssertionError(f"checker accepted repaired-hash mutation {name}")
        repaired += 1
    stale = deepcopy(base)
    stale["finite_replay"]["moment_rows"][0]["ordered_pair_word_return_count"] = 2
    if not rejected(stale):
        raise AssertionError("checker accepted stale-hash mutation")
    print(json.dumps({"status": "C183_MUTATION_PASS", "repaired_hash_rejections": repaired, "stale_hash_rejections": 1, "total_rejections": repaired + 1}, sort_keys=True))

if __name__ == "__main__":
    main()
