#!/usr/bin/env python3
"""Hostile semantic/schema mutation suite for the C241 receipt.

Several mutations repair the outer payload digest so that the independent
checker must reject the changed mathematics rather than merely a stale hash.
"""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c241_luroth_evidence.json"
CHECKER = ROOT / "code/c241_luroth_checker.py"


def repaired_hash(item: dict) -> dict:
    body = dict(item)
    body.pop("payload_sha256", None)
    item["payload_sha256"] = sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()
    return item


def main() -> None:
    pristine = json.loads(EVIDENCE.read_text())
    mutations: list[tuple[str, dict]] = []

    def add(name: str, fn, repaired: bool = False) -> None:
        item = deepcopy(pristine)
        fn(item)
        mutations.append((name, repaired_hash(item) if repaired else item))

    # Branch and word arithmetic.
    add("branch_slope", lambda x: x["regression"]["branch_rows"][0].__setitem__("slope", 3))
    add("branch_interval", lambda x: x["regression"]["branch_rows"][1].__setitem__("interval_left", "0"))
    add("branch_inverse_zero", lambda x: x["regression"]["branch_rows"][2].__setitem__("inverse_at_zero", "99"))
    add("branch_weight", lambda x: x["regression"]["branch_rows"][3].__setitem__("weight_s1", "1/7"))
    add("word_product", lambda x: x["regression"]["word_rows"][0].__setitem__("branch_product", 99))
    add("word_fixed", lambda x: x["regression"]["word_rows"][1].__setitem__("fixed_x_num", 17))
    add("word_u", lambda x: x["regression"]["word_rows"][2].__setitem__("affine_u_den", 1))
    add("word_v", lambda x: x["regression"]["word_rows"][3].__setitem__("affine_v_num", 0))
    add("word_itinerary", lambda x: x["regression"]["word_rows"][4]["itinerary"].__setitem__(0, 99))
    add("word_primitive", lambda x: x["regression"]["word_rows"][31].__setitem__("primitive", False))
    add("word_canonical", lambda x: x["regression"]["word_rows"][32].__setitem__("canonical_word", [6, 2]))
    add("word_decimal", lambda x: x["regression"]["word_rows"][10].__setitem__("fixed_x_decimal", "0.0"))
    add("word_orientation", lambda x: x["regression"]["word_rows"][5].__setitem__("orientation", "reverse"))
    # Necklace, weighted and limiting receipts.
    add("necklace_count", lambda x: x["regression"]["necklace_rows"][4].__setitem__("primitive_necklaces", 0))
    add("necklace_words", lambda x: x["regression"]["necklace_rows"][7].__setitem__("all_words", 1))
    add("weighted_A", lambda x: x["regression"]["weighted_rows"][0].__setitem__("A_M_real", "9"))
    add("weighted_Z", lambda x: x["regression"]["weighted_rows"][1].__setitem__("Z_M_real", "9"))
    add("weighted_domain", lambda x: x["regression"]["weighted_rows"][2].__setitem__("full_product_condition", "|z|<1"))
    add("weighted_divergence", lambda x: x["regression"]["weighted_rows"][-1].__setitem__("full_A_status", "convergent"))
    add("weighted_s_flag", lambda x: x["regression"]["weighted_rows"][0].__setitem__("s_one_telescoping", False))
    add("limit_partial", lambda x: x["regression"]["limit_rows"][0].__setitem__("partial_sum_real", "1"))
    add("limit_tail", lambda x: x["regression"]["limit_rows"][0].__setitem__("tail_upper_bound", "0"))
    add("limit_exact", lambda x: x["regression"]["limit_rows"][0].__setitem__("limit_value_if_exact", "2"))
    add("limit_domain", lambda x: x["regression"]["limit_rows"][1].__setitem__("absolute_convergence_claim", "Re(s)>0"))
    add("finite_series", lambda x: x["regression"]["finite_product_rows"][0]["series_product_coefficients_s1"].__setitem__(1, "0"))
    add("finite_closed", lambda x: x["regression"]["finite_product_rows"][1]["closed_form_coefficients_s1"].__setitem__(2, "0"))
    add("finite_counts", lambda x: x["regression"]["finite_product_rows"][0]["primitive_factor_counts_by_length"].__setitem__(0, 0))
    # Repaired hashes test semantic validation beyond digest validation.
    add("repaired_word", lambda x: x["regression"]["word_rows"][20].__setitem__("multiplier", 1), True)
    add("repaired_necklace", lambda x: x["regression"]["necklace_rows"][10].__setitem__("primitive_necklaces", 999), True)
    add("repaired_weight", lambda x: x["regression"]["weighted_rows"][20].__setitem__("Z_M_real", "1"), True)
    add("repaired_limit", lambda x: x["regression"]["limit_rows"][0].__setitem__("tail_upper_bound", "0"), True)
    add("repaired_finite", lambda x: x["regression"]["finite_product_rows"][1].__setitem__("max_series_length", 3), True)
    # Theorem, frozen object, route and provenance locks.
    add("frozen_map", lambda x: x["frozen_object"].__setitem__("map", "T(x)=x"))
    add("frozen_partition", lambda x: x["frozen_object"].__setitem__("partition", "[0,1]"))
    add("frozen_clock", lambda x: x["frozen_object"].__setitem__("clock", "random clock"))
    add("theorem_branch_image", lambda x: x["theorem"].__setitem__("branch_partition", "onto [0,1]"))
    add("theorem_domain", lambda x: x["theorem"].__setitem__("euler_product_domain", "all complex z"))
    add("theorem_meromorphic", lambda x: x["theorem"].__setitem__("meromorphic_extension", "none"))
    add("theorem_boundary", lambda x: x["theorem"].__setitem__("telescoping_boundary", "A(1)=0"))
    add("identity_formula", lambda x: x["exact_identities"][6].__setitem__("formula", "Z=0"))
    add("route_tuple", lambda x: x["route_a"]["tuple"].__setitem__(4, "A4_NATURAL_QUANTIZATION"))
    add("route_overall", lambda x: x["route_a"].__setitem__("overall", "ROUTE_A_ACCEPTED"))
    add("route_b", lambda x: x["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("scope_flag", lambda x: x["scope_flags"].__setitem__("claims_euler_factors", True))
    add("citation_doi", lambda x: x["citations"][0].__setitem__("doi", "10.0000/fake"), True)
    add("citation_url", lambda x: x["citations"][1].__setitem__("url", "https://example.invalid"))
    add("nonclaim", lambda x: x["nonclaims"].__setitem__(0, "arithmetic primes are claimed"))
    add("unknown_top", lambda x: x.__setitem__("unexpected", True))
    add("unknown_nested", lambda x: x["theorem"].__setitem__("unexpected", True))
    add("stale_hash", lambda x: x.__setitem__("payload_sha256", "0" * 64))
    add("schema", lambda x: x.__setitem__("schema", "wrong"))
    add("candidate_id", lambda x: x.__setitem__("candidate_id", "HCS-C000"))
    add("date", lambda x: x.__setitem__("evaluation_date", "2026-08-31"))
    add("evaluator_hash", lambda x: x["evaluator"].__setitem__("sha256", "0" * 64))
    add("missing_word", lambda x: x["regression"]["word_rows"].pop())
    add("word_order", lambda x: x["regression"]["word_rows"].reverse(), True)

    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    caught: list[str] = []
    with tempfile.TemporaryDirectory(prefix="c241-luroth-mutations-") as td:
        for name, item in mutations:
            path = Path(td) / f"{name}.json"
            path.write_text(json.dumps(item, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            proc = subprocess.run(
                [sys.executable, "-B", str(CHECKER), "--input", str(path)],
                env=env,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
            )
            if proc.returncode != 0:
                caught.append(name)
    assert len(caught) == len(mutations), f"uncaught mutations: {set(name for name, _ in mutations) - set(caught)}"
    print(f"C241 hostile mutations: PASS {len(caught)}/{len(mutations)}")
    print("caught=" + ",".join(caught))


if __name__ == "__main__":
    main()
