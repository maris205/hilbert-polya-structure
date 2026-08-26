#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C169."""
from __future__ import annotations

from hashlib import sha256
import json
from math import comb
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c169_skew_shift_evidence.json"
checks = 0


def require(condition: bool, message: str) -> None:
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    data = json.loads(path.read_text())
    body = dict(data)
    claimed = body.pop("payload_sha256")
    encoded = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    require(sha256(encoded).hexdigest() == claimed, "payload hash")
    require(set(data) == {
        "schema", "candidate_id", "date_utc", "source_commit", "scope_literal",
        "source_lock", "iterate_theorem", "haar_and_fourier_theorem",
        "reversibility_and_operator_boundary", "finite_replay",
        "progress_and_boundary", "route_a", "scope_flags", "nonclaims",
        "payload_sha256",
    }, "top-level closure")
    require(data["schema"] == "HCS-C169-v1", "schema")
    require(data["candidate_id"] == "HCS-C169", "candidate")
    require(data["date_utc"] == "2026-08-26", "date")
    require(data["source_commit"] == "ee8af7b8e265fa4f901d5ed2d1c2edd51475b06f", "source commit")
    require(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")

    lock = data["source_lock"]
    require(set(lock) == {"object", "family", "arithmetic_origin", "clock", "normalization", "determinant_convention", "cutoff", "precision", "allowed_data", "forbidden_data"}, "lock closure")
    require("Furstenberg skew shift" in lock["object"], "object")
    require(lock["family"] == "every irrational alpha modulo one", "family")
    require(lock["clock"] == "one application of T_alpha", "clock")
    require("normalized Haar" in lock["normalization"] and "Fourier basis" in lock["normalization"], "normalization")
    require("Artin--Mazur" in lock["determinant_convention"] and "ordinary Fredholm" in lock["determinant_convention"], "determinant convention")
    require("all-parameter proof" in lock["cutoff"] and "n<=32" in lock["cutoff"] and "|k|<=8 on the Fourier grid" in lock["cutoff"] and "0<|k|<=12" in lock["cutoff"], "cutoff")
    require(lock["precision"] == "exact integer affine coefficients and formal irrational alpha", "precision")
    require("no prime or prime-power structure" in lock["arithmetic_origin"] and "toral affine map" in lock["allowed_data"], "arithmetic origin and allowed data")
    require("target zero or prime tables" in lock["forbidden_data"] and "Route-B" in lock["forbidden_data"], "forbidden")

    iterate = data["iterate_theorem"]
    require(set(iterate) == {"formula", "fixed_point_obstruction", "fixed_counts", "artin_mazur_zeta"}, "iterate closure")
    require("binom(n,2)" in iterate["formula"] and "every n>=1" in iterate["formula"], "iterate formula")
    require("n*alpha=0 mod 1" in iterate["fixed_point_obstruction"] and "irrational" in iterate["fixed_point_obstruction"], "fixed obstruction")
    require(iterate["fixed_counts"] == "#Fix(T_alpha^n)=0 for every n>=1", "fixed theorem")
    require(iterate["artin_mazur_zeta"].endswith("=1"), "zeta")

    fourier = data["haar_and_fourier_theorem"]
    require(set(fourier) == {"haar", "koopman_convention", "basis_action", "pure_point_sector", "shift_sectors", "global_spectrum"}, "fourier closure")
    require("determinant-one" in fourier["haar"] and "Haar" in fourier["haar"], "Haar")
    require(fourier["koopman_convention"] == "U f=f after T_alpha", "Koopman convention")
    require(fourier["basis_action"] == "U e_(m,k)=exp(2*pi*i*m*alpha)e_(m+k,k)", "basis theorem")
    require("k=0" in fourier["pure_point_sector"] and "eigenvalues" in fourier["pure_point_sector"], "pure point")
    require("|k|" in fourier["shift_sectors"] and "bilateral shift" in fourier["shift_sectors"], "shift sectors")
    require("countably infinite multiplicity" in fourier["global_spectrum"], "global spectrum")

    operator = data["reversibility_and_operator_boundary"]
    require(set(operator) == {"reversor", "antiunitary", "unitary", "noncompact", "schatten", "fredholm_boundary"}, "operator closure")
    require(operator["reversor"] == "R(x,y)=(alpha-x,y) mod 1 is involutive and R*T_alpha*R=T_alpha^(-1)", "reversor")
    require("Theta*U*Theta=U^(-1)" in operator["antiunitary"], "antiunitary")
    require("same-clock" in operator["unitary"], "unitary owner")
    require("not compact" in operator["noncompact"], "noncompact")
    require(operator["schatten"] == "U belongs to no finite Schatten class", "Schatten")
    require("not trace class" in operator["fredholm_boundary"] and "unavailable" in operator["fredholm_boundary"], "Fredholm boundary")

    replay = data["finite_replay"]
    require(set(replay) == {"n_max", "m_max", "fourier_k_max", "sector_k_max", "iterate_rows", "fourier_rows", "sector_rows", "iterate_cell_count", "fourier_cell_count", "sector_cell_count"}, "replay closure")
    require((replay["n_max"], replay["m_max"], replay["fourier_k_max"], replay["sector_k_max"]) == (32, 12, 8, 12), "replay bounds")
    require(len(replay["iterate_rows"]) == 32, "iterate length")
    for n, row in enumerate(replay["iterate_rows"], 1):
        require(set(row) == {"n", "x_coefficient_x", "x_coefficient_alpha", "y_coefficient_y", "y_coefficient_x", "y_coefficient_alpha", "fixed_points"}, f"iterate closure {n}")
        expected = {
            "n": n, "x_coefficient_x": 1, "x_coefficient_alpha": n,
            "y_coefficient_y": 1, "y_coefficient_x": n,
            "y_coefficient_alpha": n * (n - 1) // 2, "fixed_points": 0,
        }
        require(row == expected, f"iterate row {n}")
        require(row["y_coefficient_alpha"] == comb(n, 2), f"binomial {n}")
        if n < 32:
            nxt = replay["iterate_rows"][n]
            require(nxt["x_coefficient_alpha"] == row["x_coefficient_alpha"] + 1, f"x induction {n}")
            require(nxt["y_coefficient_x"] == row["y_coefficient_x"] + 1, f"y-x induction {n}")
            require(nxt["y_coefficient_alpha"] == row["y_coefficient_alpha"] + n, f"alpha induction {n}")
    require(replay["iterate_cell_count"] == 32, "iterate count")

    expected_fourier = []
    for k in range(-8, 9):
        for m in range(-12, 13):
            expected_fourier.append({
                "m": m, "k": k, "phase_alpha_coefficient": m,
                "output_m": m + k, "output_k": k,
                "sector": "pure_point" if k == 0 else "lebesgue_shift",
            })
    require(len(expected_fourier) == 425, "fourier expected size")
    require(len(replay["fourier_rows"]) == 425, "fourier row size")
    for index, (got, expected) in enumerate(zip(replay["fourier_rows"], expected_fourier)):
        require(set(got) == {"m", "k", "phase_alpha_coefficient", "output_m", "output_k", "sector"}, f"fourier closure {index}")
        require(got == expected, f"fourier row {index}")
        require(got["output_m"] - got["m"] == got["k"], f"sector invariance {index}")
    require(replay["fourier_cell_count"] == 425, "fourier count")

    expected_sectors = []
    for k in list(range(-12, 0)) + list(range(1, 13)):
        expected_sectors.append({
            "k": k, "residues_mod_abs_k": list(range(abs(k))),
            "bilateral_shift_copies": abs(k), "spectral_type": "Lebesgue",
        })
    require(replay["sector_rows"] == expected_sectors, "sector rows")
    for row in replay["sector_rows"]:
        require(len(row["residues_mod_abs_k"]) == abs(row["k"]), f"residue count {row['k']}")
        require(row["bilateral_shift_copies"] == abs(row["k"]), f"copy count {row['k']}")
    require(replay["sector_cell_count"] == 24, "sector count")

    progress = data["progress_and_boundary"]
    require(set(progress) == {"progress", "route_a_obstruction", "sentinel_boundary"}, "progress closure")
    require("all-irrational-parameter" in progress["progress"] and "spectral decomposition" in progress["progress"], "progress")
    require("empty periodic data" in progress["route_a_obstruction"] and "no primitive-orbit carrier" in progress["route_a_obstruction"], "route obstruction")
    require("regression-test" in progress["sentinel_boundary"] and "do not establish irrationality" in progress["sentinel_boundary"], "sentinel boundary")

    route = data["route_a"]
    require(set(route) == {"tuple", "overall", "A0_qualification", "A1_qualification", "A2_qualification", "A3_qualification", "A4_qualification", "route_b_invocation_allowed"}, "route closure")
    require(route["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"], "route tuple")
    require(route["overall"] == "ROUTE_A_REJECTED", "overall")
    require(route["A0_qualification"] == "NO_INTRINSIC_ARITHMETIC_ORIGIN_OR_PRIME_CORRESPONDENCE", "A0")
    require(route["A1_qualification"] == "ALL_POSITIVE_FIXED_SETS_EMPTY_SO_NO_PRIMITIVE_PERIODIC_ORBITS", "A1")
    require(route["A2_qualification"] == "TRIVIAL_SOURCE_ARTIN_MAZUR_ZETA_WITH_NO_TARGET_DIVISOR", "A2")
    require(route["A3_qualification"] == "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_CONTINUATION_COMPARISON", "A3")
    require(route["A4_qualification"] == "SAME_CLOCK_HAAR_KOOPMAN_UNITARY_WITH_EXPLICIT_ANTIUNITARY_REVERSAL", "A4")
    require(route["route_b_invocation_allowed"] is False, "Route B")

    flags = data["scope_flags"]
    require(set(flags) == {"used_target_zero_table", "used_target_prime_table", "used_arithmetic_local_data", "claimed_target_divisor_match", "claimed_target_functional_equation", "claimed_hilbert_polya", "route_b_invocation_allowed"}, "flag closure")
    require(not any(flags.values()), "all scope flags false")
    require(len(data["nonclaims"]) == 5, "nonclaim count")
    joined = " ".join(data["nonclaims"])
    require("Hilbert--Polya" in joined and "novelty priority" in joined and "external peer review" in joined, "nonclaim boundary")
    print(json.dumps({"status": "C169_INDEPENDENT_CHECK_PASS", "assertions": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
