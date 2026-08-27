#!/usr/bin/env python3
"""Hostile repaired-hash and stale-hash mutations for C189."""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c189_ws_evidence.json"
CHECKER = ROOT / "code/c189_ws_checker.py"


def canonical_hash(data: dict) -> str:
    body = deepcopy(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def rejected(data: dict) -> bool:
    handle = tempfile.NamedTemporaryFile("w", suffix=".json", prefix="c189_mutation_", delete=False)
    path = Path(handle.name)
    try:
        json.dump(data, handle, sort_keys=True, indent=2, ensure_ascii=False)
        handle.write("\n")
        handle.close()
        run = subprocess.run(["python3", str(CHECKER), str(path)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return run.returncode != 0
    finally:
        path.unlink(missing_ok=True)


def main() -> None:
    original = json.loads(EVIDENCE.read_text())
    mutations: list[tuple[str, dict]] = []

    def add(name, change) -> None:
        data = deepcopy(original)
        change(data)
        data["payload_sha256"] = canonical_hash(data)
        mutations.append((name, data))

    add("scope", lambda d: d["metadata"].__setitem__("scope_literal", "BROKEN"))
    add("source", lambda d: d["metadata"]["primary_sources"][0].__setitem__("doi", "broken"))
    add("local_frequency", lambda d: d["local_riccati_rows"][0].__setitem__("frequency_f", "0/1"))
    add("local_forcing", lambda d: d["local_riccati_rows"][1].__setitem__("forcing_H", ["9/1", "0/1"]))
    add("local_point", lambda d: d["local_riccati_rows"][2].__setitem__("circle_point_z", ["0/1", "0/1"]))
    add("phase_velocity", lambda d: d["local_riccati_rows"][3].__setitem__("phase_velocity", "99/1"))
    add("riccati_velocity", lambda d: d["local_riccati_rows"][4].__setitem__("riccati_velocity", ["0/1", "0/1"]))
    add("tangent", lambda d: d["local_riccati_rows"][5].__setitem__("circle_tangent_residual", "1/1"))
    add("alpha", lambda d: d["mobius_action_rows"][0].__setitem__("alpha", ["1/1", "0/1"]))
    add("rotation", lambda d: d["mobius_action_rows"][1].__setitem__("rotation", ["0/1", "0/1"]))
    add("coefficient", lambda d: d["mobius_action_rows"][2]["projective_coefficients_a_b_c_d"].__setitem__(0, ["0/1", "0/1"]))
    add("image", lambda d: d["mobius_action_rows"][3]["image_points"].__setitem__(0, ["0/1", "0/1"]))
    add("circle_residual", lambda d: d["mobius_action_rows"][4]["image_circle_residuals"].__setitem__(0, "1/1"))
    add("partition", lambda d: d["mobius_action_rows"][28].__setitem__("image_collision_partition", [7, 1]))
    add("orbit_dimension", lambda d: d["mobius_action_rows"][7].__setitem__("group_orbit_dimension", 3))
    add("quotient_count", lambda d: d["mobius_action_rows"][6].__setitem__("quotient_invariant_count", 99))
    add("cross_ratio", lambda d: d["mobius_action_rows"][0]["cross_ratio_invariants"][0].__setitem__("image_value", "0/1"))
    add("reconstruction", lambda d: d["mobius_action_rows"][0].__setitem__("three_landmark_reconstruction", False))
    add("constant_delta", lambda d: d["constant_generator_rows"][1].__setitem__("delta_equals_omega2_minus_absH2", "0/1"))
    add("constant_class", lambda d: d["constant_generator_rows"][1].__setitem__("classification", "hyperbolic"))
    add("fixed_root", lambda d: d["constant_generator_rows"][1]["fixed_roots"][0].__setitem__("z", ["1/1", "0/1"]))
    add("period_factor", lambda d: d["constant_generator_rows"][1].__setitem__("elliptic_projective_period_pi_coefficient", "1/1"))
    add("route", lambda d: d["route_a"].__setitem__("A4", "A4_NATURAL_QUANTIZATION"))
    add("summary", lambda d: d["summary"].__setitem__("cross_ratio_cells", 0))

    failed = [name for name, data in mutations if not rejected(data)]
    stale = deepcopy(original)
    stale["mobius_action_rows"][0]["distinct_clusters"] = 99
    stale_rejected = rejected(stale)
    if failed or not stale_rejected:
        raise AssertionError({"unrejected_repaired_hash": failed, "stale_hash_rejected": stale_rejected})
    print(json.dumps({
        "status": "C189_MUTATION_PASS",
        "repaired_hash_rejections": len(mutations),
        "stale_hash_rejections": 1,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
