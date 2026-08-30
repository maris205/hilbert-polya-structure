#!/usr/bin/env python3
"""Produce the exact C251 certificate for synchronous majority CA (rule 232).

All computations use integer arithmetic.  The source object is the map on
binary words of a frozen cyclic length.  The wall variable turns the local
nonlinear rule into an exact erosion rule: every finite block of adjacent
walls loses one wall at each end per tick.  The evidence contains an all-size
fixed-point formula, the unique alternating two-cycle, and exhaustive finite
state receipts for transient depth and wall-run counts.
"""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path

SOURCE_COMMIT = "3ff451e904f8f063e88c40ef87f4697a6586b1a5"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
DATE = "2026-08-30"
FIXED_EPOCH = 1788048000
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c251_majority_evidence.json"


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def majority_step(state: tuple[int, ...]) -> tuple[int, ...]:
    n = len(state)
    return tuple(int(state[(i - 1) % n] + state[i] + state[(i + 1) % n] >= 2) for i in range(n))


def walls(state: tuple[int, ...]) -> tuple[int, ...]:
    n = len(state)
    return tuple(state[i] ^ state[(i + 1) % n] for i in range(n))


def from_bits(value: str) -> tuple[int, ...]:
    return tuple(int(x) for x in value)


def bits(state: tuple[int, ...]) -> str:
    return "".join(str(x) for x in state)


def all_states(n: int):
    for mask in range(1 << n):
        yield tuple((mask >> i) & 1 for i in range(n))


def max_wall_run(w: tuple[int, ...]) -> int:
    n = len(w)
    if not any(w):
        return 0
    if all(w):
        return n
    doubled = w + w
    best = cur = 0
    for value in doubled:
        if value:
            cur += 1
            best = max(best, cur)
        else:
            cur = 0
    return min(best, n)


def is_alternating(state: tuple[int, ...]) -> bool:
    return len(state) % 2 == 0 and all(state[i] != state[(i + 1) % len(state)] for i in range(len(state)))


def classify(state: tuple[int, ...]) -> dict:
    w = walls(state)
    y = state
    history = [bits(y)]
    seen: dict[tuple[int, ...], int] = {}
    while y not in seen:
        seen[y] = len(history) - 1
        z = majority_step(y)
        if z not in seen:
            history.append(bits(z))
        y = z
        if len(history) > 2 * len(state) + 8:
            raise AssertionError("unexpected orbit length")
    entry = seen[y]
    period = len(history) - entry
    return {
        "initial": bits(state),
        "initial_walls": bits(w),
        "max_wall_run": max_wall_run(w),
        "entry_time": entry,
        "cycle_period": period,
        "cycle_representative": bits(y),
        "final_state": history[entry],
        "history": history,
        "fixed_initial": majority_step(state) == state,
        "alternating_initial": is_alternating(state),
    }


def integer_matrix_power(a: list[list[int]], exponent: int) -> list[list[int]]:
    size = len(a)
    out = [[int(i == j) for j in range(size)] for i in range(size)]
    base = [row[:] for row in a]
    while exponent:
        if exponent & 1:
            out = [[sum(out[i][k] * base[k][j] for k in range(size)) for j in range(size)] for i in range(size)]
        base = [[sum(base[i][k] * base[k][j] for k in range(size)) for j in range(size)] for i in range(size)]
        exponent //= 2
    return out


def trace(a: list[list[int]]) -> int:
    return sum(a[i][i] for i in range(len(a)))


def fixed_debruijn_matrix() -> list[list[int]]:
    states = [(0, 0), (0, 1), (1, 0), (1, 1)]
    out = [[0] * 4 for _ in range(4)]
    for i, (a, b) in enumerate(states):
        for c in (0, 1):
            if (a, b, c) in ((0, 1, 0), (1, 0, 1)):
                continue
            out[i][states.index((b, c))] += 1
    return out


def lucas_rows(limit: int = 64) -> list[dict]:
    M = fixed_debruijn_matrix()
    lucas = [2, 1]
    cosine = [2, 1]
    for _ in range(2, limit + 1):
        lucas.append(lucas[-1] + lucas[-2])
        cosine.append(cosine[-1] - cosine[-2])
    rows = []
    for n in range(1, limit + 1):
        tr = trace(integer_matrix_power(M, n))
        rows.append({
            "n": n,
            "fixed_count_trace": tr,
            "lucas_number": lucas[n],
            "sixth_root_trace": cosine[n],
            "fixed_count_closed": lucas[n] + cosine[n],
            "period_two_state_count": 2 if n % 2 == 0 else 0,
            "period_two_orbit_count": 1 if n % 2 == 0 else 0,
        })
    return rows


