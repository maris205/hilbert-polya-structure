#!/usr/bin/env python3
"""Producer-independent strict exact checker for HCS-C333."""
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
EVIDENCE = ROOT / "results/c333_gossip_evidence.json"
EVALUATION = ROOT / "evaluations/route_a/HCS-C333/2026-09-03.yaml"
SOURCE = "5ca65027918c0fce7ef9af82f3faf2e46ed6530c"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
EVALUATION_RAW_SHA256 = "9c442fea09225fd8a036936b37e9a74a71aa63d1dbd4438b2dc015dbc1bb08b7"
EVALUATION_SEMANTIC_SHA256 = "a244080f57e15e0e6d533f0ffaf9fe1f6cb583a33c3bd2adf23ffc6661e1ca1d"
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
MODEL = {
    "state": "x in R^N with N>=2; N=1 is separately static",
    "edge_law": "one unordered pair is selected independently and uniformly at each step",
    "update": "W_ij=I-eta(e_i-e_j)(e_i-e_j)^T",
    "parameter_domain": "0<=eta<=1",
    "centering": "P=I-J/N and y=Px",
    "clock": "discrete source interaction count",
}
THEOREM = {
    "mean": "the sample mean is pathwise invariant and E[y_t]=(1-2eta/(N-1))^t y_0",
    "decomposition": "Sym^2(1-perp) splits orthogonally into explicit scalar, standard, and zero-diagonal centered blocks",
    "spectrum": "the three orthogonal blocks are invariant for all eta; for eta>0 every present nonzero block is a distinct full eigenspace with the stated eigenvalue and multiplicity, while eta=0 is one identity eigenspace of total multiplicity N(N-1)/2",
    "evolution": "the full disagreement second moment and statistical covariance are exact at every time",
    "consensus": "for 0<eta<1 the mean-square law is sharp and implies almost-sure consensus for every initial vector",
    "tail_domain": "the normalized tail bound requires epsilon>0 and nonzero initial disagreement; consensus-line data are fixed pathwise",
    "boundaries": "N=1,2,3 and eta=0,1 are separate; eta=1 is random transposition rather than consensus",
}
REFERENCES = [{
    "identifier": "10.1109/TIT.2006.874516",
    "role": "original randomized-gossip and distributed-averaging source owner",
}]
COLLISIONS = {
    "C183": "random-transposition permutation-chain spectrum; it meets only the eta=1 boundary",
    "C203": "deterministic signed-Laplacian consensus, not iid pair-matrix products",
    "C312": "state-dependent Hegselmann--Krause finite termination, not uniform random-edge relaxation",
    "C322": "continuous-angle Kac collision spectrum, not pairwise coordinate averaging",
}
NONCLAIMS = [
    "No literature-priority claim is made for randomized gossip or for the complete-graph second-moment decomposition.",
    "The moment-transfer eigenvalues are source relaxation data, not target zeros or an orbit zeta.",
    "No target arithmetic datum, Euler factor, root number, automorphy, target divisor, functional equation, Hilbert--Polya operator, or Route-B input is claimed.",
]
EVALUATION_KEYS = {
    "schema", "candidate_id", "title", "evaluation_date", "source_commit", "fixed_epoch",
    "scope_literal", "evaluator_authority", "evaluator_version", "evaluator_authority_sha256",
    "obstruction_id", "candidate_definition", "family", "phase_space", "dynamics", "parameters",
    "parameter_provenance", "arithmetic_origin", "clock", "normalization", "determinant_convention",
    "orbit_cutoff", "precision", "training_data", "forbidden_data", "artifact_paths",
    "a0", "a1", "a2", "a3", "a4", "tuple", "overall_verdict",
    "route_b_invocation_allowed", "route_b_lock_reason", "scope_flags", "theorem_status",
    "finite_evidence_role", "source_owner_tokens",
}
GATES = {
    "a0": ("A0_FAIL", "PROVED"),
    "a1": ("A1_FAIL", "PROVED"),
    "a2": ("A2_FAIL", "STOP_SCOPED"),
    "a3": ("A3_FAIL", "STOP_SCOPED"),
    "a4": ("A4_FORMAL_HINT", "PROVED"),
}
EVALUATION_EXPECTED = {
    "schema": "route-a-evaluation-v0.2.0",
    "candidate_id": "HCS-C333",
    "title": "Complete-graph relaxed randomized gossip covariance spectrum",
    "evaluation_date": "2026-09-03",
    "source_commit": SOURCE,
    "fixed_epoch": 1788393600,
    "scope_literal": SCOPE,
    "evaluator_authority": "flow_systems/skills/route-a-evaluator.md",
    "evaluator_version": "0.2.0",
    "evaluator_authority_sha256": EVALUATOR,
    "obstruction_id": "HEN-O317",
    "candidate_definition": "relaxed uniform unordered-pair randomized gossip on the complete graph",
    "family": "stochastic switched linear averaging dynamics",
    "phase_space": "real N-vectors with the conserved consensus line and its orthogonal disagreement space",
    "dynamics": "independently select an unordered pair and apply I minus eta times its difference projector",
    "parameters": "integer N at least one and relaxation eta in the closed unit interval",
    "parameter_provenance": "source graph size and relaxation only, never target-fitted",
    "arithmetic_origin": "none",
    "clock": "source discrete interaction count",
    "normalization": "every unordered edge has probability one over N choose two for N at least two",
    "determinant_convention": "none",
    "orbit_cutoff": "exact all-time first and second moment theorem; time-three word enumeration is receipt-only",
    "precision": "exact rational matrices and identities",
    "training_data": "none",
    "forbidden_data": "target arithmetic local data, Euler factors, root numbers, automorphy, target divisor or functional equation, target zeros, Hilbert-Polya operators, Route B",
    "artifact_paths": ["results/c333_gossip_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"],
    "a0": {
        "verdict": "A0_FAIL", "evidence_status": "PROVED",
        "strongest_evidence": "no arithmetic source exists",
        "strongest_failure": "graph vertices, pair choices, relaxation, and interaction count do not intrinsically encode rational primes or prime powers",
    },
    "a1": {
        "verdict": "A1_FAIL", "evidence_status": "PROVED",
        "strongest_evidence": "the stochastic random-matrix owner and every second moment are exact",
        "strongest_failure": "random pair words are not a deterministic isolated primitive-orbit ledger with an arithmetic clock",
    },
    "a2": {
        "verdict": "A2_FAIL", "evidence_status": "STOP_SCOPED",
        "strongest_evidence": "none",
        "strongest_failure": "no primitive-orbit zeta or target Fredholm determinant is defined",
    },
    "a3": {
        "verdict": "A3_FAIL", "evidence_status": "STOP_SCOPED",
        "strongest_evidence": "the finite-dimensional second-moment transfer is exactly diagonalized",
        "strongest_failure": "a source moment spectrum is not analytic continuation, a target divisor, or a Weil compression",
    },
    "a4": {
        "verdict": "A4_FORMAL_HINT", "evidence_status": "PROVED",
        "strongest_evidence": "pair maps are symmetric and the second-moment transfer is self-adjoint on the source Frobenius space",
        "strongest_failure": "the dissipative random products provide no natural same-clock unitary, scattering, or Hamiltonian quantization",
    },
    "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
    "overall_verdict": "ROUTE_A_REJECTED",
    "route_b_invocation_allowed": False,
    "route_b_lock_reason": "a formal symmetric-moment hint is below A4_ROUTE_B_READY and every arithmetic layer fails",
    "scope_flags": FLAGS,
    "theorem_status": "PROVABLE_AS_STATED",
    "finite_evidence_role": "convention and implementation receipt, not proof",
    "source_owner_tokens": ["10.1109/TIT.2006.874516"],
}


