#!/usr/bin/env python3
"""Deterministic exact-rational evidence producer for HCS-C333."""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import sys
from fractions import Fraction
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c333_gossip_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C333/2026-09-03.yaml"
SOURCE = "5ca65027918c0fce7ef9af82f3faf2e46ed6530c"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EPOCH = 1788393600
ETAS = [Fraction(0), Fraction(1, 4), Fraction(1, 3), Fraction(1, 2),
        Fraction(2, 3), Fraction(3, 4), Fraction(1)]
WORD_ETAS = [Fraction(1, 3), Fraction(1, 2), Fraction(2, 3)]

FLAGS = {
    "claims_target_arithmetic_local_data": False,
    "claims_target_euler_factors": False,
    "claims_root_number": False,
    "claims_automorphy": False,
    "claims_target_divisor_or_counting_law": False,
    "claims_target_functional_equation": False,
    "claims_target_zero_match": False,
    "claims_hilbert_polya_operator": False,
    "invokes_route_b": False,
}


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def zero(n: int, m: int | None = None) -> list[list[Fraction]]:
    return [[Fraction(0) for _ in range(n if m is None else m)] for _ in range(n)]


def eye(n: int) -> list[list[Fraction]]:
    result = zero(n)
    for i in range(n):
        result[i][i] = Fraction(1)
    return result


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scale(c: Fraction, a):
    return [[c * value for value in row] for row in a]


def mul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b)))
             for j in range(len(b[0]))] for i in range(len(a))]


def transpose(a):
    return [list(row) for row in zip(*a)]


def matvec(a, x):
    return [sum(a[i][j] * x[j] for j in range(len(x))) for i in range(len(a))]


def outer(x, y=None):
    if y is None:
        y = x
    return [[u * v for v in y] for u in x]


def trace(a):
    return sum(a[i][i] for i in range(len(a)))


def serialize_matrix(a):
    return [[qstr(value) for value in row] for row in a]


def serialize_vector(x):
    return [qstr(value) for value in x]


def centering(n: int):
    return [[Fraction(int(i == j)) - Fraction(1, n) for j in range(n)] for i in range(n)]


def pair_matrix(n: int, eta: Fraction, i: int, j: int):
    result = eye(n)
    result[i][i] -= eta
    result[j][j] -= eta
    result[i][j] += eta
    result[j][i] += eta
    return result


def projectors(a):
    n = len(a)
    p = centering(n)
    pi0 = scale(trace(a) / Fraction(n - 1), p)
    if n == 2:
        return pi0, zero(n), zero(n)
    residual = add(a, scale(Fraction(-1), pi0))
    u = [Fraction(n, n - 2) * residual[i][i] for i in range(n)]
    pi1 = mul(mul(p, [[u[i] if i == j else Fraction(0) for j in range(n)] for i in range(n)]), p)
    pi2 = add(add(a, scale(Fraction(-1), pi0)), scale(Fraction(-1), pi1))
    return pi0, pi1, pi2


def eigenvalues(n: int, eta: Fraction):
    lam0 = Fraction(1) - 4 * eta * (1 - eta) / Fraction(n - 1)
    if n == 2:
        return lam0, None, None
    lam1 = Fraction(1) - (4 * eta - 2 * eta * eta) / Fraction(n - 1)
    if n == 3:
        return lam0, lam1, None
    lam2 = Fraction(1) - 4 * eta / Fraction(n - 1) + 4 * eta * eta / Fraction(n * (n - 1))
    return lam0, lam1, lam2


def transfer_closed(a, eta: Fraction, power: int):
    n = len(a)
    pi0, pi1, pi2 = projectors(a)
    lam0, lam1, lam2 = eigenvalues(n, eta)
    result = scale(lam0**power, pi0)
    if lam1 is not None:
        result = add(result, scale(lam1**power, pi1))
    if lam2 is not None:
        result = add(result, scale(lam2**power, pi2))
    return result


