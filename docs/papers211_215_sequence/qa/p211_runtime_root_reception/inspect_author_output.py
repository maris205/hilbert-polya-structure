"""Full saved-output semantic reception, not an independent manuscript review.

Reads one already-recorded stdout and fixed parameter bytes. Never imports
the scientific producer, writes a canonical, or expands its seven boxes.
"""
from hashlib import sha256
import json
import math
from pathlib import Path
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
PAPER = ROOT/'papers/211-kernel-image-projection-feedback'
PARAM_SHA = '8c56e641351410fb210e0462301a3321c5e2c8a036aa1a4ef8301de6419d9149'
TOP = {'schema', 'parameters', 'box_count', 'total_states', 'assertions', 'checks', 'boxes'}
BOX = {'n', 'carrier_size', 'state_records', 'image_count', 'fixed_count',
       'recurrent_count', 'maximum_height', 'theorem_height', 'sharp_witness',
       'inverse_mass', 'assertions'}
STATE = {'source', 'kernel_endpoints', 'image_values', 'completed_image',
         'successor', 'fixed', 'recurrent', 'in_image', 'orbit', 'cycle_start',
         'cycle', 'terminal', 'predicted_terminal', 'height', 'predicted_height',
         'predecessors', 'decoded_predecessors', 'fibre_count', 'laurent_count',
         'laurent_coefficients', 'anchor_blocks', 'peeled_successor'}
CHECKS = 0


def need(condition, detail):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(detail)


def unique(items):
    result = {}
    for key, value in items:
        need(key not in result, ('duplicate key', key))
        result[key] = value
    return result


def reject_constant(value):
    raise ValueError('Nonfinite JSON constant: '+value)


def integer(value, low=0):
    need(type(value) is int and value >= low, ('integer', value, low))
    return value


def function(value, n):
    need(type(value) is list and len(value) == n, ('function arity', n, value))
    need(all(type(x) is int and 1 <= x <= n for x in value), 'function codomain')
    need(value == sorted(value), 'function monotonicity')
    return tuple(value)


def functions(value, n):
    need(type(value) is list, 'function list')
    return [function(item, n) for item in value]


def supports(value):
    n = len(value)
    ends = [i for i in range(1, n) if value[i-1] != value[i]]+[n]
    return ends, [value[i-1] for i in ends]


def ceiling(sites, n):
    return tuple(min(x for x in sites if x >= i) for i in range(1, n+1))


def image_state(value):
    ends, vals = supports(value)
    return vals[-1] == len(value) and all(w <= z for w, z in zip(ends, vals)) and all(vals[i] < ends[i+1] for i in range(len(ends)-1))


def blocks(value):
    need(image_state(value), 'anchor blocks only on first image')
    ends, vals = supports(value)
    result, labels = [], []
    for end, val in zip(ends, vals):
        if end == val:
            result.append({'anchor': end, 'endpoints': labels})
            labels = []
        else:
            labels += [end, val]
    need(not labels, 'complete final anchor')
    return result


