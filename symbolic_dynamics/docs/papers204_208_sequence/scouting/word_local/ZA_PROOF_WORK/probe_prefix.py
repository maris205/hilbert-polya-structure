#!/usr/bin/env python3
"""Independent Z literal and exact coupling falsification; no root imports."""
from itertools import product
import json


def zstep(x):
    return (0,) + tuple(max(k for k in range(len(x)-i+1) if x[:k] == x[i:i+k])
                        for i in range(1, len(x)))


def main():
    rows = []
    for n in range(2, 9):
        states = tuple((0,)+x for x in product(*(range(n-i+1) for i in range(1, n))))
        image = set(map(zstep, states))
        for space, carrier in (("ambient", states), ("valid_image", tuple(sorted(image)))):
            for rounds in (1, 2, 3, 4):
                keys = {}
                witness = None
                violations = 0
                for x in carrier:
                    target = x
                    for _ in range(rounds):
                        target = zstep(target)
                    mask = tuple(a == 0 for a in x)
                    for i in range(1, n):
                        key = mask, x[:i], i
                        value = target[i]
                        if key in keys and keys[key][0] != value:
                            violations += 1
                            if witness is None:
                                witness = {"x": keys[key][1], "y": x, "coordinate": i,
                                           "Tx_coordinate": keys[key][0], "Ty_coordinate": value}
                        else:
                            keys[key] = value, x
                rows.append({"n": n, "space": space, "size": len(carrier),
                             "rounds": rounds, "strict_prefix_coupling_violations": violations,
                             "first_witness": witness})
    print(json.dumps({"claim_tested": "same zero mask and agreement before i forces agreement at i after k rounds",
                      "rows": rows}, indent=2))


if __name__ == "__main__":
    main()
