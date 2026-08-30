#!/usr/bin/env python3
"""Hostile semantic mutation suite for the C239 receipt."""
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
EVIDENCE = ROOT / "results/c239_shuffle_evidence.json"
CHECKER = ROOT / "code/c239_shuffle_checker.py"


def repaired_hash(item: dict) -> dict:
    body = dict(item)
    body.pop("payload_sha256", None)
    item["payload_sha256"] = sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()
    return item


def main() -> None:
    pristine = json.loads(EVIDENCE.read_text())
    mutations: list[tuple[str, dict]] = []

    def add(name: str, fn, repaired: bool = False) -> None:
        item = deepcopy(pristine)
        fn(item)
        mutations.append((name, repaired_hash(item) if repaired else item))

    # Numeric and combinatorial rows.
    add("atlas_fixed", lambda x: x["regression"]["atlas_rows"][0]["fixed_counts_1_to_order"].__setitem__(0, 99))
    add("atlas_exact", lambda x: x["regression"]["atlas_rows"][1]["exact_period_counts_1_to_order"].__setitem__(0, 123))
    add("atlas_cycles", lambda x: x["regression"]["atlas_rows"][2]["cycle_counts_1_to_order"].__setitem__(0, 77))
    add("atlas_modulus", lambda x: x["regression"]["atlas_rows"][3].__setitem__("modulus_M", 4))
    add("atlas_domain", lambda x: x["regression"]["atlas_rows"][4].__setitem__("domain_size", 1))
    add("atlas_order", lambda x: x["regression"]["atlas_rows"][5].__setitem__("global_order", 1))
    add("atlas_lengths", lambda x: x["regression"]["atlas_rows"][6]["direct_cycle_lengths"].append(999))
    add("position_period", lambda x: x["regression"]["position_rows"][0].__setitem__("position_period", 99))
    add("position_gcd", lambda x: x["regression"]["position_rows"][1].__setitem__("gcd_i_M", 2))
    add("position_reduced", lambda x: x["regression"]["position_rows"][2].__setitem__("reduced_modulus", 1))
    add("position_i", lambda x: x["regression"]["position_rows"][3].__setitem__("position_i", 0))
    add("spectral_zeta_factor", lambda x: x["regression"]["spectral_rows"][0]["zeta_factor_exponents"][0][2].__class__ and x["regression"]["spectral_rows"][0]["zeta_factor_exponents"].__setitem__(0, [1, -1, 999]))
    add("spectral_koopman_factor", lambda x: x["regression"]["spectral_rows"][1]["koopman_characteristic_factor_exponents"].__setitem__(0, [2, -1, 999]))
    add("spectral_zeta_denominator_coeff", lambda x: x["regression"]["spectral_rows"][2]["zeta_denominator_coefficients_low_to_high"].__setitem__(0, 7))
    add("spectral_char_coeff", lambda x: x["regression"]["spectral_rows"][3]["koopman_coefficients_low_to_high"].__setitem__(0, 8))
    add("representative_cycle", lambda x: x["regression"]["representative_cycles"][0]["members_forward"].__setitem__(0, 2))
    add("grid_parameter", lambda x: x["regression"]["parameter_grid"][0].__setitem__("k", 99))
    add("row_count", lambda x: x["regression"]["row_counts"].__setitem__("atlas", 49))
    # Repaired hashes ensure semantic checks, not only digest checks, reject.
    add("repaired_fixed", lambda x: x["regression"]["atlas_rows"][7]["fixed_counts_1_to_order"].__setitem__(0, 123), True)
    add("repaired_position", lambda x: x["regression"]["position_rows"][4].__setitem__("position_period", 1), True)
    add("repaired_spectral", lambda x: x["regression"]["spectral_rows"][4].__setitem__("zeta_degree", 0), True)
    add("repaired_rep_period", lambda x: x["regression"]["representative_cycles"][0].__setitem__("period", 9), True)
    # Frozen theorem, route, scope and provenance.
    add("frozen_map", lambda x: x["frozen_object"].__setitem__("map", "rho(i)=i"))
    add("frozen_clock", lambda x: x["frozen_object"].__setitem__("clock", "random"))
    add("theorem_fixed", lambda x: x["theorem"].__setitem__("fixed_points", "wrong formula"))
    add("theorem_zeta", lambda x: x["theorem"].__setitem__("zeta", "target product"))
    add("identity_formula", lambda x: x["exact_identities"][2].__setitem__("formula", "Fix=0"))
    add("route_tuple", lambda x: x["route_a"]["tuple"].__setitem__(1, "A1_FAIL"))
    add("route_overall", lambda x: x["route_a"].__setitem__("overall", "ROUTE_A_ACCEPTED"))
    add("route_b", lambda x: x["route_a"].__setitem__("route_b_invocation_allowed", True))
    add("scope_flag", lambda x: x["scope_flags"].__setitem__("claims_euler_factors", True))
    add("citation_title", lambda x: x["citations"][0].__setitem__("title", "fabricated"))
    add("citation_doi_repaired", lambda x: x["citations"][0].__setitem__("doi", "10.0000/fake"), True)
    add("citation_url", lambda x: x["citations"][1].__setitem__("url", "https://example.invalid"))
    add("nonclaim", lambda x: x["nonclaims"].__setitem__(0, "arithmetic claim"))
    add("unknown_nested", lambda x: x["theorem"].__setitem__("unknown", True))
    add("unknown_top", lambda x: x.__setitem__("unknown", True))
    add("stale_hash", lambda x: x.__setitem__("payload_sha256", "0" * 64))
    add("schema", lambda x: x.__setitem__("schema", "wrong"))
    add("candidate_id", lambda x: x.__setitem__("candidate_id", "HCS-C000"))
    add("date", lambda x: x.__setitem__("evaluation_date", "2026-08-31"))
    add("evaluator_hash", lambda x: x["evaluator"].__setitem__("sha256", "0" * 64))
    add("missing_atlas", lambda x: x["regression"]["atlas_rows"].pop())
    add("atlas_ordering", lambda x: x["regression"]["atlas_rows"].reverse(), True)

    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    caught: list[str] = []
    with tempfile.TemporaryDirectory(prefix="c239-shuffle-mutations-") as td:
        for name, item in mutations:
            path = Path(td) / f"{name}.json"
            path.write_text(json.dumps(item, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
            proc = subprocess.run([sys.executable, "-B", str(CHECKER), "--input", str(path)], env=env, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if proc.returncode != 0:
                caught.append(name)
    assert len(caught) == len(mutations), f"uncaught mutations: {set(name for name, _ in mutations) - set(caught)}"
    print(f"C239 hostile mutations: PASS {len(caught)}/{len(mutations)}")
    print("caught=" + ",".join(caught))


if __name__ == "__main__":
    main()
