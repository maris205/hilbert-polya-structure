#!/usr/bin/env python3
"""Producer-independent checker for the HCS-C209 evidence ledger.

The checker intentionally reimplements the formulas and, for n<=8, builds
NC(n) and K from set partitions.  It never imports the producer.
"""
from __future__ import annotations

from collections import Counter
from copy import deepcopy
from hashlib import sha256
import json
from math import comb, gcd
import os
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c209_kreweras_evidence.json"
EXPECTED_COMMIT = "e8054522273dbd545f9d406978e5d4648c627918"
EXPECTED_EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
DIRECT_MAX = 8


def canon(blocks: list[list[int]] | list[tuple[int, ...]]) -> tuple[tuple[int, ...], ...]:
    return tuple(sorted(tuple(sorted(block)) for block in blocks))


def all_partitions(n: int) -> list[tuple[tuple[int, ...], ...]]:
    if n == 0:
        return [tuple()]
    labels = [0]
    answer: list[tuple[tuple[int, ...], ...]] = []

    def visit(index: int, maximum: int) -> None:
        if index == n:
            blocks: list[list[int]] = [[] for _ in range(maximum + 1)]
            for vertex, label in enumerate(labels):
                blocks[label].append(vertex)
            answer.append(canon(blocks))
            return
        for label in range(maximum + 2):
            labels.append(label)
            visit(index + 1, max(maximum, label))
            labels.pop()

    visit(1, 0)
    return answer


def is_noncrossing(partition: tuple[tuple[int, ...], ...]) -> bool:
    # A crossing is a<b<c<d with a,c in one block and b,d in another.
    for left_index, left in enumerate(partition):
        for right in partition[left_index + 1 :]:
            for a_index in range(len(left)):
                for c_index in range(a_index + 1, len(left)):
                    a, c = left[a_index], left[c_index]
                    for b_index in range(len(right)):
                        for d_index in range(b_index + 1, len(right)):
                            b, d = right[b_index], right[d_index]
                            if a < b < c < d or b < a < d < c:
                                return False
    return True


def nc_set(n: int) -> list[tuple[tuple[int, ...], ...]]:
    return [p for p in all_partitions(n) if is_noncrossing(p)]


def inverse(permutation: tuple[int, ...]) -> tuple[int, ...]:
    result = [0] * len(permutation)
    for source, target in enumerate(permutation):
        result[target] = source
    return tuple(result)


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[index]] for index in range(len(left)))


def block_permutation(partition: tuple[tuple[int, ...], ...], n: int) -> tuple[int, ...]:
    result = list(range(n))
    for block in partition:
        for index, vertex in enumerate(block):
            result[vertex] = block[(index + 1) % len(block)]
    return tuple(result)


def cycles(permutation: tuple[int, ...]) -> tuple[tuple[int, ...], ...]:
    seen: set[int] = set()
    blocks: list[list[int]] = []
    for start in range(len(permutation)):
        if start in seen:
            continue
        block: list[int] = []
        vertex = start
        while vertex not in seen:
            seen.add(vertex)
            block.append(vertex)
            vertex = permutation[vertex]
        blocks.append(block)
    return canon(blocks)


def kreweras(partition: tuple[tuple[int, ...], ...], n: int) -> tuple[tuple[int, ...], ...]:
    cycle = tuple((index + 1) % n for index in range(n))
    return cycles(compose(inverse(block_permutation(partition, n)), cycle))


def relabel(partition: tuple[tuple[int, ...], ...], n: int, offset: int, reflection: bool = False) -> tuple[tuple[int, ...], ...]:
    if reflection:
        return canon([[(offset - vertex) % n for vertex in block] for block in partition])
    return canon([[(vertex + offset) % n for vertex in block] for block in partition])


def clock_order(n: int) -> int:
    return 1 if n == 1 else 2 if n == 2 else 2 * n


def csp_group_order(n: int) -> int:
    return 1 if n == 1 else 2 * n


def catalan(n: int) -> int:
    return comb(2 * n, n) // (n + 1)


