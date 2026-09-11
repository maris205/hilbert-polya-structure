"""Independent root record audit; never imports or executes submitted code."""
import ast
import difflib
from hashlib import sha256
import json
import os
from pathlib import Path
import re

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASE = ROOT/'docs/papers211_215_sequence/qa/p211_runtime_preparation'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
SEAL = '7cd17ff154b1a3b0b0c7ee687863962a9156c9d79e10d7ecb0600dcb95b3a95a'
LOCK_SHA = '1499a93909e39b49c16408985053936b7eb7efcf664e91fd75fa77de607be2ab'
READS = {}
CHECKS = 0
ALIASES = []


def need(value, detail):
    global CHECKS
    CHECKS += 1
    if not value:
        raise AssertionError(detail)


def raw(path):
    path = Path(path)
    need(path.is_file(), ('regular file', str(path)))
    data = path.read_bytes()
    if str(path) in READS:
        need(data == READS[str(path)], ('unchanged read', str(path)))
    READS[str(path)] = data
    return data


def value(data):
    return {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}


def rich(path):
    path = Path(path)
    return {**value(raw(path)), 'resolved': str(path.resolve(strict=True)),
            'symlink': os.readlink(path) if path.is_symlink() else None}


def pinned(path, expected):
    result = rich(path)
    expected = {'sha256': expected} if isinstance(expected, str) else expected
    need(all(result[k] == expected[k] for k in result if k in expected), ('pin', str(path)))
    return result


def doc(path):
    def unique(items):
        result = {}
        for key, item in items:
            need(key not in result, ('duplicate JSON key', str(path), key))
            result[key] = item
        return result
    return json.loads(raw(path), object_pairs_hook=unique)


def pinrows(data, self_name=None):
    need(data.endswith(b'\n'), 'manifest LF')
    rows = {}
    for line in data.decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        need(match is not None, ('manifest syntax', line))
        digest, name = match.groups()
        p = Path(name)
        need(p.parts and not p.is_absolute() and '..' not in p.parts and
             name not in rows and name != self_name, ('manifest path', name))
        rows[name] = digest
    return rows


def manifest(folder, filename='SHA256SUMS'):
    rows = pinrows(raw(folder/filename), filename)
    actual = set()
    for p in folder.rglob('*'):
        need(not p.is_symlink(), ('payload symlink', str(p)))
        if p.is_file():
            actual.add(p.relative_to(folder).as_posix())
    need(actual == set(rows) | {filename}, ('complete nonself inventory', str(folder)))
    for name, pin in rows.items():
        pinned(folder/name, pin)
    return rows


def state(path, with_bytes=True):
    p = Path(path)
    row = {'lexists': os.path.lexists(str(p)), 'exists': p.exists(),
           'is_file': p.is_file(), 'is_dir': p.is_dir(),
           'is_character_device': p.is_char_device(), 'resolved': str(p.resolve()),
           'symlink': os.readlink(p) if p.is_symlink() else None}
    if p.is_char_device():
        info = p.stat()
        row['character_device'] = {'major': os.major(info.st_rdev),
                                  'minor': os.minor(info.st_rdev), 'mode': info.st_mode}
    if with_bytes and p.is_file():
        row.update(value(raw(p)))
    return row


def historical_bytes(path, scope):
    """Resolve changed old executable inputs only through their physical copies."""
    p = Path(path)
    before_path = scope/'SOURCE_INPUTS_BEFORE.json'
    known = doc(before_path) if before_path.is_file() else {}
    pin = known.get(str(p))
    data = raw(p)
    if pin is None or value(data) == {k: pin[k] for k in ('sha256', 'bytes')}:
        return data
    if p == BASE/'REUSE_MAP.json' and scope.name == 'discovery01':
        copy = BASE/'historical_metadata/REUSE_MAP.discovery01.restored.json'
        kind = 'explicit after-the-fact metadata restoration'
    else:
        copy = scope/'source_snapshots'/p.name
        kind = 'actual pre-execution physical source snapshot'
    data = raw(copy)
    need(value(data) == {k: pin[k] for k in ('sha256', 'bytes')}, ('historical source mapping', str(p), str(copy)))
    ALIASES.append({'historical_path': str(p), 'physical_path': str(copy), 'kind': kind, **value(data)})
    return data


