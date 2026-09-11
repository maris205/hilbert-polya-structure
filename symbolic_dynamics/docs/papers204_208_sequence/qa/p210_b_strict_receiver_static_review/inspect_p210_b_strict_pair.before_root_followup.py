#!/usr/bin/env python3
"""Read-only exact-schema adaptation for the actual P210 Review B strict pair.
Derived from fully read inspect_p210_a_strict_pair.py; original remains unchanged.
Prepared before the actual B pair; missing real launch/completion refuses acceptance.
No science, build, render, page viewing, review or author-package mutation.
"""
import ast
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
PREP = QA / 'p210_b_strict_preparation'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
PREP_SHA = '987367c15fae0bd4d34ebf6c97cd1ee2dc71d1f15782ec57d73f61a332d97eec'
RUNNER_SHA = 'bacc8bf0351bdfbcc2bc671cd61131d6382fe5caccd00f02e3988afbf1d066d1'
READS = {}
CHECKS = 0


def need(test, label):
    global CHECKS
    CHECKS += 1
    if not test:
        raise AssertionError(label)


def raw(path):
    path = Path(path)
    data = path.read_bytes()
    row = {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}
    name = str(path)
    need(name not in READS or READS[name] == row, ('read_changed', name))
    READS[name] = row
    return data


def val(path):
    data = raw(path)
    return {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}


def js(path):
    return json.loads(raw(path))


def pin(path, expected):
    got = val(path)
    if isinstance(expected, str):
        expected = {'sha256': expected}
    need(all(got[k] == expected[k] for k in ('sha256', 'bytes') if k in expected), ('pin', str(path)))
    if 'resolved' in expected:
        need(str(Path(path).resolve(strict=True)) == expected['resolved'], ('resolved', str(path)))
    if 'symlink' in expected:
        need((os.readlink(path) if Path(path).is_symlink() else None) == expected['symlink'], ('symlink', str(path)))
    return got


def manifest(base, digest, count):
    pin(base / 'SHA256SUMS', digest)
    data = raw(base / 'SHA256SUMS')
    need(data.endswith(b'\n'), ('final_newline', str(base)))
    rows = {}
    for line in data.decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        need(match is not None, ('manifest_syntax', line))
        h, name = match.groups()
        p = Path(name)
        need(p.parts and not p.is_absolute() and '..' not in p.parts and name not in rows and name != 'SHA256SUMS', ('safe_nonself_unique', name))
        rows[name] = h
    files = list(base.rglob('*'))
    need(all(not p.is_symlink() for p in files), ('package_no_symlinks', str(base)))
    need(set(rows) == {p.relative_to(base).as_posix() for p in files if p.is_file()} - {'SHA256SUMS'}, ('full_inventory', str(base)))
    need(len(rows) == count, ('payload_count', str(base), len(rows), count))
    for name, h in rows.items():
        pin(base / name, h)
    return rows


def current_resources():
    names = {'/usr/bin/python3.10', '/usr/bin/cmp', '/usr/bin/ldd', '/usr/bin/env', '/bin/bash', '/bin/sh'}
    for directory, folders, files in os.walk('/usr/lib/python3.10'):
        folders[:] = [n for n in folders if n not in {'site-packages', 'dist-packages', '__pycache__'}]
        names.update(str(Path(directory) / n) for n in files if not n.endswith(('.pyc', '.pyo')))
    for base in map(Path, ('/usr/lib/x86_64-linux-gnu', '/usr/lib64', '/usr/local/lib')):
        if base.is_dir():
            paths = base.glob('*') if base == Path('/usr/local/lib') else base.rglob('*')
            names.update(str(p) for p in paths if p.is_file() and (p.name.endswith('.so') or '.so.' in p.name))
    for base in map(Path, ('/usr/lib/locale/C.utf8', '/usr/lib/x86_64-linux-gnu/gconv', '/usr/lib/gconv', '/etc/ld.so.conf.d')):
        if base.is_dir():
            names.update(str(p) for p in base.rglob('*') if p.is_file())
    return sorted(names)


