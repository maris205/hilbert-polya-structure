#!/usr/bin/env python3
"""Separate fixed-box MHT control; reuses only disclosed graph profiler."""
import json
import pilot


def rule(n):
    cube = range(1 << n)
    disjoint = [sum(1 << b for b in cube if not a & b) for a in cube]
    layers = [[a for a in cube if a.bit_count() == k] for k in range(n + 1)]

    def update(family):
        for layer in layers:
            feasible = [a for a in layer if not family & disjoint[a]]
            if feasible:
                return sum(1 << a for a in feasible)
        return 0

    return update


def main():
    profiles = []
    for n in range(5):
        profiles.append(pilot.analyze("MHT", {"ground_size": n},
                                      range(1 << (1 << n)), rule(n)))
    print(json.dumps({"status": "BOUNDED_REPLACEMENT_NOT_ADMISSION",
                      "boxes": len(profiles),
                      "states_across_boxes": sum(p["states"] for p in profiles),
                      "assertions": pilot.assertions,
                      "all_state_sha256": pilot.state_digest.hexdigest(),
                      "profiles": profiles}, sort_keys=True, indent=2))


if __name__ == "__main__":
    main()
