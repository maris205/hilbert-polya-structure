"""Root documentary preparation/full dependency reception. No scientific run.

The rich key/state conventions are explicitly reused from the fully read
p211_a_final_root/inspect.py, and the separate unmodified accepted build
comparator supplies its own current 1299-file/843-config double check.
This script neither imports the recorder nor executes submitted science.
"""
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
HERE = QA/'p211_round1_binding_root'
PREP = QA/'p211_round1_adapter01'
READS = {}
CHECKS = 0


def need(ok, label):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(label)


def read(path):
    path = Path(path)
    raw = path.read_bytes()
    key = {'bytes': len(raw), 'sha256': sha256(raw).hexdigest(),
           'resolved': str(path.resolve(strict=True)),
           'symlink': os.readlink(path) if path.is_symlink() else None}
    need(str(path) not in READS or READS[str(path)] == key, ('read drift', str(path)))
    READS[str(path)] = key
    return raw


def check_pin(path, expected):
    read(path)
    actual = READS[str(Path(path))]
    need(all(actual[k] == v for k, v in expected.items()), ('whole key', str(path)))


def obj(path):
    return json.loads(read(path))


def state(path, with_bytes=True):
    path = Path(path)
    row = {'lexists': os.path.lexists(path), 'exists': path.exists(),
           'is_file': path.is_file(), 'is_dir': path.is_dir(),
           'is_character_device': path.is_char_device(), 'resolved': str(path.resolve()),
           'symlink': os.readlink(path) if path.is_symlink() else None}
    if path.is_char_device():
        st = path.stat()
        row['character_device'] = {'major': os.major(st.st_rdev), 'minor': os.minor(st.st_rdev), 'mode': st.st_mode}
    if with_bytes and path.is_file():
        raw = read(path)
        row.update({'bytes': len(raw), 'sha256': sha256(raw).hexdigest()})
    return row


def seal(base, count):
    rows = {}
    raw = read(base/'SHA256SUMS')
    need(raw.endswith(b'\n'), 'complete manifest')
    for line in raw.decode().splitlines():
        m = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        need(m is not None, 'manifest syntax')
        digest, name = m.groups()
        need(name not in rows and name != 'SHA256SUMS' and not Path(name).is_absolute()
             and '..' not in Path(name).parts, 'safe unique nonself name')
        check_pin(base/name, {'sha256': digest})
        rows[name] = READS[str(base/name)]
    need(len(rows) == count, 'whole expected manifest population')
    files = set()
    for p in base.rglob('*'):
        need(p.resolve() == p and (p.is_file() or p.is_dir()), 'ordinary complete tree')
        if p.is_file():
            files.add(p.relative_to(base).as_posix())
    need(files == set(rows)|{'SHA256SUMS'}, 'no omitted payload')
    return rows


phase = sys.argv[1]
need(phase in ('precopy', 'postcopy') and Path.cwd() == ROOT, 'literal root phase')
out = HERE/(phase+'01')
need(not os.path.lexists(out), 'exclusive result destination')
read(__file__)
check_pin(PREP/'freeze.py', {'bytes': 35397, 'sha256': '50c32a6fa4c703275cb55535bc56507ba5bdbb909fb57ed31ffc6d3ff9566ab2'})
check_pin(PREP/'SHA256SUMS', {'sha256': 'a8b177ff6c92c630b82868d2ac537cbd49f6461b7e1f50b31f328bab09495fb8'})
prepared = seal(PREP, 16)
need(sum(p['bytes'] for p in prepared.values()) == 378182, 'whole preparation bytes')
mapping = {r['logical_path']: r for r in obj(PREP/'DRAFT_ORIGINAL_MAPPING.json')}
records = obj(PREP/'NATIVE_PREPARATION_RECORDS.json')
runs = obj(PREP/'NATIVE_STATIC_CHECKS.json')['runs']
need(len(runs) == 2 and len(mapping) == 4, 'exact actual source versions')
for i, run in enumerate(runs):
    result = run['result']
    need(result['exit_code'] == 0 and not result.get('session_id'), 'actual static settled zero')
    saved = json.loads(result['output'])
    need(saved['checks'] == [135, 140][i] == len(saved['check_labels'])
         and saved['recorder_executions'] == saved['physical_copies'] == saved['scientific_executions'] == 0,
         'complete source-only static scope')
    for logical, expected in saved['inputs'].items():
        target = mapping[logical]['physical_original'] if i == 0 and logical in mapping else logical
        check_pin(ROOT/target, expected)
for logical, row in mapping.items():
    target = ROOT/row['physical_original']
    check_pin(target, row['pin'])
    i = row['actual_native_comparison_index']
    prior = records['draft_original_source_reads'][i]
    cmp = records['draft_original_byte_comparisons'][i]
    need(prior['result']['exit_code'] == 0 and prior['result']['output'].encode() == read(target), 'entire original decoded source text')
    need(cmp['result']['exit_code'] == 0 and cmp['result']['output'] == '', 'actual native prior-source comparison')
    need(logical in cmp['request']['cmd'] and row['physical_original'] in cmp['request']['cmd'], 'actual comparison exact paths')
