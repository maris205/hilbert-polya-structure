#!/usr/bin/env python3
"""Author adapter audit: independent UPC representation; fixed original boxes."""
from collections import Counter
from hashlib import sha256
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent
checks = 0
digest = sha256()


def require(value):
    global checks
    checks += 1
    if not value:
        raise AssertionError(checks)


def submasks(mask):
    part = mask
    while True:
        yield part
        if not part:
            return
        part = (part - 1) & mask


def run(n):
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    count = 1 << len(edges)

    def encode(pairs):
        return sum(1 << k for k, pair in enumerate(edges) if pair in pairs)

    def paths(mask):
        # Exact integer path counts, no saturation and no pilot import.
        result = {}
        for length in range(1, n):
            for i in range(n - length):
                j = i + length
                result[i, j] = int(bool(mask & (1 << edges.index((i, j)))))
                result[i, j] += sum(result[i, k] for k in range(i + 1, j)
                                    if mask & (1 << edges.index((k, j))))
        return result

    closure = []
    forward = []
    for source in range(count):
        table = paths(source)
        closure.append(encode({e for e, multiplicity in table.items() if multiplicity}))
        forward.append(encode({e for e, multiplicity in table.items() if multiplicity == 1}))

    frames = {}

    def frame(pmask):
        if pmask in frames:
            return frames[pmask]
        relation = {e for k, e in enumerate(edges) if pmask & (1 << k)}
        covers = {e for e in relation
                  if not any((e[0], k) in relation and (k, e[1]) in relation
                             for k in range(e[0] + 1, e[1]))}
        intervals = {}
        for i, j in relation - covers:
            interval = {i, j} | {k for k in range(i + 1, j)
                                if (i, k) in relation and (k, j) in relation}
            if all((a, b) in relation for a in interval for b in interval if a < b):
                intervals[i, j] = interval
        qmask = encode(set(intervals))
        bmask = pmask & ~(encode(covers) | qmask)
        down = {edges.index(q): encode({r for r in intervals
                                       if set(r) <= interval})
                for q, interval in intervals.items()}
        minimum = sum(1 << q for q, below in down.items() if below == 1 << q)
        result = (encode(covers), qmask, bmask, down, minimum)
        frames[pmask] = result
        return result

    def complement_up(source, down):
        return sum(1 << q for q, below in down.items() if not source & below)

    inverse_counts = Counter(forward)
    decoded = set()
    for source in range(count):
        cover, qmask, branch, down, minimum = frame(closure[source])
        target = forward[source]
        require(source & cover == cover)
        require(closure[target] == closure[source])
        require(target == cover | complement_up(source & qmask, down))
        second = forward[target]
        fourth = forward[forward[second]]
        require(second == fourth)
        kernel = sum(1 << q for q, below in down.items()
                     if (below & minimum) & ~source == 0)
        require(second == cover | kernel)
        digest.update(f"{n}:{source}:{target}:{second}\n".encode())

    for target in range(count):
        cover, qmask, branch, down, minimum = frame(closure[target])
        tmask = target & qmask
        valid = not target & branch and all(tmask & below == below
                                           for q, below in down.items() if tmask & (1 << q))
        if not valid:
            require(inverse_counts[target] == 0)
            continue
        dmask = qmask & ~tmask
        mandatory = sum(1 << q for q, below in down.items()
                        if dmask & (1 << q) and (below & dmask) == 1 << q)
        free = branch | (dmask & ~mandatory)
        predicted = 1 << free.bit_count()
        require(inverse_counts[target] == predicted)
        fibre = []
        for choice in submasks(free):
            source = cover | mandatory | choice
            require(forward[source] == target)
            require(source not in decoded)
            decoded.add(source)
            fibre.append(source)
        require(len(fibre) == predicted)
    require(len(decoded) == count)

    recurrent = sum(forward[forward[s]] == s for s in range(count))
    fixed = sum(forward[s] == s for s in range(count))
    predicted_core = sum(1 << data[4].bit_count() for data in frames.values())
    require(recurrent == predicted_core)
    profile = {"vertices": n, "states": count, "image": len(inverse_counts),
               "recurrent": recurrent, "fixed": fixed,
               "maximum_fibre": max(inverse_counts.values()),
               "closure_strata": len(frames)}
    baseline = next(p for p in json.loads((HERE / "CANONICAL.json").read_text())["profiles"]
                    if p["rule"] == "UPC" and p["parameter"] == {"vertices": n})
    for name in ("states", "image", "recurrent", "maximum_fibre"):
        require(profile[name] == baseline[name])
    return profile


def main():
    profiles = [run(n) for n in range(7)]
    print(json.dumps({"status": "AUTHOR_ADAPTER_AUDIT_PASS_NOT_INDEPENDENT_REVIEW",
                      "assertions": checks, "boxes": len(profiles),
                      "states_across_boxes": sum(p["states"] for p in profiles),
                      "all_state_sha256": digest.hexdigest(), "profiles": profiles},
                     sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
