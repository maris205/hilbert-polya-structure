import pytest

from action_audit.scope import evaluation_scope_audit, observable_scope_classification


def _valid_step():
    return {
        "map_defined_at_input": True,
        "potential_defined_at_input": True,
        "current_gauge_defined_at_input": True,
        "next_gauge_defined_at_output": True,
        "transition_defined": True,
    }


def test_evaluation_scope_accepts_fully_defined_steps():
    record = evaluation_scope_audit([_valid_step(), _valid_step()])
    assert record["pass"]
    assert record["classification"] == "ALL_EVALUATION_POINTS_DEFINED_AND_POLE_FREE"


@pytest.mark.parametrize(
    "key",
    [
        "map_defined_at_input",
        "potential_defined_at_input",
        "current_gauge_defined_at_input",
        "next_gauge_defined_at_output",
        "transition_defined",
    ],
)
def test_each_stepwise_dependency_fails_closed(key):
    step = _valid_step()
    step[key] = False
    record = evaluation_scope_audit([step])
    assert not record["pass"]
    assert key.upper() in record["classification"]


def test_theta_gate_applies_only_when_theta_is_evaluated():
    ignored = evaluation_scope_audit(
        [_valid_step()],
        theta_evaluated=False,
        theta_defined_at_every_required_point=False,
    )
    enforced = evaluation_scope_audit(
        [_valid_step()],
        theta_evaluated=True,
        theta_defined_at_every_required_point=False,
    )
    assert ignored["pass"]
    assert not enforced["pass"]


def test_missing_step_key_is_rejected():
    with pytest.raises(ValueError):
        evaluation_scope_audit([{"map_defined_at_input": True}])


@pytest.mark.parametrize(
    "observable",
    ["ACTION", "REAL_PART_ACTION", "IMAGINARY_PART_ACTION", "ABS_ACTION"],
)
def test_admitted_algebraic_observables(observable):
    record = observable_scope_classification(observable)
    assert record["pass"]
    assert record["classification"] == "ALGEBRAIC_TRANSFORM_CERTIFICATE_APPLIES"


@pytest.mark.parametrize(
    "observable",
    ["LOG_ABS_ACTION", "ARG_ACTION", "MULTIPLIER_LOG", "RETURN_TIME"],
)
def test_nonclaim_observables_are_classified_without_execution(observable):
    record = observable_scope_classification(observable)
    assert record["pass"]
    assert record["classification"] == "OUTSIDE_SOURCE_LOCK_NONCLAIM"
    assert not record["numeric_postprocessing_executed"]


def test_unknown_observable_fails_closed():
    record = observable_scope_classification("FITTED_CLOCK")
    assert not record["pass"]
