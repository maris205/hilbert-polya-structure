#!/usr/bin/env python3
"""Disabled saved-output receiver; never imports the scientific producer.

Preparation is source-only. Only a separate exact approved root binding may
enable later reading of saved stdout and semantic reconstruction. This author
checker is not an independent manuscript review or an admission authority.
"""
from fractions import Fraction
from hashlib import sha256
import json
import os
from pathlib import Path
import sys

BOXES = ((1, 1), (2, 16), (3, 243), (4, 4096))
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
PARAMETERS = {
    'schema_version': 'finite-pointer-parameters-v1',
    'role': 'single-bounded-author-pilot', 'label_convention': 'one_based',
    'state_order': 'lexicographic_(u,v,f(1),...,f(n))',
    'boxes': [{'n': n, 'state_count': count} for n, count in BOXES],
    'box_count': 4, 'total_state_count': 4356, 'allow_box_extension': False,
}
PRODUCER_PIN = {'sha256': '9b3c22ad86b36f5dece45d47de03d3cc309f05c46c40a152aec49dc8a0262cbb', 'bytes': 27518}
PARAMETER_PIN = {'sha256': 'f71aff49cb7b4fda75851992a85ce3150cd8f69f1dd5a4512bb6e7b3afe08a16', 'bytes': 415}
COMPARED = 0


def need(test, description):
    if not test:
        raise AssertionError(description)


def compact(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=True, allow_nan=False)


def same(path, actual, expected):
    """Canonical typed equality rejects bool/int and float/int substitutions."""
    global COMPARED
    COMPARED += 1
    left, right = compact(actual), compact(expected)
    need(left == right, path + ': saved/reconstructed mismatch; saved_sha256=' +
         sha256(left.encode()).hexdigest() + '; reconstructed_sha256=' + sha256(right.encode()).hexdigest())


def keys(path, value, names):
    need(type(value) is dict, path + ': object required')
    same(path + '.keys', sorted(value), sorted(names))


def pairs(items):
    result = {}
    for key, value in items:
        need(key not in result, 'duplicate JSON object key: ' + key)
        result[key] = value
    return result


def forbidden_number(value):
    raise ValueError('floating/nonfinite JSON number forbidden: ' + value)


def parse(raw):
    return json.loads(raw.decode('ascii'), object_pairs_hook=pairs,
                      parse_float=forbidden_number, parse_constant=forbidden_number)


def integer(value, label, minimum=0):
    need(type(value) is int and value >= minimum, label + ': strict integer required')


def ratio(value):
    value = Fraction(value)
    return {'numerator': value.numerator, 'denominator': value.denominator}


def count_value(value):
    value = Fraction(value)
    return value.numerator if value.denominator == 1 else ratio(value)


def coefficient_rows(values):
    return [{'s': s, 'p': p, 'coefficient': ratio(c)} for (s, p), c in sorted(values.items()) if c]


def count_rows(values, joint=False):
    if joint:
        return [{'s': s, 'p': p, 'count': count_value(c)} for (s, p), c in sorted(values.items()) if c]
    return [{'p': p, 'count': count_value(c)} for p, c in sorted(values.items()) if c]


def add_check(records, identifier, observed, expected):
    records.append({'id': identifier, 'observed': observed, 'expected': expected,
                    'pass': observed == expected})


def decode(identifier, n):
    """Fixed-width base-n decoding gives the declared lexical Cartesian order."""
    digits = [1] * (n + 2)
    for position in range(n + 1, -1, -1):
        identifier, digit = divmod(identifier, n)
        digits[position] = digit + 1
    need(identifier == 0, 'state id outside exact carrier')
    return digits


def encode(digits, n):
    value = 0
    for digit in digits:
        need(type(digit) is int and 1 <= digit <= n, 'literal output outside carrier')
        value = n * value + digit - 1
    return value


def successor(state):
    u, v = state[:2]
    result = [v, state[v + 1]] + state[2:]
    result[v + 1] = u
    return result


def inverse(state):
    a, b = state[:2]
    result = [state[a + 1], a] + state[2:]
    result[a + 1] = b
    return result


