#!/usr/bin/env python3
"""Hostile repaired-hash semantic and stale-hash mutations for HCS-C184."""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c184_spectral_decimation_evidence.json"
CHECKER = ROOT / "code/c184_spectral_decimation_checker.py"


def rehash(data: dict) -> None:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    data["payload_sha256"] = sha256(raw).hexdigest()


def rejected(data: dict) -> bool:
    with tempfile.TemporaryDirectory(prefix="c184-mutation-") as temporary:
        path = Path(temporary) / "mutated.json"
        path.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
        result = subprocess.run([sys.executable, str(CHECKER), str(path)], capture_output=True, text=True)
        return result.returncode != 0


def main() -> None:
    base = json.loads(EVIDENCE.read_text())
    mutations = []

    def add(name, operation):
        item = deepcopy(base)
        operation(item)
        rehash(item)
        mutations.append((name, item))

    add("schema", lambda d: d.__setitem__("schema", "BROKEN"))
    add("candidate", lambda d: d.__setitem__("candidate_id", "HCS-C000"))
    add("date", lambda d: d.__setitem__("date_utc", "2026-08-25"))
    add("commit", lambda d: d.__setitem__("source_commit", "0" * 40))
    add("artifact_base", lambda d: d.__setitem__("artifact_path_base", "wrong"))
    add("scope", lambda d: d.__setitem__("scope_literal", "BROKEN"))
    add("evaluator_path", lambda d: d["evaluator"].__setitem__("authority_path", "wrong.md"))
    add("evaluator_version", lambda d: d["evaluator"].__setitem__("version", "9.9"))
    add("evaluator_hash", lambda d: d["evaluator"].__setitem__("authority_sha256", "0" * 64))
    for field, value in (
        ("object", "normalized Laplacian"), ("family", "m=3 only"),
        ("arithmetic_origin", "prime labels"), ("clock", "physical time"),
        ("normalization", "degree-normalized"), ("determinant_convention", "target zeta"),
        ("cutoff", "fitted cutoff"), ("precision", "uncertified float"),
        ("allowed_data", "target tables"), ("forbidden_data", "none"),
    ):
        add("source_" + field, lambda d, f=field, v=value: d["source_lock"].__setitem__(f, v))
    add("R_map", lambda d: d["all_level_theorem"].__setitem__("renormalization_map", "R(t)=t(4-t)"))
    add("exceptional_values", lambda d: d["all_level_theorem"].__setitem__("exceptional_values", [2, 5]))
    add("forced_three", lambda d: d["all_level_theorem"].__setitem__("six_series", "both branches immediately"))
    add("recurrence", lambda d: d["all_level_theorem"].__setitem__("characteristic_recurrence", "BROKEN"))
    add("determinant_theorem", lambda d: d["all_level_theorem"].__setitem__("determinant", "det=1"))
    add("owner_boundary", lambda d: d["all_level_theorem"].__setitem__("owner_boundary", "physical-time map"))
    add("level_min", lambda d: d["finite_regression"].__setitem__("level_min", 0))
    add("level_max", lambda d: d["finite_regression"].__setitem__("level_max", 99))
    add("level_count", lambda d: d["finite_regression"].__setitem__("level_row_count", 99))
    add("lineage_count", lambda d: d["finite_regression"].__setitem__("lineage_row_count", 99))
    add("coefficient_cells", lambda d: d["finite_regression"].__setitem__("characteristic_coefficient_cells", 1))
    add("graph_cells", lambda d: d["finite_regression"].__setitem__("graph_eigenvalue_cells", 1))
    add("dimension", lambda d: d["finite_regression"]["level_rows"][2].__setitem__("interior_dimension", 40))
    add("multiplicity_sum", lambda d: d["finite_regression"]["level_rows"][3].__setitem__("multiplicity_sum", 119))
    add("heat_trace", lambda d: d["finite_regression"]["level_rows"][1].__setitem__("heat_trace_at_zero", 11))
    add("heat_derivative", lambda d: d["finite_regression"]["level_rows"][1].__setitem__("negative_heat_trace_derivative_at_zero", 47))
    add("zeta_zero", lambda d: d["finite_regression"]["level_rows"][4].__setitem__("spectral_zeta_at_zero", 362))
    add("determinant_exponent", lambda d: d["finite_regression"]["level_rows"][3]["determinant_prime_exponents"].__setitem__("prime_3", 1))
    add("determinant", lambda d: d["finite_regression"]["level_rows"][2].__setitem__("determinant", "7"))
    add("coefficient", lambda d: d["finite_regression"]["level_rows"][2]["characteristic_polynomial_coefficients_ascending"].__setitem__(4, "17"))
    add("coefficient_hash", lambda d: d["finite_regression"]["level_rows"][0].__setitem__("characteristic_polynomial_coefficients_sha256", "0" * 64))
    add("graph_error", lambda d: d["finite_regression"]["level_rows"][4].__setitem__("graph_diagonalization_max_abs_error", "9.9e-1"))
    add("lineage_series", lambda d: d["finite_regression"]["lineage_rows"][20].__setitem__("series", "7-series"))
    add("lineage_birth", lambda d: d["finite_regression"]["lineage_rows"][30].__setitem__("birth_generation", 99))
    add("lineage_word", lambda d: d["finite_regression"]["lineage_rows"][40].__setitem__("branch_word", "BROKEN"))
    add("lineage_value", lambda d: d["finite_regression"]["lineage_rows"][50].__setitem__("eigenvalue_decimal", "99"))
    add("lineage_multiplicity", lambda d: d["finite_regression"]["lineage_rows"][60].__setitem__("multiplicity", 0))
    add("lineage_forced", lambda d: d["finite_regression"]["lineage_rows"][19].__setitem__("forced_three", False))
    for axis, value in (("A0", "A0_PASS"), ("A1", "A1_WEAK"), ("A2", "A2_ANALYTIC_DETERMINANT"), ("A3", "A3_EXACT_DIVISOR_CANDIDATE"), ("A4", "A4_ROUTE_B_READY")):
        add("route_" + axis, lambda d, a=axis, v=value: d["route_a_verdict"].__setitem__(a, v))
    add("A0_qualification", lambda d: d["route_a_verdict"].__setitem__("A0_qualification", "PRIMES"))
    add("A1_qualification", lambda d: d["route_a_verdict"].__setitem__("A1_qualification", "PHYSICAL_ORBITS"))
    add("A3_qualification", lambda d: d["route_a_verdict"].__setitem__("A3_qualification", "TARGET_FE"))
    add("overall", lambda d: d["route_a_verdict"].__setitem__("overall", "ROUTE_A_SUCCESS_ROUTE_B_READY"))
    add("route_b", lambda d: d["route_a_verdict"].__setitem__("route_b_invocation_allowed", True))
    add("scope_prime", lambda d: d["scope_flags"].__setitem__("used_target_prime_table", True))
    add("scope_time", lambda d: d["scope_flags"].__setitem__("claimed_level_as_physical_time", True))
    add("source_doi", lambda d: d["source_registry"][0].__setitem__("doi", "fake"))
    add("source_author", lambda d: d["source_registry"][0].__setitem__("authors", "Nobody"))
    add("source_year", lambda d: d["source_registry"][0].__setitem__("year", 1900))
    add("integrity_bug", lambda d: d["integrity_modes"].__setitem__("implementation_bug", "SUSPECTED"))
    add("integrity_citation", lambda d: d["integrity_modes"].__setitem__("hallucinated_citation", "SUSPECTED"))
    add("integrity_result", lambda d: d["integrity_modes"].__setitem__("hallucinated_result", "SUSPECTED"))
    add("integrity_shortcut", lambda d: d["integrity_modes"].__setitem__("shortcut_reliance", "SUSPECTED"))
    add("integrity_insight", lambda d: d["integrity_modes"].__setitem__("bug_reframed_as_insight", "SUSPECTED"))
    add("integrity_method", lambda d: d["integrity_modes"].__setitem__("methodology_fabrication", "SUSPECTED"))
    add("integrity_frame", lambda d: d["integrity_modes"].__setitem__("frame_lock", "SUSPECTED"))
    add("nonclaim", lambda d: d["nonclaims"].__setitem__(1, "the branch tree is physical time"))

    repaired = 0
    for name, item in mutations:
        if not rejected(item):
            raise AssertionError(f"checker accepted repaired-hash mutation {name}")
        repaired += 1
    stale = deepcopy(base)
    stale["finite_regression"]["level_rows"][0]["determinant"] = "51"
    if not rejected(stale):
        raise AssertionError("checker accepted stale-hash mutation")
    print(json.dumps({"status": "C184_MUTATION_PASS", "repaired_hash_rejections": repaired, "stale_hash_rejections": 1, "total_rejections": repaired + 1}, sort_keys=True))


if __name__ == "__main__":
    main()
