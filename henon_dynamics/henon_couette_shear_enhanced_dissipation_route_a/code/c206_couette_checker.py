#!/usr/bin/env python3
"""Producer-independent exact/high-precision checker for HCS-C206."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path

import mpmath as mp


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c206_couette_evidence.json"
SOURCE_COMMIT = "d108ef46fea7a8f62490a69071a83fcbda7c113b"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
HEADLINE = "The Couette advection-diffusion semigroup has an exact all-parameter Fourier formula, sharp sector norm, and complete inviscid, diffusive, recurrence, and trace-class boundaries"
WORKING_DECIMAL_DIGITS = 100
SERIALIZED_SIGNIFICANT_DIGITS = 82


def payload_hash(data: dict) -> str:
    body = dict(data); body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def mpq(q: F) -> mp.mpf:
    return mp.mpf(q.numerator) / q.denominator


def significant_digits(value: str) -> int:
    """Count decimal significant digits in a fixed/scientific mpmath string."""
    mantissa = value.lower().split("e", 1)[0].lstrip("+-").replace(".", "")
    significant = mantissa.lstrip("0")
    return len(significant) if significant else 1


def main() -> None:
    parser = argparse.ArgumentParser(); parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    data = json.loads(parser.parse_args().evidence.read_text())
    mp.mp.dps = WORKING_DECIMAL_DIGITS
    assertions = 0
    def check(cond, msg):
        nonlocal assertions; assertions += 1
        if not cond: raise AssertionError(msg)
    def keys(obj, expected, where):
        check(isinstance(obj, dict), where + " type"); check(set(obj) == set(expected), where + " keys")

    keys(data, {"schema","candidate_id","evaluation_date","source_commit","scope_literal","evaluator","headline","frozen_object","theorem","regression","summary","route_a","scope_flags","citations","nonclaims","payload_sha256"}, "top")
    keys(data["evaluator"], {"path","version","sha256"}, "evaluator")
    keys(data["frozen_object"], {"phase_space","equation","parameters","fourier_convention","transformed_equation","clock"}, "frozen")
    keys(data["theorem"], {"semigroup","sector_norm","sector_norm_attainment","composition","enhanced_scale","inviscid","boundaries","periodic_states","trace_stop","reversal"}, "theorem")
    keys(data["regression"], {"fourier_cells","composition_cells"}, "regression")
    keys(data["summary"], {"fourier_cells","composition_cells","a_values","nu_values","k_values","time_values","eta_values","working_decimal_digits","serialized_significant_digits","serialized_decimal_fields"}, "summary")
    keys(data["route_a"], {"tuple","overall","route_b_invocation_allowed","strongest_positive","strongest_failure"}, "route")
    expected_flags = {"uses_target_zero_table","uses_prime_table","claims_arithmetic_local_data","claims_euler_factors","claims_root_numbers","claims_automorphy","claims_target_divisor_or_functional_equation","claims_hilbert_polya_operator","invokes_route_b"}
    keys(data["scope_flags"], expected_flags, "flags")
    check(data["payload_sha256"] == payload_hash(data), "payload hash")
    check(data["schema"] == "hcs-c206-couette-v1", "schema")
    check(data["candidate_id"] == "HCS-C206", "candidate")
    check(data["evaluation_date"] == "2026-08-27", "date")
    check(data["source_commit"] == SOURCE_COMMIT, "source")
    check(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    check(data["evaluator"] == {"path":"flow_systems/skills/route-a-evaluator.md","version":"0.2.0","sha256":EVALUATOR_SHA256}, "evaluator lock")
    check(data["headline"] == HEADLINE, "headline")
    check(data["frozen_object"]["fourier_convention"].endswith("dy dx/(2pi)"), "Fourier convention")
    check(data["route_a"]["tuple"] == ["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"], "route tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_REJECTED", "overall")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "route B")
    check(all(value is False for value in data["scope_flags"].values()), "scope flags")
    check(data["citations"] == [{"key":"BMV2016","claim":"Couette enhanced-dissipation and inviscid-damping context; not ownership of this package's elementary Fourier derivation","doi":"10.1007/s00205-015-0917-3"}], "citation lock")

    tol = mp.mpf("2e-78")
    rows = data["regression"]["fourier_cells"]
    check(len(rows) == 675, "row count")
    zero_a = zero_nu = zero_k = zero_t = 0
    for i, row in enumerate(rows):
        keys(row, {"case_id","a","nu","k","t","eta","shift","integrated_vertical_frequency","completed_square","dissipation_exponent","sector_minimum","multiplier","sector_norm"}, f"row {i}")
        a, nu, k, t, eta = [F(row[name]) for name in ("a","nu","k","t","eta")]
        check(nu >= 0 and t >= 0, "domain")
        zero_a += a == 0; zero_nu += nu == 0; zero_k += k == 0; zero_t += t == 0
        shift = eta + a*k*t
        integral = eta*eta*t + a*k*eta*t*t + a*a*k*k*t**3/F(3)
        square = t*(eta+a*k*t/F(2))**2 + a*a*k*k*t**3/F(12)
        diss = k*k*t + integral
        minimum = k*k*t + a*a*k*k*t**3/F(12)
        check(F(row["shift"]) == shift, "shift")
        check(F(row["integrated_vertical_frequency"]) == integral, "integral")
        check(F(row["completed_square"]) == square == integral, "square")
        check(F(row["dissipation_exponent"]) == diss, "dissipation")
        check(F(row["sector_minimum"]) == minimum, "minimum")
        multiplier = mp.e ** (-mpq(nu*diss)); norm = mp.e ** (-mpq(nu*minimum))
        check(abs(mp.mpf(row["multiplier"])-multiplier) < tol, "multiplier")
        check(abs(mp.mpf(row["sector_norm"])-norm) < tol, "norm")
        check(significant_digits(row["multiplier"]) == SERIALIZED_SIGNIFICANT_DIGITS, "multiplier serialized digits")
        check(significant_digits(row["sector_norm"]) == SERIALIZED_SIGNIFICANT_DIGITS, "norm serialized digits")
        check(minimum >= 0 and diss >= minimum, "positivity")
        if nu == 0 or t == 0:
            check(mp.mpf(row["multiplier"]) == 1 and mp.mpf(row["sector_norm"]) == 1, "unitary/identity boundary")
        if k == 0:
            check(F(row["sector_minimum"]) == 0, "k0 norm boundary")

    compositions = data["regression"]["composition_cells"]
    check(len(compositions) == 54, "composition count")
    for i, row in enumerate(compositions):
        keys(row, {"a","k","eta","t","s","first_then_second","combined","final_shift"}, f"composition {i}")
        a,k,eta,t,s = [F(row[name]) for name in ("a","k","eta","t","s")]
        def d(time, freq):
            return k*k*time + freq*freq*time + a*k*freq*time*time + a*a*k*k*time**3/F(3)
        check(F(row["first_then_second"]) == d(t,eta)+d(s,eta+a*k*t), "composition left")
        check(F(row["combined"]) == d(t+s,eta), "composition right")
        check(F(row["first_then_second"]) == F(row["combined"]), "semigroup")
        check(F(row["final_shift"]) == eta+a*k*(t+s), "shift composition")

    summary = data["summary"]
    check(summary == {"fourier_cells":675,"composition_cells":54,"a_values":5,"nu_values":3,"k_values":5,"time_values":3,"eta_values":3,"working_decimal_digits":WORKING_DECIMAL_DIGITS,"serialized_significant_digits":SERIALIZED_SIGNIFICANT_DIGITS,"serialized_decimal_fields":1350}, "summary exact")
    check(zero_a == 135 and zero_nu == 225 and zero_k == 135 and zero_t == 225, "boundary populations")
    expected_periodic = "if nu>0, S_T f=f in L2 for T>0 implies f=0; if nu=0 and a T is nonzero, the T-periodic states are exactly the streamwise means k=0"
    check(data["theorem"]["periodic_states"] == expected_periodic, "periodic scope")
    expected_attainment = "the norm value is exact and sharp; for nu*t>0 no nonzero L2 vector attains it because the unique maximizing frequency is a null set, while frequency-localized packets approach it; for nu*t=0 the evolution is unitary and every nonzero vector attains the norm"
    check(data["theorem"]["sector_norm_attainment"] == expected_attainment, "norm attainment boundary")
    check("noncompact" in data["theorem"]["trace_stop"] and "not trace class" in data["theorem"]["trace_stop"], "trace stop")
    print(json.dumps({"status":"C206_CHECKER_PASS","assertions":assertions,"fourier_cells":len(rows),"composition_cells":len(compositions)}, sort_keys=True))


if __name__ == "__main__":
    main()
