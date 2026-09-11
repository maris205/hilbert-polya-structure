"""A reviewer receipt of recorded runs; root auditor adapted, no science execution."""
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
PREP = QA/'p211_runtime_preparation'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
CHECKS, READS = 0, {}


def need(condition, detail):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(detail)


def raw(path):
    path = Path(path)
    need(path.is_file(), ('file', str(path)))
    data = path.read_bytes()
    if str(path) in READS:
        need(data == READS[str(path)], ('unchanged reread', str(path)))
    READS[str(path)] = data
    return data


def identity(data):
    return {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}


def rich(path):
    path = Path(path)
    return {**identity(raw(path)), 'resolved': str(path.resolve(strict=True)),
            'symlink': os.readlink(path) if path.is_symlink() else None}


def pin(path, expected):
    actual = rich(path)
    expected = {'sha256': expected} if isinstance(expected, str) else expected
    need(all(actual[k] == expected[k] for k in actual if k in expected), ('exact file pin', str(path)))
    return actual


def unique(items):
    result = {}
    for key, value in items:
        need(key not in result, ('duplicate JSON key', key))
        result[key] = value
    return result


def doc(path):
    return json.loads(raw(path), object_pairs_hook=unique)


def manifest(folder):
    data = raw(folder/'SHA256SUMS')
    need(data.endswith(b'\n'), 'complete manifest LF')
    rows = {}
    for line in data.decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        need(match is not None, ('manifest syntax', str(folder)))
        digest, name = match.groups()
        p = Path(name)
        need(p.parts and not p.is_absolute() and '..' not in p.parts and name not in rows and name != 'SHA256SUMS', ('safe manifest path', name))
        rows[name] = digest
    actual = set()
    for p in folder.rglob('*'):
        need(not p.is_symlink(), ('physical artifact', str(p)))
        if p.is_file():
            actual.add(p.relative_to(folder).as_posix())
    need(actual == set(rows) | {'SHA256SUMS'}, ('complete artifact inventory', str(folder)))
    for name, digest in rows.items():
        pin(folder/name, digest)
    return rows


def state(path, with_bytes=True):
    p = Path(path)
    row = {'lexists': os.path.lexists(str(p)), 'exists': p.exists(),
           'is_file': p.is_file(), 'is_dir': p.is_dir(), 'is_character_device': p.is_char_device(),
           'resolved': str(p.resolve()), 'symlink': os.readlink(p) if p.is_symlink() else None}
    if p.is_char_device():
        stat = p.stat()
        row['character_device'] = {'major': os.major(stat.st_rdev), 'minor': os.minor(stat.st_rdev), 'mode': stat.st_mode}
    if with_bytes and p.is_file():
        row.update(identity(raw(p)))
    return row


need(len(sys.argv) == 5, 'BINDING_PATH BINDING_SHA256 ACTUAL_TOOL_CAPTURE NEW_OUTPUT_ABS')
output_folder = Path(sys.argv[4])
review = ROOT/'docs/papers211_215_sequence/reviews/p211_a'
need(output_folder.is_absolute() and output_folder.parent == review/'evidence', 'owned new reception folder')
need(not os.path.lexists(output_folder), 'never overwrite a reception')
raw(Path(__file__).resolve())
pin(QA/'p211_a_root_reception/inspect_production.py', 'e0ae2bd53a323c1c0869e474d98d518d90c4e326acce73987b48f4a61363e261')
pin(QA/'p211_a_root_reception/inspect_saved_output.py', '9f12cab0540af24d6a09ccc5f1b8039b7c6d812bc4c9e530bd2c0a3a225a6111')
binding_path, capture_path = Path(sys.argv[1]), Path(sys.argv[3])
need(binding_path.is_absolute() and capture_path.is_absolute(), 'exact absolute receipt inputs')
pin(binding_path, sys.argv[2])
binding, capture = doc(binding_path), doc(capture_path)
need(binding['approved'] is True and binding['purpose'] == 'P211_MANUSCRIPT' and binding['role'] == 'A', 'actual approved role-A binding')
mode, attempt = binding['mode'], Path(binding['attempt'])
need(mode in ('initial', 'pair') and attempt.parent == QA/'root_replays', 'scoped role-A mode and attempt')
need(all(type(n) is int and 0 < n <= 900 for n in binding['timeouts'].values()), 'finite positive integer deadlines')
need(binding['argv_template'] == ['$ENTRY', '--parameters', '$PARAMETERS'] and binding['parameter_locator'] == 'explicit_absolute_argv', 'actual source interface')
need({r['name'] for r in binding['capsule_files']} == {'verify.py', 'parameters.json'} and len(binding['capsule_files']) == 2, 'two distinct scientific files')
lock_path = Path(binding['runtime_lock']['path'])
pin(lock_path, binding['runtime_lock'])
lock = doc(lock_path)
expected = dict(lock['files'])
expected.update(binding['adapter_sources'])
expected[str(binding_path)] = rich(binding_path)
expected[str(lock_path)] = rich(lock_path)
for row in binding['capsule_files']+binding['provenance_inputs']:
    expected[row['path']] = row
