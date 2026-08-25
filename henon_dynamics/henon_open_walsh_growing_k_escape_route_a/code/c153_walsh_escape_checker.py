#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C153."""
from __future__ import annotations

import argparse
from fractions import Fraction
from functools import lru_cache
from hashlib import sha256
from itertools import product
import json
from math import gcd
from pathlib import Path


class E:
    __slots__ = ("x",)

    def __init__(self, a=0, b=0, c=0, d=0):
        self.x = tuple(Fraction(y) for y in (a, b, c, d))

    def __add__(self, other):
        other = other if isinstance(other, E) else E(other)
        return E(*(u + v for u, v in zip(self.x, other.x)))

    __radd__ = __add__

    def __neg__(self):
        return E(*(-u for u in self.x))

    def __sub__(self, other):
        return self + (-(other if isinstance(other, E) else E(other)))

    def __mul__(self, other):
        other = other if isinstance(other, E) else E(other)
        a, b, c, d = self.x
        e, f, g, h = other.x
        return E(
            a * e + 3 * b * f - c * g - 3 * d * h,
            a * f + b * e - c * h - d * g,
            a * g + 3 * b * h + c * e + 3 * d * f,
            a * h + b * g + c * f + d * e,
        )

    __rmul__ = __mul__

    def __pow__(self, n: int):
        answer, base = E(1), self
        while n:
            if n & 1:
                answer = answer * base
            base = base * base
            n //= 2
        return answer

    def __eq__(self, other):
        other = other if isinstance(other, E) else E(other)
        return self.x == other.x

    def __bool__(self):
        return any(self.x)

    @classmethod
    def read(cls, values):
        return cls(*(Fraction(value) for value in values))

    def receipt(self):
        return [str(v.numerator) if v.denominator == 1 else f"{v.numerator}/{v.denominator}" for v in self.x]


Z, O = E(), E(1)
R = E(0, Fraction(1, 3))
OMEGA = E(Fraction(-1, 2), 0, 0, Fraction(1, 2))
OMEGA2 = OMEGA * OMEGA
TAU = E(0, Fraction(1, 6), Fraction(-1, 2))
Q0 = E(Fraction(-1, 2), 0, 0, Fraction(-1, 6))


def canonical_hash(data):
    work = dict(data)
    work.pop("payload_sha256", None)
    raw = json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


@lru_cache(maxsize=None)
def action_a(source: int):
    if source == 1:
        return ()
    if source == 0:
        return tuple((target, R) for target in range(3))
    return (
        (0, R),
        (1, E(0, Fraction(-1, 6), Fraction(1, 2))),
        (2, E(0, Fraction(-1, 6), Fraction(-1, 2))),
    )


@lru_cache(maxsize=None)
def action_a_power(source: int, exponent: int):
    current = {source: O}
    for _ in range(exponent):
        nxt = {}
        for symbol, amplitude in current.items():
            for target, weight in action_a(symbol):
                nxt[target] = nxt.get(target, Z) + amplitude * weight
        current = nxt
    return tuple(sorted(current.items()))


def b_edges(state):
    return tuple((state[1:] + (target,), weight) for target, weight in action_a(state[0]))


def propagate_b(start, steps):
    current = {start: O}
    for _ in range(steps):
        nxt = {}
        for state, amplitude in current.items():
            for target, weight in b_edges(state):
                nxt[target] = nxt.get(target, Z) + amplitude * weight
        current = nxt
    return current


def predicted_normal_form(start, steps):
    k = len(start)
    q, r = divmod(steps, k)
    ordered = [(start[j], q) for j in range(r, k)] + [(start[j], q + 1) for j in range(r)]
    current = {(): O}
    for source, exponent in ordered:
        nxt = {}
        for prefix, amplitude in current.items():
            for target, weight in action_a_power(source, exponent):
                nxt[prefix + (target,)] = amplitude * weight
        current = nxt
    return current


def trace_powers(limit):
    values = [E(2), TAU]
    for _ in range(2, limit + 1):
        values.append(TAU * values[-1] - Q0 * values[-2])
    return values


def direct_trace(k, n):
    total = Z
    for start in product(range(3), repeat=k):
        total = total + propagate_b(start, n).get(start, Z)
    return total


def rank_value(k, n):
    m = min(n, k)
    return 2**m * 3 ** (k - m)


