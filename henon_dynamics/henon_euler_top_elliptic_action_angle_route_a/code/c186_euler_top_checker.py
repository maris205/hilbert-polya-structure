#!/usr/bin/env python3
"""Producer-independent exact checker for C186."""
from __future__ import annotations

from copy import deepcopy
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path
import sys

import mpmath as mp

DEFAULT = Path(__file__).resolve().parents[1] / "results/c186_euler_top_evidence.json"
EXPECTED_COMMIT = "908a6818caedb0c46195a591873a2ac9c685b55e"


def F(text: str) -> Fraction:
    n, d = text.split("/")
    return Fraction(int(n), int(d))


def M(x: Fraction) -> mp.mpf:
    return mp.mpf(x.numerator) / x.denominator


def payload_hash(data: dict) -> str:
    body = deepcopy(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def action(a: Fraction, b: Fraction, c: Fraction, e: Fraction, regime: str) -> mp.mpf:
    aa, bb, cc, ee = map(M, (a, b, c, e))
    if regime == "low":
        def fn(q: mp.mpf) -> mp.mpf:
            x = aa * mp.cos(q) ** 2 + bb * mp.sin(q) ** 2
            return mp.sqrt((x - ee) / (x - cc))
    else:
        def fn(q: mp.mpf) -> mp.mpf:
            x = bb * mp.cos(q) ** 2 + cc * mp.sin(q) ** 2
            return mp.sqrt((ee - x) / (aa - x))
    return 1 - 2 * mp.quad(fn, [0, mp.pi / 2]) / mp.pi


def close_decimal(x: str, y: mp.mpf) -> bool:
    return abs(mp.mpf(x) - y) < mp.mpf("1e-55") * max(1, abs(y))


def check(path: Path) -> int:
    mp.mp.dps = 90
    d = json.loads(path.read_text())
    n = 0
    def require(condition: bool) -> None:
        nonlocal n
        n += 1
        if not condition:
            raise AssertionError(f"assertion {n} failed")

    require(d["schema"] == "hcs-c186-euler-top-v1")
    require(d["payload_sha256"] == payload_hash(d))
    meta = d["metadata"]
    require(meta["candidate_id"] == "HCS-C186")
    require(meta["source_commit"] == EXPECTED_COMMIT)
    require(meta["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER")
    require(meta["target_tables_used"] == 0)
    require(meta["primary_sources"][0]["doi"] == "10.1137/070704393")
    seen = set()
    for row in d["regular_rows"]:
        I1, I2, I3 = map(F, row["inertia"])
        require(0 < I1 < I2 < I3)
        a, b, c = 1 / I1, 1 / I2, 1 / I3
        require(row["inverse_inertia"] == [f"{x.numerator}/{x.denominator}" for x in (a, b, c)])
        G, t = F(row["G"]), F(row["fraction_to_separatrix"])
        require(G > 0 and 0 < t < 1)
        regime = row["regime"]
        require(regime in {"low", "high"})
        if regime == "low":
            e = c + t * (b - c)
            A2, B2, C2 = (e-c)/(a-c), (e-c)/(b-c), (a-e)/(a-c)
            k2 = (a-b)*(e-c)/((b-c)*(a-e))
            omega2 = G*G*(b-c)*(a-e)
            residuals = [A2+C2-1, -A2+B2-C2*k2, a*A2+c*C2-e,
                         -a*A2+b*B2-c*C2*k2,
                         omega2*A2-G*G*(b-c)**2*B2*C2,
                         omega2*B2-G*G*(a-c)**2*A2*C2,
                         omega2*k2*k2*C2-G*G*(a-b)**2*A2*B2]
        else:
            e = b + t * (a - b)
            A2, B2, C2 = (e-c)/(a-c), (a-e)/(a-b), (a-e)/(a-c)
            k2 = (b-c)*(a-e)/((a-b)*(e-c))
            omega2 = G*G*(a-b)*(e-c)
            residuals = [A2+C2-1, -A2*k2+B2-C2, a*A2+c*C2-e,
                         -a*A2*k2+b*B2-c*C2,
                         omega2*A2*k2*k2-G*G*(b-c)**2*B2*C2,
                         omega2*B2-G*G*(a-c)**2*A2*C2,
                         omega2*C2-G*G*(a-b)**2*A2*B2]
        require(c < e < a and e != b)
        require(0 < k2 < 1 and omega2 > 0)
        require(row["normalized_energy_e_equals_2E_over_G2"] == f"{e.numerator}/{e.denominator}")
        require(row["amplitude_squares"] == {"A2": f"{A2.numerator}/{A2.denominator}", "B2": f"{B2.numerator}/{B2.denominator}", "C2": f"{C2.numerator}/{C2.denominator}"})
        require(row["modulus_square"] == f"{k2.numerator}/{k2.denominator}")
        require(row["frequency_square"] == f"{omega2.numerator}/{omega2.denominator}")
        require(row["exact_residuals"] == ["0/1"] * 7)
        for value in residuals:
            require(value == 0)
        period = 4 * mp.ellipk(M(k2)) / mp.sqrt(M(omega2))
        require(close_decimal(row["minimal_period"], period))
        require(close_decimal(row["normalized_kks_cap_action"], action(a, b, c, e, regime)))
        require(row["component_count"] == 2)
        expected_id = f"I{I1}-{I2}-{I3}_G{G.numerator}/{G.denominator}_{regime}_t{t.numerator}/{t.denominator}"
        require(row["row_id"] == expected_id and expected_id not in seen)
        seen.add(expected_id)
    require(len(seen) == 180)
    for row in d["equilibrium_rows"]:
        I1, I2, I3 = map(F, row["inertia"])
        a, b, c = 1/I1, 1/I2, 1/I3
        G, axis = F(row["G"]), row["axis"]
        expected = {
            1: (-G*G*(a-b)*(a-c), "elliptic_stable"),
            2: ( G*G*(a-b)*(b-c), "hyperbolic_unstable"),
            3: (-G*G*(a-c)*(b-c), "elliptic_stable"),
        }[axis]
        require(F(row["tangent_rate_square"]) == expected[0])
        require(row["classification"] == expected[1])
        require(row["signs"] == [1, -1])
    for row in d["separatrix_rows"]:
        I1, I2, I3 = map(F, row["inertia"])
        a, b, c = 1/I1, 1/I2, 1/I3
        G = F(row["G"])
        require(F(row["normalized_energy"]) == b)
        require(F(row["A2"]) == (b-c)/(a-c))
        require(F(row["C2"]) == (a-b)/(a-c))
        require(F(row["A2"]) + F(row["C2"]) == 1)
        require(F(row["rate_square"]) == G*G*(a-b)*(b-c))
        require(row["heteroclinic_branches"] == 4)
    for row in d["period_divergence_rows"]:
        values = list(map(mp.mpf, row["periods"]))
        require(len(values) == 4)
        require(all(values[i+1] > values[i] for i in range(3)))
    ft = d["fixed_time_map"]
    require(ft == {"positive_time_assumption": True, "regular_condition": "n*tau=q*T(e) for an integer q>=1", "fixed_component_dimension": 1, "equilibrium_fixed_points": 6, "separatrix_interior_fixed_points": 0, "artin_mazur_finite_count_available": False})
    require(d["theorem"]["poisson_convention"] == "{F,H}=-M dot (grad F cross grad H); Fdot={F,H}; Mdot=M cross grad H")
    require(d["theorem"]["canonical_action_charts"] == "positive low: q=arg(M1+iM2), P3=G-M3, {q,P3}=1; positive high: q=arg(M2+iM3), P1=G-M1, {q,P1}=1")
    require(d["route_a"] == {"A0": "A0_FAIL", "A1": "A1_WEAK", "A2": "A2_FAIL", "A3": "A3_FAIL", "A4": "A4_NATURAL_QUANTIZATION", "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False, "qualification": "Hamiltonian KKS flow has a canonical unitary Koopman group, but no intrinsic rational-prime origin, logarithmic clock, or target divisor"})
    require(d["summary"]["regular_rows"] == 180)
    require(d["summary"]["exact_regular_residual_cells"] == 1260)
    return n


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    assertions = check(path)
    print(json.dumps({"status": "C186_CHECKER_PASS", "assertions": assertions, "evidence_sha256": sha256(path.read_bytes()).hexdigest()}, sort_keys=True))


if __name__ == "__main__":
    main()