if mode == 'pair':
    expected[binding['canonical']['path']] = binding['canonical']
else:
    need(binding['canonical']['sha256'] is None, 'initial canonical unadopted at binding')
known = {}
for p, expected_pin in expected.items():
    actual = pin(p, expected_pin)
    known[p] = actual
    known[actual['resolved']] = rich(actual['resolved'])
for p, row in lock['configuration']['paths'].items():
    need(state(p) == row, ('live full configuration', p))
for directory, row in lock['configuration']['memberships'].items():
    p = Path(directory)
    current = {'directory': state(p, False), 'members': {}}
    if p.is_dir():
        current['members'] = {q.name: state(q, False) for q in sorted(p.iterdir())}
    need(current == row, ('live bounded direct membership', directory))
for p, row in lock['loader_search_directory_states'].items():
    need(state(p, False) == row, ('live loader directory state', p))

stages = ('outer', 'launcher', 'recorder', 'child01')+(('child02',) if mode == 'pair' else ())
capsule = attempt/'recorder/capsule'
need({p.name for p in capsule.iterdir()} == {'verify.py', 'parameters.json'}, 'physical source-only capsule')
copies = {}
for row in binding['capsule_files']:
    p = capsule/row['name']
    pin(p, {key: row[key] for key in ('sha256', 'bytes')})
    need(raw(p) == raw(row['path']), 'exact physical source copy bytes')
    copies[str(p)] = rich(p)


def argv(stage):
    return ['/usr/bin/python3.10', '-I', '-S', '-B', '-X',
            'pycache_prefix='+str(attempt/('never_created_'+stage+'_cache')),
            str(PREP/'p211_runtime.py'), stage, str(binding_path), sys.argv[2], str(attempt)]