def cycles_from_permutation(successors, predecessors):
    """Check all indegrees first, then follow unused IDs; no period/core input."""
    need(all(len(row) == 1 for row in predecessors), 'direct literal graph is not a permutation')
    unused = set(range(len(successors)))
    cycles, orbit_of, positions = [], [None] * len(successors), [None] * len(successors)
    while unused:
        start = min(unused)
        cycle, cursor = [], start
        while True:
            need(cursor in unused, 'direct graph joined an earlier cycle or repeated off-anchor')
            unused.remove(cursor)
            orbit_of[cursor], positions[cursor] = len(cycles), len(cycle)
            cycle.append(cursor)
            cursor = successors[cursor]
            if cursor == start:
                break
        cycles.append(cycle)
    return cycles, orbit_of, positions


def geometry(state):
    """Integer adjacency matrix, component flood and single-leaf deletion.

    Temporary occurrence IDs are introduced only after the labelled core is
    fixed, solely to check the saved canonical chain representation.
    """
    n = len(state) - 2
    matrix = [[0] * (n + 1) for _ in range(n + 1)]
    multiplicities = {}
    for a, b in [(state[0], state[1])] + [(v, state[v + 1]) for v in range(1, n + 1)]:
        pair = (min(a, b), max(a, b))
        multiplicities[pair] = multiplicities.get(pair, 0) + 1
        matrix[a][b] += 1
        matrix[b][a] += 1
    rows = [[a, b, m] for (a, b), m in sorted(multiplicities.items())]
    active, frontier = set(), {state[0]}
    while frontier:
        vertex = min(frontier)
        frontier.remove(vertex)
        active.add(vertex)
        frontier.update(v for v in range(1, n + 1) if matrix[vertex][v] and v not in active)
    live = set(active)
    while True:
        leaves = [v for v in live if sum(matrix[v][w] for w in live) < 2]
        if not leaves:
            break
        live.remove(min(leaves))
    vertices = sorted(live)
    degrees = {v: sum(matrix[v][w] for w in live) for v in live}
    edge_rows = [row for row in rows if row[0] in live and row[1] in live]
    expanded = [(a, b) for a, b, m in rows for _ in range(m)]
    remaining = {i for i, (a, b) in enumerate(expanded) if a in live and b in live}
    edge_count = len(remaining)
    branches = sorted(v for v in live if degrees[v] > 2)
    need(edge_count == len(live) + 1 and all(degrees[v] >= 2 for v in live), 'invalid reconstructed core excess/degrees')
    need((len(branches) == 1 and degrees[branches[0]] == 4) or
         (len(branches) == 2 and all(degrees[v] == 3 for v in branches)), 'invalid reconstructed branches')
    incident = {v: {i for i in remaining if v in expanded[i]} for v in live}
    chains = []
    while remaining:
        candidates = [(v, i) for v in branches for i in incident[v] & remaining]
        need(bool(candidates), 'core occurrence not attached to a branch chain')
        start, edge = min(candidates)
        walk, used, current = [start], [], start
        while True:
            need(edge in remaining, 'reused core occurrence in chain')
            remaining.remove(edge)
            used.append(edge)
            a, b = expanded[edge]
            need(current == a or current == b, 'chain incidence')
            current = b if current == a else a
            walk.append(current)
            if current in branches:
                break
            choices = incident[current] - {edge}
            need(len(choices) == 1, 'internal chain not forced')
            edge = min(choices)
        if tuple(reversed(walk)) < tuple(walk):
            walk.reverse()
            used.reverse()
        chains.append({'vertices': walk, 'edge_ids': used, 'length': len(used)})
    chains.sort(key=lambda row: (row['vertices'], row['edge_ids']))
    loops = [row for row in chains if row['vertices'][0] == row['vertices'][-1]]
    joins = [row for row in chains if row['vertices'][0] != row['vertices'][-1]]
    if len(branches) == 1:
        need(len(loops) == 2 and not joins, 'figure-eight chain census')
        a, b = sorted(row['length'] for row in loops)
        kind, parameters = 'figure_eight', {'a': a, 'b': b}
        predicted = 1 if a == b == 1 else (a + b) * (1 if b <= 2 else 2)
        multiplicity = 1 + int(a >= 3)
    elif len(joins) == 3:
        need(not loops, 'theta closed chain')
        a, b, c = sorted(row['length'] for row in joins)
        kind, parameters = 'theta', {'a': a, 'b': b, 'c': c}
        predicted = 2 if c == 1 else 2 * (a + b + c)
        multiplicity = 1 if b == 1 else 2
    else:
        need(len(loops) == 2 and len(joins) == 1, 'barbell chain census')
        length_at = {row['vertices'][0]: row['length'] for row in loops}
        need(set(length_at) == set(branches), 'barbell cycles must occupy separate branches')
        a, b, c = length_at[branches[0]], length_at[branches[1]], joins[0]['length']
        kind, parameters = 'barbell', {'a': a, 'b': b, 'c': c}
        predicted = (a + b + 2 * c) * (1 if max(a, b) <= 2 else 2)
        multiplicity = 1 + int(min(a, b) >= 3)
    key_object = {'vertices': vertices, 'edges': edge_rows}
    frozen = [[v, state[v + 1]] for v in range(1, n + 1) if v not in live]
    core = {**key_object, 'edge_count': edge_count,
            'degrees': [[v, degrees[v]] for v in vertices], 'kind': kind,
            'parameters': parameters, 'branches': branches, 'chains': chains,
            'predicted_period': predicted, 'predicted_orbit_count': multiplicity, 'error': None}
    return {'graph_multiset': rows, 'active_component': sorted(active),
            'attached_tree_vertices': sorted(active - live),
            'inactive_vertices': sorted(set(range(1, n + 1)) - active), 'core': core,
            'frozen_arrows': frozen, 'core_key': compact(key_object),
            'group_key': compact({'core': key_object, 'frozen_arrows': frozen})}


