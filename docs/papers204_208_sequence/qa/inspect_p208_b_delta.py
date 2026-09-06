"""Read-only root validation of P208 B's exact documentary delta closure.

No scientific producer, reviewer recorder or TeX process is imported or run.
Complete stdout is the result; no immutable package is modified.
"""
from pathlib import Path
from hashlib import sha256
import ast
import json
import sys

ROOT = Path(__file__).resolve().parents[3]
BATCH = ROOT / 'docs/papers204_208_sequence'
BASE = BATCH / 'reviews/p208_b'
D = BASE / 'delta'
PAPER = ROOT / 'papers/208-original-snapshot-triangulation-sweeps'

def h(p):
    return sha256(Path(p).read_bytes()).hexdigest()

def j(p):
    return json.loads(Path(p).read_bytes())

def rows(p):
    result = {}
    for line in Path(p).read_text().splitlines():
        digest, name = line.split('  ', 1)
        q = Path(name)
        assert len(digest) == 64 and not q.is_absolute() and '..' not in q.parts
        assert name not in result
        result[name] = digest
    return result

def complete(base, name='SHA256SUMS'):
    values = rows(base / name)
    assert set(values) == {p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file() and p != base / name}
    for n, value in values.items():
        assert not (base / n).is_symlink() and h(base / n) == value, n
    return values

