#!/usr/bin/env python3
"""Finite graph-atlas controls for RACG clique automata and join factors."""

from itertools import combinations, product

import networkx as nx
import numpy as np


def nonempty_cliques(graph):
    vertices = list(graph.nodes())
    return [
        frozenset(subset)
        for size in range(1, len(vertices) + 1)
        for subset in combinations(vertices, size)
        if all(graph.has_edge(left, right) for left, right in combinations(subset, 2))
    ]


def clique_automaton(graph):
    states = nonempty_cliques(graph)
    directed = nx.DiGraph()
    directed.add_nodes_from(states)
    for state in states:
        for vertex in graph.nodes():
            if vertex not in state:
                target = frozenset(
                    {vertex}
                    | {old for old in state if graph.has_edge(old, vertex)}
                )
                directed.add_edge(state, target)
    return directed


def recurrent_components(directed):
    answer = []
    for component in nx.strongly_connected_components(directed):
        if len(component) > 1 or any(directed.has_edge(node, node) for node in component):
            answer.append(component)
    return answer


def factor_data(graph):
    complement_components = sorted(
        (frozenset(component) for component in nx.connected_components(nx.complement(graph))),
        key=lambda component: min(component),
    )
    universal = tuple(next(iter(component)) for component in complement_components if len(component) == 1)
    nontrivial = tuple(component for component in complement_components if len(component) > 1)
    return universal, nontrivial


def adjacency_with_multiplicity(graph):
    states = nonempty_cliques(graph)
    position = {state: index for index, state in enumerate(states)}
    matrix = np.zeros((len(states), len(states)), dtype=int)
    for state in states:
        for vertex in graph.nodes():
            if vertex not in state:
                target = frozenset(
                    {vertex}
                    | {old for old in state if graph.has_edge(old, vertex)}
                )
                matrix[position[state], position[target]] += 1
    return matrix


def restricted_adjacency(graph, ordered_states):
    position = {state: index for index, state in enumerate(ordered_states)}
    matrix = np.zeros((len(ordered_states), len(ordered_states)), dtype=int)
    for state in ordered_states:
        for vertex in graph.nodes():
            if vertex not in state:
                target = frozenset(
                    {vertex}
                    | {old for old in state if graph.has_edge(old, vertex)}
                )
                if target in position:
                    matrix[position[state], position[target]] += 1
    return matrix


def kronecker_sum(matrices):
    answer = np.zeros(
        (int(np.prod([len(matrix) for matrix in matrices])),) * 2, dtype=int
    )
    for active in range(len(matrices)):
        term = np.array([[1]], dtype=int)
        for index, matrix in enumerate(matrices):
            factor = matrix if index == active else np.eye(len(matrix), dtype=int)
            term = np.kron(term, factor)
        answer += term
    return answer


def verify_component_matrices(graph):
    universal, nontrivial = factor_data(graph)
    recurrent = recurrent_components(clique_automaton(graph))
    indexed = {}
    for component in recurrent:
        supports = {
            frozenset(
                index
                for index, vertices in enumerate(nontrivial)
                if state & vertices
            )
            for state in component
        }
        universal_subsets = {
            frozenset(state & frozenset(universal)) for state in component
        }
        assert len(supports) == len(universal_subsets) == 1
        key = (next(iter(supports)), next(iter(universal_subsets)))
        assert key not in indexed
        indexed[key] = component

    expected_keys = {
        (frozenset(index for index in range(len(nontrivial)) if mask & (1 << index)),
         frozenset(universal[index] for index in range(len(universal)) if universal_mask & (1 << index)))
        for mask in range(1, 2 ** len(nontrivial))
        for universal_mask in range(2 ** len(universal))
    }
    assert set(indexed) == expected_keys

    for (support, frozen_universal), component in indexed.items():
        factor_indices = sorted(support)
        local_graphs = [graph.subgraph(nontrivial[index]).copy() for index in factor_indices]
        local_states = [nonempty_cliques(local_graph) for local_graph in local_graphs]
        ordered_states = [
            frozenset(frozen_universal).union(*state_tuple)
            for state_tuple in product(*local_states)
        ]
        assert set(ordered_states) == set(component)
        observed = restricted_adjacency(graph, ordered_states)
        expected = kronecker_sum(
            [adjacency_with_multiplicity(local_graph) for local_graph in local_graphs]
        )
        assert np.array_equal(observed, expected)

    full_support = frozenset(range(len(nontrivial)))
    maximal = sum(support == full_support for support, _ in indexed)
    if nontrivial:
        assert maximal == 2 ** len(universal)
    else:
        assert maximal == 0
    return len(recurrent), maximal


def main():
    atlas = [graph for graph in nx.graph_atlas_g() if 1 <= len(graph) <= 7]
    connected_complements = 0
    nontrivial_local_checks = 0
    structural_checks = 0
    maximal_checks = 0
    for raw_graph in atlas:
        graph = nx.convert_node_labels_to_integers(raw_graph)
        complement = nx.complement(graph)
        if nx.is_connected(complement):
            connected_complements += 1
            if len(graph) > 1:
                assert nx.is_strongly_connected(clique_automaton(graph))
                nontrivial_local_checks += 1

        universal, nontrivial = factor_data(graph)
        observed, maximal = verify_component_matrices(graph)
        expected = (2 ** len(nontrivial) - 1) * 2 ** len(universal)
        assert observed == expected
        assert maximal == 2 ** len(universal) if nontrivial else maximal == 0
        structural_checks += 1
        maximal_checks += 1

    # Extract the maximal component of an actual join of two edgeless
    # two-vertex graphs and compare it entrywise with the local Kronecker sum.
    explicit = nx.Graph()
    explicit.add_nodes_from(range(4))
    explicit.add_edges_from((left, right) for left in (0, 1) for right in (2, 3))
    universal, nontrivial = factor_data(explicit)
    assert not universal and len(nontrivial) == 2
    local_graphs = [explicit.subgraph(vertices).copy() for vertices in nontrivial]
    local_states = [nonempty_cliques(local_graph) for local_graph in local_graphs]
    ordered_states = [frozenset().union(*parts) for parts in product(*local_states)]
    observed_joined = restricted_adjacency(explicit, ordered_states)
    expected_joined = kronecker_sum(
        [adjacency_with_multiplicity(local_graph) for local_graph in local_graphs]
    )
    assert np.array_equal(observed_joined, expected_joined)
    local_rhos = [
        max(abs(np.linalg.eigvals(adjacency_with_multiplicity(local_graph))))
        for local_graph in local_graphs
    ]
    joined_rho = max(abs(np.linalg.eigvals(observed_joined)))
    assert abs(joined_rho - sum(local_rhos)) < 1e-10
    assert tuple(sorted(round(value.real) for value in np.linalg.eigvals(observed_joined))) == (
        -2,
        0,
        0,
        2,
    )

    print("connected-complement atlas graphs:", connected_complements)
    print("PASS: nontrivial local irreducibility checks:", nontrivial_local_checks)
    print("PASS: graph-atlas component matrix/count checks:", structural_checks)
    print("PASS: graph-atlas maximal-component checks:", maximal_checks)
    print("explicit two-factor spectral radius:", joined_rho)


if __name__ == "__main__":
    main()