pinned(BASE/'MANIFEST.sha256', SEAL)
payloads = manifest(BASE, 'MANIFEST.sha256')
need(len(payloads) == 625, '625 payloads')
need(sum(len(raw(BASE/name)) for name in payloads) == 6178924, 'complete payload byte census')
inputs = pinrows(raw(BASE/'INPUTPINS.sha256'))
need(len(inputs) == 10, 'ten original inputs')
for name, pin in inputs.items():
    pinned(ROOT/name, pin)
nested = {str(p.parent.relative_to(BASE)): len(manifest(p.parent))
          for p in sorted(BASE.rglob('SHA256SUMS'))}
need({k: nested[k] for k in ('discovery01', 'tests01', 'discovery02', 'tests02')} ==
     {'discovery01': 84, 'tests01': 83, 'discovery02': 102, 'tests02': 298}, 'four complete attempt inventories')

for version in ('discovery01', 'tests01', 'discovery02', 'tests02'):
    folder = BASE/version
    before, after = doc(folder/'SOURCE_INPUTS_BEFORE.json'), doc(folder/'SOURCE_INPUTS_AFTER.json')
    need(before == after, ('recorded complete source closure', version))
    for p, pin in before.items():
        data = historical_bytes(p, folder)
        need(value(data) == {k: pin[k] for k in ('sha256', 'bytes')}, ('source-before binding', version, p))
    result = doc(folder/'RESULT.json')
    need(result['scientific_executions'] == 0, ('no scientific execution', version))
    wanted = 'FAIL_PRESERVED' if version == 'tests01' else ('PASS_PREPARATION_ONLY' if version.startswith('discovery') else 'PASS_PURE_INFRASTRUCTURE_TESTS')
    need(result['status'] == wanted, ('actual retained verdict', version))
need(len(doc(BASE/'tests01/RESULT.json')['checks']) == 14, 'first failed 14 checks')
need(len(doc(BASE/'tests02/RESULT.json')['checks']) == 21, 'revised 21 checks')

trees = {name: ast.parse(raw(BASE/name), filename=str(BASE/name)) for name in
         ('runtime_core.py', 'p211_runtime.py', 'prepare_runtime.py', 'test_runtime.py')}
old_tree = ast.parse(raw(BASE/'baseline/p210_b_run_pair.py'))
old_functions = {n.name: n for n in old_tree.body if isinstance(n, ast.FunctionDef)}
new_functions = {n.name: n for n in trees['runtime_core.py'].body if isinstance(n, ast.FunctionDef)}
reuse = doc(BASE/'REUSE_MAP.json')['unchanged_functions']
need(len(reuse) == 14 and set(new_functions) == set(reuse) | {'command'}, 'exact adapted function set')
for name in reuse:
    need(ast.dump(old_functions[name], include_attributes=False) == ast.dump(new_functions[name], include_attributes=False), ('unchanged selected AST', name))
need(ast.dump(old_functions['command']) != ast.dump(new_functions['command']), 'command explicitly adapted')
constants = {}
for node in trees['p211_runtime.py'].body:
    if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
        if node.targets[0].id in ('CONFIG_PATHS', 'MEMBER_DIRS', 'ROLE_IMPORTS', 'IMPORT_PATH', 'NATIVE_FILES'):
            constants[node.targets[0].id] = ast.literal_eval(node.value)
need(constants['ROLE_IMPORTS'] == ['itertools', 'json', 'math', 'sys'], 'declared closed import interface')

