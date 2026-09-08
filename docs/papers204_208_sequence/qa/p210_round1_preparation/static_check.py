#!/usr/bin/env python3
"""Read-only preparation audit. Parse freezer AST; NEVER import/execute it.

This performs its own bounded file/manifest/link checks. It does not execute
freezer main or a refusal path, create Round1, launch another program, run
science/build/view, or materialize a broad inventory. Output is only stdout.
"""
import ast
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import sys
import traceback
from urllib.parse import unquote

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
HERE = ROOT / 'docs/papers204_208_sequence/qa/p210_round1_preparation'
CHECKS = 0
PINS = {}
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}


def check(ok, message):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(message)


def read(path):
    path = Path(path)
    check(path.is_absolute() and path.resolve() == path and not path.is_symlink() and path.is_file(), 'exact input: ' + str(path))
    check(path.is_relative_to(ROOT) or path == Path('/usr/bin/python3.10'), 'bounded declared filesystem scope')
    data = path.read_bytes()
    row = {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}
    key = str(path)
    check(key not in PINS or PINS[key] == row, 'unchanged repeated input: ' + key)
    PINS[key] = row
    return data


def digest(path):
    return sha256(read(path)).hexdigest()


def parse(path):
    return json.loads(read(path))


def rows(path):
    data = read(path)
    check(data.endswith(b'\n'), 'complete newline in manifest')
    result = {}
    for line in data.decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        check(match is not None, 'strict two-space manifest row')
        value, name = match.groups()
        relative = Path(name)
        check(relative.as_posix() == name and not relative.is_absolute() and '..' not in relative.parts and name not in result, 'unique contained manifest name')
        result[name] = value
    return result


def members(base):
    paths = list(base.rglob('*'))
    check(all(not path.is_symlink() for path in paths), 'bounded package has no symlinks')
    return {path.relative_to(base).as_posix() for path in paths if path.is_file()}


def manifest(base, name='SHA256SUMS', complete=True):
    result = rows(base / name)
    for relative, value in result.items():
        check(digest(base / relative) == value, 'manifest bytes: ' + str(base / relative))
    if complete:
        check(name not in result and members(base) == set(result) | {name}, 'exact nonself manifest membership')
    return result


def atom(node, constants):
    # A deliberately small data-expression decoder, not eval/compile/import.
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Name) and node.id in constants:
        return constants[node.id]
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
        return atom(node.left, constants) / atom(node.right, constants)
    if isinstance(node, ast.Dict):
        return {atom(k, constants): atom(v, constants) for k, v in zip(node.keys, node.values)}
    if isinstance(node, (ast.List, ast.Tuple)):
        return [atom(item, constants) for item in node.elts]
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
        if node.func.id == 'Path' and len(node.args) == 1 and not node.keywords:
            return Path(atom(node.args[0], constants))
        if node.func.id == 'dict' and not node.args and all(item.arg is not None for item in node.keywords):
            return {item.arg: atom(item.value, constants) for item in node.keywords}
    raise AssertionError('nondata AST expression: ' + ast.dump(node))


