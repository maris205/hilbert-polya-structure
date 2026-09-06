#!/usr/bin/env python3
"""Three fixed, complete thirteenth-lane pilots; no input reads or imports of old code."""
from collections import Counter
from functools import lru_cache
from hashlib import sha256
from itertools import permutations
import json
import sys

CHECKS = Counter()


def need(condition, section):
    CHECKS[section] += 1
    if not condition:
        raise AssertionError(section)


def digest(value):
    return sha256(json.dumps(value, separators=(',', ':')).encode('ascii')).hexdigest()


def partitions(total, limit=None):
    if total == 0:
        yield ()
        return
    if limit is None:
        limit = total
    for first in range(min(total, limit), 0, -1):
        for rest in partitions(total-first, first):
            yield (first,)+rest


def conjugate(part):
    return tuple(sum(row >= column for row in part) for column in range(1, max(part, default=0)+1))


def hmp(part):
    trans = conjugate(part)
    counts = Counter(part[i]-j+trans[j]-i-1 for i in range(len(part)) for j in range(part[i]))
    return tuple(sorted(counts.values(), reverse=True))


def hmp_direct(part):
    cells = {(i, j) for i, length in enumerate(part) for j in range(length)}
    counts = Counter()
    for i, j in cells:
        hook = 1+sum(x == i and y > j for x, y in cells)+sum(x > i and y == j for x, y in cells)
        counts[hook] += 1
    return tuple(sorted(counts.values(), reverse=True))


def compose(left, right):
    return tuple(left[right[i]] for i in range(len(left)))


def inverse(perm):
    result = [0]*len(perm)
    for i, value in enumerate(perm):
        result[value] = i
    return tuple(result)


def shift_cycle(n):
    return tuple((i+1) % n for i in range(n))


def ssc(perm):
    cycle = shift_cycle(len(perm))
    shifted = compose(compose(cycle, perm), inverse(cycle))
    return compose(compose(compose(perm, shifted), inverse(perm)), inverse(shifted))


def ssc_direct(perm):
    cycle = shift_cycle(len(perm))
    back, inv = inverse(cycle), inverse(perm)
    result = []
    for i in range(len(perm)):
        point = i
        for action in (back, inv, cycle, inv, back, perm, cycle, perm):
            point = action[point]
        result.append(point)
    return tuple(result)


def all_matchings(rows, columns):
    result = []

    def visit(row, used, mask, size):
        if row == rows:
            result.append((mask, size))
            return
        visit(row+1, used, mask, size)
        for column in range(columns):
            if not used >> column & 1:
                visit(row+1, used | 1 << column, mask | 1 << (row*columns+column), size+1)

    visit(0, 0, 0, 0)
    need(len(result) == len({mask for mask, size in result}), 'AMC_unique_ambient_matchings')
    return result


def allowed_exhaustive(mask, matchings):
    rank, allowed = -1, 0
    for matching, size in matchings:
        if matching & mask == matching:
            if size > rank:
                rank, allowed = size, matching
            elif size == rank:
                allowed |= matching
    return rank, allowed


def allowed_dynamic(mask, rows, columns):
    @lru_cache(None)
    def suffix(row, used):
        if row == rows:
            return 0, 0
        best, support = suffix(row+1, used)
        for column in range(columns):
            bit = 1 << (row*columns+column)
            if not used >> column & 1 and mask & bit:
                size, tail = suffix(row+1, used | 1 << column)
                size += 1
                tail |= bit
                if size > best:
                    best, support = size, tail
                elif size == best:
                    support |= tail
        return best, support

    return suffix(0, 0)


