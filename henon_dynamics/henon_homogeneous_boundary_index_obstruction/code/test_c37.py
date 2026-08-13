#!/usr/bin/env python3
from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from typing import Any


PROJECT = Path(__file__).resolve().parents[1]
CHECKER = PROJECT / "code/c37_homogeneous_index_checker.py"
PRODUCER = PROJECT / "code/c37_homogeneous_index_producer.py"
CERTIFICATE = PROJECT / "results/c37_certificate.json"


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(
        value, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")


def load_module(path: Path, name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class C37Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.base = json.loads(CERTIFICATE.read_text(encoding="utf-8"))
        cls.checker = load_module(CHECKER, "c37_checker_test")
        cls.producer = load_module(PRODUCER, "c37_producer_test")

    def rehash(self, certificate: dict[str, Any]) -> None:
        certificate["payload_sha256"] = hashlib.sha256(
            canonical_bytes(certificate["payload"])
        ).hexdigest()

    def rejected(self, mutate: Any, rehash: bool = True) -> None:
        candidate = copy.deepcopy(self.base)
        mutate(candidate)
        if rehash:
            self.rehash(candidate)
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "mutated.json"
            path.write_text(json.dumps(candidate, sort_keys=True), encoding="utf-8")
            with self.assertRaises(self.checker.GateFailure):
                self.checker.audit(path)

    def test_01_base_certificate_passes(self) -> None:
        report = self.checker.audit(CERTIFICATE)
        self.assertTrue(report["all_pass"])
        self.assertEqual((report["passed"], report["total"]), (10, 10))

    def test_02_producer_deterministic(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            one = Path(tmp) / "one.json"
            two = Path(tmp) / "two.json"
            subprocess.run(
                [sys.executable, str(PRODUCER), "--output", str(one)], check=True
            )
            subprocess.run(
                [sys.executable, str(PRODUCER), "--output", str(two)], check=True
            )
            self.assertEqual(one.read_bytes(), two.read_bytes())
            self.assertEqual(one.read_bytes(), CERTIFICATE.read_bytes())

    def test_03_unrehashed_payload_rejected(self) -> None:
        self.rejected(
            lambda c: c["payload"].update({"candidate_id": "bad"}),
            rehash=False,
        )

    def test_04_unknown_top_key_rejected(self) -> None:
        self.rejected(lambda c: c["payload"].update({"rh_proved": True}))

    def test_05_passport_bool_integer_confusion_rejected(self) -> None:
        self.rejected(
            lambda c: c["payload"]["material_passport"].update(
                {"ai_assistance_disclosed": 1}
            )
        )

    def test_06_source_digest_mutation_rejected(self) -> None:
        self.rejected(
            lambda c: c["payload"]["source_lock"]["c36_theorem_package"].update(
                {"sha256": "0" * 64}
            )
        )

    def test_07_phase_mutation_rejected(self) -> None:
        self.rejected(
            lambda c: c["payload"]["conventions"].update(
                {"phase": "P0(x)=2*x^3-x"}
            )
        )

    def test_08_determinant_float_confusion_rejected(self) -> None:
        self.rejected(
            lambda c: c["payload"]["classical_gate"].update(
                {"determinant": 1.0}
            )
        )

    def test_09_coboundary_class_promotion_rejected(self) -> None:
        self.rejected(
            lambda c: c["payload"]["equivariant_coboundary"].update(
                {"groupoid_H1_class": "NONZERO"}
            )
        )

    def test_10_gauge_mutation_rejected(self) -> None:
        self.rejected(
            lambda c: c["payload"]["equivariant_coboundary"].update(
                {"simultaneous_gauge": "unspecified"}
            )
        )

    def test_11_prime_holonomy_bool_confusion_rejected(self) -> None:
        self.rejected(
            lambda c: c["payload"]["prime_loop_gate"].update(
                {"closed_gauge_holonomy": True}
            )
        )

    def test_12_pair_index_promotion_rejected(self) -> None:
        self.rejected(
            lambda c: c["payload"]["poisson_boundary_pair"].update(
                {"essential_codimension": 1}
            )
        )

    def test_13_intrinsic_quotient_promotion_rejected(self) -> None:
        self.rejected(
            lambda c: c["payload"]["poisson_boundary_pair"].update(
                {"intrinsic_quotient_automorphism": "PROVED"}
            )
        )

    def test_14_vmo_bound_mutation_rejected(self) -> None:
        self.rejected(
            lambda c: c["payload"]["hardy_restricted_gate"][
                "l2_mean_oscillation_lower"
            ].update({"numerator": 52})
        )

    def test_15_vmo_status_promotion_rejected(self) -> None:
        self.rejected(
            lambda c: c["payload"]["hardy_restricted_gate"].update(
                {"vmo_status": "VMO"}
            )
        )

    def test_16_relative_anomaly_float_confusion_rejected(self) -> None:
        self.rejected(
            lambda c: c["payload"]["homogeneous_mellin_shadow"].update(
                {"normalized_relative_anomaly": 1.0}
            )
        )

    def test_17_route_a_promotion_rejected(self) -> None:
        self.rejected(
            lambda c: c["payload"]["route_a"].update(
                {"overall": "ROUTE_A_SUCCESS_ROUTE_B_READY"}
            )
        )

    def test_18_route_b_promotion_rejected(self) -> None:
        self.rejected(
            lambda c: c["payload"]["route_a"].update(
                {"route_b_invocation_allowed": True}
            )
        )

    def test_19_next_door_mutation_rejected(self) -> None:
        self.rejected(
            lambda c: c["payload"]["route_a"]["decisions"].update(
                {"next_big_door": "FIT_RIEMANN_ZEROS"}
            )
        )

    def test_20_rh_scope_deletion_rejected(self) -> None:
        self.rejected(
            lambda c: c["payload"]["scope"]["not_claimed"].remove(
                "RH or a Hilbert-Polya operator"
            )
        )

    def test_21_duplicate_json_key_rejected(self) -> None:
        raw = CERTIFICATE.read_text(encoding="utf-8")
        mutated = raw.replace(
            '"payload_sha256":', '"payload_sha256":"0","payload_sha256":', 1
        )
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "duplicate.json"
            path.write_text(mutated, encoding="utf-8")
            with self.assertRaises(self.checker.GateFailure):
                self.checker.audit(path)

    def test_22_unchecked_clock_text_rejected(self) -> None:
        self.rejected(
            lambda c: c["payload"]["prime_loop_gate"].update(
                {"clock_preserved": "fitted clock"}
            )
        )

    def test_23_unknown_nested_scope_key_rejected(self) -> None:
        self.rejected(
            lambda c: c["payload"]["scope"].update({"rh_proved": True})
        )

    def test_24_unknown_route_decision_rejected(self) -> None:
        self.rejected(
            lambda c: c["payload"]["route_a"]["decisions"].update(
                {"extra_divisor": "PASS"}
            )
        )

    def test_25_unvalidated_hardy_text_rejected(self) -> None:
        self.rejected(
            lambda c: c["payload"]["hardy_restricted_gate"].update(
                {"hardy_commutator_status": "COMPACT"}
            )
        )


if __name__ == "__main__":
    unittest.main()