def spectral_rows():
    rows = []
    for n in range(2, 10):
        for eta in ETAS:
            lam0, lam1, lam2 = eigenvalues(n, eta)
            m0, m1, m2 = 1, (n - 1 if n >= 3 else 0), (n * (n - 3) // 2 if n >= 4 else 0)
            total_dimension = n * (n - 1) // 2
            present_block_count = 1 + int(n >= 3) + int(n >= 4)
            rows.append({
                "N": n,
                "eta": qstr(eta),
                "edge_count": n * (n - 1) // 2,
                "mean_multiplier": qstr(Fraction(1) - 2 * eta / Fraction(n - 1)),
                "lambda0": qstr(lam0),
                "lambda1": None if lam1 is None else qstr(lam1),
                "lambda2": None if lam2 is None else qstr(lam2),
                "multiplicity0": m0,
                "multiplicity1": m1,
                "multiplicity2": m2,
                "total_symmetric_dimension": total_dimension,
                "block_status": (
                    "merged_identity_eigenspace" if eta == 0
                    else "present_nonzero_blocks_are_distinct_full_eigenspaces"
                ),
                "distinct_present_eigenvalue_count": 1 if eta == 0 else present_block_count,
                "identity_eigenspace_multiplicity": total_dimension if eta == 0 else None,
                "strict_energy_contraction": Fraction(0) < eta < Fraction(1),
            })
    return rows


def projector_rows():
    rows = []
    for n in range(3, 9):
        raw = [[Fraction((i + 1) * (j + 2) + (j + 1) * (i + 2))
                + (Fraction(i + 3) if i == j else 0)
                for j in range(n)] for i in range(n)]
        raw = [[(raw[i][j] + raw[j][i]) / 2 for j in range(n)] for i in range(n)]
        p = centering(n)
        a = mul(mul(p, raw), p)
        pi0, pi1, pi2 = projectors(a)
        rows.append({
            "N": n,
            "input": serialize_matrix(a),
            "pi0": serialize_matrix(pi0),
            "pi1": serialize_matrix(pi1),
            "pi2": serialize_matrix(pi2),
            "rank_targets": [1, n - 1, n * (n - 3) // 2],
            "pi2_is_zero": all(value == 0 for row in pi2 for value in row),
        })
    return rows


def exhaustive_moments(n: int, eta: Fraction, time: int):
    edges = list(itertools.combinations(range(n), 2))
    y0 = [Fraction(2 * i - (n - 1), 2) for i in range(n)]
    sums = [Fraction(0) for _ in range(n)]
    second = zero(n)
    words = itertools.product(edges, repeat=time)
    count = 0
    for word in words:
        state = list(y0)
        for i, j in word:
            state = matvec(pair_matrix(n, eta, i, j), state)
        sums = [sums[i] + state[i] for i in range(n)]
        second = add(second, outer(state))
        count += 1
    mean = [value / count for value in sums]
    second = scale(Fraction(1, count), second)
    return y0, count, mean, second


def word_rows():
    rows = []
    for n in range(2, 6):
        for eta in WORD_ETAS:
            for time in range(4):
                y0, count, mean, second = exhaustive_moments(n, eta, time)
                closed = transfer_closed(outer(y0), eta, time)
                if second != closed:
                    raise AssertionError("producer word/closed mismatch")
                rows.append({
                    "N": n,
                    "eta": qstr(eta),
                    "time": time,
                    "word_count": count,
                    "initial_disagreement": serialize_vector(y0),
                    "mean_vector": serialize_vector(mean),
                    "second_moment": serialize_matrix(second),
                    "energy": qstr(trace(second)),
                })
    return rows


def semantic_yaml_hash(raw: str) -> str:
    value = yaml.safe_load(raw)
    canonical = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha(canonical)


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(item) for item in value.values())
    if type(value) is list:
        return sum(leaves(item) for item in value)
    return 1


def make_data():
    evaluation_raw = EVALUATION.read_bytes()
    spectra = spectral_rows()
    projections = projector_rows()
    words = word_rows()
    data = {
        "schema": "hcs-c333-complete-graph-gossip-v1",
        "candidate_id": "HCS-C333",
        "obstruction_id": "HEN-O317",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {
            "authority": "flow_systems/skills/route-a-evaluator.md",
            "version": "0.2.0",
            "sha256": EVALUATOR,
        },
        "evaluation": {
            "path": "evaluations/route_a/HCS-C333/2026-09-03.yaml",
            "raw_sha256": sha(evaluation_raw),
            "semantic_sha256": semantic_yaml_hash(evaluation_raw.decode()),
        },
        "model": {
            "state": "x in R^N with N>=2; N=1 is separately static",
            "edge_law": "one unordered pair is selected independently and uniformly at each step",
            "update": "W_ij=I-eta(e_i-e_j)(e_i-e_j)^T",
            "parameter_domain": "0<=eta<=1",
            "centering": "P=I-J/N and y=Px",
            "clock": "discrete source interaction count",
        },
        "theorem_contract": {
            "mean": "the sample mean is pathwise invariant and E[y_t]=(1-2eta/(N-1))^t y_0",
            "decomposition": "Sym^2(1-perp) splits orthogonally into explicit scalar, standard, and zero-diagonal centered blocks",
            "spectrum": "the three orthogonal blocks are invariant for all eta; for eta>0 every present nonzero block is a distinct full eigenspace with the stated eigenvalue and multiplicity, while eta=0 is one identity eigenspace of total multiplicity N(N-1)/2",
            "evolution": "the full disagreement second moment and statistical covariance are exact at every time",
            "consensus": "for 0<eta<1 the mean-square law is sharp and implies almost-sure consensus for every initial vector",
            "tail_domain": "the normalized tail bound requires epsilon>0 and nonzero initial disagreement; consensus-line data are fixed pathwise",
            "boundaries": "N=1,2,3 and eta=0,1 are separate; eta=1 is random transposition rather than consensus",
        },
        "references": [{
            "identifier": "10.1109/TIT.2006.874516",
            "role": "original randomized-gossip and distributed-averaging source owner",
        }],
        "collision_boundary": {
            "C183": "random-transposition permutation-chain spectrum; it meets only the eta=1 boundary",
            "C203": "deterministic signed-Laplacian consensus, not iid pair-matrix products",
            "C312": "state-dependent Hegselmann--Krause finite termination, not uniform random-edge relaxation",
            "C322": "continuous-angle Kac collision spectrum, not pairwise coordinate averaging",
        },
        "nonclaims": [
            "No literature-priority claim is made for randomized gossip or for the complete-graph second-moment decomposition.",
            "The moment-transfer eigenvalues are source relaxation data, not target zeros or an orbit zeta.",
            "No target arithmetic datum, Euler factor, root number, automorphy, target divisor, functional equation, Hilbert--Polya operator, or Route-B input is claimed.",
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": FLAGS,
        "parameter_grid": {
            "N_spectral": "2..9",
            "eta_spectral": [qstr(value) for value in ETAS],
            "N_projector": "3..8",
            "N_word": "2..5",
            "eta_word": [qstr(value) for value in WORD_ETAS],
            "time_word": "0..3",
        },
        "spectral_rows": spectra,
        "projector_rows": projections,
        "word_rows": words,
        "boundary_rows": {
            "N_one": "static process with no selected edge",
            "N_two": "the sole difference is multiplied by 1-2eta; eta=1/2 reaches consensus in one step",
            "N_three": "the zero-diagonal centered block has dimension zero",
            "eta_zero": "identity second-moment transfer; all present blocks merge into eigenvalue 1 with total multiplicity N(N-1)/2",
            "eta_one": "each update is a transposition and disagreement energy is constant",
            "consensus_line": "every update fixes constant vectors for all eta",
        },
        "enumeration": {
            "spectral_rows": len(spectra),
            "projector_rows": len(projections),
            "word_rows": len(words),
            "exhaustive_edge_words": sum(row["word_count"] for row in words),
            "audited_leaf_count": 0,
        },
    }
    before = leaves(data)
    data["enumeration"]["audited_leaf_count"] = before + 1
    body = json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    data["payload_sha256"] = sha(body)
    return data


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C333 producer refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=OUTPUT)
    args = parser.parse_args()
    data = make_data()
    raw = json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(raw)
    print(
        "C333_PRODUCER_PASS "
        f"{data['enumeration']['spectral_rows']} "
        f"{data['enumeration']['word_rows']} "
        f"{data['enumeration']['audited_leaf_count']} "
        f"{data['payload_sha256']}"
    )


if __name__ == "__main__":
    main()