lock_path = BASE/'discovery02/RUNTIME_LOCK.json'
pinned(lock_path, LOCK_SHA)
lock = doc(lock_path)
need(lock['format'] == 'p211-bounded-runtime-lock-v1' and len(lock['files']) == 122, 'active bounded lock')
for p, pin in lock['files'].items():
    pinned(p, pin)
paths = set(constants['CONFIG_PATHS'])
paths.update(str(Path(directory)/name) for directory in ('/usr/bin', '/usr/lib') for name in
             ('python._pth', 'python3._pth', 'python310._pth', 'python3.10._pth'))
memberships = {}
for directory in constants['MEMBER_DIRS']:
    p = Path(directory)
    row = {'directory': state(p, False), 'members': {}}
    if p.is_dir():
        row['members'] = {q.name: state(q, False) for q in sorted(p.iterdir())}
        if directory != '/usr/lib/x86_64-linux-gnu/gconv':
            paths.update(str(q) for q in p.iterdir() if q.is_file())
    memberships[directory] = row
need(set(lock['configuration']['paths']) == paths, 'entire declared configuration path selection')
need(lock['configuration']['paths'] == {p: state(p) for p in sorted(paths)}, 'all live configuration states and bytes')
need(lock['configuration']['memberships'] == memberships, 'all declared direct memberships')
loader_lines = [line.strip() for line in raw('/etc/ld.so.conf').decode().splitlines()
                if line.strip() and not line.lstrip().startswith('#')]
need(loader_lines == ['include /etc/ld.so.conf.d/*.conf'], 'literal loader include')
loader = {}
for ptext in paths:
    p = Path(ptext)
    if p.parent == Path('/etc/ld.so.conf.d') and p.is_file():
        for line in raw(p).decode().splitlines():
            clean = line.split('#', 1)[0].strip()
            if clean:
                need(clean.startswith('/') and not any(c in clean for c in '*?[]\t '), 'explicit loader directory')
                loader[clean] = state(clean, False)
need(loader == lock['loader_search_directory_states'] and len(loader) == 9, 'nine live loader directory states')

receipt_paths = sorted(BASE.rglob('commands/*/RECEIPT.json'))
diffs = comparisons = copies = 0
for p in receipt_paths:
    row, attempted = doc(p), doc(p.with_name('ATTEMPT.json'))
    need(row['environment'] == ENV and attempted['status'] == 'ATTEMPTED' and attempted['exit_code'] is None, ('native initial state', str(p)))
    need(all(attempted[k] == row[k] for k in attempted if k not in ('status', 'exit_code')), ('entire native attempt binding', str(p)))
    for stream in ('stdout', 'stderr'):
        pinned(p.with_name(stream+'.raw'), row[stream])
    if row['spawned']:
        s = row['process_group_settlement']
        need(s['quiescent'] and row['pid'] == s['owned_pgid'] == s['owned_sid'] and
             s['native_returncode'] == row['exit_code'] and not any(m['state'] != 'Z' for m in s['remaining_members']), ('native owned settlement', str(p)))
    else:
        need(row['status'] == 'SPAWN_FAILED' and row['exit_code'] is None and row['process_group_settlement'] is None, ('truthful spawn failure', str(p)))
    scope = BASE/p.relative_to(BASE).parts[0]
    argv = row['argv']
    if argv[0] in ('/usr/bin/cmp', '/usr/bin/cp') and row['exit_code'] == 0:
        left, right = (historical_bytes(q, scope) for q in argv[-2:])
        need(left == right, ('actual recorded raw comparison/copy inputs', str(p)))
        need(raw(p.with_name('stdout.raw')) == raw(p.with_name('stderr.raw')) == b'', ('successful comparison/copy streams', str(p)))
        comparisons += argv[0] == '/usr/bin/cmp'
        copies += argv[0] == '/usr/bin/cp'
    if argv[0] == '/usr/bin/diff':
        left, right = (historical_bytes(q, scope) for q in argv[-2:])
        expected = ''.join(difflib.unified_diff(left.decode().splitlines(keepends=True), right.decode().splitlines(keepends=True), fromfile=argv[-2], tofile=argv[-1])).encode()
        actual = raw(p.with_name('stdout.raw'))
        need(row['exit_code'] == 1 and raw(p.with_name('stderr.raw')) == b'', ('expected real diff exit', str(p)))
        headers = actual.splitlines(keepends=True)[:2]
        need(headers[0].startswith(('--- '+argv[-2]+'\t').encode()) and headers[1].startswith(('+++ '+argv[-1]+'\t').encode()), ('native diff actual header paths', str(p)))
        need(b''.join(actual.splitlines(keepends=True)[2:]) == b''.join(expected.splitlines(keepends=True)[2:]), ('complete unified source diff body', str(p)))
        diffs += 1
