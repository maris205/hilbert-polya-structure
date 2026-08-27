#!/usr/bin/env python3
"""Hostile repaired-hash and stale-hash mutations for HCS-C190."""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c190_bulgarian_necklace_evidence.json"
CHECKER = ROOT / "code/c190_bulgarian_necklace_checker.py"


def rehash(data: dict) -> None:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    data["payload_sha256"] = sha256(raw).hexdigest()


def rejected(data: dict) -> bool:
    with tempfile.TemporaryDirectory(prefix="c190-mutation-") as temporary:
        path = Path(temporary) / "mutated.json"
        path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        result = subprocess.run(
            [sys.executable, str(CHECKER), str(path)],
            capture_output=True,
            text=True,
        )
        return result.returncode != 0


def main() -> None:
    base = json.loads(EVIDENCE.read_text())
    mutations: list[tuple[str, dict]] = []

    def add(name, change) -> None:
        item = deepcopy(base)
        change(item)
        rehash(item)
        mutations.append((name, item))

    add("schema", lambda d: d.__setitem__("schema", "HCS-C000-v1"))
    add("candidate", lambda d: d.__setitem__("candidate_id", "HCS-C000"))
    add("date", lambda d: d.__setitem__("date_utc", "2026-08-26"))
    add("commit", lambda d: d.__setitem__("source_commit", "0" * 40))
    add("scope", lambda d: d.__setitem__("scope_literal", "BROKEN"))
    add("evaluator_path", lambda d: d["evaluator"].__setitem__("path", "wrong.md"))
    add("evaluator_version", lambda d: d["evaluator"].__setitem__("version", "9.9.9"))
    add("evaluator_hash", lambda d: d["evaluator"].__setitem__("sha256", "0" * 64))

    for name, key, value in [
        ("source_object", "object", "invertible solitaire"),
        ("source_family", "family", "N=8 only"),
        ("source_phase", "phase_space", "recurrent set only"),
        ("source_clock", "clock", "two moves"),
        ("source_measure", "measure", "fitted weights"),
        ("source_model", "recurrent_model", "ternary words"),
        ("source_rotation", "rotation_convention", "left rotation without convention"),
        ("source_operator", "operator", "post-hoc diagonal operator"),
        ("source_determinant", "determinant_convention", "target divisor"),
        ("source_cutoff", "cutoff", "finite census proves all N"),
        ("source_allowed", "allowed_data", "target zero table"),
        ("source_forbidden", "forbidden_data", "none"),
    ]:
        add(name, lambda d, key=key, value=value: d["source_lock"].__setitem__(key, value))

    for name, key, value in [
        ("attribution_status", "status", "NEW_THEOREM_CLAIMED"),
        ("attribution_brandt", "recurrent_owner", "package owns Brandt theorem"),
        ("attribution_akin", "dynamical_background", "unattributed"),
        ("attribution_increment", "package_increment", "global novelty"),
        ("attribution_finite", "finite_evidence_role", "finite census proves all N"),
    ]:
        add(name, lambda d, key=key, value=value: d["attribution"].__setitem__(key, value))

    theorem_attacks = {
        "theorem_decomposition": ("decomposition", "N has arbitrary k and r"),
        "theorem_bijection": ("recurrent_bijection", "all partitions are binary words"),
        "theorem_fixed": ("fixed_count", "Fix(T^t)=2^k"),
        "theorem_period": ("exact_period", "P_d=Fix(T^d)"),
        "theorem_zeta": ("zeta", "zeta_T=1"),
        "theorem_koopman": ("koopman", "zero multiplicity is always zero"),
        "theorem_trace": ("trace", "Tr(U^t)=0"),
        "theorem_reversor": ("reversor", "Q commutes with rho"),
        "theorem_triangle": ("triangular_boundary", "triangular decks have many recurrent cycles"),
    }
    for name, (key, value) in theorem_attacks.items():
        add(name, lambda d, key=key, value=value: d["theorem"].__setitem__(key, value))

    for name, key in [
        ("boundary_progress", "progress"),
        ("boundary_transient", "transient_boundary"),
        ("boundary_noninvertible", "noninvertible_boundary"),
        ("boundary_proof", "proof_boundary"),
        ("boundary_arithmetic", "arithmetic_boundary"),
        ("boundary_operator", "operator_boundary"),
    ]:
        add(name, lambda d, key=key: d["progress_and_boundary"].__setitem__(key, "BROKEN"))

    for name, key, value in [
        ("n_min", "n_min", 0),
        ("n_max", "n_max", 99),
        ("system_count", "system_row_count", 999),
        ("partition_population", "partition_population", 1),
        ("word_population", "word_partition_pair_count", 1),
        ("cycle_population", "cycle_row_count", 1),
        ("fixed_population", "fixed_row_count", 1),
        ("period_population", "period_row_count", 1),
        ("spectral_population", "spectral_row_count", 1),
    ]:
        add(name, lambda d, key=key, value=value: d["finite_replay"].__setitem__(key, value))

    # Mutate the first row so the semantic validator rejects before the large
    # independent partition census.  These attacks cover every evidence layer.
    row_attacks = [
        ("row_N", lambda row: row.__setitem__("N", 99)),
        ("row_k", lambda row: row.__setitem__("k", 99)),
        ("row_r", lambda row: row.__setitem__("r", 1)),
        ("row_triangle", lambda row: row.__setitem__("triangular_base", 99)),
        ("row_partition_number", lambda row: row.__setitem__("partition_number", 99)),
        ("row_recurrent", lambda row: row.__setitem__("recurrent_count", 99)),
        ("row_transient", lambda row: row.__setitem__("transient_count", 99)),
        ("row_zero", lambda row: row.__setitem__("full_koopman_zero_algebraic_multiplicity", 99)),
        ("row_reflection_count", lambda row: row.__setitem__("phase_reflection_formula_count", 99)),
        ("row_triangular_flag", lambda row: row.__setitem__("triangular_boundary", False)),
        ("pair_word", lambda row: row["word_partition_pairs"][0].__setitem__("word", "11")),
        ("pair_partition", lambda row: row["word_partition_pairs"][0].__setitem__("partition", [99])),
        ("pair_next_word", lambda row: row["word_partition_pairs"][0].__setitem__("next_word", "11")),
        ("pair_next_partition", lambda row: row["word_partition_pairs"][0].__setitem__("next_partition", [99])),
        ("pair_reflection_word", lambda row: row["word_partition_pairs"][0].__setitem__("reflection_word", "11")),
        ("pair_reflection_partition", lambda row: row["word_partition_pairs"][0].__setitem__("reflection_partition", [99])),
        ("cycle_length", lambda row: row["cycles"][0].__setitem__("length", 99)),
        ("cycle_words", lambda row: row["cycles"][0]["words"].__setitem__(0, "11")),
        ("cycle_partitions", lambda row: row["cycles"][0]["partitions"].__setitem__(0, [99])),
        ("fixed_residue", lambda row: row["fixed_rows"][0].__setitem__("iterate_mod_k", 99)),
        ("fixed_positive", lambda row: row["fixed_rows"][0].__setitem__("positive_iterate_representative", 99)),
        ("fixed_gcd", lambda row: row["fixed_rows"][0].__setitem__("gcd_k_iterate", 99)),
        ("fixed_count", lambda row: row["fixed_rows"][0].__setitem__("fixed_count", 99)),
        ("period_coordinate", lambda row: row["period_rows"][0].__setitem__("period", 99)),
        ("period_fixed", lambda row: row["period_rows"][0].__setitem__("fixed_at_period", 99)),
        ("period_exact", lambda row: row["period_rows"][0].__setitem__("exact_period_count", 99)),
        ("period_cycle", lambda row: row["period_rows"][0].__setitem__("cycle_count", 99)),
        ("spectral_exponent", lambda row: row["spectral_rows"][0].__setitem__("root_exponent_mod_k", 99)),
        ("spectral_multiplicity", lambda row: row["spectral_rows"][0].__setitem__("multiplicity", 99)),
        ("zeta_exponent", lambda row: row["zeta_factors"][0].__setitem__("exponent", 99)),
        ("determinant_exponent", lambda row: row["koopman_determinant_factors"][0].__setitem__("exponent", 99)),
    ]
    for name, attack in row_attacks:
        add(name, lambda d, attack=attack: attack(d["finite_replay"]["rows"][0]))

    for index, value in enumerate(["A0_PASS", "A1_PASS", "A2_PASS", "A3_PASS", "A4_HILBERT_POLYA"]):
        add(f"route_tuple_{index}", lambda d, index=index, value=value: d["route_a"]["tuple"].__setitem__(index, value))
    for name, key, value in [
        ("route_overall", "overall", "ROUTE_A_SUCCESS"),
        ("route_A0", "A0_qualification", "PRIME_CLOCK"),
        ("route_A1", "A1_qualification", "PRIME_ORBITS"),
        ("route_A2", "A2_qualification", "TARGET_DIVISOR"),
        ("route_A3", "A3_qualification", "FUNCTIONAL_EQUATION"),
        ("route_A4", "A4_qualification", "HILBERT_POLYA"),
        ("route_B", "route_b_invocation_allowed", True),
    ]:
        add(name, lambda d, key=key, value=value: d["route_a"].__setitem__(key, value))

    for key in [
        "used_target_zero_table",
        "used_target_prime_table",
        "used_arithmetic_local_data",
        "claimed_target_divisor_match",
        "claimed_target_functional_equation",
        "claimed_hilbert_polya",
        "claimed_global_reversor",
        "claimed_complete_transient_classification",
        "claimed_global_novelty",
        "route_b_invocation_allowed",
    ]:
        add(f"scope_{key}", lambda d, key=key: d["scope_flags"].__setitem__(key, True))

    for name, record, key, value in [
        ("brandt_key", 0, "key", "fake"),
        ("brandt_title", 0, "title", "Fake"),
        ("brandt_author", 0, "authors", "Nobody"),
        ("brandt_year", 0, "year", 1900),
        ("brandt_journal", 0, "journal", "Fake Journal"),
        ("brandt_doi", 0, "doi", "fake"),
        ("brandt_role", 0, "role", "target input"),
        ("akin_doi", 1, "doi", "fake"),
        ("akin_jstor", 1, "jstor_doi", "fake"),
        ("akin_role", 1, "role", "target input"),
    ]:
        add(name, lambda d, record=record, key=key, value=value: d["source_registry"][record].__setitem__(key, value))

    for index in range(len(base["nonclaims"])):
        add(f"nonclaim_{index}", lambda d, index=index: d["nonclaims"].__setitem__(index, "BROKEN"))

    repaired = 0
    for name, item in mutations:
        if not rejected(item):
            raise AssertionError(f"checker accepted repaired-hash mutation {name}")
        repaired += 1

    stale = deepcopy(base)
    stale["finite_replay"]["rows"][0]["fixed_rows"][0]["fixed_count"] = 99
    if not rejected(stale):
        raise AssertionError("checker accepted stale-hash mutation")

    print(json.dumps({
        "status": "C190_MUTATION_PASS",
        "repaired_hash_rejections": repaired,
        "stale_hash_rejections": 1,
        "total_rejections": repaired + 1,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
