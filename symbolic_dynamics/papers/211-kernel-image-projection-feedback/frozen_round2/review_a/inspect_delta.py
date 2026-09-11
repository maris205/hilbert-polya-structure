"""Same-A no-change delta evidence check; no science, build, view or old-code import."""
from hashlib import sha256
import json
import os
from pathlib import Path
import re

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT/'docs/papers211_215_sequence/qa'
A = ROOT/'docs/papers211_215_sequence/reviews/p211_a'
PAPER = ROOT/'papers/211-kernel-image-projection-feedback'
RR = QA/'p211_a_report_root'
RESPONSE = ROOT/'docs/papers211_215_sequence/P211_A_RESPONSE.md'
OUT = A/'evidence/delta01'
READS = {}
CHECKS = 0


def need(ok, label):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(label)


def read(path):
    path = Path(path)
    body = path.read_bytes()
    need(str(path) not in READS or READS[str(path)] == body, ('same complete bytes', str(path)))
    READS[str(path)] = body
    return body


def identity(body):
    return {'sha256': sha256(body).hexdigest(), 'bytes': len(body)}


def pin(path, expected=None):
    path = Path(path)
    actual = {**identity(read(path)), 'resolved': str(path.resolve(strict=True)),
              'symlink': os.readlink(path) if path.is_symlink() else None}
    if expected is not None:
        need(all(actual[k] == v for k, v in expected.items()), ('all expected rich fields', str(path)))
    return actual


def unique(pairs):
    result = {}
    for k, v in pairs:
        need(k not in result, ('duplicate JSON key', k))
        result[k] = v
    return result


def doc(path):
    return json.loads(read(path), object_pairs_hook=unique)


def manifest(path, base, count):
    result = {}
    body = read(path)
    need(body.endswith(b'\n'), 'complete LF-terminated manifest')
    for line in body.decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        need(match is not None, 'exact manifest syntax')
        digest, name = match.groups()
        need(not Path(name).is_absolute() and '..' not in Path(name).parts
             and name not in result and name != path.name, ('safe nonself manifest', name))
        result[name] = pin(base/name, {'sha256': digest})
    need(len(result) == count, 'complete manifest population')
    return result


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
        row.update(identity(read(path)))
    return row


need(Path.cwd() == ROOT and not os.path.lexists(OUT), 'new owned delta evidence')
need(not os.path.lexists(A/'DELTA.md') and not os.path.lexists(A/'SHA256SUMS'),
     'actual verification before reviewer decision and final seal')
read(__file__)
response_pin = pin(RESPONSE, {'bytes': 2707, 'sha256': '80a9c780186ddc300d9cbd2b1338e4ce28143c046af4ffb0bbf56a2103adf604'})
response_keys_pin = pin(RR/'RESPONSE_KEYS.json', {'bytes': 42922, 'sha256': '8047354f4ca07f66af626d8590c77b8e4074a7f39bd8e25b5f24b24ce19599b8'})
response_keys = doc(RR/'RESPONSE_KEYS.json')
need(response_keys['status'] == 'PASS_EXACT_NO_CHANGE_RESPONSE_KEYS'
     and response_keys['checks'] == 1350 and response_keys['complete_prior_keys_checked'] == 498
     and response_keys['delta_accepted'] is False
     and response_keys['new_scientific_runs'] == response_keys['new_builds'] == response_keys['new_page_views'] == 0,
     'exact original response-check phase')
need(response_keys['response_path'] == str(RESPONSE) and response_keys['response_key'] == response_pin,
     'exact response identity')
pin(RR/'RECEPTION.md', response_keys['root_reception_key'])
pin(RR/'response_keys.py', response_keys['source_key'])
pin(RR/'INPUTS.json', response_keys['prior_root_input_ledger_key'])
root_keys = doc(RR/'INPUTS.json')
need(len(root_keys) == 498, 'all prior root report inputs')
for path, expected in root_keys.items():
    need(pin(path, expected) == expected, ('entire unchanged prior key', path))
root_result = doc(RR/'RESULT.json')
root_native = doc(RR/'NATIVE01.json')
need(root_native['result']['exit_code'] == 0 and json.loads(root_native['result']['output']) == root_result,
     'whole actual root report result')
