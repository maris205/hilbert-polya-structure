"""Documentary/static checks only; never imports or invokes the freezer."""
import ast
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import time

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BATCH = ROOT / 'docs/papers204_208_sequence'
PAPER = ROOT / 'papers/209-ordered-fibre-threading'
HERE = BATCH / 'qa/p209_round2_preparation'
R1 = PAPER / 'frozen_round1'
TARGET = PAPER / 'frozen_round2'
REVIEW = BATCH / 'reviews/p209_b'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
READS = {}
COMMANDS = []


def pin(path):
    path = Path(path)
    assert path.is_file() and not path.is_symlink(), str(path)
    value = sha256(path.read_bytes()).hexdigest()
    assert str(path) not in READS or READS[str(path)] == value
    READS[str(path)] = value
    return value


def js(path):
    pin(path)
    return json.loads(path.read_bytes())


def rows(path):
    pin(path)
    result = {}
    for line in path.read_text().splitlines():
        value, name = line.split('  ', 1)
        rel = Path(name)
        assert re.fullmatch('[0-9a-f]{64}', value) and name not in result
        assert not rel.is_absolute() and rel.as_posix() == name and '..' not in rel.parts and '.' not in rel.parts
        result[name] = value
    return result


def manifest(base, name='SHA256SUMS', complete=True):
    result = rows(base / name)
    assert name not in result
    for rel, value in result.items():
        assert pin(base / rel) == value, rel
    if complete:
        tree = list(base.rglob('*'))
        assert all(not item.is_symlink() for item in tree)
        assert {item.relative_to(base).as_posix() for item in tree if item.is_file()} == set(result) | {name}
    return result


def command(argv, expected):
    inputs = {path: pin(Path(path)) for path in argv[2:]}
    row = {'argv': argv, 'cwd': str(ROOT), 'environment': ENV,
           'started_epoch': time.time(), 'exit': None, 'outcome': 'PRE_SPAWN_ATTEMPT',
           'stdout': None, 'stderr': None, 'inputs_before': inputs}
    COMMANDS.append(row)
    process = subprocess.run(argv, cwd=ROOT, env=ENV, capture_output=True, check=False)
    row.update(exit=process.returncode, outcome='COMPLETED',
               stdout=process.stdout.decode(), stderr=process.stderr.decode(),
               inputs_after={path: pin(Path(path)) for path in inputs})
    assert row['inputs_before'] == row['inputs_after'] and process.returncode == expected
    assert process.stderr == b''
    return row