def source_audit(source, contract):
    tree = ast.parse(source, filename=str(HERE / 'freeze_p210_round1.py'))
    constants = {}
    for statement in tree.body:
        if isinstance(statement, ast.Assign) and len(statement.targets) == 1 and isinstance(statement.targets[0], ast.Name):
            constants[statement.targets[0].id] = atom(statement.value, constants)
    functions = {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}
    check(constants['ROOT'] == ROOT and constants['PREPARATION'] == HERE and constants['TARGET'] ==
          ROOT / 'papers/210-weakly-increasing-run-aggregation/frozen_round1', 'fixed exact target/source/workspace')
    check(constants['ENV'] == ENV and len(constants['ANCHORS']) == 13, 'four safe env values and 13 explicit anchors')
    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.update(alias.name for alias in node.names)
        if isinstance(node, ast.ImportFrom):
            imports.add(node.module)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            check(node.func.id not in {'eval', 'exec', 'compile', '__import__'}, 'no executable dynamic source evaluation')
    check(imports == {'hashlib', 'json', 'os', 'pathlib', 're', 'shutil', 'sys', 'traceback', 'urllib.parse'}, 'only declared standard imports; no subprocess or originals')
    req = next(node.value for node in ast.walk(functions['root_acceptance']) if isinstance(node, ast.Assign) and
               any(isinstance(target, ast.Name) and target.id == 'required' for target in node.targets))
    required = atom(req, constants)
    required.update({key: True for key in ('reviewer_delta_accepted', 'root_original_inspection_complete', 'root_replay_closure_complete')})
    check(required == contract['required_fields'], 'independent JSON contract matches freezer required data fields')
    main = functions['main']
    mutate = [node for node in ast.walk(main) if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and
              node.func.attr == 'mkdir']
    check(len(mutate) == 1 and ast.unparse(mutate[0]) == 'TARGET.mkdir()', 'one first target creation only')
    first = mutate[0].lineno
    for name in ('root_acceptance', 'complete_manifest', 'core_inputs', 'accepted_a', 'links'):
        check(any(isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == name and node.lineno < first
                  for node in ast.walk(main)), 'prerequisite before mkdir: ' + name)
    for snippet in ["require(not TARGET.exists() and not TARGET.is_symlink()", "accepted = root_acceptance(sys.argv[3])",
                    "direct['expected_root_closure_sha256'] == sys.argv[3]", "before = dict(READ_PINS)"]:
        check(source.index(snippet) < source.index('        TARGET.mkdir()'), 'explicit precreation source guard: ' + snippet)
    writer = ast.get_source_segment(source, functions['write_new'])
    for snippet in ["path.is_relative_to(TARGET)", "path.resolve() == path", "not path.is_symlink()", "path.open('xb')"]:
        check(snippet in writer, 'exclusive contained writer guard: ' + snippet)
    mutation_calls = []
    for name, function in functions.items():
        for node in ast.walk(function):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                attr = node.func.attr
                if attr in {'mkdir', 'open', 'write', 'write_bytes', 'write_text', 'unlink', 'rmdir', 'rename', 'replace'}:
                    mutation_calls.append((name, ast.unparse(node)))
                    check((name == 'write_new' and attr in {'mkdir', 'open', 'write'}) or
                          (name == 'main' and ast.unparse(node) == 'TARGET.mkdir()'), 'all mutations restricted to exact new target writer')
    check(len(mutation_calls) == 4, 'exact four syntactic filesystem-write call sites')
    for snippet in ['a == b', 'for path, value in before.items():', "len(expected) == 508", 'complete_manifest(TARGET) == expected',
                    "not (TARGET / 'SHA256SUMS').exists()", 'no_rollback_or_retry=True', 'round0_external_aliases=[]']:
        check(snippet in source, 'full comparison/pin/seal/failure/alias source guard: ' + snippet)
    check("set(os.environ) == set(ENV)" in source and 'os.environ.items' not in source and 'dict(os.environ)' not in source,
          'environment names checked; no host environment value serialization')
    return constants, mutation_calls, len(source.splitlines())


def hrefs(path):
    return [href.strip().strip('<>') for href in re.findall(r'\[[^\]]*\]\(([^)]+)\)', read(path).decode())
            if not href.strip().strip('<>').startswith(('http://', 'https://', 'mailto:', '#')) and href.split('#', 1)[0]]


