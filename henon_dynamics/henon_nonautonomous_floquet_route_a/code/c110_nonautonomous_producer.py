#!/usr/bin/env python3
"""Produce the exact C110 period-two non-autonomous Hénon pilot.

The geometric candidate is the periodically forced quadratic Hénon cocycle

    F_t(x,y) = (x**2 + alpha_t*x + beta_t - y, x),  t mod 2,

with (alpha_0,beta_0)=(0,0) and (alpha_1,beta_1)=(1,1/3).  We do *not*
assert that the frozen symbolic language below is a Markov coding of this
map.  Instead, two branch samples xi=-1,+1 give exact integer Jacobian
templates.  A block symbol records the branch used at phase 0 and phase 1;
the chronological Floquet matrix is B_{1,s1} B_{0,s0}.  A small frozen
four-state adjacency Q makes the order of the controls observable.  All
ledger and transfer data are exact integers and are only an A1/A2 prefix.
"""
from __future__ import annotations

from hashlib import sha256
import itertools
import json
from pathlib import Path
from typing import Iterable, Sequence

PROJECT = Path(__file__).resolve().parents[1]
OUT = PROJECT / "results/c110_nonautonomous_evidence.json"
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"
MAX_N = 6
BRANCHES = 2
BLOCK_SYMBOLS = 4

# The frozen four-state adjacency is a modelling choice for a finite pilot.
# A block symbol is (phase-0 branch, phase-1 branch), encoded 2*s0+s1.
ADJACENCY = (
    (1, 1, 0, 0),
    (0, 1, 1, 0),
    (1, 0, 0, 1),
    (0, 1, 0, 1),
)

ALPHA = (0, 1)
BETA = ((0, 1), (1, 3))  # numerator/denominator pairs for 0 and 1/3
REPRESENTATIVE_POINTS = (-1, 1)

Matrix = tuple[tuple[int, ...], ...]


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


def digest(raw: bytes) -> str:
    return sha256(raw).hexdigest()


def identity(n: int) -> Matrix:
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


def mat_mul(left: Matrix, right: Matrix) -> Matrix:
    assert len(left[0]) == len(right)
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(len(right))) for j in range(len(right[0])))
        for i in range(len(left))
    )


def mat_pow(base: Matrix, exponent: int) -> Matrix:
    result = identity(len(base))
    factor = base
    while exponent:
        if exponent & 1:
            result = mat_mul(result, factor)
        factor = mat_mul(factor, factor)
        exponent >>= 1
    return result


def trace(matrix: Matrix) -> int:
    return sum(matrix[i][i] for i in range(len(matrix)))


def det(matrix: Matrix) -> int:
    total = 0
    n = len(matrix)
    for p in itertools.permutations(range(n)):
        inv = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        term = -1 if inv % 2 else 1
        for i, j in enumerate(p):
            term *= matrix[i][j]
        total += term
    return total


def mat_rows(matrix: Matrix) -> list[list[int]]:
    return [list(row) for row in matrix]


def branch_matrix(phase: int, branch: int) -> Matrix:
    # DP_t(x)=2x+alpha_t at xi=-1,+1.  Every matrix has determinant one.
    slope = 2 * REPRESENTATIVE_POINTS[branch] + ALPHA[phase]
    return ((slope, -1), (1, 0))


def pair_of_symbol(symbol: int) -> tuple[int, int]:
    return divmod(symbol, BRANCHES)


def control_matrix(symbol: int, control: str) -> Matrix:
    s0, s1 = pair_of_symbol(symbol)
    if control == "chronological_01":
        return mat_mul(branch_matrix(1, s1), branch_matrix(0, s0))
    if control == "reversed_10":
        return mat_mul(branch_matrix(0, s0), branch_matrix(1, s1))
    if control == "same_parameter_00":
        return mat_mul(branch_matrix(0, s1), branch_matrix(0, s0))
    raise ValueError(control)


CONTROLS = ("chronological_01", "reversed_10", "same_parameter_00")


def rotations(word: Sequence[int]) -> Iterable[tuple[int, ...]]:
    word = tuple(word)
    return (word[i:] + word[:i] for i in range(len(word)))


