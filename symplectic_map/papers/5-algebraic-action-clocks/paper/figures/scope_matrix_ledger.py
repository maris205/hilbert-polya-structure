"""Explicit provenance ledger for every categorical cell in Figure 2.

The figure has two evidence classes and never conflates them:

* ``FROZEN_JSON_DERIVED`` means that the displayed status is obtained from
  exact predicates on the source-locked official result records.
* ``THEOREM_DEFINED`` means that the status is a scope consequence of the
  written theorem/nonclaim ledger.  It is not presented as an empirical or
  raw-result classification.

Every row is fail-closed: if a predicate used by the ledger changes, figure
generation stops rather than silently retaining an old color code.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
from pathlib import Path
from typing import Any


CERTIFIED = "CERTIFIED"
EDGE = "EDGE"
STOP_OUT = "STOP/OUT"

FROZEN_JSON_DERIVED = "FROZEN_JSON_DERIVED"
THEOREM_DEFINED = "THEOREM_DEFINED"

STATUS_CODES = {STOP_OUT: 0, EDGE: 1, CERTIFIED: 2}
ALLOWED_PROVENANCE = {FROZEN_JSON_DERIVED, THEOREM_DEFINED}
COLUMNS = ("formula applies", "algebraicity retained", "target-log conclusion")


@dataclass(frozen=True)
class ScopeCell:
    status: str
    provenance_class: str
    evidence: tuple[str, ...]


@dataclass(frozen=True)
class ScopeRow:
    label: str
    record_key: str
    cells: tuple[ScopeCell, ScopeCell, ScopeCell]


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(f"Figure 2 scope-ledger predicate failed: {message}")


def _cell(status: str, provenance_class: str, *evidence: str) -> ScopeCell:
    _require(status in STATUS_CODES, f"unknown status {status!r}")
    _require(
        provenance_class in ALLOWED_PROVENANCE,
        f"unknown provenance class {provenance_class!r}",
    )
    _require(bool(evidence) and all(evidence), "every cell needs named evidence")
    return ScopeCell(status, provenance_class, tuple(evidence))


def _positive_gauge_row(label: str, key: str, record: dict[str, Any]) -> ScopeRow:
    _require(record.get("pass") is True, f"{key}.pass must be true")
    _require(
        record.get("direct_shift") == record.get("predicted_shift"),
        f"{key} exact shift changed",
    )
    _require(
        record.get("values_declared_algebraic") is True,
        f"{key} algebraic-value declaration changed",
    )
    return ScopeRow(
        label,
        key,
        (
            _cell(
                CERTIFIED,
                FROZEN_JSON_DERIVED,
                f"results/control_audit.json:{key}.pass",
                f"results/control_audit.json:{key}.direct_shift=predicted_shift",
            ),
            _cell(
                CERTIFIED,
                FROZEN_JSON_DERIVED,
                f"results/control_audit.json:{key}.values_declared_algebraic=true",
            ),
            _cell(
                CERTIFIED,
                THEOREM_DEFINED,
                f"results/control_audit.json:{key}.values_declared_algebraic=true",
                "manuscript:Corollary 3.2 (algebraic logarithmic targets)",
            ),
        ),
    )


def derive_scope_rows(data: dict[str, Any]) -> tuple[ScopeRow, ...]:
    """Derive all 27 cells from named predicates and theorem scope rules."""

    control = data["control"]
    proof = data["proof"]
    source_lock = data["source_lock"]

    dependencies = proof.get("dependency_checks", {})
    _require(
        dependencies.get("general_endpoint_mismatch") is True,
        "general endpoint dependency must pass",
    )
    _require(
        dependencies.get("hl_zero_one_edge_cases") is True,
        "Hermite--Lindemann edge dependency must pass",
    )
    _require(
        dependencies.get("log_abs_nonclaim") is True,
        "log-absolute-action nonclaim dependency must pass",
    )
    _require(
        any("log(abs(A_G))" in item for item in source_lock.get("nonclaims", [])),
        "source lock must retain log(abs(A_G)) as a nonclaim",
    )

    pole = control["pole_negative_control"]
    _require(pole.get("pass") is False, "pole negative control must stop")
    _require(
        pole.get("dependencies", {}).get("every_potential_value_pole_free") is False,
        "pole dependency must be false",
    )

    undefined = control["stepwise_definedness_negative_control"]
    _require(undefined.get("pass") is False, "undefined-step control must stop")
    _require(
        any(step.get("pass") is False for step in undefined.get("step_records", [])),
        "undefined-step record must contain a failed step",
    )

    multivalued = control["multivalued_gauge_nonclaim"]
    _require(
        multivalued.get("single_valued_qbar_rational") is False,
        "multivalued control must remain outside the admitted gauge class",
    )
    _require(
        multivalued.get("classification")
        == "OUTSIDE_SCOPE_STOP_ABSOLUTE_ACTION_CERTIFICATE",
        "multivalued classification changed",
    )

    beta_zero = control["beta_zero_scope"]
    _require(beta_zero.get("action_is_algebraic") is True, "beta=0 action class changed")
    _require(beta_zero.get("target_excluded") is True, "beta=0 target result changed")
    _require(
        beta_zero.get("classification") == "NO_COMPLEX_LOGARITHM",
        "beta=0 logarithm-domain classification changed",
    )

    beta_one = control["hermite_lindemann_beta_one_exception"]
    _require(beta_one.get("action_is_algebraic") is True, "beta=1 action class changed")
    _require(beta_one.get("action_is_zero") is True, "beta=1 zero exception changed")
    _require(beta_one.get("target_excluded") is False, "beta=1 exception was lost")
    _require(
        beta_one.get("classification")
        == "TRIVIAL_ALGEBRAIC_EXCEPTION_A_ZERO_BETA_ONE",
        "beta=1 classification changed",
    )

    log_abs = control["log_abs_nonclaim"]
    _require(log_abs.get("pass") is True, "log|A| nonclaim audit must pass")
    _require(
        log_abs.get("classification") == "OUTSIDE_SOURCE_LOCK_NONCLAIM",
        "log|A| must remain an outside-scope nonclaim",
    )
    _require(
        log_abs.get("numeric_postprocessing_executed") is False,
        "log|A| numeric post-processing must remain absent",
    )

    rows = (
        _positive_gauge_row(
            "compatible endpoint", "compatible_gauge", control["compatible_gauge"]
        ),
        _positive_gauge_row(
            "endpoint mismatch",
            "algebraic_endpoint_mismatch",
            control["algebraic_endpoint_mismatch"],
        ),
        _positive_gauge_row(
            "uniform algebraic $C$",
            "uniform_algebraic_constant",
            control["uniform_algebraic_constant"],
        ),
        ScopeRow(
            "potential pole",
            "pole_negative_control",
            (
                _cell(
                    STOP_OUT,
                    FROZEN_JSON_DERIVED,
                    "results/control_audit.json:pole_negative_control.pass=false",
                ),
                _cell(
                    STOP_OUT,
                    THEOREM_DEFINED,
                    "results/control_audit.json:pole_negative_control.every_potential_value_pole_free=false",
                    "manuscript:Theorem 3.1 regularity hypothesis",
                ),
                _cell(
                    STOP_OUT,
                    THEOREM_DEFINED,
                    "manuscript:Theorem 3.1 regularity hypothesis fails",
                    "manuscript:Corollary 3.2 therefore inapplicable",
                ),
            ),
        ),
        ScopeRow(
            "undefined step",
            "stepwise_definedness_negative_control",
            (
                _cell(
                    STOP_OUT,
                    FROZEN_JSON_DERIVED,
                    "results/control_audit.json:stepwise_definedness_negative_control.pass=false",
                ),
                _cell(
                    STOP_OUT,
                    THEOREM_DEFINED,
                    "results/control_audit.json:stepwise_definedness_negative_control contains failed step",
                    "manuscript:Theorem 3.1 stepwise-definedness hypothesis",
                ),
                _cell(
                    STOP_OUT,
                    THEOREM_DEFINED,
                    "manuscript:Theorem 3.1 hypotheses fail",
                    "manuscript:Corollary 3.2 therefore inapplicable",
                ),
            ),
        ),
        ScopeRow(
            "multivalued gauge",
            "multivalued_gauge_nonclaim",
            (
                _cell(
                    STOP_OUT,
                    FROZEN_JSON_DERIVED,
                    "results/control_audit.json:multivalued_gauge_nonclaim.single_valued_qbar_rational=false",
                ),
                _cell(
                    STOP_OUT,
                    THEOREM_DEFINED,
                    "manuscript:single-valued rational gauge hypothesis fails",
                ),
                _cell(
                    STOP_OUT,
                    THEOREM_DEFINED,
                    "manuscript:untracked monodromy lies outside the certificate",
                ),
            ),
        ),
        ScopeRow(
            "$\\beta=0$",
            "beta_zero_scope",
            (
                _cell(
                    EDGE,
                    THEOREM_DEFINED,
                    "manuscript:target-domain edge, not a gauge formula row",
                ),
                _cell(
                    CERTIFIED,
                    FROZEN_JSON_DERIVED,
                    "results/control_audit.json:beta_zero_scope.action_is_algebraic=true",
                ),
                _cell(
                    CERTIFIED,
                    FROZEN_JSON_DERIVED,
                    "results/control_audit.json:beta_zero_scope.classification=NO_COMPLEX_LOGARITHM",
                ),
            ),
        ),
        ScopeRow(
            "$\\beta=1$, $\\mathcal{A}=0$",
            "hermite_lindemann_beta_one_exception",
            (
                _cell(
                    EDGE,
                    THEOREM_DEFINED,
                    "manuscript:target-domain edge, not a gauge formula row",
                ),
                _cell(
                    CERTIFIED,
                    FROZEN_JSON_DERIVED,
                    "results/control_audit.json:hermite_lindemann_beta_one_exception.action_is_algebraic=true",
                ),
                _cell(
                    EDGE,
                    FROZEN_JSON_DERIVED,
                    "results/control_audit.json:hermite_lindemann_beta_one_exception.target_excluded=false",
                    "results/control_audit.json:hermite_lindemann_beta_one_exception.action_is_zero=true",
                ),
            ),
        ),
        ScopeRow(
            "$\\log|\\mathcal{A}|$",
            "log_abs_nonclaim",
            (
                _cell(
                    EDGE,
                    THEOREM_DEFINED,
                    "manuscript:post-processed observable, not a gauge formula row",
                ),
                _cell(
                    STOP_OUT,
                    THEOREM_DEFINED,
                    "manuscript:Remark 3.4 makes no algebraicity claim for log|A|",
                    "experiments/source_lock.json:log(abs(A_G)) is an explicit nonclaim",
                ),
                _cell(
                    STOP_OUT,
                    FROZEN_JSON_DERIVED,
                    "results/control_audit.json:log_abs_nonclaim.classification=OUTSIDE_SOURCE_LOCK_NONCLAIM",
                ),
            ),
        ),
    )

    _require(len(rows) == 9, "scope ledger must contain exactly nine rows")
    _require(
        sum(len(row.cells) for row in rows) == 27,
        "scope ledger must contain exactly 27 cells",
    )
    return rows


def write_scope_provenance(rows: tuple[ScopeRow, ...], path: Path) -> None:
    payload = {
        "schema": "ALGEBRAIC_ACTION_FIG2_SCOPE_LEDGER_V1",
        "columns": list(COLUMNS),
        "provenance_classes": {
            FROZEN_JSON_DERIVED: "status derived from named predicates in the source-locked official JSON records",
            THEOREM_DEFINED: "scope status defined by a named theorem hypothesis, consequence, edge case, or explicit nonclaim; not a raw-result claim",
        },
        "rows": [asdict(row) for row in rows],
        "cell_count": sum(len(row.cells) for row in rows),
    }
    path.write_text(
        json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=True) + "\n",
        encoding="utf-8",
    )
