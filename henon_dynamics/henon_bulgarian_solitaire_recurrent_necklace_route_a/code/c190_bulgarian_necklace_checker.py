#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C190.

The checker intentionally does not import the producer.  It reconstructs the
binary-word model with a Cartesian-product generator, then independently
enumerates every integer partition for 1<=N<=40 and follows the actual
noninvertible Bulgarian map.
"""
from __future__ import annotations

from hashlib import sha256
from itertools import product
import json
from math import comb, gcd
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c190_bulgarian_necklace_evidence.json"
EXPECTED_COMMIT = "4d7b214759f7ff982c0b19e662918acd307e0f58"
EXPECTED_EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"

EXPECTED_SOURCE_LOCK = {
    "object": "noninvertible Bulgarian-solitaire map T_N on the integer partitions P(N)",
    "family": "every integer N>=1, uniquely N=binom(k,2)+r with 0<=r<k",
    "phase_space": "the full finite partition set P(N), with the Brandt recurrent subset marked inside it",
    "clock": "one Bulgarian move: remove one card from every pile and form a new pile from the removed cards",
    "measure": "counting measure on P(N), and counting measure on the recurrent subset",
    "recurrent_model": "length-k weight-r binary words; w maps to positive parts of (k-1,k-2,...,0)+w",
    "rotation_convention": "T_N corresponds to right rotation rho(w)_i=w_(i-1 mod k)",
    "operator": "full finite Koopman pullback U_N f=f composed with T_N and its recurrent permutation restriction",
    "determinant_convention": "Artin--Mazur zeta of the full finite map and reciprocal det(I-z U_N)",
    "cutoff": "all-N attributed recurrent theorem; exact finite regression only for 1<=N<=40",
    "allowed_data": "integer partitions, binary words, rotations, reflections, exact divisor sums, and partition numbers",
    "forbidden_data": "target zero or prime tables, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya operators, and Route-B inputs",
}

EXPECTED_ATTRIBUTION = {
    "status": "SOURCE_DERIVED_SYNTHESIS_NOT_NEW_THEOREM_CLAIM",
    "recurrent_owner": "Brandt 1982 owns the all-N characterization of cyclic partitions and its binary-necklace parametrization",
    "dynamical_background": "Akin and Davis 1985 give a classical treatment of Bulgarian solitaire and the recurrent classification",
    "package_increment": "source-locked closure of every iterate fixed count, Mobius least periods and cycles, full finite zeta, full Koopman algebraic spectrum, recurrent reflection reversal, and triangular boundary",
    "finite_evidence_role": "the N<=40 word and full-partition census is regression evidence only and does not prove the all-N recurrent theorem",
}

EXPECTED_THEOREM = {
    "decomposition": "every N>=1 has unique N=binom(k,2)+r with integers k>=2 and 0<=r<k",
    "recurrent_bijection": "Brandt recurrent partitions are exactly phi(w)=positive parts of (k-1,...,0)+w for length-k weight-r binary words, and T_N phi=phi rho",
    "fixed_count": "with g=gcd(k,t), Fix(T_N^t)=binom(g,r*g/k) if k/g divides r and is zero otherwise",
    "exact_period": "for every d|k, P_d=sum_(e|d) mu(d/e) Fix(T_N^e) and C_d=P_d/d",
    "zeta": "zeta_T(z)=product_(d|k)(1-z^d)^(-C_d) for the full noninvertible finite map",
    "koopman": "det(I-z U_N)=product_(d|k)(1-z^d)^(C_d); zero has algebraic multiplicity p(N)-binom(k,r), and mult(exp(2*pi*i*j/k))=sum_(d|k,k|j*d) C_d",
    "trace": "Tr(U_N^t)=Fix(T_N^t) for every t>=1",
    "reversor": "on the recurrent core Q(w)_i=w_(-i mod k) is an involution with Q rho Q=rho^(-1); rho^a Q gives k phase-labelled reflection formulas, not necessarily distinct on a nonfaithful weight layer",
    "triangular_boundary": "if r=0 the recurrent core is the single staircase (k-1,...,1), with zeta (1-z)^(-1) and recurrent Koopman eigenvalue one",
}

EXPECTED_BOUNDARY = {
    "progress": "one all-N theorem package closes the periodic core, every fixed iterate, primitive cycles, full finite zeta, algebraic Koopman spectrum, recurrent reflection reversal, and triangular family",
    "transient_boundary": "complete transient functional trees, exact hitting-time distributions, and nilpotent Jordan block sizes are outside the claim",
    "noninvertible_boundary": "T_N is not globally invertible in general, so reflection reversal is asserted only on the recurrent core",
    "proof_boundary": "Brandt's all-N recurrent characterization is imported with attribution; the finite census regression-tests consequences rather than proving it",
    "arithmetic_boundary": "deck size, pile sizes, word weights, rotations, and partition numbers have no intrinsic rational-prime or prime-power semantics",
    "operator_boundary": "the full Koopman map is finite and nonunitary; its recurrent unitary restriction is only a formal operator hint and no Hilbert--Polya claim",
}

EXPECTED_ROUTE_A = {
    "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
    "overall": "ROUTE_A_REJECTED",
    "A0_qualification": "PARTITIONS_AND_BINARY_NECKLACES_HAVE_NO_INTRINSIC_RATIONAL_PRIME_ORIGIN",
    "A1_qualification": "RECURRENT_PRIMITIVE_CYCLES_ARE_COMPLETE_BUT_CARRY_NO_A0_ARITHMETIC_PAYLOAD",
    "A2_qualification": "FINITE_SOURCE_ZETA_AND_KOOPMAN_DETERMINANT_HAVE_NO_TARGET_DIVISOR_MATCH",
    "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_CONTINUATION_OR_WEIL_COMPRESSION",
    "A4_qualification": "RECURRENT_FINITE_PERMUTATION_SPECTRUM_IS_A_FORMAL_HINT_ONLY_NOT_A_TARGET_QUANTIZATION",
    "route_b_invocation_allowed": False,
}

EXPECTED_SCOPE_FLAGS = {
    "used_target_zero_table": False,
    "used_target_prime_table": False,
    "used_arithmetic_local_data": False,
    "claimed_target_divisor_match": False,
    "claimed_target_functional_equation": False,
    "claimed_hilbert_polya": False,
    "claimed_global_reversor": False,
    "claimed_complete_transient_classification": False,
    "claimed_global_novelty": False,
    "route_b_invocation_allowed": False,
}

EXPECTED_SOURCE_REGISTRY = [
    {
        "key": "brandt_1982_cycles_partitions",
        "title": "Cycles of partitions",
        "authors": "Jorgen Brandt",
        "year": 1982,
        "journal": "Proceedings of the American Mathematical Society 85(3), 483--486",
        "doi": "10.1090/S0002-9939-1982-0656129-5",
        "role": "primary ownership for the cyclic-partition characterization and necklace model",
    },
    {
        "key": "akin_davis_1985_bulgarian_solitaire",
        "title": "Bulgarian Solitaire",
        "authors": "Ethan Akin and Morton Davis",
        "year": 1985,
        "journal": "The American Mathematical Monthly 92(4), 237--250",
        "doi": "10.1080/00029890.1985.11971590",
        "jstor_doi": "10.2307/2323643",
        "role": "classical dynamical treatment and recurrent-set background",
    },
]

EXPECTED_NONCLAIMS = [
    "novelty or priority for Brandt's recurrent classification, necklace parametrization, or Bulgarian-solitaire convergence theory",
    "a complete classification of transient functional trees, hitting times, or nilpotent Koopman Jordan blocks",
    "a global reversor for the noninvertible map on all partitions",
    "rational-prime semantics for deck sizes, partitions, binary words, cycle lengths, or partition numbers",
    "a target divisor, functional equation, counting law, continuation theorem, or Weil compression",
    "a self-adjoint Hilbert--Polya operator, Route-B authorization, external peer review, or acceptance score",
]


class Counter:
    def __init__(self) -> None:
        self.value = 0

    def check(self, condition: bool, message: str) -> None:
        self.value += 1
        if not condition:
            raise AssertionError(message)


def canonical_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def factors(n: int) -> list[int]:
    low, high = [], []
    divisor = 1
    while divisor * divisor <= n:
        if n % divisor == 0:
            low.append(divisor)
            if divisor * divisor != n:
                high.append(n // divisor)
        divisor += 1
    return low + high[::-1]


def mu(n: int) -> int:
    sign = 1
    candidate = 2
    remaining = n
    while candidate * candidate <= remaining:
        if remaining % candidate == 0:
            remaining //= candidate
            sign = -sign
            if remaining % candidate == 0:
                return 0
            while remaining % candidate == 0:
                remaining //= candidate
        candidate += 1
    if remaining > 1:
        sign = -sign
    return sign


def decompose(n: int) -> tuple[int, int]:
    length = 2
    while length * (length + 1) // 2 <= n:
        length += 1
    return length, n - length * (length - 1) // 2


def independent_partition_number(n: int) -> int:
    values = [1] + [0] * n
    for summand in range(1, n + 1):
        for target in range(summand, n + 1):
            values[target] += values[target - summand]
    return values[n]


def binary_words(length: int, weight: int) -> list[str]:
    return sorted("".join(map(str, bits)) for bits in product((0, 1), repeat=length) if sum(bits) == weight)


def encode(word: str) -> list[int]:
    length = len(word)
    padded = [length - position - 1 + (letter == "1") for position, letter in enumerate(word)]
    return [int(part) for part in padded if part]


def shift_right(word: str, steps: int = 1) -> str:
    steps %= len(word)
    if not steps:
        return word
    return word[len(word) - steps:] + word[:len(word) - steps]


def mirror(word: str) -> str:
    return word[0] + word[:0:-1]


def predicted_fixed(length: int, weight: int, iterate: int) -> int:
    number_of_index_cycles = gcd(length, iterate)
    index_cycle_length = length // number_of_index_cycles
    if weight % index_cycle_length:
        return 0
    return comb(number_of_index_cycles, weight // index_cycle_length)


def independent_word_cycles(words: list[str]) -> list[dict]:
    unused = set(words)
    result: list[dict] = []
    while unused:
        start = min(unused)
        orbit = [start]
        next_word = shift_right(start)
        while next_word != start:
            orbit.append(next_word)
            next_word = shift_right(next_word)
        least = min(orbit)
        offset = orbit.index(least)
        orbit = orbit[offset:] + orbit[:offset]
        unused -= set(orbit)
        result.append({
            "canonical_word": least,
            "length": len(orbit),
            "words": orbit,
            "partitions": [encode(word) for word in orbit],
        })
    return sorted(result, key=lambda item: (item["length"], item["canonical_word"]))


def partitions(total: int, ceiling: int | None = None):
    """Generate descending partitions by a recursion unlike the word model."""
    if total == 0:
        yield ()
        return
    maximum = total if ceiling is None else min(total, ceiling)
    for first in range(maximum, 0, -1):
        for tail in partitions(total - first, first):
            yield (first,) + tail


def bulgarian(partition: tuple[int, ...]) -> tuple[int, ...]:
    new_pile = len(partition)
    retained = [part - 1 for part in partition if part > 1]
    return tuple(sorted([new_pile] + retained, reverse=True))


def direct_cycles(all_partitions: list[tuple[int, ...]]) -> tuple[list[list[tuple[int, ...]]], list[tuple[int, ...]]]:
    index = {partition: position for position, partition in enumerate(all_partitions)}
    successor = [index[bulgarian(partition)] for partition in all_partitions]
    done = [False] * len(all_partitions)
    cycles: list[list[tuple[int, ...]]] = []
    for start in range(len(all_partitions)):
        if done[start]:
            continue
        path: list[int] = []
        location: dict[int, int] = {}
        current = start
        while not done[current] and current not in location:
            location[current] = len(path)
            path.append(current)
            current = successor[current]
        if current in location:
            cycle_indices = path[location[current]:]
            cycles.append([all_partitions[position] for position in cycle_indices])
        for position in path:
            done[position] = True
    cycle_nodes = sorted(partition for cycle in cycles for partition in cycle)
    return cycles, cycle_nodes


def main() -> None:
    evidence_path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    data = json.loads(evidence_path.read_text())
    count = Counter()

    count.check(data.get("payload_sha256") == canonical_hash(data), "payload hash mismatch")
    count.check(data.get("schema") == "HCS-C190-v1", "schema")
    count.check(data.get("candidate_id") == "HCS-C190", "candidate")
    count.check(data.get("date_utc") == "2026-08-27", "date")
    count.check(data.get("source_commit") == EXPECTED_COMMIT, "commit")
    count.check(data.get("scope_literal") == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    count.check(data.get("evaluator") == {
        "path": "flow_systems/skills/route-a-evaluator.md",
        "version": "0.2.0",
        "sha256": EXPECTED_EVALUATOR,
    }, "evaluator")
    count.check(data.get("source_lock") == EXPECTED_SOURCE_LOCK, "source lock")
    count.check(data.get("attribution") == EXPECTED_ATTRIBUTION, "attribution")
    count.check(data.get("theorem") == EXPECTED_THEOREM, "theorem")
    count.check(data.get("progress_and_boundary") == EXPECTED_BOUNDARY, "boundary")
    count.check(data.get("route_a") == EXPECTED_ROUTE_A, "route A")
    count.check(data.get("scope_flags") == EXPECTED_SCOPE_FLAGS, "scope flags")
    count.check(data.get("source_registry") == EXPECTED_SOURCE_REGISTRY, "sources")
    count.check(data.get("nonclaims") == EXPECTED_NONCLAIMS, "nonclaims")

    replay = data["finite_replay"]
    count.check(replay["n_min"] == 1, "n min")
    count.check(replay["n_max"] == 40, "n max")
    count.check(replay["system_row_count"] == 40, "system count")
    count.check(len(replay["rows"]) == 40, "system row length")
    count.check(replay["partition_population"] == 215307, "partition population")
    count.check(replay["word_partition_pair_count"] == 757, "word population")
    count.check(replay["cycle_row_count"] == 114, "cycle population")
    count.check(replay["fixed_row_count"] == 248, "fixed row population")
    count.check(replay["period_row_count"] == 117, "period row population")
    count.check(replay["spectral_row_count"] == 248, "spectral row population")

    direct_partition_total = 0
    direct_recurrent_total = 0
    direct_cycle_total = 0

    for expected_n, row in enumerate(replay["rows"], start=1):
        length, weight = decompose(expected_n)
        word_list = binary_words(length, weight)
        recurrent = comb(length, weight)
        p_n = independent_partition_number(expected_n)

        count.check(row["N"] == expected_n, f"N {expected_n}")
        count.check(row["k"] == length, f"k {expected_n}")
        count.check(row["r"] == weight, f"r {expected_n}")
        count.check(row["triangular_base"] == length * (length - 1) // 2, f"triangle {expected_n}")
        count.check(row["partition_number"] == p_n, f"p(N) {expected_n}")
        count.check(row["recurrent_count"] == recurrent, f"recurrent {expected_n}")
        count.check(row["transient_count"] == p_n - recurrent, f"transient {expected_n}")
        count.check(row["full_koopman_zero_algebraic_multiplicity"] == p_n - recurrent, f"zero multiplicity {expected_n}")
        count.check(row["phase_reflection_formula_count"] == length, f"reflection formulas {expected_n}")
        count.check(row["triangular_boundary"] == (weight == 0), f"triangular flag {expected_n}")

        expected_pairs = []
        for word in word_list:
            reflected = mirror(word)
            expected_pairs.append({
                "word": word,
                "partition": encode(word),
                "next_word": shift_right(word),
                "next_partition": encode(shift_right(word)),
                "reflection_word": reflected,
                "reflection_partition": encode(reflected),
            })
            count.check(mirror(mirror(word)) == word, f"Q^2 {expected_n} {word}")
            count.check(mirror(shift_right(mirror(word))) == shift_right(word, -1), f"QrhoQ {expected_n} {word}")
            for phase in range(length):
                phase_reflected = shift_right(mirror(word), phase)
                count.check(shift_right(mirror(phase_reflected), phase) == word, f"phase reflection {expected_n} {word} {phase}")
        count.check(row["word_partition_pairs"] == expected_pairs, f"word pairs {expected_n}")

        word_cycle_rows = independent_word_cycles(word_list)
        count.check(row["cycles"] == word_cycle_rows, f"word cycles {expected_n}")
        word_cycle_counts: dict[int, int] = {}
        for item in word_cycle_rows:
            word_cycle_counts[item["length"]] = word_cycle_counts.get(item["length"], 0) + 1
            count.check(item["length"] in factors(length), f"cycle divides k {expected_n}")
            count.check(len(item["words"]) == item["length"], f"cycle word length {expected_n}")
            count.check(len(item["partitions"]) == item["length"], f"cycle partition length {expected_n}")

        count.check(len(row["fixed_rows"]) == length, f"fixed length {expected_n}")
        for residue, fixed_row in enumerate(row["fixed_rows"]):
            positive = length if residue == 0 else residue
            expected_fixed = predicted_fixed(length, weight, positive)
            count.check(fixed_row["iterate_mod_k"] == residue, f"fixed residue {expected_n} {residue}")
            count.check(fixed_row["positive_iterate_representative"] == positive, f"fixed representative {expected_n} {residue}")
            count.check(fixed_row["gcd_k_iterate"] == gcd(length, positive), f"fixed gcd {expected_n} {residue}")
            count.check(fixed_row["fixed_count"] == expected_fixed, f"fixed formula {expected_n} {residue}")
            count.check(sum(shift_right(word, positive) == word for word in word_list) == expected_fixed, f"fixed word enumeration {expected_n} {residue}")

        period_lookup = {}
        count.check(len(row["period_rows"]) == len(factors(length)), f"period row length {expected_n}")
        for period_row, period in zip(row["period_rows"], factors(length)):
            exact = sum(mu(period // divisor) * predicted_fixed(length, weight, divisor) for divisor in factors(period))
            cycles_of_period = exact // period
            count.check(period_row["period"] == period, f"period coordinate {expected_n} {period}")
            count.check(period_row["fixed_at_period"] == predicted_fixed(length, weight, period), f"period fixed {expected_n} {period}")
            count.check(period_row["exact_period_count"] == exact, f"period exact {expected_n} {period}")
            count.check(period_row["cycle_count"] == cycles_of_period, f"period cycles {expected_n} {period}")
            count.check(cycles_of_period == word_cycle_counts.get(period, 0), f"word period cycles {expected_n} {period}")
            period_lookup[period] = cycles_of_period
        count.check(sum(period * cycles for period, cycles in period_lookup.items()) == recurrent, f"period population {expected_n}")

        count.check(len(row["spectral_rows"]) == length, f"spectral length {expected_n}")
        spectral_sum = 0
        for exponent, spectral_row in enumerate(row["spectral_rows"]):
            multiplicity = sum(cycles for period, cycles in period_lookup.items() if exponent * period % length == 0)
            count.check(spectral_row["root_exponent_mod_k"] == exponent, f"spectral exponent {expected_n} {exponent}")
            count.check(spectral_row["multiplicity"] == multiplicity, f"spectral multiplicity {expected_n} {exponent}")
            spectral_sum += multiplicity
        count.check(spectral_sum == recurrent, f"spectral total {expected_n}")

        nonzero = [(period, cycles) for period, cycles in period_lookup.items() if cycles]
        count.check(row["zeta_factors"] == [{"period": period, "exponent": -cycles} for period, cycles in nonzero], f"zeta {expected_n}")
        count.check(row["koopman_determinant_factors"] == [{"period": period, "exponent": cycles} for period, cycles in nonzero], f"determinant {expected_n}")

        # Completely separate full-partition oracle.
        all_partitions = list(partitions(expected_n))
        all_partition_set = set(all_partitions)
        direct_partition_total += len(all_partitions)
        count.check(len(all_partitions) == p_n, f"direct partition count {expected_n}")
        for partition in all_partitions:
            count.check(sum(partition) == expected_n, f"partition sum {expected_n}")
            count.check(all(partition[i] >= partition[i + 1] for i in range(len(partition) - 1)), f"partition order {expected_n}")
            count.check(bulgarian(partition) in all_partition_set, f"map closure {expected_n}")

        cycles, cycle_nodes = direct_cycles(all_partitions)
        expected_cycle_nodes = sorted(tuple(encode(word)) for word in word_list)
        direct_recurrent_total += len(cycle_nodes)
        direct_cycle_total += len(cycles)
        count.check(cycle_nodes == expected_cycle_nodes, f"direct recurrent set {expected_n}")
        count.check(sorted(len(cycle) for cycle in cycles) == sorted(item["length"] for item in word_cycle_rows), f"direct cycle lengths {expected_n}")
        count.check(len(cycles) == len(word_cycle_rows), f"direct cycle count {expected_n}")

        for pair in expected_pairs:
            partition = tuple(pair["partition"])
            count.check(partition in all_partition_set, f"encoded partition exists {expected_n}")
            count.check(bulgarian(partition) == tuple(pair["next_partition"]), f"T phi=phi rho {expected_n}")

        for fixed_row in row["fixed_rows"]:
            iterate = fixed_row["positive_iterate_representative"]
            direct_fixed = 0
            for partition in all_partitions:
                image = partition
                for _ in range(iterate):
                    image = bulgarian(image)
                direct_fixed += image == partition
            count.check(direct_fixed == fixed_row["fixed_count"], f"full-map fixed count {expected_n} {iterate}")

    count.check(direct_partition_total == replay["partition_population"], "direct partition population total")
    count.check(direct_recurrent_total == replay["word_partition_pair_count"], "direct recurrent population total")
    count.check(direct_cycle_total == replay["cycle_row_count"], "direct cycle population total")

    n8 = replay["rows"][7]
    count.check([item["fixed_count"] for item in n8["fixed_rows"]] == [6, 0, 2, 0], "N=8 fixed sentinel")
    count.check([(item["period"], item["cycle_count"]) for item in n8["period_rows"] if item["cycle_count"]] == [(2, 1), (4, 1)], "N=8 cycle sentinel")
    count.check(n8["full_koopman_zero_algebraic_multiplicity"] == 16, "N=8 zero sentinel")

    print(json.dumps({
        "status": "C190_CHECKER_PASS",
        "assertions": count.value,
        "direct_partitions": direct_partition_total,
        "direct_recurrent_partitions": direct_recurrent_total,
        "direct_cycles": direct_cycle_total,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
