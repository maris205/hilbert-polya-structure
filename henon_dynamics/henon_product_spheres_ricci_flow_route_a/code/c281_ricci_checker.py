#!/usr/bin/env python3
"""Producer-independent checker for HCS-C281 product-sphere Ricci flow."""
from __future__ import annotations

import hashlib
import json
import os
from fractions import Fraction as Q
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = Path(os.environ.get("C281_EVIDENCE", ROOT / "results/c281_ricci_evidence.json"))
SOURCE = "51fb3d46f96b854314811c1ad62d3103cd5d54e5"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
mp.mp.dps = 90
checks = 0

EXPECTED_CASES = {
    "flat_circle": ((1,), (Q(3, 2),)),
    "flat_torus3": ((1, 1, 1), (Q(1), Q(2), Q(3))),
    "round_s2": ((2,), (Q(2),)),
    "round_s5": ((5,), (Q(8),)),
    "einstein_s2xs3": ((2, 3), (Q(3), Q(6))),
    "einstein_s2xs4xs6": ((2, 4, 6), (Q(4), Q(12), Q(20))),
    "partial_unique_s2xs3": ((2, 3), (Q(2), Q(8))),
    "partial_tie_s2xs2xs4": ((2, 2, 4), (Q(2), Q(2), Q(12))),
    "mixed_flat_s1xs2xs3": ((1, 2, 3), (Q(5, 2), Q(2), Q(8))),
    "mixed_tie_s1xs3xs3": ((1, 3, 3), (Q(7), Q(4), Q(4))),
    "distinct_s2xs3xs4": ((2, 3, 4), (Q(1), Q(6), Q(15))),
    "tied_s3xs5xs7": ((3, 5, 7), (Q(4), Q(8), Q(30))),
    "round_s9": ((9,), (Q(16),)),
    "mixed_many_s1xs2xs2xs5": ((1, 2, 2, 5), (Q(2), Q(3), Q(3), Q(16))),
}

TOP_KEYS = {
    "analytic_proof_obligations", "candidate_id", "classification_contract",
    "collision_contract", "evaluation_date", "evaluator", "fixed_epoch",
    "headline", "model_contract", "nonclaims", "payload_sha256",
    "proof_contract", "regression", "route_a", "schema", "scope_flags",
    "scope_literal", "source_commit",
}
REGRESSION_KEYS = {
    "case_rows", "flow_rows", "normalized_rows", "collapse_rows",
    "asymptotic_rows", "covariance_rows", "boundary_rows", "counts",
}
CASE_ROW_KEYS = {
    "case", "dimensions", "initial_scales", "total_dimension",
    "curvature_coefficients", "factor_clocks", "maximal_forward_time",
    "collapsing_indices", "collapsing_dimension", "all_flat",
    "full_collapse", "partial_collapse", "einstein_or_flat",
    "normalized_forward_endpoint",
}
FLOW_ROW_KEYS = {
    "case", "time", "scales", "scalar_curvature", "riemann_norm_sq",
    "ricci_norm_sq", "volume_ratio", "diameter", "log_volume_derivative",
    "ode_residuals",
}
NORMALIZED_ROW_KEYS = {
    "case", "time", "normalized_time", "normalizing_scale",
    "normalized_scales", "normalized_scalar", "normalized_volume_ratio",
    "normalized_ode_rhs",
}
COLLAPSE_ROW_KEYS = {
    "case", "singular_time", "collapsing_indices", "collapsing_dimension",
    "total_dimension", "scalar_residue", "ricci_norm_residue_sq",
    "riemann_norm_residue_sq", "volume_exponent", "normalizer_exponent",
    "normalized_time_gap_exponent", "full_collapse", "partial_collapse",
    "normalized_forward_endpoint", "blowup_sphere_scales_at_s_minus_1",
    "pointed_blowup_euclidean_dimension", "type_I",
}
ASYMPTOTIC_ROW_KEYS = {
    "case", "epsilon", "normalizing_scale", "normalized_scales",
    "scaled_scalar_residue", "scaled_riemann_norm", "normalized_time_tail",
    "stationary_scale_defect",
}
COVARIANCE_ROW_KEYS = {
    "case", "permutation_preserves_classification", "scale_factor",
    "scaled_forward_time", "expected_scaled_forward_time",
    "collapsing_dimension_preserved",
}
BOUNDARY_ROW_KEYS = {"face", "status"}

