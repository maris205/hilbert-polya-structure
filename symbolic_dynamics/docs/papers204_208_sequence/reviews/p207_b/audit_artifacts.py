#!/usr/bin/env python3
"""Read-only audit of actual author/A/root/B bytes, not B math producer.

This script intentionally reads their canonicals and receipts. No checker
is imported or executed. Historical path aliases are explicit, not guesses.
"""
import ast
from collections import Counter, defaultdict
from hashlib import sha256
from itertools import product
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[3]
FROZEN = ROOT/'papers/207-upper-neighbor-rank-dynamics/frozen_round1'
A = BASE.parent/'p207_a'
QA = ROOT/'docs/papers204_208_sequence/qa/root_replays'
COUNT = 0
READS = {}


def ck(ok, what):
    global COUNT
    COUNT += 1
    if not ok:
        raise AssertionError(what)


def read(p):
    data = p.read_bytes()
    key = str(p.relative_to(ROOT))
    h = sha256(data).hexdigest()
    if key in READS:
        ck(READS[key] == h, ('changed during audit', key))
    READS[key] = h
    return data


def parsed(p):
    return json.loads(read(p))


def leaves(v):
    if isinstance(v, dict):
        return sum(leaves(x) for x in v.values())
    if isinstance(v, list):
        return sum(leaves(x) for x in v)
    return 1


def alias_a(name):
    return A/{'FINDINGS.json': 'FINDINGS.initial.json', 'SHA256SUMS': 'SHA256SUMS.initial'}.get(name, name)


def seal(path, directory, historical_a=False):
    rows = read(path).decode().splitlines()
    seen = []
    for row in rows:
        expected, name = row.split('  ', 1)
        target = alias_a(name) if historical_a else directory/name
        ck(sha256(read(target)).hexdigest() == expected, ('manifest hash', path, name))
        seen.append(name)
    ck(len(seen) == len(set(seen)), ('manifest duplicate', path))
    return {'path': str(path.relative_to(ROOT)), 'entries': len(rows), 'historical_a_aliases': historical_a}


def check_recorded_stream(path, record):
    data = read(path)
    ck(len(data) == record['bytes'], ('stream size', path))
    ck(sha256(data).hexdigest() == record['sha256'], ('stream hash', path))


def simple_receipt(path, stream_base):
    receipt = parsed(path)
    ck(receipt['status'] == 'PASS', ('receipt status', path))
    for command in receipt['commands']:
        ck(command['exit_code'] == 0, ('actual command exit', path, command))
        for label in ('stdout', 'stderr'):
            item = command[label]
            if isinstance(item, dict):
                check_recorded_stream(stream_base/item['path'], item)
            else:
                ck(read(path.parent/item) == b'', ('export empty stream', path, item))
    return {'path': str(path.relative_to(ROOT)), 'commands': len(receipt['commands']),
            'role': 'prior evidence audit, not B mathematical execution'}


def root_receipt(name, author):
    folder = QA/name
    receipt = parsed(folder/'RECEIPT.json')
    ck(receipt['pass'], ('root receipt result', name))
    before_key, after_key = ('before_inputs', 'after_inputs') if author else ('before_package_files', 'after_package_files')
    ck(receipt[before_key] == receipt[after_key], ('recorded whole package stability', name))
    for filename, item in receipt[before_key].items():
        check_recorded_stream(FROZEN/filename if author else alias_a(filename), item)
    if author:
        stems = ['owned_seal', 'python_version', 'run1', 'run1.cmp', 'run2', 'run2.cmp', 'pair.cmp']
    elif name == 'p207_a':
        stems = ['SHA256SUMS', 'INPUT_PINS.sha256', 'python_version', 'python_link_dependencies',
                 'run1', 'run1.cmp', 'run2', 'run2.cmp', 'pair.cmp']
    else:
        stems = ['SHA256SUMS.before', 'INPUT_PINS.sha256.before', 'CONTEXT_SOURCE_PINS.sha256.before',
                 'python_version', 'python_runtime_flags', 'python_link_dependencies', 'run1', 'run1.cmp',
                 'run2', 'run2.cmp', 'pair.cmp', 'INPUT_PINS.sha256.after',
                 'CONTEXT_SOURCE_PINS.sha256.after', 'SHA256SUMS.after']
    ck(len(stems) == len(receipt['commands']), ('root stream mapping', name))
    for stem, command in zip(stems, receipt['commands'], strict=True):
        ck(command.get('exit_code', command.get('exit')) == 0, ('root actual exit', name, stem))
        for stream in ('stdout', 'stderr'):
            check_recorded_stream(folder/f'{stem}.{stream}', command[stream])
    canonical = FROZEN/'CANONICAL.json' if author else A/'CANONICAL.json'
    for filename in ('CANONICAL.json', 'run1.stdout', 'run2.stdout'):
        ck(read(folder/filename) == read(canonical), ('root full raw canonical', name, filename))
    ck(read(folder/'verify.py') == read(FROZEN/'verify.py' if author else A/'verify.py'), ('root checker copy', name))
    if name == 'p207_a_controlled':
        flags = parsed(folder/'python_runtime_flags.stdout')
        ck(flags == {'debug': True, 'ignore_environment': 1, 'isolated': 1, 'no_user_site': 1, 'optimize': 0}, 'controlled A flags')
    return {'path': str((folder/'RECEIPT.json').relative_to(ROOT)), 'commands': len(stems),
            'all_before_after_records': len(receipt[before_key]), 'root_reproductions_not_new_reviews': 2}


