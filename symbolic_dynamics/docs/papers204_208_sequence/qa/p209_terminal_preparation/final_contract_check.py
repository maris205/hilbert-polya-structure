#!/usr/bin/env python3
"""Static/documentary final check only; never import/execute a builder."""
import ast
import hashlib
import json
import os
from pathlib import Path
import subprocess
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
    assert str(path) not in READS or READS[str(path)] == value
    READS[str(path)] = value
    return value


def read(path):
    pin(path)
    return Path(path).read_bytes()


def load(path):
    return json.loads(read(path))


def write(path, data):
    with path.open('xb') as stream:
        stream.write(data)


def save(path, value):
    write(path, (json.dumps(value, indent=2, sort_keys=True) + '\n').encode())


def command(tag, a, b, label_a, label_b):
    folder = BASE / 'checks_final' / tag
    folder.mkdir(parents=True)
    argv = ['/usr/bin/diff', '-u', '--label', label_a, '--label', label_b, str(a), str(b)]
    before = {str(p): pin(p) for p in (a, b, Path('/usr/bin/diff'))}
    save(folder / 'INPUTS_BEFORE.json', before)
    row = {'argv': argv, 'cwd': str(ROOT), 'environment': ENV, 'started_epoch': time.time(),
           'exit': None, 'outcome': 'PRE_SPAWN_ATTEMPT'}
    save(folder / 'ATTEMPT.json', row)
    with (folder / 'stdout').open('xb') as out, (folder / 'stderr').open('xb') as err:
        child = subprocess.run(argv, cwd=ROOT, env=ENV, stdout=out, stderr=err, check=False)
    after = {p: pin(p) for p in before}
    save(folder / 'INPUTS_AFTER.json', after)
    row.update(exit=child.returncode, outcome='COMPLETED', ended_epoch=time.time(),
               inputs_unchanged=before == after, stdout=pin(folder / 'stdout'), stderr=pin(folder / 'stderr'))
    save(folder / 'RECEIPT.json', row)
    assert row['exit'] == 1 and before == after and row['stderr']['bytes'] == 0
    return read(folder / 'stdout')


def assignments(tree):
    result = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            try:
                result[node.targets[0].id] = ast.literal_eval(node.value)
            except (ValueError, TypeError):
                pass
    return result


def function_delta(a, b):
    old, new = read(a).decode(), read(b).decode()
    oa, ob = ast.parse(old), ast.parse(new)
    fa = {n.name: n for n in oa.body if isinstance(n, ast.FunctionDef)}
    fb = {n.name: n for n in ob.body if isinstance(n, ast.FunctionDef)}
    changed = sorted(n for n in fa.keys() & fb.keys() if ast.dump(fa[n]) != ast.dump(fb[n]))
    unchanged = sorted(n for n in fa.keys() & fb.keys() if n not in changed)
    for name in unchanged:
        x, y = fa[name], fb[name]
        assert old.splitlines(keepends=True)[x.lineno-1:x.end_lineno] == new.splitlines(keepends=True)[y.lineno-1:y.end_lineno]
    return {'original': str(a), 'adapted': str(b), 'changed_functions': changed,
            'unchanged_source_blocks': unchanged, 'added_functions': sorted(fb.keys() - fa.keys()),
            'removed_functions': sorted(fa.keys() - fb.keys()), 'lines': len(new.splitlines())}


assert sys.argv[1:] == [] and Path.cwd() == ROOT and Path(__file__).resolve().parent == BASE
assert dict(os.environ) == ENV and sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and sys.flags.optimize == 0
revision = load(BASE / 'DRAFT_REVISION.json')
aliases = {(r['original_path'], r['sha256']): r for r in revision['historical_input_aliases']}
for row in aliases.values():
    assert pin(BASE / row['physical_path'])['sha256'] == row['sha256']
    assert pin(row['original_path'])['sha256'] == row['final_sha256']
old_commands = []
for folder in sorted((BASE / 'checks').iterdir()):
    command_row = load(folder / 'RECEIPT.json')
    before, after = load(folder / 'INPUTS_BEFORE.json'), load(folder / 'INPUTS_AFTER.json')
    assert before == after and command_row['inputs_unchanged']
    used_aliases = []
    for path, value in before.items():
        current = pin(path)
        if current != value:
            row = aliases[(path, value['sha256'])]
            historical = pin(BASE / row['physical_path'])
            assert all(historical[k] == value[k] for k in ('sha256', 'bytes', 'symlink'))
            assert value['resolved'] == path
            used_aliases.append(row['physical_path'])
    assert command_row['stdout'] == pin(folder / 'stdout') and command_row['stderr'] == pin(folder / 'stderr')
    assert command_row['exit'] == (1 if folder.name.startswith('diff_') else 0)
    assert command_row['stderr']['bytes'] == 0
    old_commands.append({'tag': folder.name, 'exit': command_row['exit'], 'exact_historical_source_aliases': used_aliases})
assert len(old_commands) == 21
whole = []
incremental = []
for old, new in (('p208_terminal_v2.py', 'root_terminal_builds.py'), ('p209_b_launch_review.py', 'root_launch_terminal.py')):
    whole.append(command('whole_' + new.replace('.', '_'), BASE / 'original_snapshot' / old,
                         BASE / new, 'original_snapshot/' + old, new))
    incremental.append(command('draft_delta_' + new.replace('.', '_'), BASE / 'history/draft_01' / new,
                               BASE / new, 'history/draft_01/' + new, new))