def fixed_formula(n: int, iterate: int) -> int:
    period = clock_order(n)
    d = iterate % period
    if n == 1:
        return 1
    if d % 2 == 0:
        half = (d // 2) % n
        return catalan(n) if half == 0 else comb(2 * gcd(n, half), gcd(n, half))
    return comb(n, (n - 1) // 2) if n % 2 and d == n else 0


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def mu(n: int) -> int:
    result = 1
    p = 2
    value = n
    while p * p <= value:
        if value % p == 0:
            value //= p
            result = -result
            if value % p == 0:
                return 0
            while value % p == 0:
                value //= p
        p += 1
    if value > 1:
        result = -result
    return result


def canonical_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def trim(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def multiply(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            result[i + j] += a * b
    return trim(result)


def divide_exact(numerator: list[int], denominator: list[int]) -> list[int]:
    work = trim(numerator[:])
    denominator = trim(denominator[:])
    quotient = [0] * max(1, len(work) - len(denominator) + 1)
    while work != [0] and len(work) >= len(denominator):
        shift = len(work) - len(denominator)
        lead = work[-1] // denominator[-1]
        quotient[shift] += lead
        for i, value in enumerate(denominator):
            work[i + shift] -= lead * value
        trim(work)
    if any(work):
        raise AssertionError("q-polynomial division remainder")
    return trim(quotient)


def qfactorial(n: int) -> list[int]:
    result = [1]
    for j in range(1, n + 1):
        result = multiply(result, [1] * j)
    return result


def q_catalan(n: int) -> list[int]:
    if n == 1:
        return [1]
    return divide_exact(qfactorial(2 * n), multiply(qfactorial(n), qfactorial(n + 1)))


def polynomial_remainder(numerator: list[int], denominator: list[int]) -> list[int]:
    work = trim(numerator[:])
    denominator = trim(denominator[:])
    while len(work) >= len(denominator):
        shift = len(work) - len(denominator)
        lead = work[-1] // denominator[-1]
        for i, value in enumerate(denominator):
            work[i + shift] -= lead * value
        trim(work)
    return trim(work)


_phi_cache: dict[int, list[int]] = {}


def cyclotomic(order: int) -> list[int]:
    if order in _phi_cache:
        return _phi_cache[order][:]
    polynomial = [-1] + [0] * (order - 1) + [1]
    for divisor in divisors(order):
        if divisor < order:
            polynomial = divide_exact(polynomial, cyclotomic(divisor))
    _phi_cache[order] = polynomial
    return polynomial[:]


def root_value(coefficients: list[int], order: int) -> int:
    if order == 1:
        return sum(coefficients)
    residue = polynomial_remainder(coefficients, cyclotomic(order))
    if len(residue) != 1:
        raise AssertionError(f"nonconstant primitive-root residue at order {order}")
    return residue[0]


def check_direct(n: int, data: dict) -> int:
    partitions = nc_set(n)
    expected_size = catalan(n)
    assert len(partitions) == expected_size
    index = {partition: i for i, partition in enumerate(partitions)}
    images = [kreweras(partition, n) for partition in partitions]
    assert all(image in index for image in images)
    permutation = [index[image] for image in images]
    assertions = 1
    # K^2 is the chosen clockwise (-1) rotation, and every reflection is a
    # reversor.  Checking all j catches orientation mistakes.
    for i, partition in enumerate(partitions):
        assert kreweras(kreweras(partition, n), n) == relabel(partition, n, -1)
        assert len(kreweras(partition, n)) + len(partition) == n + 1
        for j in range(n):
            reflected = relabel(partition, n, j, reflection=True)
            # Explicitly evaluate R_j K R_j and compare with K^{-1} by powers.
            right = partition
            for _ in range(clock_order(n) - 1):
                right = kreweras(right, n)
            left = relabel(kreweras(reflected, n), n, j, reflection=True)
            assert left == right
        assertions += 1
    # Fixed rows and cycle populations from the actual finite map.
    for d in range(clock_order(n)):
        actual = sum(1 for i in range(len(partitions)) if (lambda j: j == i)(iterate_index(permutation, i, d)))
        row = next(r for r in data["finite_replay"]["fixed_rows"] if r["n"] == n and r["iterate"] == d)
        assert actual == row["fixed_count"] == fixed_formula(n, d)
        assertions += 1
    cycle_lengths = Counter()
    seen: set[int] = set()
    for start in range(len(partitions)):
        if start in seen:
            continue
        vertex = start
        length = 0
        while vertex not in seen:
            seen.add(vertex)
            length += 1
            vertex = permutation[vertex]
        cycle_lengths[length] += 1
    periods = {ell: 0 for ell in divisors(clock_order(n))}
    for length, count in cycle_lengths.items():
        periods[length] = count * length
    for ell, population in periods.items():
        row = next(r for r in data["finite_replay"]["period_rows"] if r["n"] == n and r["period"] == ell)
        assert row["exact_period_population"] == population
    return assertions


def iterate_index(permutation: list[int], start: int, exponent: int) -> int:
    vertex = start
    for _ in range(exponent):
        vertex = permutation[vertex]
    return vertex


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    data = json.loads(path.read_text())
    assertions = 0
    assert data["schema"] == "HCS-C209-v1"
    assert data["candidate_id"] == "HCS-C209"
    assert data["source_commit"] == EXPECTED_COMMIT
    assert data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER"
    assert data["evaluator"]["version"] == "0.2.0"
    assert data["evaluator"]["sha256"] == EXPECTED_EVALUATOR
    assert data["route_a"]["tuple"] == ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"]
    assert data["route_a"]["overall"] == "ROUTE_A_REJECTED"
    assert data["route_a"]["route_b_invocation_allowed"] is False
    assert all(value is False for key, value in data["scope_flags"].items() if key != "claimed_exact_order_n_uniformly")
    assert data["scope_flags"]["claimed_exact_order_n_uniformly"] is False
    assert data["payload_sha256"] == canonical_hash(data)
    expected_source_lock = {
        "object": "ordinary noncrossing partitions NC(n) of a labelled n-gon",
        "family": "all integers n>=1",
        "phase_space": "the finite Catalan set NC(n), with refinement rank n minus number of blocks",
        "clock": "one application of K(pi)=cycles(p_pi^{-1} c), where c=(0 1 ... n-1) and p_pi cycles each block in increasing circular order; K^2 is relabelling i -> i-1",
        "measure": "counting measure on NC(n)",
        "operator": "finite Koopman permutation U_n f=f composed with K on ell2(NC(n))",
        "polynomial": "Cat_n(q)=[2n]_q!/[n]_q![n+1]_q!, the unshifted q-Catalan polynomial",
        "determinant_convention": "finite Artin--Mazur zeta of K and reciprocal finite Koopman determinant",
        "cutoff": "all-n source theorem; exact formula rows n<=24, q-polynomial rows n<=12, direct partition enumeration n<=8",
        "allowed_data": "set-partition incidences, Catalan/Narayana integers, binomial coefficients, roots of unity and finite permutation cycles",
        "forbidden_data": "target zero or prime tables, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya operators, target divisors, and Route-B inputs",
    }
    assert data["source_lock"] == expected_source_lock
    expected_theorem = {
        "cardinality": "|NC(n)|=Cat_n=binom(2n,n)/(n+1)",
        "complement_definition": "K(pi) is the cycle partition of p_pi^{-1}c; K reverses refinement and blocks(K(pi))=n+1-blocks(pi)",
        "square": "K^2=rotation by -1; hence K commutes with rotation",
        "clock_order": "order(K)=1 for n=1, 2 for n=2, and 2n for every n>=3",
        "fixed_count": "For n>=2 and d modulo L_n (L_2=2, L_n=2n for n>=3): even d=2r gives Cat_n if r=0 and binom(2g,g) if g=gcd(n,r)>0; odd d gives binom(n,(n-1)/2) exactly when n is odd and d=n, otherwise 0",
        "csp": "Fix(K^d)=Cat_n(zeta_{2n}^d) under the ordinary type-A Kreweras CSP, with the n=1,2 action kernels treated separately",
        "exact_period": "P_{n,ell}=sum_{d|ell} mu(ell/d) Fix(K^d), ell|L_n",
        "cycle_count": "C_{n,ell}=P_{n,ell}/ell and sum_ell P_{n,ell}=Cat_n",
        "zeta": "zeta_{K,n}(z)=product_{ell|L_n}(1-z^ell)^(-C_{n,ell})",
        "koopman_determinant": "det(I-zU_n)=product_{ell|L_n}(1-z^ell)^(C_{n,ell})=zeta_{K,n}(z)^(-1)",
        "spectrum": "Spec(U_n) consists of L_n-th roots; mult(exp(2pi i k/L_n))=sum_{ell|L_n, L_n|k ell} C_{n,ell}, and Tr(U_n^d)=Fix(K^d)",
        "reversor": "polygon reflection R_j(i)=j-i satisfies R_j K R_j=K^{-1}; Jf=conjugate(f composed with R_j) is an antiunitary reversor",
        "rank_duality": "rank(K(pi))=n-1-rank(pi), with Narayana rank counts N(n,b)=binom(n,b)binom(n,b-1)/n",
    }
    assert data["theorem"] == expected_theorem
    assert data["attribution"]["status"] == "SOURCE_DERIVED_SYNTHESIS_NOT_NEW_THEOREM_CLAIM"
    assert data["attribution"]["nc_owner"].startswith("Kreweras 1972")
    assert data["attribution"]["rotation_csp_owner"].startswith("Reiner--Stanton--White 2004")
    assert data["attribution"]["kreweras_csp_owner"].startswith("The type-A order-2n")
    expected_sources = [
        {
            "key": "kreweras_1972",
            "title": "Sur les partitions non croisées d'un cycle",
            "authors": "Germain Kreweras",
            "year": 1972,
            "journal": "Discrete Mathematics 1, 333--350",
            "doi": "10.1016/0012-365X(72)90041-6",
            "role": "original ordinary noncrossing-partition and complement source",
        },
        {
            "key": "reiner_stanton_white_2004",
            "title": "The cyclic sieving phenomenon",
            "authors": "Victor Reiner, Dennis Stanton, Dennis White",
            "year": 2004,
            "journal": "Journal of Combinatorial Theory, Series A 108, 17--50",
            "doi": "10.1016/j.jcta.2004.04.009",
            "role": "type-A rotation q-Catalan CSP and root-of-unity fixed-count calculations",
        },
        {
            "key": "bessis_reiner_2011_white_report",
            "title": "Cyclic sieving of noncrossing partitions for complex reflection groups",
            "authors": "David Bessis, Victor Reiner",
            "year": 2011,
            "journal": "Annals of Combinatorics 15(2), 197--222",
            "doi": "10.1007/s00026-011-0090-9",
            "arxiv": "math/0701792 (preprint 2007)",
            "role": "formal publication records the order-2n Kreweras-complement CSP as type-A m=1 and reports White's direct verification; used as attribution, not a novelty claim",
        },
    ]
    assert data["source_registry"] == expected_sources
    assertions += 21

    finite = data["finite_replay"]
    n_rows = finite["n_rows"]
    fixed_rows = finite["fixed_rows"]
    period_rows = finite["period_rows"]
    spectral_rows = finite["spectral_rows"]
    rank_rows = finite["rank_rows"]
    q_rows = finite["q_catalan_rows"]
    structural_rows = finite["structural_rows"]
    assert len(n_rows) == finite["n_row_count"] == 24
    assert len(fixed_rows) == finite["fixed_row_count"] == sum(clock_order(n) for n in range(1, 25))
    assert len(period_rows) == finite["period_row_count"] == sum(len(divisors(clock_order(n))) for n in range(1, 25))
    assert len(spectral_rows) == finite["spectral_row_count"] == len(fixed_rows)
    assert len(rank_rows) == finite["rank_row_count"] == sum(range(1, 25))
    assert len(q_rows) == finite["q_catalan_row_count"] == 12
    assert len(structural_rows) == finite["structural_row_count"] == 24
    assertions += 6

    # Coordinate-level checks prevent a duplicated or shifted row from being
    # hidden by a later lookup in the aggregate ledgers.
    for row in fixed_rows:
        n, d = row["n"], row["iterate"]
        L = clock_order(n)
        assert 0 <= d < L and row["iterate_mod_order"] == d
        assert row["parity"] == ("even" if d % 2 == 0 else "odd")
        expected_gcd = gcd(n, d // 2) if d % 2 == 0 else None
        assert row["gcd_n_half_iterate"] == expected_gcd
        assert row["fixed_count"] == fixed_formula(n, d)
        assertions += 5
    for row in period_rows:
        n, ell = row["n"], row["period"]
        assert ell in divisors(clock_order(n))
        assertions += 1
    for row in spectral_rows:
        n, L, k = row["n"], row["clock_order"], row["root_exponent"]
        assert L == clock_order(n) and 0 <= k < L
        expected_periods = {
            ell: sum(mu(ell // d) * fixed_formula(n, d) for d in divisors(ell))
            for ell in divisors(L)
        }
        expected_mult = sum(expected_periods[ell] // ell for ell in expected_periods if (k * ell) % L == 0)
        assert row["multiplicity"] == expected_mult
        assertions += 2
    for row in rank_rows:
        n, blocks, rank = row["n"], row["blocks"], row["rank"]
        assert 1 <= blocks <= n and rank == n - blocks
        assert row["count"] == comb(n, blocks) * comb(n, blocks - 1) // n
        assertions += 2
    for row in structural_rows:
        n = row["n"]
        assert row["actual_order"] == clock_order(n)
        assert row["csp_group_order"] == csp_group_order(n)
        assert row["square_rotation_offset"] == (0 if n == 1 else -1)
        assert row["rank_reversal"] == "blocks(K(pi))=n+1-blocks(pi)"
        assert row["reflection_relation"] == "R_j K R_j=K^(-1) for j=0,...,n-1"
        assert row["reflection_count"] == n
        assert row["direct_structural_check_selected"] is (n <= DIRECT_MAX)
        expected_boundary = "singleton" if n == 1 else "two_point_kernel" if n == 2 else "generic_2n"
        assert row["boundary"] == expected_boundary
        assertions += 9

    for row in n_rows:
        n = row["n"]
        L = clock_order(n)
        assert row["catalan"] == catalan(n)
        assert row["clock_order"] == L
        assert row["csp_group_order"] == csp_group_order(n)
        assert row["fixed_count_rows"] == L
        assert row["period_divisors"] == divisors(L)
        assert row["direct_enumeration_selected"] is (n <= DIRECT_MAX)
        periods = {}
        for ell in divisors(L):
            exact = sum(mu(ell // d) * fixed_formula(n, d) for d in divisors(ell))
            periods[ell] = exact
            prow = next(r for r in period_rows if r["n"] == n and r["period"] == ell)
            assert prow["fixed_at_period"] == fixed_formula(n, ell)
            assert prow["exact_period_population"] == exact
            assert prow["cycle_count"] == exact // ell
        assert sum(periods.values()) == catalan(n)
        assert row["nonzero_periods"] == [ell for ell in periods if periods[ell]]
        assert row["cycle_ledger"] == [
            {"period": ell, "exact_period_population": periods[ell], "cycles": periods[ell] // ell}
            for ell in periods
        ]
        assert row["zeta_factors"] == [
            {"period": ell, "exponent": -(periods[ell] // ell)}
            for ell in periods if periods[ell]
        ]
        assert row["koopman_determinant_factors"] == [
            {"period": ell, "exponent": periods[ell] // ell}
            for ell in periods if periods[ell]
        ]
        for blocks in range(1, n + 1):
            expected = comb(n, blocks) * comb(n, blocks - 1) // n
            rrow = next(r for r in rank_rows if r["n"] == n and r["blocks"] == blocks)
            assert rrow["rank"] == n - blocks and rrow["count"] == expected
        if n <= 12:
            coeffs = q_catalan(n)
            assert row["q_catalan"]["coefficients"] == coeffs
            assert row["q_catalan"]["csp_group_order"] == csp_group_order(n)
            assert sha256(json.dumps(coeffs, separators=(",", ":")).encode()).hexdigest() == row["q_catalan"]["sha256"]
        assertions += 8 + len(divisors(L)) * 3

    # Independent root-of-unity checks for all q-polynomial rows.
    for qrow in q_rows:
        n = qrow["n"]
        coeffs = qrow["coefficients"]
        assert qrow["degree"] == len(coeffs) - 1
        assert qrow["csp_group_order"] == csp_group_order(n)
        assert qrow["convention"] == "Cat_n(q)=[2n]_q!/[n]_q![n+1]_q!"
        assert qrow["sha256"] == sha256(json.dumps(coeffs, separators=(",", ":")).encode()).hexdigest()
        for d in range(csp_group_order(n)):
            order = csp_group_order(n) // gcd(csp_group_order(n), d)
            assert root_value(coeffs, order) == fixed_formula(n, d)
            assertions += 1

    if not os.environ.get("C209_MUTATION_FAST"):
        for n in range(1, DIRECT_MAX + 1):
            assertions += check_direct(n, data)

    print(json.dumps({
        "status": "C209_CHECK_PASS",
        "assertions": assertions,
        "direct_n_max": DIRECT_MAX,
        "direct_partition_total": sum(catalan(n) for n in range(1, DIRECT_MAX + 1)),
        "payload_sha256": data["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