def cone(row):
    rows = [tuple(row)]
    for _ in range(4):
        v = rows[-1]
        rows.append(tuple(int(v[i-1] > v[i])+int(v[i+1] > v[i]) for i in range(1, len(v)-1)))
    return rows


def local_extrema(row):
    return {i-len(row)//2 for i in range(1, len(row)-1) if (row[i-1]-row[i])*(row[i+1]-row[i]) > 0}


def main():
    roots = [FROZEN, A, QA/'p207_author', QA/'p207_a', QA/'p207_a_controlled']
    files = sorted({p for root in roots for p in root.rglob('*') if p.is_file()})
    inventory = []
    duplicates = defaultdict(list)
    for p in files:
        data = read(p)
        duplicates[sha256(data).hexdigest()].append(str(p.relative_to(ROOT)))
        row = {'path': str(p.relative_to(ROOT)), 'bytes': len(data), 'sha256': sha256(data).hexdigest()}
        if p.suffix == '.json' or p.name in ('run0.stdout', 'run1.stdout', 'run2.stdout', 'producer.stdout'):
            value = json.loads(data)
            row['all_json_scalar_leaves_traversed'] = leaves(value)
        if p.suffix == '.py':
            tree = ast.parse(data)
            row['ast_nodes'] = len(list(ast.walk(tree)))
            row['imports'] = sorted({node.module for node in ast.walk(tree) if isinstance(node, ast.ImportFrom)} |
                                    {name.name for node in ast.walk(tree) if isinstance(node, ast.Import) for name in node.names})
        inventory.append(row)
    ck(len([p for p in FROZEN.rglob('*') if p.is_file()]) == 106, 'full physical freeze')
    seals = [seal(FROZEN/'SHA256SUMS', FROZEN), seal(FROZEN/'author_replay/OWNED_MANIFEST.sha256', FROZEN),
             seal(A/'SHA256SUMS', A), seal(A/'SHA256SUMS.initial', A, historical_a=True),
             seal(A/'INPUT_PINS.sha256', ROOT), seal(A/'CONTEXT_SOURCE_PINS.sha256', ROOT),
             seal(A/'DELTA_RESPONSE_AND_REPLAY_PINS.sha256', ROOT), seal(BASE/'INPUT_PINS.sha256', ROOT),
             seal(BASE/'CONTEXT_PINS.sha256', ROOT)]
    receipts = []
    for name in ('initial_01', 'pair_01', 'export_pair_01'):
        folder = FROZEN/'author_replay'/name
        seals.append(seal(folder/'MANIFEST.sha256', folder))
        receipts.append(simple_receipt(folder/'RECEIPT.json', folder))
        if name != 'export_pair_01':
            ck(read(folder/'INPUT_PINS.before.sha256') == read(folder/'INPUT_PINS.after.sha256'), ('author raw before/after', name))
            seals.append(seal(folder/'INPUT_PINS.before.sha256', folder/'source_inputs'))
            ck(read(folder/'verify.py') == read(FROZEN/'verify.py'), ('author copied source', name))
        else:
            ck(parsed(folder/'RECEIPT.json')['new_numerical_runs'] == 0, 'export is not execution')
    for name in ('initial', 'pair_01', 'pair_02'):
        folder = A/'execution'/name
        seals.append(seal(folder/'MANIFEST.sha256', folder))
        receipts.append(simple_receipt(folder/'RECEIPT.json', A))
        ck(read(folder/'INPUT_PINS.before.sha256') == read(folder/'INPUT_PINS.after.sha256'), ('A raw before/after', name))
        seals.append(seal(folder/'INPUT_PINS.before.sha256', ROOT))
        for number in ((0,) if name == 'initial' else (1, 2)):
            ck(read(folder/f'run{number}/producer.stdout') == read(A/'CANONICAL.json'), ('A complete raw canonical', name, number))
            ck(read(folder/f'run{number}/verify.py') == read(A/'verify.py'), ('A copied source', name, number))
    receipts += [root_receipt('p207_author', True), root_receipt('p207_a', False), root_receipt('p207_a_controlled', False)]
    for p in ('author_replay/initial_01/run0.stdout', 'author_replay/pair_01/run1.stdout',
              'author_replay/pair_01/run2.stdout', 'author_replay/run1.stdout', 'author_replay/run2.stdout'):
        ck(read(FROZEN/p) == read(FROZEN/'CANONICAL.json'), ('author entire stream', p))
    author, review_a, review_b = [parsed(p/'CANONICAL.json') for p in (FROZEN, A, BASE)]
    for data, census in ((author, 1384012), (review_a, 1326321), (review_b, 2158999)):
        ck(data['status'] == 'PASS' and data['assertions'] == census, 'canonical status census')
        if 'assertions_by_section' in data:
            ck(sum(data['assertions_by_section'].values()) == census, 'section assertion sum')
    # Recompute the author's actual partition and every stored witness, separately
    # from B's independent sign-lift quotient producer.
    original = author['local_growth_certificate']
    listed = original['complete_inner_exception_and_extension_certificate']
    exceptions = {tuple(x['inner_word']): x for x in listed}
    ck(len(listed) == len(exceptions) == 204, 'unique author exception words')
    census = Counter()
    for word in product(range(3), repeat=11):
        rows = cone(word)
        if rows[2][3] == rows[4][1]:
            census['center_equal'] += 1
        elif any(local_extrema(rows[t])-local_extrema(word) for t in range(1, 5)):
            census['inner_witness'] += 1
        else:
            census['needs_outer_letters'] += 1
            ck(word in exceptions, ('missing exception', word))
    ck(dict(census) == original['inner_case_counts'], 'whole 177147-word author partition')
    for inner, rec in exceptions.items():
        nine = rec['all_nine_extensions_left_right_time_site']
        ck(len(nine) == 9 and {tuple(v[:2]) for v in nine} == set(product(range(3), repeat=2)), 'all nine distinct extensions')
        for left, right, t, site in nine:
            whole = (left,)+inner+(right,)
            rows = cone(whole)
            ck(1 <= t <= 4 and abs(site) <= 5-t, 'witness bounds')
            ck(rows[2][4] != rows[4][2], 'stored witness premise')
            ck(site in local_extrema(rows[t])-local_extrema(whole), 'stored witness direct validation')
    local_b = review_b['local_sign_lift_certificate']['census']
    ck(local_b['equal_height_lifts'] == review_a['local_certificate']['equal_centers'], 'B weighted equal census vs A direct heights')
    ck(local_b['changed_height_lifts'] == review_a['local_certificate']['unequal_centers_with_witness'], 'B weighted changed census vs A direct heights')
    for i, row in enumerate(author['core_certificate']['traces_n1_to_60']):
        ck(row['all_core_points'] == review_a['independent_overlap_core_graph']['trace_exponents_1_to_81'][i] ==
           review_b['two_time_column_pair_graph']['closed_walk_traces_1_to60'][i], ('all 60 triple-representation traces', i+1))
    boxes = []
    for o, a, b in zip(author['complete_cyclic_source_target_boxes'], review_a['complete_cyclic_boxes'],
                       review_b['source_pair_inverse_and_time_filtration']['boxes'], strict=True):
        for key, ak, bk in [('n','n','n'), ('image_points','image_points','image'), ('core_points','core_points','core'),
                           ('maximum_fibre','maximum_fibre','max_fibre'), ('all_labelled_maximizers','all_labelled_maximizers','all_maximizers'),
                           ('successor_index_vector_sha256','successor_vector_sha256','successor_sha256'),
                           ('observed_sharp_height_in_this_complete_box','observed_height_not_all_n_formula','max_height')]:
            ck(o[key] == a[ak] == b[bk], ('triple box agreement', o['n'], key))
        ck(o['depth_histogram'] == a['exact_depth_histogram'] == [[i, v] for i, v in enumerate(b['height_distribution'])], 'three independent depth algorithms')
        ck(o['target_fibre_histogram_including_empty'] == a['fibre_size_histogram_including_empty'], 'entire author/A fibre histogram')
        ck(o['cycle_histogram_period_count'] == a['cycles_by_period'] == [[1,1], [2,b['period2_cycles']]], 'cycle census')
        boxes.append({'n': b['n'], 'image': b['image'], 'core': b['core'], 'max_height': b['max_height'], 'max_fibre': b['max_fibre'],
                      'maximizers': len(b['all_maximizers'])})
    for o, a, b in zip(author['single_seed_only_checks'], review_a['seed_only_n4_to_64'], review_b['single_seed_witnesses'], strict=True):
        ck((o['n'],o['single_seed_hitting_time'],o['one_hole_source_hitting_time']) ==
           (a['n'],a['seed_entrance'],a['source_entrance']) == (b['n'],b['seed20_height'],b['seed01_height']), 'all seed clocks')
    for o, b in zip(author['mixed_kernel_checks']['matrix_word_boxes'], review_b['mixed_matrix_pressure'], strict=True):
        ck(o['length'] == b['length'], 'matrix pressure common length')
        ck(sum(row[-1] for row in o['by_B_count_J_count_equality']) == b['words'], 'all matrix pressure words')
        projected = Counter()
        for k, j, equal, count in o['by_B_count_J_count_equality']:
            projected[k,j] += count
            ck(bool(equal) == (k <= 1 and j == 0), 'all author pressure equality classes')
        ck([[k,j,v] for (k,j),v in sorted(projected.items())] == b['class_counts'], 'B matrix pressure class counts')
    b_runs = []
    for label in ('initial_01', 'pair_01', 'pair_02'):
        folder = BASE/'executions'/label
        seals.append(seal(folder/'MANIFEST.sha256', folder))
        receipt = parsed(folder/'RECEIPT.json')
        ck(receipt['status'] == 'PASS', ('B receipt', label))
        ck(read(folder/'INPUTS.before.sha256') == read(folder/'INPUTS.after.sha256'), ('B raw runtime pins', label))
        seals.append(seal(folder/'INPUTS.before.sha256', ROOT))
        flags = parsed(folder/'runtime_probe.stdout')
        ck(flags['optimize'] == 0 and flags['debug'] and flags['isolated'] == 1 and flags['dont_write_bytecode'] == 1, 'B actual runtime flags')
        commands = receipt['commands']
        stems = ['runtime_probe']
        count = 1 if label == 'initial_01' else 2
        for i in range(1,count+1):
            stems += [f'run{i}', f'run{i}.canonical.cmp']
            ck(read(folder/f'run{i}.stdout') == read(BASE/'CANONICAL.json'), 'B entire raw output')
            ck(read(folder/f'run{i}_source/verify.py') == read(BASE/'verify.py'), 'B copied checker')
        if count == 2:
            stems.append('pair.cmp')
        stems += ['canonical_live.cmp','input_pins.cmp']
        ck(len(stems) == len(commands), 'B exact stream schema')
        for stem, command in zip(stems, commands, strict=True):
            ck(command['exit_code'] == 0, ('B recorded exit', label, stem))
            for stream in ('stdout','stderr'):
                ck(sha256(read(folder/f'{stem}.{stream}')).hexdigest() == command[f'{stream}_sha256'], 'B recorded stream hash')
            if stem.startswith('run') and '.cmp' not in stem and stem != 'runtime_probe':
                ck(command['assertions'] == review_b['assertions'], 'B producer census')
        b_runs.append({'label':label,'actual_numerical_runs':count,'commands':len(commands),
                       'pinned_runtime_inputs':len(read(folder/'INPUTS.before.sha256').splitlines())})
    # AST checks accompany direct full source review; they are not a sandbox claim.
    tree = ast.parse(read(BASE/'verify.py'))
    ck(not any(isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in {'open','eval','exec','compile','__import__'} for n in ast.walk(tree)), 'B no file/dynamic imports')
    ck(not any(isinstance(n,ast.Attribute) and n.attr in {'read_text','read_bytes','open','system','popen'} for n in ast.walk(tree)), 'B no IO access')
    # Record every actually consumed object's original hash before rechecking it.
    before = dict(READS)
    for name, h in before.items():
        ck(sha256((ROOT/name).read_bytes()).hexdigest() == h, ('audit input drift',name))
    result = {'status':'PASS','kind':'actual artifact/provenance audit, separate from standalone B mathematics',
              'checks':COUNT,'inventory':inventory,'all_input_pins_before_and_after':before,
              'byte_identity_groups':[{'sha256':h,'paths':v} for h,v in sorted(duplicates.items()) if len(v)>1],
              'validated_manifests':seals,'prior_actual_receipts':receipts,'B_actual_executions':b_runs,
              'author_partition_recomputed':dict(census),'all_stored_outer_witnesses_recomputed':1836,
              'three_representation_common_boxes':boxes,
              'historical_A_path_aliases':{'FINDINGS.json':'FINDINGS.initial.json','SHA256SUMS':'SHA256SUMS.initial'},
              'source_access_not_closed_by_this_audit':True,'author_A_gate_or_old_checker_executed_or_imported':False}
    target = BASE/'ARTIFACT_AUDIT.json'
    with target.open('x') as stream:
        json.dump(result,stream,indent=2,sort_keys=True)
        stream.write('\n')
    print(json.dumps({'status':'PASS','checks':COUNT,'consumed_immutable_inputs':len(before),
                      'artifact':str(target),'sha256':sha256(target.read_bytes()).hexdigest()},sort_keys=True))


if __name__ == '__main__':
    main()