derivation = obj(PREP/'DERIVATION_NATIVE.json')
need(derivation['result']['exit_code'] == 1 and derivation['result']['output'].encode() == read(PREP/'DERIVATION.diff'), 'full actual diff and ordinary exit1')
# Reconstruct both complete source byte streams from the unified diff, no
# trust in a truncated display. Hunk context plus removed/added lines is full
# here because the sole untouched suffix/prefix is contained in the hunks.
diff_lines = read(PREP/'DERIVATION.diff').decode().splitlines(keepends=True)
old = read(QA/'p211_round0_execution01/freeze.py').decode().splitlines(keepends=True)
new = read(PREP/'freeze.py').decode().splitlines(keepends=True)
oi = ni = 0
for line in diff_lines[2:]:
    if line.startswith('@@ '):
        m = re.match(r'@@ -(\d+)(?:,\d+)? \+(\d+)(?:,\d+)? @@', line)
        need(m is not None, 'hunk header')
        a, b = int(m[1])-1, int(m[2])-1
        need(old[oi:a] == new[ni:b], 'unchanged interhunk bytes')
        oi, ni = a, b
    elif line.startswith(' '):
        need(old[oi] == new[ni] == line[1:], 'whole context line')
        oi += 1; ni += 1
    elif line.startswith('-'):
        need(old[oi] == line[1:], 'exact removed line'); oi += 1
    elif line.startswith('+'):
        need(new[ni] == line[1:], 'exact added line'); ni += 1
    else:
        raise AssertionError(('unsupported diff line', line))
need(old[oi:] == new[ni:], 'complete unchanged suffix')
preseal = obj(PREP/'PRESEAL_CHECK_NATIVE.json')
need(preseal['result']['exit_code'] == 0, 'actual preseal exit')
ps = json.loads(preseal['result']['output'])
need(ps['checks'] == 227 and ps['preseal_payload_count'] == 15, 'actual preseal population')
for name, expected in ps['preseal_pins'].items():
    check_pin(PREP/name, expected)
input_rows = read(PREP/'INPUTS.sha256').decode().splitlines()
need(len(input_rows) == 21, 'entire preparation input list')
for line in input_rows:
    digest, name = line.split('  ', 1)
    check_pin(ROOT/name, {'sha256': digest})
key_path = QA/'p211_a_final_root/run01/READ_INPUTS.json'
accepted = obj(key_path)
need(len(accepted) == 1688, 'complete accepted A root key')
for path, expected in accepted.items():
    check_pin(path, expected)
host_count = sum(not Path(p).is_relative_to(ROOT) for p in accepted)
need(host_count == 799, 'full host-key boundary')
binding = obj(QA/'p211_a_pair_binding/BINDING.json')
lock = obj(binding['runtime_lock']['path'])
check_pin(binding['runtime_lock']['path'], {k: binding['runtime_lock'][k] for k in ('sha256','bytes','resolved','symlink')})
need(len(lock['files']) == 122, 'entire ordinary runtime key')
for path, expected in lock['files'].items():
    check_pin(path, expected)
for path, expected in lock['configuration']['paths'].items():
    need(state(path) == expected, ('entire runtime setting', path))
for directory, expected in lock['configuration']['memberships'].items():
    path = Path(directory)
    current = {'directory': state(path, False), 'members': {}}
    if path.is_dir():
        current['members'] = {p.name: state(p, False) for p in sorted(path.iterdir())}
    need(current == expected, ('complete runtime membership', directory))
for path, expected in lock['loader_search_directory_states'].items():
    need(state(path, False) == expected, ('entire loader directory', path))
build = obj(HERE/('BUILD_'+phase.upper()+'_NATIVE01.json'))
old_build = obj(QA/'p211_a_final_root/BUILD_REUSE_NATIVE01.json')
need(all(build['request'][k] == old_build['request'][k] for k in ('cmd','workdir')) and build['polls'] == []
     and build['result']['exit_code'] == 0
     and build['result']['output'] == old_build['result']['output'], 'entire actual current unchanged build comparator output/request')
for path, expected in dict(READS).items():
    check_pin(path, expected)
result = {'status': 'PASS_COMPLETE_PREPARATION_AND_HOST_KEY_SETTINGS_RECHECK',
          'phase': phase, 'checks': CHECKS, 'read_paths': len(READS),
          'accepted_full_key': {'path': str(key_path), 'pin': READS[str(key_path)]},
          'accepted_key_entries': 1688, 'outside_workspace_entries': 799,
          'runtime_files': 122, 'runtime_configuration_paths': len(lock['configuration']['paths']),
          'runtime_memberships': len(lock['configuration']['memberships']),
          'runtime_loader_directory_states': len(lock['loader_search_directory_states']),
          'build_file_keys_checked_twice': 1299, 'build_configurations_checked_twice': 843,
          'new_scientific_runs': 0, 'new_builds': 0, 'new_page_views': 0,
          'round1_received': False, 'binding_authorized_by_this_script': False}
out.mkdir()
for name, data in [('RESULT.json', result), ('READ_INPUTS.json', READS)]:
    with (out/name).open('x') as stream:
        json.dump(data, stream, sort_keys=True, indent=2); stream.write('\n')
print(json.dumps(result, sort_keys=True))
