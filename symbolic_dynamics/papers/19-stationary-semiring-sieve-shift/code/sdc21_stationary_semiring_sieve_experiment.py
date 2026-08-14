#!/usr/bin/env python3
"""Generate all primary SD-C21 exact artifacts and the no-oracle certificate."""

from __future__ import annotations

import ast
import json
from pathlib import Path

from sdc21_stationary_semiring_sieve_core import graph_edges, recurrent_nodes, run


ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
CORE = ROOT / "code" / "sdc21_stationary_semiring_sieve_core.py"


def function_calls(tree: ast.AST, function_name: str) -> list[str]:
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == function_name:
            calls: list[str] = []
            for child in ast.walk(node):
                if isinstance(child, ast.Call):
                    if isinstance(child.func, ast.Name):
                        calls.append(child.func.id)
                    elif isinstance(child.func, ast.Attribute):
                        calls.append(child.func.attr)
            return sorted(calls)
    raise AssertionError(f"missing function {function_name}")


def no_oracle_certificate() -> dict[str, object]:
    source = CORE.read_text(encoding="utf-8")
    tree = ast.parse(source)
    forbidden_identifiers = ("tensor_divides", "exists_factor", "factor_exists", "has_factor")
    identifier_counts = {
        name: sum(
            isinstance(node, (ast.Name, ast.FunctionDef, ast.AsyncFunctionDef))
            and getattr(node, "id", getattr(node, "name", None)) == name
            for node in ast.walk(tree)
        )
        for name in forbidden_identifiers
    }
    audited_functions = ("trial_accepts", "graph_edges", "shuffled_presentation")
    any_calls = {
        name: function_calls(tree, name).count("any")
        for name in audited_functions
    }

    nodes, edges, accepted = graph_edges(64, cemetery_depth=4, s_integer=2)
    q_nodes = sorted(node for node in nodes if node.startswith("Q:"))
    q_edges = [edge for edge in edges if edge.source.startswith("Q:")]
    q_successor_edges = [
        edge for edge in q_edges
        if edge.target.startswith("Q:")
    ]
    q_reject_edges = [
        edge for edge in q_edges
        if edge.target.startswith("R:")
    ]
    q_overshoot_edges = [
        edge for edge in q_edges
        if edge.target.startswith("T:")
    ]
    recurrent = set(recurrent_nodes(nodes, edges))
    expected_recurrent = {f"A:{prime}" for prime in accepted}
    checks = {
        "forbidden_identifiers_absent": not any(identifier_counts.values()),
        "audited_functions_have_no_any_factor_macro": not any(any_calls.values()),
        "q_state_literal_present": 'f"Q:{n}:{d}:{q}"' in source,
        "q_states_materialized": bool(q_nodes),
        "q_successor_edges_materialized": bool(q_successor_edges),
        "q_reject_edges_materialized": bool(q_reject_edges),
        "q_overshoot_edges_materialized": bool(q_overshoot_edges),
        "recurrent_core_exact_accept_loops": recurrent == expected_recurrent,
    }
    payload: dict[str, object] = {
        "candidate_id": "SD-C21",
        "scientific_source_audited": CORE.relative_to(ROOT).as_posix(),
        "forbidden_identifier_counts": identifier_counts,
        "audited_function_any_call_counts": any_calls,
        "graph_limit": 64,
        "q_node_count": len(q_nodes),
        "q_edge_count": len(q_edges),
        "q_successor_edge_count": len(q_successor_edges),
        "q_reject_edge_count": len(q_reject_edges),
        "q_overshoot_edge_count": len(q_overshoot_edges),
        "accepted_count": len(accepted),
        "recurrent_count": len(recurrent),
        "checks": checks,
        "no_oracle_pass": all(checks.values()),
        "claim_boundary": (
            "The certificate proves that the implementation materializes local quotient-search "
            "states and does not call an existential factor helper. It does not make the "
            "verifier dynamically non-tautological."
        ),
    }
    if not payload["no_oracle_pass"]:
        raise AssertionError(json.dumps(payload, sort_keys=True))
    return payload


def main() -> int:
    RESULTS.mkdir(parents=True, exist_ok=True)
    run(RESULTS)
    certificate = no_oracle_certificate()
    (RESULTS / "source_oracle_certificate.json").write_text(
        json.dumps(certificate, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(certificate, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
