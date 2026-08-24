#!/usr/bin/env python3
"""Independent standard-library checker for C135; imports no producer code."""
from __future__ import annotations

from hashlib import sha256
import itertools
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c135_edge_roof_evidence.json"
ZERO = (0, 0, 0, 0)


def add(a, b):
    out = dict(a)
    for monomial, coefficient in b.items():
        out[monomial] = out.get(monomial, 0) + coefficient
    return {m: c for m, c in out.items() if c}


def mul(a, b):
    out = {}
    for ma, ca in a.items():
        for mb, cb in b.items():
            monomial = tuple(x + y for x, y in zip(ma, mb))
            out[monomial] = out.get(monomial, 0) + ca * cb
    return {m: c for m, c in out.items() if c}


def variable(index):
    row = [0, 0, 0, 0]
    row[index] = 1
    return {tuple(row): 1}


def eye(n):
    return [[{ZERO: 1} if i == j else {} for j in range(n)] for i in range(n)]


def mmul(a, b):
    rows = []
    for i in range(len(a)):
        row = []
        for j in range(len(b[0])):
            total = {}
            for k in range(len(b)):
                total = add(total, mul(a[i][k], b[k][j]))
            row.append(total)
        rows.append(row)
    return rows


def mpow(matrix, n):
    out = eye(len(matrix))
    base = matrix
    while n:
        if n & 1:
            out = mmul(out, base)
        base = mmul(base, base)
        n //= 2
    return out


def trace(matrix):
    out = {}
    for i in range(len(matrix)):
        out = add(out, matrix[i][i])
    return out


def receipt(poly):
    return {",".join(map(str, monomial)): coefficient for monomial, coefficient in sorted(poly.items())}


