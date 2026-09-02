#!/usr/bin/env python3
"""Produce the deterministic HCS-C285 Gordon--Newell certificate."""
from __future__ import annotations

import hashlib
import json
import math
import os
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(os.environ.get("C285_EVIDENCE_OUT", ROOT / "results/c285_gordon_newell_evidence.json"))
SOURCE = "3878fa5282ca89f75700b3ef9d623f54dcb7bcf9"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
EPOCH = 1788307200


def qstr(x: Q) -> str:
    return f"{x.numerator}/{x.denominator}"


def qlist(values) -> list[str]:
    return [qstr(Q(value)) for value in values]


def qmatrix(rows) -> list[list[str]]:
    return [qlist(row) for row in rows]


def payload_hash(data: dict) -> str:
    clean = dict(data)
    clean.pop("payload_sha256", None)
    raw = json.dumps(clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def compositions(total: int, parts: int):
    if parts == 1:
        yield (total,)
        return
    for first in range(total + 1):
        for tail in compositions(total - first, parts - 1):
            yield (first,) + tail


def multiindices(parts: int, maximum_degree: int):
    for degree in range(1, maximum_degree + 1):
        yield from compositions(degree, parts)


def solve_square(matrix: list[list[Q]], rhs: list[Q]) -> list[Q]:
    """Exact Gauss--Jordan solve used only by the producer."""
    n = len(matrix)
    aug = [list(row) + [rhs[i]] for i, row in enumerate(matrix)]
    for col in range(n):
        pivot = next(row for row in range(col, n) if aug[row][col])
        aug[col], aug[pivot] = aug[pivot], aug[col]
        scale = aug[col][col]
        aug[col] = [value / scale for value in aug[col]]
        for row in range(n):
            if row == col or not aug[row][col]:
                continue
            factor = aug[row][col]
            aug[row] = [a - factor * b for a, b in zip(aug[row], aug[col])]
    return [aug[i][-1] for i in range(n)]


def traffic(routing: tuple[tuple[Q, ...], ...]) -> tuple[Q, ...]:
    m = len(routing)
    equations = []
    rhs = []
    for target in range(m - 1):
        equations.append([
            routing[source][target] - Q(int(source == target)) for source in range(m)
        ])
        rhs.append(Q(0))
    equations.append([Q(1)] * m)
    rhs.append(Q(1))
    answer = tuple(solve_square(equations, rhs))
    assert all(value > 0 for value in answer) and sum(answer) == 1
    assert all(sum(answer[i] * routing[i][j] for i in range(m)) == answer[j] for j in range(m))
    return answer


def h_direct(weights: tuple[Q, ...], n: int) -> Q:
    return sum((math.prod(weights[i] ** state[i] for i in range(len(weights)))
                for state in compositions(n, len(weights))), Q(0))


def h_convolution(weights: tuple[Q, ...], n: int) -> Q:
    coefficients = [Q(0)] * (n + 1)
    coefficients[0] = Q(1)
    for weight in weights:
        updated = [Q(0)] * (n + 1)
        for degree in range(n + 1):
            updated[degree] = sum(coefficients[degree - k] * weight ** k for k in range(degree + 1))
        coefficients = updated
    return coefficients[n]


def h_newton(weights: tuple[Q, ...], n: int) -> Q:
    h = [Q(1)] + [Q(0)] * n
    powers = [Q(0)] + [sum((weight ** k for weight in weights), Q(0)) for k in range(1, n + 1)]
    for degree in range(1, n + 1):
        h[degree] = sum(powers[k] * h[degree - k] for k in range(1, degree + 1)) / degree
    return h[n]


def factorial_derivative(weights: tuple[Q, ...], n: int, alpha: tuple[int, ...]) -> Q:
    degree = sum(alpha)
    if degree > n:
        return Q(0)
    target = n - degree
    coefficients = [Q(1)] + [Q(0)] * target
    for weight, order in zip(weights, alpha):
        factor = [Q(math.comb(k + order, order)) * weight ** k for k in range(target + 1)]
        coefficients = [
            sum(coefficients[d - k] * factor[k] for k in range(d + 1))
            for d in range(target + 1)
        ]
    prefactor = math.prod(math.factorial(order) * weights[i] ** order for i, order in enumerate(alpha))
    return Q(prefactor) * coefficients[target]


def generator(states: list[tuple[int, ...]], routing, service) -> list[list[Q]]:
    index = {state: k for k, state in enumerate(states)}
    size = len(states)
    matrix = [[Q(0) for _ in range(size)] for _ in range(size)]
    for row, state in enumerate(states):
        for i, count in enumerate(state):
            if not count:
                continue
            for j, probability in enumerate(routing[i]):
                if i == j or not probability:
                    continue
                moved = list(state)
                moved[i] -= 1
                moved[j] += 1
                rate = service[i] * probability
                matrix[row][index[tuple(moved)]] += rate
                matrix[row][row] -= rate
    return matrix


CYCLE3 = (
    (Q(0), Q(1), Q(0)),
    (Q(0), Q(0), Q(1)),
    (Q(1), Q(0), Q(0)),
)
CYCLE4 = (
    (Q(0), Q(1), Q(0), Q(0)),
    (Q(0), Q(0), Q(1), Q(0)),
    (Q(0), Q(0), Q(0), Q(1)),
    (Q(1), Q(0), Q(0), Q(0)),
)
SELF_NONREV = (
    (Q(1, 2), Q(1, 2), Q(0)),
    (Q(0), Q(1, 3), Q(2, 3)),
    (Q(3, 4), Q(0), Q(1, 4)),
)
DENSE_NONREV = (
    (Q(1, 5), Q(1, 2), Q(3, 10)),
    (Q(1, 3), Q(1, 6), Q(1, 2)),
    (Q(2, 5), Q(1, 5), Q(2, 5)),
)
REV_LINE = (
    (Q(1, 2), Q(1, 2), Q(0)),
    (Q(1, 4), Q(1, 2), Q(1, 4)),
    (Q(0), Q(1, 2), Q(1, 2)),
)

CASES = {
    "zero_customers_nonreversible": (0, SELF_NONREV, (Q(2), Q(3), Q(5))),
    "one_customer_nonreversible": (1, SELF_NONREV, (Q(2), Q(3), Q(5))),
    "dense_nonreversible": (3, DENSE_NONREV, (Q(3, 2), Q(5, 3), Q(7, 4))),
    "reversible_line": (4, REV_LINE, (Q(1), Q(2), Q(3))),
    "unique_bottleneck_cycle": (5, CYCLE4, (Q(1, 4), Q(1, 2), Q(3, 4), Q(1))),
    "two_tied_bottlenecks": (5, CYCLE4, (Q(1, 4), Q(1, 4), Q(1, 2), Q(3, 4))),
    "all_equal_weights": (4, CYCLE3, (Q(1, 3), Q(1, 3), Q(1, 3))),
    "zero_edges_periodic_routing": (3, CYCLE4, (Q(2, 5), Q(1, 2), Q(3, 5), Q(4, 5))),
    "single_station": (3, ((Q(1),),), (Q(7, 3),)),
}


def exact_rows():
    case_rows = []
    state_rows = []
    z_rows = []
    moment_rows = []
    flow_rows = []
    reversal_rows = []
    for name, (population, routing, service) in CASES.items():
        m = len(routing)
        e = traffic(routing)
        weights = tuple(e[i] / service[i] for i in range(m))
        states = list(compositions(population, m))
        direct = h_direct(weights, population)
        convolution = h_convolution(weights, population)
        newton = h_newton(weights, population)
        assert direct == convolution == newton > 0
        z_previous = h_convolution(weights, population - 1) if population else Q(0)
        reversible = all(e[i] * routing[i][j] == e[j] * routing[j][i]
                         for i in range(m) for j in range(m))
        reversed_routing = tuple(tuple(e[j] * routing[j][i] / e[i] for j in range(m)) for i in range(m))
        case_rows.append({
            "case": name,
            "population": population,
            "stations": m,
            "routing": qmatrix(routing),
            "service_rates": qlist(service),
            "traffic": qlist(e),
            "weights": qlist(weights),
            "state_count": len(states),
            "irreducible_routing": True,
            "routing_reversible": reversible,
            "bottleneck_indices": [i for i, weight in enumerate(weights) if weight == max(weights)],
        })
        z_rows.append({
            "case": name,
            "Z_N_direct": qstr(direct),
            "Z_N_convolution": qstr(convolution),
            "Z_N_newton": qstr(newton),
            "Z_N_minus_1": qstr(z_previous),
            "three_way_equal": direct == convolution == newton,
        })

        qgen = generator(states, routing, service)
        raw_weights = [math.prod(weights[i] ** state[i] for i in range(m)) for state in states]
        for column, (state, raw_weight) in enumerate(zip(states, raw_weights)):
            balance = sum(raw_weights[row] * qgen[row][column] for row in range(len(states)))
            state_rows.append({
                "case": name,
                "state": list(state),
                "unnormalized_weight": qstr(Q(raw_weight)),
                "probability": qstr(Q(raw_weight) / direct),
                "left_balance": qstr(balance),
            })

        means = []
        raw_second = [[Q(0) for _ in range(m)] for _ in range(m)]
        for i in range(m):
            means.append(sum(Q(state[i]) * raw_weights[k] for k, state in enumerate(states)) / direct)
            for j in range(m):
                raw_second[i][j] = sum(Q(state[i] * state[j]) * raw_weights[k]
                                       for k, state in enumerate(states)) / direct
        covariance = [[raw_second[i][j] - means[i] * means[j] for j in range(m)] for i in range(m)]
        probes = []
        for alpha in multiindices(m, min(3, population)):
            value = factorial_derivative(weights, population, alpha) / direct
            probes.append({"alpha": list(alpha), "value": qstr(value)})
        moment_rows.append({
            "case": name,
            "means": qlist(means),
            "covariance": qmatrix(covariance),
            "factorial_moments_through_degree_three": probes,
        })

        ratio = z_previous / direct if population else Q(0)
        utilization = [weights[i] * ratio for i in range(m)]
        throughputs = [e[i] * ratio for i in range(m)]
        edge_flows = [[e[i] * routing[i][j] * ratio for j in range(m)] for i in range(m)]
        currents = [[edge_flows[i][j] - edge_flows[j][i] for j in range(m)] for i in range(m)]
        conservation = [sum(edge_flows[i]) - sum(edge_flows[j][i] for j in range(m)) for i in range(m)]
        flow_rows.append({
            "case": name,
            "positive_population": population > 0,
            "Z_ratio": qstr(ratio),
            "utilizations": qlist(utilization),
            "station_throughputs": qlist(throughputs),
            "directed_edge_event_flows": qmatrix(edge_flows),
            "antisymmetric_net_currents": qmatrix(currents),
            "flow_conservation_residuals": qlist(conservation),
        })
        reversed_traffic = traffic(reversed_routing)
        twice = tuple(tuple(reversed_traffic[j] * reversed_routing[j][i] / reversed_traffic[i]
                            for j in range(m)) for i in range(m))
        reversal_rows.append({
            "case": name,
            "reversed_routing": qmatrix(reversed_routing),
            "reversed_traffic": qlist(reversed_traffic),
            "reversal_is_involution": twice == routing,
            "state_process_reversible_for_positive_population": (reversible if population else "trivial_singleton"),
            "detailed_balance_defects": qmatrix([
                [e[i] * routing[i][j] - e[j] * routing[j][i] for j in range(m)] for i in range(m)
            ]),
        })
    return case_rows, state_rows, z_rows, moment_rows, flow_rows, reversal_rows


CONDENSATION_FAMILIES = {
    "unique_scaled": (Q(5, 3), Q(5, 6), Q(5, 9), Q(5, 12)),
    "two_tied_scaled": (Q(7, 5), Q(7, 5), Q(7, 10), Q(7, 15)),
    "three_tied": (Q(2), Q(2), Q(2), Q(1)),
    "all_equal": (Q(3, 7), Q(3, 7), Q(3, 7)),
}


def condensation_rows() -> list[dict]:
    rows = []
    for family, weights in CONDENSATION_FAMILIES.items():
        wstar = max(weights)
        bottlenecks = [i for i, value in enumerate(weights) if value == wstar]
        nonbottlenecks = [i for i in range(len(weights)) if i not in bottlenecks]
        r = len(bottlenecks)
        q = tuple(weights[i] / wstar for i in nonbottlenecks)
        a_at_one = math.prod(Q(1, 1) / (1 - value) for value in q) if q else Q(1)
        for population in (0, 1, 2, 4, 8, 16, 32):
            masses = []
            if q:
                for total in range(population + 1):
                    for state in compositions(total, len(q)):
                        mass = math.prod(q[i] ** state[i] for i in range(len(q)))
                        mass *= math.comb(population - total + r - 1, r - 1)
                        masses.append((state, Q(mass)))
            else:
                masses.append(((), Q(math.comb(population + r - 1, r - 1))))
            scaled_z = sum((mass for _, mass in masses), Q(0))
            z_value = wstar ** population * scaled_z
            expected_scaled = h_convolution(tuple(Q(1) for _ in bottlenecks) + q, population)
            assert scaled_z == expected_scaled
            leading = Q(math.comb(population + r - 1, r - 1)) * a_at_one
            c_means = [sum(Q(state[j]) * mass for state, mass in masses) / scaled_z
                       for j in range(len(q))]
            expected_m = sum(Q(population - sum(state)) * mass for state, mass in masses) / scaled_z
            expected_m2fall = sum(Q((population - sum(state)) * (population - sum(state) - 1)) * mass
                                  for state, mass in masses) / scaled_z
            if population:
                b_mean = [expected_m / (r * population) for _ in range(r)]
                b_second = []
                for i in range(r):
                    line = []
                    for j in range(r):
                        if i == j:
                            numerator = Q(2) * expected_m2fall / (r * (r + 1)) + expected_m / r
                        else:
                            numerator = expected_m2fall / (r * (r + 1))
                        line.append(numerator / (population * population))
                    b_second.append(line)
                remaining = expected_m / population
                scaled_means = qlist(b_mean)
                scaled_second = qmatrix(b_second)
                remaining_text = qstr(remaining)
            else:
                scaled_means = "undefined_at_N_zero"
                scaled_second = "undefined_at_N_zero"
                remaining_text = "undefined_at_N_zero"
            dirichlet_mean = [Q(1, r) for _ in range(r)]
            dirichlet_second = [[Q(2, r * (r + 1)) if i == j else Q(1, r * (r + 1))
                                 for j in range(r)] for i in range(r)]
            zero_mass = Q(math.comb(population + r - 1, r - 1), 1)
            rows.append({
                "family": family,
                "population": population,
                "weights": qlist(weights),
                "max_weight": qstr(wstar),
                "bottleneck_indices": bottlenecks,
                "nonbottleneck_indices": nonbottlenecks,
                "Z_N": qstr(z_value),
                "scaled_Z_N": qstr(scaled_z),
                "leading_scaled_Z_N": qstr(leading),
                "leading_ratio": qstr(scaled_z / leading),
                "nonbottleneck_zero_probability": qstr(zero_mass / scaled_z),
                "nonbottleneck_zero_limit": qstr(Q(1) / a_at_one),
                "nonbottleneck_means": qlist(c_means),
                "independent_geometric_limit_means": qlist([value / (1 - value) for value in q]),
                "bottleneck_scaled_means": scaled_means,
                "bottleneck_scaled_second_moments": scaled_second,
                "dirichlet_limit_means": qlist(dirichlet_mean),
                "dirichlet_limit_second_moments": qmatrix(dirichlet_second),
                "remaining_mass_fraction_mean": remaining_text,
                "zero_nonbottleneck_conditional_composition_count": math.comb(population + r - 1, r - 1),
                "zero_nonbottleneck_conditional_each_probability": qstr(Q(1, math.comb(population + r - 1, r - 1))),
            })
    return rows


BOUNDARIES = [
    {"face": "N=0", "status": "included", "exact_consequence": "singleton empty state; Z_0=1; all moments and event flows are zero"},
    {"face": "N=1", "status": "included", "exact_consequence": "pi(customer at i)=w_i/sum_j w_j and covariance is categorical"},
    {"face": "m=1", "status": "included", "exact_consequence": "P=[1], one state, Z_N=w_1^N, all service events are self-routes"},
    {"face": "zero routing entries", "status": "included", "exact_consequence": "allowed whenever the directed routing graph remains irreducible"},
    {"face": "self-routing probabilities", "status": "included", "exact_consequence": "counted in service event flows but omitted from state-change generator off-diagonals"},
    {"face": "all weights equal", "status": "included", "exact_consequence": "uniform law on weak compositions and exact all-station Dirichlet limit"},
    {"face": "tied maximal weights", "status": "included", "exact_consequence": "all maximizers retained; conditional bottleneck allocation is exactly uniform"},
    {"face": "traffic-vector gauge", "status": "included", "exact_consequence": "e to c e scales every w and Z_N by c and c^N but leaves all probabilities and flows invariant"},
    {"face": "mu_i=0", "status": "singular_excluded", "exact_consequence": "positive service rates are required; an infinite weight is not evaluated"},
    {"face": "w_i=0", "status": "singular_excluded", "exact_consequence": "irreducibility and positive service rates force e_i>0 and w_i>0; a zero weight is not an interior network"},
    {"face": "reducible routing", "status": "singular_excluded", "exact_consequence": "the unique positive traffic vector and irreducible composition chain need not exist"},
    {"face": "negative population", "status": "outside_state_space", "exact_consequence": "N is a nonnegative integer"},
]


def main() -> None:
    cases, states, zrows, moments, flows, reversals = exact_rows()
    condensations = condensation_rows()
    counts = {
        "case_rows": len(cases),
        "state_rows": len(states),
        "z_rows": len(zrows),
        "moment_rows": len(moments),
        "factorial_cells": sum(len(row["factorial_moments_through_degree_three"]) for row in moments),
        "flow_rows": len(flows),
        "reversal_rows": len(reversals),
        "condensation_rows": len(condensations),
        "boundary_rows": len(BOUNDARIES),
    }
    data = {
        "schema": "hcs-c285-gordon-newell-bottleneck-v1",
        "candidate_id": "HCS-C285",
        "source_commit": SOURCE,
        "evaluation_date": "2026-09-02",
        "fixed_epoch": EPOCH,
        "scope_literal": "NO_BAD_EULER_OR_ROOT_NUMBER",
        "evaluator": {"version": "0.2.0", "sha256": EVAL},
        "headline": "Finite irreducible Gordon--Newell networks have an exact canonical product form, exact flows and time reversal, and a complete unique-or-tied bottleneck condensation limit.",
        "model_contract": {
            "state_space": "S_N={n in Z_+^m: sum_i n_i=N}, m>=1, N>=0",
            "routing": "finite irreducible row-stochastic P; zero entries and self routes allowed; reversibility not assumed",
            "service": "one exponential single server of total rate mu_i>0 at each occupied station i",
            "transition": "n to n-e_i+e_j at service completion i routed to j; i=j is an event but not a state change",
            "traffic_gauge": "the unique positive e=eP is normalized by sum_i e_i=1; w_i=e_i/mu_i",
        },
        "analytic_proof_obligations": [
            "derive canonical product form and Z_N=h_N(w) by exact global balance",
            "derive every joint factorial moment and covariance by weight derivatives",
            "derive station throughput, directed service-event flow, and current conservation",
            "derive P-star, exact state-process time reversal, and the positive-population reversibility criterion",
            "prove complete-homogeneous asymptotics for every unique or tied maximal-weight set",
            "prove joint independent-geometric nonbottleneck and Dirichlet(1,...,1) bottleneck condensation",
            "separate N=0, N=1, m=1, zero-edge, self-route, equal-weight, zero-service, and reducible faces",
        ],
        "asymptotic_contract": {
            "bottleneck_set": "B={i:w_i=w_*}, r=|B|, C=B^c, q_j=w_j/w_*<1",
            "normalizer": "Z_N~w_*^N N^(r-1)/(r-1)! product_{j in C}(1-q_j)^(-1)",
            "joint_limit": "(n_C,n_B/N) converges to independent geometric(q_j) variables and an independent Dirichlet(1,...,1) vector",
            "unique_gate": "r=1 gives N-n_b=O_P(1); tied r>1 retains random macroscopic shares",
            "all_equal_gate": "C is empty, the finite law is exactly uniform on compositions, and the full vector has the Dirichlet limit",
        },
        "proof_contract": {
            "status": "PROVABLE AS STATED",
            "dependencies": ["finite CTMC global balance", "complete homogeneous symmetric polynomials", "elementary singularity analysis", "lattice Riemann sums on a simplex"],
            "scope": "closed single-class exponential single-server networks with fixed finite station set and fixed population",
            "novelty_boundary": "classical Gordon--Newell ownership is explicit; this is a source-local synthesis and executable closure, not an originality claim",
        },
        "citation_contract": {
            "classical_owner": "William J. Gordon and Gordon F. Newell, Operations Research 15(2), 254--265 (1967), doi:10.1287/opre.15.2.254",
            "reversal_reference": "F. P. Kelly, Reversibility and Stochastic Networks, Wiley 1979; Cambridge reissue 2011",
            "modern_text": "Frank Kelly and Elena Yudovina, Stochastic Networks, Cambridge University Press (2014), doi:10.1017/CBO9781139565363",
        },
        "collision_contract": {
            "registry_range": "HCS-C1 through HCS-C283 plus obstruction registry",
            "closest_distinctions": [
                "C225 is one finite-capacity birth--death queue with spectral mixing, not a closed routed many-station canonical ensemble",
                "C263 is a reinforced Polya urn with Dirichlet mixing, not stationary bottleneck condensation in a queueing network",
                "C220 is boundary-driven open TASEP with a matrix Ansatz, not Gordon--Newell product form",
                "C246 is a one-dimensional AIMD PDMP perpetuity, and C282 is a killed compound-Poisson risk process; neither owns closed routing or canonical condensation",
                "C181 is deterministic rotor routing on a finite digraph, not stochastic exponential service and traffic-equation time reversal",
            ],
        },
        "boundary_contract": BOUNDARIES,
        "nonclaims": [
            "No claim is made to originate the Gordon--Newell product form or its classical bottleneck principle.",
            "Finite exact cells are regression evidence and do not prove the all-m, all-N theorem or the N-to-infinity limit.",
            "No multiclass, multiserver, state-dependent-service, open-network, reducible-routing, or zero-service extension is claimed.",
            "No rational-prime carrier, logarithmic-prime clock, dynamical zeta, target divisor, Euler factor, root number, or Hilbert--Polya operator is obtained.",
        ],
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
        "route_a": {
            "tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
            "overall": "ROUTE_A_REJECTED",
            "route_b_invocation_allowed": False,
        },
        "regression": {
            "case_rows": cases,
            "state_rows": states,
            "z_rows": zrows,
            "moment_rows": moments,
            "flow_rows": flows,
            "reversal_rows": reversals,
            "condensation_rows": condensations,
            "boundary_rows": BOUNDARIES,
            "counts": counts,
        },
    }
    data["payload_sha256"] = payload_hash(data)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({"status": "C285_PRODUCER_PASS", "counts": counts,
                      "payload_sha256": data["payload_sha256"], "bytes": OUT.stat().st_size}, sort_keys=True))


if __name__ == "__main__":
    main()
