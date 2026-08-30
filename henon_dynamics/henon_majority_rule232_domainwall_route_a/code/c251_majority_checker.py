#!/usr/bin/env python3
"""Producer-independent checker for the C251 rule-232 certificate."""
from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_INPUT = ROOT / "results/c251_majority_evidence.json"
SOURCE_COMMIT = "3ff451e904f8f063e88c40ef87f4697a6586b1a5"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
DATE = "2026-08-30"
FIXED_EPOCH = 1788048000


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def check_keys(obj: dict, expected: set[str], where: str) -> int:
    assert isinstance(obj, dict), where
    assert set(obj) == expected, f"{where}: key mismatch"
    return 1


def step(state: tuple[int, ...]) -> tuple[int, ...]:
    n = len(state)
    return tuple(int(state[(i - 1) % n] + state[i] + state[(i + 1) % n] >= 2) for i in range(n))


def wall(state: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(state[i] ^ state[(i + 1) % len(state)] for i in range(len(state)))


def from_bits(value: str) -> tuple[int, ...]:
    assert value and set(value) <= {"0", "1"}
    return tuple(int(x) for x in value)


def as_bits(value: tuple[int, ...]) -> str:
    return "".join(map(str, value))


def max_run(w: tuple[int, ...]) -> int:
    n = len(w)
    if not any(w):
        return 0
    if all(w):
        return n
    doubled = w + w
    best = cur = 0
    for x in doubled:
        cur = cur + 1 if x else 0
        best = max(best, cur)
    return min(best, n)


def alternating(x: tuple[int, ...]) -> bool:
    return len(x) % 2 == 0 and all(x[i] != x[(i + 1) % len(x)] for i in range(len(x)))


def classify(x: tuple[int, ...]) -> dict:
    y = x
    hist = [as_bits(y)]
    seen: dict[tuple[int, ...], int] = {}
    while y not in seen:
        seen[y] = len(hist) - 1
        z = step(y)
        if z not in seen:
            hist.append(as_bits(z))
        y = z
        assert len(hist) <= 2 * len(x) + 9
    entry = seen[y]
    return {
        "initial": as_bits(x),
        "initial_walls": as_bits(wall(x)),
        "max_wall_run": max_run(wall(x)),
        "entry_time": entry,
        "cycle_period": len(hist) - entry,
        "cycle_representative": as_bits(y),
        "final_state": hist[entry],
        "history": hist,
        "fixed_initial": step(x) == x,
        "alternating_initial": alternating(x),
    }


def mpow(a: list[list[int]], exponent: int) -> list[list[int]]:
    n = len(a)
    out = [[int(i == j) for j in range(n)] for i in range(n)]
    base = [row[:] for row in a]
    while exponent:
        if exponent & 1:
            out = [[sum(out[i][k] * base[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
        base = [[sum(base[i][k] * base[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
        exponent //= 2
    return out


def tr(a: list[list[int]]) -> int:
    return sum(a[i][i] for i in range(len(a)))


def fixed_matrix() -> list[list[int]]:
    states = [(0, 0), (0, 1), (1, 0), (1, 1)]
    out = [[0] * 4 for _ in range(4)]
    for i, (a, b) in enumerate(states):
        for c in (0, 1):
            if (a, b, c) not in ((0, 1, 0), (1, 0, 1)):
                out[i][states.index((b, c))] += 1
    return out


def run_matrix(bound: int, signed: bool = False) -> list[list[int]]:
    out = [[0] * (bound + 1) for _ in range(bound + 1)]
    for r in range(bound + 1):
        out[r][0] = 1
        if r < bound:
            out[r][r + 1] = -1 if signed else 1
    return out


def even_walls(n: int, bound: int) -> int:
    return (tr(mpow(run_matrix(bound), n)) + tr(mpow(run_matrix(bound, True), n))) // 2


def validate(data: dict) -> int:
    checks = 0
    top = {"schema", "candidate_id", "evaluation_date", "fixed_epoch", "source_commit", "scope_literal", "evaluator", "headline", "frozen_object", "theorem", "regression", "exact_identities", "route_a", "scope_flags", "citations", "nonclaims", "payload_sha256"}
    checks += check_keys(data, top, "top")
    expected_top = {"schema": "hcs-c251-majority-rule232-domainwall-v1", "candidate_id": "HCS-C251", "evaluation_date": DATE, "fixed_epoch": FIXED_EPOCH, "source_commit": SOURCE_COMMIT, "scope_literal": SCOPE}
    for k, v in expected_top.items():
        assert data[k] == v, k
        checks += 1
    assert data["payload_sha256"] == payload_hash(data); checks += 1
    assert data["evaluator"] == {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256}; checks += 1

    frozen_keys = {"phase_space", "map", "clock", "wall_coordinate", "primitive_periodic_orbit", "normalization", "forbidden_data"}
    checks += check_keys(data["frozen_object"], frozen_keys, "frozen")
    f = data["frozen_object"]
    expected_frozen = {
        "phase_space": "X_n={0,1}^n with labelled cyclic indices modulo n, for every n>=1",
        "map": "F_n(x)_i=1 iff x_{i-1}+x_i+x_{i+1}>=2 (synchronous radius-one majority, elementary rule 232)",
        "clock": "one simultaneous local update",
        "wall_coordinate": "w_i=x_i xor x_{i+1}; admissible wall words have even parity and lift to exactly two x words",
        "primitive_periodic_orbit": "fixed points plus the unique alternating temporal 2-cycle when n is even; no period greater than two",
        "normalization": "labelled words are counted before quotienting by rotation; complement is a distinct state",
    }
    for key, expected in expected_frozen.items():
        assert f[key] == expected, key
        checks += 1
    for phrase in ("{0,1}^n", "cyclic", "majority", "rule 232", "synchronous", "wall", "even parity", "two", "2-cycle", "no period greater", "labelled", SCOPE, "Euler"):
        assert phrase.lower() in " ".join(f.values()).lower(), phrase
        checks += 1

    theorem_keys = {"wall_update", "attractor_classification", "transient_bound", "fixed_language", "fixed_count", "transient_generating", "scope"}
    checks += check_keys(data["theorem"], theorem_keys, "theorem")
    theorem_text = " ".join(data["theorem"].values()).lower()
    for phrase in ("w_i'", "block", "fixed", "alternating", "no other cycles", "floor", "010", "tr(m^n)", "lucas", "parity", "source-local"):
        assert phrase in theorem_text, phrase
        checks += 1

    reg_keys = {"fixed_debruijn_matrix", "fixed_matrix_characteristic_polynomial", "fixed_formula_rows", "wall_run_rows", "finite_state_rows", "sample_trajectories", "rule_truth_table", "parameter_grid", "row_counts", "integer_arithmetic_only"}
    checks += check_keys(data["regression"], reg_keys, "regression")
    reg = data["regression"]
    M = fixed_matrix()
    assert reg["fixed_debruijn_matrix"] == M; checks += 1
    assert reg["fixed_matrix_characteristic_polynomial"] == "(lambda^2-lambda-1)(lambda^2-lambda+1)"; checks += 1
    assert reg["integer_arithmetic_only"] is True; checks += 1
    assert reg["parameter_grid"] == [{"n": n} for n in range(1, 65)]; checks += 1
    assert reg["row_counts"] == {"fixed_formula": 64, "wall_run": 216, "finite_state": 14, "samples": 4, "truth_table": 8}; checks += 1

    fixed_rows = reg["fixed_formula_rows"]
    assert len(fixed_rows) == 64; checks += 1
    lucas, cosine = [2, 1], [2, 1]
    for _ in range(2, 65):
        lucas.append(lucas[-1] + lucas[-2]); cosine.append(cosine[-1] - cosine[-2])
    for n, row in enumerate(fixed_rows, 1):
        checks += check_keys(row, {"n", "fixed_count_trace", "lucas_number", "sixth_root_trace", "fixed_count_closed", "period_two_state_count", "period_two_orbit_count"}, f"fixed[{n}]")
        assert row["n"] == n; checks += 1
        assert row["fixed_count_trace"] == tr(mpow(M, n)); checks += 1
        assert row["lucas_number"] == lucas[n] and row["sixth_root_trace"] == cosine[n]; checks += 1
        assert row["fixed_count_closed"] == lucas[n] + cosine[n]; checks += 1
        assert row["fixed_count_trace"] == row["fixed_count_closed"]; checks += 1
        assert row["period_two_state_count"] == (2 if n % 2 == 0 else 0); checks += 1
        assert row["period_two_orbit_count"] == (1 if n % 2 == 0 else 0); checks += 1

    wall_rows = reg["wall_run_rows"]
    assert len(wall_rows) == 216; checks += 1
    for row in wall_rows:
        checks += check_keys(row, {"n", "max_run_bound", "cyclic_wall_words_all_parities", "cyclic_wall_words_even_parity", "state_count_with_wall_bound"}, "wall")
        n, m = row["n"], row["max_run_bound"]
        assert 1 <= n <= 24 and 0 <= m <= 8; checks += 1
        plain = tr(mpow(run_matrix(m), n)); signed = tr(mpow(run_matrix(m, True), n))
        assert row["cyclic_wall_words_all_parities"] == plain; checks += 1
        assert row["cyclic_wall_words_even_parity"] == (plain + signed) // 2; checks += 1
        assert row["state_count_with_wall_bound"] == 2 * row["cyclic_wall_words_even_parity"]; checks += 1

    finite_rows = reg["finite_state_rows"]
    assert len(finite_rows) == 14; checks += 1
    for row in finite_rows:
        n = row["n"]
        checks += check_keys(row, {"n", "state_count", "fixed_state_count_direct", "period_two_state_count_direct", "period_two_orbit_count_direct", "transient_state_count", "max_entry_time", "depth_histogram_fixed_at_t", "wall_run_histogram", "alternating_states", "all_periods"}, f"finite[{n}]")
        assert 1 <= n <= 14 and row["state_count"] == 1 << n; checks += 1
        records = [classify(x) for x in (tuple((mask >> i) & 1 for i in range(n)) for mask in range(1 << n))]
        assert row["fixed_state_count_direct"] == sum(r["cycle_period"] == 1 and r["entry_time"] == 0 for r in records); checks += 1
        c2 = sum(r["cycle_period"] == 2 for r in records)
        assert row["period_two_state_count_direct"] == c2 == (2 if n % 2 == 0 else 0); checks += 1
        assert row["period_two_orbit_count_direct"] == c2 // 2; checks += 1
        assert row["transient_state_count"] == sum(r["entry_time"] > 0 for r in records); checks += 1
        assert row["max_entry_time"] == max(r["entry_time"] for r in records); checks += 1
        depth_max = (n - 1) // 2
        expected_depth = [sum(r["entry_time"] == t and r["cycle_period"] == 1 for r in records) for t in range(depth_max + 1)]
        assert row["depth_histogram_fixed_at_t"] == expected_depth; checks += 1
        expected_wall = [sum(r["max_wall_run"] == k for r in records) for k in range(n + 1)]
        assert row["wall_run_histogram"] == expected_wall; checks += 1
        assert sorted(row["alternating_states"]) == sorted(r["initial"] for r in records if r["alternating_initial"]); checks += 1
        assert row["all_periods"] == sorted(set(r["cycle_period"] for r in records)); checks += 1

    samples = reg["sample_trajectories"]
    assert len(samples) == 4; checks += 1
    for sample in samples:
        checks += check_keys(sample, {"n", "initial", "trajectory", "entry_time", "cycle_period", "wall_trajectory"}, "sample")
        x = from_bits(sample["initial"])
        assert sample["n"] == len(x); checks += 1
        rec = classify(x)
        assert sample["trajectory"] == rec["history"] and sample["entry_time"] == rec["entry_time"]; checks += 1
        assert sample["cycle_period"] == rec["cycle_period"]; checks += 1
        assert sample["wall_trajectory"] == [as_bits(wall(from_bits(y))) for y in rec["history"]]; checks += 1

    truth = reg["rule_truth_table"]
    assert len(truth) == 8; checks += 1
    for row in truth:
        checks += check_keys(row, {"neighborhood", "output"}, "truth")
        q = from_bits(row["neighborhood"])
        assert len(q) == 3 and row["output"] == int(sum(q) >= 2); checks += 1

    identities = reg_identity = data["exact_identities"]
    assert isinstance(identities, list) and len(identities) == 4; checks += 1
    assert [x["name"] for x in identities] == ["wall_erosion", "periodic_classification", "fixed_count_transfer", "parity_twisted_transient_count"]; checks += 1
    assert all(set(x) == {"name", "formula", "status"} and x["status"] == "proved_and_receipted" for x in identities); checks += 1

    route = data["route_a"]
    checks += check_keys(route, {"tuple", "overall", "route_b_invocation_allowed", "strongest_positive", "strongest_failure"}, "route")
    assert route["tuple"] == ["A0_FAIL", "A1_PASS_ANALYTIC", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"]; checks += 1
    assert route["overall"] == "ROUTE_A_REJECTED" and route["route_b_invocation_allowed"] is False; checks += 1
    assert "all-size" in route["strongest_positive"] and "target" in route["strongest_failure"]; checks += 1

    scope = data["scope_flags"]
    expected_scope = {"uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"}
    checks += check_keys(scope, expected_scope, "scope")
    assert all(v is False for v in scope.values()); checks += 1

    citations = data["citations"]
    assert len(citations) == 2; checks += 1
    expected_citations = {"Wolfram1983": ("10.1103/RevModPhys.55.601", "https://doi.org/10.1103/RevModPhys.55.601"), "Toom1980": ("10.1007/978-1-4613-3044-2_19", "https://doi.org/10.1007/978-1-4613-3044-2_19")}
    for item in citations:
        checks += check_keys(item, {"id", "title", "authors", "venue", "doi", "url", "role"}, "citation")
        assert item["id"] in expected_citations and (item["doi"], item["url"]) == expected_citations[item["id"]]; checks += 1
    assert {x["id"] for x in citations} == set(expected_citations); checks += 1

    assert isinstance(data["nonclaims"], list) and len(data["nonclaims"]) == 4; checks += 1
    nonclaims = " ".join(data["nonclaims"]).lower()
    for phrase in ("finite cyclic", "asynchronous", "euler", "2-cycle", "hilbert"):
        assert phrase in nonclaims; checks += 1
    return checks


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT)
    args = parser.parse_args()
    checks = validate(json.loads(args.input.read_text()))
    print(f"C251 independent checker: PASS ({checks} assertions)")


if __name__ == "__main__":
    main()
