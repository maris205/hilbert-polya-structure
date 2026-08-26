#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C187."""
from __future__ import annotations

from collections import Counter, defaultdict
from functools import lru_cache
from hashlib import sha256
import json
from math import factorial, gcd, lcm, prod
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c187_tableau_csp_evidence.json"
EXPECTED_COMMIT = "908a6818caedb0c46195a591873a2ac9c685b55e"
EXPECTED_EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"

EXPECTED_SOURCE_LOCK = {
    "object": "Schuetzenberger jeu-de-taquin promotion j on standard Young tableaux of rectangular shape b^a",
    "family": "all positive integers a,b with N=ab",
    "phase_space": "the finite set SYT(b^a)",
    "clock": "one application of Rhoades's convention: remove N, slide the hole northwest, increment retained entries, and insert 1",
    "measure": "counting probability on SYT(b^a)",
    "operator": "finite Koopman permutation U_ab f=f composed with j on ell2(SYT(b^a))",
    "q_hook_convention": "F_ab(q)=[N]_q!/product_(cells c)[h(c)]_q, exactly the unshifted standard-tableau polynomial in Rhoades Theorem 1.3",
    "determinant_convention": "Artin--Mazur zeta of the finite promotion permutation and the reciprocal finite Koopman determinant",
    "cutoff": "all-rectangle source theorem; exact formula regression uses 1<=a,b<=6 and direct tableau enumeration only on declared small rectangles",
    "allowed_data": "rectangular hook lengths, exact cyclotomic polynomials, source-derived CSP evaluations, and direct small-tableau promotion",
    "forbidden_data": "target zero or prime tables, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya operators, and Route-B inputs",
}

EXPECTED_ATTRIBUTION = {
    "status": "SOURCE_DERIVED_SYNTHESIS_NOT_NEW_THEOREM_CLAIM",
    "all_rectangle_owner": "Rhoades 2010 owns the rectangular standard-tableau CSP and records the promotion order-divides-N theorem and dihedral promotion--evacuation action",
    "order_background": "Haiman 1992 is the classical source cited by Rhoades for the rectangular promotion-order result",
    "package_increment": "source-locked Route-A synthesis of every-iterate fixed counts, Mobius period/cycle recovery, finite zeta, Koopman determinant and spectral multiplicities, with executable regression and stopping boundaries",
    "finite_evidence_role": "finite enumeration and symbolic reconstruction are regression checks only and do not prove the all-rectangle CSP",
}

EXPECTED_THEOREM = {
    "order_bound": "j^N is the identity on SYT(b^a); the actual order divides N and need not equal N",
    "csp_fixed_count": "Fix(j^d)=F_ab(zeta_N^d) for every integer d, where F_ab(q) is the unshifted q-hook polynomial",
    "exact_period": "P_l=sum_(d|l) mu(l/d) Fix(j^d) for every l|N",
    "cycle_count": "C_l=P_l/l",
    "zeta": "zeta_j(z)=product_(l|N)(1-z^l)^(-C_l)",
    "koopman_determinant": "det(I-z U_ab)=product_(l|N)(1-z^l)^(C_l)=zeta_j(z)^(-1)",
    "spectral_multiplicity": "mult(zeta_N^k)=sum_(l|N and N divides k*l) C_l",
    "trace": "Tr(U_ab^d)=Fix(j^d)",
    "reversor": "evacuation e is an involution and e*j*e=j^(-1); e followed by complex conjugation is an antiunitary reversor",
    "identity_boundary": "if a=1 or b=1 then SYT(b^a) is a singleton and j has order one",
}

EXPECTED_BOUNDARY = {
    "progress": "one theorem package closes the all-rectangle fixed ledger, exact periods and cycles, zeta, finite Koopman determinant, spectrum, and evacuation reversal",
    "order_boundary": "j^N=id is uniform, but exact order N is false in general; one-row, one-column, and 2-by-2 rectangles are explicit controls",
    "proof_boundary": "the all-rectangle CSP is imported with attribution; finite rows and enumeration regression-test consequences rather than prove it",
    "arithmetic_boundary": "rectangle dimensions, hook lengths, and cyclotomic roots have no intrinsic rational-prime or prime-power semantics",
    "operator_boundary": "the natural finite unitary is the source Koopman permutation; it has only roots of unity and no target divisor or self-adjoint Hilbert--Polya conclusion",
}