EXPECTED_HEADLINE = (
    "Every product of round spheres has an exact homogeneous Ricci flow whose "
    "tied first-collapse set, Type-I model, and volume-normalized lifetime are "
    "classified in all dimensions, including flat-circle and full-torus faces."
)
EXPECTED_ANALYTIC_OBLIGATIONS = [
    "derive the coefficient ODE and maximal interval",
    "retain every d_i=1 clock as infinity",
    "prove tied-collapse curvature, volume, diameter, and Type-I limits",
    "derive the volume-normalized conjugacy and its time integral",
    "prove partial collapse gives finite normalized time and full collapse gives a stationary Einstein metric",
    "prove the pointed product shrinker times Euclidean blowup",
    "separate all-flat and one-factor boundaries",
]
EXPECTED_COLLISION_CONTRACT = {
    "registry_range": "HCS-C1 through HCS-C280 plus obstruction registry",
    "closest_distinctions": [
        "C185 is an isospectral Brockett matrix-sorting gradient flow, not a geometric PDE or collapsing metric family",
        "C270 is static Heisenberg sub-Riemannian geodesic/cut-locus geometry, not Ricci evolution",
        "C277 and C283 are linear heat-semigroup owners on function spaces, not nonlinear metric evolution",
        "C133 is metric-graph unitary scattering, not Riemannian curvature flow",
    ],
}
EXPECTED_NONCLAIMS = [
    "No rational-prime carrier, logarithmic prime clock, isolated primitive-orbit ledger, or target determinant is obtained.",
    "The word heat in general Ricci-flow background does not make this a Markov heat-semigroup or spectral-zeta paper.",
    "No surgery continuation, stability under non-product perturbations, or classification of general homogeneous Ricci flows is claimed.",
    "Finite regression cells independently test formulas but do not prove the all-parameter theorem.",
]
EXPECTED_SCOPE_FLAGS = {
    "arithmetic_local_data": False, "euler_factors": False,
    "root_numbers": False, "automorphy": False,
    "target_divisor_or_counting_law": False,
    "target_functional_equation": False, "target_zero_match": False,
    "hilbert_polya_operator": False, "route_b_authorization": False,
}


def claim(value: bool) -> None:
    global checks
    assert value
    checks += 1


def payload_hash(data: dict) -> str:
    clean = dict(data); clean.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def mq(x: Q) -> mp.mpf:
    return mp.mpf(x.numerator) / x.denominator


def close(text: str, value: mp.mpf, tol: str = "1e-64") -> bool:
    return abs(mp.mpf(text) - value) <= mp.mpf(tol) * max(1, abs(value))


def derive(dims: tuple[int, ...], scales: tuple[Q, ...]) -> dict:
    clocks = [None if d == 1 else a / (2 * (d - 1)) for d, a in zip(dims, scales)]
    finite = [x for x in clocks if x is not None]
    T = min(finite) if finite else None
    I = [] if T is None else [i for i, x in enumerate(clocks) if x == T]
    n = sum(dims); D = sum(dims[i] for i in I)
    return {"clocks": clocks, "T": T, "I": I, "n": n, "D": D, "flat": T is None, "full": T is not None and D == n}


def normalizer(dims: tuple[int, ...], scales: tuple[Q, ...], t: mp.mpf) -> mp.mpf:
    n = sum(dims); answer = mp.mpf(1)
    for d, a in zip(dims, scales):
        answer *= ((mq(a) - 2 * (d - 1) * t) / mq(a)) ** (-mp.mpf(d) / n)
    return answer