def sample(data, known, cache):
    need(data['environment'] == ENV and data['cwd'] == str(ROOT) and data['executable'] == '/usr/bin/python3.10', 'runtime_identity')
    need(data['sys_path'] == ['/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload'], 'runtime_path')
    need(data['pycache_prefix'] == str(cache) and not data['cache_lexists'] and not os.path.lexists(cache), 'no_old_or_new_cache')
    need(all(s in data['flags'] for s in ('optimize=0', 'isolated=1', 'no_site=1', 'dont_write_bytecode=1')), 'runtime_flags')
    maps = data['proc_maps'].encode()
    need(sha256(maps).hexdigest() == data['proc_maps_sha256'] and len(maps) == data['proc_maps_bytes'], 'entire_maps')
    for name, row in list(data['mapped_files'].items()) + [(r['path'], r) for r in data['modules'].values()]:
        need(name in known and all(known[name][k] == row[k] for k in ('sha256', 'bytes')), ('runtime_sample_coverage', name))
        need(Path(name).suffix not in {'.pyc', '.pyo'}, ('no_sampled_bytecode', name))
        pin(name, row)


def main():
    need(sys.flags.isolated == sys.flags.no_site == 1 and sys.dont_write_bytecode and sys.flags.optimize == 0, 'isolated_readonly_inspector')
    need(dict(os.environ) == ENV and Path.cwd() == ROOT, 'inspector_environment')
    need(Path(__file__).resolve() == QA / 'inspect_p210_b_strict_pair.py' and Path(sys.executable).resolve() == Path('/usr/bin/python3.10'), 'exact_receiver_source_and_interpreter')
    need(sys.pycache_prefix == str(QA / 'p210_b_strict_receiver_unused_cache') and not os.path.lexists(sys.pycache_prefix), 'separate_absent_receiver_cache')
    val(Path(__file__).resolve())
    manifest(PREP, PREP_SHA, 4)
    pin(PREP / 'run_pair.py', RUNNER_SHA)
    tree = ast.parse(raw(PREP / 'run_pair.py'))
    specs = next(ast.literal_eval(n.value) for n in tree.body if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == 'SPECS' for t in n.targets))
    need(set(specs) == {'p210_b'}, 'exact_one_role')
    for name, row in js(PREP / 'INPUT_PINS.json')['inputs'].items():
        pin(name, row)
    preflight = js(QA / 'P210_B_STRICT_ROOT_PREFLIGHT.actual.json')['result']
    need(preflight['exit_code'] == 0 and json.loads(preflight['output'])['fresh_scientific_executions'] == 0, 'actual_preflight_not_execution')
    records = []
    expected_labels = ['00_cmp_runner_source', '01_cmp_verifier_source', '01a_cmp_parameters_source', '02_ldd_before', '03_verify_01', '03_verify_02', '04_cmp_canonical_01', '04_cmp_canonical_02', '05_cmp_pair', '06_ldd_after']
    for role, spec in specs.items():
        package = ROOT / spec['package']
        package_rows = manifest(package, spec['manifest_sha'], spec['payloads'])
        pin(package / 'verify.py', spec['verifier_sha'])
        pin(package / 'CANONICAL.json', {'sha256': spec['canonical_sha'], 'bytes': spec['canonical_bytes']})
        out = QA / 'root_replays/p210_b_strict_pair_01'
        launch_record = js(QA / 'P210_B_STRICT_ROOT_LAUNCH.actual.json')
        launch = launch_record['result']
        completion_record = js(QA / 'P210_B_STRICT_ROOT_COMPLETION.actual.json')
        completion = completion_record['result']
        need(completion_record['launch_record'] == 'P210_B_STRICT_ROOT_LAUNCH.actual.json' and completion['exit_code'] == 0, ('actual_parent_return', role))
        if 'session_id' in launch:
            need(type(launch['session_id']) is int and launch['session_id'] == completion_record['session_id'] and not launch['output'], 'same_actual_root_session')
        else:
            need(launch['exit_code'] == 0 and launch == completion, 'immediate_actual_native_completion')
        need(launch_record['cwd'] == str(ROOT) and ' run --role p210_b --expected-preparation-sha256 ' + PREP_SHA in launch_record['command'], 'exact_actual_launch_role')
        native = json.loads(completion['output'])
        need(native['role'] == role and native['status'] == 'PASS_ROOT_P210_B_STRICT_PAIR' and native['errors'] == [], 'actual_parent_success')
        need(native['closure']['payloads'] == 59 and native['checks_each'] == [spec['checks']] * 2 and native['command_count'] == 10, 'parent_complete_census')
        manifest(out, native['closure']['manifest'], 59)
        result = js(out / 'RESULT.json')
        need(result['status'] == native['status'] and result['errors'] == [] and result['role'] == role and result['unfinalized_native_labels'] == [] and result['no_new_all_size_proof_or_review'] is True, 'pair_result')
        need(result['raw_canonical_comparisons'] == 2 and result['raw_pair_comparisons'] == 1, 'exact_three_raw_comparisons')
        pin(out / 'sources/run_pair.py', RUNNER_SHA)
        pin(out / 'sources/verify.py', spec['verifier_sha'])
        pin(package / 'PARAMETERS.json', spec['parameters_sha'])
        pin(out / 'sources/PARAMETERS.json', spec['parameters_sha'])
        need({p.name for p in (out / 'sources').iterdir()} == {'verify.py', 'run_pair.py', 'PARAMETERS.json'}, 'source_only_capsule')
        known = js(out / 'INPUTS_BEFORE.json')
        need(known == js(out / 'INPUTS_AFTER.json') and len(known) == native['known_inputs'] == result['known_input_count'], 'entire_before_after_key')
        for name, row in known.items():
            pin(name, row)
        resources = js(out / 'RESOURCE_NAMES_BEFORE.json')
        need(resources == js(out / 'RESOURCE_NAMES_AFTER.json') == current_resources(), 'current_resource_membership')
        conf = js(out / 'CONFIGURATION_BEFORE.json')
        need(conf == js(out / 'CONFIGURATION_AFTER.json'), 'entire_configuration_before_after')
        for name, row in conf.items():
            p = Path(name)
            now = {'lexists': os.path.lexists(p), 'exists': p.exists(), 'is_file': p.is_file(), 'is_dir': p.is_dir(), 'resolved': str(p.resolve()), 'symlink': os.readlink(p) if p.is_symlink() else None}
            if p.is_file():
                now.update(val(p))
            need(now == row, ('current_configuration_role', name))
        samples = [('parent_' + phase + '.json', out / 'unused_parent_cache') for phase in ('before', 'after')]
        for name, cache in samples:
            sample(js(out / 'observations' / name), known, cache)
        commands = result['commands']
        need([c['label'] for c in commands] == expected_labels, 'all_ten_native_commands')
        for command in commands:
            folder = out / 'commands' / command['label']
            receipt = js(folder / 'RECEIPT.json')
            need(receipt == {k: v for k, v in command.items() if k != 'label'}, 'whole_native_record')
            attempt = js(folder / 'ATTEMPT.json')
            need(attempt['status'] == 'ATTEMPTED' and attempt['exit_code'] is None and all(attempt[k] == receipt[k] for k in ('argv', 'cwd', 'environment', 'started_utc', 'timeout_seconds')), 'whole_prespawn_record')
            need(receipt['exit_code'] == receipt['wrapper_exit_code'] == 0 and receipt['streams_complete'] and receipt['spawned'] and not receipt['timed_out'] and receipt['failure'] is None, 'native_success')
            need(receipt['environment'] == ENV and receipt['cwd'] == str(ROOT) and receipt['new_owned_session_requested'] is True, 'native_settings')
            settlement = receipt['process_group_settlement']
            need(settlement['quiescent'] is True and settlement['signals'] == [] and settlement['native_returncode'] == 0, 'actual_owned_native_settlement')
            need(type(settlement['owned_pgid']) is int and settlement['owned_pgid'] == settlement['owned_sid'] and all(r['state'] == 'Z' and r['pgid'] == r['sid'] == settlement['owned_pgid'] for r in settlement['remaining_members']), 'only_quiescent_owned_members')
            for stream in ('stdout', 'stderr'):
                pin(folder / (stream + '.raw'), receipt[stream])
            need(raw(folder / 'stderr.raw') == b'', 'full_empty_stderr')
            if receipt['argv'][0] == '/usr/bin/cmp':
                need(raw(folder / 'stdout.raw') == b'' and raw(receipt['argv'][-2]) == raw(receipt['argv'][-1]), 'full_raw_native_cmp_operands')
        for number in ('01', '02'):
            observed = js(out / ('observations/child_' + number + '.json'))
            need(observed['status'] == 'RETURNED' and not observed['volatile_open_paths'], 'actual_returned_child')
            need(observed['source'] == {'path': str(out / 'sources/verify.py'), **val(package / 'verify.py')} and
                 observed['parameters'] == {'path': str(out / 'sources/PARAMETERS.json'), **val(package / 'PARAMETERS.json')} and
                 observed['scientific_argv'] == [str(out / 'sources/verify.py')] and observed['parameter_locator'] == 'sibling of scientific __file__', 'exact_original_scientific_parameter_interface')
            cache = out / ('unused_child_' + number + '_cache')
            for phase in ('before', 'after'):
                need(observed[phase]['argv'] == observed['scientific_argv'], 'observed_scientific_argv')
                sample(observed[phase], known, cache)
            for name, row in observed['opened_ordinary_files'].items():
                need(name in known and all(row[k] == known[name][k] for k in ('sha256', 'bytes')), ('open_coverage', name))
                pin(name, row)
                need(not Path(name).is_relative_to(ROOT) or name in {str(out / 'sources/verify.py'), str(out / 'sources/PARAMETERS.json')}, 'no_other_project_scientific_open')
            for phase in ('before', 'after'):
                need(all(not Path(r['path']).is_relative_to(ROOT) or r['path'] == str(out / 'sources/run_pair.py') for r in observed[phase]['modules'].values()), 'no_author_A_or_project_module_import')
            for row in observed['nonfile_open_paths_at_end']:
                need(Path(row['path']).is_relative_to(cache) and not row['lexists_after'] and not row['exists_after'] and not row['is_dir_after'] and not os.path.lexists(cache), 'only_absent_new_cache_probes')
            output = out / ('commands/03_verify_' + number + '/stdout.raw')
            need(raw(output) == raw(package / 'CANONICAL.json'), 'entire_original_canonical')
            data = js(output)
            parameters = js(package / 'PARAMETERS.json')
            need(data[spec['check_field']] == spec['checks'] and data['representation'] == parameters['carrier'] and data['edge_construction'] == parameters['edges'] and parameters['masses'] == list(range(1, 13)) and data['states'] == 4095 and [row['mass'] for row in data['census']] == list(range(1, 13)) and sum(len(row['states']) for row in data['census']) == 4095 and sum(len(row['triangular_codes']) for row in data['census']) == 265, 'original_scientific_counts_and_box')
        links = js(out / 'LINKED_RUNTIME.json')
        need(links['before'] == links['after'] and all(n in known for n in links['before']), 'ldd_closure')
        for label, phase in [('02_ldd_before', 'before'), ('06_ldd_after', 'after')]:
            body = raw(out / ('commands/' + label + '/stdout.raw'))
            paths = sorted({str(Path(os.fsdecode(p)).resolve()) for p in re.findall(rb'(/[^\s()]+)', body) if Path(os.fsdecode(p)).is_file()})
            need(b'not found' not in body and paths == links[phase], 'full_archived_ldd_parse')
        closure = js(out / 'PACKAGE_AND_PREPARATION_CLOSURE.json')
        need(closure['before'] == closure['after'] and closure['before']['role'] == role, 'entire_package_closure')
        need(set(closure['before']['package_files']) == {str(package / n) for n in package_rows} | {str(package / 'SHA256SUMS')}, 'exact_old_package_dependency_set')
        records.append({'role': role, 'checks_each': spec['checks'], 'known_inputs': len(known), 'pair_manifest': val(out / 'SHA256SUMS'), 'native_commands': 10})
    initial_reads = dict(READS)
    for name, row in initial_reads.items():
        pin(name, row)
    print(json.dumps({'status': 'PASS_ROOT_P210_B_STRICT_PAIR_ORIGINAL_RECEPTION', 'checks': CHECKS, 'physical_read_paths_rechecked': len(initial_reads), 'read_ledger_sha256': sha256(json.dumps(initial_reads, sort_keys=True, separators=(',', ':')).encode()).hexdigest(), 'pairs': records, 'actual_new_scientific_runs_in_pairs': 2, 'fresh_scientific_runs_by_this_inspector': 0, 'full_recorded_native_commands': 10, 'scope': 'Original source/runtime/native/canonical/full-key reception only; not proof, review, build, view or five-paper terminal PASS', 'owner': 'OWNER_AMBER', 'external_status': 'HOLD_EXTERNAL'}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
