#!/usr/bin/env python3
"""Produce the exact HCS-C170 Kac-ring cycle-classification certificate."""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c170_kac_ring_evidence.json"
SOURCE_COMMIT = "ee8af7b8e265fa4f901d5ed2d1c2edd51475b06f"
N_MAX = 24
BRUTE_N_MAX = 10


def canonical_bytes(data: dict) -> bytes:
    body = dict(data)
    body.pop("payload_sha256", None)
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def markers(n: int, mask: int) -> list[int]:
    return [1 if (mask >> j) & 1 else -1 for j in range(n)]


def eta_of(eps: list[int]) -> int:
    answer = 1
    for value in eps:
        answer *= value
    return answer


def states(n: int) -> list[tuple[int, int]]:
    return [(j, s) for j in range(n) for s in (-1, 1)]


def step(state: tuple[int, int], eps: list[int]) -> tuple[int, int]:
    j, s = state
    return ((j + 1) % len(eps), eps[j] * s)


def gauge(eps: list[int]) -> list[int]:
    result = [1]
    for j in range(1, len(eps)):
        result.append(result[-1] * eps[j - 1])
    return result


def reversor(state: tuple[int, int], eps: list[int]) -> tuple[int, int]:
    n = len(eps)
    eta = eta_of(eps)
    g = gauge(eps)
    j, s = state
    q = g[j] * s
    if eta == 1:
        new_j = (-j) % n
        new_q = q
    else:
        t = j if q == 1 else n + j
        reflected = (-t) % (2 * n)
        if reflected < n:
            new_j, new_q = reflected, 1
        else:
            new_j, new_q = reflected - n, -1
    return new_j, g[new_j] * new_q


def inverse_step(state: tuple[int, int], eps: list[int]) -> tuple[int, int]:
    j, s = state
    previous = (j - 1) % len(eps)
    return previous, eps[previous] * s


def permutation(eps: list[int]) -> list[int]:
    listing = states(len(eps))
    position = {state: index for index, state in enumerate(listing)}
    return [position[step(state, eps)] for state in listing]


def cycle_lengths(perm: list[int]) -> list[int]:
    seen: set[int] = set()
    lengths = []
    for start in range(len(perm)):
        if start in seen:
            continue
        current = start
        length = 0
        while current not in seen:
            seen.add(current)
            current = perm[current]
            length += 1
        lengths.append(length)
    return sorted(lengths)


def fixed_count(perm: list[int], exponent: int) -> int:
    count = 0
    for start in range(len(perm)):
        current = start
        for _ in range(exponent):
            current = perm[current]
        count += current == start
    return count


def brute_row(n: int) -> dict:
    eta_counts = {1: 0, -1: 0}
    classification_counts = {1: 0, -1: 0}
    state_checks = 0
    fixed_checks = 0
    reversor_checks = 0
    signatures = []
    for mask in range(1 << n):
        eps = markers(n, mask)
        eta = eta_of(eps)
        eta_counts[eta] += 1
        perm = permutation(eps)
        expected_l = n if eta == 1 else 2 * n
        expected_c = 2 if eta == 1 else 1
        lengths = cycle_lengths(perm)
        assert lengths == [expected_l] * expected_c
        classification_counts[eta] += 1
        listing = states(n)
        rperm = []
        pos = {state: index for index, state in enumerate(listing)}
        for state in listing:
            rstate = reversor(state, eps)
            rperm.append(pos[rstate])
            assert reversor(rstate, eps) == state
            assert reversor(step(reversor(state, eps), eps), eps) == inverse_step(state, eps)
            reversor_checks += 2
        for exponent in range(1, 2 * n + 1):
            got = fixed_count(perm, exponent)
            expected = 2 * n if exponent % expected_l == 0 else 0
            assert got == expected
            fixed_checks += 1
        state_checks += len(listing)
        signatures.append(f"{n}:{mask}:{eta}:{expected_l}:{','.join(map(str,lengths))}:{','.join(map(str,rperm))}")
    digest = sha256("\n".join(signatures).encode()).hexdigest()
    return {
        "N": n,
        "marker_configurations": 1 << n,
        "eta_plus_configurations": eta_counts[1],
        "eta_minus_configurations": eta_counts[-1],
        "eta_plus_correct_classifications": classification_counts[1],
        "eta_minus_correct_classifications": classification_counts[-1],
        "states_checked": state_checks,
        "fixed_time_checks": fixed_checks,
        "reversor_identity_checks": reversor_checks,
        "configuration_signature_sha256": digest,
    }


