#!/usr/bin/python3.10
"""Independent saved-evidence inspection. Never imports submitted source.

Read scope is an explicit infrastructure-only selection. In particular, pins
pointing to manuscripts, science, baselines or host runtime files are NOT
followed. New native commands compare selected existing pure-infra files only.
"""
import ast
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
PREP = ROOT / 'docs/papers211_215_sequence/qa/p211_runtime_preparation'
OUT = Path(__file__).resolve().parent
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
reads = {}
checks = []


def require(test, label):
    if not test:
        raise AssertionError(label)
    checks.append(label)


def identity(data):
    return {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}


def write(name, data):
    p = OUT / name
    assert p.is_relative_to(OUT) and not p.exists()
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('xb') as stream:
        stream.write(data)


def dump(name, data):
    write(name, (json.dumps(data, sort_keys=True, indent=2) + '\n').encode())


def read(path):
    p = Path(path)
    assert p in selected, ('outside explicit infrastructure read scope', str(p))
    assert p.is_file() and not p.is_symlink()
    data = p.read_bytes()
    row = identity(data)
    if str(p) in reads:
        assert reads[str(p)] == row, ('read changed', str(p))
    reads[str(p)] = row
    return data


def document(path):
    return json.loads(read(path))


def manifest(path, expected_count=None, require_entire=True):
    raw = read(path)
    require(raw.endswith(b'\n'), 'manifest LF: ' + str(path))
    rows = {}
    for line in raw.decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        assert match, ('manifest line', str(path))
        digest, name = match.groups()
        p = Path(name)
        assert name not in rows and name != path.name and not p.is_absolute() and '..' not in p.parts
        rows[name] = digest
    if expected_count is not None:
        require(len(rows) == expected_count, 'manifest count: ' + str(path))
    if require_entire:
        actual = {p.relative_to(path.parent).as_posix() for p in path.parent.rglob('*') if p.is_file()}
        require(set(rows) == actual - {path.name}, 'complete manifest inventory: ' + str(path))
    checked = 0
    for name, digest in rows.items():
        p = path.parent / name
        if p in selected:
            require(identity(read(p))['sha256'] == digest, 'payload digest: ' + str(p))
            checked += 1
        elif require_entire:
            raise AssertionError(('unselected required payload', str(p)))
    return {'declared_payloads': len(rows), 'selected_verified_payloads': checked}


controls = [ROOT / p for p in ('.agents/skills/symbolic-dynamics-research/SKILL.md',
    'docs/research_state/WORKFLOW.md', 'SYMBOLIC_DYNAMICS_STATE.md',
    'docs/papers211_215_sequence/PIPELINE_STATE.md')]
main_names = ['HANDOFF.md', 'PLAN.md', 'runtime_core.py', 'p211_runtime.py',
              'prepare_runtime.py', 'test_runtime.py', 'final_checks.py',
              'REUSE_MAP.json', 'BINDING.pending.json', 'MANIFEST.sha256',
              'discovery02/RUNTIME_LOCK.json']
selected = set(controls + [PREP / p for p in main_names])
for folder in ('fixtures', 'tests02', 'final_checks01'):
    selected.update(p for p in (PREP / folder).rglob('*') if p.is_file())
for name in ('RESULT.json', 'STATIC_CHECK.json', 'RUNTIME_INPUTS_BEFORE.json', 'RUNTIME_INPUTS_AFTER.json'):
    selected.add(PREP / 'discovery02' / name)
for stage in ('outer', 'launcher', 'recorder', 'child'):
    selected.update(p for p in (PREP / ('discovery02/commands/03_probe_' + stage)).iterdir() if p.is_file())

for p in sorted(selected):
    read(p)
dump('READ_INPUTS_BEFORE.json', reads)

require(identity(read(PREP / 'MANIFEST.sha256'))['sha256'] ==
        '7cd17ff154b1a3b0b0c7ee687863962a9156c9d79e10d7ecb0600dcb95b3a95a', 'parent preparation manifest pin')