counts, native_count = {}, 0
for stage in stages:
    folder = attempt/stage
    counts[stage] = len(manifest(folder))
    result, entered = doc(folder/'RESULT.json'), doc(folder/'ENTERED.json')
    need(result['status'] == 'PASS' and result['errors'] == [] and result['wrapper_return'] == 0 and result['stage'] == stage and
         result['role'] == 'A' and result['mode'] == mode and not result['unfinalized_native'] and not result['unknown_descendant_closure'], ('complete successful stage', stage))
    cwd = capsule if stage.startswith('child') else ROOT
    need(entered['orig_argv'] == argv(stage) and entered['argv'] == argv(stage)[6:] and entered['cwd'] == str(cwd) and entered['environment'] == ENV, ('actual complete entry settings', stage))
    preknown = dict(known)
    if stage.startswith('child'):
        preknown.update(copies)
    need(doc(folder/'INPUTS_BEFORE.json') == preknown, ('entire expected prefrozen key', stage))
    final_known = {**preknown, **copies} if stage == 'recorder' else preknown
    if stage == 'recorder':
        need(doc(folder/'CAPSULE_ADDED_INPUTS.json') == copies and doc(folder/'INPUTS_BEFORE_SCIENCE.json') == final_known, 'entire pre-science source-copy key')
    need(doc(folder/'INPUTS_AFTER.json') == final_known, ('entire unchanged stage key', stage))
    for phase in ('BEFORE', 'AFTER'):
        sample = doc(folder/('RUNTIME_'+phase+'.json'))
        sample_known = preknown if phase == 'BEFORE' else final_known
        need(sample['environment'] == ENV and sample['cwd'] == str(cwd) and sample['interpreter_argv'] == argv(stage), ('actual sampled argv/ENV/cwd', stage, phase))
        need(sample['executable'] == '/usr/bin/python3.10' and sample['sys_path'] == ['/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload'], 'actual isolated interpreter/search path')
        need(all(flag in sample['flags'] for flag in ('isolated=1', 'no_site=1', 'optimize=0', 'dont_write_bytecode=1')), 'actual source-only flags')
        need(sample['pycache_prefix'] == str(attempt/('never_created_'+stage+'_cache')) and not sample['cache_lexists'] and not os.path.lexists(sample['pycache_prefix']), 'actual absent unique cache')
        need(identity(sample['proc_maps'].encode()) == {'sha256': sample['proc_maps_sha256'], 'bytes': sample['proc_maps_bytes']}, 'complete raw volatile maps identity')
        for p, row in list(sample['mapped_files'].items())+[(m['path'], m) for m in sample['modules'].values()]:
            need(p in sample_known and not p.endswith(('.pyc', '.pyo')), ('actual consumed file prefrozen', p))
            pin(p, row)
        need(doc(folder/('CONFIGURATION_'+phase+'.json')) == lock['configuration'], 'complete actual lock configuration')
    observed = doc(folder/'OPEN_OBSERVATIONS.json')
    need(observed['events'] == doc(folder/'OPEN_EVENTS_RAW.json'), 'complete actual open events')
    for p, row in observed['ordinary_files'].items():
        need(p in final_known, ('observed ordinary input in complete key', p))
        pin(p, row)
    for p in observed['absent_cache_probes']:
        need(not os.path.lexists(p), 'observed cache absence remains')
    if stage.startswith('child'):
        need(not observed['nonordinary_devices'] and not observed['volatile_proc_reads'] and not observed['own_attempt_io'], 'scientific read scope')
        need(all(not row.get('writing') and 'forbidden_process_event' not in row for row in observed['events']), 'no observed science write/process event')
        need(set(observed['ordinary_files']) == set(copies), 'science actually read only own two source files')
        need(result['output']['scientific_argv'] == [str(capsule/'verify.py'), '--parameters', str(capsule/'parameters.json')] and
             result['output']['parameter_locator'] == 'explicit_absolute_argv' and result['output']['scientific_outcome'] == 'RETURNED', 'actual pinned compile/exec outcome')
        need(result['output']['source'] == copies[str(capsule/'verify.py')], 'actual executed source pin')
    commands = result['commands']
    actual_receipts = {p.parent.name: doc(p) for p in folder.glob('commands/*/RECEIPT.json')}
    need(set(actual_receipts) == {row['label'] for row in commands}, 'entire stage native census')
    for row in commands:
        label = row['label']
        native = actual_receipts[label]
        need({k: row[k] for k in native} == native, 'entire result/native binding')
        directory = folder/'commands'/label
        entry = doc(directory/'ATTEMPT.json')
        need(entry['status'] == 'ATTEMPTED' and entry['exit_code'] is None and all(entry[k] == native[k] for k in entry if k not in ('status', 'exit_code')), 'entire native pre-attempt relation')
        need(native['environment'] == ENV and native['exit_code'] == native['wrapper_exit_code'] == 0 and native['status'] == 'COMPLETED' and native['spawned'] and native['streams_complete'] and not native['timed_out'] and not native['interrupted'], 'actual successful complete native result')
        settlement = native['process_group_settlement']
        need(settlement['quiescent'] and not settlement['signals'] and not any(m['state'] != 'Z' for m in settlement['remaining_members']) and native['pid'] == settlement['owned_pgid'] == settlement['owned_sid'] and settlement['native_returncode'] == 0, 'actual settled native process identity')
        for stream in ('stdout', 'stderr'):
            pin(directory/(stream+'.raw'), native[stream])
        need(raw(directory/'stderr.raw') == b'', 'declared empty native stderr')
        if native['argv'][0] == '/usr/bin/cmp':
            need(raw(native['argv'][-2]) == raw(native['argv'][-1]) and raw(directory/'stdout.raw') == b'', 'actual full native raw comparison inputs')
        native_count += 1
    if stage in ('outer', 'launcher'):
        child = 'launcher' if stage == 'outer' else 'recorder'
        need(len(commands) == 1 and commands[0]['label'] == '01_'+child and commands[0]['argv'] == argv(child), 'exact actual envelope child launch')
    elif stage.startswith('child'):
        need(not commands, 'scientific child no native command creation')