def main():
    check(len(sys.argv) == 4 and sys.argv[1:3] == ['inspect-final-preparation', '--expected-root-closure-sha256'], 'explicit static-only invocation')
    check(set(os.environ) == set(ENV) and all(os.environ[k] == v for k, v in ENV.items()), 'exact empty-launcher safe environment')
    check(sys.flags.isolated and sys.flags.no_site and sys.flags.dont_write_bytecode and sys.flags.optimize == 0 and
          Path(sys.executable).resolve() == Path('/usr/bin/python3.10') and Path.cwd() == ROOT, 'fixed unoptimized source-only interpreter/cwd')
    source_path = HERE / 'freeze_p210_round1.py'
    source = read(source_path).decode()
    contract = parse(HERE / 'ROOT_CLOSURE_CONTRACT.json')
    c, mutation_calls, source_lines = source_audit(source, contract)
    paper, r0, review, pair, target = [c[key] for key in ('PAPER', 'ROUND0', 'REVIEW', 'PAIR', 'TARGET')]
    check(not target.exists() and not target.is_symlink(), 'Round1 absent; audit must never create it')
    check(re.fullmatch('[0-9a-f]{64}', sys.argv[3]) is not None and digest(c['ACCEPTANCE']) == sys.argv[3], 'actual explicit root closure hash')
    closure = parse(c['ACCEPTANCE'])
    for key, value in contract['required_fields'].items():
        check(type(closure.get(key)) is type(value) and closure[key] == value, 'actual required root field: ' + key)
    check(closure['initial_review_aliases'] == contract['initial_review_aliases'] and
          not closure.get('historical_input_aliases', []), 'only exact initial A aliases; no R0 aliases')
    check(isinstance(closure['evidence'], dict) and len(closure['evidence']) >= 2, 'actual root evidence map')
    for name, value in closure['evidence'].items():
        check(Path(name) != c['ACCEPTANCE'] and digest(Path(name)) == value, 'actual root evidence referent')
    direct = parse(HERE / 'INPUT_PINS.json')
    check(direct['schema'] == 'p210-round1-preparation-direct-input-pins-v1' and direct['expected_root_closure_sha256'] == sys.argv[3] and
          direct['pins'][str(c['ACCEPTANCE'])] == sys.argv[3], 'actual closure bound in direct pins')
    for name, value in direct['pins'].items():
        check(digest(Path(name)) == value, 'actual preparation direct input')
    for name, value in c['ORIGINAL_SOURCES'].items():
        check(digest(name) == value, 'exact original freezer infrastructure source, read only')
    core, accepted, rootpair = manifest(r0), manifest(review), manifest(pair)
    check(len(core) == 493 and len(accepted) == 552 and len(rootpair) == 59, '493/552/59 complete package sizes')
    for path, value in [(r0 / 'SHA256SUMS', c['ROUND0_SEAL']), (review / 'SHA256SUMS', c['FINAL_A_SEAL']),
                        (pair / 'SHA256SUMS', c['PAIR_SEAL']), (paper / 'SHA256SUMS', c['AUTHOR_SEAL']),
                        (paper / 'AUTHOR_MANIFEST.sha256', c['AUTHOR_SEAL']),
                        (paper / 'PAPER_MANIFEST.sha256', c['PRIOR_WHOLE_SEAL']), (paper / 'ROOT_LIFECYCLE.md', c['PRIOR_LIFECYCLE'])]:
        check(digest(path) == value, 'exact fixed milestone seal or body')
    author = manifest(paper, 'AUTHOR_MANIFEST.sha256', False)
    check(len(author) == 489 and rows(r0 / 'AUTHOR_MANIFEST.sha256') == author, 'unchanged exact489 author roles')
    raw_comparisons = 0
    for name in author:
        check(read(paper / name) == read(r0 / name), 'full live/R0 author byte comparison')
        raw_comparisons += 1
    expected_core = dict(author)
    expected_core.update({'AUTHOR_MANIFEST.sha256': c['AUTHOR_SEAL'], 'ROOT_ADOPTION.md': digest(paper / 'ROOT_ADOPTION.md'),
        'FREEZE_ADAPTER.py': c['ORIGINAL_SOURCES'][c['QA'] / 'freeze_p210_round0.py'], 'FROZEN_LINK_MAP.json': digest(r0 / 'FROZEN_LINK_MAP.json')})
    check(core == expected_core, 'exact original493 role set, no nested freeze')
    whole = manifest(paper, 'PAPER_MANIFEST.sha256')
    check(len(whole) == 987, 'old whole987 complete before Round1 only')
    initial, current = parse(review / 'FINDINGS.json'), parse(review / 'CURRENT_FINDINGS.json')
    census = {'Critical': {'open': 0, 'resolved': 0}, 'Major': {'open': 0, 'resolved': 1},
              'Minor': {'open': 0, 'resolved': 0}, 'total_open': 0, 'total_resolved': 1}
    check(initial['schema'] == 'p210-a-findings-v1' and initial['round'] == 'A_initial' and initial['census'] == census, 'honest initial E1 census')
    check(current['schema'] == 'p210-a-current-findings-v1' and current['round'] == 'A_same_process_exact_delta' and
          current['reviewer'] == '/root/p210_a_reviewer' and current['verdict'] == 'ACCEPTED_EXACT_NO_CHANGE_DELTA' and
          current['census'] == census and current['findings'] == initial['findings'] and len(current['findings']) == 1 and
          current['findings'][0]['id'] == 'P210-A-E1' and current['findings'][0]['status'] == 'resolved' and
          current['findings'][0]['changed_scientific_inputs'] == [] and 'remain unavailable' in current['findings'][0]['historical_loss_not_repaired'],
          'complete resolved Major E1 retained, historical loss not invented back')
    check(current['response'] == '../../P210_A_RESPONSE.md' and current['response_sha256'] == c['RESPONSE_SHA'] and
          current['initial_findings_sha256'] == c['INITIAL_FINDINGS'], 'current exact response and initial findings provenance')
    for row in contract['initial_review_aliases']:
        check(digest(Path(row['physical_path'])) == row['sha256'], 'original A document physically preserved')
    initial_rows = rows(c['INITIAL_HISTORY'] / 'SHA256SUMS')
    check(len(initial_rows) == 484 and initial_rows['DELTA.md'] == c['INITIAL_DELTA'], 'initial484 membership and old Delta')
    projected = {}
    for name, value in initial_rows.items():
        physical = 'history/initial_before_delta/DELTA.md' if name == 'DELTA.md' else name
        check(accepted[physical] == value, 'all original484 bytes included in verified current manifest')
        projected[physical] = value
    projected['history/initial_before_delta/SHA256SUMS'] = c['INITIAL_A_SEAL']
    check(rows(review / 'INITIAL_PRESERVED_PINS.sha256') == projected, 'exact485 projected original roles')
    inputs = {str((r0 / name).relative_to(ROOT)): value for name, value in core.items()}
    inputs[str((r0 / 'SHA256SUMS').relative_to(ROOT))] = c['ROUND0_SEAL']
    check(rows(review / 'INPUT_PINS.sha256') == inputs, 'exact494 reviewed input roles')
    receipt = parse(pair / 'RESULT.json')
    check(receipt['status'] == 'PASS_ROOT_P210_A_STRICT_PAIR' and receipt['role'] == 'p210_a' and receipt['errors'] == [] and
          receipt['known_input_count'] == 3634 and len(receipt['commands']) == 10 and receipt['raw_canonical_comparisons'] == 2 and
          receipt['raw_pair_comparisons'] == 1 and [row['checks'] for row in receipt['results']] == [133978, 133978] and
          all(row['stdout'] == {'bytes': 703850, 'sha256': c['A_CANONICAL']} for row in receipt['results']), 'actual root original pair result fields')
    for label in ('03_verify_01', '03_verify_02'):
        check(read(pair / 'commands' / label / 'stdout.raw') == read(review / 'CANONICAL.json'), 'actual full canonical raw comparison')
        raw_comparisons += 1
    check(digest(review / 'CANONICAL.json') == c['A_CANONICAL'], 'exact original independent canonical')
    old = parse(r0 / 'FROZEN_LINK_MAP.json')
    check(len(old['links']) == 57 and len(old['external_input_pins']) == 33 and old['author_payloads'] == 489 and
          old['historical_author_manifest_sha256'] == c['AUTHOR_SEAL'], 'original57/33 exact link-map scope')
    for name, value in old['external_input_pins'].items():
        check(digest(Path(name)) == value, 'all33 exact current external originals; no alias fallback')
    rebuilt = []
    for name in sorted(core):
        if not name.endswith('.md'):
            continue
        origin = Path(old['exact_document_origin_roles'].get(name, str(paper / name)))
        for href in hrefs(r0 / name):
            candidate = (origin.parent / unquote(href.split('#', 1)[0])).resolve()
            if candidate == paper / 'SHA256SUMS':
                physical, value, mode = r0 / 'AUTHOR_MANIFEST.sha256', c['AUTHOR_SEAL'], 'exact-author-seal-alias'
            elif candidate.is_relative_to(paper) and candidate.relative_to(paper).as_posix() in core:
                relative = candidate.relative_to(paper).as_posix()
                physical, value, mode = r0 / relative, core[relative], 'physical-copied-input'
            else:
                check(str(candidate) in old['external_input_pins'], 'declared exact old original origin')
                physical, value, mode = candidate, old['external_input_pins'][str(candidate)], 'external-exact-original-origin'
            rebuilt.append(dict(document=name, document_sha256=core[name], exact_markdown_origin=str(origin), href=href,
                                mode=mode, physical_target=str(physical), sha256=value))
    check(rebuilt == old['links'], 'all57 exact source-origin link rows independently reconstructed')
    anchor_links = []
    for name, path in c['ANCHORS'].items():
        digest(path)
        if path.suffix == '.md':
            origin = review / 'DELTA.md' if name == 'A_INITIAL_DELTA.md' else path
            for href in hrefs(path):
                referent = (origin.parent / unquote(href.split('#', 1)[0])).resolve()
                value = digest(referent)
                anchor_links.append({'anchor': name, 'original_document': str(origin), 'href': href, 'original_target': str(referent), 'sha256': value})
    planned_names = set(core) | {'ROUND1_ACCEPTANCE/' + name for name in c['ANCHORS']} | {'ROUND1_FREEZE_ADAPTER.py', 'ROUND1_PROVENANCE.json'}
    check(len(planned_names) == 508 and len(c['ANCHORS']) == 13, 'plan only:493+13+source+provenance=508 payloads')
    before = dict(PINS)
    for name, value in before.items():
        read(Path(name))
        check(PINS[name] == value, 'all actual read inputs unchanged on full reread')
    check(not target.exists() and not target.is_symlink(), 'Round1 remains absent after static audit')
    print(json.dumps({'status': 'PASS_READONLY_P210_ROUND1_PREPARATION_STATIC', 'checks': CHECKS,
        'scope': 'AST and separately implemented bounded read-only data checks; not freezer execution or physical Round1 acceptance',
        'freezer_runtime_or_refusal_executions': 0, 'science_build_view_or_original_program_executions': 0,
        'source_sha256': digest(source_path), 'source_lines': source_lines, 'static_checker_sha256': digest(Path(__file__).resolve()),
        'actual_root_closure_sha256': sys.argv[3], 'input_pins_sha256': digest(HERE / 'INPUT_PINS.json'),
        'bounded_read_input_count': len(before), 'bounded_read_input_map_sha256': sha256(json.dumps(before, sort_keys=True, separators=(',', ':')).encode()).hexdigest(),
        'bounded_read_input_map_scope': 'Actual current bytes were reread; map is digest-bound here, not copied into a new broad audit archive.',
        'complete_packages': {'round0_payloads': 493, 'accepted_a_payloads': 552, 'root_pair_payloads': 59, 'prior_whole_payloads': 987},
        'original_initial_a_payloads_preserved': 484, 'projected_initial_roles': 485, 'author_raw_byte_comparisons': 489,
        'canonical_raw_byte_comparisons': 2, 'all_actual_raw_byte_comparisons': raw_comparisons,
        'raw_method': 'full Python bytes equality; not a native cmp command', 'round0_link_roles': len(rebuilt),
        'round0_external_originals_no_aliases': 33, 'anchor_link_roles': anchor_links,
        'planned_payloads_not_created': 508, 'target_absent': True, 'mutation_call_sites_inspected_as_text_only': mutation_calls,
        'limits': ['Actual freezer is unexecuted, including refusal paths.', 'No science or build rerun or PDF view.',
            'Only future root execution may create the absent Round1.', 'Initial resolved Major E1 historical losses remain explicit.'],
        'environment': ENV, 'argv': sys.argv, 'orig_argv': sys.orig_argv, 'cwd': str(ROOT)}, sort_keys=True, indent=2))
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except Exception:
        print(json.dumps({'status': 'FAIL_STATIC_PREPARATION_NO_FREEZER_EXECUTION', 'checks_before_failure': CHECKS,
                          'traceback': traceback.format_exc(), 'freezer_runtime_or_refusal_executions': 0,
                          'known_read_pins': PINS}, sort_keys=True, indent=2))
        raise SystemExit(1)
