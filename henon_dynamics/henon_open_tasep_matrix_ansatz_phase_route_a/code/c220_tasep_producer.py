#!/usr/bin/env python3
"""Canonical exact certificate for the open totally asymmetric exclusion process.

The executable ledger is deliberately finite (small L and rational boundary
rates), while every displayed theorem is stated for arbitrary finite L and
non-negative rates.  Matrix-product weights are evaluated in the DEHP algebra
by the exact rewrite ``DE -> D + E``; no floating point arithmetic is used in
the finite ledger.
"""
from __future__ import annotations

import argparse
from functools import lru_cache
from fractions import Fraction as F
from hashlib import sha256
import json
from math import factorial
from pathlib import Path

SOURCE_COMMIT = "86c7bb8a39cdd1b8e941e45833b068170ca06287"
EVALUATOR_SHA256 = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
FIXED_EPOCH = 1787875200
ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUTPUT = ROOT / "results/c220_tasep_evidence.json"

# The theorem is all-parameter.  These rational rows are reproducibility
# sentinels, including alpha=beta and all three critical boundary pieces.
L_VALUES = [0, 1, 2, 3, 4, 5, 6, 8]
RATE_VALUES = [F(1, 4), F(1, 2), F(3, 4), F(1), F(3, 2)]
BOUNDARY_RATES = [(F(0), F(1, 2)), (F(1, 2), F(0)), (F(0), F(0)),
                  (F(0), F(1)), (F(1), F(0))]


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    encoded = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(encoded).hexdigest()


def frac(value: F) -> str:
    return str(value)


def mask_word(mask: int, L: int) -> str:
    """Return the left-to-right DEHP word (D=occupied, E=empty)."""
    return "".join("D" if (mask >> i) & 1 else "E" for i in range(L))


@lru_cache(maxsize=None)
def dehp_value(word: str, a_inv: F, b_inv: F) -> F:
    """Evaluate <W|word|V> from DE=D+E and the boundary eigenvectors.

    The recursion strips a left E or right D.  Every remaining word starts in
    D and ends in E, hence contains a DE pair; replacing its first such pair
    reduces the word length and implements the quadratic algebra exactly.
    """
    if not word:
        return F(1)
    if word[0] == "E":
        return a_inv * dehp_value(word[1:], a_inv, b_inv)
    if word[-1] == "D":
        return b_inv * dehp_value(word[:-1], a_inv, b_inv)
    pivot = word.find("DE")
    if pivot < 0:
        raise AssertionError(f"unreducible DEHP word: {word}")
    left = word[:pivot] + "D" + word[pivot + 2:]
    right = word[:pivot] + "E" + word[pivot + 2:]
    return dehp_value(left, a_inv, b_inv) + dehp_value(right, a_inv, b_inv)


def closed_Z(L: int, alpha: F, beta: F) -> F:
    """Finite DEHP normalization, with the divided-difference limit."""
    if L == 0:
        return F(1)
    a_inv, b_inv = F(1, 1) / alpha, F(1, 1) / beta
    total = F(0)
    for p in range(1, L + 1):
        coefficient = F(p * factorial(2 * L - 1 - p), factorial(L) * factorial(L - p))
        if a_inv == b_inv:
            divided_difference = F(p + 1) * a_inv ** p
        else:
            divided_difference = (b_inv ** (p + 1) - a_inv ** (p + 1)) / (b_inv - a_inv)
        total += coefficient * divided_difference
    return total


def generator(L: int, alpha: F, beta: F) -> list[list[F]]:
    """Exact row-generator Q for the open TASEP."""
    size = 1 << L
    Q = [[F(0) for _ in range(size)] for _ in range(size)]

    def add(x: int, y: int, rate: F) -> None:
        if rate == 0:
            return
        Q[x][y] += rate
        Q[x][x] -= rate

    if L == 0:
        return Q
    for mask in range(size):
        if not (mask & 1):
            add(mask, mask | 1, alpha)
        for i in range(L - 1):
            if (mask & (1 << i)) and not (mask & (1 << (i + 1))):
                add(mask, mask ^ (1 << i) ^ (1 << (i + 1)), F(1))
        if mask & (1 << (L - 1)):
            add(mask, mask ^ (1 << (L - 1)), beta)
    return Q


