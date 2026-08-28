#!/usr/bin/env python3
"""Producer-independent recursive audit for the C215 Kingman certificate."""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
from pathlib import Path
import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EVIDENCE = ROOT / "results/c215_kingman_evidence.json"
SOURCE_COMMIT = "077a098ac5811e465b69db71b5e6031a4827eb55"
EVAL = {"path": "flow_systems/skills/route-a-evaluator.md", "version": "0.2.0", "sha256": "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"}
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"
HEADLINE = "The partition-valued Kingman coalescent has an exact all-n genealogy, hypoexponential block transitions and branch-length laws"
N_MAX = 12
TIME_VALUES = [F(0), F(1, 5), F(1), F(2)]
S_VALUES = [F(0), F(1, 5), F(1), F(3)]
ELL_VALUES = [F(0), F(1, 5), F(1), F(2), F(4)]
WORKING_DECIMAL_DIGITS = 100


def payload_hash(data: dict) -> str:
    body = dict(data)
    body.pop("payload_sha256", None)
    return sha256(json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def mpq(value: F) -> mp.mpf:
    return mp.mpf(value.numerator) / value.denominator


def rate(k: int) -> F:
    return F(k * (k - 1), 2)


def hypo_transition(i: int, j: int, t: F) -> mp.mpf:
    if j < 1 or j > i:
        return mp.mpf(0)
    if t == 0:
        return mp.mpf(1) if i == j else mp.mpf(0)
    if i == j:
        return mp.exp(-mpq(rate(i)) * mpq(t))
    numerator = mp.mpf(1)
    for m in range(j + 1, i + 1):
        numerator *= mpq(rate(m))
    total = mp.mpf(0)
    for ell in range(j, i + 1):
        denominator = mp.mpf(1)
        for m in range(j, i + 1):
            if m != ell:
                denominator *= mpq(rate(m) - rate(ell))
        total += mp.exp(-mpq(rate(ell)) * mpq(t)) / denominator
    return numerator * total


def mrca_lt(n: int, s: F) -> mp.mpf:
    value = mp.mpf(1)
    for k in range(2, n + 1):
        value *= mpq(rate(k)) / (mpq(rate(k)) + mpq(s))
    return value


def mrca_mean(n: int) -> mp.mpf:
    return sum((1 / mpq(rate(k)) for k in range(2, n + 1)), mp.mpf(0))


def mrca_variance(n: int) -> mp.mpf:
    return sum((1 / (mpq(rate(k)) ** 2) for k in range(2, n + 1)), mp.mpf(0))


def branch_lt(n: int, s: F) -> mp.mpf:
    value = mp.mpf(1)
    for j in range(1, n):
        rr = mp.mpf(j) / 2
        value *= rr / (rr + mpq(s))
    return value


def branch_cdf(n: int, ell: F) -> mp.mpf:
    if n == 1:
        return mp.mpf(1)
    return (1 - mp.exp(-mpq(ell) / 2)) ** (n - 1)


def harmonic(n: int, order: int = 1) -> mp.mpf:
    return sum((mp.mpf(1) / (j ** order) for j in range(1, n + 1)), mp.mpf(0))


def partitions(items: tuple[int, ...]) -> list[tuple[tuple[int, ...], ...]]:
    if not items:
        return [tuple()]
    first, rest = items[0], items[1:]
    out: list[tuple[tuple[int, ...], ...]] = []
    for part in partitions(rest):
        out.append(((first,),) + part)
        for idx in range(len(part)):
            blocks = [tuple(block) for block in part]
            blocks[idx] = tuple(sorted((first,) + blocks[idx]))
            out.append(tuple(blocks))
    return out


def main() -> None:
    ap = argparse.ArgumentParser(); ap.add_argument("--evidence", type=Path, default=DEFAULT_EVIDENCE)
    data = json.loads(ap.parse_args().evidence.read_text())
    mp.mp.dps = WORKING_DECIMAL_DIGITS
    assertions = 0

    def check(condition, message: str) -> None:
        nonlocal assertions
        assertions += 1
        if not condition:
            raise AssertionError(message)

    def keys(obj, expected, where: str) -> None:
        check(isinstance(obj, dict), where + " mapping")
        check(set(obj) == set(expected), where + " keys")

    keys(data, ["schema", "candidate_id", "evaluation_date", "source_commit", "scope_literal", "evaluator", "headline", "frozen_object", "theorem", "regression", "summary", "route_a", "scope_flags", "citations", "nonclaims", "payload_sha256"], "top")
    keys(data["evaluator"], ["path", "version", "sha256"], "evaluator")
    keys(data["frozen_object"], ["phase_space", "process", "generator", "parameters", "clock", "normalization", "determinant_convention", "arithmetic_origin", "allowed_data", "forbidden_data"], "frozen")
    theorem_keys = ["partition_owner", "block_rates", "hypoexponential_transition", "independent_holdings", "mrca_laplace", "mrca_moments", "infinite_absorption", "total_branch_length", "branch_cdf", "n1_boundary", "determinant_boundary"]
    keys(data["theorem"], theorem_keys, "theorem")
    keys(data["regression"], ["n_max", "time_values", "s_values", "ell_values", "transition_rows", "holding_rows", "mrca_rows", "branch_rows", "partition_rows", "limit_rows"], "regression")
    keys(data["summary"], ["transition_row_count", "holding_row_count", "mrca_row_count", "branch_row_count", "partition_row_count", "limit_row_count", "n_max", "serialized_decimal_digits"], "summary")
    keys(data["route_a"], ["tuple", "overall", "route_b_invocation_allowed", "strongest_positive", "strongest_failure"], "route")
    flag_keys = ["uses_target_zero_table", "uses_prime_table", "claims_arithmetic_local_data", "claims_euler_factors", "claims_root_numbers", "claims_automorphy", "claims_target_divisor_or_functional_equation", "claims_hilbert_polya_operator", "invokes_route_b"]
    keys(data["scope_flags"], flag_keys, "scope_flags")
    check(data["schema"] == "hcs-c215-kingman-coalescent-v1", "schema")
    check(data["candidate_id"] == "HCS-C215", "candidate")
    check(data["evaluation_date"] == "2026-08-28", "date")
    check(data["source_commit"] == SOURCE_COMMIT, "source commit")
    check(data["scope_literal"] == SCOPE, "scope")
    check(data["evaluator"] == EVAL, "evaluator lock")
    check(data["headline"] == HEADLINE, "headline")
    expected_frozen = {
        "phase_space": "partitions of [n] for every n>=1, with projective restriction maps",
        "process": "each unordered pair of current blocks merges at rate 1; the block-counting state is K_t",
        "generator": "Q_{k,k-1}=lambda_k=C(k,2), Q_{k,k}=-lambda_k for k>=2, and Q_{1,1}=0",
        "parameters": "sample size n>=1 and physical time t>=0",
        "clock": "physical elapsed time; no fitted or logarithmic clock",
        "normalization": "probability on labelled partitions; conditional on k blocks each merger pair is uniform",
        "determinant_convention": "none; finite Markov transition determinants are not Artin--Mazur zeta functions",
        "arithmetic_origin": "none; this is a scope-locked non-arithmetic genealogical process",
        "allowed_data": "exact integer block rates, rational time/Laplace sentinels and source-local partition combinatorics",
        "forbidden_data": "prime/zero tables, target labels, fitted rates, Euler factors and external observations",
    }
    check(data["frozen_object"] == expected_frozen, "frozen object")
    expected_theorem = {
        "partition_owner": "Kingman n-coalescent on labelled set partitions, consistent under restriction from n+1 to n",
        "block_rates": "K_t is pure death k->k-1 with lambda_k=C(k,2), k>=2, and state 1 absorbing",
        "hypoexponential_transition": "p_{ij}(t)=prod_{m=j+1}^i lambda_m * sum_{ell=j}^i exp(-lambda_ell*t)/prod_{m=j,m!=ell}^i(lambda_m-lambda_ell), with p_{ii}=exp(-lambda_i*t)",
        "independent_holdings": "holding times E_k are independent Exp(lambda_k), independent of the uniform pair-merger jump chain",
        "mrca_laplace": "E[exp(-s T_n)]=prod_{k=2}^n lambda_k/(lambda_k+s)",
        "mrca_moments": "E[T_n]=sum_{k=2}^n 1/lambda_k=2(1-1/n), Var(T_n)=sum_{k=2}^n 1/lambda_k^2",
        "infinite_absorption": "under projective coupling T_n increases to finite T_infinity almost surely; mean limit 2 and variance limit 4*(2*zeta(2)-3)",
        "total_branch_length": "L_n=sum_{k=2}^n k E_k is a sum of independent Exp((k-1)/2) variables; LT=prod_{j=1}^{n-1}(j/2)/(j/2+s), mean=2 H_{n-1}, variance=4 H_{n-1}^{(2)}",
        "branch_cdf": "P(L_n<=ell)=(1-exp(-ell/2))^(n-1) for ell>=0, with the n=1 convention L_1=0",
        "n1_boundary": "n=1 has one partition, K_t=1, T_1=L_1=0 and all transforms equal 1",
        "determinant_boundary": "a finite Markov matrix determinant or trace-log is not an Artin--Mazur dynamical zeta and is not used as one",
    }
    check(data["theorem"] == expected_theorem, "theorem")
    expected_citation = {"key": "Kingman1982", "claim": "partition-valued coalescent and pure-death block-counting construction", "title": "The coalescent", "authors": "John F. C. Kingman", "venue": "Stochastic Processes and their Applications 13, 235--248", "date": "1982", "url": "https://doi.org/10.1016/0304-4149(82)90011-4", "persistent_url": "https://doi.org/10.1016/0304-4149(82)90011-4"}
    keys(data["citations"][0], ["key", "claim", "title", "authors", "venue", "date", "url", "persistent_url"], "citation")
    check(data["citations"] == [expected_citation], "citation")
    check(data["route_a"]["tuple"] == ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "route tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_REJECTED", "route overall")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "route B")
    check(all(v is False for v in data["scope_flags"].values()), "scope flags")
    check(data["payload_sha256"] == payload_hash(data), "payload hash")

    reg = data["regression"]
    check(reg["n_max"] == N_MAX, "n max")
    check(reg["time_values"] == [str(x) for x in TIME_VALUES], "time grid")
    check(reg["s_values"] == [str(x) for x in S_VALUES], "s grid")
    check(reg["ell_values"] == [str(x) for x in ELL_VALUES], "ell grid")
    tol = mp.mpf("1e-64")

    tkeys = ["case_id", "i", "j", "t", "probability"]
    seen = set()
    for idx, row in enumerate(reg["transition_rows"]):
        keys(row, tkeys, f"transition[{idx}]")
        i, j, t = int(row["i"]), int(row["j"]), F(row["t"])
        check(1 <= j <= i <= N_MAX and t in TIME_VALUES, f"transition[{idx}] domain")
        ident = (i, j, str(t)); check(ident not in seen, f"duplicate transition {ident}"); seen.add(ident)
        check(row["case_id"] == f"i{i}_j{j}_t{t}", f"transition[{idx}] id")
        expected = hypo_transition(i, j, t)
        check(abs(mp.mpf(row["probability"]) - expected) < tol, f"transition[{idx}] value")
        check(mp.mpf(row["probability"]) >= -tol, f"transition[{idx}] positivity")
    check(len(seen) == 312, "transition count")
    # Row sums and Chapman--Kolmogorov are independent all-state checks.
    for i in range(1, N_MAX + 1):
        for t in TIME_VALUES:
            total = sum((hypo_transition(i, j, t) for j in range(1, i + 1)), mp.mpf(0))
            check(abs(total - 1) < tol, f"row sum i={i},t={t}")
    for i in range(1, 9):
        for j in range(1, i + 1):
            lhs = hypo_transition(i, j, F(1, 5) + F(1, 5))
            rhs = sum((hypo_transition(i, k, F(1, 5)) * hypo_transition(k, j, F(1, 5)) for k in range(j, i + 1)), mp.mpf(0))
            check(abs(lhs - rhs) < tol, f"Chapman i={i},j={j}")

    hkeys = ["case_id", "k", "lambda", "mean", "variance", "pair_count", "pair_probability"]
    seen = set()
    for idx, row in enumerate(reg["holding_rows"]):
        keys(row, hkeys, f"holding[{idx}]")
        k = int(row["k"]); check(1 <= k <= N_MAX, f"holding[{idx}] domain")
        check(row["case_id"] == ("k1_absorbing" if k == 1 else f"k{k}"), f"holding[{idx}] id")
        if k == 1:
            check(row["lambda"] == row["mean"] == row["variance"] == row["pair_probability"] == "0", f"holding[{idx}] boundary")
            check(row["pair_count"] == 0, f"holding[{idx}] pair count")
        else:
            lam = rate(k); pairs = k * (k - 1) // 2
            check(F(row["lambda"]) == lam, f"holding[{idx}] rate")
            check(abs(mp.mpf(row["mean"]) - 1 / mpq(lam)) < tol, f"holding[{idx}] mean")
            check(abs(mp.mpf(row["variance"]) - 1 / (mpq(lam) ** 2)) < tol, f"holding[{idx}] variance")
            check(row["pair_count"] == pairs, f"holding[{idx}] pair count")
            check(abs(mp.mpf(row["pair_probability"]) - mp.mpf(1) / pairs) < tol, f"holding[{idx}] pair probability")
        seen.add(k)
    check(len(seen) == N_MAX, "holding count")

    mkeys = ["case_id", "n", "s", "laplace", "mean", "variance"]
    seen = set()
    for idx, row in enumerate(reg["mrca_rows"]):
        keys(row, mkeys, f"mrca[{idx}]")
        n, s = int(row["n"]), F(row["s"]); check(1 <= n <= N_MAX and s in S_VALUES, f"mrca[{idx}] domain")
        ident = (n, str(s)); check(ident not in seen, f"duplicate mrca {ident}"); seen.add(ident)
        check(row["case_id"] == f"n{n}_s{s}", f"mrca[{idx}] id")
        check(abs(mp.mpf(row["laplace"]) - mrca_lt(n, s)) < tol, f"mrca[{idx}] LT")
        check(abs(mp.mpf(row["mean"]) - mrca_mean(n)) < tol, f"mrca[{idx}] mean")
        check(abs(mp.mpf(row["variance"]) - mrca_variance(n)) < tol, f"mrca[{idx}] variance")
        if n == 1:
            check(abs(mp.mpf(row["laplace"]) - 1) < tol, f"mrca[{idx}] n1")
    check(len(seen) == 48, "mrca count")

    bkeys = ["case_id", "n", "ell", "laplace_at_one", "cdf", "mean", "variance"]
    seen = set()
    for idx, row in enumerate(reg["branch_rows"]):
        keys(row, bkeys, f"branch[{idx}]")
        n, ell = int(row["n"]), F(row["ell"]); check(1 <= n <= N_MAX and ell in ELL_VALUES, f"branch[{idx}] domain")
        ident = (n, str(ell)); check(ident not in seen, f"duplicate branch {ident}"); seen.add(ident)
        check(row["case_id"] == f"n{n}_ell{ell}", f"branch[{idx}] id")
        check(abs(mp.mpf(row["laplace_at_one"]) - branch_lt(n, F(1))) < tol, f"branch[{idx}] LT")
        check(abs(mp.mpf(row["cdf"]) - branch_cdf(n, ell)) < tol, f"branch[{idx}] CDF")
        check(abs(mp.mpf(row["mean"]) - 2 * harmonic(n - 1)) < tol, f"branch[{idx}] mean")
        check(abs(mp.mpf(row["variance"]) - 4 * harmonic(n - 1, 2)) < tol, f"branch[{idx}] variance")
    check(len(seen) == 60, "branch count")

    pkeys = ["case_id", "n", "bell_number", "pair_count_at_n", "uniform_pair_probability"]
    bell_expected = [1, 2, 5, 15, 52, 203, 877, 4140]
    seen = set()
    for idx, row in enumerate(reg["partition_rows"]):
        keys(row, pkeys, f"partition[{idx}]")
        n = int(row["n"]); check(1 <= n <= 8, f"partition[{idx}] domain")
        check(row["case_id"] == f"n{n}", f"partition[{idx}] id")
        enum_count = len(partitions(tuple(range(n))))
        check(enum_count == bell_expected[n - 1] == row["bell_number"], f"partition[{idx}] Bell")
        pairs = n * (n - 1) // 2
        check(row["pair_count_at_n"] == pairs, f"partition[{idx}] pairs")
        expected_prob = "0" if pairs == 0 else mp.mpf(1) / pairs
        if pairs == 0:
            check(row["uniform_pair_probability"] == "0", f"partition[{idx}] probability")
        else:
            check(abs(mp.mpf(row["uniform_pair_probability"]) - expected_prob) < tol, f"partition[{idx}] probability")
        seen.add(n)
    check(len(seen) == 8, "partition count")

    lkeys = ["case_id", "absorption_probability", "mrca_mean_limit", "mrca_variance_limit", "mrca_laplace_limit", "coupling_statement"]
    check(len(reg["limit_rows"]) == 1, "limit row count")
    keys(reg["limit_rows"][0], lkeys, "limit")
    lim = reg["limit_rows"][0]
    check(lim["case_id"] == "n_to_infinity" and lim["absorption_probability"] == "1" and lim["mrca_mean_limit"] == "2", "limit locks")
    check(abs(mp.mpf(lim["mrca_variance_limit"]) - 4 * (2 * mp.zeta(2) - 3)) < tol, "variance limit")
    check(lim["mrca_laplace_limit"] == "product_{k=2}^infinity lambda_k/(lambda_k+s)", "limit LT")
    check(lim["coupling_statement"] == "under the standard projective coupling T_n increases to a finite T_infinity almost surely", "coupling")

    check(data["summary"] == {"transition_row_count": 312, "holding_row_count": 12, "mrca_row_count": 48, "branch_row_count": 60, "partition_row_count": 8, "limit_row_count": 1, "n_max": 12, "serialized_decimal_digits": 82}, "summary")
    expected_nonclaims = [
        "priority or novelty for the Kingman coalescent or its classical distribution formulae",
        "a finite n grid proves the all-n projective theorem",
        "a Markov transition determinant, trace-log, or Laplace product is an Artin--Mazur zeta, Euler factor, or target determinant",
        "genealogical block counts or branch lengths have arithmetic-prime meaning",
        "a Hilbert-Polya operator, target divisor, Euler factor, root number, automorphy, external review, or Route-B authorization",
    ]
    check(data["nonclaims"] == expected_nonclaims, "nonclaims")
    print(json.dumps({"status": "C215_CHECKER_PASS", "assertions": assertions, "transition_rows": len(reg["transition_rows"]), "holding_rows": len(reg["holding_rows"]), "mrca_rows": len(reg["mrca_rows"]), "branch_rows": len(reg["branch_rows"]), "partition_rows": len(reg["partition_rows"]), "producer_imported": False}, sort_keys=True))


if __name__ == "__main__":
    main()
