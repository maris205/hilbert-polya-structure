#!/usr/bin/env python3
"""Independent backward, two-sign IR1 finite-core certification.

No imports from the author package; no bound on period or parameter.
The proof-derived amplitude bound is 100. See REVIEW_PLAN.md.
Author evidence is parsed only for comparison after independent discovery.
"""

from collections import Counter, defaultdict
from hashlib import sha256
import json
from pathlib import Path
import platform
from time import monotonic


AMPLITUDE_BOUND = 100
DESTINATION = Path(__file__).resolve().parent
AUTHOR = DESTINATION.parents[1] / "integral_return"


def require(condition, explanation):
    if not condition:
        raise RuntimeError(explanation)


def step(a, state):
    x, y, z = state
    return y, z, y*z+a-x


def back(a, state):
    x, y, z = state
    return x*y+a-z, x, y


def seed_stream():
    """Right difference first, both signs, coordinate intervals second."""
    for amplitude in range(1, AMPLITUDE_BOUND+1):
        low, high = -3*amplitude-1, 3*amplitude-1
        for delta in (-amplitude, amplitude):
            for center in range(-3, 2):
                for right in range(-amplitude, amplitude+1):
                    left = (center+1)*delta-right
                    if not -amplitude <= left <= amplitude:
                        continue
                    u_low = max(low, low-delta)
                    u_high = min(high, high-delta)
                    if left != 0:
                        radius = 2*amplitude//abs(left)
                        u_low = max(u_low, -1-radius)
                        u_high = min(u_high, -1+radius)
                    if right != 0:
                        radius = 2*amplitude//abs(right)
                        u_low = max(u_low, -delta-1-radius)
                        u_high = min(u_high, -delta-1+radius)
                    for first in range(u_low, u_high+1):
                        third = first+delta
                        a = right-center*third+first+center
                        require(third-center*first+center-a == left,
                                "left difference reconstruction failed")
                        require(center*third+a-first-center == right,
                                "right difference reconstruction failed")
                        require(abs(left) <= amplitude and abs(right) <= amplitude,
                                "neighbor difference bound failed")
                        require(abs((first+1)*left) <= 2*amplitude,
                                "left neighbor-center bound failed")
                        require(abs((third+1)*right) <= 2*amplitude,
                                "right neighbor-center bound failed")
                        yield amplitude, delta, a, (first, center, third)


def walk_backwards(amplitude, a, initial):
    low, high = -3*amplitude-1, 3*amplitude-1
    visited = set()
    state = initial
    while True:
        if min(state) < low or max(state) > high:
            return "height", len(visited), None
        if abs(state[2]-state[0]) > amplitude:
            return "difference", len(visited), None
        if state in visited:
            require(state == initial, "injective orbit acquired a noninitial repeat")
            return "return", len(visited), frozenset(visited)
        visited.add(state)
        next_state = back(a, state)
        require(step(a, next_state) == state, "inverse identity failed")
        state = next_state


def word_states(a, word):
    """Validate a closed word and retain orientation through triples."""
    require(len(word) > 0, "empty periodic word")
    n = len(word)
    states = tuple(tuple(word[(j+k) % n] for k in range(3)) for j in range(n))
    for j, state in enumerate(states):
        require(step(a, state) == states[(j+1) % n], "word recurrence failed")
        require(back(a, state) == states[(j-1) % n], "word inverse recurrence failed")
    return frozenset(states)


def native_word(a, states):
    """Reconstruct from the least triple, without rotating a scalar word."""
    initial = min(states)
    state = initial
    observed = set()
    word = []
    while state not in observed:
        require(state in states, "forward reconstruction left inverse cycle")
        observed.add(state)
        word.append(state[0])
        state = step(a, state)
    require(state == initial and observed == states, "forward cycle mismatch")
    require(len(word_states(a, word)) == len(word), "word not primitive")
    return tuple(word)


