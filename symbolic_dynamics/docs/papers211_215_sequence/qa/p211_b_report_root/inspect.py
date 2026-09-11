"""Root reception of sealed actual B report; no scientific or build execution.

Uses the disclosed rich-key/manifest idiom from the accepted A reception,
with explicit B envelopes and counts. Reads original native bodies in full.
Only new documentary INPUTS/RESULT files are written exclusively.
"""
from pathlib import Path
from hashlib import sha256
import json
import os
import re
import shlex

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASE = ROOT/'docs/papers211_215_sequence'
QA = BASE/'qa'
B = BASE/'reviews/p211_b'
PAPER = ROOT/'papers/211-kernel-image-projection-feedback'
HERE = Path(__file__).resolve().parent
KEYS = {}
checks = 0


def need(ok, label):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(label)


def raw(path):
    path = Path(path)
    body = path.read_bytes()
    key = {'bytes': len(body), 'sha256': sha256(body).hexdigest(),
           'resolved': str(path.resolve(strict=True)),
           'symlink': os.readlink(path) if path.is_symlink() else None}
    need(str(path) not in KEYS or KEYS[str(path)] == key, ('stable complete key', str(path)))
    KEYS[str(path)] = key
    return body


def pin(path, expected=None):
    raw(path)
    key = KEYS[str(Path(path))]
    if expected is not None:
        need(all(key[k] == v for k, v in expected.items()), ('all expected fields', str(path)))
    return key


def unique(pairs):
    value = {}
    for k, v in pairs:
        need(k not in value, ('duplicate JSON key', k))
        value[k] = v
    return value


def doc(path):
    return json.loads(raw(path), object_pairs_hook=unique)


def manifest(path, base, count, exact=False, absolute=False):
    rows = {}
    data = raw(path)
    need(data.endswith(b'\n'), 'LF terminated manifest')
    for line in data.decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        need(match is not None, 'exact manifest syntax')
        digest, name = match.groups()
        need(name not in rows and '..' not in Path(name).parts
             and Path(name).is_absolute() == absolute, ('safe unique member', name))
        target = Path(name) if absolute else base/name
        need(target != path, 'nonself manifest')
        rows[name] = pin(target, {'sha256': digest})
    need(len(rows) == count, ('full manifest count', str(path)))
    if exact:
        need(not any(p.is_symlink() for p in base.rglob('*')), 'no tree symlinks')
        need({p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file()}
             == set(rows)|{path.name}, 'complete physical inventory')
    return rows


def native(path, cmd):
    cap = doc(path)
    need(cap['request']['cmd'] == cmd and cap['request']['workdir'] == str(ROOT),
         ('exact actual invocation', str(path)))
    parts = [cap['result']]
    for poll in cap.get('polls', []):
        need(poll['request']['session_id'] == parts[-1]['session_id'], 'actual session chain')
        parts.append(poll['result'])
    need(parts[-1]['exit_code'] == 0 and not parts[-1].get('session_id'), 'actual settled exit')
    output = ''.join(p['output'] for p in parts)
    need('Warning: truncated output' not in output, 'complete native output')
    return output, json.loads(output, object_pairs_hook=unique)


need(Path.cwd() == ROOT, 'explicit root workdir')
read_source = pin(__file__)
pin(B/'REPORT_SHA256SUMS', {'sha256': 'c32074e6e61021bd88adab9a515256bcaac74b14cea854617696402aaa95aabc'})
stage = manifest(B/'REPORT_SHA256SUMS', B, 31, True)
need(sum(k['bytes'] for k in stage.values()) == 4714092, 'all report payload bytes')
manifest(B/'PREPARATION_SHA256SUMS', B, 19)
manifest(B/'INPUT_PINS.sha256', ROOT, 84)
manifest(B/'EXTERNAL_READ_PINS.sha256', ROOT, 50)
manifest(B/'RECEPTION_INPUT_PINS.sha256', ROOT, 515, absolute=True)
frozen = manifest(PAPER/'frozen_round1/SHA256SUMS', PAPER/'frozen_round1', 83, True)
author = manifest(PAPER/'frozen_round0/SHA256SUMS', PAPER/'frozen_round0', 32, True)
for name in author:
    need(raw(PAPER/name) == raw(PAPER/'frozen_round1'/name)
         == raw(PAPER/'frozen_round0'/name), ('whole live/frozen author bytes', name))