def length_sum_coefficients():
    """Independent coefficient implementation, not producer polynomial helpers.

    Sum the reviewed ordered length weights at s<=4. Theta uses positive
    internal-list compositions and the reviewed k! / orbit multiplicities.
    No empirical graph, saved coefficient, or period cap is consumed.
    """
    pieces = {name: {} for name in ('figure_eight', 'barbell', 'theta')}
    def put(kind, s, p, value):
        key = (s, p)
        pieces[kind][key] = pieces[kind].get(key, Fraction(0)) + Fraction(value)
    for s in range(1, 5):
        for a in range(1, s + 1):
            b = s + 1 - a
            if a == b == 1:
                put('figure_eight', s, 1, 1)
            else:
                short = max(a, b) <= 2
                put('figure_eight', s, (a + b) * (1 if short else 2), Fraction(1, 2 if short else 4))
        for a in range(1, s + 1):
            for b in range(1, s + 1):
                c = s + 1 - a - b
                if c >= 1:
                    short = max(a, b) <= 2
                    put('barbell', s, (a + b + 2 * c) * (1 if short else 2), Fraction(1, 2 if short else 4))
        if s == 2:
            put('theta', s, 2, Fraction(1, 2))
        r = s - 2
        if r >= 1:
            # Q, Q^2 and Q^3/3, with Q=x/(1-x), times the branch factor 1/2.
            value = Fraction(1, 2)
            if r >= 2:
                value += Fraction(r - 1, 2)
            if r >= 3:
                value += Fraction((r - 1) * (r - 2), 12)
            put('theta', s, 2 * (s + 1), value)
    total = {}
    for piece in pieces.values():
        for key, value in piece.items():
            total[key] = total.get(key, Fraction(0)) + value
    return pieces, total


def total_coefficient(s):
    return Fraction(1) if s == 1 else Fraction(2) if s == 2 else Fraction(5 * s * s + s + 24, 24)


def extension_multiplier(n, s):
    result = n ** (n - s)
    for value in range(n - s + 1, n + 1):
        result *= value
    return result


def period_set(n):
    return [1] if n == 1 else list(range(1, 2 * n + 1)) + list(range(2 * n + 2, 4 * n - 3, 2))


