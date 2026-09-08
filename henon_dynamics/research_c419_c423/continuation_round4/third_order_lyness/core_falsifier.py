"""One exact all-parameter, finite-alphabet Lyness cycle diagnostic."""

from array import array
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
from itertools import product
import json
from pathlib import Path
import platform
import sys
import time


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def main():
    started = time.monotonic()
    values = tuple(range(-8, 0)) + tuple(range(1, 9))
    radix = len(values)
    lookup = {value: digit for digit, value in enumerate(values)}
    size = radix**4
    edges = array("i", [-1]) * size
    legal = 0
    for index, (x, y, z, w) in enumerate(product(values, repeat=4)):
        quotient, remainder = divmod(w * (x + 1), y)
        new_value = quotient - 1
        if remainder == 0 and new_value in lookup:
            edges[index] = (index % radix**3) * radix + lookup[new_value]
            legal += 1

    def decode(index):
        digits = [0] * 4
        for pos in range(3, -1, -1):
            index, digit = divmod(index, radix)
            digits[pos] = values[digit]
        return tuple(digits)

    seen = array("i", [0]) * size
    records = []
    for initial in range(size):
        if seen[initial]:
            continue
        tag = initial + 1
        path = []
        node = initial
        while node >= 0 and seen[node] == 0:
            seen[node] = tag
            path.append(node)
            node = edges[node]
        if node < 0 or seen[node] != tag:
            continue
        cycle = path[path.index(node):]
        states = [decode(index) for index in cycle]
        word = tuple(state[0] for state in states)
        word = min(word[j:] + word[:j] for j in range(len(word)))
        period = len(word)
        parameter = word[0] * word[3 % period] - word[1 % period] - word[2 % period]
        for j in range(period):
            require(word[j] * word[(j+3) % period]
                    == parameter + word[(j+1) % period] + word[(j+2) % period],
                    "original recurrence failed")
        require(all(any(word[j] != word[(j+shift) % period]
                        for j in range(period)) for shift in range(1, period)),
                "reported period not least")
        require(len(set(states)) == period, "repeated state in cycle")
        require(all(x*w-y-z == parameter for x, y, z, w in states),
                "parameter drift in four-state representation")
        records.append({"a": parameter, "period": period, "word": list(word),
                        "height": max(map(abs, word)), "contains_minus_one": -1 in word})

    records.sort(key=lambda row: (row["a"], row["period"], row["word"]))
    require(len({tuple(row["word"]) for row in records}) == len(records),
            "duplicate cyclic word")
    counterexamples = [row for row in records if row["a"] != 1
                       and row["period"] > 3 and not row["contains_minus_one"]
                       and row["height"] > 4]
    payload = {
        "status": "EXACT_FINITE_ALPHABET_ONLY",
        "utc": datetime.now(timezone.utc).isoformat(),
        "python": platform.python_version(), "optimize": sys.flags.optimize,
        "alphabet": list(values), "states": size, "retained_edges": legal,
        "coefficient_range": "all coefficients represented by in-alphabet cycles",
        "period_cutoff": None, "cycles": records,
        "cycle_period_counts": dict(sorted(Counter(row["period"] for row in records).items())),
        "core_hypothesis_counterexamples": counterexamples,
        "full_height_classification_claimed": False,
        "independent_reconstruction_claimed": False,
        "script_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "elapsed_seconds": time.monotonic() - started,
    }
    destination = Path(__file__).with_name("FINITE_ALPHABET_RESULT.json")
    encoded = json.dumps(payload, sort_keys=True, indent=2) + "\n"
    with destination.open("x", encoding="utf-8") as handle:
        handle.write(encoded)
    summary = {key: value for key, value in payload.items() if key != "cycles"}
    summary["cycle_count"] = len(records)
    summary["output_sha256"] = sha256(encoded.encode()).hexdigest()
    print(json.dumps(summary, sort_keys=True))


if __name__ == "__main__":
    main()
