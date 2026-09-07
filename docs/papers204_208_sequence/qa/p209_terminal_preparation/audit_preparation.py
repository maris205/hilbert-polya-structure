#!/usr/bin/env python3
"""Close/recheck preparation bytes only; never import or execute a builder."""
import ast
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASE = ROOT / 'docs/papers204_208_sequence/qa/p209_terminal_preparation'
PAPER = ROOT / 'papers/209-ordered-fibre-threading'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
READS = {}


def pin(path):
    path = Path(path)
    raw = path.read_bytes()
    value = {'sha256': hashlib.sha256(raw).hexdigest(), 'bytes': len(raw),
             'resolved': str(path.resolve()), 'symlink': os.readlink(path) if path.is_symlink() else None}
    if str(path) in READS:
        assert READS[str(path)] == value, str(path)
    READS[str(path)] = value
    return value


def read(path):
    pin(path)
    return Path(path).read_bytes()


def load(path):
    return json.loads(read(path))


def save(path, data):
    with path.open('xb') as stream:
        stream.write((json.dumps(data, sort_keys=True, indent=2) + '\n').encode())


def physical_entries(base):
    assert base.is_dir() and base.resolve() == base and not base.is_symlink()
    entries = list(base.rglob('*'))
    assert all(not p.is_symlink() and p.resolve() == p for p in entries)
    return sorted(p for p in entries if p.is_file())


def manifest(base):
    seal = base / 'SHA256SUMS'
    rows = {}
    for line in read(seal).decode().splitlines():
        digest, relative = line.split('  ', 1)
        path = Path(relative)
        assert re.fullmatch(r'[0-9a-f]{64}', digest)
        assert path.as_posix() == relative and path.parts and not path.is_absolute() and '..' not in path.parts
        assert relative != 'SHA256SUMS' and relative not in rows
        assert pin(base / relative)['sha256'] == digest
        rows[relative] = digest
    assert set(rows) == {p.relative_to(base).as_posix() for p in physical_entries(base) if p != seal}
    return rows