need(root_result['status'] == 'PASS_ROOT_A_REPORT_STAGE_ORIGINAL_RECEPTION'
     and root_result['checks'] == 13371 and root_result['read_paths'] == 498
     and root_result['open_findings'] == 0 and root_result['delta_accepted'] is False,
     'actual report reception not a prior delta acceptance')
read(RR/'inspect.py')
response_native = doc(RR/'RESPONSE_NATIVE01.json')
need(response_native['request'] == {'cmd': '/usr/bin/python3 -I -S -B docs/papers211_215_sequence/qa/p211_a_report_root/response_keys.py',
                                  'workdir': str(ROOT), 'max_output_tokens': 2000}, 'exact original response check command')
need(response_native['result']['exit_code'] == 0, 'actual response check exit')
need(json.loads(response_native['result']['output']) == {
    'checks': 1350, 'response_key': response_pin, 'result_key': response_keys_pin,
    'status': 'PASS_EXACT_NO_CHANGE_RESPONSE_KEYS'}, 'whole response native output and key relation')
stage = manifest(A/'REPORT_STAGE_SHA256SUMS', A, 41)
need(pin(A/'REPORT_STAGE_SHA256SUMS', response_keys['report_stage_manifest_key'])['sha256']
     == 'f6385b69c079eea88502baf5513091ea25cffdc2c7927aeb7ca20835edb5e531', 'unchanged historical report seal')
need(stage == response_keys['report_stage_payload_keys'] and response_keys['report_stage_payload_count'] == 41
     and sum(row['bytes'] for row in stage.values()) == 1980184, 'all exact report-stage before/after fields')
prep = manifest(A/'PREPARATION_SHA256SUMS', A, 20)
need(pin(A/'PREPARATION_SHA256SUMS')['sha256'] == '67b61e77cca2195f264902e54fedb5688ca39d1c3b649282f3306c1172519a07',
     'unchanged historical preparation seal')
freeze = PAPER/'frozen_round0'
frozen = manifest(freeze/'SHA256SUMS', freeze, 32)
need(pin(freeze/'SHA256SUMS')['sha256'] == '459459486a82c8f787d04e5e7fcb81e6c01b3abef320d1e82ea4cbb30ea8a8bd',
     'unchanged Round0 seal')
need({p.relative_to(freeze).as_posix() for p in freeze.rglob('*') if p.is_file()}
     == set(frozen)|{'SHA256SUMS'}, 'whole physical frozen membership')
need(set(response_keys['author_before_after']) == set(frozen)
     and response_keys['author_payload_count'] == 32, 'complete author delta target set')
author_delta = {}
for name, frozen_pin in frozen.items():
    live, saved = PAPER/name, freeze/name
    current = pin(live)
    expected = {'before': root_keys[str(live)], 'after': current, 'frozen': frozen_pin}
    need(response_keys['author_before_after'][name] == expected
         and expected['before'] == expected['after'] and read(live) == read(saved),
         ('exact whole author before/after and raw frozen pair', name))
    author_delta[name] = expected
live_files = set()
for parent, dirs, files in os.walk(PAPER):
    if Path(parent) == PAPER:
        need('frozen_round0' in dirs, 'expected sole existing freeze')
        dirs.remove('frozen_round0')
    for name in dirs+files:
        need(not (Path(parent)/name).is_symlink(), 'unlinked author inventory')
    for name in files:
        path = Path(parent)/name
        need(path.is_file(), 'ordinary author payload')
        live_files.add(path.relative_to(PAPER).as_posix())
need(live_files == set(frozen), 'zero author additions/removals')
finding = doc(A/'FINDINGS.json')
need(finding['recommendation'] == 'PASS_NO_REPAIR_REQUESTED'
     and finding['current_open_total'] == finding['new_A_findings_total'] == 0 and finding['findings'] == []
     and finding['delta_received'] is False and finding['delta_accepted'] is False,
     'immutable initial finding census; decision will be additive')
# Recheck the complete live bounded runtime settings, not merely the lock file.
binding = doc(QA/'p211_a_pair_binding/BINDING.json')
lock = doc(binding['runtime_lock']['path'])
pin(binding['runtime_lock']['path'], {k: binding['runtime_lock'][k] for k in ('sha256', 'bytes', 'resolved', 'symlink')})
need(len(lock['files']) == 122, 'whole accepted ordinary runtime key')
for path, expected in lock['files'].items():
    pin(path, expected)
