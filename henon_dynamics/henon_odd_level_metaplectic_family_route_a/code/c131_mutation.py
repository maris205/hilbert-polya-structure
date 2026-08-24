#!/usr/bin/env python3
"""Repaired-hash semantic and schema mutations for C131."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("c131_checker", ROOT / "code/c131_odd_metaplectic_checker.py")
checker = importlib.util.module_from_spec(spec)
assert spec.loader
spec.loader.exec_module(checker)
base = json.loads((ROOT / "results/c131_odd_metaplectic_evidence.json").read_text())

renamed_checks = copy.deepcopy(base["checks"])
renamed_checks["uniform_antiunitary_pass_renamed"] = renamed_checks.pop("uniform_antiunitary_pass")
renamed_scope_flags = copy.deepcopy(base["scope_flags"])
renamed_scope_flags["claims_hilbert_polya_renamed"] = renamed_scope_flags.pop("claims_hilbert_polya")


def trial(path, value, repair=True):
    data = copy.deepcopy(base)
    node = data
    for key in path[:-1]:
        node = node[key]
    node[path[-1]] = value
    if repair:
        data.pop("payload_sha256", None)
        payload = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
        data["payload_sha256"] = hashlib.sha256(payload).hexdigest()
    return data


mutations = [
    (["schema"], "bad", True),
    (["candidate_id"], "HCS-C999", True),
    (["family", "levels"], "odd primes", True),
    (["phase_conventions", "half"], "h=1/2 over R", True),
    (["phase_conventions", "fourier"], "wrong sign", True),
    (["phase_conventions", "chirp"], "wrong chirp", True),
    (["phase_conventions", "weyl"], "no half phase", True),
    (["all_odd_level_theorem", "egorov"], "wrong matrix", True),
    (["all_odd_level_theorem", "antiunitary_reversal"], "false", True),
    (["matrix_power_receipts", 3, "max_norm_A_n_minus_I"], 999, True),
    (["certified_level_receipts", 0, "inverse_of_2"], 1, True),
    (["certified_level_receipts", 2, "egorov_cases"], 48, True),
    (["certified_level_receipts", 4, "egorov_case_sha256"], "0" * 64, True),
    (["certified_level_receipts", 5, "antiunitary_case_sha256"], "0" * 64, True),
    (["certified_level_receipts", 6, "certified_no_action_alias_window"], 2, True),
    (["certified_level_receipts", 7, "action_residues", 0, "A_n_minus_I_mod_N"], [0, 0, 0, 0], True),
    (["total_exact_egorov_cases"], 25312, True),
    (["unbounded_window_witnesses", 4, "window"], 4, True),
    (["even_modulus_control", "inverse_of_2_exists"], True, True),
    (["even_modulus_control", "scope"], "all even quantizations impossible", True),
    (["nonclaims", "semiclassical_trace_match"], True, True),
    (["checks", "uniform_antiunitary_pass"], False, True),
    (["route_a", "tuple"], ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_ROUTE_B_READY"], True),
    (["route_a", "route_b_invocation_allowed"], True, True),
    (["scope_flags", "claims_hilbert_polya"], True, True),
    (["unexpected_top_level_key"], False, True),
    (["checks"], renamed_checks, True),
    (["scope_flags"], renamed_scope_flags, True),
    (["certified_level_receipts", 0, "unexpected_receipt_key"], False, True),
    (["payload_sha256"], "0" * 64, False),
]
caught = 0
for path, value, repair in mutations:
    try:
        checker.validate(trial(path, value, repair))
    except (AssertionError, KeyError, ValueError):
        caught += 1
assert caught == len(mutations)
repaired = sum(1 for _path, _value, repair in mutations if repair)
stale = len(mutations) - repaired
assert (repaired, stale, len(mutations)) == (29, 1, 30)
print(
    f"C131 mutation suite: PASS ({caught}/{len(mutations)} mutations rejected; "
    f"repaired_hash={repaired}; stale_hash={stale})"
)
