#!/usr/bin/python3.10
"""Read-only SAME-B exact-response intake, not a scientific/infra producer.

Only existing bytes, JSON fields, manifests, raw identities, and bounded
runtime metadata are checked. No submitted or root module is imported or
executed. Full rich input rows and native-output bindings are emitted only
to stdout; the caller must preserve the real tool envelope. The subsequent
reviewer decision is separate from this documentary result.
"""
from hashlib import sha256
import json
import math
import os
from pathlib import Path
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASE = ROOT / 'docs/papers211_215_sequence'
HERE = BASE / 'qa/p211_b_report_root'
B = BASE / 'reviews/p211_b'
PAPER = ROOT / 'papers/211-kernel-image-projection-feedback'
READS = {}
JSON_CENSUS = {}
checks = 0


def need(ok, message):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(message)


def raw(path):
    path = Path(path)
    body = path.read_bytes()
    row = {'bytes': len(body), 'sha256': sha256(body).hexdigest(),
           'resolved': str(path.resolve(strict=True)),
           'symlink': os.readlink(path) if path.is_symlink() else None}
    need(str(path) not in READS or READS[str(path)] == row, 'stable complete read ' + str(path))
    READS[str(path)] = row
    return body


def pin(path, expected=None):
    raw(path)
    row = READS[str(Path(path))]
    if expected is not None:
        need(set(expected) == {'bytes', 'sha256', 'resolved', 'symlink'}
             and type(expected['bytes']) is int and expected['bytes'] >= 0
             and type(expected['sha256']) is str and len(expected['sha256']) == 64
             and type(expected['resolved']) is str
             and (expected['symlink'] is None or type(expected['symlink']) is str),
             'typed complete rich-key schema')
        need(row == expected, 'entire four-field rich key ' + str(path))
    return row


def unique(rows):
    result = {}
    for key, value in rows:
        need(key not in result, 'duplicate JSON key')
        result[key] = value
    return result


def bad(value):
    raise ValueError('nonfinite JSON constant ' + value)


def visit(value, census):
    kind = type(value).__name__
    census[kind] = census.get(kind, 0) + 1
    if type(value) is dict:
        for key, item in value.items():
            need(type(key) is str, 'JSON string key')
            visit(item, census)
    elif type(value) is list:
        for item in value:
            visit(item, census)
    elif type(value) is float:
        need(math.isfinite(value), 'finite JSON float')
    else:
        need(value is None or type(value) in (int, str, bool), 'JSON primitive')


def decode(body, label):
    value = json.loads(body, object_pairs_hook=unique, parse_constant=bad)
    census = {}
    visit(value, census)
    JSON_CENSUS[label] = census
    return value


def doc(path):
    return decode(raw(path), str(path))


def native(path, command, exit_code=0):
    value = doc(path)
    need(value['request']['cmd'] == command and value['request']['workdir'] == str(ROOT),
         'actual exact native request')
    parts = [value['result']]
    for poll in value.get('polls', []):
        need(poll['request']['session_id'] == parts[-1]['session_id'], 'native session continuity')
        parts.append(poll['result'])
    need(parts[-1].get('exit_code') == exit_code and not parts[-1].get('session_id'),
         'actual terminal native outcome')
    body = ''.join(part['output'] for part in parts).encode('utf-8')
    need(b'Warning: truncated output' not in body, 'complete native output')
    return body, parts


def manifest(path, count, exact=False):
    path = Path(path)
    rows = {}
    for line in raw(path).decode('ascii').splitlines():
        need(len(line) > 66 and line[64:66] == '  ', 'manifest syntax')
        digest, name = line[:64], line[66:]
        need(all(c in '0123456789abcdef' for c in digest) and len(digest) == 64,
             'manifest digest')
        need(name not in rows and not Path(name).is_absolute()
             and '..' not in Path(name).parts and name != path.name, 'nonself safe member')
        target = path.parent / name
        need(target.is_file() and not target.is_symlink(), 'regular manifest member')
        key = pin(target)
        need(key['sha256'] == digest, 'manifest bytes ' + name)
        rows[name] = key
    need(len(rows) == count, 'manifest complete expected cardinality')
    if exact:
        actual = {p.relative_to(path.parent).as_posix() for p in path.parent.rglob('*') if p.is_file()}
        need(actual == set(rows) | {path.name}, 'whole frozen membership')
    return rows


