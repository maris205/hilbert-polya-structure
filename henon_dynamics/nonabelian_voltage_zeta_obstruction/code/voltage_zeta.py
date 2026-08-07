#!/usr/bin/env python3
"""Exact certificates for the HCS-C15 nonabelian voltage-zeta obstruction.

The program has two deliberately separate jobs.

1.  It verifies Artin--Ihara block factorization for the two-generator
    bouquet with deck group D4.  All determinants are computed over ZZ.
2.  It exhibits two cyclically reduced Heisenberg words with identical
    directed Parikh data but distinct central holonomy.  The aggregated
    nontrivial regular-representation factor cannot distinguish them.

The zero-density theorem itself is analytic; numerical zero counts below are
only an illustration of the exact unit-roof lattice formula.
"""

from __future__ import annotations

import argparse
import cmath
import json
import math
from fractions import Fraction
from pathlib import Path
from typing import Iterable

import sympy as sp


INVERSE_EDGE = (1, 0, 3, 2)


def block_nonbacktracking(representatives: list[sp.Matrix], weights: list[sp.Expr]) -> sp.Matrix:
    """Return the chronology-preserving twisted Hashimoto matrix.

    Directed edges are (a, A, b, B).  The block in row f, column e is
    weight(f) rho(g_f), unless f immediately reverses e.
    """

    if len(representatives) != 4 or len(weights) != 4:
        raise ValueError("four directed-edge representatives and weights are required")
    dimension = representatives[0].rows
    if any(matrix.shape != (dimension, dimension) for matrix in representatives):
        raise ValueError("representation matrices must have one common square size")

    matrix = sp.zeros(4 * dimension)
    for edge in range(4):
        for following in range(4):
            if following == INVERSE_EDGE[edge]:
                continue
            block = weights[following] * representatives[following]
            matrix[
                dimension * following : dimension * (following + 1),
                dimension * edge : dimension * (edge + 1),
            ] = block
    return matrix


def d4_multiply(left: tuple[int, int], right: tuple[int, int]) -> tuple[int, int]:
    """Multiply r^k s^b using s r s = r^{-1}."""

    k, b = left
    ell, c = right
    return ((k + (-1 if b else 1) * ell) % 4, (b + c) % 2)


def d4_elements() -> list[tuple[int, int]]:
    return [(k, b) for b in range(2) for k in range(4)]


def d4_regular_cover_matrix(u: sp.Symbol) -> sp.Matrix:
    """Untwisted nonbacktracking matrix of the eight-sheeted D4 cover."""

    group = d4_elements()
    index = {element: position for position, element in enumerate(group)}
    generators = ((1, 0), (3, 0), (0, 1), (0, 1))
    matrix = sp.zeros(4 * len(group))
    for edge in range(4):
        for following in range(4):
            if following == INVERSE_EDGE[edge]:
                continue
            for element in group:
                target = d4_multiply(element, generators[following])
                row = 4 * index[target] + following
                column = 4 * index[element] + edge
                matrix[row, column] = u
    return matrix


