"""Post-commitment semantic adapter; never imports another scientific program.

B inverse-graph records remain the reference. Mask/interval conversion below
only interprets archived author/A output roles; it is not B's graph producer.
"""
import collections
import hashlib
import json
from pathlib import Path
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
HERE = Path(__file__).resolve().parent
FROZEN = ROOT / 'papers/210-weakly-increasing-run-aggregation/frozen_round1'
A = ROOT / 'docs/papers204_208_sequence/reviews/p210_a'
checks = 0

def demand(ok, label):
    global checks
    checks += 1
    assert ok, label

def pin(p):
    return {'sha256': hashlib.sha256(p.read_bytes()).hexdigest(), 'bytes': p.stat().st_size}

def mask(s):
    total, code = 0, 0
    for x in s[:-1]:
        total += x
        code += 2 ** (total - 1)
    return code

def intervals(s):
    pos, out = 0, []
    for x in s:
        out.append((pos, pos + x))
        pos += x
    return out

def weights(code):
    return None if code is None else [k * (k + 1) // 2 for k in code]

inputs = [HERE / 'CANONICAL.json', HERE / 'PRE_COMPARISON_PROOF_CODE_COMMITMENT.actual.json',
          HERE / 'compare_outputs.py', FROZEN / 'CANONICAL.json', FROZEN / 'verify.py',
          A / 'CANONICAL.json', A / 'verify.py']
before = {str(p): pin(p) for p in inputs}
started = time.time()
ours = json.loads(inputs[0].read_bytes())
author = json.loads((FROZEN / 'CANONICAL.json').read_bytes())
review_a = json.loads((A / 'CANONICAL.json').read_bytes())
tables = {row['mass']: row for row in ours['census']}
lookup = {n: {tuple(s['state']): s for s in row['states']} for n, row in tables.items()}
output = []
for au, ar in zip(author['masses'], review_a['tables']):
    n = au['N']
    demand(ar['N'] == n, 'same mass')
    states = lookup[n]
    demand(set(states) == {tuple(row['state']) for row in au['states']}, 'author complete states')
    demand(len(ar['states']) == len(ar['targets']) == len(states), 'A complete states and targets')
    a_by_mask = {row[0]: row for row in ar['states']}
    a_targets = {row[0]: row for row in ar['targets']}
    targets = {tuple(row['target']): row for row in au['targets']}
    per_state = []
    for au_state in au['states']:
        s = tuple(au_state['state'])
        b = states[s]
        ma = mask(s)
        demand(au_state['edge'] == b['next'], 'author edge')
        demand(au_state['depth'] == b['time'], 'author time')
        demand(au_state['fixed_endpoint'] == b['orbit'][-1], 'author final')
        demand(au_state['orbit'] == b['orbit'], 'author complete orbit')
        demand(a_by_mask[ma][:4] == [ma, mask(b['next']), b['time'], mask(b['orbit'][-1])], 'A state record')
        born = {q: 0 for q in intervals(s)}
        expected_author, expected_A = [], []
        for t, (old, new) in enumerate(zip(b['orbit'], b['orbit'][1:]), 1):
            old_intervals, new_intervals = intervals(old), intervals(new)
            retained = {v for u, v in new_intervals[:-1]}
            deleted, removed = [], []
            for left, right in zip(old_intervals, old_intervals[1:]):
                u, v = left
                w, z = right
                if v not in retained:
                    demand(v-u >= t and (t == 1 or born[right] == t-1), 'oriented birth pressure')
                    deleted.append({'cut': v, 'left_mass': v-u, 'right_mass': z-w, 'right_birth': born[right]})
                    removed.append([v, v-u, z-w, born[right]])
            births, a_births = [], []
            for q in new_intervals:
                if q not in old_intervals:
                    parents = [list(p) for p in old_intervals if q[0] <= p[0] and p[1] <= q[1]]
                    demand(q[1]-q[0] >= 1+t*(t+1)//2, 'triangular birth pressure')
                    born[q] = t
                    births.append({'interval': list(q), 'mass': q[1]-q[0], 'parents': parents})
                    a_births.append([q[0], q[1], t])
            expected_author.append({'round': t, 'old': old, 'new': new, 'deleted_cuts': deleted, 'new_blocks': births})
            expected_A.append([t, mask(old), mask(new), removed, a_births])
        demand(au_state['birth_rounds'] == expected_author, 'full author birth/cut ledger')
        demand(a_by_mask[ma][4] == expected_A, 'full A event ledger')
        target = targets[s]
        pre = sorted(p['source'] for p in b['preimages'])
        code = weights(b['triangular_code_as_heights'])
        demand(target['sources'] == pre and target['fibre'] == b['fibre'], 'full author inverse set and fibre')
        demand(target['image'] == bool(pre) and target['code'] == code, 'author image/code')
        attained_sets = []
        for i, row in enumerate(target['suffixes']):
            suffix = s[i:]
            ref = lookup[sum(suffix)][suffix]
            counts = collections.Counter(p['source'][0] for p in ref['preimages'])
            attainable = sorted(counts)
            attained_sets.append(attainable)
            expected_branch = ('initial' if i == len(s)-1 else
                'infeasible_suffix' if lookup[sum(s[i+1:])][s[i+1:]]['attained_minimum'] is None else
                'fail' if ref['attained_minimum'] is None else
                'increment' if ref['attained_minimum'] != 1 else 'reset')
            demand(row['index'] == i and row['part'] == s[i] and row['branch'] == expected_branch, 'author suffix branch/index')
            demand(row['threshold'] == ref['attained_minimum'], 'all author suffix minima')
            demand(row['attainable_first_parts'] == attainable, 'all attained endpoint sets')
            demand(row['first_part_counts'] == [list(x) for x in sorted(counts.items())], 'all suffix endpoint multiplicities')
            witness = row['attaining_preimage']
            demand((witness is None) == (not counts), 'attainment existence')
            if witness is not None:
                demand(witness in [x['source'] for x in ref['preimages']] and witness[0] == min(counts), 'actual attained witness')
        a_target = a_targets[ma]
        demand(a_target == [ma, list(s), sorted(mask(p) for p in pre), attained_sets,
             [min(x) for x in attained_sets] if pre else None, b['fibre'], code], 'full A target record')
        per_state.append({'state': list(s), 'A_mask': ma, 'orbit_updates': b['time'],
                          'fibre': b['fibre'], 'all_author_A_fields_equal': True})
    demand(au['fixed_points'] == [list(s) for s, row in states.items() if row['fixed']], 'fixed list')
    hist = collections.Counter(s['time'] for s in states.values())
    expected_summary = {'states': len(states), 'fixed': hist[0], 'depth_histogram': [list(x) for x in sorted(hist.items())],
        'max_depth': max(hist), 'H': tables[n]['height'], 'image': tables[n]['image_size'],
        'triangular_count': tables[n]['image_size'], 'witness_count': len(au['witnesses'])}
    demand(au['summary'] == expected_summary and ar['H'] == tables[n]['height'] and ar['image_count'] == tables[n]['image_size'], 'mass summary')
    tri_expected = sorted((weights(r['heights']), r['decoded']) for r in tables[n]['triangular_codes'])
    demand(au['triangular_objects'] == [{'parts': q, 'decoded_target': s} for q, s in tri_expected], 'all author triangles')
    demand(sorted((r[1], r[2]) for r in ar['triangular']) == tri_expected, 'all A triangles')
    demand(all(r[0] == mask(r[1]) and r[3] == mask(r[2]) for r in ar['triangular']), 'A triangle mask roles')
    for w in au['witnesses']:
        h, r = w['h'], w['surplus']
        s = tuple(range(h, 0, -1)) + (1+r,)
        demand(w == {'h': h, 'surplus': n-1-h*(h+1)//2, 'state': list(s), 'orbit': states[s]['orbit']}, 'author every surplus witness')
        demand(states[s]['time'] == h, 'witness time')
    demand(ar['witnesses'] == [[w['h'], w['surplus'], w['state'], [mask(s) for s in w['orbit']]] for w in au['witnesses']], 'all A witnesses')
    partitions = [p['source'] for p in states[(n,)]['preimages']]
    expected_endpoints = [[a, b, sum(p[0] == a and p[-1] == b for p in partitions)]
                         for a in range(1, n+1) for b in range(a, n+1)]
    demand(au['endpoint_partition_coefficients'] == expected_endpoints, 'all endpoint coefficients')
    output.append({'mass': n, 'states': per_state, 'all_scientific_mass_tables_checked': True})
demand(author['totals'] == {'states': 4095, 'edges': 4095, 'targets': 4095,
       'image_objects': 265, 'triangular_objects': 265, 'surplus_witnesses': 28}, 'author totals')
demand(author['checks'] == sum(author['checks_by_kind'].values()), 'author check-count arithmetic not independent count')
demand(review_a['total_states'] == 4095, 'A total')
after = {str(p): pin(p) for p in inputs}
demand(before == after, 'all comparison inputs unchanged')
print(json.dumps({'status': 'PASS_FULL_SEMANTIC_COMPARISON_NOT_RAW_CROSS_SCHEMA_EQUALITY',
       'checks': checks, 'started_epoch': started, 'ended_epoch': time.time(),
       'inputs_before': before, 'inputs_after': after, 'masses': output,
       'boundary': 'Post-commitment comparison sidecar, not original B canonical or additional independent review.'}, sort_keys=True, indent=2))
