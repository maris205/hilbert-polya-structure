#!/usr/bin/env python3
"""Independent exact checker for HCS-C142; imports no producer code."""
from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
import json
from pathlib import Path


def parse_q(text: str) -> Fraction:
    return Fraction(text)


def canonical_hash(payload: dict) -> str:
    work = dict(payload)
    work.pop("payload_sha256", None)
    raw = json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def mm(a, b):
    n = len(a)
    out = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for k in range(n):
            for j in range(n):
                out[i][j] += a[i][k] * b[k][j]
    return out


def finite_matrix(n: int):
    out = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for j in range(n):
        out[0][j] += Fraction(1, 2 ** (j + 1))
        if j + 1 < n:
            out[j + 1][j] += Fraction(1, 2 ** (j + 1))
    return out


def comps(total: int):
    if total == 0:
        return [()]
    ans = []
    for cuts in range(1 << (total - 1)):
        w, last = [], 0
        for j in range(total - 1):
            if cuts & (1 << j):
                w.append(j + 1 - last)
                last = j + 1
        w.append(total - last)
        ans.append(tuple(w))
    return ans


def primitive(w):
    return all(len(w) % d or w != w[:d] * (len(w) // d) for d in range(1, len(w)))


def canon(w):
    return min(w[i:] + w[:i] for i in range(len(w)))


def c(m: int) -> Fraction:
    return Fraction(1, 2 ** (m * (m + 1) // 2))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("evidence", nargs="?", type=Path, default=Path(__file__).resolve().parents[1] / "results/c142_renewal_evidence.json")
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    checks = 0

    def check(cond, message):
        nonlocal checks
        checks += 1
        if not cond:
            raise AssertionError(message)

    check(data["schema"] == "hcs-c142-renewal-evidence-v1", "schema")
    check(data["candidate_id"] == "HCS-C142", "candidate")
    check(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    check(data["payload_sha256"] == canonical_hash(data), "payload hash")
    lock = data["source_lock"]
    check(lock["precision"] == "exact rational arithmetic", "precision")
    check(lock["normalization"] == "a_n=b_n=2^(-(n+1)); no fitted parameter", "normalization")
    check(lock["determinant_convention"] == "D(z)=det_F(I-zT)", "determinant")
    check(lock["cutoff"] == {"coefficient": 16, "finite_section_size": 14, "primitive_clock": 10, "trace": 12}, "cutoffs")

    rows = data["coefficient_ledger"]
    check(len(rows) == 16, "coefficient length")
    for m, row in enumerate(rows, 1):
        check(row["m"] == m, f"coefficient index {m}")
        check(row["triangular_exponent"] == m * (m + 1) // 2, f"exponent {m}")
        check(parse_q(row["c_m"]) == c(m), f"coefficient {m}")

    n = 14
    t = finite_matrix(n)
    power = [row[:] for row in t]
    trace_rows = data["trace_ledger"]
    check(len(trace_rows) == 12, "trace length")
    for k, row in enumerate(trace_rows, 1):
        expected = sum(power[i][i] for i in range(n))
        check(row == {"n": k, "trace_Tn": str(expected.numerator) if expected.denominator == 1 else f"{expected.numerator}/{expected.denominator}"}, f"trace {k}")
        power = mm(power, t)

    for row in data["primitive_ledger"]:
        clock = row["clock"]
        words = sorted({w for w in comps(clock) if primitive(w) and canon(w) == w})
        encoded = ["-".join(map(str, w)) for w in words]
        check(row["count"] == len(words), f"primitive count {clock}")
        check(row["words"] == encoded, f"primitive words {clock}")
        weight = sum((__import__("functools").reduce(lambda x, m: x * c(m), w, Fraction(1)) for w in words), Fraction(0))
        check(parse_q(row["weight_sum"]) == weight, f"primitive weight {clock}")

    theorem = data["operator_theorem"]
    check(theorem["shift_trace_norm"] == "1", "shift trace norm")
    check(theorem["return_trace_norm"] == "1/sqrt(3)", "return trace norm")
    check(theorem["fredholm_determinant_formula"] == "D(z)=1-sum_(m>=1)c_m z^m", "Fredholm formula")
    check(theorem["entire_order"] == "0", "entire order")
    neg = data["negative_control"]
    check(neg["formal_scalar_determinant"] == "(1-3z/4)/(1-z/4)", "negative formal determinant")
    # For every witness size N, the first N columns of the constant-weight
    # unilateral shift, represented in N+1 rows, have Gram matrix (1/4) I_N.
    # Since N is arbitrary, the singular value 1/2 has infinite multiplicity;
    # this is an executable noncompactness receipt rather than a string-only
    # lock on the negative-control verdict.
    witness_size = 16
    shift_columns = [
        [Fraction(1, 2) if row == column + 1 else Fraction(0)
         for row in range(witness_size + 1)]
        for column in range(witness_size)
    ]
    gram = [
        [sum((left * right for left, right in zip(shift_columns[i], shift_columns[j])), Fraction(0))
         for j in range(witness_size)]
        for i in range(witness_size)
    ]
    check(
        neg["operator_fact"] == "the weighted shift has singular value 1/2 with infinite multiplicity"
        and gram == [[Fraction(1, 4) if i == j else Fraction(0) for j in range(witness_size)]
                     for i in range(witness_size)]
        and neg["verdict"] == "NONCOMPACT_NOT_ORDINARY_FREDHOLM_DETERMINANT_CLASS",
        "negative constant-shift singular-value witness",
    )
    check(data["route_a"]["tuple"] == ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_FAIL"], "Route-A tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_EXPLORATORY", "overall")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "Route B")
    check(all(value is False for value in data["claim_boundary"].values()), "claim boundary")
    print(json.dumps({"status": "PASS", "assertions": checks}, sort_keys=True))


if __name__ == "__main__":
    main()
