#!/usr/bin/env python3
"""Hostile repaired-hash and stale-hash mutations for HCS-C187."""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c187_tableau_csp_evidence.json"
CHECKER = ROOT / "code/c187_tableau_csp_checker.py"


def rehash(data: dict) -> None:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    data["payload_sha256"] = sha256(raw).hexdigest()


def rejected(data: dict) -> bool:
    with tempfile.TemporaryDirectory(prefix="c187-mutation-") as temporary:
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
    add("date", lambda d: d.__setitem__("date_utc", "2026-08-25"))
    add("commit", lambda d: d.__setitem__("source_commit", "0" * 40))
    add("scope", lambda d: d.__setitem__("scope_literal", "BROKEN"))
    add("evaluator_path", lambda d: d["evaluator"].__setitem__("path", "wrong.md"))
    add("evaluator_version", lambda d: d["evaluator"].__setitem__("version", "9.9.9"))
    add("evaluator_hash", lambda d: d["evaluator"].__setitem__("sha256", "0" * 64))

    source_mutations = {
        "source_object": ("object", "arbitrary tableaux"),
        "source_family": ("family", "a=b=3 only"),
        "source_phase": ("phase_space", "all partitions"),
        "source_clock": ("clock", "remove 1 instead without declaring the inverse convention"),
        "source_measure": ("measure", "fitted weights"),
        "source_operator": ("operator", "post-hoc diagonal operator"),
        "source_q_shift": ("q_hook_convention", "q-shifted major-index polynomial"),
        "source_determinant": ("determinant_convention", "target determinant"),
        "source_cutoff": ("cutoff", "finite enumeration proves all rectangles"),
        "source_allowed": ("allowed_data", "target zero table"),
        "source_forbidden": ("forbidden_data", "none"),
    }
    for name, (key, value) in source_mutations.items():
        add(name, lambda d, key=key, value=value: d["source_lock"].__setitem__(key, value))

    add("attribution_status", lambda d: d["attribution"].__setitem__("status", "NEW_THEOREM_CLAIMED"))
    add("attribution_owner", lambda d: d["attribution"].__setitem__("all_rectangle_owner", "package owns CSP"))
    add("attribution_order", lambda d: d["attribution"].__setitem__("order_background", "unattributed"))
    add("attribution_increment", lambda d: d["attribution"].__setitem__("package_increment", "global novelty"))
    add("attribution_finite_proof", lambda d: d["attribution"].__setitem__("finite_evidence_role", "finite enumeration proves the infinite theorem"))

    theorem_mutations = {
        "theorem_exact_order": ("order_bound", "j has exact order N for every rectangle"),
        "theorem_shift": ("csp_fixed_count", "Fix(j^d)=q^shift F_ab(zeta_N^d)"),
        "theorem_period": ("exact_period", "P_l=Fix(j^l)"),
        "theorem_cycles": ("cycle_count", "C_l=P_l"),
        "theorem_zeta": ("zeta", "zeta_j(z)=1"),
        "theorem_determinant": ("koopman_determinant", "det(I-zU)=zeta_j(z)"),
        "theorem_spectrum": ("spectral_multiplicity", "every root has multiplicity one"),
        "theorem_trace": ("trace", "Tr(U^d)=0"),
        "theorem_reversor": ("reversor", "evacuation commutes with promotion"),
        "theorem_identity": ("identity_boundary", "one row has order N"),
    }
    for name, (key, value) in theorem_mutations.items():
        add(name, lambda d, key=key, value=value: d["theorem"].__setitem__(key, value))

    for name, key in [
        ("boundary_progress", "progress"),
        ("boundary_order", "order_boundary"),
        ("boundary_proof", "proof_boundary"),
        ("boundary_arithmetic", "arithmetic_boundary"),
        ("boundary_operator", "operator_boundary"),
    ]:
        add(name, lambda d, key=key: d["progress_and_boundary"].__setitem__(key, "BROKEN"))

    finite_mutations = {
        "a_min": ("a_min", 0),
        "a_max": ("a_max", 99),
        "b_min": ("b_min", 0),
        "b_max": ("b_max", 99),
        "enum_n": ("enumeration_n_max", 99),
        "enum_population": ("enumeration_tableau_max", 1),
        "rectangle_count": ("rectangle_row_count", 999),
        "iterate_count": ("iterate_row_count", 999),
        "period_count": ("period_row_count", 999),
        "spectral_count": ("spectral_row_count", 999),
        "enum_count": ("enumeration_rectangle_count", 999),
    }
    for name, (key, value) in finite_mutations.items():
        add(name, lambda d, key=key, value=value: d["finite_replay"].__setitem__(key, value))

    add("rectangle_shape", lambda d: d["finite_replay"]["rectangles"][8].__setitem__("shape", [99]))
    add("rectangle_hook", lambda d: d["finite_replay"]["rectangles"][9]["hook_multiset"].__setitem__("1", 99))
    add("rectangle_count_value", lambda d: d["finite_replay"]["rectangles"][14].__setitem__("tableau_count", 999))
    add("rectangle_q_convention", lambda d: d["finite_replay"]["rectangles"][8].__setitem__("q_hook_convention", "shifted"))
    add("rectangle_cyclotomic", lambda d: d["finite_replay"]["rectangles"][14]["q_hook_cyclotomic_exponents"].__setitem__("2", 99))
    add("rectangle_degree", lambda d: d["finite_replay"]["rectangles"][14].__setitem__("q_hook_degree", 999))
    add("rectangle_coefficient", lambda d: d["finite_replay"]["rectangles"][14]["q_hook_coefficients"].__setitem__(0, 7))
    add("rectangle_coefficient_hash", lambda d: d["finite_replay"]["rectangles"][14].__setitem__("q_hook_coefficients_sha256", "0" * 64))
    add("rectangle_order_bound", lambda d: d["finite_replay"]["rectangles"][14].__setitem__("promotion_order_divides", 999))
    add("rectangle_actual_order", lambda d: d["finite_replay"]["rectangles"][7].__setitem__("actual_promotion_order", 4))
    add("rectangle_identity", lambda d: d["finite_replay"]["rectangles"][1].__setitem__("identity_boundary", False))
    add("rectangle_enumeration", lambda d: d["finite_replay"]["rectangles"][14].__setitem__("enumeration_regression_selected", False))
    add("rectangle_cycle_lengths", lambda d: d["finite_replay"]["rectangles"][14].__setitem__("nonzero_cycle_lengths", [99]))
    add("rectangle_zeta", lambda d: d["finite_replay"]["rectangles"][14]["zeta_factors"][0].__setitem__("exponent", 99))
    add("rectangle_determinant", lambda d: d["finite_replay"]["rectangles"][14]["koopman_determinant_factors"][0].__setitem__("exponent", 99))

    add("iterate_gcd", lambda d: d["finite_replay"]["iterate_rows"][100].__setitem__("gcd_n_iterate", 99))
    add("iterate_root_order", lambda d: d["finite_replay"]["iterate_rows"][100].__setitem__("root_order", 99))
    add("iterate_fixed", lambda d: d["finite_replay"]["iterate_rows"][100].__setitem__("fixed_count", 99))
    add("iterate_coordinate", lambda d: d["finite_replay"]["iterate_rows"][100].__setitem__("iterate", 99))
    add("period_fixed", lambda d: d["finite_replay"]["period_rows"][80].__setitem__("fixed_at_period", 99))
    add("period_exact", lambda d: d["finite_replay"]["period_rows"][80].__setitem__("exact_period_count", 99))
    add("period_cycle", lambda d: d["finite_replay"]["period_rows"][80].__setitem__("cycle_count", 99))
    add("spectral_multiplicity", lambda d: d["finite_replay"]["spectral_rows"][100].__setitem__("multiplicity", 99))

    add("route_A0", lambda d: d["route_a"]["tuple"].__setitem__(0, "A0_PASS"))
    add("route_A1", lambda d: d["route_a"]["tuple"].__setitem__(1, "A1_PASS_ANALYTIC"))
    add("route_A2", lambda d: d["route_a"]["tuple"].__setitem__(2, "A2_PASS"))
    add("route_A3", lambda d: d["route_a"]["tuple"].__setitem__(3, "A3_PASS"))
    add("route_A4", lambda d: d["route_a"]["tuple"].__setitem__(4, "A4_HILBERT_POLYA"))
    add("route_overall", lambda d: d["route_a"].__setitem__("overall", "ROUTE_A_SUCCESS"))
    add("route_A0_qualification", lambda d: d["route_a"].__setitem__("A0_qualification", "A0_PASS_AND_PRIME_CLOCK"))
    add("route_A1_qualification", lambda d: d["route_a"].__setitem__("A1_qualification", "A1_PASS_CANONICAL_PRIME_ORBITS"))
    add("route_A2_qualification", lambda d: d["route_a"].__setitem__("A2_qualification", "A2_TARGET_DIVISOR_IDENTIFIED"))
    add("route_A3_qualification", lambda d: d["route_a"].__setitem__("A3_qualification", "A3_TARGET_FUNCTIONAL_EQUATION"))
    add("route_A4_qualification", lambda d: d["route_a"].__setitem__("A4_qualification", "A4_TARGET_OPERATOR_IDENTIFIED"))
    add("route_b", lambda d: d["route_a"].__setitem__("route_b_invocation_allowed", True))

    for name, key in [
        ("scope_zero", "used_target_zero_table"),
        ("scope_prime", "used_target_prime_table"),
        ("scope_local", "used_arithmetic_local_data"),
        ("scope_divisor", "claimed_target_divisor_match"),
        ("scope_fe", "claimed_target_functional_equation"),
        ("scope_hp", "claimed_hilbert_polya"),
        ("scope_exact_order", "claimed_exact_order_n_uniformly"),
        ("scope_novelty", "claimed_global_novelty"),
        ("scope_route_b", "route_b_invocation_allowed"),
    ]:
        add(name, lambda d, key=key: d["scope_flags"].__setitem__(key, True))

    add("source_key", lambda d: d["source_registry"][0].__setitem__("key", "fake"))
    add("source_title", lambda d: d["source_registry"][0].__setitem__("title", "Fake title"))
    add("source_authors", lambda d: d["source_registry"][0].__setitem__("authors", "Nobody"))
    add("source_year", lambda d: d["source_registry"][0].__setitem__("year", 1900))
    add("source_journal", lambda d: d["source_registry"][0].__setitem__("journal", "Fake Journal"))
    add("source_doi", lambda d: d["source_registry"][0].__setitem__("doi", "fake"))
    add("source_arxiv", lambda d: d["source_registry"][0].__setitem__("arxiv", "0000.0000"))
    add("source_role", lambda d: d["source_registry"][0].__setitem__("role", "new theorem claimed"))
    add("haiman_doi", lambda d: d["source_registry"][1].__setitem__("doi", "fake"))
    add("haiman_role", lambda d: d["source_registry"][1].__setitem__("role", "target input"))
    add("nonclaim_order", lambda d: d["nonclaims"].__setitem__(1, "promotion always has exact order N"))
    add("nonclaim_finite", lambda d: d["nonclaims"].__setitem__(2, "finite enumeration proves all rectangles"))
    add("nonclaim_hp", lambda d: d["nonclaims"].__setitem__(5, "Hilbert--Polya operator constructed"))

    repaired = 0
    for name, item in mutations:
        if not rejected(item):
            raise AssertionError(f"checker accepted repaired-hash mutation {name}")
        repaired += 1

    stale = deepcopy(base)
    stale["finite_replay"]["iterate_rows"][0]["fixed_count"] = 2
    if not rejected(stale):
        raise AssertionError("checker accepted stale-hash mutation")

    print(json.dumps({
        "status": "C187_MUTATION_PASS",
        "repaired_hash_rejections": repaired,
        "stale_hash_rejections": 1,
        "total_rejections": repaired + 1,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