def normalized_time(dims: tuple[int, ...], scales: tuple[Q, ...], t: mp.mpf) -> mp.mpf:
    if t == 0: return mp.mpf(0)
    if t > 0: return mp.quad(lambda s: normalizer(dims, scales, s), [0, t])
    return -mp.quad(lambda s: normalizer(dims, scales, s), [t, 0])


def normalized_tail(
    dims: tuple[int, ...], scales: tuple[Q, ...], T: Q, eps: Q, D: int
) -> mp.mpf:
    """Independently regularize int_{T-eps}^T C(t)dt for D<n."""
    n = sum(dims)
    beta = mp.mpf(D) / n
    exponent = 1 / (1 - beta)
    endpoint = mq(eps)
    singular_time = mq(T)
    collapsing = set(derive(dims, scales)["I"])

    # The substitution u=eps*x^(1/(1-beta)) cancels the complete
    # u^(-beta) endpoint singularity.  Perform that cancellation before
    # numerical evaluation, independently of the producer's stored tail.
    prefactor = endpoint * exponent
    for index, (d, a0) in enumerate(zip(dims, scales)):
        if index in collapsing:
            prefactor *= (mp.mpf(2 * (d - 1)) * endpoint / mq(a0)) ** (-mp.mpf(d) / n)

    def regularized(x: mp.mpf) -> mp.mpf:
        u = endpoint * x ** exponent
        value = prefactor
        for index, (d, a0) in enumerate(zip(dims, scales)):
            if index not in collapsing:
                survivor = mq(a0) - 2 * (d - 1) * singular_time
                value *= ((survivor + 2 * (d - 1) * u) / mq(a0)) ** (-mp.mpf(d) / n)
        return value

    return mp.quad(regularized, [0, 1])