for p in sorted(BASE.rglob('RESULT.json')):
    result = doc(p)
    if isinstance(result.get('commands'), list):
        recorded = {r['label']: r for r in result['commands']}
        actual = {q.parent.name: doc(q) for q in p.parent.glob('commands/*/RECEIPT.json')}
        need(set(recorded) == set(actual), ('complete result native census', str(p)))
        need(all({k: row[k] for k in actual[name]} == actual[name] for name, row in recorded.items()), ('result-to-native full binding', str(p)))

test = BASE/'tests02'
need(len(list(test.rglob('commands/*/RECEIPT.json'))) == 41 and len(list(test.rglob('commands/*/ATTEMPT.json'))) == 43, 'complete revised native census')
unfinalized = sorted(test.rglob('commands/*/UNFINALIZED_NATIVE.json'))
need(len(unfinalized) == 2, 'two disclosed exception branches')
for p in unfinalized:
    need(not p.with_name('RECEIPT.json').exists() and doc(p)['output_hashes_not_finalized'] is True, ('no invented native completion', str(p)))
injected = doc(test/'INJECTED_SETTLEMENT_TEST.json')
need(injected['code_under_test_refused_its_seal'] and all(r['quiescent'] and not r['remaining_members'] for r in injected['actual_settlement']), 'test-only actual settlement justification')
need('Not an actual escaped or unkillable' in injected['limitation'], 'fault injection limitation')

