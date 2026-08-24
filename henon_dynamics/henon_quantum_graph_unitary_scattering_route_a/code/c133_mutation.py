#!/usr/bin/env python3
import copy
import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("c133_checker", ROOT / "code" / "c133_quantum_graph_checker.py")
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)
base = json.loads((ROOT / "results" / "c133_quantum_graph_evidence.json").read_text())


def mutate(path, value, repair=True):
    obj = copy.deepcopy(base)
    node = obj
    for key in path[:-1]:
        node = node[key]
    node[path[-1]] = value
    if repair:
        obj.pop("payload_sha256", None)
        obj["payload_sha256"] = hashlib.sha256(
            json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest()
    return obj


cases = [
    (["schema"], "bad", True),
    (["candidate_id"], "HCS-C999", True),
    (["date_utc"], "2026-08-23", True),
    (["scope"], "expanded", True),
    (["graph", "vertices"], ["L", "X"], True),
    (["graph", "undirected_edges"], ["e1", "e2", "e4"], True),
    (["graph", "edge_lengths"], [1, 2, 4], True),
    (["graph", "directed_bond_order", 0], "bad", True),
    (["graph", "vertex_condition"], "degree-three fitted", True),
    (["graph", "clock"], "one topological step", True),
    (["kirchhoff_vertex_scattering", 0, 0], "-1/2", True),
    (["global_bond_scattering", 0, 3], "1", True),
    (["bond_reversal", 0, 3], "0", True),
    (["exact_operator", "unitary_for_real_k"], False, True),
    (["exact_operator", "definition"], "U(k)=S", True),
    (["exact_operator", "unitarity_entries_checked"], 35, True),
    (["exact_operator", "antiunitary"], "K", True),
    (["exact_operator", "time_reversal_identity"], "Theta U Theta^-1=U", True),
    (["exact_operator", "time_reversal_symbolic_defect_zero"], False, True),
    (["secular_determinant", "convention"], "det(I-zP*S*P)", True),
    (["secular_determinant", "multivariate_expanded"], "1", True),
    (["secular_determinant", "physical_z1_factorized"], "1", True),
    (["secular_determinant", "length_specialization_factorized"], "1-t", True),
    (["secular_determinant", "length_specialization_coefficients", "12"], "0", True),
    (["secular_determinant", "determinant_degree_in_z"], 5, True),
    (["orbit_trace_certificate", "trace_polynomials_n1_to_n6", "2"], {}, True),
    (["orbit_trace_certificate", "rooted_closed_walks_n1_to_n8", "8"], 1, True),
    (["orbit_trace_certificate", "primitive_directed_cycles_n1_to_n8", "6"], 1, True),
    (["orbit_trace_certificate", "period_two_amplitude_sum_by_metric_length", "2"], "0", True),
    (["orbit_trace_certificate", "all_period_identity"], "det(I-zM)=1", True),
    (["orbit_trace_certificate", "primitive_product"], "unsigned product", True),
    (["controls", "wrong_vertex_normalization", "unitary"], True, True),
    (["controls", "wrong_vertex_normalization", "nonzero_defect_entries"], 0, True),
    (["controls", "direction_asymmetric_length", "time_reversal_preserved"], True, True),
    (["controls", "direction_asymmetric_length", "scope"], "same metric graph", True),
    (["controls", "direction_asymmetric_length", "theta_JK_reversal_defect_nonzero_entries"], 1, True),
    (["controls", "direction_asymmetric_length", "theta_JK_reversal_defect_nonzero_entries"], 0, True),
    (["exact_certificate", "all_exact_checks_pass"], False, True),
    (["exact_certificate", "unexpected"], True, True),
    (["progress", "closed_gate"], "target match", True),
    (["progress", "new_route_a_coordinate"], "A4_FORMAL_HINT", True),
    (["progress", "over_prior_round"], "Route-B ready", True),
    (["route_a", "tuple"], ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], True),
    (["route_a", "overall"], "ROUTE_A_PASS", True),
    (["route_a", "route_b_invocation_allowed"], True, True),
    (["scope_flags", "claims_hilbert_polya"], True, True),
    (["scope_flags", "unexpected"], False, True),
    (["nonclaims", 0], "prime correspondence proved", True),
    (["payload_sha256"], "0" * 64, False),
]

caught = 0
for path, value, repair in cases:
    try:
        checker.validate(mutate(path, value, repair))
    except (AssertionError, KeyError, ValueError, TypeError):
        caught += 1
assert caught == len(cases)
print(f"C133 mutation suite: PASS ({caught}/{len(cases)} mutations rejected)")
