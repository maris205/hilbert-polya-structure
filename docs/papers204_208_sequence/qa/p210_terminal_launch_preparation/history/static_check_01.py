#!/usr/bin/env python3
"""Documentary AST/data-only audit. Never import or invoke inspected source."""
import ast
import difflib
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
HERE = QA / 'p210_terminal_launch_preparation'
OLD = QA / 'p209_terminal_preparation'
SCHEMA = QA / 'p210_terminal_build_preparation'
SOURCE = HERE / 'launch_p210_terminal.py'
KEYS, CHECKS = {}, []


def check(value, label):
    if not value:
        raise AssertionError(label)
    CHECKS.append(label)


def key(body):
    return {'sha256': hashlib.sha256(body).hexdigest(), 'bytes': len(body)}


def read(path):
    check(path.resolve() == path and path.is_file() and not path.is_symlink(), 'physical explicit input ' + str(path))
    body = path.read_bytes()
    KEYS[str(path)] = key(body)
    return body


def main():
    check(sys.argv[1:] == ['ast-data-only'], 'only documentary AST/data mode')
    check(sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode and sys.flags.optimize == 0,
          'static interpreter isolated/no-site/no-bytecode/opt0')
    old = read(OLD / 'root_launch_terminal.py').decode()
    old_readme = read(OLD / 'README.md')
    builder = read(SCHEMA / 'build_p210.py').decode()
    source = read(SOURCE).decode()
    contract = json.loads(read(HERE / 'INPUT_CONTRACT.json'))
    read(HERE / 'README.md')
    read(HERE / 'static_check.py')
    check(key(old.encode()) == {'sha256': '773ffba4850783614366732d47ae54aa9ad73c947048e6e9013ba4d0d90ec462', 'bytes': 11548},
          'exact complete original P209 launcher')
    check(key(old_readme)['sha256'] == 'ad2c66d4b9414ed001e034775a8d4700ed0548a4e2728d5a6c722aa61a9a2dd2' and
          len(old.splitlines()) == 217 and len(old_readme.splitlines()) == 156, 'complete original source/README line census')
    check(key(builder.encode()) == {'sha256': 'f71ea7d3e402e4e94bbf579d29714e2abce967ed161afb4801b898150dfc5f39', 'bytes': 31282},
          'immutable original P210 512-line unbound writer schema only')
    old_tree, tree, writer = ast.parse(old), ast.parse(source), ast.parse(builder)
    functions = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
    bindings = {t.id: n.value for n in tree.body if isinstance(n, ast.Assign) for t in n.targets if isinstance(t, ast.Name)}
    expected_env = {'PATH': '/usr/bin:/bin', 'LANG': 'C', 'LC_ALL': 'C', 'TZ': 'UTC',
                    'SOURCE_DATE_EPOCH': '1704067200', 'FORCE_SOURCE_DATE': '1', 'openin_any': 'p', 'openout_any': 'p'}
    check(ast.literal_eval(bindings['ENV']) == expected_env and len(expected_env) == 8, 'exact required ENV8')
    check(ast.literal_eval(bindings['PYTHON']) == '/usr/bin/python3.10' and
          ast.literal_eval(bindings['SEARCH_PATH']) == ['/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload'],
          'exact source-only interpreter/search path')
    check(ast.literal_eval(bindings['TIMEOUT']) == contract['timeout_seconds'] == 21600, 'bounded documented total timeout')
    stub = functions['final_builder_binding']
    check(isinstance(stub.body[-1], ast.Raise) and not any(isinstance(n, ast.Return) for n in ast.walk(stub)),
          'unconditional hard binding failure with no return')
    gate = next(n.lineno for n in ast.walk(functions['main']) if isinstance(n, ast.Call) and
                isinstance(n.func, ast.Name) and n.func.id == 'final_builder_binding')
    for n in ast.walk(functions['main']):
        if isinstance(n, ast.Call) and ((isinstance(n.func, ast.Name) and n.func.id in {'manifest', 'runtime', 'save'}) or
                                      (isinstance(n.func, ast.Attribute) and n.func.attr in {'mkdir', 'Popen'})):
            check(n.lineno > gate, 'hard gate before effect/inspection at line ' + str(n.lineno))
    calls = [n for n in ast.walk(tree) if isinstance(n, ast.Call)]
    spawns = [n for n in calls if isinstance(n.func, ast.Attribute) and n.func.attr == 'Popen']
    check(len(spawns) == 1 and any(k.arg == 'start_new_session' and ast.literal_eval(k.value) is True for k in spawns[0].keywords),
          'exactly one native spawn, owns a new builder session/group')
    check('proc.wait(timeout=TIMEOUT)' in source and "row['original_wait_exit_code'] = proc.wait(timeout=TIMEOUT)" in source,
          'original bounded native return recorded directly')
    check("row['original_wait_outcome'] = 'TIMED_OUT' if isinstance(error, subprocess.TimeoutExpired)" in source and
          "row['original_wait_exception'] = traceback.format_exc()" in source, 'original timeout/exception preserved separately')
    settle_source = ast.get_source_segment(source, functions['settle'])
    check("row['cleanup_exit_code'] = proc.wait(timeout=10)" in settle_source and
          "row['original_wait_exit_code'] =" not in settle_source and "row['original_wait_outcome'] =" not in settle_source,
          'cleanup does not overwrite original wait outcome/return')
    check('((signal.SIGINT, 30), (signal.SIGKILL, 10))' in settle_source and
          'os.killpg(proc.pid, sig)' in settle_source and 'time.monotonic() + seconds' in settle_source,
          'bounded cleanup owns builder group only')
    check('signal.signal(signal.SIGTERM, interrupted)' in source and 'signal.signal(signal.SIGHUP, interrupted)' in source,
          'TERM/HUP become recorded interruptions; SIGINT keeps normal KeyboardInterrupt')
    check('os.killpg(pid, 0)' in ast.get_source_segment(source, functions['group_absent']), 'read-only exact group-presence probes')
    main_source = ast.get_source_segment(source, functions['main'])
    early_failure = main_source[main_source.index('    if closure is None:'):main_source.index('    after, late_closed')]
    check('return 1' in early_failure and "streams_hashed=False" in early_failure and
          'SHA256SUMS' not in early_failure and 'pin(' not in early_failure, 'unclosed/abnormal path preserves raw evidence without stream hashes/seal')
    check("row['original_wait_exit_code'] == 0 and not row['cleanup_events']" in main_source and
          "row['original_wait_outcome'] == 'COMPLETED'" in main_source, 'success closure gated on original zero/no cleanup/normal wait')
    check("with (OUT / 'builder.stdout').open('xb') as stdout, (OUT / 'builder.stderr').open('xb') as stderr:" in source and
          'stdout=stdout, stderr=stderr' in source, 'independent exclusive full native builder stdout/stderr files')
    check("'outer_native_exit': None" in source and 'Root must archive the actual tool completion separately.' in source,
          'no inferred outer native exit or missing-stderr inference')
    check('manifest(BUILDER_PREP, binding[\'preparation_sha256\'], binding[\'preparation_payloads\'])' in source and
          "binding['required_input_pins'].items()" in source and "'Complete immediate preflight reread'" in source,
          'full actual builder preparation and consumed-original preflight before output')
    closure = ast.get_source_segment(source, functions['builder_closure'])
    for token in ("manifest(BUILD_OUT)", "'RESULT.json'", "len(result['commands']) == 33", "len(result['builds']) == 2",
                  "result['failures'] == []", "command['streams_settled'] is True", "'cleanup' not in command",
                  "group_absent(command['pid'])", "result['paper_completion'] is False", "'NOT_VIEWED'"):
        check(token in closure, 'required closed actual output check ' + token)
    check('PASS_P210_SOURCE_ONLY_BUILD_PAIR_NOT_VIEWED' in builder and 'PASS_P210_SOURCE_ONLY_BUILD_PAIR_NOT_VIEWED' in closure,
          'known immutable builder success token only, not future native success')
    check(not any(isinstance(n, ast.Call) and isinstance(n.func, ast.Name) and n.func.id in {'exec', 'eval', 'compile', '__import__'}
                  for n in ast.walk(tree)), 'no dynamic code execution/import shortcut')
    check({n.module for n in tree.body if isinstance(n, ast.ImportFrom)} == {'pathlib'} and
          {a.name for n in tree.body if isinstance(n, ast.Import) for a in n.names} ==
          {'hashlib', 'json', 'os', 'signal', 'subprocess', 'sys', 'time', 'traceback'}, 'stdlib-only declared imports; no old/new program imported')
    check(not any(isinstance(n.func, ast.Attribute) and n.func.attr in {'remove', 'unlink', 'rmdir', 'rename', 'replace', 'system'}
                  for n in calls), 'no deletion, replacement or shell execution surface')
    mkdirs = [ast.get_source_segment(source, n) for n in calls if isinstance(n.func, ast.Attribute) and n.func.attr == 'mkdir']
    check(mkdirs == ['OUT.mkdir(mode=0o700)'], 'one prospective outer-only mkdir; never qa_final/parent creation')
    check(contract['stage'] == 'PRELIMINARY_UNBOUND_NO_EXECUTION' and contract['final_builder_binding'] is None and
          contract['actual_launcher_executions'] == contract['actual_builder_executions'] == contract['actual_page_views'] == 0,
          'honest hard-unbound contract census')
    check(not os.path.lexists(QA / 'p210_terminal_launch_01') and
          not os.path.lexists(ROOT / 'papers/210-weakly-increasing-run-aggregation/qa_final'), 'both prospective outputs actually absent')
    old_path, new_path = str(OLD / 'root_launch_terminal.py'), str(SOURCE)
    argv = ['/usr/bin/diff', '-u', '--label', old_path, '--label', new_path, old_path, new_path]
    diff = subprocess.run(argv, cwd=ROOT, capture_output=True, check=False, timeout=30)
    expected_diff = ''.join(difflib.unified_diff(old.splitlines(keepends=True), source.splitlines(keepends=True),
                                              fromfile=old_path, tofile=new_path))
    check(diff.returncode == 1 and diff.stderr == b'' and diff.stdout.decode() == expected_diff,
          'actual separate diff streams, legitimate exit 1, full exact original-to-new diff')
    originals = {path: value for path, value in KEYS.items() if not Path(path).is_relative_to(HERE)}
    for path, expected in dict(KEYS).items():
        check(key(Path(path).read_bytes()) == expected, 'final uncached explicit input reread ' + path)
    print(json.dumps({'schema': 'p210-terminal-outer-static-v1', 'status': 'PASS_STATIC_HARD_UNBOUND_NOT_EXECUTED',
        'checks': len(CHECKS), 'check_labels': CHECKS, 'input_keys': KEYS, 'original_pins': originals,
        'original_source_lines': len(old.splitlines()), 'source_lines': len(source.splitlines()), 'source': key(source.encode()),
        'original_readme_lines': len(old_readme.splitlines()), 'source_diff': expected_diff,
        'diff_native': {'argv': argv, 'cwd': str(ROOT), 'exit_code': diff.returncode,
                        'stdout': diff.stdout.decode(), 'stderr': diff.stderr.decode()},
        'launcher_executions': 0, 'builder_executions': 0, 'receiver_executions': 0, 'scientific_runs': 0,
        'page_views': 0, 'host_inventory_collections': 0, 'host_tree_copies': 0, 'qa_final_created': False,
        'outer_output_created': False, 'root_acceptance': False, 'external': 'OWNER_AMBER / HOLD_EXTERNAL'}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
