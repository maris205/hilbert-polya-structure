#!/usr/bin/env python3
"""Lane40's one fixed scientific pilot: all compositions for 1 <= N <= 12.

No CLI cutoffs, imports from repository science, random sampling or data files.
This is a finite falsification check of the prior all-size author proof.
"""
from collections import Counter
from functools import lru_cache
import json

N_MIN = 1
N_MAX = 12


def emit(obj):
    print(json.dumps(obj, sort_keys=True, separators=(',', ':')), flush=True)


def compositions(n):
    for mask in range(1 << (n - 1)):
        endpoints = [0] + [i for i in range(1, n) if mask & (1 << (i - 1))] + [n]
        yield tuple(endpoints[i + 1] - endpoints[i] for i in range(len(endpoints) - 1))


def direct_rule(parts):
    result = []
    mass = parts[0]
    for i in range(1, len(parts)):
        if parts[i - 1] <= parts[i]:
            mass += parts[i]
        else:
            result.append(mass)
            mass = parts[i]
    return tuple(result + [mass])


def interval_rule(parts):
    endpoints = [0]
    for mass in parts:
        endpoints.append(endpoints[-1] + mass)
    retained = [0]
    for i in range(1, len(parts)):
        if parts[i - 1] > parts[i]:
            retained.append(endpoints[i])
    retained.append(endpoints[-1])
    return tuple(retained[i + 1] - retained[i] for i in range(len(retained) - 1))


def intervals(parts):
    result = []
    pos = 0
    for mass in parts:
        result.append((pos, pos + mass))
        pos += mass
    return result


def triangular(t):
    return 1 + t * (t + 1) // 2


def depth_bound(n):
    h = 0
    while triangular(h + 1) <= n:
        h += 1
    return h


@lru_cache(None)
def endpoint_partitions(total, first, last):
    if not 1 <= first <= last <= total:
        return 0
    if first == last:
        return int(total % first == 0)
    remainder = total - first - last
    if remainder < 0:
        return 0
    coefficients = [1] + [0] * remainder
    for value in range(first, last + 1):
        for degree in range(value, remainder + 1):
            coefficients[degree] += coefficients[degree - value]
    return coefficients[remainder]


def fibre_formula(target):
    values = {
        first: sum(endpoint_partitions(target[-1], first, last)
                   for last in range(first, target[-1] + 1))
        for first in range(1, target[-1] + 1)
    }
    for total in reversed(target[:-1]):
        values = {
            first: sum(endpoint_partitions(total, first, last)
                       * sum(count for nxt, count in values.items() if nxt < last)
                       for last in range(first, total + 1))
            for first in range(1, total + 1)
        }
    return sum(values.values())


def image_threshold(target):
    threshold = 1
    for total in reversed(target[:-1]):
        if total <= threshold:
            return False
        threshold = total if total == threshold + 1 else 1
    return True


def trajectory_check(source, transition):
    seen = set()
    orbit = [source]
    current = source
    round_number = 0
    event_counts = Counter()
    while transition[current] != current:
        assert current not in seen, ('nonfixed cycle', source, current)
        seen.add(current)
        nxt = transition[current]
        round_number += 1
        old_intervals = intervals(current)
        new_intervals = set(intervals(nxt))
        new_cuts = {left for left, right in new_intervals if left != 0}
        older_intervals = set(intervals(orbit[-2])) if round_number >= 2 else None
        for i in range(len(current) - 1):
            boundary = old_intervals[i][1]
            if boundary not in new_cuts:
                assert current[i] >= round_number, ('lemma A', source, orbit, i)
                event_counts['deleted_cut_A'] += 1
                if round_number >= 2:
                    assert old_intervals[i + 1] not in older_intervals, (
                        'right block not newly formed', source, orbit, i)
                    event_counts['previous_round_right_block'] += 1
        for left, right in new_intervals - set(old_intervals):
            assert right - left >= triangular(round_number), (
                'lemma B', source, orbit, (left, right))
            event_counts['new_block_B'] += 1
        assert len(nxt) < len(current), ('nonfixed no contraction', source)
        orbit.append(nxt)
        current = nxt
    return round_number, current, orbit, event_counts


def main():
    emit({'type': 'contract', 'map': 'sum_maximal_weakly_increasing_old_runs',
          'carrier': 'positive_compositions_fixed_total',
          'N_min': N_MIN, 'N_max': N_MAX, 'expected_total_states': 4095,
          'role': 'one_fixed_pilot_not_proof_or_independent_review'})
    total_states = 0
    total_events = Counter()
    for n in range(N_MIN, N_MAX + 1):
        states = list(compositions(n))
        assert len(states) == len(set(states)) == 1 << (n - 1)
        carrier = set(states)
        transition = {state: direct_rule(state) for state in states}
        for state, nxt in transition.items():
            assert nxt == interval_rule(state), ('literal disagreement', state)
            assert nxt in carrier and sum(nxt) == n, ('closedness', state, nxt)
        fibres = Counter(transition.values())
        tails = Counter()
        fixed = []
        max_states = []
        bound = depth_bound(n)
        for state in states:
            tau, terminal, orbit, events = trajectory_check(state, transition)
            total_events.update(events)
            strict = all(state[i] > state[i + 1] for i in range(len(state) - 1))
            assert (transition[state] == state) == strict, ('fixed locus', state)
            assert tau <= bound, ('clock bound', state, tau, bound)
            actual_fibre = fibres[state]
            predicted_fibre = fibre_formula(state)
            assert predicted_fibre == actual_fibre, (
                'fibre formula', state, actual_fibre, predicted_fibre)
            image = image_threshold(state)
            assert image == (actual_fibre > 0), ('image threshold', state, image)
            tails[tau] += 1
            if tau == 0:
                fixed.append(state)
            if tau == bound:
                max_states.append(state)
            emit({'type': 'state', 'N': n, 'state': state, 'next': transition[state],
                  'tail': tau, 'terminal': terminal, 'orbit': orbit,
                  'fibre': actual_fibre, 'fibre_formula': predicted_fibre,
                  'image_threshold': image})
        assert max(tails) == bound
        if bound == 0:
            witness = (1,)
        else:
            surplus = n - triangular(bound)
            witness = tuple(range(bound, 0, -1)) + (1 + surplus,)
        witness_tau, terminal, witness_orbit, events = trajectory_check(witness, transition)
        assert sum(witness) == n and witness_tau == bound
        maximum_fibre = max(fibres.values())
        emit({'type': 'summary', 'N': n, 'states': len(states), 'image': len(fibres),
              'fixed': len(fixed), 'max_tail': max(tails), 'bound': bound,
              'tail_histogram': dict(sorted(tails.items())),
              'max_tail_states': len(max_states), 'max_fibre': maximum_fibre,
              'max_fibre_targets': [list(x) for x in states if fibres[x] == maximum_fibre],
              'witness': witness, 'witness_orbit': witness_orbit})
        total_states += len(states)
    assert total_states == 4095
    emit({'type': 'completion', 'status': 'PASS', 'total_states': total_states,
          'N_min': N_MIN, 'N_max': N_MAX, 'event_checks': dict(total_events),
          'endpoint_partition_cache_entries': endpoint_partitions.cache_info().currsize})


if __name__ == '__main__':
    main()