class UniqueLoader(yaml.SafeLoader):
    pass


UniqueLoader.yaml_implicit_resolvers = {
    key: [(tag, regexp) for tag, regexp in values if tag != "tag:yaml.org,2002:timestamp"]
    for key, values in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def unique_mapping(loader, node, deep=False):
    result = {}
    for key_node, value_node in node.value:
        if key_node.tag == "tag:yaml.org,2002:merge":
            raise ValueError("YAML merge forbidden")
        key = loader.construct_object(key_node, deep=deep)
        if type(key) is not str or key in result:
            raise ValueError("duplicate or non-string YAML key")
        result[key] = loader.construct_object(value_node, deep=deep)
    return result


UniqueLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, unique_mapping)


def duplicate_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def strict_json(path: Path):
    value = json.loads(
        path.read_text(), object_pairs_hook=duplicate_pairs,
        parse_constant=lambda token: (_ for _ in ()).throw(ValueError(f"nonfinite {token}")),
    )
    if type(value) is not dict:
        raise TypeError("JSON root must be object")
    return value


def strict_yaml(path: Path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("YAML aliases forbidden")
    value = yaml.load(raw, Loader=UniqueLoader)
    if type(value) is not dict:
        raise TypeError("YAML root must be object")
    return value


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def semantic_hash(value) -> str:
    return sha(json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())


def qstr(value: Fraction) -> str:
    return str(value.numerator) if value.denominator == 1 else f"{value.numerator}/{value.denominator}"


def frac(value) -> Fraction:
    if type(value) is not str:
        raise TypeError("rational must be string")
    result = Fraction(value)
    if qstr(result) != value:
        raise ValueError("noncanonical rational")
    return result


def matrix(value, n: int):
    if type(value) is not list or len(value) != n or any(type(row) is not list or len(row) != n for row in value):
        raise TypeError("matrix shape")
    return [[frac(entry) for entry in row] for row in value]


def vector(value, n: int):
    if type(value) is not list or len(value) != n:
        raise TypeError("vector shape")
    return [frac(entry) for entry in value]


def zmat(n):
    return [[Fraction(0) for _ in range(n)] for _ in range(n)]


def identity(n):
    result = zmat(n)
    for i in range(n):
        result[i][i] = 1
    return result


def madd(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a))] for i in range(len(a))]


