#!/usr/bin/env python3
"""P215 AUTHOR SOURCE; execution requires a later separate grant.

Only sys is imported. No files, old implementations, random inputs, or CLI
parameter overrides are read. Complete deterministic JSON goes to stdout.
This source is not an execution receipt or an all-parameter proof.
"""
import sys


def wire(value):
    """Encode precisely the finite ASCII JSON grammar documented locally."""
    if value is None:
        return "null"
    if type(value) is bool:
        return "true" if value else "false"
    if type(value) is int:
        return str(value)
    if type(value) is str:
        result = '"'
        for character in value:
            number = ord(character)
            if number < 32 or number > 126:
                raise ValueError("non_ascii_wire_string")
            if character == '"' or character == "\\":
                result += "\\"
            result += character
        return result + '"'
    if type(value) is list:
        return "[" + ",".join(wire(item) for item in value) + "]"
    if type(value) is dict:
        if any(type(key) is not str for key in value):
            raise ValueError("non_string_wire_key")
        return "{" + ",".join(wire(key) + ":" + wire(value[key])
                              for key in sorted(value)) + "}"
    raise ValueError("unsupported_wire_type")


def words(length, q):
    result = [()]
    for unused in range(length):
        result = [prefix + (digit,) for prefix in result
                  for digit in range(q + 1)]
    return result


def arrays(items):
    return [list(item) for item in items]


def transition(x):
    peak = 0
    result = []
    for value in x:
        if value > peak:
            peak = value
        result.append(peak - value)
    return tuple(result)


def signs(x):
    previous = 0
    differences = []
    nonzero = []
    runs = []
    for value in x:
        difference = value - previous
        differences.append(difference)
        previous = value
        if difference != 0:
            sign = 1 if difference > 0 else -1
            nonzero.append(sign)
            if not runs or runs[-1] != sign:
                runs.append(sign)
    return differences, nonzero, runs


def choose(upper, lower):
    if upper < 0 or lower < 0:
        raise ValueError("negative_binomial_argument")
    if lower > upper:
        return 0
    result = 1
    for index in range(1, lower + 1):
        result = result * (upper - index + 1) // index
    return result


def inverse_formula(y, q):
    # No call to transition, and no access to actual predecessor buckets.
    if not y:
        return {"zeros": [], "b": [], "B": [], "c": [], "A": [1],
                "recurrence_terms": [], "height_sequences": [[]],
                "constructed_sources": [[]], "count": 1}
    if y[0] != 0:
        return {"zeros": [], "b": [], "B": [], "c": [], "A": [],
                "recurrence_terms": [], "height_sequences": [],
                "constructed_sources": [], "count": 0}
    zeros = [index for index in range(len(y)) if y[index] == 0]
    ends = zeros[1:] + [len(y)]
    barriers = [max(y[start:end]) for start, end in zip(zeros, ends)]
    prefix = []
    for barrier in barriers:
        prefix.append(max(prefix[-1] if prefix else 0, barrier))
    ceilings = [q - barrier for barrier in reversed(prefix)]
    heights = []
    sources = []
    for height in words(len(zeros), q):
        if any(height[j] < prefix[j] for j in range(len(zeros))):
            continue
        if any(height[j] > height[j + 1] for j in range(len(zeros) - 1)):
            continue
        source = []
        for j in range(len(zeros)):
            source.extend(height[j] - y[i] for i in range(zeros[j], ends[j]))
        heights.append(list(height))
        sources.append(source)
    values = [1]
    terms = []
    for m in range(1, len(zeros) + 1):
        base = choose(ceilings[m - 1] + m, m)
        subtractions = []
        for i in range(1, m):
            upper = ceilings[m - 1] - ceilings[i - 1] + m - i
            lower = m - i + 1
            coefficient = choose(upper, lower)
            subtractions.append({"i": i, "prefix_count": values[i - 1],
                                 "upper": upper, "lower": lower,
                                 "binomial": coefficient,
                                 "product": values[i - 1] * coefficient})
        value = base - sum(term["product"] for term in subtractions)
        values.append(value)
        terms.append({"m": m, "base_upper": ceilings[m - 1] + m,
                      "base_lower": m, "base": base,
                      "subtractions": subtractions, "value": value})
    return {"zeros": [index + 1 for index in zeros], "b": barriers,
            "B": prefix, "c": ceilings, "A": values,
            "recurrence_terms": terms, "height_sequences": heights,
            "constructed_sources": sources, "count": values[-1]}


class Ledger:
    def __init__(self):
        self.checks = 0
        self.failures = 0

    def compare(self, name, actual, expected):
        passed = actual == expected
        self.checks += 1
        if not passed:
            self.failures += 1
        return {"name": name, "actual": actual, "expected": expected,
                "pass": passed}


