"""Mechanical source recipe/diff refresh after the disclosed link-origin addition.

Initial draft evidence remains in its nonself-sealed subdirectory. No target
code executes; AST source extraction/compile checks only syntax and identity.
"""
import ast
from hashlib import sha256
import json
from pathlib import Path
import subprocess

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
HERE = Path(__file__).resolve().parent
OLD = ROOT / 'docs/papers204_208_sequence/qa/p209_terminal_artifact_revision_01'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}


def digest(data): return sha256(data).hexdigest()


def fn(source):
    tree = ast.parse(source)
    compile(tree, '<source-only-static>', 'exec', dont_inherit=True, optimize=0)
    return {n.name: ast.get_source_segment(source, n) for n in tree.body if isinstance(n, ast.FunctionDef)}


def dump(name, data):
    # These measured documentary products are the only replaced nonsealed
    # files; all their first-draft bytes were copied and sealed beforehand.
    (HERE / name).write_text(json.dumps(data, indent=2, sort_keys=True) + '\n')


def main():
    draft = HERE / 'unexecuted_draft_before_link_registration'
    seal = draft / 'SHA256SUMS'
    assert digest(seal.read_bytes()) == '501f7f25cd3dc6756926d73ad089a5a297eb3fe75c70c45d709e468c821bda14'
    for line in seal.read_text().splitlines():
        value, rel = line.split('  ', 1)
        assert digest((draft / rel).read_bytes()) == value
    recipes = json.loads((draft / 'SOURCE_EDITS.json').read_bytes())
    source = (HERE / 'audit_p209.py').read_text()
    begin = source.index('    # Semantic document origins are not historical input-hash aliases.')
    end = source.index("    for row in j(B / 'assignment_context/ROLES.json')", begin)
    old_line = "    for original, row in j(A / 'delta_check_02/RESPONSE_ORIGINALS_AND_COPIES.json').items(): origins[row['copy']] = Path(original)\n"
    recipes['audit_p209.py'].append({'old': old_line, 'new': source[begin:end], 'required_old_occurrences': 1})
    changes = {'audit_p209.py': {'reviews', 'revision_originals_and_failure', 'pages_and_links'},
               'record_audit.py': {'main'}, 'lifecycle_audit.py': set()}
    checks, commands, diffs = {}, [], b''
    for name, edits in recipes.items():
        original = OLD / name; copy = HERE / 'original_snapshot' / original.relative_to(ROOT)
        raw = original.read_bytes(); assert raw == copy.read_bytes()
        rebuilt = raw.decode()
        for edit in edits:
            assert rebuilt.count(edit['old']) == edit['required_old_occurrences'] == 1
            rebuilt = rebuilt.replace(edit['old'], edit['new'], 1)
        prepared = (HERE / name).read_bytes()
        assert rebuilt.encode() == prepared
        old_fn, new_fn = fn(raw.decode()), fn(prepared.decode())
        assert set(old_fn) == set(new_fn)
        changed = {k for k in old_fn if old_fn[k] != new_fn[k]}
        assert changed == changes[name]
        checks[name] = {'original_sha256': digest(raw), 'prepared_sha256': digest(prepared), 'lines': len(prepared.splitlines()),
            'function_count': len(old_fn), 'changed_functions': sorted(changed), 'literal_unchanged_functions': sorted(set(old_fn) - changed),
            'literal_function_source_comparisons': {k: {'original_sha256': digest(old_fn[k].encode()),
                'prepared_sha256': digest(new_fn[k].encode()), 'equal': old_fn[k] == new_fn[k]} for k in old_fn}}
        argv = ['/usr/bin/diff', '-u', '--', str(copy), str(HERE / name)]
        run = subprocess.run(argv, cwd=ROOT, env=ENV, capture_output=True, check=False)
        assert run.returncode == 1 and run.stdout and run.stderr == b''
        (HERE / (name + '.diff')).write_bytes(run.stdout); (HERE / (name + '.diff.stderr')).write_bytes(run.stderr)
        diffs += run.stdout
        commands.append({'argv': argv, 'cwd': str(ROOT), 'env': ENV, 'exit_code': run.returncode,
            'stdout_path': name + '.diff', 'stdout_sha256': digest(run.stdout), 'stdout_bytes': len(run.stdout),
            'stderr_path': name + '.diff.stderr', 'stderr_sha256': digest(run.stderr), 'stderr_bytes': len(run.stderr)})
    (HERE / 'ADAPTATION.diff').write_bytes(diffs)
    dump('SOURCE_EDITS.json', recipes); dump('SOURCE_FUNCTION_CHECKS.json', checks); dump('DIFF_COMMANDS.json', commands)
    argv = ['/usr/bin/diff', '-u', '--', str(draft / 'audit_p209.py'), str(HERE / 'audit_p209.py')]
    run = subprocess.run(argv, cwd=ROOT, env=ENV, capture_output=True, check=False)
    assert run.returncode == 1 and run.stdout and run.stderr == b''
    for name, raw in [('LINK_ADDITION_ONLY.diff', run.stdout), ('LINK_ADDITION_ONLY.diff.stderr', run.stderr)]:
        with (HERE / name).open('xb') as stream: stream.write(raw)
    dump('LINK_ADDITION_DIFF_COMMAND.json', {'argv': argv, 'cwd': str(ROOT), 'env': ENV, 'exit_code': run.returncode,
        'stdout_path': 'LINK_ADDITION_ONLY.diff', 'stdout_sha256': digest(run.stdout), 'stdout_bytes': len(run.stdout),
        'stderr_path': 'LINK_ADDITION_ONLY.diff.stderr', 'stderr_sha256': digest(run.stderr), 'stderr_bytes': len(run.stderr)})
    print(json.dumps({'status': 'STATIC_FULL_REPLACE_ONCE_RECIPE_AND_LITERAL_FUNCTION_CHECKS_PASS',
        'sources': {k: {'lines': v['lines'], 'sha256': v['prepared_sha256'],
            'unchanged_functions': len(v['literal_unchanged_functions']), 'changed_functions': v['changed_functions']} for k, v in checks.items()},
        'new_target_executions': 0}, sort_keys=True))


if __name__ == '__main__': main()
