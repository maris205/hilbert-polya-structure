#!/usr/bin/env python3
"""Generate and strictly verify the Paper-13 deterministic controls package.

All control arithmetic is integral.  Generation is allowed only into an
existing empty directory.  ``--verify-only`` computes the complete expected
package in memory and never opens a controlled artifact for writing.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import io
import json
import os
import stat
import sys
import unittest
from fractions import Fraction
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Mapping, MutableMapping, Sequence, Tuple


SCHEMA_V1 = "paper13-circle-twists-controls/1"
SCHEMA_V2 = "paper13-circle-twists-controls/2"
MANIFEST_SCHEMA = "paper13-circle-twists-controls-manifest/2"
PACKAGE_ID = "paper13-circle-twists-controls-v2"

PAPER_DIR = Path(__file__).resolve().parents[1]
WORKSPACE_ROOT = PAPER_DIR.parents[1]
RESULTS_DIR = PAPER_DIR / "results"

DESIGN_HEAD = {
    "path": "notes/phase3_control_design_amendment_v2.md",
    "sha256": "0c0113cff7cf7853d2f4e90ab311ace347f0bebbd8bbf36ab38501fd279c54d9",
}

BASE_BINDINGS = {
    "notes/research_protocol.md": "519563a28c3f11e3b3853f6875a84191444a68cd2c032c4cfcf69ca4152d5064",
    "notes/candidate_lock.md": "8cc0d08971762aa784afe1c844215353f170a75a3c0ab892415458ab010d0266",
    "notes/pipeline_state.md": "d98bf49d2eb5c1905ea3625251d787b247f3cf19577ff40f8bc0136186280fd5",
    "notes/phase1_amendment_v1.md": "ea5242ba6a8a1f2f867e8b258abc802fdeaace54db76629f0a9f0629e3e90d27",
    "notes/phase1_final_gate.md": "8a97a0bedcb048f1c9aa7db18d43bde45b17f1d7e92d38d2eeace688c64aee19",
    "notes/phase2_novelty_search.md": "444507f623a998152fdc8e427ee8a3f917c11d5823278b110d431dbcacac6eea",
    "notes/phase2_convention_owner_audit.md": "498830945b10a9213da945710d21b7ea74d9e0747864e23ca6223efc9bb74f52",
    "notes/phase2_framework_source_audit.md": "b47b1d6319c8419d96ca8679e3ff13b531a58f06a8b14afd95ec11f773345592",
    "notes/phase2_final_review.md": "ffcfbac5768fc409b3fa9e5df4f3b46a2366f553373664c78f4364d456854cd9",
    "notes/sources/framework_source_manifest.md": "4712cabd696d6d00205eb1eddd3c0d2dbf6706bfa14c097690a278941128606e",
    "notes/sources/framework_sources.sha256": "7fe6067bfc8e16e8b0447df295a887d48c2c04fa5ba25c9cca8acc7afade733f",
    "notes/sources/.gitignore": "c36e58e6a0e338579a7be747879a2891b023bfb79a676da58afca5e1b94c86be",
}

V2_BINDINGS = {
    "notes/phase3_control_design_lock.md": "900c541713b1711bdab7fa0d264355b6d8ee27014094e60eac6aabe38190604c",
    "notes/phase3_control_design_amendment_v1.md": "5c9caea983b0047c4b16d0437c23b117a6b8150bbeb67b79c60fb9b2ba6a737e",
    "notes/phase3_control_design_review.md": "bf56b96e19b682600ed5de43f7df51ef381fe82d4e12363f66cd1e7d2a5a5184",
    "notes/phase3_standalone_review.md": "0397e1555a1ff07d30f06c3182b6cf570228ccd3e8db9e3c96666d118079c224",
    "notes/phase3_standalone_amendment_v2.md": "99c796bffe24f262d8ac8458b21fd253451bca51bac4b283660dab319992ed82",
    "notes/phase3_standalone_amendment_v2_ownership_addendum.md": "d9523d1692d60fbdff7bbf5ab6c00d44bdcd26f02dc5cdeeba8c7ba43d78a39f",
    "notes/phase3_v2_methodology_review.md": "96a5067015847ff88155b91658ae94e9ef5a6355ae176c1945644b3e729f4f74",
    "notes/phase3_v2_devils_advocate.md": "1c6bbb0bc7d3fc366de4d8a4eb869d4d4708f19647f10d780be095ac9e81f110",
    "notes/phase3_v2_source_feasibility.md": "3ce4e8db7914c0053a31b7e0e08e8f0fe02e0b2db15620f194c1ccae5ffeb320",
    "notes/phase3_v2_design_gate.md": "0094462b1e06cde0cf1fcc3536c608dcd96ef1e9eb0d85a0714df1666b799706",
    "papers/2-flow-zeta/paper/manuscript.tex": "72c34a0a30279ed7c070917a2c9242b8e9cb0a37a56779c246fa2cae04097fdc",
    "papers/2-flow-zeta/notes/proof_audit.md": "aaab83c32eb9d6c172be192dbb14acc6ed927a972d61c24a90dbfe94ecd0dbae",
}

BINDINGS = {**BASE_BINDINGS, **V2_BINDINGS}

IMPLEMENTATION_PATHS = (
    "code/README.md",
    "code/generate_controls.py",
    "code/test_controls.py",
    "experiments/README.md",
    "experiments/reproduce.sh",
    "results/README.md",
)

ARTIFACT_ORDER = (
    "nerve_factorization_controls.csv",
    "circle_multiplier_cocycle_controls.csv",
    "lift_integer_defect_controls.csv",
    "gauge_coboundary_controls.csv",
    "twisted_convolution_controls.csv",
    "twisted_involution_controls.csv",
    "completion_gauge_controls.csv",
    "action_period_nonretention_controls.csv",
    "negative_domain_controls.csv",
    "actual_standard_support_transfer_controls.csv",
    "target_summary.csv",
    "completion_corona_controls_v2.csv",
)

HEADERS = {
    "nerve_factorization_controls.csv": "schema_version,row_id,owner_case,degree,cochain_profile,unit_id,t,u,actual_exp_mod24,time_exp_mod24,normalized,factors_through_time,case_kind,negative_reason,oracle,tolerance,status".split(","),
    "circle_multiplier_cocycle_controls.csv": "schema_version,row_id,k_index,t,u,v,sigma_tu_exp,sigma_tplusu_v_exp,sigma_uv_exp,sigma_t_uplusv_exp,lhs_exp_mod24,rhs_exp_mod24,norm_t0,norm_0u,cocycle_holds,case_kind,negative_reason,oracle,tolerance,status".split(","),
    "lift_integer_defect_controls.csv": "schema_version,row_id,k_index,t,u,v,r_tu,r_tplusu_v,r_uv,r_t_uplusv,defect_numerator_24,defect_multiple_2pi,is_integer_multiple,normalization_axes,cocycle_mod24,case_kind,negative_reason,oracle,tolerance,status".split(","),
    "gauge_coboundary_controls.csv": "schema_version,row_id,k_index,t,u,alpha_t_exp,alpha_u_exp,alpha_tplusu_exp,delta_alpha_exp,sigma_tu_exp,quotient_sigma_over_one_exp,gauge_direction,normalized_alpha,coboundary_match,case_kind,negative_reason,oracle,tolerance,status".split(","),
    "twisted_convolution_controls.csv": "schema_version,row_id,fixture_id,k_index,t,fg_re,fg_im,left_assoc_re,left_assoc_im,right_assoc_re,right_assoc_im,gauge_product_re,gauge_product_im,untwisted_of_gauged_re,untwisted_of_gauged_im,fg_support_within_minkowski,associativity_holds,gauge_product_holds,case_kind,negative_reason,oracle,tolerance,status".split(","),
    "twisted_involution_controls.csv": "schema_version,row_id,fixture_id,k_index,t,f_starstar_re,f_starstar_im,f_re,f_im,fg_star_re,fg_star_im,gstar_fstar_re,gstar_fstar_im,actual_star_re,actual_star_im,time_star_re,time_star_im,sigma_inverse_symmetry,star_involutive,anti_multiplicative,actual_time_star_match,case_kind,negative_reason,oracle,tolerance,status".split(","),
    "completion_gauge_controls.csv": "schema_version,row_id,fixture_id,k_index,character_m,s,u,t,projective_lhs_re,projective_lhs_im,projective_rhs_re,projective_rhs_im,intertwiner_lhs_re,intertwiner_lhs_im,intertwiner_rhs_re,intertwiner_rhs_im,xi_norm_sq,character_times_xi_norm_sq,projective_holds,intertwiner_holds,choice_map_holds,character_isometry_holds,completion_scope,case_kind,negative_reason,oracle,tolerance,status".split(","),
    "action_period_nonretention_controls.csv": "schema_version,row_id,action_case,component_id,stabilizer_literal,orbit_count_class,k_index,global_time_sample_class,isotropy_restriction_sample_class,test_algebra_sample_signature,full_sample_signature,reduced_sample_signature,dense_h_scope,named_output_signature_matches_baseline,restriction_coboundary_match,case_kind,negative_reason,oracle,tolerance,status".split(","),
    "negative_domain_controls.csv": "schema_version,row_id,case_kind,negative_reason,fixture,violated_lock,expected_detector,observed_detector,expected_disposition,oracle,tolerance,status".split(","),
    "actual_standard_support_transfer_controls.csv": "schema_version,row_id,q_case,q_class,q_cardinality,function_id,is_zero,support_components,gauge_id,gauge_nowhere_zero,actual_support_quasicompact,standard_support_compact,lands_in_standard_cc,support_preserved,fixed_prime_conditional,evidence_scope,case_kind,negative_reason,oracle,tolerance,status".split(","),
    "target_summary.csv": "schema_version,row_id,artifact,expected_rows,expected_columns,expected_negative_rows,oracle_class,tolerance_policy,canonical_order_key,scope,status".split(","),
    "completion_corona_controls_v2.csv": "schema_version,row_id,control_family,owner_case,q_class,q_model_size,epsilon,input_id,input_norm,coordinate_norm_class,multiplier_member,algebra_member,finite_c0_member,tail_window_size,quotient_distance,quotient_image_nonzero,quotient_map_injective,gauge_id,gauge_lhs_exp_mod24,gauge_rhs_exp_mod24,gauge_commutes,max_evidence_status,reduced_evidence_status,cardinality_credit_owner,topology_owner,fixed_prime_branch,evidence_scope,summary_artifact,summary_rows,summary_columns,summary_negative_rows,summary_test_methods,case_kind,negative_reason,fixture,violated_lock,expected_detector,observed_detector,oracle,tolerance,status".split(","),
}

SPECS = {
    "nerve_factorization_controls.csv": (SCHEMA_V1, 280, 17, 0),
    "circle_multiplier_cocycle_controls.csv": (SCHEMA_V1, 500, 20, 0),
    "lift_integer_defect_controls.csv": (SCHEMA_V1, 500, 20, 0),
    "gauge_coboundary_controls.csv": (SCHEMA_V1, 196, 19, 0),
    "twisted_convolution_controls.csv": (SCHEMA_V1, 78, 23, 0),
    "twisted_involution_controls.csv": (SCHEMA_V1, 54, 26, 0),
    "completion_gauge_controls.csv": (SCHEMA_V1, 756, 28, 0),
    "action_period_nonretention_controls.csv": (SCHEMA_V1, 56, 20, 0),
    "negative_domain_controls.csv": (SCHEMA_V1, 20, 12, 20),
    "actual_standard_support_transfer_controls.csv": (SCHEMA_V1, 96, 21, 27),
    "target_summary.csv": (SCHEMA_V1, 12, 11, 0),
    "completion_corona_controls_v2.csv": (SCHEMA_V2, 117, 41, 20),
}

K24 = (-6, -1, 0, 6)
KG = (-6, 0, 6)
T1 = (-2, -1, 0, 1, 2)
T2 = (-1, 0, 1)
T3 = (-3, -2, -1, 0, 1, 2, 3)
TOUT = tuple(range(-6, 7))
TSTAR = tuple(range(-4, 5))
SHIFT = (-1, 0, 2)
TEVAL = tuple(range(-3, 4))

FIXTURES = {
    "C1": (
        {-2: 1, -1: -2, 0: 3, 1: 1},
        {-1: 2, 0: -1, 2: 1},
        {-2: -1, 0: 2, 1: 1, 2: -2},
    ),
    "C2": (
        {-1: 1, 0: 2, 2: -1},
        {-2: 2, 1: -1, 2: 2},
        {-1: -2, 0: 1, 2: 1},
    ),
}

VECTORS = {
    "V1": {-2: 1, 0: 2, 1: -1},
    "V2": {-1: 1, 1: 1, 2: 2},
}

Gaussian = Tuple[int, int]
ZERO_G: Gaussian = (0, 0)


class ValidationError(RuntimeError):
    """A frozen design or package invariant failed."""


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def resolve_binding(path: str) -> Path:
    return WORKSPACE_ROOT / path if path.startswith("papers/") else PAPER_DIR / path


def bool_text(value: bool) -> str:
    return "true" if value else "false"


def field(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return bool_text(value)
    if isinstance(value, float):
        raise ValidationError("floating-point fields are prohibited")
    return str(value)


def make_row(header: Sequence[str], **values: object) -> Dict[str, str]:
    unknown = set(values) - set(header)
    if unknown:
        raise ValidationError(f"unknown row fields: {sorted(unknown)}")
    return {name: field(values.get(name, "")) for name in header}


def sigma_exp(k: int, t: int, u: int) -> int:
    return (2 * k * t * u) % 24


def alpha_exp(k: int, t: int) -> int:
    return (-k * t * t) % 24


def chi_exp(m: int, t: int) -> int:
    return (6 * m * t) % 24


def pr24(n: int) -> int:
    return ((n + 12) % 24) - 12


def phase(exp: int) -> Gaussian:
    table = {0: (1, 0), 6: (0, 1), 12: (-1, 0), 18: (0, -1)}
    reduced = exp % 24
    if reduced not in table:
        raise ValidationError(f"non-Gaussian phase exponent: {reduced}")
    return table[reduced]


def gadd(a: Gaussian, b: Gaussian) -> Gaussian:
    return (a[0] + b[0], a[1] + b[1])


def gmul(a: Gaussian, b: Gaussian) -> Gaussian:
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def gconj(a: Gaussian) -> Gaussian:
    return (a[0], -a[1])


def as_gaussian(value: object) -> Gaussian:
    if isinstance(value, tuple):
        return value  # type: ignore[return-value]
    return (int(value), 0)


def seq_value(seq: Mapping[int, object], t: int) -> Gaussian:
    return as_gaussian(seq.get(t, 0))


def conv_value(a: Mapping[int, object], b: Mapping[int, object], k: int, t: int) -> Gaussian:
    total = ZERO_G
    for u in sorted(a):
        av = seq_value(a, u)
        bv = seq_value(b, t - u)
        if av == ZERO_G or bv == ZERO_G:
            continue
        total = gadd(total, gmul(gmul(av, bv), phase(sigma_exp(k, u, t - u))))
    return total


def conv_map(a: Mapping[int, object], b: Mapping[int, object], k: int) -> Dict[int, Gaussian]:
    if not a or not b:
        return {}
    result = {}
    for t in range(min(a) + min(b), max(a) + max(b) + 1):
        value = conv_value(a, b, k, t)
        if value != ZERO_G:
            result[t] = value
    return result


def gauge_value(seq: Mapping[int, object], k: int, t: int) -> Gaussian:
    return gmul(phase(alpha_exp(k, t)), seq_value(seq, t))


def gauge_map(seq: Mapping[int, object], k: int) -> Dict[int, Gaussian]:
    return {t: gauge_value(seq, k, t) for t in seq if seq_value(seq, t) != ZERO_G}


def star_value(seq: Mapping[int, object], k: int, t: int) -> Gaussian:
    """Actual-owner star: conjugate the evaluated cocycle and coefficient."""
    return gmul(gconj(phase(sigma_exp(k, t, -t))), gconj(seq_value(seq, -t)))


def time_owner_star_value(seq: Mapping[int, object], k: int, t: int) -> Gaussian:
    """Time-owner star from the expanded quadratic exponent.

    This intentionally shares neither ``star_value`` nor ``sigma_exp`` with
    the actual-owner path: overline(sigma(t,-t)) has exponent 2*k*t^2.
    """
    time_phase_exp = (2 * k * t * t) % 24
    reflected = seq_value(seq, -t)
    return gmul(phase(time_phase_exp), (reflected[0], -reflected[1]))


def star_map(seq: Mapping[int, object], k: int) -> Dict[int, Gaussian]:
    return {t: star_value(seq, k, t) for t in sorted((-u for u in seq)) if star_value(seq, k, t) != ZERO_G}


def lambda_value(k: int, s: int, xi: Mapping[int, object], t: int) -> Gaussian:
    return gmul(phase(sigma_exp(k, s, t - s)), seq_value(xi, t - s))


def generate_nerve() -> List[Dict[str, str]]:
    name = "nerve_factorization_controls.csv"
    h = HEADERS[name]
    owners = (
        ("SINGLETON", ("star",)),
        ("TRIVIAL_TWO", ("a", "b")),
        ("PERIOD_THREE_SAMPLE", ("p0", "p1", "p2")),
        ("HETEROGENEOUS_SAMPLE", ("free0", "period0", "fixed0", "dense0")),
    )
    rows: List[Dict[str, str]] = []
    for owner, units in owners:
        for unit in units:
            for profile in ("A_ZERO", "A_LINEAR3"):
                for t in T1:
                    value = 0 if profile == "A_ZERO" else (3 * t) % 24
                    normalized = (0 if profile == "A_ZERO" else 0) == 0
                    rows.append(make_row(h, schema_version=SCHEMA_V1, row_id=f"NF-{len(rows)+1:04d}", owner_case=owner, degree=1, cochain_profile=profile, unit_id=unit, t=t, actual_exp_mod24=value, time_exp_mod24=value, normalized=normalized, factors_through_time=True, case_kind="DIAGNOSTIC", oracle="TIME_PHASE_EQUALITY_AND_NORMALIZATION", tolerance=0, status="PASS"))
            for profile in ("S_ZERO", "S_QUADRATIC1"):
                for t in T2:
                    for u in T2:
                        value = 0 if profile == "S_ZERO" else (2 * t * u) % 24
                        rows.append(make_row(h, schema_version=SCHEMA_V1, row_id=f"NF-{len(rows)+1:04d}", owner_case=owner, degree=2, cochain_profile=profile, unit_id=unit, t=t, u=u, actual_exp_mod24=value, time_exp_mod24=value, normalized=True, factors_through_time=True, case_kind="DIAGNOSTIC", oracle="TIME_PHASE_EQUALITY_AND_NORMALIZATION", tolerance=0, status="PASS"))
    return rows


def generate_cocycle() -> List[Dict[str, str]]:
    name = "circle_multiplier_cocycle_controls.csv"
    h = HEADERS[name]
    rows = []
    for k in K24:
        for t in T1:
            for u in T1:
                for v in T1:
                    a = sigma_exp(k, t, u)
                    b = sigma_exp(k, t + u, v)
                    c = sigma_exp(k, u, v)
                    d = sigma_exp(k, t, u + v)
                    lhs, rhs = (a + b) % 24, (c + d) % 24
                    ok = sigma_exp(k, t, 0) == sigma_exp(k, 0, u) == 0 and lhs == rhs
                    rows.append(make_row(h, schema_version=SCHEMA_V1, row_id=f"CM-{len(rows)+1:04d}", k_index=k, t=t, u=u, v=v, sigma_tu_exp=a, sigma_tplusu_v_exp=b, sigma_uv_exp=c, sigma_t_uplusv_exp=d, lhs_exp_mod24=lhs, rhs_exp_mod24=rhs, norm_t0=True, norm_0u=True, cocycle_holds=ok, case_kind="DIAGNOSTIC", oracle="NORMALIZED_COCYCLE_MOD24", tolerance=0, status="PASS" if ok else "FAIL"))
    return rows


def generate_lift() -> List[Dict[str, str]]:
    name = "lift_integer_defect_controls.csv"
    h = HEADERS[name]
    rows = []
    for k in K24:
        for t in T1:
            for u in T1:
                for v in T1:
                    values = (pr24(2*k*t*u), pr24(2*k*(t+u)*v), pr24(2*k*u*v), pr24(2*k*t*(u+v)))
                    defect = values[0] + values[1] - values[2] - values[3]
                    ok = defect % 24 == 0 and sigma_exp(k, t, 0) == sigma_exp(k, 0, u) == 0
                    rows.append(make_row(h, schema_version=SCHEMA_V1, row_id=f"LI-{len(rows)+1:04d}", k_index=k, t=t, u=u, v=v, r_tu=values[0], r_tplusu_v=values[1], r_uv=values[2], r_t_uplusv=values[3], defect_numerator_24=defect, defect_multiple_2pi=defect//24, is_integer_multiple=defect % 24 == 0, normalization_axes=True, cocycle_mod24=defect % 24, case_kind="DIAGNOSTIC", oracle="LIFT_DEFECT_IN_2PI_Z", tolerance=0, status="PASS" if ok else "FAIL"))
    return rows


def generate_gauge() -> List[Dict[str, str]]:
    name = "gauge_coboundary_controls.csv"
    h = HEADERS[name]
    rows = []
    for k in K24:
        for t in T3:
            for u in T3:
                at, au, atu = alpha_exp(k, t), alpha_exp(k, u), alpha_exp(k, t+u)
                delta = (at + au - atu) % 24
                sig = sigma_exp(k, t, u)
                normalized = alpha_exp(k, 0) == 0
                ok = normalized and delta == sig
                rows.append(make_row(h, schema_version=SCHEMA_V1, row_id=f"GC-{len(rows)+1:04d}", k_index=k, t=t, u=u, alpha_t_exp=at, alpha_u_exp=au, alpha_tplusu_exp=atu, delta_alpha_exp=delta, sigma_tu_exp=sig, quotient_sigma_over_one_exp=sig, gauge_direction="A_SIGMA_TO_A_ONE", normalized_alpha=normalized, coboundary_match=delta == sig, case_kind="DIAGNOSTIC", oracle="FROZEN_SIGN_COBOUNDARY_AND_DIRECTION", tolerance=0, status="PASS" if ok else "FAIL"))
    return rows


def generate_convolution() -> List[Dict[str, str]]:
    name = "twisted_convolution_controls.csv"
    h = HEADERS[name]
    rows = []
    for fixture_id, (f, g, third) in FIXTURES.items():
        minkowski = {u + v for u in f for v in g}
        for k in KG:
            fg_map = conv_map(f, g, k)
            gh_map = conv_map(g, third, k)
            left_map = conv_map(fg_map, third, k)
            right_map = conv_map(f, gh_map, k)
            gauged_f, gauged_g = gauge_map(f, k), gauge_map(g, k)
            untwisted = conv_map(gauged_f, gauged_g, 0)
            for t in TOUT:
                fg = seq_value(fg_map, t)
                left, right = seq_value(left_map, t), seq_value(right_map, t)
                gauge_product = gauge_value(fg_map, k, t)
                untwisted_value = seq_value(untwisted, t)
                support_ok = fg == ZERO_G or t in minkowski
                assoc_ok = left == right
                gauge_ok = gauge_product == untwisted_value
                ok = support_ok and assoc_ok and gauge_ok
                rows.append(make_row(h, schema_version=SCHEMA_V1, row_id=f"TC-{len(rows)+1:04d}", fixture_id=fixture_id, k_index=k, t=t, fg_re=fg[0], fg_im=fg[1], left_assoc_re=left[0], left_assoc_im=left[1], right_assoc_re=right[0], right_assoc_im=right[1], gauge_product_re=gauge_product[0], gauge_product_im=gauge_product[1], untwisted_of_gauged_re=untwisted_value[0], untwisted_of_gauged_im=untwisted_value[1], fg_support_within_minkowski=support_ok, associativity_holds=assoc_ok, gauge_product_holds=gauge_ok, case_kind="DIAGNOSTIC", oracle="FINITE_GAUSSIAN_PRODUCT_ASSOC_GAUGE", tolerance=0, status="PASS" if ok else "FAIL"))
    return rows


def generate_involution() -> List[Dict[str, str]]:
    name = "twisted_involution_controls.csv"
    h = HEADERS[name]
    rows = []
    for fixture_id, (f, g, _third) in FIXTURES.items():
        for k in KG:
            fs, gs = star_map(f, k), star_map(g, k)
            fss = star_map(fs, k)
            fg = conv_map(f, g, k)
            fg_star = star_map(fg, k)
            gs_fs = conv_map(gs, fs, k)
            for t in TSTAR:
                fss_v, f_v = seq_value(fss, t), seq_value(f, t)
                fg_s_v, gs_fs_v = seq_value(fg_star, t), seq_value(gs_fs, t)
                actual = star_value(f, k, t)
                time = time_owner_star_value(f, k, t)
                symmetry = sigma_exp(k, t, -t) == sigma_exp(k, -t, t)
                involutive = fss_v == f_v
                anti = fg_s_v == gs_fs_v
                actual_match = actual == time
                ok = symmetry and involutive and anti and actual_match
                rows.append(make_row(h, schema_version=SCHEMA_V1, row_id=f"TI-{len(rows)+1:04d}", fixture_id=fixture_id, k_index=k, t=t, f_starstar_re=fss_v[0], f_starstar_im=fss_v[1], f_re=f_v[0], f_im=f_v[1], fg_star_re=fg_s_v[0], fg_star_im=fg_s_v[1], gstar_fstar_re=gs_fs_v[0], gstar_fstar_im=gs_fs_v[1], actual_star_re=actual[0], actual_star_im=actual[1], time_star_re=time[0], time_star_im=time[1], sigma_inverse_symmetry=symmetry, star_involutive=involutive, anti_multiplicative=anti, actual_time_star_match=actual_match, case_kind="DIAGNOSTIC", oracle="FINITE_GAUSSIAN_STAR_LAWS", tolerance=0, status="PASS" if ok else "FAIL"))
    return rows


def generate_completion() -> List[Dict[str, str]]:
    name = "completion_gauge_controls.csv"
    h = HEADERS[name]
    rows = []
    for fixture_id, xi in VECTORS.items():
        norm_sq = sum(value * value for value in xi.values())
        for k in KG:
            for m in (0, 1):
                for s in SHIFT:
                    for u in SHIFT:
                        for t in TEVAL:
                            coeff = seq_value(xi, t-s-u)
                            lhs = gmul(phase(sigma_exp(k, s, t-s) + sigma_exp(k, u, t-s-u)), coeff)
                            rhs = gmul(phase(sigma_exp(k, s, u) + sigma_exp(k, s+u, t-s-u)), coeff)
                            icoeff = seq_value(xi, t-s)
                            ilhs = gmul(phase(alpha_exp(k, t) + sigma_exp(k, s, t-s) - alpha_exp(k, t-s)), icoeff)
                            irhs = gmul(phase(alpha_exp(k, s)), icoeff)
                            choice_lhs = gmul(phase((chi_exp(m, t)+alpha_exp(k, t)) % 24), seq_value(xi, t))
                            choice_rhs = gmul(phase(chi_exp(m, t)), gauge_value(xi, k, t))
                            projective = lhs == rhs
                            intertwiner = ilhs == irhs
                            choice = choice_lhs == choice_rhs
                            character_weighted = {
                                q: gmul(phase((6 * m * q) % 24), (value, 0))
                                for q, value in xi.items()
                            }
                            character_norm_sq = sum(re*re + im*im for re, im in character_weighted.values())
                            isometry = norm_sq == character_norm_sq
                            ok = projective and intertwiner and choice and isometry
                            rows.append(make_row(h, schema_version=SCHEMA_V1, row_id=f"CG-{len(rows)+1:04d}", fixture_id=fixture_id, k_index=k, character_m=m, s=s, u=u, t=t, projective_lhs_re=lhs[0], projective_lhs_im=lhs[1], projective_rhs_re=rhs[0], projective_rhs_im=rhs[1], intertwiner_lhs_re=ilhs[0], intertwiner_lhs_im=ilhs[1], intertwiner_rhs_re=irhs[0], intertwiner_rhs_im=irhs[1], xi_norm_sq=norm_sq, character_times_xi_norm_sq=character_norm_sq, projective_holds=projective, intertwiner_holds=intertwiner, choice_map_holds=choice, character_isometry_holds=isometry, completion_scope="FINITE_MATRIX_ELEMENT_DIAGNOSTIC_ONLY", case_kind="DIAGNOSTIC", oracle="FINITE_REGULAR_INTERTWINER_CHARACTER", tolerance=0, status="PASS" if ok else "FAIL"))
    return rows


def ap_predicates(k: int) -> Tuple[bool, bool, bool, bool, bool]:
    time_ok = alpha_exp(k, 0) == 0 and all((alpha_exp(k,t)+alpha_exp(k,u)-alpha_exp(k,t+u)-sigma_exp(k,t,u)) % 24 == 0 for t in T3 for u in T3)
    isotropy_ok = (-k + k == 0) and (-2*k + 2*k == 0) and (-k + k == 0)
    test_ok = True
    for f, g, third in FIXTURES.values():
        for u in f:
            for v in g:
                for w in third:
                    test_ok &= (sigma_exp(k,u,v)+sigma_exp(k,u+v,w)-sigma_exp(k,v,w)-sigma_exp(k,u,v+w)) % 24 == 0
        for u in f:
            for v in g:
                test_ok &= (alpha_exp(k,u+v)+sigma_exp(k,u,v)-alpha_exp(k,u)-alpha_exp(k,v)) % 24 == 0
        for t in set(f) | {-x for x in f}:
            test_ok &= (alpha_exp(k,t)-sigma_exp(k,t,-t)+alpha_exp(k,-t)) % 24 == 0
    full_ok = all((chi_exp(m,t)+chi_exp(m,u)-chi_exp(m,t+u)) % 24 == 0 and ((chi_exp(m,t)+alpha_exp(k,t))-alpha_exp(k,t)-chi_exp(m,t)) % 24 == 0 and (chi_exp(m,t)+chi_exp(m,-t)) % 24 == 0 for m in (0,1) for t in T3 for u in T3)
    reduced_ok = all((sigma_exp(k,s,t-s)+sigma_exp(k,u,t-s-u)-sigma_exp(k,s,u)-sigma_exp(k,s+u,t-s-u)) % 24 == 0 and (alpha_exp(k,t)+sigma_exp(k,s,t-s)-alpha_exp(k,t-s)-alpha_exp(k,s)) % 24 == 0 for s in SHIFT for u in SHIFT for t in TEVAL)
    return time_ok, isotropy_ok, test_ok, full_ok, reduced_ok


def generate_action_period() -> List[Dict[str, str]]:
    name = "action_period_nonretention_controls.csv"
    h = HEADERS[name]
    cases = (
        ("SINGLETON_TIME_OWNER", "star", "R", "ONE"),
        ("TRIVIAL_TWO_POINT", "all", "R", "TWO"),
        ("FREE_TRANSLATION", "free", "{0}", "ONE"),
        ("TRANSITIVE_PERIOD_1", "periodic", "Z", "ONE"),
        ("TRANSITIVE_PERIOD_2", "periodic", "2Z", "ONE"),
        ("FIXED_PRIME_2", "packet", "(log 2)Z", "QP_UNKNOWN"),
        ("FIXED_PRIME_3", "packet", "(log 3)Z", "QP_UNKNOWN"),
        ("COMPOSITE_LABEL_6", "label_control", "(log 6)Z", "UNSPECIFIED"),
        ("ARBITRARY_LABEL_A", "label_control", "L_a Z", "UNSPECIFIED"),
        ("NONTRANSITIVE_COMMON_L", "all", "LZ", "FINITE_3"),
        ("HETEROGENEOUS_ACTION", "free_component", "{0}", "HETEROGENEOUS"),
        ("HETEROGENEOUS_ACTION", "periodic_component", "LZ", "HETEROGENEOUS"),
        ("HETEROGENEOUS_ACTION", "fixed_component", "R", "HETEROGENEOUS"),
        ("HETEROGENEOUS_ACTION", "dense_component", "Q", "HETEROGENEOUS"),
    )
    rows = []
    for action_case, component, stabilizer, orbit_class in cases:
        for k in K24:
            predicates = ap_predicates(k)
            all_ok = all(predicates)
            dense = action_case == "HETEROGENEOUS_ACTION" and component == "dense_component"
            rows.append(make_row(h, schema_version=SCHEMA_V1, row_id=f"AP-{len(rows)+1:04d}", action_case=action_case, component_id=component, stabilizer_literal=stabilizer, orbit_count_class=orbit_class, k_index=k, global_time_sample_class="TIME_QUADRATIC_GAUGE_CLASS_ZERO_SAMPLE", isotropy_restriction_sample_class="ISOTROPY_QUADRATIC_RESTRICTION_CLASS_ZERO_SAMPLE", test_algebra_sample_signature="TWISTED_TEST_GAUGE_STAR_TERM_CHECK_PASS", full_sample_signature="FULL_TRANSPORT_CHARACTER_PHASE_CHECK_PASS", reduced_sample_signature="REDUCED_TRANSPORT_INTERTWINER_CHECK_PASS", dense_h_scope="FINITE_RATIONAL_WINDOW_DIAGNOSTIC_ONLY" if dense else "NOT_DENSE_H_CONTROL", named_output_signature_matches_baseline=all_ok, restriction_coboundary_match=predicates[1], case_kind="DIAGNOSTIC", oracle="QUADRATIC_RESTRICTION_SIGNATURE_DIAGNOSTIC", tolerance=0, status="PASS" if all_ok else "FAIL"))
    return rows


V1_NEGATIVES = (
    ("NON_T0_COEFFICIENT_TARGET", "DOM=INDISC2;COD=INDISC2;MAP=a:0|b:1", "T0_TARGET_REQUIRED_FOR_TIME_FACTORIZATION", "REJECT_T0_FACTORIZATION_USE", "DOMAIN_EXCLUDED"),
    ("MEASURABLE_ONLY_PHASE", "ALPHA_RULE=LE0_TO_1_GT0_TO_MINUS1;WITNESS=SEQ_1_OVER_N", "COCHAINS_MUST_BE_GLOBALLY_CONTINUOUS", "REJECT_CONTINUITY_DOMAIN", "DOMAIN_EXCLUDED"),
    ("DISCONTINUOUS_PHASE", "ALPHA_RULE=EQ0_TO_1_NE0_TO_MINUS1;WITNESS=SEQ_1_OVER_N", "COCHAINS_MUST_BE_GLOBALLY_CONTINUOUS", "REJECT_CONTINUITY_DOMAIN", "DOMAIN_EXCLUDED"),
    ("UNNORMALIZED_ONE_COCHAIN", "ALPHA_0=-1", "ONE_COCHAIN_NORMALIZATION_ALPHA_0_EQ_1", "REJECT_ONE_COCHAIN_NORMALIZATION", "ROW_REJECTED"),
    ("UNNORMALIZED_TWO_COCHAIN", "SIGMA_T_0=-1", "TWO_COCHAIN_NORMALIZATION_BOTH_AXES_EQ_1", "REJECT_TWO_COCHAIN_NORMALIZATION", "ROW_REJECTED"),
    ("WRONG_COBOUNDARY_SIGN", "K=-1;T=1;U=1;CANDIDATE=CONJUGATE_DELTA", "COBOUNDARY_SIGN_DELTA_A_EQ_A_T_A_U_OVERLINE_A_TPLUSU", "COBOUNDARY_MISMATCH", "ROW_REJECTED"),
    ("WRONG_GAUGE_ORIENTATION", "K=-1;MAP=U_OVERLINE_ALPHA;TYPE=A_SIGMA_TO_A_ONE", "GAUGE_DIRECTION_SIGMA_OVERLINE_TAU_EQ_DELTA_A", "GAUGE_DIRECTION_MISMATCH", "ROW_REJECTED"),
    ("TWISTED_PRODUCT_WRONG_SIGMA_ARGUMENT", "K=6;U=1;T=2;CANDIDATE=SIGMA_U_T", "TWISTED_PRODUCT_KERNEL_SIGMA_U_TMINUSU", "PRODUCT_GAUGE_OR_ASSOCIATIVITY_MISMATCH", "ROW_REJECTED"),
    ("TWISTED_STAR_OMITS_COCYCLE", "K=6;T=1;CANDIDATE=CONJ_F_MINUS_T", "TWISTED_STAR_FACTOR_OVERLINE_SIGMA_T_MINUST", "STAR_INVOLUTION_MISMATCH", "ROW_REJECTED"),
    ("REGULAR_TRANSLATION_WRONG_DIRECTION", "VECTOR=V1;S=1;T=0;CANDIDATE=XI_T_PLUS_S", "LEFT_REGULAR_TRANSLATION_T_MINUS_S", "PROJECTIVE_LAW_MISMATCH", "ROW_REJECTED"),
    ("INTERTWINER_CONJUGATIONS_SWAPPED", "VECTOR=V2;K=6;S=1;T=0;CANDIDATE=M_BARALPHA_LAMBDA_SIGMA_M_ALPHA", "INTERTWINER_M_ALPHA_LEFT_M_BARALPHA_RIGHT", "INTERTWINER_MISMATCH", "ROW_REJECTED"),
    ("R2_NONSYMMETRIC_COMMUTATOR", "OMEGA=EXP_I_PI_S1_T2_OVER2;S=1|0;T=0|1;COMM_EXP_MOD4=1", "P13_3_ONE_DIMENSIONAL_R_ONLY", "NONTRIVIAL_R2_COMMUTATOR", "ONE_DIMENSION_ONLY"),
    ("DENSE_H_HAAR_COMPLETION_PROMOTION", "H=Q;WINDOW=REDUCED_ABS_LE_2_DEN_LE_6;PROMOTION=HAAR_COMPLETION", "DENSE_Q_NO_HAAR_OR_COMPLETION_PROMOTION", "REJECT_DENSE_H_ANALYTIC_PROMOTION", "CLAIM_BLOCKED"),
    ("HETEROGENEOUS_AS_COMMON_LATTICE", "STABILIZERS=ZERO|LZ|R|Q;CANDIDATE=COMMON_LZ", "P13_8_COMMON_STABILIZER_H_EQ_LZ", "REJECT_COMMON_STABILIZER_HYPOTHESIS", "CLAIM_BLOCKED"),
    ("ACTUAL_STANDARD_REVERSE_IDENTITY", "MAP=IDENTITY;DIRECTION=G_ACTUAL_TO_G_STD;CLAIM=CONTINUOUS", "J_DIRECTION_G_STD_TO_G_ACTUAL_ONLY", "REJECT_J_DIRECTION", "CLAIM_BLOCKED"),
    ("INFINITE_Q_FINITE_SURROGATE_AS_PROOF", "Q=Q_1000;CLAIM=INFINITE_Q_COMPACTNESS_DECISION", "FINITE_CONTROLS_NEVER_PROVE_INFINITE_CLAIMS", "REJECT_FINITE_AS_INFINITE_PROOF", "CLAIM_BLOCKED"),
    ("FIXED_PRIME_Q_CARDINALITY_INFERENCE", "OWNER=FIXED_PRIME;INPUT=H_LOG_P_Z;CLAIM=QP_FINITE_OR_INFINITE", "QP_CARDINALITY_UNSPECIFIED", "REJECT_QP_CARDINALITY_INFERENCE", "CLAIM_BLOCKED"),
    ("STANDARD_ACTUAL_GROUPOID_CSTAR_TRANSFER", "OWNER=G_ACTUAL;CANDIDATE=STANDARD_GROUPOID_CSTAR", "TRANSPORTED_RECORDS_NOT_ACTUAL_GROUPOID_CSTAR", "REJECT_OWNER_FRAMEWORK_TRANSFER", "CLAIM_BLOCKED"),
    ("FINITE_CONTROL_UNIVERSAL_H2_PROOF", "GRID=K24_X_T1_CUBED;CLAIM=UNIVERSAL_H2_ZERO", "FINITE_CONTROLS_NEVER_PROVE_UNIVERSAL_H2", "REJECT_CONTROL_AS_PROOF", "CLAIM_BLOCKED"),
    ("CONCURRENT_PROOF_HASH_BINDING", "MUTATION=proof_binding.concurrent_phase3_proof_hash_included:true;PAYLOAD=NON_NULL_PROOF_DIGEST", "CONTROL_MANIFEST_EXCLUDES_CONCURRENT_PROOF_BINDING", "REJECT_PROOF_HASH_BINDING", "MANIFEST_REJECTED"),
)


def parse_fixture(text: str) -> Dict[str, str]:
    """Parse the frozen one-line fixture grammar without normalization.

    Clause order is semantically significant.  The parser consequently
    returns an insertion-ordered mapping and rejects every spelling that
    would otherwise be silently normalized (additional equals signs,
    whitespace, empty clauses, or duplicate keys).
    """
    if not isinstance(text, str) or not text or text.startswith(";") or text.endswith(";"):
        raise ValidationError(f"noncanonical fixture: {text!r}")
    result = {}
    for clause in text.split(";"):
        if clause.count("=") != 1:
            raise ValidationError(f"bad fixture clause: {clause}")
        key, value = clause.split("=")
        if (
            not key
            or not value
            or key in result
            or any(ch.isspace() for ch in clause)
            or not key.replace("_", "").isalnum()
            or key.upper() != key
        ):
            raise ValidationError(f"noncanonical fixture: {text}")
        result[key] = value
    return result


def fixture_int(parsed: Mapping[str, str], key: str) -> int:
    """Return a canonically serialized base-ten integer fixture field."""
    if key not in parsed:
        raise ValidationError(f"missing integer fixture field: {key}")
    token = parsed[key]
    if token == "0":
        return 0
    negative = token.startswith("-")
    digits = token[1:] if negative else token
    if not digits.isdigit() or digits.startswith("0"):
        raise ValidationError(f"noncanonical integer fixture field: {key}")
    return -int(digits) if negative else int(digits)


def fixture_equals(parsed: Mapping[str, str], *items: Tuple[str, str]) -> bool:
    """Exact fixture comparison, including the frozen clause order."""
    return list(parsed.items()) == list(items)


def derive_v1_negative(fixture: str) -> Tuple[str, str, str]:
    """Construct a v1 attempted promotion and derive its failed invariant.

    The reason, violated-lock and detector tokens are outputs of the semantic
    branch.  None is accepted as input to select the detector.
    """
    p = parse_fixture(fixture)
    if fixture_equals(p, ("DOM","INDISC2"),("COD","INDISC2"),("MAP","a:0|b:1")):
        opens = (frozenset(), frozenset({0, 1}))
        t0 = any((0 in op) != (1 in op) for op in opens)
        unit_map = {"a": 0, "b": 1}
        if not t0 and len(set(unit_map.values())) == 2:
            return ("NON_T0_COEFFICIENT_TARGET", "T0_TARGET_REQUIRED_FOR_TIME_FACTORIZATION", "REJECT_T0_FACTORIZATION_USE")
    if tuple(p) == ("ALPHA_RULE", "WITNESS") and p["WITNESS"] == "SEQ_1_OVER_N":
        if p["ALPHA_RULE"] == "LE0_TO_1_GT0_TO_MINUS1":
            alpha_zero = 1
            sequence_values = [-1 if Fraction(1,n) > 0 else 1 for n in range(1,9)]
            if all(value != alpha_zero for value in sequence_values):
                return ("MEASURABLE_ONLY_PHASE", "COCHAINS_MUST_BE_GLOBALLY_CONTINUOUS", "REJECT_CONTINUITY_DOMAIN")
        if p["ALPHA_RULE"] == "EQ0_TO_1_NE0_TO_MINUS1":
            alpha_zero = 1
            sequence_values = [-1 if Fraction(1,n) != 0 else 1 for n in range(1,9)]
            if all(value != alpha_zero for value in sequence_values):
                return ("DISCONTINUOUS_PHASE", "COCHAINS_MUST_BE_GLOBALLY_CONTINUOUS", "REJECT_CONTINUITY_DOMAIN")
    if fixture_equals(p, ("ALPHA_0","-1")) and fixture_int(p,"ALPHA_0") != 1:
        return ("UNNORMALIZED_ONE_COCHAIN", "ONE_COCHAIN_NORMALIZATION_ALPHA_0_EQ_1", "REJECT_ONE_COCHAIN_NORMALIZATION")
    if fixture_equals(p, ("SIGMA_T_0","-1")) and fixture_int(p,"SIGMA_T_0") != 1:
        return ("UNNORMALIZED_TWO_COCHAIN", "TWO_COCHAIN_NORMALIZATION_BOTH_AXES_EQ_1", "REJECT_TWO_COCHAIN_NORMALIZATION")
    if fixture_equals(p, ("K","-1"),("T","1"),("U","1"),("CANDIDATE","CONJUGATE_DELTA")):
        k,t,u = fixture_int(p,"K"),fixture_int(p,"T"),fixture_int(p,"U")
        frozen = (2*k*t*u) % 24
        candidate = (-2*k*t*u) % 24
        if candidate != frozen:
            return ("WRONG_COBOUNDARY_SIGN", "COBOUNDARY_SIGN_DELTA_A_EQ_A_T_A_U_OVERLINE_A_TPLUSU", "COBOUNDARY_MISMATCH")
    if fixture_equals(p, ("K","-1"),("MAP","U_OVERLINE_ALPHA"),("TYPE","A_SIGMA_TO_A_ONE")):
        if p["MAP"] != "U_ALPHA" and p["TYPE"] == "A_SIGMA_TO_A_ONE":
            return ("WRONG_GAUGE_ORIENTATION", "GAUGE_DIRECTION_SIGMA_OVERLINE_TAU_EQ_DELTA_A", "GAUGE_DIRECTION_MISMATCH")
    if fixture_equals(p, ("K","6"),("U","1"),("T","2"),("CANDIDATE","SIGMA_U_T")):
        k,u,t = fixture_int(p,"K"),fixture_int(p,"U"),fixture_int(p,"T")
        correct = (2*k*u*(t-u)) % 24
        candidate = (2*k*u*t) % 24
        if candidate != correct:
            return ("TWISTED_PRODUCT_WRONG_SIGMA_ARGUMENT", "TWISTED_PRODUCT_KERNEL_SIGMA_U_TMINUSU", "PRODUCT_GAUGE_OR_ASSOCIATIVITY_MISMATCH")
    if fixture_equals(p, ("K","6"),("T","1"),("CANDIDATE","CONJ_F_MINUS_T")):
        k,t = fixture_int(p,"K"),fixture_int(p,"T")
        required_phase = (-2*k*t*(-t)) % 24
        if required_phase != 0:
            return ("TWISTED_STAR_OMITS_COCYCLE", "TWISTED_STAR_FACTOR_OVERLINE_SIGMA_T_MINUST", "STAR_INVOLUTION_MISMATCH")
    if fixture_equals(p, ("VECTOR","V1"),("S","1"),("T","0"),("CANDIDATE","XI_T_PLUS_S")):
        vector,s,t = VECTORS[p["VECTOR"]],fixture_int(p,"S"),fixture_int(p,"T")
        if vector.get(t+s,0) != vector.get(t-s,0):
            return ("REGULAR_TRANSLATION_WRONG_DIRECTION", "LEFT_REGULAR_TRANSLATION_T_MINUS_S", "PROJECTIVE_LAW_MISMATCH")
    if fixture_equals(p, ("VECTOR","V2"),("K","6"),("S","1"),("T","0"),("CANDIDATE","M_BARALPHA_LAMBDA_SIGMA_M_ALPHA")):
        vector,k,s,t = VECTORS[p["VECTOR"]],fixture_int(p,"K"),fixture_int(p,"S"),fixture_int(p,"T")
        coefficient = vector.get(t-s,0)
        correct = ((-k*t*t) + 2*k*s*(t-s) - (-k*(t-s)*(t-s))) % 24
        swapped = (-(-k*t*t) + 2*k*s*(t-s) + (-k*(t-s)*(t-s))) % 24
        if coefficient != 0 and correct != swapped:
            return ("INTERTWINER_CONJUGATIONS_SWAPPED", "INTERTWINER_M_ALPHA_LEFT_M_BARALPHA_RIGHT", "INTERTWINER_MISMATCH")
    if fixture_equals(p, ("OMEGA","EXP_I_PI_S1_T2_OVER2"),("S","1|0"),("T","0|1"),("COMM_EXP_MOD4","1")):
        try:
            s1,s2 = (int(x) for x in p["S"].split("|"))
            t1,t2 = (int(x) for x in p["T"].split("|"))
        except (TypeError,ValueError) as exc:
            raise ValidationError("malformed R2 vector fixture") from exc
        commutator = (s1*t2-t1*s2) % 4
        if commutator == fixture_int(p,"COMM_EXP_MOD4") != 0:
            return ("R2_NONSYMMETRIC_COMMUTATOR", "P13_3_ONE_DIMENSIONAL_R_ONLY", "NONTRIVIAL_R2_COMMUTATOR")
    if fixture_equals(p, ("H","Q"),("WINDOW","REDUCED_ABS_LE_2_DEN_LE_6"),("PROMOTION","HAAR_COMPLETION")):
        window = sorted({Fraction(a,b) for b in range(1,7) for a in range(-2*b,2*b+1)}, key=lambda q:(q,q.denominator,q.numerator))
        if p["H"] == "Q" and len(window) < 1000 and p["PROMOTION"] == "HAAR_COMPLETION":
            return ("DENSE_H_HAAR_COMPLETION_PROMOTION", "DENSE_Q_NO_HAAR_OR_COMPLETION_PROMOTION", "REJECT_DENSE_H_ANALYTIC_PROMOTION")
    if fixture_equals(p, ("STABILIZERS","ZERO|LZ|R|Q"),("CANDIDATE","COMMON_LZ")):
        stabilizers = p["STABILIZERS"].split("|")
        if len(set(stabilizers)) > 1 and p["CANDIDATE"] == "COMMON_LZ":
            return ("HETEROGENEOUS_AS_COMMON_LATTICE", "P13_8_COMMON_STABILIZER_H_EQ_LZ", "REJECT_COMMON_STABILIZER_HYPOTHESIS")
    if fixture_equals(p, ("MAP","IDENTITY"),("DIRECTION","G_ACTUAL_TO_G_STD"),("CLAIM","CONTINUOUS")):
        if p["DIRECTION"] != "G_STD_TO_G_ACTUAL":
            return ("ACTUAL_STANDARD_REVERSE_IDENTITY", "J_DIRECTION_G_STD_TO_G_ACTUAL_ONLY", "REJECT_J_DIRECTION")
    if fixture_equals(p, ("Q","Q_1000"),("CLAIM","INFINITE_Q_COMPACTNESS_DECISION")):
        finite_surrogate_size = int(p["Q"].split("_")[1])
        if finite_surrogate_size < 10**9 and "INFINITE_Q" in p["CLAIM"]:
            return ("INFINITE_Q_FINITE_SURROGATE_AS_PROOF", "FINITE_CONTROLS_NEVER_PROVE_INFINITE_CLAIMS", "REJECT_FINITE_AS_INFINITE_PROOF")
    if fixture_equals(p, ("OWNER","FIXED_PRIME"),("INPUT","H_LOG_P_Z"),("CLAIM","QP_FINITE_OR_INFINITE")):
        if p["INPUT"] == "H_LOG_P_Z" and p["CLAIM"] == "QP_FINITE_OR_INFINITE":
            return ("FIXED_PRIME_Q_CARDINALITY_INFERENCE", "QP_CARDINALITY_UNSPECIFIED", "REJECT_QP_CARDINALITY_INFERENCE")
    if fixture_equals(p, ("OWNER","G_ACTUAL"),("CANDIDATE","STANDARD_GROUPOID_CSTAR")):
        if p["OWNER"] != "G_STANDARD":
            return ("STANDARD_ACTUAL_GROUPOID_CSTAR_TRANSFER", "TRANSPORTED_RECORDS_NOT_ACTUAL_GROUPOID_CSTAR", "REJECT_OWNER_FRAMEWORK_TRANSFER")
    if fixture_equals(p, ("GRID","K24_X_T1_CUBED"),("CLAIM","UNIVERSAL_H2_ZERO")):
        finite_grid_size = len(K24) * len(T1) ** 3
        if finite_grid_size == 500 and p["CLAIM"] == "UNIVERSAL_H2_ZERO":
            return ("FINITE_CONTROL_UNIVERSAL_H2_PROOF", "FINITE_CONTROLS_NEVER_PROVE_UNIVERSAL_H2", "REJECT_CONTROL_AS_PROOF")
    if fixture_equals(p, ("MUTATION","proof_binding.concurrent_phase3_proof_hash_included:true"),("PAYLOAD","NON_NULL_PROOF_DIGEST")):
        candidate = valid_manifest_firewall_skeleton()
        mutation_path, raw_value = p["MUTATION"].rsplit(":",1)
        if mutation_path != "proof_binding.concurrent_phase3_proof_hash_included" or raw_value != "true":
            raise ValidationError("unrecognized v1 manifest mutation")
        proof = candidate["proof_binding"]
        assert isinstance(proof, dict)
        proof["concurrent_phase3_proof_hash_included"] = True
        proof["proof_sha256"] = "1" * 64 if p["PAYLOAD"] == "NON_NULL_PROOF_DIGEST" else None
        if manifest_firewall_failure(candidate) == "PROOF_BINDING":
            return ("CONCURRENT_PROOF_HASH_BINDING", "CONTROL_MANIFEST_EXCLUDES_CONCURRENT_PROOF_BINDING", "REJECT_PROOF_HASH_BINDING")
    raise ValidationError("v1 negative fixture has no semantic failure")


def detect_v1_negative(reason: str, fixture: str, violated: str) -> str:
    try:
        derived_reason, derived_lock, detector = derive_v1_negative(fixture)
    except ValidationError:
        raise
    except (AssertionError, KeyError, TypeError, ValueError) as exc:
        raise ValidationError("malformed v1 negative fixture") from exc
    if reason != derived_reason:
        raise ValidationError(f"v1 reason/fixture mismatch: {reason}")
    if violated != derived_lock:
        raise ValidationError(f"v1 lock/fixture mismatch: {reason}")
    return detector


def generate_negative_domain() -> List[Dict[str, str]]:
    h = HEADERS["negative_domain_controls.csv"]
    rows = []
    for reason, fixture, violated, expected, disposition in V1_NEGATIVES:
        observed = detect_v1_negative(reason, fixture, violated)
        rows.append(make_row(h, schema_version=SCHEMA_V1, row_id=f"ND-{len(rows)+1:04d}", case_kind="NEGATIVE", negative_reason=reason, fixture=fixture, violated_lock=violated, expected_detector=expected, observed_detector=observed, expected_disposition=disposition, oracle="EXPECTED_DETECTOR_TOKEN", tolerance=0, status="PASS" if observed == expected else "FAIL"))
    return rows


def generate_support_transfer() -> List[Dict[str, str]]:
    h = HEADERS["actual_standard_support_transfer_controls.csv"]
    q_cases = (
        ("QF1", "FINITE", "1", False, "FINITE_COMPONENT_DIAGNOSTIC"),
        ("QF2", "FINITE", "2", False, "FINITE_COMPONENT_DIAGNOSTIC"),
        ("QF4", "FINITE", "4", False, "FINITE_COMPONENT_DIAGNOSTIC"),
        ("QF7", "FINITE", "7", False, "FINITE_COMPONENT_DIAGNOSTIC"),
        ("QINF_N", "INFINITE", "INF", False, "ANALYTIC_INFINITE_COPRODUCT_BRANCH_ONLY"),
        ("QINF_Z", "INFINITE", "INF", False, "ANALYTIC_INFINITE_COPRODUCT_BRANCH_ONLY"),
        ("QP_FINITE_CONDITIONAL", "QP_FINITE_CONDITIONAL", "FINITE_UNSPECIFIED", True, "CONDITIONAL_QP_BRANCH_ONLY"),
        ("QP_INFINITE_CONDITIONAL", "QP_INFINITE_CONDITIONAL", "INFINITE_ASSUMED", True, "CONDITIONAL_QP_BRANCH_ONLY"),
    )
    functions = (("ZERO", True, "EMPTY"), ("TENT_CENTER", False, "[-1,1]"), ("TENT_SHIFT", False, "[1,3]"), ("TWO_BUMP", False, "[-3,-1]|[1,2]"))
    gauges = ("ONE", "ALPHA_K_MINUS6", "ALPHA_K_6")
    rows = []
    for q_case, q_class, cardinality, conditional, scope in q_cases:
        for function_id, is_zero, support in functions:
            for gauge in gauges:
                finite_class = q_class in {"FINITE", "QP_FINITE_CONDITIONAL"}
                compact = is_zero or finite_class
                negative = (not is_zero) and q_case in {"QINF_N", "QINF_Z", "QP_INFINITE_CONDITIONAL"}
                reason = "CONDITIONAL_NONZERO_QP_INFINITE_NOT_COMPACT" if negative and q_case == "QP_INFINITE_CONDITIONAL" else "NONZERO_INFINITE_Q_NOT_COMPACT" if negative else ""
                rows.append(make_row(h, schema_version=SCHEMA_V1, row_id=f"ST-{len(rows)+1:04d}", q_case=q_case, q_class=q_class, q_cardinality=cardinality, function_id=function_id, is_zero=is_zero, support_components=support, gauge_id=gauge, gauge_nowhere_zero=True, actual_support_quasicompact=True, standard_support_compact=compact, lands_in_standard_cc=compact, support_preserved=True, fixed_prime_conditional=conditional, evidence_scope=scope, case_kind="NEGATIVE" if negative else "POSITIVE", negative_reason=reason, oracle="ZERO_OR_FINITE_Q_SUPPORT_BRANCH", tolerance=0, status=""))
    validate_support_transfer_rows(rows,finalize=True)
    return rows


def validate_support_transfer_rows(rows: Sequence[MutableMapping[str,str]], *, finalize: bool = False) -> None:
    q_cases = (
        ("QF1","FINITE","1",False,"FINITE_COMPONENT_DIAGNOSTIC"),("QF2","FINITE","2",False,"FINITE_COMPONENT_DIAGNOSTIC"),
        ("QF4","FINITE","4",False,"FINITE_COMPONENT_DIAGNOSTIC"),("QF7","FINITE","7",False,"FINITE_COMPONENT_DIAGNOSTIC"),
        ("QINF_N","INFINITE","INF",False,"ANALYTIC_INFINITE_COPRODUCT_BRANCH_ONLY"),("QINF_Z","INFINITE","INF",False,"ANALYTIC_INFINITE_COPRODUCT_BRANCH_ONLY"),
        ("QP_FINITE_CONDITIONAL","QP_FINITE_CONDITIONAL","FINITE_UNSPECIFIED",True,"CONDITIONAL_QP_BRANCH_ONLY"),("QP_INFINITE_CONDITIONAL","QP_INFINITE_CONDITIONAL","INFINITE_ASSUMED",True,"CONDITIONAL_QP_BRANCH_ONLY"),
    )
    functions = (("ZERO",True,"EMPTY"),("TENT_CENTER",False,"[-1,1]"),("TENT_SHIFT",False,"[1,3]"),("TWO_BUMP",False,"[-3,-1]|[1,2]"))
    gauges = ("ONE","ALPHA_K_MINUS6","ALPHA_K_6")
    expected: List[Dict[str,str]] = []
    h = HEADERS["actual_standard_support_transfer_controls.csv"]
    q_registry = {
        q_case:(q_class,cardinality,conditional,scope)
        for q_case,q_class,cardinality,conditional,scope in q_cases
    }
    function_registry = {
        function_id:(is_zero,support)
        for function_id,is_zero,support in functions
    }

    # Interpret each serialized row as its own implicit attempted-state
    # fixture before comparing canonical order.  In particular, every one of
    # the 27 nonzero infinite branches derives noncompact support from its
    # own q/function/gauge fields rather than inheriting a stored status.
    for index,row in enumerate(rows,1):
        q_case = row.get("q_case","")
        if q_case not in q_registry:
            raise ValidationError(f"ST_Q_CASE:{index}")
        q_class,cardinality,conditional,scope = q_registry[q_case]
        if row.get("q_class") != q_class:
            raise ValidationError(f"ST_Q_CLASS:{index}")
        if row.get("q_cardinality") != cardinality:
            raise ValidationError(f"ST_Q_CARDINALITY:{index}")
        function_id = row.get("function_id","")
        if function_id not in function_registry:
            raise ValidationError(f"ST_FUNCTION:{index}")
        is_zero,support = function_registry[function_id]
        if row.get("is_zero") != bool_text(is_zero) or row.get("support_components") != support:
            raise ValidationError(f"ST_FUNCTION_STATE:{index}")
        gauge = row.get("gauge_id","")
        if gauge not in gauges or row.get("gauge_nowhere_zero") != "true":
            raise ValidationError(f"ST_GAUGE:{index}")
        finite = q_class in {"FINITE","QP_FINITE_CONDITIONAL"}
        compact = is_zero or finite
        negative = (not is_zero) and q_case in {
            "QINF_N","QINF_Z","QP_INFINITE_CONDITIONAL"
        }
        semantic_fields = {
            "actual_support_quasicompact":"true",
            "standard_support_compact":bool_text(compact),
            "lands_in_standard_cc":bool_text(compact),
            "support_preserved":"true",
            "fixed_prime_conditional":bool_text(conditional),
            "evidence_scope":scope,
            "case_kind":"NEGATIVE" if negative else "POSITIVE",
            "negative_reason":(
                "CONDITIONAL_NONZERO_QP_INFINITE_NOT_COMPACT"
                if negative and q_case=="QP_INFINITE_CONDITIONAL"
                else "NONZERO_INFINITE_Q_NOT_COMPACT" if negative else ""
            ),
            "status":"" if finalize else "PASS",
        }
        for field_name,wanted in semantic_fields.items():
            if row.get(field_name) != wanted:
                raise ValidationError(f"ST_{field_name}:{index}")
    for q_case,q_class,cardinality,conditional,scope in q_cases:
        for function_id,is_zero,support in functions:
            for gauge in gauges:
                finite = q_class == "FINITE" or q_class == "QP_FINITE_CONDITIONAL"
                compact = is_zero or finite
                gauge_nonzero = gauge in gauges
                negative = (not is_zero) and q_case in {"QINF_N","QINF_Z","QP_INFINITE_CONDITIONAL"}
                reason = "CONDITIONAL_NONZERO_QP_INFINITE_NOT_COMPACT" if negative and q_case=="QP_INFINITE_CONDITIONAL" else "NONZERO_INFINITE_Q_NOT_COMPACT" if negative else ""
                expected.append(make_row(h,schema_version=SCHEMA_V1,row_id=f"ST-{len(expected)+1:04d}",q_case=q_case,q_class=q_class,q_cardinality=cardinality,function_id=function_id,is_zero=is_zero,support_components=support,gauge_id=gauge,gauge_nowhere_zero=gauge_nonzero,actual_support_quasicompact=True,standard_support_compact=compact,lands_in_standard_cc=compact,support_preserved=gauge_nonzero,fixed_prime_conditional=conditional,evidence_scope=scope,case_kind="NEGATIVE" if negative else "POSITIVE",negative_reason=reason,oracle="ZERO_OR_FINITE_Q_SUPPORT_BRANCH",tolerance=0,status="" if finalize else "PASS"))
    if len(rows)!=96:
        raise ValidationError("ST_ROW_COUNT")
    for i,(actual,wanted) in enumerate(zip(rows,expected),1):
        for key in h:
            if actual[key] != wanted[key]:
                raise ValidationError(f"ST_FIELD_{key}:{i}")
    if finalize:
        for row in rows:
            row["status"]="PASS"


def validate_convolution_independence(rows: Sequence[Mapping[str,str]]) -> None:
    """Rebuild the product, both parenthesizations, and gauge square.

    These expressions deliberately do not call ``conv_value``, ``conv_map``,
    ``gauge_value``, ``alpha_exp``, or ``sigma_exp``.  A defect in one of the
    generation helpers therefore cannot certify its own output.
    """
    def add_terms(terms: Iterable[Gaussian]) -> Gaussian:
        total = ZERO_G
        for term in terms:
            total = gadd(total,term)
        return total

    def direct_product(a: Mapping[int,object], b: Mapping[int,object], k: int, t: int) -> Gaussian:
        return add_terms(
            gmul(
                gmul(seq_value(a,u),seq_value(b,t-u)),
                phase((2*k*u*(t-u)) % 24),
            )
            for u in sorted(a)
            if seq_value(a,u) != ZERO_G and seq_value(b,t-u) != ZERO_G
        )

    if len(rows) != SPECS["twisted_convolution_controls.csv"][1]:
        raise ValidationError("CONV_ROW_COUNT")
    for index,row in enumerate(rows,1):
        try:
            fixture_id = row["fixture_id"]
            f,g,third = FIXTURES[fixture_id]
            k,t = int(row["k_index"]),int(row["t"])
        except (KeyError,TypeError,ValueError) as exc:
            raise ValidationError(f"CONV_FIXTURE:{index}") from exc
        if k not in KG or t not in TOUT:
            raise ValidationError(f"CONV_DOMAIN:{index}")
        product = direct_product(f,g,k,t)
        left = add_terms(
            gmul(
                gmul(gmul(seq_value(f,u),seq_value(g,v)),seq_value(third,w)),
                phase((2*k*u*v + 2*k*(u+v)*w) % 24),
            )
            for u in sorted(f) for v in sorted(g) for w in sorted(third)
            if u+v+w == t
        )
        right = add_terms(
            gmul(
                gmul(seq_value(f,u),gmul(seq_value(g,v),seq_value(third,w))),
                phase((2*k*v*w + 2*k*u*(v+w)) % 24),
            )
            for u in sorted(f) for v in sorted(g) for w in sorted(third)
            if u+v+w == t
        )
        gauge_product = gmul(phase((-k*t*t) % 24),product)
        untwisted = add_terms(
            gmul(
                gmul(phase((-k*u*u) % 24),seq_value(f,u)),
                gmul(phase((-k*(t-u)*(t-u)) % 24),seq_value(g,t-u)),
            )
            for u in sorted(f)
            if seq_value(f,u) != ZERO_G and seq_value(g,t-u) != ZERO_G
        )
        expected_fields = {
            "fg_re":str(product[0]), "fg_im":str(product[1]),
            "left_assoc_re":str(left[0]), "left_assoc_im":str(left[1]),
            "right_assoc_re":str(right[0]), "right_assoc_im":str(right[1]),
            "gauge_product_re":str(gauge_product[0]), "gauge_product_im":str(gauge_product[1]),
            "untwisted_of_gauged_re":str(untwisted[0]), "untwisted_of_gauged_im":str(untwisted[1]),
            "fg_support_within_minkowski":bool_text(product == ZERO_G or t in {u+v for u in f for v in g}),
            "associativity_holds":bool_text(left == right),
            "gauge_product_holds":bool_text(gauge_product == untwisted),
        }
        for key,wanted in expected_fields.items():
            if row.get(key) != wanted:
                raise ValidationError(f"CONV_{key}:{index}")
        if not (left == right and gauge_product == untwisted):
            raise ValidationError(f"CONV_POSITIVE_PREDICATE:{index}")


def validate_involution_independence(rows: Sequence[Mapping[str,str]]) -> None:
    """Check separately expanded actual-owner and time-owner star formulas."""
    if len(rows) != SPECS["twisted_involution_controls.csv"][1]:
        raise ValidationError("STAR_ROW_COUNT")
    for index,row in enumerate(rows,1):
        try:
            f = FIXTURES[row["fixture_id"]][0]
            k,t = int(row["k_index"]),int(row["t"])
        except (KeyError,TypeError,ValueError) as exc:
            raise ValidationError(f"STAR_FIXTURE:{index}") from exc
        reflected_actual = seq_value(f,-t)
        actual_sigma = (2*k*t*(-t)) % 24
        actual = gmul(gconj(phase(actual_sigma)),gconj(reflected_actual))
        reflected_time = as_gaussian(f.get(-t,0))
        time = gmul(phase((2*k*t*t) % 24),(reflected_time[0],-reflected_time[1]))
        expected = {
            "actual_star_re":str(actual[0]), "actual_star_im":str(actual[1]),
            "time_star_re":str(time[0]), "time_star_im":str(time[1]),
            "actual_time_star_match":bool_text(actual == time),
        }
        for key,wanted in expected.items():
            if row.get(key) != wanted:
                raise ValidationError(f"STAR_{key}:{index}")
        if actual != time:
            raise ValidationError(f"STAR_POSITIVE_PREDICATE:{index}")


def validate_completion_independence(rows: Sequence[Mapping[str,str]]) -> None:
    """Recompute regular/intertwiner witnesses and both norm expressions."""
    if len(rows) != SPECS["completion_gauge_controls.csv"][1]:
        raise ValidationError("COMPLETION_ROW_COUNT")
    for index,row in enumerate(rows,1):
        try:
            xi = VECTORS[row["fixture_id"]]
            k,m,s,u,t = (int(row[name]) for name in ("k_index","character_m","s","u","t"))
        except (KeyError,TypeError,ValueError) as exc:
            raise ValidationError(f"COMPLETION_FIXTURE:{index}") from exc
        coefficient = seq_value(xi,t-s-u)
        lhs = gmul(phase((2*k*s*(t-s) + 2*k*u*(t-s-u)) % 24),coefficient)
        rhs = gmul(phase((2*k*s*u + 2*k*(s+u)*(t-s-u)) % 24),coefficient)
        icoefficient = seq_value(xi,t-s)
        intertwiner_lhs = gmul(
            phase((-k*t*t + 2*k*s*(t-s) + k*(t-s)*(t-s)) % 24),
            icoefficient,
        )
        intertwiner_rhs = gmul(phase((-k*s*s) % 24),icoefficient)
        source_norm = sum(value*value for value in xi.values())
        weighted_coefficients = [
            gmul(phase((6*m*q) % 24),(value,0))
            for q,value in sorted(xi.items())
        ]
        weighted_norm = sum(re*re+im*im for re,im in weighted_coefficients)
        choice_lhs = gmul(phase((6*m*t-k*t*t) % 24),seq_value(xi,t))
        choice_rhs = gmul(
            phase((6*m*t) % 24),
            gmul(phase((-k*t*t) % 24),seq_value(xi,t)),
        )
        expected = {
            "projective_lhs_re":str(lhs[0]), "projective_lhs_im":str(lhs[1]),
            "projective_rhs_re":str(rhs[0]), "projective_rhs_im":str(rhs[1]),
            "intertwiner_lhs_re":str(intertwiner_lhs[0]), "intertwiner_lhs_im":str(intertwiner_lhs[1]),
            "intertwiner_rhs_re":str(intertwiner_rhs[0]), "intertwiner_rhs_im":str(intertwiner_rhs[1]),
            "xi_norm_sq":str(source_norm),
            "character_times_xi_norm_sq":str(weighted_norm),
            "projective_holds":bool_text(lhs == rhs),
            "intertwiner_holds":bool_text(intertwiner_lhs == intertwiner_rhs),
            "choice_map_holds":bool_text(choice_lhs == choice_rhs),
            "character_isometry_holds":bool_text(source_norm == weighted_norm),
        }
        for key,wanted in expected.items():
            if row.get(key) != wanted:
                raise ValidationError(f"COMPLETION_{key}:{index}")
        if not (lhs == rhs and intertwiner_lhs == intertwiner_rhs and choice_lhs == choice_rhs and source_norm == weighted_norm):
            raise ValidationError(f"COMPLETION_POSITIVE_PREDICATE:{index}")


TARGET_SUMMARY = (
    ("nerve_factorization_controls.csv",280,17,0,"owner_case|unit_id|degree|cochain_profile|t|u","FINITE_TIME_ONLY_WITNESS_NOT_TOPOLOGICAL_PROOF"),
    ("circle_multiplier_cocycle_controls.csv",500,20,0,"k_index|t|u|v","FINITE_PHASE_GRID_DIAGNOSTIC_NOT_H2_PROOF"),
    ("lift_integer_defect_controls.csv",500,20,0,"k_index|t|u|v","FINITE_LIFT_WRAP_DIAGNOSTIC_NOT_CONTINUOUS_LIFT_PROOF"),
    ("gauge_coboundary_controls.csv",196,19,0,"k_index|t|u","FINITE_COBOUNDARY_SIGN_DIAGNOSTIC_NOT_H2_PROOF"),
    ("twisted_convolution_controls.csv",78,23,0,"fixture_id|k_index|t","FINITE_LATTICE_SIGN_DIAGNOSTIC_ONLY"),
    ("twisted_involution_controls.csv",54,26,0,"fixture_id|k_index|t","FINITE_LATTICE_SIGN_DIAGNOSTIC_ONLY"),
    ("completion_gauge_controls.csv",756,28,0,"fixture_id|k_index|character_m|s|u|t","FINITE_MATRIX_ELEMENT_DIAGNOSTIC_ONLY"),
    ("action_period_nonretention_controls.csv",56,20,0,"action_case_ordinal|k_index","FINITE_ACTION_SIGNATURE_DIAGNOSTIC_ONLY"),
    ("negative_domain_controls.csv",20,12,20,"row_id","FAIL_CLOSED_DOMAIN_AND_CLAIM_FIREWALL"),
    ("actual_standard_support_transfer_controls.csv",96,21,27,"q_case|function_id|gauge_id","ANALYTIC_BRANCH_LEDGER_FINITE_CONTROLS_NOT_PROOF"),
    ("target_summary.csv",12,11,0,"artifact_ordinal","PACKAGE_METADATA_NO_SELF_DIGEST"),
    ("PACKAGE_TOTAL",2548,"MIXED",47,"ARTIFACT_ORDER_ABOVE","PACKAGE_AGGREGATE_NO_THEOREM_CREDIT"),
)


def generate_target_summary() -> List[Dict[str, str]]:
    h = HEADERS["target_summary.csv"]
    return [make_row(h, schema_version=SCHEMA_V1, row_id=f"TS-{i:04d}", artifact=a, expected_rows=r, expected_columns=c, expected_negative_rows=n, oracle_class="COUNT_SCHEMA_NEGATIVE_TOTAL", tolerance_policy="EXACT_ZERO", canonical_order_key=o, scope=s, status="PASS") for i,(a,r,c,n,o,s) in enumerate(TARGET_SUMMARY,1)]


V2_NEGATIVES = (
    ("FINITE_SIGN_PROJECTION_AS_CONTINUUM_PROOF", "MODEL=SIGN_COORDS_16;CLAIM=QP_CARDINALITY_CONTINUUM", "FINITE_CONTROLS_NEVER_PROVE_CONTINUUM", "REJECT_FINITE_AS_CONTINUUM_PROOF"),
    ("FINITE_C0_WINDOW_AS_ARBITRARY_INDEX_PROOF", "MODEL=QF4;CLAIM=ARBITRARY_INDEX_MULTIPLIER_IDENTITY", "FINITE_CONTROLS_NEVER_PROVE_ARBITRARY_INDEX_THEOREM", "REJECT_FINITE_AS_ARBITRARY_INDEX_PROOF"),
    ("FINITE_TAIL_QUOTIENT_AS_CORONA_PROOF", "MODEL=CORE2_TAIL3;CLAIM=FAITHFUL_MULTIPLIER_CORONA", "FINITE_QUOTIENT_MODEL_NOT_ACTUAL_CORONA", "REJECT_FINITE_AS_CORONA_PROOF"),
    ("PAPER2_LOWER_BOUND_CREDIT_TO_P13", "SOURCE=PAPER2_PROP_UNCOUNTABLE;CREDIT=P13_NOVELTY", "PAPER2_LOWER_BOUND_ZERO_P13_CREDIT", "REJECT_INHERITED_CARDINALITY_CREDIT"),
    ("ACTUAL_QUOTIENT_GIVEN_DISCRETE_TOPOLOGY", "OWNER=Q_P_ACTUAL;TOPOLOGY=DISCRETE", "Q_P_ACTUAL_RETAINS_INDISCRETE_TOPOLOGY", "REJECT_ACTUAL_DISCRETE_PROMOTION"),
    ("BARE_SET_GIVEN_TOPOLOGY", "OWNER=Q_P_BARE;TOPOLOGY=INDISCRETE", "Q_P_BARE_HAS_NO_TOPOLOGY", "REJECT_BARE_TOPOLOGY"),
    ("STANDARD_FAILURE_ASSIGNED_TO_ACTUAL", "SOURCE=STD_GAMMA_P;TARGET=Q_P_ACTUAL;CLAIM=NONSECONDCOUNTABLE", "STANDARD_TOPOLOGY_NOT_TRANSPORTED_TO_ACTUAL", "REJECT_STANDARD_ACTUAL_OWNER_CONFLATION"),
    ("DISCRETE_QUOTIENT_IDENTIFIED_WITH_ACTUAL", "SOURCE=Q_P_DISC;TARGET=Q_P_ACTUAL;MAP=TOPOLOGICAL_IDENTITY", "ACTUAL_AND_DISCRETE_QUOTIENT_OWNERS_DISTINCT", "REJECT_DISCRETE_ACTUAL_IDENTITY"),
    ("BOUNDED_MULTIPLIER_PRODUCT_IDENTIFIED_WITH_C0_ALGEBRA", "OWNER=INFINITE_Q;CANDIDATE=PRODUCT_BOUNDED_EQ_C0_SUM", "MULTIPLIER_PRODUCT_DISTINCT_FROM_C0_ALGEBRA", "REJECT_MULTIPLIER_ALGEBRA_CONFLATION"),
    ("NONZERO_INFINITE_DIAGONAL_DECLARED_C0", "Q=INFINITE;INPUT=ONE;CLAIM=ALGEBRA_MEMBER", "CONSTANT_NONZERO_NORM_NOT_C0", "REJECT_CONSTANT_NORM_C0_MEMBERSHIP"),
    ("FINITE_Q_CORONA_MAP_DECLARED_INJECTIVE", "Q=QF2;INPUT=ONE;CLAIM=CORONA_MAP_INJECTIVE", "FINITE_BRANCH_DIAGONAL_LIES_IN_ALGEBRA", "REJECT_FINITE_BRANCH_CORONA_INJECTIVITY"),
    ("CORONA_KERNEL_LARGER_THAN_INTERSECTION", "Q=INFINITE;CANDIDATE=KERNEL_STRICTLY_CONTAINS_PREIMAGE_A", "QUOTIENT_KERNEL_EQUALS_PREIMAGE_OF_ALGEBRA", "REJECT_QUOTIENT_KERNEL_MISMATCH"),
    ("V2_GAUGE_ORIENTATION_REVERSED", "RELATION=TAU_OVERLINE_SIGMA_EQ_DELTA_ALPHA;MAP=U_ALPHA_SIGMA_TO_TAU", "GAUGE_DIRECTION_SIGMA_OVERLINE_TAU_EQ_DELTA_ALPHA", "GAUGE_DIRECTION_MISMATCH"),
    ("MAX_REDUCED_EVIDENCE_CONFLATED", "MAX_STATUS=COPIED_COMMON_PASS;REDUCED_STATUS=COPIED_COMMON_PASS", "MAX_REDUCED_EVIDENCE_SERIALIZED_SEPARATELY", "REJECT_MAX_REDUCED_EVIDENCE_CONFLATION"),
    ("V1_CONDITIONAL_QP_BRANCH_USED_AS_V2_RESULT", "SOURCE=V1_QP_FINITE_CONDITIONAL;CLAIM=V2_FIXED_PRIME_BRANCH", "V1_CONDITIONAL_ROWS_ARE_IMMUTABLE_HISTORICAL_DIAGNOSTICS", "REJECT_V1_CONDITIONAL_AS_V2_BRANCH"),
    ("FIXED_PRIME_CONTINUUM_INFERRED_FROM_PERIOD_ONLY", "INPUT=H_LOG_P_Z;CLAIM=QP_CONTINUUM", "FIXED_PRIME_CARDINALITY_REQUIRES_PAPER2_LOWER_AND_P13_UPPER", "REJECT_PERIOD_ONLY_CARDINALITY_INFERENCE"),
    ("GLOBAL_TWISTED_GROUPOID_CSTAR_PROMOTION_V2", "OWNER=STD_GLOBAL;CANDIDATE=TWISTED_GROUPOID_CSTAR", "COMPONENTWISE_AUTHOR_RECORD_NOT_GLOBAL_TWISTED_GROUPOID_CSTAR", "REJECT_GLOBAL_TWISTED_FRAMEWORK_PROMOTION"),
    ("CONCURRENT_PROOF_HASH_BINDING_V2", "MANIFEST=PROOF_PATH_AND_NON_NULL_SHA256", "CONTROL_MANIFEST_EXCLUDES_CONCURRENT_PROOF_BINDING", "REJECT_PROOF_HASH_BINDING"),
    ("MANIFEST_SELF_HASH_BINDING_V2", "MANIFEST=ARTIFACT_LIST_INCLUDES_MANIFEST_JSON_SHA256", "MANIFEST_NEVER_HASHES_ITSELF", "REJECT_MANIFEST_SELF_HASH"),
    ("V2_DESIGN_OR_GATE_UNBOUND", "MANIFEST=OMIT_V2_DESIGN_HEAD_OR_AUTHORIZATION_GATE", "MANIFEST_BINDS_V2_DESIGN_AND_GATE", "REJECT_UNBOUND_V2_AUTHORITY"),
)


def valid_manifest_firewall_skeleton() -> Dict[str, object]:
    return {
        "schema_version": MANIFEST_SCHEMA,
        "package_id": PACKAGE_ID,
        "design_head": dict(DESIGN_HEAD),
        "bindings": [{"path": path, "sha256": digest} for path,digest in sorted(BINDINGS.items())],
        "proof_binding": {
            "concurrent_phase3_proof_hash_included": False,
            "policy": "POST_PROOF_AUDIT_BINDS_SEPARATELY",
        },
        "implementation": [{"path":path,"bytes":1,"sha256":"0"*64} for path in sorted(IMPLEMENTATION_PATHS)],
        "artifacts": [{"path":f"results/{name}","schema":SPECS[name][0],"columns":SPECS[name][2],"rows":SPECS[name][1],"negative_rows":SPECS[name][3],"bytes":1,"sha256":"0"*64} for name in ARTIFACT_ORDER],
    }


def derive_v2_negative(fixture: str) -> Tuple[str, str, str]:
    """Derive a v2 failure from the parsed attempted state, never its reason."""
    p = parse_fixture(fixture)
    if fixture_equals(p,("MODEL","SIGN_COORDS_16"),("CLAIM","QP_CARDINALITY_CONTINUUM")):
        finite_model_cardinality = 2 ** int(p["MODEL"].rsplit("_",1)[1])
        if finite_model_cardinality < 2 ** 64 and p["CLAIM"] == "QP_CARDINALITY_CONTINUUM":
            return ("FINITE_SIGN_PROJECTION_AS_CONTINUUM_PROOF", "FINITE_CONTROLS_NEVER_PROVE_CONTINUUM", "REJECT_FINITE_AS_CONTINUUM_PROOF")
    if fixture_equals(p,("MODEL","QF4"),("CLAIM","ARBITRARY_INDEX_MULTIPLIER_IDENTITY")):
        model_size = int(p["MODEL"][2:])
        claim_quantifies_arbitrary_indices = p["CLAIM"] == "ARBITRARY_INDEX_MULTIPLIER_IDENTITY"
        if model_size == 4 and claim_quantifies_arbitrary_indices:
            return ("FINITE_C0_WINDOW_AS_ARBITRARY_INDEX_PROOF", "FINITE_CONTROLS_NEVER_PROVE_ARBITRARY_INDEX_THEOREM", "REJECT_FINITE_AS_ARBITRARY_INDEX_PROOF")
    if fixture_equals(p,("MODEL","CORE2_TAIL3"),("CLAIM","FAITHFUL_MULTIPLIER_CORONA")):
        core,tail = 2,3
        finite_quotient_dimension = tail
        if core+tail == 5 and finite_quotient_dimension > 0 and p["CLAIM"] == "FAITHFUL_MULTIPLIER_CORONA":
            return ("FINITE_TAIL_QUOTIENT_AS_CORONA_PROOF", "FINITE_QUOTIENT_MODEL_NOT_ACTUAL_CORONA", "REJECT_FINITE_AS_CORONA_PROOF")
    if fixture_equals(p,("SOURCE","PAPER2_PROP_UNCOUNTABLE"),("CREDIT","P13_NOVELTY")):
        inherited_owner = "PAPER2_PROP_UNCOUNTABLE"
        if p["SOURCE"] == inherited_owner and p["CREDIT"] != "PAPER2_ZERO_P13_CREDIT":
            return ("PAPER2_LOWER_BOUND_CREDIT_TO_P13", "PAPER2_LOWER_BOUND_ZERO_P13_CREDIT", "REJECT_INHERITED_CARDINALITY_CREDIT")
    if fixture_equals(p,("OWNER","Q_P_ACTUAL"),("TOPOLOGY","DISCRETE")):
        actual_topology = "INDISCRETE"
        if p["TOPOLOGY"] != actual_topology:
            return ("ACTUAL_QUOTIENT_GIVEN_DISCRETE_TOPOLOGY", "Q_P_ACTUAL_RETAINS_INDISCRETE_TOPOLOGY", "REJECT_ACTUAL_DISCRETE_PROMOTION")
    if fixture_equals(p,("OWNER","Q_P_BARE"),("TOPOLOGY","INDISCRETE")):
        bare_has_topology = False
        if p["TOPOLOGY"] and not bare_has_topology:
            return ("BARE_SET_GIVEN_TOPOLOGY", "Q_P_BARE_HAS_NO_TOPOLOGY", "REJECT_BARE_TOPOLOGY")
    if fixture_equals(p,("SOURCE","STD_GAMMA_P"),("TARGET","Q_P_ACTUAL"),("CLAIM","NONSECONDCOUNTABLE")):
        source_topology_owner = {"STD_GAMMA_P":"STANDARD"}.get(p["SOURCE"])
        target_topology_owner = {"Q_P_ACTUAL":"ACTUAL"}.get(p["TARGET"])
        if source_topology_owner == "STANDARD" and target_topology_owner == "ACTUAL":
            return ("STANDARD_FAILURE_ASSIGNED_TO_ACTUAL", "STANDARD_TOPOLOGY_NOT_TRANSPORTED_TO_ACTUAL", "REJECT_STANDARD_ACTUAL_OWNER_CONFLATION")
    if fixture_equals(p,("SOURCE","Q_P_DISC"),("TARGET","Q_P_ACTUAL"),("MAP","TOPOLOGICAL_IDENTITY")):
        if p["SOURCE"] != p["TARGET"] and p["MAP"] == "TOPOLOGICAL_IDENTITY":
            return ("DISCRETE_QUOTIENT_IDENTIFIED_WITH_ACTUAL", "ACTUAL_AND_DISCRETE_QUOTIENT_OWNERS_DISTINCT", "REJECT_DISCRETE_ACTUAL_IDENTITY")
    if fixture_equals(p,("OWNER","INFINITE_Q"),("CANDIDATE","PRODUCT_BOUNDED_EQ_C0_SUM")):
        constant_one_tail = [1] * 8
        c0_tail_tends_to_zero = all(value == 0 for value in constant_one_tail[-3:])
        if not c0_tail_tends_to_zero:
            return ("BOUNDED_MULTIPLIER_PRODUCT_IDENTIFIED_WITH_C0_ALGEBRA", "MULTIPLIER_PRODUCT_DISTINCT_FROM_C0_ALGEBRA", "REJECT_MULTIPLIER_ALGEBRA_CONFLATION")
    if fixture_equals(p,("Q","INFINITE"),("INPUT","ONE"),("CLAIM","ALGEBRA_MEMBER")):
        constant_norm = 1
        algebra_member = constant_norm == 0
        if not algebra_member and p["CLAIM"] == "ALGEBRA_MEMBER":
            return ("NONZERO_INFINITE_DIAGONAL_DECLARED_C0", "CONSTANT_NONZERO_NORM_NOT_C0", "REJECT_CONSTANT_NORM_C0_MEMBERSHIP")
    if fixture_equals(p,("Q","QF2"),("INPUT","ONE"),("CLAIM","CORONA_MAP_INJECTIVE")):
        finite_q = int(p["Q"][2:])
        diagonal_in_algebra = finite_q < 10 and p["INPUT"] == "ONE"
        if diagonal_in_algebra:
            return ("FINITE_Q_CORONA_MAP_DECLARED_INJECTIVE", "FINITE_BRANCH_DIAGONAL_LIES_IN_ALGEBRA", "REJECT_FINITE_BRANCH_CORONA_INJECTIVITY")
    if fixture_equals(p,("Q","INFINITE"),("CANDIDATE","KERNEL_STRICTLY_CONTAINS_PREIMAGE_A")):
        quotient_kernel_equals_preimage = True
        if quotient_kernel_equals_preimage and "STRICTLY_CONTAINS" in p["CANDIDATE"]:
            return ("CORONA_KERNEL_LARGER_THAN_INTERSECTION", "QUOTIENT_KERNEL_EQUALS_PREIMAGE_OF_ALGEBRA", "REJECT_QUOTIENT_KERNEL_MISMATCH")
    if fixture_equals(p,("RELATION","TAU_OVERLINE_SIGMA_EQ_DELTA_ALPHA"),("MAP","U_ALPHA_SIGMA_TO_TAU")):
        frozen_relation = "SIGMA_OVERLINE_TAU_EQ_DELTA_ALPHA"
        if p["RELATION"] != frozen_relation:
            return ("V2_GAUGE_ORIENTATION_REVERSED", "GAUGE_DIRECTION_SIGMA_OVERLINE_TAU_EQ_DELTA_ALPHA", "GAUGE_DIRECTION_MISMATCH")
    if fixture_equals(p,("MAX_STATUS","COPIED_COMMON_PASS"),("REDUCED_STATUS","COPIED_COMMON_PASS")):
        tokens_are_distinct = p["MAX_STATUS"] != p["REDUCED_STATUS"]
        prohibited_proof_claim = any(token in p["MAX_STATUS"] for token in ("PASS","PROVED","CONTROL_EVIDENCE"))
        if not tokens_are_distinct or prohibited_proof_claim:
            return ("MAX_REDUCED_EVIDENCE_CONFLATED", "MAX_REDUCED_EVIDENCE_SERIALIZED_SEPARATELY", "REJECT_MAX_REDUCED_EVIDENCE_CONFLATION")
    if fixture_equals(p,("SOURCE","V1_QP_FINITE_CONDITIONAL"),("CLAIM","V2_FIXED_PRIME_BRANCH")):
        if "CONDITIONAL" in p["SOURCE"] and p["CLAIM"] == "V2_FIXED_PRIME_BRANCH":
            return ("V1_CONDITIONAL_QP_BRANCH_USED_AS_V2_RESULT", "V1_CONDITIONAL_ROWS_ARE_IMMUTABLE_HISTORICAL_DIAGNOSTICS", "REJECT_V1_CONDITIONAL_AS_V2_BRANCH")
    if fixture_equals(p,("INPUT","H_LOG_P_Z"),("CLAIM","QP_CONTINUUM")):
        required_premises = {"PAPER2_LOWER", "P13_UPPER"}
        supplied_premises = {p["INPUT"]}
        if not required_premises.issubset(supplied_premises):
            return ("FIXED_PRIME_CONTINUUM_INFERRED_FROM_PERIOD_ONLY", "FIXED_PRIME_CARDINALITY_REQUIRES_PAPER2_LOWER_AND_P13_UPPER", "REJECT_PERIOD_ONLY_CARDINALITY_INFERENCE")
    if fixture_equals(p,("OWNER","STD_GLOBAL"),("CANDIDATE","TWISTED_GROUPOID_CSTAR")):
        authorized_owner = "COMPONENTWISE_AUTHOR_RECORD"
        if p["OWNER"] != authorized_owner:
            return ("GLOBAL_TWISTED_GROUPOID_CSTAR_PROMOTION_V2", "COMPONENTWISE_AUTHOR_RECORD_NOT_GLOBAL_TWISTED_GROUPOID_CSTAR", "REJECT_GLOBAL_TWISTED_FRAMEWORK_PROMOTION")
    if fixture_equals(p,("MANIFEST","PROOF_PATH_AND_NON_NULL_SHA256")):
        candidate = valid_manifest_firewall_skeleton()
        candidate["proof_path"] = "notes/concurrent-proof.md"
        proof = candidate["proof_binding"]
        assert isinstance(proof,dict)
        proof["concurrent_phase3_proof_hash_included"] = True
        proof["proof_sha256"] = "1"*64
        if manifest_firewall_failure(candidate) == "PROOF_BINDING":
            return ("CONCURRENT_PROOF_HASH_BINDING_V2", "CONTROL_MANIFEST_EXCLUDES_CONCURRENT_PROOF_BINDING", "REJECT_PROOF_HASH_BINDING")
    if fixture_equals(p,("MANIFEST","ARTIFACT_LIST_INCLUDES_MANIFEST_JSON_SHA256")):
        candidate = valid_manifest_firewall_skeleton()
        artifacts = candidate["artifacts"]
        assert isinstance(artifacts,list)
        artifacts.append({"path":"results/manifest.json","sha256":"1"*64})
        if manifest_firewall_failure(candidate) == "SELF_HASH":
            return ("MANIFEST_SELF_HASH_BINDING_V2", "MANIFEST_NEVER_HASHES_ITSELF", "REJECT_MANIFEST_SELF_HASH")
    if fixture_equals(p,("MANIFEST","OMIT_V2_DESIGN_HEAD_OR_AUTHORIZATION_GATE")):
        missing_head = valid_manifest_firewall_skeleton()
        missing_head.pop("design_head")
        missing_gate = valid_manifest_firewall_skeleton()
        bindings = missing_gate["bindings"]
        assert isinstance(bindings,list)
        missing_gate["bindings"] = [
            item for item in bindings
            if item["path"] != "notes/phase3_v2_design_gate.md"
        ]
        if all(
            manifest_firewall_failure(candidate) == "UNBOUND_AUTHORITY"
            for candidate in (missing_head, missing_gate)
        ):
            return ("V2_DESIGN_OR_GATE_UNBOUND", "MANIFEST_BINDS_V2_DESIGN_AND_GATE", "REJECT_UNBOUND_V2_AUTHORITY")
    raise ValidationError("v2 negative fixture has no semantic failure")


def detect_v2_negative(reason: str, fixture: str, violated: str) -> str:
    try:
        derived_reason, derived_lock, detector = derive_v2_negative(fixture)
    except ValidationError:
        raise
    except (AssertionError, KeyError, TypeError, ValueError) as exc:
        raise ValidationError("malformed v2 negative fixture") from exc
    if reason != derived_reason:
        raise ValidationError(f"v2 reason/fixture mismatch: {reason}")
    if violated != derived_lock:
        raise ValidationError(f"v2 lock/fixture mismatch: {reason}")
    return detector


def manifest_firewall_failure(candidate: Mapping[str, object]) -> str:
    """Return the first frozen DAG/firewall failure for a candidate object."""
    if not isinstance(candidate, Mapping):
        return "INVENTORY"

    def walk(value: object, path: Tuple[str, ...] = ()) -> str:
        """Recursively reject proof bindings and manifest self-digests.

        The canonical Paper-2 ``proof_audit.md`` authority is an ordinary
        frozen binding value and is deliberately allowed.  What is forbidden
        is a field that tries to bind a concurrent proof or the manifest's
        own path/digest.
        """
        if isinstance(value, Mapping):
            for raw_key, child in value.items():
                key = str(raw_key)
                lowered = key.lower()
                child_path = path + (key,)
                in_proof_policy = child_path[:1] == ("proof_binding",)
                if in_proof_policy:
                    if child_path == ("proof_binding",):
                        pass
                    elif len(child_path) == 2 and key in {
                        "concurrent_phase3_proof_hash_included", "policy"
                    }:
                        pass
                    else:
                        return "PROOF_BINDING"
                elif "proof" in lowered:
                    return "PROOF_BINDING"
                if "manifest" in lowered and any(
                    marker in lowered for marker in ("sha", "digest", "hash")
                ):
                    return "SELF_HASH"
                failure = walk(child, child_path)
                if failure:
                    return failure
        elif isinstance(value, list):
            for index, child in enumerate(value):
                failure = walk(child, path + (str(index),))
                if failure:
                    return failure
        elif isinstance(value, str):
            lowered_value = value.lower()
            allowed_policy = (
                path == ("proof_binding","policy")
                and value == "POST_PROOF_AUDIT_BINDS_SEPARATELY"
            )
            allowed_paper2_authority = (
                len(path) == 3
                and path[0] == "bindings"
                and path[2] == "path"
                and value == "papers/2-flow-zeta/notes/proof_audit.md"
            )
            if "proof" in lowered_value and not (allowed_policy or allowed_paper2_authority):
                return "PROOF_BINDING"
            if value == "results/manifest.json" and path[-1:] == ("path",):
                return "SELF_HASH"
        return ""

    proof = candidate.get("proof_binding")
    if not isinstance(proof, dict):
        return "PROOF_BINDING"
    if proof != {
        "concurrent_phase3_proof_hash_included": False,
        "policy": "POST_PROOF_AUDIT_BINDS_SEPARATELY",
    }:
        return "PROOF_BINDING"
    recursive_failure = walk(candidate)
    if recursive_failure:
        return recursive_failure
    artifacts = candidate.get("artifacts")
    if not isinstance(artifacts, list):
        return "SELF_HASH"
    if candidate.get("design_head") != DESIGN_HEAD:
        return "UNBOUND_AUTHORITY"
    bindings = candidate.get("bindings")
    if not isinstance(bindings, list):
        return "UNBOUND_AUTHORITY"
    canonical_bindings = [{"path":path,"sha256":digest} for path,digest in sorted(BINDINGS.items())]
    if bindings != canonical_bindings:
        return "UNBOUND_AUTHORITY"
    implementation = candidate.get("implementation")
    if not isinstance(implementation,list) or [item.get("path") for item in implementation if isinstance(item,dict)] != list(sorted(IMPLEMENTATION_PATHS)) or len(implementation)!=6:
        return "INVENTORY"
    artifact_paths = [item.get("path") for item in artifacts if isinstance(item,dict)]
    if artifact_paths != [f"results/{name}" for name in ARTIFACT_ORDER] or len(artifacts)!=12:
        return "INVENTORY"
    return ""


V2_INPUTS = (("ZERO",(0,0)),("ONE",(1,0)),("I",(0,1)))
V2_FINITE_CASES = (("GENERIC_COMMON_LATTICE_QF1",1),("GENERIC_COMMON_LATTICE_QF2",2),("GENERIC_COMMON_LATTICE_QF4",4))
V2_INFINITE_CASES = (
    ("GENERIC_COMMON_LATTICE_QINF_N","INFINITE","COUNTABLY_INFINITE","NOT_APPLICABLE","GENERIC_INFINITE_BRANCH","ANALYTIC_INFINITE_BRANCH_LEDGER_NOT_FINITE_PROOF"),
    ("GENERIC_COMMON_LATTICE_QINF_UNCOUNTABLE","INFINITE","UNCOUNTABLE_SYMBOLIC","NOT_APPLICABLE","GENERIC_INFINITE_BRANCH","ANALYTIC_INFINITE_BRANCH_LEDGER_NOT_FINITE_PROOF"),
    ("FIXED_PRIME_RATIONAL_WITT_QP","CONTINUUM","2^ALEPH_0","PAPER2_LOWER_BOUND_INHERITED_ZERO_P13_CREDIT","UNCONDITIONAL_FIXED_PRIME_PAPER2_LOWER_PLUS_P13_UPPER","FIXED_PRIME_ANALYTIC_BRANCH_LEDGER_NOT_CONTROL_PROOF"),
)
V2_TAIL_CASES = (("FINITE_QUOTIENT_CORE0_TAIL1",0,1),("FINITE_QUOTIENT_CORE2_TAIL3",2,3))
V2_OWNER_ROWS = (
    ("PAPER2_LOWER_BOUND_OWNER","CONTINUUM_LOWER_BOUND","PAPER2_PROP_UNCOUNTABLE_ZERO_P13_CREDIT","Q_P_BARE_NO_TOPOLOGY","INHERITED_FIXED_PRIME_PREMISE","CLAIM=QP_CONTINUUM_LOWER_BOUND"),
    ("P13_EQUALITY_CLOSURE_OWNER","CONTINUUM","P13_UPPER_BOUND_EQUALITY_SUPPORTING_ONLY","Q_P_BARE_NO_TOPOLOGY","UNCONDITIONAL_FIXED_PRIME_BRANCH","CLAIM=QP_EXACT_CARDINALITY_EQUALITY"),
    ("ACTUAL_QUOTIENT_OWNER","ACTUAL","PAPER9_ACTUAL_OWNER","Q_P_ACTUAL_INDISCRETE_SECOND_COUNTABLE_NONHAUSDORFF","FIXED_PRIME_OWNER_SPLIT","CLAIM=ACTUAL_QUOTIENT_TOPOLOGY"),
    ("BARE_INDEX_OWNER","BARE","PAPER2_LOWER_PLUS_P13_UPPER_RETYPE","Q_P_BARE_NO_TOPOLOGY","FIXED_PRIME_OWNER_SPLIT","CLAIM=BARE_CARDINALITY_ONLY"),
    ("STANDARD_UNIT_OWNER","STANDARD","PAPER12_STANDARD_OWNER_P13_DIRECT_CONSEQUENCE","STD_GAMMA_P_NONSECONDCOUNTABLE_NONSIGMACOMPACT","FIXED_PRIME_OWNER_SPLIT","CLAIM=STANDARD_UNIT_TOPOLOGY_FAILURES"),
    ("STANDARD_ARROW_OWNER","STANDARD_ARROW","PAPER12_STANDARD_OWNER_P13_DIRECT_CONSEQUENCE","STD_ARROW_P_NONSECONDCOUNTABLE_NONSIGMACOMPACT","FIXED_PRIME_OWNER_SPLIT","CLAIM=STANDARD_ARROW_TOPOLOGY_FAILURES"),
    ("DISCRETE_QUOTIENT_OWNER","DISCRETE","PAPER12_DISCRETE_OWNER_P13_DIRECT_CONSEQUENCE","Q_P_DISC_NONSECONDCOUNTABLE_NONSIGMACOMPACT","FIXED_PRIME_OWNER_SPLIT","CLAIM=DISCRETE_QUOTIENT_TOPOLOGY_FAILURES"),
    ("GENERIC_BARE_COMPONENT_INDEX_OWNER","BARE","NOT_APPLICABLE","Q_BARE_NO_TOPOLOGY","GENERIC_BRANCH","CLAIM=ARBITRARY_INDEX_OWNER"),
)
V2_EVIDENCE_ROWS = (
    ("COMPONENT_MAX_NORM","max","DIRECT_COMPONENT_MAX_RESTRICTION_CHAIN_REQUIRED","","CLAIM=COMPONENT_MAX_UPPER_AND_REGULAR_LOWER"),
    ("COMPONENT_REDUCED_NORM","r","","EVERY_UNIT_REGULAR_RESTRICTION_REQUIRED","CLAIM=EVERY_UNIT_REDUCED_RESTRICTION"),
    ("TIME_AMENABLE_ENDPOINT_EQUALITY","both","TIME_MAX_NORM_ENDPOINT_REQUIRED","TIME_REDUCED_NORM_ENDPOINT_REQUIRED","CLAIM=TIME_AMENABILITY_ENDPOINT_EQUALITY"),
    ("MAX_REDUCED_SERIALIZATION","separate","SEPARATE_MAX_EVIDENCE_STATUS_REQUIRED","SEPARATE_REDUCED_EVIDENCE_STATUS_REQUIRED","CLAIM=MAX_REDUCED_SERIALIZED_SEPARATELY"),
)


def scalar_norm_from_pair(value: Gaussian) -> int:
    squared = value[0]*value[0] + value[1]*value[1]
    if squared not in {0,1}:
        raise ValidationError("v2 scalar is outside the exact zero/unit fixtures")
    return squared


def scalar_norm_class(value: Gaussian) -> str:
    return "CONSTANT_0" if scalar_norm_from_pair(value) == 0 else "CONSTANT_1"


def v2_gauge_lhs_exp(k: int, t: int, tau: str) -> int:
    if tau != "ONE":
        raise ValidationError("v2 gauge lhs requires tau=ONE")
    return ((-k) * (t*t)) % 24


def v2_gauge_rhs_exp(k: int, t: int, tau: str, orientation: str) -> int:
    if tau != "ONE" or orientation != "SIGMA_OVERLINE_TAU_EQ_DELTA_ALPHA":
        raise ValidationError("v2 gauge rhs orientation mismatch")
    coefficient = 0 - k
    return (coefficient * t * t + 24*(abs(t)+1)) % 24


def discover_unittest_method_count() -> int:
    path = PAPER_DIR / "code/test_controls.py"
    module_name = "_p13_controls_discovery"
    spec = importlib.util.spec_from_file_location(module_name,path)
    if spec is None or spec.loader is None:
        raise ValidationError("cannot load unittest module for discovery")
    module = importlib.util.module_from_spec(spec)
    previous = sys.modules.get(module_name)
    sys.modules[module_name] = module
    try:
        spec.loader.exec_module(module)
        suite = unittest.defaultTestLoader.loadTestsFromModule(module)
        count = suite.countTestCases()
        declared = module.discoverable_method_count()
    finally:
        if previous is None:
            sys.modules.pop(module_name,None)
        else:
            sys.modules[module_name] = previous
    if count != declared:
        raise ValidationError("unittest declared/discovered count mismatch")
    return count


def _default_v1_context() -> Dict[str,List[Dict[str,str]]]:
    return {name:GENERATORS[name]() for name in ARTIFACT_ORDER[:11]}


def generate_v2(v1_context: Mapping[str,Sequence[Mapping[str,str]]] | None = None, test_method_count: int | None = None) -> List[Dict[str, str]]:
    h = HEADERS["completion_corona_controls_v2.csv"]
    rows: List[Dict[str, str]] = []

    def add(family: str, kind: str, oracle: str, **values: object) -> None:
        rows.append(make_row(h, schema_version=SCHEMA_V2, row_id=f"V2-{len(rows)+1:04d}", control_family=family, case_kind=kind, oracle=oracle, tolerance=0, status="", **values))

    finite_scalar_kernel_nontrivial = any(
        scalar_norm_from_pair(scalar) != 0 for _input_id,scalar in V2_INPUTS
    )
    for owner, size in V2_FINITE_CASES:
        for input_id, scalar in V2_INPUTS:
            norm,norm_class = scalar_norm_from_pair(scalar),scalar_norm_class(scalar)
            coordinates = [scalar for _index in range(size)]
            coordinate_norms = [re*re+im*im for re,im in coordinates]
            multiplier_member = bool(coordinates) and max(coordinate_norms,default=0) <= 1
            algebra_member = len(coordinates) == size
            finite_c0_member = all(value in {0,1} for value in coordinate_norms)
            quotient_distance = 0 if algebra_member else max(coordinate_norms,default=0)
            quotient_image_nonzero = quotient_distance != 0
            quotient_map_injective = not finite_scalar_kernel_nontrivial
            for epsilon in ("max","r"):
                add("FINITE_C0_MODEL","DIAGNOSTIC","FINITE_C0_CONSTANT_COORDINATE_MODEL",owner_case=owner,q_class="FINITE",q_model_size=size,epsilon=epsilon,input_id=input_id,input_norm=norm,coordinate_norm_class=norm_class,multiplier_member=multiplier_member,algebra_member=algebra_member,finite_c0_member=finite_c0_member,quotient_distance=quotient_distance,quotient_image_nonzero=quotient_image_nonzero,quotient_map_injective=quotient_map_injective,max_evidence_status="FINITE_SCALAR_MAX_NORM_DIAGNOSTIC_ONLY" if epsilon=="max" else "",reduced_evidence_status="FINITE_SCALAR_REDUCED_NORM_DIAGNOSTIC_ONLY" if epsilon=="r" else "",cardinality_credit_owner="NOT_APPLICABLE",topology_owner="Q_BARE_INDEX_ONLY",fixed_prime_branch="GENERIC_FINITE_BRANCH",evidence_scope="FINITE_SCALAR_C0_MODEL_ONLY")
    infinite_scalar_kernel_is_zero = all(
        (scalar_norm_from_pair(scalar) == 0) == (input_id == "ZERO")
        for input_id,scalar in V2_INPUTS
    )
    for owner,q_class,size,credit,branch,scope in V2_INFINITE_CASES:
        for input_id,scalar in V2_INPUTS:
            norm,norm_class = scalar_norm_from_pair(scalar),scalar_norm_class(scalar)
            constant_tail = [norm for _index in range(8)]
            multiplier_member = max(constant_tail,default=0) <= 1
            algebra_member = all(value == 0 for value in constant_tail[-4:])
            quotient_distance = max(constant_tail,default=0)
            quotient_image_nonzero = quotient_distance != 0
            quotient_map_injective = infinite_scalar_kernel_is_zero
            for epsilon in ("max","r"):
                add("INFINITE_ANALYTIC_BOUNDARY","DIAGNOSTIC","INFINITE_CONSTANT_NORM_C0_CORONA_BRANCH",owner_case=owner,q_class=q_class,q_model_size=size,epsilon=epsilon,input_id=input_id,input_norm=norm,coordinate_norm_class=norm_class,multiplier_member=multiplier_member,algebra_member=algebra_member,quotient_distance=quotient_distance,quotient_image_nonzero=quotient_image_nonzero,quotient_map_injective=quotient_map_injective,max_evidence_status="ANALYTIC_MAX_BRANCH_REQUIRES_THEOREM_PROOF" if epsilon=="max" else "",reduced_evidence_status="ANALYTIC_REDUCED_BRANCH_REQUIRES_THEOREM_PROOF" if epsilon=="r" else "",cardinality_credit_owner=credit,topology_owner="Q_BARE_INDEX_ONLY",fixed_prime_branch=branch,evidence_scope=scope)
    for owner,core,tail in V2_TAIL_CASES:
        size = core+tail
        for input_id,scalar in V2_INPUTS:
            norm,norm_class = scalar_norm_from_pair(scalar),scalar_norm_class(scalar)
            for epsilon in ("max","r"):
                add("FINITE_TAIL_QUOTIENT_MODEL","DIAGNOSTIC","FINITE_TAIL_SUP_QUOTIENT_DISTANCE",owner_case=owner,q_class="FINITE_QUOTIENT_MODEL",q_model_size=size,epsilon=epsilon,input_id=input_id,input_norm=norm,coordinate_norm_class=norm_class,tail_window_size=tail,quotient_distance=norm,quotient_image_nonzero=norm!=0,quotient_map_injective=True,max_evidence_status="FINITE_TAIL_MAX_QUOTIENT_MODEL_ONLY" if epsilon=="max" else "",reduced_evidence_status="FINITE_TAIL_REDUCED_QUOTIENT_MODEL_ONLY" if epsilon=="r" else "",cardinality_credit_owner="NOT_APPLICABLE",topology_owner="NO_ACTUAL_OR_STANDARD_OWNER_FINITE_MODEL",fixed_prime_branch="NOT_APPLICABLE",evidence_scope="FINITE_IDEAL_QUOTIENT_MODEL_NOT_MULTIPLIER_CORONA_PROOF")
    gauge_ids = {-6:"ALPHA_K_MINUS6",-1:"ALPHA_K_MINUS1",0:"ALPHA_K_0",6:"ALPHA_K_6"}
    term_ids = {-1:"TERM_MINUS1",0:"TERM_0",1:"TERM_1"}
    for k in K24:
        for t in (-1,0,1):
            for epsilon in ("max","r"):
                lhs = v2_gauge_lhs_exp(k,t,"ONE")
                rhs = v2_gauge_rhs_exp(k,t,"ONE","SIGMA_OVERLINE_TAU_EQ_DELTA_ALPHA")
                add("GAUGE_COMMUTATION_MODEL","DIAGNOSTIC","FROZEN_COMPONENT_DIAGONAL_GAUGE_TERM",owner_case="GENERIC_ORIGIN_FREE_COMPONENT_GAUGE_TERM",q_class="FINITE_SYMBOLIC_COMPONENT",q_model_size=1,epsilon=epsilon,input_id=term_ids[t],input_norm=1,coordinate_norm_class="CONSTANT_1",gauge_id=gauge_ids[k],gauge_lhs_exp_mod24=lhs,gauge_rhs_exp_mod24=rhs,gauge_commutes=lhs==rhs,max_evidence_status="DENSE_MAX_GAUGE_IDENTITY_EXTENSION_REQUIRES_PROOF" if epsilon=="max" else "",reduced_evidence_status="DENSE_REDUCED_GAUGE_IDENTITY_EXTENSION_REQUIRES_PROOF" if epsilon=="r" else "",cardinality_credit_owner="NOT_APPLICABLE",topology_owner="ORIGIN_FREE_COMPONENT_OWNER",fixed_prime_branch="GENERIC_NOT_FIXED_PRIME",evidence_scope="FINITE_GAUGE_TERM_DIAGNOSTIC_NOT_COMPLETION_SQUARE_PROOF",fixture=f"K={k};T={t};TAU=ONE;ORIENTATION=SIGMA_OVERLINE_TAU_EQ_DELTA_ALPHA")
    for owner,q_class,credit,topology,branch,fixture in V2_OWNER_ROWS:
        add("OWNER_CREDIT_LEDGER","DIAGNOSTIC","OWNER_CREDIT_TOPOLOGY_EXACT_TOKEN",owner_case=owner,q_class=q_class,cardinality_credit_owner=credit,topology_owner=topology,fixed_prime_branch=branch,evidence_scope="OWNER_CREDIT_LEDGER_ONLY",fixture=fixture)
    for owner,epsilon,max_status,reduced_status,fixture in V2_EVIDENCE_ROWS:
        add("MAX_REDUCED_EVIDENCE_LEDGER","DIAGNOSTIC","MAX_REDUCED_EVIDENCE_SEPARATION",owner_case=owner,q_class="ARBITRARY_Q_BARE",epsilon=epsilon,max_evidence_status=max_status,reduced_evidence_status=reduced_status,topology_owner="COMPONENT_RECORDS_B_Q_MAX_OR_R",evidence_scope="EVIDENCE_STATUS_LEDGER_NOT_NORM_PROOF",fixture=fixture)
    for reason,fixture,violated,expected in V2_NEGATIVES:
        observed = detect_v2_negative(reason,fixture,violated)
        add("FIREWALL_NEGATIVE","NEGATIVE","EXPECTED_DETECTOR_TOKEN",owner_case="FIREWALL_ATTEMPT",evidence_scope="FAIL_CLOSED_V2_CLAIM_AND_MANIFEST_FIREWALL",negative_reason=reason,fixture=fixture,violated_lock=violated,expected_detector=expected,observed_detector=observed)
    context = dict(v1_context) if v1_context is not None else _default_v1_context()
    discovered = discover_unittest_method_count() if test_method_count is None else test_method_count
    summaries = []
    for i,name in enumerate(ARTIFACT_ORDER,1):
        if name == "completion_corona_controls_v2.csv":
            count,columns,negatives = len(rows)+13,len(h),sum(r["case_kind"]=="NEGATIVE" for r in rows)
        else:
            emitted = context[name]
            count,columns = len(emitted),len(HEADERS[name])
            negatives = sum(r.get("case_kind")=="NEGATIVE" for r in emitted)
        summaries.append((f"ARTIFACT_{i:02d}",name,count,columns,negatives,"", "V2_NEW_BODY" if name.endswith("_v2.csv") else "V1_BODY_BYTE_IDENTITY"))
    summaries.append(("PACKAGE","PACKAGE_TOTAL_V2",sum(item[2] for item in summaries),"MIXED",sum(item[4] for item in summaries),discovered,"V2_PACKAGE_AGGREGATE"))
    for owner,artifact,count,columns,negatives,methods,scope in summaries:
        add("V2_PACKAGE_SUMMARY","SUMMARY","V2_COUNT_SCHEMA_NEGATIVE_TOTAL",owner_case=owner,summary_artifact=artifact,summary_rows=count,summary_columns=columns,summary_negative_rows=negatives,summary_test_methods=methods,evidence_scope=scope)
    validate_v2_families(rows,context,discovered,finalize=True)
    return rows


def validate_v2_families(
    rows: Sequence[MutableMapping[str,str]],
    v1_context: Mapping[str,Sequence[Mapping[str,str]]],
    test_method_count: int,
    *,
    finalize: bool = False,
) -> None:
    """Independently reconstruct and validate every v2 family.

    Generation supplies blank statuses.  Only after this full reconstruction
    succeeds does ``finalize=True`` assign PASS.  Validation of serialized
    rows requires the already-derived PASS token and never repairs it.
    """
    h = HEADERS["completion_corona_controls_v2.csv"]
    expected: List[Dict[str,str]] = []

    # Candidate negative rows are interpreted from their own fixture bytes.
    # This must precede comparison with the frozen registry so fixture,
    # reason, lock, expected-detector, and observed-detector corruptions remain
    # five distinct fail-closed classes.
    for index,row in enumerate(rows,1):
        if row.get("control_family") != "FIREWALL_NEGATIVE":
            continue
        try:
            reason,lock,detector = derive_v2_negative(row.get("fixture", ""))
        except ValidationError as exc:
            raise ValidationError(f"V2_NEGATIVE_FIXTURE:{index}") from exc
        if row.get("negative_reason") != reason:
            raise ValidationError(f"V2_NEGATIVE_REASON:{index}")
        if row.get("violated_lock") != lock:
            raise ValidationError(f"V2_NEGATIVE_LOCK:{index}")
        if row.get("expected_detector") != detector:
            raise ValidationError(f"V2_NEGATIVE_EXPECTED_DETECTOR:{index}")
        if row.get("observed_detector") != detector:
            raise ValidationError(f"V2_NEGATIVE_OBSERVED_DETECTOR:{index}")

    def emit(family: str,kind: str,oracle: str,**values: object) -> None:
        expected.append(make_row(h,schema_version=SCHEMA_V2,row_id=f"V2-{len(expected)+1:04d}",control_family=family,case_kind=kind,oracle=oracle,tolerance=0,status="" if finalize else "PASS",**values))

    finite_domain_model = {
        input_id:(re,im) for input_id,(re,im) in V2_INPUTS
    }
    finite_kernel = {
        input_id for input_id,(re,im) in finite_domain_model.items()
        if re*re+im*im > 0
    }
    finite_map_injective = len(finite_kernel) == 0
    for owner,size in V2_FINITE_CASES:
        for input_id,(re,im) in V2_INPUTS:
            norm = re*re+im*im
            if norm not in {0,1}:
                raise ValidationError("V2_SCALAR_NORM")
            norm_class = "CONSTANT_0" if norm == 0 else "CONSTANT_1"
            coordinates = tuple((re,im) for _index in range(size))
            coordinate_norms = tuple(x*x+y*y for x,y in coordinates)
            bounded_product_member = len(coordinates)==size and max(coordinate_norms,default=0)<2
            finite_algebra_member = all(index < size for index,_value in enumerate(coordinates))
            finite_c0_member = all(
                sum(1 for value in coordinate_norms if value >= threshold) <= size
                for threshold in (1,)
            )
            ideal_distance = 0 if finite_algebra_member else max(coordinate_norms,default=0)
            for epsilon in ("max","r"):
                emit("FINITE_C0_MODEL","DIAGNOSTIC","FINITE_C0_CONSTANT_COORDINATE_MODEL",owner_case=owner,q_class="FINITE",q_model_size=size,epsilon=epsilon,input_id=input_id,input_norm=norm,coordinate_norm_class=norm_class,multiplier_member=bounded_product_member,algebra_member=finite_algebra_member,finite_c0_member=finite_c0_member,quotient_distance=ideal_distance,quotient_image_nonzero=ideal_distance!=0,quotient_map_injective=finite_map_injective,max_evidence_status="FINITE_SCALAR_MAX_NORM_DIAGNOSTIC_ONLY" if epsilon=="max" else "",reduced_evidence_status="FINITE_SCALAR_REDUCED_NORM_DIAGNOSTIC_ONLY" if epsilon=="r" else "",cardinality_credit_owner="NOT_APPLICABLE",topology_owner="Q_BARE_INDEX_ONLY",fixed_prime_branch="GENERIC_FINITE_BRANCH",evidence_scope="FINITE_SCALAR_C0_MODEL_ONLY")
    infinite_input_receipts = {
        input_id:(re*re+im*im) for input_id,(re,im) in V2_INPUTS
    }
    infinite_kernel = {
        input_id for input_id,norm in infinite_input_receipts.items() if norm == 0
    }
    infinite_map_injective = infinite_kernel == {"ZERO"}
    for owner,q_class,size,credit,branch,scope in V2_INFINITE_CASES:
        for input_id,(re,im) in V2_INPUTS:
            norm = re*re+im*im
            norm_class = "CONSTANT_0" if norm == 0 else "CONSTANT_1"
            constant_prefix = tuple(norm for _index in range(12))
            multiplier_member = max(constant_prefix,default=0) < 2
            algebra_member = all(value==0 for value in constant_prefix[6:])
            quotient_distance = max(constant_prefix[6:],default=0)
            for epsilon in ("max","r"):
                emit("INFINITE_ANALYTIC_BOUNDARY","DIAGNOSTIC","INFINITE_CONSTANT_NORM_C0_CORONA_BRANCH",owner_case=owner,q_class=q_class,q_model_size=size,epsilon=epsilon,input_id=input_id,input_norm=norm,coordinate_norm_class=norm_class,multiplier_member=multiplier_member,algebra_member=algebra_member,quotient_distance=quotient_distance,quotient_image_nonzero=quotient_distance!=0,quotient_map_injective=infinite_map_injective,max_evidence_status="ANALYTIC_MAX_BRANCH_REQUIRES_THEOREM_PROOF" if epsilon=="max" else "",reduced_evidence_status="ANALYTIC_REDUCED_BRANCH_REQUIRES_THEOREM_PROOF" if epsilon=="r" else "",cardinality_credit_owner=credit,topology_owner="Q_BARE_INDEX_ONLY",fixed_prime_branch=branch,evidence_scope=scope)
    for owner,core,tail in V2_TAIL_CASES:
        if tail <= 0:
            raise ValidationError("V2_TAIL_EMPTY")
        for input_id,(re,im) in V2_INPUTS:
            norm = re*re+im*im
            vector = [(re,im)]*(core+tail)
            ideal_quotient_tail = vector[core:]
            distance = max((x*x+y*y for x,y in ideal_quotient_tail),default=0)
            norm_class = "CONSTANT_0" if norm == 0 else "CONSTANT_1"
            for epsilon in ("max","r"):
                emit("FINITE_TAIL_QUOTIENT_MODEL","DIAGNOSTIC","FINITE_TAIL_SUP_QUOTIENT_DISTANCE",owner_case=owner,q_class="FINITE_QUOTIENT_MODEL",q_model_size=core+tail,epsilon=epsilon,input_id=input_id,input_norm=norm,coordinate_norm_class=norm_class,tail_window_size=tail,quotient_distance=distance,quotient_image_nonzero=distance!=0,quotient_map_injective=len(ideal_quotient_tail)>0,max_evidence_status="FINITE_TAIL_MAX_QUOTIENT_MODEL_ONLY" if epsilon=="max" else "",reduced_evidence_status="FINITE_TAIL_REDUCED_QUOTIENT_MODEL_ONLY" if epsilon=="r" else "",cardinality_credit_owner="NOT_APPLICABLE",topology_owner="NO_ACTUAL_OR_STANDARD_OWNER_FINITE_MODEL",fixed_prime_branch="NOT_APPLICABLE",evidence_scope="FINITE_IDEAL_QUOTIENT_MODEL_NOT_MULTIPLIER_CORONA_PROOF")
    gauge_ids = {-6:"ALPHA_K_MINUS6",-1:"ALPHA_K_MINUS1",0:"ALPHA_K_0",6:"ALPHA_K_6"}
    term_ids = {-1:"TERM_MINUS1",0:"TERM_0",1:"TERM_1"}
    for k in K24:
        for t in (-1,0,1):
            fixture = f"K={k};T={t};TAU=ONE;ORIENTATION=SIGMA_OVERLINE_TAU_EQ_DELTA_ALPHA"
            parsed = parse_fixture(fixture)
            if tuple(parsed) != ("K","T","TAU","ORIENTATION"):
                raise ValidationError("V2_GAUGE_FIXTURE")
            lhs = (-int(parsed["K"])*int(parsed["T"])*int(parsed["T"])) % 24
            rhs_coefficient = -int(parsed["K"])
            rhs = (rhs_coefficient*(int(parsed["T"])**2)) % 24 if parsed["TAU"]=="ONE" and parsed["ORIENTATION"]=="SIGMA_OVERLINE_TAU_EQ_DELTA_ALPHA" else -1
            if lhs != rhs:
                raise ValidationError("V2_GAUGE_WITNESS")
            for epsilon in ("max","r"):
                emit("GAUGE_COMMUTATION_MODEL","DIAGNOSTIC","FROZEN_COMPONENT_DIAGONAL_GAUGE_TERM",owner_case="GENERIC_ORIGIN_FREE_COMPONENT_GAUGE_TERM",q_class="FINITE_SYMBOLIC_COMPONENT",q_model_size=1,epsilon=epsilon,input_id=term_ids[t],input_norm=1,coordinate_norm_class="CONSTANT_1",gauge_id=gauge_ids[k],gauge_lhs_exp_mod24=lhs,gauge_rhs_exp_mod24=rhs,gauge_commutes=lhs==rhs,max_evidence_status="DENSE_MAX_GAUGE_IDENTITY_EXTENSION_REQUIRES_PROOF" if epsilon=="max" else "",reduced_evidence_status="DENSE_REDUCED_GAUGE_IDENTITY_EXTENSION_REQUIRES_PROOF" if epsilon=="r" else "",cardinality_credit_owner="NOT_APPLICABLE",topology_owner="ORIGIN_FREE_COMPONENT_OWNER",fixed_prime_branch="GENERIC_NOT_FIXED_PRIME",evidence_scope="FINITE_GAUGE_TERM_DIAGNOSTIC_NOT_COMPLETION_SQUARE_PROOF",fixture=fixture)
    for owner,q_class,credit,topology,branch,fixture in V2_OWNER_ROWS:
        parsed = parse_fixture(fixture)
        if not fixture_equals(parsed,("CLAIM",parsed.get("CLAIM",""))):
            raise ValidationError("V2_OWNER_FIXTURE")
        emit("OWNER_CREDIT_LEDGER","DIAGNOSTIC","OWNER_CREDIT_TOPOLOGY_EXACT_TOKEN",owner_case=owner,q_class=q_class,cardinality_credit_owner=credit,topology_owner=topology,fixed_prime_branch=branch,evidence_scope="OWNER_CREDIT_LEDGER_ONLY",fixture=fixture)
    for owner,epsilon,max_status,reduced_status,fixture in V2_EVIDENCE_ROWS:
        if not max_status and not reduced_status:
            raise ValidationError("V2_EVIDENCE_EMPTY")
        if max_status == reduced_status and max_status:
            raise ValidationError("V2_EVIDENCE_CONFLATED")
        if any(word in token for token in (max_status,reduced_status) for word in ("PASS","PROVED","CONTROL_EVIDENCE")):
            raise ValidationError("V2_EVIDENCE_PROOF_PROMOTION")
        emit("MAX_REDUCED_EVIDENCE_LEDGER","DIAGNOSTIC","MAX_REDUCED_EVIDENCE_SEPARATION",owner_case=owner,q_class="ARBITRARY_Q_BARE",epsilon=epsilon,max_evidence_status=max_status,reduced_evidence_status=reduced_status,topology_owner="COMPONENT_RECORDS_B_Q_MAX_OR_R",evidence_scope="EVIDENCE_STATUS_LEDGER_NOT_NORM_PROOF",fixture=fixture)
    for registered_reason,fixture,registered_lock,registered_detector in V2_NEGATIVES:
        reason,lock,detector = derive_v2_negative(fixture)
        if (reason,lock,detector) != (registered_reason,registered_lock,registered_detector):
            raise ValidationError("V2_NEGATIVE_REGISTRY")
        emit("FIREWALL_NEGATIVE","NEGATIVE","EXPECTED_DETECTOR_TOKEN",owner_case="FIREWALL_ATTEMPT",evidence_scope="FAIL_CLOSED_V2_CLAIM_AND_MANIFEST_FIREWALL",negative_reason=reason,fixture=fixture,violated_lock=lock,expected_detector=detector,observed_detector=detector)
    summaries: List[Tuple[str,str,int,object,int,object,str]] = []
    for i,name in enumerate(ARTIFACT_ORDER,1):
        if name == "completion_corona_controls_v2.csv":
            count,columns,negatives = len(rows),len(h),sum(r.get("case_kind")=="NEGATIVE" for r in rows)
        else:
            if name not in v1_context:
                raise ValidationError("V2_SUMMARY_MISSING_ARTIFACT")
            emitted = v1_context[name]
            count,columns = len(emitted),len(HEADERS[name])
            negatives = sum(r.get("case_kind")=="NEGATIVE" for r in emitted)
        summaries.append((f"ARTIFACT_{i:02d}",name,count,columns,negatives,"","V2_NEW_BODY" if name.endswith("_v2.csv") else "V1_BODY_BYTE_IDENTITY"))
    summaries.append(("PACKAGE","PACKAGE_TOTAL_V2",sum(x[2] for x in summaries),"MIXED",sum(x[4] for x in summaries),test_method_count,"V2_PACKAGE_AGGREGATE"))
    for owner,artifact,count,columns,negatives,methods,scope in summaries:
        emit("V2_PACKAGE_SUMMARY","SUMMARY","V2_COUNT_SCHEMA_NEGATIVE_TOTAL",owner_case=owner,summary_artifact=artifact,summary_rows=count,summary_columns=columns,summary_negative_rows=negatives,summary_test_methods=methods,evidence_scope=scope)
    if len(rows) != 117 or len(expected) != 117:
        raise ValidationError("V2_ROW_COUNT")
    family_counts = [(name,sum(row["control_family"]==name for row in rows)) for name in (
        "FINITE_C0_MODEL","INFINITE_ANALYTIC_BOUNDARY","FINITE_TAIL_QUOTIENT_MODEL","GAUGE_COMMUTATION_MODEL","OWNER_CREDIT_LEDGER","MAX_REDUCED_EVIDENCE_LEDGER","FIREWALL_NEGATIVE","V2_PACKAGE_SUMMARY")]
    if family_counts != [("FINITE_C0_MODEL",18),("INFINITE_ANALYTIC_BOUNDARY",18),("FINITE_TAIL_QUOTIENT_MODEL",12),("GAUGE_COMMUTATION_MODEL",24),("OWNER_CREDIT_LEDGER",8),("MAX_REDUCED_EVIDENCE_LEDGER",4),("FIREWALL_NEGATIVE",20),("V2_PACKAGE_SUMMARY",13)]:
        raise ValidationError("V2_FAMILY_COUNT")
    kind_counts = {
        kind:sum(row.get("case_kind")==kind for row in rows)
        for kind in ("DIAGNOSTIC","NEGATIVE","SUMMARY")
    }
    if kind_counts != {"DIAGNOSTIC":84,"NEGATIVE":20,"SUMMARY":13}:
        raise ValidationError("V2_ROW_KIND_COUNT")
    for index,(actual,wanted) in enumerate(zip(rows,expected),1):
        if list(actual) != h:
            raise ValidationError("V2_HEADER")
        for key in h:
            if actual[key] != wanted[key]:
                raise ValidationError(f"V2_FIELD_{key}:{index}")
    if finalize:
        for row in rows:
            row["status"] = "PASS"


GENERATORS = {
    "nerve_factorization_controls.csv": generate_nerve,
    "circle_multiplier_cocycle_controls.csv": generate_cocycle,
    "lift_integer_defect_controls.csv": generate_lift,
    "gauge_coboundary_controls.csv": generate_gauge,
    "twisted_convolution_controls.csv": generate_convolution,
    "twisted_involution_controls.csv": generate_involution,
    "completion_gauge_controls.csv": generate_completion,
    "action_period_nonretention_controls.csv": generate_action_period,
    "negative_domain_controls.csv": generate_negative_domain,
    "actual_standard_support_transfer_controls.csv": generate_support_transfer,
    "target_summary.csv": generate_target_summary,
    "completion_corona_controls_v2.csv": generate_v2,
}


def validate_rows(name: str, rows: Sequence[Mapping[str, str]]) -> None:
    schema, expected_rows, columns, expected_negatives = SPECS[name]
    header = HEADERS[name]
    if len(header) != columns or len(rows) != expected_rows:
        raise ValidationError(f"{name}: schema/count drift")
    negatives = 0
    ids = set()
    for row in rows:
        if list(row) != header or len(row) != columns:
            raise ValidationError(f"{name}: header/order drift")
        if row["schema_version"] != schema or row["status"] != "PASS":
            raise ValidationError(f"{name}: schema/status failure")
        if row["row_id"] in ids:
            raise ValidationError(f"{name}: duplicate row id")
        ids.add(row["row_id"])
        if "tolerance" in row and row["tolerance"] != "0":
            raise ValidationError(f"{name}: nonzero tolerance")
        if row.get("case_kind") == "NEGATIVE":
            negatives += 1
            if not row.get("negative_reason"):
                raise ValidationError(f"{name}: negative without reason")
        elif row.get("negative_reason"):
            raise ValidationError(f"{name}: nonnegative with reason")
        for value in row.values():
            if value != value.strip() or "\r" in value or "\n" in value:
                raise ValidationError(f"{name}: noncanonical field")
    if negatives != expected_negatives:
        raise ValidationError(f"{name}: expected {expected_negatives} negatives, got {negatives}")


def csv_bytes(name: str, rows: Sequence[Mapping[str, str]]) -> bytes:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=HEADERS[name], delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL, doublequote=True, escapechar=None, lineterminator="\n", extrasaction="raise")
    writer.writeheader()
    writer.writerows(rows)
    text = output.getvalue()
    if "\r" in text or not text.endswith("\n"):
        raise ValidationError(f"{name}: serialization drift")
    return text.encode("utf-8")


def build_csv_payloads() -> Tuple[Dict[str, bytes], Dict[str, List[Dict[str, str]]]]:
    payloads: Dict[str, bytes] = {}
    rowsets: Dict[str, List[Dict[str, str]]] = {}
    discovered_methods: int | None = None
    for name in ARTIFACT_ORDER:
        if name == "completion_corona_controls_v2.csv":
            discovered_methods = discover_unittest_method_count()
            rows = generate_v2(rowsets,discovered_methods)
        else:
            rows = GENERATORS[name]()
        validate_rows(name, rows)
        if name == "twisted_convolution_controls.csv":
            validate_convolution_independence(rows)
        elif name == "twisted_involution_controls.csv":
            validate_involution_independence(rows)
        elif name == "completion_gauge_controls.csv":
            validate_completion_independence(rows)
        elif name == "actual_standard_support_transfer_controls.csv":
            validate_support_transfer_rows(rows)
        if name == "completion_corona_controls_v2.csv":
            assert discovered_methods is not None
            validate_v2_families(rows,rowsets,discovered_methods)
        rowsets[name] = rows
        payloads[name] = csv_bytes(name, rows)
    if sum(len(rowsets[n]) for n in ARTIFACT_ORDER) != 2665:
        raise ValidationError("aggregate row count drift")
    if sum(SPECS[n][3] for n in ARTIFACT_ORDER) != 67:
        raise ValidationError("aggregate negative count drift")
    return payloads, rowsets


def verify_authorities() -> None:
    if len(BINDINGS) != 24 or set(BASE_BINDINGS) & set(V2_BINDINGS):
        raise ValidationError("binding union is not the frozen disjoint 24-path set")
    for path, expected in sorted(BINDINGS.items()):
        resolved = resolve_binding(path)
        if not resolved.is_file() or sha256_file(resolved) != expected:
            raise ValidationError(f"authority binding mismatch: {path}")
    design = PAPER_DIR / DESIGN_HEAD["path"]
    if not design.is_file() or sha256_file(design) != DESIGN_HEAD["sha256"]:
        raise ValidationError("v2 design-head mismatch")


def implementation_records() -> List[Dict[str, object]]:
    records = []
    for path in sorted(IMPLEMENTATION_PATHS):
        resolved = PAPER_DIR / path
        if not resolved.is_file() or resolved.is_symlink():
            raise ValidationError(f"missing or nonregular implementation path: {path}")
        data = resolved.read_bytes()
        records.append({"path": path, "bytes": len(data), "sha256": sha256_bytes(data)})
    return records


def build_manifest(csv_payloads: Mapping[str, bytes]) -> bytes:
    if list(csv_payloads) != list(ARTIFACT_ORDER):
        raise ValidationError("manifest input artifact order drift")
    metrics: Dict[str,Tuple[int,int,int]] = {}
    for name in ARTIFACT_ORDER:
        try:
            parsed = list(csv.reader(io.StringIO(csv_payloads[name].decode("utf-8"),newline="")))
        except (KeyError,UnicodeDecodeError,csv.Error) as exc:
            raise ValidationError(f"manifest cannot parse emitted artifact: {name}") from exc
        if not parsed or parsed[0] != HEADERS[name]:
            raise ValidationError(f"manifest emitted header drift: {name}")
        body = parsed[1:]
        kind_index = HEADERS[name].index("case_kind") if "case_kind" in HEADERS[name] else -1
        negatives = sum(row[kind_index]=="NEGATIVE" for row in body) if kind_index >= 0 else 0
        metrics[name]=(len(body),len(parsed[0]),negatives)
        if metrics[name] != (SPECS[name][1],SPECS[name][2],SPECS[name][3]):
            raise ValidationError(f"manifest emitted metrics drift: {name}")
    discovered_methods = discover_unittest_method_count()
    v1_rows = sum(metrics[name][0] for name in ARTIFACT_ORDER[:11])
    v1_negatives = sum(metrics[name][2] for name in ARTIFACT_ORDER[:11])
    v2_rows,v2_columns,v2_negatives = metrics[ARTIFACT_ORDER[11]]
    total_rows = sum(item[0] for item in metrics.values())
    total_negatives = sum(item[2] for item in metrics.values())
    artifacts = []
    for name in ARTIFACT_ORDER:
        schema = SPECS[name][0]
        rows,columns,negatives = metrics[name]
        data = csv_payloads[name]
        artifacts.append({"path": f"results/{name}", "schema": schema, "columns": columns, "rows": rows, "negative_rows": negatives, "bytes": len(data), "sha256": sha256_bytes(data)})
    manifest = {
        "schema_version": MANIFEST_SCHEMA,
        "package_id": PACKAGE_ID,
        "design_head": dict(DESIGN_HEAD),
        "bindings": [{"path": path, "sha256": digest} for path,digest in sorted(BINDINGS.items())],
        "proof_binding": {"concurrent_phase3_proof_hash_included": False, "policy": "POST_PROOF_AUDIT_BINDS_SEPARATELY"},
        "implementation": implementation_records(),
        "artifacts": artifacts,
        "legacy_v1": {"csv_bodies_byte_identical": True, "csv_count": len(ARTIFACT_ORDER[:11]), "body_rows": v1_rows, "negative_rows": v1_negatives, "target_summary_role": "V1_SNAPSHOT_ONLY"},
        "aggregates": {
            "design_schema_v1": SCHEMA_V1,
            "design_schema_v2": SCHEMA_V2,
            "manifest_schema": MANIFEST_SCHEMA,
            "header_widths": [metrics[name][1] for name in ARTIFACT_ORDER],
            "csv_artifacts": len(ARTIFACT_ORDER),
            "generated_artifacts_including_manifest": len(ARTIFACT_ORDER)+1,
            "manifest_binding_paths": 24,
            "v1_csv_body_rows_byte_identical": v1_rows,
            "v2_new_csv_body_rows": v2_rows,
            "csv_body_rows": total_rows,
            "v1_explicit_negative_rows": v1_negatives,
            "v2_new_explicit_negative_rows": v2_negatives,
            "explicit_negative_rows": total_negatives,
            "expected_negatives_detected": total_negatives,
            "negative_failures": 0,
            "unittest_methods": discovered_methods,
            "unittest_failures": 0,
            "unittest_errors": 0,
            "fresh_generations": 2,
            "byte_identical_copies": 3,
            "tolerance_policy": "EXACT_ZERO",
        },
        "reproduction": {"deterministic": True, "random_used": False, "network_used": False, "fresh_generations": 2, "byte_identical_copies": 3},
        "status": "PASS",
    }
    encoded = (json.dumps(manifest, ensure_ascii=False, sort_keys=True, indent=2) + "\n").encode("utf-8")
    return encoded


def validate_manifest_candidate(candidate: Mapping[str,object], expected: Mapping[str,object]) -> None:
    failure = manifest_firewall_failure(candidate)
    if failure:
        raise ValidationError(f"MANIFEST_{failure}")
    if list(candidate) != list(expected):
        raise ValidationError("MANIFEST_INVENTORY")
    if candidate.get("schema_version") != MANIFEST_SCHEMA or candidate.get("package_id") != PACKAGE_ID:
        raise ValidationError("MANIFEST_SCHEMA")
    if candidate.get("design_head") != expected.get("design_head"):
        raise ValidationError("MANIFEST_DESIGN_HEAD")
    if candidate.get("bindings") != expected.get("bindings"):
        raise ValidationError("MANIFEST_BINDING_EDGE")
    actual_impl, expected_impl = candidate.get("implementation"),expected.get("implementation")
    if not isinstance(actual_impl,list) or not isinstance(expected_impl,list) or len(actual_impl)!=len(expected_impl):
        raise ValidationError("MANIFEST_IMPLEMENTATION_INVENTORY")
    for actual,wanted in zip(actual_impl,expected_impl):
        if actual != wanted:
            raise ValidationError("MANIFEST_IMPLEMENTATION_EDGE")
    actual_artifacts,expected_artifacts = candidate.get("artifacts"),expected.get("artifacts")
    if not isinstance(actual_artifacts,list) or not isinstance(expected_artifacts,list) or len(actual_artifacts)!=len(expected_artifacts):
        raise ValidationError("MANIFEST_ARTIFACT_INVENTORY")
    for actual,wanted in zip(actual_artifacts,expected_artifacts):
        if actual != wanted:
            raise ValidationError("MANIFEST_ARTIFACT_EDGE")
    if candidate != expected:
        raise ValidationError("MANIFEST_CONTENT")


def strict_json_object(pairs: Sequence[Tuple[str,object]]) -> Dict[str,object]:
    result: Dict[str,object] = {}
    for key,value in pairs:
        if key in result:
            raise ValidationError(f"MANIFEST_DUPLICATE_KEY:{key}")
        result[key]=value
    return result


ROW_PREFIXES = {
    "nerve_factorization_controls.csv":"NF","circle_multiplier_cocycle_controls.csv":"CM","lift_integer_defect_controls.csv":"LI",
    "gauge_coboundary_controls.csv":"GC","twisted_convolution_controls.csv":"TC","twisted_involution_controls.csv":"TI",
    "completion_gauge_controls.csv":"CG","action_period_nonretention_controls.csv":"AP","negative_domain_controls.csv":"ND",
    "actual_standard_support_transfer_controls.csv":"ST","target_summary.csv":"TS","completion_corona_controls_v2.csv":"V2",
}


def read_and_validate_csv(path: Path,name: str) -> List[Dict[str,str]]:
    try:
        raw = path.read_bytes()
        text = raw.decode("utf-8")
    except (OSError,UnicodeDecodeError) as exc:
        raise ValidationError(f"CSV_CONTENT:{name}") from exc
    if raw.startswith(b"\xef\xbb\xbf") or "\r" in text or not text.endswith("\n"):
        raise ValidationError(f"CSV_SERIALIZATION:{name}")
    try:
        parsed = list(csv.reader(io.StringIO(text,newline=""),delimiter=",",quotechar='"',doublequote=True,escapechar=None))
    except csv.Error as exc:
        raise ValidationError(f"CSV_CONTENT:{name}") from exc
    if not parsed or parsed[0] != HEADERS[name]:
        raise ValidationError(f"CSV_HEADER:{name}")
    body = parsed[1:]
    if len(body) != SPECS[name][1]:
        raise ValidationError(f"CSV_ROW_COUNT:{name}")
    if any(len(values)!=len(HEADERS[name]) for values in body):
        raise ValidationError(f"CSV_COLUMNS:{name}")
    rows = [dict(zip(HEADERS[name],values)) for values in body]
    prefix = ROW_PREFIXES[name]
    if [row["row_id"] for row in rows] != [f"{prefix}-{i:04d}" for i in range(1,len(rows)+1)]:
        raise ValidationError(f"CSV_ROW_ORDER:{name}")
    return rows


def validate_negative_domain_rows(rows: Sequence[Mapping[str,str]]) -> None:
    if len(rows)!=20:
        raise ValidationError("ND_ROW_COUNT")
    for index,row in enumerate(rows,1):
        try:
            reason,lock,detector = derive_v1_negative(row.get("fixture", ""))
        except ValidationError as exc:
            raise ValidationError(f"ND_FIXTURE:{index}") from exc
        if row.get("negative_reason") != reason:
            raise ValidationError(f"ND_REASON:{index}")
        if row.get("violated_lock") != lock:
            raise ValidationError(f"ND_LOCK:{index}")
        if detector != row.get("expected_detector"):
            raise ValidationError(f"ND_EXPECTED_DETECTOR:{index}")
        if detector != row.get("observed_detector"):
            raise ValidationError(f"ND_OBSERVED_DETECTOR:{index}")
        if row["status"] != "PASS":
            raise ValidationError(f"ND_STATUS:{index}")


def validate_package_semantics(output_dir: Path,expected: Mapping[str,bytes]) -> None:
    rowsets: Dict[str,List[Dict[str,str]]] = {}
    for name in ARTIFACT_ORDER:
        rowsets[name] = read_and_validate_csv(output_dir/name,name)
    for name in ARTIFACT_ORDER[:11]:
        if name == "twisted_convolution_controls.csv":
            validate_convolution_independence(rowsets[name])
        elif name == "twisted_involution_controls.csv":
            validate_involution_independence(rowsets[name])
        elif name == "completion_gauge_controls.csv":
            validate_completion_independence(rowsets[name])
        elif name == "negative_domain_controls.csv":
            validate_negative_domain_rows(rowsets[name])
        elif name == "actual_standard_support_transfer_controls.csv":
            validate_support_transfer_rows(rowsets[name])
        validate_rows(name,rowsets[name])
    discovered = discover_unittest_method_count()
    validate_v2_families(rowsets["completion_corona_controls_v2.csv"],rowsets,discovered)
    validate_rows("completion_corona_controls_v2.csv",rowsets["completion_corona_controls_v2.csv"])
    try:
        candidate_manifest = json.loads(
            (output_dir/"manifest.json").read_text(encoding="utf-8"),
            object_pairs_hook=strict_json_object,
        )
        expected_manifest = json.loads(
            expected["manifest.json"].decode("utf-8"),
            object_pairs_hook=strict_json_object,
        )
    except (OSError,UnicodeDecodeError,json.JSONDecodeError) as exc:
        raise ValidationError("MANIFEST_CONTENT") from exc
    validate_manifest_candidate(candidate_manifest,expected_manifest)


def expected_package() -> Dict[str, bytes]:
    verify_authorities()
    csv_payloads, _ = build_csv_payloads()
    package = dict(csv_payloads)
    package["manifest.json"] = build_manifest(csv_payloads)
    return package


def prohibited_cache_entries(roots: Iterable[Path]) -> List[str]:
    bad = []
    for root in roots:
        if not root.exists():
            continue
        for path in root.rglob("*"):
            if path.name in {"__pycache__", ".pytest_cache", ".mypy_cache"} or path.suffix in {".pyc", ".pyo"}:
                bad.append(str(path))
    return sorted(bad)


def assert_no_cache(*roots: Path) -> None:
    bad = prohibited_cache_entries(roots)
    if bad:
        raise ValidationError("prohibited cache/residue: " + ", ".join(bad))


def verify_source_inventory() -> None:
    expected = {
        PAPER_DIR / "code": {"README.md", "generate_controls.py", "test_controls.py"},
        PAPER_DIR / "experiments": {"README.md", "reproduce.sh"},
    }
    for root, names in expected.items():
        if not root.is_dir():
            raise ValidationError(f"missing implementation directory: {root.name}")
        actual = {p.name for p in root.iterdir()}
        if actual != names or any(not p.is_file() or p.is_symlink() for p in root.iterdir()):
            raise ValidationError(f"extra/missing/nonregular implementation path under {root.name}")


def verify_package(output_dir: Path) -> Dict[str, object]:
    if not output_dir.is_dir() or output_dir.is_symlink():
        raise ValidationError("package path is not a regular directory")
    verify_source_inventory()
    assert_no_cache(PAPER_DIR / "code", PAPER_DIR / "experiments", output_dir)
    controlled = set(ARTIFACT_ORDER) | {"manifest.json"}
    allowed = set(controlled)
    if output_dir.resolve() == RESULTS_DIR.resolve():
        allowed.add("README.md")
    entries = list(output_dir.iterdir())
    actual = {p.name for p in entries}
    missing = allowed - actual
    if missing:
        raise ValidationError(f"PACKAGE_MISSING_ARTIFACT:{sorted(missing)}")
    extras = actual - allowed
    if extras:
        extra_entries = [output_dir/name for name in sorted(extras)]
        if any(path.is_dir() and not path.is_symlink() for path in extra_entries):
            raise ValidationError(f"PACKAGE_EXTRA_DIRECTORY:{sorted(extras)}")
        raise ValidationError(f"PACKAGE_EXTRA_ARTIFACT:{sorted(extras)}")
    if any(not p.is_file() or p.is_symlink() for p in entries):
        raise ValidationError("PACKAGE_NONREGULAR_ARTIFACT")
    expected = expected_package()
    # Parse and evaluate all semantic predicates before exact-byte identity.
    # This ordering makes isolated row mutations report their intended family
    # or detector failure rather than collapsing into a generic hash mismatch.
    validate_package_semantics(output_dir,expected)
    for name, data in expected.items():
        if (output_dir / name).read_bytes() != data:
            raise ValidationError(f"ARTIFACT_BYTE_IDENTITY:{name}")
    return package_receipt(output_dir)


def verification_snapshot(root: Path) -> Dict[str,Tuple[str,int,int,int,str]]:
    """Capture content and metadata without following package symlinks."""
    snapshot: Dict[str,Tuple[str,int,int,int,str]] = {}
    for path in sorted(root.rglob("*"),key=lambda item:item.relative_to(root).as_posix()):
        relative = path.relative_to(root).as_posix()
        info = path.stat(follow_symlinks=False)
        if stat.S_ISREG(info.st_mode):
            kind,digest = "file",sha256_file(path)
        elif stat.S_ISDIR(info.st_mode):
            kind,digest = "directory",""
        elif stat.S_ISLNK(info.st_mode):
            kind,digest = "symlink",os.readlink(path)
        else:
            kind,digest = "other",""
        snapshot[relative] = (
            kind,stat.S_IMODE(info.st_mode),info.st_size,info.st_mtime_ns,digest
        )
    return snapshot


def guarded_verify_package(
    output_dir: Path,
    operation: Callable[[Path],None] | None = None,
) -> Dict[str,object]:
    """Verify while proving that neither bytes nor metadata were written.

    ``operation`` exists solely for isolated mutation tests of the guard.  It
    is executed inside the protected interval, and any verification failure
    is deferred until the before/after write classification has run.
    """
    before = verification_snapshot(output_dir)
    receipt: Dict[str,object] | None = None
    failure: BaseException | None = None
    try:
        if operation is not None:
            operation(output_dir)
        receipt = verify_package(output_dir)
    except BaseException as exc:  # classification must run even on tamper
        failure = exc
    after = verification_snapshot(output_dir)
    if set(before) != set(after):
        raise ValidationError("VERIFY_ONLY_BYTE_WRITE") from failure
    byte_changed = any(
        before[path][0] != after[path][0]
        or before[path][2] != after[path][2]
        or before[path][4] != after[path][4]
        for path in before
    )
    if byte_changed:
        raise ValidationError("VERIFY_ONLY_BYTE_WRITE") from failure
    metadata_changed = any(
        before[path][1] != after[path][1]
        or before[path][3] != after[path][3]
        for path in before
    )
    if metadata_changed:
        raise ValidationError("VERIFY_ONLY_METADATA_WRITE") from failure
    if failure is not None:
        raise failure
    assert receipt is not None
    return receipt


def package_receipt(output_dir: Path) -> Dict[str, object]:
    entries = []
    for path in sorted(output_dir.iterdir(), key=lambda p: p.name):
        info = path.stat(follow_symlinks=False)
        entry: Dict[str, object] = {"path": path.name, "type": "file" if stat.S_ISREG(info.st_mode) else "other", "mode": stat.S_IMODE(info.st_mode), "size": info.st_size, "mtime_ns": info.st_mtime_ns}
        if stat.S_ISREG(info.st_mode):
            entry["sha256"] = sha256_file(path)
        entries.append(entry)
    return {"entries": entries}


def generate_package(output_dir: Path) -> Dict[str, object]:
    if not output_dir.is_dir() or output_dir.is_symlink():
        raise ValidationError("output directory must already exist and be regular")
    if any(output_dir.iterdir()):
        raise ValidationError("generator output directory must be empty")
    verify_source_inventory()
    assert_no_cache(PAPER_DIR / "code", PAPER_DIR / "experiments", RESULTS_DIR, output_dir)
    package = expected_package()
    for name, data in package.items():
        with (output_dir / name).open("xb") as handle:
            handle.write(data)
    return verify_package(output_dir)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--output-dir", type=Path)
    mode.add_argument("--verify-only", type=Path)
    mode.add_argument("--receipt", type=Path)
    args = parser.parse_args(argv)
    try:
        if args.output_dir is not None:
            receipt = generate_package(args.output_dir)
            action = "GENERATE"
        elif args.verify_only is not None:
            receipt = guarded_verify_package(args.verify_only)
            action = "VERIFY_ONLY"
        else:
            receipt = package_receipt(args.receipt)
            action = "RECEIPT"
        print(json.dumps({"action": action, "status": "PASS", **receipt}, ensure_ascii=False, sort_keys=True))
        return 0
    except (OSError, ValueError, ValidationError, csv.Error, json.JSONDecodeError) as exc:
        print(f"P13_CONTROLS_FAIL: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
