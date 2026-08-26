#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C170."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "results/c170_kac_ring_evidence.json"
checks = 0


def require(condition: bool, message: str) -> None:
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def make_markers(n: int, mask: int) -> tuple[int, ...]:
    return tuple(1 if mask & (1 << j) else -1 for j in range(n))


def product(values: tuple[int, ...]) -> int:
    answer = 1
    for value in values:
        answer *= value
    return answer


def listing(n: int) -> list[tuple[int, int]]:
    return [(j, sign) for j in range(n) for sign in (-1, 1)]


def forward(state: tuple[int, int], eps: tuple[int, ...]) -> tuple[int, int]:
    j, sign = state
    return (j + 1) % len(eps), eps[j] * sign


def backward(state: tuple[int, int], eps: tuple[int, ...]) -> tuple[int, int]:
    j, sign = state
    old_j = (j - 1) % len(eps)
    return old_j, eps[old_j] * sign


def gauge_prefix(eps: tuple[int, ...]) -> tuple[int, ...]:
    values = [1]
    for j in range(1, len(eps)):
        values.append(values[-1] * eps[j - 1])
    return tuple(values)


def reflect(state: tuple[int, int], eps: tuple[int, ...]) -> tuple[int, int]:
    n = len(eps)
    eta = product(eps)
    g = gauge_prefix(eps)
    j, sign = state
    q = g[j] * sign
    if eta == 1:
        new_j, new_q = (-j) % n, q
    else:
        coordinate = j if q == 1 else n + j
        reflected = (-coordinate) % (2 * n)
        if reflected < n:
            new_j, new_q = reflected, 1
        else:
            new_j, new_q = reflected - n, -1
    return new_j, g[new_j] * new_q


def perm_for(eps: tuple[int, ...]) -> list[int]:
    state_list = listing(len(eps))
    lookup = {state: index for index, state in enumerate(state_list)}
    return [lookup[forward(state, eps)] for state in state_list]


def cycles(perm: list[int]) -> list[int]:
    unseen = set(range(len(perm)))
    answer = []
    while unseen:
        start = min(unseen)
        current = start
        length = 0
        while current in unseen:
            unseen.remove(current)
            current = perm[current]
            length += 1
        answer.append(length)
    return sorted(answer)


def fixed(perm: list[int], exponent: int) -> int:
    answer = 0
    for initial in range(len(perm)):
        current = initial
        for _ in range(exponent):
            current = perm[current]
        answer += current == initial
    return answer


def expected_brute(n: int) -> dict:
    plus = minus = plus_good = minus_good = 0
    states_checked = fixed_checks = reversor_checks = 0
    signatures = []
    for mask in range(1 << n):
        eps = make_markers(n, mask)
        eta = product(eps)
        if eta == 1:
            plus += 1
        else:
            minus += 1
        length = n if eta == 1 else 2 * n
        cycle_count = 2 if eta == 1 else 1
        perm = perm_for(eps)
        lens = cycles(perm)
        require(lens == [length] * cycle_count, f"cycle classification {n}:{mask}")
        if eta == 1:
            plus_good += 1
        else:
            minus_good += 1
        state_list = listing(n)
        lookup = {state: index for index, state in enumerate(state_list)}
        rperm = []
        for state in state_list:
            image = reflect(state, eps)
            rperm.append(lookup[image])
            require(reflect(image, eps) == state, f"R square {n}:{mask}:{state}")
            require(reflect(forward(reflect(state, eps), eps), eps) == backward(state, eps), f"RTR {n}:{mask}:{state}")
            reversor_checks += 2
        for exponent in range(1, 2 * n + 1):
            require(fixed(perm, exponent) == (2 * n if exponent % length == 0 else 0), f"fixed {n}:{mask}:{exponent}")
            fixed_checks += 1
        states_checked += len(state_list)
        signatures.append(f"{n}:{mask}:{eta}:{length}:{','.join(map(str,lens))}:{','.join(map(str,rperm))}")
    return {
        "N": n, "marker_configurations": 1 << n,
        "eta_plus_configurations": plus, "eta_minus_configurations": minus,
        "eta_plus_correct_classifications": plus_good,
        "eta_minus_correct_classifications": minus_good,
        "states_checked": states_checked, "fixed_time_checks": fixed_checks,
        "reversor_identity_checks": reversor_checks,
        "configuration_signature_sha256": sha256("\n".join(signatures).encode()).hexdigest(),
    }


