#!/usr/bin/env python3
"""Record a read-only P207 lifecycle delta check, never a numerical replay.

An exclusive attempt directory preserves exact child streams and this source.
The check accepts exactly the two already authorized lifecycle changes. It
does not rewrite either full terminal result or any historical dependency map.
"""
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
PAPER = ROOT/'papers/207-upper-neighbor-rank-dynamics'
STATUS_KEY = 'papers/207-upper-neighbor-rank-dynamics/PAPER_STATUS.md'
MANIFEST_KEY = 'papers/207-upper-neighbor-rank-dynamics/SHA256SUMS'
ALIASES = {STATUS_KEY: HERE/'lifecycle_before/PAPER_STATUS.md',
           MANIFEST_KEY: HERE/'lifecycle_before/PAPER_SHA256SUMS'}
CHECKS = 0
CONSUMED = {}


def need(condition, label):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise RuntimeError(label)


def info(raw):
    return {'bytes': len(raw), 'sha256': sha256(raw).hexdigest()}


def read(path):
    path = Path(path)
    need(path.is_file(), f'regular file: {path}')
    if path.is_relative_to(ROOT):
        need(not path.is_symlink(), f'no workspace symlink: {path}')
    raw = path.read_bytes()
    key = str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)
    actual = info(raw)
    need(key not in CONSUMED or CONSUMED[key] == actual, f'stable consumed bytes: {key}')
    CONSUMED[key] = actual
    return raw


def manifest(raw):
    rows = []
    for line in raw.decode('utf-8').splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        need(match is not None, 'exact SHA256SUMS syntax')
        digest, name = match.groups()
        rel = Path(name)
        need(not rel.is_absolute() and '..' not in rel.parts, 'relative manifest entry')
        rows.append((name, digest))
    need(len(dict(rows)) == len(rows), 'unique manifest entries')
    return rows


