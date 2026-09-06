#!/usr/bin/env python3
"""Bounded exact diagnostics for WILD_CUBIC_PROOF.md; stdout only.

These are consistency tests, not substitutes for the all-level proof.
No old batch or field-specialization census is run. GAP checks heights
1,2,3 only; the largest orbit enumerated has 2187 elements.
"""

from __future__ import annotations

import json
import subprocess
from fractions import Fraction
from math import prod

import sympy as sp


def rank_mod(rows: list[list[int]], p: int) -> int:
    mat = [[v % p for v in row] for row in rows]
    rank = 0
    for col in range(len(mat[0])):
        pivot = next((j for j in range(rank, len(mat)) if mat[j][col]), None)
        if pivot is None:
            continue
        mat[rank], mat[pivot] = mat[pivot], mat[rank]
        inv = pow(mat[rank][col], -1, p)
        mat[rank] = [(v * inv) % p for v in mat[rank]]
        for j in range(len(mat)):
            if j != rank and mat[j][col]:
                factor = mat[j][col]
                mat[j] = [(u - factor * v) % p for u, v in zip(mat[j], mat[rank])]
        rank += 1
        if rank == len(mat):
            break
    return rank


def symbolic_checks() -> dict:
    x, z, a, t = sp.symbols("x z a t")
    f = lambda v: v**3 + a * v**2
    roots = [a * (z**2 - 1), a * (z**2 + z), a * (z**2 - z)]
    target = a**3 * (z**3 - z) ** 2
    for root in roots:
        assert sp.Poly(sp.expand(f(root) - target), z, a, modulus=3).is_zero
    assert sp.Poly(sp.expand(prod(roots) - target), z, a, modulus=3).is_zero
    disc = sp.discriminant(f(x) - t, x)
    assert sp.Poly(disc - a**3 * t, a, t, modulus=3).is_zero
    iterates = []
    current = sp.Poly(x, x, modulus=3)
    for n in range(1, 6):
        current = current**3 + current**2
        orders = sorted(monom[0] for monom, coeff in current.terms() if coeff)
        assert orders[0] == 2**n
        assert current.degree() == 3**n
        derivative = current.diff()
        assert derivative.degree() == (3**n - 1) // 2
        iterates.append({"n": n, "degree": current.degree(), "zero_order": orders[0],
                         "derivative_degree": derivative.degree()})

    # At the four infinity points of the height-one biquadratic cover,
    # principal parts are u/a, v/a, uv/(a(z+1)), up to a common local unit.
    pole_matrix = [[s, r, s * r] for s in (1, -1) for r in (1, -1)]
    assert rank_mod(pole_matrix, 3) == 3
    assert all(rank_mod([row], 3) == 1 for row in pole_matrix)
    # Sibling root-square relations at height one: each nonzero root
    # class has two of the three zero-place valuations odd.
    square_matrix = [[1, 1, 0], [1, 0, 1], [0, 1, 1]]
    assert rank_mod(square_matrix, 2) == 2
    level_two_degree = 6 * 2**2 * 3**3
    assert level_two_degree == 648
    return {"normal_form_three_roots": True, "discriminant_exact_constant": True,
            "iterates_a1": iterates, "height_one_square_rank": 2,
            "height_one_global_as_pole_rank": 3,
            "height_one_each_local_as_pole_rank": 1,
            "level_two_field_degree_from_ranks": level_two_degree}


def compose(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(p[j] for j in q)


def parity(p: tuple[int, ...]) -> int:
    return sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) % 2


def group_generators(n: int) -> list[tuple[int, ...]]:
    if n == 1:
        return [(1, 0, 2), (1, 2, 0)]
    size = 3**n
    branch = size // 3
    identity = tuple(range(size))
    top_swap = tuple(j + branch if j < branch else j - branch if j < 2 * branch else j
                     for j in range(size))
    top_cycle = tuple((j + branch) % size for j in range(size))
    wreath = [top_swap, top_cycle]
    for block in range(3):
        for g in group_generators(n - 1):
            perm = list(identity)
            for j in range(branch):
                perm[block * branch + j] = block * branch + g[j]
            wreath.append(tuple(perm))
    result = set()
    chunk = 3 ** (n - 2)
    for g in wreath:
        action_at_depth_two = tuple(g[j * chunk] // chunk for j in range(9))
        if parity(action_at_depth_two):
            result.add(compose(g, top_swap))
            result.add(compose(top_swap, g))
        else:
            result.add(g)
            result.add(compose(top_swap, compose(g, top_swap)))
    result.discard(identity)
    return sorted(result)


def gap_checks() -> dict:
    commands = ["SetInfoLevel(InfoWarning,0);;"]
    expected = []
    for n in (1, 2, 3):
        size = 3**n
        generators = group_generators(n)
        expressions = ["PermList(" + str([j + 1 for j in g]) + ")" for g in generators]
        commands.append("g := Group([" + ",".join(expressions) + "]);;")
        support = [j + 1 for j in range(size)
                   if all((j // 3**k) % 3 != 2 for k in range(n))]
        commands.append("orb := Orbit(g," + str(support) + ",OnSets);;")
        commands.append("rows := List(orb,s -> List([1.." + str(size)
                        + "],i -> (0*Z(2)) + Z(2)*Number(s,j -> j=i)));;")
        commands.append('Print("CHECK ",' + str(n)
                        + '," ",Size(g)," ",Length(orb)," ",RankMat(rows),"\\n");;')
        expected.append((n, 2 ** (3 ** (n - 1)) * 3 ** ((3**n - 1) // 2),
                         3 ** (2**n - 1), 2 * 3 ** (n - 1)))
    commands.append("QUIT;")
    proc = subprocess.run(["gap", "-q", "-b"], input="\n".join(commands), text=True,
                          capture_output=True, timeout=45, check=True)
    assert not proc.stderr.strip(), proc.stderr
    actual = [tuple(map(int, row.split()[1:])) for row in proc.stdout.splitlines()
              if row.startswith("CHECK ")]
    assert actual == expected, (actual, expected, proc.stdout)
    return {"engine": "GAP", "heights": [
        {"n": n, "order": order, "zero_support_orbit": orbit, "valuation_span_rank": rank}
        for n, order, orbit, rank in actual]}


def genus_checks() -> list[dict]:
    result = []
    for n in range(1, 6):
        order = 2 ** (3 ** (n - 1)) * 3 ** ((3**n - 1) // 2)
        e0, einf = 2**n, 2 * 3**n
        d0, dinf = e0 - 1, 3 ** (n + 1) - 2
        rh = order * (-2 + Fraction(d0, e0) + Fraction(dinf, einf))
        genus = 1 + rh / 2
        assert genus.denominator == 1 and genus >= 0
        assert genus == 1 + Fraction(order, 2) * (Fraction(1, 2)
                        - Fraction(1, 2**n) - Fraction(1, 3**n))
        result.append({"n": n, "group_order": order, "e0": e0, "d0": d0,
                       "e_infinity": einf, "d_infinity": dinf, "genus": int(genus)})
    assert result[0]["genus"] == 0 and result[1]["genus"] == 46
    return result


def main() -> None:
    payload = {"symbolic": symbolic_checks(), "groups": gap_checks(),
               "genus_consistency": genus_checks(),
               "boundaries": {"a_zero_excluded": True, "p_gt_3_not_tested": True,
                              "finite_tests_are_not_all_level_proof": True,
                              "group_engine_does_not_compute_function_field_galois_group": True}}
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