def mscale(c, a):
    return [[c * entry for entry in row] for row in a]


def mmul(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b))]
            for i in range(len(a))]


def mvec(a, x):
    return [sum(a[i][j] * x[j] for j in range(len(x))) for i in range(len(x))]


def outer(x):
    return [[u * v for v in x] for u in x]


def tr(a):
    return sum(a[i][i] for i in range(len(a)))


def dot(a, b):
    return sum(a[i][j] * b[i][j] for i in range(len(a)) for j in range(len(a)))


def center(n):
    return [[Fraction(int(i == j)) - Fraction(1, n) for j in range(n)] for i in range(n)]


def edge_matrix(n, eta, i, j):
    w = identity(n)
    w[i][i] -= eta
    w[j][j] -= eta
    w[i][j] += eta
    w[j][i] += eta
    return w


def transpose(a):
    return [list(row) for row in zip(*a)]


def transfer(a, eta):
    n = len(a)
    total = zmat(n)
    edges = list(itertools.combinations(range(n), 2))
    for i, j in edges:
        w = edge_matrix(n, eta, i, j)
        total = madd(total, mmul(mmul(w, a), w))
    return mscale(Fraction(1, len(edges)), total)


def rank(a):
    work = [list(row) for row in a]
    nrow, ncol = len(work), len(work[0])
    pivot = 0
    for col in range(ncol):
        choice = next((row for row in range(pivot, nrow) if work[row][col]), None)
        if choice is None:
            continue
        work[pivot], work[choice] = work[choice], work[pivot]
        lead = work[pivot][col]
        work[pivot] = [value / lead for value in work[pivot]]
        for row in range(nrow):
            if row != pivot and work[row][col]:
                factor = work[row][col]
                work[row] = [work[row][j] - factor * work[pivot][j] for j in range(ncol)]
        pivot += 1
        if pivot == nrow:
            break
    return pivot


def leaves(value) -> int:
    if type(value) is dict:
        return sum(leaves(item) for item in value.values())
    if type(value) is list:
        return sum(leaves(item) for item in value)
    return 1


CHECKS = 0


def need(condition: bool, label: str) -> None:
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(label)


def keys(value, expected, label):
    need(type(value) is dict and set(value) == set(expected), label)


