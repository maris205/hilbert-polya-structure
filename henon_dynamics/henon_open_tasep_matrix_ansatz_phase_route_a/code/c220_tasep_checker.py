#!/usr/bin/env python3
"""Independent exact checker for the C220 open-TASEP certificate.

This file intentionally does not import the producer.  It reconstructs the
DEHP rewrite, generator, divided-difference normalization, currents, and
selected exact nullspaces from the serialized rational rows.
"""
from __future__ import annotations

import argparse
from functools import lru_cache
from fractions import Fraction as F
from hashlib import sha256
import json
from math import factorial
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c220_tasep_evidence.json"
SOURCE_COMMIT = "86c7bb8a39cdd1b8e941e45833b068170ca06287"
EVAL = {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"}
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1787875200
L_VALUES = [0, 1, 2, 3, 4, 5, 6, 8]
RATE_VALUES = [F(1, 4), F(1, 2), F(3, 4), F(1), F(3, 2)]
BOUNDARY_RATES = [(F(0), F(1, 2)), (F(1, 2), F(0)), (F(0), F(0)), (F(0), F(1)), (F(1), F(0))]


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def mask_word(mask: int, L: int) -> str:
    return "".join("D" if (mask >> i) & 1 else "E" for i in range(L))


@lru_cache(maxsize=None)
def dehp_value(word: str, a_inv: F, b_inv: F) -> F:
    # Reverse stripping order from the producer (right D first) is a simple
    # independence guard; both paths implement the same quadratic algebra.
    if not word:
        return F(1)
    if word[-1] == "D":
        return b_inv * dehp_value(word[:-1], a_inv, b_inv)
    if word[0] == "E":
        return a_inv * dehp_value(word[1:], a_inv, b_inv)
    pivot = word.rfind("DE")
    if pivot < 0:
        raise AssertionError(f"unreducible word {word}")
    return (dehp_value(word[:pivot] + "D" + word[pivot + 2:], a_inv, b_inv)
            + dehp_value(word[:pivot] + "E" + word[pivot + 2:], a_inv, b_inv))


def closed_Z(L: int, alpha: F, beta: F) -> F:
    if L == 0:
        return F(1)
    x, y = F(1, 1) / alpha, F(1, 1) / beta
    total = F(0)
    for p in range(1, L + 1):
        c = F(p * factorial(2 * L - 1 - p), factorial(L) * factorial(L - p))
        dd = F(p + 1) * x ** p if x == y else (y ** (p + 1) - x ** (p + 1)) / (y - x)
        total += c * dd
    return total


def generator(L: int, alpha: F, beta: F) -> list[list[F]]:
    size = 1 << L
    Q = [[F(0) for _ in range(size)] for _ in range(size)]

    def add(i: int, j: int, rate: F) -> None:
        if rate:
            Q[i][j] += rate
            Q[i][i] -= rate

    if L == 0:
        return Q
    for mask in range(size):
        if mask & 1 == 0:
            add(mask, mask | 1, alpha)
        for i in range(L - 1):
            if (mask & (1 << i)) and not (mask & (1 << (i + 1))):
                add(mask, mask ^ (1 << i) ^ (1 << (i + 1)), F(1))
        if mask & (1 << (L - 1)):
            add(mask, mask ^ (1 << (L - 1)), beta)
    return Q


def rank_fraction(matrix: list[list[F]]) -> int:
    A = [row[:] for row in matrix]
    if not A:
        return 0
    m, n = len(A), len(A[0])
    row = 0
    rank = 0
    for col in range(n):
        pivot = next((r for r in range(row, m) if A[r][col]), None)
        if pivot is None:
            continue
        A[row], A[pivot] = A[pivot], A[row]
        scale = A[row][col]
        A[row] = [x / scale for x in A[row]]
        for r in range(m):
            if r != row and A[r][col]:
                q = A[r][col]
                A[r] = [x - q * y for x, y in zip(A[r], A[row])]
        row += 1
        rank += 1
        if row == m:
            break
    return rank


def sympy_nullity(Q: list[list[F]]) -> int:
    M = sp.Matrix([[sp.Rational(x.numerator, x.denominator) for x in row] for row in Q])
    return len(M.T.nullspace())


def packed_mask(L: int, k: int) -> int:
    return 0 if k == 0 else ((1 << k) - 1) << (L - k)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    data = json.loads(parser.parse_args().evidence.read_text())
    assertions = 0

    def check(condition: bool, message: str) -> None:
        nonlocal assertions
        assertions += 1
        if not condition:
            raise AssertionError(message)

    def keys(obj: dict, expected: list[str], where: str) -> None:
        check(isinstance(obj, dict), where + " mapping")
        check(set(obj) == set(expected), where + " keys")

    top = ["schema", "candidate_id", "evaluation_date", "fixed_epoch", "source_commit", "scope_literal", "evaluator", "headline", "frozen_object", "theorem", "regression", "exact_identities", "summary", "route_a", "scope_flags", "citations", "nonclaims", "payload_sha256"]
    keys(data, top, "top")
    keys(data["evaluator"], ["path", "version", "sha256"], "evaluator")
    keys(data["frozen_object"], ["state_space", "generator", "matrix_ansatz", "parameters", "clock", "normalization", "determinant_convention", "arithmetic_origin", "allowed_data", "forbidden_data"], "frozen")
    theorem_keys = ["finite_unique_stationary", "dehp_weight", "normalization", "equal_rate_limit", "current", "phase_diagram", "zero_faces", "small_sizes", "thermodynamic_scope"]
    keys(data["theorem"], theorem_keys, "theorem")
    keys(data["regression"], ["L_values", "rate_values", "boundary_rates", "interior_rows", "boundary_rows", "phase_rows"], "regression")
    keys(data["summary"], ["interior_row_count", "boundary_row_count", "total_interior_states", "max_L", "max_state_count", "phase_row_count", "fixed_epoch"], "summary")
    keys(data["route_a"], ["tuple", "overall", "route_b_invocation_allowed", "strongest_positive", "strongest_failure"], "route")

    expected_frozen = {
        "state_space": "binary occupations eta in {0,1}^L with sites ordered left to right",
        "generator": "injection alpha at site 1, bulk 10->01 at rate 1, extraction beta at site L",
        "matrix_ansatz": "DE=D+E; <W|E=alpha^{-1}<W|; D|V>=beta^{-1}|V>",
        "parameters": "finite L>=0 and alpha,beta>=0; bulk rate is normalized to one",
        "clock": "physical continuous time",
        "normalization": "Z_L=<W|(D+E)^L|V>; pi(eta)=<W|word(eta)|V>/Z_L for alpha,beta>0",
        "determinant_convention": "finite Markov generator and matrix-product normalization only; no target determinant",
        "arithmetic_origin": "none; reservoir rates and site labels are source-defined",
        "allowed_data": "exact rational finite-state generators, DEHP rewrites, nullspaces, and asymptotic theorem formulas",
        "forbidden_data": "target primes/zeros, fitted rates, Euler factors, root numbers, automorphy, target divisors, Hilbert-Polya operators",
    }
    expected_theorem = {
        "finite_unique_stationary": "For alpha>0 and beta>0 every finite L chain is irreducible and has one stationary law.",
        "dehp_weight": "w(eta)=<W|prod_i(eta_i D+(1-eta_i)E)|V>, with DE=D+E and boundary eigenvectors",
        "normalization": "Z_0=1; for N>=1, Z_N=sum_{p=1}^N p(2N-1-p)!/[N!(N-p)!] * ((beta^{-p-1}-alpha^{-p-1})/(beta^{-1}-alpha^{-1}))",
        "equal_rate_limit": "When alpha=beta, each divided difference is (p+1) alpha^{-p}; this is the continuous alpha=beta limit.",
        "current": "J_L=Z_{L-1}/Z_L for L>=1, and the injection, every bulk, and extraction currents agree.",
        "phase_diagram": "LD alpha<min(beta,1/2); HD beta<min(alpha,1/2); MC alpha,beta>1/2; coexistence 0<alpha=beta<1/2 in the positive-rate interior; CRIT_ALPHA alpha=1/2,beta>1/2; CRIT_BETA beta=1/2,alpha>1/2; CRIT_CORNER alpha=beta=1/2 is the multicritical phase-boundary junction; alpha=beta=0 is handled by the zero-rate boundary theorem; all critical pieces have finite-size corrections.",
        "zero_faces": "alpha=0,beta>0 has empty absorbing state; beta=0,alpha>0 has full absorbing state; alpha=beta=0 has L+1 right-packed absorbing states (one per particle number), and the stationary set is the simplex on these absorbers with affine dimension L.",
        "small_sizes": "L=0 is the one-state chain; L=1 has two states and current alpha*beta/(alpha+beta) in the positive interior.",
        "thermodynamic_scope": "Phase and density statements are analytic all-parameter consequences; finite ledgers are regression sentinels and do not prove the limit.",
    }
    check(data["frozen_object"] == expected_frozen, "frozen values")
    check(data["theorem"] == expected_theorem, "theorem values")

    check(data["schema"] == "hcs-c220-open-tasep-v1", "schema")
    check(data["candidate_id"] == "HCS-C220", "candidate")
    check(data["evaluation_date"] == "2026-08-28", "date")
    check(data["fixed_epoch"] == FIXED_EPOCH, "epoch")
    check(data["source_commit"] == SOURCE_COMMIT, "source commit")
    check(data["scope_literal"] == SCOPE, "scope")
    check(data["evaluator"] == EVAL, "evaluator lock")
    check(data["headline"] == "Open TASEP has an exact finite matrix-Ansatz stationary atlas, current formula, and all-boundary phase theorem.", "headline")
    check(data["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"], "route tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_REJECTED", "route overall")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "route B")
    check(all(v is False for v in data["scope_flags"].values()), "scope flags")
    check(data["payload_sha256"] == payload_hash(data), "payload hash")

    reg = data["regression"]
    check(reg["L_values"] == L_VALUES, "L grid")
    check(reg["rate_values"] == [str(x) for x in RATE_VALUES], "rate grid")
    check(reg["boundary_rates"] == [[str(a), str(b)] for a, b in BOUNDARY_RATES], "boundary grid")
    expected_interior = len(L_VALUES) * len(RATE_VALUES) ** 2
    check(len(reg["interior_rows"]) == expected_interior, "interior count")
    check(len(reg["boundary_rows"]) == len(L_VALUES) * len(BOUNDARY_RATES), "boundary count")
    seen = set()
    for idx, row in enumerate(reg["interior_rows"]):
        expected_row_keys = ["case_id", "L", "alpha", "beta", "state_count", "weights", "Z", "closed_Z", "J_ratio", "currents", "nullspace_dimension", "stationary_residual"]
        keys(row, expected_row_keys, f"interior[{idx}]")
        L, alpha, beta = int(row["L"]), F(row["alpha"]), F(row["beta"])
        check(L in L_VALUES and alpha in RATE_VALUES and beta in RATE_VALUES, f"interior[{idx}] domain")
        ident = (L, str(alpha), str(beta))
        check(ident not in seen, f"duplicate interior {ident}")
        seen.add(ident)
        check(row["case_id"] == f"L{L}_a{alpha}_b{beta}", f"interior[{idx}] id")
        size = 1 << L
        check(row["state_count"] == size and len(row["weights"]) == size, f"interior[{idx}] size")
        ai, bi = F(1, 1) / alpha, F(1, 1) / beta
        weights = [dehp_value(mask_word(mask, L), ai, bi) for mask in range(size)]
        check(row["weights"] == [str(x) for x in weights], f"interior[{idx}] weights")
        Z = sum(weights, F(0))
        check(F(row["Z"]) == Z, f"interior[{idx}] Z")
        check(F(row["closed_Z"]) == closed_Z(L, alpha, beta), f"interior[{idx}] closed Z")
        Q = generator(L, alpha, beta)
        probs = [w / Z for w in weights]
        residual = [sum((probs[r] * Q[r][c] for r in range(size)), F(0)) for c in range(size)]
        check(row["stationary_residual"] == [str(x) for x in residual], f"interior[{idx}] residual")
        check(all(w > 0 for w in weights), f"interior[{idx}] positive weights")
        if L == 0:
            check(row["currents"] == [] and row["J_ratio"] is None, f"interior[{idx}] L0 current")
        else:
            currents = [alpha * sum((probs[m] for m in range(size) if not (m & 1)), F(0))]
            currents.extend(sum((probs[m] for m in range(size) if (m & (1 << i)) and not (m & (1 << (i + 1)))), F(0)) for i in range(L - 1))
            currents.append(beta * sum((probs[m] for m in range(size) if m & (1 << (L - 1))), F(0)))
            check(row["currents"] == [str(x) for x in currents], f"interior[{idx}] currents")
            check(len(set(currents)) == 1, f"interior[{idx}] current uniformity")
            expected_j = F(1, 1) / Z if L == 1 else closed_Z(L - 1, alpha, beta) / Z
            check(F(row["J_ratio"]) == expected_j == currents[0], f"interior[{idx}] current ratio")
        expected_nullity = size - rank_fraction(Q) if L <= 4 else 1
        check(row["nullspace_dimension"] == expected_nullity, f"interior[{idx}] nullity")
        if L <= 4:
            check(sympy_nullity(Q) == expected_nullity, f"interior[{idx}] SymPy nullspace")
    check(len(seen) == expected_interior, "interior uniqueness")

    seen = set()
    for idx, row in enumerate(reg["boundary_rows"]):
        keys(row, ["case_id", "L", "alpha", "beta", "state_count", "absorbing_states", "description", "nullspace_dimension"], f"boundary[{idx}]")
        L, alpha, beta = int(row["L"]), F(row["alpha"]), F(row["beta"])
        check(L in L_VALUES and (alpha, beta) in BOUNDARY_RATES, f"boundary[{idx}] domain")
        ident = (L, str(alpha), str(beta))
        check(ident not in seen, f"duplicate boundary {ident}")
        seen.add(ident)
        check(row["case_id"] == f"L{L}_a{alpha}_b{beta}", f"boundary[{idx}] id")
        size = 1 << L
        check(row["state_count"] == size, f"boundary[{idx}] size")
        if L == 0:
            expected_abs = [0]
            expected_dim = 1
            expected_description = "the unique empty configuration"
        elif alpha == 0 and beta > 0:
            expected_abs, expected_dim = [0], 1
            expected_description = "unique empty absorbing state"
        elif beta == 0 and alpha > 0:
            expected_abs, expected_dim = [packed_mask(L, L)], 1
            expected_description = "unique full absorbing state"
        else:
            expected_abs, expected_dim = [packed_mask(L, k) for k in range(L + 1)], L + 1
            expected_description = "simplex on L+1 right-packed absorbing states; affine dimension L"
        check(row["absorbing_states"] == expected_abs, f"boundary[{idx}] absorbing states")
        check(row["description"] == expected_description, f"boundary[{idx}] description")
        Q = generator(L, alpha, beta)
        expected_nullity = size - rank_fraction(Q) if L <= 4 else expected_dim
        check(row["nullspace_dimension"] == expected_nullity, f"boundary[{idx}] nullity")
        if L <= 4:
            check(sympy_nullity(Q) == expected_dim, f"boundary[{idx}] SymPy nullspace")
        for state in expected_abs:
            check(all(rate == 0 for rate in Q[state]), f"boundary[{idx}] absorbing witness")
    check(len(seen) == len(L_VALUES) * len(BOUNDARY_RATES), "boundary uniqueness")

    expected_phases = [
        ("LD", "0<=alpha<min(beta,1/2)", "alpha", "alpha*(1-alpha)", "left reservoir controls"),
        ("HD", "0<=beta<min(alpha,1/2)", "1-beta", "beta*(1-beta)", "right reservoir controls"),
        ("MC", "alpha>1/2 and beta>1/2", "1/2", "1/4", "bulk capacity controls"),
        ("COEXISTENCE", "0<alpha=beta<1/2", "shock profile; no single selected density", "alpha*(1-alpha)", "first-order shock line"),
        ("CRIT_ALPHA", "alpha=1/2, beta>1/2", "1/2", "1/4", "critical finite-size corrections"),
        ("CRIT_BETA", "beta=1/2, alpha>1/2", "1/2", "1/4", "critical finite-size corrections"),
        ("CRIT_CORNER", "alpha=beta=1/2", "1/2", "1/4", "multicritical/phase-boundary junction with finite-size critical corrections"),
    ]
    check(len(reg["phase_rows"]) == len(expected_phases), "phase row count")
    for idx, (row, expected) in enumerate(zip(reg["phase_rows"], expected_phases)):
        keys(row, ["phase_id", "condition", "bulk_density", "current", "boundary_note"], f"phase[{idx}]")
        check(tuple(row[k] for k in ["phase_id", "condition", "bulk_density", "current", "boundary_note"]) == expected, f"phase[{idx}] values")

    check(data["summary"] == {"interior_row_count": expected_interior, "boundary_row_count": len(L_VALUES) * len(BOUNDARY_RATES), "total_interior_states": sum(1 << L for L in L_VALUES) * len(RATE_VALUES) ** 2, "max_L": 8, "max_state_count": 256, "phase_row_count": 7, "fixed_epoch": FIXED_EPOCH}, "summary")
    check(len(data["citations"]) == 2, "citation count")
    expected_citations = [
        {"key": "DerridaDomanyMukamel1992", "claim": "open-boundary exact recursion and phase diagram", "title": "An Exact Solution of a One-Dimensional Asymmetric Exclusion Model with Open Boundaries", "authors": "B. Derrida, E. Domany, and D. Mukamel", "venue": "Journal of Statistical Physics 69, 667-687", "date": "1992", "doi": "10.1007/BF01050430", "url": "https://doi.org/10.1007/BF01050430", "persistent_url": "https://doi.org/10.1007/BF01050430"},
        {"key": "DerridaEvansHakimPasquier1993", "claim": "matrix Ansatz, finite current and density profiles", "title": "Exact solution of a 1D asymmetric exclusion model using a matrix formulation", "authors": "B. Derrida, M. R. Evans, V. Hakim, and V. Pasquier", "venue": "Journal of Physics A: Mathematical and General 26, 1493-1517", "date": "1993", "doi": "10.1088/0305-4470/26/7/011", "url": "https://doi.org/10.1088/0305-4470/26/7/011", "persistent_url": "https://doi.org/10.1088/0305-4470/26/7/011"},
    ]
    check(data["citations"] == expected_citations, "citation values")
    for i, citation in enumerate(data["citations"]):
        keys(citation, ["key", "claim", "title", "authors", "venue", "date", "doi", "url", "persistent_url"], f"citation[{i}]")
        check(citation["url"] == citation["persistent_url"] and citation["url"].startswith("https://doi.org/"), f"citation[{i}] DOI URL")
    check(all(isinstance(x, str) for x in data["nonclaims"]), "nonclaims")
    print(json.dumps({"status": "C220_CHECKER_PASS", "assertions": assertions, "interior_rows": len(reg["interior_rows"]), "boundary_rows": len(reg["boundary_rows"]), "sympy_nullspace_rows": sum(1 for r in reg["interior_rows"] + reg["boundary_rows"] if int(r["L"]) <= 4), "producer_imported": False}, sort_keys=True))


if __name__ == "__main__":
    main()
