#!/usr/bin/env python3
"""Author's standalone LNR temporal check; no I/O or imported task code."""
from collections import Counter
from hashlib import sha256
from itertools import product
import json


checks = Counter()


def require(test, kind, witness=None):
    checks[kind] += 1
    if not test:
        raise AssertionError((kind, witness))


def step(x):
    n = len(x)
    return tuple(int(x[(i - 1) % n] < a) + int(x[(i + 1) % n] < a)
                 for i, a in enumerate(x))


def fixed_language(x):
    if not any(x):
        return True
    if 0 not in x:
        return False
    allowed = {(2,), (1, 1), (1, 2), (2, 1), (1, 2, 1)}
    origin = x.index(0)
    run = []
    for offset in range(1, len(x) + 1):
        a = x[(origin + offset) % len(x)]
        if a:
            run.append(a)
        elif run:
            if tuple(run) not in allowed:
                return False
            run = []
    return not run


def run_projection(y):
    """Two further steps from an image, computed by the proved run cases."""
    n = len(y)
    out = list(y)
    anchor = next(i for i, a in enumerate(y) if a != 1)
    cursor = anchor + 1
    stop = anchor + n
    while cursor < stop:
        if y[cursor % n] != 1:
            cursor += 1
            continue
        begin = cursor
        while cursor < stop and y[cursor % n] == 1:
            cursor += 1
        length = cursor - begin
        left, right = y[(begin - 1) % n], y[cursor % n]
        if length == 1:
            out[begin % n] = 2 if left == right == 0 else 0 if left == right == 2 else 1
        elif length == 2 and left == right == 0:
            out[begin % n] = out[(begin + 1) % n] = 1
        else:
            for j in range(begin, cursor):
                out[j % n] = 0
            if left == 0:
                out[begin % n] = 2
            if right == 0:
                out[(cursor - 1) % n] = 2
    return tuple(out)


def main():
    boxes = []
    for n in range(3, 11):
        histogram, digest = Counter(), sha256()
        image, fixed = set(), set()
        for x in product(range(3), repeat=n):
            y = step(x)
            image.add(y)
            require(all(not (y[i] == y[(i + 1) % n] == 2) for i in range(n)), "no_image_22")
            require(y != (1,) * n, "no_all_one_image")
            z = step(y)
            end = step(z)
            require(step(end) == end, "F4_equals_F3")
            require(run_projection(y) == end, "complete_run_endpoint")
            require(fixed_language(x) == (x == y), "exact_fixed_language")
            if x == y:
                fixed.add(x)
            depth = 0 if x == y else 1 if y == z else 2 if z == end else 3
            histogram[depth] += 1
            require(depth <= (1 if n == 3 else 3), "sharp_height_upper")
            for i in range(n):
                if y[i] in (0, 2):
                    require(z[i] == end[i] == y[i], "permanent_image_symbols")
            digest.update((json.dumps([x, y, end, depth], separators=(",", ":")) + "\n").encode())
        require(max(histogram) == (1 if n == 3 else 3), "attained_box_height")
        boxes.append({"n": n, "states": 3 ** n, "image_size": len(image),
                      "fixed_size": len(fixed), "depth_histogram": dict(sorted(histogram.items())),
                      "ordered_temporal_record_sha256": digest.hexdigest()})
    sharp = sha256()
    for n in range(4, 1001):
        x = (0,) * (n - 3) + (1, 2, 2)
        expected = [(0,) * (n - 3) + s for s in ((1, 1, 1), (1, 0, 1), (2, 0, 2))]
        current = x
        for target in expected:
            current = step(current)
            require(current == target, "all_length_family_step")
        require(step(current) == current, "all_length_family_fixed")
        sharp.update(f"{n}:{''.join(map(str, current))}\n".encode())
    print(json.dumps({"status": "AUTHOR_FINITE_CHECKS_NOT_ALL_PARAMETER_PROOF",
                      "map": "ternary cyclic strict lower-neighbor count, n>=3",
                      "boxes": boxes, "witness_n": [4, 1000],
                      "witness_sha256": sharp.hexdigest(),
                      "assertions": dict(sorted(checks.items())),
                      "total_assertions": sum(checks.values())}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