for path, expected in lock['configuration']['paths'].items():
    need(state(path) == expected, ('entire current bounded runtime state', path))
for directory, expected in lock['configuration']['memberships'].items():
    path = Path(directory)
    current = {'directory': state(path, False), 'members': {}}
    if path.is_dir():
        current['members'] = {p.name: state(p, False) for p in sorted(path.iterdir())}
    need(current == expected, ('entire bounded runtime directory membership', directory))
for path, expected in lock['loader_search_directory_states'].items():
    need(state(path, False) == expected, ('entire loader directory state', path))
# The new build-key check is not a build/view; require its full original output.
build_native = doc(A/'evidence/DELTA_BUILD_REUSE_NATIVE01.json')
parts = [build_native['result']]+[p['result'] for p in build_native['polls']]
need(parts[-1]['exit_code'] == 0 and not parts[-1].get('session_id'), 'actual settled delta build-key checker')
build_raw = ''.join(p['output'] for p in parts)
build_result = json.loads(build_raw)
old_build = doc(A/'evidence/BUILD_REUSE_RESULT01.json')
need(build_result == old_build and build_raw == (json.dumps(old_build, sort_keys=True, indent=2)+'\n'),
     'entire exact original build-reuse output, not selected counts')
need(build_result['checks'] == 5974 and build_result['prior_read_key_entries_checked_twice'] == 1299
     and build_result['configuration_entries_checked_twice'] == 843
     and build_result['scientific_execution'] is False and build_result['fresh_build'] is False,
     'complete unchanged build dependency scope')
old_build_key = doc(build_result['prior_read_key']['path'])
pin(build_result['prior_read_key']['path'], build_result['prior_read_key']['pin'])
pin(build_result['historical_mapping']['path'], build_result['historical_mapping']['pin'])
need(len(old_build_key) == 1299 and len(build_result['exact_navigation_substitutions']) == 2,
     'only exact accepted navigation substitutions')
for path, expected in old_build_key.items():
    pin(build_result['exact_navigation_substitutions'].get(path, path), expected)
key = {path: {**identity(body), 'resolved': str(Path(path).resolve(strict=True)),
              'symlink': os.readlink(path) if Path(path).is_symlink() else None}
       for path, body in sorted(READS.items())}
for path, expected in key.items():
    need(pin(path) == expected, ('complete final unchanged delta input key', path))
result = {'status': 'PASS_EXACT_NO_CHANGE_BYTES_FOR_SAME_A_DECISION', 'checks': CHECKS,
          'read_paths': len(key), 'response': response_pin, 'response_keys': response_keys_pin,
          'prior_root_inputs_unchanged': 498, 'author_payloads_unchanged': 32,
          'report_stage_payloads_unchanged': 41, 'preparation_payloads_unchanged': 20,
          'author_additions': [], 'author_removals': [], 'author_modifications': [],
          'author_before_after': author_delta, 'report_stage_before_after': stage,
          'runtime_ordinary_keys': 122, 'runtime_configuration_paths': len(lock['configuration']['paths']),
          'runtime_configuration_memberships': len(lock['configuration']['memberships']),
          'runtime_loader_directory_states': len(lock['loader_search_directory_states']),
          'full_build_key_recheck': {'checks': 5974, 'prior_file_keys_twice': 1299, 'configuration_entries_twice': 843,
                                     'exact_navigation_substitutions': build_result['exact_navigation_substitutions']},
          'new_scientific_runs': 0, 'new_builds': 0, 'new_page_views': 0,
          'reviewer_decision': 'Not supplied by this artifact check; the same A reviewer must actually decide in DELTA.md.'}
OUT.mkdir()
for name, value in (('READ_INPUTS.json', key), ('RESULT.json', result)):
    with (OUT/name).open('xb') as stream:
        stream.write((json.dumps(value, sort_keys=True, indent=2, allow_nan=False)+'\n').encode())
print(json.dumps({'status': result['status'], 'checks': result['checks'], 'read_paths': len(key),
                  'result_sha256': sha256((OUT/'RESULT.json').read_bytes()).hexdigest(),
                  'new_scientific_runs': 0, 'new_builds': 0, 'new_page_views': 0}, sort_keys=True))