require(identity(read(PREP / 'discovery02/RUNTIME_LOCK.json'))['sha256'] ==
        '1499a93909e39b49c16408985053936b7eb7efcf664e91fd75fa77de607be2ab', 'parent lock pin')
manifests = {'preparation_selected_only': manifest(PREP / 'MANIFEST.sha256', 625, False)}
for p in sorted(selected):
    if p.name == 'SHA256SUMS':
        manifests[p.relative_to(PREP).as_posix()] = manifest(p)

source_ast = {}
for name in ('runtime_core.py', 'p211_runtime.py', 'prepare_runtime.py', 'test_runtime.py',
             'final_checks.py', 'fixtures/verify_fixture.py', 'fixtures/pre_spawn_refusal.py'):
    tree = ast.parse(read(PREP / name), filename=str(PREP / name))
    source_ast[name] = {'functions': [n.name for n in tree.body if isinstance(n, ast.FunctionDef)],
                        'lines': len(read(PREP / name).splitlines())}
pending = document(PREP / 'BINDING.pending.json')
require(pending['approved'] is False and pending['attempt'] is None, 'pending binding genuinely disabled')
lock = document(PREP / 'discovery02/RUNTIME_LOCK.json')
require(lock['format'] == 'p211-bounded-runtime-lock-v1', 'lock format')
require(len(lock['files']) == 122 and len(lock['loader_search_directory_states']) == 9, 'bounded lock census')
require(lock['declared_imports'] == ['itertools', 'json', 'math', 'sys'], 'standalone declared import interface')
require(document(PREP / 'discovery02/RUNTIME_INPUTS_BEFORE.json') == lock['files'] ==
        document(PREP / 'discovery02/RUNTIME_INPUTS_AFTER.json'), 'saved runtime full input pair equals lock')
for name in ('runtime_core.py', 'p211_runtime.py'):
    require(all(lock['files'][str(PREP / name)][k] == v for k, v in identity(read(PREP / name)).items()),
            'current execution source equals lock: ' + name)
device = lock['configuration']['paths']['/dev/null']
require(device['is_character_device'] and device['character_device']['major'] == 1 and
        device['character_device']['minor'] == 3 and '/dev/null' not in lock['files'], 'separate DEVNULL device role')
require(all(not p.endswith(('.pyc', '.pyo')) for p in lock['files']), 'no lock bytecode file keys')

receipts = sorted(p for p in selected if p.name == 'RECEIPT.json')
native_census = []
for p in receipts:
    row = document(p)
    attempted = document(p.with_name('ATTEMPT.json'))
    require(attempted['status'] == 'ATTEMPTED' and attempted['exit_code'] is None and
            all(row[k] == v for k, v in attempted.items() if k not in ('status', 'exit_code')),
            'native attempted/full receipt binding: ' + str(p))
    require(row['environment'] == ENV and row['ended_epoch'] >= row['started_epoch'], 'native environment/epochs: ' + str(p))
    for stream in ('stdout', 'stderr'):
        require(identity(read(p.with_name(stream + '.raw'))) == row[stream], 'raw native stream pin: ' + str(p) + ':' + stream)
    if row['spawned']:
        settlement = row['process_group_settlement']
        require(settlement['quiescent'] and settlement['owned_pgid'] == settlement['owned_sid'] == row['pid'] and
                settlement['native_returncode'] == row['exit_code'], 'saved owned-group closure: ' + str(p))
    else:
        require(row['status'] == 'SPAWN_FAILED' and row['exit_code'] is None and not row['streams_complete'] and
                row['process_group_settlement'] is None, 'saved actual spawn failure: ' + str(p))
    native_census.append({'path': p.relative_to(PREP).as_posix(), 'argv': row['argv'], 'status': row['status'],
                         'exit_code': row['exit_code'], 'stdout': row['stdout'], 'stderr': row['stderr']})