def divisors(n):
    return [d for d in range(1, n + 1) if n % d == 0]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "evidence",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "results/c153_walsh_escape_evidence.json",
    )
    parser.add_argument("--mutation-fast", action="store_true")
    args = parser.parse_args()
    data = json.loads(args.evidence.read_text())
    assertions = 0

    def check(condition, message):
        nonlocal assertions
        assertions += 1
        if not condition:
            raise AssertionError(message)

    check(data["schema"] == "hcs-c153-walsh-growing-k-escape-v1", "schema")
    check(data["candidate_id"] == "HCS-C153", "candidate")
    check(data["evaluation_date"] == "2026-08-25", "date")
    check(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    check(data["payload_sha256"] == canonical_hash(data), "payload hash")

    lock = data["source_lock"]
    expected_lock = {
        "source_commit": "2d4e6211a254ef49d87718569d23466f4c6dcf4c",
        "object": "B_k(v0 tensor ... tensor v_(k-1))=v1 tensor ... tensor v_(k-1) tensor A*v0",
        "one_qutrit_gate": "A=F3^* diag(1,0,1), F3[j,l]=omega^(j*l)/sqrt(3)",
        "clock": "one application of B_k",
        "normalization": "dimension normalization is 3^(-k); no spectral rescaling",
        "trace_convention": "ordinary finite-dimensional Tr(B_k^n)",
        "rank_cutoff": {"k_max": 24, "n_range": "0<=n<=2k"},
        "fixed_period_cluster_cutoff": 20,
        "alpha_ratios": ["0/1", "1/4", "1/2", "3/4", "1/1", "5/4", "3/2", "2/1"],
        "precision": "exact integers and Q(sqrt(3),i) receipts",
        "allowed_data": "frozen DFT, rank-two projector, tensor shift, exact source traces",
        "forbidden_data": "target zeros or divisors, primes, arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya, Route B",
    }
    for key, value in expected_lock.items():
        check(lock[key] == value, f"source lock {key}")

    one = data["one_qutrit_theorem"]
    check(one["tau_q_sqrt3_i_sqrt3i"] == TAU.receipt(), "tau")
    check(one["q0_q_sqrt3_i_sqrt3i"] == Q0.receipt(), "q0")
    check(bool(Q0) and one["q0_is_nonzero"] is True, "q0 nonzero")
    check(one["zero_eigenvalue_is_simple"] is True, "simple zero")
    check(one["rank_A_power_m"] == "2 for every integer m>=1; rank(A^0)=3", "one-site ranks")
    check(OMEGA**3 == O and OMEGA != O, "root of unity")
    check(action_a(1) == (), "middle hole")
    check(len(action_a(0)) == len(action_a(2)) == 3, "two nonzero columns")

    theorem = data["all_parameter_rank_theorem"]
    check(theorem["statement"] == "rank(B_k^n)=2^min(n,k)*3^(k-min(n,k)) for k>=1,n>=0", "rank statement")
    check(theorem["initial_boundary"] == "n=0 gives B_k^0=I and full rank 3^k", "initial rank")
    rows = theorem["ledger_rows"]
    check(len(rows) == 624, "rank row count")
    cursor = 0
    for k in range(1, 25):
        for n in range(0, 2 * k + 1):
            row = rows[cursor]
            cursor += 1
            q, r = divmod(n, k)
            opened = min(n, k)
            rank = rank_value(k, n)
            check(row["k"] == k and row["n"] == n, f"rank index {k},{n}")
            check(row["q"] == q and row["r"] == r, f"division {k},{n}")
            check(row["opened_tensor_factors"] == opened, f"opened {k},{n}")
            check(row["rank_Bk_power_n"] == rank, f"rank {k},{n}")
            check(row["kernel_dimension"] == 3**k - rank, f"kernel {k},{n}")
            check(row["rank_fraction"] == f"{2**opened}/{3**opened}", f"fraction {k},{n}")

    if not args.mutation_fast:
        for k in range(1, 5):
            for source in product(range(3), repeat=k):
                for n in range(0, 2 * k + 1):
                    check(propagate_b(source, n) == predicted_normal_form(source, n), f"normal form k={k},n={n},source={source}")

    macro = data["macroscopic_escape_theorem"]
    check(macro["time_scale"] == "n_k=floor(alpha*k), alpha>=0", "macro scale")
    check(macro["signed_log_survival_limit"].endswith("min(alpha,1)*log(2/3)"), "signed exponent")
    check(macro["positive_escape_exponent"] == "E(alpha)=min(alpha,1)*log(3/2)", "positive exponent")
    check(macro["alpha_zero_boundary"] == "alpha=0 gives n_k=0 and E(0)=0", "alpha zero")
    alpha_rows = macro["finite_ratio_ledger"]
    check(len(alpha_rows) == 192, "alpha row count")
    index = 0
    for p, q in ((0, 1), (1, 4), (1, 2), (3, 4), (1, 1), (5, 4), (3, 2), (2, 1)):
        for k in range(1, 25):
            row = alpha_rows[index]
            index += 1
            n = p * k // q
            opened = min(n, k)
            coefficient = Fraction(opened, k)
            coefficient_text = str(coefficient.numerator) if coefficient.denominator == 1 else f"{coefficient.numerator}/{coefficient.denominator}"
            check(row["alpha"] == f"{p}/{q}" and row["k"] == k, f"alpha index {p}/{q},{k}")
            check(row["n_floor_alpha_k"] == n, f"alpha floor {p}/{q},{k}")
            check(row["rank"] == rank_value(k, n), f"alpha rank {p}/{q},{k}")
            check(row["finite_k_log_survival_coefficient"] == coefficient_text, f"alpha coefficient {p}/{q},{k}")

    trace_section = data["fixed_period_trace_theorem"]
    traces = trace_powers(20)
    check(trace_section["trace_formula"] == "for d=gcd(n,k), Tr(B_k^n)=t_(n/d)^d", "trace formula")
    check(trace_section["normalized_limit"].startswith("for fixed n, 3^(-k)*Tr"), "normalized limit")
    periods = trace_section["periods"]
    check(len(periods) == 20, "period count")
    for n, period in enumerate(periods, 1):
        check(period["n"] == n, f"period index {n}")
        ds = divisors(n)
        check([row["d"] for row in period["divisor_classes"]] == ds, f"divisor list {n}")
        grouped = {}
        for row, d in zip(period["divisor_classes"], ds):
            value = traces[n // d] ** d
            check(row["trace_value_q_sqrt3_i_sqrt3i"] == value.receipt(), f"divisor value {n},{d}")
            check(row["infinite_subsequence"] == f"k=d*(1+j*(n/d)), j>=0", f"subsequence text {n},{d}")
            for j in range(6):
                k = d * (1 + j * (n // d))
                check(gcd(n, k) == d, f"infinite gcd sentinel {n},{d},{j}")
            grouped.setdefault(value.x, []).append(d)
        expected_merged = [(E(*key).receipt(), value) for key, value in sorted(grouped.items(), key=lambda item: item[1][0])]
        check(period["distinct_cluster_value_count"] == len(expected_merged), f"cluster count {n}")
        check(
            [(row["trace_value_q_sqrt3_i_sqrt3i"], row["divisor_classes"]) for row in period["merged_cluster_values"]] == expected_merged,
            f"merged clusters {n}",
        )

    if not args.mutation_fast:
        for k in range(1, 6):
            for n in range(1, 9):
                d = gcd(n, k)
                check(direct_trace(k, n) == traces[n // d] ** d, f"direct trace k={k},n={n}")

    witness = data["unnormalized_nonconvergence_witness"]
    t2 = traces[2]
    tau2 = TAU**2
    check(witness["fixed_period"] == 2, "witness period")
    check(witness["odd_k_trace_t2_q_sqrt3_i_sqrt3i"] == t2.receipt(), "odd trace")
    check(witness["even_k_trace_tau_squared_q_sqrt3_i_sqrt3i"] == tau2.receipt(), "even trace")
    check(witness["difference_t2_minus_tau_squared_q_sqrt3_i_sqrt3i"] == (t2 - tau2).receipt(), "witness difference")
    check(t2 - tau2 == -E(2) * Q0 and bool(t2 - tau2), "difference nonzero")
    for j in range(1, 9):
        check(gcd(2, 2 * j + 1) == 1 and gcd(2, 2 * j) == 2, f"parity witness {j}")

    controls = data["controls"]
    check(controls["closed_parent"]["projector"] == "P_closed=I_3", "closed control")
    check("escape exponent is zero" in controls["closed_parent"]["result"], "closed exponent")
    check(controls["projector_order"]["gate"] == "A_right=P F3^*=F3 A F3^*", "order control")
    check(controls["hole_position"]["one_site_characteristic_polynomial"] == "lambda*(lambda+i)*(3*lambda+sqrt(3))/3", "moved-hole charpoly")
    check("rank(A0^m)=2 for every m>=1" in controls["hole_position"]["rank_result"], "moved-hole power ranks")
    check("trace cluster values can change" in controls["hole_position"]["trace_result"], "hole control")

    check(data["route_a"]["tuple"] == ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_UNITARY_OR_SCATTERING_CANDIDATE"], "tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_EXPLORATORY", "overall")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "Route B")
    boundary = data["claim_boundary"]
    check(boundary["finite_k_and_growing_k_source_gate_only"] is True, "positive boundary")
    check(all(value is False for key, value in boundary.items() if key != "finite_k_and_growing_k_source_gate_only"), "negative boundaries")
    check(any("Route-B" in item for item in data["nonclaims"]), "Route B nonclaim")

    print(json.dumps({"status": "C153_CHECKER_PASS", "assertions": assertions}, sort_keys=True))


if __name__ == "__main__":
    main()