recorder = doc(attempt/'recorder/RESULT.json')
labels = ['00_copy_0', '00_copy_1', '01_ldd_before', '03_verify_01']
if mode == 'pair':
    labels += ['03_verify_02', '04_canonical_1', '04_canonical_2', '05_pair']
labels += ['06_ldd_after']
need([row['label'] for row in recorder['commands']] == labels, 'exact ordered recorder native census')
for label in ('01_ldd_before', '06_ldd_after'):
    directory = attempt/'recorder/commands'/label
    native = doc(directory/'RECEIPT.json')
    need(native['argv'] == ['/usr/bin/ldd']+lock['ldd_targets'], 'exact linkage targets')
    data = raw(directory/'stdout.raw')
    need(b'not found' not in data, 'no unresolved ELF input')
    linked = sorted({os.fsdecode(p) for p in re.findall(rb'(/[^\s()]+)', data) if Path(os.fsdecode(p)).is_file()})
    need(linked == lock['ldd_paths'] and all(p in known for p in linked), 'complete actual prefrozen linkage membership')
streams = recorder['output']['raw_stdout']
need(len(streams) == (1 if mode == 'initial' else 2) and recorder['output']['actual_raw_comparisons'] == (0 if mode == 'initial' else 3), 'initial/pair output distinction')
for index, row in enumerate(streams, 1):
    wanted = attempt/'recorder/commands'/('03_verify_'+str(index).zfill(2))/'stdout.raw'
    need(row['path'] == str(wanted), 'literal scientific stdout locator')
    pin(wanted, row)
    native = doc(wanted.with_name('RECEIPT.json'))
    need(native['argv'] == argv('child'+str(index).zfill(2)) and native['cwd'] == str(capsule), 'exact actual science native argv/cwd')
    science = doc(wanted)
    need(set(science) == set(binding['schema']['top_keys']), 'exact role-A output keys')
    need(bool(binding['schema']['equalities']), 'nonempty root-reviewed role-A schema')
    for predicate in binding['schema']['equalities']:
        value = science
        for key in predicate['path']:
            value = value[key]
        need(value == predicate['value'], ('exact role-A equality locator', predicate['path']))
    for predicate in binding['schema']['lengths']:
        value = science
        for key in predicate['path']:
            value = value[key]
        need(len(value) == predicate['value'], ('exact role-A length locator', predicate['path']))
    need(raw(wanted) == (json.dumps(science, sort_keys=True, separators=(',', ':'), allow_nan=False)+'\n').encode(), 'complete role-A compact sorted JSON raw bytes')
if mode == 'pair':
    need(raw(streams[0]['path']) == raw(streams[1]['path']) == raw(binding['canonical']['path']), 'entire actual pair/canonical raw bytes')
else:
    # The root's initial inspection occurred before adoption. We do not rerun
    # or counterfeit that historical absence: verify its exact recorded transition.
    adoption_folder = binding_path.parent/'ADOPTION'
    need(len(manifest(adoption_folder)) == 6, 'complete original adoption payload')
    adoption = doc(adoption_folder/'RESULT.json')
    started = doc(adoption_folder/'ADOPTION_ATTEMPT.json')
    need(started['target_lexisted_before'] is False and
         started['source'] == adoption['source'] == streams[0]['path'] and
         started['target'] == adoption['target'] == binding['canonical']['path'],
         'recorded absent-to-exclusive-canonical transition')
    need(adoption['status'] == 'ROOT_A_CANONICAL_ADOPTED_FROM_COMPLETE_ACTUAL_INITIAL_STDOUT'
         and adoption['scientific_producer_invocations'] == 0 and adoption['native_comparisons'] == 1
         and adoption['strict_pair_completed'] is False, 'exact original adoption phase')
    pin(adoption['source'], started['approved_source'])
    pin(adoption['target'], adoption)
    need(raw(adoption['source']) == raw(adoption['target']), 'all adopted canonical raw bytes')
    pin(binding_path.parent/'PRODUCTION_RECORDS_NATIVE01.json', started['production_native_pin'])
    pin(binding_path.parent/'OUTPUT_SEMANTICS_NATIVE01.json', started['semantic_native_pin'])
    adopted_native = doc(binding_path.parent/'ADOPTION_NATIVE01.json')
    need(adopted_native['exit_code'] == 0 and json.loads(adopted_native['output']) == adoption,
         'actual root adoption tool result')
    comparison = doc(adoption_folder/'CMP_RECEIPT.json')
    attempted_comparison = doc(adoption_folder/'CMP_ATTEMPT.json')
    need(comparison['argv'] == ['/usr/bin/cmp', '--', adoption['source'], adoption['target']]
         and comparison['cwd'] == str(ROOT) and comparison['environment'] == ENV
         and comparison['exit_code'] == 0 and comparison['timeout_seconds'] == 30
         and comparison['stdin'] == 'DEVNULL', 'actual original adoption cmp')
    need(attempted_comparison == {key: comparison[key] for key in attempted_comparison},
         'entire adoption native attempt/receipt relation')
    need(started['started_epoch'] <= comparison['started_epoch'] <= comparison['ended_epoch']
         <= adoption['completed_epoch'], 'recorded adoption event order')
    for stream in ('stdout', 'stderr'):
        body = raw(adoption_folder/('cmp.'+stream+'.raw'))
        need(body == b'' and identity(body) == comparison[stream], 'complete actual adoption raw streams')
