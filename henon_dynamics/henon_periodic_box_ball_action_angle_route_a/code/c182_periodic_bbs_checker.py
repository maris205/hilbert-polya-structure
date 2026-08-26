#!/usr/bin/env python3
"""Producer-independent exact and brute-force checker for HCS-C182."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, product
import json
from math import comb, gcd
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c182_periodic_bbs_evidence.json"
SOURCE_COMMIT = "bbb809ee198bc9ad5f196383baab1e3d9de38e43"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"


def canonical_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def factors(n: int) -> list[int]:
    small: list[int] = []
    large: list[int] = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            small.append(d)
            if d * d != n:
                large.append(n // d)
        d += 1
    return small + large[::-1]


def mu(n: int) -> int:
    distinct = 0
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            n //= divisor
            distinct += 1
            if n % divisor == 0:
                return 0
            while n % divisor == 0:
                n //= divisor
        divisor += 1
    if n > 1:
        distinct += 1
    return -1 if distinct % 2 else 1


def determinant_q(matrix: list[list[int]]) -> int:
    n = len(matrix)
    if n == 0:
        return 1
    a = [[Fraction(value) for value in row] for row in matrix]
    answer = Fraction(1)
    for col in range(n):
        pivot = next((row for row in range(col, n) if a[row][col]), None)
        if pivot is None:
            return 0
        if pivot != col:
            a[col], a[pivot] = a[pivot], a[col]
            answer = -answer
        pivot_value = a[col][col]
        answer *= pivot_value
        for j in range(col, n):
            a[col][j] /= pivot_value
        for row in range(col + 1, n):
            scale = a[row][col]
            for j in range(col, n):
                a[row][j] -= scale * a[col][j]
    if answer.denominator != 1:
        raise ArithmeticError("integer determinant became fractional")
    return answer.numerator


def independent_smith(matrix: list[list[int]]) -> list[int]:
    r = len(matrix)
    c = len(matrix[0]) if r else 0
    previous = 1
    answer: list[int] = []
    for size in range(1, min(r, c) + 1):
        delta = 0
        for rows in combinations(range(r), size):
            for cols in combinations(range(c), size):
                sub = [[matrix[i][j] for j in cols] for i in rows]
                delta = gcd(delta, abs(determinant_q(sub)))
        if delta == 0:
            break
        answer.append(delta // previous)
        previous = delta
    return answer


def solve_order(matrix: list[list[int]], h: list[int]) -> int:
    """Independent order calculation from denominators of F^{-1}h."""
    n = len(matrix)
    if n == 0:
        return 1
    a = [
        [Fraction(matrix[i][j]) for j in range(n)] + [Fraction(h[i])]
        for i in range(n)
    ]
    for col in range(n):
        pivot = next(row for row in range(col, n) if a[row][col])
        a[col], a[pivot] = a[pivot], a[col]
        scale = a[col][col]
        a[col] = [value / scale for value in a[col]]
        for row in range(n):
            if row == col:
                continue
            scale = a[row][col]
            a[row] = [a[row][j] - scale * a[col][j] for j in range(n + 1)]
    order = 1
    for row in range(n):
        denominator = a[row][-1].denominator
        order = order * denominator // gcd(order, denominator)
    return order


def lambda_count(m: int, p: int, alpha: int) -> int:
    answer = 0
    common = gcd(m, p)
    for beta in factors(common):
        if beta % alpha == 0:
            answer += mu(beta // alpha) * comb((m + p) // beta - 1, m // beta - 1)
    return answer


def expected_cycles(rows: list[dict]) -> dict[int, int]:
    return {row["order"]: row["points"] for row in rows}


def carrier_step(state: tuple[int, ...], capacity: int) -> tuple[tuple[int, ...], int]:
    """Periodic carrier update and conserved energy, independent of angle variables."""
    solutions: list[tuple[tuple[int, ...], int]] = []
    for initial in range(capacity + 1):
        load = initial
        output: list[int] = []
        energy = 0
        for ball in state:
            if ball:
                if load < capacity:
                    load += 1
                    output.append(0)
                    energy += 1
                else:
                    output.append(1)
            else:
                if load:
                    load -= 1
                    output.append(1)
                else:
                    output.append(0)
        if load == initial:
            solutions.append((tuple(output), energy))
    if not solutions or len(set(solutions)) != 1:
        raise AssertionError(f"periodic carrier ambiguity: {state}, l={capacity}")
    return solutions[0]


def state_content(state: tuple[int, ...]) -> str:
    mass = sum(state)
    if mass == 0:
        return "vacuum"
    energies = [0] + [carrier_step(state, l)[1] for l in range(1, mass + 2)]
    entries = []
    recovered = 0
    for j in range(1, mass + 1):
        count = 2 * energies[j] - energies[j - 1] - energies[j + 1]
        if count:
            if count < 0:
                raise AssertionError("negative soliton multiplicity")
            entries.append(f"{j}^{count}")
            recovered += j * count
    if recovered != mass:
        raise AssertionError("energy/content recovery failed")
    return "+".join(entries)


def brute_spectra(L: int, M: int, l_value: int) -> tuple[dict[int, int], dict[str, dict[int, int]]]:
    states = []
    for occupied in combinations(range(L), M):
        state = [0] * L
        for position in occupied:
            state[position] = 1
        states.append(tuple(state))
    mapping = {state: carrier_step(state, l_value)[0] for state in states}
    if len(set(mapping.values())) != len(states):
        raise AssertionError("T_l is not a permutation")
    visited: set[tuple[int, ...]] = set()
    aggregate: dict[int, int] = {}
    by_content: dict[str, dict[int, int]] = {}
    for start in states:
        if start in visited:
            continue
        orbit: list[tuple[int, ...]] = []
        point = start
        while point not in orbit:
            orbit.append(point)
            visited.add(point)
            point = mapping[point]
        if point != start:
            raise AssertionError("permutation orbit did not close at its start")
        order = len(orbit)
        aggregate[order] = aggregate.get(order, 0) + order
        key = state_content(start)
        bucket = by_content.setdefault(key, {})
        bucket[order] = bucket.get(order, 0) + order
        for point in orbit:
            if state_content(point) != key:
                raise AssertionError("soliton content was not conserved")
    return aggregate, by_content


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT)
    args = parser.parse_args()
    data = json.loads(args.input.read_text())
    assertions = 0

    def check(condition: bool, label: str) -> None:
        nonlocal assertions
        assertions += 1
        if not condition:
            raise AssertionError(label)

    check(data["payload_sha256"] == canonical_hash(data), "canonical payload hash")
    check(data["schema"] == "hcs-c182-periodic-bbs-action-angle-v1", "schema")
    check(data["candidate_id"] == "HCS-C182", "candidate")
    check(data["evaluation_date"] == "2026-08-26", "date")
    check(data["source_commit"] == SOURCE_COMMIT, "source commit")
    check(data["evaluator"]["skill"] == "route-a-evaluator", "evaluator skill")
    check(data["evaluator"]["version"] == "0.2.0", "evaluator version")
    check(data["evaluator"]["path"] == "flow_systems/skills/route-a-evaluator.md", "evaluator path")
    check(data["evaluator"]["sha256"] == EVALUATOR_SHA256, "evaluator hash")
    check(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")

    lock_fragments = {
        "object": "periodic A_1^(1) box--ball system",
        "family": "all integers L>=1",
        "phase_space": "P_(L,M)",
        "dynamics": "capacity-l periodic combinatorial-R carrier map",
        "parameters": "L,M,l",
        "parameter_provenance": "intrinsic lattice",
        "arithmetic_origin": "none:",
        "clock": "one application of T_l",
        "normalization": "binary symbols",
        "determinant_convention": "Artin--Mazur zeta",
        "orbit_cutoff": "none in the theorem",
        "precision": "exact integers",
        "training_data": "none",
        "allowed_data": "KTT/Takagi",
        "forbidden_data": "target zero or prime tables",
    }
    for key, fragment in lock_fragments.items():
        check(fragment in data["source_lock"][key], f"source lock {key}")

    check(len(data["source_attribution"]) == 2, "source population")
    for source in data["source_attribution"]:
        check(source["verified"] is True, "source verification")
        check(source["url"].startswith("https://"), "source URL")
        check("source theorem" in source["role"], "source role")

    theorem = data["theorem"]
    theorem_fragments = {
        "feasibility_triage": "PROVABLE AS STATED",
        "admissible_domain": "L>=2M",
        "internal_symmetry": "for each j in H choose alpha_j",
        "sector_matrix": "F_alpha[j,k]",
        "sector_torus": "each connected component",
        "sector_multiplicity": "prod_j",
        "mobius_count": "|Lambda^(alpha)",
        "snf_order": "ord_alpha,l",
        "component_fixed_points": "#Fix",
        "aggregate_fixed_points": "sum_alpha",
        "primitive_cycles": "P_n=sum_",
        "zeta_koopman": "zeta_T(z)=",
        "commutativity": "all T_l commute",
        "saturation": "h_l=(j)",
        "vacuum_boundary": "M=0",
        "half_filling_boundary": "when L=2M",
        "source_novelty_boundary": "the action--angle",
    }
    for key, fragment in theorem_fragments.items():
        check(theorem[key].startswith(fragment), f"theorem {key}")

    finite = data["finite_regression_sentinels"]
    check(finite["sentinels_are_proof"] is False, "sentinel/proof boundary")
    coverage = finite["coverage"]
    check(coverage["L_max"] == 14, "L max")
    check(coverage["fixed_n_max"] == 12, "fixed prefix")
    levels = finite["level_rows"]
    check(coverage["level_count"] == len(levels), "level count")

    level_index: dict[tuple[int, int, str], dict] = {}
    sector_count = 0
    translation_count = 0
    component_sum = 0
    sector_point_sum = 0
    for level in levels:
        L, M, key = level["L"], level["M"], level["content_key"]
        check(2 <= L <= 14, f"level L {L}")
        check(0 <= M <= L // 2, f"level M {L},{M}")
        check((L, M, key) not in level_index, f"unique level {L},{M},{key}")
        level_index[(L, M, key)] = level
        content = {entry["j"]: entry["m_j"] for entry in level["content"]}
        vacancies = {entry["j"]: entry["p_j"] for entry in level["content"]}
        check(sum(j * count for j, count in content.items()) == M, f"mass {key}")
        expected_key = "+".join(f"{j}^{content[j]}" for j in sorted(content)) if content else "vacuum"
        check(key == expected_key, f"content key {key}")
        for j in content:
            p = L - 2 * sum(min(j, k) * count for k, count in content.items())
            check(vacancies[j] == p >= 0, f"vacancy {L},{key},{j}")

        l_values = list(range(1, L // 2 + 2))
        check([row["l"] for row in level["evolutions"]] == l_values, f"level l ledger {key}")
        aggregate = {l_value: {} for l_value in l_values}
        points_total = 0
        positive_expected = 0
        if content:
            alpha_ranges = [factors(gcd(content[j], vacancies[j])) for j in sorted(content)]
            candidate_count = 1
            for values in alpha_ranges:
                candidate_count *= len(values)
            positive_expected = sum(
                1
                for alpha in product(*alpha_ranges)
                if all(lambda_count(content[j], vacancies[j], alpha[pos]) > 0 for pos, j in enumerate(sorted(content)))
            )
        else:
            candidate_count = 1
            positive_expected = 1
        check(level["sector_candidate_count"] == candidate_count, f"sector candidates {key}")
        check(level["positive_sector_count"] == positive_expected, f"positive sectors {key}")

        for sector in level["sectors"]:
            sector_count += 1
            support = sorted(content)
            alpha = sector["alpha"]
            check(len(alpha) == len(support), f"alpha rank {key}")
            lambda_values = []
            factors_mult = []
            matrix = []
            for row_j, j in enumerate(support):
                matrix_row = []
                for col_k, k in enumerate(support):
                    check(gcd(content[k], vacancies[k]) % alpha[col_k] == 0, f"alpha divisor {key}")
                    numerator = (vacancies[k] if j == k else 0) + 2 * min(j, k) * content[k]
                    check(numerator % alpha[col_k] == 0, f"matrix integrality {key}")
                    matrix_row.append(numerator // alpha[col_k])
                matrix.append(matrix_row)
                count = lambda_count(content[j], vacancies[j], alpha[row_j])
                lambda_values.append(count)
                check(count % (content[j] // alpha[row_j]) == 0, f"multiplicity integrality {key}")
                factors_mult.append(count // (content[j] // alpha[row_j]))
            multiplicity = 1
            for value in factors_mult:
                multiplicity *= value
            det_f = abs(determinant_q(matrix))
            check(sector["lambda_exact_counts"] == lambda_values, f"Lambda counts {key}")
            check(sector["component_multiplicity_factors"] == factors_mult, f"multiplicity factors {key}")
            check(sector["component_multiplicity"] == multiplicity > 0, f"multiplicity {key}")
            check(sector["F_alpha"] == matrix, f"F alpha {key}")
            check(sector["det_F_alpha"] == det_f > 0, f"det F {key}")
            check(sector["smith_invariants"] == independent_smith(matrix), f"Smith F {key}")
            check(sector["points_in_sector"] == multiplicity * det_f, f"sector points {key}")
            points_total += multiplicity * det_f
            component_sum += multiplicity
            sector_point_sum += multiplicity * det_f
            check([row["l"] for row in sector["translations"]] == l_values, f"translation l ledger {key}")
            for translation in sector["translations"]:
                translation_count += 1
                l_value = translation["l"]
                h = [min(j, l_value) for j in support]
                order = solve_order(matrix, h)
                augmented = [matrix[i] + [h[i]] for i in range(len(matrix))]
                check(translation["h"] == h, f"h vector {key},{l_value}")
                check(translation["augmented_smith_invariants"] == independent_smith(augmented), f"Smith augmented {key},{l_value}")
                check(translation["order"] == order >= 1, f"translation order {key},{l_value}")
                for row in translation["fixed_component_prefix"]:
                    expected = det_f if row["n"] % order == 0 else 0
                    check(row["fixed_points_per_component"] == expected, f"component fixed {key},{l_value},{row['n']}")
                bucket = aggregate[l_value]
                bucket[order] = bucket.get(order, 0) + multiplicity * det_f

        check(points_total == level["level_cardinality"], f"level sector sum {key}")
        if content:
            base = []
            for j in sorted(content):
                base.append([
                    (vacancies[k] if j == k else 0) + 2 * min(j, k) * content[k]
                    for k in sorted(content)
                ])
            formula = Fraction(abs(determinant_q(base)))
            for j in sorted(content):
                formula *= Fraction(comb(vacancies[j] + content[j] - 1, content[j] - 1), content[j])
            check(formula.denominator == 1, f"integral level formula {key}")
            level_formula = formula.numerator
        else:
            level_formula = 1
        check(level["ktt_level_cardinality"] == level_formula == points_total, f"KTT level size {key}")
        for evolution in level["evolutions"]:
            l_value = evolution["l"]
            spectrum = aggregate[l_value]
            check(expected_cycles(evolution["cycle_spectrum"]) == spectrum, f"level cycles {key},{l_value}")
            for row in evolution["cycle_spectrum"]:
                check(row["points"] % row["order"] == 0, f"cycle divisibility {key},{l_value}")
                check(row["cycles"] == row["points"] // row["order"], f"cycle count {key},{l_value}")
            for row in evolution["fixed_point_prefix"]:
                expected = sum(points for order, points in spectrum.items() if row["n"] % order == 0)
                check(row["fixed_points"] == expected, f"level fixed {key},{l_value},{row['n']}")
            check(
                evolution["artin_mazur_zeta_factors"]
                == [{"degree": row["order"], "exponent": -row["cycles"]} for row in evolution["cycle_spectrum"]],
                f"level zeta {key},{l_value}",
            )
            check(
                evolution["koopman_determinant_factors"]
                == [{"degree": row["order"], "exponent": row["cycles"]} for row in evolution["cycle_spectrum"]],
                f"level determinant {key},{l_value}",
            )

    check(coverage["sector_count"] == sector_count, "sector total")
    check(coverage["translation_count"] == translation_count, "translation total")
    check(coverage["component_multiplicity_sum"] == component_sum, "component total")
    check(coverage["sector_point_sum"] == sector_point_sum, "sector point total")

    state_rows = finite["state_aggregate_rows"]
    check(coverage["state_aggregate_count"] == len(state_rows), "state aggregate total")
    state_index: dict[tuple[int, int, int], dict] = {}
    for row in state_rows:
        key = (row["L"], row["M"], row["l"])
        check(key not in state_index, f"unique state aggregate {key}")
        state_index[key] = row
        constituent = [level for (L, M, _), level in level_index.items() if (L, M) == key[:2]]
        check(sum(level["level_cardinality"] for level in constituent) == comb(row["L"], row["M"]), f"binomial partition {key}")
        check(row["state_count"] == comb(row["L"], row["M"]), f"state count {key}")
        spectrum: dict[int, int] = {}
        for level in constituent:
            evolution = level["evolutions"][row["l"] - 1]
            for cycle in evolution["cycle_spectrum"]:
                spectrum[cycle["order"]] = spectrum.get(cycle["order"], 0) + cycle["points"]
        check(expected_cycles(row["cycle_spectrum"]) == spectrum, f"state spectrum {key}")
        for fixed in row["fixed_point_prefix"]:
            check(fixed["fixed_points"] == sum(points for order, points in spectrum.items() if fixed["n"] % order == 0), f"state fixed {key},{fixed['n']}")

    length_rows = finite["length_aggregate_rows"]
    check(coverage["length_aggregate_count"] == len(length_rows), "length aggregate total")
    for row in length_rows:
        L, l_value = row["L"], row["l"]
        constituents = [state_index[(L, M, l_value)] for M in range(L // 2 + 1)]
        total = sum(comb(L, M) for M in range(L // 2 + 1))
        check(row["positive_weight_state_count"] == total, f"positive weight count {L},{l_value}")
        spectrum: dict[int, int] = {}
        for constituent in constituents:
            for cycle in constituent["cycle_spectrum"]:
                spectrum[cycle["order"]] = spectrum.get(cycle["order"], 0) + cycle["points"]
        check(expected_cycles(row["cycle_spectrum"]) == spectrum, f"length spectrum {L},{l_value}")

    # Direct carrier enumeration is independent of KTT angle variables and attacks
    # every word for L<=9, including vacuum and half filling.
    brute_states = 0
    brute_maps = 0
    brute_cycles = 0
    for L in range(2, 10):
        for M in range(L // 2 + 1):
            brute_states += comb(L, M)
            for l_value in range(1, L // 2 + 2):
                aggregate, by_content = brute_spectra(L, M, l_value)
                brute_maps += 1
                brute_cycles += sum(points // order for order, points in aggregate.items())
                check(expected_cycles(state_index[(L, M, l_value)]["cycle_spectrum"]) == aggregate, f"brute state {L},{M},{l_value}")
                for content_key, spectrum in by_content.items():
                    level = level_index[(L, M, content_key)]
                    check(expected_cycles(level["evolutions"][l_value - 1]["cycle_spectrum"]) == spectrum, f"brute level {L},{M},{l_value},{content_key}")

    progress = data["progress_and_boundary"]
    check(progress["progress"].startswith("an all-L"), "progress")
    check(progress["source_boundary"].startswith("KTT/Takagi own"), "source boundary")
    check(progress["arithmetic_clock_obstruction"].startswith("the intrinsic clock"), "clock obstruction")
    check(progress["analytic_obstruction"].startswith("every fixed-(L,M,l) zeta"), "analytic obstruction")
    check(progress["operator_progress"].startswith("the counting-measure Koopman"), "operator progress")
    check(progress["route_boundary"].endswith("Hilbert--Polya operator"), "route boundary")

    route = data["route_a"]
    check(route["tuple"] == ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"], "Route tuple")
    check(route["overall"] == "ROUTE_A_REJECTED", "Route overall")
    check(route["A0_qualification"].startswith("NO_INTRINSIC_RATIONAL_PRIME"), "A0")
    check(route["A1_qualification"].startswith("COMPLETE_INTRINSIC_PRIMITIVE"), "A1")
    check(route["A2_qualification"].startswith("EXACT_FINITE_SOURCE_ZETA"), "A2")
    check(route["A3_qualification"].startswith("FINITE_RATIONAL_SOURCE"), "A3")
    check(route["A4_qualification"].startswith("SAME_CLOCK_FINITE"), "A4")
    check(route["route_b_invocation_allowed"] is False, "Route B")
    for key, value in data["scope_flags"].items():
        check(value is False, f"scope flag {key}")
    integrity = data["integrity"]
    check(integrity["finite_ledgers_are_proof"] is False, "finite ledger boundary")
    check(integrity["citation_population"] == 2, "citation population")
    check(integrity["verified_reference_population"] == 2, "reference population")
    check(integrity["external_reviewer_simulated"] is False, "review boundary")
    check(integrity["acceptance_score_claimed"] is False, "acceptance boundary")
    check(integrity["all_parameter_claims_have_proof_dependencies"] is True, "proof dependencies")
    check(integrity["model_rejected_as_primary_route_a_candidate"] is True, "Route rejection integrity")
    check(len(data["nonclaims"]) == 7, "nonclaim population")

    print(
        json.dumps(
            {
                "status": "C182_CHECKER_PASS",
                "assertions": assertions,
                "brute_states": brute_states,
                "brute_maps": brute_maps,
                "brute_cycles": brute_cycles,
                "payload_sha256": data["payload_sha256"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
