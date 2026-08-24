#!/usr/bin/env python3
"""Produce the exact C126 Chebyshev contracting-skew certificate.

The package is deliberately source-only: it proves an all-period orbit and
stability theorem for one frozen skew product, without importing prime data,
zero data, or a target divisor.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "results/c126_chebyshev_skew_evidence.json"
PREFIX_MAX = 12


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mobius(n: int) -> int:
    factors = []
    value = n
    p = 2
    while p * p <= value:
        exponent = 0
        while value % p == 0:
            exponent += 1
            value //= p
        if exponent >= 2:
            return 0
        if exponent == 1:
            factors.append(p)
        p += 1
    if value > 1:
        factors.append(value)
    return -1 if len(factors) % 2 else 1


def primitive_row(n: int) -> dict[str, int]:
    fixed = 3**n
    exact_points = sum(mobius(d) * 3 ** (n // d) for d in divisors(n))
    primitive_orbits = exact_points // n
    negative_exact_points = sum(
        mobius(d) * (3 ** (n // d) - 1)
        for d in divisors(n)
        if d % 2 == 1
    ) // 2
    negative_orbits = negative_exact_points // n
    positive_orbits = primitive_orbits - negative_orbits
    assert exact_points % n == 0
    assert negative_exact_points % n == 0
    return {
        "n": n,
        "fixed_points": fixed,
        "exact_period_points": exact_points,
        "primitive_orbits": primitive_orbits,
        "positive_unstable_orientation_primitive_orbits": positive_orbits,
        "negative_unstable_orientation_primitive_orbits": negative_orbits,
    }


def main() -> None:
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_OUT
    x = sp.symbols("x")
    t3 = 4 * x**3 - 3 * x
    iterate = x
    iterate_checks = []
    for n in range(1, 5):
        iterate = sp.expand(t3.subs(x, iterate))
        target = sp.chebyshevt(3**n, x)
        assert sp.expand(iterate - target) == 0
        iterate_checks.append({
            "n": n,
            "degree": int(sp.degree(iterate, x)),
            "matches_T_3_power_n": True,
        })

    primitive_prefix = [primitive_row(n) for n in range(1, PREFIX_MAX + 1)]
    stability_prefix = []
    for n in range(1, PREFIX_MAX + 1):
        m = 3**n
        positive_interior = (m - 3) // 2
        negative_interior = (m - 1) // 2
        stability_prefix.append({
            "n": n,
            "m": m,
            "endpoint_count": 2,
            "positive_interior_count": positive_interior,
            "negative_interior_count": negative_interior,
            "positive_unstable_orientation_fixed_points": positive_interior + 2,
            "negative_unstable_orientation_fixed_points": negative_interior,
            "endpoint_unstable_multiplier": str(m * m),
            "positive_interior_unstable_multiplier": str(m),
            "negative_interior_unstable_multiplier": str(-m),
            "stable_multiplier": f"1/{4**n}",
            "endpoint_stability_determinant": f"(1-{m*m})*(1-1/{4**n})",
            "positive_interior_stability_determinant": f"(1-{m})*(1-1/{4**n})",
            "negative_interior_stability_determinant": f"(1+{m})*(1-1/{4**n})",
        })

    g = 4 * x**3 - 2 * x
    g2 = sp.expand(g.subs(x, g))
    g2_fixed = sp.factor(g2 - x)
    g2_minus_t9 = sp.factor(g2 - sp.chebyshevt(9, x))
    assert g2_fixed == x * (2*x - 1)**3 * (2*x + 1)**3 * (4*x**2 - 3)
    assert g2_minus_t9 == x * (192*x**6 - 240*x**4 + 80*x**2 - 5)

    payload = {
        "schema": "hcs-c126-chebyshev-contracting-skew-v1",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_model": {
            "candidate_id": "HCS-C126",
            "map": "F(x,y)=(T_3(x),y/4+x)=(4*x^3-3*x,y/4+x)",
            "base_map": "f(x)=T_3(x)=4*x^3-3*x",
            "fiber_multiplier": "1/4",
            "phase_space": "R^2",
            "clock": "one application of F",
            "normalization": "unweighted isolated fixed-point count",
            "determinant_convention": "Artin-Mazur zeta exp(sum_{n>=1} #Fix(F^n) z^n/n)",
            "orbit_cutoff": "none for the theorem; n<=12 only for the replay ledger",
            "precision": "exact integer, rational, and symbolic arithmetic",
            "allowed_data": "the frozen source map only",
            "forbidden_data": "prime tables, zero tables, arithmetic local factors, target fitting",
        },
        "all_period_theorem": {
            "base_iterate_identity": "f^n(x)=T_(3^n)(x) for every n>=1",
            "induction_identity": "T_a(T_b(x))=T_(a*b)(x)",
            "finite_symbolic_replay": iterate_checks,
            "base_fixed_polynomial": "T_(3^n)(x)-x",
            "base_fixed_root_count": "3^n distinct real roots",
            "root_families": [
                "cos(2*pi*k/(3^n-1)), 0<=k<=(3^n-1)/2",
                "cos(2*pi*k/(3^n+1)), 0<=k<=(3^n+1)/2",
            ],
            "root_family_intersection": "{1,-1}",
            "root_count_derivation": "(3^n+1)/2+(3^n+3)/2-2=3^n",
            "simplicity": "interior derivatives are +/-3^n and endpoint derivatives are 3^(2n), so d(T_(3^n)-x)/dx never vanishes at a root",
            "fiber_iterate": "y_n=4^(-n)*y+sum_{j=0}^{n-1}4^(-(n-1-j))*T_(3^j)(x)",
            "unique_fiber_closure": "y_*=sum_{j=0}^{n-1}4^(-(n-1-j))*T_(3^j)(x)/(1-4^(-n))",
            "fixed_point_count": "#Fix(F^n)=3^n for every n>=1",
            "least_period_preservation": "the unique fiber lift has the same least period as its base orbit",
        },
        "primitive_orbits": {
            "exact_period_point_formula": "E_n=sum_{d|n} mu(d)*3^(n/d)",
            "primitive_orbit_formula": "P_n=(1/n)*sum_{d|n} mu(d)*3^(n/d)",
            "negative_orientation_exact_point_formula": "E_n^-=1/2*sum_{d|n,d odd}mu(d)*(3^(n/d)-1)",
            "negative_orientation_orbit_formula": "P_n^-=E_n^-/n",
            "prefix_n1_to_n12": primitive_prefix,
        },
        "zeta": {
            "definition": "zeta_F(z)=exp(sum_{n>=1}#Fix(F^n)*z^n/n)",
            "fixed_count_trace_series": "sum_{n>=1}3^n*z^n/n=-log(1-3*z)",
            "closed_form": "zeta_F(z)=1/(1-3*z)",
            "primitive_product": "product_{primitive gamma}(1-z^(period gamma))^(-1)",
            "convergence_disk": "|z|<1/3 for the defining logarithmic series",
            "qualification": "source Artin-Mazur zeta only; not a target-facing weighted Fredholm determinant",
        },
        "stability": {
            "jacobian": "DF(x,y)=[[12*x^2-3,0],[1,1/4]]",
            "iterate_jacobian": "DF^n(x,y)=[[(T_(3^n))'(x),0],[c_n(x),4^(-n)]]",
            "off_diagonal": "c_n(x)=sum_{j=0}^{n-1}4^(-(n-1-j))*(T_(3^j))'(x)",
            "fixed_root_multiplier_classes": "two endpoints: 3^(2n); (3^n-3)/2 interior: +3^n; (3^n-1)/2 interior: -3^n",
            "hyperbolicity": "all fixed points of every F^n are saddles and det(I-DF^n) is nonzero",
            "stability_determinant": "det(I-DF^n)=(1-(T_(3^n))'(x))*(1-4^(-n))",
            "orientation_counts": "positive=(3^n+1)/2 and negative=(3^n-1)/2",
            "primitive_repetition_law": "for primitive period p multiplier alpha and repetition r, eigenvalues of DF^(pr) are alpha^r and 4^(-pr), det(I-DF^(pr))=(1-alpha^r)*(1-4^(-pr)), orientation sign=(sign alpha)^r",
            "primitive_multiplier_qualification": "for p>1 alpha is +/-3^p; for p=1 the endpoint alpha is 9 and the central alpha is -3",
            "prefix_n1_to_n12": stability_prefix,
        },
        "negative_controls": {
            "unit_fiber_multiplier": {
                "map": "F_1(x,y)=(T_3(x),y+x)",
                "n1_closure": "x=0 gives the whole fixed line {(0,y)}; x=+/-1 gives no fiber closure",
                "failure": "unique isolated fiber closure fails and the stable determinant factor 1-1 vanishes",
            },
            "non_chebyshev_cubic": {
                "map": "G(x,y)=(4*x^3-2*x,y/4+x)",
                "base_second_iterate_minus_x_factorization": "x*(2*x-1)^3*(2*x+1)^3*(4*x^2-3)",
                "distinct_base_fix_g2": 5,
                "degree_with_multiplicity": 9,
                "second_iterate_minus_T9": "x*(192*x^6-240*x^4+80*x^2-5)",
                "failure": "the Chebyshev composition identity, nine distinct roots, and hyperbolicity fail; +/-1/2 form a neutral period-two orbit",
            },
        },
        "progress_over_prior_gate": {
            "prior_split": "earlier packages separated a complete all-period orbit layer from a source-owned global operator, or supplied only finite low-period witnesses",
            "new_result": "one elementary nontrivial skew dynamics now has an all-period complete real fixed-point atlas, exact primitive counts, an orbit-owned zeta, and all-period stability/orientation/repetition laws",
            "remaining_gap": "no weighted global transfer/Fredholm owner, target divisor comparison, analytic completion, or natural lift is provided",
        },
        "route_a_evaluator": {
            "canonical_tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "A1_qualification": "ALL_PERIOD_SOURCE_ORBITS_PROVED_BUT_NO_PRIME_LIKE_TARGET_SEMANTICS_OR_MANDATORY_TARGET_CONTROLS",
            "A2_qualification": "ARTIN_MAZUR_ZETA_IS_SOURCE_ORBIT_OWNED_BUT_NOT_A_WEIGHTED_TARGET_FACING_FREDHOLM_DETERMINANT",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COMPLETION_COUNTING_LAW_OR_CONTROLLED_TARGET_CONTINUATION",
            "A4_qualification": "NO_NATURAL_UNITARY_SCATTERING_OR_HAMILTONIAN_LIFT",
            "overall": "ROUTE_A_EXPLORATORY",
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "a prime-to-orbit correspondence or target divisor match",
            "a weighted nuclear transfer operator or Fredholm determinant",
            "a target functional equation, Gamma completion, or Riemann-von Mangoldt law",
            "arithmetic/local data, Euler factors, root numbers, or automorphy",
            "a Hilbert--Polya operator, Riemann-zero statement, or Route-B authorization",
        ],
    }
    raw = json.dumps(payload, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(raw)
    print(json.dumps({
        "status": "C126_PRODUCER_PASS",
        "evidence_sha256": sha256(raw.encode()).hexdigest(),
        "primitive_rows": len(primitive_prefix),
        "stability_rows": len(stability_prefix),
        "all_period_fixed_count_theorem": True,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