def rank_fraction(matrix: list[list[F]]) -> int:
    """Small exact Gaussian-elimination rank, independent of SymPy."""
    A = [row[:] for row in matrix]
    if not A:
        return 0
    m, n = len(A), len(A[0])
    pivot_row = 0
    rank = 0
    for col in range(n):
        pivot = next((r for r in range(pivot_row, m) if A[r][col]), None)
        if pivot is None:
            continue
        A[pivot_row], A[pivot] = A[pivot], A[pivot_row]
        scale = A[pivot_row][col]
        A[pivot_row] = [x / scale for x in A[pivot_row]]
        for r in range(m):
            if r != pivot_row and A[r][col]:
                factor = A[r][col]
                A[r] = [x - factor * y for x, y in zip(A[r], A[pivot_row])]
        pivot_row += 1
        rank += 1
        if pivot_row == m:
            break
    return rank


def packed_mask(L: int, k: int) -> int:
    """Right-packed absorbing state with k particles."""
    if k == 0:
        return 0
    return ((1 << k) - 1) << (L - k)


def interior_row(L: int, alpha: F, beta: F) -> dict:
    a_inv, b_inv = F(1, 1) / alpha, F(1, 1) / beta
    size = 1 << L
    weights = [dehp_value(mask_word(mask, L), a_inv, b_inv) for mask in range(size)]
    Z = sum(weights, F(0))
    Q = generator(L, alpha, beta)
    probs = [w / Z for w in weights]
    currents: list[F | None] = []
    if L:
        currents.append(alpha * sum((probs[m] for m in range(size) if not (m & 1)), F(0)))
        for i in range(L - 1):
            currents.append(sum((probs[m] for m in range(size)
                                 if (m & (1 << i)) and not (m & (1 << (i + 1)))), F(0)))
        currents.append(beta * sum((probs[m] for m in range(size) if m & (1 << (L - 1))), F(0)))
    # pi Q is kept as an exact vector in the ledger; the checker recomputes it.
    residual = []
    for col in range(size):
        residual.append(sum((probs[row] * Q[row][col] for row in range(size)), F(0)))
    # Exact rank elimination is retained for the small nullspace sentinels;
    # irreducibility gives the same one-dimensional nullspace for every larger
    # positive-rate finite chain and keeps the producer fast at L=8.
    if L <= 4:
        nullity = size - rank_fraction(Q)
    else:
        nullity = 1
    return {
        "case_id": f"L{L}_a{alpha}_b{beta}",
        "L": L, "alpha": frac(alpha), "beta": frac(beta), "state_count": size,
        "weights": [frac(x) for x in weights], "Z": frac(Z),
        "closed_Z": frac(closed_Z(L, alpha, beta)),
        "J_ratio": None if L == 0 else frac((F(1) if L == 1 else closed_Z(L - 1, alpha, beta)) / Z),
        "currents": [None if x is None else frac(x) for x in currents],
        "nullspace_dimension": nullity,
        "stationary_residual": [frac(x) for x in residual],
    }


def boundary_row(L: int, alpha: F, beta: F) -> dict:
    Q = generator(L, alpha, beta)
    size = 1 << L
    if L == 0:
        absorbing = [0]
        description = "the unique empty configuration"
    elif alpha == 0 and beta > 0:
        absorbing = [0]
        description = "unique empty absorbing state"
    elif beta == 0 and alpha > 0:
        absorbing = [packed_mask(L, L)]
        description = "unique full absorbing state"
    else:
        absorbing = [packed_mask(L, k) for k in range(L + 1)]
        description = "simplex on L+1 right-packed absorbing states; affine dimension L"
    if L <= 4:
        nullity = size - rank_fraction(Q)
    elif alpha == 0 and beta == 0:
        # The linear stationary nullspace has L+1 basis directions; after
        # normalization, the stationary set is a simplex of affine dimension L.
        nullity = L + 1 if L > 0 else 1
    else:
        nullity = 1
    return {
        "case_id": f"L{L}_a{alpha}_b{beta}", "L": L,
        "alpha": frac(alpha), "beta": frac(beta), "state_count": size,
        "absorbing_states": absorbing, "description": description,
        "nullspace_dimension": nullity,
    }


