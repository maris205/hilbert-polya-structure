#!/usr/bin/env python3
"""Independent arithmetic/structure checker for the CAPD local-slab smoke.

This checker deliberately does not import the production Python package or
rerun the CAPD flow.  It reconstructs the exact algebraic constants, parses
the two raw MPFR transcripts, recomputes all Krawczyk inclusion margins, and
verifies the frozen hashes.  A later full proof checker must additionally
replay the archived Taylor/Lohner flow objects.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from decimal import Decimal, getcontext
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "research/route_a_wave_trace/R401_VALIDATED_THEOREM_DOMAIN_PROTOCOL.md":
        "d00d95f32ddfe4420da2cdac46ef1a3bb39bb3ea2277a21a9776652794a20d82",
    "research/route_a_wave_trace/R401_VAL_PROTOCOL_AMENDMENT_V2.md":
        "a163be8800ecc1677ccaf2f6342becfe834d55d80ad59dcc24180e3f0f5e62aa",
    "research/route_a_wave_trace/A411_RADIAL_PERIOD_BOUND.md":
        "b991cf5ffce043db60ceaf2448f383364c66dca66812180fb996c19debcd11bb",
    "research/route_a_wave_trace/A411_WARPED_PERIOD_FLOOR.md":
        "71cc840cd6518ecb4672402fbe2517ae5096bb654872abce32ef21d02a7e26d8",
    "validated/capd_r401_local_slab_mp.cpp":
        "663287f629457d81f716a1a56a032c660bd91a79a1ae7aa77bc980483819c929",
}
EXPECTED_CAPD_COMMIT = "731079217a9254ea2948d742df2b170895effe7f"
NUMBER = r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?"
INTERVAL_PATTERN = re.compile(rf"\[\s*({NUMBER})\s*,\s*({NUMBER})\s*\]")


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_values(raw: str) -> dict[str, str]:
    values: dict[str, str] = {}
    for line in raw.splitlines():
        if "=" in line and not line.startswith("{"):
            key, value = line.split("=", 1)
            values[key] = value
    return values


def intervals(text: str) -> list[tuple[Decimal, Decimal]]:
    return [
        (Decimal(match.group(1)), Decimal(match.group(2)))
        for match in INTERVAL_PATTERN.finditer(text)
    ]


def contains(interval: tuple[Decimal, Decimal], value: Decimal) -> bool:
    return interval[0] <= value <= interval[1]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--result",
        type=Path,
        default=ROOT / "results/r401_val_local_slab_smoke",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    result = args.result.resolve()
    summary = json.loads((result / "summary.json").read_text(encoding="utf-8"))
    manifest = json.loads((result / "manifest.json").read_text(encoding="utf-8"))
    checks: dict[str, bool] = {}

    for relative, expected in EXPECTED.items():
        checks[f"frozen_hash:{relative}"] = sha256(ROOT / relative) == expected
    checks["protocol_id"] = summary.get("protocol_id") == "R401-VAL-V2"
    checks["milestone_not_final"] = (
        summary.get("milestone_status") == "PASS_LOCAL_SLAB_SMOKE"
        and summary.get("final_status") is None
    )
    checks["capd_commit"] = (
        summary.get("environment", {}).get("capd_commit") == EXPECTED_CAPD_COMMIT
        and manifest.get("capd_commit") == EXPECTED_CAPD_COMMIT
    )
    flags = set(summary.get("environment", {}).get("capd_config_flags", []))
    checks["mpfr_build_flags"] = {
        "-D__HAVE_MPFR__",
        "-lmpfr",
        "-lgmp",
        "-frounding-math",
    }.issubset(flags)

    for stored_path, stored_hash in manifest.get("files", {}).items():
        path = Path(stored_path)
        if not path.is_absolute():
            path = ROOT / path
        checks[f"manifest_hash:{stored_path}"] = (
            path.is_file() and sha256(path) == stored_hash
        )

    getcontext().prec = 110
    a_exact = Decimal(51) / Decimal(50)
    c_exact = Decimal(2) * ((Decimal(1) + a_exact).sqrt() - Decimal(1))
    discriminant = c_exact * (c_exact * c_exact + Decimal(4)).sqrt()
    lambda_slow = (c_exact * c_exact + Decimal(2) - discriminant) / Decimal(2)
    lambda_fast = (c_exact * c_exact + Decimal(2) + discriminant) / Decimal(2)
    slow_raw = (Decimal(1) - lambda_slow, -c_exact)
    fast_raw = (lambda_fast - Decimal(1), c_exact)
    slow_norm = (slow_raw[0] ** 2 + slow_raw[1] ** 2).sqrt()
    fast_norm = (fast_raw[0] ** 2 + fast_raw[1] ** 2).sqrt()
    e_slow = (slow_raw[0] / slow_norm, slow_raw[1] / slow_norm)
    e_fast = (fast_raw[0] / fast_norm, fast_raw[1] / fast_norm)

    root_centers = (
        Decimal("-0.002217614251311155746359014235924058"),
        Decimal("0.148503551176855185013286874895890763"),
        Decimal(0),
        Decimal("0.663569791793793062672019028284358387"),
    )
    root_radii = (
        Decimal("0.00004"),
        Decimal("0.00002"),
        Decimal("0.00008"),
        Decimal("0.00002"),
    )

    parsed_runs: dict[int, dict[str, object]] = {}
    for bits in (128, 256):
        raw = (result / f"capd_{bits}.txt").read_text(encoding="utf-8")
        values = parse_values(raw)
        prefix = f"p{bits}:"
        checks[prefix + "status"] = values.get("status") == "PASS_LOCAL_SLAB_SMOKE"
        checks[prefix + "precision"] = values.get("precision_bits") == str(bits)
        checks[prefix + "subset_flag"] = values.get("subset_interior") == "1"

        epsilon = intervals(values.get("epsilon", ""))
        x_box = intervals(values.get("X", ""))
        k_box = intervals(values.get("K", ""))
        left = intervals(values.get("left_margin", ""))
        right = intervals(values.get("right_margin", ""))
        checks[prefix + "dimensions"] = (
            len(epsilon) == 1
            and len(x_box) == len(k_box) == len(left) == len(right) == 4
        )
        if not checks[prefix + "dimensions"]:
            continue

        checks[prefix + "epsilon_exact_slab"] = (
            contains(epsilon[0], Decimal("0.099"))
            and contains(epsilon[0], Decimal("0.101"))
        )
        checks[prefix + "frozen_root_box"] = all(
            x_interval[0] <= center - radius
            and x_interval[1] >= center + radius
            for x_interval, center, radius in zip(
                x_box, root_centers, root_radii, strict=True
            )
        )
        recomputed = [
            (k_interval[0] - x_interval[0], x_interval[1] - k_interval[1])
            for x_interval, k_interval in zip(x_box, k_box, strict=True)
        ]
        checks[prefix + "strict_krawczyk_replay"] = all(
            left_margin > 0 and right_margin > 0
            for left_margin, right_margin in recomputed
        )
        checks[prefix + "reported_margins_positive"] = all(
            item[0] > 0 for item in left + right
        )

        a_box = intervals(values.get("a", ""))
        c_box = intervals(values.get("c", ""))
        ls_box = intervals(values.get("lambda_slow", ""))
        lf_box = intervals(values.get("lambda_fast", ""))
        es_box = intervals(values.get("e_slow", ""))
        ef_box = intervals(values.get("e_fast", ""))
        checks[prefix + "algebraic_constants"] = (
            len(a_box) == len(c_box) == len(ls_box) == len(lf_box) == 1
            and len(es_box) == len(ef_box) == 2
            and contains(a_box[0], a_exact)
            and contains(c_box[0], c_exact)
            and contains(ls_box[0], lambda_slow)
            and contains(lf_box[0], lambda_fast)
            and all(contains(box, value) for box, value in zip(es_box, e_slow, strict=True))
            and all(contains(box, value) for box, value in zip(ef_box, e_fast, strict=True))
        )
        parsed_runs[bits] = {
            "epsilon": epsilon[0],
            "x": x_box,
            "k": k_box,
            "minimum_margin": min(value for pair in recomputed for value in pair),
        }

    if 128 in parsed_runs and 256 in parsed_runs:
        checks["precision_krawczyk_overlap"] = all(
            max(first[0], second[0]) <= min(first[1], second[1])
            for first, second in zip(
                parsed_runs[128]["k"], parsed_runs[256]["k"], strict=True
            )
        )
    else:
        checks["precision_krawczyk_overlap"] = False

    overall = all(checks.values())
    output = {
        "status": "PASS" if overall else "FAIL",
        "scope": (
            "independent hash, algebraic-constant, transcript, and Krawczyk "
            "arithmetic replay; not an independent ODE integration"
        ),
        "checks": checks,
        "check_count": len(checks),
        "minimum_margins": {
            str(bits): str(data["minimum_margin"])
            for bits, data in parsed_runs.items()
        },
    }
    (result / "independent_checker.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"status": output["status"], "checks": len(checks)}, indent=2))
    return 0 if overall else 1


if __name__ == "__main__":
    raise SystemExit(main())

