#!/usr/bin/env python3
"""Static preparation only. Never import or execute receive.py or originals.

Check receiver AST and sealed original data schemas, not current3276 resource
keys/discovery or the child's136582-path audit. Runtime reception is root-owned.
"""
import ast
import gzip
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import sys
import traceback

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
HERE = QA / 'p208_p209_reuse_root_preparation'
OUT = QA / 'p208_p209_reuse_02'
CHECKER = QA / 'p208_p209_reuse_revision_01'
LAUNCHER = QA / 'p208_p209_reuse_launcher_revision_01'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
CHECKS = 0
PINS = {}


def check(ok, message):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(message)


def read(path):
    path = Path(path)
    check(path.is_file() and path.is_absolute() and path.resolve() == path and not path.is_symlink() and
          (path.is_relative_to(ROOT) or path == Path('/usr/bin/python3.10')), 'bounded exact static input')
    data = path.read_bytes()
    row = {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}
    check(str(path) not in PINS or PINS[str(path)] == row, 'unchanged repeated bounded input')
    PINS[str(path)] = row
    return data


def obj(path):
    return json.loads(read(path))


def package(base, count, expected):
    check(sha256(read(base / 'SHA256SUMS')).hexdigest() == expected, 'exact original package seal')
    rows = {}
    for line in read(base / 'SHA256SUMS').decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        check(match is not None, 'strict original manifest row')
        value, name = match.groups()
        check(Path(name).as_posix() == name and not Path(name).is_absolute() and '..' not in Path(name).parts and
              name not in rows and name != 'SHA256SUMS', 'exact nonself contained original member')
        check(sha256(read(base / name)).hexdigest() == value, 'actual small original package bytes')
        rows[name] = value
    entries = list(base.rglob('*'))
    check(all(not path.is_symlink() for path in entries) and len(rows) == count and
          {path.relative_to(base).as_posix() for path in entries if path.is_file()} == set(rows) | {'SHA256SUMS'}, 'complete actual bounded original membership')