all_rows = manifest(attempt)
need(len(all_rows) == (77 if mode == 'initial' else 104) and native_count == (7 if mode == 'initial' else 11), 'complete physical output/native population')
parts = [capture['result']]+[row['result'] for row in capture.get('polls', [])]
need(parts[-1]['exit_code'] == 0 and not parts[-1].get('session_id'), 'actual product-boundary completion')
need(capture['request']['workdir'] == str(ROOT), 'actual product cwd')
launch = ['/usr/bin/env', '-i']+[key+'='+value for key, value in ENV.items()]+argv('outer')
need(capture['request']['cmd'] == ' '.join(launch), 'entire actual product launch command')
messages = [json.loads(line) for line in ''.join(p['output'] for p in parts).splitlines()]
need(messages and all(row.get('status') == 'P211_OWNED_NATIVE_RUNNING' for row in messages[:-1]), 'only known envelope progress before final control')
need(messages[-1] == {'attempt': str(attempt), 'seal': {'manifest': identity(raw(attempt/'SHA256SUMS')), 'payloads': len(all_rows)}, 'status': 'PASS'}, 'entire product control/physical seal relation')

# Complete original binding records and full unchanged current key, not selected hashes.
binding_inputs = doc(binding_path.parent/'INPUTS_AT_BINDING.json')
need(len(binding_inputs) == (226 if mode == 'initial' else 244), 'entire original binding key population')
for path, item in binding_inputs.items():
    need(pin(path, item) == item, ('entire original rich binding pin', path))
binding_manifest = manifest(binding_path.parent)
need(len(binding_manifest) == (17 if mode == 'initial' else 10), 'entire sealed binding package')
prior_native = doc(binding_path.parent/'PRODUCTION_RECORDS_NATIVE01.json')
need(prior_native['exit_code'] == 0, 'actual accepted original root record inspection')
prior_result = json.loads(prior_native['output'])
need(prior_result['status'] == 'PASS_ROOT_COMPLETE_A_PRODUCTION_RECORDS'
     and prior_result['mode'] == mode and prior_result['attempt'] == str(attempt)
     and prior_result['raw_stdout'] == streams and prior_result['complete_payloads'] == len(all_rows)
     and prior_result['native_commands'] == native_count
     and prior_result['complete_manifest'] == identity(raw(attempt/'SHA256SUMS'))
     and prior_result['binding'] == {'path': str(binding_path), **rich(binding_path)},
     'entire original result-to-actual-package relation')
