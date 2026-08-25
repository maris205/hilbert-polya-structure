#!/usr/bin/env python3
"""Produce exact rectangular-billiard deformation evidence for HCS-C167."""
from __future__ import annotations

import argparse
from collections import defaultdict
from hashlib import sha256
import json
from math import gcd, isqrt
from pathlib import Path

import mpmath as mp


CUTOFF = 24
SOURCE_COMMIT = "4342893ce5e2516924181744bfacc01c12e4959d"
C157_SHA256 = "de4f1a278c576fd4584e7a20ff5d35144f68b4369a4e93a5acdcf625f09af567"
C162_SHA256 = "1a2cf270689cd73d6c77643c76e0e781ede9c401189a8be9f3bcbf2741653161"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"


def canonical_hash(payload: dict) -> str:
    return sha256(json.dumps(payload, sort_keys=True, separators=(",", ":"),
                             ensure_ascii=False).encode()).hexdigest()


def rational_fibres(u: int, v: int) -> dict:
    """Exact absolute-coordinate fibres for beta=u/v on a frozen sentinel box."""
    fibres: dict[int, list[list[int]]] = defaultdict(list)
    for m in range(CUTOFF + 1):
        for n in range(CUTOFF + 1):
            if m or n:
                fibres[v * m * m + u * n * n].append([m, n])
    collisions = {energy: reps for energy, reps in fibres.items() if len(reps) > 1}
    positive_primitive = {}
    for energy, reps in fibres.items():
        kept = [rep for rep in reps if rep[0] and rep[1] and gcd(rep[0], rep[1]) == 1]
        if len(kept) > 1:
            positive_primitive[energy] = kept
    first = min(collisions)
    first_pp = min(positive_primitive) if positive_primitive else None
    return {
        "beta": f"{u}/{v}",
        "u": u,
        "v": v,
        "absolute_coordinate_cutoff": CUTOFF,
        "occupied_fibres": len(fibres),
        "collision_fibres": len(collisions),
        "first_absolute_collision": {
            "N": first,
            "representatives": collisions[first],
            "globally_minimal_from_coordinate_bound": CUTOFF >= isqrt(first // min(u, v) + 1),
        },
        "first_positive_primitive_collision": None if first_pp is None else {
            "N": first_pp,
            "representatives": positive_primitive[first_pp],
            "globally_minimal_from_coordinate_bound":
                CUTOFF >= isqrt(first_pp // min(u, v) + 1),
        },
        "collision_rows": [
            {"N": energy, "representatives": reps}
            for energy, reps in sorted(collisions.items())
        ],
    }


def square_swap_quotient() -> dict:
    fibres: dict[int, list[list[int]]] = defaultdict(list)
    for m in range(1, CUTOFF + 1):
        for n in range(m, CUTOFF + 1):
            if gcd(m, n) == 1:
                fibres[m * m + n * n].append([m, n])
    energy = min(key for key, reps in fibres.items() if len(reps) > 1)
    return {
        "coordinate_cutoff": CUTOFF,
        "first_square_symmetry_inequivalent_positive_primitive_collision_N": energy,
        "representatives": fibres[energy],
        "globally_minimal_from_coordinate_bound": CUTOFF >= isqrt(energy),
    }


def complex_parts(value: mp.mpc) -> dict[str, str]:
    return {"real": mp.nstr(mp.re(value), 38), "imag": mp.nstr(mp.im(value), 38)}


def convergence_row(label: str, alpha: mp.mpf, energy: mp.mpf,
                    energy_symbol: str, multiplicity: int) -> dict:
    time = 2 * mp.sqrt(energy)
    target = (alpha * multiplicity * mp.e ** (mp.j * mp.pi / 4) /
              (8 * mp.pi * energy ** (mp.mpf(1) / 4)))
    approximants = []
    for epsilon in (mp.mpf("0.04"), mp.mpf("0.01"), mp.mpf("0.0025"),
                    mp.mpf("0.000625")):
        s = epsilon - mp.j * time
        value = (epsilon ** (mp.mpf(3) / 2) * alpha * multiplicity * s /
                 (2 * mp.pi) * (s * s + 4 * energy) ** (-mp.mpf(3) / 2))
        approximants.append({
            "epsilon": str(epsilon),
            "value": complex_parts(value),
            "absolute_error": mp.nstr(abs(value - target), 28),
        })
    assert all(mp.mpf(approximants[index + 1]["absolute_error"]) <
               mp.mpf(approximants[index]["absolute_error"])
               for index in range(len(approximants) - 1))
    return {
        "label": label,
        "alpha": mp.nstr(alpha, 40),
        "energy_symbol": energy_symbol,
        "energy": mp.nstr(energy, 40),
        "full_signed_shell_multiplicity": multiplicity,
        "target": complex_parts(target),
        "approximants": approximants,
        "strict_error_decrease": True,
    }


def irrational_box_check() -> dict:
    """Check equality in Q(sqrt(2)) coefficient-by-coefficient."""
    seen: dict[tuple[int, int], list[list[int]]] = defaultdict(list)
    for m in range(CUTOFF + 1):
        for n in range(CUTOFF + 1):
            if m or n:
                seen[(m * m, n * n)].append([m, n])
    return {
        "beta": "sqrt(2)",
        "absolute_coordinate_cutoff": CUTOFF,
        "fibres": len(seen),
        "non_sign_collisions": sum(len(reps) > 1 for reps in seen.values()),
        "comparison_rule": "equality of m^2+sqrt(2)*n^2 is coefficientwise over Q(sqrt(2))",
    }


def build_evidence() -> dict:
    mp.mp.dps = 80
    sqrt_two = mp.sqrt(2)
    fourth_root_two = mp.sqrt(sqrt_two)
    rational = [rational_fibres(1, 1), rational_fibres(2, 1),
                rational_fibres(4, 1)]
    sentinels = [
        convergence_row("square_ordered_collision", mp.mpf(1), mp.mpf(5), "5", 8),
        convergence_row("beta_two_interior_collision", sqrt_two, mp.mpf(33), "33", 8),
        convergence_row("beta_four_double_axis_double_boundary", mp.mpf(2), mp.mpf(4), "4", 4),
        convergence_row("irrational_beta_sign_only_shell", fourth_root_two,
                        1 + sqrt_two, "1+sqrt(2)", 4),
    ]
    payload = {
        "schema": "hcs-c167-rectangular-billiard-deformation-branch-evidence-v1",
        "candidate_id": "HCS-C167",
        "evaluation_date": "2026-08-25",
        "scope_literal": SCOPE,
        "source_commit": SOURCE_COMMIT,
        "source_lock": {
            "object": "Dirichlet Abel half-wave trace on Q_alpha=(0,1)x(0,alpha), alpha>0",
            "upstream_c157_evidence_sha256": C157_SHA256,
            "upstream_c162_evidence_sha256": C162_SHA256,
            "trace": "W_alpha(s)=sum_(j,k>=1) exp(-pi*s*sqrt(j^2+k^2/alpha^2)), Re(s)>0",
            "clock": "half-wave boundary time t under s=epsilon-i*t",
            "normalization": "epsilon^(3/2) at t=plus_or_minus 2*sqrt(E)",
            "determinant_convention": "none; clean lattice shells are not isolated-orbit determinants",
            "cutoff": {"all_alpha_all_shell_theorem": True,
                       "finite_collision_sentinel_absolute_coordinate": CUTOFF},
            "precision": "exact integer/quadratic-field collision arithmetic and 80-decimal branch sentinels",
            "training_data": "none",
            "forbidden_data": "target zero/prime tables, target divisor/counting law, arithmetic local or Euler factors, root numbers, automorphy, Hilbert--Polya, Route B",
        },
        "hard_gate": {
            "required": "an all-aspect trace identity plus a proved deformation law for complete shell coefficients",
            "status": "PASS_NO_MODEL_PIVOT",
            "advance_over_c162": "the square coefficient becomes an all-alpha coefficient with an exact rational collision locus and pairwise-transverse branch splitting",
        },
        "poisson_identity": {
            "formula": "W_alpha(s)=alpha*s/(2*pi)*sum_(m,n in Z)(s^2+4*(m^2+alpha^2*n^2))^(-3/2)-1/4-1/(2*(exp(pi*s)-1))-1/(2*(exp(pi*s/alpha)-1))",
            "principal_branch": True,
            "area_factor": "alpha",
            "square_recovery": "alpha=1 gives the C157 square identity exactly",
            "reciprocal_aspect": "W_alpha(s)=W_(1/alpha)(s/alpha)",
        },
        "branch_theorem": {
            "positive_time": "lim_(epsilon down to 0) epsilon^(3/2) W_alpha(epsilon-i*2*sqrt(E))=alpha*exp(i*pi/4)*R_alpha(E)/(8*pi*E^(1/4))",
            "negative_time": "the limit at -2*sqrt(E) is the complex conjugate",
            "shell": "R_alpha(E)=#{(m,n) in Z^2:m^2+alpha^2*n^2=E}",
            "uniform_tail": "outside a fixed radius, m^2+alpha^2*n^2>=min(1,alpha^2)*(m^2+n^2) gives an epsilon-uniform summable |(m,n)|^-3 majorant",
            "nonmatching_shells": "finitely many nonmatching denominators stay bounded and vanish after epsilon^(3/2)",
            "boundary_terms": "each axis subtraction has at most a simple O(epsilon^-1) pole, so even coincident axis/boundary poles vanish as O(epsilon^(1/2)) after normalization",
            "double_boundary_control": "coincident horizontal and vertical boundary poles are a sum of simple poles, never a second-order pole",
        },
        "collision_theorem": {
            "parameter": "beta=alpha^2",
            "classification": "for distinct absolute representatives with n^2!=n'^2, collision iff beta=(m'^2-m^2)/(n^2-n'^2)>0",
            "irrational_branch": "irrational beta has no collision beyond coordinate signs",
            "rational_branch": "for beta=u/v in lowest terms, complete shells are exactly fibres v*m^2+u*n^2=N",
            "squared_energy_transversality": "d(E_p-E_p')/d beta=n^2-n'^2!=0",
            "time_transversality": "at beta_0, d(t_p-t_p')/d beta=(n^2-n'^2)/sqrt(E_0)!=0",
            "multiple_collision_slopes": "distinct absolute representatives in one collision fibre have distinct n^2 slopes",
            "general_divisor_formula_claimed": False,
            "irrational_uniform_gap_claimed": False,
        },
        "quantization": {
            "operator": "sqrt(-Delta_D,alpha)",
            "hilbert_space": "L^2(Q_alpha) with Dirichlet boundary conditions",
            "same_clock": "the half-wave boundary time is unchanged",
            "antiunitary": "complex conjugation reverses exp(-i*t*sqrt(-Delta_D,alpha))",
            "target_operator_claimed": False,
        },
        "finite_sentinels": {
            "rational_fibres": rational,
            "square_swap_quotient": square_swap_quotient(),
            "irrational_quadratic_field": irrational_box_check(),
            "branch_convergence": sentinels,
        },
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "claim_boundary": {
            "isolated_primitive_orbit_determinant": False,
            "target_trace_identity": False,
            "target_divisor_matching": False,
            "target_functional_equation": False,
            "target_counting_law": False,
            "arithmetic_local_data": False,
            "euler_factors": False,
            "root_numbers": False,
            "automorphy": False,
            "hilbert_polya_operator": False,
            "route_b": False,
        },
    }
    payload["payload_sha256"] = canonical_hash(payload)
    return payload


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path,
                        default=root / "results/c167_rectangle_evidence.json")
    args = parser.parse_args()
    payload = build_evidence()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    print(json.dumps({
        "status": "C167_PRODUCER_PASS",
        "payload_sha256": payload["payload_sha256"],
        "rational_fibre_rows": len(payload["finite_sentinels"]["rational_fibres"]),
        "branch_sentinels": len(payload["finite_sentinels"]["branch_convergence"]),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