def profile(states, arrows, rule, parameters, encoding):
    size = len(states)
    need(size > 0 and len(arrows) == size, rule+'_complete_map')
    need(all(isinstance(target, int) and 0 <= target < size for target in arrows), rule+'_carrier')
    indegrees = [0]*size
    for target in arrows:
        indegrees[target] += 1
    depth, periods = [-1]*size, [0]*size
    cycles = []
    for start in range(size):
        if depth[start] >= 0:
            continue
        path, positions = [], {}
        current = start
        while depth[current] < 0 and current not in positions:
            positions[current] = len(path)
            path.append(current)
            current = arrows[current]
        if current in positions:
            cycle = path[positions[current]:]
            pivot = cycle.index(min(cycle))
            cycle = cycle[pivot:]+cycle[:pivot]
            cycles.append(cycle)
            for node in cycle:
                depth[node], periods[node] = 0, len(cycle)
        for node in reversed(path):
            if depth[node] < 0:
                depth[node] = depth[arrows[node]]+1
                periods[node] = periods[arrows[node]]
    cycles.sort()
    cycle_counts = Counter(map(len, cycles))
    fibre_counts = Counter(indegrees)
    need(sum(indegrees) == size, rule+'_all_sources_conserved')
    need(sum(fibre_counts.values()) == size, rule+'_all_targets_conserved')
    need(sum(count*amount for count, amount in fibre_counts.items()) == size, rule+'_fibre_weight')
    need(sum(map(len, cycles)) == depth.count(0), rule+'_core_count')
    for source, target in enumerate(arrows):
        need(periods[source] == periods[target], rule+'_period_propagation')
        need(depth[source] == 0 and depth[target] == 0 or depth[source] == depth[target]+1,
             rule+'_depth_propagation')
    for cycle in cycles:
        need(all(arrows[node] == cycle[(i+1) % len(cycle)] for i, node in enumerate(cycle)), rule+'_cycle_edges')
    height = max(depth)
    deepest = min(i for i, value in enumerate(depth) if value == height)
    tail_path = [deepest]
    for _ in range(height):
        tail_path.append(arrows[tail_path[-1]])
    longest = min((cycle for cycle in cycles if len(cycle) == max(cycle_counts)), key=tuple)
    maximum = max(indegrees)
    maximizers = [i for i, count in enumerate(indegrees) if count == maximum]
    result = {'rule': rule, 'parameters': parameters, 'state_count': size,
              'state_index_encoding': encoding, 'image_size': size-indegrees.count(0),
              'recurrent_states': depth.count(0), 'cycles_by_length': dict(sorted(cycle_counts.items())),
              'height': height, 'depth_histogram': dict(sorted(Counter(depth).items())),
              'target_fibre_histogram_including_zero': dict(sorted(fibre_counts.items())),
              'maximum_fibre': maximum, 'all_maximum_fibre_target_indices': maximizers,
              'first_maximum_target': states[maximizers[0]],
              'first_maximum_target_all_source_indices': [i for i, target in enumerate(arrows) if target == maximizers[0]],
              'longest_cycle_indices': longest, 'longest_cycle_states': [states[i] for i in longest],
              'maximum_tail_indices': tail_path, 'maximum_tail_states': [states[i] for i in tail_path],
              'all_forward_target_indices': arrows, 'all_target_fibre_sizes': indegrees,
              'ordered_transition_sha256': digest(arrows), 'ordered_fibre_sha256': digest(indegrees)}
    if rule != 'AMC':
        result['complete_carrier_in_index_order'] = states
    return result, depth, periods