fixture_stages = []
for mode in ('initial', 'pair'):
    binding_path = test/(mode+'.binding.json')
    binding = doc(binding_path)
    attempt = test/('fixture_'+mode)
    need(binding['approved'] is True and binding['purpose'] == 'INFRASTRUCTURE_TEST_ONLY' and binding['role'] == 'infra_fixture', 'toy-only binding')
    need(binding['runtime_lock']['sha256'] == LOCK_SHA, 'fixture actually used revised lock')
    for stage in ('outer', 'launcher', 'recorder', 'child01') + (('child02',) if mode == 'pair' else ()):
        folder = attempt/stage
        result = doc(folder/'RESULT.json')
        need(result['status'] == 'PASS' and result['errors'] == [] and not result['unfinalized_native'] and not result['unknown_descendant_closure'], ('closed fixture stage', mode, stage))
        before = doc(folder/('INPUTS_BEFORE_SCIENCE.json' if stage == 'recorder' else 'INPUTS_BEFORE.json'))
        need(before == doc(folder/'INPUTS_AFTER.json'), ('complete fixture input closure', mode, stage))
        for p, pin in before.items():
            pinned(p, pin)
        wanted_argv = ['/usr/bin/python3.10', '-I', '-S', '-B', '-X', 'pycache_prefix='+str(attempt/('never_created_'+stage+'_cache')), str(BASE/'p211_runtime.py'), stage, str(binding_path), value(raw(binding_path))['sha256'], str(attempt)]
        need(doc(folder/'ENTERED.json')['orig_argv'] == wanted_argv, ('full original fixture argv', mode, stage))
        for phase in ('BEFORE', 'AFTER'):
            sample = doc(folder/('RUNTIME_'+phase+'.json'))
            need(sample['environment'] == ENV and sample['interpreter_argv'] == wanted_argv and sample['sys_path'] == constants['IMPORT_PATH'], ('actual fixture invocation settings', mode, stage, phase))
            need(sample['executable'] == '/usr/bin/python3.10' and not os.path.lexists(sample['pycache_prefix']), 'actual interpreter/cache')
            need(all(flag in sample['flags'] for flag in ('isolated=1', 'no_site=1', 'optimize=0', 'dont_write_bytecode=1')), 'actual source-only flags')
            maps = sample['proc_maps'].encode()
            need(value(maps) == {'sha256': sample['proc_maps_sha256'], 'bytes': sample['proc_maps_bytes']}, 'complete volatile map raw binding')
            for p, pin in list(sample['mapped_files'].items()) + [(m['path'], m) for m in sample['modules'].values()]:
                need(p in before, ('fixture consumed ordinary file in prefrozen key', p))
                pinned(p, pin)
            need(doc(folder/('CONFIGURATION_'+phase+'.json')) == lock['configuration'], 'actual full fixture configuration')
        observed = doc(folder/'OPEN_OBSERVATIONS.json')
        need(observed['events'] == doc(folder/'OPEN_EVENTS_RAW.json'), 'full raw open-event binding')
        for p, pin in observed['ordinary_files'].items():
            need(p in before, ('observed prefrozen ordinary input', p))
            pinned(p, pin)
        for p in observed['absent_cache_probes']:
            need(not os.path.lexists(p), 'absent old-cache probe remains absent')
        fixture_stages.append(mode+':'+stage)
    recorder = doc(attempt/'recorder/RESULT.json')
    need(recorder['output']['actual_raw_comparisons'] == (0 if mode == 'initial' else 3), 'initial and pair distinct output policy')
    for row in recorder['output']['raw_stdout']:
        pinned(row['path'], row)
        need(raw(row['path']) == b'{"fixture_only":true,"value":17}\n', 'complete fixed toy stdout')

calls = doc(BASE/'TOOL_INVOCATIONS.actual.json')['calls']
need(len(calls) == 4, 'four actual helper tool returns')
for call in calls:
    folder = ('discovery' if call['kind'] == 'prepare' else 'tests')+call['attempt']
    control = json.loads(call['completion']['output'])
    result = doc(BASE/folder/'RESULT.json')
    need(control['status'] == result['status'] and (call['completion']['exit_code'] == 0) == (result['errors'] == []), ('actual helper completion', folder))
    need(control['seal']['manifest'] == value(raw(BASE/folder/'SHA256SUMS')), ('actual helper final manifest return', folder))
need(doc(BASE/'BINDING.pending.json')['approved'] is False, 'production still disabled')

for p, before in list(READS.items()):
    need(Path(p).read_bytes() == before, ('final entire read-set unchanged', p))
print(json.dumps({'status': 'PASS_ROOT_RUNTIME_PREPARATION_RECEPTION',
    'checks': CHECKS, 'distinct_files_read': len(READS), 'complete_payloads': 625,
    'complete_payload_bytes': 6178924, 'preparation_manifest_sha256': SEAL,
    'original_pins': len(inputs), 'nested_complete_manifests': nested,
    'active_lock': {'sha256': LOCK_SHA, 'file_keys': 122, 'loader_directory_states': 9},
    'native_receipts_checked': len(receipt_paths), 'decoded_complete_diff_bodies': diffs,
    'raw_cmp_bindings': comparisons, 'raw_copy_bindings': copies,
    'fixture_stages': fixture_stages, 'historical_source_resolutions': ALIASES,
    'submitted_code_imports_or_executions': 0, 'new_scientific_producer_invocations': 0,
    'scope': 'Original complete byte sets, selected AST equality, saved native bindings and live bounded runtime/configuration closure. Not fresh fixture execution, OS tracing or manuscript review.'}, sort_keys=True, indent=2))
