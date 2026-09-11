"""Final nonself accepted-delta seal, after both actual same-B evidence passes."""
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import time

B = Path(__file__).resolve().parent
ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
assert dict(os.environ) == ENV and Path.cwd() == ROOT
assert sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and sys.flags.optimize == 0
assert sys.pycache_prefix and not os.path.lexists(sys.pycache_prefix)
assert not (B / 'DELTA_CLOSURE.actual.json').exists()
CHECKS = 0
started = time.time()


def need(ok, why):
    global CHECKS
    CHECKS += 1
    assert ok, why


def key(path):
    p = Path(path)
    data = p.read_bytes()
    return {'sha256': hashlib.sha256(data).hexdigest(), 'bytes': len(data),
            'resolved': str(p.resolve()), 'symlink': os.readlink(p) if p.is_symlink() else None}


def js(path):
    body = Path(path).read_bytes()
    return json.loads(gzip.decompress(body) if str(path).endswith('.gz') else body)


history = B / 'history/initial_before_delta'
old_seal = key(history / 'SHA256SUMS')
need(old_seal['sha256'] == '81b5f97a6b25d6f9e82db87001da1a54668c01268038694d4b8a3b61006b02c3', 'exact physically preserved initial seal')
need((B / 'SHA256SUMS').read_bytes() == (history / 'SHA256SUMS').read_bytes(), 'old current seal intact until final replacement')
initial = {}
for line in (history / 'SHA256SUMS').read_text().splitlines():
    digest, name = line.split('  ', 1)
    need(name not in initial and not Path(name).is_absolute() and '..' not in Path(name).parts, 'exact safe initial manifest')
    selected = history / name if name == 'DELTA.md' else B / name
    need(key(selected)['sha256'] == digest, 'all initial payload bytes preserved')
    initial[name] = digest
need(len(initial) == 407, 'all 407 initial payloads')
preserved = (B / 'INITIAL_PRESERVED_PINS.sha256').read_text().splitlines()
need(len(preserved) == 408, 'all 408 preserved roles including initial seal')
for line in preserved:
    digest, name = line.split('  ', 1)
    need(key(ROOT / name)['sha256'] == digest, 'full current preserved-role pin')
before = js(B / 'DELTA_INPUTS_BEFORE.json.gz')
after = js(B / 'DELTA_INPUTS_AFTER.json.gz')
need(before == after and len(before) == 121013, 'complete common before-after physical map equality')
extra = js(B / 'DELTA_AFTER_EXTRA_INPUTS.actual.json')
need(set(extra) == {str(B / name) for name in ['DELTA_INPUTS_BEFORE.json.gz', 'CURRENT_FINDINGS.json', 'DELTA.md']}, 'exact three later decision inputs')
for name, wanted in extra.items():
    need(key(name) == wanted, 'actual unchanged after-decision input')
for name in ['delta_inspect.py', 'launch_command.py', 'preserve_initial_delta.py']:
    need(key(B / name) == before[str(B / name)], 'actual unchanged delta source across both passes')
findings = js(B / 'CURRENT_FINDINGS.json')
need(findings['phase'] == 'ACCEPTED_EXACT_NOCHANGE_DELTA' and findings['accepted_delta'] and findings['same_actual_initial_reviewer'], 'actual same-reviewer accepted decision')
need(findings['current_open_counts'] == {'Critical': 0, 'Major': 0, 'Minor': 0}, 'all three current severity counts zero')
need(findings['reviewer_infrastructure_resolved_counts'] == {'Critical': 0, 'Major': 0, 'Minor': 2} and findings['inherited_A_findings']['resolved_Major'] == 1, 'all resolved historical findings retained')
need(key(B / 'FINDINGS.json')['sha256'] == findings['initial_findings_sha256'] and key(B / 'REPORT.md')['sha256'] == findings['initial_report_sha256'], 'initial report and findings unchanged')
need(key(findings['accepted_response_path'])['sha256'] == findings['accepted_response_sha256'] == '10d856f1c5b0ab7aa12229c9b4262b6888b439bacaa28b0374483f9a60cf12c7', 'exact actual response')
native = []
for result_file in sorted(B.rglob('RESULT.json')):
    directory = result_file.parent
    if not (directory / 'ATTEMPT.json').is_file():
        continue
    start, end = js(directory / 'ATTEMPT.json'), js(result_file)
    expected = 1 if directory in {B / 'native/build01', B / 'native/audit01'} else 0
    need(type(end['native_returncode']) is int and end['native_returncode'] == expected, 'real numeric native code including preserved failures')
    need(start['environment'] == ENV, 'safe actual native environment')
    need(end.get('end_ns', end.get('ended_epoch')) >= start.get('start_ns', start.get('started_epoch')), 'native chronological binding')
    for stream in ['stdout', 'stderr']:
        wanted = end[stream]['sha256'] if stream in end else end[stream + '_sha256']
        need(key(directory / stream)['sha256'] == wanted, 'entire actual raw native stream binding')
        if stream in end:
            need(key(directory / stream)['bytes'] == end[stream]['bytes'], 'entire actual raw native stream size')
    settlement = end.get('settlement', end.get('process_group_settlement'))
    need(settlement['quiescent'] and not any(row['state'] != 'Z' for row in settlement['remaining_members']), 'native process group settled')
    if 'launcher_source' in start:
        name = directory.name
        launcher = 'launch_build_v2.py' if name == 'build02' else 'launch.py' if name in ['produce01', 'pair01', 'build01'] else 'launch_command.py'
        need(key(B / launcher)['sha256'] == start['launcher_source']['sha256'], 'actual native launcher source remains exact')
    for argument in start['argv']:
        if argument.startswith('pycache_prefix='):
            need(not os.path.lexists(argument.split('=', 1)[1]), 'actual declared cache remains absent')
    native.append({'directory': str(directory.relative_to(B)), 'native_returncode': expected})
