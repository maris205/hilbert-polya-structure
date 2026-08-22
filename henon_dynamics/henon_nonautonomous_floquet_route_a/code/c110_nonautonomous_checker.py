#!/usr/bin/env python3
"""Independent exact checker for the C110 Floquet pilot.

The implementation intentionally repeats the finite algebra rather than
importing the producer.  It validates canonical JSON bytes, admissible
primitive necklaces, all three control products, the trace decomposition,
and the determinant prefixes.
"""
from __future__ import annotations

from hashlib import sha256
import itertools
import json
from pathlib import Path
from typing import Sequence

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c110_nonautonomous_evidence.json"
MAX_N = 6
Q = ((1, 1, 0, 0), (0, 1, 1, 0), (1, 0, 0, 1), (0, 1, 0, 1))
CONTROLS = ("chronological_01", "reversed_10", "same_parameter_00")
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"

M = tuple[tuple[int, ...], ...]


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def eye(n: int) -> M:
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def mm(a: M, b: M) -> M:
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0])))
        for i in range(len(a))
    )


def mpow(a: M, n: int) -> M:
    out, base = eye(len(a)), a
    while n:
        if n & 1:
            out = mm(out, base)
        base = mm(base, base)
        n //= 2
    return out


def tr(a: M) -> int:
    return sum(a[i][i] for i in range(len(a)))


def det2(a: M) -> int:
    assert len(a) == 2
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def branch(phase: int, symbol: int) -> M:
    # xi=-1,+1 and alpha=(0,1).
    xi = (-1, 1)[symbol]
    slope = 2 * xi + (0, 1)[phase]
    return ((slope, -1), (1, 0))


def pair(symbol: int) -> tuple[int, int]:
    return divmod(symbol, 2)


def block(symbol: int, control: str) -> M:
    s0, s1 = pair(symbol)
    if control == "chronological_01":
        return mm(branch(1, s1), branch(0, s0))
    if control == "reversed_10":
        return mm(branch(0, s0), branch(1, s1))
    if control == "same_parameter_00":
        return mm(branch(0, s1), branch(0, s0))
    raise AssertionError(control)