live = {p.relative_to(PAPER).as_posix() for p in PAPER.rglob('*') if p.is_file()
        and not p.relative_to(PAPER).parts[0].startswith('frozen_round')}
need(live == set(author), 'zero author additions/removals')
need(not os.path.lexists(B/'DELTA.md') and not os.path.lexists(B/'SHA256SUMS'), 'delta genuinely pending')
finding = doc(B/'FINDINGS.json')
need(finding['recommendation'] == 'PASS_NO_REPAIR_REQUESTED'
     and finding['current_open_total'] == finding['new_B_findings_total'] == 0
     and finding['findings'] == [] and not finding['delta_received']
     and not finding['delta_accepted'], 'actual report census and phase')
need(all(finding['census'][s] == {'open': 0, 'resolved': 0}
         for s in ('Critical', 'Major', 'Minor')), 'all severity fields')
need({r['id'] for r in finding['inherited_findings']} == {'m01', 'm02'}
     and all(r['status'] == 'RESOLVED_BEFORE_B_IMPLEMENTATION_IN_ROUND1_VERIFIED'
             for r in finding['inherited_findings']), 'inherited findings not new B findings')
cmd = '/usr/bin/python3.10 -I -S -B docs/papers211_215_sequence/reviews/p211_b/receive_documents.py'
old_raw, old = native(B/'evidence/DOCUMENTARY_INTAKE_NATIVE01.json', cmd)
new_raw, new = native(HERE/'DOCUMENTARY_REUSE_NATIVE01.json', cmd)
need(old_raw.encode() == new_raw.encode() and old == new, 'whole actual documentary reuse output')
need(old['documentary_checks'] == 1658754 and old['read_paths'] == len(old['read_inputs']) == 515
     and old['scientific_executions'] == old['builds'] == old['submitted_imports'] == 0,
     'entire original documentary scope')
for path, expected in old['read_inputs'].items():
    need(pin(path, expected) == expected, ('complete original B documentary key', path))
for row in old['actual_native_commands']:
    path = Path(row['receipt'])
    need(doc(path) == row['whole_receipt'] and doc(path.with_name('ATTEMPT.json'))
         == row['whole_attempt'], 'entire original command bodies')
need(len(old['actual_native_commands']) == 18, 'all native command census')
closure = doc(QA/'p211_b_binding_closure/INPUTS.json')
need(len(closure) == 512, 'entire root accepted runtime closure key')
for path, expected in closure.items():
    need(pin(path, expected) == expected, ('entire root runtime key unchanged', path))
prep = doc(QA/'p211_b_root_reception/PREPARATION_READ_INPUTS.json')
need(len(prep) == 161, 'complete accepted preparation key')
for path, expected in prep.items():
    pin(path, expected)
closing = doc(B/'evidence/REPORT_CLOSING_METADATA_NATIVE01.json')
reads = doc(B/'evidence/FINAL_REVIEW_NATIVE_READS01.json')['reads']
need(len(reads) == 30 and reads[6]['result']['exit_code'] == 2, 'preserved actual navigation failure')
need('No such file or directory' in reads[6]['result']['output'], 'original diagnostic preserved')
slice_count = 0
for i, rec in enumerate(reads):
    # Navigation/index and an earlier pre-final reception body are historical,
    # not compared to later mutable text. All other actual sed slices bind.
    if i in (0, 1, 2, 3, 6, 14, 15, 16):
        continue
    args = shlex.split(rec['request']['cmd'])
    need(args[0:2] == ['sed', '-n'] and len(args) == 4, 'recorded exact sed request')
    lo, hi = map(int, re.fullmatch(r'(\d+),(\d+)p', args[2]).groups())
    body = b''.join(raw(ROOT/args[3]).splitlines(keepends=True)[lo-1:hi])
    need(rec['result']['exit_code'] == 0 and rec['result']['output'].encode() == body,
         ('whole recorded selected slice', i))
    slice_count += 1