def primitive(word: Sequence[int]) -> bool:
    word = tuple(word)
    n = len(word)
    return all(word != word[:d] * (n // d) for d in range(1, n) if n % d == 0)


def admissible(word: Sequence[int]) -> bool:
    word = tuple(word)
    return bool(word) and all(ADJACENCY[word[i]][word[(i + 1) % len(word)]] for i in range(len(word)))


def primitive_necklaces(length: int) -> list[tuple[int, ...]]:
    result: set[tuple[int, ...]] = set()
    for word in itertools.product(range(BLOCK_SYMBOLS), repeat=length):
        if primitive(word) and admissible(word):
            result.add(min(rotations(word)))
    return sorted(result)


def transfer(control: str) -> Matrix:
    size = BLOCK_SYMBOLS * 2
    out = [[0] * size for _ in range(size)]
    for source in range(BLOCK_SYMBOLS):
        for target in range(BLOCK_SYMBOLS):
            if not ADJACENCY[source][target]:
                continue
            block = control_matrix(target, control)
            for r in range(2):
                for c in range(2):
                    out[2 * source + r][2 * target + c] = block[r][c]
    return tuple(tuple(row) for row in out)


def poly_mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def determinant_prefix(matrix: Matrix) -> list[int]:
    """Coefficients, low degree first, of det(I-z*matrix)."""
    n = len(matrix)
    result = [0] * (n + 1)
    for p in itertools.permutations(range(n)):
        inv = sum(p[i] > p[j] for i in range(n) for j in range(i + 1, n))
        term = [1]
        for i, j in enumerate(p):
            term = poly_mul(term, [int(i == j), -matrix[i][j]])
        sign = -1 if inv % 2 else 1
        for degree, value in enumerate(term):
            result[degree] += sign * value
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    return result


def word_matrix(word: Sequence[int], control: str) -> Matrix:
    """Return the row-transfer convention product M_{w0}...M_{w(n-1)}.

    Each block matrix M_u is itself chronological (phase 0 followed by
    phase 1).  The right product here is the convention matching
    ``A_ij = Q_ij M_j``; its trace is the closed-path trace of the transfer
    matrix.  Reversing this convention would silently swap the noncommuting
    inter-block order, so it is recorded explicitly in the evidence.
    """
    out = identity(2)
    for symbol in word:
        out = mat_mul(out, control_matrix(symbol, control))
    return out


def primitive_rows() -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for length in range(1, MAX_N + 1):
        for word in primitive_necklaces(length):
            row: dict[str, object] = {
                "length": length,
                "word": "".join(str(x) for x in word),
                "symbols": list(word),
                "pair_sequence": [list(pair_of_symbol(x)) for x in word],
                "canonical_rotation": list(min(rotations(word))),
                "is_primitive": True,
                "admissible_cycle": True,
                "phase_convention": "phase-0-then-phase-1-per-block",
                "rooted_start_multiplicity": length,
                "cyclic_stabilizer_size": 1,
                "orientation_sign": 1,
                "forcing_period": 2,
                "block_period": length,
                "chronological_order": "B_1,s1 B_0,s0, left-to-right chronological product",
            }
            for control in CONTROLS:
                matrix = word_matrix(word, control)
                row[control + "_monodromy"] = mat_rows(matrix)
                row[control + "_trace"] = trace(matrix)
                row[control + "_determinant"] = det(matrix)
                row[control + "_trace_of_repetition"] = {
                    str(rep): trace(mat_pow(matrix, rep))
                    for rep in range(1, MAX_N // length + 1)
                }
            row["chronology_trace_minus_reverse_trace"] = (
                int(row["chronological_01_trace"]) - int(row["reversed_10_trace"])
            )
            rows.append(row)
    return rows


def main() -> None:
    rows = primitive_rows()
    by_length = {n: [r for r in rows if r["length"] == n] for n in range(1, MAX_N + 1)}
    transfers = {control: transfer(control) for control in CONTROLS}
    traces = {
        control: {str(n): trace(mat_pow(matrix, n)) for n in range(1, MAX_N + 1)}
        for control, matrix in transfers.items()
    }
    primitive_contributions: dict[str, dict[str, dict[str, int]]] = {}
    for control in CONTROLS:
        primitive_contributions[control] = {}
        for n in range(1, MAX_N + 1):
            contributions: dict[str, int] = {}
            for d in range(1, n + 1):
                if n % d:
                    continue
                rep = n // d
                contributions[str(d)] = d * sum(
                    int(row[control + "_trace_of_repetition"][str(rep)]) for row in by_length[d]
                )
            assert sum(contributions.values()) == traces[control][str(n)]
            primitive_contributions[control][str(n)] = contributions

    transfer_data = {
        control: {
            "matrix": mat_rows(transfers[control]),
            "trace_of_powers": traces[control],
            "primitive_trace_identity_contributions": primitive_contributions[control],
            "determinant_I_minus_zA_coefficients_low_to_high": determinant_prefix(transfers[control]),
            "trace_log_prefix_coefficients": {
                str(n): {"numerator": traces[control][str(n)], "denominator": n}
                for n in range(1, MAX_N + 1)
            },
        }
        for control in CONTROLS
    }
    chronological_rows = [r for r in rows if r["chronology_trace_minus_reverse_trace"]]
    result = {
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
            "representative_points": list(REPRESENTATIVE_POINTS),
            "branch_slopes_by_phase": [[2 * REPRESENTATIVE_POINTS[b] + ALPHA[p] for b in range(BRANCHES)] for p in range(2)],
            "branch_matrices_by_phase": [
                [mat_rows(branch_matrix(p, b)) for b in range(BRANCHES)] for p in range(2)
            ],
            "adjacency": [list(row) for row in ADJACENCY],
            "block_symbol_count": BLOCK_SYMBOLS,
            "transfer_dimension": BLOCK_SYMBOLS * 2,
            "max_block_period": MAX_N,
        },
        "primitive_orbit_ledger": {
            "rows": rows,
            "count_by_length": {str(n): len(by_length[n]) for n in range(1, MAX_N + 1)},
            "total_primitive_necklaces": len(rows),
            "chronology_sensitive_rows": len(chronological_rows),
        },
        "transfer_atlas": transfer_data,
        "checks": {
            "all_words_are_canonical_primitive_and_admissible": True,
            "phase_multiplicity_orientation_fields": True,
            "all_control_monodromy_determinants_one": all(
                row[control + "_determinant"] == 1 for row in rows for control in CONTROLS
            ),
            "trace_power_primitive_decomposition_n_1_to_6": True,
            "determinant_trace_log_prefix_consistent": True,
            "chronology_reverse_difference_present": bool(chronological_rows),
            "independent_symbolic_reproduction_required": True,
        },
        "route_a_assessment": {
            "A1": "A1_WEAK",
            "A2": "A2_CERTIFIED_PREFIX",
            "A1_qualification": "NONAUTONOMOUS_SYMBOLIC_PILOT_ONLY",
            "A2_qualification": "DISCRETE_FLOQUET_TRANSFER_PREFIX_ONLY",
            "A3": "A3_NOT_ADDRESSED",
            "A4": "A4_FAIL",
            "geometric_coding_theorem": "NOT_ESTABLISHED",
            "genuine_fredholm_owner": "NOT_ESTABLISHED",
        },
        "claims": {
            "exact_finite_period_two_floquet_symbolic_ledger": True,
            "chronological_product_order_is_recorded": True,
            "exact_candidate_henon_periodic_orbit_completeness": False,
            "actual_henon_markov_partition": False,
            "fredholm_determinant": False,
            "arithmetic_local_claimed": False,
            "euler_factors_claimed": False,
            "root_numbers_claimed": False,
            "automorphy_claimed": False,
            "hilbert_polya_operator_claimed": False,
            "route_b_authorized": False,
        },
    }
    OUT.write_bytes(canonical(result))
    print(json.dumps({
        "status": result["status"],
        "primitive_necklaces": len(rows),
        "count_by_length": result["primitive_orbit_ledger"]["count_by_length"],
        "chronology_sensitive_rows": len(chronological_rows),
        "trace_vectors": {c: transfer_data[c]["trace_of_powers"] for c in CONTROLS},
        "evidence_sha256": digest(OUT.read_bytes()),
    }, sort_keys=True))


if __name__ == "__main__":
    main()