def d4_certificates() -> dict[str, object]:
    x, y, u = sp.symbols("x y u")
    rotation = sp.Matrix([[0, -1], [1, 0]])
    reflection = sp.Matrix([[1, 0], [0, -1]])
    irrep_two = [rotation, rotation.inv(), reflection, reflection]

    weighted = block_nonbacktracking(irrep_two, [x, x, y, y])
    bivariate = sp.factor((sp.eye(8) - weighted).det())
    unit_two = sp.factor(bivariate.subs({x: u, y: u}))

    one_dimensional: list[sp.Expr] = []
    one_dimensional_ledger: list[dict[str, object]] = []
    for rotation_sign in (1, -1):
        for reflection_sign in (1, -1):
            representatives = [
                sp.Matrix([[rotation_sign]]),
                sp.Matrix([[rotation_sign]]),
                sp.Matrix([[reflection_sign]]),
                sp.Matrix([[reflection_sign]]),
            ]
            determinant = sp.factor(
                (sp.eye(4) - block_nonbacktracking(representatives, [u] * 4)).det()
            )
            one_dimensional.append(determinant)
            one_dimensional_ledger.append(
                {
                    "rho_r": rotation_sign,
                    "rho_s": reflection_sign,
                    "determinant": str(determinant),
                }
            )

    artin_product = sp.factor(sp.prod(one_dimensional) * unit_two**2)
    cover = d4_regular_cover_matrix(u)
    cover_determinant = sp.factor((sp.eye(32) - cover).det(method="domain-ge"))
    if sp.expand(cover_determinant - artin_product) != 0:
        raise AssertionError("D4 Artin factorization failed")

    exact_roots = sp.roots(unit_two, u)
    if sum(exact_roots.values()) != sp.degree(unit_two, u):
        raise AssertionError("exact unit-roof root ledger is incomplete")
    root_angles: list[float] = []
    for root, multiplicity in exact_roots.items():
        angle = cmath.phase(complex(sp.N(root, 40)))
        root_angles.extend([angle] * multiplicity)
    root_angles.sort()

    return {
        "directed_edges": ["a", "A", "b", "B"],
        "two_dimensional_weighted_determinant": str(bivariate),
        "two_dimensional_unit_roof_determinant": str(unit_two),
        "one_dimensional_factors": one_dimensional_ledger,
        "regular_cover_determinant": str(cover_determinant),
        "artin_product": str(artin_product),
        "factorization_exact": True,
        "unit_roof_degree": int(sp.degree(unit_two, u)),
        "unit_roof_root_arguments": root_angles,
    }


def heisenberg_multiply(
    left: tuple[int, int, int], right: tuple[int, int, int], prime: int
) -> tuple[int, int, int]:
    """Multiply coordinates in H(F_p), with c-coordinate c+c'+a b'."""

    a, b, c = left
    aa, bb, cc = right
    return ((a + aa) % prime, (b + bb) % prime, (c + cc + a * bb) % prime)


def heisenberg_holonomy(word: str, prime: int) -> tuple[int, int, int]:
    generators = {
        "x": (1, 0, 0),
        "X": (-1 % prime, 0, 0),
        "y": (0, 1, 0),
        "Y": (0, -1 % prime, 0),
    }
    result = (0, 0, 0)
    for letter in word:
        result = heisenberg_multiply(result, generators[letter], prime)
    return result


def group_order(element: tuple[int, int, int], prime: int) -> int:
    product = (0, 0, 0)
    for exponent in range(1, prime**3 + 1):
        product = heisenberg_multiply(product, element, prime)
        if product == (0, 0, 0):
            return exponent
    raise AssertionError("finite group order search failed")


def cyclically_reduced(word: str) -> bool:
    inverse = {"x": "X", "X": "x", "y": "Y", "Y": "y"}
    return all(inverse[word[index]] != word[(index + 1) % len(word)] for index in range(len(word)))