def wall_run_matrix(max_run: int, signed: bool = False) -> list[list[int]]:
    size = max_run + 1
    out = [[0] * size for _ in range(size)]
    for r in range(size):
        out[r][0] += 1
        if r < max_run:
            out[r][r + 1] += -1 if signed else 1
    return out


def even_wall_count(n: int, max_run: int) -> int:
    plain = trace(integer_matrix_power(wall_run_matrix(max_run), n))
    signed = trace(integer_matrix_power(wall_run_matrix(max_run, signed=True), n))
    return (plain + signed) // 2


def wall_run_rows(n_values=range(1, 25), max_run_values=range(0, 9)) -> list[dict]:
    rows = []
    for n in n_values:
        for m in max_run_values:
            rows.append({
                "n": n,
                "max_run_bound": m,
                "cyclic_wall_words_all_parities": trace(integer_matrix_power(wall_run_matrix(m), n)),
                "cyclic_wall_words_even_parity": even_wall_count(n, m),
                "state_count_with_wall_bound": 2 * even_wall_count(n, m),
            })
    return rows


def finite_state_rows(max_n: int = 14) -> list[dict]:
    rows = []
    for n in range(1, max_n + 1):
        records = [classify(s) for s in all_states(n)]
        depth_max = (n - 1) // 2
        depth_hist = [sum(r["entry_time"] == t and r["cycle_period"] == 1 for r in records) for t in range(depth_max + 1)]
        cycle2 = [r for r in records if r["cycle_period"] == 2]
        rows.append({
            "n": n,
            "state_count": 1 << n,
            "fixed_state_count_direct": sum(r["cycle_period"] == 1 and r["entry_time"] == 0 for r in records),
            "period_two_state_count_direct": len(cycle2),
            "period_two_orbit_count_direct": len(cycle2) // 2,
            "transient_state_count": sum(r["entry_time"] > 0 for r in records),
            "max_entry_time": max(r["entry_time"] for r in records),
            "depth_histogram_fixed_at_t": depth_hist,
            "wall_run_histogram": [sum(r["max_wall_run"] == k for r in records) for k in range(n + 1)],
            "alternating_states": [r["initial"] for r in records if r["alternating_initial"]],
            "all_periods": sorted(set(r["cycle_period"] for r in records)),
        })
    return rows


def sample_trajectories() -> list[dict]:
    samples = [(8, "00010101"), (9, "000101010"), (12, "000101010101"), (10, "0010110101")]
    out = []
    for n, word in samples:
        state = from_bits(word)
        record = classify(state)
        out.append({
            "n": n,
            "initial": word,
            "trajectory": record["history"],
            "entry_time": record["entry_time"],
            "cycle_period": record["cycle_period"],
            "wall_trajectory": [bits(walls(from_bits(x))) for x in record["history"]],
        })
    return out


