"""Exactly one bounded author pressure test for the predeclared KIP claims."""
import hashlib
import itertools
import json
import math
import os
import sys

NS = tuple(range(1, 8))
EXPECTED_SIZES = (1, 3, 10, 35, 126, 462, 1716)
CATEGORIES = (
    "C1_literal_closure",
    "C2_recurrence_and_terminal",
    "C3_pointwise_and_sharp_height",
    "C4_complete_image",
    "C5_every_predecessor",
    "C6_laurent_fibres_and_mass",
    "C7_exact_endpoint_peeling",
)
TOTAL = {key: 0 for key in CATEGORIES}


def emit(row):
    print(json.dumps(row, sort_keys=True, separators=(",", ":")), flush=True)


def check(category, predicate, details, counts):
    counts[category] += 1
    TOTAL[category] += 1
    if not predicate:
        emit({"kind": "assertion_failure", "category": category, "details": details})
        raise AssertionError((category, details))


def file_pin(path):
    path = os.path.realpath(path)
    with open(path, "rb") as stream:
        raw = stream.read()
    return {"path": path, "bytes": len(raw), "sha256": hashlib.sha256(raw).hexdigest()}


def runtime_observation():
    modules = []
    paths = {os.path.realpath(sys.executable)}
    for name, module in sorted(sys.modules.items()):
        path = getattr(module, "__file__", None)
        if path and os.path.isfile(path):
            resolved = os.path.realpath(path)
            modules.append({"module": name, "path": resolved})
            paths.add(resolved)
    mapped = set()
    with open("/proc/self/maps", encoding="utf-8") as stream:
        for line in stream:
            fields = line.rstrip("\n").split(None, 5)
            if len(fields) == 6 and fields[5].startswith("/") and os.path.isfile(fields[5]):
                mapped.add(os.path.realpath(fields[5]))
    paths.update(mapped)
    return {"kind": "runtime", "python_version": sys.version,
            "executable": os.path.realpath(sys.executable),
            "argv": sys.argv, "cwd": os.getcwd(), "sys_path": sys.path,
            "environment": dict(sorted(os.environ.items())),
            "modules": modules, "mapped_runtime_paths": sorted(mapped),
            "file_pins": [file_pin(path) for path in sorted(paths)],
            "boundary": "observed_runtime_files_not_a_complete_hermetic_reuse_key"}


def endpoints(word):
    ends, values = [], []
    n = len(word)
    for index, value in enumerate(word, 1):
        if index == n or word[index] != value:
            ends.append(index)
            values.append(value)
    return tuple(ends), tuple(values)


def ceiling(points, n):
    return tuple(min(point for point in points if point >= index)
                 for index in range(1, n + 1))


def literal(word):
    n = len(word)
    kernel_ends, image_values = endpoints(word)
    left = ceiling(kernel_ends, n)
    right = ceiling(tuple(sorted(set(image_values) | {n})), n)
    return tuple(left[value - 1] for value in right)


def reconstruct(kernel_ends, image_values, n):
    if len(kernel_ends) != len(image_values) or not kernel_ends or kernel_ends[-1] != n:
        raise AssertionError("invalid endpoint pair")
    result, previous = [], 0
    for end, value in zip(kernel_ends, image_values):
        result.extend([value] * (end - previous))
        previous = end
    return tuple(result)


def in_image(word):
    ends, values = endpoints(word)
    n = len(word)
    return (ends[-1] == values[-1] == n
            and all(end <= value for end, value in zip(ends, values))
            and all(values[index] < ends[index + 1] for index in range(len(ends) - 1)))


def strict_runs(word):
    ends, values = endpoints(word)
    result, active = [], []
    for end, value in zip(ends, values):
        if end == value:
            result.append((tuple(active), end))
            active = []
        else:
            active.append((end, value))
    if active:
        raise AssertionError("missing final anchor in claimed image")
    return tuple(result)


def remaining_height(word):
    return max((len(run) for run, _anchor in strict_runs(word)), default=0)


