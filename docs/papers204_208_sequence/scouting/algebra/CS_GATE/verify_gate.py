#!/usr/bin/env python3
"""Independent bounded CS gate: literal integer-coded matrix arrows.

No author imports or stored author outputs. Matrices are column-major packed
base-q integers. Fields use explicit tiny multiplication tables. All graphs,
fibres, and coordinate-bijection sets are recomputed from literal arrows.
This finite verification is not the all-q proof in CANDIDATE_GATE.md.
"""
from collections import Counter, deque
import json


TABLES = {
    2: ((0, 0), (0, 1)),
    4: ((0, 0, 0, 0), (0, 1, 2, 3),
        (0, 2, 3, 1), (0, 3, 1, 2)),
}


def check_box(q):
    checks = Counter()

    def require(label, condition):
        checks[label] += 1
        if not condition:
            raise AssertionError((q, label, checks[label]))

    mm = TABLES[q]
    size = q**4
    entries = [tuple((code // q**j) % q for j in range(4))
               for code in range(size)]

    def encode(v):
        return sum(x*q**j for j, x in enumerate(v))

    def trace(code):
        v = entries[code]
        return v[0] ^ v[3]

    def scalar(code):
        v = entries[code]
        return v[1] == v[2] == 0 and v[0] == v[3]

    def scale(a, code):
        return encode(mm[a][x] for x in entries[code])

    product_table = []
    for a in range(size):
        u = entries[a]
        row = []
        for b in range(size):
            v = entries[b]
            w = [0]*4
            for i in range(2):
                for j in range(2):
                    w[i+2*j] = mm[u[i]][v[2*j]] ^ mm[u[i+2]][v[1+2*j]]
            row.append(encode(w))
        product_table.append(row)

    def bracket(a, b):
        return product_table[a][b] ^ product_table[b][a]

    def step(code):
        a, b = divmod(code, size)
        return bracket(a, b)*size + (a ^ b)

    arrows = [step(code) for code in range(size**2)]
    one = Counter(arrows)
    degree = [one[code] for code in range(size**2)]
    queue = deque(code for code, d in enumerate(degree) if d == 0)
    peeled = []
    while queue:
        code = queue.popleft()
        peeled.append(code)
        target = arrows[code]
        degree[target] -= 1
        if degree[target] == 0:
            queue.append(target)
    depths = [0]*(size**2)
    for code in reversed(peeled):
        depths[code] = depths[arrows[code]] + 1
    cycles = Counter()
    visited = set()
    for code, d in enumerate(degree):
        if not d or code in visited:
            continue
        cursor, length = code, 0
        while cursor not in visited:
            visited.add(cursor)
            length += 1
            cursor = arrows[cursor]
        cycles[length] += 1

    transformed = set()
    scalar_action_counts = Counter()
    for code in range(size**2):
        a, b = divmod(code, size)
        c, s_matrix = divmod(arrows[code], size)
        s = trace(s_matrix)
        require("trace_constraints", trace(c) == 0 and
                trace(product_table[c][s_matrix]) == 0)
        # The literal orbit is independent of the formula-side recurrence.
        cursor = code
        power, beta = 1, 0
        for k in range(8):
            cursor = arrows[cursor]
            expected = scale(power, c)*size + (s_matrix ^ scale(beta, c))
            require("eight_literal_iterates", cursor == expected)
            beta ^= power
            power = mm[power][s]
        recurrent = a == 0 or (trace(a) == 0 and
            trace(product_table[a][b]) == 0 and trace(b) != 0)
        require("every_state_recurrent_criterion", (depths[code] == 0) == recurrent)
        possible = (a == 0) if scalar(b) else (
            trace(a) == 0 and trace(product_table[a][b]) == 0)
        expected_one = (q**4 if scalar(b) else q**2) if possible else 0
        require("every_target_first_fibre", one[code] == expected_one)

        if s == 0:
            d, c_entry, b_entry, last = entries[a]
            z, y, x, z_again = entries[s_matrix]
            require("zero_trace_coordinates", z == z_again)
            tau = d ^ last
            r = 1 ^ tau
            alpha = z ^ mm[b_entry][y] ^ mm[c_entry][x]
            new = (r, x, y, alpha, d, b_entry, c_entry)
            require("triangular_coordinates_injective", new not in transformed)
            transformed.add(new)
            # Inverse construction checks the full original pair, not just Z.
            old_z = alpha ^ mm[b_entry][y] ^ mm[c_entry][x]
            old_a = encode((d, c_entry, b_entry, d ^ (1 ^ r)))
            old_s = encode((old_z, y, x, old_z))
            require("triangular_coordinates_inverse", (old_a, old_a ^ old_s) == (a, b))
            endpoint = encode((alpha, mm[r][y], mm[r][x], alpha))
            require("scalar_action_endpoint", arrows[arrows[code]] == endpoint)
            scalar_action_counts[endpoint] += 1

    require("triangular_coordinates_surjective", len(transformed) == q**7)
    fibres_by_time = []
    cursor_map = list(range(size**2))
    for t in range(1, 9):
        cursor_map = [arrows[code] for code in cursor_map]
        actual = Counter(cursor_map)
        fibres_by_time.append(Counter(actual.get(code, 0) for code in range(size**2)))
        if t < 2:
            continue
        for code in range(size**2):
            c, s_matrix = divmod(code, size)
            if trace(s_matrix):
                expected = q**2 if trace(c) == 0 and trace(product_table[c][s_matrix]) == 0 else 0
            elif c:
                expected = 0
            else:
                expected = q**5+q**4-q**3 if scalar(s_matrix) else q**4-q**3
            require("every_target_later_fibre", actual[code] == expected)

    require("first_image", len(one) == q**6-q**3+q)
    require("core_count", len(visited) == q**6-q**5+q**3)
    require("depth_two_count", Counter(depths)[2] == q**7-2*q**5+q**3)
    require("sharp_tail", max(depths) == 2)
    require("fixed_count", cycles[1] == q**4)
    require("two_cycle_count", cycles[2] == (q**5-q**3)//2)
    if q == 4:
        require("three_cycle_count", cycles[3] == 2*(q**5-q**3)//3)
    for endpoint in range(size):
        expected = 0 if trace(endpoint) else (
            q**5+q**4-q**3 if scalar(endpoint) else q**4-q**3)
        require("scalar_action_all_endpoint_counts", scalar_action_counts[endpoint] == expected)
    return {
        "q": q, "states": size**2, "zero_trace_input_states": len(transformed),
        "image": len(one), "recurrent": len(visited),
        "depth_census": dict(sorted(Counter(depths).items())),
        "cycle_census": dict(sorted(cycles.items())),
        "first_fibre_spectrum": dict(sorted(fibres_by_time[0].items())),
        "later_fibre_spectrum": dict(sorted(fibres_by_time[1].items())),
        "checked_times": list(range(1, 9)),
        "checks_by_kind": dict(sorted(checks.items())),
        "checks_total": sum(checks.values()), "status": "PASS",
    }


if __name__ == "__main__":
    result = [check_box(q) for q in (2, 4)]
    print(json.dumps({"scope": "CS independent candidate gate, not manuscript review",
        "field4_basis": "F2[z]/(z^2+z+1), packed column-major matrices",
        "boxes": result, "total_checks": sum(row["checks_total"] for row in result),
        "status": "PASS"}, indent=2, sort_keys=True))
