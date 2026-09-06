#!/usr/bin/env python3
"""Two immutable complete boxes; only author checks, no input file reads."""
from collections import Counter
from hashlib import sha256
from itertools import combinations
import json
from math import gcd, prod
import sys

CHECKS = Counter()
PRIMES = (2, 3, 5, 7, 11, 13, 17, 19)


def need(condition, name):
    CHECKS[name] += 1
    if not condition:
        raise AssertionError(name)


def digest(value):
    return sha256(json.dumps(value, separators=(',', ':')).encode('ascii')).hexdigest()


def profile(states, arrows, rule, parameters, encoding):
    count = len(states)
    need(count > 0 and len(arrows) == count, rule+'_total_map')
    need(all(isinstance(t, int) and 0 <= t < count for t in arrows), rule+'_carrier')
    fibres = [0]*count
    for target in arrows:
        fibres[target] += 1
    depths, periods, cycles = [-1]*count, [0]*count, []
    for start in range(count):
        if depths[start] >= 0:
            continue
        path, visited, node = [], {}, start
        while depths[node] < 0 and node not in visited:
            visited[node] = len(path)
            path.append(node)
            node = arrows[node]
        if node in visited:
            cycle = path[visited[node]:]
            pivot = cycle.index(min(cycle))
            cycle = cycle[pivot:]+cycle[:pivot]
            cycles.append(cycle)
            for member in cycle:
                depths[member], periods[member] = 0, len(cycle)
        for member in reversed(path):
            if depths[member] < 0:
                depths[member] = depths[arrows[member]]+1
                periods[member] = periods[arrows[member]]
    cycles.sort()
    need(sum(fibres) == count, rule+'_fibre_weight')
    need(sum(len(c) for c in cycles) == depths.count(0), rule+'_core_count')
    for source, target in enumerate(arrows):
        need(periods[source] == periods[target], rule+'_period_propagation')
        need(depths[source] == depths[target] == 0 or depths[source] == depths[target]+1,
             rule+'_depth_propagation')
    for cycle in cycles:
        need(all(arrows[node] == cycle[(j+1) % len(cycle)] for j, node in enumerate(cycle)),
             rule+'_all_cycle_edges')
    height = max(depths)
    path = [depths.index(height)]
    for _ in range(height):
        path.append(arrows[path[-1]])
    maximum = max(fibres)
    maxima = [i for i, amount in enumerate(fibres) if amount == maximum]
    longest = min((c for c in cycles if len(c) == max(map(len, cycles))), key=tuple)
    return {'rule': rule, 'parameters': parameters, 'state_count': count,
            'state_index_encoding': encoding, 'states_by_index': states,
            'arrows_by_source_index': arrows, 'target_fibre_sizes_by_index': fibres,
            'depths_by_source_index': depths, 'eventual_periods_by_source_index': periods,
            'all_cycles_as_indices': cycles,
            'cycles_by_length': dict(sorted(Counter(map(len, cycles)).items())),
            'depth_histogram': dict(sorted(Counter(depths).items())),
            'target_fibre_histogram_including_zero': dict(sorted(Counter(fibres).items())),
            'image_size': count-fibres.count(0), 'recurrent_states': depths.count(0),
            'height': height, 'maximum_fibre': maximum,
            'all_maximum_fibre_target_indices': maxima,
            'all_maximum_fibre_targets': [states[i] for i in maxima],
            'deepest_tail_indices_through_first_recurrent': path,
            'deepest_tail_states_through_first_recurrent': [states[i] for i in path],
            'one_longest_cycle_indices': longest,
            'one_longest_cycle_states': [states[i] for i in longest],
            'array_sha256': {'states': digest(states), 'arrows': digest(arrows),
                             'fibres': digest(fibres), 'depths': digest(depths)}}


