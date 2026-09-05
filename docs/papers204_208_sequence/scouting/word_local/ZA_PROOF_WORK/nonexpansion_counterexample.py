#!/usr/bin/env python3
"""Find and shrink an exact valid-array counterexample; no root imports."""
from random import Random
import json
from probe_complete_valid import zscan


def failure(a, b):
    x, y = zscan(a), zscan(b)
    if x == y or tuple(t == 0 for t in x) != tuple(t == 0 for t in y):
        return None
    d = next(i for i in range(len(x)) if x[i] != y[i])
    gx, gy = zscan(zscan(x)), zscan(zscan(y))
    if gx[:d] == gy[:d]:
        return None
    e = next(i for i in range(len(x)) if gx[i] != gy[i])
    return {"x": x, "y": y, "Gx": gx, "Gy": gy,
            "first_input_difference": d, "first_output_difference": e}


def right_recode(word):
    labels = sorted(set(word)-{word[0]}, key=lambda a: max(i for i, b in enumerate(word) if b == a), reverse=True)
    code = {word[0]: 0, **{a: i+1 for i, a in enumerate(labels)}}
    return tuple(code[a] for a in word)


def main():
    rng = Random(204208)
    found = None
    for trial in range(4000):
        n = 16
        a = (0,)+tuple(rng.randrange(3) for _ in range(n-1))
        i = rng.randrange(1, n)
        if a[i] == 0:
            continue
        b = a[:i]+(3-a[i],)+a[i+1:]
        if failure(a, b) is not None:
            found = a, b
            break
    assert found is not None
    original = {"trial": trial, "a": found[0], "b": found[1], **failure(*found)}
    a, b = found
    deletions = []
    changed = True
    while changed:
        changed = False
        for i in range(len(a)-1, 0, -1):
            aa, bb = a[:i]+a[i+1:], b[:i]+b[i+1:]
            if failure(aa, bb) is not None:
                deletions.append({"old_n": len(a), "deleted_index": i})
                a, b, changed = aa, bb, True
                break
    aa, bb = right_recode(a), right_recode(b)
    for word in (aa, bb):
        assert word[0] == 0
        assert all(0 <= word[i] <= len(word)-i for i in range(1, len(word)))
    assert zscan(a) == zscan(aa) and zscan(b) == zscan(bb)
    result = {"original": original, "greedy_deletions": deletions,
              "deletion_minimal_not_global_minimal": True,
              "bounded_source_a": aa, "bounded_source_b": bb,
              "final": failure(aa, bb)}
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
