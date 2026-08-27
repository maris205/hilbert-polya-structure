#!/usr/bin/env python3
"""Producer-independent semantic checker for HCS-C202.

This path uses Fraction and Decimal only.  It imports no producer code and
locks every recursive JSON schema before recomputing the finite ledger.
"""
from __future__ import annotations

from decimal import Decimal, getcontext
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c202_fisher_kpp_evidence.json"
SOURCE_COMMIT = "d1e58971e570b855488009af384995702ddb887b"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EXPECTED_SECTION_HASHES = {
    "source_lock": "812357940544ca09df154dc018a7b67a246e753464ab8a31c0f705ab094953e8",
    "source_registry": "77875d2d50860060a8be6475456dc7a73bf75632e50417bf9b565036bdb1687f",
    "attribution": "346a86bfd2f8216f2f738d7837e0f4840e76f84338f1e1453879e01b796207da",
    "theorem": "783cd23e5e32ffb65b5b8fd9961a6a5f3847139a016958c9077b51af8e9ba807",
    "proof_boundary": "a69589414dba385af0ddca685c94c28d20fc5265b43ff77a95cc21a14208d1ed",
    "route_a": "dd0383dcd82a25e685d2bf5423876d9aac70480d998c833ce665ac78e06471bc",
    "scope_flags": "b3b89b2f708124e69ea9ad598059757745f6f279329a812818f8f489105cb910",
    "nonclaims": "03a39eac5a709b29eb522831974761eb11ee914a7b34edfdee9decd0de12a709",
}
TOP_KEYS = {
    "attribution", "candidate_id", "evaluation_date", "evaluator",
    "finite_regression", "headline", "nonclaims", "payload_sha256",
    "proof_boundary", "route_a", "schema", "scope_flags", "scope_literal",
    "source_commit", "source_lock", "source_registry", "summary", "theorem",
}
FINITE_KEYS = {
    "az_rows", "hamiltonian_oval_rows", "phase_rows", "physical_scalings",
    "speed_rows", "trapping_rows",
}
SPEED_KEYS = {
    "admissible_unit_interval_front", "dimensionless_speed", "divergence",
    "energy_derivative_sign", "saddle_negative_rate", "saddle_positive_rate",
    "speed_family", "tail_discriminant", "zero_equilibrium_type",
    "zero_spectral_data",
}
PHASE_KEYS = {"U", "U_prime", "V", "V_prime", "divergence", "energy_derivative", "speed"}
TRAPPING_KEYS = {
    "U", "boundary_G_prime", "quadratic_residual_abs", "slow_slope_q", "speed", "triangle",
}
OVAL_KEYS = {
    "energy", "inner_positive_turning_point", "inner_residual_abs",
    "negative_residual_abs", "negative_turning_point", "outer_residual_abs",
    "outer_unbounded_component_root", "periodic_oval_component",
}
AZ_KEYS = {
    "U", "U_xi_coefficient_over_sqrt6", "U_xixi", "exponential_coordinate_y",
    "ode_residual", "reaction_U_one_minus_U", "speed_times_U_xi", "strictly_decreasing",
}
PHYSICAL_KEYS = {
    "D", "az_inverse_length_sqrt_r_over_6D", "az_speed_5sqrt_Dr_over_sqrt6",
    "length_scale_sqrt_D_over_r", "minimal_speed_2sqrt_Dr", "r",
}


class Counter:
    def __init__(self) -> None:
        self.value = 0

    def check(self, condition: bool, message: str) -> None:
        self.value += 1
        if not condition:
            raise AssertionError(message)


def canonical_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def section_hash(value) -> str:
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def dec(value: F | str | int) -> Decimal:
    if isinstance(value, str):
        if "/" in value:
            value = F(value)
        else:
            return Decimal(value)
    value = F(value)
    return Decimal(value.numerator) / Decimal(value.denominator)


def close(stored: str, expected: Decimal, tolerance: Decimal = Decimal("2e-78")) -> bool:
    return abs(Decimal(stored) - expected) <= tolerance * max(Decimal(1), abs(expected))


