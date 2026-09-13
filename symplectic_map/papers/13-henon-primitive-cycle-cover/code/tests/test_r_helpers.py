from copy import deepcopy
from fractions import Fraction

import pytest

from candidate_v1.bootstrap.canonical import canonical_bytes, strict_canonical_load, strict_load_bytes
from candidate_v1.track_r import engine as r


F = Fraction
ZERO = {}
ONE = {(0, 0, 0, 0): F(1)}
A = {(1, 0, 0, 0): F(1)}
C = {(0, 1, 0, 0): F(1)}
X = {(0, 0, 1, 0): F(1)}
Y = {(0, 0, 0, 1): F(1)}


def _inputs(paper_root):
    definitions = strict_load_bytes((paper_root / "code/candidate_v1/shared/definitions.json").read_bytes())
    fixture = strict_load_bytes((paper_root / "code/candidate_v1/track_r/private_fixture.json").read_bytes())
    return definitions, fixture


def _pair_wire(value):
    if type(value) is not tuple or len(value) != 2:
        raise TypeError("R endpoint must be a pair")
    left, right = value
    if type(left) not in (tuple, dict) or type(right) not in (tuple, dict):
        raise TypeError("R endpoint pair members")
    return strict_canonical_load(
        canonical_bytes({"left_type": type(left).__name__, "right_type": type(right).__name__})
    )


def test_r_helper_endpoint_shapes_without_top_level_science(paper_root):
    definitions, fixture = _inputs(paper_root)
    r._r_validate_inputs(definitions, fixture)
    assert r._r_fraction([-1, 2]) == F(-1, 2)
    assert r._r_fraction_wire(F(-2, 4)) == [-1, 2]
    assert r._r_exact_nonnegative_power(F(-1, 2), 3) == F(-1, 8)
    assert r._r_exact_nonnegative_power(2, 0) == 1
    with pytest.raises(TypeError):
        r._r_exact_nonnegative_power(2, -1)
    assert r._r_normalize({(0, 0, 0, 0): 0}) == ZERO
    assert r._r_plus(A, C) == {**A, **C}
    assert r._r_times_scalar(2, A) == {(1, 0, 0, 0): F(2)}
    assert r._r_minus(A, A) == ZERO
    assert r._r_times(A, C) == {(1, 1, 0, 0): F(1)}
    assert r._r_power(A, 0) == ONE
    assert r._r_leading(X)[0] == (0, 0, 1, 0)
    sparse_pair = r._r_exact_division(A, C)
    assert sparse_pair == (ZERO, A)
    assert r._r_bareiss(()) == (ONE, ())
    assert r._r_bareiss(((A,),)) == (A, (A,))
    zero_det, zero_pivots = r._r_bareiss(((ZERO, ZERO), (ZERO, ZERO)))
    assert zero_det == ZERO and type(zero_pivots) is tuple
    resultant, pivots = r._r_sylvester_linear_quadratic((ONE, ONE), (ONE, ZERO, ONE))
    assert type(resultant) is dict and type(pivots) is tuple and len(pivots) == 3
    assert r._r_dense_strip((1, 0)) == (F(1),)
    assert r._r_dense_sum((1, 1), (-1, 1)) == (F(0), F(2))
    assert r._r_dense_product((), (1,)) == ()
    assert r._r_dense_composition((1, 1), (0, 1)) == (F(1), F(1))
    dense_pair = r._r_dense_quotient((1,), (0, 1))
    assert dense_pair == ((), (F(1),))
    assert r._r_dense_value((1, 2), 3) == 7
    identity = ((ONE, ZERO), (ZERO, ONE))
    assert r._r_matrix_product2(identity, identity) == identity
    assert r._r_matrix_trace2(identity) == r._r_times_scalar(2, ONE)
    assert r._r_substitute_xy(r._r_times(X, Y), A) == A
    assert r._r_coefficients_in_x(r._r_plus(ONE, X)) == (ONE, ONE)
    assert r._r_semigroup_membership(6, (2, 3)) is True
    assert r._r_semigroup_membership(1, (2, 3)) is False
    nilpotent, square = r._r_fitting_nilpotent_matrix((0, 0, 1))
    assert nilpotent == ((F(0), F(0)), (F(1), F(0)))
    assert square == ((F(0), F(0)), (F(0), F(0)))
    assert r._r_vandermonde((X, Y)) == r._r_minus(Y, X)
    assert r._r_degree_one_boundary(1) is True
    assert r._r_degree_one_boundary(2) is False
    with pytest.raises(TypeError):
        r._r_degree_one_boundary(True)
    assert r._r_exterior_monodromy_evidence(1, ONE) is False
    assert r._r_exterior_monodromy_evidence(2, r._r_minus(Y, X)) is True
    with pytest.raises(TypeError):
        r._r_exterior_monodromy_evidence(True, r._r_minus(Y, X))
    assert r._r_wire(A) == [{"coefficient": [1, 1], "exponents_acxy": [1, 0, 0, 0]}]
    assert len(r._r_scope_guard(fixture["counter_inputs"][3])) == 2
    assert _pair_wire(sparse_pair) == {"left_type": "dict", "right_type": "dict"}
    assert _pair_wire(dense_pair) == {"left_type": "tuple", "right_type": "tuple"}


