#!/usr/bin/env python3
import copy
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("checker", ROOT / "code" / "c128_metaplectic_checker.py")
checker = importlib.util.module_from_spec(spec); spec.loader.exec_module(checker)
base = json.loads((ROOT / "results" / "c128_metaplectic_evidence.json").read_text())


def trial(path, value, repair=True):
    data = copy.deepcopy(base); node = data
    for key in path[:-1]: node = node[key]
    node[path[-1]] = value
    if repair:
        data.pop("payload_sha256", None)
        payload = json.dumps(data, sort_keys=True, separators=(",", ":")).encode()
        data["payload_sha256"] = hashlib.sha256(payload).hexdigest()
    return data


mutations = [
    (["schema"], "bad", True), (["quantum_level"], 5, True),
    (["candidate_id"], "HCS-C999", True),
    (["reversor_matrix", 0, 0], 1, True),
    (["classical_matrix", 0, 0], 2, True),
    (["phase_conventions", "omega"], "exp(2*pi*i/5)", True),
    (["phase_conventions", "inverse_of_2_mod_7"], 3, True),
    (["phase_conventions", "fourier"], "wrong sign", True),
    (["phase_conventions", "chirp"], "wrong chirp", True),
    (["phase_conventions", "weyl"], "missing half phase", True),
    (["phase_conventions", "antiunitary"], "K", True),
    (["quantum_traces_n1_to_n8", 0], "1", True),
    (["classical_quantum_clock", 2, "fixed_points"], 15, True),
    (["classical_quantum_clock", 5, "primitive_cycles"], 49, True),
    (["classical_quantum_clock", 7, "quantum_trace_N7"], "1", True),
    (["exact_certificate", "egorov_cases"], 48, True),
    (["exact_certificate", "time_reversal_entries"], 48, True),
    (["exact_certificate", "all_exact_checks_pass"], False, True),
    (["characteristic_polynomial"], "t^7-1", True),
    (["fredholm_determinant"], "1-z^7", True),
    (["spectrum"], "all seventh roots of unity", True),
    (["action_sum", "phase"], "zero", True),
    (["action_sum", "stationary_equation"], "x_j=0", True),
    (["even_modulus_control", "test_modulus"], 6, True),
    (["even_modulus_control", "inverse_of_2_exists"], True, True),
    (["even_modulus_control", "same_half_phase_formula_directly_defined"], True, True),
    (["progress", "natural_quantization_gate"], "FAIL", True),
    (["progress", "even_modulus_same_convention_obstruction"], "FAIL", True),
    (["route_a", "tuple",], ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], True),
    (["route_a", "route_b_invocation_allowed"], True, True),
    (["scope_flags", "claims_hilbert_polya"], True, True),
    (["payload_sha256"], "0" * 64, False),
]
caught = 0
for path, value, repair in mutations:
    try: checker.validate(trial(path, value, repair))
    except (AssertionError, KeyError, ValueError): caught += 1
assert caught == len(mutations)
print(f"C128 mutation suite: PASS ({caught}/{len(mutations)} mutations rejected)")