for rec in closing['post_intake_original_reads'] + closing['actual_final_report_reads']:
    args = shlex.split(rec['request']['cmd'])
    need(args[0:2] == ['sed', '-n'] and len(args) == 4, 'exact final report read')
    lo, hi = map(int, re.fullmatch(r'(\d+),(\d+)p', args[2]).groups())
    need(rec['result']['exit_code'] == 0 and rec['result']['output'].encode()
         == b''.join(raw(ROOT/args[3]).splitlines(keepends=True)[lo-1:hi]), 'full final native slice bytes')
    slice_count += 1
for rec in closing['closing_pin_checks'][:4]:
    args = shlex.split(rec['request']['cmd'])
    need(args[:3] == ['sha256sum', '--strict', '-c'], 'actual final pin command')
    seal = Path(rec['request']['workdir'])/args[3]
    expected = ''.join(line[66:] + ': OK\n' for line in raw(seal).decode().splitlines())
    need(rec['result']['exit_code'] == 0 and rec['result']['output'] == expected,
         'entire native successful pin stream')
links = closing['local_link_check']
need(links['result']['exit_code'] == 0 and len(links['occurrences']) == 39, 'actual reported local-link census')
for row in links['occurrences']:
    target = (B/row['source']).parent/row['target']
    need(str(target.resolve()) == row['resolved'] and target.is_file(), 'exact live local target')
build_cmd = '/usr/bin/python3 -I -S -B '+str(BASE/'reviews/p211_a/inspect_build_reuse.py')
build_raw, build = native(HERE/'BUILD_REUSE_NATIVE01.json', build_cmd)
need(build_raw.encode() == raw(QA/'p211_b_root_reception/BUILD_REUSE_STDOUT01.raw'),
     'whole unchanged original build reuse output')
need(build['checks'] == 5974 and build['prior_read_key_entries_checked_twice'] == 1299
     and build['configuration_entries_checked_twice'] == 843, 'full build dependency scope')
build_key = doc(build['prior_read_key']['path'])
for path, expected in build_key.items():
    pin(build['exact_navigation_substitutions'].get(path, path), expected)
pin(build['configuration_key']['path'], build['configuration_key']['pin'])
pin(build['executed_checker']['path'], build['executed_checker']['pin'])
for path, expected in list(KEYS.items()):
    need(pin(path) == expected, ('complete final input key unchanged', path))
result = {'status': 'PASS_ROOT_B_REPORT_STAGE_ORIGINAL_RECEPTION', 'checks': checks,
          'read_paths': len(KEYS), 'report_payloads': 31, 'report_payload_bytes': 4714092,
          'preparation_payloads_unchanged': 19, 'preparation_files_with_seal': 20,
          'frozen_Round1_payloads': 83, 'author_live_frozen_pairs': 32,
          'complete_B_documentary_original_keys': 515, 'root_runtime_closure_keys': 512,
          'documentary_reuse_checks': 1658754, 'whole_documentary_output_unchanged': True,
          'original_native_commands_received': 18, 'native_slice_pairs': slice_count,
          'full_build_reuse_checks': 5974, 'build_original_keys': 1299,
          'build_configuration_entries_twice': 843, 'open_findings': 0,
          'delta_accepted': False, 'new_scientific_runs': 0, 'new_builds': 0, 'new_page_views': 0,
          'scope': 'Complete report reception and explicit documentary/build-key reuse; not new science or same-B delta acceptance.'}
for name, value in [('INPUTS.json', KEYS), ('RESULT.json', result)]:
    with (HERE/name).open('xb') as stream:
        stream.write((json.dumps(value, sort_keys=True, indent=2)+'\n').encode())
print(json.dumps(result, sort_keys=True))