def main():
    check(set(os.environ) == set(ENV) and all(os.environ[k] == v for k, v in ENV.items()), 'exact safe static ENV4')
    check(Path.cwd() == ROOT and Path(sys.executable).resolve() == Path('/usr/bin/python3.10') and
          sys.flags.isolated and sys.flags.no_site and sys.flags.dont_write_bytecode and sys.flags.optimize == 0, 'source-only fixed static interpreter')
    source = read(HERE / 'receive.py').decode()
    tree = ast.parse(source, filename=str(HERE / 'receive.py'))
    imports = set()
    calls = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.update(alias.name for alias in node.names)
        if isinstance(node, ast.ImportFrom):
            imports.add(node.module)
        if isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                check(node.func.id not in {'eval', 'exec', 'compile', '__import__'}, 'no dynamic executable evaluation')
            if isinstance(node.func, ast.Attribute):
                check(node.func.attr not in {'write', 'write_bytes', 'write_text', 'mkdir', 'unlink', 'rmdir', 'rename', 'replace',
                    'Popen', 'run', 'system', 'fork', 'kill', 'killpg', 'sleep'}, 'no file/process mutations or launches')
                if node.func.attr == 'open':
                    calls.append(ast.unparse(node))
                    check(len(node.args) == 1 and isinstance(node.args[0], ast.Constant) and node.args[0].value == 'rb', 'only explicit read-binary open')
    check(imports == {'gzip', 'hashlib', 'json', 'os', 'pathlib', 're', 'sys', 'sysconfig', 'traceback'}, 'stdlib-only receiver, no original imports')
    check(calls == ["path.open('rb')"], 'one read-only stream-opening call site')
    for snippet in ['set(os.environ) == set(ENV)', 'before, after = ledger(', 'before == after', 'configuration() == config',
        'runtime_names(config) == runtime', 'need(measure(name) == value', "package(OUT, OUTPUT_SEAL, 20)",
        "package(CHECKER_PREP, CHECKER_SEAL, 7)", "package(LAUNCHER_PREP, LAUNCHER_SEAL, 5)",
        "child['current_paths_reread'] == 136582", "len(inventory) == 34", "len(declarations) == 6",
        "new_scientific_executions': 0", "new_builds': 0", "new_page_views': 0"]:
        check(snippet in source, 'explicit reception/scope guard present: ' + snippet)
    refs = next(node for node in tree.body if isinstance(node, ast.FunctionDef) and node.name == 'aliases_and_child')
    check(not any(isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id in {'ledger', 'configuration', 'runtime_names'}
                  for node in ast.walk(refs)), 'child output-role handler does not re-expand child resource ledgers')
    direct = obj(HERE / 'INPUT_PINS.json')
    check(len(direct['pins']) == 16, 'sixteen exact direct pins')
    for name, value in direct['pins'].items():
        check(sha256(read(Path(name))).hexdigest() == value, 'exact actual direct pinned input')
    for base, count in [(OUT, 20), (CHECKER, 7), (LAUNCHER, 5), (QA / 'p208_p209_reuse_01', 20),
                        (QA / 'p208_p209_reuse_preparation', 5), (QA / 'p208_p209_reuse_launcher_preparation', 4)]:
        package(base, count, direct['pins'][str(base / 'SHA256SUMS')])
    parent = obj(OUT / 'RECEIPT.json')
    child = obj(OUT / 'checker.stdout')
    check(parent['native'] == obj(OUT / 'NATIVE_RESULT.json') and parent['native']['exit'] == 0 and
          parent['native']['process_group_settled'] is True and parent['failures'] == [], 'actual original native receipt schema')
    check(child['checks'] == 3988646 and child['current_paths_reread'] == 136582 and len(child['original_ledger_references']) == 40,
          'actual child counts and40 reference roles, not new static tests')
    for name in ('checker.stdout', 'checker.stderr'):
        data = read(OUT / name)
        check(parent['streams'][name]['sha256'] == sha256(data).hexdigest() and parent['streams'][name]['bytes'] == len(data), 'actual complete raw stream hashes')
    known = []
    for phase in ('BEFORE', 'AFTER'):
        path = OUT / ('KNOWN_INPUTS_' + phase + '.json.gz')
        data = read(path)
        meta = obj(OUT / ('KNOWN_INPUTS_' + phase + '.meta.json'))
        decoded = gzip.decompress(data)
        value = json.loads(decoded)
        check(meta['compressed']['sha256'] == sha256(data).hexdigest() and meta['compressed']['bytes'] == len(data) and
              meta['json'] == {'bytes': len(decoded), 'sha256': sha256(decoded).hexdigest()} and len(value) == meta['entries'] == 3276,
              'original lossless3276-key ledger schema only; no current resource reads')
        check(all(set(row) == {'sha256', 'bytes', 'resolved', 'symlink'} for row in value.values()), 'all recorded original key field sets')
        known.append(value)
    check(known[0] == known[1], 'original3276 before-after records equal')
    check(obj(OUT / 'CONFIGURATION_BEFORE.json') == obj(OUT / 'CONFIGURATION_AFTER.json'), 'original configuration interval')
    check(obj(OUT / 'SCOPED_INPUTS_BEFORE.json') == obj(OUT / 'SCOPED_INPUTS_AFTER.json'), 'original scoped interval')
    contract, declarations = obj(CHECKER / 'INPUT_PINS.json'), obj(CHECKER / 'ALIASES.json')
    check(len(contract['fixed_inputs']) == 128 and len(declarations) == 6 and child['documentary_aliases_used'] ==
          {row['original'] + ' @ ' + row['sha256']: {'case': row['cases'][0], 'physical': row['physical']} for row in declarations}, 'exact128/six output roles')
    failure_pins = obj(CHECKER / 'FAILURE_PINS.json')
    check(len(failure_pins) == 34, 'all34 failed originals declared')
    for name, value in failure_pins.items():
        read(name)
        check(PINS[name] == value, 'exact physical failed-attempt bytes preserved')
    for left, right in [(OUT / 'executed_inspect.py', CHECKER / 'inspect.py'), (OUT / 'executed_launcher.py', LAUNCHER / 'launcher.py')]:
        check(read(left) == read(right), 'full actual executed-source bytes bind revised source')
    completion = obj(QA / 'P208_P209_REUSE02_ROOT_COMPLETION.actual.json')
    launch = obj(QA / 'P208_P209_REUSE02_ROOT_LAUNCH.actual.json')
    check(completion['session_id'] == launch['result']['session_id'] == 68034 and completion['result']['exit_code'] == 0 and
          json.loads(completion['result']['output'])['output_seal']['manifest']['sha256'] == direct['pins'][str(OUT / 'SHA256SUMS')], 'actual root outer native session/seal binding')
    before = dict(PINS)
    for name, value in before.items():
        read(name)
        check(PINS[name] == value, 'all static-consumed actual input bytes reread unchanged')
    print(json.dumps({'status': 'PASS_STATIC_RECEIVER_AST_AND_BOUNDED_ORIGINAL_SCHEMAS_ONLY', 'checks': CHECKS,
        'receiver_source_sha256': sha256(source.encode()).hexdigest(), 'receiver_lines': len(source.splitlines()),
        'static_checker_sha256': sha256(read(Path(__file__).resolve())).hexdigest(), 'actual_static_read_paths': len(before),
        'actual_static_input_key_sha256': sha256((json.dumps(before, sort_keys=True, separators=(',', ':')) + '\n').encode()).hexdigest(),
        'direct_pins': 16, 'actual_small_package_payload_counts': [20, 7, 5, 20, 5, 4],
        'original_parent_ledger_schema_entries': 3276, 'current_parent_resource_key_rereads': 0,
        'original_child_audit_reexpanded': False, 'receiver_or_original_program_imports_or_executions': 0,
        'science_build_view_executions': 0, 'root_receiver_runtime_acceptance': 'NOT_RUN',
        'scope': 'Only AST/static schemas and bounded original package bytes. Current runtime/configuration discovery and3276 current resource reads are left to actual root receiver execution.',
        'env': ENV, 'cwd': str(ROOT), 'orig_argv': sys.orig_argv}, sort_keys=True, indent=2))


if __name__ == '__main__':
    try:
        main()
    except Exception:
        print(json.dumps({'status': 'FAIL_STATIC_PREPARATION_NOT_RECEIVER_EXECUTION', 'checks_before_failure': CHECKS,
                          'traceback': traceback.format_exc()}, sort_keys=True, indent=2))
        raise SystemExit(1)