def check():
    started = datetime.now(timezone.utc).isoformat()
    read(Path(__file__).resolve())
    old = json.loads(read(HERE/'initial_02/run.stdout'))
    new = json.loads(read(HERE/'lifecycle_01/run.stdout'))
    need(set(old) == set(new), 'same terminal result field set')
    for label, data in [('initial_02', old), ('lifecycle_01', new)]:
        receipt = json.loads(read(HERE/label/'RECEIPT.json'))
        need(receipt['exit_code'] == 0 and receipt['execution_succeeded_and_inputs_stable'] is True,
             f'{label}: actual successful receipt')
        need(receipt['before_execution_inputs'] == receipt['after_execution_inputs'], f'{label}: stable recorder inputs')
        need(receipt['before_execution_inputs']['recorder'] == info(read(HERE/'record_attempt.py')),
             f'{label}: unchanged terminal recorder')
        need(receipt['before_execution_inputs']['python'] == info(read(Path(sys.executable).resolve())),
             f'{label}: unchanged recorded Python binary')
        need(receipt['command'] == [str(Path(sys.executable).resolve()), '-I', '-B', str(HERE.parent/'audit_p207.py')]
             and receipt['cwd'] == str(ROOT), f'{label}: explicit actual command and cwd')
        for kind in ['stdout', 'stderr']:
            actual = info(read(HERE/label/receipt[kind]['path']))
            need(actual == {k: receipt[kind][k] for k in ['bytes', 'sha256']}, f'{label}: complete raw {kind}')
        need(receipt['stderr']['bytes'] == 0, f'{label}: empty stderr')
        need(data['status'] == 'PASS_P207_TERMINAL_ARTIFACT_GATE', f'{label}: actual artifact PASS')
        need(data['fresh_mathematical_executions'] == data['fresh_builds'] == data['fresh_page_views'] == 0,
             f'{label}: no new mathematics, build or view')
        need(info(read(HERE/label/'executed_source_snapshot.py')) == receipt['before_execution_inputs']['checker'],
             f'{label}: exact executed-source snapshot')
        need(data['auditor_sha256'] == receipt['before_execution_inputs']['checker']['sha256'], f'{label}: code binding')
        need(receipt['artifact_checks'] == data['checks'], f'{label}: check count')
        expected = manifest(read(HERE/label/'SHA256SUMS'))
        need(len(expected) == 4, f'{label}: four sealed attempt files')
        for name, digest in expected:
            need(info(read(HERE/label/name))['sha256'] == digest, f'{label}: attempt seal {name}')
    need(old['auditor_sha256'] == new['auditor_sha256'] == info(read(HERE.parent/'audit_p207.py'))['sha256'],
         'identical unchanged terminal checker for both actual runs')
    allowed = {'actual_final_page_attestations_and_links', 'all_consumed_inputs_rechecked',
               'checks', 'checks_by_section', 'ended_utc', 'started_utc'}
    need({key for key in old if old[key] != new[key]} == allowed, 'exact terminal result field differences')
    need(old['checks'] == 84416 and new['checks'] == 84417, 'one extra link check only')
    expected_sections = dict(old['checks_by_section'])
    expected_sections['local_links'] += 1
    need(new['checks_by_section'] == expected_sections, 'only local-link check count changes')
    old_views = old['actual_final_page_attestations_and_links']
    new_views = new['actual_final_page_attestations_and_links']
    need({key for key in old_views if old_views[key] != new_views[key]} == {'all_local_links', 'local_links_checked'},
         'all page-view attestations unchanged')
    encode = lambda row: json.dumps(row, sort_keys=True, separators=(',', ':'))
    before_links = Counter(map(encode, old_views['all_local_links']))
    after_links = Counter(map(encode, new_views['all_local_links']))
    addition = {'document': STATUS_KEY, 'semantic_origin': STATUS_KEY,
                'target': '../../docs/papers204_208_sequence/P207_FINAL_QA.md'}
    need(after_links - before_links == Counter({encode(addition): 1}) and not before_links - after_links,
         'exact one added completion-evidence link, zero removed links')
    need(old_views['local_links_checked'] == 415 and new_views['local_links_checked'] == 416, 'exact link totals')
    need((ROOT/STATUS_KEY).parent.joinpath(addition['target']).resolve().is_file(), 'added link exists')
    before_map = old['all_consumed_inputs_rechecked']
    after_map = new['all_consumed_inputs_rechecked']
    need(set(before_map) == set(after_map) and len(before_map) == 1197, 'same complete 1197-key input set')
    changes = {key: {'before': before_map[key], 'after': after_map[key]}
               for key in before_map if before_map[key] != after_map[key]}
    need(set(changes) == set(ALIASES), 'exactly status plus whole-paper manifest changed')
    alias_records = {}
    for key, wanted in before_map.items():
        target = ALIASES.get(key, ROOT/key)
        need(info(read(target)) == wanted, f'historical input verified via explicit lifecycle alias: {key}')
        if key in ALIASES:
            alias_records[key] = {'preserved_path': str(target.relative_to(ROOT)), 'verified_original_bytes': wanted}
    for key, wanted in after_map.items():
        need(info(read(ROOT/key)) == wanted, f'current input verified with no lifecycle alias: {key}')
    preserved_manifest = manifest(read(HERE/'lifecycle_before/SHA256SUMS'))
    need({name for name, digest in preserved_manifest} == {'PAPER_STATUS.md', 'PAPER_SHA256SUMS'},
         'exact two-file historical lifecycle seal')
    for name, digest in preserved_manifest:
        need(info(read(HERE/'lifecycle_before'/name))['sha256'] == digest, f'preserved lifecycle seal: {name}')
    old_manifest = manifest(read(ALIASES[MANIFEST_KEY]))
    new_manifest = manifest(read(PAPER/'SHA256SUMS'))
    need([name for name, digest in old_manifest] == [name for name, digest in new_manifest],
         'same complete ordered whole-paper manifest paths')
    need(len(new_manifest) == 614, 'complete 614-entry paper closure')
    before_hashes, after_hashes = dict(old_manifest), dict(new_manifest)
    need(before_hashes['PAPER_STATUS.md'] == before_map[STATUS_KEY]['sha256'] and
         after_hashes['PAPER_STATUS.md'] == after_map[STATUS_KEY]['sha256'], 'both manifest status rows bind exact respective inputs')
    manifest_changes = {name: {'before': before_hashes[name], 'after': after_hashes[name]}
                        for name in before_hashes if before_hashes[name] != after_hashes[name]}
    need(set(manifest_changes) == {'PAPER_STATUS.md'}, 'only status payload changed inside paper manifest')
    actual_files = {str(path.relative_to(PAPER)) for path in PAPER.rglob('*') if path.is_file()}
    need(actual_files == set(after_hashes) | {'SHA256SUMS'}, 'complete current paper nonself coverage')
    for name, digest in new_manifest:
        need(info(read(PAPER/name))['sha256'] == digest, f'current paper payload: {name}')
    for path, resolved in new['contemporaneous_host_symlink_resolutions'].items():
        need(str(Path(path).resolve()) == resolved, f'unchanged host symlink resolution: {path}')
    consumed_before = dict(CONSUMED)
    for key, wanted in consumed_before.items():
        need(info(read(ROOT/key)) == wanted, f'all consumed bytes rechecked at end: {key}')
    print(json.dumps({'status': 'PASS_P207_LIFECYCLE_ONLY_DELTA', 'checks': CHECKS,
                      'started_utc': started, 'ended_utc': datetime.now(timezone.utc).isoformat(),
                      'old_actual_artifact_checks': old['checks'], 'new_actual_artifact_checks': new['checks'],
                      'same_input_keyset_count': 1197, 'historical_inputs_rechecked_with_explicit_aliases': 1197,
                      'current_inputs_rechecked_without_lifecycle_aliases': 1197,
                      'explicit_historical_lifecycle_aliases': alias_records, 'exact_changed_inputs': changes,
                      'ordered_paper_manifest_entries': 614, 'exact_changed_manifest_payloads': manifest_changes,
                      'exact_added_link': addition, 'same_current_page_attestations': True,
                      'all_consumed_input_count': len(consumed_before), 'all_consumed_inputs_rechecked': consumed_before,
                      'fresh_mathematical_executions': 0, 'fresh_builds': 0, 'fresh_page_views': 0,
                      'scope': 'Lifecycle-only supplement to two immutable actual terminal outputs; not a third review or a five-paper batch gate.',
                      'historical_alias_note': 'Only the two named before-status snapshots replace those historical keys; the original result map is never edited.',
                      'external_status': 'HOLD_EXTERNAL'}, indent=2, sort_keys=True))


