#!/usr/bin/env python3
"""Deterministic exact/algebraic evidence producer for HCS-C295."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from fractions import Fraction
from pathlib import Path

import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c295_isochrone_evidence.json"
SOURCE = "f8d3ad9a8940b54e82854b2924be353575ed8fcb"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788307200
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"

MODEL = {
    "hamiltonian": "H=p_r^2/2+L^2/(2r^2)-mu/(b+sqrt(b^2+r^2))",
    "parameters": "mu>0, b>0, signed angular momentum L; ell=abs(L)",
    "phase_space": "planar central motion; polar chart for ell>0 and Cartesian continuation for ell=0",
    "clock": "physical Hamiltonian time",
    "radial_action_convention": "J_r=(1/pi) integral from periapsis to apoapsis; at ell=0 use the continuous half-line limit",
}
THEOREM = {
    "energy_domain": "bound motion exists exactly for E_c(ell)<=E<0, where E_c=-2 mu^2/(ell+sqrt(ell^2+4 mu b))^2",
    "action": "J_r=mu/sqrt(-2E)-(ell+sqrt(ell^2+4 mu b))/2",
    "period": "T_r=2 pi mu/(-2E)^(3/2), independent of ell",
    "frequency_ratio": "for ell>0, Omega_phi/Omega_r=(1+ell/sqrt(ell^2+4 mu b))/2; this is the L>=0 convention",
    "closure": "a noncircular bound orbit with ell>0 is phase-space periodic iff the frequency ratio is rational",
    "degenerate_boundaries": "circular orbits are closed independently of the ratio; ell=0 noncentral bound motions cross the smooth center and return after 2 T_r",
    "escape": "E=0 is the marginal escape threshold and E>0 is unbound; J_r and T_r diverge as E increases to zero",
    "kepler_limit": "for fixed ell>0, b decreases to zero gives J_r=mu/sqrt(-2E)-ell and frequency ratio one",
}
PROOF = {
    "substitution": "x=b+sqrt(b^2+r^2), so r^2=x(x-2b) and dt=(x-b) dx/sqrt(Q(x))",
    "quadratic": "Q(x)=2E x^2+(2mu-4bE)x-(4mu b+ell^2)",
    "period_integral": "the root sum and the arcsine integral give the exact angular-momentum-independent radial period",
    "action_integration": "partial_E J_r=T_r/(2pi), with J_r=0 at the unique circular energy",
    "apsidal_integral": "partial fractions of (x-b)/(x(x-2b)) and both root products give Delta_phi=pi(1+ell/sqrt(ell^2+4mu b))",
    "closure_logic": "return of the nonconstant radial phase forces an integer number of radial cycles; angular return is then equivalent to rational frequency ratio",
    "finite_role": "finite algebraic cells and quadrature controls are regression evidence only, not the all-parameter proof",
}
ROUTE = {
    "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
    "overall": "ROUTE_A_REJECTED",
    "route_b_invocation_allowed": False,
}
FLAGS = {
    "arithmetic_local_data": False,
    "euler_factors": False,
    "root_numbers": False,
    "automorphy": False,
    "target_divisor_or_counting_law": False,
    "target_functional_equation": False,
    "target_zero_match": False,
    "hilbert_polya_operator": False,
    "route_b_input": False,
}
REFERENCES = [
    {
        "id": "Henon1959I",
        "authors": "Michel Henon",
        "title": "L'amas isochrone I",
        "venue": "Annales d'Astrophysique 22 (1959), 126-139",
        "identifier": "1959AnAp...22..126H",
        "url": "https://ui.adsabs.harvard.edu/abs/1959AnAp...22..126H/abstract",
        "ownership": "original isochrone-cluster construction",
    },
    {
        "id": "Henon1959II",
        "authors": "Michel Henon",
        "title": "L'amas isochrone II: Le calcul des orbites",
        "venue": "Annales d'Astrophysique 22 (1959), 491-498",
        "identifier": "1959AnAp...22..491H",
        "url": "https://ui.adsabs.harvard.edu/abs/1959AnAp...22..491H/abstract",
        "ownership": "original orbit calculation",
    },
    {
        "id": "RamondPerez2021",
        "authors": "Paul Ramond and Jerome Perez",
        "title": "New Methods of Isochrone Mechanics",
        "venue": "Journal of Mathematical Physics 62 (2021), 112704",
        "identifier": "10.1063/5.0056957",
        "url": "https://arxiv.org/abs/2104.05643",
        "ownership": "modern action-angle and Hamiltonian treatment",
    },
    {
        "id": "FouvryPrunet2022",
        "authors": "Jean-Baptiste Fouvry and Simon Prunet",
        "title": "Linear response theory and damped modes of stellar clusters",
        "venue": "Monthly Notices of the Royal Astronomical Society 509 (2022), 2443-2456",
        "identifier": "10.1093/mnras/stab3020",
        "url": "https://academic.oup.com/mnras/article/509/2/2443/6407532",
        "ownership": "official appendix recording the isochrone frequency map",
    },
]
NONCLAIMS = [
    "the isochrone potential, its action formula, and its frequency map are classical and are not claimed as literature originality",
    "finite algebraic cells and numerical quadratures do not prove the all-parameter theorem",
    "closed resonant tori are continuous families rather than isolated arithmetic primitive owners",
    "the natural Schroedinger quantization is not identified with a target Hilbert-Polya operator",
]


def fs(value: Fraction) -> str:
    return str(value)


def quad(a: Fraction, c: Fraction, d: int) -> dict[str, object]:
    """Represent a+c*sqrt(d) without silently reducing square radicands."""
    return {"a": fs(a), "c": fs(c), "d": d}


def qadd(x: tuple[Fraction, Fraction], y: tuple[Fraction, Fraction]) -> tuple[Fraction, Fraction]:
    return x[0] + y[0], x[1] + y[1]


def qmul(x: tuple[Fraction, Fraction], y: tuple[Fraction, Fraction], d: int) -> tuple[Fraction, Fraction]:
    return x[0] * y[0] + x[1] * y[1] * d, x[0] * y[1] + x[1] * y[0]


def qscale(x: tuple[Fraction, Fraction], scale: Fraction) -> tuple[Fraction, Fraction]:
    return scale * x[0], scale * x[1]


def qvalue(x: tuple[Fraction, Fraction], d: int) -> mp.mpf:
    return mp.mpf(x[0].numerator) / x[0].denominator + mp.mpf(x[1].numerator) / x[1].denominator * mp.sqrt(d)


def dec(value: mp.mpf) -> str:
    return mp.nstr(value, 60)


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def orbit_row(mu_i: int, b_i: int, ell_i: int, multiplier: int) -> dict:
    mu = Fraction(mu_i)
    scale_b = Fraction(b_i)
    ell = Fraction(ell_i)
    d = ell_i * ell_i + 4 * mu_i * b_i
    root = int(math.isqrt(d))
    square = root * root == d

    big_b = (ell, Fraction(1))
    invariant = qscale(big_b, Fraction(multiplier, 2))
    radial_action = qscale(big_b, Fraction(multiplier - 1, 2))
    circular_energy = (
        -Fraction(ell_i * ell_i + 2 * mu_i * b_i, 4 * b_i * b_i),
        Fraction(ell_i, 4 * b_i * b_i),
    )
    energy = qscale(circular_energy, Fraction(1, multiplier * multiplier))
    circular_s = (
        Fraction(b_i) + Fraction(ell_i * ell_i, 2 * mu_i),
        Fraction(ell_i, 2 * mu_i),
    )
    circular_r2 = qadd(qmul(circular_s, circular_s, d), (-scale_b * scale_b, Fraction(0)))
    omega_r = (
        -Fraction(ell_i * (ell_i * ell_i + 3 * mu_i * b_i), 2 * multiplier**3 * mu_i * b_i**3),
        Fraction(ell_i * ell_i + mu_i * b_i, 2 * multiplier**3 * mu_i * b_i**3),
    )
    beta = (Fraction(1, 2), Fraction(ell_i, 2 * d))
    tr_over_2pi = (
        Fraction(multiplier**3 * ell_i * (ell_i * ell_i + 3 * mu_i * b_i), 2 * mu_i * mu_i),
        Fraction(multiplier**3 * (ell_i * ell_i + mu_i * b_i), 2 * mu_i * mu_i),
    )

    e_num = qvalue(energy, d)
    q_num = -2 * e_num
    root_sum = 2 * b_i + 2 * mu_i / q_num
    root_product = d / q_num
    discriminant = max(mp.mpf("0"), root_sum * root_sum - 4 * root_product)
    x_peri = (root_sum - mp.sqrt(discriminant)) / 2
    x_apo = (root_sum + mp.sqrt(discriminant)) / 2

    if multiplier == 1:
        orbit_class = "center_equilibrium" if ell_i == 0 else "circular"
        closure_class = "closed_degenerate"
        primitive_cycles = None
    elif ell_i == 0:
        orbit_class = "radial_through_center"
        closure_class = "closed_radial"
        primitive_cycles = 2
    elif square:
        orbit_class = "noncircular_rosette"
        closure_class = "closed_resonant"
        beta_q = Fraction(1, 2) * (1 + Fraction(ell_i, root))
        primitive_cycles = beta_q.denominator
    else:
        orbit_class = "noncircular_rosette"
        closure_class = "nonclosed_irrational"
        primitive_cycles = None

    return {
        "mu": mu_i,
        "b": b_i,
        "ell": ell_i,
        "action_multiplier": multiplier,
        "radicand": d,
        "radicand_square": square,
        "sqrt_radicand_decimal": dec(mp.sqrt(d)),
        "invariant_I": quad(*invariant, d),
        "radial_action": quad(*radial_action, d),
        "circular_energy": quad(*circular_energy, d),
        "energy": quad(*energy, d),
        "circular_s": quad(*circular_s, d),
        "circular_radius_squared": quad(*circular_r2, d),
        "omega_r": quad(*omega_r, d),
        "frequency_ratio": quad(*beta, d),
        "period_over_2pi": quad(*tr_over_2pi, d),
        "x_peri_decimal": dec(x_peri),
        "x_apo_decimal": dec(x_apo),
        "orbit_class": orbit_class,
        "closure_class": closure_class,
        "primitive_radial_cycles": primitive_cycles,
    }


def build() -> dict:
    mp.mp.dps = 90
    rows = [orbit_row(mu, scale_b, ell, k) for mu in (1, 2, 3) for scale_b in (1, 2, 3) for ell in (0, 1, 2, 3) for k in (1, 2, 3)]
    counts: dict[str, int] = {}
    for row in rows:
        counts[row["closure_class"]] = counts.get(row["closure_class"], 0) + 1
    boundaries = [
        {"face": "below_circular_minimum", "status": "forbidden", "statement": "E<E_c(ell) has no real radial motion"},
        {"face": "circular_energy", "status": "included", "statement": "E=E_c has J_r=0 and a closed circular orbit, or the center equilibrium when ell=0"},
        {"face": "bound_open_energy", "status": "included", "statement": "E_c<E<0 gives radial oscillation"},
        {"face": "escape_threshold", "status": "excluded_from_action_chart", "statement": "E=0 is marginal escape and T_r,J_r diverge"},
        {"face": "positive_energy", "status": "unbound", "statement": "E>0 gives escape/scattering motion"},
        {"face": "zero_angular_momentum", "status": "separate", "statement": "noncentral bound trajectories cross the smooth center and their full Cartesian period is 2T_r"},
        {"face": "signed_angular_momentum", "status": "separate", "statement": "the displayed positive ratio uses L>=0; negative L reverses its sign while ell=abs(L) controls the geometry"},
        {"face": "kepler_limit", "status": "singular_corner", "statement": "b to zero at fixed ell>0 gives ratio one; ell=0 reaches the Kepler collision singularity and is not a smooth commuting corner"},
    ]
    data = {
        "schema": "hcs-c295-henon-isochrone-action-frequency-v1",
        "candidate_id": "HCS-C295",
        "obstruction_id": "HEN-O279",
        "evaluation_date": "2026-09-02",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "model": MODEL,
        "theorem_contract": THEOREM,
        "proof_contract": PROOF,
        "route_a": ROUTE,
        "scope_flags": FLAGS,
        "enumeration": {
            "mu_values": [1, 2, 3],
            "b_values": [1, 2, 3],
            "ell_values": [0, 1, 2, 3],
            "action_multipliers": [1, 2, 3],
            "orbit_cells": len(rows),
            "boundary_cells": len(boundaries),
            "closure_counts": counts,
        },
        "orbit_cells": rows,
        "boundary_cells": boundaries,
        "references": REFERENCES,
        "nonclaims": NONCLAIMS,
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False, allow_nan=False) + "\n")
    print(f"C295_PRODUCER_PASS {data['payload_sha256']} cells={len(data['orbit_cells']) + len(data['boundary_cells'])}")


if __name__ == "__main__":
    main()
