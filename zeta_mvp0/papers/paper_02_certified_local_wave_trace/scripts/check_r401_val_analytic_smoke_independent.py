#!/usr/bin/env python3
"""Independent no-production-import check of the R401-VAL analytic smoke."""

from __future__ import annotations

import argparse
import json
from hashlib import sha256
from pathlib import Path

from flint import arb, ctx, fmpq


ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    ROOT / "research/route_a_wave_trace/R401_VALIDATED_THEOREM_DOMAIN_PROTOCOL.md": "d00d95f32ddfe4420da2cdac46ef1a3bb39bb3ea2277a21a9776652794a20d82",
    ROOT / "research/route_a_wave_trace/A411_RADIAL_PERIOD_BOUND.md": "b991cf5ffce043db60ceaf2448f383364c66dca66812180fb996c19debcd11bb",
    ROOT / "research/route_a_wave_trace/A411_WARPED_PERIOD_FLOOR.md": "71cc840cd6518ecb4672402fbe2517ae5096bb654872abce32ef21d02a7e26d8",
}


def q(n: int, d: int = 1) -> arb:
    return arb(fmpq(n, d))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--result-dir",
        type=Path,
        default=ROOT / "results/r401_val_analytic_smoke",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    result_dir = args.result_dir.resolve()
    stored = json.loads((result_dir / "summary.json").read_text(encoding="utf-8"))
    ctx.prec = 256
    pi = arb.pi()
    a = q(51, 50)
    epsilon = q(101, 1000)
    c = 2 * ((1 + a).sqrt() - 1)
    radius = epsilon / (q(2).sqrt() * pi)
    y_bound = (1 + c) * radius + a * radius**2
    f_bound = (1 + 2 * c) * radius + 2 * a * radius**2
    u2_bound = f_bound**2 + radius**2
    d_bound = c + 2 * a * radius
    trace = d_bound**2 + 2
    jacobian_norm_sq = (trace + (trace**2 - 4).sqrt()) / 2
    potential = 2 * pi * (pi * u2_bound).exp()
    warped_hessian = potential * (
        2 * pi * (jacobian_norm_sq + 2 * a * f_bound)
        + 4 * pi**2 * jacobian_norm_sq * u2_bound
    )
    warped_period = 2 * pi / warped_hessian.sqrt()
    delta = epsilon**2
    radial_hessian = (2 * pi + delta) * (2 * pi + 2 * delta)
    radial_period = 2 * pi / radial_hessian.sqrt()
    normalized_radius = 1 / (q(2).sqrt() * pi)
    normalized_q2 = (1 + c) * normalized_radius + a * epsilon * normalized_radius**2

    checks: dict[str, bool] = {
        "stored_status_is_smoke": stored.get("status") == "PASS_IMPLEMENTATION_SMOKE",
        "warped_hessian_lt_103": warped_hessian < q(103),
        "warped_period_gt_point60": warped_period > q(60, 100),
        "radial_period_gt_point99": radial_period > q(99, 100),
        "physical_q1_lt_point02274": radius < q(2274, 100000),
        "physical_q2_lt_point042427": y_bound < q(42427, 1000000),
        "warped_u1_lt_point062114": f_bound < q(62114, 1000000),
        "normalized_q1_lt_point226": normalized_radius < q(226, 1000),
        "normalized_q2_lt_point421": normalized_q2 < q(421, 1000),
        "epsilon_cap_strictly_beyond_r401": epsilon > q(1, 10),
    }
    for path, expected in EXPECTED.items():
        checks[f"hash:{path.name}"] = sha256(path.read_bytes()).hexdigest() == expected
    for run in stored.get("precision_runs", []):
        precision = run.get("precision_bits")
        checks[f"stored_run_{precision}_all_gates"] = (
            run.get("status") == "PASS_IMPLEMENTATION_SMOKE"
            and all(run.get("gates", {}).values())
        )

    status = "PASS" if all(checks.values()) else "FAIL"
    payload = {
        "status": status,
        "checks_count": len(checks),
        "checks": checks,
        "recomputed": {
            "warped_hessian": str(warped_hessian),
            "warped_period": str(warped_period),
            "radial_period": str(radial_period),
            "normalized_q2_bound": str(normalized_q2),
        },
        "claim_level": "independent analytic implementation check only",
    }
    (result_dir / "independent_checker.json").write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    print(json.dumps({"status": status, "checks": len(checks)}, indent=2))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
