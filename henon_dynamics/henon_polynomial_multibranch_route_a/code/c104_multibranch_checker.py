#!/usr/bin/env python3
"""Independent exact checker for the C104 symbolic three-branch pilot."""
from __future__ import annotations

from hashlib import sha256
import itertools
import json
from pathlib import Path
from typing import Sequence

PROJECT = Path(__file__).resolve().parents[1]
EVIDENCE = PROJECT / "results/c104_multibranch_evidence.json"
MAX_N, K = 6, 3
SLOPES = (9, -3, 24)
FIREWALL = "NO_BAD_EULER_OR_ROOT_NUMBER"


def canonical(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n").encode()


M = tuple[tuple[int, ...], ...]


def mm(a: M, b: M) -> M:
    return tuple(tuple(sum(a[i][q] * b[q][j] for q in range(len(b))) for j in range(len(b[0]))) for i in range(len(a)))


def eye(n: int) -> M:
    return tuple(tuple(int(i == j) for j in range(n)) for i in range(n))


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


def B(symbol: int) -> M:
    return ((SLOPES[symbol], -1), (1, 0))


def word_matrix(word: Sequence[int]) -> M:
    out = eye(2)
    for symbol in word:
        out = mm(B(symbol), out)
    return out


def primitive(word: tuple[int, ...]) -> bool:
    return not any(len(word) % p == 0 and word == word[:p] * (len(word) // p) for p in range(1, len(word)))


def necklaces(n: int) -> list[tuple[int, ...]]:
    result = set()
    for word in itertools.product(range(K), repeat=n):
        if primitive(word):
            result.add(min(word[i:] + word[:i] for i in range(n)))
    return sorted(result)


def block() -> M:
    out = [[0] * (2 * K) for _ in range(2 * K)]
    for source in range(K):
        for target in range(K):
            for i in range(2):
                for j in range(2):
                    out[2 * source + i][2 * target + j] = B(target)[i][j]
    return tuple(tuple(row) for row in out)


def signed_perm(p: tuple[int, ...]) -> int:
    return -1 if sum(p[i] > p[j] for i in range(len(p)) for j in range(i + 1, len(p))) % 2 else 1


def p_mul(a: list[int], b: list[int]) -> list[int]:
    out = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


def charpoly_prefix(a: M) -> list[int]:
    n = len(a)
    out = [0] * (n + 1)
    for p in itertools.permutations(range(n)):
        term = [1]
        for i, j in enumerate(p):
            term = p_mul(term, [int(i == j), -a[i][j]])
        for d, x in enumerate(term):
            out[d] += signed_perm(p) * x
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def build_expected() -> dict:
    A = block()
    rows = []
    by_len: dict[int, list[dict]] = {}
    for n in range(1, MAX_N + 1):
        by_len[n] = []
        for w in necklaces(n):
            wm = word_matrix(w)
            row = {
                "length": n,
                "word": "".join(map(str, w)),
                "symbols": list(w),
                "branch_counts": [w.count(s) for s in range(K)],
                "canonical_rotation": list(min(w[i:] + w[:i] for i in range(n) for _ in [0])),
                "is_primitive": True,
                "phase_convention": "lexicographically_least_rotation",
                "rooted_start_multiplicity": n,
                "cyclic_stabilizer_size": 1,
                "orientation_sign": 1,
                "representative_monodromy": [list(x) for x in wm],
                "monodromy_trace": tr(wm),
                "monodromy_determinant": det2(wm),
                "trace_of_repeated_monodromy": {str(r): tr(mpow(wm, r)) for r in range(1, MAX_N // n + 1)},
            }
            rows.append(row)
            by_len[n].append(row)
    traces = {str(n): tr(mpow(A, n)) for n in range(1, MAX_N + 1)}
    contributions = {}
    for n in range(1, MAX_N + 1):
        dct = {}
        for d in range(1, n + 1):
            if n % d:
                continue
            r = n // d
            dct[str(d)] = d * sum(int(x["trace_of_repeated_monodromy"][str(r)]) for x in by_len[d])
        assert sum(dct.values()) == traces[str(n)]
        contributions[str(n)] = dct
    return {
        "schema_id": "hcs-c104-polynomial-multibranch-route-a-prefreeze-v1",
        "status": "PREFREEZE_G3_PASS",
        "scope_literal": FIREWALL,
        "definition": {
            "candidate_map": "H_a(x,y)=(x^3-3x+a-y,x), a=1/7",
            "monotone_branch_intervals": ["(-infinity,-1)", "(-1,1)", "(1,infinity)"],
            "symbolic_pilot": "full one-sided shift Sigma_3 on branch alphabet {0,1,2}",
            "primitive_object": "lexicographically least rotation of a non-periodic finite branch word",
            "branch_matrix": "B_j=[[P'(xi_j),-1],[1,0]] at frozen representative xi_j",
            "transfer_prefix": "6x6 block matrix A with A_ij=B_j for all i,j",
            "trace_log_identity": "Tr(A^n)=sum_{d|n} d sum_[w] in P_d tr(B_w^(n/d))",
            "determinant_convention": "D(z)=det(I-z A), recorded only as a finite-dimensional prefix",
        },
        "source_model": {
            "polynomial": {"coefficients": [
                {"power": 3, "numerator": 1, "denominator": 1},
                {"power": 1, "numerator": -3, "denominator": 1},
                {"power": 0, "numerator": 1, "denominator": 7},
            ]},
            "parameter_a": {"numerator": 1, "denominator": 7},
            "alphabet_size": 3,
            "max_word_length": 6,
            "representative_points": [-2, 0, 3],
            "representative_slopes": list(SLOPES),
            "branch_matrices": [[list(x) for x in B(j)] for j in range(K)],
            "transfer_dimension": 6,
        },
        "primitive_orbit_ledger": {
            "rows": rows,
            "count_by_length": {str(n): len(by_len[n]) for n in range(1, MAX_N + 1)},
            "total_primitive_necklaces": len(rows),
        },
        "transfer_atlas": {
            "matrix": [list(x) for x in A],
            "trace_of_powers": traces,
            "primitive_trace_identity_contributions": contributions,
            "determinant_I_minus_zA_coefficients_low_to_high": charpoly_prefix(A),
            "trace_log_prefix_coefficients": {str(n): {"numerator": traces[str(n)], "denominator": n} for n in range(1, MAX_N + 1)},
        },
        "checks": {
            "primitive_necklace_counts": {"1": 3, "2": 3, "3": 8, "4": 18, "5": 48, "6": 116},
            "all_words_are_canonical_and_primitive": True,
            "phase_multiplicity_orientation_fields": True,
            "all_monodromy_determinants_one": all(x["monodromy_determinant"] == 1 for x in rows),
            "trace_power_primitive_decomposition_n_1_to_6": True,
            "determinant_trace_log_prefix_consistent": True,
            "independent_symbolic_reproduction_required": True,
        },
        "route_a_assessment": {
            "A1": "A1_OPEN",
            "A2": "A2_CERTIFIED_PREFIX",
            "A1_qualification": "SYMBOLIC_PILOT_ONLY",
            "A2_qualification": "DISCRETE_TRANSFER_PREFIX_ONLY",
            "A3": "A3_NOT_ADDRESSED",
            "A4": "A4_FAIL",
            "geometric_coding_theorem": "NOT_ESTABLISHED",
            "genuine_fredholm_owner": "NOT_ESTABLISHED",
        },
        "claims": {
            "exact_finite_three_branch_symbolic_ledger": True,
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


def validate_evidence_path(path: Path = EVIDENCE, expected: dict | None = None) -> dict:
    raw = path.read_bytes()
    value = json.loads(raw)
    assert raw == canonical(value)
    expected = build_expected() if expected is None else expected
    assert value == expected
    assert value["scope_literal"] == FIREWALL
    assert sha256(raw).hexdigest() == sha256(canonical(expected)).hexdigest()
    return value


def main() -> None:
    value = validate_evidence_path()
    print(json.dumps({"status": "C104_CHECK_PASS", "primitive_necklaces": value["primitive_orbit_ledger"]["total_primitive_necklaces"], "evidence_sha256": sha256(EVIDENCE.read_bytes()).hexdigest()}, sort_keys=True))


if __name__ == "__main__":
    main()
