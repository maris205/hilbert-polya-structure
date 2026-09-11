#!/usr/bin/env python3
"""Root read-only complete initial-A archive check, not scientific execution."""
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASE = ROOT / 'docs/papers204_208_sequence/reviews/p209_a'
FREEZE = ROOT / 'papers/209-ordered-fibre-threading/frozen_round0'
SEAL = '7105dd2c22a7fb8df5586a59880fdc47e26f62f2d7573d3f08570eda5c62fb0c'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
READS = {}


def pin(raw, fresh=False):
    p = Path(raw)
    key = str(p)
    if fresh or key not in READS:
        assert p.is_file(), key
        h = sha256()
        with p.open('rb') as stream:
            for b in iter(lambda: stream.read(1048576), b''):
                h.update(b)
        row = {'sha256': h.hexdigest(), 'bytes': p.stat().st_size,
               'resolved': str(p.resolve()),
               'symlink': os.readlink(p) if p.is_symlink() else None}
        if key in READS:
            assert row == READS[key], 'current read-set drift: ' + key
        READS[key] = row
    return READS[key]


def checkpin(path, expected):
    got = pin(path)
    assert all(got[k] == v for k, v in expected.items()), str(path)


def obj(path):
    pin(path)
    return json.loads(Path(path).read_bytes())


def manifest(path, base=None, complete=False):
    path = Path(path)
    base = path.parent if base is None else base
    pin(path)
    rows = {}
    for line in path.read_text().splitlines():
        h, n = line.split('  ', 1)
        p = Path(n)
        assert re.fullmatch('[0-9a-f]{64}', h) and not p.is_absolute()
        assert '..' not in p.parts and p.as_posix() == n and n not in rows
        assert not (base / p).is_symlink()
        assert pin(base / p)['sha256'] == h, str(base / p)
        rows[n] = h
    if complete:
        entries = list(base.rglob('*'))
        assert not any(p.is_symlink() for p in entries)
        assert set(rows) == {p.relative_to(base).as_posix() for p in entries
                             if p.is_file() and p != path}
    return rows