def run_hmp():
    results = []
    for mass in range(21):
        states = list(partitions(mass))
        index = {part: i for i, part in enumerate(states)}
        need(len(index) == len(states), 'HMP_unique_partitions')
        arrows = []
        for part in states:
            target = hmp(part)
            need(target == hmp_direct(part), 'HMP_direct_hook_arm_leg_agreement')
            need(sum(target) == mass and target in index, 'HMP_mass_and_partition_carrier')
            need(target == hmp(conjugate(part)), 'HMP_transpose_invariance')
            for k in range(1, mass+1):
                need(sum(target[:k]) <= sum(part[:k]), 'HMP_full_dominance')
                need(sum(target[:k]) <= sum(conjugate(part)[:k]), 'HMP_transposed_dominance')
            potential = sum((i+1)*value for i, value in enumerate(part))
            next_potential = sum((i+1)*value for i, value in enumerate(target))
            need(target == part or next_potential > potential, 'HMP_strict_potential_if_changed')
            arrows.append(index[target])
        result, depth, periods = profile(states, arrows, 'HMP', {'N': mass}, 'Descending lexicographic positive-part tuples; empty at N=0.')
        need(all(period == 1 for period in periods), 'HMP_generic_fixed_recurrence')
        need(max(depth) <= mass*(mass-1)//2, 'HMP_generic_potential_bound')
        results.append(result)
    need(sum(row['state_count'] for row in results) == 2714, 'HMP_declared_complete_total')
    return results


def run_ssc():
    results = []
    for n in range(8):
        states = list(permutations(range(n)))
        index = {perm: i for i, perm in enumerate(states)}
        arrows = []
        cycle = shift_cycle(n)
        for perm in states:
            target = ssc(perm)
            need(target == ssc_direct(perm), 'SSC_pointwise_word_agreement')
            need(target in index, 'SSC_permutation_carrier')
            inversions = sum(target[i] > target[j] for i in range(n) for j in range(i+1, n))
            need(inversions % 2 == 0, 'SSC_even_output')
            arrows.append(index[target])
        for i, perm in enumerate(states):
            shifted = compose(compose(cycle, perm), inverse(cycle))
            shifted_target = compose(compose(cycle, states[arrows[i]]), inverse(cycle))
            need(arrows[index[shifted]] == index[shifted_target], 'SSC_cyclic_conjugation_equivariance')
        result, depth, periods = profile(states, arrows, 'SSC', {'n': n}, 'Lexicographic permutations of range(n), rightmost composition first.')
        if n <= 4:
            bound = max(0, n-1)
            need(max(depth) <= bound and all(period == 1 for period in periods), 'SSC_small_solvable_derived_series_bound')
        results.append(result)
    need(sum(row['state_count'] for row in results) == 5914, 'SSC_declared_complete_total')
    return results


def run_amc():
    results = []
    for rows in range(5):
        for columns in range(rows, 5):
            cells = rows*columns
            whole = (1 << cells)-1
            states = list(range(whole+1))
            matchings = all_matchings(rows, columns)
            ranks, allowed = [], []
            for mask in states:
                rank, support = allowed_exhaustive(mask, matchings)
                need((rank, support) == allowed_dynamic(mask, rows, columns), 'AMC_full_literal_DP_agreement')
                need(0 <= rank <= min(rows, columns) and support & mask == support, 'AMC_allowed_support_and_rank')
                ranks.append(rank)
                allowed.append(support)
            arrows = [whole ^ support for support in allowed]
            for mask in states:
                need(allowed[allowed[mask]] == allowed[mask], 'AMC_deducted_allowed_core_retraction')
                two = arrows[arrows[mask]]
                need(allowed[mask] & two == allowed[mask], 'AMC_generic_two_step_inclusion')
                need(ranks[two] >= ranks[mask], 'AMC_generic_parity_rank_monotonicity')
                if ranks[two] == ranks[mask]:
                    need(allowed[mask] & allowed[two] == allowed[mask], 'AMC_generic_equal_rank_support_inclusion')
            result, depth, periods = profile(states, arrows, 'AMC', {'rows': rows, 'columns': columns},
                                             'Integer mask; cell (i,j) is bit i*columns+j, low bit first.')
            need(all(period <= 2 for period in periods), 'AMC_generic_period_at_most_two')
            need(max(depth) <= 2*(min(rows, columns)*(cells+1)+cells)+1, 'AMC_generic_rank_support_bound')
            result['all_maximum_matching_ranks'] = ranks
            result['all_allowed_support_masks'] = allowed
            result['ambient_matching_count'] = len(matchings)
            results.append(result)
    need(len(results) == 15 and sum(row['state_count'] for row in results) == 70515, 'AMC_declared_complete_total')
    return results


def main():
    need(sys.flags.isolated == 1 and sys.flags.optimize == 0 and sys.flags.dont_write_bytecode == 1,
         'isolated_nonoptimized_no_bytecode_runtime')
    hmp_results = run_hmp()
    ssc_results = run_ssc()
    amc_results = run_amc()
    rows = hmp_results+ssc_results+amc_results
    need(len(rows) == 44 and sum(row['state_count'] for row in rows) == 79143, 'all_declared_box_and_state_totals')
    print(json.dumps({'status': 'PASS_FIXED_THIRTEENTH_AUTHOR_PILOT',
                      'kind': 'Complete bounded author enumeration; not an admission, independent review or all-size proof.',
                      'executed_rules': ['HMP', 'SSC', 'AMC'], 'desk_only_rules_not_executed': ['FBT', 'CSP', 'EIM'],
                      'boxes': rows, 'box_count': len(rows), 'state_map_pairs': sum(row['state_count'] for row in rows),
                      'assertions': sum(CHECKS.values()), 'assertions_by_section': dict(sorted(CHECKS.items())),
                      'imports_of_historical_or_other_producer_code': False, 'input_file_reads': 0,
                      'randomness': False, 'integer_only': True,
                      'serialization': 'json.dumps indent=2 sort_keys=True, ASCII default, one final LF; inner array hashes use compact separators.',
                      'all_parameter_exclusions': ['No sharp HMP clock or complete fixed-language/inverse classification.',
                                                   'No all-S_n SSC temporal atlas or full fibre evaluation.',
                                                   'No matching-specific sharp AMC clock or evaluated inverse extrema.',
                                                   'No extrapolation, paper ID, reserve, external clearance or batch completion.'],
                      'external_status': 'HOLD_EXTERNAL'}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