def build() -> dict:
    class_rows = []
    for n in range(1, N_MAX + 1):
        for eta in (1, -1):
            length = n if eta == 1 else 2 * n
            cycles = 2 * n // length
            class_rows.append({
                "N": n,
                "eta": eta,
                "cycle_length_L": length,
                "cycle_count_c": cycles,
                "cycle_lengths": [length] * cycles,
                "fixed_rows": [
                    {"time_n": time, "fixed_points": 2 * n if time % length == 0 else 0}
                    for time in range(1, 2 * n + 1)
                ],
                "zeta": f"(1-z^{length})^(-{cycles})",
                "koopman_determinant": f"(1-z^{length})^{cycles}",
                "root_spectrum": f"all {length}-th roots of unity, each with multiplicity {cycles}",
            })
    brute_rows = [brute_row(n) for n in range(1, BRUTE_N_MAX + 1)]
    data = {
        "schema": "HCS-C170-v1",
        "candidate_id": "HCS-C170",
        "date_utc": "2026-08-26",
        "source_commit": SOURCE_COMMIT,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_lock": {
            "object": "Kac ring T(j,s)=(j+1,epsilon_j*s) on Z/NZ times {+1,-1}",
            "family": "every N>=1 and every marker configuration epsilon in {+1,-1}^N",
            "arithmetic_origin": "none; N and the arbitrary binary marker word are kinetic source inputs with no intrinsic prime semantics",
            "clock": "one site advance with the marker at the departed site",
            "normalization": "labelled states first, then least periods and geometric cycles",
            "determinant_convention": "finite Artin--Mazur zeta and same-clock Koopman determinant det(I-zU_T)",
            "cutoff": "all-parameter theorem; class ledger N<=24 and exhaustive marker enumeration N<=10",
            "precision": "exact signs, permutations, integers, and symbolic polynomials",
            "allowed_data": "the frozen marker word and source-derived sign product eta",
            "forbidden_data": "target zero or prime tables, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya operators, and Route-B inputs",
        },
        "classification_theorem": {
            "marker_invariant": "eta=product_(j=0)^(N-1) epsilon_j in {+1,-1}",
            "N_step_law": "T^N(j,s)=(j,eta*s)",
            "eta_plus": "if eta=+1, all 2N states have exact period N and form two N-cycles",
            "eta_minus": "if eta=-1, all 2N states have exact period 2N and form one 2N-cycle",
            "fixed_counts": "with L=N for eta=+1 and L=2N for eta=-1, #Fix(T^n)=2N if L divides n and 0 otherwise",
            "all_markers": "the theorem depends on the marker configuration only through eta and includes N=1",
        },
        "zeta_and_koopman_theorem": {
            "cycle_count": "c=2N/L, hence c=2 for eta=+1 and c=1 for eta=-1",
            "zeta": "zeta_T(z)=(1-z^L)^(-c)",
            "koopman": "on l2 of the 2N states, U_T is the same-clock permutation unitary and det(I-zU_T)=(1-z^L)^c=zeta_T(z)^(-1)",
            "root_spectrum": "the eigenvalues are all L-th roots of unity, each with multiplicity c",
            "self_adjoint_boundary": "U_T is self-adjoint exactly when L<=2; this is a finite kinetic toy model, not a Hilbert--Polya construction",
        },
        "gauge_and_reversal_theorem": {
            "gauge": "g_0=1, g_j=product_(r<j)epsilon_r, q=g_j*s",
            "normal_form": "the gauge coordinate advances j by one, preserves q off the wrap, and sends q to eta*q at the wrap",
            "unfolding": "for eta=-1, psi(j,q)=j when q=+1 and N+j when q=-1 conjugates T to t->t+1 on Z/(2N)Z",
            "reversor": "reflect j to -j in each eta=+1 cycle, or t to -t in the eta=-1 unfolded cycle, then pull back through the gauge",
            "antiunitary": "Theta f=conjugate(f after R) is involutive and Theta*U_T*Theta=U_T^(-1)",
        },
        "finite_replay": {
            "class_n_max": N_MAX,
            "brute_n_max": BRUTE_N_MAX,
            "class_rows": class_rows,
            "brute_rows": brute_rows,
            "class_row_count": len(class_rows),
            "enumerated_marker_configurations": sum(row["marker_configurations"] for row in brute_rows),
            "enumerated_states": sum(row["states_checked"] for row in brute_rows),
            "fixed_time_checks": sum(row["fixed_time_checks"] for row in brute_rows),
            "reversor_identity_checks": sum(row["reversor_identity_checks"] for row in brute_rows),
        },
        "progress_and_boundary": {
            "progress": "reduces every marker configuration at every N to the parity invariant eta and proves the complete cycle, fixed-count, zeta, determinant, spectrum, gauge, and reversal laws",
            "route_a_obstruction": "the cycles are finite and exactly reducible, with no intrinsic prime semantics, target divisor comparison, or target global analytic comparison",
            "sentinel_boundary": "the exhaustive N<=10 enumeration is a regression sentinel only; the all-N and all-marker statement rests on the N-step and gauge proofs",
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_NATURAL_QUANTIZATION"],
            "overall": "ROUTE_A_REJECTED",
            "A0_qualification": "NO_INTRINSIC_ARITHMETIC_ORIGIN_OR_PRIME_CORRESPONDENCE",
            "A1_qualification": "ALL_N_ALL_MARKER_PRIMITIVE_CYCLE_CLASSIFICATION_BUT_FINITE_REDUCIBLE_TOY_DYNAMICS",
            "A2_qualification": "EXACT_FINITE_SOURCE_ZETA_WITH_NO_TARGET_DIVISOR_COMPARISON",
            "A3_qualification": "NO_TARGET_FUNCTIONAL_EQUATION_COUNTING_LAW_OR_CONTINUATION_COMPARISON",
            "A4_qualification": "SAME_CLOCK_FINITE_KOOPMAN_UNITARY_WITH_EXPLICIT_ANTIUNITARY_REVERSAL",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "used_target_zero_table": False,
            "used_target_prime_table": False,
            "used_arithmetic_local_data": False,
            "claimed_target_divisor_match": False,
            "claimed_target_functional_equation": False,
            "claimed_hilbert_polya": False,
            "route_b_invocation_allowed": False,
        },
        "nonclaims": [
            "prime-like semantics for the finite Kac-ring cycles",
            "a target divisor, functional equation, counting law, or continuation match",
            "arithmetic local factors, Euler factors, root numbers, automorphy, or target spectral data",
            "a Hilbert--Polya operator or Route-B authorization",
            "novelty priority, external peer review, or an independent error process",
        ],
    }
    data["payload_sha256"] = sha256(canonical_bytes(data)).hexdigest()
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": "C170_PRODUCER_PASS", "class_rows": data["finite_replay"]["class_row_count"],
        "marker_configurations": data["finite_replay"]["enumerated_marker_configurations"],
        "payload_sha256": data["payload_sha256"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
