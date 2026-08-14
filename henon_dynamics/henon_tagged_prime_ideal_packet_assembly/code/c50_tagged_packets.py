#!/usr/bin/env python3
"""Exact HCS-P50 tagged prime-ideal packet certificate.

The certificate works in the inversion-fixed trace fields of the three
source-locked H6 multipliers.  It never identifies a rational prime with an
orbit.  Instead it records the orbit, cyclotomic index, trace-field prime
ideal, residue degree, ramification index, and ideal valuation separately.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import warnings
from collections import defaultdict
from pathlib import Path
from typing import Any

import sympy as sp
from sympy.utilities.exceptions import SymPyDeprecationWarning


warnings.filterwarnings("ignore", category=SymPyDeprecationWarning)


PROJECT = Path(__file__).resolve().parents[1]
TRACK = PROJECT.parent
DEFAULT_OUTPUT = PROJECT / "results" / "c50_certificate.json"
X, T = sp.symbols("X T")

DEPENDENCIES = {
    "p49_readme": (
        TRACK / "henon_cyclic_resultant_packet_obstruction" / "README.md",
        "89cc224510fd6d3eb2e3f1a0c1f0996bb40ea753e4fdb0d50630bb48b024f9a9",
    ),
    "p49_proof": (
        TRACK / "henon_cyclic_resultant_packet_obstruction" / "PROOF_PACKAGE.md",
        "1adc57e42ecba61f1e1d5b8a1e076a3999eef328588ded230e556d0a0c45ad9c",
    ),
    "p49_code": (
        TRACK
        / "henon_cyclic_resultant_packet_obstruction"
        / "code"
        / "c49_cyclic_packets.py",
        "bbc11c5ce5fc482b64fffa8403cb45dfe971cd3d9488fbf19bd0b98c4fb4622d",
    ),
    "p49_certificate": (
        TRACK
        / "henon_cyclic_resultant_packet_obstruction"
        / "results"
        / "c49_certificate.json",
        "da866888620533376a487667c2d0900c109ed7b984d57e28d49a0a319c407450",
    ),
}

# The trace variable is t=lambda+lambda^{-1}.  For the signed period-three
# branch, t=-38-42*sqrt(5); replacing it by a positive modulus is forbidden.
ORBIT_SPECS: dict[str, dict[str, Any]] = {
    "period_1": {
        "primitive_period": 1,
        "signed_branch": "+L1",
        "multiplier_polynomial": sp.Poly(X**4 - 4 * X**3 - 22 * X**2 - 4 * X + 1, X),
        "trace_field": "Q(sqrt(7))",
        "integral_basis": "1,w with w=sqrt(7)",
        "basis_minpoly": sp.Poly(X**2 - 7, X),
        "field_discriminant": 28,
        "trace_value": 2 + 2 * sp.sqrt(7),
        "basis_coordinates": lambda a, b: (int(a), int(b)),
    },
    "period_3": {
        "primitive_period": 3,
        "signed_branch": "-L3",
        "multiplier_polynomial": sp.Poly(X**4 + 76 * X**3 - 7374 * X**2 + 76 * X + 1, X),
        "trace_field": "Q(sqrt(5))",
        "integral_basis": "1,w with w=(1+sqrt(5))/2",
        "basis_minpoly": sp.Poly(X**2 - X - 1, X),
        "field_discriminant": 5,
        "trace_value": -38 - 42 * sp.sqrt(5),
        # a+b*sqrt(5)=(a-b)+2*b*w.
        "basis_coordinates": lambda a, b: (int(a - b), int(2 * b)),
    },
    "period_4": {
        "primitive_period": 4,
        "signed_branch": "+L4",
        "multiplier_polynomial": sp.Poly(X**2 - 578 * X + 1, X),
        "trace_field": "Q",
        "integral_basis": "1",
        "basis_minpoly": None,
        "field_discriminant": 1,
        "trace_value": sp.Integer(578),
        "basis_coordinates": lambda a, b: (int(a), 0),
    },
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_sha(payload: object) -> str:
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(encoded).hexdigest()


def dependency_locks() -> dict[str, dict[str, str]]:
    locks: dict[str, dict[str, str]] = {}
    for name, (path, expected) in DEPENDENCIES.items():
        observed = sha256(path)
        if observed != expected:
            raise RuntimeError(f"dependency hash changed: {name}")
        locks[name] = {"path": str(path.relative_to(TRACK)), "sha256": observed}
    return locks


def factorization(value: int) -> dict[str, int]:
    return {
        str(prime): int(exponent)
        for prime, exponent in sp.factorint(abs(int(value))).items()
    }


def beta_trace_polynomial(index: int) -> sp.Expr:
    """Return X^{-phi(n)/2} Phi_n(X) as a polynomial in T=X+X^{-1}."""
    if index <= 2:
        raise ValueError("the inversion-fixed half packet starts at index 3")
    cyclotomic = sp.Poly(sp.cyclotomic_poly(index, X), X)
    half_degree = int(sp.totient(index)) // 2
    laurent = {
        int(power[0] - half_degree): sp.Integer(coefficient)
        for power, coefficient in cyclotomic.terms()
    }
    symmetric = {0: sp.Integer(2), 1: T}
    for power in range(2, half_degree + 1):
        symmetric[power] = sp.expand(T * symmetric[power - 1] - symmetric[power - 2])
    result = sp.Integer(laurent.get(0, 0))
    for power in range(1, half_degree + 1):
        if laurent.get(power, 0) != laurent.get(-power, 0):
            raise ArithmeticError(f"cyclotomic reciprocity failed at index {index}")
        result += laurent.get(power, 0) * symmetric[power]
    return sp.expand(result)


def trace_element(orbit: str, index: int) -> dict[str, Any]:
    spec = ORBIT_SPECS[orbit]
    polynomial = beta_trace_polynomial(index)
    value = sp.expand(polynomial.subs(T, spec["trace_value"]))
    if spec["trace_field"] == "Q":
        a, b = sp.Integer(value), sp.Integer(0)
    else:
        radical = sp.sqrt(7) if orbit == "period_1" else sp.sqrt(5)
        a = sp.expand(value).coeff(radical, 0)
        b = sp.expand(value).coeff(radical)
    u, v = spec["basis_coordinates"](a, b)
    if orbit == "period_1":
        norm = u * u - 7 * v * v
    elif orbit == "period_3":
        # w^2=w+1 and conjugate(w)=1-w.
        norm = u * u + u * v - v * v
    else:
        norm = u
    if norm == 0:
        raise ArithmeticError(f"zero half packet: {orbit}, {index}")
    return {
        "trace_polynomial": str(polynomial),
        "basis_u": int(u),
        "basis_v": int(v),
        "signed_norm": int(norm),
        "absolute_norm": abs(int(norm)),
    }


def p_adic_valuation(value: int, prime: int) -> int:
    if value == 0:
        raise ValueError("zero has no finite p-adic valuation here")
    value = abs(int(value))
    valuation = 0
    while value % prime == 0:
        valuation += 1
        value //= prime
    return valuation


def polynomial_value(value: int, orbit: str) -> int:
    if orbit == "period_1":
        return value * value - 7
    if orbit == "period_3":
        return value * value - value - 1
    raise ValueError("the rational trace field has no quadratic basis polynomial")


def polynomial_derivative(value: int, orbit: str) -> int:
    return 2 * value if orbit == "period_1" else 2 * value - 1


def split_roots(prime: int, orbit: str) -> list[int]:
    if orbit == "period_1":
        return sorted(int(root) for root in sp.sqrt_mod(7, prime, all_roots=True))
    if prime == 2:
        return []
    inverse_two = pow(2, -1, prime)
    return sorted(
        int((1 + root) * inverse_two % prime)
        for root in sp.sqrt_mod(5, prime, all_roots=True)
    )


def split_prime_valuation(
    u: int,
    v: int,
    prime: int,
    root: int,
    norm_exponent: int,
    orbit: str,
) -> int:
    """Compute v_(p,w-root)(u+v*w) by Hensel lifting the simple root."""
    modulus = prime
    lifted_root = root % prime
    valuation = 0
    for exponent in range(1, norm_exponent + 2):
        if (u + v * lifted_root) % modulus != 0:
            break
        valuation = exponent
        next_modulus = modulus * prime
        derivative = polynomial_derivative(lifted_root, orbit)
        lifted_root = (
            lifted_root
            - polynomial_value(lifted_root, orbit) * pow(derivative, -1, next_modulus)
        ) % next_modulus
        modulus = next_modulus
    return valuation


def factor_trace_ideal(orbit: str, index: int, element: dict[str, Any]) -> list[dict[str, Any]]:
    spec = ORBIT_SPECS[orbit]
    u, v = int(element["basis_u"]), int(element["basis_v"])
    rational_factors = sp.factorint(int(element["absolute_norm"]))
    atoms: list[dict[str, Any]] = []
    for prime_raw, norm_exponent_raw in rational_factors.items():
        prime, norm_exponent = int(prime_raw), int(norm_exponent_raw)
        order_certified = index % prime != 0
        if orbit == "period_4":
            atoms.append(
                {
                    "rational_prime": prime,
                    "prime_ideal": f"({prime}) in Z",
                    "splitting_type": "rational",
                    "ramification_index": 1,
                    "residue_degree": 1,
                    "ideal_valuation": norm_exponent,
                    "norm_exponent": norm_exponent,
                    "residue_order_certified": order_certified,
                    "residue_order": index if order_certified else None,
                }
            )
            continue

        discriminant = int(spec["field_discriminant"])
        symbol = int(sp.kronecker_symbol(discriminant, prime))
        if discriminant % prime == 0:
            repeated_roots = [
                root
                for root in range(prime)
                if polynomial_value(root, orbit) % prime == 0
            ]
            if len(repeated_roots) != 1:
                raise ArithmeticError(f"ramified root failure: {orbit}, p={prime}")
            atoms.append(
                {
                    "rational_prime": prime,
                    "prime_ideal": f"({prime},w-{repeated_roots[0]})",
                    "splitting_type": "ramified",
                    "ramification_index": 2,
                    "residue_degree": 1,
                    "ideal_valuation": norm_exponent,
                    "norm_exponent": norm_exponent,
                    "residue_order_certified": order_certified,
                    "residue_order": index if order_certified else None,
                }
            )
        elif symbol == -1:
            valuation = min(p_adic_valuation(u, prime), p_adic_valuation(v, prime))
            if 2 * valuation != norm_exponent:
                raise ArithmeticError(f"inert valuation mismatch: {orbit}, {index}, p={prime}")
            atoms.append(
                {
                    "rational_prime": prime,
                    "prime_ideal": f"({prime})O_F",
                    "splitting_type": "inert",
                    "ramification_index": 1,
                    "residue_degree": 2,
                    "ideal_valuation": valuation,
                    "norm_exponent": 2 * valuation,
                    "residue_order_certified": order_certified,
                    "residue_order": index if order_certified else None,
                }
            )
        elif symbol == 1:
            split_atoms = []
            for root in split_roots(prime, orbit):
                valuation = split_prime_valuation(u, v, prime, root, norm_exponent, orbit)
                if valuation:
                    split_atoms.append(
                        {
                            "rational_prime": prime,
                            "prime_ideal": f"({prime},w-{root})",
                            "splitting_type": "split",
                            "ramification_index": 1,
                            "residue_degree": 1,
                            "ideal_valuation": valuation,
                            "norm_exponent": valuation,
                            "residue_order_certified": order_certified,
                            "residue_order": index if order_certified else None,
                        }
                    )
            if sum(atom["norm_exponent"] for atom in split_atoms) != norm_exponent:
                raise ArithmeticError(f"split valuation mismatch: {orbit}, {index}, p={prime}")
            atoms.extend(split_atoms)
        else:
            raise ArithmeticError(f"unexpected splitting symbol: {orbit}, p={prime}")
    return atoms


def poly_power_mod(exponent: int, modulus_poly: sp.Poly, prime: int) -> sp.Poly:
    result = sp.Poly(1, X, modulus=prime)
    base = sp.Poly(X, X, modulus=prime).rem(modulus_poly)
    power = int(exponent)
    while power:
        if power & 1:
            result = (result * base).rem(modulus_poly)
        base = (base * base).rem(modulus_poly)
        power //= 2
    return result


def multiplier_order_control(orbit: str, index: int, prime: int) -> dict[str, Any]:
    """Verify exact residue order in every finite-field factor when p does not divide n."""
    spec = ORBIT_SPECS[orbit]
    multiplier_poly = sp.Poly(spec["multiplier_polynomial"].as_expr(), X, modulus=prime)
    cyclotomic = sp.Poly(sp.cyclotomic_poly(index, X), X, modulus=prime)
    common = sp.gcd(multiplier_poly, cyclotomic)
    if common.degree() <= 0:
        raise ArithmeticError(f"missing multiplier-field support: {orbit}, {index}, p={prime}")
    factors = sp.factor_list(common.as_expr(), X, modulus=prime)[1]
    degrees: list[int] = []
    verified = index % prime != 0
    for factor_expr, multiplicity in factors:
        factor = sp.Poly(factor_expr, X, modulus=prime)
        degrees.extend([int(factor.degree())] * int(multiplicity))
        if verified:
            if poly_power_mod(index, factor, prime) != sp.Poly(1, X, modulus=prime):
                raise ArithmeticError(f"x^n != 1 in residue field: {orbit}, {index}, p={prime}")
            for divisor in sp.divisors(index):
                if divisor < index and poly_power_mod(divisor, factor, prime) == sp.Poly(1, X, modulus=prime):
                    raise ArithmeticError(
                        f"residue order dropped: {orbit}, {index}, p={prime}, divisor={divisor}"
                    )
    return {
        "common_factor_degree": int(common.degree()),
        "residue_factor_degrees": degrees,
        "exact_order_verified": verified,
        "exact_order": index if verified else None,
    }


def build_certificate(min_index: int = 3, max_index: int = 20) -> dict[str, Any]:
    if min_index != 3 or max_index < min_index:
        raise ValueError("the frozen certificate starts at index 3")

    p49 = json.loads(DEPENDENCIES["p49_certificate"][0].read_text(encoding="utf-8"))
    p49_crosschecks = 0
    rows: list[dict[str, Any]] = []
    tagged_atoms: list[dict[str, Any]] = []
    for orbit, spec in ORBIT_SPECS.items():
        for index in range(min_index, max_index + 1):
            element = trace_element(orbit, index)
            if index <= 12:
                inherited = p49["orbits"][orbit]["rows"][index - 1]["canonical_half_norm"]
                if inherited != element["absolute_norm"]:
                    raise ArithmeticError(f"P49 half-norm mismatch: {orbit}, {index}")
                p49_crosschecks += 1
            atoms = factor_trace_ideal(orbit, index, element)
            rational_factorization = factorization(element["absolute_norm"])
            reconstructed: dict[str, int] = defaultdict(int)
            order_controls: dict[str, Any] = {}
            for atom in atoms:
                prime = int(atom["rational_prime"])
                reconstructed[str(prime)] += int(atom["norm_exponent"])
                atom_with_tags = {
                    "orbit": orbit,
                    "primitive_period": int(spec["primitive_period"]),
                    "cyclotomic_index": index,
                    **atom,
                }
                tagged_atoms.append(atom_with_tags)
                key = str(prime)
                if key not in order_controls:
                    order_controls[key] = multiplier_order_control(orbit, index, prime)
            if dict(sorted(reconstructed.items(), key=lambda item: int(item[0]))) != rational_factorization:
                raise ArithmeticError(f"norm pushforward mismatch: {orbit}, {index}")
            rows.append(
                {
                    "orbit": orbit,
                    "primitive_period": int(spec["primitive_period"]),
                    "signed_branch": spec["signed_branch"],
                    "cyclotomic_index": index,
                    "trace_field": spec["trace_field"],
                    "integral_basis": spec["integral_basis"],
                    **element,
                    "rational_factorization": rational_factorization,
                    "prime_ideal_atoms": atoms,
                    "multiplier_order_controls": order_controls,
                    "norm_pushforward_exact": True,
                }
            )

    by_prime: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for atom in tagged_atoms:
        by_prime[int(atom["rational_prime"])].append(atom)
    collisions = {
        str(prime): atoms
        for prime, atoms in sorted(by_prime.items())
        if len(atoms) > 1
    }
    cross_orbit_primes = sorted(
        prime for prime, atoms in by_prime.items() if len({atom["orbit"] for atom in atoms}) > 1
    )
    cross_index_primes = sorted(
        prime
        for prime, atoms in by_prime.items()
        if len({atom["cyclotomic_index"] for atom in atoms}) > 1
    )
    multi_order_primes = {
        str(prime): sorted(
            {
                int(atom["residue_order"])
                for atom in atoms
                if atom["residue_order_certified"]
            }
        )
        for prime, atoms in sorted(by_prime.items())
        if len(
            {
                int(atom["residue_order"])
                for atom in atoms
                if atom["residue_order_certified"]
            }
        )
        > 1
    }

    expected_multi_order = {
        "11": [5, 12],
        "19": [3, 10, 20],
        "29": [7, 14, 15],
        "79": [8, 16],
        "131": [5, 12],
        "307": [11, 17],
        "38039": [13, 19],
    }
    # The precise set is a frozen adversarial checksum, not an asymptotic claim.
    if multi_order_primes != expected_multi_order:
        raise ArithmeticError(f"multi-order collision ledger changed: {multi_order_primes}")

    p109 = by_prime[109]
    if not (
        len(p109) == 3
        and {atom["orbit"] for atom in p109} == {"period_1", "period_3"}
        and {atom["cyclotomic_index"] for atom in p109} == {11}
        and len({atom["prime_ideal"] for atom in p109 if atom["orbit"] == "period_1"}) == 2
    ):
        raise ArithmeticError("orbit/prime-ideal tag necessity control failed at p=109")

    total_atoms = len(tagged_atoms)
    distinct_rational_primes = len(by_prime)
    rational_pushforward_kernel_rank = total_atoms - distinct_rational_primes
    if rational_pushforward_kernel_rank <= 0:
        raise ArithmeticError("rational pushforward unexpectedly injective")

    core = {
        "candidate_id": "HCS-P50",
        "obstruction_id": "HEN-O90",
        "claim_status": "PROVED_WITH_EXACT_FINITE_CERTIFICATE",
        "assembly_status": "PROVED_TAGGED_FINITE_CUTOFF_LEDGER",
        "untagged_pushforward_status": "STOP_SCOPED_NONINJECTIVE",
        "min_index": min_index,
        "max_index": max_index,
        "orbit_specs": {
            orbit: {
                key: (str(value.as_expr()) if isinstance(value, sp.Poly) else str(value))
                for key, value in spec.items()
                if key not in {"basis_coordinates"}
            }
            for orbit, spec in ORBIT_SPECS.items()
        },
        "rows": rows,
        "collision_ledger": collisions,
        "multi_order_collision_primes": multi_order_primes,
        "tag_necessity_controls": {
            "orbit_tag": "p=109,index=11 occurs in period_1 and period_3",
            "index_tag": "p=29 carries exact good orders 7,14,15",
            "prime_ideal_tag": "period_1,p=109,index=11 has two distinct split prime ideals",
            "signed_branch_tag": "period_3 uses -L3 inherited from HCS-P49",
        },
        "finite_summary": {
            "orbit_count": len(ORBIT_SPECS),
            "index_count_per_orbit": max_index - min_index + 1,
            "packet_row_count": len(rows),
            "tagged_prime_ideal_atom_count": total_atoms,
            "distinct_rational_prime_count": distinct_rational_primes,
            "rational_pushforward_kernel_rank": rational_pushforward_kernel_rank,
            "collision_prime_count": len(collisions),
            "cross_orbit_collision_prime_count": len(cross_orbit_primes),
            "cross_index_collision_prime_count": len(cross_index_primes),
            "multi_order_collision_prime_count": len(multi_order_primes),
            "good_order_atom_count": sum(
                bool(atom["residue_order_certified"]) for atom in tagged_atoms
            ),
            "bad_characteristic_atom_count": sum(
                not bool(atom["residue_order_certified"]) for atom in tagged_atoms
            ),
            "p49_half_norm_crosschecks": p49_crosschecks,
        },
        "theorem_ledger": {
            "trace_field_half_packets_integral": True,
            "tagged_divisor_assembly_canonical_at_finite_cutoff": True,
            "norm_pushforward_exact": True,
            "good_characteristic_residue_order_equals_index": True,
            "rational_prime_pushforward_injective": False,
            "orbit_index_prime_ideal_tags_all_needed_on_certificate": True,
            "pressure_weighted_all_orbit_limit": "OPEN",
            "von_mangoldt_trace": "OPEN",
            "analytic_continuation": "OPEN",
            "hilbert_polya_operator": "OPEN",
        },
        "claim_boundary": (
            "a lossless finite-cutoff tagged prime-ideal ledger and an intrinsic good-characteristic "
            "residue-order clock are proved; the untagged rational-prime pushforward is noninjective, "
            "but no all-orbit convergence, von Mangoldt weighting, determinant continuation, or operator is proved"
        ),
        "sources": {
            "cyclic_resultants": "Hillar, Journal of Symbolic Computation 39 (2005), 653-669",
            "cyclic_recurrences": "Hillar-Levine, Proceedings AMS 135 (2007), 1607-1618",
            "quadratic_primitive_divisors": "Flatters, arXiv:0708.2190",
            "lucas_lehmer_primitive_divisors": "Bilu-Hanrot-Voutier, J. Reine Angew. Math. 539 (2001), 75-122",
            "arithmetic_dynamics_scope_control": "Ingram-Silverman, arXiv:0707.2505",
        },
    }
    return {
        **core,
        "core_sha256": canonical_sha(core),
        "dependency_locks": dependency_locks(),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--min-index", type=int, default=3)
    parser.add_argument("--max-index", type=int, default=20)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    certificate = build_certificate(args.min_index, args.max_index)
    if args.check:
        print(
            json.dumps(
                {
                    "assembly_status": certificate["assembly_status"],
                    "candidate_id": certificate["candidate_id"],
                    "check": True,
                    "core_sha256": certificate["core_sha256"],
                    "finite_summary": certificate["finite_summary"],
                    "untagged_pushforward_status": certificate["untagged_pushforward_status"],
                },
                sort_keys=True,
            )
        )
        return 0
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
