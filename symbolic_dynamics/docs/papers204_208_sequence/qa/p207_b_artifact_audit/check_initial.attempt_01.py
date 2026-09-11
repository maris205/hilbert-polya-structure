#!/usr/bin/env python3
"""Independent artifact-only P207 B intake check; never executes a math producer.

Prints its complete audit result. All review/freeze/root-replay inputs are
read-only. This is initial-package integrity, not review/delta acceptance.
"""
import ast
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[4]
BATCH = ROOT/'docs/papers204_208_sequence'
B = BATCH/'reviews/p207_b'
A = BATCH/'reviews/p207_a'
F = ROOT/'papers/207-upper-neighbor-rank-dynamics/frozen_round1'
R = BATCH/'qa/root_replays/p207_b_controlled'
CHECKS = Counter()
READS = {}
SEALS = []


def ck(ok, section, detail):
    CHECKS[section] += 1
    if not ok:
        raise AssertionError((section, detail))


def key(path):
    return str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)


def read(path):
    raw = path.read_bytes()
    value = {'bytes': len(raw), 'sha256': sha256(raw).hexdigest()}
    name = key(path)
    if name in READS:
        ck(READS[name] == value, 'read_stability', name)
    READS[name] = value
    return raw


def data(path):
    return json.loads(read(path))


def hashcheck(path, expected, section='pins'):
    ck(sha256(read(path)).hexdigest() == expected, section, key(path))


def seal(path, base, complete=False, alias=None):
    found = {}
    for row in read(path).decode().splitlines():
        digest, name = row.split('  ', 1)
        p = Path(name)
        ck(bool(re.fullmatch('[0-9a-f]{64}', digest)) and not p.is_absolute()
           and '..' not in p.parts, 'manifest_schema', key(path))
        ck(name not in found, 'manifest_schema', ('duplicate', name))
        found[name] = digest
        hashcheck(base/(alias or {}).get(name, name), digest)
    if complete:
        physical = {str(p.relative_to(base)) for p in base.rglob('*') if p.is_file() and p != path}
        ck(set(found) == physical, 'manifest_coverage', key(path))
    SEALS.append({'path': key(path), 'entries': len(found), 'complete_nonself': complete,
                  'explicit_historical_alias': alias or {}})
    return found


def leaves(value):
    if isinstance(value, dict):
        return sum(leaves(v) for v in value.values())
    if isinstance(value, list):
        return sum(leaves(v) for v in value)
    return 1


def raw_equal(left, right, detail):
    ck(read(left) == read(right), 'raw_bytes', detail)


def command_streams(folder, stem, record, root_schema=False):
    ck(record['exit' if root_schema else 'exit_code'] == 0, 'command_receipts', stem)
    for stream in ('stdout', 'stderr'):
        raw = read(folder/f'{stem}.{stream}')
        if root_schema:
            ck(record[stream] == {'bytes': len(raw), 'sha256': sha256(raw).hexdigest()},
               'command_receipts', (stem, stream))
        else:
            ck(record[f'{stream}_sha256'] == sha256(raw).hexdigest(),
               'command_receipts', (stem, stream))
        if stream == 'stderr' or '.cmp' in stem:
            ck(raw == b'', 'command_receipts', ('expected empty', stem, stream))


