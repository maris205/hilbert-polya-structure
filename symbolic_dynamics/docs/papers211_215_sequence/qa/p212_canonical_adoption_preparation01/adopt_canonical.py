"""Disabled-by-default P212 raw adoption source; root must bind a new one-use approval.

Authorship: P212 verifier/manuscript contributor, not an independent reviewer.
Derived from the received P211-B exclusive xb/fsync/native-cmp mechanism.
This is document/adoption infrastructure, never a scientific producer.
"""
from hashlib import sha256
import json
import os
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers211_215_sequence/qa'
PREP = QA / 'p212_canonical_adoption_preparation01'
PAPER = ROOT / 'papers/212-closed-pointer-orbits'
TARGET = PAPER / 'CANONICAL.json'
ALIAS = PAPER / 'canonical.stdout.json'
SOURCE = QA / 'root_replays/p212_author_initial_01/recorder/commands/03_verify_01/stdout.raw'
EXPECTED = {'bytes': 12501943, 'sha256': '1a32be6bb36dd8b4b27b9891a42876fe235bf2555a3dd9f4e36195a6ad72676c'}
SEMANTIC = QA / 'p212_saved_output_root_reception01'
RUNTIME = QA / 'p212_author_initial_runtime_reception01'
ROOT_GATE = QA / 'p212_canonical_adoption_root01'
BINDING_PATH = ROOT_GATE / 'BINDING.json'
OUT = ROOT_GATE / 'adoption01'
ENV4 = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}


def require(condition, label):
    if not condition:
        raise RuntimeError(label)


def identity(data):
    return {'bytes': len(data), 'sha256': sha256(data).hexdigest()}


def pairs(items):
    result = {}
    for key, value in items:
        require(key not in result, 'duplicate JSON key')
        result[key] = value
    return result


def decode(data):
    return json.loads(data, object_pairs_hook=pairs)


def safe(path, exists=True, directory=False):
    path = Path(path)
    require(path.is_absolute() and str(path) == os.path.normpath(str(path)), 'noncanonical path')
    require(path == ROOT or ROOT in path.parents, 'outside workspace')
    # Reject all workspace ancestor aliases; do not inspect unrelated host paths.
    for ancestor in reversed((path,) + tuple(path.parents)):
        if ancestor == ROOT or ROOT in ancestor.parents:
            if ancestor == path and not exists:
                require(not os.path.lexists(ancestor), 'output already lexists')
            else:
                require(not ancestor.is_symlink(), 'workspace alias')
                require(ancestor.exists(), 'missing input/ancestor')
                if ancestor != path or directory:
                    require(ancestor.is_dir(), 'not directory')
    require(not exists or directory or path.is_file(), 'not regular input')
    require(path.resolve() == path, 'resolved path differs')
    return path


def read(path):
    return safe(path).read_bytes()


def pin(path):
    path = safe(path)
    return {**identity(path.read_bytes()), 'resolved': str(path), 'symlink': None}


def pinned(record):
    require(set(record) == {'path', 'bytes', 'sha256', 'resolved', 'symlink'}, 'rich pin shape')
    require(pin(record['path']) == {key: value for key, value in record.items() if key != 'path'}, 'input pin changed')
    return read(record['path'])


def tree(directory):
    directory = safe(directory, directory=True)
    files, directories = {}, []
    def visit(current):
        for child in sorted(current.iterdir()):
            require(not child.is_symlink(), 'tree symlink')
            relative = str(child.relative_to(directory))
            if child.is_dir():
                directories.append(relative)
                visit(child)
            else:
                files[relative] = pin(child)
    visit(directory)
    return {'files': files, 'directories': sorted(directories)}


def verify_inventory(inventory, adopted=False):
    require(inventory['schema'] == 'p212-adoption-workspace-inputs-v1', 'inventory schema')
    require(inventory['host_paths_dereferenced'] == 0, 'not workspace-only inventory')
    for directory, expected in inventory['trees'].items():
        actual = tree(directory)
        if adopted and directory == str(PAPER):
            require(actual['files'].pop('CANONICAL.json', None) == {**EXPECTED, 'resolved': str(TARGET), 'symlink': None}, 'canonical addition')
        require(actual == expected, 'exact old tree changed: ' + directory)
    for path, expected in inventory['files'].items():
        require(pin(path) == expected, 'standalone input changed')
    for path in inventory['absent']:
        if not (adopted and path == str(TARGET)):
            safe(path, exists=False)
    require(str(SEMANTIC) in inventory['trees'] and str(RUNTIME) in inventory['trees'], 'reception trees required')
    require(len(inventory['trees'][str(SEMANTIC)]['files']) == 93, 'semantic complete tree')
    require(len(inventory['trees'][str(RUNTIME)]['files']) == 15, 'runtime complete tree')
    # Every listed nonself manifest was accepted as an exact tree at preparation.
    # Whole current file maps above bind manifests, payloads and nested manifests.
    require(inventory['checks']['sealed_payloads']['semantic'] == 92, 'semantic payloads')
    require(inventory['checks']['sealed_payloads']['runtime'] == 14, 'runtime payloads')


