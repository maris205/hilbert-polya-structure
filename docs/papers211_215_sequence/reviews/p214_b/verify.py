"""P214 Review B verifier source. SOURCE ONLY until a separate root grant."""


def field_add(q, a, b):
    return (a ^ b) if q == 4 else (a + b) % q


def field_neg(q, a):
    return a if q == 4 else (-a) % q


def field_mul(q, a, b):
    if q != 4:
        return (a * b) % q
    out = 0
    left = a
    right = b
    while right:
        if right & 1:
            out ^= left
        right >>= 1
        left <<= 1
        if left & 4:
            left ^= 7
    return out & 3


def field_inv(q, a):
    for b in range(1, q):
        if field_mul(q, a, b) == 1:
            return b
    raise AssertionError("nonzero field element has no inverse")


def digits(code, q, length):
    out = []
    for _ in range(length):
        out.append(code % q)
        code //= q
    return tuple(out)


def ideal_element(index, q, m):
    return (0,) + digits(index, q, m - 1)


def ideal_index(element, q):
    value = 0
    place = 1
    for coefficient in element[1:]:
        value += coefficient * place
        place *= q
    return value


def ring_add(q, left, right):
    return tuple(field_add(q, a, b) for a, b in zip(left, right))


def ring_mul(q, m, left, right):
    out = [0] * m
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j < m:
                out[i + j] = field_add(
                    q, out[i + j], field_mul(q, a, b)
                )
    return tuple(out)


def valuation(element, m):
    for i, coefficient in enumerate(element):
        if coefficient:
            return i
    return m


class Audit:
    def __init__(self):
        self.checks = 0

    def equal(self, actual, expected, label):
        self.checks += 1
        if actual != expected:
            raise AssertionError(
                label + ": actual=" + repr(actual) + " expected=" + repr(expected)
            )

    def true(self, condition, label):
        self.equal(bool(condition), True, label)


def check_field(q, audit):
    for a in range(q):
        audit.equal(field_add(q, a, 0), a, "field additive identity")
        audit.equal(field_mul(q, a, 1), a, "field multiplicative identity")
        audit.equal(field_add(q, a, field_neg(q, a)), 0, "field additive inverse")
        if a:
            audit.equal(field_mul(q, a, field_inv(q, a)), 1, "field inverse")
        for b in range(q):
            audit.equal(field_add(q, a, b), field_add(q, b, a), "field addition commutative")
            audit.equal(field_mul(q, a, b), field_mul(q, b, a), "field multiplication commutative")
            for c in range(q):
                audit.equal(
                    field_add(q, field_add(q, a, b), c),
                    field_add(q, a, field_add(q, b, c)),
                    "field addition associative",
                )
                audit.equal(
                    field_mul(q, field_mul(q, a, b), c),
                    field_mul(q, a, field_mul(q, b, c)),
                    "field multiplication associative",
                )
                audit.equal(
                    field_mul(q, a, field_add(q, b, c)),
                    field_add(q, field_mul(q, a, b), field_mul(q, a, c)),
                    "field distributive",
                )
    if q == 4:
        audit.equal(field_add(q, 2, 2), 0, "F4 characteristic two")
        audit.equal(field_mul(q, 2, 2), 3, "F4 alpha square alpha plus one")


def successor_table(q, m, elements, linear=False):
    size = len(elements)
    t = tuple([0, 1] + [0] * (m - 2))
    out = []
    for x_index, x in enumerate(elements):
        for y_index, y in enumerate(elements):
            multiplier = t if linear else ring_add(q, t, y)
            z = ring_mul(q, m, x, multiplier)
            out.append(y_index * size + ideal_index(z, q))
    return out


def forward_signature(start, successors):
    seen = {}
    path = []
    current = start
    while current not in seen:
        seen[current] = len(path)
        path.append(current)
        current = successors[current]
    cycle_start = seen[current]
    cycle = tuple(path[cycle_start:])
    zero_depth = path.index(0) if 0 in seen else -1
    return zero_depth, cycle


def triangular_x_solutions(q, m, multiplier, target_w):
    d = min(valuation(multiplier, m), m - 1)
    if any(target_w[i] for i in range(d + 1)):
        return d, []
    ideal_size = q ** (m - 1)
    if d == m - 1:
        return d, list(range(ideal_size))

    solved = [0] * m
    inverse_lead = field_inv(q, multiplier[d])
    for k in range(1, m - d):
        degree = d + k
        known = 0
        for i in range(d + 1, degree):
            known = field_add(
                q, known, field_mul(q, multiplier[i], solved[degree - i])
            )
        remainder = field_add(q, target_w[degree], field_neg(q, known))
        solved[k] = field_mul(q, inverse_lead, remainder)

    free_count = d
    answers = []
    for free_code in range(q ** free_count):
        candidate = list(solved)
        free = digits(free_code, q, free_count)
        for offset, coefficient in enumerate(free):
            candidate[m - d + offset] = coefficient
        answers.append(ideal_index(tuple(candidate), q))
    return d, sorted(answers)