semantic_results, carrier_census = [], []
for index, row in enumerate(streams, 1):
    saved_native = doc(binding_path.parent/('OUTPUT_SEMANTICS_NATIVE'+str(index).zfill(2)+'.json'))
    need(saved_native['exit_code'] == 0, 'actual accepted saved-output semantic inspection')
    saved = json.loads(saved_native['output'])
    need(saved['status'] == 'PASS_FULL_SAVED_A_OUTPUT_SEMANTICS'
         and saved['saved_output'] == row['path']
         and {key: saved[key] for key in ('sha256', 'bytes')} == identity(raw(row['path']))
         and saved['binding_sha256'] == identity(raw(binding_path))['sha256']
         and saved['inspector_sha256'] == identity(raw(QA/'p211_a_root_reception/inspect_saved_output.py'))['sha256']
         and saved['scientific_producer_invocations'] == 0
         and saved['actual_A_check_total'] == 30951, 'full saved-output semantic reuse key')
    whole = doc(row['path'])
    census = [{'n': box['n'], 'vertices': box['vertex_count'],
               'image_targets': len(box['image_vertex_ids']),
               'zero_targets': len(box['zero_fibre_vertex_ids']),
               'height': box['height'], 'actual_A_checks': box['check_total']}
              for box in whole['carriers']]
    need(saved['carriers'] == census and whole['check_total'] == 30951
         and sum(box['vertex_count'] for box in whole['carriers']) == 2353,
         'complete original semantic census and saved output')
    semantic_results.append(saved)
    carrier_census.append(census)
if mode == 'pair':
    initial_path = QA/'p211_a_initial_binding/BINDING.json'
    initial = doc(initial_path)
    delta = {key: {'before': initial[key], 'after': binding[key]}
             for key in initial if initial[key] != binding[key]}
    need(set(initial) == set(binding) and
         set(delta) == {'mode', 'attempt', 'canonical', 'schema', 'provenance_inputs', 'root_canonical_policy'}
         and doc(binding_path.parent/'EXACT_INITIAL_TO_PAIR_DELTA.json') == delta,
         'entire exact initial-to-pair binding delta')
    for field in ('capsule_files', 'declared_imports', 'local_helper_imports', 'runtime_lock',
                  'adapter_sources', 'timeouts', 'argv_template', 'parameter_locator'):
        need(initial[field] == binding[field], ('unchanged scientific/runtime dependency', field))
# Preserve the complete key and reread every consumed file. No submitted program ran.
read_inputs = {p: {**identity(data), 'resolved': str(Path(p).resolve(strict=True)),
                  'symlink': os.readlink(p) if Path(p).is_symlink() else None}
               for p, data in sorted(READS.items())}
for p, expected in read_inputs.items():
    need(rich(p) == expected, ('entire final rich read-set unchanged', p))
result = {'status': 'PASS_A_REVIEWER_RUNTIME_ORIGINAL_RECEPTION', 'mode': mode,
    'binding': {'path': str(binding_path), **rich(binding_path)}, 'attempt': str(attempt),
    'checks': CHECKS, 'actual_read_paths': len(read_inputs), 'complete_payloads': len(all_rows),
    'complete_manifest': identity(raw(attempt/'SHA256SUMS')), 'stage_payloads': counts,
    'binding_payloads': len(binding_manifest), 'binding_original_inputs': len(binding_inputs),
    'native_commands': native_count, 'actual_A_invocations_received': len(streams),
    'actual_pair_comparisons_received': 0 if mode == 'initial' else 3,
    'raw_stdout': streams, 'original_root_record_reception': prior_result,
    'original_root_semantic_receptions': semantic_results, 'saved_census': carrier_census,
    'new_scientific_producer_invocations': 0, 'new_builds': 0, 'new_native_commands_from_receiver': 0,
    'initial_absence_scope': 'Original pre-adoption root assertion reused with complete exclusive-adoption attempt, result, pin and cmp transition; present canonical is not falsely called absent.',
    'reuse': 'Full root record-auditor mechanics adapted only for reviewer output and historical initial adoption; saved-output semantics explicitly reused under complete unchanged key, not a new scientific or semantic production.'}
result['checks'] = CHECKS
output_folder.mkdir()
for name, value in (('READ_INPUTS.json', read_inputs), ('RESULT.json', result)):
    with (output_folder/name).open('xb') as stream:
        stream.write((json.dumps(value, sort_keys=True, indent=2, allow_nan=False)+'\n').encode())
print(json.dumps({'status': result['status'], 'mode': mode, 'checks': CHECKS,
                  'actual_read_paths': len(read_inputs), 'output_folder': str(output_folder),
                  'result_sha256': sha256((output_folder/'RESULT.json').read_bytes()).hexdigest(),
                  'new_scientific_producer_invocations': 0}, sort_keys=True))
