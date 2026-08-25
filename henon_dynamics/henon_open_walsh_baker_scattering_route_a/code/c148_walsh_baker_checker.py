#!/usr/bin/env python3
"""Independent exact checker for C148; imports no producer module."""
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

    def __truediv__(self, value):
        value = Fraction(value)
        return E(*(u / value for u in self.x))

    def __pow__(self, n):
        ans, base = E(1), self
        while n:
            if n & 1:
                ans = ans * base
            base = base * base
            n //= 2
        return ans

    def __eq__(self, other):
        other = other if isinstance(other, E) else E(other)
        return self.x == other.x

    def __bool__(self):
        return any(self.x)

    def conj(self):
        a, b, c, d = self.x
        return E(a, b, -c, -d)

    @classmethod
    def read(cls, values):
        return cls(*(Fraction(value) for value in values))

    def receipt(self):
        return [str(v.numerator) if v.denominator == 1 else f"{v.numerator}/{v.denominator}" for v in self.x]


Z, O = E(), E(1)
R = E(0, Fraction(1, 3))
OMEGA = E(Fraction(-1, 2), 0, 0, Fraction(1, 2))
OMEGA2 = OMEGA * OMEGA


def canonical_hash(data):
    work = dict(data)
    work.pop("payload_sha256", None)
    raw = json.dumps(work, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return sha256(raw).hexdigest()


def eye(n):
    return [[O if i == j else Z for j in range(n)] for i in range(n)]


def mm(a, b):
    out = [[Z for _ in range(len(b[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for h in range(len(b)):
            if not a[i][h]:
                continue
            for j in range(len(b[0])):
                if b[h][j]:
                    out[i][j] = out[i][j] + a[i][h] * b[h][j]
    return out


def adjoint(a):
    return [[a[j][i].conj() for j in range(len(a))] for i in range(len(a[0]))]


def mtrace(a):
    return sum((a[i][i] for i in range(len(a))), Z)


def mpow(a, n):
    ans, base = eye(len(a)), a
    while n:
        if n & 1:
            ans = mm(ans, base)
        base = mm(base, base)
        n //= 2
    return ans


def fourier_star():
    # F3^*[j,l]=omega^(-j*l)/sqrt(3).
    return [[R * (OMEGA2 ** ((j * ell) % 3)) for ell in range(3)] for j in range(3)]


def diagonal(values):
    return [[E(values[i]) if i == j else Z for j in range(len(values))] for i in range(len(values))]


@lru_cache(maxsize=None)
def action_a(source):
    a = mm(fourier_star(), diagonal((1, 0, 1)))
    return [(target, a[target][source]) for target in range(3) if a[target][source]]


@lru_cache(maxsize=None)
def all_states(k):
    return tuple(product(range(3), repeat=k))


@lru_cache(maxsize=None)
def edges(state):
    return tuple((state[1:] + (target,), weight) for target, weight in action_a(state[0]))


def propagate(start, steps):
    current = {start: O}
    for _ in range(steps):
        nxt = {}
        for state, amplitude in current.items():
            for target, weight in edges(state):
                nxt[target] = nxt.get(target, Z) + amplitude * weight
        current = nxt
    return current


def tensor_a_action(source):
    current = {(): O}
    for symbol in source:
        nxt = {}
        for prefix, amplitude in current.items():
            for target, weight in action_a(symbol):
                nxt[prefix + (target,)] = amplitude * weight
        current = nxt
    return current


def direct_traces(k, cutoff):
    totals = [Z for _ in range(cutoff)]
    for start in all_states(k):
        current = {start: O}
        for n in range(cutoff):
            nxt = {}
            for state, amplitude in current.items():
                for target, weight in edges(state):
                    nxt[target] = nxt.get(target, Z) + amplitude * weight
            current = nxt
            totals[n] = totals[n] + current.get(start, Z)
    return totals


def trace_a(n):
    return mtrace(mpow(mm(fourier_star(), diagonal((1, 0, 1))), n))


def coeff_from_traces(k):
    degree = 2**k
    values = []
    for n in range(1, degree + 1):
        d = gcd(n, k)
        values.append(trace_a(n // d) ** d)
    coeff = [O]
    for n in range(1, degree + 1):
        coeff.append(-sum((coeff[n - j] * values[j - 1] for j in range(1, n + 1)), Z) / n)
    return coeff


def rotations(word):
    return [word[j:] + word[:j] for j in range(len(word))]


def primitive(word):
    n = len(word)
    return all(n % d or word != word[:d] * (n // d) for d in range(1, n))


def path_rows(cutoff):
    basis = all_states(2)
    index = {state: j for j, state in enumerate(basis)}
    adjacency = {index[s]: [(index[t], w) for t, w in edges(s)] for s in basis}
    answer = []
    for n in range(1, cutoff + 1):
        rooted, total, cycles = 0, Z, {}

        def visit(start, current, vertices, amplitude, left):
            nonlocal rooted, total
            if left == 0:
                if current == start:
                    rooted += 1
                    total = total + amplitude
                    cycle = tuple(vertices)
                    if primitive(cycle):
                        cycles[min(rotations(cycle))] = amplitude
                return
            for target, weight in adjacency[current]:
                visit(start, target, vertices if left == 1 else vertices + [target], amplitude * weight, left - 1)

        for start in range(9):
            visit(start, start, [start], O, n)
        answer.append(
            {
                "n": n,
                "rooted_nonzero_closed_walks": rooted,
                "closed_walk_amplitude_sum_q_sqrt3_i_sqrt3i": total.receipt(),
                "primitive_cycle_count": len(cycles),
                "primitive_amplitude_sum_q_sqrt3_i_sqrt3i": sum(cycles.values(), Z).receipt(),
            }
        )
    return answer


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "evidence",
        nargs="?",
        type=Path,
        default=Path(__file__).resolve().parents[1] / "results/c148_walsh_baker_evidence.json",
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

    check(data["schema"] == "hcs-c148-open-walsh-baker-evidence-v1", "schema")
    check(data["candidate_id"] == "HCS-C148", "candidate")
    check(data["evaluation_date"] == "2026-08-25", "date")
    check(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER", "scope")
    check(data["payload_sha256"] == canonical_hash(data), "payload hash")
    lock = data["source_lock"]
    expected_lock = {
        "object": "three-symbol Walsh open baker family B_k on H_k=(C^3)^(tensor k)",
        "basis_order": "lexicographic qutrit words 0,1,2 of length k",
        "omega": "exp(2*pi*i/3)=(-1+i*sqrt(3))/2",
        "fourier": "F3[j,l]=omega^(j*l)/sqrt(3), j,l in {0,1,2}",
        "projector": "P=diag(1,0,1)",
        "one_qutrit_gate": "A=F3^* P",
        "shift_gate": "B_k(v0 tensor ... tensor v_(k-1))=v1 tensor ... tensor v_(k-1) tensor A*v0",
        "clock": "one application of B_k",
        "normalization": "unitary normalized three-point DFT and no spectral rescaling",
        "determinant_convention": "D_k(z)=det(I_(3^k)-z*B_k)",
        "finite_polynomial_range": [1, 2, 3, 4, 5],
        "direct_trace_sentinel": 12,
        "primitive_path_sentinel": {"k": 2, "period": 8},
        "precision": "exact Q(sqrt(3),i) arithmetic represented in the ordered basis 1,sqrt(3),i,sqrt(3)*i",
        "allowed_data": "the frozen DFT, projector, tensor shift, and exact complex path amplitudes",
        "forbidden_data": "target zeros or divisors, prime or arithmetic local data, Euler factors, root numbers, automorphy, Hilbert--Polya, Route B",
    }
    for key, value in expected_lock.items():
        check(lock[key] == value, f"source lock {key}")

    fs = fourier_star()
    f = adjoint(fs)
    check(mm(f, fs) == eye(3), "Fourier normalization")
    check(OMEGA**3 == O and OMEGA != O, "cube root")
    p = diagonal((1, 0, 1))
    a = mm(fs, p)
    astar_a, a_astar = mm(adjoint(a), a), mm(a, adjoint(a))
    check(astar_a == p, "A*A=P")
    check(mm(a_astar, a_astar) == a_astar, "AA* projection")
    check(mtrace(astar_a) == E(2), "rank A")
    receipt = data["one_qutrit_receipt"]
    check(receipt["matrix_columns"] == "A=(1/sqrt(3))*[[1,0,1],[1,0,omega],[1,0,omega^2]]", "A receipt")
    check(receipt["trace_A_q_sqrt3_i_sqrt3i"] == mtrace(a).receipt(), "trace A")
    nonzero_product = E(Fraction(-1, 2), 0, 0, Fraction(-1, 6))
    check(receipt["nonzero_eigenvalue_product_q_sqrt3_i_sqrt3i"] == nonzero_product.receipt(), "product")
    check(receipt["characteristic_polynomial"] == "lambda*(lambda^2-(sqrt(3)/6-i/2)*lambda-1/2-sqrt(3)*i/6)", "A characteristic polynomial")
    check(receipt["A_star_A"] == "P" and receipt["A_A_star"] == "F3^* P F3", "Gram text")
    check(receipt["rank_A"] == 2 and receipt["operator_norm_A"] == "1", "rank/norm")

    correction = data["rank_correction_and_escape_ledger"]
    check(correction["rejected_statement"] == "rank(B_k)=2^k", "rejected rank")
    check(correction["correct_statement"] == "rank(B_k)=rank(A)*3^(k-1)=2*3^(k-1)", "correct rank")
    check(correction["k_step_statement"] == "B_k^k=A^(tensor k) and rank(B_k^k)=2^k", "k-step rank")
    for k, row in enumerate(correction["rows"], 1):
        check(row["k"] == k, f"rank row k={k}")
        check(row["dimension"] == 3**k, f"dimension k={k}")
        check(row["rank_Bk"] == 2 * 3 ** (k - 1), f"rank B k={k}")
        check(row["kernel_dimension_Bk"] == 3 ** (k - 1), f"kernel B k={k}")
        check(row["rank_Bk_power_k"] == 2**k, f"rank power k={k}")
        check(row["kernel_dimension_Bk_power_k"] == 3**k - 2**k, f"kernel power k={k}")
        check(row["left_defect_rank"] == row["right_defect_rank"] == 3 ** (k - 1), f"defects k={k}")
        if not args.mutation_fast:
            for source in all_states(k):
                check(propagate(source, k) == tensor_a_action(source), f"B^k tensor identity k={k} source={source}")

    theorem = data["all_period_theorem"]
    check(theorem["trace_formula"] == "for d=gcd(n,k), Tr(B_k^n)=Tr(A^(n/d))^d for every n>=1", "trace theorem")
    check(theorem["k_step_identity"] == "B_k^k=A^(tensor k)", "power theorem")
    check(theorem["primitive_product"] == "D_k(z)=product_[gamma primitive](1-z^|gamma|*amplitude(gamma))", "product theorem")
    check(theorem["formal_status"].endswith("|z|<1/sqrt(3)"), "product domain")
    for k in range(1, 6):
        rows = data["trace_ledgers"][str(k)]
        check(len(rows) == 12, f"trace row count k={k}")
        direct_values = direct_traces(k, 12) if not args.mutation_fast else None
        for n, row in enumerate(rows, 1):
            d = gcd(n, k)
            formula = trace_a(n // d) ** d
            direct = direct_values[n - 1] if direct_values is not None else formula
            check(row["n"] == n, f"trace index k={k},n={n}")
            check(row["rooted_nonzero_closed_walks"] == 2**n, f"closed-walk count k={k},n={n}")
            check(row["trace_Bk_power_q_sqrt3_i_sqrt3i"] == direct.receipt(), f"direct trace k={k},n={n}")
            check(direct == formula, f"gcd trace k={k},n={n}")

        ledger = data["characteristic_polynomials_k1_to_k5"][str(k)]
        coeff = coeff_from_traces(k)
        check(ledger["matrix_dimension"] == 3**k, f"poly dimension k={k}")
        check(ledger["secular_degree"] == 2**k, f"poly degree k={k}")
        check(ledger["zero_eigenvalue_algebraic_multiplicity"] == 3**k - 2**k, f"zero mult k={k}")
        check(ledger["secular_coefficients_ascending"] == [x.receipt() for x in coeff], f"coefficients k={k}")
        check(ledger["nonzero_coefficient_degrees"] == [j for j, x in enumerate(coeff) if x], f"support k={k}")
        check(bool(coeff[-1]), f"leading nonzero k={k}")

    primitive_ledger = data["primitive_path_ledger"]
    check(primitive_ledger["k"] == 2 and primitive_ledger["period_limit"] == 8, "path lock")
    check(primitive_ledger["rows"] == path_rows(8), "independent path ledger")
    check(primitive_ledger["finite_prefix_is_not_theorem_cutoff"] is True, "path boundary")

    defect = data["subunitarity_defect"]
    check(defect["right_gram"] == "B_k^* B_k=P tensor I_(3^(k-1))", "right Gram")
    check(defect["left_gram"] == "B_k B_k^*=I_(3^(k-1)) tensor F3^* P F3", "left Gram")
    check(defect["projection_status"] == "both defects are orthogonal projections", "projection status")
    check(defect["rank_each"] == "3^(k-1)", "defect rank")

    controls = data["controls"]
    closed = controls["closed_control"]
    check(mm(f, fs) == eye(3), "closed unitary")
    check(closed["trace_A_closed_q_sqrt3_i_sqrt3i"] == mtrace(fs).receipt() == E(0, 0, -1, 0).receipt(), "closed trace")
    check(closed["result"] == "B_k,closed is unitary, has rank 3^k, and both defects vanish", "closed result")
    right = mm(p, fs)
    check(right == mm(mm(f, a), fs), "projector order similarity")
    order = controls["projector_order_control"]
    check(order["similarity"] == "A_right=F3 A F3^*", "order similarity text")
    for n in range(1, 13):
        check(mtrace(mpow(right, n)) == mtrace(mpow(a, n)), f"order spectra n={n}")
    p0 = diagonal((0, 1, 1))
    a0 = mm(fs, p0)
    hole = controls["hole_position_control"]
    check(hole["trace_A0_q_sqrt3_i_sqrt3i"] == mtrace(a0).receipt(), "hole trace")
    check(hole["frozen_linear_coefficient_q_sqrt3_i_sqrt3i"] == (-mtrace(a)).receipt(), "frozen c1")
    check(hole["alternative_linear_coefficient_q_sqrt3_i_sqrt3i"] == (-mtrace(a0)).receipt(), "hole c1")
    check(mtrace(a0) != mtrace(a), "hole spectral difference")
    check(controls["antiunitary_symmetry"] == "NOT_ASSERTED", "antiunitary boundary")

    check(data["route_a"]["tuple"] == ["A1_WEAK", "A2_FAIL", "A3_FAIL", "A4_UNITARY_OR_SCATTERING_CANDIDATE"], "tuple")
    check(data["route_a"]["overall"] == "ROUTE_A_EXPLORATORY", "overall")
    check(data["route_a"]["route_b_invocation_allowed"] is False, "Route B")
    boundary = data["claim_boundary"]
    check(boundary["finite_k_scattering_gate_only"] is True, "finite gate")
    check(all(value is False for key, value in boundary.items() if key != "finite_k_scattering_gate_only"), "claim flags")
    check("rank(B_k)=2^k at one step" in data["nonclaims"], "rank nonclaim")
    check(any("Route-B" in item for item in data["nonclaims"]), "Route B nonclaim")
    print(json.dumps({"status": "PASS", "assertions": assertions}, sort_keys=True))


if __name__ == "__main__":
    main()