def peeled_successor(word):
    new_ends, new_values = [], []
    for run, anchor in strict_runs(word):
        for index in range(len(run) - 1):
            new_ends.append(run[index][1])
            new_values.append(run[index + 1][0])
        new_ends.append(anchor)
        new_values.append(anchor)
    return reconstruct(tuple(new_ends), tuple(new_values), len(word))


def gap_options(locations):
    choices = []
    for count in range(len(locations) + 1):
        for selected in itertools.combinations(locations, count):
            for split in range(count + 1):
                choices.append((selected[:split], selected[split:]))
    return tuple(choices)


def gap_sources(target):
    if not in_image(target):
        return []
    n = len(target)
    ends, values = endpoints(target)
    previous = 0
    options = []
    for end, value in zip(ends, values):
        options.append(gap_options(tuple(range(previous + 1, end))))
        previous = value
    sources = []
    for selected in itertools.product(*options):
        source_x = set(values)
        source_a = set(ends)
        for x_extra, a_extra in selected:
            source_x.update(x_extra)
            source_a.update(a_extra)
        difference = len(source_a) - len(source_x)
        if difference == 0:
            source_y = source_a
        elif difference == 1:
            source_y = source_a - {n}
        else:
            continue
        sources.append(reconstruct(tuple(sorted(source_x)), tuple(sorted(source_y)), n))
    return sorted(sources)


def laurent_count(target):
    if not in_image(target):
        return 0
    ends, values = endpoints(target)
    polynomial = {0: 1}
    previous = 0
    for end, value in zip(ends, values):
        gap = end - previous - 1
        local = {}
        for a_count in range(gap + 1):
            for b_count in range(gap - a_count + 1):
                exponent = b_count - a_count
                local[exponent] = local.get(exponent, 0) + math.comb(gap, a_count + b_count)
        product = {}
        for left, left_count in polynomial.items():
            for right, right_count in local.items():
                exponent = left + right
                product[exponent] = product.get(exponent, 0) + left_count * right_count
        polynomial = product
        previous = value
    return polynomial.get(0, 0) + polynomial.get(1, 0)


def orbit_data(start, successors):
    visited, sequence = {}, []
    current = start
    while current not in visited:
        visited[current] = len(sequence)
        sequence.append(current)
        current = successors[current]
    depth = visited[current]
    return depth, tuple(sequence[depth:])


