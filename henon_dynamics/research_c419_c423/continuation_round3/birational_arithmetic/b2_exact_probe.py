"""One predeclared complete finite-parameter B2 diagnostic."""

from collections import Counter
from pathlib import Path
import json

from exact_probe import graph_cycles


def parameter_cycles(a, b):
    height = 2 * abs(a) + abs(b) + 1
    digits = [r for r in range(-height, height + 1) if r and r + b]
    allowed = set(digits)
    successor = {}
    for x in digits:
        for y in digits:
            q, remainder = divmod(y + a, x + b)
            if not remainder and q in allowed:
                successor[x, y] = (y, q)
    cycles = graph_cycles(successor)
    for word in cycles:
        n = len(word)
        assert all((word[i] + b) * word[(i + 2) % n]
                   == word[(i + 1) % n] + a for i in range(n))
        assert all(word[i] and word[i] + b for i in range(n))
    return len(digits) ** 2, len(successor), cycles


def main():
    histogram = Counter()
    all_cycles = []
    vertices = edges = 0
    for a in range(-8, 9):
        for b in range(-8, 9):
            if b == 0:
                continue
            v, e, cycles = parameter_cycles(a, b)
            vertices += v
            edges += e
            for word in cycles:
                histogram[len(word)] += 1
                all_cycles.append({"a": a, "b": b, "word": word,
                                   "native_period": len(word),
                                   "visits_unit_denominator_section": any(abs(r + b) == 1 for r in word)})
    longer = [row for row in all_cycles if row["native_period"] > 3]
    avoid = [row for row in all_cycles if row["native_period"] > 1
             and not row["visits_unit_denominator_section"]]
    result = {
        "status": "EXACT_FINITE_PARAMETER_DIAGNOSTIC_ONLY",
        "sample": "All 272 integer pairs -8 <= a,b <= 8 with b != 0",
        "bound": "All periodic nonzero integer coordinates satisfy abs(x) <= 2*abs(a)+abs(b)+1",
        "vertices_examined": vertices,
        "retained_edges": edges,
        "cycles_by_native_period": dict(sorted(histogram.items())),
        "period_at_most_three_guess_survives": not longer,
        "all_longer_cycles_in_sample": longer,
        "nonfixed_cycles_avoiding_section": avoid,
        "all_cycles_in_sample": all_cycles,
        "global_claim": "NONE: height lemma is proved but no all-parameter recurrent-core theorem follows",
    }
    encoded = json.dumps(result, indent=2)
    Path(__file__).with_name("B2_EXACT_PROBE_OUTPUT.json").write_text(encoded + "\n")
    summary = {k: v for k, v in result.items() if k != "all_cycles_in_sample"}
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