def settings_and_commands(folder, mode):
    expected_n = 85 if mode == 'pair' else 125
    receipt = obj(folder / 'RECEIPT.json')
    assert receipt['status'] == 'PASS_REVIEW_A_' + mode.upper() and not receipt['failures']
    before = obj(folder / 'ALL_INPUTS_INCLUDING_CAPSULES_BEFORE.json')
    assert before == obj(folder / 'ALL_INPUTS_AFTER.json')
    for p, value in before.items():
        checkpin(p, value)
    assert len(before) == receipt['known_all_inputs_including_capsules']
    cfg = obj(folder / 'CONFIGURATION_BEFORE.json')
    assert cfg == obj(folder / 'CONFIGURATION_AFTER.json')
    for p, row in cfg['optional'].items():
        q = Path(p)
        assert q.exists() == row['exists'] and q.is_file() == row['is_file']
        assert str(q.resolve()) == row['resolved']
        if q.is_file():
            checkpin(q, {k: row[k] for k in ('sha256', 'bytes')})
    for p, names in cfg['directories'].items():
        q = Path(p)
        assert (sorted(str(x) for x in q.rglob('*') if x.is_file()) if q.is_dir() else None) == names
    assert obj(folder / 'RUNTIME_BEFORE.json') == obj(folder / 'RUNTIME_AFTER.json')
    closure = obj(folder / 'OBSERVED_CLOSURE.json')
    assert not closure['uncovered'] and not closure['bytecode']
    for phase in ('BEFORE', 'AFTER'):
        obs = obj(folder / ('PARENT_' + phase + '.json'))
        assert obs['env'] == ENV and obs['cwd'] == str(ROOT)
        assert obs['optimization'] == 0 and not obs['cache_exists']
        assert obs['pycache_prefix'] == str(folder / 'never_created_parent_cache')
    commands = obj(folder / 'ALL_COMMAND_RECORDS.json')
    assert len(commands) == expected_n
    for entry in commands:
        where, tag, row = Path(entry['folder']), entry['tag'], entry['command']
        assert where.is_relative_to(folder)
        assert obj(where / (tag + '.command.json')) == row
        attempt = obj(where / (tag + '.attempt.json'))
        assert all(attempt[k] == row[k] for k in ('argv', 'cwd', 'env', 'stdout', 'stderr'))
        assert row['process_outcome'] == 'COMPLETED' and row['exit'] == 0
        assert row['spawn_error'] is None and row['cleanup'] == []
        assert all(row['env'][k] == v for k, v in ENV.items())
        for stream in ('stdout', 'stderr'):
            checkpin(where / row[stream], row[stream + '_info'])
    if mode == 'pair':
        assert len(before) == 5145 and receipt['result']['canonical_adopted'] is True
        for label in ('replay_01', 'replay_02'):
            p = folder / label
            child = obj(p / 'RECEIPT.json')
            assert child['status'] == 'PASS' and child['checks'] == 135605 and child['total_states'] == 3414
            assert child['source_only_initial_names'] == ['bootstrap.py', 'verify.py']
            for name in child['source_only_initial_names']:
                assert pin(BASE / name)['sha256'] == pin(p / 'source_inputs' / name)['sha256']
            for phase in ('before', 'after'):
                obs = obj(p / ('child.' + phase + '.json'))
                assert obs['env'] == ENV and obs['cwd'] == str(p)
                assert obs['optimize'] == 0 and obs['isolated'] == obs['no_site'] == 1
                assert obs['dont_write_bytecode'] and not obs['cache_exists']
                assert obs['pycache_prefix'] == str(p / 'never_created_child_cache')
    else:
        assert len(before) == 120345 and receipt['result']['pages'] == 4
        assert receipt['result']['embedded_fonts'] == 20
        assert not any(receipt['result']['diagnostics'].values())
        tex = obj(folder / 'TEX_RESOURCES_BEFORE.json')
        assert tex == obj(folder / 'TEX_RESOURCES_AFTER.json')
        assert {str(p) for r in tex['roots'] if Path(r).is_dir()
                for p in Path(r).rglob('*') if p.is_file()} == set(tex['files'])
        for p, exists in tex['roots'].items():
            assert Path(p).exists() == exists
        sources = obj(folder / 'SOURCE_ONLY_INITIAL.json')
        assert len(sources) == 8
        for p, value in sources.items():
            checkpin(p, value)
            checkpin(FREEZE / Path(p).relative_to(folder / 'cold_build'),
                     {k: value[k] for k in ('sha256', 'bytes')})
        used = obj(folder / 'CONSUMED_TEX.json')
        assert len(used) == 131
        for p, value in used.items():
            checkpin(p, value)
        for phase in ('BEFORE', 'AFTER'):
            assert all(not row['exists'] and not Path(row['path']).exists()
                       for row in obj(folder / ('USER_ROOTS_' + phase + '.json')).values())
    return {'mode': mode, 'known_inputs': len(before), 'commands': len(commands)}