write(BASE / 'ADAPTATION_FINAL.diff', b''.join(whole))
write(BASE / 'DRAFT_TO_FINAL.diff', b''.join(incremental))
builder = ast.parse(read(BASE / 'root_terminal_builds.py').decode())
launcher = ast.parse(read(BASE / 'root_launch_terminal.py').decode())
ba, la = assignments(builder), assignments(launcher)
sources = load(BASE / 'SOURCE_PINS.json')
assert set(ba['SOURCE_NAMES']) == set(sources) and len(sources) == 8
assert ba['ENV'] == la['ENV'] == {**ENV, 'SOURCE_DATE_EPOCH': '1788652800', 'FORCE_SOURCE_DATE': '1', 'openin_any': 'p', 'openout_any': 'p'}
assert ba['EXPECTED_SOURCE_PINS'] == la['EXPECTED_SOURCE_PINS'] == pin(BASE / 'SOURCE_PINS.json')['sha256']
for n, value in sources.items():
    for base in (PAPER, PAPER / 'frozen_round1', BASE / 'source_snapshot'):
        assert all(pin(base / n)[k] == value[k] for k in ('sha256', 'bytes'))
for name, row in load(BASE / 'ORIGINAL_INPUTS.json').items():
    assert {k: row[k] for k in ('sha256', 'bytes', 'resolved', 'symlink')} == pin(row['original_path'])
    assert read(row['original_path']) == read(BASE / 'original_snapshot' / name)
for tree in (builder, launcher):
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            assert node.func.id not in {'eval', 'exec', 'compile', '__import__'}
    imports = [n for n in tree.body if isinstance(n, (ast.Import, ast.ImportFrom))]
    assert all(not isinstance(n, ast.ImportFrom) or n.level == 0 for n in imports)
main = next(n for n in builder.body if isinstance(n, ast.FunctionDef) and n.name == 'main')
assert isinstance(main.body[0], ast.If) and 'sys.flags.optimize' in ast.unparse(main.body[0])
science_index = next(i for i, n in enumerate(main.body) if isinstance(n, ast.Assign) and isinstance(n.value, ast.Call) and isinstance(n.value.func, ast.Name) and n.value.func.id == 'science')
mkdir_index = next(i for i, n in enumerate(main.body) if isinstance(n, ast.Expr) and isinstance(n.value, ast.Call) and isinstance(n.value.func, ast.Attribute) and n.value.func.attr == 'mkdir')
assert science_index < mkdir_index and all(isinstance(n, ast.If) for n in main.body[:science_index])
text = read(BASE / 'root_terminal_builds.py').decode()
assert "objects = sorted(p for p in candidates if is_elf(p))" in text
assert "Path(p).is_relative_to(STDLIB)" in text
assert "'actual_page_mismatch', pages_n" in text and text.index("'_MEASURED_PDF.json'") < text.index("'actual_page_mismatch'")
assert 'UNREAPED_CHILDREN' in text and "'UNCLOSED_BUILD_NO_SEAL'" in text
assert "'PENDING_NOT_INFERRED_FROM_HASH_OR_RENDER'" in text
libc = Path('/usr/lib/x86_64-linux-gnu/libc.so')
assert pin(libc)['sha256'] == revision['non_elf_observation']['sha256']
assert read(libc).startswith(b'/* GNU ld script') and not read(libc).startswith(b'\x7fELF')
functions = [function_delta(BASE / 'original_snapshot' / old, BASE / new) for old, new in
             (('p208_terminal_v2.py', 'root_terminal_builds.py'), ('p209_b_launch_review.py', 'root_launch_terminal.py'))]
expected_labels = ['ldd_before', 'pdflatex_version', 'bibtex_version', 'texmf_roots']
for k in (1, 2):
    label = 'cold_build_' + str(k)
    expected_labels.extend(label + '_' + v for v in ba['USER_TEX_VARS'])
    expected_labels.extend(label + '_' + v for v in ('tex1', 'bst', 'bibtex', 'tex2', 'tex3', 'pdfinfo', 'pdffonts', 'pdftotext', 'render', 'frozen_pdf_cmp'))
expected_labels.extend(['pair_pdf_cmp', 'ldd_after'])
assert len(expected_labels) == 32 and len(set(expected_labels)) == 32
for path in (PAPER / 'qa_final', ROOT / 'docs/papers204_208_sequence/qa/root_replays/p209_terminal_strict'):
    assert not path.exists() and not path.is_symlink()
assert not any(p.suffix in {'.pyc', '.pyo'} or p.name == '__pycache__' for p in BASE.rglob('*'))
before = dict(READS)
assert before == {p: pin(p) for p in before}
save(BASE / 'CONTRACT_READ_PINS.json', before)
result = {'status': 'PASS_FINAL_STATIC_PREPARATION_ONLY', 'builder_executions': 0,
          'future_gate_values_supplied': False, 'output_roots_absent': True,
          'original_documentary_commands_preserved': old_commands, 'new_actual_diff_commands': 4,
          'whole_final_diff_bytes': sum(map(len, whole)), 'draft_to_final_diff_bytes': sum(map(len, incremental)),
          'function_checks': functions, 'exact_source_names': list(ba['SOURCE_NAMES']),
          'expected_command_labels_if_executed': expected_labels, 'read_paths_rechecked': len(before),
          'scope': 'AST/source inspection, exact draft alias closure, actual full diffs and current byte pins only; not a guard execution, build, replay, review or view.'}
save(BASE / 'FINAL_STATIC_CHECK.json', result)
print(json.dumps({k: result[k] for k in ('status', 'builder_executions', 'future_gate_values_supplied', 'output_roots_absent', 'new_actual_diff_commands', 'whole_final_diff_bytes', 'draft_to_final_diff_bytes', 'function_checks', 'read_paths_rechecked')}, sort_keys=True))