def state(path, content=True):
    path = Path(path)
    value = {'lexists': os.path.lexists(path), 'exists': path.exists(),
             'is_file': path.is_file(), 'is_dir': path.is_dir(),
             'is_character_device': path.is_char_device(), 'resolved': str(path.resolve()),
             'symlink': os.readlink(path) if path.is_symlink() else None}
    if path.is_char_device():
        st = path.stat()
        value['character_device'] = {'major': os.major(st.st_rdev),
                                    'minor': os.minor(st.st_rdev), 'mode': st.st_mode}
    if content and path.is_file():
        key = pin(path)
        value.update({name: key[name] for name in ('bytes', 'sha256')})
    return value


def main():
    need(len(sys.argv) == 1 and Path.cwd() == ROOT, 'fixed documentary invocation')
    need(not os.path.lexists(B / 'DELTA.md') and not os.path.lexists(B / 'DELTA_ACCEPTANCE.json')
         and not os.path.lexists(B / 'SHA256SUMS'), 'genuine pre-decision phase')
    pin(__file__)
    response_path = BASE / 'P211_B_RESPONSE.md'
    response = raw(response_path)
    need(len(response) == 2924 and sha256(response).hexdigest()
         == 'c4665cd9e790b97e7cadf1a9074c93a3b298835d360a94fd78b75008f8165edb',
         'exact issued response')
    keys_path = HERE / 'RESPONSE_KEYS.json'
    keys_raw = raw(keys_path)
    need(len(keys_raw) == 39749 and sha256(keys_raw).hexdigest()
         == 'bb0872855e1dcb94cbb113a8a4d52a2f87f808d085202486e13f9105f4a36692',
         'exact response keys bytes')
    keys = decode(keys_raw, str(keys_path))
    expected_fields = {'author_additions', 'author_before_after', 'author_modifications',
        'author_removals', 'checks', 'complete_prior_keys_checked', 'delta_accepted',
        'full_runtime_ordinary_keys', 'new_builds', 'new_page_views', 'new_scientific_runs',
        'prior_root_input_ledger_key', 'report_stage_manifest_key', 'report_stage_payload_keys',
        'response_key', 'response_path', 'root_reception_key', 'runtime_configuration_paths',
        'runtime_memberships', 'source_key', 'status'}
    need(set(keys) == expected_fields and keys['delta_accepted'] is False, 'full exact response schema')
    prior = doc(HERE / 'INPUTS.json')
    response_inputs = doc(HERE / 'RESPONSE_INPUTS.json')
    need(len(prior) == 1751 and len(response_inputs) == 1757, 'actual prior and pre-output ledgers')
    for ledger in (prior, response_inputs):
        for spelling, expected in ledger.items():
            need(set(expected) == {'bytes', 'sha256', 'resolved', 'symlink'}, 'exact rich input schema')
            pin(spelling, expected)
    need(all(response_inputs[path] == expected for path, expected in prior.items()), 'prior ledger contained unchanged')
    need(set(response_inputs) - set(prior) == {str(HERE / name) for name in
         ('response_keys.py', 'INPUTS.json', 'NATIVE07.json', 'RESULT.json', 'RECEPTION.md')}
         | {str(response_path)}, 'exact six pre-output additional keys')
    for name, path in (('source_key', HERE / 'response_keys.py'),
                       ('prior_root_input_ledger_key', HERE / 'INPUTS.json'),
                       ('root_reception_key', HERE / 'RECEPTION.md'),
                       ('response_key', response_path),
                       ('report_stage_manifest_key', B / 'REPORT_SHA256SUMS')):
        pin(path, keys[name])
    need(keys['response_path'] == str(response_path), 'response exact path')
    response_native_raw, response_parts = native(HERE / 'RESPONSE_NATIVE01.json',
        '/usr/bin/python3.10 -I -S -B docs/papers211_215_sequence/qa/p211_b_report_root/response_keys.py')
    response_native = decode(response_native_raw, 'root response native stdout')
    need(response_native['result_key'] == pin(keys_path)
         and response_native['response_key'] == pin(response_path)
         and response_native['status'] == keys['status'] == 'PASS_EXACT_NO_CHANGE_B_RESPONSE_KEYS'
         and response_native['checks'] == keys['checks'] == 5867
         and response_native['read_paths'] == len(response_inputs) + 1 == 1758,
         'post-output native count includes newly pinned RESPONSE_KEYS')
    report_native_raw, report_parts = native(HERE / 'NATIVE07.json',
        '/usr/bin/python3.10 -I -S -B docs/papers211_215_sequence/qa/p211_b_report_root/inspect_v7.py')
    report_result = doc(HERE / 'RESULT.json')
    need(decode(report_native_raw, 'root report native stdout') == report_result
         and report_result['checks'] == 31473 and report_result['read_paths'] == 1751
         and report_result['delta_accepted'] is False, 'whole actual report reception result')
    for member in sorted(HERE.iterdir()):
        need(member.is_file() and not member.is_symlink(), 'root report original regular file')
        doc(member) if member.suffix == '.json' else raw(member)
    failures = []
    for number in range(1, 7):
        source_name = 'inspect.py' if number == 1 else 'inspect_v' + str(number) + '.py'
        failed_raw, failed_parts = native(HERE / ('NATIVE0' + str(number) + '.json'),
            '/usr/bin/python3.10 -I -S -B docs/papers211_215_sequence/qa/p211_b_report_root/' + source_name, 1)
        failures.append({'native': str(HERE / ('NATIVE0' + str(number) + '.json')),
                         'source': str(HERE / source_name), 'actual_terminal': failed_parts[-1],
                         'source_key': pin(HERE / source_name)})
    report = manifest(B / 'REPORT_SHA256SUMS', 31)
    need(report == keys['report_stage_payload_keys'] and sum(x['bytes'] for x in report.values()) == 4711295,
         'all unchanged report payload rows and payload-only byte sum')
    need(pin(B / 'REPORT_SHA256SUMS')['sha256']
         == 'c32074e6e61021bd88adab9a515256bcaac74b14cea854617696402aaa95aabc', 'report seal unchanged')
    manifest(B / 'PREPARATION_SHA256SUMS', 19)
    round0 = manifest(PAPER / 'frozen_round0/SHA256SUMS', 32, True)
    manifest(PAPER / 'frozen_round1/SHA256SUMS', 83, True)
    live = {p.relative_to(PAPER).as_posix() for p in PAPER.rglob('*') if p.is_file()
            and not p.relative_to(PAPER).parts[0].startswith('frozen_round')}
    need(live == set(round0) == set(keys['author_before_after']), 'exact 32 author filenames; no addition/removal')
    author_rows = {}
    for name, recorded in keys['author_before_after'].items():
        need(set(recorded) == {'before', 'after', 'frozen'}, 'exact before/after source schema')
        live_path = PAPER / name
        need(recorded['before'] == prior[str(live_path)] == recorded['after'], 'root historical before/after identity')
        pin(live_path, recorded['after'])
        pin(PAPER / 'frozen_round1' / name, recorded['frozen'])
        need(raw(live_path) == raw(PAPER / 'frozen_round1' / name)
             == raw(PAPER / 'frozen_round0' / name), 'all live/Round1/Round0 raw bytes equal')
        author_rows[name] = recorded
    need(keys['author_additions'] == keys['author_removals'] == keys['author_modifications'] == [], 'zero declared author delta')
    binding = doc(BASE / 'qa/p211_b_pair_binding/BINDING.json')
    lock_pin = binding['runtime_lock']
    pin(lock_pin['path'], {k: lock_pin[k] for k in ('bytes', 'sha256', 'resolved', 'symlink')})
    lock = doc(lock_pin['path'])
    need(len(lock['files']) == keys['full_runtime_ordinary_keys'] == 122, 'all runtime files')
    for spelling, expected in lock['files'].items():
        pin(spelling, expected)
    for spelling, expected in lock['configuration']['paths'].items():
        need(state(spelling) == expected, 'entire runtime configured path ' + spelling)
    for spelling, expected in lock['configuration']['memberships'].items():
        path = Path(spelling)
        current = {'directory': state(path, False), 'members': {}}
        if path.is_dir():
            current['members'] = {p.name: state(p, False) for p in sorted(path.iterdir())}
        need(current == expected, 'whole runtime directory membership')
    for spelling, expected in lock['loader_search_directory_states'].items():
        need(state(spelling, False) == expected, 'full loader directory state')
    need(len(lock['configuration']['paths']) == keys['runtime_configuration_paths'] == 69
         and len(lock['configuration']['memberships']) == keys['runtime_memberships'] == 5,
         'complete configuration census')
    old_doc_raw, _ = native(B / 'evidence/DOCUMENTARY_INTAKE_NATIVE01.json',
        '/usr/bin/python3.10 -I -S -B docs/papers211_215_sequence/reviews/p211_b/receive_documents.py')
    new_doc_raw, _ = native(HERE / 'DOCUMENTARY_REUSE_NATIVE01.json',
        '/usr/bin/python3.10 -I -S -B docs/papers211_215_sequence/reviews/p211_b/receive_documents.py')
    need(old_doc_raw == new_doc_raw, 'root documentary reuse entire original stdout equality')
    document_result = decode(new_doc_raw, 'whole documentary reused stdout')
    need(document_result['documentary_checks'] == 1658754 and document_result['read_paths'] == 515,
         'documentary not science census')
    build_raw, _ = native(HERE / 'BUILD_REUSE_NATIVE01.json',
        '/usr/bin/python3 -I -S -B ' + str(BASE / 'reviews/p211_a/inspect_build_reuse.py'))
    need(build_raw == raw(BASE / 'qa/p211_b_root_reception/BUILD_REUSE_STDOUT01.raw'), 'entire reused build-key output')
    build = decode(build_raw, 'whole build-key reused stdout')
    need(build['checks'] == 5974 and build['prior_read_key_entries_checked_twice'] == 1299
         and build['configuration_entries_checked_twice'] == 843
         and build['fresh_build'] is False and build['scientific_execution'] is False,
         'separate nonauthor full build-key evidence scope')
    closing = doc(B / 'evidence/REPORT_CLOSING_METADATA_NATIVE01.json')
    replay_record = [r for r in closing['actual_final_report_reads']
                     if r['request']['cmd'].endswith('/REPLAY_LOG.md')]
    need(len(replay_record) == 1, 'one original pre-seal prose read')
    before = b'retains the actual complete 74,519-token tool output, not a re-created'
    after = b'retains the complete output (tool-reported 74,519 tokens), not a re-created'
    recorded = replay_record[0]['result']['output'].encode('utf-8')
    need(recorded.count(before) == 1 and recorded.replace(before, after) == raw(B / 'REPLAY_LOG.md'),
         'exact disclosed pre-seal sentence change, not raw-equal')
    for spelling, expected in list(READS.items()):
        pin(spelling, expected)
    result = {'status': 'EXACT_NO_CHANGE_RESPONSE_DOCUMENTS_RECEIVED_NOT_YET_REVIEWER_DECISION',
              'documentary_checks': checks, 'read_paths': len(READS), 'read_inputs': READS,
              'whole_json_censuses': JSON_CENSUS, 'prior_root_rich_keys': len(prior),
              'response_input_keys_before_output_pin': len(response_inputs),
              'root_native_read_paths_after_output_pin': response_native['read_paths'],
              'response_key': READS[str(response_path)], 'response_keys_key': READS[str(keys_path)],
              'report_stage_payloads_unchanged': 31, 'report_stage_payload_bytes': 4711295,
              'report_stage_total_bytes_with_seal': 4714092,
              'all_author_raw_triples_equal': True, 'author_before_after': author_rows,
              'author_additions': [], 'author_removals': [], 'author_modifications': [],
              'runtime_file_keys': 122, 'runtime_configuration_paths': 69,
              'runtime_memberships': 5, 'loader_directory_states': len(lock['loader_search_directory_states']),
              'root_report_native_result': report_result, 'root_response_native_result': response_native,
              'preserved_failed_root_adapters': failures, 'whole_documentary_reuse_output_equal': True,
              'whole_build_reuse_output_equal': True, 'exact_disclosed_preseal_prose_delta': 1,
              'scientific_executions': 0, 'submitted_imports': 0, 'builds': 0, 'page_views': 0,
              'scope': 'SAME-B documentary delta input reception; reuses attributed root science/build evidence, not independent self-certification of B-authored infrastructure.'}
    sys.stdout.write(json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + '\n')


if __name__ == '__main__':
    main()