def bisect(function, left: Decimal, right: Decimal) -> Decimal:
    f_left = function(left)
    f_right = function(right)
    if f_left * f_right >= 0:
        raise AssertionError("bad bisection bracket")
    for _ in range(430):
        middle = (left + right) / 2
        f_middle = function(middle)
        if f_left * f_middle <= 0:
            right, f_right = middle, f_middle
        else:
            left, f_left = middle, f_middle
    return (left + right) / 2


def classify(speed: F) -> tuple[str, str, str]:
    if speed > 2:
        return "positive_supercritical", "stable_node", "decreasing_1_to_0"
    if speed == 2:
        return "positive_critical", "degenerate_stable_node", "decreasing_1_to_0"
    if speed > 0:
        return "positive_subcritical", "stable_focus", "none_in_unit_interval"
    if speed == 0:
        return "stationary_hamiltonian", "center", "none_in_unit_interval"
    if speed > -2:
        return "negative_subcritical", "unstable_focus", "none_in_unit_interval"
    if speed == -2:
        return "negative_critical", "degenerate_unstable_node", "increasing_0_to_1"
    return "negative_supercritical", "unstable_node", "increasing_0_to_1"


def main() -> None:
    getcontext().prec = 115
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    data = json.loads(path.read_text())
    count = Counter()

    count.check(set(data) == TOP_KEYS, "exact top schema")
    count.check(data["payload_sha256"] == canonical_hash(data), "payload hash")
    count.check(data["schema"] == "hcs-c202-fisher-kpp-wave-atlas-v1", "schema")
    count.check(data["candidate_id"] == "HCS-C202", "candidate")
    count.check(data["evaluation_date"] == "2026-08-27", "date")
    count.check(data["source_commit"] == SOURCE_COMMIT, "source commit")
    count.check(data["scope_literal"] == SCOPE, "scope")
    count.check(data["evaluator"] == {
        "path": "flow_systems/skills/route-a-evaluator.md",
        "version": "0.2.0", "sha256": EVALUATOR_SHA256,
    }, "evaluator")
    count.check(isinstance(data["headline"], str) and len(data["headline"]) > 120, "headline")
    for key, digest in EXPECTED_SECTION_HASHES.items():
        count.check(section_hash(data[key]) == digest, f"section hash {key}")
    count.check(len(data["source_registry"]) == 3, "three sources")
    count.check(data["source_registry"][0]["doi"] == "10.1111/j.1469-1809.1937.tb02153.x", "Fisher DOI")
    count.check("Kluwer 1991, pp. 242--270" in data["source_registry"][1]["translation_locator"], "KPP translation")
    count.check(data["source_registry"][2]["doi"] == "10.1007/BF02462380", "AZ DOI")
    count.check(data["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "route tuple")
    count.check(data["route_a"]["overall"] == "ROUTE_A_REJECTED", "route overall")
    count.check(data["route_a"]["route_b_invocation_allowed"] is False, "route B")
    count.check(all(value is False for value in data["scope_flags"].values()), "scope flags")

    finite = data["finite_regression"]
    count.check(set(finite) == FINITE_KEYS, "finite schema")
    speeds = tuple(F(value, 2) for value in range(-8, 9))
    count.check(len(finite["speed_rows"]) == len(speeds), "speed population")
    for row, speed in zip(finite["speed_rows"], speeds):
        count.check(set(row) == SPEED_KEYS, "speed row schema")
        count.check(F(row["dimensionless_speed"]) == speed, "speed value")
        count.check(row["tail_discriminant"] == str(speed * speed - 4), "tail discriminant")
        family, zero_type, front = classify(speed)
        count.check((row["speed_family"], row["zero_equilibrium_type"], row["admissible_unit_interval_front"]) == (family, zero_type, front), "speed classification")
        count.check(F(row["divergence"]) == -speed, "speed divergence")
        expected_sign = "decreasing" if speed > 0 else "increasing" if speed < 0 else "conserved"
        count.check(row["energy_derivative_sign"] == expected_sign, "energy sign")
        s = dec(speed)
        saddle_disc = (s * s + 4).sqrt()
        count.check(close(row["saddle_positive_rate"], (-s + saddle_disc) / 2), "saddle positive")
        count.check(close(row["saddle_negative_rate"], (-s - saddle_disc) / 2), "saddle negative")
        discriminant = speed * speed - 4
        spectral = row["zero_spectral_data"]
        if discriminant > 0:
            count.check(set(spectral) == {"kind", "lambda_slow", "lambda_fast"} and spectral["kind"] == "real", "real spectral schema")
            root = dec(discriminant).sqrt()
            count.check(close(spectral["lambda_slow"], (-s + root) / 2), "slow root")
            count.check(close(spectral["lambda_fast"], (-s - root) / 2), "fast root")
        elif discriminant == 0:
            count.check(set(spectral) == {"kind", "lambda"} and spectral["kind"] == "repeated_real", "repeated schema")
            count.check(close(spectral["lambda"], -s / 2), "repeated root")
        else:
            count.check(set(spectral) == {"kind", "real_part", "imaginary_part_magnitude"} and spectral["kind"] == "complex_pair", "complex schema")
            count.check(close(spectral["real_part"], -s / 2), "focus real part")
            count.check(close(spectral["imaginary_part_magnitude"], dec(-discriminant).sqrt() / 2), "focus frequency")

    expected_phase = len(speeds) * 5 * 4
    count.check(len(finite["phase_rows"]) == expected_phase, "phase population")
    ordinal = 0
    for speed in speeds:
        for u in (F(1, 10), F(1, 4), F(1, 2), F(3, 4), F(9, 10)):
            for v in (F(-2, 3), F(-1, 4), F(1, 4), F(2, 3)):
                row = finite["phase_rows"][ordinal]
                ordinal += 1
                count.check(set(row) == PHASE_KEYS, "phase row schema")
                count.check((F(row["speed"]), F(row["U"]), F(row["V"])) == (speed, u, v), "phase coordinates")
                count.check(F(row["U_prime"]) == v, "phase U prime")
                count.check(F(row["V_prime"]) == -speed * v - u * (1 - u), "phase V prime")
                count.check(F(row["energy_derivative"]) == -speed * v * v, "phase energy")
                count.check(F(row["divergence"]) == -speed, "phase divergence")

    trap_speeds = (F(2), F(5, 2), F(3), F(7, 2), F(4))
    count.check(len(finite["trapping_rows"]) == len(trap_speeds) * 5, "trapping population")
    ordinal = 0
    for speed in trap_speeds:
        s = dec(speed)
        q = (s - (s * s - 4).sqrt()) / 2
        for u in (F(1, 10), F(1, 4), F(1, 2), F(3, 4), F(9, 10)):
            row = finite["trapping_rows"][ordinal]
            ordinal += 1
            count.check(set(row) == TRAPPING_KEYS, "trapping schema")
            count.check(F(row["speed"]) == speed and F(row["U"]) == u, "trapping coordinates")
            count.check(close(row["slow_slope_q"], q), "trapping slope")
            count.check(Decimal(row["quadratic_residual_abs"]) < Decimal("1e-78"), "trapping quadratic")
            count.check(F(row["boundary_G_prime"]) == u * u, "inward derivative")
            count.check(row["triangle"] == "0<=U<=1 and -qU<=V<=0", "triangle declaration")

    energies = (F(1, 96), F(1, 48), F(1, 24), F(1, 12), F(1, 8), F(5, 32))
    count.check(len(finite["hamiltonian_oval_rows"]) == len(energies), "oval population")
    potential = lambda x: x * x / 2 - x * x * x / 3
    for row, energy in zip(finite["hamiltonian_oval_rows"], energies):
        count.check(set(row) == OVAL_KEYS, "oval schema")
        count.check(F(row["energy"]) == energy, "oval energy")
        h = dec(energy)
        function = lambda x, h=h: potential(x) - h
        negative = bisect(function, Decimal(-2), Decimal(0))
        inner = bisect(function, Decimal(0), Decimal(1))
        right = Decimal(2)
        while function(right) > 0:
            right *= 2
        outer = bisect(function, Decimal(1), right)
        count.check(close(row["negative_turning_point"], negative), "negative root")
        count.check(close(row["inner_positive_turning_point"], inner), "inner root")
        count.check(close(row["outer_unbounded_component_root"], outer), "outer root")
        for key in ("negative_residual_abs", "inner_residual_abs", "outer_residual_abs"):
            count.check(Decimal(row[key]) < Decimal("1e-78"), f"oval residual {key}")
        count.check(row["periodic_oval_component"] == "negative_to_inner_positive", "oval component")

    y_values = (F(1, 16), F(1, 9), F(1, 4), F(1, 2), F(1), F(2), F(4), F(9), F(16))
    count.check(len(finite["az_rows"]) == len(y_values), "AZ population")
    for row, y in zip(finite["az_rows"], y_values):
        count.check(set(row) == AZ_KEYS, "AZ schema")
        denominator = 1 + y
        profile = 1 / denominator**2
        first_coefficient = -2 * y / denominator**3
        second = -y * (1 - 2 * y) / (3 * denominator**4)
        speed_first = -5 * y / (3 * denominator**3)
        reaction = profile * (1 - profile)
        count.check(F(row["exponential_coordinate_y"]) == y, "AZ coordinate")
        count.check(F(row["U"]) == profile, "AZ profile")
        count.check(F(row["U_xi_coefficient_over_sqrt6"]) == first_coefficient, "AZ first")
        count.check(F(row["U_xixi"]) == second, "AZ second")
        count.check(F(row["speed_times_U_xi"]) == speed_first, "AZ speed first")
        count.check(F(row["reaction_U_one_minus_U"]) == reaction, "AZ reaction")
        count.check(F(row["ode_residual"]) == second + speed_first + reaction == 0, "AZ residual")
        count.check(row["strictly_decreasing"] is True, "AZ monotonicity")

    physical = (
        (F(1), F(1)), (F(1, 2), F(3, 2)), (F(2), F(1, 3)),
        (F(3, 2), F(5, 2)), (F(5, 3), F(7, 4)), (F(7, 5), F(11, 6)),
    )
    count.check(len(finite["physical_scalings"]) == len(physical), "physical population")
    sqrt6 = Decimal(6).sqrt()
    for row, (diffusion, growth) in zip(finite["physical_scalings"], physical):
        count.check(set(row) == PHYSICAL_KEYS, "physical schema")
        count.check(F(row["D"]) == diffusion and F(row["r"]) == growth, "physical coordinates")
        D, r = dec(diffusion), dec(growth)
        scale = (D * r).sqrt()
        count.check(close(row["length_scale_sqrt_D_over_r"], (D / r).sqrt()), "length scale")
        count.check(close(row["minimal_speed_2sqrt_Dr"], 2 * scale), "minimal speed")
        count.check(close(row["az_speed_5sqrt_Dr_over_sqrt6"], 5 * scale / sqrt6), "AZ speed")
        count.check(close(row["az_inverse_length_sqrt_r_over_6D"], (r / (6 * D)).sqrt()), "AZ inverse length")

    expected_summary = {
        "speed_case_count": 17,
        "phase_vector_field_row_count": 340,
        "trapping_boundary_row_count": 25,
        "hamiltonian_oval_count": 6,
        "az_exact_sample_count": 9,
        "physical_scaling_count": 6,
        "precision_decimal_digits": 100,
    }
    count.check(data["summary"] == expected_summary, "summary exact")
    print(json.dumps({
        "status": "C202_CHECKER_PASS",
        "assertions": count.value,
        "speed_cases": len(finite["speed_rows"]),
        "phase_rows": len(finite["phase_rows"]),
        "algorithm": "Fraction plus Decimal square roots and independent bisection",
    }, sort_keys=True))


if __name__ == "__main__":
    main()