def received(native):
    record = decode(read(native))
    parts = [record['result']]
    for item in record.get('polls', []):
        require(item['request']['session_id'] == parts[-1]['session_id'], 'native session chain')
        parts.append(item['result'])
    require(parts[-1].get('exit_code') == 0 and not parts[-1].get('session_id'), 'native not complete zero')
    require(all(part.get('exit_code') is None and part.get('session_id') for part in parts[:-1]), 'intermediate native state')
    return decode(''.join(part['output'] for part in parts))


def write(path, value):
    data = value if isinstance(value, bytes) else (json.dumps(value, sort_keys=True, indent=2) + '\n').encode()
    path = safe(path, exists=False)
    with path.open('xb') as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())


def main():
    require(len(sys.argv) == 5 and sys.argv[1] == '--adopt-once' and sys.argv[2] == str(BINDING_PATH), 'explicit fixed one-use binding required')
    binding_bytes = read(BINDING_PATH)
    require(identity(binding_bytes) == {'sha256': sys.argv[3], 'bytes': int(sys.argv[4])}, 'external binding digest/size')
    binding = decode(binding_bytes)
    require(binding['schema'] == 'p212-exclusive-canonical-adoption-v1' and binding['approved'] is True, 'disabled adoption')
    require(binding['authority'] == 'AUTHORIZE_ONE_EXCLUSIVE_P212_RAW_CANONICAL_ADOPTION_NO_PRODUCER_NO_PAIR', 'authority role')
    require(binding['role'] == 'author' and binding['independent_review'] is False, 'authorship')
    require(binding['source'] == {'path': str(SOURCE), **EXPECTED}, 'fixed accepted raw source')
    require(binding['destination'] == str(TARGET) and binding['output'] == str(OUT), 'fixed exclusive destinations')
    require(binding['environment'] == ENV4 and dict(os.environ) == ENV4 and Path.cwd() == ROOT, 'exact cwd/ENV4')
    require(sys.flags.isolated == 1 and sys.flags.no_site == 1 and sys.flags.dont_write_bytecode == 1 and sys.flags.optimize == 0, 'startup flags')
    require(binding['helper']['path'] == str(PREP / 'adopt_canonical.py') and Path(__file__).absolute() == PREP / 'adopt_canonical.py', 'helper source path')
    pinned(binding['helper'])
    require(binding['inputs']['path'] == str(PREP / 'WORKSPACE_INPUTS.json'), 'inventory source path')
    inventory = decode(pinned(binding['inputs']))
    require(binding['root_source_reception']['path'].startswith(str(ROOT_GATE) + '/'), 'root source reception scope')
    require(binding['authority_record']['path'] == str(ROOT_GATE / 'AUTHORITY.md'), 'new root authority path')
    pinned(binding['root_source_reception'])
    pinned(binding['authority_record'])
    require(binding['reviewed'] == {'complete_prepared_source': True, 'complete_actual_semantics': True, 'complete_actual_runtime': True, 'exclusive_raw_adoption': True, 'root_native_capture': True}, 'root gates remain pending')
    require(binding['cmp'] == {'argv': ['/usr/bin/cmp', '--', str(SOURCE), str(TARGET)], 'cwd': str(ROOT), 'environment': ENV4, 'stdin': 'DEVNULL', 'timeout_seconds': 30}, 'fixed cmp contract')
    safe(OUT, exists=False)
    safe(TARGET, exists=False)
    safe(ALIAS, exists=False)
    verify_inventory(inventory)
    semantic = received(SEMANTIC / 'EXECUTION_RECEPTION_NATIVE.json')
    runtime = received(RUNTIME / 'ROOT_NATIVE02.json')
    require(semantic == decode(read(SEMANTIC / 'EXECUTION_RECEPTION_RESULT.json')), 'whole semantic native/result binding')
    require(runtime == decode(read(RUNTIME / 'RESULT.json')), 'whole runtime native/result binding')
    require(semantic['status'] == 'PASS_ROOT_COMPLETE_P212_INITIAL_SAVED_OUTPUT_SEMANTICS', 'semantic status')
    require(runtime['status'] == 'PASS_ROOT_COMPLETE_P212_INITIAL_PRODUCTION_RECORDS_PENDING_SEMANTICS' and runtime['mode'] == 'initial', 'runtime status')
    require(semantic['saved_scientific_stdout'] == binding['source'] and runtime['raw_stdout'] == [binding['source']], 'same accepted actual stdout')
    require(semantic['producer_invocations_in_reception'] == 0 and semantic['canonical_adopted'] is False and runtime['actual_author_invocations_received'] == 1, 'accepted phase boundaries')
    require(semantic['actual_semantic_primitive_checks'] == 12375789 and semantic['actual_named_predicates'] == 72476 and semantic['actual_states'] == 4356, 'complete accepted semantics')
    data = read(SOURCE)
    require(identity(data) == EXPECTED, 'raw source identity')
    OUT.mkdir()
    write(OUT / 'BINDING_ORIGINAL.json', binding_bytes)
    write(OUT / 'ADOPTION_ATTEMPT.json', {'operation': 'exclusive raw P212 initial stdout adoption', 'source': binding['source'], 'target': str(TARGET), 'target_lexisted_before': False, 'started_epoch': time.time(), 'inputs': binding['inputs'], 'producer_invocations': 0})
    # Never serialize scientific JSON, normalize, overwrite, retry or clean up.
    write(TARGET, data)
    require(read(TARGET) == read(SOURCE) == data, 'complete byte comparison before native cmp')
    command = {**binding['cmp'], 'started_epoch': time.time()}
    write(OUT / 'CMP_ATTEMPT.json', command)
    try:
        native = subprocess.run(command['argv'], cwd=ROOT, env=ENV4, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)
    except subprocess.TimeoutExpired as error:
        write(OUT / 'cmp.stdout.raw', error.stdout or b'')
        write(OUT / 'cmp.stderr.raw', error.stderr or b'')
        write(OUT / 'CMP_FAILURE.json', {'status': 'TIMEOUT_NO_SUCCESS', 'ended_epoch': time.time(), 'timeout_seconds': 30, 'partial_streams_only': True, 'canonical_may_exist': True, 'automatic_retry_or_cleanup': False})
        raise
    except OSError as error:
        write(OUT / 'CMP_FAILURE.json', {'status': 'SPAWN_ERROR_NO_SUCCESS', 'ended_epoch': time.time(), 'errno': error.errno, 'canonical_may_exist': True, 'automatic_retry_or_cleanup': False})
        raise
    write(OUT / 'cmp.stdout.raw', native.stdout)
    write(OUT / 'cmp.stderr.raw', native.stderr)
    write(OUT / 'CMP_RECEIPT.json', {**command, 'ended_epoch': time.time(), 'exit_code': native.returncode, 'stdout': identity(native.stdout), 'stderr': identity(native.stderr)})
    require(native.returncode == 0 and native.stdout == native.stderr == b'', 'native raw cmp did not pass')
    require(read(SOURCE) == read(TARGET) == data, 'complete final raw bytes')
    verify_inventory(inventory, adopted=True)
    require(read(BINDING_PATH) == binding_bytes, 'root binding changed')
    for role in ('helper', 'inputs', 'root_source_reception', 'authority_record'):
        pinned(binding[role])
    result = {'status': 'P212_CANONICAL_EXCLUSIVELY_ADOPTED_FROM_ACCEPTED_ACTUAL_INITIAL_STDOUT', 'source': str(SOURCE), 'target': str(TARGET), **EXPECTED, 'raw_native_comparisons': 1, 'producer_invocations': 0, 'strict_pair_completed': False, 'independent_review': False, 'author_contribution': True, 'old_exact_trees_unchanged': True, 'host_runtime_revalidation': False, 'completed_epoch': time.time()}
    write(OUT / 'RESULT.json', result)
    files = sorted(OUT.iterdir())
    require(all(not path.is_symlink() and path.is_file() for path in files), 'output contains nonregular member')
    require({path.name for path in files} == {'BINDING_ORIGINAL.json', 'ADOPTION_ATTEMPT.json', 'CMP_ATTEMPT.json', 'cmp.stdout.raw', 'cmp.stderr.raw', 'CMP_RECEIPT.json', 'RESULT.json'}, 'exact successful output members')
    write(OUT / 'SHA256SUMS', ''.join(sha256(path.read_bytes()).hexdigest() + '  ' + path.name + '\n' for path in files).encode())
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