def save(path, raw):
    with path.open('xb') as stream:
        stream.write(raw)


def record(label):
    need(re.fullmatch('[a-z0-9_]+', label) is not None, 'fresh lowercase attempt label')
    out = HERE/label
    out.mkdir(exist_ok=False)
    source = Path(__file__).resolve()
    python = Path(sys.executable).resolve()
    save(out/'executed_source_snapshot.py', source.read_bytes())
    before = {'checker_and_recorder': info(source.read_bytes()), 'python': info(python.read_bytes())}
    command = [str(python), '-I', '-B', str(source), '--check']
    started = datetime.now(timezone.utc).isoformat()
    with (out/'run.stdout').open('xb') as stdout, (out/'run.stderr').open('xb') as stderr:
        child = subprocess.run(command, cwd=ROOT, stdout=stdout, stderr=stderr, check=False)
    after = {'checker_and_recorder': info(source.read_bytes()), 'python': info(python.read_bytes())}
    result = json.loads((out/'run.stdout').read_bytes()) if child.returncode == 0 else None
    passed = child.returncode == 0 and before == after and result.get('status') == 'PASS_P207_LIFECYCLE_ONLY_DELTA'
    receipt = {'kind': 'ACTUAL_READ_ONLY_P207_LIFECYCLE_DELTA_NOT_MATHEMATICS_BUILD_OR_VIEW',
               'command': command, 'cwd': str(ROOT), 'started_utc': started,
               'ended_utc': datetime.now(timezone.utc).isoformat(), 'exit_code': child.returncode,
               'pass_and_execution_inputs_stable': passed, 'before_execution_inputs': before,
               'after_execution_inputs': after, 'checks': result.get('checks') if result else None,
               'raw_output_note': 'Binary child streams, no JSON reserialization, text normalization or patch transport.',
               'source_note': 'Original script executed; exact source snapshot matches its before/after hash.',
               'stdout': {'path': 'run.stdout', **info((out/'run.stdout').read_bytes())},
               'stderr': {'path': 'run.stderr', **info((out/'run.stderr').read_bytes())}}
    save(out/'RECEIPT.json', (json.dumps(receipt, indent=2, sort_keys=True)+'\n').encode())
    save(out/'SHA256SUMS', ''.join(info(path.read_bytes())['sha256']+'  '+path.name+'\n'
                                  for path in sorted(out.iterdir()) if path.is_file()).encode())
    print(json.dumps({'pass': passed, 'exit_code': child.returncode, 'checks': receipt['checks'],
                      'receipt': str(out/'RECEIPT.json'), 'stdout': receipt['stdout'], 'stderr': receipt['stderr']}, indent=2))
    raise SystemExit(0 if passed else 1)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        raise SystemExit('Expected --check or one fresh lowercase attempt label')
    if sys.argv[1] == '--check':
        check()
    else:
        record(sys.argv[1])