def test_r_exact_elimination_controls_are_nonhollow_and_mutation_sensitive(paper_root):
    definitions, fixture = _inputs(paper_root)
    n1 = fixture["counter_inputs"][0]
    parameter = r._r_fraction(n1["t_parameter"])
    point = r._r_fraction(n1["point"])
    scalar_map = (parameter, F(0), F(1))
    second_minus_identity = r._r_dense_sum(r._r_dense_composition(scalar_map, scalar_map), (0, -1))
    first_minus_identity = r._r_dense_sum(scalar_map, (0, -1))
    phi2, remainder = r._r_dense_quotient(second_minus_identity, first_minus_identity)
    assert remainder == ()
    assert r._r_dense_value(scalar_map, point) == point
    assert r._r_dense_value(phi2, point) == 0

    b = r._r_minus(A, ONE)
    coefficient_a = r._r_plus(r._r_power(X, 2), C)
    coefficient_d = r._r_plus(r._r_times(b, X), C)
    resultant, pivots = r._r_sylvester_linear_quadratic(
        (coefficient_a, b), (coefficient_d, ZERO, ONE)
    )
    fixed_factor = r._r_plus(r._r_plus(r._r_power(X, 2), r._r_times(b, X)), C)
    primitive, factor_remainder = r._r_exact_division(resultant, fixed_factor)
    coefficients = r._r_coefficients_in_x(primitive)
    assert factor_remainder == ZERO
    assert len(pivots) == 3 and len(coefficients) == 3 and coefficients[2] == ONE
    assert r._r_semigroup_membership(1, (2, 3)) is False

    for mutation in (
        lambda value: value["elimination_input"].__setitem__("degree", 3),
        lambda value: value["elimination_input"].__setitem__("degree", True),
        lambda value: value["elimination_input"].__setitem__("cycle_length", True),
        lambda value: value["elimination_input"]["variables"].__setitem__("base", ["a", "a"]),
        lambda value: value["elimination_input"]["variables"].__setitem__("cycle", ["x", "x"]),
        lambda value: value["elimination_input"].__setitem__("route", "neighbor_scan"),
        lambda value: value["counter_inputs"][0].__setitem__("point", [-2, 3]),
        lambda value: value["counter_inputs"][1]["specialize"].__setitem__("a", 1),
        lambda value: value["counter_inputs"][2]["presentation"].__setitem__("v_as_t_power", 4),
        lambda value: value["counter_inputs"][3]["malformed"].__setitem__(1, value["counter_inputs"][3]["malformed"][0]),
        lambda value: value["counter_inputs"][4]["malformed"].__setitem__(1, value["counter_inputs"][4]["malformed"][0]),
        lambda value: value["counter_inputs"][5].__setitem__("proposed_restriction_arrow", "G_special -> subgroup_of -> G_global"),
        lambda value: value["counter_inputs"][6].__setitem__("proposed_observable_kinds", ["field_extension_trace", "field_extension_trace"]),
    ):
        changed = deepcopy(fixture)
        mutation(changed)
        with pytest.raises((TypeError, ValueError, ArithmeticError)):
            r._r_validate_inputs(definitions, changed)


def test_r_scalar_tuple_wire_mutation_is_rejected(paper_root):
    valid = r._r_bareiss(())
    assert _pair_wire(valid)["right_type"] == "tuple"
    source_path = paper_root / "code/candidate_v1/track_r/engine.py"
    source = source_path.read_text(encoding="utf-8")
    needle = "return one, ()"
    assert source.count(needle) == 1
    mutated = source.replace(needle, "return 0", 1)
    namespace = {}
    exec(compile(mutated, source_path.as_posix(), "exec"), namespace)
    scalar = namespace["_r_bareiss"](())
    assert scalar == 0
    with pytest.raises(TypeError):
        _pair_wire(scalar)
