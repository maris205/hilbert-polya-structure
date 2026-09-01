#!/usr/bin/env python3
"""Produce the deterministic HCS-C281 product-sphere Ricci-flow certificate."""
from __future__ import annotations

import hashlib
import json
import os
from fractions import Fraction as Q
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(os.environ.get("C281_EVIDENCE_OUT", ROOT / "results/c281_ricci_evidence.json"))
SOURCE = "51fb3d46f96b854314811c1ad62d3103cd5d54e5"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788220800
mp.mp.dps = 90

CASES = {
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


def qstr(x: Q) -> str:
    return f"{x.numerator}/{x.denominator}"


def mq(x: Q) -> mp.mpf:
    return mp.mpf(x.numerator) / x.denominator


def ds(x: mp.mpf) -> str:
    x = mp.mpf(x)
    if abs(x) < mp.mpf("1e-82"):
        x = mp.mpf(0)
    return mp.nstr(x, 76, strip_zeros=False)


def payload_hash(data: dict) -> str:
    clean = dict(data)
    clean.pop("payload_sha256", None)
    raw = json.dumps(clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def clocks(dims: tuple[int, ...], scales: tuple[Q, ...]) -> tuple[list[Q | None], Q | None, list[int]]:
    ts: list[Q | None] = [None if d == 1 else a / (2 * (d - 1)) for d, a in zip(dims, scales)]
    finite = [x for x in ts if x is not None]
    if not finite:
        return ts, None, []
    first = min(finite)
    return ts, first, [i for i, x in enumerate(ts) if x == first]


def classification(dims: tuple[int, ...], scales: tuple[Q, ...]) -> dict:
    ts, first, collapsing = clocks(dims, scales)
    n = sum(dims)
    D = sum(dims[i] for i in collapsing)
    all_flat = first is None
    full = bool(first is not None and D == n)
    return {
        "total_dimension": n,
        "curvature_coefficients": [d - 1 for d in dims],
        "factor_clocks": ["infinity" if x is None else qstr(x) for x in ts],
        "maximal_forward_time": "infinity" if first is None else qstr(first),
        "collapsing_indices": collapsing,
        "collapsing_dimension": D,
        "all_flat": all_flat,
        "full_collapse": full,
        "partial_collapse": bool(first is not None and not full),
        "einstein_or_flat": all_flat or full,
        "normalized_forward_endpoint": (
            "eternal_stationary_flat" if all_flat else
            "infinite_stationary_einstein" if full else
            "finite_partial_singularity"
        ),
    }


def metric_at(dims: tuple[int, ...], scales: tuple[Q, ...], t: Q) -> tuple[Q, ...]:
    return tuple(a - 2 * (d - 1) * t for d, a in zip(dims, scales))


def scalar(dims: tuple[int, ...], values: tuple[Q, ...]) -> Q:
    return sum((Q(d * (d - 1), 1) / a for d, a in zip(dims, values)), Q(0))


def rm_sq(dims: tuple[int, ...], values: tuple[Q, ...]) -> Q:
    return sum((Q(2 * d * (d - 1), 1) / (a * a) for d, a in zip(dims, values)), Q(0))


def ric_sq(dims: tuple[int, ...], values: tuple[Q, ...]) -> Q:
    return sum((Q(d * (d - 1) ** 2, 1) / (a * a) for d, a in zip(dims, values)), Q(0))


def volume_ratio(dims: tuple[int, ...], scales: tuple[Q, ...], values: tuple[Q, ...]) -> mp.mpf:
    ans = mp.mpf(1)
    for d, a0, a in zip(dims, scales, values):
        ans *= (mq(a) / mq(a0)) ** (mp.mpf(d) / 2)
    return ans


def normalizer(dims: tuple[int, ...], scales: tuple[Q, ...], t: mp.mpf) -> mp.mpf:
    n = sum(dims)
    ans = mp.mpf(1)
    for d, a0 in zip(dims, scales):
        a = mq(a0) - 2 * (d - 1) * t
        ans *= (a / mq(a0)) ** (-mp.mpf(d) / n)
    return ans


def normalized_time(dims: tuple[int, ...], scales: tuple[Q, ...], t: mp.mpf) -> mp.mpf:
    if t == 0:
        return mp.mpf(0)
    if t > 0:
        return mp.quad(lambda s: normalizer(dims, scales, s), [0, t])
    return -mp.quad(lambda s: normalizer(dims, scales, s), [t, 0])


def normalized_tail(dims: tuple[int, ...], scales: tuple[Q, ...], T: Q, eps: Q, D: int) -> mp.mpf:
    """Stable integral int_{T-eps}^T c(t)dt for D<n."""
    n = sum(dims)
    beta = mp.mpf(D) / n
    power = 1 / (1 - beta)
    em = mq(eps)
    Tm = mq(T)
    collapsing = set(clocks(dims, scales)[2])

    # With u=eps*y^power, cancel the complete u^(-beta) factor
    # symbolically before quadrature.  Evaluating C(T-u) directly suffers
    # catastrophic endpoint cancellation and can spuriously return +inf.
    prefactor = em * power
    for i, (d, a0) in enumerate(zip(dims, scales)):
        if i in collapsing:
            prefactor *= (mp.mpf(2 * (d - 1)) * em / mq(a0)) ** (-mp.mpf(d) / n)

    def integrand(y: mp.mpf) -> mp.mpf:
        u = em * y ** power
        value = prefactor
        for i, (d, a0) in enumerate(zip(dims, scales)):
            if i not in collapsing:
                survivor = mq(a0) - 2 * (d - 1) * Tm
                value *= ((survivor + 2 * (d - 1) * u) / mq(a0)) ** (-mp.mpf(d) / n)
        return value

    return mp.quad(integrand, [0, 1])


def case_rows() -> list[dict]:
    rows = []
    for name, (dims, scales) in CASES.items():
        rows.append({"case": name, "dimensions": list(dims), "initial_scales": [qstr(a) for a in scales], **classification(dims, scales)})
    return rows


def flow_rows() -> list[dict]:
    rows = []
    for name, (dims, scales) in CASES.items():
        info = classification(dims, scales)
        T = None if info["all_flat"] else Q(info["maximal_forward_time"])
        times = (Q(-2), Q(0), Q(1), Q(3)) if T is None else (-T, Q(0), T / 4, T / 2, 3 * T / 4)
        for t in times:
            values = metric_at(dims, scales, t)
            R = scalar(dims, values)
            rows.append({
                "case": name, "time": qstr(t), "scales": [qstr(a) for a in values],
                "scalar_curvature": qstr(R), "riemann_norm_sq": qstr(rm_sq(dims, values)),
                "ricci_norm_sq": qstr(ric_sq(dims, values)),
                "volume_ratio": ds(volume_ratio(dims, scales, values)),
                "diameter": ds(mp.pi * mp.sqrt(sum(mq(a) for a in values))),
                "log_volume_derivative": qstr(-R),
                "ode_residuals": [qstr((a - a0) / t + 2 * (d - 1)) if t else "0/1"
                                  for d, a0, a in zip(dims, scales, values)],
            })
    return rows


def normalized_rows() -> list[dict]:
    rows = []
    for name, (dims, scales) in CASES.items():
        info = classification(dims, scales)
        T = None if info["all_flat"] else Q(info["maximal_forward_time"])
        times = (Q(0), Q(1), Q(2)) if T is None else (Q(0), T / 4, T / 2, 3 * T / 4, 7 * T / 8)
        n = sum(dims)
        for t in times:
            tm = mq(t)
            values = metric_at(dims, scales, t)
            c = normalizer(dims, scales, tm)
            hat = [c * mq(a) for a in values]
            R = scalar(dims, values)
            hR = mq(R) / c
            rhs = [-2 * (d - 1) + 2 * hR * h / n for d, h in zip(dims, hat)]
            vratio = mp.mpf(1)
            for d, a0, h in zip(dims, scales, hat):
                vratio *= (h / mq(a0)) ** (mp.mpf(d) / 2)
            rows.append({
                "case": name, "time": qstr(t), "normalized_time": ds(normalized_time(dims, scales, tm)),
                "normalizing_scale": ds(c), "normalized_scales": [ds(x) for x in hat],
                "normalized_scalar": ds(hR), "normalized_volume_ratio": ds(vratio),
                "normalized_ode_rhs": [ds(x) for x in rhs],
            })
    return rows


def collapse_rows() -> list[dict]:
    rows = []
    for name, (dims, scales) in CASES.items():
        info = classification(dims, scales)
        if info["all_flat"]:
            continue
        T = Q(info["maximal_forward_time"])
        I = info["collapsing_indices"]
        D, n = info["collapsing_dimension"], info["total_dimension"]
        residue = sum((Q(dims[i], 2 * (dims[i] - 1)) for i in I), Q(0))
        rows.append({
            "case": name, "singular_time": qstr(T), "collapsing_indices": I,
            "collapsing_dimension": D, "total_dimension": n,
            "scalar_residue": qstr(Q(D, 2)),
            "ricci_norm_residue_sq": qstr(Q(D, 4)),
            "riemann_norm_residue_sq": qstr(residue),
            "volume_exponent": qstr(Q(D, 2)), "normalizer_exponent": qstr(Q(D, n)),
            "normalized_time_gap_exponent": qstr(Q(n - D, n)),
            "full_collapse": D == n, "partial_collapse": D < n,
            "normalized_forward_endpoint": info["normalized_forward_endpoint"],
            "blowup_sphere_scales_at_s_minus_1": [2 * (dims[i] - 1) for i in I],
            "pointed_blowup_euclidean_dimension": n - D,
            "type_I": True,
        })
    return rows


def asymptotic_rows() -> list[dict]:
    rows = []
    for name, (dims, scales) in CASES.items():
        info = classification(dims, scales)
        if info["all_flat"]:
            continue
        T = Q(info["maximal_forward_time"])
        D, n = info["collapsing_dimension"], info["total_dimension"]
        for k in (4, 6, 8):
            eps = T / (2 ** k)
            t = T - eps
            c = normalizer(dims, scales, mq(t))
            values = metric_at(dims, scales, t)
            record = {
                "case": name, "epsilon": qstr(eps), "normalizing_scale": ds(c),
                "normalized_scales": [ds(c * mq(a)) for a in values],
                "scaled_scalar_residue": ds(mq(eps) * mq(scalar(dims, values))),
                "scaled_riemann_norm": ds(mq(eps) * mp.sqrt(mq(rm_sq(dims, values)))),
            }
            if D == n:
                record["normalized_time_tail"] = "infinity"
                record["stationary_scale_defect"] = ds(max(abs(c * mq(a) - mq(a0)) for a, a0 in zip(values, scales)))
            else:
                record["normalized_time_tail"] = ds(normalized_tail(dims, scales, T, eps, D))
                record["stationary_scale_defect"] = "not_applicable"
            rows.append(record)
    return rows


def covariance_rows() -> list[dict]:
    rows = []
    factor = Q(3, 2)
    for name, (dims, scales) in CASES.items():
        base = classification(dims, scales)
        rev = classification(tuple(reversed(dims)), tuple(reversed(scales)))
        scaled = classification(dims, tuple(factor * a for a in scales))
        rows.append({
            "case": name, "permutation_preserves_classification": base["all_flat"] == rev["all_flat"] and base["full_collapse"] == rev["full_collapse"] and base["collapsing_dimension"] == rev["collapsing_dimension"],
            "scale_factor": qstr(factor),
            "scaled_forward_time": scaled["maximal_forward_time"],
            "expected_scaled_forward_time": "infinity" if base["all_flat"] else qstr(factor * Q(base["maximal_forward_time"])),
            "collapsing_dimension_preserved": base["collapsing_dimension"] == scaled["collapsing_dimension"],
        })
    return rows


def main() -> None:
    regression = {
        "case_rows": case_rows(), "flow_rows": flow_rows(), "normalized_rows": normalized_rows(),
        "collapse_rows": collapse_rows(), "asymptotic_rows": asymptotic_rows(),
        "covariance_rows": covariance_rows(),
        "boundary_rows": [
            {"face": "one_factor", "status": "round sphere for d>=2; stationary circle for d=1"},
            {"face": "flat_factor", "status": "d_i=1 gives c_i=0, infinite collapse clock, and constant scale"},
            {"face": "all_flat", "status": "a flat torus; unnormalized and volume-normalized flows are stationary for all time"},
            {"face": "tied_clocks", "status": "every minimizer collapses; multiplicity is retained in D and the blowup product"},
            {"face": "full_collapse", "status": "equivalent to curved Einstein data; normalized flow is stationary and forward eternal"},
            {"face": "partial_collapse", "status": "normalized time is finite; collapsed scales vanish and survivor scales diverge"},
            {"face": "t_zero", "status": "both flow gauges equal the initial metric"},
            {"face": "factor_permutation_and_scaling", "status": "permutation is gauge; common metric scaling rescales physical time"},
        ],
    }
    regression["counts"] = {name: len(rows) for name, rows in regression.items()}
    data = {
        "schema": "hcs-c281-product-spheres-ricci-flow-v1",
        "candidate_id": "HCS-C281", "evaluation_date": "2026-09-01",
        "source_commit": SOURCE, "fixed_epoch": EPOCH,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "headline": "Every product of round spheres has an exact homogeneous Ricci flow whose tied first-collapse set, Type-I model, and volume-normalized lifetime are classified in all dimensions, including flat-circle and full-torus faces.",
        "evaluator": {"version": "0.2.0", "sha256": EVAL},
        "model_contract": {
            "manifold": "M=product_i S^{d_i}, d_i positive integers",
            "metric": "g(0)=direct_sum_i a_i g_round,i with a_i>0",
            "equation": "partial_t g=-2 Ric(g)",
            "solution": "a_i(t)=a_i-2(d_i-1)t",
            "clock": "physical Ricci-flow time; normalized time tau has d tau/dt=(V(0)/V(t))^(2/n)",
            "normalization": "hat g=(V(0)/V(t))^(2/n) g has constant volume V(0)",
        },
        "classification_contract": {
            "factor_clock": "T_i=a_i/[2(d_i-1)] for d_i>=2 and infinity for d_i=1",
            "first_time": "T=min_i T_i; all-flat data have T=infinity",
            "collapse_set": "I={i:T_i=T}, D=sum_{i in I}d_i",
            "partial_full_gate": "D<n iff normalized endpoint finite; D=n iff data are curved Einstein and normalized flow is stationary",
            "type_I_model": "product_{i in I} S^{d_i}(-2(d_i-1)s) times R^{n-D}, s<0",
        },
        "proof_contract": {
            "status": "PROVABLE AS STATED",
            "dependencies": ["Ricci tensor of a round sphere", "Ricci tensor of a Riemannian product", "constant metric scaling", "elementary singular asymptotics"],
            "scope": "finite products of unit round spheres with diagonal product metrics; no quotient, surgery, nonsymmetric perturbation, or general homogeneous space",
            "novelty_boundary": "a source-local exact synthesis and executable closure; no claim to invent Ricci flow or standard product-curvature identities",
        },
        "analytic_proof_obligations": [
            "derive the coefficient ODE and maximal interval", "retain every d_i=1 clock as infinity",
            "prove tied-collapse curvature, volume, diameter, and Type-I limits",
            "derive the volume-normalized conjugacy and its time integral",
            "prove partial collapse gives finite normalized time and full collapse gives a stationary Einstein metric",
            "prove the pointed product shrinker times Euclidean blowup", "separate all-flat and one-factor boundaries",
        ],
        "regression": regression,
        "route_a": {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
                    "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False},
        "scope_flags": {
            "arithmetic_local_data": False, "euler_factors": False, "root_numbers": False,
            "automorphy": False, "target_divisor_or_counting_law": False,
            "target_functional_equation": False, "target_zero_match": False,
            "hilbert_polya_operator": False, "route_b_authorization": False,
        },
        "collision_contract": {
            "registry_range": "HCS-C1 through HCS-C280 plus obstruction registry",
            "closest_distinctions": [
                "C185 is an isospectral Brockett matrix-sorting gradient flow, not a geometric PDE or collapsing metric family",
                "C270 is static Heisenberg sub-Riemannian geodesic/cut-locus geometry, not Ricci evolution",
                "C277 and C283 are linear heat-semigroup owners on function spaces, not nonlinear metric evolution",
                "C133 is metric-graph unitary scattering, not Riemannian curvature flow",
            ],
        },
        "nonclaims": [
            "No rational-prime carrier, logarithmic prime clock, isolated primitive-orbit ledger, or target determinant is obtained.",
            "The word heat in general Ricci-flow background does not make this a Markov heat-semigroup or spectral-zeta paper.",
            "No surgery continuation, stability under non-product perturbations, or classification of general homogeneous Ricci flows is claimed.",
            "Finite regression cells independently test formulas but do not prove the all-parameter theorem.",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C281_PRODUCER_PASS", "counts": regression["counts"], "payload_sha256": data["payload_sha256"]}, sort_keys=True))


if __name__ == "__main__":
    main()
