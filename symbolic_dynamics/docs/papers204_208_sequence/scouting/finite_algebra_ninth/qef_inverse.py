#!/usr/bin/env python3
"""Independent static inverse check within original QEF boxes only."""
from collections import Counter
from itertools import product
from hashlib import sha256
import json


checks = 0


def check(condition):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(checks)


def forward(source, p):
    x, y, z = source
    return ((x+y*z) % p, (y+x*z) % p, (z+x*y) % p)


def inverse(target, p):
    a, b, c = target
    answer = set()
    branches = []
    for z in range(p):
        determinant = (1-z*z) % p
        if determinant:
            factor = pow(determinant, -1, p)
            x = (a-z*b)*factor % p
            y = (b-z*a)*factor % p
            if (z+x*y-c) % p == 0:
                answer.add((x, y, z))
                branches.append((z, 1))
        elif (b-z*a) % p == 0:
            count = 0
            for x in range(p):
                y = z*(a-x) % p
                if (z+x*y-c) % p == 0:
                    answer.add((x, y, z))
                    count += 1
            branches.append((z, count))
    return answer, branches


records = []
for p in (2, 3, 5, 7, 11, 13):
    states = list(product(range(p), repeat=3))
    predecessor = {target: set() for target in states}
    for source in states:
        target = forward(source, p)
        predecessor[target].add(source)
        a, b, c = target
        x, y, z = source
        check(((c-z)*(1-z*z)**2-(a-z*b)*(b-z*a)) % p == 0)
        check((target == source) == (sum(v != 0 for v in source) <= 1))
    bound = 3 if p == 2 else 5
    sizes = Counter()
    branch_records = []
    maximizing = []
    for target in states:
        decoded, branches = inverse(target, p)
        check(decoded == predecessor[target])
        check(len(decoded) <= bound)
        for z, count in branches:
            if (1-z*z) % p == 0 and p != 2:
                check(count <= 2)
        sizes[len(decoded)] += 1
        if len(decoded) == bound:
            maximizing.append(target)
        branch_records.append((target, branches, sorted(decoded)))
    check(bool(maximizing))
    if p != 2:
        expected = {(0, 0, 0)} | {
            (x, y, z) for x, y, z in product((1, p-1), repeat=3)
            if x*y*z % p == p-1}
        check(predecessor[(0, 0, 0)] == expected)
        check(len(expected) == 5)
    else:
        check(predecessor[(1, 1, 1)] == {(0, 1, 1), (1, 0, 1), (1, 1, 0)})
    witness = (1, 0, 0)
    old_lv = tuple(witness[i]*(witness[(i+1)%3]-witness[(i-1)%3]) % p
                   for i in range(3))
    check(old_lv == (0, 0, 0) and forward(witness, p) == witness)
    raw = json.dumps(branch_records, separators=(",", ":")).encode()
    records.append({"p": p, "sources": len(states), "targets": len(states),
                    "maximum_fibre": bound, "all_maximizing_targets": maximizing,
                    "fibre_histogram": sorted(sizes.items()),
                    "zero_predecessors": sorted(predecessor[(0, 0, 0)]),
                    "all_branch_predecessor_records_sha256": sha256(raw).hexdigest(),
                    "correct_old_LV_witness": {"source": witness, "old": old_lv,
                                               "QEF": witness}})
print(json.dumps({"schema": "qef-static-inverse-check-v1", "checks": checks,
                  "sources": sum(r["sources"] for r in records),
                  "records": records, "status": "PASS_STATIC_ONLY_NO_TEMPORAL_CLAIM"},
                 sort_keys=True, indent=2))
