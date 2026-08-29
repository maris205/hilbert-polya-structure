#!/usr/bin/env python3
"""Producer-independent exact/high-precision checker for HCS-C228."""
from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
import json
import math
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "results/c228_coagulation_evidence.json"
SOURCE_COMMIT = "489672bd36abd3a4f6da92d1446a0af575917959"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
mp.mp.dps = 90

PRE_TIMES = ["0", "1/10", "1/2", "9/10", "1"]
POST_TIMES = ["6/5", "2", "5", "10"]
TAIL_K = [20, 50, 100, 200, 500]
TOP_KEYS = {
    "schema", "candidate_id", "evaluation_date", "source_commit", "scope_literal", "evaluator",
    "headline", "frozen_object", "theorem", "coefficient_ledger", "regression",
    "exact_identities", "route_a", "scope_flags", "citations", "nonclaims", "payload_sha256",
}
SCOPE_KEYS = {
    "uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors",
    "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation",
    "claims_hilbert_polya_operator", "invokes_route_b",
}
HEADLINE = "The monodisperse product-kernel coagulation equation has an exact tree-function pregel law, a k^-5/2 gel point, and two rigorously separated postgel closures: Smoluchowski/Stockmayer and gel-reactive Flory."
FROZEN_OBJECT = {
    "smoluchowski_equation": "c_k'=1/2 sum_{i+j=k} i j c_i c_j-k c_k M1(t), M1=sum_j j c_j",
    "flory_equation": "same gain but postgel loss -k c_k M1(0), so finite clusters continue to react with gel",
    "kernel": "K(i,j)=i j",
    "initial_data": "c_1(0)=1 and c_k(0)=0 for k>1",
    "normalization": "unordered gain carries 1/2; gel time is t_g=1",
    "clock": "coagulation time t>=0",
    "tree_functions": "T(u)=sum k^(k-1)u^k/k!, T=u exp(T); U=T-T^2/2",
    "forbidden_data": "target primes/zeros, arithmetic local data, Euler factors, root numbers, automorphy, target divisor/functional equation, Hilbert-Polya operators",
}
THEOREM = {
    "pregel_coefficients": "for 0<t<=1, c_k=k^(k-2)t^(k-1)e^(-kt)/k!; at t=0 the continuous convention is c_1=1 and c_k=0 for k>1",
    "pregel_generating_functions": "as formal power series in z, G=sum k c_k z^k=T(t z e^-t)/t and C=sum c_k z^k=U(t z e^-t)/t; analytically these hold on the principal convergence disk, including 0<=z<=1, with continuous t=0 limits",
    "pregel_moments": "M0=1-t/2, M1=1, M2=(1-t)^-1, M3=(1-t)^-3 for t<1",
    "gel_point": "t_g=1 and c_k(1)~(2 pi)^(-1/2) k^(-5/2), hence M2 diverges",
    "subcritical_tail": "c_k(t)~[1/(sqrt(2 pi)t)] k^(-5/2)[t exp(1-t)]^k for 0<t<1",
    "smoluchowski_postgel": "one explicit Stockmayer continuation is c_k=k^(k-2)e^(-k)/(k! t), t>=1; it solves loss mass M1=1/t and has M0=1/(2t), M1=1/t, M2=infinity",
    "flory_postgel": "the gel-reactive continuation is c_k=k^(k-2)t^(k-1)e^(-kt)/k!, with q=M1 in (0,1) solving q=exp[-t(1-q)] and modified loss mass M1(0)=1",
    "flory_moments": "if r=tq=-W_0(-t e^-t), then M0=q-tq^2/2, M2=q/(1-r), M3=q/(1-r)^3",
    "closure_boundary": "the two postgel formulas coincide at t=1 but solve different loss terms for t>1; neither is substituted for the other",
    "uniqueness_scope": "the released algebra verifies the displayed continuations; it does not claim uniqueness among every weak postgel solution",
}
IDENTITIES = [
    {"name": "Cayley_recurrence", "formula": "(k-1)a_k=1/2 sum_{i+j=k}ij a_i a_j, a_k=k^(k-2)/k!"},
    {"name": "tree_equation", "formula": "T=u exp(T)"},
    {"name": "unrooted_tree", "formula": "U=T-T^2/2 and u U'(u)=T"},
    {"name": "moment_ODE", "formula": "M2'=M2^2 and M3'=3 M2 M3 while M1=1"},
    {"name": "critical_tail", "formula": "Stirling gives a_k e^-k~(2pi)^-1/2 k^-5/2"},
    {"name": "Stockmayer_balance", "formula": "gain=(k-1)c_k/t and loss=k c_k/t, hence c_k'=-c_k/t"},
    {"name": "Flory_balance", "formula": "gain=(k-1)c_k/t and gel-reactive loss=k c_k, matching c_k'=((k-1)/t-k)c_k"},
    {"name": "branch_separation", "formula": "for t>1, 1/t differs from q=-W0(-t e^-t)/t and the loss masses differ"},
]
CITATIONS = [
    {"id": "McLeod1962I", "doi": "10.1093/qmath/13.1.119", "role": "classical infinite coagulation equations and exact-solution context"},
    {"id": "McLeod1962II", "doi": "10.1093/qmath/13.1.193", "role": "continuation of the classical analysis"},
    {"id": "ZiffStell1980", "doi": "10.1063/1.440502", "role": "kinetics of polymer gelation and postgel conventions"},
    {"id": "NormandZambotti2011", "doi": "10.1016/j.anihpc.2010.10.005", "role": "global Smoluchowski and Flory solution theory"},
    {"id": "Norris1999", "doi": "10.1214/aoap/1029962598", "role": "uniqueness, nonuniqueness and hydrodynamic-limit boundary"},
]
NONCLAIMS = [
    "The classical tree coefficients and gelation law are not claimed as new discoveries.",
    "The pregel coefficient formula is not silently continued as a solution of the postgel Smoluchowski loss term.",
    "The explicit Stockmayer continuation is not promoted to uniqueness among all weak postgel solutions.",
    "Finite coefficient regression is not used as a proof of the infinite tail or gel point.",
    "No target arithmetic, Euler product, target functional equation, Hilbert-Polya operator, or Route-B input is claimed.",
]


