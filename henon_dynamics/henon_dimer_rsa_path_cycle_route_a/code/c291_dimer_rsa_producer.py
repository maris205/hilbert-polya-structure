#!/usr/bin/env python3
"""Deterministic exact-evidence producer for HCS-C291.

The producer uses the first-arriving-edge convolution.  It deliberately does
not enumerate edge orders; the independent checker does that from the greedy
bitmask rule.
"""
from __future__ import annotations

import hashlib
import json
import math
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results/c291_dimer_rsa_evidence.json"
SOURCE = "7fbe9db30cc460a82883533d7cfb2edd988c5b65"
EVALUATOR = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788307200
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"


def qtext(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def convolution(left: list[Fraction], right: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(left) + len(right) - 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            out[i + j] += a * b
    return out


def path_pgfs(limit: int) -> list[list[Fraction]]:
    values: list[list[Fraction]] = [[Fraction(1)], [Fraction(1)]]
    if limit == 0:
        return values[:1]
    for n in range(2, limit + 1):
        row = [Fraction(0)] * (n // 2 + 1)
        for a in range(n - 1):
            product = convolution(values[a], values[n - 2 - a])
            for degree, coefficient in enumerate(product):
                row[degree + 1] += coefficient / (n - 1)
        while row and row[-1] == 0:
            row.pop()
        values.append(row)
    return values


def factorial_moment(poly: list[Fraction], order: int) -> Fraction:
    total = Fraction(0)
    for k, probability in enumerate(poly):
        falling = 1
        for j in range(order):
            falling *= k - j
        total += probability * falling
    return total


def mean_second(limit: int) -> tuple[list[Fraction], list[Fraction]]:
    means = [Fraction(0)] * (limit + 1)
    seconds = [Fraction(0)] * (limit + 1)
    for n in range(2, limit + 1):
        first_sum = Fraction(0)
        second_sum = Fraction(0)
        for a in range(n - 1):
            b = n - 2 - a
            first_sum += 1 + means[a] + means[b]
            second_sum += (
                seconds[a] + seconds[b]
                + 2 * means[a] * means[b]
                + 2 * means[a] + 2 * means[b]
            )
        means[n] = first_sum / (n - 1)
        seconds[n] = second_sum / (n - 1)
    return means, seconds


def closed_mean(n: int) -> Fraction:
    if n < 2:
        return Fraction(0)
    return sum(
        Fraction((n - j) * ((-1) ** (j + 1)) * (2 ** (j - 1)), math.factorial(j))
        for j in range(1, n)
    )


def distribution(poly: list[Fraction], edge_count: int) -> list[dict]:
    scale = math.factorial(edge_count)
    result = []
    for size, probability in enumerate(poly):
        if probability:
            count = probability * scale
            assert count.denominator == 1
            result.append({
                "matching_size": size,
                "order_count": count.numerator,
                "probability": qtext(probability),
            })
    return result


def path_row(n: int, poly: list[Fraction]) -> dict:
    mean = factorial_moment(poly, 1)
    second = factorial_moment(poly, 2)
    variance = second + mean - mean * mean
    support = [item["matching_size"] for item in distribution(poly, max(0, n - 1))]
    return {
        "n": n,
        "edge_count": max(0, n - 1),
        "order_count": math.factorial(max(0, n - 1)),
        "distribution": distribution(poly, max(0, n - 1)),
        "support_min": min(support),
        "support_max": max(support),
        "mean": qtext(mean),
        "factorial_second": qtext(second),
        "variance": qtext(variance),
        "closed_mean": qtext(closed_mean(n)),
    }


def cycle_row(n: int, path_poly: list[Fraction]) -> dict:
    poly = [Fraction(0)] + path_poly
    mean = factorial_moment(poly, 1)
    second = factorial_moment(poly, 2)
    variance = second + mean - mean * mean
    support = [item["matching_size"] for item in distribution(poly, n)]
    return {
        "n": n,
        "edge_count": n,
        "order_count": math.factorial(n),
        "distribution": distribution(poly, n),
        "support_min": min(support),
        "support_max": max(support),
        "mean": qtext(mean),
        "factorial_second": qtext(second),
        "variance": qtext(variance),
        "path_identity_index": n - 2,
    }


def decimal_text(value: Decimal) -> str:
    return format(value, ".36E")


def payload_hash(data: dict) -> str:
    clean = dict(data)
    clean.pop("payload_sha256", None)
    raw = json.dumps(clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(raw.encode()).hexdigest()


def build() -> dict:
    polys = path_pgfs(20)
    means, seconds = mean_second(200)
    for n in range(21):
        assert factorial_moment(polys[n], 1) == means[n]
        assert factorial_moment(polys[n], 2) == seconds[n]
        assert means[n] == closed_mean(n)

    getcontext().prec = 90
    e_minus_2 = Decimal(-2).exp()
    e_minus_4 = Decimal(-4).exp()
    asymptotic_rows = []
    for n in (20, 50, 100, 200):
        mean = means[n]
        variance = seconds[n] + mean - mean * mean
        mean_decimal = Decimal(mean.numerator) / Decimal(mean.denominator)
        variance_decimal = Decimal(variance.numerator) / Decimal(variance.denominator)
        asymptotic_rows.append({
            "n": n,
            "mean": qtext(mean),
            "variance": qtext(variance),
            "mean_density": decimal_text(mean_decimal / Decimal(n)),
            "variance_density": decimal_text(variance_decimal / Decimal(n)),
            "variance_centered": decimal_text(
                variance_decimal - e_minus_4 * Decimal(n + 2)
            ),
        })

    data = {
        "schema": "hcs-c291-dimer-rsa-path-cycle-v1",
        "candidate_id": "HCS-C291",
        "evaluation_date": "2026-09-02",
        "source_commit": SOURCE,
        "fixed_epoch": EPOCH,
        "scope_literal": SCOPE,
        "evaluator": {"version": "0.2.0", "sha256": EVALUATOR},
        "headline": (
            "Finite path and cycle dimer random sequential adsorption has an exact "
            "PGF convolution/Riccati hierarchy, complete factorial-moment triangle, "
            "sharp support, and linear variance with coefficient exp(-4)."
        ),
        "model_contract": {
            "path": "P_n has vertices 1,...,n and edges {i,i+1}; n>=0",
            "cycle": "C_n is the simple labeled cycle; n>=3",
            "sampling": "a uniformly random permutation of all labeled edges, equivalently iid continuous priorities",
            "acceptance_rule": "scan once and accept an edge exactly when both endpoints are currently unmatched",
            "output_semantics": "the terminal set is a jammed maximal matching, not generally a maximum matching",
            "clock": "one finite edge-order scan; there is no physical-time periodic flow",
        },
        "theorem_contract": {
            "path_pgf": "F_0=F_1=1 and (n-1)F_n(z)=z*sum_{a+b=n-2}F_a(z)F_b(z) for n>=2",
            "riccati_ogf": "F_x=(F-1)/x+z*x*F^2, F(0,z)=1, [x]F=1",
            "factorial_moments": "H_r=partial_z^r F|_{z=1} obeys the displayed all-r triangular linear ODE with H_0=(1-x)^(-1)",
            "exact_mean": "E[M_n]=sum_{j=1}^{n-1}(n-j)(-1)^(j+1)2^(j-1)/j!",
            "variance": "Var(M_n)=exp(-4)*n+2*exp(-4)+o(1), hence exp(-4)*n+O(1)",
            "path_support": "{0} for n=0,1; every integer ceil((n-1)/3),...,floor(n/2) for n>=2",
            "cycle_identity": "G_n(z)=z*F_{n-2}(z) for every simple cycle n>=3",
            "cycle_support": "every integer ceil(n/3),...,floor(n/2) for n>=3",
            "cycle_mean_boundary": "E[C_n]=1+E[M_{n-2}]=((1-exp(-2))/2)n+o(1), and E[C_n]-E[M_n] tends to exp(-2)",
            "occupancy": "2E[M_n]/n and 2E[C_n]/n tend to 1-exp(-2)",
        },
        "proof_contract": {
            "status": "PROVABLE AS STATED",
            "dependencies": [
                "condition on the unique first edge in the continuous-priority order",
                "independence and uniform relative orders on the two residual path components",
                "differentiate the Riccati OGF at z=1 for the all-order factorial hierarchy",
                "solve the first two linear ODEs and extract the pole parts at x=1",
                "use maximal-matching domination bounds plus explicit path and cycle constructions",
            ],
            "finite_evidence_boundary": "edge-order enumeration is a regression oracle only and is not an all-n proof",
            "ownership_boundary": "the RSA model and one-dimensional jamming law are classical; this package is a reproducible reconstruction, not a literature-priority claim",
        },
        "enumeration_contract": {
            "path_min_n": 0,
            "path_max_n": 10,
            "cycle_min_n": 3,
            "cycle_max_n": 9,
            "factorial_max_n": 20,
            "factorial_max_order": 5,
            "asymptotic_n": [20, 50, 100, 200],
        },
        "path_rows": [path_row(n, polys[n]) for n in range(11)],
        "cycle_rows": [cycle_row(n, polys[n - 2]) for n in range(3, 10)],
        "factorial_moment_rows": [
            {
                "n": n,
                "moments": [qtext(factorial_moment(polys[n], r)) for r in range(6)],
            }
            for n in range(21)
        ],
        "asymptotic_rows": asymptotic_rows,
        "boundary_rows": [
            {"face": "empty_path", "condition": "n=0", "status": "no vertices, no edges, M_0=0 and F_0=1"},
            {"face": "singleton_path", "condition": "n=1", "status": "one vertex, no edges, M_1=0 and F_1=1"},
            {"face": "first_nontrivial_path", "condition": "n=2", "status": "one edge is accepted with certainty, so F_2=z"},
            {"face": "cycle_domain", "condition": "n>=3", "status": "only simple cycles are covered; loops and parallel edges are excluded"},
            {"face": "priority_ties", "condition": "iid continuous priorities", "status": "ties have probability zero; discrete priorities require an extra tie-breaking rule"},
            {"face": "jamming_semantics", "condition": "all edges scanned", "status": "the result is maximal under edge addition but need not have maximum cardinality"},
            {"face": "path_lower_support", "condition": "n>=2", "status": "maximality forces at least ceil((n-1)/3) dimers and constructions attain every size through floor(n/2)"},
            {"face": "cycle_lower_support", "condition": "n>=3", "status": "maximality forces at least ceil(n/3) dimers and first-edge reduction transfers all attainable sizes"},
            {"face": "finite_oracle", "condition": "enumerated n only", "status": "finite order tables test implementations and do not prove any all-n identity"},
        ],
        "references": [
            {
                "authors": "Paul J. Flory",
                "title": "Intramolecular Reaction between Neighboring Substituents of Vinyl Polymers",
                "venue": "Journal of the American Chemical Society 61(6), 1518-1521 (1939)",
                "identifier": "10.1021/ja01875a053",
                "role": "classical one-dimensional blocking/jamming lineage",
            },
            {
                "authors": "J. W. Evans",
                "title": "Random and cooperative sequential adsorption",
                "venue": "Reviews of Modern Physics 65(4), 1281-1329 (1993)",
                "identifier": "10.1103/RevModPhys.65.1281",
                "role": "authoritative RSA review and terminology",
            },
            {
                "authors": "Mathew D. Penrose",
                "title": "Random Parking, Sequential Adsorption, and the Jamming Limit",
                "venue": "Communications in Mathematical Physics 218(1), 153-176 (2001)",
                "identifier": "10.1007/s002200100387",
                "role": "rigorous stochastic-geometric RSA context",
            },
            {
                "authors": "Martin Dyer and Alan Frieze",
                "title": "Randomized greedy matching",
                "venue": "Random Structures & Algorithms 2(1), 29-45 (1991)",
                "identifier": "10.1002/rsa.3240020104",
                "role": "random greedy matching terminology and algorithmic lineage",
            },
        ],
        "collision_snapshot": {
            "token": "C291_READ_ONLY_COLLISION_SNAPSHOT_AT_7fbe9db3",
            "registry_bytes_required": False,
            "closest": [
                {"candidate": "HCS-C208", "distinction": "continuous-time linear birth-death branching PGFs, not greedy adsorption on finite graphs"},
                {"candidate": "HCS-C243", "distinction": "Bose-Josephson Hamiltonian dimer, not an adsorbing graph matching"},
                {"candidate": "HCS-C285", "distinction": "closed queueing-network product form and condensation, not a random edge-order jamming law"},
            ],
            "direct_owner_risk": "high: the model and limiting density are classical, so only exact reconstruction and audit closure are claimed",
            "obstruction_id": "HEN-O275",
        },
        "nonclaims": [
            "A jammed matching is called maximal, never maximum unless its cardinality happens to attain floor(n/2).",
            "Finite edge-order enumeration is not used as proof of the all-n recurrence, support, or asymptotics.",
            "No literature originality or priority is claimed for dimer RSA, random greedy matching, or the Flory jamming constant.",
            "No rational-prime carrier, prime-power repetition law, logarithmic prime clock, target divisor, or target functional equation is obtained.",
            "No source-native self-adjoint Hilbert-Polya operator or Route-B authorization is claimed.",
        ],
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "scope_flags": {
            "arithmetic_local_data": False,
            "euler_factors": False,
            "root_numbers": False,
            "automorphy": False,
            "target_divisor_or_counting_law": False,
            "target_functional_equation": False,
            "target_zero_match": False,
            "hilbert_polya_operator": False,
            "route_b_authorization": False,
        },
    }
    data["payload_sha256"] = payload_hash(data)
    return data


def main() -> None:
    data = build()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(
        "C291_PRODUCER_PASS "
        f"path_rows={len(data['path_rows'])} cycle_rows={len(data['cycle_rows'])} "
        f"factorial_rows={len(data['factorial_moment_rows'])} "
        f"payload_sha256={data['payload_sha256']}"
    )


if __name__ == "__main__":
    main()
