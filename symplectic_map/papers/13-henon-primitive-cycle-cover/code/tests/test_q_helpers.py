from copy import deepcopy
from fractions import Fraction

import pytest

from candidate_v1.bootstrap.canonical import canonical_bytes, strict_canonical_load, strict_load_bytes
from candidate_v1.track_q import engine as q


F = Fraction
ZERO = {}
ONE = {(0, 0, 0, 0): F(1)}
A = {(1, 0, 0, 0): F(1)}
C = {(0, 1, 0, 0): F(1)}
Z0 = {(0, 0, 1, 0): F(1)}
Z1 = {(0, 0, 0, 1): F(1)}


def _inputs(paper_root):
    definitions = strict_load_bytes((paper_root / "code/candidate_v1/shared/definitions.json").read_bytes())
    fixture = strict_load_bytes((paper_root / "code/candidate_v1/track_q/private_fixture.json").read_bytes())
    return definitions, fixture


def _pair_wire(value):
    if type(value) is not tuple or len(value) != 2:
        raise TypeError("endpoint must be an exact pair")
    left, right = value
    if type(left) not in (tuple, dict) or type(right) not in (tuple, dict):
        raise TypeError("endpoint pair members")
    payload = canonical_bytes({"left_type": type(left).__name__, "right_type": type(right).__name__})
    return strict_canonical_load(payload)


def test_q_helper_endpoint_shapes_without_top_level_science(paper_root):
    definitions, fixture = _inputs(paper_root)
    q._q_validate_inputs(definitions, fixture)
    assert q._q_rat({"denominator": 2, "numerator": -1}) == F(-1, 2)
    assert q._q_rat_wire(F(-2, 4)) == {"denominator": 2, "numerator": -1}
    assert q._q_exact_nonnegative_power(F(-1, 2), 3) == F(-1, 8)
    assert q._q_exact_nonnegative_power(2, 0) == 1
    with pytest.raises(TypeError):
        q._q_exact_nonnegative_power(2, -1)
    assert q._q_poly_clean({(0, 0, 0, 0): 0}) == ZERO
    assert q._q_poly_add(A, C) == {**A, **C}
    assert q._q_poly_scale(2, A) == {(1, 0, 0, 0): F(2)}
    assert q._q_poly_sub(A, A) == ZERO
    assert q._q_poly_mul(A, C) == {(1, 1, 0, 0): F(1)}
    assert q._q_poly_pow(A, 0) == ONE
    assert q._q_poly_lead_all(Z0)[0] == (0, 0, 1, 0)
    sparse_pair = q._q_poly_exact_div(A, C)
    assert type(sparse_pair) is tuple and len(sparse_pair) == 2 and sparse_pair == (ZERO, A)
    assert q._q_dense_trim((1, 0, 0)) == (F(1),)
    assert q._q_dense_add((1, 1), (-1, 1)) == (F(0), F(2))
    assert q._q_dense_mul((), (1,)) == ()
    assert q._q_dense_compose((1, 1), (0, 1)) == (F(1), F(1))
    dense_pair = q._q_dense_divmod((1,), (0, 1))
    assert dense_pair == ((), (F(1),))
    assert q._q_dense_eval((1, 2), F(3)) == 7
    assert q._q_cycle_groups(q._q_poly_add(Z0, A))[(1, 0)] == {(0, 0): F(1)}
    assert q._q_cycle_lead(q._q_poly_add(Z0, A))[0] == (1, 0)
    assert q._q_standard_exponents_from_leads(((2, 0), (0, 2))) == ((0, 0), (0, 1), (1, 0), (1, 1))
    linear = q._q_poly_add(q._q_poly_add(Z0, Z1), q._q_poly_scale(-1, A))
    assert q._q_sum_from_exact_cycle_linear(linear) == A
    g0 = q._q_poly_sub(q._q_poly_pow(Z0, 2), ONE)
    g1 = q._q_poly_sub(q._q_poly_pow(Z1, 2), ONE)
    normal, steps = q._q_standard_reduce_boundary(
        q._q_poly_add(q._q_poly_pow(Z0, 2), q._q_poly_pow(Z1, 2)), g0, g1
    )
    assert normal == q._q_poly_scale(2, ONE) and type(steps) is tuple and len(steps) == 2
    assert q._q_swap_cycles(Z0) == Z1
    assert q._q_reynolds_boundary(Z0) == q._q_poly_scale(F(1, 2), q._q_poly_add(Z0, Z1))
    identity = ((ONE, ZERO), (ZERO, ONE))
    assert q._q_matmul2(identity, identity) == identity
    assert q._q_trace2(identity) == q._q_poly_scale(2, ONE)
    assert len(q._q_scope_rejections(fixture["controls"]["N5"]["assertions"], "tau")) == 2
    assert q._q_direction_rejection(fixture["controls"]["N7"])["disposition"] == "REJECTED_DIRECTION"
    assert len(q._q_trace_rejections(fixture["controls"]["N8"])) == 2
    assert q._q_semigroup_member(6, (2, 3)) is True
    assert q._q_semigroup_member(1, (2, 3)) is False
    assert q._q_substitute_cycle_product_once(q._q_poly_mul(Z0, Z1), A) == A
    assert q._q_degree_one_boundary(1) is True
    assert q._q_degree_one_boundary(2) is False
    with pytest.raises(TypeError):
        q._q_degree_one_boundary(True)
    assert q._q_route_monodromy_evidence(1, [ZERO, ONE]) is False
    assert q._q_route_monodromy_evidence(2, [ZERO, ONE, ONE]) is True
    with pytest.raises(ValueError):
        q._q_route_monodromy_evidence(2, [ZERO, ONE])
    with pytest.raises(TypeError):
        q._q_route_monodromy_evidence(True, [ZERO, ONE])
    assert q._q_wire_poly(A) == [{"coefficient": {"denominator": 1, "numerator": 1}, "exponents_acz0z1": [1, 0, 0, 0]}]
    assert _pair_wire(sparse_pair) == {"left_type": "dict", "right_type": "dict"}
    assert _pair_wire(dense_pair) == {"left_type": "tuple", "right_type": "tuple"}