def inspect_box(saved, n, count, series):
    prefix = 'n' + str(n)
    checks = []
    states = [decode(i, n) for i in range(count)]
    next_ids = [encode(successor(state), n) for state in states]
    predecessors = [[] for _ in states]
    for i, target in enumerate(next_ids):
        predecessors[target].append(i)
    cycles, orbit_of, positions = cycles_from_permutation(next_ids, predecessors)
    shapes = [geometry(state) for state in states]
    group_keys = sorted({row['group_key'] for row in shapes})
    core_keys = sorted({row['core_key'] for row in shapes})
    group_id = {key: i for i, key in enumerate(group_keys)}
    core_id = {key: i for i, key in enumerate(core_keys)}
    need(type(saved) is dict and type(saved.get('states')) is list and len(saved['states']) == count,
         prefix + ': complete saved state array required')
    group_members = {key: [] for key in group_keys}
    for i, state in enumerate(states):
        info = shapes[i]
        period = len(cycles[orbit_of[i]])
        wanted = {'id': i, 'u': state[0], 'v': state[1], 'f': state[2:],
                  'next': next_ids[i], 'predecessors': predecessors[i],
                  'inverse_formula_state_id': encode(inverse(state), n),
                  'orbit_id': orbit_of[i], 'orbit_position': positions[i], 'preperiod': 0,
                  'observed_period': period, 'core_id': core_id[info['core_key']],
                  'group_id': group_id[info['group_key']], **info}
        same(prefix + '.states[' + str(i) + ']', saved['states'][i], wanted)
        group_members[info['group_key']].append(i)
        root = prefix + '.state' + str(i)
        add_check(checks, root + '.S01_successor_closed', 0 <= next_ids[i] < count, True)
        add_check(checks, root + '.S02_inverse_forward', successor(inverse(state)), state)
        add_check(checks, root + '.S03_inverse_backward', inverse(successor(state)), state)
        add_check(checks, root + '.S04_indegree', len(predecessors[i]), 1)
        add_check(checks, root + '.S05_preperiod', 0, 0)
        following = shapes[next_ids[i]]
        add_check(checks, root + '.S06_multiset_invariant', following['graph_multiset'], info['graph_multiset'])
        add_check(checks, root + '.S07_core_frozen_invariant', following['group_key'], info['group_key'])
        live = set(info['core']['vertices'])
        add_check(checks, root + '.S08_core_closed', state[0] in live and state[1] in live and
                  all(state[v + 1] in live for v in live), True)
        add_check(checks, root + '.S09_core_valid', info['core']['kind'] in ('figure_eight', 'barbell', 'theta'), True)
        add_check(checks, root + '.S10_period', period, info['core']['predicted_period'])
    orbit_records, period_counts, joint_counts = [], {}, {}
    for i, cycle in enumerate(cycles):
        group_ids = sorted({group_id[shapes[v]['group_key']] for v in cycle})
        core_sizes = sorted({len(shapes[v]['core']['vertices']) for v in cycle})
        period = len(cycle)
        orbit_records.append({'id': i, 'states': cycle, 'period': period,
                              'group_ids': group_ids, 'core_sizes': core_sizes})
        period_counts[period] = period_counts.get(period, 0) + 1
        key = (len(shapes[cycle[0]]['core']['vertices']), period)
        joint_counts[key] = joint_counts.get(key, 0) + 1
        root = prefix + '.orbit' + str(i)
        add_check(checks, root + '.O01_edges', [next_ids[v] for v in cycle], cycle[1:] + cycle[:1])
        add_check(checks, root + '.O02_unique_members', len(set(cycle)), period)
        add_check(checks, root + '.O03_one_group', len(group_ids), 1)
    groups = []
    for key in group_keys:
        members = group_members[key]
        info = shapes[members[0]]
        orbit_ids = sorted({orbit_of[v] for v in members})
        periods = sorted({len(cycles[i]) for i in orbit_ids})
        predicted, multiplicity = info['core']['predicted_period'], info['core']['predicted_orbit_count']
        gid = group_id[key]
        groups.append({'id': gid, 'key': key, 'core_id': core_id[info['core_key']],
                       'core': info['core'], 'frozen_arrows': info['frozen_arrows'],
                       'state_ids': members, 'orbit_ids': orbit_ids, 'observed_periods': periods,
                       'predicted_period': predicted, 'observed_orbit_count': len(orbit_ids),
                       'predicted_orbit_count': multiplicity})
        root = prefix + '.group' + str(gid)
        add_check(checks, root + '.G01_orbit_count', len(orbit_ids), multiplicity)
        add_check(checks, root + '.G02_periods', periods, [predicted])
        add_check(checks, root + '.G03_exact_cover', sorted(v for i in orbit_ids for v in cycles[i]), members)
    catalog = []
    for key in core_keys:
        info = next(row for row in shapes if row['core_key'] == key)
        cid = core_id[key]
        catalog.append({'id': cid, 'key': key, 'core': info['core'],
                        'group_ids': [row['id'] for row in groups if row['core_id'] == cid]})
    expected_joint, expected_period, extension_terms = {}, {}, []
    for (s, p), coefficient in sorted(series.items()):
        if s > n:
            continue
        multiplier = extension_multiplier(n, s)
        contribution = coefficient * multiplier
        expected_joint[(s, p)] = contribution
        expected_period[p] = expected_period.get(p, Fraction(0)) + contribution
        extension_terms.append({'s': s, 'p': p, 'core_coefficient': ratio(coefficient),
                                'label_and_frozen_multiplier': multiplier, 'contribution': ratio(contribution)})
        add_check(checks, prefix + '.E01_integral_s' + str(s) + '_p' + str(p), contribution.denominator, 1)
    total_terms, expected_total = [], Fraction(0)
    for s in range(1, n + 1):
        coefficient, multiplier = total_coefficient(s), extension_multiplier(n, s)
        contribution = coefficient * multiplier
        total_terms.append({'s': s, 'coefficient': ratio(coefficient), 'multiplier': multiplier,
                            'contribution': ratio(contribution)})
        expected_total += contribution
    periods, maximum = sorted(period_counts), max(period_counts)
    tests = [
        ('B01_carrier_count', len(states), count), ('B02_cardinality_formula', len(states), n ** (n + 2)),
        ('B03_edge_count', len(next_ids), count),
        ('B04_cycle_cover', sorted(v for cycle in cycles for v in cycle), list(range(count))),
        ('B05_period_set', periods, period_set(n)), ('B06_maximum_period', maximum, 1 if n == 1 else 4 * n - 4),
        ('B07_period_egf', count_rows(period_counts), count_rows(expected_period)),
        ('B08_core_period_egf', count_rows(joint_counts, True), count_rows(expected_joint, True)),
        ('B09_total_orbits', len(cycles), count_value(expected_total)),
        ('B10_fixed_states', sum(i == target for i, target in enumerate(next_ids)), n ** n),
        ('B11_weighted_cycle_cover', sum(p * c for p, c in period_counts.items()), count),
    ]
    for suffix, observed, expected in tests:
        add_check(checks, prefix + '.' + suffix, observed, expected)
    fields = {'n': n, 'declared_state_count': count, 'state_count': count,
              'edges': [[i, target] for i, target in enumerate(next_ids)], 'orbits': orbit_records,
              'groups': groups, 'core_catalog': catalog, 'observed_periods': periods,
              'expected_periods': period_set(n), 'observed_maximum_period': maximum,
              'expected_maximum_period': 1 if n == 1 else 4 * n - 4,
              'observed_period_orbit_counts': count_rows(period_counts),
              'expected_period_orbit_counts': count_rows(expected_period),
              'observed_core_period_orbit_counts': count_rows(joint_counts, True),
              'expected_core_period_orbit_counts': count_rows(expected_joint, True),
              'egf_extension_terms': extension_terms, 'total_orbit_formula_terms': total_terms,
              'observed_total_orbits': len(cycles), 'expected_total_orbits': count_value(expected_total),
              'checks': checks}
    keys(prefix, saved, set(fields) | {'states'})
    for key, wanted in fields.items():
        same(prefix + '.' + key, saved[key], wanted)
    return checks, {'n': n, 'states': count, 'edges': count, 'orbits': len(cycles),
                    'groups': len(groups), 'labelled_cores': len(catalog), 'saved_checks': len(checks)}