def primitive_word(word: str) -> bool:
    """Test primitivity as a cyclic word via its based periods."""

    length = len(word)
    return all(
        word != word[:period] * (length // period)
        for period in range(1, length)
        if length % period == 0
    )


def cyclic_rotations(word: str) -> set[str]:
    return {word[index:] + word[:index] for index in range(len(word))}


def inverse_word(word: str) -> str:
    inverse = {"x": "X", "X": "x", "y": "Y", "Y": "y"}
    return "".join(inverse[letter] for letter in reversed(word))


def dihedrally_equivalent(left: str, right: str) -> bool:
    return right in cyclic_rotations(left) | cyclic_rotations(inverse_word(left))


def parikh(word: str) -> dict[str, int]:
    return {letter: word.count(letter) for letter in ("x", "X", "y", "Y")}


def cyclic_bigram_counts(word: str) -> dict[str, int]:
    alphabet = ("x", "X", "y", "Y")
    return {
        left + right: sum(
            1
            for index in range(len(word))
            if word[index] == left and word[(index + 1) % len(word)] == right
        )
        for left in alphabet
        for right in alphabet
    }


def heisenberg_certificates(prime: int) -> dict[str, object]:
    if prime < 7 or not sp.isprime(prime):
        raise ValueError("the upgraded Heisenberg witness requires a prime p >= 7")

    # These witnesses agree even in their cyclic directed-bigram ledger.  At
    # p=7 their holonomies z^3 and z^2 are neither equal nor inverses.
    words = ("XXXyxxyxYY", "XXXyxyxxYY")
    holonomies = [heisenberg_holonomy(word, prime) for word in words]
    orders = [group_order(element, prime) for element in holonomies]
    if not all(cyclically_reduced(word) for word in words):
        raise AssertionError("Heisenberg witnesses must be cyclically reduced")
    if not all(primitive_word(word) for word in words):
        raise AssertionError("Heisenberg witnesses must be primitive")
    if dihedrally_equivalent(*words):
        raise AssertionError("Heisenberg witnesses must not be cyclic or time-reversal copies")
    if parikh(words[0]) != parikh(words[1]):
        raise AssertionError("Heisenberg witnesses lost equal Parikh data")
    if cyclic_bigram_counts(words[0]) != cyclic_bigram_counts(words[1]):
        raise AssertionError("Heisenberg witnesses lost equal cyclic bigram data")
    if holonomies[0] == holonomies[1]:
        raise AssertionError("Heisenberg holonomies should be distinct")
    if holonomies[0][2] == (-holonomies[1][2]) % prime:
        raise AssertionError("Heisenberg holonomies should not be inverse central elements")
    if orders != [prime, prime]:
        raise AssertionError("central witnesses should both have order p")

    variable = sp.symbols("q")
    group_size = prime**3
    lifted_cycle_count = group_size // prime
    regular_inverse_factor = sp.expand((1 - variable**prime) ** lifted_cycle_count)
    nontrivial_inverse_factor = sp.cancel(regular_inverse_factor / (1 - variable))

    # In the p-dimensional Schrodinger sector k, the two central holonomies
    # act by distinct p-th root phases.  Recording exponents is exact and
    # avoids floating-point cyclotomic arithmetic.
    resolved_phase_exponents = {
        words[index]: {
            str(k): (-k * holonomies[index][2]) % prime for k in range(1, prime)
        }
        for index in range(2)
    }

    return {
        "prime": prime,
        "group_size": group_size,
        "words": list(words),
        "cyclically_reduced": [cyclically_reduced(word) for word in words],
        "primitive": [primitive_word(word) for word in words],
        "dihedrally_equivalent": dihedrally_equivalent(*words),
        "directed_parikh": parikh(words[0]),
        "cyclic_directed_bigram_counts": cyclic_bigram_counts(words[0]),
        "holonomies": [list(element) for element in holonomies],
        "holonomy_orders": orders,
        "distinct_central_conjugacy_classes": True,
        "regular_inverse_local_factor": str(sp.factor(regular_inverse_factor)),
        "nontrivial_inverse_local_factor": str(sp.factor(nontrivial_inverse_factor)),
        "aggregated_factors_equal": True,
        "resolved_central_phase_exponents_mod_p": resolved_phase_exponents,
        "resolved_sectors_distinguish": resolved_phase_exponents[words[0]]
        != resolved_phase_exponents[words[1]],
    }


def rational_schrodinger_certificate_q243() -> dict[str, object]:
    """Return the exact rational Rayleigh certificate at q=243 and L=15."""

    modulus = 243
    window_radius = 15
    window_size = 2 * window_radius + 1
    shift_term = Fraction(2 * (window_size - 1), window_size)
    phase_term_lower_bound = Fraction(2) - Fraction(1000, 6561)
    lower_bound = shift_term + phase_term_lower_bound
    threshold = Fraction(7, 2)
    excess = lower_bound - threshold

    if lower_bound != Fraction(769442, 203391):
        raise AssertionError("q=243 rational Rayleigh fraction changed")
    if excess != Fraction(115147, 406782) or excess <= 0:
        raise AssertionError("q=243 rational Rayleigh bound must exceed 7/2")
    if threshold * threshold <= 12:
        raise AssertionError("7/2 must exceed the positive Ramanujan bound 2*sqrt(3)")

    return {
        "modulus": modulus,
        "window_radius": window_radius,
        "window_size": window_size,
        "cosine_inequalities": "cos(x)>=1-x^2/2 and pi^2<10",
        "shift_term_fraction": str(shift_term),
        "phase_term_lower_bound_fraction": str(phase_term_lower_bound),
        "rayleigh_lower_bound_expression": "60/31 + 2 - 1000/6561",
        "rayleigh_lower_bound_fraction": str(lower_bound),
        "excess_over_7_over_2_fraction": str(excess),
        "exceeds_7_over_2": True,
        "seven_over_two_exceeds_2_sqrt_3": True,
        "ramanujan_comparison": "(7/2)^2=49/4>12=(2*sqrt(3))^2",
    }


def heisenberg_tower_certificates(prime: int = 3, max_level: int = 6) -> dict[str, object]:
    """Exact-formula pilot for conductor-new characters in H(Z/p^m)."""

    if prime < 3 or not sp.isprime(prime):
        raise ValueError("an odd prime is required")
    if max_level < 1:
        raise ValueError("max_level must be positive")

    degree = 4
    branching = degree - 1
    ramanujan_bound = 2.0 * math.sqrt(branching)
    rows: list[dict[str, object]] = []
    for level in range(1, max_level + 1):
        modulus = prime**level
        eigenvalue = 2.0 + 2.0 * math.cos(2.0 * math.pi / modulus)
        discriminant = eigenvalue * eigenvalue - 4.0 * branching
        if discriminant >= 0.0:
            square_root = math.sqrt(discriminant)
            abelian_bass_roots = [
                (eigenvalue - square_root) / (2.0 * branching),
                (eigenvalue + square_root) / (2.0 * branching),
            ]
        else:
            real_part = eigenvalue / (2.0 * branching)
            imaginary_part = math.sqrt(-discriminant) / (2.0 * branching)
            abelian_bass_roots = [
                {"real": real_part, "imag": -imaginary_part},
                {"real": real_part, "imag": imaginary_part},
            ]
        # Primitive Schrodinger sector: U+U*+V+V*.  On the normalized
        # indicator of {-L,...,L}, its Rayleigh quotient is bounded below by
        # 2(1-1/(2L+1))+2 cos(2*pi*L/modulus).  The central frequency is one,
        # hence this sector also has exact conductor p^m.
        window_radius = math.isqrt(modulus)
        if 2 * window_radius + 1 >= modulus:
            window_radius = 0
        window_size = 2 * window_radius + 1
        schrodinger_lower_bound = (
            2.0 * (1.0 - 1.0 / window_size)
            + 2.0 * math.cos(2.0 * math.pi * window_radius / modulus)
        )

        rows.append(
            {
                "level": level,
                "modulus": modulus,
                "character_frequency_a": 1,
                "factors_through_previous_level": False,
                "adjacency_eigenvalue": eigenvalue,
                "ramanujan_bound": ramanujan_bound,
                "violates_ramanujan_bound": eigenvalue > ramanujan_bound,
                "abelian_bass_roots": abelian_bass_roots,
                "schrodinger_central_frequency": 1,
                "schrodinger_dimension": modulus,
                "schrodinger_factors_through_previous_level": False,
                "schrodinger_trial_window_radius": window_radius,
                "schrodinger_rayleigh_lower_bound": schrodinger_lower_bound,
                "schrodinger_bound_violates_ramanujan": schrodinger_lower_bound
                > ramanujan_bound,
            }
        )

    result: dict[str, object] = {
        "tower": "Cay(H(Z/p^m), x^{+/-1}, y^{+/-1})",
        "prime": prime,
        "degree": degree,
        "branching_q": branching,
        "new_character": "chi_m(x)=exp(2*pi*i/p^m), chi_m(y)=1",
        "eigenvalue_formula": "lambda_m=2+2*cos(2*pi/p^m)",
        "newness_reason": "frequency 1 is not divisible by p, so chi_m does not factor through level m-1",
        "limit_eigenvalue": 4,
        "limit_bass_roots": [1 / 3, 1],
        "primitive_schrodinger_block": "H_m=U_m+U_m^*+V_m+V_m^*, with U_m V_m=exp(-2*pi*i/p^m)V_m U_m",
        "schrodinger_limit_proof": "the recorded finite-window Rayleigh lower bound tends to 4, while ||H_m||<=4",
        "sector_boundary": "the 1D row kills trivial-only subtraction; the primitive Schrodinger row also survives deletion of every abelian sector",
        "rows": rows,
    }
    if prime == 3 and max_level >= 5:
        result["rational_schrodinger_certificate_q243"] = (
            rational_schrodinger_certificate_q243()
        )
    return result


def positive_unit_roof_zero_count(root_angles: Iterable[float], height: float) -> int:
    """Count unit-roof zeros with 0 < Im(s) <= height, including multiplicity."""

    count = 0
    two_pi = 2.0 * math.pi
    for angle in root_angles:
        # e^{-s}=u gives Im(s)=-(arg(u)+2*pi*k).
        lower = (-height - angle) / two_pi
        upper = (-angle) / two_pi
        first = math.ceil(lower - 1e-12)
        last = math.ceil(upper - 1e-12) - 1
        if last >= first:
            count += last - first + 1
    return count


def density_table(root_angles: list[float]) -> list[dict[str, float | int]]:
    rows: list[dict[str, float | int]] = []
    for height in (100.0, 1_000.0, 10_000.0, 100_000.0, 1_000_000.0):
        graph_count = positive_unit_roof_zero_count(root_angles, height)
        rvm_main = height / (2.0 * math.pi) * (
            math.log(height / (2.0 * math.pi)) - 1.0
        ) + 0.875
        rows.append(
            {
                "T": int(height),
                "twisted_unit_roof_count": graph_count,
                "twisted_count_over_T": graph_count / height,
                "riemann_von_mangoldt_main": rvm_main,
                "rvm_main_over_T": rvm_main / height,
            }
        )
    return rows


def write_outputs(output_directory: Path, payload: dict[str, object]) -> None:
    output_directory.mkdir(parents=True, exist_ok=True)
    json_path = output_directory / "exact_certificates.json"
    json_path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    rows = payload["unit_roof_density_illustration"]
    csv_lines = [
        "T,twisted_unit_roof_count,twisted_count_over_T,riemann_von_mangoldt_main,rvm_main_over_T"
    ]
    for row in rows:  # type: ignore[assignment]
        csv_lines.append(
            f"{row['T']},{row['twisted_unit_roof_count']},"
            f"{row['twisted_count_over_T']:.12g},"
            f"{row['riemann_von_mangoldt_main']:.12g},"
            f"{row['rvm_main_over_T']:.12g}"
        )
    (output_directory / "unit_roof_density.csv").write_text(
        "\n".join(csv_lines) + "\n", encoding="utf-8"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prime", type=int, default=7)
    parser.add_argument("--output", type=Path, default=Path("results"))
    arguments = parser.parse_args()

    d4 = d4_certificates()
    heisenberg = heisenberg_certificates(arguments.prime)
    payload: dict[str, object] = {
        "candidate": "HCS-C15",
        "scope": "finite base, finite-dimensional unitary twist, finite positive roof alphabet",
        "d4_artin_factorization": d4,
        "heisenberg_order_collapse": heisenberg,
        "heisenberg_congruence_tower": heisenberg_tower_certificates(),
        "unit_roof_density_illustration": density_table(
            d4["unit_roof_root_arguments"]  # type: ignore[arg-type]
        ),
        "claim_boundary": (
            "The exact computations certify chronology and finite Artin factorization. "
            "The O(T) zero bound is proved analytically, not inferred from this table."
        ),
    }
    write_outputs(arguments.output, payload)
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