def box(n, expected_size):
    counts = {key: 0 for key in CATEGORIES}
    states = tuple(itertools.combinations_with_replacement(range(1, n + 1), n))
    state_set = set(states)
    successors = {state: literal(state) for state in states}
    check(CATEGORIES[0], len(states) == expected_size == math.comb(2 * n - 1, n),
          {"n": n, "carrier_size": len(states)}, counts)
    observed = {target: [] for target in states}
    for source in states:
        successor = successors[source]
        check(CATEGORIES[0], successor in state_set,
              {"n": n, "source": source, "successor": successor}, counts)
        observed[successor].append(source)
    graph = {state: orbit_data(state, successors) for state in states}
    observed_fixed = tuple(state for state in states if successors[state] == state)
    observed_core = tuple(state for state in states if graph[state][0] == 0)
    projected = []
    for mask in itertools.product((False, True), repeat=n - 1):
        points = tuple(index for index, bit in enumerate(mask, 1) if bit) + (n,)
        projected.append(ceiling(points, n))
    projected = tuple(sorted(projected))
    check(CATEGORIES[1], observed_fixed == observed_core == projected,
          {"n": n, "fixed": observed_fixed, "core": observed_core,
           "projected": projected}, counts)
    inverse_mass = 0
    for state in states:
        depth, cycle = graph[state]
        kernel_ends, image_values = endpoints(state)
        anchor_set = tuple(sorted(set(kernel_ends) & (set(image_values) | {n})))
        expected_terminal = ceiling(anchor_set, n)
        check(CATEGORIES[1], len(cycle) == 1 and cycle[0] == expected_terminal,
              {"n": n, "state": state, "cycle": cycle,
               "expected_terminal": expected_terminal}, counts)
        predicted_depth = 0 if successors[state] == state else 1 + remaining_height(successors[state])
        check(CATEGORIES[2], depth == predicted_depth,
              {"n": n, "state": state, "depth": depth,
               "prediction": predicted_depth}, counts)
        image_predicate = in_image(state)
        check(CATEGORIES[3], bool(observed[state]) == image_predicate,
              {"n": n, "target": state, "observed_nonempty": bool(observed[state]),
               "criterion": image_predicate}, counts)
        decoded = gap_sources(state)
        check(CATEGORIES[4], decoded == sorted(observed[state]) and len(decoded) == len(set(decoded)),
              {"n": n, "target": state, "observed": observed[state], "decoded": decoded}, counts)
        formula_count = laurent_count(state)
        check(CATEGORIES[5], formula_count == len(observed[state]),
              {"n": n, "target": state, "observed_count": len(observed[state]),
               "formula_count": formula_count}, counts)
        inverse_mass += formula_count
        if image_predicate:
            prediction = peeled_successor(state)
            check(CATEGORIES[6], prediction == successors[state],
                  {"n": n, "state": state, "literal": successors[state],
                   "peeling_prediction": prediction}, counts)
        emit({"kind": "state", "n": n, "source": state,
              "successor": successors[state], "height": depth,
              "period": len(cycle), "cycle": cycle,
              "terminal": cycle[0] if len(cycle) == 1 else None,
              "anchor_set": anchor_set, "predicted_height": predicted_depth,
              "target_in_image": image_predicate, "predecessors": observed[state],
              "decoded_predecessors": decoded, "laurent_count": formula_count})
    maximum_height = max(graph[state][0] for state in states)
    theorem_height = 0 if n == 1 else (n + 1) // 2
    check(CATEGORIES[2], maximum_height == theorem_height,
          {"n": n, "maximum_height": maximum_height, "theorem_height": theorem_height}, counts)
    check(CATEGORIES[5], inverse_mass == len(states),
          {"n": n, "inverse_mass": inverse_mass, "carrier_size": len(states)}, counts)
    max_fibre = max(len(observed[state]) for state in states)
    histogram = {}
    for state in states:
        size = len(observed[state])
        histogram[size] = histogram.get(size, 0) + 1
    emit({"kind": "box", "n": n, "states": len(states),
          "image": sum(bool(observed[state]) for state in states),
          "fixed": len(observed_fixed), "recurrent": len(observed_core),
          "maximum_height": maximum_height, "theorem_height": theorem_height,
          "inverse_mass": inverse_mass, "assertions": counts,
          "fibre_histogram": [[size, histogram[size]] for size in sorted(histogram)],
          "observed_maximum_fibre": max_fibre,
          "observed_maximum_fibre_targets": [state for state in states if len(observed[state]) == max_fibre],
          "maximum_fibre_is_descriptive_only": True})


def main():
    desk = os.path.join(os.path.dirname(os.path.realpath(__file__)), "desk")
    emit({"kind": "contract", "n_values": NS, "expected_box_sizes": EXPECTED_SIZES,
          "expected_total_states": sum(EXPECTED_SIZES), "categories": CATEGORIES,
          "contract": file_pin(os.path.join(desk, "PREPILOT_CONTRACT.md")),
          "proof": file_pin(os.path.join(desk, "PROOF_PACKAGE.md")),
          "boundary": "one_exploratory_author_run_not_independent_review"})
    for n, expected_size in zip(NS, EXPECTED_SIZES):
        box(n, expected_size)
    emit(runtime_observation())
    emit({"kind": "complete", "n_values": NS, "total_states": sum(EXPECTED_SIZES),
          "assertions": TOTAL, "assertion_total": sum(TOTAL.values()),
          "scientific_producer_invocations": 1})


if __name__ == "__main__":
    main()
