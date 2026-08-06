#!/usr/bin/env python3
"""Independent arbitrary-precision checker for R300.

This script deliberately does not import ``hp_candidate_search``.
"""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import mpmath as mp


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RESULT_DIR = PROJECT_ROOT / "results" / "r300_heat_activity"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    digest.update(path.read_bytes())
    return digest.hexdigest()


def main() -> int:
    summary_path = RESULT_DIR / "summary.json"
    payload = json.loads(summary_path.read_text(encoding="utf-8"))
    mp.mp.dps = 60
    a = mp.mpf(51) / 50
    r = 1 / (1 + mp.sqrt(1 + a))
    gamma = mp.euler
    coefficient = -(a * a) / (24 * mp.pi)
    beta = 2 * (1 - gamma) + 4 * mp.pi * r * r
    kappa = mp.pi**2 / 6 - 2 * gamma + gamma**2 + 4 * mp.pi * r * r * (1 - gamma)

    rows = []
    high_precision_internal_max = mp.mpf("0")
    production_max = mp.mpf("0")
    for record in payload["records"]:
        t = mp.mpf(str(record["t"]))
        lam = 2 * mp.pi * t
        log_clock = mp.log(1 / lam)
        # A finite endpoint of 200 leaves an exponentially small tail below
        # 1e-80.  Avoiding mp.inf also keeps the check fast and deterministic.
        w_intervals = [lam, mp.mpf("1"), mp.mpf("5"), mp.mpf("20"), mp.mpf("200")]
        a1 = mp.quad(lambda w: w * mp.exp(-w) * mp.log(w / lam), w_intervals)
        a2 = mp.quad(lambda w: w * mp.exp(-w) * mp.log(w / lam) ** 2, w_intervals)
        bracket_w = a2 + 4 * mp.pi * r * r * a1

        # Independent log-radial path: x=z-log(1/lambda) removes the very
        # large lambda^{-2} scale.  The x>8 tail is super-exponentially tiny.
        x_intervals = [-log_clock, mp.mpf("0"), mp.mpf("2"), mp.mpf("4"), mp.mpf("8")]
        bracket_z = mp.quad(
            lambda x: mp.exp(2 * x - mp.exp(x))
            * ((log_clock + x) ** 2 + 4 * mp.pi * r * r * (log_clock + x)),
            x_intervals,
        )
        internal_error = abs(bracket_z - bracket_w) / abs(bracket_w)
        production_error = abs(mp.mpf(str(record["exact_bracket"])) - bracket_w) / abs(bracket_w)
        high_precision_internal_max = max(high_precision_internal_max, internal_error)
        production_max = max(production_max, production_error)
        rows.append(
            {
                "t": str(t),
                "bracket_70dps": mp.nstr(bracket_w, 50),
                "internal_relative_error": mp.nstr(internal_error, 12),
                "production_relative_error": mp.nstr(production_error, 12),
            }
        )

    stored = payload["constants"]
    constant_errors = {
        "coefficient": abs(mp.mpf(str(stored["coefficient"])) - coefficient),
        "beta": abs(mp.mpf(str(stored["beta"])) - beta),
        "kappa": abs(mp.mpf(str(stored["kappa"])) - kappa),
        "r_a": abs(mp.mpf(str(stored["r_a"])) - r),
    }
    passed = bool(
        high_precision_internal_max <= mp.mpf("1e-45")
        and production_max <= mp.mpf("1e-12")
        and max(constant_errors.values()) <= mp.mpf("1e-12")
    )
    output = {
        "run_id": "R300-independent",
        "passed": passed,
        "summary_sha256": sha256(summary_path),
        "mpmath_dps": mp.mp.dps,
        "max_high_precision_internal_relative_error": mp.nstr(
            high_precision_internal_max, 20
        ),
        "max_production_relative_error": mp.nstr(production_max, 20),
        "constant_absolute_errors": {
            key: mp.nstr(value, 20) for key, value in constant_errors.items()
        },
        "records": rows,
        "scope": "carrier_identity_only; no full heat-trace remainder certification",
    }
    (RESULT_DIR / "independent_checker.json").write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )
    print(json.dumps(output, indent=2, sort_keys=True))
    return 0 if passed else 2


if __name__ == "__main__":
    raise SystemExit(main())