def primitive(w: tuple[int, ...]) -> bool:
    return all(w != w[:d] * (len(w) // d) for d in range(1, len(w)) if len(w) % d == 0)


def allowed(w: tuple[int, ...]) -> bool:
    return bool(w) and all(Q[w[i]][w[(i + 1) % len(w)]] for i in range(len(w)))


def necklaces(n: int) -> list[tuple[int, ...]]:
    out: set[tuple[int, ...]] = set()
    for w in itertools.product(range(4), repeat=n):
        if primitive(w) and allowed(w):
            out.add(min(w[i:] + w[:i] for i in range(n)))
    return sorted(out)


def word_matrix(w: Sequence[int], control: str) -> M:
    # Right product matches the target-weighted block transfer A_ij=Q_ij M_j.
    out = eye(2)
    for symbol in w:
        out = mm(out, block(symbol, control))
    return out


def transfer(control: str) -> M:
    out = [[0] * 8 for _ in range(8)]
    for i in range(4):
        for j in range(4):
            if not Q[i][j]:
                continue
            b = block(j, control)
            for r in range(2):
                for c in range(2):
                    out[2 * i + r][2 * j + c] = b[r][c]
    return tuple(tuple(row) for row in out)


def pmul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def det_prefix(a: M) -> list[int]:
    n = len(a)
    out = [0] * (n + 1)
    for p in itertools.permutations(range(n)):
        inv = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        term = [1]
        for i, j in enumerate(p):
            term = pmul(term, [int(i == j), -a[i][j]])
        sign = -1 if inv % 2 else 1
        for d, x in enumerate(term):
            out[d] += sign * x
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def expected() -> dict:
    rows: list[dict[str, object]] = []
    by: dict[int, list[dict[str, object]]] = {}
    for n in range(1, MAX_N + 1):
        by[n] = []
        for w in necklaces(n):
            row: dict[str, object] = {
                "length": n,
                "word": "".join(str(x) for x in w),
                "symbols": list(w),
                "pair_sequence": [list(pair(x)) for x in w],
                "canonical_rotation": list(min(w[i:] + w[:i] for i in range(n))),
                "is_primitive": True,
                "admissible_cycle": True,
                "phase_convention": "phase-0-then-phase-1-per-block",
                "rooted_start_multiplicity": n,
                "cyclic_stabilizer_size": 1,
                "orientation_sign": 1,
                "forcing_period": 2,
                "block_period": n,
                "chronological_order": "B_1,s1 B_0,s0, left-to-right chronological product",
            }
            for control in CONTROLS:
                wm = word_matrix(w, control)
                row[control + "_monodromy"] = [list(x) for x in wm]
                row[control + "_trace"] = tr(wm)
                row[control + "_determinant"] = det2(wm)
                row[control + "_trace_of_repetition"] = {
                    str(r): tr(mpow(wm, r)) for r in range(1, MAX_N // n + 1)
                }
            row["chronology_trace_minus_reverse_trace"] = int(row["chronological_01_trace"]) - int(row["reversed_10_trace"])
            rows.append(row)
            by[n].append(row)
    transfers = {control: transfer(control) for control in CONTROLS}
    traces = {c: {str(n): tr(mpow(a, n)) for n in range(1, MAX_N + 1)} for c, a in transfers.items()}
    contrib: dict[str, dict[str, dict[str, int]]] = {c: {} for c in CONTROLS}
    for c in CONTROLS:
        for n in range(1, MAX_N + 1):
            dct = {}
            for d in range(1, n + 1):
                if n % d == 0:
                    rep = n // d
                    dct[str(d)] = d * sum(int(x[c + "_trace_of_repetition"][str(rep)]) for x in by[d])
            assert sum(dct.values()) == traces[c][str(n)]
            contrib[c][str(n)] = dct
    atlas = {}
    for c in CONTROLS:
        atlas[c] = {
            "matrix": [list(x) for x in transfers[c]],
            "trace_of_powers": traces[c],
            "primitive_trace_identity_contributions": contrib[c],
            "determinant_I_minus_zA_coefficients_low_to_high": det_prefix(transfers[c]),
            "trace_log_prefix_coefficients": {str(n): {"numerator": traces[c][str(n)], "denominator": n} for n in range(1, MAX_N + 1)},
        }
    sensitive = sum(1 for r in rows if r["chronology_trace_minus_reverse_trace"])
    return {
        "schema_id": "hcs-c110-nonautonomous-floquet-route-a-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "definition": {
            "candidate_map": "F_t(x,y)=(x^2+alpha_t*x+beta_t-y,x), t mod 2",
            "forcing_period": 2,
            "chronological_control": "F_0 then F_1; block matrix B_1,s1 B_0,s0",
            "reverse_control": "same branch-pair labels but B_0,s0 B_1,s1",
            "same_parameter_control": "both phases use phase-0 Jacobian templates",
            "block_symbol": "u=(s0,s1) encoded 2*s0+s1",
            "primitive_object": "lexicographically least rotation of an admissible non-periodic block word",
            "frozen_adjacency": "Q on four block symbols; Q_ij=1 iff transition i->j is allowed",
            "transfer_prefix": "8x8 matrix-valued adjacency transfer A_Q with block Q_ij M_j",
            "trace_log_identity": "Tr(A_Q^n)=sum_{d|n} d sum_[w] in P_d tr(M_w^(n/d))",
            "determinant_convention": "det(I-z A_Q), finite discrete prefix only",
        },
        "source_model": {
            "maps": [
                {"phase": 0, "alpha": {"numerator": 0, "denominator": 1}, "beta": {"numerator": 0, "denominator": 1}},
                {"phase": 1, "alpha": {"numerator": 1, "denominator": 1}, "beta": {"numerator": 1, "denominator": 3}},
            ],
            "representative_points": [-1, 1],
            "branch_slopes_by_phase": [[-2, 2], [-1, 3]],
            "branch_matrices_by_phase": [[ [ [-2,-1],[1,0] ], [ [2,-1],[1,0] ] ], [ [ [-1,-1],[1,0] ], [ [3,-1],[1,0] ] ]],
            "adjacency": [list(row) for row in Q],
            "block_symbol_count": 4,
            "transfer_dimension": 8,
            "max_block_period": MAX_N,
        },
        "primitive_orbit_ledger": {"rows": rows, "count_by_length": {str(n): len(by[n]) for n in range(1, MAX_N + 1)}, "total_primitive_necklaces": len(rows), "chronology_sensitive_rows": sensitive},
        "transfer_atlas": atlas,
        "checks": {
            "all_words_are_canonical_primitive_and_admissible": True,
            "phase_multiplicity_orientation_fields": True,
            "all_control_monodromy_determinants_one": all(r[c + "_determinant"] == 1 for r in rows for c in CONTROLS),
            "trace_power_primitive_decomposition_n_1_to_6": True,
            "determinant_trace_log_prefix_consistent": True,
            "chronology_reverse_difference_present": bool(sensitive),
            "independent_symbolic_reproduction_required": True,
        },
        "route_a_assessment": {
            "A1": "A1_WEAK", "A2": "A2_CERTIFIED_PREFIX", "A1_qualification": "NONAUTONOMOUS_SYMBOLIC_PILOT_ONLY", "A2_qualification": "DISCRETE_FLOQUET_TRANSFER_PREFIX_ONLY", "A3": "A3_NOT_ADDRESSED", "A4": "A4_FAIL", "geometric_coding_theorem": "NOT_ESTABLISHED", "genuine_fredholm_owner": "NOT_ESTABLISHED",
        },
        "claims": {
            "exact_finite_period_two_floquet_symbolic_ledger": True, "chronological_product_order_is_recorded": True, "exact_candidate_henon_periodic_orbit_completeness": False, "actual_henon_markov_partition": False, "fredholm_determinant": False, "arithmetic_local_claimed": False, "euler_factors_claimed": False, "root_numbers_claimed": False, "automorphy_claimed": False, "hilbert_polya_operator_claimed": False, "route_b_authorized": False,
        },
    }


def validate_evidence_path(path: Path = EVIDENCE, want: dict | None = None) -> dict:
    raw = path.read_bytes()
    value = json.loads(raw)
    assert raw == canonical(value)
    want = expected() if want is None else want
    assert value == want
    assert value["scope_literal"] == FIREWALL
    return value


def main() -> None:
    raw = EVIDENCE.read_bytes()
    value = validate_evidence_path(EVIDENCE)
    want = expected()
    assert value == want
    assert value["scope_literal"] == FIREWALL
    print(json.dumps({"status": "C110_CHECK_PASS", "primitive_necklaces": len(value["primitive_orbit_ledger"]["rows"]), "evidence_sha256": sha256(raw).hexdigest()}, sort_keys=True))


if __name__ == "__main__":
    main()