def generated_family_match(a, word):
    """Compare full directed-state sets, not author's rotation predicates."""
    actual = word_states(a, word)
    n = len(word)
    proposals = []
    if n <= 2:
        proposals.append(("F2", (word[0], word[1 % n])))
    if a % 2 == 0:
        proposals.append(("F3", (-2, -2, (a+4)//2)))
    for t in set(word):
        proposals.append(("F4", (-1, t, -1, a+1-t)))
        if a == -1:
            proposals.append(("F5", (t, -1, -1-t, 0, 0)))
            proposals.append(("F8", (-1, t, 1, t, -1, -t-2, 1, -t-2)))
        if a == 0:
            proposals.append(("F6", (0, 0, t, 0, 0, -t)))
    if a == 0:
        m = max(abs(t) for t in word)
        if m >= 1:
            proposals.append(("F12", (1, m, 1, m-1, -1, -m,
                                      1, 1-m, 1, -m, -1, m-1)))
    matches = set()
    for label, candidate in proposals:
        candidate_states = word_states(a, candidate)
        if candidate_states == actual:
            matches.add(label)
    # Degenerate F8 is already F4, and degenerate F3/F4/F6 is F2.
    for label in ("F2", "F3", "F4", "F5", "F6", "F8", "F12"):
        if label in matches:
            return label
    return "EXCEPTION"


# Tiny explicit polynomial arithmetic over Z[X,Y], used only to validate
# family identities. It has no numerical evaluation or external CAS.
def constant(value):
    return {(0, 0): value} if value else {}


def plus(*polynomials):
    coefficients = Counter()
    for polynomial in polynomials:
        for exponent, coefficient in polynomial.items():
            coefficients[exponent] += coefficient
    return {exponent: value for exponent, value in coefficients.items() if value}


def neg(polynomial):
    return {exponent: -value for exponent, value in polynomial.items()}


def times(first, second):
    coefficients = Counter()
    for (i, j), x in first.items():
        for (k, ell), y in second.items():
            coefficients[i+k, j+ell] += x*y
    return {exponent: value for exponent, value in coefficients.items() if value}


def symbolic_family_check():
    x, y = {(1, 0): 1}, {(0, 1): 1}
    c = constant
    families = {
        "F2": (plus(x, y, neg(times(x, y))), (x, y)),
        "F3": (plus(times(c(2), x), c(-4)), (c(-2), c(-2), x)),
        "F4": (x, (c(-1), y, c(-1), plus(x, c(1), neg(y)))),
        "F5": (c(-1), (x, c(-1), plus(c(-1), neg(x)), c(0), c(0))),
        "F6": (c(0), (c(0), c(0), x, c(0), c(0), neg(x))),
        "F8": (c(-1), (c(-1), x, c(1), x, c(-1),
                        plus(neg(x), c(-2)), c(1), plus(neg(x), c(-2)))),
        "F12": (c(0), (c(1), x, c(1), plus(x, c(-1)), c(-1), neg(x),
                        c(1), plus(c(1), neg(x)), c(1), neg(x), c(-1),
                        plus(x, c(-1)))),
    }
    identities = {}
    for label, (parameter, word) in families.items():
        n = len(word)
        for j in range(n):
            difference = plus(word[(j+3) % n], word[j], neg(parameter),
                              neg(times(word[(j+1) % n], word[(j+2) % n])))
            require(not difference, f"symbolic recurrence failed for {label} at {j}")
        identities[label] = n
    return identities


def check_author_output(discovered, independent_labels, author_bytes):
    rows = [json.loads(line) for line in author_bytes.splitlines() if line.strip()]
    author_cycles = {}
    for row in rows:
        a, word = row["a"], tuple(row["word"])
        require(type(a) is int and all(type(x) is int for x in word),
                "author evidence has noninteger coordinates")
        require(row["least_period"] == len(word), "author period/word-length mismatch")
        states = word_states(a, word)
        require(len(states) == len(word), "author word repeats an earlier triple")
        key = a, min(states)
        require(key not in author_cycles, "author output repeats an oriented cycle")
        author_cycles[key] = states
        require(row["family"] == independent_labels.get(key),
                f"family disagreement at {key}")
    missing = set(discovered)-set(author_cycles)
    extra = set(author_cycles)-set(discovered)
    require(not missing and not extra, f"author cycle set mismatch: missing={missing}, extra={extra}")
    for key in discovered:
        require(discovered[key] == author_cycles[key], "full directed-state set mismatch")
    return len(rows)


def run():
    started = monotonic()
    source_names = ("IR1_PROOF.md", "certify_ir1_core.py", "IR1_CORE_SUMMARY.json",
                    "IR1_CORE_CYCLES.jsonl")
    captured = {name: (AUTHOR/name).read_bytes() for name in source_names}
    identity_counts = symbolic_family_check()
    seed_counts, dispositions = Counter(), Counter()
    per_amplitude = defaultdict(Counter)
    discovered = {}
    max_steps = 0
    parameter_min = parameter_max = None
    seeds_seen = set()
    for amplitude, delta, a, initial in seed_stream():
        seed_key = amplitude, a, initial
        require(seed_key not in seeds_seen, "duplicate generated seed")
        seeds_seen.add(seed_key)
        orientation = "positive" if delta > 0 else "negative"
        seed_counts[orientation] += 1
        per_amplitude[amplitude]["seeds"] += 1
        parameter_min = a if parameter_min is None else min(a, parameter_min)
        parameter_max = a if parameter_max is None else max(a, parameter_max)
        kind, steps_taken, states = walk_backwards(amplitude, a, initial)
        dispositions[orientation+"_"+kind] += 1
        per_amplitude[amplitude][kind] += 1
        max_steps = max(max_steps, steps_taken)
        if kind == "return":
            key = a, min(states)
            if key in discovered:
                require(discovered[key] == states, "two cycles share a triple")
            discovered[key] = states
    require(sum(seed_counts.values()) == sum(dispositions.values()), "seed partition incomplete")
    words, labels, family_counts = {}, {}, Counter()
    output_rows = []
    self_reversing = 0
    for key, states in sorted(discovered.items()):
        a = key[0]
        word = native_word(a, states)
        words[key] = word
        label = generated_family_match(a, word)
        labels[key] = label
        family_counts[label] += 1
        reverse_states = word_states(a, tuple(reversed(word)))
        reverse_key = a, min(reverse_states)
        require(reverse_key in discovered, "missing opposite native orientation")
        require(discovered[reverse_key] == reverse_states, "opposite orientation states mismatch")
        self_reversing += reverse_key == key
        output_rows.append({"a": a, "least_period": len(word), "word": list(word),
                            "family": label, "least_native_triple": list(key[1])})
    compared = check_author_output(discovered, labels, captured["IR1_CORE_CYCLES.jsonl"])
    old_summary = json.loads(captured["IR1_CORE_SUMMARY.json"])
    require(seed_counts["positive"] == old_summary["all_counts"]["seeds"],
            "positive seed count differs from author")
    require(seed_counts["negative"] == seed_counts["positive"], "orientation seed asymmetry")
    require(family_counts == old_summary["family_cycle_counts_in_finite_certificate_only"],
            "family count comparison failed")
    require(compared == old_summary["distinct_oriented_cycles_in_completed_seed_output"],
            "author summary total mismatch")
    stable = {name: (AUTHOR/name).read_bytes() == content for name, content in captured.items()}
    require(all(stable.values()), "author inputs changed during independent reconstruction")
    raw_cycles = "".join(json.dumps(row, sort_keys=True, separators=(",", ":"))+"\n"
                         for row in output_rows)
    summary = {
        "status": "PASS_CONDITIONAL_ON_ANALYTIC_REDUCTION",
        "python": platform.python_version(),
        "amplitude_bound_from_proof": AMPLITUDE_BOUND,
        "parameter_cutoff": None, "period_cutoff": None,
        "search_direction": "inverse_map", "both_extremal_signs_enumerated": True,
        "seed_counts_by_sign": dict(seed_counts),
        "dispositions_by_sign": dict(sorted(dispositions.items())),
        "total_seeds": sum(seed_counts.values()),
        "discovered_oriented_cycles": len(discovered),
        "cycles_equal_to_their_reverse_up_to_rotation": self_reversing,
        "distinct_reverse_pairs": (len(discovered)-self_reversing)//2,
        "max_steps_observed_not_imposed": max_steps,
        "parameter_min_observed_not_imposed": parameter_min,
        "parameter_max_observed_not_imposed": parameter_max,
        "symbolic_recurrence_identities_checked": identity_counts,
        "family_counts": dict(sorted(family_counts.items())),
        "exceptions": [row for row in output_rows if row["family"] == "EXCEPTION"],
        "full_author_cycle_state_set_comparison": "PASS",
        "full_author_family_label_comparison": "PASS",
        "author_rows_individually_validated": compared,
        "per_amplitude": {str(d): dict(sorted(value.items()))
                          for d, value in sorted(per_amplitude.items())},
        "author_input_sha256": {name: sha256(value).hexdigest()
                                for name, value in captured.items()},
        "author_inputs_unchanged_during_run": stable,
        "independent_code_sha256": sha256(Path(__file__).read_bytes()).hexdigest(),
        "independent_cycles_sha256": sha256(raw_cycles.encode()).hexdigest(),
        "elapsed_seconds": round(monotonic()-started, 6),
    }
    (DESTINATION/"INDEPENDENT_CYCLES.jsonl").write_text(raw_cycles, encoding="utf-8")
    (DESTINATION/"INDEPENDENT_SUMMARY.json").write_text(
        json.dumps(summary, sort_keys=True, indent=2)+"\n", encoding="utf-8")
    compact = {key: value for key, value in summary.items() if key != "per_amplitude"}
    print(json.dumps(compact, sort_keys=True, indent=2))


if __name__ == "__main__":
    run()