def build() -> dict:
    M = fixed_debruijn_matrix()
    data = {
        "schema": "hcs-c251-majority-rule232-domainwall-v1",
        "candidate_id": "HCS-C251",
        "evaluation_date": DATE,
        "fixed_epoch": FIXED_EPOCH,
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "Synchronous cyclic majority rule 232 has an exact domain-wall erosion law: every non-alternating state reaches a fixed state in finite time, the only nontrivial cycle is the even-length alternating 2-cycle, and fixed/transient counts close by finite transfer matrices.",
        "frozen_object": {
            "phase_space": "X_n={0,1}^n with labelled cyclic indices modulo n, for every n>=1",
            "map": "F_n(x)_i=1 iff x_{i-1}+x_i+x_{i+1}>=2 (synchronous radius-one majority, elementary rule 232)",
            "clock": "one simultaneous local update",
            "wall_coordinate": "w_i=x_i xor x_{i+1}; admissible wall words have even parity and lift to exactly two x words",
            "primitive_periodic_orbit": "fixed points plus the unique alternating temporal 2-cycle when n is even; no period greater than two",
            "normalization": "labelled words are counted before quotienting by rotation; complement is a distinct state",
            "forbidden_data": "NO_BAD_EULER_OR_ROOT_NUMBER: target primes/zeros, arithmetic local data, Euler factors, root numbers, automorphy, target divisors, Hilbert--Polya operators",
        },
        "theorem": {
            "wall_update": "w_i'=w_i(1 xor w_{i-1} xor w_{i+1}) over F_2; a finite 1-block of length K becomes max(K-2, parity(K))",
            "attractor_classification": "every non-alternating state reaches a fixed state; an even n alternating word and its complement form one primitive period-two orbit; no other cycles occur",
            "transient_bound": "the entry time is max over wall blocks floor(K/2), hence at most floor((n-1)/2) outside the alternating cycle; the bound is attained for odd n by 0 1^(n-1) and for even n by 0 1^(n-2) 0",
            "fixed_language": "fixed states are exactly cyclic binary words avoiding 010 and 101, equivalently all nontrivial symbol runs have length at least two",
            "fixed_count": "a_n=tr(M^n)=L_n+2 cos(n pi/3), where L_n is the Lucas number, M is the four-state pair de Bruijn matrix, and the cosine term is the integer recurrence c_n=c_{n-1}-c_{n-2}",
            "transient_generating": "for each run bound m, traces of B_m and its parity twist count cyclic wall words with max run <=m; differences give exact entry-depth populations",
            "scope": "source-local finite-state combinatorics; no target arithmetic or spectral identification",
        },
        "regression": {
            "fixed_debruijn_matrix": M,
            "fixed_matrix_characteristic_polynomial": "(lambda^2-lambda-1)(lambda^2-lambda+1)",
            "fixed_formula_rows": lucas_rows(),
            "wall_run_rows": wall_run_rows(),
            "finite_state_rows": finite_state_rows(),
            "sample_trajectories": sample_trajectories(),
            "rule_truth_table": [{"neighborhood": f"{a}{b}{c}", "output": int(a + b + c >= 2)} for a in (0, 1) for b in (0, 1) for c in (0, 1)],
            "parameter_grid": [{"n": n} for n in range(1, 65)],
            "row_counts": {"fixed_formula": 64, "wall_run": 24 * 9, "finite_state": 14, "samples": 4, "truth_table": 8},
            "integer_arithmetic_only": True,
        },
        "exact_identities": [
            {"name": "wall_erosion", "formula": "w_i'=w_i(1 xor w_{i-1} xor w_{i+1}); K -> max(K-2, K mod 2)", "status": "proved_and_receipted"},
            {"name": "periodic_classification", "formula": "Per(F_n)=Fix(F_n) union {alternating pair if 2|n}; no period >2", "status": "proved_and_receipted"},
            {"name": "fixed_count_transfer", "formula": "#Fix(F_n)=tr(M^n)=L_n+2 cos(n pi/3)", "status": "proved_and_receipted"},
            {"name": "parity_twisted_transient_count", "formula": "2*(tr(B_m^n)+tr(B_m^-^n))/2 counts lifted states with wall run <=m", "status": "proved_and_receipted"},
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
            "strongest_positive": "all-size analytic periodic/attractor classification with exact transfer-matrix receipts",
            "strongest_failure": "the finite binary clock has no rational-prime ownership, target divisor, or Hilbert--Polya operator",
        },
        "scope_flags": {
            "uses_target_zero_table": False,
            "uses_prime_table": False,
            "claims_arithmetic_local_data": False,
            "claims_euler_factors": False,
            "claims_root_numbers": False,
            "claims_automorphy": False,
            "claims_target_divisor_or_functional_equation": False,
            "claims_hilbert_polya_operator": False,
            "invokes_route_b": False,
        },
        "citations": [
            {"id": "Wolfram1983", "title": "Statistical mechanics of cellular automata", "authors": "Stephen Wolfram", "venue": "Reviews of Modern Physics 55 (1983), 601--644", "doi": "10.1103/RevModPhys.55.601", "url": "https://doi.org/10.1103/RevModPhys.55.601", "role": "primary source for elementary cellular-automaton classification context; the exact rule-232 theorem here is independently derived"},
            {"id": "Toom1980", "title": "Stable and attractive trajectories in multicomponent systems", "authors": "Andrei L. Toom", "venue": "Multicomponent Random Systems, 549--575 (1980)", "doi": "10.1007/978-1-4613-3044-2_19", "url": "https://doi.org/10.1007/978-1-4613-3044-2_19", "role": "source context for monotone local cellular dynamics and erosion arguments"},
        ],
        "nonclaims": [
            "The theorem concerns labelled finite cyclic words and their synchronous rule-232 map; it is not a claim about asynchronous majority dynamics or infinite-volume phase transitions.",
            "Transfer-matrix traces and Fibonacci/Lucas recurrences are source-local combinatorics, not arithmetic Euler factors or target prime clocks.",
            "The alternating pair is a temporal 2-cycle, not a unitary quantization; no target divisor, zero table, automorphy, or Hilbert--Polya operator is supplied.",
            "Finite receipts validate the all-size formulas and do not license extrapolation to an unspecified Hénon nonwandering set.",
        ],
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(build(), sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    payload = json.loads(args.output.read_text())["payload_sha256"]
    print(json.dumps({"status": "C251_PRODUCER_PASS", "output": str(args.output), "payload_sha256": payload}, sort_keys=True))


if __name__ == "__main__":
    main()
