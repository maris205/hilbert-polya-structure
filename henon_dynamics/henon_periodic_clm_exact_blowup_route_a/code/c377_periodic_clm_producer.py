#!/usr/bin/env python3
"""Canonical exact evidence producer for HCS-C377."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("c377 producer refuses optimized Python")

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results/c377_periodic_clm_evidence.json"
EVAL = ROOT / "evaluations/route_a/HCS-C377/2026-09-04.yaml"
SOURCE = "f58422d8f03235329863f946654981ecb5d4dc97"
AUTHORITY_SHA = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
YAML_RAW_SHA = "f7a15957460d7ebdf3b18c51044e31899d66fb4d4fba3a7f280c50e2355e8920"
YAML_SEMANTIC_SHA = "9645872c74a85036a2aa42bb9221ab20a7295731034dcd624f8599150424e2d8"


def canonical(value) -> bytes:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def digest(value) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def frac(value: Fraction):
    return {"numerator": value.numerator, "denominator": value.denominator}


ZERO = (Fraction(0), Fraction(0))
ONE = (Fraction(1), Fraction(0))
I = (Fraction(0), Fraction(1))


def gadd(a, b):
    return (a[0] + b[0], a[1] + b[1])


def gsub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def gmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def gscale(value, scale):
    return (value[0] * scale, value[1] * scale)


def gabs2(value):
    return value[0] * value[0] + value[1] * value[1]


def gdiv(a, b):
    norm = gabs2(b)
    if norm == 0:
        raise ZeroDivisionError
    return ((a[0] * b[0] + a[1] * b[1]) / norm, (a[1] * b[0] - a[0] * b[1]) / norm)


def gencode(value):
    return {"re": frac(value[0]), "im": frac(value[1])}


def clean(poly):
    return {k: v for k, v in poly.items() if v != ZERO}


def padd(a, b, scale=Fraction(1)):
    keys = set(a) | set(b)
    return clean({k: gadd(a.get(k, ZERO), gscale(b.get(k, ZERO), scale)) for k in keys})


def pconv(a, b):
    out = {}
    for ka, va in a.items():
        for kb, vb in b.items():
            key = ka + kb
            out[key] = gadd(out.get(key, ZERO), gmul(va, vb))
    return clean(out)


def hilbert(poly):
    out = {}
    for k, value in poly.items():
        multiplier = (Fraction(0), Fraction(-1 if k > 0 else 1 if k < 0 else 0))
        out[k] = gmul(multiplier, value)
    return clean(out)


def encode_poly(poly):
    return [[k, gencode(poly[k])] for k in sorted(poly)]


def multiplier_rows():
    return [
        {"k": k, "multiplier": gencode((Fraction(0), Fraction(-1 if k > 0 else 1))), "square_on_nonzero_mode": -1}
        for k in tuple(range(-128, 0)) + tuple(range(1, 129))
    ]


def tricomi_rows():
    rows = []
    for k in range(1, 33):
        for ell in range(1, 33):
            a = Fraction(k % 5 + 1, ell % 7 + 2)
            b = Fraction(ell % 3 + 1, k % 6 + 2)
            f = {}
            f[k] = gadd(f.get(k, ZERO), (Fraction(0), -a / 2))
            f[-k] = gadd(f.get(-k, ZERO), (Fraction(0), a / 2))
            f[ell] = gadd(f.get(ell, ZERO), (b / 2, Fraction(0)))
            f[-ell] = gadd(f.get(-ell, ZERO), (b / 2, Fraction(0)))
            f = clean(f)
            h = hilbert(f)
            lhs = hilbert(pconv(f, h))
            rhs = padd(pconv(h, h), pconv(f, f), Fraction(-1))
            rhs = {mode: gscale(value, Fraction(1, 2)) for mode, value in rhs.items()}
            rhs = clean(rhs)
            assert lhs == rhs
            rows.append({
                "k": k, "ell": ell, "sin_coefficient": frac(a), "cos_coefficient": frac(b),
                "mode_count_f": len(f), "mode_count_identity": len(lhs),
                "identity_coefficient_sha256": digest(encode_poly(lhs)), "residual_nonzero_count": 0,
            })
    assert len(rows) == 1024
    return rows


def zero_mean_rows():
    values = [Fraction(-2), Fraction(-3, 2), Fraction(-1), Fraction(-1, 2), Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(2)]
    times = [Fraction(1, 4), Fraction(1, 3), Fraction(1, 2), Fraction(2, 3), Fraction(3, 4), Fraction(1), Fraction(4, 3), Fraction(3, 2)]
    rows = []
    for h in values:
        for w in values:
            for t in times:
                z0 = (h, w)
                denominator = gsub((Fraction(2), Fraction(0)), gscale(z0, t))
                z = gdiv(gscale(z0, 2), denominator)
                scalar_denominator = (2 - t * h) ** 2 + (t * w) ** 2
                omega_formula = 4 * w / scalar_denominator
                assert z[1] == omega_formula
                rows.append({
                    "h0": frac(h), "omega0": frac(w), "t": frac(t),
                    "denominator_abs_squared": frac(scalar_denominator),
                    "z": gencode(z), "omega_formula": frac(omega_formula),
                })
    assert len(rows) == 512
    return rows


def nonzero_mean_rows():
    values = [Fraction(-2), Fraction(-3, 2), Fraction(-1), Fraction(-1, 2), Fraction(1, 2), Fraction(1), Fraction(3, 2), Fraction(2)]
    r_values = [Fraction(1, 4), Fraction(1, 2), Fraction(1), Fraction(2)]
    rows = []
    for mu in values:
        for h in values:
            for f in values:
                z0 = (h, f)
                for r in r_values:
                    eitheta = (Fraction(1) - r * r, 2 * r)
                    eitheta = gscale(eitheta, Fraction(1, 1) / (1 + r * r))
                    delta = gsub(gscale(I, 2 * mu), gmul(gsub(eitheta, ONE), z0))
                    norm = gabs2(delta)
                    singular = norm == 0
                    if singular:
                        z = None
                        omega = None
                    else:
                        z = gdiv(gmul(gscale(I, 2 * mu), gmul(eitheta, z0)), delta)
                        omega = mu + z[1]
                        assert omega == 4 * mu * mu * (mu + f) / norm
                    rows.append({
                        "mu": frac(mu), "h0": frac(h), "f0": frac(f), "tan_half_angle": frac(r),
                        "e_i_mu_t": gencode(eitheta), "delta": gencode(delta),
                        "delta_abs_squared": frac(norm), "singular": singular,
                        "z": None if z is None else gencode(z),
                        "omega": None if omega is None else frac(omega),
                    })
    assert len(rows) == 2048
    return rows


def one_mode_rows():
    rows = []
    amplitudes = [Fraction(j, 2) for j in tuple(range(-8, 0)) + tuple(range(1, 9))]
    for mu_integer in range(-4, 5):
        mu = Fraction(mu_integer)
        for amplitude in amplitudes:
            for mode in range(1, 17):
                if mu == 0:
                    regime = "zero_mean_crossing"
                    time = {"kind": "rational", "value": frac(Fraction(2, 1) / abs(amplitude))}
                    hmax_sq = amplitude * amplitude
                elif abs(mu) > abs(amplitude):
                    regime = "zero_free_global_periodic"
                    time = None
                    hmax_sq = None
                else:
                    hmax_sq = amplitude * amplitude - mu * mu
                    regime = "tangent_zero" if hmax_sq == 0 else "simple_crossing_zeros"
                    time = {
                        "kind": "two_over_abs_mu_times_arccot",
                        "arccot_argument_squared": frac(hmax_sq / (mu * mu)),
                        "arccot_branch": "(0,pi)",
                    }
                rows.append({
                    "mu": frac(mu), "amplitude": frac(amplitude), "mode": mode,
                    "regime": regime, "zero_exists": abs(mu) <= abs(amplitude),
                    "maximum_H_on_zero_set_squared": None if hmax_sq is None else frac(hmax_sq),
                    "first_forward_time": time,
                })
    assert len(rows) == 2304
    return rows


def arithmetic_control_rows(one_modes, zero_modes):
    stripped_hashes = {}
    for mode in range(1, 17):
        stripped = [
            {key: value for key, value in row.items() if key != "mode"}
            for row in one_modes if row["mode"] == mode
        ]
        assert len(stripped) == 144
        stripped_hashes[mode] = digest(stripped)
    assert len(set(stripped_hashes.values())) == 1
    permutation = {mode: 1 + ((5 * (mode - 1) + 3) % 16) for mode in range(1, 17)}
    assert sorted(permutation.values()) == list(range(1, 17))
    assert all(stripped_hashes[mode] == stripped_hashes[permutation[mode]] for mode in permutation)
    regime_counts = {}
    for row in one_modes:
        regime_counts[row["regime"]] = regime_counts.get(row["regime"], 0) + 1
        mu = Fraction(row["mu"]["numerator"], row["mu"]["denominator"])
        amplitude = Fraction(row["amplitude"]["numerator"], row["amplitude"]["denominator"])
        assert row["zero_exists"] == (abs(mu) <= abs(amplitude))
    return [
        {
            "control": "composite_vs_prime_fourier_modes", "status": "PASS_EXACT",
            "prime_modes": [2, 3, 5, 7, 11, 13],
            "composite_modes": [4, 6, 8, 9, 10, 12, 14, 15, 16], "unit_mode": 1,
            "common_stripped_clock_sha256": stripped_hashes[1],
        },
        {
            "control": "deterministic_affine_mode_relabeling", "status": "PASS_EXACT",
            "mapping": [[mode, permutation[mode]] for mode in range(1, 17)],
            "all_stripped_clock_hashes_preserved": True,
        },
        {
            "control": "neighboring_mean_amplitude_grid", "status": "PASS_EXACT",
            "cell_count": len(one_modes), "regime_counts": regime_counts,
            "only_threshold": "abs(mu)=abs(amplitude)",
        },
        {
            "control": "simpler_zero_mean_parent", "status": "PASS_EXACT",
            "cell_count": len(zero_modes), "section_sha256": digest(zero_modes),
            "arithmetic_labels_used": False,
        },
    ]


def nonzero_profile_rows():
    rows = []
    values = [Fraction(-2), Fraction(-1), Fraction(1), Fraction(2)]
    for mu in values:
        for cot_half in values:
            eitheta = gdiv((cot_half, Fraction(1)), (cot_half, Fraction(-1)))
            zstar = (mu * cot_half, -mu)
            assert gsub(gscale(I, 2 * mu), gmul(gsub(eitheta, ONE), zstar)) == ZERO
            for hprime in values:
                for wprime in values:
                    zprime = (hprime, wprime)
                    for y in values:
                        leading_denominator = gsub(
                            gmul(gscale(I, mu), gmul(eitheta, zstar)),
                            gscale(gmul(gsub(eitheta, ONE), zprime), y),
                        )
                        norm = gabs2(leading_denominator)
                        assert norm > 0
                        profile = 4 * mu * mu * wprime * y / norm
                        assert profile != 0
                        rows.append({
                            "mu": frac(mu), "cot_half_angle": frac(cot_half),
                            "h_prime": frac(hprime), "omega_prime": frac(wprime), "y": frac(y),
                            "leading_denominator": gencode(leading_denominator),
                            "profile": frac(profile), "transverse": True,
                        })
    assert len(rows) == 1024
    return rows


def zero_profile_rows():
    rows = []
    hstars = [Fraction(1, 2), Fraction(1), Fraction(2), Fraction(3)]
    values = [Fraction(-2), Fraction(-1), Fraction(1), Fraction(2)]
    for hstar in hstars:
        blowup_time = Fraction(2, 1) / hstar
        for hprime in values:
            for wprime in values:
                for y in values:
                    leading_denominator = gsub((hstar, Fraction(0)), gscale((hprime, wprime), blowup_time * y))
                    norm = gabs2(leading_denominator)
                    assert norm > 0
                    profile = 4 * wprime * y / norm
                    assert profile != 0
                    rows.append({
                        "h_star": frac(hstar), "blowup_time": frac(blowup_time),
                        "h_prime": frac(hprime), "omega_prime": frac(wprime), "y": frac(y),
                        "leading_denominator": gencode(leading_denominator),
                        "profile": frac(profile), "transverse": True,
                    })
    assert len(rows) == 256
    return rows


BOUNDARY_ROWS = [
    {"case": "mu_nonzero_zero_free", "status": "global smooth and periodic with period 2*pi/abs(mu)"},
    {"case": "mu_nonzero_simple_zero", "status": "finite first Riccati pole and conditional inverse-time self-similar vorticity profile"},
    {"case": "mu_nonzero_tangent_zero", "status": "finite Riccati breakdown; no simple-pole vorticity profile claimed"},
    {"case": "mu_zero_nontrivial", "status": "first positive pole is minimum of 2/Homega0 over zeros with Homega0 positive, if nonempty"},
    {"case": "mu_zero_identically_zero", "status": "stationary global zero solution"},
    {"case": "one_mode_threshold", "status": "absolute mean equals absolute amplitude, tangent zero, first time pi/abs(mu)"},
    {"case": "after_first_pole", "status": "classical smooth solution not continued through the singular denominator"},
]


FLAGS = {
    key: False
    for key in (
        "claims_target_arithmetic_local_data", "claims_target_euler_factors", "claims_root_number",
        "claims_automorphy", "claims_target_divisor_or_counting_law",
        "claims_target_functional_equation", "claims_target_zero_match",
        "claims_hilbert_polya_operator", "invokes_route_b",
    )
}


def build():
    raw = EVAL.read_bytes()
    evaluation = yaml.safe_load(raw)
    assert hashlib.sha256(raw).hexdigest() == YAML_RAW_SHA
    assert digest(evaluation) == YAML_SEMANTIC_SHA
    zero_modes = zero_mean_rows()
    one_modes = one_mode_rows()
    controls = arithmetic_control_rows(one_modes, zero_modes)
    sections = {
        "multiplier_rows": multiplier_rows(),
        "tricomi_rows": tricomi_rows(),
        "zero_mean_rows": zero_modes,
        "nonzero_mean_rows": nonzero_mean_rows(),
        "one_mode_rows": one_modes,
        "arithmetic_control_rows": controls,
        "nonzero_profile_rows": nonzero_profile_rows(),
        "zero_profile_rows": zero_profile_rows(),
        "boundary_rows": BOUNDARY_ROWS,
    }
    value = {
        "schema": "hcs-c377-evidence-v1", "candidate_id": "HCS-C377", "obstruction_id": "HEN-O361",
        "evaluation_date": "2026-09-04", "source_commit": SOURCE, "fixed_epoch": 1788480000,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "evaluator": {"authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": AUTHORITY_SHA},
        "route_a_yaml": {"relative_path": "evaluations/route_a/HCS-C377/2026-09-04.yaml", "raw_sha256": YAML_RAW_SHA, "semantic_sha256": YAML_SEMANTIC_SHA},
        "conventions": {
            "equation": "omega_t=omega*H(omega) on R/(2*pi*Z)",
            "hilbert": "H(e^(i*k*x))=-i*sign(k)*e^(i*k*x), H(1)=0",
            "decomposition": "mu=mean(omega0), f=omega-mu, h=Hf, z=h+i*f",
            "tricomi": "H(f*Hf)=((Hf)^2-f^2)/2 for real mean-zero f",
            "riccati": "z_t=i*mu*z+z^2/2",
            "arccot_branch": "arccot:R->(0,pi), strictly decreasing",
        },
        "theorem_contract": {
            "mean": "mu is conserved",
            "zero_mean": "z=2*z0/(2-t*z0) and omega=4*omega0/((2-t*h0)^2+t^2*omega0^2)",
            "nonzero_mean": "z=e^(i*mu*t)*z0/(1-(e^(i*mu*t)-1)*z0/(2*i*mu))",
            "nonzero_omega": "omega=4*mu^2*omega0/abs(2*i*mu-(e^(i*mu*t)-1)*z0)^2",
            "nonzero_criterion": "forward breakdown iff omega0 has a zero; first time is min 2/abs(mu)*arccot(Homega0/abs(mu)) on that zero set",
            "zero_criterion": "first positive time is min 2/Homega0 on zeros with Homega0 positive; empty set means forward global",
            "one_mode": "omega0=mu+A*sin(k*x) has the exact zero-free, tangent, crossing, and zero-mean clock regimes",
            "profile": "at every simple first pole, (T-t)*omega(xstar+(T-t)*y,t) converges to the displayed rational profile locally; a global Theta rate needs all first poles simple",
            "boundaries": "tangent and higher-order zeros are excluded from the simple-pole rate, but not from the Riccati breakdown criterion",
        },
        "finite_grid": {
            "hilbert_multiplier_count": 256, "tricomi_polynomial_count": 1024,
            "zero_mean_mobius_count": 512, "nonzero_mean_mobius_count": 2048,
            "one_mode_regime_count": 2304, "nonzero_mean_profile_count": 1024,
            "zero_mean_profile_count": 256, "arithmetic_control_count": 4, "boundary_case_count": 7,
        },
        "collision_boundary": {
            "C309": "finite matrix Riccati and Mobius dynamics, not periodic Hilbert closure",
            "C324": "Hunter-Saxton geometric blow-up, not CLM pointwise Riccati dynamics",
            "C278": "Camassa-Holm peakons, not periodic Hilbert-transform stretching",
            "C363": "Keller-Segel mass concentration, not CLM zero-set clocks",
        },
        "nonclaims": [
            "no unconditional self-similar rate at tangent or higher-order zeros",
            "no continuation of a classical smooth solution through the first denominator pole",
            "no implication for singularity formation in three-dimensional Euler",
            "no global literature novelty claim beyond this package ownership boundary",
            "no target arithmetic data, Euler product, root number, target zeros, Hilbert-Polya operator, or Route B",
        ],
        "references": [
            {"authors": "P. Constantin, P. D. Lax, and A. Majda", "title": "A simple one-dimensional model for the three-dimensional vorticity equation", "doi": "10.1002/cpa.3160380605"},
            {"authors": "P. M. Lushnikov, D. A. Silantyev, and M. Siegel", "title": "Collapse vs. blow up and global existence in the generalized Constantin-Lax-Majda equation", "doi": "10.1007/s00332-021-09737-x", "arxiv": "2010.01201"},
        ],
        "scope_flags": FLAGS,
        "route_a": {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False, "theorem_status": "PROVABLE_AS_STATED_WITH_SIMPLE_POLE_CONDITION_FOR_PROFILE"},
        "finite_evidence_role": "exact algebraic regression only; the periodic Hilbert and Riccati proofs establish the infinite theorem",
        **sections,
        "section_sha256": {name: digest(section) for name, section in sections.items()},
    }
    value["payload_sha256"] = digest(value)
    return value


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUT)
    args = parser.parse_args()
    value = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_bytes(json.dumps(value, sort_keys=True, indent=2, ensure_ascii=False).encode() + b"\n")
    print(
        "C377 producer PASS: multipliers=256 tricomi=1024 zero_mean=512 nonzero_mean=2048 "
        "one_mode=2304 controls=4 profiles=1280 payload=" + value["payload_sha256"]
    )


if __name__ == "__main__":
    main()
