#!/usr/bin/env python3
"""Process-separated Review-A falsifier for P193.

This file intentionally imports no paper-local code.  It builds the literal
mutual-nomination map, the prefix-sum component model, the complete functional
graph, the target fibres, and the depth series independently.
"""

from collections import Counter
from hashlib import sha256
from itertools import permutations
from math import factorial
from pathlib import Path


CHECKS = 0


def check(statement, message):
    global CHECKS
    CHECKS += 1
    if not statement:
        raise AssertionError(message)


def intervals(word):
    """Direct-sum blocks detected by the extremal prefix-sum criterion."""
    cuts = []
    total = 0
    for r, value in enumerate(word, 1):
        total += value
        if total == r * (r + 1) // 2:
            cuts.append(r)
    left = 0
    answer = []
    for right in cuts:
        answer.append((left, right))
        left = right
    return tuple(answer)


def sizes(word):
    return tuple(right - left for left, right in intervals(word))


def literal_pairs(word):
    chosen = []
    n = len(word)
    for i in range(n):
        smaller = [word[k] for k in range(i + 1, n) if word[k] < word[i]]
        if not smaller:
            continue
        nominated_value = min(smaller)
        j = word.index(nominated_value)
        earlier_larger = [k for k in range(j) if word[k] > word[j]]
        if earlier_larger and min(earlier_larger) == i:
            chosen.append((i, j))
    flat = [v for edge in chosen for v in edge]
    check(len(flat) == len(set(flat)), "literal active pairs overlap")
    return tuple(chosen)


def surgery_pairs(word):
    chosen = []
    for left, right in intervals(word):
        if right - left > 1:
            j = min(range(left, right), key=lambda p: word[p])
            chosen.append((left, j))
    return tuple(chosen)


def exchange(word, chosen):
    out = list(word)
    for i, j in chosen:
        out[i], out[j] = out[j], out[i]
    return tuple(out)


def update(word):
    return exchange(word, literal_pairs(word))


def tail(word):
    goal = tuple(range(1, len(word) + 1))
    seen = set()
    state = word
    steps = 0
    while state != goal:
        check(state not in seen, "nontrivial cycle")
        seen.add(state)
        state = update(state)
        steps += 1
        check(steps <= len(word) - 1, "tail exceeds theorem bound")
    return steps


def fibre_claim(target):
    c = sizes(target)
    if c[0] != 1:
        return 0
    value = c[-1]
    for j in range(1, len(c)):
        if c[j] == 1:
            value *= 1 + c[j - 1]
    return value


def sequence_inverse(block, degree):
    out = [0] * (degree + 1)
    out[0] = 1
    for d in range(1, degree + 1):
        out[d] = sum(block[j] * out[d - j] for j in range(1, d + 1))
    return out


def refine_blocks(all_series, block_series, degree):
    nxt = [0] * (degree + 1)
    nxt[1] = 1
    for d in range(2, degree + 1):
        nxt[d] = sum(
            all_series[u] * (d - 1 - u) * block_series[d - 1 - u]
            for u in range(d - 1)
        )
    return nxt


def main():
    max_n = 8
    workspace = Path(__file__).resolve().parents[4]
    paper = workspace / "papers/193-mutual-best-block-refinement"
    manuscript = (paper / "main.tex").read_text(encoding="utf-8")
    bibliography = (paper / "references.bib").read_text(encoding="utf-8")
    source_ledger = (paper / "SOURCE_VERIFICATION.md").read_text(encoding="utf-8")
    check("SchipperZhang2025" in manuscript, "P193-A1 citation not installed")
    check("2504.01280" in bibliography, "P193-A1 arXiv record not installed")
    check("2504.01280" in source_ledger, "P193-A1 source ledger not installed")
    check("sequential or stochastic" in manuscript,
          "P193-A1 process distinction not installed")
    check("OWNER\\_AMBER/HOLD\\_EXTERNAL" in manuscript,
          "P193 release gate missing")
    digest = sha256()
    rows = []
    depth_tables = {}
    indecomposable_tables = {}
    transitions = 0

    for n in range(1, max_n + 1):
        states = tuple(permutations(range(1, n + 1)))
        fibres = Counter()
        depths = Counter()
        indecomposable_depths = Counter()
        for source in states:
            raw_pairs = literal_pairs(source)
            structural_pairs = surgery_pairs(source)
            check(raw_pairs == structural_pairs, f"block surgery fails on {source}")
            target = exchange(source, raw_pairs)
            transitions += 1
            fibres[target] += 1
            digest.update(f"{n}:{source}>{target}\n".encode("ascii"))
            if source != target:
                check(len(intervals(target)) > len(intervals(source)),
                      f"component Lyapunov failure on {source}")
            else:
                check(source == tuple(range(1, n + 1)), "extra fixed point")
            d = tail(source)
            depths[d] += 1
            if len(intervals(source)) == 1:
                indecomposable_depths[d] += 1

        check(max(depths) == n - 1, f"wrong maximum tail at n={n}")
        check(depths[n - 1] == factorial(n - 1),
              f"wrong deepest count at n={n}")
        for target in states:
            predicted = fibre_claim(target)
            check(fibres[target] == predicted, f"fibre failure on {target}")
            check((fibres[target] > 0) == (target[0] == 1),
                  f"image criterion failure on {target}")
        check(sum(fibres.values()) == factorial(n), f"mass failure at n={n}")
        image = sum(value > 0 for value in fibres.values())
        check(image == factorial(n - 1), f"image size failure at n={n}")
        maximum = max(fibres.values())
        maximizers = [x for x in states if fibres[x] == maximum]
        check(maximum == 2 ** (n - 1), f"max fibre failure at n={n}")
        check(maximizers == [tuple(range(1, n + 1))],
              f"nonunique max fibre at n={n}")
        depth_tables[n] = depths
        indecomposable_tables[n] = indecomposable_depths
        hist = ",".join(f"{d}:{depths[d]}" for d in sorted(depths))
        rows.append((n, len(states), image, n - 1, depths[n - 1], maximum, hist))

    block = [0] * (max_n + 1)
    block[1] = 1
    for epoch in range(max_n):
        all_objects = sequence_inverse(block, max_n)
        for n in range(1, max_n + 1):
            actual_all = sum(v for d, v in depth_tables[n].items() if d <= epoch)
            actual_block = sum(v for d, v in indecomposable_tables[n].items()
                               if d <= epoch)
            check(all_objects[n] == actual_all,
                  f"A-series failure at t={epoch}, n={n}")
            check(block[n] == actual_block,
                  f"B-series failure at t={epoch}, n={n}")
        block = refine_blocks(all_objects, block, max_n)

    print("P193 hostile Review-A independent control")
    for n, states, image, mt, deepest, mf, hist in rows:
        print(f"n={n} states={states} image={image} max_tail={mt} "
              f"deepest={deepest} max_fibre={mf} depth_hist={hist}")
    print(f"complete_range=1..{max_n}")
    print(f"transitions={transitions}")
    print(f"checks={CHECKS}")
    print(f"transition_digest={digest.hexdigest()}")
    print("imports_author_code=false")
    print("owner_state=OWNER_AMBER/HOLD_EXTERNAL")
    print("historical_findings_closed=P193-A1")
    print("open_findings=critical:0,major:0,minor:0")
    print("review_decision=PASS")
    print("status=PASS")


if __name__ == "__main__":
    main()
