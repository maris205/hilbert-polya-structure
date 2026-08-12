import json
from pathlib import Path
import subprocess
import sys

import mpmath as mp

from symplectic_henon.audit import audit_ledger_payload
from symplectic_henon.cycles import build_orbit_ledger


def _small_ledger():
    return build_orbit_ledger(
        a=6.0,
        rho=1.0,
        max_period=4,
        regime="full_shift_positive_control",
    )


def test_mpmath_audit_refines_residual_and_checks_determinant() -> None:
    audit = audit_ledger_payload(_small_ledger(), digits=80)
    assert audit["audit_kind"] == "high_precision_residual_audit"
    assert audit["precision_decimal_digits"] == 80
    assert not audit["interval_certification"]
    assert audit["runs"][0]["all_orbits_refined_to_target"]
    for period in audit["runs"][0]["periods"]:
        for orbit in period["orbits"]:
            assert mp.mpf(orbit["refined_residual_inf"]) < mp.mpf("1e-60")
            assert mp.mpf(orbit["determinant_absolute_error"]) < mp.mpf("1e-60")
            with mp.workdps(80):
                first = mp.mpc(orbit["multipliers"][0]["real"], orbit["multipliers"][0]["imag"])
                second = mp.mpc(orbit["multipliers"][1]["real"], orbit["multipliers"][1]["imag"])
                assert abs(first * second - 1) < mp.mpf("1e-60")


def test_audit_script_round_trip(tmp_path) -> None:
    input_path = tmp_path / "ledger.json"
    output_path = tmp_path / "audit.json"
    input_path.write_text(json.dumps({"runs": [_small_ledger()]}), encoding="utf-8")
    script = CODE_ROOT / "scripts" / "audit_ledger.py"
    subprocess.run(
        [sys.executable, str(script), str(input_path), "--output", str(output_path)],
        check=True,
    )
    audit = json.loads(output_path.read_text(encoding="utf-8"))
    assert audit["audit_kind"] == "high_precision_residual_audit"
    assert audit["runs"][0]["all_orbits_refined_to_target"]


CODE_ROOT = Path(__file__).resolve().parents[1]