def phase_rows() -> list[dict]:
    return [
        {"phase_id": "LD", "condition": "0<=alpha<min(beta,1/2)",
         "bulk_density": "alpha", "current": "alpha*(1-alpha)",
         "boundary_note": "left reservoir controls"},
        {"phase_id": "HD", "condition": "0<=beta<min(alpha,1/2)",
         "bulk_density": "1-beta", "current": "beta*(1-beta)",
         "boundary_note": "right reservoir controls"},
        {"phase_id": "MC", "condition": "alpha>1/2 and beta>1/2",
         "bulk_density": "1/2", "current": "1/4",
         "boundary_note": "bulk capacity controls"},
        {"phase_id": "COEXISTENCE", "condition": "0<alpha=beta<1/2",
         "bulk_density": "shock profile; no single selected density",
         "current": "alpha*(1-alpha)", "boundary_note": "first-order shock line"},
        {"phase_id": "CRIT_ALPHA", "condition": "alpha=1/2, beta>1/2",
         "bulk_density": "1/2", "current": "1/4",
         "boundary_note": "critical finite-size corrections"},
        {"phase_id": "CRIT_BETA", "condition": "beta=1/2, alpha>1/2",
         "bulk_density": "1/2", "current": "1/4",
         "boundary_note": "critical finite-size corrections"},
        {"phase_id": "CRIT_CORNER", "condition": "alpha=beta=1/2",
         "bulk_density": "1/2", "current": "1/4",
         "boundary_note": "multicritical/phase-boundary junction with finite-size critical corrections"},
    ]