need(len(native) == 66, '63 original plus preservation and two delta native parents')
for phase, expected_checks in [('before', 1978529), ('after', 1978541)]:
    record = js(B / ('DELTA_' + phase.upper() + '.actual.json'))
    need(record == js(B / ('native/delta_' + phase + '01/stdout')), 'entire delta native stdout equals actual summary')
    need(record['checks'] == expected_checks and record['full_physical_input_paths_reread_twice'] == 121013 and record['full_Python_byte_comparisons'] == 995, 'actual completed delta audit counts')
    need(record['new_scientific_runs'] == record['new_builds'] == record['new_views'] == record['old_writers_executed'] == 0, 'change-sensitive no new science or old writer execution')
need(js(B / 'DELTA_AFTER.actual.json')['all_common_before_after_keys_equal'], 'actual after-pass equality predicate')
links = []
for path in sorted(B.glob('*.md')):
    for href in re.findall(r'\[[^\]]*\]\(([^)]+)\)', path.read_text()):
        if href.startswith(('http://', 'https://', '#')):
            continue
        target = (path.parent / href.split('#', 1)[0]).resolve()
        need(target.is_file(), ('current physical markdown link', str(path), href))
        links.append({'document': path.name, 'href': href, 'physical': str(target), **key(target)})
closure = {'status': 'PASS_ACCEPTED_SAME_B_DELTA_FINAL_SEAL_GATE', 'checks': CHECKS,
    'started_epoch': started, 'ended_epoch': time.time(), 'source': key(Path(__file__)),
    'initial_payloads_preserved': 407, 'initial_seal': old_seal, 'initial_unchanged_in_place_except_delta': 406,
    'common_input_keys': 121013, 'later_decision_input_keys': 3, 'native_records': native,
    'native_record_count': 66, 'links': links, 'current_findings': key(B / 'CURRENT_FINDINGS.json'),
    'accepted_delta': key(B / 'DELTA.md'), 'accepted_response': key(findings['accepted_response_path']),
    'before_summary': key(B / 'DELTA_BEFORE.actual.json'), 'after_summary': key(B / 'DELTA_AFTER.actual.json'),
    'no_new_full_host_reaudit_by_sealer': True, 'full_host_keys_checked_twice_in_each_actual_delta_phase': True,
    'root_final_reception': 'SEPARATE_PENDING_GATE', 'round2_or_terminal_completion': 'NOT_PREGRANTED',
    'owner': 'OWNER_AMBER', 'external': 'HOLD_EXTERNAL'}
with (B / 'DELTA_CLOSURE.actual.json').open('x') as stream:
    json.dump(closure, stream, sort_keys=True, indent=2)
    stream.write('\n')
manifest_path = B / 'SHA256SUMS'
pending = B / 'SHA256SUMS.final.pending'
need(not pending.exists(), 'exclusive final manifest staging path')
payloads = sorted(p for p in B.rglob('*') if p.is_file() and p != manifest_path)
need(all(not p.is_symlink() for p in B.rglob('*')), 'physical review package no symlinks')
with pending.open('x') as stream:
    for path in payloads:
        stream.write(key(path)['sha256'] + '  ' + str(path.relative_to(B)) + '\n')
os.replace(pending, manifest_path)
rows = {}
for line in manifest_path.read_text().splitlines():
    digest, name = line.split('  ', 1)
    need(name not in rows and key(B / name)['sha256'] == digest, 'complete final nonself payload verification')
    rows[name] = digest
need(set(rows) == {str(p.relative_to(B)) for p in B.rglob('*') if p.is_file() and p != manifest_path}, 'exact final nonself physical coverage including historical seal')
print(json.dumps({'status': 'SEALED_ACCEPTED_SAME_B_EXACT_NOCHANGE_DELTA', 'payloads': len(rows), 'physical_files': len(rows)+1,
    'manifest_sha256': key(manifest_path)['sha256'], 'checks_including_final_manifest': CHECKS,
    'initial_payloads_preserved': 407, 'unchanged_initial_payloads_in_place_except_delta': 406,
    'actual_native_records': 66, 'common_delta_keys': 121013,
    'current_open': findings['current_open_counts'], 'root_final_reception': 'SEPARATE_PENDING_GATE'}, sort_keys=True))
