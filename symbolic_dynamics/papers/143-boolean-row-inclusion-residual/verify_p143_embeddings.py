#!/usr/bin/env python3
"""Independent induced-embedding/bijection controls for P143.

This lane deliberately does not import verify_p143.py and does not evaluate
the inclusion--exclusion formula.  It constructs labelled embedding maps,
expands them class by class to source matrices, and compares against direct
fibres through order four.  A second lane enumerates every labelled
four-element poset against a five-coordinate Boolean host.
"""

from collections import defaultdict
from itertools import product


ASSERTIONS = 0


def check(condition, message):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def matrix_rows(code, n):
    mask = (1 << n) - 1
    return tuple((code >> (n * i)) & mask for i in range(n))


def encode(row_tuple, n):
    return sum(row << (n * i) for i, row in enumerate(row_tuple))


def residual(row_tuple):
    target = []
    for left in row_tuple:
        row = 0
        for j, right in enumerate(row_tuple):
            if left & ~right == 0:
                row |= 1 << j
        target.append(row)
    return tuple(target)


def is_preorder(relation):
    n = len(relation)
    for i in range(n):
        if not (relation[i] >> i & 1):
            return False
        for j in range(n):
            if relation[i] >> j & 1 and relation[j] & ~relation[i]:
                return False
    return True


def is_poset(relation):
    if not is_preorder(relation):
        return False
    n = len(relation)
    return all(
        i == j or not (
            relation[i] >> j & 1 and relation[j] >> i & 1
        )
        for i in range(n) for j in range(n)
    )


def quotient_data(target):
    n = len(target)
    unused = set(range(n))
    classes = []
    while unused:
        i = min(unused)
        block = tuple(
            j for j in sorted(unused)
            if target[i] >> j & 1 and target[j] >> i & 1
        )
        classes.append(block)
        unused.difference_update(block)
    class_of = {}
    for q, block in enumerate(classes):
        for label in block:
            class_of[label] = q
    relation = tuple(
        sum(
            (target[left[0]] >> right[0] & 1) << r
            for r, right in enumerate(classes)
        )
        for left in classes
    )
    return tuple(classes), class_of, relation


def is_induced_map(values, relation):
    m = len(relation)
    return all(
        bool(relation[q] >> r & 1)
        == (values[q] & ~values[r] == 0)
        for q in range(m) for r in range(m)
    )


def embedding_sources(target):
    n = len(target)
    classes, class_of, relation = quotient_data(target)
    m = len(classes)
    sources = set()
    candidates = 0
    for values in product(range(1 << n), repeat=m):
        candidates += 1
        if not is_induced_map(values, relation):
            continue
        source_rows = tuple(values[class_of[label]] for label in range(n))
        source = encode(source_rows, n)
        check(residual(source_rows) == target,
              (n, target, values, "embedding-forward"))
        check(source not in sources,
              (n, target, values, "labelled-map-injectivity"))
        sources.add(source)
    return sources, candidates


def direct_bijection_lane():
    summaries = []
    total_candidates = 0
    total_fibre_states = 0
    for n in range(1, 5):
        direct = defaultdict(set)
        for source in range(1 << (n * n)):
            target = residual(matrix_rows(source, n))
            check(is_preorder(target), (n, source, "direct-image"))
            direct[target].add(source)
        for target, source_set in direct.items():
            embedded, candidates = embedding_sources(target)
            total_candidates += candidates
            total_fibre_states += len(source_set)
            check(embedded == source_set,
                  (n, target, len(embedded), len(source_set),
                   "embedding-fibre-bijection"))
        summaries.append((n, len(direct), 1 << (n * n),
                          sum(map(len, direct.values()))))
    return summaries, total_candidates, total_fibre_states


def upper_sets(relation):
    m = len(relation)
    return tuple(
        subset for subset in range(1 << m)
        if all(
            not (subset >> q & 1) or relation[q] & ~subset == 0
            for q in range(m)
        )
    )


def lifted_target(relation):
    blocks = ((0, 1), (2,), (3,), (4,))
    target = [0] * 5
    for q, left_block in enumerate(blocks):
        for r, right_block in enumerate(blocks):
            if relation[q] >> r & 1:
                for left in left_block:
                    for right in right_block:
                        target[left] |= 1 << right
    return tuple(target), blocks


def boolean_five_lane():
    posets = []
    for code in range(1 << 16):
        relation = matrix_rows(code, 4)
        if is_poset(relation):
            posets.append(relation)
    check(len(posets) == 219, ("four-poset-census", len(posets)))

    isotone_maps = 0
    induced_maps = 0
    min_induced = None
    max_induced = 0
    for relation in posets:
        upsets = upper_sets(relation)
        target, blocks = lifted_target(relation)
        local_induced = 0
        for coordinates in product(upsets, repeat=5):
            isotone_maps += 1
            values = tuple(
                sum((coordinates[c] >> q & 1) << c for c in range(5))
                for q in range(4)
            )
            check(all(
                not (relation[q] >> r & 1)
                or values[q] & ~values[r] == 0
                for q in range(4) for r in range(4)
            ), (relation, values, "preservation"))
            if not is_induced_map(values, relation):
                continue
            local_induced += 1
            induced_maps += 1
            source_rows = tuple(
                values[q] for q, block in enumerate(blocks) for _ in block
            )
            check(residual(source_rows) == target,
                  (relation, values, "B5-lift-forward"))
            check(source_rows[0] == source_rows[1],
                  (relation, values, "B5-class-equality"))
            recovered = tuple(source_rows[block[0]] for block in blocks)
            check(recovered == values,
                  (relation, values, "B5-labelled-map-recovery"))
        check(local_induced > 0, (relation, "B5-embeddability"))
        min_induced = (
            local_induced if min_induced is None
            else min(min_induced, local_induced)
        )
        max_induced = max(max_induced, local_induced)
    return len(posets), isotone_maps, induced_maps, min_induced, max_induced


def main():
    summaries, candidates, fibre_states = direct_bijection_lane()
    posets, isotone, induced, minimum, maximum = boolean_five_lane()
    print("P143 INDEPENDENT EMBEDDING CONTROL")
    print("columns=n,preorder_targets,direct_sources,bijection_sources")
    for n, targets, sources, bijection_sources in summaries:
        print(n, targets, sources, bijection_sources, sep=",")
    print(f"direct_embedding_candidates={candidates}")
    print(f"direct_fibre_states={fibre_states}")
    print(f"B5_labelled_posets={posets}")
    print(f"B5_isotone_maps={isotone}")
    print(f"B5_induced_maps={induced}")
    print(f"B5_min_induced={minimum}")
    print(f"B5_max_induced={maximum}")
    print(f"assertions={ASSERTIONS}")
    print("P143_EMBEDDING_BIJECTION_PASS")


if __name__ == "__main__":
    main()
