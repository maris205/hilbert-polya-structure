#!/usr/bin/env python3
"""P214 author verifier SOURCE; no results are supplied by this source file.

Frozen finite box only. See OUTPUT_PLAN.md and OUTPUT_SCHEMA.json.
The program reads no data/configuration files and writes JSONL only to stdout.
It must not be run until a separate source reception and runtime grant exist.
"""

import json
import sys


SCHEMA_VERSION = "p214-author-jsonl-v1"
Q_VALUES = (2, 3, 4)
M_VALUES = (2, 3, 4)
PARAMETERS = tuple((q, m) for q in Q_VALUES for m in M_VALUES)


class VerificationMismatch(Exception):
    def __init__(self, scope, name, actual, expected):
        self.detail = {"scope": scope, "check": name,
                       "actual": actual, "expected": expected}


class Audit:
    def __init__(self):
        self.check_count = 0
        self.check_counts = {}
        self.record_counts = {}

    def equal(self, scope, name, actual, expected, checks):
        self.check_count += 1
        self.check_counts[name] = self.check_counts.get(name, 0) + 1
        if actual != expected:
            raise VerificationMismatch(scope, name, actual, expected)
        checks[name] = True

    def emit(self, kind, **payload):
        record = {"schema_version": SCHEMA_VERSION, "kind": kind}
        record.update(payload)
        sys.stdout.write(json.dumps(record, ensure_ascii=True, sort_keys=True,
                                    separators=(",", ":"), allow_nan=False))
        sys.stdout.write("\n")
        self.record_counts[kind] = self.record_counts.get(kind, 0) + 1


class Field:
    def __init__(self, q):
        if q not in Q_VALUES:
            raise ValueError("field order is outside the frozen box")
        self.q = q

    def add(self, a, b):
        return a ^ b if self.q == 4 else (a + b) % self.q

    def neg(self, a):
        return a if self.q == 4 else (-a) % self.q

    def mul(self, a, b):
        if self.q != 4:
            return (a * b) % self.q
        # Codes 0,1,2,3 are 0,1,alpha,1+alpha. Binary polynomial
        # multiplication is reduced by alpha^2+alpha+1 = binary 111.
        product = 0
        left, right = a, b
        while right:
            if right & 1:
                product ^= left
            right >>= 1
            left <<= 1
            if left & 4:
                left ^= 7
        return product

    def inv(self, a):
        if a == 0:
            raise ValueError("zero has no field inverse")
        for b in range(1, self.q):
            if self.mul(a, b) == 1:
                return b
        raise ValueError("field inverse missing")