def inspect_report(report):
    keys('report', report, ('schema_version', 'role', 'parameters', 'coefficient_arithmetic',
                          'core_series', 'boxes', 'checks', 'summary'))
    same('report.schema_version', report['schema_version'], 'finite-pointer-pilot-output-v1')
    same('report.role', report['role'], 'bounded-author-evidence-not-admission')
    same('report.parameters', report['parameters'], PARAMETERS)
    same('report.coefficient_arithmetic', report['coefficient_arithmetic'],
         'fractions.Fraction; t-degree <= 4; q-degree uncapped')
    pieces, series = length_sum_coefficients()
    same('report.core_series', report['core_series'], {
        'pieces': {name: coefficient_rows(piece) for name, piece in sorted(pieces.items())},
        'total': coefficient_rows(series)})
    need(type(report['boxes']) is list and len(report['boxes']) == 4, 'exact_four_saved_boxes')
    global_checks = []
    for (s, p), coefficient in sorted(series.items()):
        add_check(global_checks, 'series.C01_nonnegative_s' + str(s) + '_p' + str(p), coefficient >= 0, True)
    for s in range(1, 5):
        ordinary = sum(c for (size, _), c in series.items() if size == s)
        weighted = sum(p * c for (size, p), c in series.items() if size == s)
        add_check(global_checks, 'series.C02_total_s' + str(s), ratio(ordinary), ratio(total_coefficient(s)))
        add_check(global_checks, 'series.C03_state_weight_s' + str(s), ratio(weighted), ratio(Fraction(s * s * (s + 1), 2)))
    box_checks, summaries = [], []
    for saved, (n, count) in zip(report['boxes'], BOXES):
        records, summary = inspect_box(saved, n, count, series)
        box_checks.extend(records)
        summaries.append(summary)
    add_check(global_checks, 'global.T01_four_boxes', [row['n'] for row in summaries], [1, 2, 3, 4])
    add_check(global_checks, 'global.T02_total_states', sum(row['states'] for row in summaries), 4356)
    identifiers = [row['id'] for row in global_checks + box_checks]
    final_id = 'global.T03_unique_check_ids'
    add_check(global_checks, final_id, len(set(identifiers + [final_id])), len(identifiers) + 1)
    same('report.checks', report['checks'], global_checks)
    all_checks = global_checks + box_checks
    failed = [row['id'] for row in all_checks if not row['pass']]
    same('report.summary', report['summary'], {'check_count': len(all_checks), 'failed_count': len(failed),
          'failed_ids': failed, 'status': 'FAIL' if failed else 'PASS'})
    need(not failed, 'reconstructed finite assertions failed; saved input is preserved, no retry authorized')
    return summaries, len(all_checks)


