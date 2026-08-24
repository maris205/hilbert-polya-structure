#!/usr/bin/env python3
"""Produce the exact C135 edge-roof suspension certificate."""
from __future__ import annotations

import argparse
from hashlib import sha256
import itertools
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c135_edge_roof_evidence.json"
PREFIX = 10
ZERO = (0, 0, 0, 0)


def pclean(poly):
    return {m: c for m, c in poly.items() if c}


def padd(left, right):
    out = dict(left)
    for monomial, coefficient in right.items():
        out[monomial] = out.get(monomial, 0) + coefficient
    return pclean(out)


def pmul(left, right):
    out = {}
    for m1, c1 in left.items():
        for m2, c2 in right.items():
            monomial = tuple(a + b for a, b in zip(m1, m2))
            out[monomial] = out.get(monomial, 0) + c1 * c2
    return pclean(out)


def pvar(index):
    exponent = [0, 0, 0, 0]
    exponent[index] = 1
    return {tuple(exponent): 1}


def eye(n):
    return [[{ZERO: int(i == j)} if i == j else {} for j in range(n)] for i in range(n)]


def mmul(left, right):
    return [[
        sum_poly(pmul(left[i][k], right[k][j]) for k in range(len(right)))
        for j in range(len(right[0]))
    ] for i in range(len(left))]


def sum_poly(items):
    total = {}
    for item in items:
        total = padd(total, item)
    return total


def mpow(matrix, n):
    out = eye(len(matrix))
    base = matrix
    while n:
        if n & 1:
            out = mmul(out, base)
        base = mmul(base, base)
        n //= 2
    return out


def mtrace(matrix):
    return sum_poly(matrix[i][i] for i in range(len(matrix)))


def poly_receipt(poly):
    return {
        ",".join(str(value) for value in monomial): coefficient
        for monomial, coefficient in sorted(poly.items())
    }