def main() -> None:
    data = json.loads(EVIDENCE.read_text())
    claim(set(data) == TOP_KEYS)
    claim(data["payload_sha256"] == payload_hash(data))
    claim(data["schema"] == "hcs-c281-product-spheres-ricci-flow-v1")
    claim(data["candidate_id"] == "HCS-C281" and data["source_commit"] == SOURCE)
    claim(data["fixed_epoch"] == 1788220800 and data["evaluation_date"] == "2026-09-01")
    claim(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER")
    claim(data["evaluator"] == {"version": "0.2.0", "sha256": EVAL})
    claim(data["headline"] == EXPECTED_HEADLINE)
    claim(data["analytic_proof_obligations"] == EXPECTED_ANALYTIC_OBLIGATIONS)
    claim(data["collision_contract"] == EXPECTED_COLLISION_CONTRACT)
    claim(data["nonclaims"] == EXPECTED_NONCLAIMS)
    claim(data["proof_contract"]["status"] == "PROVABLE AS STATED")
    claim(data["route_a"] == {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False})
    claim(data["scope_flags"] == EXPECTED_SCOPE_FLAGS)
    claim(data["model_contract"] == {
        "manifold": "M=product_i S^{d_i}, d_i positive integers",
        "metric": "g(0)=direct_sum_i a_i g_round,i with a_i>0",
        "equation": "partial_t g=-2 Ric(g)",
        "solution": "a_i(t)=a_i-2(d_i-1)t",
        "clock": "physical Ricci-flow time; normalized time tau has d tau/dt=(V(0)/V(t))^(2/n)",
        "normalization": "hat g=(V(0)/V(t))^(2/n) g has constant volume V(0)",
    })
    claim(data["classification_contract"] == {
        "factor_clock": "T_i=a_i/[2(d_i-1)] for d_i>=2 and infinity for d_i=1",
        "first_time": "T=min_i T_i; all-flat data have T=infinity",
        "collapse_set": "I={i:T_i=T}, D=sum_{i in I}d_i",
        "partial_full_gate": "D<n iff normalized endpoint finite; D=n iff data are curved Einstein and normalized flow is stationary",
        "type_I_model": "product_{i in I} S^{d_i}(-2(d_i-1)s) times R^{n-D}, s<0",
    })
    claim(data["proof_contract"] == {
        "status": "PROVABLE AS STATED",
        "dependencies": ["Ricci tensor of a round sphere", "Ricci tensor of a Riemannian product", "constant metric scaling", "elementary singular asymptotics"],
        "scope": "finite products of unit round spheres with diagonal product metrics; no quotient, surgery, nonsymmetric perturbation, or general homogeneous space",
        "novelty_boundary": "a source-local exact synthesis and executable closure; no claim to invent Ricci flow or standard product-curvature identities",
    })

    claim(set(data["regression"]) == REGRESSION_KEYS)

    cases = {}
    rows = data["regression"]["case_rows"]
    claim(len(rows) == 14)
    case_names = [row["case"] for row in rows]
    claim(len(case_names) == len(set(case_names)) and set(case_names) == set(EXPECTED_CASES))
    for row in rows:
        claim(set(row) == CASE_ROW_KEYS)
        name = row["case"]
        dims = tuple(row["dimensions"]); scales = tuple(Q(x) for x in row["initial_scales"])
        claim(name not in cases and all(d >= 1 for d in dims) and all(a > 0 for a in scales))
        claim((dims, scales) == EXPECTED_CASES[name])
        info = derive(dims, scales); cases[name] = (dims, scales, info)
        claim(row["total_dimension"] == info["n"])
        claim(row["curvature_coefficients"] == [d - 1 for d in dims])
        claim(row["factor_clocks"] == ["infinity" if x is None else f"{x.numerator}/{x.denominator}" for x in info["clocks"]])
        claim(row["maximal_forward_time"] == ("infinity" if info["T"] is None else f"{info['T'].numerator}/{info['T'].denominator}"))
        claim(row["collapsing_indices"] == info["I"] and row["collapsing_dimension"] == info["D"])
        claim(row["all_flat"] == info["flat"] and row["full_collapse"] == info["full"])
        claim(row["partial_collapse"] == (info["T"] is not None and not info["full"]))
        claim(row["einstein_or_flat"] == (info["flat"] or info["full"]))
        endpoint = "eternal_stationary_flat" if info["flat"] else "infinite_stationary_einstein" if info["full"] else "finite_partial_singularity"
        claim(row["normalized_forward_endpoint"] == endpoint)
    claim(sum(info[2]["flat"] for info in cases.values()) == 2)
    claim(sum(info[2]["full"] for info in cases.values()) == 5)

    flow = data["regression"]["flow_rows"]
    claim(len(flow) == 68)
    flow_keys = [(row["case"], Q(row["time"])) for row in flow]
    expected_flow_keys = set()
    for name, (_, _, info) in cases.items():
        times = (Q(-2), Q(0), Q(1), Q(3)) if info["flat"] else (-info["T"], Q(0), info["T"]/4, info["T"]/2, 3*info["T"]/4)
        expected_flow_keys.update((name, t) for t in times)
    claim(len(flow_keys) == len(set(flow_keys)) and set(flow_keys) == expected_flow_keys)
    for row in flow:
        claim(set(row) == FLOW_ROW_KEYS)
        dims, scales, info = cases[row["case"]]
        t = Q(row["time"])
        values = tuple(a - 2 * (d - 1) * t for d, a in zip(dims, scales))
        claim(all(a > 0 for a in values))
        claim([Q(x) for x in row["scales"]] == list(values))
        R = sum((Q(d * (d - 1), 1) / a for d, a in zip(dims, values)), Q(0))
        rm2 = sum((Q(2 * d * (d - 1), 1) / (a * a) for d, a in zip(dims, values)), Q(0))
        ric2 = sum((Q(d * (d - 1) ** 2, 1) / (a * a) for d, a in zip(dims, values)), Q(0))
        claim(Q(row["scalar_curvature"]) == R and Q(row["riemann_norm_sq"]) == rm2)
        claim(Q(row["ricci_norm_sq"]) == ric2 and Q(row["log_volume_derivative"]) == -R)
        vol = mp.mpf(1)
        for d, a0, a in zip(dims, scales, values): vol *= (mq(a) / mq(a0)) ** (mp.mpf(d) / 2)
        claim(close(row["volume_ratio"], vol))
        claim(close(row["diameter"], mp.pi * mp.sqrt(sum(mq(a) for a in values))))
        claim(len(row["scales"]) == len(dims) and len(row["ode_residuals"]) == len(dims))
        claim(all(Q(x) == 0 for x in row["ode_residuals"]))

    normalized = data["regression"]["normalized_rows"]
    claim(len(normalized) == 66)
    normalized_keys = [(row["case"], Q(row["time"])) for row in normalized]
    expected_normalized_keys = set()
    for name, (_, _, info) in cases.items():
        times = (Q(0), Q(1), Q(2)) if info["flat"] else (Q(0), info["T"]/4, info["T"]/2, 3*info["T"]/4, 7*info["T"]/8)
        expected_normalized_keys.update((name, t) for t in times)
    claim(len(normalized_keys) == len(set(normalized_keys)) and set(normalized_keys) == expected_normalized_keys)
    for row in normalized:
        claim(set(row) == NORMALIZED_ROW_KEYS)
        dims, scales, _ = cases[row["case"]]
        t = Q(row["time"]); tm = mq(t); n = sum(dims)
        values = tuple(a - 2 * (d - 1) * t for d, a in zip(dims, scales))
        c = normalizer(dims, scales, tm)
        hat = [c * mq(a) for a in values]
        R = sum(mq(Q(d * (d - 1), 1) / a) for d, a in zip(dims, values))
        hR = R / c
        claim(close(row["normalized_time"], normalized_time(dims, scales, tm), "2e-63"))
        claim(close(row["normalizing_scale"], c))
        claim(len(row["normalized_scales"]) == len(dims) and len(row["normalized_ode_rhs"]) == len(dims))
        for got, want in zip(row["normalized_scales"], hat): claim(close(got, want))
        claim(close(row["normalized_scalar"], hR))
        claim(close(row["normalized_volume_ratio"], mp.mpf(1)))
        for got, d, h in zip(row["normalized_ode_rhs"], dims, hat):
            claim(close(got, -2 * (d - 1) + 2 * hR * h / n))

    collapse = data["regression"]["collapse_rows"]
    claim(len(collapse) == 12)
    collapse_keys = [row["case"] for row in collapse]
    expected_collapse_keys = {name for name, (_, _, info) in cases.items() if not info["flat"]}
    claim(len(collapse_keys) == len(set(collapse_keys)) and set(collapse_keys) == expected_collapse_keys)
    for row in collapse:
        claim(set(row) == COLLAPSE_ROW_KEYS)
        dims, scales, info = cases[row["case"]]
        claim(Q(row["singular_time"]) == info["T"] and row["collapsing_indices"] == info["I"])
        claim(row["collapsing_dimension"] == info["D"] and row["total_dimension"] == info["n"])
        claim(Q(row["scalar_residue"]) == Q(info["D"], 2))
        claim(Q(row["ricci_norm_residue_sq"]) == Q(info["D"], 4))
        residue = sum((Q(dims[i], 2 * (dims[i] - 1)) for i in info["I"]), Q(0))
        claim(Q(row["riemann_norm_residue_sq"]) == residue)
        claim(Q(row["volume_exponent"]) == Q(info["D"], 2))
        claim(Q(row["normalizer_exponent"]) == Q(info["D"], info["n"]))
        claim(Q(row["normalized_time_gap_exponent"]) == Q(info["n"] - info["D"], info["n"]))
        claim(row["full_collapse"] == info["full"] and row["partial_collapse"] == (not info["full"]))
        endpoint = "infinite_stationary_einstein" if info["full"] else "finite_partial_singularity"
        claim(row["normalized_forward_endpoint"] == endpoint)
        claim(row["blowup_sphere_scales_at_s_minus_1"] == [2 * (dims[i] - 1) for i in info["I"]])
        claim(row["pointed_blowup_euclidean_dimension"] == info["n"] - info["D"] and row["type_I"] is True)

    asymptotic = data["regression"]["asymptotic_rows"]
    claim(len(asymptotic) == 36)
    asymptotic_keys = [(row["case"], Q(row["epsilon"])) for row in asymptotic]
    expected_asymptotic_keys = {(name, info["T"]/(2**k)) for name, (_, _, info) in cases.items()
                                if not info["flat"] for k in (4, 6, 8)}
    claim(len(asymptotic_keys) == len(set(asymptotic_keys)) and set(asymptotic_keys) == expected_asymptotic_keys)
    for row in asymptotic:
        claim(set(row) == ASYMPTOTIC_ROW_KEYS)
        dims, scales, info = cases[row["case"]]
        eps = Q(row["epsilon"]); t = info["T"] - eps
        values = tuple(a - 2 * (d - 1) * t for d, a in zip(dims, scales))
        c = normalizer(dims, scales, mq(t))
        claim(close(row["normalizing_scale"], c))
        claim(len(row["normalized_scales"]) == len(dims))
        for got, a in zip(row["normalized_scales"], values): claim(close(got, c * mq(a)))
        R = sum((Q(d * (d - 1), 1) / a for d, a in zip(dims, values)), Q(0))
        rm2 = sum((Q(2 * d * (d - 1), 1) / (a * a) for d, a in zip(dims, values)), Q(0))
        claim(close(row["scaled_scalar_residue"], mq(eps * R)))
        claim(close(row["scaled_riemann_norm"], mq(eps) * mp.sqrt(mq(rm2))))
        if info["full"]:
            claim(row["normalized_time_tail"] == "infinity")
            claim(abs(mp.mpf(row["stationary_scale_defect"])) < mp.mpf("1e-64"))
        else:
            tail = normalized_tail(dims, scales, info["T"], eps, info["D"])
            claim(close(row["normalized_time_tail"], tail, "2e-63"))
            claim(row["stationary_scale_defect"] == "not_applicable")

    covariance = data["regression"]["covariance_rows"]
    claim(len(covariance) == 14)
    covariance_keys = [row["case"] for row in covariance]
    claim(len(covariance_keys) == len(set(covariance_keys)) and set(covariance_keys) == set(cases))
    for row in covariance:
        claim(set(row) == COVARIANCE_ROW_KEYS)
        _, _, info = cases[row["case"]]
        claim(row["permutation_preserves_classification"] is True and row["collapsing_dimension_preserved"] is True)
        factor = Q(row["scale_factor"])
        expected = "infinity" if info["flat"] else f"{(factor * info['T']).numerator}/{(factor * info['T']).denominator}"
        claim(row["scaled_forward_time"] == expected == row["expected_scaled_forward_time"])

    boundaries = data["regression"]["boundary_rows"]
    expected_boundaries = {
        "one_factor": "round sphere for d>=2; stationary circle for d=1",
        "flat_factor": "d_i=1 gives c_i=0, infinite collapse clock, and constant scale",
        "all_flat": "a flat torus; unnormalized and volume-normalized flows are stationary for all time",
        "tied_clocks": "every minimizer collapses; multiplicity is retained in D and the blowup product",
        "full_collapse": "equivalent to curved Einstein data; normalized flow is stationary and forward eternal",
        "partial_collapse": "normalized time is finite; collapsed scales vanish and survivor scales diverge",
        "t_zero": "both flow gauges equal the initial metric",
        "factor_permutation_and_scaling": "permutation is gauge; common metric scaling rescales physical time",
    }
    boundary_keys = [row["face"] for row in boundaries]
    claim(len(boundaries) == 8 and len(boundary_keys) == len(set(boundary_keys)))
    claim(all(set(row) == BOUNDARY_ROW_KEYS for row in boundaries))
    claim({row["face"]: row["status"] for row in boundaries} == expected_boundaries)
    claim(data["regression"]["counts"] == {"case_rows": 14, "flow_rows": 68, "normalized_rows": 66, "collapse_rows": 12, "asymptotic_rows": 36, "covariance_rows": 14, "boundary_rows": 8})
    print(f"C281 independent checker: PASS ({checks} assertions; producer-independent geometric reconstruction)")


if __name__ == "__main__":
    main()