def main(argv):
    need(len(argv) == 3, 'DISABLED: requires ROOT_BINDING_JSON and EXACT_BINDING_SHA256')
    binding_path = Path(argv[1])
    need(binding_path.is_absolute() and binding_path.resolve(strict=True) == binding_path and
         binding_path.is_file(), 'exact physical binding file required')
    binding_raw = binding_path.read_bytes()
    need(len(argv[2]) == 64 and sha256(binding_raw).hexdigest() == argv[2], 'binding byte pin')
    binding = parse(binding_raw)
    keys('binding', binding, ('format', 'approved', 'receiver_source', 'saved_stdout',
                            'accepted_producer', 'accepted_parameters', 'execution',
                            'root_received_source_runtime_and_native_evidence',
                            'canonical_adoption_authorized', 'retry_authorized', 'admission_authorized'))
    need(binding['format'] == 'finite-pointer-saved-output-binding-v1' and binding['approved'] is True and
         binding['root_received_source_runtime_and_native_evidence'] is True, 'ROOT_APPROVAL_REQUIRED')
    need(binding['canonical_adoption_authorized'] is False and binding['retry_authorized'] is False and
         binding['admission_authorized'] is False, 'saved_output_reception_only')
    same('binding.accepted_producer', binding['accepted_producer'], PRODUCER_PIN)
    same('binding.accepted_parameters', binding['accepted_parameters'], PARAMETER_PIN)
    own = Path(__file__).resolve(strict=True)
    keys('binding.receiver_source', binding['receiver_source'], ('path', 'sha256', 'bytes'))
    same('binding.receiver_source.path', binding['receiver_source']['path'], str(own))
    source_raw = own.read_bytes()
    same('binding.receiver_source.pin', {k: binding['receiver_source'][k] for k in ('sha256', 'bytes')},
         {'sha256': sha256(source_raw).hexdigest(), 'bytes': len(source_raw)})
    keys('binding.execution', binding['execution'], ('cwd', 'pycache_prefix'))
    execution = binding['execution']
    need(Path(execution['cwd']).is_absolute() and Path(execution['cwd']).resolve(strict=True) == Path(execution['cwd']) and
         str(Path.cwd()) == execution['cwd'], 'exact physical root-bound cwd')
    cache = execution['pycache_prefix']
    need(type(cache) is str and Path(cache).is_absolute() and not os.path.lexists(cache), 'new_absent_root_bound_cache')
    need(sys.executable == '/usr/bin/python3.10' and sys.version_info[:2] == (3, 10) and
         sys.flags.isolated == sys.flags.no_site == 1 and sys.flags.optimize == 0 and sys.dont_write_bytecode,
         'clean_system_python_I_S_B_required')
    same('actual.environment', dict(os.environ), ENV)
    same('actual.sys_path', sys.path, ['/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload'])
    same('actual.pycache_prefix', sys.pycache_prefix, cache)
    same('actual.original_argv', sys.orig_argv, [sys.executable, '-I', '-S', '-B', '-X',
         'pycache_prefix=' + cache, str(own), str(binding_path), argv[2]])
    item = binding['saved_stdout']
    keys('binding.saved_stdout', item, ('path', 'sha256', 'bytes'))
    integer(item['bytes'], 'saved_stdout.bytes', 1)
    path = Path(item['path'])
    need(path.is_absolute() and path.resolve(strict=True) == path and path.is_file() and
         path not in (own, binding_path), 'exact physical saved_stdout file')
    raw = path.read_bytes()
    same('saved_stdout.byte_pin', {'sha256': sha256(raw).hexdigest(), 'bytes': len(raw)},
         {k: item[k] for k in ('sha256', 'bytes')})
    report = parse(raw)
    need((compact(report) + '\n').encode('ascii') == raw, 'entire deterministic ASCII compact sorted JSON plus one LF')
    summaries, saved_checks = inspect_report(report)
    need(path.read_bytes() == raw and own.read_bytes() == source_raw and
         binding_path.read_bytes() == binding_raw and not os.path.lexists(cache), 'exact_inputs_unchanged_after_reception')
    print(compact({'status': 'PASS_SAVED_OUTPUT_RECEPTION_ONLY', 'saved_stdout': item,
          'boxes': summaries, 'states': 4356, 'saved_check_records': saved_checks,
          'typed_comparisons': COMPARED,
          'deductive_only_missing_families': [
              {'family': 'figure_eight_two_long_cycles', 'first_core_size': 5},
              {'family': 'barbell_two_long_cycles', 'first_core_size': 6},
              {'family': 'theta_three_nondirect_paths', 'first_core_size': 5}],
          'producer_invocations': 0, 'canonical_adoption': False, 'admission': 'NOT_DECIDED',
          'execution_provenance': 'Separate root native/runtime reception required; this checker inspects saved output only.',
          'contributor_scope': 'Author/verifier reconstruction, not independent manuscript review or same-gate acceptance.'}))
    return 0


if __name__ == '__main__':
    try:
        code = main(sys.argv)
    except Exception as error:
        print(compact({'status': 'FAIL_SAVED_OUTPUT_RECEPTION', 'error_type': type(error).__name__,
                       'error': str(error), 'typed_comparisons_completed': COMPARED,
                       'producer_invocations': 0, 'admission': 'NOT_DECIDED'}), file=sys.stderr)
        code = 1
    raise SystemExit(code)