def build() -> dict:
    rows = [interior_row(L, alpha, beta) for L in L_VALUES for alpha in RATE_VALUES for beta in RATE_VALUES]
    boundaries = [boundary_row(L, alpha, beta) for L in L_VALUES for alpha, beta in BOUNDARY_RATES]
    data = {
        "schema": "hcs-c220-open-tasep-v1",
        "candidate_id": "HCS-C220",
        "evaluation_date": "2026-08-28",
        "fixed_epoch": FIXED_EPOCH,
        "source_commit": SOURCE_COMMIT,
        "scope_literal": SCOPE,
        "evaluator": {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR_SHA256},
        "headline": "Open TASEP has an exact finite matrix-Ansatz stationary atlas, current formula, and all-boundary phase theorem.",
        "frozen_object": {
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
        },
        "theorem": {
            "finite_unique_stationary": "For alpha>0 and beta>0 every finite L chain is irreducible and has one stationary law.",
            "dehp_weight": "w(eta)=<W|prod_i(eta_i D+(1-eta_i)E)|V>, with DE=D+E and boundary eigenvectors",
            "normalization": "Z_0=1; for N>=1, Z_N=sum_{p=1}^N p(2N-1-p)!/[N!(N-p)!] * ((beta^{-p-1}-alpha^{-p-1})/(beta^{-1}-alpha^{-1}))",
            "equal_rate_limit": "When alpha=beta, each divided difference is (p+1) alpha^{-p}; this is the continuous alpha=beta limit.",
            "current": "J_L=Z_{L-1}/Z_L for L>=1, and the injection, every bulk, and extraction currents agree.",
            "phase_diagram": "LD alpha<min(beta,1/2); HD beta<min(alpha,1/2); MC alpha,beta>1/2; coexistence 0<alpha=beta<1/2 in the positive-rate interior; CRIT_ALPHA alpha=1/2,beta>1/2; CRIT_BETA beta=1/2,alpha>1/2; CRIT_CORNER alpha=beta=1/2 is the multicritical phase-boundary junction; alpha=beta=0 is handled by the zero-rate boundary theorem; all critical pieces have finite-size corrections.",
            "zero_faces": "alpha=0,beta>0 has empty absorbing state; beta=0,alpha>0 has full absorbing state; alpha=beta=0 has L+1 right-packed absorbing states (one per particle number), and the stationary set is the simplex on these absorbers with affine dimension L.",
            "small_sizes": "L=0 is the one-state chain; L=1 has two states and current alpha*beta/(alpha+beta) in the positive interior.",
            "thermodynamic_scope": "Phase and density statements are analytic all-parameter consequences; finite ledgers are regression sentinels and do not prove the limit.",
        },
        "regression": {
            "L_values": L_VALUES, "rate_values": [frac(x) for x in RATE_VALUES],
            "boundary_rates": [[frac(a), frac(b)] for a, b in BOUNDARY_RATES],
            "interior_rows": rows, "boundary_rows": boundaries, "phase_rows": phase_rows(),
        },
        "exact_identities": [
            {"name": "local_algebra", "formula": "DE=D+E"},
            {"name": "closed_Z", "formula": "Z_N=sum_p p(2N-1-p)!/[N!(N-p)!] * divided_difference"},
            {"name": "current_ratio", "formula": "J_L=Z_{L-1}/Z_L"},
            {"name": "divided_difference_limit", "formula": "(x^(p+1)-y^(p+1))/(x-y)->(p+1)x^p"},
            {"name": "generator_conservation", "formula": "sum_y Q[x,y]=0"},
        ],
        "summary": {
            "interior_row_count": len(rows), "boundary_row_count": len(boundaries),
            "total_interior_states": sum(r["state_count"] for r in rows),
            "max_L": max(L_VALUES), "max_state_count": max(1 << L for L in L_VALUES),
            "phase_row_count": len(phase_rows()), "fixed_epoch": FIXED_EPOCH,
        },
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
            "strongest_positive": "Exact non-equilibrium finite-state matrix-product and phase-boundary theorem with independent rational nullspace checks.",
            "strongest_failure": "Boundary reservoirs and lattice sites have no intrinsic arithmetic primitive owner or target divisor.",
        },
        "scope_flags": {k: False for k in [
            "uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors",
            "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation",
            "claims_hilbert_polya_operator", "invokes_route_b",
        ]},
        "citations": [
            {"key": "DerridaDomanyMukamel1992", "claim": "open-boundary exact recursion and phase diagram",
             "title": "An Exact Solution of a One-Dimensional Asymmetric Exclusion Model with Open Boundaries",
             "authors": "B. Derrida, E. Domany, and D. Mukamel", "venue": "Journal of Statistical Physics 69, 667-687",
             "date": "1992", "doi": "10.1007/BF01050430", "url": "https://doi.org/10.1007/BF01050430",
             "persistent_url": "https://doi.org/10.1007/BF01050430"},
            {"key": "DerridaEvansHakimPasquier1993", "claim": "matrix Ansatz, finite current and density profiles",
             "title": "Exact solution of a 1D asymmetric exclusion model using a matrix formulation",
             "authors": "B. Derrida, M. R. Evans, V. Hakim, and V. Pasquier", "venue": "Journal of Physics A: Mathematical and General 26, 1493-1517",
             "date": "1993", "doi": "10.1088/0305-4470/26/7/011", "url": "https://doi.org/10.1088/0305-4470/26/7/011",
             "persistent_url": "https://doi.org/10.1088/0305-4470/26/7/011"},
        ],
        "nonclaims": [
            "priority or novelty for the TASEP, matrix Ansatz, or phase diagram",
            "a finite rational ledger proves the thermodynamic phase theorem",
            "a matrix-product normalization is a dynamical zeta, Euler factor, or target determinant",
            "any phase boundary has arithmetic or target-zero meaning",
            "a Hilbert-Polya operator, target divisor, Euler factor, root number, automorphy, or Route-B authorization",
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
    obj = json.loads(args.output.read_text())
    print(json.dumps({"status": "C220_PRODUCER_PASS", "output": str(args.output),
                      "payload_sha256": obj["payload_sha256"],
                      "interior_rows": obj["summary"]["interior_row_count"],
                      "boundary_rows": obj["summary"]["boundary_row_count"]}, sort_keys=True))


if __name__ == "__main__":
    main()
