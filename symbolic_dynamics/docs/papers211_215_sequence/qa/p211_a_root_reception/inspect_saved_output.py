"""Root semantic reception of saved A stdout; never imports A or author code."""
import ast
from hashlib import sha256
import itertools
import json
import math
from pathlib import Path
import sys

CHECKS = 0


def need(ok, label):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(label)


def unique(pairs):
    result = {}
    for key, value in pairs:
        need(key not in result, ('duplicate JSON key', key))
        result[key] = value
    return result


def parse(data):
    return json.loads(data, object_pairs_hook=unique)


def shape(obj, names, label):
    need(type(obj) is dict and set(obj) == set(names.split()), ('exact object keys', label))


def wire_types(value):
    need(type(value) in (dict, list, int, bool, str, type(None)), 'no floating or non-JSON wire value')
    if type(value) is dict:
        for key, child in value.items():
            need(type(key) is str, 'string object key')
            wire_types(child)
    elif type(value) is list:
        for child in value:
            wire_types(child)


def supports(values):
    ends = [i for i in range(1, len(values)+1) if i == len(values) or values[i-1] != values[i]]
    return ends, [values[i-1] for i in ends]


def reconstruct(x, y, n):
    return tuple(y[next(j for j, end in enumerate(x) if end >= i)] for i in range(1, n+1))


def intervals(w, z):
    groups, strict = [], []
    for left, right in zip(w, z):
        if left == right:
            groups.append({'anchor': left, 'strict_labels': strict})
            strict = []
        else:
            strict += [left, right]
    need(not strict and groups, 'image groups terminate with anchor')
    return groups


def coeffs(length):
    terms = {}
    for a in range(length+1):
        for b in range(length-a+1):
            terms[b-a] = terms.get(b-a, 0) + math.comb(length, a+b)
    return terms


def rows_of(terms):
    return [[k, terms[k]] for k in sorted(terms)]


need(len(sys.argv) == 3, 'BINDING_ABS SAVED_STDOUT_ABS')
binding_path, output_path = map(Path, sys.argv[1:])
need(binding_path.is_absolute() and output_path.is_absolute(), 'explicit absolute inputs')
binding_raw, data = binding_path.read_bytes(), output_path.read_bytes()
binding, out = parse(binding_raw), parse(data)
need(binding['role'] == 'A' and binding['approved'] is True, 'exact accepted A role')
shape(out, 'schema role parameters carriers total_vertices total_targets total_edges check_total verdict scope', 'top')
wire_types(out)
need(data == (json.dumps(out, sort_keys=True, separators=(',', ':'), ensure_ascii=True, allow_nan=False)+'\n').encode(), 'entire compact sorted ASCII wire')
for predicate in binding['schema']['equalities']:
    value = out
    for key in predicate['path']:
        value = value[key]
    need(value == predicate['value'], ('all bound equality paths', predicate['path']))
for predicate in binding['schema']['lengths']:
    value = out
    for key in predicate['path']:
        value = value[key]
    need(len(value) == predicate['value'], ('all bound length paths', predicate['path']))
capsule = {row['name']: row for row in binding['capsule_files']}
for item in capsule.values():
    body = Path(item['path']).read_bytes()
    need(len(body) == item['bytes'] and sha256(body).hexdigest() == item['sha256'], 'unchanged scientific source/parameters')
