"""Post-commitment full author-row reconciliation; imports no math code.

Representation adapter only: reconstruct all author mathematical output
fields from independent canonical state rows and direct vertex-following.
Comparison deliberately normalizes different JSON schemas; raw author
canonical bytes are NOT claimed identical to the independent canonical.
"""
import collections
import hashlib
import json
from pathlib import Path
import sys

assert sys.flags.optimize == 0 and sys.flags.no_site and sys.flags.isolated
author_path, independent_path = map(Path, sys.argv[1:])
author = json.loads(author_path.read_bytes())
independent = json.loads(independent_path.read_bytes())
assert author['schema'] == 'p209-author-v1'
assert independent['schema'] == 'p209-review-a-independent-v1'
assert [b['n'] for b in author['boxes']] == [b['n'] for b in independent['boxes']] == list(range(6))
comparisons, projected_boxes = [], []
for a, b in zip(author['boxes'], independent['boxes']):
    n, records = b['n'], b['records']
    states = [r['f'] for r in records]
    predicted_rows = []
    for index, r in enumerate(records):
        f = r['f']
        image_set, vertex_images = list(range(n)), []
        for _ in range(n + 2):
            vertex_images.append(image_set)
            image_set = sorted({f[i] for i in image_set})
        cycles = []
        for support in r['cycle_sccs']:
            cycle, v = [min(support)], f[min(support)]
            while v != cycle[0]:
                cycle.append(v)
                v = f[v]
            assert sorted(cycle) == support
            cycles.append(cycle)
        cyc = {i for c in cycles for i in c}
        indegree = [sum(value == i for value in f) for i in range(n)]
        paths = []
        if r['recurrent']:
            for start in range(n):
                if start not in cyc and indegree[start] == 0:
                    path, v = [], start
                    while v not in cyc:
                        path.append(v)
                        v = f[v]
                    paths.append({'vertices': path, 'attachment': v})
        graph = {'cycles': cycles, 'cycle_vertices': sorted(cyc), 'indegree': indegree,
                 'paths': paths, 'finals': [i for i in range(n) if i not in cyc and f[i] in cyc],
                 'recurrent_predicate': r['recurrent'], 'predicted_period': r['carrier_period']}
        orbit, seen, j = [], set(), index
        while j not in seen:
            seen.add(j)
            orbit.append(states[j])
            j = records[j]['image_rank']
        codes = []
        for source_rank in r['inverse_ranks']:
            source = states[source_rank]
            selected = [i for i in range(n) if any(source[i] == source[j] for j in range(i + 1, n))]
            endpoints = []
            for i in range(n):
                while i in selected:
                    i = f[i]
                endpoints.append(i)
            codes.append({'selected': selected, 'endpoints': endpoints, 'source': source})
        codes.sort(key=lambda c: sum(1 << i for i in c['selected']))
        assert sorted(sum(1 << i for i in c['selected']) for c in codes) == r['inverse_masks']
        row = {'state': f, 'image': states[r['image_rank']], 'vertex_images': vertex_images,
               'graph': graph, 'entrance_steps_observed': r['entrance'],
               'whole_function_period': r['period'], 'whole_orbit': orbit,
               'eligible': [i for i in range(n) if i < f[i]],
               'inverse_codes': codes, 'literal_predecessors': [states[i] for i in r['inverse_ranks']],
               'fibre_size': len(r['inverse_ranks'])}
        assert row == a['rows'][index], (n, index, row, a['rows'][index])
        comparisons.append({'n': n, 'state_rank': index, 'state': f,
                            'all_author_row_fields_equal': True,
                            'fields': sorted(row),
                            'inverse_source_count': row['fibre_size']})
        predicted_rows.append(row)
    result = {'n': n, 'state_count': b['state_count'],
              'recurrent_count': sum(r['recurrent'] for r in records),
              'recurrent_period_census': sorted([k, v] for k, v in collections.Counter(r['period'] for r in records if r['recurrent']).items()),
              'fibre_census': sorted([k, v] for k, v in collections.Counter(len(r['inverse_ranks']) for r in records).items()),
              'maximum_fibre': b['maximum_fibre'],
              'maximizing_targets': [states[i] for i in b['extremizer_ranks']],
              'rows': predicted_rows}
    assert result == {k: v for k, v in a.items() if k != 'checks'}
    projected_boxes.append(result)
author_projection = {'boxes': [{k: v for k, v in b.items() if k != 'checks'} for b in author['boxes']], 'total_states': author['total_states']}
reviewer_projection = {'boxes': projected_boxes, 'total_states': sum(b['state_count'] for b in independent['boxes'])}
for label, payload in [('author_projection.json', author_projection), ('reviewer_projection.json', reviewer_projection)]:
    with Path(label).open('x') as stream:
        stream.write(json.dumps(payload, sort_keys=True, separators=(',', ':')) + '\n')
print(json.dumps({'status': 'PASS_FULL_STATE_RECONCILIATION', 'states': len(comparisons),
                  'author_sha256': hashlib.sha256(author_path.read_bytes()).hexdigest(),
                  'independent_sha256': hashlib.sha256(independent_path.read_bytes()).hexdigest(),
                  'scope': 'Every author row field and all mathematical box totals; differing implementation check counts and descriptive schema annotations excluded. Normalized projection comparison, not raw equality of original canonicals.',
                  'state_comparisons': comparisons}, sort_keys=True, indent=2))