def main():
    if sys.flags.optimize or not (sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode):
        raise RuntimeError('Require optimization zero and -I -S -B')
    seal_before = h(BASE / 'SHA256SUMS')
    final = complete(BASE)
    assert len(final) == 3545
    initial = rows(D / 'initial_snapshot/SHA256SUMS')
    assert h(D / 'initial_snapshot/SHA256SUMS') == '64a58b80ac92f98caff178a34a8ef6199c83eace414c043d72d4ce81eeff78a5'
    mapping = j(D / 'INITIAL_PAYLOAD_MAPPING.json')
    assert set(mapping) == set(initial) and len(initial) == 1546
    for n, row in mapping.items():
        expected = 'delta/initial_snapshot/FINDINGS.json' if n == 'FINDINGS.json' else n
        assert row['historical_path'] == expected
        assert h(BASE / expected) == row['sha256'] == initial[n]
    history = j(D / 'HISTORY_INPUT_MAPPING.json')
    old = j(BASE / 'history_context/SEARCH_INPUTS_BEFORE.json')
    assert old == j(BASE / 'history_context/SEARCH_INPUTS_AFTER.json')
    assert len(history) == 1917 and set(history) == {str(ROOT / n) for n in old}
    for p, row in history.items():
        rel = Path(p).relative_to(ROOT).as_posix()
        assert row['historical_path'] == 'delta/history_inputs/' + rel
        assert h(BASE / row['historical_path']) == row['sha256'] == old[rel]
    archive_observation = j(D / 'HISTORY_ORIGINALS_AT_ARCHIVE.json')
    assert set(archive_observation) == set(history)
    assert all(v['matches_initial_search'] and v['sha256'] == history[p]['sha256'] for p, v in archive_observation.items())
    baseline = j(D / 'INPUTS_BEFORE.json')
    assert len(baseline) == 114998
    for p, row in baseline.items():
        expected = (str(D / 'initial_snapshot' / Path(p).name) if p in (str(BASE / 'SHA256SUMS'), str(BASE / 'FINDINGS.json'))
                    else str(BASE / history[p]['historical_path']) if p in history else p)
        assert row['validated_path'] == expected and h(expected) == row['sha256'], p
    response = j(D / 'ROOT_RESPONSE_PINS_BEFORE.json')
    assert len(response) == 45
    for p, row in response.items():
        assert row['snapshot'] == 'delta/root_context/' + Path(p).relative_to(ROOT).as_posix()
        assert h(p) == h(BASE / row['snapshot']) == row['sha256']
    config = j(D / 'CONFIGURATION_BEFORE.json')
    for group in config.values():
        for p, row in group.items():
            q = Path(p)
            current = {'exists': q.exists()}
            if 'resolved' in row: current['resolved'] = str(q.resolve())
            if 'sha256' in row: current['sha256'] = h(q) if q.is_file() else None
            if 'bytes' in row: current['bytes'] = q.stat().st_size if q.is_file() else None
            assert current == row, p
    audit_results = []
    covered = {row['validated_path']: row['sha256'] for row in baseline.values()}
    for phase, checks in [('audit01', 120677), ('audit02', 120678)]:
        directory = D / phase
        command = j(directory / 'COMMAND.json')
        assert command['exit_code'] == 0 and command['unused_cache_absent']
        assert command['environment'] == {'LANG': 'C', 'LC_ALL': 'C', 'PATH': '/root/miniconda3/bin:/usr/bin:/bin', 'TZ': 'UTC'}
        assert command['argv'][1:4] == ['-I', '-S', '-B'] and '-O' not in command['argv']
        for stream in ('stdout', 'stderr'):
            assert h(directory / ('audit.' + stream)) == command[stream + '_sha256']
        assert (directory / 'audit.stderr').read_bytes() == b''
        result = j(directory / 'audit.stdout')
        assert result['status'] == 'PASS_DOCUMENTARY_DELTA_AUDIT' and result['checks'] == checks
        assert result['delta_accepted'] == (phase == 'audit02')
        assert j(directory / 'INPUTS_AFTER.json') == baseline
        assert j(directory / 'ROOT_RESPONSE_PINS_AFTER.json') == response
        assert j(directory / 'CONFIGURATION_AFTER.json') == config
        consumed = {}
        for when in ('BEFORE', 'AFTER'):
            rt = j(directory / ('RUNTIME_' + when + '.json'))
            assert 'optimize=0' in rt['flags'] and 'isolated=1' in rt['flags'] and 'no_site=1' in rt['flags']
            assert not Path(rt['pycache_prefix']).exists()
            consumed.update(rt['mapped_files'])
            consumed.update({v['file']: v['sha256'] for v in rt['modules'].values() if v['sha256']})
        assert j(directory / 'RUNTIME_COVERAGE.json') == {'consumed': consumed, 'missing': {}}
        for p, digest in consumed.items():
            assert covered[p] == h(p) == digest, p
        audit_results.append({'phase': phase, 'checks': checks, 'observed_runtime_paths': len(consumed), 'exit_code': 0})
    for n, digest in j(D / 'audit02/CHANGED_DOCUMENTS_AFTER.json').items():
        assert h(BASE / n) == digest
    prep = j(BASE / 'delta_prepare_execution/COMMAND.json')
    assert prep['exit_code'] == 0
    for stream in ('stdout', 'stderr'):
        assert h(BASE / 'delta_prepare_execution' / ('audit.' + stream)) == prep[stream + '_sha256']
    assert j(BASE / 'delta_prepare_execution/audit.stdout') == j(D / 'PREPARE_RECEIPT.json')
    # Read only literal infrastructure constants, never execute its recorder.
    tree = ast.parse((BASE / 'record_build.py').read_bytes())
    constants = {n.targets[0].id: ast.literal_eval(n.value) for n in tree.body if isinstance(n, ast.Assign)
                 and len(n.targets) == 1 and isinstance(n.targets[0], ast.Name)
                 and n.targets[0].id in ('TEX_ROOTS', 'CONFIG_ROOTS', 'CONFIG_EXPLICIT')}
    def inventory(roots):
        return {str(p.resolve()): h(p) for root in roots if Path(root).exists() for p in Path(root).rglob('*') if p.is_file()}
    tex = inventory(constants['TEX_ROOTS'])
    config_files = inventory(constants['CONFIG_ROOTS'])
    config_files.update({p: h(p) for p in constants['CONFIG_EXPLICIT'] if Path(p).is_file()})
    assert tex == j(BASE / 'source_build/TEX_INVENTORY_BEFORE.json')
    assert config_files == j(BASE / 'source_build/CONFIG_BEFORE.json')
    freeze = complete(PAPER / 'frozen_round1')
    assert len(freeze) == 487 and freeze == complete(PAPER / 'frozen_round0')
    for n, digest in freeze.items():
        assert h(PAPER / n) == digest
    findings = j(BASE / 'FINDINGS.json')
    assert findings['delta_accepted'] and findings['stage'] == 'ACCEPTED_NO_CHANGE_DELTA'
    assert findings['census']['open'] == {'critical': 0, 'major': 0, 'minor': 0}
    assert all(f['status'] == 'resolved' for f in findings['findings'])
    final_receipt = j(D / 'FINAL_SEAL_RECEIPT.json')
    assert final_receipt['payload_count'] == len(final) and final_receipt['delta_sha256'] == h(BASE / 'DELTA.md')
    assert seal_before == h(BASE / 'SHA256SUMS') and final == complete(BASE)
    print(json.dumps({'status': 'ROOT_ACCEPTED_B_DELTA_ORIGINAL_CLOSURE_PASS',
        'review_manifest_entries': len(final), 'review_manifest_sha256': seal_before,
        'delta_sha256': h(BASE / 'DELTA.md'), 'baseline_referents': len(baseline),
        'initial_payloads_preserved': len(initial), 'history_inputs_preserved': len(history),
        'root_response_paths': len(response), 'actual_audits': audit_results,
        'recaptured_tex_paths': len(tex), 'recaptured_build_config_paths': len(config_files),
        'unchanged_live_frozen_inputs': len(freeze), 'current_open_findings': 0,
        'new_scientific_execution': False, 'new_build_or_view': False,
        'inspection_script_sha256': h(__file__)}, sort_keys=True, indent=2))

if __name__ == '__main__':
    main()
