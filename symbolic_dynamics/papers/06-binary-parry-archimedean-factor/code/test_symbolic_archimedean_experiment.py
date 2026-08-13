#!/usr/bin/env python3
import importlib.util
import math
from pathlib import Path

import numpy as np

MODULE_PATH = Path(__file__).with_name("symbolic_archimedean_experiment.py")
SPEC = importlib.util.spec_from_file_location("paper06_prototype", MODULE_PATH)
MOD = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(MOD)


def test_k2_idempotent_ledger():
    k2 = np.ones((2, 2)) / 2.0
    for r in range(1, 20):
        assert np.linalg.norm(np.linalg.matrix_power(k2, r) - k2) < 1e-14
        assert abs(np.trace(np.linalg.matrix_power(k2, r)) - 1.0) < 1e-14
    for n in (1, 3, 31, 127):
        for t in (0.0, 0.5, 2.0, 7.0):
            u = t / math.sqrt(n)
            h = k2 @ np.diag([np.exp(-1j * u), np.exp(1j * u)])
            assert abs(np.trace(np.linalg.matrix_power(h, n)) - math.cos(u) ** n) < 2e-13


def test_chiral_block():
    s = 0.5 + 7.0j
    for p in MOD.recovered_multiplicative_atoms(256):
        b = np.array([[0.0, p ** (-s)], [p ** (-(1.0 - s)), 0.0]], dtype=complex)
        assert np.linalg.norm(b @ b - np.eye(2) / p) < 1e-13


def test_completed_gamma_normalization():
    for s in (1.0, 2.0, 3.0, 0.5 + 2.0j):
        target = np.exp(-0.5 * s * math.log(math.pi) + MOD.loggamma(s / 2.0))
        assert abs(MOD.gaussian_absolute_mellin(s) - target) < 1e-14


def test_fair_characteristic_converges():
    a = MOD.fair_characteristic_local_rows(31)
    b = MOD.fair_characteristic_local_rows(32767)
    assert b["characteristic_max_abs_error_t_le_4"] < a["characteristic_max_abs_error_t_le_4"]
    assert b["local_clt_max_relative_error_abs_z_le_3"] < a["local_clt_max_relative_error_abs_z_le_3"]


def test_radial_kq_dimensions_reject_k2_target():
    s = 2.0
    for q in (3, 4):
        radial = MOD.radial_gaussian_mellin(s, q - 1)
        k2 = MOD.gaussian_absolute_mellin(s)
        assert abs(radial - k2) > 1e-3


def test_reversible_control_fails_trace_ledger():
    k = np.array([[0.7, 0.3], [0.3, 0.7]])
    for r in range(1, 8):
        assert abs(np.trace(np.linalg.matrix_power(k, r)) - (1.0 + 0.4**r)) < 1e-13


if __name__ == "__main__":
    for f in (
        test_k2_idempotent_ledger,
        test_chiral_block,
        test_completed_gamma_normalization,
        test_fair_characteristic_converges,
        test_radial_kq_dimensions_reject_k2_target,
        test_reversible_control_fails_trace_ledger,
    ):
        f()
        print("PASS", f.__name__)