def csv(values):
    return ",".join(str(value) for value in values) if values else "-"


def run_carrier(q, m, audit):
    ideal_size = q ** (m - 1)
    elements = [ideal_element(i, q, m) for i in range(ideal_size)]
    states = ideal_size * ideal_size
    transition = successor_table(q, m, elements)
    linear = successor_table(q, m, elements, linear=True)
    predecessors = [[] for _ in range(states)]
    for source, target in enumerate(transition):
        predecessors[target].append(source)

    depths = []
    depth_counts = {}
    for state in range(states):
        x_index = state // ideal_size
        y_index = state % ideal_size
        x = elements[x_index]
        y = elements[y_index]
        depth, cycle = forward_signature(state, transition)
        linear_depth, linear_cycle = forward_signature(state, linear)
        expected = max(2 * (m - valuation(y, m)), 2 * (m - valuation(x, m)) - 1)
        audit.equal(cycle, (0,), "unique F cycle")
        audit.equal(linear_cycle, (0,), "unique linear cycle")
        audit.equal(depth, expected, "forward clock")
        audit.equal(linear_depth, expected, "linear forward clock")
        if m == 2:
            audit.equal(transition[state], linear[state], "m=2 literal boundary")
        depths.append(depth)
        depth_counts[depth] = depth_counts.get(depth, 0) + 1
        print(
            "STATE|q=%d|m=%d|id=%d|x=%d|y=%d|next=%d|depth=%d|formula=%d"
            % (q, m, state, x_index, y_index, transition[state], depth, expected)
        )

    for h in range(0, 2 * m - 1):
        cumulative = sum(count for depth, count in depth_counts.items() if depth <= h)
        exact = depth_counts.get(h, 0)
        audit.equal(cumulative, q ** h, "depth cumulative census")
        audit.equal(exact, 1 if h == 0 else (q - 1) * q ** (h - 1), "depth exact census")

    fibre_counts = {}
    t = tuple([0, 1] + [0] * (m - 2))
    image_count = 0
    max_targets = []
    for target in range(states):
        u_index = target // ideal_size
        w_index = target % ideal_size
        u = elements[u_index]
        w = elements[w_index]
        multiplier = ring_add(q, t, u)
        d, x_solutions = triangular_x_solutions(q, m, multiplier, w)
        predicted = sorted(x_index * ideal_size + u_index for x_index in x_solutions)
        actual = predecessors[target]
        audit.equal(actual, predicted, "coefficient-triangular predecessor set")
        expected_size = 0 if not predicted else q ** d
        audit.equal(len(actual), expected_size, "fibre size formula")
        for source in actual:
            audit.equal(transition[source], target, "listed predecessor transition")
        fibre_counts[len(actual)] = fibre_counts.get(len(actual), 0) + 1
        if actual:
            image_count += 1
        if len(actual) == q ** (m - 1):
            max_targets.append(target)
        print(
            "TARGET|q=%d|m=%d|id=%d|u=%d|w=%d|d=%d|pre=%s|triangular=%s"
            % (q, m, target, u_index, w_index, d, csv(actual), csv(predicted))
        )

    expected_image = q + (q - 1) * sum(q ** (2 * j) for j in range(1, m - 1))
    audit.equal(image_count, expected_image, "image census")
    audit.equal(len(max_targets), q, "maximum-fibre target count")
    audit.true(all(len(predecessors[tg]) == q ** (m - 1) for tg in max_targets), "maximum fibre")
    for d in range(1, m - 1):
        audit.equal(
            fibre_counts.get(q ** d, 0),
            (q - 1) * q ** (2 * (m - d - 1)),
            "ordinary fibre census",
        )
    if m >= 3:
        audit.true(fibre_counts.get(q, 0) > 0, "small positive fibre exists")
        audit.true(fibre_counts.get(q ** (m - 1), 0) > 0, "large positive fibre exists")

    print(
        "CARRIER|q=%d|m=%d|states=%d|maxdepth=%d|image=%d|maxfibre=%d|max_targets=%s"
        % (q, m, states, max(depths), image_count, max(len(x) for x in predecessors), csv(max_targets))
    )
    return states


def main():
    audit = Audit()
    print("P214_B_FORWARD_TRIANGULAR_V1")
    total_states = 0
    carriers = 0
    for q in (2, 3, 4):
        check_field(q, audit)
        for m in (2, 3, 4):
            total_states += run_carrier(q, m, audit)
            carriers += 1
    audit.equal(total_states, 5271, "complete state total")
    audit.equal(carriers, 9, "complete carrier total")
    print(
        "PASS|carriers=%d|states=%d|state_records=%d|target_records=%d|checks=%d"
        % (carriers, total_states, total_states, total_states, audit.checks)
    )


if __name__ == "__main__":
    main()