def main():
    started = datetime.now(timezone.utc).isoformat()
    ck(__debug__ and sys.flags.optimize == 0 and sys.flags.isolated == 1,
       'auditor_runtime', 'assertions and isolation')
    b_manifest = seal(B/'SHA256SUMS', B, complete=True)
    freeze = seal(F/'SHA256SUMS', F, complete=True)
    inputs = seal(B/'INPUT_PINS.sha256', ROOT)
    context = seal(B/'CONTEXT_PINS.sha256', ROOT)
    supplemental = seal(B/'SUPPLEMENTAL_READ_PINS.sha256', ROOT)
    pages = seal(B/'PAGE_VIEW_PINS.sha256', ROOT)
    physical_freeze = {key(p) for p in F.rglob('*') if p.is_file()}
    physical_a = {key(p) for p in A.rglob('*') if p.is_file()}
    ck(len(b_manifest) == 118 and len(freeze) == 105, 'intake', 'initial closure sizes')
    ck(set(inputs) == physical_freeze and len(inputs) == 106, 'intake', 'exact physical Round1')
    ck(physical_a <= set(context) and len(physical_a) == 134 and len(context) == 144,
       'intake', 'all final-A plus ten contexts')
    ck(len(supplemental) == 7 and len(pages) == 7, 'intake', 'supplement and page counts')
    raw_equal(F/'SHA256SUMS', F.parent/'frozen_round0/SHA256SUMS', 'unchanged Round0/Round1 manifest')
    findings = data(B/'FINDINGS.json')
    ck(findings['accepted_delta'] is False and findings['findings'] == [] and not (B/'DELTA.md').exists(),
       'intake', 'initial, not fabricated delta')
    ck(findings['census']['open'] == {'critical': 0, 'major': 0, 'minor': 0}, 'intake', 'initial finding census')

    source = read(B/'verify.py')
    tree = ast.parse(source)
    imports = sorted({n.module for n in ast.walk(tree) if isinstance(n, ast.ImportFrom)} |
                     {a.name for n in ast.walk(tree) if isinstance(n, ast.Import) for a in n.names})
    ck(imports == ['collections', 'fractions', 'hashlib', 'itertools', 'json', 'sys'],
       'producer_dependencies', 'exact stdlib-only direct imports')
    prohibited = {'open', 'eval', 'exec', 'compile', '__import__'}
    ck(not any(isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in prohibited
               for n in ast.walk(tree)), 'producer_dependencies', 'no direct IO/dynamic loader')
    ck(not any(isinstance(n, ast.Attribute) and n.attr in {'read_text', 'read_bytes', 'open', 'system', 'popen'}
               for n in ast.walk(tree)), 'producer_dependencies', 'no file/subprocess methods')
    # AST checks supplement the auditor's full direct reading, not a sandbox proof.
    canonical = data(B/'CANONICAL.json')
    ck(read(B/'CANONICAL.json') == (json.dumps(canonical, indent=2, sort_keys=True)+'\n').encode(),
       'canonical_shape', 'complete producer JSON format')
    ck(canonical['status'] == 'PASS' and canonical['assertions'] == 2158999,
       'canonical_shape', 'recorded status/count; not new mathematical execution')
    ck(set(canonical) == {'assertions', 'deducted_independent_set_attainers', 'local_sign_lift_certificate',
       'mixed_matrix_pressure', 'positive_kernels', 'review', 'scope', 'single_seed_witnesses',
       'source_pair_inverse_and_time_filtration', 'status', 'two_time_column_pair_graph'},
       'canonical_shape', 'all eleven output sections')
    local = canonical['local_sign_lift_certificate']
    census = local['census']
    records = local['changed_sign_classes']
    ck(census['sign_words'] == 3**12 and census['height_lifts'] == 3**13,
       'canonical_shape', 'declared local exhaustive bounds')
    ck(census['realizable'] + census['unrealizable'] == census['sign_words'] and
       census['changed_classes'] + census['equal_classes'] == census['realizable'] and
       census['changed_height_lifts'] + census['equal_height_lifts'] == census['height_lifts'],
       'canonical_shape', 'local census partition')
    ck(len(records) == census['changed_classes'] == 20115 and
       len({r[0] for r in records}) == len(records), 'canonical_shape', 'complete unique changed classes')
    ck(sum(r[1] for r in records) == census['changed_height_lifts'],
       'canonical_shape', 'full changed lift census, not witness recomputation')
    for sign_word, weight, time, site in records:
        ck(len(sign_word) == 12 and set(sign_word) <= set('012') and type(weight) is int and weight > 0
           and 1 <= time <= 4 and abs(site) <= 5-time, 'stored_record_shape', sign_word)
    graph = canonical['two_time_column_pair_graph']
    ck(len(graph['columns']) == 6 and len(graph['vertices']) == 36 and
       len(graph['allowed_triples']) == 45 and len(graph['integer_determinant_samples_z0_to36']) == 37
       and len(graph['determinant_coefficients_degree0_to36']) == 37 and
       len(graph['closed_walk_traces_1_to60']) == 60, 'canonical_shape', 'full graph/polynomial/trace output')
    cyclic = canonical['source_pair_inverse_and_time_filtration']
    boxes = cyclic['boxes']
    ck([v['n'] for v in boxes] == list(range(3, 11)) and len(cyclic['machine_pairs']) == 9,
       'canonical_shape', 'complete original cyclic boxes and nine-state decoder')
    for row in boxes:
        n = row['n']
        ck(row['states'] == 3**n and sum(row['height_distribution']) == 3**n
           and row['height_distribution'][0] == row['core']
           and len(row['height_distribution']) == row['max_height']+1,
           'canonical_shape', ('cyclic totals', n))
        ck(all(len(w) == n and set(w) <= {0, 1, 2} for w in row['all_maximizers']) and
           len({tuple(w) for w in row['all_maximizers']}) == len(row['all_maximizers']),
           'canonical_shape', ('labelled equality list', n))
        for name in ('successor_sha256', 'fibre_counts_sha256', 'every_labelled_inverse_set_sha256'):
            ck(bool(re.fullmatch('[0-9a-f]{64}', row[name])), 'canonical_shape', (n, name))
    ck(sum(v['states'] for v in boxes) == 88560, 'canonical_shape', 'full cyclic source/target census')
    ck([v['length'] for v in canonical['positive_kernels']['census']] == list(range(1, 7)),
       'canonical_shape', 'local run bounds')
    pressure = canonical['mixed_matrix_pressure']
    ck([v['length'] for v in pressure] == list(range(2, 11)), 'canonical_shape', 'matrix-word bounds')
    for row in pressure:
        ck(row['words'] == 3**row['length'] == sum(v[2] for v in row['class_counts']),
           'canonical_shape', ('complete matrix-word census', row['length']))
    seeds = canonical['single_seed_witnesses']
    ck([v['n'] for v in seeds] == list(range(4, 65)) and
       all(len(v['meeting_word']) == v['n'] for v in seeds), 'canonical_shape', 'seed-only full output')
    ck([v['n'] for v in canonical['deducted_independent_set_attainers']] == [4, 6, 8, 10],
       'canonical_shape', 'classical-attainer fixed bounds')

    own_roles = {key(B/name) for name in ('verify.py', 'record_review.py', 'INPUT_PINS.sha256', 'CONTEXT_PINS.sha256')}
    receipts = []
    for label, count in [('initial_01', 1), ('pair_01', 2), ('pair_02', 2)]:
        folder = B/'executions'/label
        seal(folder/'MANIFEST.sha256', folder, complete=True)
        receipt = data(folder/'RECEIPT.json')
        before = seal(folder/'INPUTS.before.sha256', ROOT)
        after = seal(folder/'INPUTS.after.sha256', ROOT)
        expected = set(inputs) | set(context) | own_roles
        if count == 2:
            expected.add(key(B/'CANONICAL.json'))
        ck(set(before) == expected and before == after and len(before) == (254 if count == 1 else 255),
           'runtime_dependencies', label)
        raw_equal(folder/'INPUTS.before.sha256', folder/'INPUTS.after.sha256', (label, 'before-after'))
        raw_equal(folder/'CANONICAL.input.json', B/'CANONICAL.json', (label, 'snapshot'))
        flags = data(folder/'runtime_probe.stdout')
        ck(flags['optimize'] == 0 and flags['debug'] is True and flags['isolated'] == 1
           and flags['dont_write_bytecode'] == 1, 'runtime_dependencies', (label, 'actual probe'))
        hashcheck(Path(flags['executable']).resolve(), receipt['python_binary_sha256'], 'runtime_dependencies')
        stems = ['runtime_probe']
        for i in range(1, count+1):
            stems += [f'run{i}', f'run{i}.canonical.cmp']
            copied = folder/f'run{i}_source/verify.py'
            raw_equal(copied, B/'verify.py', (label, i, 'source copy'))
            ck({p.name for p in copied.parent.iterdir()} == {'verify.py'},
               'producer_dependencies', (label, i, 'retained source-only cwd'))
            raw_equal(folder/f'run{i}.stdout', B/'CANONICAL.json', (label, i, 'complete stream'))
        if count == 2:
            stems.append('pair.cmp')
        stems += ['canonical_live.cmp', 'input_pins.cmp']
        ck(receipt['status'] == 'PASS' and len(stems) == len(receipt['commands']), 'command_receipts', label)
        for stem, command in zip(stems, receipt['commands'], strict=True):
            command_streams(folder, stem, command)
            if stem in ('run1', 'run2'):
                copied = folder/f'{stem}_source/verify.py'
                ck(command['command'] == [str(Path(flags['executable']).resolve()), '-I', '-B', str(copied)]
                   and command['cwd'] == str(copied.parent) and command['assertions'] == 2158999,
                   'command_receipts', (label, stem, 'exact command'))
            if '.cmp' in stem:
                ck(command['command'][0] == 'cmp' and len(command['command']) == 3,
                   'command_receipts', (label, stem, 'actual cmp role'))
                raw_equal(Path(command['command'][1]), Path(command['command'][2]), (label, stem))
        receipts.append({'attempt': label, 'commands': len(stems), 'archived_mathematical_runs': count,
                         'runtime_pins': len(before)})

    audit = data(B/'ARTIFACT_AUDIT.json')
    ck(audit['status'] == 'PASS' and audit['checks'] == 12845 and
       len(audit['all_input_pins_before_and_after']) == 501, 'prior_audit', 'recorded audit dimensions')
    for name, digest in audit['all_input_pins_before_and_after'].items():
        hashcheck(ROOT/name, digest, 'prior_audit')
    for item in audit['inventory']:
        raw = read(ROOT/item['path'])
        ck(item['bytes'] == len(raw) and item['sha256'] == sha256(raw).hexdigest(),
           'prior_audit', ('inventory', item['path']))
        if 'all_json_scalar_leaves_traversed' in item:
            ck(leaves(json.loads(raw)) == item['all_json_scalar_leaves_traversed'],
               'prior_audit', ('complete parsed leaves', item['path']))
    for item in audit['validated_manifests']:
        p = ROOT/item['path']
        if item['historical_a_aliases']:
            base = A
            alias = {'FINDINGS.json': 'FINDINGS.initial.json', 'SHA256SUMS': 'SHA256SUMS.initial'}
        elif p.name == 'OWNED_MANIFEST.sha256':
            base, alias = F, None
        elif 'author_replay' in p.parts and p.name == 'INPUT_PINS.before.sha256':
            base, alias = p.parent/'source_inputs', None
        elif p.name in {'SHA256SUMS', 'MANIFEST.sha256'}:
            base, alias = p.parent, None
        else:
            base, alias = ROOT, None
        checked = seal(p, base, alias=alias)
        ck(len(checked) == item['entries'], 'prior_audit', ('listed manifest count', key(p)))
    audit_execution = data(B/'AUDIT_EXECUTION.json')
    audit_console = json.loads(audit_execution['complete_stdout'])
    ck(audit_execution['exit_code'] == 0 and audit_execution['complete_stderr'] == '' and
       audit_console['sha256'] == sha256(read(B/'ARTIFACT_AUDIT.json')).hexdigest(),
       'prior_audit', 'actual audit command/output binding')

    root_receipt = data(R/'RECEIPT.json')
    ck(root_receipt['pass'] is True and root_receipt['failure'] is None and
       root_receipt['before_package_files'] == root_receipt['after_package_files'],
       'root_replay', 'successful whole-package stable receipt')
    ck(set(root_receipt['before_package_files']) == set(b_manifest) | {'SHA256SUMS'},
       'root_replay', 'exact initial package snapshot coverage')
    for name, item in root_receipt['before_package_files'].items():
        raw = read(B/name)
        ck(item == {'bytes': len(raw), 'sha256': sha256(raw).hexdigest()}, 'root_replay', name)
    raw_equal(R/'verify.py', B/'verify.py', 'root copy')
    raw_equal(R/'CANONICAL.json', B/'CANONICAL.json', 'root canonical copy')
    raw_equal(R/'harness_input.py', BATCH/'qa/replay_p207_review.py', 'root exact adapted harness')
    ck(root_receipt['harness'] == READS[key(R/'harness_input.py')], 'root_replay', 'harness hash')
    stems = ['SHA256SUMS.before', 'INPUT_PINS.sha256.before', 'CONTEXT_PINS.sha256.before',
             'python_version', 'python_runtime_flags', 'python_link_dependencies',
             'run1', 'run1.cmp', 'run2', 'run2.cmp', 'pair.cmp',
             'INPUT_PINS.sha256.after', 'CONTEXT_PINS.sha256.after', 'SHA256SUMS.after']
    ck(len(root_receipt['commands']) == len(stems) == 14, 'root_replay', 'all actual commands')
    for stem, command in zip(stems, root_receipt['commands'], strict=True):
        command_streams(R, stem, command, root_schema=True)
        if 'CONTEXT_PINS' in stem:
            ck(command['command'] == ['sha256sum', '-c', str(B/'CONTEXT_PINS.sha256')],
               'root_replay', ('mandatory B context adaptation', stem))
        if stem in ('run1', 'run2'):
            ck(command['command'][1:] == ['-I', '-B', str(R/'verify.py')], 'root_replay', stem)
            raw_equal(R/f'{stem}.stdout', B/'CANONICAL.json', ('root', stem))
    ck(data(R/'python_runtime_flags.stdout') == {'debug': True, 'ignore_environment': 1, 'isolated': 1,
       'no_user_site': 1, 'optimize': 0}, 'root_replay', 'actual assertion-enabled isolated probe')

    build = B/'cold_build_01'
    sources = seal(build/'SOURCE_INPUTS.sha256', build)
    source_names = {'main.tex', 'math_commands.tex', 'references.bib'} | {
        str(p.relative_to(F)) for p in (F/'sections').rglob('*.tex')}
    ck(set(sources) == source_names and len(sources) == 9, 'build', 'exact source-only copy set')
    for name in sources:
        raw_equal(build/name, F/name, ('build source', name))
    raw_equal(build/'main.pdf', F/'main.pdf', 'B build vs exact reviewed PDF')
    seal(build/'PDF.sha256', build)
    ck(read(build/'BUILD_ENVIRONMENT.txt').decode().splitlines() ==
       ['SOURCE_DATE_EPOCH=1704067200', 'FORCE_SOURCE_DATE=1', 'TZ=UTC', 'LC_ALL=C'], 'build', 'recorded settings')
    build_execution = data(B/'BUILD_EXECUTION.json')
    ck(build_execution['exit_code'] == 0 and build_execution['source_only_inputs'] == 9,
       'build', 'actual helper completion, no invented per-stage exits')
    ck(build_execution['visual_review_status'] == 'PENDING_ACTUAL_PAGE_VIEWS_NOT_INFERRED_FROM_HASH',
       'build', 'preserved original pending-view record')
    fls_inputs = {line[6:] for line in read(build/'main.fls').decode().splitlines() if line.startswith('INPUT ')}
    local_fls = {str(Path(n)) for n in fls_inputs if not Path(n).is_absolute()}
    external_fls = sorted(n for n in fls_inputs if Path(n).is_absolute())
    ck(local_fls == source_names-{'references.bib'} | {'main.aux', 'main.bbl', 'main.out'},
       'build', 'last pass local inputs are sources plus same-build products')
    ck('The style file: plainnat.bst' in read(build/'main.blg').decode() and
       'Database file #1: references.bib' in read(build/'main.blg').decode(), 'build', 'bibliography inputs')
    ck(read(build/'DIAGNOSTICS.txt') == b'', 'build', 'saved diagnostics empty')
    final_log = read(build/'main.log').decode()
    ck(not re.search('undefined|Overfull|Underfull|Warning', final_log), 'build', 'full log diagnostic surface')
    ck(re.search(r'^Pages:\s+7$', read(build/'PDFINFO.txt').decode(), re.M) is not None,
       'build', 'recorded seven-page PDF metadata')
    fonts = read(build/'FONTS.txt').decode().splitlines()[2:]
    ck(len(fonts) == 31 and all('Type 1' in row and row.split()[-5] == 'yes' for row in fonts),
       'build', 'all 31 font objects embedded Type 1')
    ck(set(pages) == {key(B/f'page_views/page-{i}.png') for i in range(1, 8)},
       'build', 'exact seven page pins, not a new visual inspection')
    final_check = data(B/'FINAL_INPUT_CHECK.json')
    ck(final_check['status'] == 'PASS' and len(final_check['commands']) == 6 and
       all(c['exit_code'] == 0 for c in final_check['commands']), 'build', 'actual final checks')

    # Re-read the entire consumed dependency set after all checks. External
    # host-system .fls names are recorded as paths only, not retroactive pins.
    stable = dict(READS)
    for name, item in stable.items():
        p = Path(name) if Path(name).is_absolute() else ROOT/name
        raw = p.read_bytes()
        ck(item == {'bytes': len(raw), 'sha256': sha256(raw).hexdigest()}, 'final_dependency_stability', name)
    print(json.dumps({
        'status': 'PASS_ARTIFACT_INITIAL_SCOPE_ONLY', 'started_utc': started,
        'ended_utc': datetime.now(timezone.utc).isoformat(), 'checks': sum(CHECKS.values()),
        'checks_by_section': dict(CHECKS), 'new_mathematical_producer_executions': 0,
        'new_builds': 0, 'new_visual_reviews': 0, 'accepted_delta': False,
        'canonical_bytes': len(read(B/'CANONICAL.json')), 'canonical_scalar_leaves': leaves(canonical),
        'canonical_sha256': sha256(read(B/'CANONICAL.json')).hexdigest(),
        'B_manifest_sha256': sha256(read(B/'SHA256SUMS')).hexdigest(),
        'B_direct_stdlib_imports': imports, 'B_archived_receipts': receipts,
        'root_archived_runs_independently_checked': 2, 'root_context_manifest_name': 'CONTEXT_PINS.sha256',
        'root_harness_sha256': root_receipt['harness']['sha256'],
        'validated_manifests': SEALS, 'consumed_objects': len(stable),
        'all_consumed_inputs_before_after': stable,
        'unhashed_historical_host_TeX_input_paths': external_fls,
        'limits': ['Not a mathematical review or new theorem check.',
                   'No B edit, delta acceptance, central update, or Git action.',
                   'Reported B page views and source reads are provenance statements, not recreated by this checker.',
                   'No hermetic historical stdlib/TeX snapshot is claimed; changed host dependencies require affected reruns.',
                   'Canonical fingerprints of exhaustive inverse/source sets are not full enumerated text dumps.',
                   'B artifact-audit 12845 and B mathematics 2158999 are distinct archived counts.',
                   'Round2, terminal two builds/all-page views and external clearance remain separate.']
    }, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()

