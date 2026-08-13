"""Paper-stage assertions for the Figure 2 categorical provenance ledger."""

from __future__ import annotations

from copy import deepcopy

import pytest

from frozen_data import load_frozen_package
from scope_matrix_ledger import (
    ALLOWED_PROVENANCE,
    CERTIFIED,
    EDGE,
    STOP_OUT,
    derive_scope_rows,
)


EXPECTED_STATUSES = (
    (CERTIFIED, CERTIFIED, CERTIFIED),
    (CERTIFIED, CERTIFIED, CERTIFIED),
    (CERTIFIED, CERTIFIED, CERTIFIED),
    (STOP_OUT, STOP_OUT, STOP_OUT),
    (STOP_OUT, STOP_OUT, STOP_OUT),
    (STOP_OUT, STOP_OUT, STOP_OUT),
    (EDGE, CERTIFIED, CERTIFIED),
    (EDGE, CERTIFIED, EDGE),
    (EDGE, STOP_OUT, STOP_OUT),
)


def test_all_27_scope_cells_have_exact_status_and_named_provenance():
    rows = derive_scope_rows(load_frozen_package())
    assert tuple(tuple(cell.status for cell in row.cells) for row in rows) == EXPECTED_STATUSES
    cells = [cell for row in rows for cell in row.cells]
    assert len(cells) == 27
    assert all(cell.provenance_class in ALLOWED_PROVENANCE for cell in cells)
    assert all(cell.evidence and all(cell.evidence) for cell in cells)


def test_log_abs_row_never_claims_algebraicity_or_target_exclusion():
    rows = derive_scope_rows(load_frozen_package())
    row = next(row for row in rows if row.record_key == "log_abs_nonclaim")
    assert tuple(cell.status for cell in row.cells) == (EDGE, STOP_OUT, STOP_OUT)


def test_log_abs_classification_mutation_fails_closed():
    data = deepcopy(load_frozen_package())
    data["control"]["log_abs_nonclaim"]["classification"] = "CERTIFIED"
    with pytest.raises(RuntimeError, match=r"log\|A\| must remain"):
        derive_scope_rows(data)


def test_algebraic_gauge_declaration_mutation_fails_closed():
    data = deepcopy(load_frozen_package())
    data["control"]["compatible_gauge"]["values_declared_algebraic"] = False
    with pytest.raises(RuntimeError, match="algebraic-value declaration changed"):
        derive_scope_rows(data)


def test_beta_zero_edge_mutation_fails_closed():
    data = deepcopy(load_frozen_package())
    data["control"]["beta_zero_scope"]["target_excluded"] = False
    with pytest.raises(RuntimeError, match="beta=0 target result changed"):
        derive_scope_rows(data)