def main():
    assert sys.argv[1:] == ['static-only']
    assert dict(os.environ) == ENV and Path.cwd() == ROOT
    assert sys.flags.isolated == 1 and sys.flags.no_site == 1 and sys.flags.optimize == 0 and sys.dont_write_bytecode
    assert not TARGET.exists() and not TARGET.is_symlink()
    pin(Path('/usr/bin/python3.10'))
    pin(Path('/usr/bin/cmp'))
    pin(Path('/usr/bin/diff'))
    source = HERE / 'freeze_p209_round2.py'
    source_hash = pin(source)
    text = source.read_text()
    tree = ast.parse(text, filename=str(source))
    functions = {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}
    imports = sorted({node.module if isinstance(node, ast.ImportFrom) else alias.name
                      for node in ast.walk(tree) if isinstance(node, (ast.Import, ast.ImportFrom))
                      for alias in node.names})
    assert imports == ['hashlib', 'json', 'os', 'pathlib', 're', 'shutil', 'subprocess', 'sys', 'time', 'traceback', 'urllib.parse']
    calls = [ast.unparse(node.func) for node in ast.walk(tree) if isinstance(node, ast.Call)]
    assert not any(name in calls for name in ('exec', 'eval', '__import__', 'compile', 'shutil.copytree', 'os.system', 'subprocess.Popen'))
    assert calls.count('subprocess.run') == 1
    assert "argv = ['/usr/bin/cmp', '--', str(a), str(b)]" in text
    main_source = ast.get_source_segment(text, functions['main'])
    target_creation = main_source.index('TARGET.mkdir()')
    for required in ('complete_manifest(PREPARATION)', 'core_inputs()', 'accepted_b(core)',
                     'historical_resolution(core, accepted, initial_rows)', 'link_mapping(core, prior, history)'):
        assert main_source.index(required) < target_creation, required
    for required in (
        "['freeze-round2-after-accepted-b']", "sys.flags.optimize == 0", "sys.flags.no_site == 1",
        "dict(os.environ) == ENV", "not TARGET.exists() and not TARGET.is_symlink()",
        "shutil.copyfile(ROUND1 / name, destination)", "'ROUND2_FREEZE_ADAPTER.py'",
        "'ROUND2_PROVENANCE.json'", "len(expected) == 2020 + len(copies)",
        "if p.is_file() and not p.is_relative_to(TARGET)} == preexisting",
        "complete_current_paper_after_round2': False", "'original_referent_base': str(PAPER)",
        "initial_rows['DELTA.md'] == digest(REVIEW / 'INITIAL_DELTA.md')",
        "current['delta_status'] == 'ACCEPTED_EXACT_NOCHANGE_DELTA'",
        "key = (row['original_path'], row['sha256'])",
        "assert used == set(supplied)"):
        assert required in text, required
    assert "current['phase']" not in text and "current['verdict']" not in text
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == 'open':
            assert len(node.args) == 1 and isinstance(node.args[0], ast.Constant) and node.args[0].value == 'x'
    original = BATCH / 'qa/p209_round1_preparation_v2'
    assert pin(original / 'SHA256SUMS') == 'baf747d531a06c76dfcff7a086819df0fc4668549f70c20894b9783750a9e0f7'
    assert len(manifest(original)) == 9
    bprep = BATCH / 'qa/p209_b_root_preparation'
    assert pin(bprep / 'SHA256SUMS') == '4beef4a4e9f60c6039ceb89df1f3a12b2d61049ad75654e35825390c4b68133a'
    assert len(manifest(bprep)) == 57
    originals = [(original / 'freeze_p209_round1.py', 'freeze_p209_round1_v2.py'),
                 (original / 'README.md', 'ROUND1_PREPARATION_README.md'),
                 (BATCH / 'qa/P209_ROUND1_ROOT_INSPECTION.md', 'P209_ROUND1_ROOT_INSPECTION.md'),
                 (bprep / 'root_record_pair.py', 'root_record_pair.py'),
                 (bprep / 'root_launch_pair.py', 'root_launch_pair.py'),
                 (bprep / 'README.md', 'B_ROOT_PREPARATION_README.md')]
    for origin, name in originals:
        command(['/usr/bin/cmp', '--', str(origin), str(HERE / 'original_snapshot' / name)], 0)
    command(['/usr/bin/cmp', '--', str(R1 / 'ROUND1_FREEZE_ADAPTER.py'),
             str(HERE / 'original_snapshot/freeze_p209_round1_v2.py')], 0)
    difference = command(['/usr/bin/diff', '-u', str(HERE / 'original_snapshot/freeze_p209_round1_v2.py'), str(source)], 1)
    assert difference['stdout']
    assert pin(R1 / 'SHA256SUMS') == 'c93e16cf20d2eb87f3b454fbdb3576e52c6c79fb74c8712a277efeab7e60ce57'
    core = manifest(R1)
    assert len(core) == 2003
    assert pin(PAPER / 'PAPER_MANIFEST.sha256') == '3e94a72637733ca46f7950f4feb8508fdf14b5ff6386c971821932ae9231e5a9'
    whole = manifest(PAPER, 'PAPER_MANIFEST.sha256')
    assert len(whole) == 5982
    author = manifest(PAPER, 'AUTHOR_MANIFEST.sha256', False)
    assert len(author) == 1985 and all(core[name] == value for name, value in author.items())
    assert pin(PAPER / 'SHA256SUMS') == pin(PAPER / 'AUTHOR_MANIFEST.sha256') == '9fd20cd746f1ae03c22a87283313248ad79ffcfb9a0f1ea45458937dd5901a0e'
    prior = js(R1 / 'ROUND1_PROVENANCE.json')
    history_aliases = {}
    for row in prior['anchor_mapping'].values():
        history_aliases[(row['original_path'], row['sha256'])] = R1 / row['physical_path']
    for row in prior['historical_external_resolution'].values():
        history_aliases[(row['original_path'], row['sha256'])] = Path(row['round1_physical_path'])
    lifecycle = BATCH / 'qa/central_lifecycle_p209_round1'
    manifest(lifecycle)
    for row in js(lifecycle / 'CAPTURE.actual.json')['copies']:
        history_aliases[(row['original_path'], row['sha256'])] = Path(row['physical_path'])
    historical_drift = []
    for origin, value in prior['all_source_inputs_before_and_rechecked_after'].items():
        now = pin(Path(origin))
        if now != value:
            alias = history_aliases[(origin, value)]
            assert pin(alias) == value
            historical_drift.append({'original_path': origin, 'sha256': value,
                                     'physical_path': str(alias), 'current_original_sha256': now})
    initial_seal = 'd88b831e60414d47ae0b2afb2583b73d02fc9764877a00952f4a9d90d13488ea'
    if pin(REVIEW / 'SHA256SUMS') == initial_seal:
        assert len(manifest(REVIEW)) == 1298
        initial_source = REVIEW / 'SHA256SUMS'
    else:
        initial_source = REVIEW / 'INITIAL_REVIEW_SEAL.sha256'
        assert pin(initial_source) == initial_seal
        initial_rows = rows(initial_source)
        assert len(initial_rows) == 1298
        for name, value in initial_rows.items():
            assert pin(REVIEW / ('INITIAL_DELTA.md' if name == 'DELTA.md' else name)) == value
        manifest(REVIEW)
    anchors_node = next(node for node in tree.body if isinstance(node, ast.Assign)
                        and any(isinstance(target, ast.Name) and target.id == 'ANCHORS' for target in node.targets))
    anchors = [key.value for key in anchors_node.value.keys]
    assert len(anchors) == len(set(anchors)) == 15
    before = dict(READS)
    assert all(pin(Path(path)) == value for path, value in before.items())
    assert pin(source) == source_hash and not TARGET.exists()
    print(json.dumps({'status': 'PASS_STATIC_PREPARATION_ONLY',
        'boundary': 'No freezer import/invocation/refusal test, mathematical execution, build, view, acceptance or external action.',
        'source_sha256': source_hash, 'source_lines': len(text.splitlines()),
        'imports': imports, 'complete_original_preparation_payloads': 9,
        'complete_B_root_preparation_payloads': 57,
        'round1_payloads': 2003, 'author_payloads': 1985, 'prior_whole_payloads': 5982,
        'round2_fixed_anchor_names': anchors,
        'initial_B_seal_reference': str(initial_source), 'initial_B_seal_sha256': initial_seal,
        'round1_prior_read_pins_documentarily_checked': len(prior['all_source_inputs_before_and_rechecked_after']),
        'historical_drift_exact_physical_aliases': historical_drift,
        'target_absent': True, 'actual_commands': COMMANDS,
        'before_and_after_input_map_sha256': sha256(json.dumps(before, sort_keys=True).encode()).hexdigest(),
        'input_map_storage': 'Digest and count only; exact compared-source pins remain in command rows and package referents remain in the named complete manifests. This is not a full standalone input capsule.',
        'rechecked_input_paths': len(before),
        'launch_argv': sys.argv, 'launch_orig_argv': sys.orig_argv,
        'cwd': str(ROOT), 'environment': ENV}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