def primitive(word):
    n = len(word)
    return not any(n % d == 0 and word == word[:d] * (n // d) for d in range(1, n))


def least(word):
    return min(word[k:] + word[:k] for k in range(len(word)))


def rotations(word):
    return [word[k:] + word[:k] for k in range(len(word))]


def edge_counts(word):
    out = [0, 0, 0, 0]
    for k, source in enumerate(word):
        target = word[(k + 1) % len(word)]
        out[2 * source + target] += 1
    return tuple(out)


def payload_hash(data):
    body = dict(data)
    body.pop("payload_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_EVIDENCE
    data = json.loads(path.read_text())
    checks = 0

    def ck(condition, label):
        nonlocal checks
        if not condition:
            raise AssertionError(label)
        checks += 1

    def keys(mapping, expected, label):
        ck(set(mapping) == set(expected), label)

    keys(data, {"schema", "candidate_id", "date_utc", "scope_literal", "source_lock", "frozen_model", "all_period_identity", "edge_sector_theorem", "controls", "replay_prefix", "progress_and_boundary", "route_a", "scope_flags", "nonclaims", "payload_sha256"}, "payload keys")
    ck(data["schema"] == "HCS-C135-v1", "schema")
    ck(data["candidate_id"] == "HCS-C135", "candidate")
    ck(data["date_utc"] == "2026-08-24", "date")
    ck(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    ck(data["payload_sha256"] == payload_hash(data), "payload hash")

    lock = data["source_lock"]
    keys(lock, {"base", "roof_matrix", "suspension", "clock", "normalization", "determinant_convention", "precision", "cutoff", "forbidden_data"}, "lock keys")
    ck(lock["base"] == "two-sided full binary shift with B=[[1,1],[1,1]]", "base")
    ck(lock["roof_matrix"] == [["1", "sqrt(2)"], ["sqrt(3)", "sqrt(6)"]], "roof matrix")
    ck(lock["determinant_convention"] == "d_tau(s)=det(I-M_tau(s))", "det convention")
    ck(lock["precision"] == "exact integer edge-count vectors in the Q-basis (1,sqrt(2),sqrt(3),sqrt(6))", "precision")
    ck("prime or zero tables" in lock["forbidden_data"], "forbidden data")

    x = [variable(k) for k in range(4)]
    M = [[x[0], x[1]], [x[2], x[3]]]
    determinant = {ZERO: 1, (1, 0, 0, 0): -1, (0, 0, 0, 1): -1, (1, 0, 0, 1): 1, (0, 1, 1, 0): -1}
    model = data["frozen_model"]
    keys(model, {"formal_edge_matrix", "formal_determinant", "formal_determinant_receipt", "laplace_matrix", "exponential_polynomial", "zeta_specialization", "entropy_characterization", "basis_independence"}, "model keys")
    ck(model["formal_edge_matrix"] == [["x00", "x01"], ["x10", "x11"]], "formal matrix")
    ck(model["formal_determinant"] == "Delta=1-x00-x11+x00*x11-x01*x10", "formal determinant")
    ck(model["formal_determinant_receipt"] == receipt(determinant), "det receipt")
    ck(model["laplace_matrix"] == [["exp(-s)", "exp(-sqrt(2)*s)"], ["exp(-sqrt(3)*s)", "exp(-sqrt(6)*s)"]], "Laplace matrix")
    ck(model["exponential_polynomial"] == "d_tau(s)=1-exp(-s)-exp(-sqrt(6)*s)+exp(-(1+sqrt(6))*s)-exp(-(sqrt(2)+sqrt(3))*s)", "exp polynomial")
    ck(model["basis_independence"] == "1,sqrt(2),sqrt(3),sqrt(6) are the Q-basis of Q(sqrt(2),sqrt(3))", "basis")

    identity = data["all_period_identity"]
    keys(identity, {"trace_formula", "log_determinant", "primitive_product", "suspension_product", "roof_length", "convergence", "all_period", "replay_cutoff_is_not_theorem_cutoff"}, "identity keys")
    ck(identity["trace_formula"] == "Tr(M(x)^n)=sum_(rooted closed w, |w|=n) product_(edges ij in w) x_ij", "trace formula")
    ck(identity["log_determinant"] == "-log Delta(x)=sum_(n>=1) Tr(M(x)^n)/n", "log determinant")
    ck(identity["primitive_product"] == "Delta(x)=product_[gamma primitive](1-product_ij x_ij^N_ij(gamma))", "primitive product")
    ck(identity["suspension_product"] == "d_tau(s)=product_[gamma primitive](1-exp(-s*ell(gamma)))", "suspension product")
    ck(identity["roof_length"] == "ell=N00+sqrt(2)N01+sqrt(3)N10+sqrt(6)N11", "roof length")
    ck(identity["all_period"] is True and identity["replay_cutoff_is_not_theorem_cutoff"] is True, "all period")

    theorem = data["edge_sector_theorem"]
    keys(theorem, {"injectivity", "flow_conservation", "observable_off_diagonal_combination", "orientation_blindness", "nonlattice_witness", "no_imaginary_period"}, "sector keys")
    ck(theorem["injectivity"] == "equal roof lengths imply equal directed edge-count vectors by Q-basis independence", "sector injectivity")
    ck(theorem["flow_conservation"] == "every closed binary word satisfies N01=N10", "flow conservation")
    ck(theorem["observable_off_diagonal_combination"] == "periodic data depend on tau01 and tau10 only through tau01+tau10", "observable sum")
    ck(theorem["orientation_blindness"] == "tau01-tau10 is invisible to every periodic trace and determinant coefficient", "orientation blindness")
    ck(theorem["nonlattice_witness"] == "the fixed cycles [0] and [1] have lengths 1 and sqrt(6), whose ratio is irrational", "nonlattice")

    prefix = data["replay_prefix"]
    keys(prefix, {"period_limit", "rows", "primitive_representatives", "same_edge_count_groups", "rooted_closed_words_total", "primitive_cycles_total"}, "prefix keys")
    rows = []
    representatives = {}
    collision_groups = {}
    rooted_total = 0
    primitive_total = 0
    first_collision = None
    for n in range(1, 11):
        rooted = list(itertools.product((0, 1), repeat=n))
        enumerated = {}
        for word in rooted:
            counts = edge_counts(word)
            ck(counts[1] == counts[2], f"flow n={n},word={word}")
            enumerated[counts] = enumerated.get(counts, 0) + 1
        polynomial = trace(mpow(M, n))
        ck(polynomial == enumerated, f"trace enumeration n={n}")
        reps = sorted({least(word) for word in rooted if primitive(word)})
        groups = {}
        for word in reps:
            groups.setdefault(edge_counts(word), []).append("".join(map(str, word)))
        collisions = {",".join(map(str, key)): value for key, value in sorted(groups.items()) if len(value) > 1}
        if collisions and first_collision is None:
            first_collision = n
        representatives[str(n)] = ["".join(map(str, word)) for word in reps]
        collision_groups[str(n)] = collisions
        rows.append({"period": n, "rooted_closed_words": len(rooted), "primitive_cycles": len(reps), "trace_edge_count_coefficients": receipt(polynomial), "same_edge_count_primitive_groups": collisions})
        rooted_total += len(rooted)
        primitive_total += len(reps)
    ck(prefix["period_limit"] == 10, "period limit")
    ck(prefix["rows"] == rows, "complete rows")
    ck(prefix["primitive_representatives"] == representatives, "primitive reps")
    ck(prefix["same_edge_count_groups"] == collision_groups, "collision groups")
    ck(prefix["rooted_closed_words_total"] == rooted_total == 2046, "rooted total")
    ck(prefix["primitive_cycles_total"] == primitive_total == 226, "primitive total")
    ck(first_collision == 6, "first collision")

    controls = data["controls"]
    keys(controls, {"word_receipts", "separated_pair", "separation_vector_1_sqrt2_sqrt3_sqrt6", "separation_statement", "period6_trace_multiplicity_000111_sector", "period6_trace_multiplicity_001011_sector", "remaining_collision_pair", "remaining_collision_edge_counts", "remaining_collision_is_nonrotation", "first_same_edge_count_primitive_collision_period", "C130_destination_symbol_control"}, "control keys")
    words = {"symbol_count_collision_C130_a": tuple(map(int, "000111")), "symbol_count_collision_C130_b": tuple(map(int, "001011")), "remaining_edge_collision": tuple(map(int, "001101"))}
    expected_words = {}
    for name, word in words.items():
        counts = edge_counts(word)
        expected_words[name] = {"word": "".join(map(str, word)), "primitive": primitive(word), "canonical_rotation": "".join(map(str, least(word))), "edge_counts_N00_N01_N10_N11": list(counts), "roof_basis_coefficients_1_sqrt2_sqrt3_sqrt6": list(counts), "symbol_counts_N0_N1": [word.count(0), word.count(1)]}
    ck(controls["word_receipts"] == expected_words, "word receipts")
    a = edge_counts(words["symbol_count_collision_C130_a"])
    b = edge_counts(words["symbol_count_collision_C130_b"])
    c = edge_counts(words["remaining_edge_collision"])
    ck(a == (2, 1, 1, 2) and b == c == (1, 2, 2, 1), "edge vectors")
    ck(words["remaining_edge_collision"] not in rotations(words["symbol_count_collision_C130_b"]), "nonrotation")
    ck(controls["separated_pair"] == ["000111", "001011"], "separated pair")
    ck(controls["separation_vector_1_sqrt2_sqrt3_sqrt6"] == [1, -1, -1, 1], "separation vector")
    ck(controls["separation_statement"] == "ell(000111)-ell(001011)=1-sqrt(2)-sqrt(3)+sqrt(6), which is nonzero", "separation statement")
    trace6 = trace(mpow(M, 6))
    ck(controls["period6_trace_multiplicity_000111_sector"] == trace6[a] == 6, "multiplicity 6")
    ck(controls["period6_trace_multiplicity_001011_sector"] == trace6[b] == 12, "multiplicity 12")
    ck(controls["remaining_collision_pair"] == ["001011", "001101"], "collision pair")
    ck(controls["remaining_collision_edge_counts"] == [1, 2, 2, 1], "collision counts")
    ck(controls["remaining_collision_is_nonrotation"] is True, "collision nonrotation flag")
    ck(controls["first_same_edge_count_primitive_collision_period"] == 6, "collision period")
    ck(controls["C130_destination_symbol_control"] == "tau_ij=rho_j with rho=(1,sqrt(2)) gives both 000111 and 001011 the length 3+3sqrt(2)", "C130 control")

    progress = data["progress_and_boundary"]
    keys(progress, {"progress_over_C130", "remaining_internal_obstruction", "target_obstruction"}, "progress keys")
    ck(progress["progress_over_C130"] == "refines the nonlattice clock from symbol populations to admissible directed-edge-count vectors and separates 000111 from 001011", "progress")
    ck(progress["remaining_internal_obstruction"] == "distinct primitive necklaces with the same edge-count vector remain aggregated, and binary periodic data cannot see off-diagonal orientation asymmetry", "boundary")
    route = data["route_a"]
    keys(route, {"tuple", "overall", "A1_qualification", "A2_qualification", "A3_qualification", "A4_qualification", "route_b_invocation_allowed"}, "route keys")
    ck(route["tuple"] == ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "tuple")
    ck(route["overall"] == "ROUTE_A_EXPLORATORY", "overall")
    ck(route["A1_qualification"] == "ALL_PERIOD_INTRINSIC_PRIMITIVE_SUSPENSION_ORBITS_WITH_NO_PRIME_LIKE_TARGET_CORRESPONDENCE", "A1 qualification")
    ck(route["route_b_invocation_allowed"] is False, "route B")
    flags = data["scope_flags"]
    keys(flags, {"scope", "uses_prime_table", "uses_zero_table", "claims_arithmetic_euler_factors", "claims_root_number", "claims_automorphy", "claims_hilbert_polya", "uses_route_b_inputs"}, "scope keys")
    ck(flags == {"scope": "NO_BAD_EULER_OR_ROOT_NUMBER", "uses_prime_table": False, "uses_zero_table": False, "claims_arithmetic_euler_factors": False, "claims_root_number": False, "claims_automorphy": False, "claims_hilbert_polya": False, "uses_route_b_inputs": False}, "scope flags")
    ck(data["nonclaims"] == ["orbit injectivity inside one directed-edge-count sector", "recovery of the antisymmetric off-diagonal roof component", "an arithmetic Euler product or local factorization", "a target zero or pole divisor match, functional equation, or counting law", "a natural self-adjoint Hilbert--Polya operator", "Route-B authorization or a solution of the larger program"], "nonclaims")

    print(json.dumps({"status": "C135_INDEPENDENT_CHECK_PASS", "checks": checks, "evidence": str(path)}, sort_keys=True))


if __name__ == "__main__":
    main()