def test_q_exact_algebra_controls_are_nonhollow_and_mutation_sensitive(paper_root):
    definitions, fixture = _inputs(paper_root)
    point = q._q_rat(fixture["controls"]["N1"]["coordinate"])
    parameter = q._q_rat(fixture["controls"]["N1"]["parameter"])
    scalar_map = (parameter, F(0), F(1))
    second_minus_identity = q._q_dense_add(q._q_dense_compose(scalar_map, scalar_map), (0, -1))
    first_minus_identity = q._q_dense_add(scalar_map, (0, -1))
    dynatomic, remainder = q._q_dense_divmod(second_minus_identity, first_minus_identity)
    assert remainder == ()
    assert q._q_dense_eval(scalar_map, point) == point
    assert q._q_dense_eval(dynatomic, point) == 0
    assert 2 * point == -1

    b = q._q_poly_sub(A, ONE)
    g0 = q._q_poly_add(q._q_poly_add(q._q_poly_pow(Z0, 2), q._q_poly_mul(b, Z1)), C)
    g1 = q._q_poly_add(q._q_poly_add(q._q_poly_pow(Z1, 2), q._q_poly_mul(b, Z0)), C)
    difference = q._q_poly_sub(g0, g1)
    linear, sparse_remainder = q._q_poly_exact_div(difference, q._q_poly_sub(Z0, Z1))
    assert sparse_remainder == ZERO
    cycle_sum = q._q_sum_from_exact_cycle_linear(linear)
    assert cycle_sum == q._q_poly_sub(A, ONE)
    normal, steps = q._q_standard_reduce_boundary(
        q._q_poly_add(q._q_poly_pow(Z0, 2), q._q_poly_pow(Z1, 2)), g0, g1
    )
    expected = q._q_poly_sub(q._q_poly_scale(-2, C), q._q_poly_mul(b, q._q_poly_add(Z0, Z1)))
    assert normal == expected and len(steps) == 2

    for mutation in (
        lambda value: value["boundary"].__setitem__("degree", True),
        lambda value: value["boundary"].__setitem__("period", True),
        lambda value: value["boundary"].__setitem__("coordinate_names", ["z0", "z0"]),
        lambda value: value["boundary"].__setitem__("parameter_names", ["a", "a"]),
        lambda value: value["boundary"].__setitem__("route", "neighbor_scan"),
        lambda value: value["controls"]["N1"].__setitem__("family_degree", 3),
        lambda value: value["controls"]["N2"]["relation"].__setitem__("quadratic", 2),
        lambda value: value["controls"]["N3"].__setitem__("normalizer_exponent", 2),
        lambda value: value["controls"]["N5"]["assertions"].__setitem__(1, value["controls"]["N5"]["assertions"][0]),
        lambda value: value["controls"]["N6"]["assertions"].__setitem__(1, value["controls"]["N6"]["assertions"][0]),
        lambda value: value["controls"]["N7"].__setitem__("relation", "contains"),
        lambda value: value["controls"]["N8"].__setitem__("replacements", ["field_trace", "field_trace"]),
        lambda value: value["controls"]["N8"].__setitem__("target", "field_trace"),
    ):
        changed = deepcopy(fixture)
        mutation(changed)
        with pytest.raises((TypeError, ValueError, ArithmeticError)):
            q._q_validate_inputs(definitions, changed)


def test_q_scalar_tuple_wire_mutation_is_rejected(paper_root):
    valid = q._q_dense_divmod((1,), (0, 1))
    assert _pair_wire(valid)["left_type"] == "tuple"
    source_path = paper_root / "code/candidate_v1/track_q/engine.py"
    source = source_path.read_text(encoding="utf-8")
    needle = "return (), tuple(numerator)"
    assert source.count(needle) == 1
    mutated = source.replace(needle, "return 0", 1)
    namespace = {}
    exec(compile(mutated, source_path.as_posix(), "exec"), namespace)
    scalar = namespace["_q_dense_divmod"]((1,), (0, 1))
    assert scalar == 0
    with pytest.raises(TypeError):
        _pair_wire(scalar)