EXPECTED_ROUTE_A = {
    "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
    "overall": "ROUTE_A_REJECTED",
    "A0_qualification": "RECTANGLE_AND_HOOK_DATA_HAVE_NO_INTRINSIC_RATIONAL_PRIME_ORIGIN",
    "A1_qualification": "FINITE_PROMOTION_CYCLES_ARE_COMPLETE_BUT_CARRY_NO_A0_ARITHMETIC_PAYLOAD",
    "A2_qualification": "FINITE_SOURCE_ZETA_AND_KOOPMAN_DETERMINANT_HAVE_NO_TARGET_DIVISOR_MATCH",
    "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_CONTINUATION_OR_WEIL_COMPRESSION",
    "A4_qualification": "SOURCE_NATIVE_FINITE_UNITARY_AND_EVACUATION_ANTIUNITARY_REVERSOR_ONLY",
    "route_b_invocation_allowed": False,
}

EXPECTED_SCOPE_FLAGS = {
    "used_target_zero_table": False,
    "used_target_prime_table": False,
    "used_arithmetic_local_data": False,
    "claimed_target_divisor_match": False,
    "claimed_target_functional_equation": False,
    "claimed_hilbert_polya": False,
    "claimed_exact_order_n_uniformly": False,
    "claimed_global_novelty": False,
    "route_b_invocation_allowed": False,
}

EXPECTED_SOURCE_REGISTRY = [
    {
        "key": "rhoades_2010_rectangular_promotion_csp",
        "title": "Cyclic sieving, promotion, and representation theory",
        "authors": "Brendon Rhoades",
        "year": 2010,
        "journal": "Journal of Combinatorial Theory, Series A 117(1), 38--76",
        "doi": "10.1016/j.jcta.2009.03.017",
        "arxiv": "1005.2568",
        "role": "primary ownership for the unshifted q-hook CSP, order-divides-N corollary, and promotion--evacuation dihedral relation",
    },
    {
        "key": "haiman_1992_dual_equivalence",
        "title": "Dual equivalence with applications, including a conjecture of Proctor",
        "authors": "Mark D. Haiman",
        "year": 1992,
        "journal": "Discrete Mathematics 99, 79--113",
        "doi": "10.1016/0012-365X(92)90368-P",
        "role": "classical promotion-order background cited by Rhoades",
    },
]

EXPECTED_NONCLAIMS = [
    "novelty or priority for the rectangular promotion CSP, q-hook formula, order bound, or evacuation relation",
    "uniform equality between the order of promotion and the number N of boxes",
    "use of finite enumeration as a proof of the all-rectangle theorem",
    "rational-prime semantics for rectangle dimensions, hook lengths, cyclotomic orders, or promotion cycles",
    "a target divisor, functional equation, counting law, continuation, or Weil compression",
    "a self-adjoint Hilbert--Polya operator, Route-B authorization, external peer review, or acceptance score",
]