def documentary_check():
    pin(__file__)
    pin('/usr/bin/python3.10')
    revision = load(BASE / 'DRAFT_REVISION.json')
    assert revision['status'] == 'UNEXECUTED_DRAFT_CORRECTED_BEFORE_SEAL' and revision['builder_executions'] == 0
    aliases = {(r['original_path'], r['sha256']): r for r in revision['historical_input_aliases']}
    assert len(aliases) == 2
    for row in aliases.values():
        assert pin(BASE / row['physical_path'])['sha256'] == row['sha256']
        assert pin(row['original_path'])['sha256'] == row['final_sha256']
    commands = []
    for directory, count in (('checks', 21), ('checks_final', 4)):
        folders = sorted((BASE / directory).iterdir())
        assert len(folders) == count and all(p.is_dir() for p in folders)
        for folder in folders:
            assert {p.name for p in folder.iterdir()} == {'INPUTS_BEFORE.json', 'INPUTS_AFTER.json', 'ATTEMPT.json', 'RECEIPT.json', 'stdout', 'stderr'}
            before, after = load(folder / 'INPUTS_BEFORE.json'), load(folder / 'INPUTS_AFTER.json')
            row, attempt = load(folder / 'RECEIPT.json'), load(folder / 'ATTEMPT.json')
            assert before == after and row['inputs_unchanged'] is True
            used = []
            for path, value in before.items():
                if pin(path) != value:
                    assert directory == 'checks'
                    alias = aliases[(path, value['sha256'])]
                    old = pin(BASE / alias['physical_path'])
                    assert all(old[k] == value[k] for k in ('sha256', 'bytes', 'symlink')) and value['resolved'] == path
                    used.append(alias['physical_path'])
            assert row['environment'] == attempt['environment'] == ENV
            assert row['cwd'] == attempt['cwd'] == str(ROOT) and row['argv'] == attempt['argv']
            is_diff = row['argv'][0] == '/usr/bin/diff'
            assert row['argv'][0] in {'/usr/bin/diff', '/usr/bin/cmp'}
            assert row['exit'] == (1 if is_diff else 0) and row['outcome'] == 'COMPLETED'
            for kind in ('stdout', 'stderr'):
                assert row[kind] == pin(folder / kind)
            assert row['stderr']['bytes'] == 0
            if not is_diff:
                assert row['stdout']['bytes'] == 0
            commands.append({'path': str(folder), 'exit': row['exit'], 'historical_aliases': used})
    assert sum(r['exit'] == 0 for r in commands) == 19 and sum(r['exit'] == 1 for r in commands) == 6
    for combined, parts in (
        ('ADAPTATION.diff', ['checks/diff_root_terminal_builds_py/stdout', 'checks/diff_root_launch_terminal_py/stdout']),
        ('ADAPTATION_FINAL.diff', ['checks_final/whole_root_terminal_builds_py/stdout', 'checks_final/whole_root_launch_terminal_py/stdout']),
        ('DRAFT_TO_FINAL.diff', ['checks_final/draft_delta_root_terminal_builds_py/stdout', 'checks_final/draft_delta_root_launch_terminal_py/stdout'])):
        assert read(BASE / combined) == b''.join(read(BASE / p) for p in parts)
    sources = load(BASE / 'SOURCE_PINS.json')
    assert len(sources) == 8 and pin(BASE / 'SOURCE_PINS.json')['sha256'] == 'bb707e351669318169eb558dc9097ef700bb44c01418253e3944aaa8dd4cd8f2'
    assert {p.relative_to(BASE / 'source_snapshot').as_posix() for p in physical_entries(BASE / 'source_snapshot')} == set(sources)
    for n, value in sources.items():
        for base in (PAPER, PAPER / 'frozen_round1', BASE / 'source_snapshot'):
            assert all(pin(base / n)[k] == value[k] for k in ('sha256', 'bytes'))
    original = load(BASE / 'ORIGINAL_INPUTS.json')
    assert len(original) == 11 and {p.name for p in physical_entries(BASE / 'original_snapshot')} == set(original)
    for name, value in original.items():
        assert pin(value['original_path']) == {k: value[k] for k in ('sha256', 'bytes', 'resolved', 'symlink')}
        assert read(value['original_path']) == read(BASE / 'original_snapshot' / name)
    captured = load(BASE / 'SOURCE_CAPTURE.json')
    assert captured['future_round2_hash_supplied'] is False and captured['live_and_round1_unchanged'] is True
    assert captured['original_pdf'] == pin(PAPER / 'frozen_round1/main.pdf')
    contract = load(BASE / 'GATE_CONTRACT.json')
    assert contract['status'] == 'SCHEMA_ONLY_NOT_ACCEPTANCE'
    assert contract['acceptance_result_claimed'] is False and contract['execution_authorized_by_this_file'] is False
    assert contract['root_round2_gate']['future_hashes_prefilled'] is False
    static = load(BASE / 'FINAL_STATIC_CHECK.json')
    assert static['status'] == 'PASS_FINAL_STATIC_PREPARATION_ONLY' and static['builder_executions'] == 0
    assert static['whole_final_diff_bytes'] == pin(BASE / 'ADAPTATION_FINAL.diff')['bytes'] == 46304
    assert static['draft_to_final_diff_bytes'] == pin(BASE / 'DRAFT_TO_FINAL.diff')['bytes'] == 3657
    assert len(static['expected_command_labels_if_executed']) == 32
    read_pins = load(BASE / 'CONTRACT_READ_PINS.json')
    assert len(read_pins) == static['read_paths_rechecked'] == 169
    for path, value in read_pins.items():
        assert pin(path) == value, path
    python_files = sorted(p for p in physical_entries(BASE) if p.suffix == '.py')
    for path in python_files:
        ast.parse(read(path).decode(), filename=str(path))
    for name, count in (('root_terminal_builds.py', 596), ('root_launch_terminal.py', 217)):
        assert len(read(BASE / name).splitlines()) == count
    legacy = ROOT / 'papers/208-original-snapshot-triangulation-sweeps/qa_final'
    legacy_rows = manifest(legacy)
    assert len(legacy_rows) == 225
    assert read(legacy / 'executed_recorder_snapshot.py') == read(BASE / 'original_snapshot/p208_terminal_v2.py')
    assert read(legacy / 'BUILD_EXECUTION.json') == read(BASE / 'original_snapshot/P208_BUILD_EXECUTION.json')
    for path in (PAPER / 'qa_final', ROOT / 'docs/papers204_208_sequence/qa/root_replays/p209_terminal_strict'):
        assert not path.exists() and not path.is_symlink(), str(path)
    assert not any(p.suffix in {'.pyc', '.pyo'} or p.name == '__pycache__' for p in BASE.rglob('*'))
    for path in physical_entries(BASE):
        pin(path)
    before = dict(READS)
    assert before == {path: pin(path) for path in before}
    return {'status': 'PASS_DOCUMENTARY_PREPARATION_CLOSURE_ONLY', 'builder_executions': 0,
            'math_tex_pdf_render_or_guard_executions': 0, 'future_acceptance_values_supplied': False,
            'source_copy_count': 8, 'original_copy_count': 11, 'documentary_commands': commands,
            'old_p208_terminal_payloads_checked': len(legacy_rows), 'python_sources_AST_checked': len(python_files),
            'read_paths_rechecked': len(before), 'output_roots_absent': True,
            'boundary': 'Byte/role/static closure only. Not independent code approval, gate acceptance, build, replay or view.'}, before


