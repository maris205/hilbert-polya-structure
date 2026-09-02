#!/usr/bin/env python3
"""Independent exact symbolic identities for HCS-C292."""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "results/c292_sticky_evidence.json"


def R(value: str) -> sp.Rational:
    return sp.Rational(value)


def main() -> None:
    data = json.loads(DATA.read_text())
    checks = 0
    for event in data["event_cells"]:
        event_loss = sp.Rational(0)
        for group in event["groups"]:
            m = [R(z) for z in group["incoming_masses"]]
            v = [R(z) for z in group["incoming_velocities"]]
            M = sum(m)
            P = sum(mi * vi for mi, vi in zip(m, v))
            before = sum(mi * vi**2 / 2 for mi, vi in zip(m, v))
            after = P**2 / (2 * M)
            pair = sum(m[i] * m[j] * (v[i] - v[j])**2 for i in range(len(m)) for j in range(i + 1, len(m))) / (2 * M)
            identities = [
                M == R(group["mass"]), P == R(group["momentum"]),
                P / M == R(group["outgoing_velocity"]),
                before == R(group["energy_before"]), after == R(group["energy_after"]),
                before - after == pair == R(group["energy_loss"]), pair >= 0,
            ]
            if not all(identities):
                raise AssertionError((event["scenario"], event["event_index"], group))
            checks += len(identities)
            event_loss += pair
        if event_loss != R(event["total_energy_loss"]):
            raise AssertionError("event loss sum")
        checks += 1

    for cell in data["conservation_cells"]:
        if R(cell["final_energy"]) + R(cell["total_energy_loss"]) != R(cell["initial_energy"]):
            raise AssertionError("energy telescope")
        if R(cell["center_velocity"]) * R(cell["total_mass"]) != R(cell["total_momentum"]):
            raise AssertionError("center velocity")
        checks += 2

    by_query: dict[tuple[str, str], list[dict]] = {}
    for row in data["projection_cells"]:
        by_query.setdefault((row["scenario"], row["time"]), []).append(row)
    for _, rows in by_query.items():
        rows.sort(key=lambda row: row["canonical_index"])
        positions = [R(row["position"]) for row in rows]
        if any(a > b for a, b in zip(positions, positions[1:])):
            raise AssertionError("isotonic ordering")
        checks += max(1, len(positions) - 1)
        for members, group in __import__("itertools").groupby(rows, key=lambda row: tuple(row["cluster_members"])):
            block = list(group)
            if [row["canonical_index"] for row in block] != list(members):
                raise AssertionError("contiguous block")
            if len({row["position"] for row in block}) != 1 or len({row["velocity"] for row in block}) != 1:
                raise AssertionError("block constants")
            checks += 2

    for row in data["weak_balance_cells"]:
        if R(row["mass_jump"]) != 0 or R(row["momentum_jump"]) != 0 or R(row["energy_entropy_defect"]) > 0:
            raise AssertionError("weak event balance")
        checks += 3
    print(f"C292_SYMPY_PASS ({checks} symbolic identities)")


if __name__ == "__main__":
    main()