class Ring:
    def __init__(self, field, m):
        self.field = field
        self.q = field.q
        self.m = m
        self.size = self.q ** m
        self.coefficients = [self.decode(z) for z in range(self.size)]
        self.ideal = list(range(0, self.size, self.q))
        self.ideal_size = len(self.ideal)
        self.state_count = self.ideal_size ** 2
        self.t = self.q

    def decode(self, z):
        result = []
        for unused in range(self.m):
            result.append(z % self.q)
            z //= self.q
        return result

    def encode(self, coefficients):
        return sum(c * self.q ** i for i, c in enumerate(coefficients))

    def add(self, a, b):
        return self.encode([self.field.add(x, y) for x, y in
                            zip(self.coefficients[a], self.coefficients[b])])

    def neg(self, a):
        return self.encode([self.field.neg(c) for c in self.coefficients[a]])

    def mul(self, a, b):
        result = [0] * self.m
        for i, x in enumerate(self.coefficients[a]):
            for j in range(self.m - i):
                result[i + j] = self.field.add(
                    result[i + j], self.field.mul(x, self.coefficients[b][j]))
        return self.encode(result)

    def valuation(self, a):
        for i, c in enumerate(self.coefficients[a]):
            if c != 0:
                return i
        return self.m

    def in_ideal(self, a):
        return 0 <= a < self.size and self.coefficients[a][0] == 0

    def ideal_power(self, r):
        return [a for a in range(self.size) if self.valuation(a) >= r]

    def shift_down(self, a, r):
        return self.encode(self.coefficients[a][r:] + [0] * r)

    def inverse_unit(self, a):
        coefficients = self.coefficients[a]
        inverse_constant = self.field.inv(coefficients[0])
        result = [inverse_constant]
        for degree in range(1, self.m):
            total = 0
            for j in range(1, degree + 1):
                total = self.field.add(total, self.field.mul(
                    coefficients[j], result[degree - j]))
            result.append(self.field.neg(self.field.mul(inverse_constant, total)))
        return self.encode(result)

    def state_id(self, x, y):
        if not self.in_ideal(x) or not self.in_ideal(y):
            raise ValueError("state coordinate is outside I")
        return (x // self.q) * self.ideal_size + (y // self.q)

    def state(self, state_id):
        i, j = divmod(state_id, self.ideal_size)
        return self.ideal[i], self.ideal[j]


def literal_orbit(transitions, start):
    """Repeat detection alone: no valuation, theorem, or clock bound used."""
    path = []
    seen = {}
    current = start
    while current not in seen:
        seen[current] = len(path)
        path.append(current)
        current = transitions[current]
    cycle_start = seen[current]
    return {"state_ids": path + [current],
            "cycle_start_index": cycle_start,
            "cycle_state_ids": path[cycle_start:],
            "period": len(path) - cycle_start,
            "first_zero_index": seen.get(0)}


def invert_transitions(transitions):
    predecessors = [[] for unused in transitions]
    for source, target in enumerate(transitions):
        predecessors[target].append(source)
    return predecessors


def verify_field(audit, field):
    q = field.q
    scope = {"q": q}
    checks = {}
    elements = list(range(q))
    addition = [[field.add(a, b) for b in elements] for a in elements]
    multiplication = [[field.mul(a, b) for b in elements] for a in elements]
    for a in elements:
        audit.equal(scope, "field_additive_identity", field.add(a, 0), a, checks)
        audit.equal(scope, "field_multiplicative_identity", field.mul(a, 1), a, checks)
        audit.equal(scope, "field_additive_inverse", field.add(a, field.neg(a)), 0, checks)
        if a:
            audit.equal(scope, "field_multiplicative_inverse", field.mul(a, field.inv(a)), 1, checks)
        for b in elements:
            audit.equal(scope, "field_addition_closure", field.add(a, b) in elements, True, checks)
            audit.equal(scope, "field_multiplication_closure", field.mul(a, b) in elements, True, checks)
            audit.equal(scope, "field_addition_commutative", field.add(a, b), field.add(b, a), checks)
            audit.equal(scope, "field_multiplication_commutative", field.mul(a, b), field.mul(b, a), checks)
            for c in elements:
                audit.equal(scope, "field_addition_associative", field.add(field.add(a, b), c), field.add(a, field.add(b, c)), checks)
                audit.equal(scope, "field_multiplication_associative", field.mul(field.mul(a, b), c), field.mul(a, field.mul(b, c)), checks)
                audit.equal(scope, "field_distributive", field.mul(a, field.add(b, c)), field.add(field.mul(a, b), field.mul(a, c)), checks)
    if q == 4:
        audit.equal(scope, "gf4_alpha_square", field.mul(2, 2), 3, checks)
        audit.equal(scope, "gf4_characteristic_two", field.add(1, 1), 0, checks)
    audit.emit("field", q=q, characteristic=2 if q == 4 else q,
               element_labels=["0", "1", "alpha", "1+alpha"] if q == 4 else [str(a) for a in elements],
               modulus_binary=7 if q == 4 else None,
               addition_table=addition, multiplication_table=multiplication,
               additive_inverses=[field.neg(a) for a in elements],
               multiplicative_inverses=[None] + [field.inv(a) for a in elements[1:]],
               checks=checks)


def verify_carrier(audit, field, m):
    ring = Ring(field, m)
    q = field.q
    n = ring.state_count
    ids = list(range(n))
    scope = {"q": q, "m": m}
    checks = {}
    audit.equal(scope, "carrier_ideal_size", ring.ideal_size, q ** (m - 1), checks)
    audit.equal(scope, "carrier_state_count", n, q ** (2 * (m - 1)), checks)
    for z in range(ring.size):
        audit.equal(scope, "ring_encoding_round_trip", ring.encode(ring.coefficients[z]), z, checks)
    for r in range(m + 1):
        audit.equal(scope, "ideal_power_cardinality", len(ring.ideal_power(r)), q ** (m - r), checks)
    audit.emit("carrier", q=q, m=m, ring_size=ring.size,
               ideal_size=ring.ideal_size, state_count=n, t_code=ring.t,
               negative_t_code=ring.neg(ring.t), ideal_codes=ring.ideal,
               ring_elements=[{"code": z, "coefficients": ring.coefficients[z],
                               "valuation": ring.valuation(z)} for z in range(ring.size)],
               checks=checks)

    transitions, linear, multiplication_map = [], [], []
    p_map, p_inverse, q_map, q_inverse = [], [], [], []
    for state_id in ids:
        x, y = ring.state(state_id)
        transitions.append(ring.state_id(y, ring.mul(x, ring.add(ring.t, y))))
        linear.append(ring.state_id(y, ring.mul(ring.t, x)))
        multiplication_map.append(ring.state_id(y, ring.mul(x, y)))
        p_map.append(ring.state_id(x, ring.add(y, ring.t)))
        p_inverse.append(ring.state_id(x, ring.add(y, ring.neg(ring.t))))
        q_map.append(ring.state_id(ring.add(x, ring.neg(ring.t)), y))
        q_inverse.append(ring.state_id(ring.add(x, ring.t), y))
    predecessors = invert_transitions(transitions)
    m_predecessors = invert_transitions(multiplication_map)
    checks = {}
    for name, mapping in (("P", p_map), ("P_inverse", p_inverse),
                          ("Q", q_map), ("Q_inverse", q_inverse)):
        audit.equal(scope, "adapter_" + name + "_permutation", sorted(mapping), ids, checks)
    audit.equal(scope, "adapter_P_inverse", [p_inverse[p_map[s]] for s in ids], ids, checks)
    audit.equal(scope, "adapter_Q_inverse", [q_inverse[q_map[s]] for s in ids], ids, checks)
    audit.equal(scope, "adapter_Q_is_not_P_inverse_at_zero", q_map[0] != p_inverse[0], True, checks)
    audit.emit("adapter", q=q, m=m, P=p_map, P_inverse=p_inverse,
               Q=q_map, Q_inverse=q_inverse, M_transitions=multiplication_map,
               nonconjugacy_warning_witness={"state_id": 0, "Q_state_id": q_map[0],
                                             "P_inverse_state_id": p_inverse[0]},
               checks=checks)

    depths, linear_depths = [], []
    recurrent, fixed, linear_recurrent = [], [], []
    for state_id in ids:
        x, y = ring.state(state_id)
        a, b = ring.valuation(x), ring.valuation(y)
        successor = transitions[state_id]
        sx, sy = ring.state(successor)
        orbit = literal_orbit(transitions, state_id)
        linear_orbit = literal_orbit(linear, state_id)
        depth = orbit["first_zero_index"]
        expected_depth = max(2 * (m - b), 2 * (m - a) - 1)
        state_scope = {"q": q, "m": m, "state_id": state_id}
        checks = {}
        audit.equal(state_scope, "state_encoding_round_trip", ring.state_id(x, y), state_id, checks)
        audit.equal(state_scope, "closure", ring.in_ideal(sx) and ring.in_ideal(sy), True, checks)
        audit.equal(state_scope, "product_valuation", ring.valuation(ring.mul(x, y)), min(m, a + b), checks)
        audit.equal(state_scope, "second_successor_in_t_squared", ring.valuation(sy) >= 2, True, checks)
        audit.equal(state_scope, "orbit_repeat_bound", len(orbit["state_ids"]) <= n + 1, True, checks)
        audit.equal(state_scope, "unique_recurrent_sink_per_orbit", orbit["cycle_state_ids"], [0], checks)
        audit.equal(state_scope, "recurrent_period_one", orbit["period"], 1, checks)
        audit.equal(state_scope, "exact_clock", depth, expected_depth, checks)
        audit.equal(state_scope, "maximum_depth_characterization", depth == 2 * m - 2, b == 1, checks)
        audit.equal(state_scope, "QMP_pointwise", q_map[multiplication_map[p_map[state_id]]], successor, checks)
        audit.equal(state_scope, "linear_unique_recurrent_sink", linear_orbit["cycle_state_ids"], [0], checks)
        audit.equal(state_scope, "linear_clock", linear_orbit["first_zero_index"], expected_depth, checks)
        if m == 2:
            audit.equal(state_scope, "m2_linear_boundary", successor, linear[state_id], checks)
            audit.equal(state_scope, "m2_literal_boundary", successor, ring.state_id(y, 0), checks)
        scalar_path = [ring.state(s)[0] for s in orbit["state_ids"][:-1]]
        scalar_path.append(ring.state(orbit["state_ids"][-2])[1])
        for index, z in enumerate(scalar_path):
            if index >= 2:
                audit.equal(state_scope, "later_scalar_in_t_squared", ring.valuation(z) >= 2, True, checks)
                audit.equal(state_scope, "later_multiplier_valuation_one", ring.valuation(ring.add(ring.t, z)), 1, checks)
            if b >= 2:
                chain_expected = min(m, (a if index % 2 == 0 else b) + index // 2)
                audit.equal(state_scope, "noncancellation_chain_valuation", ring.valuation(z), chain_expected, checks)
            elif index % 2:
                audit.equal(state_scope, "cancellation_safe_odd_chain", ring.valuation(z), min(m, 1 + index // 2), checks)
            else:
                audit.equal(state_scope, "cancellation_even_chain_lower_bound", ring.valuation(z) >= min(m, a + index // 2), True, checks)
        depths.append(depth)
        linear_depths.append(linear_orbit["first_zero_index"])
        if orbit["cycle_start_index"] == 0:
            recurrent.append(state_id)
        if linear_orbit["cycle_start_index"] == 0:
            linear_recurrent.append(state_id)
        if successor == state_id:
            fixed.append(state_id)
        audit.emit("state", q=q, m=m, state_id=state_id, x_code=x, y_code=y,
                   x_valuation=a, y_valuation=b, successor_state_id=successor,
                   linear_successor_state_id=linear[state_id], orbit=orbit,
                   linear_orbit=linear_orbit, actual_depth=depth,
                   expected_depth=expected_depth, scalar_path_codes=scalar_path,
                   P_state_id=p_map[state_id], M_P_state_id=multiplication_map[p_map[state_id]],
                   Q_M_P_state_id=q_map[multiplication_map[p_map[state_id]]], checks=checks)

    predicted_predecessors = []
    target_d = []
    for target in ids:
        u, w = ring.state(target)
        s = ring.add(ring.t, u)
        valuation_s = ring.valuation(s)
        d = min(valuation_s, m - 1)
        target_d.append(d)
        feasible = ring.valuation(w) >= d + 1
        kernel = ring.ideal_power(m - d)
        unit = unit_inverse = shifted_w = x0 = None
        if d < m - 1:
            unit = ring.shift_down(s, d)
            unit_inverse = ring.inverse_unit(unit)
        if feasible:
            if d == m - 1:
                x0 = 0
            else:
                shifted_w = ring.shift_down(w, d + 1)
                x0 = ring.mul(ring.t, ring.mul(unit_inverse, shifted_w))
            coset = sorted(ring.state_id(ring.add(x0, k), u) for k in kernel)
        else:
            coset = []
        predicted_predecessors.append(coset)
        literal = predecessors[target]
        m_target = q_inverse[target]
        transported = sorted(p_inverse[z] for z in m_predecessors[m_target])
        target_scope = {"q": q, "m": m, "target_state_id": target}
        checks = {}
        audit.equal(target_scope, "fibre_feasibility", bool(literal), feasible, checks)
        audit.equal(target_scope, "fibre_kernel_size", len(kernel), q ** d, checks)
        audit.equal(target_scope, "fibre_size", len(literal), q ** d if feasible else 0, checks)
        audit.equal(target_scope, "fibre_coset_equality", literal, coset, checks)
        audit.equal(target_scope, "fibre_QMP_transport", literal, transported, checks)
        audit.equal(target_scope, "fibre_first_coordinate_constraint", [ring.state(z)[1] for z in literal], [u] * len(literal), checks)
        audit.equal(target_scope, "fibre_kernel_equation", [ring.mul(s, k) for k in kernel], [0] * len(kernel), checks)
        if unit is not None:
            audit.equal(target_scope, "fibre_unit_inverse", ring.mul(unit, unit_inverse), 1, checks)
            audit.equal(target_scope, "fibre_shifted_unit", ring.mul(q ** d, unit), s, checks)
        if feasible:
            audit.equal(target_scope, "fibre_representative_in_I", ring.in_ideal(x0), True, checks)
            audit.equal(target_scope, "fibre_representative_equation", ring.mul(s, x0), w, checks)
        if d == m - 1:
            audit.equal(target_scope, "saturated_feasibility", feasible, w == 0, checks)
        audit.emit("target", q=q, m=m, target_state_id=target, u_code=u, w_code=w,
                   multiplier_code=s, multiplier_valuation=valuation_s, d=d,
                   feasible=feasible, predecessor_state_ids=literal,
                   actual_fibre_size=len(literal), expected_fibre_size=q ** d if feasible else 0,
                   kernel_codes=kernel, unit_code=unit, inverse_unit_code=unit_inverse,
                   shifted_w_code=shifted_w, representative_x_code=x0,
                   coset_predecessor_state_ids=coset, M_target_state_id=m_target,
                   M_predecessor_state_ids=m_predecessors[m_target],
                   transported_predecessor_state_ids=transported, checks=checks)

    for h in range(2 * m - 1):
        actual_exact = [s for s in ids if depths[s] == h]
        actual_cumulative = [s for s in ids if depths[s] <= h]
        linear_exact = [s for s in ids if linear_depths[s] == h]
        linear_cumulative = [s for s in ids if linear_depths[s] <= h]
        threshold_x = m - (h + 1) // 2
        threshold_y = m - h // 2
        ideal_rectangle = [s for s in ids if ring.valuation(ring.state(s)[0]) >= threshold_x
                           and ring.valuation(ring.state(s)[1]) >= threshold_y]
        checks = {}
        expected_exact = 1 if h == 0 else (q - 1) * q ** (h - 1)
        depth_scope = {"q": q, "m": m, "h": h}
        audit.equal(depth_scope, "cumulative_depth_rectangle", actual_cumulative, ideal_rectangle, checks)
        audit.equal(depth_scope, "cumulative_depth_count", len(actual_cumulative), q ** h, checks)
        audit.equal(depth_scope, "exact_depth_count", len(actual_exact), expected_exact, checks)
        audit.equal(depth_scope, "linear_exact_depth_census", linear_exact, actual_exact, checks)
        audit.equal(depth_scope, "linear_cumulative_depth_census", linear_cumulative, actual_cumulative, checks)
        audit.emit("depth_row", q=q, m=m, h=h, threshold_x=threshold_x,
                   threshold_y=threshold_y, exact_state_ids=actual_exact,
                   cumulative_state_ids=actual_cumulative, rectangle_state_ids=ideal_rectangle,
                   linear_exact_state_ids=linear_exact, linear_cumulative_state_ids=linear_cumulative,
                   actual_exact_count=len(actual_exact), expected_exact_count=expected_exact,
                   actual_cumulative_count=len(actual_cumulative), expected_cumulative_count=q ** h,
                   checks=checks)

    image = [s for s in ids if predecessors[s]]
    expected_image_size = q + (q - 1) * sum(q ** (2 * j) for j in range(1, m - 1))
    for d in range(m):
        size = 0 if d == 0 else q ** d
        actual_targets = [s for s in ids if len(predecessors[s]) == size]
        if d == 0:
            expected_targets = [s for s in ids if not predicted_predecessors[s]]
        else:
            expected_targets = [s for s in ids if target_d[s] == d and predicted_predecessors[s]]
        expected_count = (n - expected_image_size if d == 0 else
                          q if d == m - 1 else (q - 1) * q ** (2 * (m - d - 1)))
        checks = {}
        census_scope = {"q": q, "m": m, "d": d}
        audit.equal(census_scope, "fibre_census_target_set", actual_targets, expected_targets, checks)
        audit.equal(census_scope, "fibre_census_count", len(actual_targets), expected_count, checks)
        audit.emit("fibre_row", q=q, m=m, d=d, fibre_size=size,
                   target_state_ids=actual_targets, expected_target_state_ids=expected_targets,
                   actual_count=len(actual_targets), expected_count=expected_count, checks=checks)

    max_depth_ids = [s for s in ids if depths[s] == max(depths)]
    expected_max_depth_ids = [s for s in ids if ring.valuation(ring.state(s)[1]) == 1]
    largest_fibre = max(len(bucket) for bucket in predecessors)
    largest_fibre_ids = [s for s in ids if len(predecessors[s]) == largest_fibre]
    saturated = sorted(ring.state_id(ring.add(ring.neg(ring.t), c * q ** (m - 1)), 0)
                       for c in range(q))
    checks = {}
    audit.equal(scope, "zero_fixed", transitions[0], 0, checks)
    audit.equal(scope, "unique_recurrent_set", recurrent, [0], checks)
    audit.equal(scope, "unique_fixed_set", fixed, [0], checks)
    audit.equal(scope, "linear_unique_recurrent_set", linear_recurrent, [0], checks)
    audit.equal(scope, "maximum_depth_value", max(depths), 2 * m - 2, checks)
    audit.equal(scope, "maximum_depth_exact_set", max_depth_ids, expected_max_depth_ids, checks)
    audit.equal(scope, "maximum_fibre_value", largest_fibre, q ** (m - 1), checks)
    audit.equal(scope, "maximum_fibre_exact_set", largest_fibre_ids, saturated, checks)
    audit.equal(scope, "saturated_target_count", len(saturated), q, checks)
    audit.equal(scope, "image_size", len(image), expected_image_size, checks)
    audit.equal(scope, "image_exact_set", image, [s for s in ids if predicted_predecessors[s]], checks)
    audit.equal(scope, "predecessor_partition", sorted(z for bucket in predecessors for z in bucket), ids, checks)
    audit.equal(scope, "fibre_mass", sum(len(bucket) for bucket in predecessors), n, checks)
    cancellation_seed = ring.state_id(ring.t, ring.neg(ring.t))
    cancellation_orbit = literal_orbit(transitions, cancellation_seed)
    cancellation_expected = [cancellation_seed]
    for index in range(1, len(cancellation_orbit["state_ids"])):
        exponent = index // 2 + 1
        power = q ** exponent if exponent < m else 0
        negative_power = ring.neg(power)
        cancellation_expected.append(ring.state_id(negative_power, 0) if index % 2
                                     else ring.state_id(0, negative_power))
    audit.equal(scope, "cancellation_witness_trajectory", cancellation_orbit["state_ids"], cancellation_expected, checks)
    audit.equal(scope, "cancellation_witness_clock", cancellation_orbit["first_zero_index"], 2 * m - 2, checks)
    cancellation_witness = {"state_id": cancellation_seed, "orbit": cancellation_orbit,
                            "expected_state_ids": cancellation_expected}
    unequal_witness = None
    nonlinear_witness = None
    if m >= 3:
        small, large = ring.state_id(0, 0), ring.state_id(ring.neg(ring.t), 0)
        unequal_witness = {"small_target_state_id": small, "large_target_state_id": large,
                           "small_predecessor_state_ids": predecessors[small],
                           "large_predecessor_state_ids": predecessors[large],
                           "small_fibre_size": len(predecessors[small]),
                           "large_fibre_size": len(predecessors[large])}
        audit.equal(scope, "unequal_positive_fibre_small", len(predecessors[small]), q, checks)
        audit.equal(scope, "unequal_positive_fibre_large", len(predecessors[large]), q ** (m - 1), checks)
        audit.equal(scope, "unequal_positive_fibres", 0 < len(predecessors[small]) < len(predecessors[large]), True, checks)
        witness = ring.state_id(ring.t, ring.t)
        nonlinear_witness = {"state_id": witness, "F_state_id": transitions[witness],
                             "L_state_id": linear[witness]}
        audit.equal(scope, "m_ge_3_literal_nonlinear_difference", transitions[witness] != linear[witness], True, checks)
    audit.emit("carrier_complete", q=q, m=m, state_count=n, target_count=n,
               recurrent_state_ids=recurrent, fixed_state_ids=fixed,
               linear_recurrent_state_ids=linear_recurrent,
               maximum_depth=max(depths), maximum_depth_state_ids=max_depth_ids,
               expected_maximum_depth_state_ids=expected_max_depth_ids,
               maximum_fibre_size=largest_fibre, maximum_fibre_target_state_ids=largest_fibre_ids,
               saturated_target_state_ids=saturated, image_target_state_ids=image,
               actual_image_size=len(image), expected_image_size=expected_image_size,
               empty_fibre_count=n - len(image), unequal_positive_fibre_witness=unequal_witness,
               nonlinear_literal_witness=nonlinear_witness,
               cancellation_witness=cancellation_witness, checks=checks)
    return n


def main(audit):
    if len(sys.argv) != 1:
        raise VerificationMismatch({"run": "configuration"}, "no_cli_arguments",
                                   sys.argv[1:], [])
    audit.emit("run_start", parameters=[[q, m] for q, m in PARAMETERS],
               q_values=list(Q_VALUES), m_values=list(M_VALUES),
               program_role="author_verifier", mathematical_scope="fixed_finite_box_only",
               configuration_policy="embedded_constants_no_external_reads")
    total = 0
    for q in Q_VALUES:
        field = Field(q)
        verify_field(audit, field)
        for m in M_VALUES:
            total += verify_carrier(audit, field, m)
    checks = {}
    expected_total = sum(q ** (2 * (m - 1)) for q, m in PARAMETERS)
    audit.equal({"run": "complete"}, "complete_cartesian_state_total", total, expected_total, checks)
    audit.equal({"run": "complete"}, "complete_cartesian_target_total", audit.record_counts.get("target", 0), expected_total, checks)
    audit.equal({"run": "complete"}, "complete_cartesian_carriers", audit.record_counts.get("carrier_complete", 0), len(PARAMETERS), checks)
    audit.equal({"run": "complete"}, "complete_state_records", audit.record_counts.get("state", 0), expected_total, checks)
    expected_record_counts = {"run_start": 1, "field": 3, "carrier": 9,
                              "adapter": 9, "state": 5271, "target": 5271,
                              "depth_row": 45, "fibre_row": 27,
                              "carrier_complete": 9}
    audit.equal({"run": "complete"}, "complete_record_census", audit.record_counts, expected_record_counts, checks)
    audit.emit("run_complete", status="FINITE_BOX_CHECKS_PASSED",
               parameters=[[q, m] for q, m in PARAMETERS], state_count=total,
               target_count=total, carrier_count=len(PARAMETERS),
               check_count=audit.check_count, check_counts=audit.check_counts,
               preceding_record_counts=dict(audit.record_counts), checks=checks,
               limitation="finite checks do not prove all-parameter theorems or establish novelty")


if __name__ == "__main__":
    audit = Audit()
    try:
        main(audit)
    except VerificationMismatch as mismatch:
        audit.emit("verification_failure", status="FAIL", detail=mismatch.detail,
                   attempted_check_count=audit.check_count,
                   preceding_record_counts=dict(audit.record_counts))
        sys.exit(1)
    except Exception as error:
        audit.emit("runtime_error", status="ERROR", error_type=type(error).__name__,
                   message=str(error), attempted_check_count=audit.check_count,
                   preceding_record_counts=dict(audit.record_counts))
        sys.exit(2)
