#!/usr/bin/env python3
"""Producer-independent exact checker for HCS-C285."""
from __future__ import annotations

import hashlib
import json
import math
import os
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = Path(os.environ.get("C285_EVIDENCE", ROOT / "results/c285_gordon_newell_evidence.json"))
SOURCE = "3878fa5282ca89f75700b3ef9d623f54dcb7bcf9"
EVAL = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
checks = 0


def claim(condition: bool) -> None:
    global checks
    assert condition
    checks += 1


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_unique(path: Path) -> dict:
    return json.loads(path.read_text(), object_pairs_hook=unique_object)


def payload_hash(data: dict) -> str:
    clean = dict(data)
    clean.pop("payload_sha256", None)
    return hashlib.sha256(json.dumps(clean, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def compositions(total: int, length: int):
    if length == 1:
        yield (total,)
    else:
        for last in range(total + 1):
            for head in compositions(total - last, length - 1):
                yield head + (last,)


def solve_linear(a: list[list[Q]], b: list[Q]) -> tuple[Q, ...]:
    """Exact elimination with column search, independent of producer layout."""
    n = len(a)
    work = [a[i][:] + [b[i]] for i in range(n)]
    pivot_row = 0
    for column in range(n):
        options = [row for row in range(pivot_row, n) if work[row][column] != 0]
        assert options
        chosen = options[-1]
        work[pivot_row], work[chosen] = work[chosen], work[pivot_row]
        divisor = work[pivot_row][column]
        for k in range(column, n + 1):
            work[pivot_row][k] /= divisor
        for row in range(n):
            if row == pivot_row:
                continue
            multiplier = work[row][column]
            if multiplier:
                for k in range(column, n + 1):
                    work[row][k] -= multiplier * work[pivot_row][k]
        pivot_row += 1
    return tuple(work[i][n] for i in range(n))


def stationary_traffic(p) -> tuple[Q, ...]:
    m = len(p)
    a = []
    b = []
    for j in range(1, m):
        a.append([p[i][j] - Q(int(i == j)) for i in range(m)])
        b.append(Q(0))
    a.append([Q(1)] * m)
    b.append(Q(1))
    return solve_linear(a, b)


def direct_partition(weights, population: int) -> Q:
    total = Q(0)
    for state in compositions(population, len(weights)):
        term = Q(1)
        for coordinate, weight in zip(state, weights):
            term *= weight ** coordinate
        total += term
    return total


def series_partition(weights, population: int) -> Q:
    polynomial = [Q(1)] + [Q(0)] * population
    for weight in reversed(weights):
        factor = [weight ** k for k in range(population + 1)]
        polynomial = [sum(polynomial[k] * factor[d - k] for k in range(d + 1))
                      for d in range(population + 1)]
    return polynomial[population]


def newton_partition(weights, population: int) -> Q:
    answer = [Q(1)]
    for n in range(1, population + 1):
        numerator = Q(0)
        for k in range(1, n + 1):
            numerator += sum((weight ** k for weight in weights), Q(0)) * answer[n - k]
        answer.append(numerator / n)
    return answer[population]


def falling(value: int, order: int) -> int:
    answer = 1
    for offset in range(order):
        answer *= value - offset
    return answer


def derivative_partition(weights, population: int, alpha: tuple[int, ...]) -> Q:
    target = population - sum(alpha)
    if target < 0:
        return Q(0)
    polynomial = [Q(1)] + [Q(0)] * target
    for i in range(len(weights) - 1, -1, -1):
        order = alpha[i]
        factor = [Q(math.comb(k + order, order)) * weights[i] ** k for k in range(target + 1)]
        polynomial = [sum(polynomial[k] * factor[d - k] for k in range(d + 1))
                      for d in range(target + 1)]
    scale = Q(1)
    for i, order in enumerate(alpha):
        scale *= math.factorial(order) * weights[i] ** order
    return scale * polynomial[target]


def build_generator(states, routing, service) -> list[list[Q]]:
    index = {state: position for position, state in enumerate(states)}
    q = [[Q(0) for _ in states] for _ in states]
    for position, state in enumerate(states):
        for origin in range(len(state)):
            if state[origin] == 0:
                continue
            for destination in range(len(state)):
                if destination == origin:
                    continue
                rate = service[origin] * routing[origin][destination]
                if rate == 0:
                    continue
                new_state = list(state)
                new_state[origin] -= 1
                new_state[destination] += 1
                target = index[tuple(new_state)]
                q[position][target] += rate
                q[position][position] -= rate
    return q


def left_nullspace(q: list[list[Q]]) -> list[tuple[Q, ...]]:
    """RREF nullspace of Q transpose, not a balance check against a guessed law."""
    matrix = [list(column) for column in zip(*q)]
    rows = len(matrix)
    columns = len(matrix[0])
    pivot_columns = []
    pivot_row = 0
    for column in range(columns):
        chosen = next((row for row in range(pivot_row, rows) if matrix[row][column]), None)
        if chosen is None:
            continue
        matrix[pivot_row], matrix[chosen] = matrix[chosen], matrix[pivot_row]
        divisor = matrix[pivot_row][column]
        matrix[pivot_row] = [value / divisor for value in matrix[pivot_row]]
        for row in range(rows):
            if row != pivot_row and matrix[row][column]:
                factor = matrix[row][column]
                matrix[row] = [a - factor * b for a, b in zip(matrix[row], matrix[pivot_row])]
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == rows:
            break
    free = [column for column in range(columns) if column not in pivot_columns]
    basis = []
    for free_column in free:
        vector = [Q(0)] * columns
        vector[free_column] = Q(1)
        for row, pivot in enumerate(pivot_columns):
            vector[pivot] = -matrix[row][free_column]
        basis.append(tuple(vector))
    return basis


SELF_NONREV = (
    (Q(1, 2), Q(1, 2), Q(0)), (Q(0), Q(1, 3), Q(2, 3)), (Q(3, 4), Q(0), Q(1, 4)),
)
DENSE_NONREV = (
    (Q(1, 5), Q(1, 2), Q(3, 10)), (Q(1, 3), Q(1, 6), Q(1, 2)), (Q(2, 5), Q(1, 5), Q(2, 5)),
)
REV_LINE = (
    (Q(1, 2), Q(1, 2), Q(0)), (Q(1, 4), Q(1, 2), Q(1, 4)), (Q(0), Q(1, 2), Q(1, 2)),
)
CYCLE3 = ((Q(0), Q(1), Q(0)), (Q(0), Q(0), Q(1)), (Q(1), Q(0), Q(0)))
CYCLE4 = ((Q(0), Q(1), Q(0), Q(0)), (Q(0), Q(0), Q(1), Q(0)),
          (Q(0), Q(0), Q(0), Q(1)), (Q(1), Q(0), Q(0), Q(0)))
EXPECTED_CASES = {
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
CONDENSATION_FAMILIES = {
    "unique_scaled": (Q(5, 3), Q(5, 6), Q(5, 9), Q(5, 12)),
    "two_tied_scaled": (Q(7, 5), Q(7, 5), Q(7, 10), Q(7, 15)),
    "three_tied": (Q(2), Q(2), Q(2), Q(1)),
    "all_equal": (Q(3, 7), Q(3, 7), Q(3, 7)),
}

TOP_KEYS = {
    "analytic_proof_obligations", "asymptotic_contract", "boundary_contract", "candidate_id",
    "citation_contract", "collision_contract", "evaluation_date", "evaluator", "fixed_epoch",
    "headline", "model_contract", "nonclaims", "payload_sha256", "proof_contract", "regression",
    "route_a", "schema", "scope_flags", "scope_literal", "source_commit",
}
REGRESSION_KEYS = {"case_rows", "state_rows", "z_rows", "moment_rows", "flow_rows",
                   "reversal_rows", "condensation_rows", "boundary_rows", "counts"}
CASE_KEYS = {"case", "population", "stations", "routing", "service_rates", "traffic", "weights",
             "state_count", "irreducible_routing", "routing_reversible", "bottleneck_indices"}
STATE_KEYS = {"case", "state", "unnormalized_weight", "probability", "left_balance"}
Z_KEYS = {"case", "Z_N_direct", "Z_N_convolution", "Z_N_newton", "Z_N_minus_1", "three_way_equal"}
MOMENT_KEYS = {"case", "means", "covariance", "factorial_moments_through_degree_three"}
FACTORIAL_KEYS = {"alpha", "value"}
FLOW_KEYS = {"case", "positive_population", "Z_ratio", "utilizations", "station_throughputs",
             "directed_edge_event_flows", "antisymmetric_net_currents", "flow_conservation_residuals"}
REVERSAL_KEYS = {"case", "reversed_routing", "reversed_traffic", "reversal_is_involution",
                 "state_process_reversible_for_positive_population", "detailed_balance_defects"}
CONDENSATION_KEYS = {"family", "population", "weights", "max_weight", "bottleneck_indices",
                     "nonbottleneck_indices", "Z_N", "scaled_Z_N", "leading_scaled_Z_N",
                     "leading_ratio", "nonbottleneck_zero_probability", "nonbottleneck_zero_limit",
                     "nonbottleneck_means", "independent_geometric_limit_means",
                     "bottleneck_scaled_means", "bottleneck_scaled_second_moments",
                     "dirichlet_limit_means", "dirichlet_limit_second_moments",
                     "remaining_mass_fraction_mean", "zero_nonbottleneck_conditional_composition_count",
                     "zero_nonbottleneck_conditional_each_probability"}
BOUNDARY_KEYS = {"face", "status", "exact_consequence"}

EXPECTED_BOUNDARIES = [
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


def index_unique(rows: list[dict], key: str, expected: set) -> dict:
    values = [row[key] for row in rows]
    claim(len(values) == len(set(values)))
    claim(set(values) == expected)
    return {row[key]: row for row in rows}


def parse_matrix(value):
    return tuple(tuple(Q(entry) for entry in row) for row in value)


def exact_type(value, expected: type) -> None:
    """Require the exact JSON-decoded type; bool is never accepted as int."""
    claim(type(value) is expected)


def exact_object(value, keys: set[str]) -> None:
    exact_type(value, dict)
    claim(set(value) == keys)


def exact_string(value) -> None:
    exact_type(value, str)


def exact_integer(value) -> None:
    exact_type(value, int)


def exact_boolean(value) -> None:
    exact_type(value, bool)


def exact_list(value) -> None:
    exact_type(value, list)


def exact_fraction_text(value) -> None:
    """Require the producer's reduced numerator/positive-denominator syntax."""
    exact_string(value)
    try:
        parsed = Q(value)
    except (ValueError, ZeroDivisionError) as error:
        raise AssertionError("invalid rational string") from error
    claim(value == f"{parsed.numerator}/{parsed.denominator}")


def string_list(value) -> None:
    exact_list(value)
    for item in value:
        exact_string(item)


def integer_list(value) -> None:
    exact_list(value)
    for item in value:
        exact_integer(item)


def fraction_list(value) -> None:
    exact_list(value)
    for item in value:
        exact_fraction_text(item)


def fraction_matrix(value) -> None:
    exact_list(value)
    for row in value:
        fraction_list(row)


def validate_exact_json_schema(data: dict) -> None:
    """Validate every object, key set, list, scalar, and tagged union."""
    exact_object(data, TOP_KEYS)
    for key in (
        "schema", "candidate_id", "source_commit", "evaluation_date",
        "scope_literal", "headline", "payload_sha256",
    ):
        exact_string(data[key])
    exact_integer(data["fixed_epoch"])

    exact_object(data["evaluator"], {"version", "sha256"})
    exact_string(data["evaluator"]["version"])
    exact_string(data["evaluator"]["sha256"])

    model_keys = {"state_space", "routing", "service", "transition", "traffic_gauge"}
    exact_object(data["model_contract"], model_keys)
    for key in model_keys:
        exact_string(data["model_contract"][key])
    string_list(data["analytic_proof_obligations"])

    asymptotic_keys = {"bottleneck_set", "normalizer", "joint_limit", "unique_gate", "all_equal_gate"}
    exact_object(data["asymptotic_contract"], asymptotic_keys)
    for key in asymptotic_keys:
        exact_string(data["asymptotic_contract"][key])

    proof_keys = {"status", "dependencies", "scope", "novelty_boundary"}
    exact_object(data["proof_contract"], proof_keys)
    exact_string(data["proof_contract"]["status"])
    string_list(data["proof_contract"]["dependencies"])
    exact_string(data["proof_contract"]["scope"])
    exact_string(data["proof_contract"]["novelty_boundary"])

    citation_keys = {"classical_owner", "reversal_reference", "modern_text"}
    exact_object(data["citation_contract"], citation_keys)
    for key in citation_keys:
        exact_string(data["citation_contract"][key])

    exact_object(data["collision_contract"], {"registry_range", "closest_distinctions"})
    exact_string(data["collision_contract"]["registry_range"])
    string_list(data["collision_contract"]["closest_distinctions"])

    string_list(data["nonclaims"])
    exact_object(data["scope_flags"], {
        "arithmetic_local_data", "euler_factors", "root_numbers", "automorphy",
        "target_divisor_or_counting_law", "target_functional_equation",
        "target_zero_match", "hilbert_polya_operator", "route_b_authorization",
    })
    for value in data["scope_flags"].values():
        exact_boolean(value)

    exact_object(data["route_a"], {"tuple", "overall", "route_b_invocation_allowed"})
    string_list(data["route_a"]["tuple"])
    exact_string(data["route_a"]["overall"])
    exact_boolean(data["route_a"]["route_b_invocation_allowed"])

    def boundary_rows(value) -> None:
        exact_list(value)
        for row in value:
            exact_object(row, BOUNDARY_KEYS)
            for key in BOUNDARY_KEYS:
                exact_string(row[key])

    boundary_rows(data["boundary_contract"])

    regression = data["regression"]
    exact_object(regression, REGRESSION_KEYS)
    exact_object(regression["counts"], {
        "case_rows", "state_rows", "z_rows", "moment_rows", "factorial_cells",
        "flow_rows", "reversal_rows", "condensation_rows", "boundary_rows",
    })
    for value in regression["counts"].values():
        exact_integer(value)

    exact_list(regression["case_rows"])
    for row in regression["case_rows"]:
        exact_object(row, CASE_KEYS)
        exact_string(row["case"])
        exact_integer(row["population"])
        exact_integer(row["stations"])
        fraction_matrix(row["routing"])
        fraction_list(row["service_rates"])
        fraction_list(row["traffic"])
        fraction_list(row["weights"])
        exact_integer(row["state_count"])
        exact_boolean(row["irreducible_routing"])
        exact_boolean(row["routing_reversible"])
        integer_list(row["bottleneck_indices"])

    exact_list(regression["state_rows"])
    for row in regression["state_rows"]:
        exact_object(row, STATE_KEYS)
        exact_string(row["case"])
        integer_list(row["state"])
        exact_fraction_text(row["unnormalized_weight"])
        exact_fraction_text(row["probability"])
        exact_fraction_text(row["left_balance"])

    exact_list(regression["z_rows"])
    for row in regression["z_rows"]:
        exact_object(row, Z_KEYS)
        exact_string(row["case"])
        for key in {"Z_N_direct", "Z_N_convolution", "Z_N_newton", "Z_N_minus_1"}:
            exact_fraction_text(row[key])
        exact_boolean(row["three_way_equal"])

    exact_list(regression["moment_rows"])
    for row in regression["moment_rows"]:
        exact_object(row, MOMENT_KEYS)
        exact_string(row["case"])
        fraction_list(row["means"])
        fraction_matrix(row["covariance"])
        exact_list(row["factorial_moments_through_degree_three"])
        for probe in row["factorial_moments_through_degree_three"]:
            exact_object(probe, FACTORIAL_KEYS)
            integer_list(probe["alpha"])
            exact_fraction_text(probe["value"])

    exact_list(regression["flow_rows"])
    for row in regression["flow_rows"]:
        exact_object(row, FLOW_KEYS)
        exact_string(row["case"])
        exact_boolean(row["positive_population"])
        exact_fraction_text(row["Z_ratio"])
        fraction_list(row["utilizations"])
        fraction_list(row["station_throughputs"])
        fraction_matrix(row["directed_edge_event_flows"])
        fraction_matrix(row["antisymmetric_net_currents"])
        fraction_list(row["flow_conservation_residuals"])

    exact_list(regression["reversal_rows"])
    for row in regression["reversal_rows"]:
        exact_object(row, REVERSAL_KEYS)
        exact_string(row["case"])
        fraction_matrix(row["reversed_routing"])
        fraction_list(row["reversed_traffic"])
        exact_boolean(row["reversal_is_involution"])
        claim(type(row["state_process_reversible_for_positive_population"]) in {bool, str})
        if type(row["state_process_reversible_for_positive_population"]) is str:
            claim(row["state_process_reversible_for_positive_population"] == "trivial_singleton")
        fraction_matrix(row["detailed_balance_defects"])

    exact_list(regression["condensation_rows"])
    for row in regression["condensation_rows"]:
        exact_object(row, CONDENSATION_KEYS)
        exact_string(row["family"])
        exact_integer(row["population"])
        fraction_list(row["weights"])
        exact_fraction_text(row["max_weight"])
        integer_list(row["bottleneck_indices"])
        integer_list(row["nonbottleneck_indices"])
        for key in {
            "Z_N", "scaled_Z_N", "leading_scaled_Z_N", "leading_ratio",
            "nonbottleneck_zero_probability", "nonbottleneck_zero_limit",
            "zero_nonbottleneck_conditional_each_probability",
        }:
            exact_fraction_text(row[key])
        fraction_list(row["nonbottleneck_means"])
        fraction_list(row["independent_geometric_limit_means"])
        if type(row["bottleneck_scaled_means"]) is str:
            claim(row["bottleneck_scaled_means"] == "undefined_at_N_zero")
        else:
            fraction_list(row["bottleneck_scaled_means"])
        if type(row["bottleneck_scaled_second_moments"]) is str:
            claim(row["bottleneck_scaled_second_moments"] == "undefined_at_N_zero")
        else:
            fraction_matrix(row["bottleneck_scaled_second_moments"])
        fraction_list(row["dirichlet_limit_means"])
        fraction_matrix(row["dirichlet_limit_second_moments"])
        if row["remaining_mass_fraction_mean"] == "undefined_at_N_zero":
            exact_string(row["remaining_mass_fraction_mean"])
        else:
            exact_fraction_text(row["remaining_mass_fraction_mean"])
        exact_integer(row["zero_nonbottleneck_conditional_composition_count"])

    boundary_rows(regression["boundary_rows"])


def main() -> None:
    data = load_unique(EVIDENCE)
    validate_exact_json_schema(data)
    claim(set(data) == TOP_KEYS)
    claim(data["payload_sha256"] == payload_hash(data))
    claim(data["schema"] == "hcs-c285-gordon-newell-bottleneck-v1")
    claim(data["candidate_id"] == "HCS-C285" and data["source_commit"] == SOURCE)
    claim(data["evaluation_date"] == "2026-09-02" and data["fixed_epoch"] == 1788307200)
    claim(data["scope_literal"] == "NO_BAD_EULER_OR_ROOT_NUMBER")
    claim(data["evaluator"] == {"version": "0.2.0", "sha256": EVAL})
    claim(data["headline"] == "Finite irreducible Gordon--Newell networks have an exact canonical product form, exact flows and time reversal, and a complete unique-or-tied bottleneck condensation limit.")
    claim(data["model_contract"] == {
        "state_space": "S_N={n in Z_+^m: sum_i n_i=N}, m>=1, N>=0",
        "routing": "finite irreducible row-stochastic P; zero entries and self routes allowed; reversibility not assumed",
        "service": "one exponential single server of total rate mu_i>0 at each occupied station i",
        "transition": "n to n-e_i+e_j at service completion i routed to j; i=j is an event but not a state change",
        "traffic_gauge": "the unique positive e=eP is normalized by sum_i e_i=1; w_i=e_i/mu_i",
    })
    claim(data["analytic_proof_obligations"] == [
        "derive canonical product form and Z_N=h_N(w) by exact global balance",
        "derive every joint factorial moment and covariance by weight derivatives",
        "derive station throughput, directed service-event flow, and current conservation",
        "derive P-star, exact state-process time reversal, and the positive-population reversibility criterion",
        "prove complete-homogeneous asymptotics for every unique or tied maximal-weight set",
        "prove joint independent-geometric nonbottleneck and Dirichlet(1,...,1) bottleneck condensation",
        "separate N=0, N=1, m=1, zero-edge, self-route, equal-weight, zero-service, and reducible faces",
    ])
    claim(data["asymptotic_contract"] == {
        "bottleneck_set": "B={i:w_i=w_*}, r=|B|, C=B^c, q_j=w_j/w_*<1",
        "normalizer": "Z_N~w_*^N N^(r-1)/(r-1)! product_{j in C}(1-q_j)^(-1)",
        "joint_limit": "(n_C,n_B/N) converges to independent geometric(q_j) variables and an independent Dirichlet(1,...,1) vector",
        "unique_gate": "r=1 gives N-n_b=O_P(1); tied r>1 retains random macroscopic shares",
        "all_equal_gate": "C is empty, the finite law is exactly uniform on compositions, and the full vector has the Dirichlet limit",
    })
    claim(data["proof_contract"] == {
        "status": "PROVABLE AS STATED",
        "dependencies": ["finite CTMC global balance", "complete homogeneous symmetric polynomials", "elementary singularity analysis", "lattice Riemann sums on a simplex"],
        "scope": "closed single-class exponential single-server networks with fixed finite station set and fixed population",
        "novelty_boundary": "classical Gordon--Newell ownership is explicit; this is a source-local synthesis and executable closure, not an originality claim",
    })
    claim(data["citation_contract"] == {
        "classical_owner": "William J. Gordon and Gordon F. Newell, Operations Research 15(2), 254--265 (1967), doi:10.1287/opre.15.2.254",
        "reversal_reference": "F. P. Kelly, Reversibility and Stochastic Networks, Wiley 1979; Cambridge reissue 2011",
        "modern_text": "Frank Kelly and Elena Yudovina, Stochastic Networks, Cambridge University Press (2014), doi:10.1017/CBO9781139565363",
    })
    claim(data["collision_contract"] == {
        "registry_range": "HCS-C1 through HCS-C283 plus obstruction registry",
        "closest_distinctions": [
            "C225 is one finite-capacity birth--death queue with spectral mixing, not a closed routed many-station canonical ensemble",
            "C263 is a reinforced Polya urn with Dirichlet mixing, not stationary bottleneck condensation in a queueing network",
            "C220 is boundary-driven open TASEP with a matrix Ansatz, not Gordon--Newell product form",
            "C246 is a one-dimensional AIMD PDMP perpetuity, and C282 is a killed compound-Poisson risk process; neither owns closed routing or canonical condensation",
            "C181 is deterministic rotor routing on a finite digraph, not stochastic exponential service and traffic-equation time reversal",
        ],
    })
    claim(data["nonclaims"] == [
        "No claim is made to originate the Gordon--Newell product form or its classical bottleneck principle.",
        "Finite exact cells are regression evidence and do not prove the all-m, all-N theorem or the N-to-infinity limit.",
        "No multiclass, multiserver, state-dependent-service, open-network, reducible-routing, or zero-service extension is claimed.",
        "No rational-prime carrier, logarithmic-prime clock, dynamical zeta, target divisor, Euler factor, root number, or Hilbert--Polya operator is obtained.",
    ])
    claim(data["scope_flags"] == {"arithmetic_local_data": False, "euler_factors": False,
                                   "root_numbers": False, "automorphy": False,
                                   "target_divisor_or_counting_law": False,
                                   "target_functional_equation": False, "target_zero_match": False,
                                   "hilbert_polya_operator": False, "route_b_authorization": False})
    claim(data["route_a"] == {"tuple": ["A0_FAIL", "A1_FAIL", "A2_FAIL", "A3_FAIL", "A4_FAIL"],
                               "overall": "ROUTE_A_REJECTED", "route_b_invocation_allowed": False})
    claim(data["boundary_contract"] == EXPECTED_BOUNDARIES)
    claim(set(data["regression"]) == REGRESSION_KEYS)
    regression = data["regression"]
    claim(regression["counts"] == {"case_rows": 9, "state_rows": 177, "z_rows": 9,
                                    "moment_rows": 9, "factorial_cells": 165, "flow_rows": 9,
                                    "reversal_rows": 9, "condensation_rows": 28, "boundary_rows": 12})

    case_map = index_unique(regression["case_rows"], "case", set(EXPECTED_CASES))
    z_map = index_unique(regression["z_rows"], "case", set(EXPECTED_CASES))
    moment_map = index_unique(regression["moment_rows"], "case", set(EXPECTED_CASES))
    flow_map = index_unique(regression["flow_rows"], "case", set(EXPECTED_CASES))
    reversal_map = index_unique(regression["reversal_rows"], "case", set(EXPECTED_CASES))
    state_groups = {name: [] for name in EXPECTED_CASES}
    for row in regression["state_rows"]:
        claim(set(row) == STATE_KEYS)
        claim(row["case"] in state_groups)
        state_groups[row["case"]].append(row)

    for name, (population, routing, service) in EXPECTED_CASES.items():
        row = case_map[name]
        claim(set(row) == CASE_KEYS)
        m = len(routing)
        e = stationary_traffic(routing)
        claim(all(value > 0 for value in e) and sum(e) == 1)
        for j in range(m):
            claim(sum(e[i] * routing[i][j] for i in range(m)) == e[j])
        weights = tuple(e[i] / service[i] for i in range(m))
        reversible = all(e[i] * routing[i][j] == e[j] * routing[j][i] for i in range(m) for j in range(m))
        states = list(compositions(population, m))
        claim(row["population"] == population and row["stations"] == m)
        claim(parse_matrix(row["routing"]) == routing)
        claim(tuple(Q(x) for x in row["service_rates"]) == service)
        claim(tuple(Q(x) for x in row["traffic"]) == e)
        claim(tuple(Q(x) for x in row["weights"]) == weights)
        claim(row["state_count"] == len(states) and row["irreducible_routing"] is True)
        claim(row["routing_reversible"] == reversible)
        claim(row["bottleneck_indices"] == [i for i, value in enumerate(weights) if value == max(weights)])

        z_direct = direct_partition(weights, population)
        z_series = series_partition(weights, population)
        z_newton = newton_partition(weights, population)
        claim(z_direct == z_series == z_newton)
        zr = z_map[name]
        claim(set(zr) == Z_KEYS)
        claim(Q(zr["Z_N_direct"]) == z_direct and Q(zr["Z_N_convolution"]) == z_series)
        claim(Q(zr["Z_N_newton"]) == z_newton and zr["three_way_equal"] is True)
        previous = series_partition(weights, population - 1) if population else Q(0)
        claim(Q(zr["Z_N_minus_1"]) == previous)

        evidence_states = state_groups[name]
        keys = [tuple(item["state"]) for item in evidence_states]
        claim(len(keys) == len(set(keys)) == len(states) and set(keys) == set(states))
        by_state = {tuple(item["state"]): item for item in evidence_states}
        qgen = build_generator(states, routing, service)
        for qrow in qgen:
            claim(sum(qrow) == 0)
        basis = left_nullspace(qgen)
        claim(len(basis) == 1)
        vector = basis[0]
        normalized = tuple(value / sum(vector) for value in vector)
        claim(all(value > 0 for value in normalized) and sum(normalized) == 1)
        raw_weights = []
        for state in states:
            raw = math.prod(weights[i] ** state[i] for i in range(m))
            raw_weights.append(Q(raw))
            stored = by_state[state]
            claim(set(stored) == STATE_KEYS)
            claim(Q(stored["unnormalized_weight"]) == raw)
            claim(Q(stored["probability"]) == raw / z_direct)
            claim(Q(stored["left_balance"]) == 0)
        for position in range(len(states)):
            claim(normalized[position] == raw_weights[position] / z_direct)
            claim(sum(normalized[row_index] * qgen[row_index][position]
                      for row_index in range(len(states))) == 0)

        mr = moment_map[name]
        claim(set(mr) == MOMENT_KEYS)
        claim(len(mr["means"]) == m and len(mr["covariance"]) == m)
        means = [sum(Q(state[i]) * raw_weights[k] for k, state in enumerate(states)) / z_direct
                 for i in range(m)]
        claim([Q(x) for x in mr["means"]] == means)
        covariance = []
        for i in range(m):
            claim(len(mr["covariance"][i]) == m)
            line = []
            for j in range(m):
                second = sum(Q(state[i] * state[j]) * raw_weights[k]
                             for k, state in enumerate(states)) / z_direct
                line.append(second - means[i] * means[j])
                claim(Q(mr["covariance"][i][j]) == line[-1])
            covariance.append(line)
            claim(sum(line) == 0)
        expected_alphas = []
        for degree in range(1, min(3, population) + 1):
            expected_alphas.extend(compositions(degree, m))
        probes = mr["factorial_moments_through_degree_three"]
        probe_keys = [tuple(probe["alpha"]) for probe in probes]
        claim(len(probe_keys) == len(set(probe_keys)) and set(probe_keys) == set(expected_alphas))
        for probe in probes:
            claim(set(probe) == FACTORIAL_KEYS)
            alpha = tuple(probe["alpha"])
            enumeration = sum(Q(math.prod(falling(state[i], alpha[i]) for i in range(m))) * raw_weights[k]
                              for k, state in enumerate(states)) / z_direct
            derivative = derivative_partition(weights, population, alpha) / z_direct
            claim(Q(probe["value"]) == enumeration == derivative)

        fr = flow_map[name]
        claim(set(fr) == FLOW_KEYS)
        ratio = previous / z_direct if population else Q(0)
        utilization = [weights[i] * ratio for i in range(m)]
        throughputs = [e[i] * ratio for i in range(m)]
        edge = [[e[i] * routing[i][j] * ratio for j in range(m)] for i in range(m)]
        current = [[edge[i][j] - edge[j][i] for j in range(m)] for i in range(m)]
        claim(fr["positive_population"] == (population > 0) and Q(fr["Z_ratio"]) == ratio)
        claim([Q(x) for x in fr["utilizations"]] == utilization)
        claim([Q(x) for x in fr["station_throughputs"]] == throughputs)
        claim(parse_matrix(fr["directed_edge_event_flows"]) == tuple(tuple(line) for line in edge))
        claim(parse_matrix(fr["antisymmetric_net_currents"]) == tuple(tuple(line) for line in current))
        claim(len(fr["flow_conservation_residuals"]) == m and all(Q(x) == 0 for x in fr["flow_conservation_residuals"]))
        for i in range(m):
            claim(sum(edge[i]) == throughputs[i])
            claim(sum(edge[j][i] for j in range(m)) == throughputs[i])

        rr = reversal_map[name]
        claim(set(rr) == REVERSAL_KEYS)
        pstar = tuple(tuple(e[j] * routing[j][i] / e[i] for j in range(m)) for i in range(m))
        claim(parse_matrix(rr["reversed_routing"]) == pstar)
        for line in pstar:
            claim(sum(line) == 1 and all(value >= 0 for value in line))
        estar = stationary_traffic(pstar)
        claim(tuple(Q(x) for x in rr["reversed_traffic"]) == estar == e)
        twice = tuple(tuple(estar[j] * pstar[j][i] / estar[i] for j in range(m)) for i in range(m))
        claim(twice == routing and rr["reversal_is_involution"] is True)
        defects = tuple(tuple(e[i] * routing[i][j] - e[j] * routing[j][i] for j in range(m)) for i in range(m))
        claim(parse_matrix(rr["detailed_balance_defects"]) == defects)
        expected_reversibility = reversible if population else "trivial_singleton"
        claim(rr["state_process_reversible_for_positive_population"] == expected_reversibility)

    condensation_rows = regression["condensation_rows"]
    condensation_keys = [(row["family"], row["population"]) for row in condensation_rows]
    expected_condensation_keys = {(family, n) for family in CONDENSATION_FAMILIES
                                  for n in (0, 1, 2, 4, 8, 16, 32)}
    claim(len(condensation_keys) == len(set(condensation_keys)) and set(condensation_keys) == expected_condensation_keys)
    for row in condensation_rows:
        claim(set(row) == CONDENSATION_KEYS)
        family = row["family"]
        population = row["population"]
        weights = CONDENSATION_FAMILIES[family]
        claim(tuple(Q(x) for x in row["weights"]) == weights)
        wstar = max(weights)
        b = [i for i, value in enumerate(weights) if value == wstar]
        c = [i for i in range(len(weights)) if i not in b]
        r = len(b)
        ratios = tuple(weights[i] / wstar for i in c)
        a1 = math.prod(Q(1, 1 - value) for value in ratios) if ratios else Q(1)
        claim(Q(row["max_weight"]) == wstar and row["bottleneck_indices"] == b)
        claim(row["nonbottleneck_indices"] == c)
        masses = []
        if ratios:
            for total in range(population + 1):
                for state in compositions(total, len(ratios)):
                    mass = math.prod(ratios[i] ** state[i] for i in range(len(ratios)))
                    mass *= math.comb(population - total + r - 1, r - 1)
                    masses.append((state, Q(mass)))
        else:
            masses = [((), Q(math.comb(population + r - 1, r - 1)))]
        scaled_z = sum((mass for _, mass in masses), Q(0))
        z = wstar ** population * scaled_z
        leading = Q(math.comb(population + r - 1, r - 1)) * a1
        claim(Q(row["Z_N"]) == z and Q(row["scaled_Z_N"]) == scaled_z)
        claim(Q(row["leading_scaled_Z_N"]) == leading and Q(row["leading_ratio"]) == scaled_z / leading)
        zero_mass = Q(math.comb(population + r - 1, r - 1))
        claim(Q(row["nonbottleneck_zero_probability"]) == zero_mass / scaled_z)
        claim(Q(row["nonbottleneck_zero_limit"]) == Q(1) / a1)
        cmeans = [sum(Q(state[j]) * mass for state, mass in masses) / scaled_z for j in range(len(ratios))]
        claim([Q(x) for x in row["nonbottleneck_means"]] == cmeans)
        claim([Q(x) for x in row["independent_geometric_limit_means"]] == [q / (1 - q) for q in ratios])
        em = sum(Q(population - sum(state)) * mass for state, mass in masses) / scaled_z
        emfall = sum(Q((population - sum(state)) * (population - sum(state) - 1)) * mass
                     for state, mass in masses) / scaled_z
        dir_mean = [Q(1, r)] * r
        dir_second = [[Q(2, r * (r + 1)) if i == j else Q(1, r * (r + 1))
                       for j in range(r)] for i in range(r)]
        claim([Q(x) for x in row["dirichlet_limit_means"]] == dir_mean)
        claim(parse_matrix(row["dirichlet_limit_second_moments"]) == tuple(tuple(line) for line in dir_second))
        if population == 0:
            claim(row["bottleneck_scaled_means"] == "undefined_at_N_zero")
            claim(row["bottleneck_scaled_second_moments"] == "undefined_at_N_zero")
            claim(row["remaining_mass_fraction_mean"] == "undefined_at_N_zero")
        else:
            claim([Q(x) for x in row["bottleneck_scaled_means"]] == [em / (r * population)] * r)
            expected_second = []
            for i in range(r):
                expected_second.append([])
                for j in range(r):
                    numerator = (Q(2) * emfall / (r * (r + 1)) + em / r) if i == j else emfall / (r * (r + 1))
                    expected_second[-1].append(numerator / (population * population))
            claim(parse_matrix(row["bottleneck_scaled_second_moments"]) == tuple(tuple(line) for line in expected_second))
            claim(Q(row["remaining_mass_fraction_mean"]) == em / population)
        composition_count = math.comb(population + r - 1, r - 1)
        claim(row["zero_nonbottleneck_conditional_composition_count"] == composition_count)
        claim(Q(row["zero_nonbottleneck_conditional_each_probability"]) == Q(1, composition_count))

    boundaries = regression["boundary_rows"]
    claim(len(boundaries) == len(EXPECTED_BOUNDARIES))
    for row in boundaries:
        claim(set(row) == BOUNDARY_KEYS)
    claim(boundaries == EXPECTED_BOUNDARIES)
    print(
        f"C285 independent checker: PASS ({checks} assertions; strict exact JSON types, "
        "canonical Fraction text, generator left nullspace, three-way Z, moments, "
        "reversal, condensation, and boundaries)"
    )


if __name__ == "__main__":
    main()