test = document(PREP / 'tests02/RESULT.json')
require(test['status'] == 'PASS_PURE_INFRASTRUCTURE_TESTS' and not test['errors'] and len(test['checks']) == 21,
        'saved 21 pure-infrastructure predicates')
require(len([p for p in receipts if p.is_relative_to(PREP / 'tests02')]) == 41, 'tests02 receipt count 41')
require(len([p for p in selected if p.name == 'ATTEMPT.json' and p.is_relative_to(PREP / 'tests02')]) == 43,
        'tests02 attempt count 43')
unfinalized = sorted(p for p in selected if p.name == 'UNFINALIZED_NATIVE.json')
require(len(unfinalized) == 2 and all(not p.with_name('RECEIPT.json').exists() for p in unfinalized),
        'two deliberately unfinalized branches have no native receipt')
require(all(document(p)['output_hashes_not_finalized'] for p in unfinalized), 'unfinalized streams not internally relabelled final')
require(document(PREP / 'tests02/INJECTED_SETTLEMENT_TEST.json')['actual_settlement'][0]['quiescent'],
        'withheld-settlement test has separate actual settlement, not escaped writer test')

stages = []
for mode in ('initial', 'pair'):
    attempt = PREP / ('tests02/fixture_' + mode)
    bindpath = PREP / ('tests02/' + mode + '.binding.json')
    binding = document(bindpath)
    require(binding['role'] == 'infra_fixture' and binding['purpose'] == 'INFRASTRUCTURE_TEST_ONLY', 'fixture-only binding ' + mode)
    for stage in ('outer', 'launcher', 'recorder', 'child01') + (('child02',) if mode == 'pair' else ()):
        p = attempt / stage
        before = document(p / ('INPUTS_BEFORE_SCIENCE.json' if stage == 'recorder' else 'INPUTS_BEFORE.json'))
        require(before == document(p / 'INPUTS_AFTER.json'), 'full layer input equality ' + mode + ':' + stage)
        result = document(p / 'RESULT.json')
        require(result['status'] == 'PASS' and result['wrapper_return'] == 0 and not result['errors'] and
                not result['unknown_descendant_closure'] and not result['unfinalized_native'], 'closed successful layer ' + mode + ':' + stage)
        expected_argv = ['/usr/bin/python3.10', '-I', '-S', '-B', '-X',
            'pycache_prefix=' + str(attempt / ('never_created_' + stage + '_cache')),
            str(PREP / 'p211_runtime.py'), stage, str(bindpath), identity(read(bindpath))['sha256'], str(attempt)]
        entered = document(p / 'ENTERED.json')
        require(entered['orig_argv'] == expected_argv, 'exact original Python argv ' + mode + ':' + stage)
        for phase in ('BEFORE', 'AFTER'):
            require(document(p / ('CONFIGURATION_' + phase + '.json')) == lock['configuration'], 'exact lock config ' + mode + ':' + stage + ':' + phase)
            sample = document(p / ('RUNTIME_' + phase + '.json'))
            require(sample['environment'] == ENV and sample['interpreter_argv'] == expected_argv and
                    sample['executable'] == '/usr/bin/python3.10' and not sample['cache_lexists'] and
                    sample['sys_path'] == ['/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload'],
                    'ENV4 argv path cache sample ' + mode + ':' + stage + ':' + phase)
            require(all(token in sample['flags'] for token in ('isolated=1', 'no_site=1', 'optimize=0', 'dont_write_bytecode=1')),
                    'I S B unoptimized sample ' + mode + ':' + stage + ':' + phase)
            require(identity(sample['proc_maps'].encode()) == {'sha256': sample['proc_maps_sha256'], 'bytes': sample['proc_maps_bytes']},
                    'full saved maps bytes ' + mode + ':' + stage + ':' + phase)
            sampled = list(sample['mapped_files'].items()) + [(m['path'], m) for m in sample['modules'].values()]
            require(all(path in before and all(before[path][k] == row[k] for k in ('sha256', 'bytes')) for path, row in sampled),
                    'saved runtime sample entire frozen membership ' + mode + ':' + stage + ':' + phase)
        observations = document(p / 'OPEN_OBSERVATIONS.json')
        require(observations['events'] == document(p / 'OPEN_EVENTS_RAW.json'), 'full raw open event relation ' + mode + ':' + stage)
        stages.append(mode + ':' + stage)