def box(n, q, ledger):
    states = words(n, q)
    zero = (0,) * n
    edges = {x: transition(x) for x in states}
    buckets = {y: [] for y in states}
    for x in states:
        # A malformed transition raises, producing an identifiable failure.
        buckets[edges[x]].append(x)
    state_records = []
    recurrent = set()
    clock_counts = [0] * (len(states) + 1)
    deepest = []
    height_actual = -1
    expected_deepest = []
    for x in states:
        orbit = []
        seen = {}
        current = x
        # Stop only on a repeated state, never on a predicted clock or zero.
        while current not in seen:
            seen[current] = len(orbit)
            orbit.append(current)
            current = edges[current]
        entry = seen[current]
        cycle = orbit[entry:]
        recurrent.update(cycle)
        clock_counts[entry] += 1
        if entry > height_actual:
            height_actual = entry
            deepest = [x]
        elif entry == height_actual:
            deepest.append(x)
        differences, nonzero, runs = signs(x)
        out_differences, out_nonzero, out_runs = signs(edges[x])
        alternating = (all(value != 0 for value in differences)
                       and all(differences[i] * differences[i + 1] < 0
                               for i in range(n - 1)))
        maximal_predicate = alternating if n > 0 and q > 0 else x == zero
        if maximal_predicate:
            expected_deepest.append(x)
        checks = [
            ledger.compare("exact_clock", entry, len(runs)),
            ledger.compare("cycle_is_zero", arrays(cycle), [list(zero)]),
            ledger.compare("output_runs", out_runs,
                           [-sign for sign in runs[1:]]),
            ledger.compare("run_drop", len(out_runs), max(0, len(runs) - 1)),
            ledger.compare("deepest_predicate", entry == (n if n and q else 0),
                           maximal_predicate),
        ]
        state_records.append({"x": list(x), "Fx": list(edges[x]),
                              "orbit": arrays(orbit) + [list(current)],
                              "repeat_index": entry, "period": len(cycle),
                              "cycle": arrays(cycle), "clock": entry,
                              "differences": differences,
                              "nonzero_signs": nonzero, "runs": runs,
                              "output_differences": out_differences,
                              "output_nonzero_signs": out_nonzero,
                              "output_runs": out_runs,
                              "alternating_nonzero": alternating,
                              "maximal_predicate": maximal_predicate,
                              "comparisons": checks})
    targets = []
    actual_image = []
    expected_image = []
    largest = -1
    largest_targets = []
    fibre_counts = [0] * (len(states) + 1)
    for y in states:
        actual = arrays(buckets[y])
        formula = inverse_formula(y, q)
        constructed = formula["constructed_sources"]
        image_predicate = not y or y[0] == 0
        if actual:
            actual_image.append(y)
        if image_predicate:
            expected_image.append(y)
        count = len(actual)
        fibre_counts[count] += 1
        if count > largest:
            largest = count
            largest_targets = [y]
        elif count == largest:
            largest_targets.append(y)
        checks = [
            ledger.compare("complete_fibre", actual, sorted(constructed)),
            ledger.compare("construction_injective", len(constructed),
                           len(set(tuple(source) for source in constructed))),
            ledger.compare("height_source_lengths", len(formula["height_sequences"]),
                           len(constructed)),
            ledger.compare("recurrence_actual", formula["count"], count),
            ledger.compare("recurrence_construction", formula["count"], len(constructed)),
            ledger.compare("image_predicate", bool(actual), image_predicate),
        ]
        targets.append({"y": list(y), "actual_predecessors": actual,
                        "actual_count": count, "image_predicate": image_predicate,
                        "formula": formula, "comparisons": checks})
    checks = [
        ledger.compare("carrier_size", len(states), (q + 1) ** n),
        ledger.compare("unique_recurrent", arrays(sorted(recurrent)), [list(zero)]),
        ledger.compare("sharp_height", height_actual, n if n and q else 0),
        ledger.compare("complete_deepest_set", arrays(deepest), arrays(expected_deepest)),
        ledger.compare("complete_image", arrays(actual_image), arrays(expected_image)),
        ledger.compare("image_size", len(actual_image), (q + 1) ** (n - 1) if n else 1),
        ledger.compare("maximum_fibre", largest, choose(q + n, n)),
        ledger.compare("maximum_fibre_targets", arrays(largest_targets), [list(zero)]),
        ledger.compare("clock_census_total", sum(clock_counts), len(states)),
        ledger.compare("target_census_total", sum(fibre_counts), len(states)),
        ledger.compare("fibre_mass", sum(i * fibre_counts[i] for i in range(len(fibre_counts))),
                       len(states)),
    ]
    return {"n": n, "q": q, "carrier_size": len(states),
            "states": state_records, "targets": targets,
            "recurrent_states": arrays(sorted(recurrent)),
            "height": height_actual, "deepest_states": arrays(deepest),
            "expected_deepest_states": arrays(expected_deepest),
            "image": arrays(actual_image), "expected_image": arrays(expected_image),
            "maximum_fibre": largest, "maximum_fibre_targets": arrays(largest_targets),
            "clock_census": clock_counts, "fibre_census": fibre_counts,
            "comparisons": checks}


def main():
    if len(sys.argv) != 1:
        sys.stdout.write(wire({"kind": "failure", "reason": "arguments_forbidden"}) + "\n")
        return 2
    ledger = Ledger()
    boxes = []
    context = {"n": None, "q": None}
    try:
        for n in range(6):
            for q in range(4):
                context = {"n": n, "q": q}
                boxes.append(box(n, q, ledger))
        comparisons = [
            ledger.compare("box_count", len(boxes), 24),
            ledger.compare("state_count", sum(item["carrier_size"] for item in boxes), 1798),
        ]
        result = {"kind": "p215_author_verification", "schema_version": 1,
                  "parameters": {"n": [0, 1, 2, 3, 4, 5], "q": [0, 1, 2, 3]},
                  "boxes": boxes, "comparisons": comparisons,
                  "checks": ledger.checks, "failures": ledger.failures,
                  "pass": ledger.failures == 0}
        sys.stdout.write(wire(result) + "\n")
        return 0 if ledger.failures == 0 else 1
    except Exception:
        # Preserve all completed boxes; never replace or suppress a bad run.
        sys.stdout.write(wire({"kind": "failure", "reason": "runtime_exception",
                               "context": context, "completed_boxes": boxes,
                               "checks": ledger.checks,
                               "failures": ledger.failures}) + "\n")
        return 2


if __name__ == "__main__":
    sys.exit(main())