def main() -> None:
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT
    data = json.loads(path.read_text())
    body = dict(data)
    claimed = body.pop("payload_sha256")
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    require(sha256(raw).hexdigest() == claimed, "payload hash")
    require(set(data) == {
        "schema", "candidate_id", "date_utc", "source_commit", "scope_literal",
        "source_lock", "classification_theorem", "zeta_and_koopman_theorem",
        "gauge_and_reversal_theorem", "finite_replay", "progress_and_boundary",
        "route_a", "scope_flags", "nonclaims", "payload_sha256",
    }, "top-level closure")
    require(data["schema"] == "HCS-C170-v1", "schema")
    require(data["candidate_id"] == "HCS-C170", "candidate")
    require(data["date_utc"] == "2026-08-26", "date")
    require(data["source_commit"] == "ee8af7b8e265fa4f901d5ed2d1c2edd51475b06f", "source commit")
    require(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")

    lock = data["source_lock"]
    require(set(lock) == {"object", "family", "arithmetic_origin", "clock", "normalization", "determinant_convention", "cutoff", "precision", "allowed_data", "forbidden_data"}, "lock closure")
    require("Kac ring" in lock["object"] and "epsilon_j" in lock["object"], "object")
    require("every N>=1" in lock["family"] and "every marker configuration" in lock["family"], "family")
    require(lock["clock"] == "one site advance with the marker at the departed site", "clock")
    require("labelled states" in lock["normalization"] and "geometric cycles" in lock["normalization"], "normalization")
    require("Artin--Mazur" in lock["determinant_convention"] and "det(I-zU_T)" in lock["determinant_convention"], "determinant")
    require("all-parameter theorem" in lock["cutoff"] and "N<=10" in lock["cutoff"], "cutoff")
    require(lock["precision"] == "exact signs, permutations, integers, and symbolic polynomials", "precision")
    require("no intrinsic prime semantics" in lock["arithmetic_origin"] and "sign product eta" in lock["allowed_data"], "arithmetic origin and allowed data")
    require("target zero or prime tables" in lock["forbidden_data"] and "Route-B" in lock["forbidden_data"], "forbidden")

    theorem = data["classification_theorem"]
    require(set(theorem) == {"marker_invariant", "N_step_law", "eta_plus", "eta_minus", "fixed_counts", "all_markers"}, "classification closure")
    require("product_" in theorem["marker_invariant"] and "eta" in theorem["marker_invariant"], "eta")
    require(theorem["N_step_law"] == "T^N(j,s)=(j,eta*s)", "N-step")
    require("exact period N" in theorem["eta_plus"] and "two N-cycles" in theorem["eta_plus"], "eta plus")
    require("exact period 2N" in theorem["eta_minus"] and "one 2N-cycle" in theorem["eta_minus"], "eta minus")
    require("#Fix(T^n)=2N" in theorem["fixed_counts"] and "otherwise" in theorem["fixed_counts"], "fixed theorem")
    require("only through eta" in theorem["all_markers"] and "N=1" in theorem["all_markers"], "all markers")

    zeta = data["zeta_and_koopman_theorem"]
    require(set(zeta) == {"cycle_count", "zeta", "koopman", "root_spectrum", "self_adjoint_boundary"}, "zeta closure")
    require(zeta["cycle_count"] == "c=2N/L, hence c=2 for eta=+1 and c=1 for eta=-1", "cycle count")
    require(zeta["zeta"] == "zeta_T(z)=(1-z^L)^(-c)", "zeta")
    require("same-clock permutation unitary" in zeta["koopman"] and "zeta_T(z)^(-1)" in zeta["koopman"], "Koopman")
    require("L-th roots of unity" in zeta["root_spectrum"] and "multiplicity c" in zeta["root_spectrum"], "roots")
    require("self-adjoint exactly when L<=2" in zeta["self_adjoint_boundary"] and "not a Hilbert--Polya" in zeta["self_adjoint_boundary"], "self-adjoint boundary")

    gauge = data["gauge_and_reversal_theorem"]
    require(set(gauge) == {"gauge", "normal_form", "unfolding", "reversor", "antiunitary"}, "gauge closure")
    require("g_0=1" in gauge["gauge"] and "q=g_j*s" in gauge["gauge"], "gauge")
    require("eta*q" in gauge["normal_form"], "normal form")
    require("Z/(2N)Z" in gauge["unfolding"] and "t->t+1" in gauge["unfolding"], "unfolding")
    require("pull back through the gauge" in gauge["reversor"], "reversor")
    require("Theta*U_T*Theta=U_T^(-1)" in gauge["antiunitary"], "antiunitary")

    replay = data["finite_replay"]
    require(set(replay) == {"class_n_max", "brute_n_max", "class_rows", "brute_rows", "class_row_count", "enumerated_marker_configurations", "enumerated_states", "fixed_time_checks", "reversor_identity_checks"}, "replay closure")
    require((replay["class_n_max"], replay["brute_n_max"]) == (24, 10), "replay bounds")
    expected_classes = []
    for n in range(1, 25):
        for eta in (1, -1):
            length = n if eta == 1 else 2 * n
            count = 2 * n // length
            expected_classes.append({
                "N": n, "eta": eta, "cycle_length_L": length,
                "cycle_count_c": count, "cycle_lengths": [length] * count,
                "fixed_rows": [{"time_n": time, "fixed_points": 2 * n if time % length == 0 else 0} for time in range(1, 2 * n + 1)],
                "zeta": f"(1-z^{length})^(-{count})",
                "koopman_determinant": f"(1-z^{length})^{count}",
                "root_spectrum": f"all {length}-th roots of unity, each with multiplicity {count}",
            })
    require(replay["class_rows"] == expected_classes, "class rows")
    require(replay["class_row_count"] == len(expected_classes) == 48, "class count")
    for row in replay["class_rows"]:
        require(set(row) == {"N", "eta", "cycle_length_L", "cycle_count_c", "cycle_lengths", "fixed_rows", "zeta", "koopman_determinant", "root_spectrum"}, f"class closure {row['N']}:{row['eta']}")
        require(sum(row["cycle_lengths"]) == 2 * row["N"], f"state partition {row['N']}:{row['eta']}")
        require(row["cycle_count_c"] * row["cycle_length_L"] == 2 * row["N"], f"cycle identity {row['N']}:{row['eta']}")
        for fixed_row in row["fixed_rows"]:
            expected = 2 * row["N"] if fixed_row["time_n"] % row["cycle_length_L"] == 0 else 0
            require(fixed_row["fixed_points"] == expected, f"fixed class {row['N']}:{row['eta']}:{fixed_row['time_n']}")

    expected_brute_rows = [expected_brute(n) for n in range(1, 11)]
    require(replay["brute_rows"] == expected_brute_rows, "brute rows")
    require(replay["enumerated_marker_configurations"] == sum(1 << n for n in range(1, 11)) == 2046, "marker total")
    require(replay["enumerated_states"] == sum(row["states_checked"] for row in expected_brute_rows), "state total")
    require(replay["fixed_time_checks"] == sum(row["fixed_time_checks"] for row in expected_brute_rows), "fixed check total")
    require(replay["reversor_identity_checks"] == sum(row["reversor_identity_checks"] for row in expected_brute_rows), "reversor check total")

    progress = data["progress_and_boundary"]
    require(set(progress) == {"progress", "route_a_obstruction", "sentinel_boundary"}, "progress closure")
    require("every marker configuration" in progress["progress"] and "complete cycle" in progress["progress"], "progress")
    require("finite and exactly reducible" in progress["route_a_obstruction"] and "no intrinsic prime semantics" in progress["route_a_obstruction"], "obstruction")
    require("regression sentinel only" in progress["sentinel_boundary"] and "rests on" in progress["sentinel_boundary"], "sentinel")

    route = data["route_a"]
    require(set(route) == {"tuple", "overall", "A0_qualification", "A1_qualification", "A2_qualification", "A3_qualification", "A4_qualification", "route_b_invocation_allowed"}, "route closure")
    require(route["tuple"] == ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"], "route tuple")
    require(route["overall"] == "ROUTE_A_REJECTED", "overall")
    require(route["A0_qualification"] == "NO_INTRINSIC_ARITHMETIC_ORIGIN_OR_PRIME_CORRESPONDENCE", "A0")
    require("ALL_N_ALL_MARKER" in route["A1_qualification"] and "TOY_DYNAMICS" in route["A1_qualification"], "A1")
    require(route["A2_qualification"] == "EXACT_FINITE_SOURCE_ZETA_WITH_NO_TARGET_DIVISOR_COMPARISON", "A2")
    require(route["A3_qualification"] == "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_CONTINUATION_COMPARISON", "A3")
    require(route["A4_qualification"] == "SAME_CLOCK_FINITE_KOOPMAN_UNITARY_WITH_EXPLICIT_ANTIUNITARY_REVERSAL", "A4")
    require(route["route_b_invocation_allowed"] is False, "Route B")

    flags = data["scope_flags"]
    require(set(flags) == {"used_target_zero_table", "used_target_prime_table", "used_arithmetic_local_data", "claimed_target_divisor_match", "claimed_target_functional_equation", "claimed_hilbert_polya", "route_b_invocation_allowed"}, "flags closure")
    require(not any(flags.values()), "scope flags false")
    require(len(data["nonclaims"]) == 5, "nonclaim count")
    joined = " ".join(data["nonclaims"])
    require("Hilbert--Polya" in joined and "external peer review" in joined and "prime-like semantics" in joined, "nonclaim boundary")
    print(json.dumps({"status": "C170_INDEPENDENT_CHECK_PASS", "assertions": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