def run_adg():
    results = []
    for ambient_mask in range(1 << len(PRIMES)):
        primes = tuple(p for i, p in enumerate(PRIMES) if ambient_mask >> i & 1)
        ambient = prod(primes)
        states = sorted(prod(p for i, p in enumerate(primes) if mask >> i & 1)
                        for mask in range(1 << len(primes)))
        index = {d: i for i, d in enumerate(states)}
        need(len(index) == 1 << len(primes), 'ADG_distinct_complete_divisors')
        arrows = []
        for divisor in states:
            support = tuple(p for p in primes if divisor % p == 0)
            derivative = sum(divisor//p for p in support)
            target = gcd(ambient, derivative)
            alternate = prod(p for p in primes if p not in support
                             and sum(pow(q, -1, p) for q in support) % p == 0)
            need(target == alternate, 'ADG_integer_vs_reciprocal_CRT')
            need(gcd(divisor, derivative) == 1, 'ADG_squarefree_primitive')
            need(gcd(divisor, target) == 1, 'ADG_adjacent_disjoint')
            arrows.append(index[target])
        need(states[arrows[index[1]]] == ambient, 'ADG_one_to_ambient')
        need(states[arrows[index[ambient]]] == 1, 'ADG_ambient_to_one')
        if ambient > 1:
            need(all(i != j for i, j in enumerate(arrows)), 'ADG_no_fixed_for_nontrivial_N')
        results.append(profile(states, arrows, 'ADG',
                               {'ambient_mask_in_fixed_prime_list': ambient_mask,
                                'primes': primes, 'N': ambient},
                               'Ascending positive integer divisors of the displayed squarefree N.'))
    return results


def antichains_incomparability(n):
    size = 1 << n
    incomparable = []
    for a in range(size):
        incomparable.append(sum(1 << b for b in range(size)
                                if a & b != a and a & b != b))
    result = []

    def visit(available, selected):
        if available == 0:
            result.append(tuple(sorted(selected)))
            return
        bit = available & -available
        a = bit.bit_length()-1
        rest = available ^ bit
        visit(rest, selected)
        visit(rest & incomparable[a], selected+(a,))

    visit((1 << size)-1, ())
    need(len(result) == len(set(result)), 'FSD_incomparability_unique')
    return sorted(result)


def antichains_ideal_frontiers(n):
    # Independently enumerate downsets in a topological order using literal
    # frozensets and predecessor constraints, then take their maximal frontiers.
    elements = [frozenset(c) for k in range(n+1) for c in combinations(range(n), k)]
    predecessors = {a: {a-{v} for v in a} for a in elements}
    result = []

    def visit(position, ideal):
        if position == len(elements):
            frontier = [a for a in ideal if not any(a < b for b in ideal)]
            result.append(tuple(sorted(sum(1 << v for v in a) for a in frontier)))
            return
        a = elements[position]
        visit(position+1, ideal)
        if predecessors[a] <= ideal:
            visit(position+1, ideal | {a})

    visit(0, set())
    need(len(result) == len(set(result)), 'FSD_ideal_frontiers_unique')
    return sorted(result)


def fsd_masks(family):
    differences = {a ^ b for a, b in combinations(family, 2)}
    return tuple(sorted(a for a in differences
                        if not any(a != b and a & b == a for b in differences)))


def fsd_literal_sets(family, n):
    old = [frozenset(i for i in range(n) if a >> i & 1) for a in family]
    differences = {a.symmetric_difference(b) for a, b in combinations(old, 2)}
    frontier = {a for a in differences if not any(a < b for b in differences)}
    return tuple(sorted(sum(1 << i for i in a) for a in frontier))


def run_fsd():
    results = []
    expected = (2, 3, 6, 20, 168, 7581)
    for n, amount in enumerate(expected):
        states = antichains_incomparability(n)
        alternative_states = antichains_ideal_frontiers(n)
        need(states == alternative_states, 'FSD_two_complete_carrier_constructions')
        need(len(states) == amount, 'FSD_expected_full_carrier_size')
        index = {c: i for i, c in enumerate(states)}
        need(() in index and (0,) in index and index[()] != index[(0,)], 'FSD_empty_conventions')
        arrows = []
        noninclusion_witness = None
        for family in states:
            need(all(a & b != a and a & b != b for a, b in combinations(family, 2)),
                 'FSD_input_antichain')
            target = fsd_masks(family)
            need(target == fsd_literal_sets(family, n), 'FSD_masks_vs_literal_sets')
            need(target in index, 'FSD_closed_antichain_carrier')
            if len(family) < 2:
                need(target == (), 'FSD_distinct_pair_boundary')
            else:
                old_union, old_intersection, new_union = 0, (1 << n)-1, 0
                for a in family:
                    old_union |= a
                    old_intersection &= a
                for a in target:
                    new_union |= a
                need(new_union == old_union ^ old_intersection, 'FSD_union_minus_intersection_shadow')
            arrows.append(index[target])
        for i, target in enumerate(arrows):
            following = arrows[target]
            if noninclusion_witness is None and not set(states[target]) <= set(states[following]):
                noninclusion_witness = [states[i], states[target], states[following]]
        report = profile(states, arrows, 'FSD', {'n': n},
                         'Lexicographically sorted tuples of ascending subset bitmasks; bit i represents i. Empty tuple is the empty family; (0,) contains the empty subset.')
        report['first_image_inclusion_counterexample_if_any'] = noninclusion_witness
        results.append(report)
    return results


def main():
    adg = run_adg()
    fsd = run_fsd()
    boxes = adg+fsd
    need(len(boxes) == 262, 'TOTAL_immutable_box_count')
    need(sum(b['state_count'] for b in adg) == 6561, 'TOTAL_ADG_state_pairs')
    need(sum(b['state_count'] for b in fsd) == 7780, 'TOTAL_FSD_state_pairs')
    result = {'status': 'PASS_FIXED_FIFTEENTH_AUTHOR_PILOT',
              'scope': 'Six desk literals, only two pilots; finite evidence, not universal theorems or review.',
              'fixed_prime_list': PRIMES, 'fixed_fsd_n': list(range(6)),
              'box_count': len(boxes), 'state_map_pairs': sum(b['state_count'] for b in boxes),
              'assertions': dict(sorted(CHECKS.items())), 'assertion_total': sum(CHECKS.values()),
              'boxes': boxes, 'external_status': 'HOLD_EXTERNAL'}
    sys.stdout.write(json.dumps(result, indent=2, sort_keys=True)+'\n')


if __name__ == '__main__':
    main()