def clock(value):
    return max(len(b['endpoints'])//2 for b in blocks(value))


def expand(values, endpoints):
    previous, output = 0, []
    for val, end in zip(values, endpoints):
        output += [val]*(end-previous)
        previous = end
    return tuple(output)


def polynomial(value):
    if not image_state(value):
        return []
    ends, vals = supports(value)
    result = {0: 1}
    for end, previous in zip(ends, [0]+vals[:-1]):
        gap = end-previous-1
        need(gap >= 0, 'nonnegative target gap')
        factor = {}
        for selected in range(gap+1):
            weight = math.comb(gap, selected)
            for split in range(selected+1):
                degree = selected-2*split
                factor[degree] = factor.get(degree, 0)+weight
        combined = {}
        for first, count in result.items():
            for second, weight in factor.items():
                combined[first+second] = combined.get(first+second, 0)+count*weight
        result = combined
    return [[degree, result[degree]] for degree in sorted(result)]


need(len(sys.argv) == 3, 'ABS_RECORDED_STDOUT EXPECTED_STDOUT_SHA256')
path = Path(sys.argv[1])
need(path.is_absolute() and path.is_relative_to(ROOT/'docs/papers211_215_sequence/qa/root_replays') and
     path.name == 'stdout.raw' and not path.is_symlink(), 'recorded raw output path')
data = path.read_bytes()
need(sha256(data).hexdigest() == sys.argv[2], 'pinned complete actual stdout')
parameter_bytes = (PAPER/'parameters.json').read_bytes()
need(sha256(parameter_bytes).hexdigest() == PARAM_SHA, 'exact approved parameter bytes')
parameters = json.loads(parameter_bytes, object_pairs_hook=unique, parse_constant=reject_constant)
output = json.loads(data, object_pairs_hook=unique, parse_constant=reject_constant)
need(type(output) is dict and set(output) == TOP, 'exact top-level schema')
need(data == (json.dumps(output, sort_keys=True, ensure_ascii=True, separators=(',', ':'), allow_nan=False)+'\n').encode(), 'entire compact sorted ASCII JSON plus one LF')
need(output['schema'] == 'p211-author-kip-v1' and output['parameters'] == parameters, 'complete parameter/schema binding')
need(integer(output['box_count']) == 7 and integer(output['total_states']) == 2353, 'exact seven-box state census')
need(type(output['boxes']) is list and len(output['boxes']) == 7, 'complete ordered box list')
predicates = parameters['predicates']
need(parameters['n_values'] == list(range(1, 8)) and parameters['carrier_sizes'] == [1, 3, 10, 35, 126, 462, 1716], 'original unexpanded boxes')
totals = {key: 0 for key in predicates}
summaries = []
for box, n, size in zip(output['boxes'], parameters['n_values'], parameters['carrier_sizes']):
    need(type(box) is dict and set(box) == BOX, ('exact box keys', n))
    need(integer(box['n'], 1) == n and integer(box['carrier_size'], 1) == size == math.comb(2*n-1, n), 'exact box population')
    records = box['state_records']
    need(type(records) is list and len(records) == size, 'complete record population')
    sources = [function(row['source'], n) for row in records]
    need(sources == sorted(set(sources)) and len(sources) == size, 'entire carrier by arity/range/monotonicity/distinctness/census')
    by_source = dict(zip(sources, records))
    reverse = {source: [] for source in sources}
    for source, row in zip(sources, records):
        need(type(row) is dict and set(row) == STATE, 'exact complete state record keys')
        successor = function(row['successor'], n)
        need(successor in by_source, 'recorded successor carrier closure')
        reverse[successor].append(source)
    for source, row in zip(sources, records):
        ends, vals = supports(source)
        completed = sorted(set(vals) | {n})
        need(row['kernel_endpoints'] == ends and row['image_values'] == vals and row['completed_image'] == completed, 'full recorded support coordinates')
        for labels in (row['kernel_endpoints'], row['image_values'], row['completed_image']):
            need(type(labels) is list and all(type(x) is int for x in labels), 'strict support integer types')
        first, second = ceiling(completed, n), ceiling(ends, n)
        successor = tuple(second[x-1] for x in first)
        need(tuple(row['successor']) == successor, 'actual literal composed ceiling orientation')
        orbit, cycle = functions(row['orbit'], n), functions(row['cycle'], n)
        entry = integer(row['cycle_start'])
        need(orbit and orbit[0] == source and len(set(orbit)) == len(orbit) and all(s in by_source for s in orbit), 'whole distinct recorded orbit')
        need(entry < len(orbit) and cycle == orbit[entry:] and len(cycle) == 1, 'complete singleton recurrent suffix')
        for a, b in zip(orbit, orbit[1:]+[orbit[entry]]):
            need(tuple(by_source[a]['successor']) == b, 'every recorded orbit edge and closing edge')
        terminal = ceiling(sorted(set(ends) & set(completed)), n)
        need(function(row['terminal'], n) == function(row['predicted_terminal'], n) == cycle[0] == terminal, 'full terminal identity')
        need(all(type(row[k]) is bool for k in ('fixed', 'recurrent', 'in_image')), 'actual Boolean flags')
        need(row['fixed'] == (successor == source) == (ends == vals) and row['recurrent'] == (entry == 0), 'exact fixed and recurrent flags')
        predicted_height = 0 if ends == vals else 1+clock(successor)
        need(integer(row['height']) == integer(row['predicted_height']) == entry == predicted_height, 'pointwise saved height relations')
        predecessors = functions(row['predecessors'], n)
        decoded = functions(row['decoded_predecessors'], n)
        need(predecessors == decoded == reverse[source] == sorted(set(reverse[source])), 'complete predecessor/reverse-edge consistency including zero targets')
        in_image = image_state(source)
        need(row['in_image'] == bool(predecessors) == in_image, 'complete image iff')
        terms = row['laurent_coefficients']
        need(type(terms) is list and all(type(term) is list and len(term) == 2 and type(term[0]) is int and type(term[1]) is int and term[1] > 0 for term in terms), 'full Laurent terms types')
        need(terms == polynomial(source), 'all Laurent coefficients, not only two selected coefficients')
        coefficients = dict(terms)
        need(integer(row['fibre_count']) == integer(row['laurent_count']) == len(predecessors) == coefficients.get(0, 0)+coefficients.get(1, 0), 'full fibre counts')
        if in_image:
            anchor_blocks = row['anchor_blocks']
            need(type(anchor_blocks) is list and all(type(b) is dict and set(b) == {'anchor', 'endpoints'} and type(b['anchor']) is int and type(b['endpoints']) is list and all(type(e) is int for e in b['endpoints']) for b in anchor_blocks), 'exact anchor block structure')
            need(anchor_blocks == blocks(source), 'all complete anchor blocks')
            new_ends, new_vals = [], []
            for block in anchor_blocks:
                internal = block['endpoints'][1:-1]
                new_ends += internal[::2]+[block['anchor']]
                new_vals += internal[1::2]+[block['anchor']]
            need(function(row['peeled_successor'], n) == expand(new_vals, new_ends) == successor, 'full peeled image successor')
            need([b['anchor'] for b in blocks(successor)] == [b['anchor'] for b in anchor_blocks] and clock(successor) == max(clock(source)-1, 0), 'complete anchor and remaining-clock relations')
        else:
            need(row['anchor_blocks'] is None and row['peeled_successor'] is None, 'explicit off-image null records')
    image_count = sum(row['in_image'] for row in records)
    need(integer(box['image_count']) == image_count, 'whole image count')
    fixed = sum(row['fixed'] for row in records)
    recurrent = sum(row['recurrent'] for row in records)
    need(integer(box['fixed_count']) == fixed == integer(box['recurrent_count']) == recurrent == 2**(n-1), 'complete fixed/recurrent census')
    maximum = max(row['height'] for row in records)
    expected_height = 0 if n == 1 else (n+1)//2
    need(integer(box['maximum_height']) == integer(box['theorem_height']) == maximum == expected_height, 'actual sharp whole-carrier height')
    if n == 1:
        expected_witness = (1,)
    elif n % 2:
        expected_witness = expand(list(range(1, n-1, 2))+[n], list(range(2, n, 2))+[n])
    else:
        expected_witness = expand(list(range(1, n, 2)), list(range(2, n+1, 2)))
    witness = function(box['sharp_witness'], n)
    need(witness == expected_witness and by_source[witness]['height'] == maximum, 'exact parity witness and observed sharpness')
    need(integer(box['inverse_mass']) == sum(row['laurent_count'] for row in records) == size, 'complete reverse-edge mass')
    census = dict(zip(predicates, [size+1, size+1, size+1, size, size, size+1, image_count]))
    need(type(box['assertions']) is dict and set(box['assertions']) == set(predicates) and all(type(v) is int for v in box['assertions'].values()) and box['assertions'] == census, 'exact seven predicate counts per box')
    for key in predicates:
        totals[key] += census[key]
    summaries.append({'n': n, 'states': size, 'image_count': image_count, 'height': maximum, 'assertions': census})
need(type(output['assertions']) is dict and all(type(v) is int for v in output['assertions'].values()) and output['assertions'] == totals, 'entire aggregate predicate census')
need(integer(output['checks']) == sum(totals.values()), 'complete aggregate check count')
need(sum(box['carrier_size'] for box in output['boxes']) == 2353, 'entire output population sum')
need(path.read_bytes() == data and (PAPER/'parameters.json').read_bytes() == parameter_bytes, 'saved stdout and parameters unchanged')
print(json.dumps({'status': 'PASS_FULL_SAVED_AUTHOR_OUTPUT_SEMANTICS', 'saved_output_relationship_checks': CHECKS,
    'path': str(path), 'sha256': sha256(data).hexdigest(), 'bytes': len(data),
    'parameter_sha256': PARAM_SHA, 'box_count': 7, 'total_states': 2353,
    'author_assertions': totals, 'author_checks': output['checks'], 'boxes': summaries,
    'record_keys': len(STATE), 'scientific_producer_invocations': 0,
    'scope': 'Full already-recorded output relationships and declared scope, with no producer import or invocation and no new all-parameter proof or independent manuscript review.'}, sort_keys=True, indent=2))
