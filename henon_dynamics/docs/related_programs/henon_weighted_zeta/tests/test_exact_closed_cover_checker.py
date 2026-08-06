"""Regression checks for the independent R053 reconstruction."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

from scripts.check_exact_closed_cover import closed_indices, make_edges


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CHECK_RESULT = (
    PROJECT_ROOT
    / "results"
    / "exact_closed_cover_independent_check_r053.json"
)


def test_independent_closed_indexing_keeps_both_shared_edge_neighbors():
    edges = make_edges(Fraction(1), 2, Fraction(0))
    assert edges == (Fraction(-1), Fraction(0), Fraction(1))
    assert closed_indices(edges, Fraction(0), Fraction(0)) == (0, 1)


def test_independent_r053_reconstruction_matches_all_producer_records():
    payload = json.loads(CHECK_RESULT.read_text(encoding="utf-8"))
    assert not payload["checker_imports_producer_geometry"]
    assert payload["all_configurations_match"]
    assert len(payload["records"]) == 4
    assert all(record["all_recomputed_fields_match"] for record in payload["records"])