def primitive(word):
    n = len(word)
    return not any(n % d == 0 and word == word[:d] * (n // d) for d in range(1, n))


def least_rotation(word):
    return min(word[k:] + word[:k] for k in range(len(word)))


def edge_counts(word):
    counts = [0, 0, 0, 0]
    for k, source in enumerate(word):
        target = word[(k + 1) % len(word)]
        counts[2 * source + target] += 1
    return tuple(counts)


def rotations(word):
    return [word[k:] + word[:k] for k in range(len(word))]


def canonical_payload(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    return json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def build():
    x00, x01, x10, x11 = (pvar(k) for k in range(4))
    M = [[x00, x01], [x10, x11]]
    determinant = {
        ZERO: 1,
        (1, 0, 0, 0): -1,
        (0, 0, 0, 1): -1,
        (1, 0, 0, 1): 1,
        (0, 1, 1, 0): -1,
    }

    rows = []
    representatives = {}
    edge_groups = {}
    rooted_total = 0
    primitive_total = 0
    first_collision_period = None
    for n in range(1, PREFIX + 1):
        trace = mtrace(mpow(M, n))
        rooted_words = list(itertools.product((0, 1), repeat=n))
        enumeration = {}
        for word in rooted_words:
            counts = edge_counts(word)
            enumeration[counts] = enumeration.get(counts, 0) + 1
        assert trace == enumeration
        reps = sorted({least_rotation(word) for word in rooted_words if primitive(word)})
        groups = {}
        for word in reps:
            groups.setdefault(edge_counts(word), []).append("".join(map(str, word)))
        collisions = {",".join(map(str, key)): value for key, value in sorted(groups.items()) if len(value) > 1}
        if collisions and first_collision_period is None:
            first_collision_period = n
        representatives[str(n)] = ["".join(map(str, word)) for word in reps]
        edge_groups[str(n)] = collisions
        rows.append({
            "period": n,
            "rooted_closed_words": len(rooted_words),
            "primitive_cycles": len(reps),
            "trace_edge_count_coefficients": poly_receipt(trace),
            "same_edge_count_primitive_groups": collisions,
        })
        rooted_total += len(rooted_words)
        primitive_total += len(reps)

    words = {
        "symbol_count_collision_C130_a": tuple(int(v) for v in "000111"),
        "symbol_count_collision_C130_b": tuple(int(v) for v in "001011"),
        "remaining_edge_collision": tuple(int(v) for v in "001101"),
    }
    word_receipts = {}
    for name, word in words.items():
        counts = edge_counts(word)
        word_receipts[name] = {
            "word": "".join(map(str, word)),
            "primitive": primitive(word),
            "canonical_rotation": "".join(map(str, least_rotation(word))),
            "edge_counts_N00_N01_N10_N11": list(counts),
            "roof_basis_coefficients_1_sqrt2_sqrt3_sqrt6": list(counts),
            "symbol_counts_N0_N1": [word.count(0), word.count(1)],
        }

    a = edge_counts(words["symbol_count_collision_C130_a"])
    b = edge_counts(words["symbol_count_collision_C130_b"])
    c = edge_counts(words["remaining_edge_collision"])
    assert a == (2, 1, 1, 2)
    assert b == c == (1, 2, 2, 1)
    assert words["remaining_edge_collision"] not in rotations(words["symbol_count_collision_C130_b"])
    separation = tuple(x - y for x, y in zip(a, b))
    assert separation == (1, -1, -1, 1)
    trace6 = mtrace(mpow(M, 6))
    assert trace6[a] == 6 and trace6[b] == 12
    assert first_collision_period == 6

    data = {
        "schema": "HCS-C135-v1",
        "candidate_id": "HCS-C135",
        "date_utc": "2026-08-24",
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "source_lock": {
            "base": "two-sided full binary shift with B=[[1,1],[1,1]]",
            "roof_matrix": [["1", "sqrt(2)"], ["sqrt(3)", "sqrt(6)"]],
            "suspension": "(Sigma_B x R)/((x,t+tau_(x0,x1))~(sigma(x),t))",
            "clock": "continuous edge-roof time with base return count retained",
            "normalization": "one unit transition weight and the literal ordered edge basis (1,sqrt(2),sqrt(3),sqrt(6))",
            "determinant_convention": "d_tau(s)=det(I-M_tau(s))",
            "precision": "exact integer edge-count vectors in the Q-basis (1,sqrt(2),sqrt(3),sqrt(6))",
            "cutoff": "none in theorem; periods 1 through 10 are replay only",
            "forbidden_data": "external prime or zero tables, arithmetic/local factors, root numbers, and Route-B inputs",
        },
        "frozen_model": {
            "formal_edge_matrix": [["x00", "x01"], ["x10", "x11"]],
            "formal_determinant": "Delta=1-x00-x11+x00*x11-x01*x10",
            "formal_determinant_receipt": poly_receipt(determinant),
            "laplace_matrix": [["exp(-s)", "exp(-sqrt(2)*s)"], ["exp(-sqrt(3)*s)", "exp(-sqrt(6)*s)"]],
            "exponential_polynomial": "d_tau(s)=1-exp(-s)-exp(-sqrt(6)*s)+exp(-(1+sqrt(6))*s)-exp(-(sqrt(2)+sqrt(3))*s)",
            "zeta_specialization": "zeta_tau(s)=1/d_tau(s)",
            "entropy_characterization": "h is the unique positive solution of spectral_radius(M_tau(h))=1",
            "basis_independence": "1,sqrt(2),sqrt(3),sqrt(6) are the Q-basis of Q(sqrt(2),sqrt(3))",
        },
        "all_period_identity": {
            "trace_formula": "Tr(M(x)^n)=sum_(rooted closed w, |w|=n) product_(edges ij in w) x_ij",
            "log_determinant": "-log Delta(x)=sum_(n>=1) Tr(M(x)^n)/n",
            "primitive_product": "Delta(x)=product_[gamma primitive](1-product_ij x_ij^N_ij(gamma))",
            "suspension_product": "d_tau(s)=product_[gamma primitive](1-exp(-s*ell(gamma)))",
            "roof_length": "ell=N00+sqrt(2)N01+sqrt(3)N10+sqrt(6)N11",
            "convergence": "formal in total edge degree and absolutely for Re(s)>h; d_tau is entire and zeta_tau meromorphic",
            "all_period": True,
            "replay_cutoff_is_not_theorem_cutoff": True,
        },
        "edge_sector_theorem": {
            "injectivity": "equal roof lengths imply equal directed edge-count vectors by Q-basis independence",
            "flow_conservation": "every closed binary word satisfies N01=N10",
            "observable_off_diagonal_combination": "periodic data depend on tau01 and tau10 only through tau01+tau10",
            "orientation_blindness": "tau01-tau10 is invisible to every periodic trace and determinant coefficient",
            "nonlattice_witness": "the fixed cycles [0] and [1] have lengths 1 and sqrt(6), whose ratio is irrational",
            "no_imaginary_period": "d_tau(s+iT)=d_tau(s) for every s forces T=0",
        },
        "controls": {
            "word_receipts": word_receipts,
            "separated_pair": ["000111", "001011"],
            "separation_vector_1_sqrt2_sqrt3_sqrt6": list(separation),
            "separation_statement": "ell(000111)-ell(001011)=1-sqrt(2)-sqrt(3)+sqrt(6), which is nonzero",
            "period6_trace_multiplicity_000111_sector": 6,
            "period6_trace_multiplicity_001011_sector": 12,
            "remaining_collision_pair": ["001011", "001101"],
            "remaining_collision_edge_counts": [1, 2, 2, 1],
            "remaining_collision_is_nonrotation": True,
            "first_same_edge_count_primitive_collision_period": first_collision_period,
            "C130_destination_symbol_control": "tau_ij=rho_j with rho=(1,sqrt(2)) gives both 000111 and 001011 the length 3+3sqrt(2)",
        },
        "replay_prefix": {
            "period_limit": PREFIX,
            "rows": rows,
            "primitive_representatives": representatives,
            "same_edge_count_groups": edge_groups,
            "rooted_closed_words_total": rooted_total,
            "primitive_cycles_total": primitive_total,
        },
        "progress_and_boundary": {
            "progress_over_C130": "refines the nonlattice clock from symbol populations to admissible directed-edge-count vectors and separates 000111 from 001011",
            "remaining_internal_obstruction": "distinct primitive necklaces with the same edge-count vector remain aggregated, and binary periodic data cannot see off-diagonal orientation asymmetry",
            "target_obstruction": "no target divisor, functional equation, counting law, or arithmetic interpretation is compared",
        },
        "route_a": {
            "tuple": ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_EXPLORATORY",
            "A1_qualification": "ALL_PERIOD_INTRINSIC_PRIMITIVE_SUSPENSION_ORBITS_WITH_NO_PRIME_LIKE_TARGET_CORRESPONDENCE",
            "A2_qualification": "EXACT SOURCE DETERMINANT AND PRIMITIVE PRODUCT BUT NO FROZEN TARGET DIVISOR MATCH",
            "A3_qualification": "NO TARGET FUNCTIONAL EQUATION GAMMA FACTOR COUNTING LAW OR CONTINUATION COMPARISON",
            "A4_qualification": "NO NATURAL SELF_ADJOINT UNITARY SCATTERING OR HAMILTONIAN LIFT",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "scope": "NO_BAD_EULER_OR_ROOT_NUMBER",
            "uses_prime_table": False,
            "uses_zero_table": False,
            "claims_arithmetic_euler_factors": False,
            "claims_root_number": False,
            "claims_automorphy": False,
            "claims_hilbert_polya": False,
            "uses_route_b_inputs": False,
        },
        "nonclaims": [
            "orbit injectivity inside one directed-edge-count sector",
            "recovery of the antisymmetric off-diagonal roof component",
            "an arithmetic Euler product or local factorization",
            "a target zero or pole divisor match, functional equation, or counting law",
            "a natural self-adjoint Hilbert--Polya operator",
            "Route-B authorization or a solution of the larger program",
        ],
    }
    data["payload_sha256"] = sha256(canonical_payload(data)).hexdigest()
    return data


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()
    data = build()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    raw = json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    args.output.write_text(raw)
    print(json.dumps({
        "status": "C135_EXACT_EVIDENCE_PASS",
        "evidence_sha256": sha256(raw.encode()).hexdigest(),
        "payload_sha256": data["payload_sha256"],
        "rooted_words_through_10": data["replay_prefix"]["rooted_closed_words_total"],
        "primitive_cycles_through_10": data["replay_prefix"]["primitive_cycles_total"],
        "first_edge_collision_period": data["controls"]["first_same_edge_count_primitive_collision_period"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