def main():
    if sys.argv[1:] not in (['seal'], ['audit']) or sys.flags.optimize != 0:
        raise RuntimeError('Use seal or audit with optimization zero')
    if Path(__file__).resolve() != BASE / 'audit_preparation.py' or Path.cwd() != ROOT:
        raise RuntimeError('Unexpected preparation path or cwd')
    if dict(os.environ) != ENV or not (sys.flags.isolated == 1 and sys.flags.no_site == 1 and sys.dont_write_bytecode):
        raise RuntimeError('Require exact documentary ENV and -I -S -B')
    mode = sys.argv[1]
    if mode == 'seal':
        assert all(not (BASE / name).exists() for name in ('SHA256SUMS', 'PREPARATION_AUDIT.json', 'PREPARATION_READ_PINS.json'))
    result, before = documentary_check()
    if mode == 'seal':
        result.update(actual_argv=sys.orig_argv, actual_environment=dict(os.environ), actual_flags=str(sys.flags),
                      actual_interpreter=pin('/usr/bin/python3.10'), closed_epoch=time.time())
        save(BASE / 'PREPARATION_READ_PINS.json', before)
        save(BASE / 'PREPARATION_AUDIT.json', result)
        entries = physical_entries(BASE)
        with (BASE / 'SHA256SUMS').open('x') as stream:
            stream.write(''.join(pin(p)['sha256'] + '  ' + p.relative_to(BASE).as_posix() + '\n' for p in entries))
    else:
        saved = load(BASE / 'PREPARATION_AUDIT.json')
        assert saved['status'] == result['status'] and saved['builder_executions'] == 0
        for path, value in load(BASE / 'PREPARATION_READ_PINS.json').items():
            assert pin(path) == value
    rows = manifest(BASE)
    result = {k: result[k] for k in ('status', 'builder_executions', 'source_copy_count', 'original_copy_count',
              'old_p208_terminal_payloads_checked', 'python_sources_AST_checked', 'read_paths_rechecked', 'output_roots_absent')}
    result.update(mode=mode, complete_nonself_payloads=len(rows), manifest=pin(BASE / 'SHA256SUMS'))
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