def canonical_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def divisors(n: int) -> list[int]:
    small, large = [], []
    d = 1
    while d * d <= n:
        if n % d == 0:
            small.append(d)
            if d * d != n:
                large.append(n // d)
        d += 1
    return small + large[::-1]


def mu(n: int) -> int:
    answer = 1
    prime = 2
    value = n
    while prime * prime <= value:
        if value % prime == 0:
            value //= prime
            answer = -answer
            if value % prime == 0:
                return 0
            while value % prime == 0:
                value //= prime
        prime += 1
    if value > 1:
        answer = -answer
    return answer


def clean(poly: list[int]) -> list[int]:
    while len(poly) > 1 and poly[-1] == 0:
        poly.pop()
    return poly


def multiply(left: list[int], right: list[int]) -> list[int]:
    result = [0] * (len(left) + len(right) - 1)
    for i, coefficient in enumerate(left):
        for j, other in enumerate(right):
            result[i + j] += coefficient * other
    return clean(result)


def quotient(numerator: list[int], denominator: list[int]) -> list[int]:
    remainder = clean(numerator[:])
    denominator = clean(denominator[:])
    result = [0] * (len(remainder) - len(denominator) + 1)
    while len(remainder) >= len(denominator):
        shift = len(remainder) - len(denominator)
        coefficient = remainder[-1] // denominator[-1]
        result[shift] += coefficient
        for index, item in enumerate(denominator):
            remainder[index + shift] -= coefficient * item
        clean(remainder)
        if remainder == [0]:
            break
    if any(remainder):
        raise AssertionError("non-exact polynomial quotient")
    return clean(result)


def remainder(numerator: list[int], denominator: list[int]) -> list[int]:
    work = clean(numerator[:])
    denominator = clean(denominator[:])
    while len(work) >= len(denominator):
        shift = len(work) - len(denominator)
        coefficient = work[-1]
        for index, item in enumerate(denominator):
            work[index + shift] -= coefficient * item
        clean(work)
    return clean(work)


def q_integer(n: int) -> list[int]:
    return [1] * n


@lru_cache(maxsize=None)
def q_factorial(n: int) -> tuple[int, ...]:
    result = [1]
    for value in range(1, n + 1):
        result = multiply(result, q_integer(value))
    return tuple(result)


@lru_cache(maxsize=None)
def phi(n: int) -> tuple[int, ...]:
    polynomial = [-1] + [0] * (n - 1) + [1]
    for divisor in divisors(n):
        if divisor < n:
            polynomial = quotient(polynomial, list(phi(divisor)))
    return tuple(polynomial)


def hooks(a: int, b: int) -> list[int]:
    return [a + b - row - column - 1 for row in range(a) for column in range(b)]


def independent_q_hook(a: int, b: int) -> list[int]:
    denominator = [1]
    for hook in hooks(a, b):
        denominator = multiply(denominator, q_integer(hook))
    return quotient(list(q_factorial(a * b)), denominator)


def root_value(coefficients: list[int], order: int) -> int:
    if order == 1:
        return sum(coefficients)
    residue = remainder(coefficients, list(phi(order)))
    if len(residue) != 1:
        raise AssertionError("nonconstant primitive-root residue")
    return residue[0]


def is_standard(tableau: tuple[int, ...], a: int, b: int) -> bool:
    if sorted(tableau) != list(range(1, a * b + 1)):
        return False
    for row in range(a):
        for column in range(b - 1):
            if tableau[row * b + column] >= tableau[row * b + column + 1]:
                return False
    for row in range(a - 1):
        for column in range(b):
            if tableau[row * b + column] >= tableau[(row + 1) * b + column]:
                return False
    return True


def tableaux(a: int, b: int):
    n = a * b
    prerequisites = []
    for row in range(a):
        for column in range(b):
            mask = 0
            if row:
                mask |= 1 << ((row - 1) * b + column)
            if column:
                mask |= 1 << (row * b + column - 1)
            prerequisites.append(mask)
    values = [0] * n

    def visit(label: int, occupied: int):
        if label > n:
            yield tuple(values)
            return
        for cell in range(n):
            bit = 1 << cell
            if occupied & bit:
                continue
            if prerequisites[cell] & occupied != prerequisites[cell]:
                continue
            values[cell] = label
            yield from visit(label + 1, occupied | bit)
            values[cell] = 0

    yield from visit(1, 0)


def promotion(tableau: tuple[int, ...], a: int, b: int) -> tuple[int, ...]:
    grid = list(tableau)
    hole = a * b - 1
    grid[hole] = 0
    while hole:
        row, column = divmod(hole, b)
        candidates = []
        if row:
            candidates.append(hole - b)
        if column:
            candidates.append(hole - 1)
        chosen = max(candidates, key=lambda index: grid[index])
        grid[hole] = grid[chosen]
        grid[chosen] = 0
        hole = chosen
    grid = [value + 1 if value else 1 for value in grid]
    return tuple(grid)


def demotion(tableau: tuple[int, ...], a: int, b: int) -> tuple[int, ...]:
    grid = list(tableau)
    grid[0] = 0
    hole = 0
    final = a * b - 1
    while hole != final:
        row, column = divmod(hole, b)
        candidates = []
        if row + 1 < a:
            candidates.append(hole + b)
        if column + 1 < b:
            candidates.append(hole + 1)
        chosen = min(candidates, key=lambda index: grid[index])
        grid[hole] = grid[chosen]
        grid[chosen] = 0
        hole = chosen
    n = a * b
    grid = [value - 1 if value else n for value in grid]
    return tuple(grid)


def evacuation(tableau: tuple[int, ...], a: int, b: int) -> tuple[int, ...]:
    n = a * b
    answer = [0] * n
    for row in range(a):
        for column in range(b):
            source = (a - 1 - row) * b + (b - 1 - column)
            answer[row * b + column] = n + 1 - tableau[source]
    return tuple(answer)


def direct_cycles(mapping: dict[tuple[int, ...], tuple[int, ...]]) -> Counter:
    unseen = set(mapping)
    counts: Counter = Counter()
    while unseen:
        start = next(iter(unseen))
        current = start
        length = 0
        while current in unseen:
            unseen.remove(current)
            current = mapping[current]
            length += 1
        if current != start:
            raise AssertionError("promotion map is not a permutation cycle")
        counts[length] += 1
    return counts


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    data = json.loads(path.read_text())
    checks = 0

    def check(condition: bool, label: str) -> None:
        nonlocal checks
        if not condition:
            raise AssertionError(label)
        checks += 1

    check(set(data) == {
        "schema", "candidate_id", "date_utc", "source_commit", "scope_literal",
        "evaluator", "source_lock", "attribution", "theorem", "finite_replay",
        "progress_and_boundary", "route_a", "scope_flags", "source_registry",
        "nonclaims", "payload_sha256",
    }, "top-level exact map")
    check(data["payload_sha256"] == canonical_hash(data), "payload hash")
    check(data["schema"] == "HCS-C187-v1", "schema")
    check(data["candidate_id"] == "HCS-C187", "candidate")
    check(data["date_utc"] == "2026-08-26", "date")
    check(data["source_commit"] == EXPECTED_COMMIT, "commit")
    check(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    check(data["evaluator"] == {
        "path": "flow_systems/skills/route-a-evaluator.md",
        "version": "0.2.0",
        "sha256": EXPECTED_EVALUATOR,
    }, "evaluator exact map")
    check(data["source_lock"] == EXPECTED_SOURCE_LOCK, "source lock exact map")
    check(data["attribution"] == EXPECTED_ATTRIBUTION, "attribution exact map")
    check(data["theorem"] == EXPECTED_THEOREM, "theorem exact map")
    check(data["progress_and_boundary"] == EXPECTED_BOUNDARY, "boundary exact map")
    check(data["route_a"] == EXPECTED_ROUTE_A, "Route-A exact map")
    check(data["scope_flags"] == EXPECTED_SCOPE_FLAGS, "scope flags exact map")
    check(data["source_registry"] == EXPECTED_SOURCE_REGISTRY, "source registry exact list")
    check(data["nonclaims"] == EXPECTED_NONCLAIMS, "nonclaims exact list")

    finite = data["finite_replay"]
    check(set(finite) == {
        "a_min", "a_max", "b_min", "b_max", "enumeration_n_max",
        "enumeration_tableau_max", "rectangles", "iterate_rows", "period_rows",
        "spectral_rows", "rectangle_row_count", "iterate_row_count",
        "period_row_count", "spectral_row_count", "enumeration_rectangle_count",
    }, "finite exact map")
    check((finite["a_min"], finite["a_max"], finite["b_min"], finite["b_max"]) == (1, 6, 1, 6), "rectangle cutoff")
    check(finite["enumeration_n_max"] == 16, "enumeration n cutoff")
    check(finite["enumeration_tableau_max"] == 50_000, "enumeration population cutoff")

    rectangles = finite["rectangles"]
    iterates = finite["iterate_rows"]
    periods = finite["period_rows"]
    spectra = finite["spectral_rows"]
    check(len(rectangles) == finite["rectangle_row_count"] == 36, "rectangle row count")
    check(len(iterates) == finite["iterate_row_count"] == 441, "iterate row count")
    check(len(periods) == finite["period_row_count"] == 162, "period row count")
    check(len(spectra) == finite["spectral_row_count"] == 441, "spectral row count")

    rectangle_map = {(row["a"], row["b"]): row for row in rectangles}
    iterate_map = {(row["a"], row["b"], row["iterate"]): row for row in iterates}
    period_map = {(row["a"], row["b"], row["period"]): row for row in periods}
    spectral_map = {(row["a"], row["b"], row["root_exponent_mod_n"]): row for row in spectra}
    check(len(rectangle_map) == len(rectangles), "unique rectangles")
    check(len(iterate_map) == len(iterates), "unique iterate rows")
    check(len(period_map) == len(periods), "unique period rows")
    check(len(spectral_map) == len(spectra), "unique spectral rows")

    selected = 0
    for a in range(1, 7):
        for b in range(1, 7):
            n = a * b
            row = rectangle_map[(a, b)]
            hook_list = hooks(a, b)
            count = factorial(n) // prod(hook_list)
            coefficients = independent_q_hook(a, b)
            cyclotomic_exponents = {
                str(order): n // order - sum(hook % order == 0 for hook in hook_list)
                for order in range(2, n + 1)
                if n // order - sum(hook % order == 0 for hook in hook_list)
            }
            hook_counter = Counter(hook_list)
            check(set(row) == {
                "a", "b", "n", "shape", "hook_multiset", "tableau_count",
                "q_hook_convention", "q_hook_cyclotomic_exponents", "q_hook_degree",
                "q_hook_coefficients", "q_hook_coefficients_sha256",
                "promotion_order_divides", "actual_promotion_order", "identity_boundary",
                "enumeration_regression_selected", "nonzero_cycle_lengths",
                "zeta_factors", "koopman_determinant_factors",
            }, "rectangle row exact map")
            check((row["a"], row["b"], row["n"]) == (a, b, n), "rectangle coordinates")
            check(row["shape"] == [b] * a, "shape")
            check(row["hook_multiset"] == {str(key): hook_counter[key] for key in sorted(hook_counter)}, "hook multiset")
            check(row["tableau_count"] == count, "hook count")
            check(row["q_hook_convention"] == "F_ab(q)=[ab]_q!/product_(cells c)[h(c)]_q with no q-shift", "row q-hook convention")
            check(row["q_hook_cyclotomic_exponents"] == cyclotomic_exponents, "cyclotomic exponent ledger")
            check(row["q_hook_coefficients"] == coefficients, "q-hook coefficients")
            check(row["q_hook_degree"] == len(coefficients) - 1, "q-hook degree")
            check(row["q_hook_coefficients_sha256"] == sha256(json.dumps(coefficients, separators=(",", ":")).encode()).hexdigest(), "coefficient hash")
            check(sum(coefficients) == count, "q-hook at one")
            check(row["promotion_order_divides"] == n, "order divisor")
            check(row["identity_boundary"] == (a == 1 or b == 1), "identity boundary")
            selection = n <= 16 and count <= 50_000
            check(row["enumeration_regression_selected"] == selection, "enumeration selection")
            selected += int(selection)

            fixed: dict[int, int] = {}
            for power in range(n):
                item = iterate_map[(a, b, power)]
                order = n // gcd(n, power)
                value = root_value(coefficients, order)
                check(set(item) == {"a", "b", "n", "iterate", "gcd_n_iterate", "root_order", "fixed_count"}, "iterate exact map")
                check((item["a"], item["b"], item["n"], item["iterate"]) == (a, b, n, power), "iterate coordinates")
                check(item["gcd_n_iterate"] == gcd(n, power), "iterate gcd")
                check(item["root_order"] == order, "root order")
                check(item["fixed_count"] == value >= 0, "CSP root value")
                fixed[power] = value

            cycle_counts: dict[int, int] = {}
            exact_counts: dict[int, int] = {}
            for period in divisors(n):
                item = period_map[(a, b, period)]
                exact = sum(mu(period // d) * (count if d == n else fixed[d]) for d in divisors(period))
                check(set(item) == {"a", "b", "n", "period", "fixed_at_period", "exact_period_count", "cycle_count"}, "period exact map")
                check((item["a"], item["b"], item["n"], item["period"]) == (a, b, n, period), "period coordinates")
                check(item["fixed_at_period"] == (count if period == n else fixed[period]), "period fixed count")
                check(item["exact_period_count"] == exact >= 0, "Mobius exact-period count")
                check(exact % period == 0 and item["cycle_count"] == exact // period, "cycle count")
                exact_counts[period] = exact
                cycle_counts[period] = exact // period
            check(sum(exact_counts.values()) == count, "period population")
            actual_order = 1
            for period, population in exact_counts.items():
                if population:
                    actual_order = lcm(actual_order, period)
            check(row["actual_promotion_order"] == actual_order, "actual order")
            check(n % actual_order == 0, "actual order divides n")
            nonzero = [period for period in divisors(n) if cycle_counts[period]]
            check(row["nonzero_cycle_lengths"] == nonzero, "nonzero cycle lengths")
            check(row["zeta_factors"] == [
                {"period": period, "exponent": -cycle_counts[period]} for period in nonzero
            ], "zeta factors")
            check(row["koopman_determinant_factors"] == [
                {"period": period, "exponent": cycle_counts[period]} for period in nonzero
            ], "determinant factors")

            spectral_sum = 0
            for exponent in range(n):
                item = spectral_map[(a, b, exponent)]
                multiplicity = sum(
                    cycle_counts[period] for period in divisors(n)
                    if exponent * period % n == 0
                )
                check(set(item) == {"a", "b", "n", "root_exponent_mod_n", "multiplicity"}, "spectral exact map")
                check((item["a"], item["b"], item["n"], item["root_exponent_mod_n"]) == (a, b, n, exponent), "spectral coordinates")
                check(item["multiplicity"] == multiplicity, "spectral multiplicity")
                spectral_sum += multiplicity
            check(spectral_sum == count, "spectral population")

            transposed = rectangle_map[(b, a)]
            check(row["q_hook_coefficients"] == transposed["q_hook_coefficients"], "transpose q-hook symmetry")
            check(row["tableau_count"] == transposed["tableau_count"], "transpose hook symmetry")

            if selection:
                population = list(tableaux(a, b))
                check(len(population) == count, "direct tableau population")
                check(len(set(population)) == count, "direct tableau uniqueness")
                population_set = set(population)
                mapping = {}
                for tableau in population:
                    check(is_standard(tableau, a, b), "enumerated tableau standard")
                    promoted = promotion(tableau, a, b)
                    check(promoted in population_set, "promotion closure")
                    check(demotion(promoted, a, b) == tableau, "demotion inverse")
                    evacuated = evacuation(tableau, a, b)
                    check(evacuated in population_set, "evacuation closure")
                    check(evacuation(evacuated, a, b) == tableau, "evacuation involution")
                    check(evacuation(promotion(evacuated, a, b), a, b) == demotion(tableau, a, b), "evacuation reversor")
                    mapping[tableau] = promoted
                direct = direct_cycles(mapping)
                check(sum(length * number for length, number in direct.items()) == count, "direct cycle population")
                check(all(n % length == 0 for length in direct), "direct order-divides-n")
                for period in divisors(n):
                    check(direct.get(period, 0) == cycle_counts[period], "direct cycle ledger")
                for power in range(n):
                    direct_fixed = sum(length * number for length, number in direct.items() if power % length == 0)
                    check(direct_fixed == fixed[power], "direct fixed ledger")
                direct_order = 1
                for length in direct:
                    direct_order = lcm(direct_order, length)
                check(direct_order == actual_order, "direct actual order")
                if a == 1 or b == 1:
                    check(count == 1 and actual_order == 1 and direct == Counter({1: 1}), "one-dimensional identity")

    check(selected == finite["enumeration_rectangle_count"] == 26, "enumeration rectangle count")
    row_22 = rectangle_map[(2, 2)]
    check(row_22["tableau_count"] == 2, "2-by-2 population")
    check(row_22["actual_promotion_order"] == 2 < row_22["n"], "2-by-2 strict order boundary")
    print(json.dumps({
        "status": "C187_CHECKER_PASS",
        "assertions": checks,
        "direct_rectangles": selected,
        "direct_tableaux": sum(
            row["tableau_count"] for row in rectangles if row["enumeration_regression_selected"]
        ),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