def main() -> None:
    if sys.flags.optimize:
        raise RuntimeError("C333 checker refuses optimized Python")
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", type=Path, default=EVIDENCE)
    parser.add_argument("--evaluation", type=Path, default=EVALUATION)
    args = parser.parse_args()
    data = strict_json(args.evidence)
    evaluation = strict_yaml(args.evaluation)

    top = {
        "schema", "candidate_id", "obstruction_id", "source_commit", "fixed_epoch", "scope_literal",
        "evaluator", "evaluation", "model", "theorem_contract", "references", "collision_boundary",
        "nonclaims", "route_a", "scope_flags", "parameter_grid", "spectral_rows", "projector_rows",
        "word_rows", "boundary_rows", "enumeration", "payload_sha256",
    }
    keys(data, top, "top schema")
    need(data["schema"] == "hcs-c333-complete-graph-gossip-v1", "schema")
    need(data["candidate_id"] == "HCS-C333" and data["obstruction_id"] == "HEN-O317", "identity")
    need(data["source_commit"] == SOURCE and data["fixed_epoch"] == 1788393600, "provenance")
    need(data["scope_literal"] == SCOPE, "scope")
    need(data["evaluator"] == {
        "authority": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": EVALUATOR,
    }, "evaluator")
    need(data["model"] == MODEL and data["theorem_contract"] == THEOREM, "model and theorem")
    need(data["references"] == REFERENCES and data["collision_boundary"] == COLLISIONS, "sources and collisions")
    need(data["nonclaims"] == NONCLAIMS and data["scope_flags"] == FLAGS, "scope lock")
    need(data["route_a"] == {
        "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FORMAL_HINT"],
        "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False,
    }, "route A")
    need(payload_hash(data) == data["payload_sha256"], "payload hash")

    raw = args.evaluation.read_bytes()
    need(sha(raw) == EVALUATION_RAW_SHA256, "YAML raw hash")
    need(semantic_hash(evaluation) == EVALUATION_SEMANTIC_SHA256, "YAML semantic hash")
    need(data["evaluation"] == {
        "path": "evaluations/route_a/HCS-C333/2026-09-03.yaml",
        "raw_sha256": EVALUATION_RAW_SHA256,
        "semantic_sha256": EVALUATION_SEMANTIC_SHA256,
    }, "evidence YAML lock")
    keys(evaluation, EVALUATION_KEYS, "YAML schema")
    need(evaluation == EVALUATION_EXPECTED, "YAML full semantic field lock")
    need(evaluation["schema"] == "route-a-evaluation-v0.2.0", "YAML schema literal")
    need(evaluation["candidate_id"] == "HCS-C333" and evaluation["obstruction_id"] == "HEN-O317", "YAML identity")
    need(evaluation["source_commit"] == SOURCE and evaluation["fixed_epoch"] == 1788393600, "YAML provenance")
    need(evaluation["scope_literal"] == SCOPE, "YAML scope")
    need(evaluation["evaluator_authority"] == "flow_systems/skills/route-a-evaluator.md", "YAML authority")
    need(evaluation["evaluator_version"] == "0.2.0" and evaluation["evaluator_authority_sha256"] == EVALUATOR, "YAML evaluator")
    for gate, expected in GATES.items():
        keys(evaluation[gate], {"verdict", "evidence_status", "strongest_evidence", "strongest_failure"}, f"YAML {gate} keys")
        need((evaluation[gate]["verdict"], evaluation[gate]["evidence_status"]) == expected, f"YAML {gate}")
    need(evaluation["tuple"] == data["route_a"]["tuple"], "YAML tuple")
    need(evaluation["overall_verdict"] == "ROUTE_A_REJECTED" and evaluation["route_b_invocation_allowed"] is False, "YAML verdict")
    need(evaluation["scope_flags"] == FLAGS, "YAML flags")
    need(evaluation["theorem_status"] == "PROVABLE_AS_STATED", "YAML theorem")
    need(evaluation["source_owner_tokens"] == ["10.1109/TIT.2006.874516"], "YAML source")
    need(evaluation["artifact_paths"] == ["results/c333_gossip_evidence.json", "THEOREM_PACKAGE.md", "paper/main.pdf"], "YAML artifacts")

    grid = {
        "N_spectral": "2..9", "eta_spectral": [qstr(value) for value in ETAS],
        "N_projector": "3..8", "N_word": "2..5",
        "eta_word": [qstr(value) for value in WORD_ETAS], "time_word": "0..3",
    }
    need(data["parameter_grid"] == grid, "grid")

    spectral_keys = {
        "N", "eta", "edge_count", "mean_multiplier", "lambda0", "lambda1", "lambda2",
        "multiplicity0", "multiplicity1", "multiplicity2", "total_symmetric_dimension",
        "block_status", "distinct_present_eigenvalue_count", "identity_eigenspace_multiplicity",
        "strict_energy_contraction",
    }
    expected_pairs = [(n, eta) for n in range(2, 10) for eta in ETAS]
    need(len(data["spectral_rows"]) == len(expected_pairs), "spectral count")
    for row, (n, eta) in zip(data["spectral_rows"], expected_pairs):
        keys(row, spectral_keys, "spectral row keys")
        need(row["N"] == n and frac(row["eta"]) == eta, "spectral indexing")
        need(row["edge_count"] == n * (n - 1) // 2, "edge count")
        mean = Fraction(1) - 2 * eta / Fraction(n - 1)
        lam0 = Fraction(1) - 4 * eta * (1 - eta) / Fraction(n - 1)
        lam1 = None if n == 2 else Fraction(1) - (4 * eta - 2 * eta * eta) / Fraction(n - 1)
        lam2 = None if n <= 3 else Fraction(1) - 4 * eta / Fraction(n - 1) + 4 * eta * eta / Fraction(n * (n - 1))
        need(frac(row["mean_multiplier"]) == mean and frac(row["lambda0"]) == lam0, "mean and energy rates")
        need(row["lambda1"] is None if lam1 is None else frac(row["lambda1"]) == lam1, "lambda1")
        need(row["lambda2"] is None if lam2 is None else frac(row["lambda2"]) == lam2, "lambda2")
        multiplicities = [1, n - 1 if n >= 3 else 0, n * (n - 3) // 2 if n >= 4 else 0]
        need([row[f"multiplicity{k}"] for k in range(3)] == multiplicities, "multiplicities")
        need(sum(multiplicities) == row["total_symmetric_dimension"] == n * (n - 1) // 2, "dimension sum")
        present_rates = [lam0] + ([lam1] if lam1 is not None else []) + ([lam2] if lam2 is not None else [])
        if eta == 0:
            need(all(rate == 1 for rate in present_rates), "eta-zero merged eigenvalue")
            need(row["block_status"] == "merged_identity_eigenspace", "eta-zero block status")
            need(row["distinct_present_eigenvalue_count"] == 1, "eta-zero eigenvalue count")
            need(row["identity_eigenspace_multiplicity"] == n * (n - 1) // 2,
                 "eta-zero full multiplicity")
        else:
            need(len(set(present_rates)) == len(present_rates), "positive-eta distinct present eigenvalues")
            need(row["block_status"] == "present_nonzero_blocks_are_distinct_full_eigenspaces",
                 "positive-eta block status")
            need(row["distinct_present_eigenvalue_count"] == len(present_rates),
                 "positive-eta eigenvalue count")
            need(row["identity_eigenspace_multiplicity"] is None, "positive-eta no merged multiplicity")
        need(row["strict_energy_contraction"] is (Fraction(0) < eta < Fraction(1)), "contraction chamber")

    projector_keys = {"N", "input", "pi0", "pi1", "pi2", "rank_targets", "pi2_is_zero"}
    need(len(data["projector_rows"]) == 6, "projector count")
    for row, n in zip(data["projector_rows"], range(3, 9)):
        keys(row, projector_keys, "projector row keys")
        need(row["N"] == n, "projector index")
        a, p0, p1, p2 = (matrix(row[name], n) for name in ("input", "pi0", "pi1", "pi2"))
        p = center(n)
        need(a == transpose(a) and mmul(p, mmul(a, p)) == a, "input centered symmetric")
        expected0 = mscale(tr(a) / Fraction(n - 1), p)
        residual = madd(a, mscale(-1, expected0))
        u = [Fraction(n, n - 2) * residual[i][i] for i in range(n)]
        diagonal = [[u[i] if i == j else Fraction(0) for j in range(n)] for i in range(n)]
        expected1 = mmul(p, mmul(diagonal, p))
        expected2 = madd(madd(a, mscale(-1, expected0)), mscale(-1, expected1))
        need((p0, p1, p2) == (expected0, expected1, expected2), "projector formula")
        need(madd(madd(p0, p1), p2) == a, "projector completeness")
        need(dot(p0, p1) == dot(p0, p2) == dot(p1, p2) == 0, "projector orthogonality")
        need(all(sum(p2[i][j] for j in range(n)) == 0 and p2[i][i] == 0 for i in range(n)), "pi2 geometry")
        need(row["rank_targets"] == [1, n - 1, n * (n - 3) // 2], "rank targets")
        # The rank_targets describe invariant-space dimensions, not ranks of
        # these individual receipt matrices.  Every nonzero centered receipt
        # matrix itself has rank at most N-1.
        need(rank(p0) == n - 1 and rank(p1) <= n - 1 and rank(p2) <= n - 1,
             "receipt matrix ranks")
        need(row["pi2_is_zero"] is (n == 3), "low-dimensional pi2")
        need(transfer(a, Fraction(0)) == a, "eta-zero identity on the full receipt matrix")
        for eta in ETAS:
            rates = [
                Fraction(1) - 4 * eta * (1 - eta) / Fraction(n - 1),
                Fraction(1) - (4 * eta - 2 * eta * eta) / Fraction(n - 1),
                None if n == 3 else Fraction(1) - 4 * eta / Fraction(n - 1) + 4 * eta * eta / Fraction(n * (n - 1)),
            ]
            for component, rate in zip((p0, p1, p2), rates):
                if rate is not None:
                    need(transfer(component, eta) == mscale(rate, component), "direct block eigen-equation")

    word_keys = {"N", "eta", "time", "word_count", "initial_disagreement", "mean_vector", "second_moment", "energy"}
    expected_words = [(n, eta, time) for n in range(2, 6) for eta in WORD_ETAS for time in range(4)]
    need(len(data["word_rows"]) == len(expected_words), "word row count")
    total_words = 0
    for row, (n, eta, time) in zip(data["word_rows"], expected_words):
        keys(row, word_keys, "word row keys")
        need(row["N"] == n and frac(row["eta"]) == eta and row["time"] == time, "word indexing")
        y0 = [Fraction(2 * i - (n - 1), 2) for i in range(n)]
        need(vector(row["initial_disagreement"], n) == y0 and sum(y0) == 0, "initial disagreement")
        edges = list(itertools.combinations(range(n), 2))
        count = len(edges)**time
        total_words += count
        sum_state = [Fraction(0) for _ in range(n)]
        second = zmat(n)
        for word in itertools.product(edges, repeat=time):
            state = list(y0)
            for i, j in word:
                state = mvec(edge_matrix(n, eta, i, j), state)
            sum_state = [sum_state[i] + state[i] for i in range(n)]
            second = madd(second, outer(state))
        mean = [value / count for value in sum_state]
        second = mscale(Fraction(1, count), second)
        need(row["word_count"] == count, "word count")
        need(vector(row["mean_vector"], n) == mean, "exhaustive mean")
        need(matrix(row["second_moment"], n) == second and frac(row["energy"]) == tr(second), "exhaustive second moment")
        expected_mean_factor = (Fraction(1) - 2 * eta / Fraction(n - 1))**time
        expected_energy_factor = (Fraction(1) - 4 * eta * (1 - eta) / Fraction(n - 1))**time
        need(mean == [expected_mean_factor * value for value in y0], "closed mean")
        need(tr(second) == expected_energy_factor * sum(value * value for value in y0), "closed energy")
        closed = outer(y0)
        for _ in range(time):
            closed = transfer(closed, eta)
        need(second == closed, "direct transfer iteration")

    boundaries = {
        "N_one": "static process with no selected edge",
        "N_two": "the sole difference is multiplied by 1-2eta; eta=1/2 reaches consensus in one step",
        "N_three": "the zero-diagonal centered block has dimension zero",
        "eta_zero": "identity second-moment transfer; all present blocks merge into eigenvalue 1 with total multiplicity N(N-1)/2",
        "eta_one": "each update is a transposition and disagreement energy is constant",
        "consensus_line": "every update fixes constant vectors for all eta",
    }
    need(data["boundary_rows"] == boundaries, "boundaries")
    enum = data["enumeration"]
    keys(enum, {"spectral_rows", "projector_rows", "word_rows", "exhaustive_edge_words", "audited_leaf_count"}, "enumeration keys")
    need(enum["spectral_rows"] == 56 and enum["projector_rows"] == 6 and enum["word_rows"] == 48, "enumeration row counts")
    need(enum["exhaustive_edge_words"] == total_words, "total words")
    shadow = dict(data)
    shadow.pop("payload_sha256")
    recorded = shadow["enumeration"]["audited_leaf_count"]
    shadow["enumeration"] = dict(shadow["enumeration"])
    shadow["enumeration"]["audited_leaf_count"] = 0
    need(recorded == leaves(shadow) + 1, "audited leaves")
    print(f"C333 independent gossip checker: PASS {CHECKS} checks")


if __name__ == "__main__":
    main()