def q(text: str) -> Fraction:
    return Fraction(text)


def mpq(text: str) -> mp.mpf:
    value = q(text)
    return mp.mpf(value.numerator) / value.denominator


def ftext(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def dec(value: mp.mpf, digits: int = 64) -> str:
    if abs(value) < mp.mpf("1e-82"):
        return "0.0"
    return mp.nstr(value, digits, strip_zeros=False, min_fixed=-70, max_fixed=70)


def a(k: int) -> Fraction:
    return Fraction(1) if k == 1 else Fraction(k ** (k - 2), math.factorial(k))


def ma(k: int) -> mp.mpf:
    value = a(k)
    return mp.mpf(value.numerator) / value.denominator


def standard_c(k: int, t: mp.mpf) -> mp.mpf:
    if t == 0:
        return mp.mpf(1) if k == 1 else mp.mpf(0)
    return ma(k) * t ** (k - 1) * mp.exp(-k * t)


def stockmayer_c(k: int, t: mp.mpf) -> mp.mpf:
    return ma(k) * mp.exp(-k) / t


def residual(t: mp.mpf, branch: str, mass: mp.mpf) -> mp.mpf:
    worst = mp.mpf(0)
    for k in range(1, 21):
        if branch == "stockmayer":
            ck = stockmayer_c(k, t)
            derivative = -ck / t
            getter = stockmayer_c
            loss_mass = mass
        else:
            ck = standard_c(k, t)
            derivative = ck * ((k - 1) / t - k)
            getter = standard_c
            loss_mass = mp.mpf(1)
        gain = mp.fsum(mp.mpf(i * (k - i)) * getter(i, t) * getter(k - i, t) for i in range(1, k)) / 2
        worst = max(worst, abs(derivative - (gain - k * ck * loss_mass)))
    return worst


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


class Audit:
    def __init__(self) -> None:
        self.count = 0

    def check(self, condition: bool, message: str) -> None:
        self.count += 1
        if not condition:
            raise AssertionError(message)


def validate(data: dict) -> int:
    au = Audit()
    au.check(set(data) == TOP_KEYS, "top-level schema closure")
    au.check(data["schema"] == "hcs-c228-product-kernel-gelation-v1", "schema")
    au.check(data["candidate_id"] == "HCS-C228", "candidate")
    au.check(data["evaluation_date"] == "2026-08-29", "date")
    au.check(data["source_commit"] == SOURCE_COMMIT, "source")
    au.check(data["scope_literal"] == SCOPE, "scope")
    au.check(set(data["evaluator"]) == {"path", "version", "sha256"}, "evaluator keys")
    au.check(data["evaluator"] == {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256}, "evaluator lock")
    au.check(data["payload_sha256"] == payload_hash(data), "payload hash")
    au.check(data["headline"] == HEADLINE, "headline lock")
    au.check(set(data["frozen_object"]) == {"smoluchowski_equation", "flory_equation", "kernel", "initial_data", "normalization", "clock", "tree_functions", "forbidden_data"}, "object keys")
    au.check(data["frozen_object"] == FROZEN_OBJECT, "frozen object lock")
    au.check(data["frozen_object"]["kernel"] == "K(i,j)=i j", "kernel")
    au.check("loss -k c_k M1(0)" in data["frozen_object"]["flory_equation"], "Flory convention")
    theorem_keys = {
        "pregel_coefficients", "pregel_generating_functions", "pregel_moments", "gel_point",
        "subcritical_tail", "smoluchowski_postgel", "flory_postgel", "flory_moments",
        "closure_boundary", "uniqueness_scope",
    }
    au.check(set(data["theorem"]) == theorem_keys, "theorem keys")
    au.check(data["theorem"] == THEOREM, "theorem text lock")
    au.check("solve different loss terms" in data["theorem"]["closure_boundary"], "closure boundary")
    au.check("does not claim uniqueness" in data["theorem"]["uniqueness_scope"], "uniqueness scope")

    ledger = data["coefficient_ledger"]
    au.check(set(ledger) == {"rows", "row_count"}, "coefficient ledger keys")
    au.check(ledger["row_count"] == 40 == len(ledger["rows"]), "coefficient count")
    for expected_k, row in enumerate(ledger["rows"], start=1):
        au.check(set(row) == {"k", "a_k", "recurrence_lhs", "recurrence_rhs"}, f"coefficient {expected_k} keys")
        au.check(row["k"] == expected_k, f"coefficient {expected_k} index")
        ak = a(expected_k)
        lhs = (expected_k - 1) * ak
        rhs = sum((Fraction(i * (expected_k - i), 2) * a(i) * a(expected_k - i) for i in range(1, expected_k)), Fraction(0))
        au.check(row["a_k"] == ftext(ak), f"coefficient {expected_k}")
        au.check(row["recurrence_lhs"] == ftext(lhs), f"coefficient {expected_k} lhs")
        au.check(row["recurrence_rhs"] == ftext(rhs), f"coefficient {expected_k} rhs")
        au.check(lhs == rhs, f"coefficient {expected_k} Cayley recurrence")

    regression = data["regression"]
    au.check(set(regression) == {"pregel_and_critical_rows", "smoluchowski_postgel_rows", "flory_postgel_rows", "critical_tail_rows", "serialized_cluster_cutoff", "working_decimal_digits", "serialized_significant_digits"}, "regression keys")
    au.check(regression["serialized_cluster_cutoff"] == 20, "cluster cutoff")
    au.check(regression["working_decimal_digits"] == 90, "working precision")
    au.check(regression["serialized_significant_digits"] == 64, "serialized precision")

    pre_keys = {"time", "regime", "number_density_M0", "sol_mass_M1", "second_moment_M2", "third_moment_M3", "coefficients_k1_to_20", "ode_residual_max_k20"}
    pre_rows = regression["pregel_and_critical_rows"]
    au.check([row["time"] for row in pre_rows] == PRE_TIMES, "pregel time ledger")
    for row in pre_rows:
        au.check(set(row) == pre_keys, f"pregel {row['time']} keys")
        t = mpq(row["time"])
        regime = "initial" if t == 0 else ("pregel" if t < 1 else "critical")
        au.check(row["regime"] == regime, f"pregel {t} regime")
        au.check(row["number_density_M0"] == dec(1 - t / 2), f"pregel {t} M0")
        au.check(row["sol_mass_M1"] == dec(mp.mpf(1)), f"pregel {t} M1")
        expected_m2 = dec(1 / (1 - t)) if t < 1 else "infinity"
        expected_m3 = dec(1 / (1 - t) ** 3) if t < 1 else "infinity"
        au.check(row["second_moment_M2"] == expected_m2, f"pregel {t} M2")
        au.check(row["third_moment_M3"] == expected_m3, f"pregel {t} M3")
        au.check(len(row["coefficients_k1_to_20"]) == 20, f"pregel {t} coefficient count")
        for k, value in enumerate(row["coefficients_k1_to_20"], start=1):
            au.check(value == dec(standard_c(k, t)), f"pregel {t} c{k}")
        expected_residual = "boundary_t0_exact" if t == 0 else dec(residual(t, "standard", mp.mpf(1)))
        au.check(row["ode_residual_max_k20"] == expected_residual, f"pregel {t} residual")

    smol_keys = {"time", "branch", "number_density_M0", "sol_mass_M1", "gel_fraction", "second_moment_M2", "coefficients_k1_to_20", "ode_residual_max_k20", "loss_mass_used"}
    smol_rows = regression["smoluchowski_postgel_rows"]
    au.check([row["time"] for row in smol_rows] == POST_TIMES, "Smoluchowski time ledger")
    for row in smol_rows:
        au.check(set(row) == smol_keys, f"Smoluchowski {row['time']} keys")
        t = mpq(row["time"]); mass = 1 / t
        au.check(row["branch"] == "Smoluchowski_Stockmayer", "Smoluchowski branch")
        au.check(row["number_density_M0"] == dec(1 / (2 * t)), f"Smoluchowski {t} M0")
        au.check(row["sol_mass_M1"] == dec(mass), f"Smoluchowski {t} M1")
        au.check(row["gel_fraction"] == dec(1 - mass), f"Smoluchowski {t} gel")
        au.check(row["second_moment_M2"] == "infinity", f"Smoluchowski {t} M2")
        au.check(row["loss_mass_used"] == dec(mass), f"Smoluchowski {t} loss")
        au.check(len(row["coefficients_k1_to_20"]) == 20, f"Smoluchowski {t} count")
        for k, value in enumerate(row["coefficients_k1_to_20"], start=1):
            au.check(value == dec(stockmayer_c(k, t)), f"Smoluchowski {t} c{k}")
        au.check(row["ode_residual_max_k20"] == dec(residual(t, "stockmayer", mass)), f"Smoluchowski {t} residual")

    flory_keys = {"time", "branch", "small_root_r", "sol_mass_q", "fixed_point_residual", "number_density_M0", "gel_fraction", "second_moment_M2", "third_moment_M3", "coefficients_k1_to_20", "modified_ode_residual_max_k20", "loss_mass_used"}
    flory_rows = regression["flory_postgel_rows"]
    au.check([row["time"] for row in flory_rows] == POST_TIMES, "Flory time ledger")
    for row in flory_rows:
        au.check(set(row) == flory_keys, f"Flory {row['time']} keys")
        t = mpq(row["time"])
        rooted = -mp.re(mp.lambertw(-t * mp.exp(-t), 0)); sol = rooted / t
        au.check(row["branch"] == "Flory_gel_reactive", "Flory branch")
        au.check(0 < rooted < 1 and 0 < sol < 1, f"Flory {t} small branch")
        au.check(row["small_root_r"] == dec(rooted), f"Flory {t} r")
        au.check(row["sol_mass_q"] == dec(sol), f"Flory {t} q")
        au.check(row["fixed_point_residual"] == dec(sol - mp.exp(-t * (1 - sol))), f"Flory {t} fixed point")
        au.check(row["number_density_M0"] == dec(sol - t * sol * sol / 2), f"Flory {t} M0")
        au.check(row["gel_fraction"] == dec(1 - sol), f"Flory {t} gel")
        au.check(row["second_moment_M2"] == dec(sol / (1 - rooted)), f"Flory {t} M2")
        au.check(row["third_moment_M3"] == dec(sol / (1 - rooted) ** 3), f"Flory {t} M3")
        au.check(row["loss_mass_used"] == dec(mp.mpf(1)), f"Flory {t} loss")
        au.check(len(row["coefficients_k1_to_20"]) == 20, f"Flory {t} count")
        for k, value in enumerate(row["coefficients_k1_to_20"], start=1):
            au.check(value == dec(standard_c(k, t)), f"Flory {t} c{k}")
        au.check(row["modified_ode_residual_max_k20"] == dec(residual(t, "standard", sol)), f"Flory {t} residual")
        au.check(abs(sol - 1 / t) > mp.mpf("1e-8"), f"Flory {t} differs from Stockmayer")

    tail_rows = regression["critical_tail_rows"]
    au.check([row["k"] for row in tail_rows] == TAIL_K, "tail index ledger")
    previous_error = mp.inf
    for row in tail_rows:
        au.check(set(row) == {"k", "c_k_at_t1", "scaled_tail_ratio"}, f"tail {row['k']} keys")
        k = row["k"]
        ck = ma(k) * mp.exp(-k)
        ratio = mp.sqrt(2 * mp.pi) * mp.mpf(k) ** (mp.mpf(5) / 2) * ck
        au.check(row["c_k_at_t1"] == dec(ck), f"tail {k} c")
        au.check(row["scaled_tail_ratio"] == dec(ratio), f"tail {k} ratio")
        error = abs(ratio - 1)
        au.check(error < previous_error, f"tail {k} monotone approach")
        previous_error = error

    au.check(len(data["exact_identities"]) == 8, "identity count")
    au.check(all(set(item) == {"name", "formula"} for item in data["exact_identities"]), "identity keys")
    au.check(data["exact_identities"] == IDENTITIES, "identity formula lock")
    au.check([item["name"] for item in data["exact_identities"]] == ["Cayley_recurrence", "tree_equation", "unrooted_tree", "moment_ODE", "critical_tail", "Stockmayer_balance", "Flory_balance", "branch_separation"], "identity ledger")
    route = data["route_a"]
    au.check(set(route) == {"tuple", "overall", "route_b_invocation_allowed", "strongest_positive", "strongest_failure"}, "route keys")
    au.check(route["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "route tuple")
    au.check(route["overall"] == "ROUTE_A_REJECTED", "route verdict")
    au.check(route["route_b_invocation_allowed"] is False, "Route B")
    au.check(route["strongest_positive"] == "an exact infinite-dimensional nonlinear coefficient law with gelation and a sharp postgel model boundary", "route positive lock")
    au.check(route["strongest_failure"] == "cluster size is not an arithmetic primitive owner and the tree generating functions are not a target determinant or analytic target", "route failure lock")
    au.check(set(data["scope_flags"]) == SCOPE_KEYS, "scope keys")
    au.check(all(value is False for value in data["scope_flags"].values()), "scope flags")
    au.check([c["doi"] for c in data["citations"]] == ["10.1093/qmath/13.1.119", "10.1093/qmath/13.1.193", "10.1063/1.440502", "10.1016/j.anihpc.2010.10.005", "10.1214/aoap/1029962598"], "citation ledger")
    au.check(all(set(c) == {"id", "doi", "role"} for c in data["citations"]), "citation keys")
    au.check(data["citations"] == CITATIONS, "citation role lock")
    au.check(data["nonclaims"] == NONCLAIMS, "nonclaim lock")
    return au.count


def main() -> None:
    count = validate(json.loads(EVIDENCE.read_text()))
    print(f"C228 independent checker: PASS ({count} assertions; exact recurrence and branch reconstruction)")


if __name__ == "__main__":
    main()