tree = ast.parse(Path(capsule['verify.py']['path']).read_bytes())
source_names = {node.args[0].value for node in ast.walk(tree)
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == 'check'}
global_names = 'carrier_size unique_lexicographic_states only_fixed_cycles complete_recurrent_projections fixed_projection_census edge_mass sharp_full_height parity_witness_attains_height complete_target_rows decoded_total_mass'.split()
vertex_names = 'literal_closure support_reconstruction image_iff product_support_containments product_common_anchor_identity first_image_extensive_top_fixing terminal_formula full_carrier_time orbit_graph_tail_agreement orbit_graph_period_agreement orbit_graph_terminal_agreement'.split()
image_names = 'labelled_endpoint_peeling image_exact_time image_label_budget constructive_image_sufficiency decoder_injective complete_inverse_atlas laurent_fibre_count laurent_rank_branch_counts'.split()
need(source_names == set(global_names+vertex_names+image_names+['zero_fibre', 'parity_witness_initial_change']), 'every exact named source predicate')
carrier_results = []
for n, box in enumerate(out['carriers'], 1):
    shape(box, 'n vertex_count rows cycles indegree_pruning_order reverse_breadth_first_order image_vertex_ids zero_fibre_vertex_ids height height_prediction height_attaining_vertex_ids specified_parity_witness_id check_counts check_total', n)
    states = list(itertools.combinations_with_replacement(range(1, n+1), n))
    ids = {state: i for i, state in enumerate(states)}
    count = len(states)
    need(box['n'] == n and box['vertex_count'] == count == math.comb(2*n-1, n), 'complete carrier population')
    records = box['rows']
    need(len(records) == count, 'all rows, no target omission')
    edges, incoming = [], [[] for _ in states]
    for i, (state, row) in enumerate(zip(states, records)):
        shape(row, 'id values kernel_ends image_values successor_id predecessor_ids cycle_index graph_depth orbit_with_repeated_terminal terminal_id terminal_support_prediction image_criterion time_prediction image_intervals image_radius peeled_successor_id inverse_atlas', (n, i))
        need(row['id'] == i and tuple(row['values']) == state, 'every lexicographic labelled vertex')
        x, y = supports(state)
        need(row['kernel_ends'] == x and row['image_values'] == y, 'complete whole-function support record')
        a = sorted(set(y)|{n})
        successor = tuple(next(end for end in x if end >= next(site for site in a if site >= j)) for j in range(1, n+1))
        target = ids[successor]
        need(type(row['successor_id']) is int and row['successor_id'] == target, 'every actual literal edge')
        edges.append(target)
        incoming[target].append(i)
    image_ids = [i for i in range(count) if incoming[i]]
    zero_ids = [i for i in range(count) if not incoming[i]]
    need(box['image_vertex_ids'] == image_ids and box['zero_fibre_vertex_ids'] == zero_ids, 'entire image/zero-fibre partition')
    # Reconstruct queue orders from the saved graph, not any temporal formula.
    degrees = list(map(len, incoming))
    pruning = [i for i in range(count) if not degrees[i]]
    for vertex in pruning:
        degrees[edges[vertex]] -= 1
        if degrees[edges[vertex]] == 0:
            pruning.append(edges[vertex])
    recurrent = [i for i in range(count) if degrees[i]]
    need(all(edges[i] == i for i in recurrent), 'no nontrivial saved graph cycle')
    need(box['cycles'] == [[i] for i in recurrent], 'entire ordered fixed cycle list')
    expected_fixed = [i for i, state in enumerate(states) if supports(state)[0] == supports(state)[1]]
    need(recurrent == expected_fixed and len(recurrent) == 2**(n-1), 'all and only ceiling projections')
    breadth = list(recurrent)
    reached = set(breadth)
    for target in breadth:
        for source in incoming[target]:
            if source not in reached:
                reached.add(source)
                breadth.append(source)
    need(box['indegree_pruning_order'] == pruning and box['reverse_breadth_first_order'] == breadth
         and len(breadth) == count, 'entire deterministic graph traversal orders')
    depths = []
    decoded_mass = 0
    for i, row in enumerate(records):
        state = states[i]
        w, z = supports(state)
        need(row['predecessor_ids'] == incoming[i], 'every actual incoming source ID')
        orbit, visited, current = [], {}, i
        while current not in visited:
            visited[current] = len(orbit)
            orbit.append(current)
            current = edges[current]
        depth = visited[current]
        need(len(orbit)-depth == 1, 'full forward orbit period')
        need(row['orbit_with_repeated_terminal'] == orbit+[current]
             and row['terminal_id'] == current and row['graph_depth'] == depth
             and row['cycle_index'] == recurrent.index(current), 'full orbit, depth, terminal and cycle component')
        depths.append(depth)
        c = sorted(set(w)&(set(z)|{n}))
        need(row['terminal_support_prediction'] == c and states[current] == reconstruct(c, c, n), 'literal terminal-support identity')
        iw, iz = supports(states[edges[i]])
        need(set(iw) <= set(z)|{n} and set(iz) <= set(w)
             and set(iw)&set(iz) == set(c), 'product containments and exact common anchors')
        need(iz[-1] == n and all(v >= j for j, v in enumerate(states[edges[i]], 1)), 'first-image extensive/top facts')
        first_groups = intervals(iw, iz)
        radius_after = max(len(group['strict_labels'])//2 for group in first_groups)
        need(row['time_prediction'] == depth == (0 if edges[i] == i else 1+radius_after), 'fixed-zero and full first-step time')
        image = z[-1] == n and all(a <= b for a, b in zip(w, z)) and all(z[j] < w[j+1] for j in range(len(w)-1))
        need(type(row['image_criterion']) is bool and row['image_criterion'] == image == bool(incoming[i]), 'exact full-target image iff')
        if not image:
            need(all(row[key] is None for key in ('image_intervals', 'image_radius', 'peeled_successor_id', 'inverse_atlas')), 'exact off-image null evidence')
            continue
        groups = intervals(w, z)
        need(row['image_intervals'] == groups and row['image_radius'] == depth
             == max(len(group['strict_labels'])//2 for group in groups) <= (n-1)//2, 'all labelled anchor intervals and exact image time')
        px, py = [], []
        for group in groups:
            labels = group['strict_labels'][1:-1]
            px += labels[::2]+[group['anchor']]
            py += labels[1::2]+[group['anchor']]
        need(row['peeled_successor_id'] == edges[i] == ids[reconstruct(px, py, n)], 'full literal labelled peel')
        need(edges[ids[reconstruct(z, w, n)]] == i, 'exchanged-support constructive predecessor')
        atlas = row['inverse_atlas']
        shape(atlas, 'gaps gap_polynomials product_polynomial balance_counts predicted_count descriptions', ('atlas', n, i))
        previous = [0]+z[:-1]
        gaps = [list(range(left+1, right)) for left, right in zip(previous, w)]
        need(atlas['gaps'] == gaps, 'every empty or nonempty labelled free gap')
        polys = [coeffs(len(gap)) for gap in gaps]
        need(atlas['gap_polynomials'] == [rows_of(poly) for poly in polys], 'entire Laurent gap coefficient tables')
        product = {0: 1}
        for poly in polys:
            combined = {}
            for a, ca in product.items():
                for b, cb in poly.items():
                    combined[a+b] = combined.get(a+b, 0)+ca*cb
            product = combined
        need(atlas['product_polynomial'] == rows_of(product), 'all product Laurent terms')
        expected_descriptions, branch = [], [0, 0]
        for source in incoming[i]:
            x, y = supports(states[source])
            a = sorted(set(y)|{n})
            balance = len(a)-len(x)
            need(balance in (0, 1) and y == (a if balance == 0 else a[:-1]), 'known exact rank branches')
            words = []
            forced_x, forced_a = set(z), set(w)
            for gap in gaps:
                word = []
                for site in gap:
                    need(not (site in x and site in a), 'free site not common anchor')
                    colour = 1 if site in x else 2 if site in a else 0
                    word.append(colour)
                    if colour == 1:
                        forced_x.add(site)
                    elif colour == 2:
                        forced_a.add(site)
                reduced = [colour for colour in word if colour]
                need(reduced == sorted(reduced), 'X-before-A gap orientation')
                words.append(word)
            need(sorted(forced_x) == x and sorted(forced_a) == a, 'complete forced/free/forbidden support partition')
            expected_descriptions.append({'source_id': source, 'gap_words': words, 'X': x, 'A': a, 'Y': y, 'balance': balance})
            branch[balance] += 1
        need(atlas['descriptions'] == expected_descriptions, 'every complete unique predecessor description, exact keys')
        need(atlas['balance_counts'] == branch == [product.get(0, 0), product.get(1, 0)]
             and atlas['predicted_count'] == sum(branch) == len(incoming[i]), 'full inverse count and both branches')
        decoded_mass += atlas['predicted_count']
    height = 0 if n == 1 else (n+1)//2
    need(box['height'] == box['height_prediction'] == max(depths) == height, 'sharp whole carrier height')
    need(box['height_attaining_vertex_ids'] == [i for i, d in enumerate(depths) if d == height], 'all finite height maximizers, no theorem extension')
    if n == 1:
        wx, wy = [1], [1]
    elif n % 2:
        wx, wy = list(range(2, n, 2))+[n], list(range(1, n-1, 2))+[n]
    else:
        wx, wy = list(range(2, n+1, 2)), list(range(1, n, 2))
    witness = ids[reconstruct(wx, wy, n)]
    need(box['specified_parity_witness_id'] == witness and depths[witness] == height, 'exact manuscript parity witness')
    if n > 1:
        need(states[witness][0] == 1 and states[edges[witness]][0] == 2, 'genuine initial witness step')
    expected_counts = {name: 1 for name in global_names}
    expected_counts.update({name: count for name in vertex_names})
    expected_counts.update({name: len(image_ids) for name in image_names})
    if zero_ids:
        expected_counts['zero_fibre'] = len(zero_ids)
    if n > 1:
        expected_counts['parity_witness_initial_change'] = 1
    need(box['check_counts'] == expected_counts and box['check_total'] == sum(expected_counts.values()), 'entire named actual predicate census')
    need(decoded_mass == count == sum(map(len, incoming)), 'entire inverse and edge mass')
    carrier_results.append({'n': n, 'vertices': count, 'image_targets': len(image_ids),
                            'zero_targets': len(zero_ids), 'height': height, 'actual_A_checks': box['check_total']})
need(out['check_total'] == sum(row['actual_A_checks'] for row in carrier_results), 'complete reported total predicate sum')
need(output_path.read_bytes() == data and binding_path.read_bytes() == binding_raw, 'received complete inputs unchanged')
print(json.dumps({'status': 'PASS_FULL_SAVED_A_OUTPUT_SEMANTICS', 'saved_output': str(output_path),
                  'sha256': sha256(data).hexdigest(), 'bytes': len(data), 'root_checks': CHECKS,
                  'carriers': carrier_results, 'actual_A_check_total': out['check_total'],
                  'binding_sha256': sha256(binding_raw).hexdigest(),
                  'inspector_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
                  'scientific_producer_invocations': 0,
                  'scope': 'Every saved vertex, edge, incoming list, orbit, graph traversal, inverse description, coefficient and count; no submitted code import or new scientific producer.'}, sort_keys=True))