final = document(PREP / 'final_checks01/RESULT.json')
require(final['status'] == 'PASS_DOCUMENTARY_CHECKS' and not final['errors'], 'saved author final-check status')
require(final['checks']['closed_fixture_stages'] == stages, 'saved final-check exact nine stages')

# All new native commands are byte comparisons of infrastructure already read.
comparisons = []
for name in ('runtime_core.py', 'p211_runtime.py', 'test_runtime.py', 'BINDING.pending.json'):
    comparisons.append((PREP / name, PREP / 'tests02/source_snapshots' / name))
canonical = PREP / 'tests02/CANONICAL.fixture.json'
streams = [PREP / p for p in ('tests02/fixture_initial/recorder/commands/03_verify_01/stdout.raw',
    'tests02/fixture_pair/recorder/commands/03_verify_01/stdout.raw',
    'tests02/fixture_pair/recorder/commands/03_verify_02/stdout.raw')]
comparisons.extend((p, canonical) for p in streams)
comparisons.append((streams[1], streams[2]))
new_native = []
for index, (first, second) in enumerate(comparisons):
    assert first in selected and second in selected
    argv = ['/usr/bin/cmp', '--', str(first), str(second)]
    label = 'native/' + str(index).zfill(2) + '_cmp'
    started = time.time()
    dump(label + '/ATTEMPT.json', {'argv': argv, 'cwd': str(ROOT), 'environment': ENV, 'started_epoch': started,
                                'operation': 'fresh read-only infrastructure byte comparison', 'timeout_seconds': 30})
    result = subprocess.run(argv, cwd=ROOT, env=ENV, stdin=subprocess.DEVNULL, capture_output=True, timeout=30)
    write(label + '/stdout.raw', result.stdout)
    write(label + '/stderr.raw', result.stderr)
    receipt = {'argv': argv, 'cwd': str(ROOT), 'environment': ENV, 'started_epoch': started,
               'ended_epoch': time.time(), 'exit_code': result.returncode,
               'stdout': identity(result.stdout), 'stderr': identity(result.stderr),
               'scope': 'Real cmp process completed; not a scientific execution or hermetic runtime test.'}
    dump(label + '/RECEIPT.json', receipt)
    new_native.append(receipt)
    require(result.returncode == 0 and result.stdout == result.stderr == b'', 'fresh raw cmp ' + str(index))

after = {str(p): identity(p.read_bytes()) for p in sorted(selected)}
require(after == reads, 'entire explicit read input set unchanged')
dump('READ_INPUTS_AFTER.json', after)
dump('CHECKS.json', checks)
dump('SAVED_NATIVE_CENSUS.json', native_census)
summary = {'status': 'PASS_BOUNDED_INFRASTRUCTURE_ORIGINAL_INSPECTION',
           'scope': 'Independent static infrastructure reading and saved-evidence integrity; zero submitted-script execution/import, science reading, science execution, build or manuscript review.',
           'input_files': len(reads), 'input_bytes': sum(row['bytes'] for row in reads.values()),
           'checks': len(checks), 'manifests': manifests, 'source_AST_inventory_only': source_ast,
           'saved_native_receipts': len(receipts), 'closed_fixture_stages': stages, 'fresh_cmp_commands': len(new_native),
           'whole_preparation_manifest_claim': 'Pinned 625-line manifest; only explicitly selected payloads verified here. Root separately audits all originals.',
           'host_lock_recapture': False, 'external_pin_referents_followed': False,
           'finished_utc': datetime.now(timezone.utc).isoformat()}
dump('RESULT.json', summary)
print(json.dumps(summary, sort_keys=True))
