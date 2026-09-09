#!/usr/bin/env python3
"""One exact, period-unbounded AM1 residual certificate; standard library only."""

import argparse
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
from math import isqrt
from pathlib import Path
import json
import sys


def canonical(word):
    word = tuple(word)
    return min(word[i:] + word[:i] for i in range(len(word)))


def step_z(point, parameter):
    z, w = point
    numerator = w * w + 8 * parameter + 7
    assert z % 2 == w % 2 == 1
    assert numerator % 8 == 0
    result = (w, numerator // 4 - z)
    assert result[0] % 2 == result[1] % 2 == 1
    return result


def states_z(word):
    return {
        (2 * word[i] + 1, 2 * word[(i + 1) % len(word)] + 1)
        for i in range(len(word))
    }


def verify_word(word, parameter):
    length = len(word)
    assert length > 0
    assert len(states_z(word)) == length, "nonprimitive state word"
    for i, value in enumerate(word):
        assert value * (value + 1) % 2 == 0
        assert (
            word[i - 1] + word[(i + 1) % length]
            == value * (value + 1) // 2 + parameter
        )


def symbolic_words(parameter):
    result = {}
    k = 0
    while k * (k + 1) // 2 <= 1 - parameter:
        triangular = k * (k + 1) // 2
        choices = [
            (1 - triangular, (1 - k,), "fixed_lower", k),
            (1 - triangular, (k + 2,), "fixed_upper", k),
            (-1 - triangular, (-k - 1, -k - 1, k, k), "period_four", k),
            (-3 - triangular, (-k - 3, k, k), "period_three_upper", k),
            (-3 - triangular, (k - 2, -k - 1, -k - 1), "period_three_lower", k),
            (-7 - triangular, (-k - 3, k - 2), "period_two", k),
        ]
        for value, word, label, index in choices:
            if value == parameter:
                verify_word(word, parameter)
                result.setdefault(canonical(word), []).append(
                    {"family": label, "k": index}
                )
        k += 1
    return result


def certificate(parameter):
    bound = 4 + isqrt(9 - 8 * parameter)
    alphabet = tuple(
        z for z in range(-bound, bound + 1)
        if z % 2 == 1 and abs(z * z + 8 * parameter + 7) <= 8 * bound
    )
    current = {(z, w) for z in alphabet for w in alphabet}
    sizes = [len(current)]
    while True:
        following = {point for point in current if step_z(point, parameter) in current}
        if following == current:
            break
        assert len(following) < len(current)
        current = following
        sizes.append(len(current))
    assert {step_z(point, parameter) for point in current} == current

    visited = set()
    words = []
    for start in sorted(current):
        if start in visited:
            continue
        local_seen = set()
        orbit = []
        point = start
        while point not in local_seen:
            assert point in current and point not in visited
            local_seen.add(point)
            orbit.append(point)
            point = step_z(point, parameter)
        assert point == start
        visited.update(local_seen)
        word = canonical(tuple((point[0] - 1) // 2 for point in orbit))
        verify_word(word, parameter)
        assert states_z(word) == local_seen
        words.append(word)
    assert visited == current
    assert len(words) == len(set(words))
    words.sort()
    symbolic = symbolic_words(parameter)
    assert set(symbolic).issubset(words), "missing proved symbolic family"
    covered = set()
    for word in words:
        assert not covered.intersection(states_z(word))
        covered.update(states_z(word))
    assert covered == current

    cycles = [
        {"word": word, "least_period": len(word), "symbolic_families": symbolic.get(word, [])}
        for word in words
    ]
    return {
        "a": parameter,
        "doubled_coordinate_bound": bound,
        "doubled_coordinate_alphabet": alphabet,
        "strict_pruning_sizes": sizes,
        "stable_next_step_equal": True,
        "periodic_points": len(current),
        "oriented_cycles": len(cycles),
        "least_period_cycle_counts": dict(sorted(Counter(map(len, words)).items())),
        "cycles": cycles,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    arguments = parser.parse_args()
    if arguments.output.exists() or arguments.output.is_symlink():
        raise FileExistsError("The exact output must not already exist.")
    rows = [certificate(parameter) for parameter in range(-145, 2)]
    all_cycles = [
        {"a": row["a"], **cycle} for row in rows for cycle in row["cycles"]
    ]
    exceptions = [cycle for cycle in all_cycles if not cycle["symbolic_families"]]
    document = {
        "schema": "am1_exact_finite_core/1",
        "executed_at_utc": datetime.now(timezone.utc).isoformat(),
        "python_version": sys.version,
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "parameter_min": -145,
        "parameter_max": 1,
        "parameter_count": len(rows),
        "period_cutoff": None,
        "proof_boundary": "All a <= -146 classified analytically; all a >= 2 empty.",
        "summary": {
            "total_periodic_points_across_parameters": sum(row["periodic_points"] for row in rows),
            "total_oriented_cycles_across_parameters": len(all_cycles),
            "least_periods": sorted({cycle["least_period"] for cycle in all_cycles}),
            "maximum_points_at_one_parameter": max(row["periodic_points"] for row in rows),
            "parameters_at_maximum": [
                row["a"] for row in rows
                if row["periodic_points"] == max(r["periodic_points"] for r in rows)
            ],
            "exceptional_oriented_cycle_count": len(exceptions),
            "exceptions": exceptions,
        },
        "parameters": rows,
    }
    serialized = json.dumps(document, ensure_ascii=True, indent=2, sort_keys=True) + "\n"
    with arguments.output.open("x", encoding="utf-8") as destination:
        destination.write(serialized)
    print(json.dumps({"output": str(arguments.output), "summary": document["summary"]}, indent=2))


if __name__ == "__main__":
    main()