def main():
    assert pin(BASE / 'SHA256SUMS')['sha256'] == SEAL
    outer = manifest(BASE / 'SHA256SUMS', complete=True)
    initial = manifest(BASE / 'INITIAL_ARTIFACTS.sha256')
    assert len(outer) == 1227 and len(initial) == 1226
    assert set(initial) == set(outer) - {'INITIAL_ARTIFACTS.sha256'}
    assert pin(BASE / 'REPORT.md')['sha256'] == pin(BASE / 'INITIAL_REPORT.md')['sha256']
    final = obj(BASE / 'initial_audit_01/RESULT.json')
    assert final['status'] == 'PASS_INITIAL_PACKAGE_CLOSURE' and not final['delta_exists']
    inner = obj(BASE / 'initial_audit_01/INNER_MANIFESTS.json')
    assert inner == final['inner_manifests'] and len(inner) == 9
    for row in inner:
        assert pin(row['path'])['sha256'] == row['sha256']
        assert len(manifest(row['path'], complete=True)) == row['payloads']
    frozen = manifest(BASE / 'INPUT_PINS.sha256', ROOT)
    assert len(frozen) == 1990
    assert set(frozen) == {p.relative_to(ROOT).as_posix() for p in FREEZE.rglob('*') if p.is_file()}
    known = obj(BASE / 'initial_audit_01/CURRENT_INPUT_CLOSURE.json')
    assert len(known) == final['current_input_paths'] == 120491
    for p, h in known.items():
        assert pin(p)['sha256'] == h
    modes = [settings_and_commands(BASE / ('review_' + mode + '_01'), mode) for mode in ('pair', 'build')]
    for mode in ('pair', 'build'):
        launcher = BASE / ('launcher_review_' + mode + '_01')
        row = obj(launcher / 'RECEIPT.json')
        assert row['status'] == 'PASS_LAUNCH' and row['exit'] == 0 and row['inputs_unchanged'] and row['cache_absent']
        before = obj(launcher / 'INPUTS_BEFORE.json')
        assert before == obj(launcher / 'INPUTS_AFTER.json')
        for p, value in before.items():
            checkpin(p, value)
        for stream in ('recorder.stdout', 'recorder.stderr'):
            checkpin(launcher / stream, row[stream + '_pin'])
    for name in ('reconciliation_01', 'auxiliary_01'):
        folder = BASE / name
        receipt = obj(folder / 'RECEIPT.json')
        before = obj(folder / 'INPUTS_BEFORE.json')
        assert before == obj(folder / 'INPUTS_AFTER.json') and receipt['inputs_unchanged']
        for p, value in before.items():
            checkpin(p, value)
        for row in receipt['commands']:
            assert row['exit'] == 0 and row['env'] == ENV
            for stream in ('stdout', 'stderr'):
                checkpin(folder / row[stream], row[stream + '_pin'])
    rec = obj(BASE / 'reconciliation_01/reconcile.stdout')
    assert rec['status'] == 'PASS_FULL_STATE_RECONCILIATION' and rec['states'] == 3414
    assert len(rec['state_comparisons']) == 3414 and all(r['all_author_row_fields_equal'] for r in rec['state_comparisons'])
    assert obj(BASE / 'auxiliary_01/PDF_PREFLIGHT.json')['verdict'] == 'UNAVAILABLE'
    failed = obj(BASE / 'PREFLIGHT_INITIAL_FAILURE.json')
    assert failed['exit'] == 1 and 'ModuleNotFoundError' in failed['stderr']
    findings = obj(BASE / 'FINDINGS.json')
    assert findings['findings'] == [] and not any(findings['current_open_counts'].values())
    assert not (BASE / 'DELTA.md').exists()
    pairs = [(BASE / 'review_pair_01/replay_01/producer.stdout', BASE / 'review_pair_01/replay_02/producer.stdout')]
    pairs += [(BASE / ('review_pair_01/' + s + '/producer.stdout'), BASE / 'CANONICAL.json') for s in ('replay_01', 'replay_02')]
    pairs += [(BASE / 'reconciliation_01/author_projection.json', BASE / 'reconciliation_01/reviewer_projection.json'),
              (BASE / 'review_build_01/cold_build/main.pdf', FREEZE / 'main.pdf')]
    pairs += [(BASE / ('review_build_01/cold_build/pages/page-' + str(i) + '.png'),
               FREEZE / ('author_build_01/cold_build/pages/page-' + str(i) + '.png')) for i in range(1, 5)]
    comparisons = []
    for a, b in pairs:
        argv = ['/usr/bin/cmp', '--', str(a), str(b)]
        p = subprocess.run(argv, capture_output=True, env=ENV)
        assert p.returncode == 0
        comparisons.append({'argv': argv, 'exit': p.returncode,
                            'stdout': p.stdout.decode(), 'stderr': p.stderr.decode()})
    for p in list(READS):
        pin(p, fresh=True)
    assert manifest(BASE / 'SHA256SUMS', complete=True) == outer
    print(json.dumps({'status': 'PASS_ROOT_A_INITIAL_ORIGINAL_CLOSURE',
                      'review_payloads': len(outer), 'initial_preserved_payloads': len(initial),
                      'inner_manifests': len(inner), 'frozen_inputs': len(frozen),
                      'full_recorded_current_inputs': len(known), 'all_actual_read_paths_twice': len(READS),
                      'modes': modes, 'actual_root_raw_comparisons': comparisons,
                      'seal': SEAL, 'preflight_remains': 'UNAVAILABLE',
                      'boundary': 'Archive/current-input inspection and raw comparisons; no new math/build/view, no delta'},
                     indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
