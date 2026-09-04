#!/usr/bin/env python3
"""Independent SymPy lane for exact identities in HCS-C374."""
from __future__ import annotations

import argparse
import json
import sys
from fractions import Fraction
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c374_kummer_arboreal_evidence.json"


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C374 SymPy lane refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT)
    args = parser.parse_args()
    evidence = json.loads(args.input.read_text())
    checks = 0

    def require(statement: bool, label: str) -> None:
        nonlocal checks
        if not statement:
            raise AssertionError(label)
        checks += 1

    x, t = sp.symbols("x t")
    require(sp.factor(x**4 - 2) == x**4 - 2, "x^4-2 irreducibility receipt")
    require(sp.Poly(x**4 - 2, x).is_irreducible, "SymPy irreducibility")
    resultant = sp.factor(sp.resultant(t**4 + 1, t * x - t**2 - 1, t))
    require(resultant == (x**2 - 2) ** 2, "zeta_8 trace identity")

    for a, value in ((1, 1), (3, -1), (5, -1), (7, 1)):
        require(int(sp.kronecker_symbol(2, a)) == value, f"Kronecker character {a}")

    for row in evidence["group_ledger"]:
        n = row["n"]
        order = sp.Integer(2) ** (2 * n - 2)
        positive = sp.Integer(2) ** (2 * n - 4) + 1
        for k in range(3, n):
            positive += sp.Integer(2) ** (2 * n - 2 * k - 1)
        closed = sp.Rational(7, 24) + sp.Rational(1, 3 * 4 ** (n - 1))
        require(sp.simplify(positive / order - closed) == 0, f"density sum n={n}")
        require(Fraction(int(positive), int(order)) == Fraction(row["root_prime_density"]), f"stored density n={n}")
        polynomial = x ** (2**n) - 2
        discriminant = sp.discriminant(polynomial, x)
        expected_abs = (2**n) ** (2**n) * 2 ** (2**n - 1)
        require(abs(int(discriminant)) == expected_abs, f"binomial discriminant n={n}")
        require(set(sp.factorint(abs(int(discriminant)))) == {2}, f"only bad prime n={n}")

    parent = evidence["arithmetic_controls"]["simpler_parent_full_affine"]
    for row in parent["level_ledger"]:
        n = row["n"]
        require(row["group_order"] == 2 ** (2 * n - 1), f"full-affine order n={n}")
        require(row["four_fixed_elements"] == 2 ** (2 * n - 5),
                f"full-affine four-root stratum n={n}")
    require(evidence["arithmetic_controls"]["neighboring_basepoint_3"]
            ["shared_Q_sqrt_2_character_entanglement"] is False,
            "basepoint-three entanglement control")
    require(evidence["arithmetic_controls"]["empirical_density_earns_a0_credit"] is False,
            "empirical density no-credit control")
    composite = evidence["arithmetic_controls"]["composite_label_decomposition"]
    require([(row["value"], row["prime"], row["exponent"])
             for row in composite["prime_power_labels"]] == [
                 (9, 3, 2), (25, 5, 2), (27, 3, 3), (49, 7, 2), (81, 3, 4),
             ], "prime-power repetition labels")
    require(composite["prime_power_count"] == 5, "prime-power count")
    require(composite["mixed_composite_count"] == 20, "mixed-composite count")
    require(composite["odd_composite_count_below_100"] == 25,
            "odd-composite decomposition count")
    require(composite["mixed_composite_has_single_prime_frobenius_owner"] is False,
            "mixed-composite owner boundary")
    require("Frob_p^r" in composite["prime_power_owner"],
            "prime-power Frobenius repetition owner")
    require(evidence["route_a"]["tuple"][1] == "A1_WEAK", "strict A1 verdict")
    require(evidence["route_a"]["tuple"][4] == "A4_FORMAL_HINT", "strict A4 verdict")
    require(evidence["route_a"]["overall"] == "ROUTE_A_EXPLORATORY",
            "strict overall verdict")
    quantization = evidence["quantization_boundary"]
    require(quantization["same_level_and_iterate_clock"] is True,
            "finite Koopman clock")
    require(quantization["canonical_global_time_reversal_to_inverse"] is False,
            "no canonical family time reversal")
    require(quantization["nontrivial_orbit_phase_or_weight_package"] is False,
            "no phase-weight package")
    require(quantization["global_self_adjoint_hamiltonian_owner"] is False,
            "no global Hamiltonian owner")
    require(quantization["route_a_verdict"] == "A4_FORMAL_HINT",
            "formal A4 boundary")

    # The defining parity condition is closed under the affine group law.
    for n in range(3, 9):
        modulus = 2**n
        elements = [
            (a, b)
            for a in range(1, modulus, 2)
            for b in range(modulus)
            if ((-1) ** b) == int(sp.kronecker_symbol(2, a))
        ]
        require(len(elements) == 2 ** (2 * n - 2), f"image order n={n}")
        probes = elements[:: max(1, len(elements) // 97)]
        for a, b in probes:
            inverse_a = pow(a, -1, modulus)
            inverse = (inverse_a, (-inverse_a * b) % modulus)
            require(inverse in elements, f"inverse closure n={n}")
            for c, d in probes[:7]:
                product = ((a * c) % modulus, (a * d + b) % modulus)
                require(product in elements, f"product closure n={n}")

    print(f"C374 SymPy cross-check: PASS ({checks} exact checks)")


if __name__ == "__main__":
    main()
