#!/usr/bin/env python3
"""Dedicated read-only P207 terminal artifact adapter.

This program does not import/execute a mathematical verifier, build TeX,
render/view pages, accept reviewer deltas, or edit any input. It checks the
actual P207 schemas; historical generic auditors and packages are untouched.
"""
import ast
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[3]
BATCH = ROOT/'docs/papers204_208_sequence'
PAPER = ROOT/'papers/207-upper-neighbor-rank-dynamics'
A = BATCH/'reviews/p207_a'
B = BATCH/'reviews/p207_b'
REPLAYS = BATCH/'qa/root_replays'
FINAL = PAPER/'qa_final'
AUTHORS = {'/root', '/root/batch197_fosp_gate'}
REVIEWERS = {'a': '/root/batch197_lzk_gate', 'b': '/root/batch197_fifth_scout'}
COUNTS = {'author': 1384012, 'a': 1326321, 'b': 2158999}
SETTINGS = {'LC_ALL': 'C', 'TZ': 'UTC', 'PYTHONHASHSEED': '0',
            'PYTHONDONTWRITEBYTECODE': '1', 'PYTHONSAFEPATH': '1'}
CHECKS = Counter()
READS = {}
MANIFESTS = []
RECEIPTS = []
ALIASES_USED = {}
HOST_SYMLINKS = {}


def require(ok, section, detail):
    CHECKS[section] += 1
    if not ok:
        raise AssertionError((section, detail))


def label(path):
    return str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)


def read(path):
    require(path.is_file() and not path.is_symlink(), 'regular_inputs', label(path))
    raw = path.read_bytes()
    record = {'bytes': len(raw), 'sha256': sha256(raw).hexdigest()}
    name = label(path)
    if name in READS:
        require(READS[name] == record, 'read_stability', name)
    READS[name] = record
    return raw


def parsed(path):
    return json.loads(read(path))


def digest(path):
    return sha256(read(path)).hexdigest()


def physical(folder):
    found = set()
    for p in folder.rglob('*'):
        require(not p.is_symlink(), 'regular_inputs', ('no symlink in owned package', label(p)))
        if p.is_file():
            found.add(str(p.relative_to(folder)))
    return found


def equal(left, right, detail):
    require(read(left) == read(right), 'raw_equality', detail)


def historical(path, family):
    """Only concrete preserved initial aliases, never hash-based guessing."""
    base = A if family == 'a' else B
    aliases = {'FINDINGS.json': 'FINDINGS.initial.json', 'SHA256SUMS': 'SHA256SUMS.initial'}
    if family == 'b':
        aliases.update({'BUILD_REPORT.md': 'BUILD_REPORT.initial.md', 'REPORT.md': 'REPORT.initial.md',
                        'check_delta_artifacts.py': 'check_delta_artifacts.initial.py'})
    if path.parent == base and path.name in aliases:
        actual = base/aliases[path.name]
        ALIASES_USED[label(path)] = label(actual)
        return actual
    return path


def check_info(path, expected, section):
    raw = read(path)
    require(type(expected) is dict and expected['bytes'] == len(raw) and
            expected['sha256'] == sha256(raw).hexdigest(), section, label(path))


def host_info(path, expected):
    allowed = (Path('/etc/texmf'), Path('/usr/share/texmf'), Path('/usr/share/texlive'),
               Path('/usr/share/fonts'), Path('/var/lib/texmf'))
    require(any(path.is_relative_to(base) for base in allowed), 'terminal_host_provenance', ('declared TeX host path', str(path)))
    resolved = path.resolve(strict=True)
    if path.is_symlink():
        HOST_SYMLINKS[str(path)] = str(resolved)
    check_info(resolved, expected, 'terminal_host_provenance')


def manifest(path, base, complete=False, family=None, expected_names=None):
    pins = {}
    for line in read(path).decode().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        require(match is not None, 'manifest_syntax', label(path))
        pin, name = match.groups()
        rel = Path(name)
        require(not rel.is_absolute() and '..' not in rel.parts and name not in pins,
                'manifest_syntax', (label(path), name))
        pins[name] = pin
        target = base/name
        if family:
            target = historical(target, family)
        require(digest(target) == pin, 'manifest_hashes', (label(path), name))
    if complete:
        require(set(pins) == physical(base)-{str(path.relative_to(base))},
                'manifest_coverage', label(path))
    if expected_names is not None:
        require(set(pins) == set(expected_names), 'manifest_coverage', (label(path), 'exact expected set'))
    MANIFESTS.append({'path': label(path), 'base': label(base), 'entries': len(pins),
                      'complete_nonself': complete, 'historical_family': family})
    return pins


def workspace_target(name):
    relative = Path(name)
    require(not relative.is_absolute() and '..' not in relative.parts, 'workspace_reference', name)
    return ROOT/relative


def json_pin_map(record, family=None, info_values=False):
    for name, expected in record.items():
        if Path(name).is_absolute():
            require(name == '/root/miniconda3/bin/python3.12', 'workspace_reference', 'exact recorded external Python executable only')
            path = Path(name)
        else:
            path = workspace_target(name)
        if family:
            path = historical(path, family)
        if info_values:
            check_info(path, expected, 'json_referent_hashes')
        else:
            require(digest(path) == expected, 'json_referent_hashes', name)


def leaves(value):
    if isinstance(value, dict):
        return sum(leaves(v) for v in value.values())
    if isinstance(value, list):
        return sum(leaves(v) for v in value)
    return 1


def inspect_producer(path, allowed_imports, author=False):
    tree = ast.parse(read(path))
    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.update(a.name for a in node.names)
        if isinstance(node, ast.ImportFrom):
            require(node.level == 0, 'producer_scope', (label(path), 'relative import'))
            imports.add(node.module)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            require(node.func.id not in {'open', 'eval', 'exec', '__import__', 'compile'},
                    'producer_scope', (label(path), node.lineno, 'file/dynamic call'))
        if isinstance(node, ast.Attribute):
            require(node.attr not in {'read_text', 'read_bytes', 'open', 'system', 'popen'},
                    'producer_scope', (label(path), node.lineno, 'IO method'))
    require(imports == set(allowed_imports), 'producer_scope', (label(path), sorted(imports)))
    if author:
        # Its old -B evidence is not retroactively called isolated. Explicit
        # if/raise checks have no Python assert statements to optimize away.
        require(not any(isinstance(n, ast.Assert) for n in ast.walk(tree)),
                'producer_scope', 'author has no optimization-removable assert statements')
    return {'imports': sorted(imports), 'ast_nodes': len(list(ast.walk(tree))),
            'sha256': digest(path), 'no_formal_sandbox_claim': True}


def commands_with_stems(folder, receipt, stems, exit_field='exit', flat_hashes=False):
    commands = receipt['commands']
    require(len(commands) == len(stems), 'command_schema', label(folder))
    for stem, row in zip(stems, commands, strict=True):
        require(row[exit_field] == 0, 'recorded_exit', (label(folder), stem))
        for stream in ('stdout', 'stderr'):
            path = folder/f'{stem}.{stream}'
            if flat_hashes:
                require(digest(path) == row[f'{stream}_sha256'], 'stream_binding', (label(folder), stem, stream))
            else:
                check_info(path, row[stream], 'stream_binding')
            if stream == 'stderr' or '.cmp' in stem:
                require(read(path) == b'', 'empty_stream', (label(folder), stem, stream))
        argv = row.get('command', row.get('argv'))
        require(type(argv) is list and bool(argv), 'command_schema', (label(folder), stem))
        if '.cmp' in stem:
            require(argv[0] == 'cmp' and len(argv) == 3, 'command_schema', (label(folder), stem, 'cmp'))
            left, right = map(Path, argv[1:])
            require(left.is_relative_to(ROOT) and right.is_relative_to(ROOT),
                    'command_schema', (label(folder), stem, 'workspace raw pair'))
            equal(left, right, (label(folder), stem))


def check_freezes():
    copies = []
    for round_number in range(3):
        folder = PAPER/f'frozen_round{round_number}'
        pins = manifest(folder/'SHA256SUMS', folder, complete=True)
        require(len(pins) == 105 and len(physical(folder)) == 106, 'frozen_science', round_number)
        for name in pins:
            equal(folder/name, PAPER/name, ('exact live/freeze', round_number, name))
        if round_number:
            equal(folder/'SHA256SUMS', PAPER/'frozen_round0/SHA256SUMS', ('no science delta', round_number))
        copies.append({'round': round_number, 'entries': len(pins), 'manifest_sha256': digest(folder/'SHA256SUMS')})
    return copies


def check_author_archive():
    pins = manifest(PAPER/'author_replay/OWNED_MANIFEST.sha256', PAPER)
    require(len(pins) == 85, 'author_archive', 'exact owned seal')
    required = {'verify.py', 'CANONICAL.json', 'record_author.py', 'AUTHOR_EXECUTION.md'}
    required |= {str((PAPER/'author_replay'/name).relative_to(PAPER))
                 for name in physical(PAPER/'author_replay') if name != 'OWNED_MANIFEST.sha256'}
    require(set(pins) == required, 'author_archive', 'full author-owned scope')
    for attempt, runs, expected_entries in [('initial_01', (0,), 30), ('pair_01', (1, 2), 36)]:
        folder = PAPER/'author_replay'/attempt
        sealed = manifest(folder/'MANIFEST.sha256', folder, complete=True)
        require(len(sealed) == expected_entries, 'author_archive', attempt)
        before = manifest(folder/'INPUT_PINS.before.sha256', folder/'source_inputs',
                          expected_names=physical(folder/'source_inputs'))
        after = manifest(folder/'INPUT_PINS.after.sha256', folder/'source_inputs')
        require(len(before) == 17 and before == after, 'author_archive', ('exact physical before/after provenance', attempt))
        equal(folder/'INPUT_PINS.before.sha256', folder/'INPUT_PINS.after.sha256', ('author before/after bytes', attempt))
        equal(folder/'verify.py', PAPER/'verify.py', ('author copied producer', attempt))
        equal(folder/'CANONICAL.input.json', PAPER/'CANONICAL.json', ('author canonical snapshot', attempt))
        rec = parsed(folder/'RECEIPT.json')
        require(rec['status'] == 'PASS' and rec['inputs_unchanged'] and rec['input_pins'] == 17,
                'author_archive', ('recorded successful attempt', attempt))
        require(rec['declared_environment'] == SETTINGS, 'author_archive', ('original nonisolated settings', attempt))
        python = Path(rec['python_executable']).resolve()
        require(digest(python) == rec['python_executable_sha256'], 'author_archive', ('current binary vs recorded binary', attempt))
        for command in rec['commands']:
            require(command['exit_code'] == 0, 'recorded_exit', (attempt, command['argv']))
            for stream in ('stdout', 'stderr'):
                item = command[stream]
                path = folder/item['path']
                check_info(path, item, 'stream_binding')
                if stream == 'stderr' or command['argv'][0] == 'cmp':
                    require(read(path) == b'', 'empty_stream', (attempt, item['path']))
            if command['argv'][0] == 'cmp':
                equal(Path(command['argv'][1]), Path(command['argv'][2]), ('recorded author cmp', attempt))
        for number in runs:
            equal(folder/f'run{number}.stdout', PAPER/'CANONICAL.json', ('full author raw output', attempt, number))
        require([v['run'] for v in rec['numerical_outputs']] == list(runs) and
                all(v['assertions'] == COUNTS['author'] for v in rec['numerical_outputs']),
                'author_archive', ('exact actual producer census', attempt))
        RECEIPTS.append({'path': label(folder/'RECEIPT.json'), 'commands': len(rec['commands']),
                         'archived_mathematical_runs': len(runs), 'new_runs_by_auditor': 0})
    export = PAPER/'author_replay/export_pair_01'
    require(len(manifest(export/'MANIFEST.sha256', export, complete=True)) == 9,
            'author_archive', 'complete alias-export package')
    rec = parsed(export/'RECEIPT.json')
    require(rec['status'] == 'PASS' and rec['new_numerical_runs'] == 0 and len(rec['commands']) == 4,
            'author_archive', 'copy-only export, not new execution')
    require(digest(PAPER/'author_replay/export_pair.py') == rec['exporter_sha256'] and
            digest(PAPER/'author_replay/pair_01/RECEIPT.json') == rec['pair_receipt_sha256'],
            'author_archive', 'exporter and actual pair receipt pins')
    for command in rec['commands']:
        require(command['exit_code'] == 0 and command['argv'][0] == 'cmp', 'recorded_exit', 'author export')
        for stream in ('stdout', 'stderr'):
            require(read(export/command[stream]) == b'', 'empty_stream', command[stream])
        equal(Path(command['argv'][1]), Path(command['argv'][2]), 'actual export comparison')
    for number in (1, 2):
        equal(PAPER/f'author_replay/run{number}.stdout', PAPER/f'author_replay/pair_01/run{number}.stdout',
              ('flat original pair alias', number))
    return {'owned_inputs': len(pins), 'original_numerical_runs': 3, 'flat_alias_additional_runs': 0,
            'runtime_scope': 'Original -B/settings evidence; no isolated or hermetic historical environment claim.'}


def check_root_author():
    folder = REPLAYS/'p207_author'
    rec = parsed(folder/'RECEIPT.json')
    require(rec['pass'] and rec['inputs_unchanged'] and rec['owned_input_count'] == 85 and
            rec['before_inputs'] == rec['after_inputs'], 'root_author', 'successful unchanged 85-input pair')
    owned = manifest(PAPER/'author_replay/OWNED_MANIFEST.sha256', PAPER)
    require(set(rec['before_inputs']) == set(owned), 'root_author', 'full reused dependency key')
    for name, info in rec['before_inputs'].items():
        check_info(PAPER/name, info, 'root_author')
    require(rec['settings'] == SETTINGS and rec['assertions_per_run'] == [COUNTS['author']]*2,
            'root_author', 'recorded original settings and exact counts')
    check_info(BATCH/'qa/replay_p207_author.py', rec['harness'], 'root_author')
    check_info(PAPER/'author_replay/OWNED_MANIFEST.sha256', rec['author_owned_manifest'], 'root_author')
    equal(folder/'verify.py', PAPER/'verify.py', 'root author copied standalone source')
    equal(folder/'CANONICAL.json', PAPER/'CANONICAL.json', 'root author copied canonical')
    stems = ['owned_seal', 'python_version', 'run1', 'run1.cmp', 'run2', 'run2.cmp', 'pair.cmp']
    commands_with_stems(folder, rec, stems, exit_field='exit_code')
    for stem, command in zip(stems, rec['commands'], strict=True):
        if stem in ('run1', 'run2'):
            require(command['command'][1:] == ['-B', str(folder/'verify.py')],
                    'root_author', ('recorded nonisolated original command', stem))
            equal(folder/f'{stem}.stdout', PAPER/'CANONICAL.json', ('root author exact raw output', stem))
    RECEIPTS.append({'path': label(folder/'RECEIPT.json'), 'commands': len(stems),
                     'archived_root_reproduction_runs': 2, 'new_runs_by_auditor': 0,
                     'runtime_scope': 'Original -B only; no assertion statements in author code; not retroactively isolated.'})


def check_root_review(letter, controlled=True):
    package = A if letter == 'a' else B
    suffix = '_controlled' if controlled else ''
    folder = REPLAYS/f'p207_{letter}{suffix}'
    rec = parsed(folder/'RECEIPT.json')
    require(rec['pass'] and rec['before_package_files'] == rec['after_package_files'],
            'root_review', (letter, suffix, 'recorded successful stable package'))
    initial = manifest(package/'SHA256SUMS.initial', package, family=letter)
    require(set(rec['before_package_files']) == set(initial) | {'SHA256SUMS'},
            'root_review', (letter, suffix, 'exact original physical package baseline'))
    for name, info in rec['before_package_files'].items():
        check_info(historical(package/name, letter), info, 'root_review')
    equal(folder/'verify.py', package/'verify.py', (letter, suffix, 'copied source'))
    equal(folder/'CANONICAL.json', package/'CANONICAL.json', (letter, suffix, 'copied canonical'))
    check_info(folder/'harness_input.py', rec['harness'], 'root_review')
    if controlled:
        context_name = 'CONTEXT_SOURCE_PINS.sha256' if letter == 'a' else 'CONTEXT_PINS.sha256'
        stems = ['SHA256SUMS.before', 'INPUT_PINS.sha256.before', context_name+'.before',
                 'python_version', 'python_runtime_flags', 'python_link_dependencies',
                 'run1', 'run1.cmp', 'run2', 'run2.cmp', 'pair.cmp',
                 'INPUT_PINS.sha256.after', context_name+'.after', 'SHA256SUMS.after']
        require(rec['python_flags'] == ['-I', '-B'] and rec['environment_overrides'] == SETTINGS,
                'root_review', (letter, 'controlled command environment'))
        require(parsed(folder/'python_runtime_flags.stdout') ==
                {'debug': True, 'ignore_environment': 1, 'isolated': 1, 'no_user_site': 1, 'optimize': 0},
                'root_review', (letter, 'actual assertion-enabled isolated runtime probe'))
        python = Path(rec['python']['executable']).resolve()
        check_info(python, rec['python']['file'], 'root_review')
    else:
        require(letter == 'a', 'root_review', 'only the actual earlier noncontrolled A pair exists')
        stems = ['SHA256SUMS', 'INPUT_PINS.sha256', 'python_version', 'python_link_dependencies',
                 'run1', 'run1.cmp', 'run2', 'run2.cmp', 'pair.cmp']
    commands_with_stems(folder, rec, stems)
    for stem, command in zip(stems, rec['commands'], strict=True):
        if controlled and stem in (context_name+'.before', context_name+'.after'):
            require(command['command'] == ['sha256sum', '-c', str(package/context_name)] and
                    command['cwd'] == str(ROOT), 'root_review', (letter, stem, 'exact context referents'))
        if stem in ('run1', 'run2'):
            expected = ['-I', '-B', str(folder/'verify.py')] if controlled else ['-B', str(folder/'verify.py')]
            require(command['command'][1:] == expected, 'root_review', (letter, suffix, stem, 'actual flags'))
            equal(folder/f'{stem}.stdout', package/'CANONICAL.json', (letter, suffix, stem, 'complete raw output'))
    require([run['assertions'] for run in rec['runs']] == [COUNTS[letter]]*2,
            'root_review', (letter, suffix, 'complete run assertion census'))
    if letter == 'b':
        # This is the actual scope adaptation made before the first root B
        # execution; the historical A harness copies are not rewritten.
        source = read(folder/'harness_input.py').decode()
        require("else 'CONTEXT_PINS.sha256'" in source and "pin_names = ['INPUT_PINS.sha256', context_name]" in source,
                'root_review', 'B context manifest was mandatory before actual first B pair')
    RECEIPTS.append({'path': label(folder/'RECEIPT.json'), 'commands': len(stems),
                     'archived_root_reproduction_runs': 2, 'new_runs_by_auditor': 0,
                     'reused_for_terminal_pair': controlled,
                     'runtime_scope': 'controlled isolated/assertion-enabled' if controlled else 'preserved original noncontrolled A evidence only'})


def check_terminal_builds():
    terminal_manifest = manifest(FINAL/'SHA256SUMS', FINAL, complete=True)
    rec = parsed(FINAL/'BUILD_EXECUTION.json')
    require(rec['kind'] == 'ACTUAL_TWO_POST_DELTA_SOURCE_ONLY_TERMINAL_BUILDS_NOT_VISUAL_REVIEW' and
            rec['status'] == 'BUILD_PAIR_PASS' and rec['failure'] is None and rec['input_bytes_unchanged']
            and rec['before_inputs'] == rec['after_inputs'], 'terminal_build', 'actual successful stable terminal pair')
    freeze = PAPER/'frozen_round2'
    expected = {label(freeze/name) for name in physical(freeze)}
    expected |= {label(BATCH/'qa/cold_build.sh'), label(BATCH/'qa/run_p207_terminal_builds.py')}
    expected |= {label(review/name) for review in (A, B) for name in ('FINDINGS.json', 'DELTA.md', 'SHA256SUMS')}
    require(set(rec['before_inputs']) == expected, 'terminal_build', 'complete 114-object build/lifecycle launch dependency set')
    json_pin_map(rec['before_inputs'], info_values=True)
    require(rec['actual_page_view_status'] == 'PENDING_NOT_INFERRED_FROM_PDF_OR_PNG_HASH',
            'terminal_build', 'preserved actual build-time pending-view statement')
    require(rec['external_status'] == 'HOLD_EXTERNAL' and len(rec['commands']) == 5,
            'terminal_build', 'actual five build/pin/cmp commands')
    expected_commands = [
        ('round2_pins_before', ['sha256sum', '-c', str(freeze/'SHA256SUMS')], freeze),
        ('cold_build_1', ['bash', str(BATCH/'qa/cold_build.sh'), str(freeze), str(FINAL/'cold_build_1'), str(freeze/'main.pdf')], ROOT),
        ('cold_build_2', ['bash', str(BATCH/'qa/cold_build.sh'), str(freeze), str(FINAL/'cold_build_2'), str(freeze/'main.pdf')], ROOT),
        ('pair_pdf_cmp', ['cmp', str(FINAL/'cold_build_1/main.pdf'), str(FINAL/'cold_build_2/main.pdf')], ROOT),
        ('round2_pins_after', ['sha256sum', '-c', str(freeze/'SHA256SUMS')], freeze),
    ]
    for row, (stem, argv, cwd) in zip(rec['commands'], expected_commands, strict=True):
        require(row['label'] == stem and row['command'] == argv and row['cwd'] == str(cwd) and row['exit_code'] == 0,
                'terminal_build', ('exact actual command', stem))
        for stream in ('stdout', 'stderr'):
            require(row[stream]['path'] == f'{stem}.{stream}', 'terminal_build', ('stream path', stem, stream))
            check_info(FINAL/row[stream]['path'], row[stream], 'stream_binding')
            if stream == 'stderr' or stem == 'pair_pdf_cmp':
                require(read(FINAL/row[stream]['path']) == b'', 'empty_stream', ('terminal', stem, stream))
    require([b['number'] for b in rec['builds']] == [1, 2], 'terminal_build', 'two actual physical builds')
    source_names = {'main.tex', 'math_commands.tex', 'references.bib'} | {
        str(p.relative_to(PAPER)) for p in (PAPER/'sections').rglob('*.tex')}
    require(len(source_names) == 9, 'terminal_build', 'nine-source modular carrier')
    expected_underfull = r'Underfull \vbox (badness 1038) has occurred while \output is active []'
    build_records = []
    for number, row in enumerate(rec['builds'], 1):
        build = FINAL/f'cold_build_{number}'
        require(row['directory'] == f'qa_final/cold_build_{number}' and row['source_only_inputs_count'] == 9
                and set(row['source_inputs']) == source_names, 'terminal_build', ('exact copied sources', number))
        manifest(build/'SOURCE_INPUTS.sha256', build, expected_names=source_names)
        for name in source_names:
            equal(build/name, PAPER/name, ('actual terminal source-only input', number, name))
        equal(build/'main.pdf', PAPER/'main.pdf', ('terminal exact final PDF', number))
        check_info(build/'main.pdf', row['pdf'], 'terminal_build')
        manifest(build/'PDF.sha256', build, expected_names={'main.pdf'})
        require(read(build/'BUILD_ENVIRONMENT.txt').decode().splitlines() ==
                ['SOURCE_DATE_EPOCH=1704067200', 'FORCE_SOURCE_DATE=1', 'TZ=UTC', 'LC_ALL=C'],
                'terminal_build', ('explicit reproducibility settings', number))
        log = read(build/'main.log').decode()
        diagnostics = [line for line in log.splitlines() if any(word in line for word in ('Underfull', 'Overfull', 'Warning', 'undefined'))]
        require(diagnostics == row['actual_diagnostics'] == [expected_underfull] and not re.search(r'^!', log, re.M),
                'terminal_build', ('exact singleton spacing diagnostic, not blanket suppression', number))
        require(read(build/'DIAGNOSTICS.txt') == b'', 'terminal_build', ('narrow helper scanner only', number))
        fls = {line[6:] for line in read(build/'main.fls').decode().splitlines() if line.startswith('INPUT ')}
        local = {str(Path(name)) for name in fls if not Path(name).is_absolute()}
        external = {name for name in fls if Path(name).is_absolute()}
        require(local == source_names-{'references.bib'} | {'main.aux', 'main.bbl', 'main.out'},
                'terminal_build', ('last-pass inputs, not stale source launch products', number))
        host_pins = row['external_TeX_inputs_pinned_after_build']
        require(set(host_pins) == external and len(host_pins) > 0,
                'terminal_build', ('every actual external TeX path post-build pinned', number))
        for name, wanted in host_pins.items():
            host_info(Path(name), wanted)
        bib_log = read(build/'main.blg').decode()
        require('The style file: plainnat.bst' in bib_log and 'Database file #1: references.bib' in bib_log,
                'terminal_build', ('actual bibliography database and host style', number))
        metadata = read(build/'PDFINFO.txt').decode()
        require(re.search(r'^Pages:\s+7$', metadata, re.M) is not None, 'terminal_build', ('seven actual pages', number))
        for field in ('Title', 'Author', 'Creator', 'Producer', 'CreationDate', 'ModDate'):
            found = re.search(rf'^{field}:(.*)$', metadata, re.M)
            require(not found or not found.group(1).strip(), 'terminal_build', ('blank metadata', number, field))
        fonts = read(build/'FONTS.txt').decode().splitlines()[2:]
        require(len(fonts) == 31 and all('Type 1' in s and s.split()[-5] == 'yes' for s in fonts),
                'terminal_build', ('all 31 embedded Type 1 font objects', number))
        build_records.append({'number': number, 'source_inputs': 9, 'pdf_sha256': digest(build/'main.pdf'),
                              'host_inputs_pinned_after_build': len(host_pins), 'actual_diagnostics': diagnostics})
    equal(FINAL/'cold_build_1/main.pdf', FINAL/'cold_build_2/main.pdf', 'two physical final builds raw-identical')
    for name in ('ENGINE.txt', 'BIBTEX_ENGINE.txt', 'BUILD_ENVIRONMENT.txt'):
        equal(FINAL/'cold_build_1'/name, FINAL/'cold_build_2'/name, ('same recorded terminal engine/settings', name))
    RECEIPTS.append({'path': label(FINAL/'BUILD_EXECUTION.json'), 'commands': 5,
                     'archived_actual_terminal_builds': 2, 'new_builds_by_auditor': 0})
    return {'complete_terminal_manifest_entries': len(terminal_manifest), 'builds': build_records,
            'host_runtime_limit': rec['environment_boundary']}


def check_initial_artifact_history():
    folder = BATCH/'qa/p207_b_artifact_audit'
    # The seven-entry original seal remains a historical seal. Its later
    # supplement has a distinct manifest, so no false full-live seal claim.
    old = manifest(folder/'SHA256SUMS', folder)
    require(len(old) == 7, 'initial_artifact_history', 'exact preserved initial seven-file seal')
    supplemental = manifest(folder/'SUPPLEMENT_PINS.sha256', folder)
    require(set(supplemental) == {'PACKAGING_SUPPLEMENT.md', 'PACKAGING_CORRECTION.actual.json',
                                  'attempt_03.stdout.exact.json'},
            'initial_artifact_history', 'exact separately sealed packaging correction')
    initial_set = set(old) | {'SHA256SUMS'} | set(supplemental) | {'SUPPLEMENT_PINS.sha256'}
    require(physical(folder) == initial_set, 'initial_artifact_history', 'complete union of old seal and disclosed supplement')
    serialized = read(folder/'attempt_03.stdout.json')
    exact = read(folder/'attempt_03.stdout.exact.json')
    actual = parsed(folder/'attempt_03.actual.json')
    require(len(exact) == actual['output_chars'] == 147133 and len(serialized) == 147134
            and serialized == exact+b'\n', 'initial_artifact_history', 'exact one-LF archival distinction')
    correction = parsed(folder/'PACKAGING_CORRECTION.actual.json')
    require(correction['status'] == 'EXACT_STDOUT_PACKAGING_CORRECTION_VERIFIED' and
            correction['roundtrip_exit_code'] == 0 and correction['recovered_stdout_equals_retained_actual_tool_output']
            and correction['original_is_ascii'] and correction['closed_original_preserved'],
            'initial_artifact_history', 'actual retained-stdout recovery receipt')
    require(digest(folder/'attempt_03.stdout.exact.json') == correction['recovered_exact_sha256'] and
            digest(folder/'attempt_03.stdout.json') == correction['closed_original_sha256'],
            'initial_artifact_history', 'both exact byte hashes, not parsed normalization')
    inspected = json.loads(exact)
    require(inspected == json.loads(serialized) and inspected['checks'] == 39623 and
            inspected['status'] == 'INITIAL_ARTIFACT_MINOR_FINDING_REQUIRES_DOCUMENTARY_DELTA',
            'initial_artifact_history', 'original open finding never relabelled clean PASS')
    require(actual['exit_code'] == 0 and inspected['new_mathematical_producer_executions'] == 0
            and inspected['new_builds'] == 0 and inspected['new_visual_reviews'] == 0,
            'initial_artifact_history', 'artifact-only actual command, not numerical/build/view runs')
    require(len(inspected['all_consumed_inputs_before_after']) == 599,
            'initial_artifact_history', 'complete recorded point-in-time read set')
    for name, wanted in inspected['all_consumed_inputs_before_after'].items():
        path = Path(name) if Path(name).is_absolute() else workspace_target(name)
        # The changed in-progress B delta helper was physically preserved as
        # an exact additional initial alias; no five-path exemption is used.
        path = historical(path, 'b')
        check_info(path, wanted, 'initial_artifact_history')
    expected_outside_initial = ['DELTA_INTAKE_CHECKS.json', 'FINDINGS.initial.json', 'REPORT.initial.md',
                                'SHA256SUMS.initial', 'check_delta_artifacts.py']
    require(inspected['concurrent_delta_additions_explicitly_excluded_from_initial_scope'] == expected_outside_initial,
            'initial_artifact_history', 'exact documented phase-transition boundary')
    require([f['id'] for f in inspected['artifact_findings']] == ['P207-B-ART1'] and
            inspected['artifact_findings'][0]['status'] == 'OPEN_ON_EXACT_INITIAL_PACKAGE',
            'initial_artifact_history', 'genuine initial Minor evidence finding preserved')
    for attempt in (1, 2):
        failed = parsed(folder/f'attempt_0{attempt}.actual.json')
        require(failed['exit_code'] == 1 and 'AssertionError' in failed['output'],
                'initial_artifact_history', ('preserved actual stopped attempt', attempt))
        source = read(folder/f'check_initial.attempt_0{attempt}.py')
        require(source.endswith(b'\n\n'), 'initial_artifact_history', ('disclosed content snapshot transport LF', attempt))
    require(read(folder/'check_initial.py').endswith(b'\n') and
            not read(folder/'check_initial.py').endswith(b'\n\n'),
            'initial_artifact_history', 'final executed checker unchanged, one final LF')
    read(BATCH/'qa/P207_B_INITIAL_ARTIFACT_AUDIT.md')
    return {'original_status': inspected['status'], 'archived_checks': inspected['checks'],
            'all_historical_read_referents_checked': 599, 'exact_stdout_bytes': len(exact),
            'serialized_archival_bytes': len(serialized), 'corrected_raw_vs_serialized_boundary': True}


def check_page_views_and_links():
    views = parsed(FINAL/'PAGE_VIEWS.json')
    require(views['pdf_sha256'] == digest(PAPER/'main.pdf'), 'final_page_views', 'attested exact final PDF')
    require([page['number'] for page in views['pages']] == list(range(1, 8)),
            'final_page_views', 'all seven final pages, once each')
    page_paths = set()
    for page in views['pages']:
        path = Path(page['path'])
        require(not path.is_absolute() and '..' not in path.parts and str(path) not in page_paths,
                'final_page_views', ('safe unique page path', page['number']))
        page_paths.add(str(path))
        require(page['actually_viewed'] is True and type(page['inspection']) is str and bool(page['inspection'].strip()),
                'final_page_views', ('actual substantive attestation, not PNG existence', page['number']))
        require(digest(FINAL/path) == page['sha256'], 'final_page_views', ('actual inspected image bytes', page['number']))
    page4 = views['pages'][3]['inspection']
    require('1038' in page4 and ('underfull' in page4.lower() or 'vbox' in page4.lower()),
            'final_page_views', 'affected page-4 spacing diagnostic explicitly inspected')
    report = read(FINAL/'TERMINAL_BUILD_REPORT.md').decode()
    require('1038' in report and 'Underfull' in report and 'HOLD_EXTERNAL' in report,
            'final_page_views', 'terminal report honestly preserves warning and external boundary')
    links = []
    for folder in (PAPER, A, B):
        for doc in sorted(folder.rglob('*.md')):
            relative = doc.relative_to(ROOT)
            if 'source_inputs' in relative.parts:
                at = relative.parts.index('source_inputs')
                origin = ROOT.joinpath(*relative.parts[at+1:])
            else:
                origin = Path(re.sub(r'/frozen_round[012]/', '/', str(doc)))
            content = read(doc).decode()
            for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', content):
                target = target.strip('<>').split('#', 1)[0]
                if not target or re.match(r'[a-zA-Z][a-zA-Z0-9+.-]*:', target):
                    continue
                destination = origin.parent/target
                require(destination.exists(), 'local_links', (label(doc), target, label(origin)))
                links.append({'document': label(doc), 'semantic_origin': label(origin), 'target': target})
    return {'actual_final_pages_attested': 7, 'new_visual_views_by_auditor': 0,
            'page_paths': sorted(page_paths), 'local_links_checked': len(links), 'all_local_links': links}


def check_review_packages():
    result = {}
    after_names = {'a': ('AFTER_FROZEN_PINS.sha256', 'AFTER_LIVE_PINS.sha256'),
                   'b': ('INPUT_PINS.after.sha256', 'LIVE_SCIENTIFIC_PINS.after.sha256')}
    live_names = {label(PAPER/name) for name in physical(PAPER/'frozen_round0') if name != 'SHA256SUMS'}
    for letter, package, round_number, count in [('a', A, 0, 133), ('b', B, 1, 138)]:
        current = manifest(package/'SHA256SUMS', package, complete=True)
        require(len(current) == count, 'review_package', (letter, 'exact final nonself entry count'))
        initial = manifest(package/'SHA256SUMS.initial', package, family=letter)
        require(len(initial) == 118, 'review_package', (letter, 'exact original manifest count'))
        freeze = PAPER/f'frozen_round{round_number}'
        freeze_names = {label(freeze/name) for name in physical(freeze)}
        manifest(package/'INPUT_PINS.sha256', ROOT, expected_names=freeze_names)
        manifest(package/after_names[letter][0], ROOT, expected_names=freeze_names)
        manifest(package/after_names[letter][1], ROOT, expected_names=live_names)
        equal(package/'INPUT_PINS.sha256', package/after_names[letter][0], (letter, 'exact original/after freeze pins'))
        findings = parsed(package/'FINDINGS.json')
        old = parsed(package/'FINDINGS.initial.json')
        require(findings['paper'] == 'P207' and findings['round'] == letter.upper() and
                findings['input'] == f'frozen_round{round_number}' and findings['reviewer'] == REVIEWERS[letter]
                and findings['reviewer'] not in AUTHORS, 'review_acceptance', (letter, 'exact distinct nonauthor identity'))
        require(findings['accepted_delta'] is True and findings['mathematics'] == 'MATH_VALID' and
                findings['owner'] == 'OWNER_AMBER' and findings['external'] == 'HOLD_EXTERNAL',
                'review_acceptance', (letter, 'actual accepted bounded state'))
        require(findings['census']['open'] == {'critical': 0, 'major': 0, 'minor': 0},
                'review_acceptance', (letter, 'zero current findings, not erased history'))
        require(old['accepted_delta'] is False and old['findings'] == [] and
                old['census']['open'] == {'critical': 0, 'major': 0, 'minor': 0},
                'review_acceptance', (letter, 'unmodified historical initial census'))
        delta = read(package/'DELTA.md').decode()
        if letter == 'a':
            require(findings['verdict'] == 'ACCEPTED_EXACT_NO_CHANGE' and findings['findings'] == [] and
                    findings['census']['resolved'] == {'critical': 0, 'major': 0, 'minor': 0}
                    and 'ACCEPTED_EXACT_NO_CHANGE' in delta, 'review_acceptance', 'actual exact A no-change delta')
            context = manifest(A/'CONTEXT_SOURCE_PINS.sha256', ROOT)
            require(len(context) == 10, 'review_package', 'A actual ten source contexts')
            response = manifest(A/'DELTA_RESPONSE_AND_REPLAY_PINS.sha256', ROOT)
            expected = {label(REPLAYS/'p207_a_controlled'/name) for name in physical(REPLAYS/'p207_a_controlled')}
            expected.add(label(BATCH/'P207_A_RESPONSE.md'))
            require(len(response) == 34 and set(response) == expected, 'review_package', 'complete A response and root replay referents')
        else:
            require(findings['verdict'] == 'ACCEPT_EXACT_SCIENTIFIC_NO_CHANGE_WITH_DOCUMENTARY_REPAIR' and
                    findings['census']['resolved'] == {'critical': 0, 'major': 0, 'minor': 1}
                    and len(findings['findings']) == 1, 'review_acceptance', 'actual B documentary repair, no scientific delta')
            finding = findings['findings'][0]
            require(finding['id'] == 'P207-B-ART1' and finding['severity'] == 'minor' and finding['status'] == 'resolved'
                    and 'DOCUMENTARY_REPAIR' in delta, 'review_acceptance', 'ART1 explicitly resolved by same B reviewer')
            opened = parsed(B/'FINDINGS.delta_open.json')
            require(opened['census']['open'] == {'critical': 0, 'major': 0, 'minor': 1} and
                    opened['findings'][0]['id'] == finding['id'], 'review_acceptance', 'actual intermediate open finding preserved')
            equal(B/'REPORT.md', B/'REPORT.initial.md', 'B initial main report unchanged')
            context = manifest(B/'CONTEXT_PINS.sha256', ROOT)
            manifest(B/'CONTEXT_PINS.after.sha256', ROOT, expected_names=context)
            equal(B/'CONTEXT_PINS.sha256', B/'CONTEXT_PINS.after.sha256', 'B exact before/after contexts')
            require(len(context) == 144 and {label(A/name) for name in physical(A)} <= set(context),
                    'review_package', 'B all final-A objects plus contexts')
            supplemental = manifest(B/'SUPPLEMENTAL_READ_PINS.sha256', ROOT)
            manifest(B/'SUPPLEMENTAL_READ_PINS.after.sha256', ROOT, expected_names=supplemental)
            equal(B/'SUPPLEMENTAL_READ_PINS.sha256', B/'SUPPLEMENTAL_READ_PINS.after.sha256', 'B exact supplemental before/after')
            require(len(supplemental) == 7, 'review_package', 'seven source/read supplements')
            manifest(B/'PAGE_VIEW_PINS.sha256', ROOT, expected_names={label(B/f'page_views/page-{i}.png') for i in range(1, 8)})
            response = manifest(B/'RESPONSE_AND_ROOT_REPLAY_PINS.after.sha256', ROOT)
            earlier = manifest(B/'RESPONSE_AND_ROOT_REPLAY_PINS.before_packaging.sha256', ROOT)
            expected = {label(REPLAYS/'p207_b_controlled'/name) for name in physical(REPLAYS/'p207_b_controlled')}
            expected |= {label(BATCH/'qa/p207_b_artifact_audit'/name) for name in physical(BATCH/'qa/p207_b_artifact_audit')}
            expected |= {label(BATCH/name) for name in ('P207_B_RESPONSE.md', 'P207_B_RESPONSE_SUPPLEMENT.md',
                                                       'qa/replay_p207_review.py', 'qa/P207_B_INITIAL_ARTIFACT_AUDIT.md')}
            require(len(response) == 49 and set(response) == expected and len(earlier) == 45 and
                    set(earlier.items()) < set(response.items()), 'review_package', 'complete final49 and preserved45 response/replay/audit pins')
            old_report = read(B/'BUILD_REPORT.initial.md').decode()
            corrected = read(B/'BUILD_REPORT.md').decode()
            require('undefined reference, overfull or underfull box diagnostic remains' in old_report and
                    'That scan does not include `Underfull`.' in corrected and
                    r'Underfull \vbox (badness 1038)' in corrected and 'underfull box diagnostic remains' not in corrected,
                    'review_acceptance', 'specific evidence overstatement actually corrected')
        require('HOLD_EXTERNAL' in delta and 'LNR-S1' in delta and 'nonsharp' in delta,
                'review_acceptance', (letter, 'scope limitations remain explicit'))
        intake_name = 'intake/FREEZE_PIN_CHECK.json' if letter == 'a' else 'intake/REVIEW_SCOPE.md'
        for name in ('SOURCE_AND_PROOF.md', 'REPORT.md', 'BUILD_REPORT.md', intake_name):
            read(package/name)
        result[letter] = {'reviewer': findings['reviewer'], 'accepted_delta': True,
                          'final_manifest_entries': len(current), 'final_manifest_sha256': digest(package/'SHA256SUMS'),
                          'initial_manifest_entries': len(initial), 'current_open': findings['census']['open'],
                          'resolved_history': findings['census']['resolved'], 'delta_sha256': digest(package/'DELTA.md')}
    require(len(set(REVIEWERS.values())) == 2 and not AUTHORS.intersection(REVIEWERS.values()),
            'review_acceptance', 'two distinct processes, neither scientific author')
    return result


def check_review_execution_archives():
    original_inputs_a = {name for name in manifest(A/'INPUT_PINS.sha256', ROOT)}
    original_inputs_a |= {label(A/name) for name in ('verify.py', 'record_review.py', 'INPUT_PINS.sha256')}
    for attempt, numbers, size in [('initial', (0,), 15), ('pair_01', (1, 2), 22), ('pair_02', (1, 2), 22)]:
        folder = A/'execution'/attempt
        require(len(manifest(folder/'MANIFEST.sha256', folder, complete=True)) == size, 'A_archived_execution', attempt)
        before = manifest(folder/'INPUT_PINS.before.sha256', ROOT, expected_names=original_inputs_a)
        manifest(folder/'INPUT_PINS.after.sha256', ROOT, expected_names=original_inputs_a)
        equal(folder/'INPUT_PINS.before.sha256', folder/'INPUT_PINS.after.sha256', ('A original before/after bytes', attempt))
        rec = parsed(folder/'RECEIPT.json')
        require(rec['status'] == 'PASS' and rec['inputs_unchanged'] and rec['frozen_plus_own_inputs'] == len(before) == 109
                and rec['reviewer_not_mathematical_author'] is True and rec['declared_environment'] == SETTINGS,
                'A_archived_execution', (attempt, 'actual full input and runtime scope'))
        require(digest(Path(rec['python']['executable']).resolve()) == rec['python']['sha256'],
                'A_archived_execution', (attempt, 'actual original binary'))
        require([v['number'] for v in rec['numerical_runs']] == list(numbers) and
                all(v['assertions'] == COUNTS['a'] for v in rec['numerical_runs']), 'A_archived_execution', (attempt, 'actual producer census'))
        require(len(rec['commands']) == (5 if len(numbers) == 1 else 8), 'A_archived_execution', (attempt, 'exact command count'))
        for row in rec['commands']:
            require(row['exit_code'] == 0, 'recorded_exit', ('A archive', attempt))
            for stream in ('stdout', 'stderr'):
                item = row[stream]
                check_info(A/item['path'], item, 'stream_binding')
                if stream == 'stderr' or row['argv'][0] == 'cmp':
                    require(read(A/item['path']) == b'', 'empty_stream', ('A archive', attempt, item['path']))
            if row['argv'][0] == 'cmp':
                equal(Path(row['argv'][1]), Path(row['argv'][2]), ('A actual archived cmp', attempt))
        for number in numbers:
            source = folder/f'run{number}/verify.py'
            equal(source, A/'verify.py', ('A original source copy', attempt, number))
            equal(source.parent/'producer.stdout', A/'CANONICAL.json', ('A original full stdout', attempt, number))
            producers = [row for row in rec['commands'] if row['argv'] == [rec['python']['executable'], '-B', str(source)]]
            require(len(producers) == 1 and producers[0]['cwd'] == str(source.parent),
                    'A_archived_execution', (attempt, number, 'original nonisolated command, not retrofitted -I'))
        equal(folder/'CANONICAL.input.json', A/'CANONICAL.json', ('A original canonical snapshot', attempt))
        RECEIPTS.append({'path': label(folder/'RECEIPT.json'), 'commands': len(rec['commands']),
                         'archived_independent_A_runs': len(numbers), 'new_runs_by_auditor': 0})
    original_inputs_b = set(manifest(B/'INPUT_PINS.sha256', ROOT)) | set(manifest(B/'CONTEXT_PINS.sha256', ROOT))
    original_inputs_b |= {label(B/name) for name in ('verify.py', 'record_review.py', 'INPUT_PINS.sha256', 'CONTEXT_PINS.sha256')}
    for attempt, count, size in [('initial_01', 1, 15), ('pair_01', 2, 22), ('pair_02', 2, 22)]:
        folder = B/'executions'/attempt
        require(len(manifest(folder/'MANIFEST.sha256', folder, complete=True)) == size, 'B_archived_execution', attempt)
        expected = original_inputs_b | ({label(B/'CANONICAL.json')} if count == 2 else set())
        before = manifest(folder/'INPUTS.before.sha256', ROOT, expected_names=expected)
        manifest(folder/'INPUTS.after.sha256', ROOT, expected_names=expected)
        require(len(before) == (254 if count == 1 else 255), 'B_archived_execution', (attempt, 'exact full input key'))
        equal(folder/'INPUTS.before.sha256', folder/'INPUTS.after.sha256', ('B actual before/after raw pins', attempt))
        equal(folder/'CANONICAL.input.json', B/'CANONICAL.json', ('B canonical snapshot', attempt))
        rec = parsed(folder/'RECEIPT.json')
        require(rec['status'] == 'PASS' and rec['initialize'] == (count == 1), 'B_archived_execution', (attempt, 'actual initialized/canonical role'))
        flags = parsed(folder/'runtime_probe.stdout')
        require(flags['debug'] is True and flags['optimize'] == 0 and flags['isolated'] == 1 and flags['dont_write_bytecode'] == 1,
                'B_archived_execution', (attempt, 'actual -I -B probe'))
        require(digest(Path(flags['executable']).resolve()) == rec['python_binary_sha256'], 'B_archived_execution', (attempt, 'runtime binary'))
        stems = ['runtime_probe']
        for number in range(1, count+1):
            stems += [f'run{number}', f'run{number}.canonical.cmp']
            source = folder/f'run{number}_source/verify.py'
            equal(source, B/'verify.py', ('B original source copy', attempt, number))
            require(physical(source.parent) == {'verify.py'}, 'B_archived_execution', (attempt, number, 'source-only child directory'))
            equal(folder/f'run{number}.stdout', B/'CANONICAL.json', ('B original full stdout', attempt, number))
        if count == 2:
            stems.append('pair.cmp')
        stems += ['canonical_live.cmp', 'input_pins.cmp']
        commands_with_stems(folder, rec, stems, exit_field='exit_code', flat_hashes=True)
        for stem, row in zip(stems, rec['commands'], strict=True):
            if stem in ('run1', 'run2'):
                source = folder/f'{stem}_source/verify.py'
                require(row['command'] == [str(Path(flags['executable']).resolve()), '-I', '-B', str(source)]
                        and row['cwd'] == str(source.parent) and row['assertions'] == COUNTS['b'],
                        'B_archived_execution', (attempt, stem, 'exact actual child'))
        RECEIPTS.append({'path': label(folder/'RECEIPT.json'), 'commands': len(stems),
                         'archived_independent_B_runs': count, 'new_runs_by_auditor': 0})


def check_prior_artifact_and_delta_audits():
    frozen = PAPER/'frozen_round0'
    author_audit = parsed(A/'AUTHOR_ARTIFACT_AUDIT.json')
    require(author_audit['status'] == 'PASS' and author_audit['checks'] == 6562 and
            author_audit['all_physical_frozen_files'] == 106 and author_audit['author_programs_executed_or_imported'] is False,
            'prior_artifact_audits', 'A actual frozen-author audit metadata, not a new computation')
    for row in author_audit['complete_json_inventory']:
        target = frozen/row['path']
        check_info(target, row, 'prior_artifact_audits')
        value = parsed(target)
        require(leaves(value) == row['all_scalar_values_traversed'] and sorted(value) == row['top_level_keys'],
                'prior_artifact_audits', ('A full JSON inventory', row['path']))
    for row in author_audit['complete_python_ast_inventory']:
        source = read(frozen/row['path'])
        require(sha256(source).hexdigest() == row['sha256'] and len(source.decode().splitlines()) == row['lines'],
                'prior_artifact_audits', ('A whole copied-code inventory', row['path']))
        ast.parse(source)
    for row in author_audit['validated_nested_manifests']:
        target = frozen/row['path']
        require(digest(target) == row['sha256'], 'prior_artifact_audits', ('A nested seal', row['path']))
    for row in author_audit['author_receipts']:
        target = frozen/'author_replay'/row['attempt']/'RECEIPT.json'
        require(digest(target) == row['sha256'] and row['status'] == 'PASS', 'prior_artifact_audits', ('A inspected author receipt', row['attempt']))
    audit = parsed(B/'ARTIFACT_AUDIT.json')
    require(audit['status'] == 'PASS' and audit['checks'] == 12845 and len(audit['all_input_pins_before_and_after']) == 501,
            'prior_artifact_audits', 'B separate original artifact audit dimensions')
    json_pin_map(audit['all_input_pins_before_and_after'])
    for row in audit['inventory']:
        target = workspace_target(row['path'])
        check_info(target, row, 'prior_artifact_audits')
        if 'all_json_scalar_leaves_traversed' in row:
            require(leaves(parsed(target)) == row['all_json_scalar_leaves_traversed'],
                    'prior_artifact_audits', ('B complete JSON inventory', row['path']))
    for row in audit['validated_manifests']:
        target = workspace_target(row['path'])
        family = 'a' if row['historical_a_aliases'] else None
        if family:
            base = A
        elif target.name == 'OWNED_MANIFEST.sha256':
            base = PAPER/'frozen_round1'
        elif 'author_replay' in target.parts and target.name == 'INPUT_PINS.before.sha256':
            base = target.parent/'source_inputs'
        elif target.name in {'SHA256SUMS', 'MANIFEST.sha256'}:
            base = target.parent
        else:
            base = ROOT
        require(len(manifest(target, base, family=family)) == row['entries'],
                'prior_artifact_audits', ('B prior complete seal referents', row['path']))
    execution = parsed(B/'AUDIT_EXECUTION.json')
    console = json.loads(execution['complete_stdout'])
    require(execution['exit_code'] == 0 and execution['complete_stderr'] == '' and
            execution['mathematical_producers_executed_by_this_command'] == 0 and
            console['sha256'] == digest(B/'ARTIFACT_AUDIT.json'), 'prior_artifact_audits', 'actual artifact command/bytes binding')

    # The A delta uses actual-result envelopes; do not invent the later B schema.
    delta_outputs = {}
    for path in sorted((A/'delta_checks').glob('*.json')):
        record = parsed(path)
        actual = record.get('actual_result', record)
        require(actual['exit_code'] == 0 and type(actual['output']) is str,
                'A_actual_delta', (path.name, 'actual zero-exit recorded check'))
        delta_outputs[path.name] = actual['output']
    freeze_names = [line.split('  ', 1)[1] for line in read(frozen/'SHA256SUMS').decode().splitlines()]
    require(delta_outputs['live_cmp.json'] == ''.join('raw_cmp_exit_0 '+name+'\n' for name in freeze_names),
            'A_actual_delta', 'all 105 actual raw comparisons recorded, no count-only substitution')
    controlled = json.loads(delta_outputs['root_controlled_receipt.json'])
    require(controlled['status'] == 'PASS' and controlled['full_package_snapshot_entries_checked'] == 119 and
            controlled['recorded_commands_checked'] == 14 and controlled['recorded_full_streams_checked'] == 28
            and controlled['root_pair_math_rerun_by_delta_reviewer'] is False and
            controlled['root_receipt_sha256'] == digest(REPLAYS/'p207_a_controlled/RECEIPT.json'),
            'A_actual_delta', 'actual recorded root-pair inspection, not another execution')

    # B's output binds actual read-only commands and all 727 referents. Its
    # consumed keys already name exact aliases/current versions as read.
    delta_raw = read(B/'DELTA_AUDIT.json')
    delta = json.loads(delta_raw)
    actual = parsed(B/'DELTA_AUDIT.actual.json')
    require(delta['pass'] is True and delta['checks'] == 5258 and
            delta['consumed_inputs_before'] == delta['consumed_inputs_after'] and
            len(delta['consumed_inputs_before']) == 727, 'B_actual_delta', 'actual complete stable dependency audit')
    json_pin_map(delta['consumed_inputs_before'], info_values=True)
    require(actual['exit_code'] == 0 and actual['stdout'] == 'DELTA_AUDIT.json' and
            actual['stdout_characters'] == len(delta_raw) == 396230 and delta_raw.isascii() and
            actual['complete_stdout_file_equals_actual_tool_output'] is True and actual['roundtrip_exit_code'] == 0 and
            actual['output_file_sha256'] == sha256(delta_raw).hexdigest(), 'B_actual_delta', 'actual exact stdout length/hash/roundtrip, no extra LF')
    commands = delta['actual_delta_commands']
    require(len(commands) == 23 and Counter(row['command'][0] for row in commands) ==
            {'sha256sum': 13, 'cmp': 8, 'diff': 1, 'rg': 1}, 'B_actual_delta', 'all 23 actual command roles')
    for row in commands:
        argv = row['command']
        expected_exit = 1 if argv[0] == 'diff' else 0
        require(row['exit'] == row['expected_exit'] == expected_exit and row['stderr'] == '',
                'B_actual_delta', ('actual expected outcome', argv[0]))
        if argv[0] == 'cmp':
            require(len(argv) == 3 and row['stdout'] == '', 'B_actual_delta', 'actual raw cmp, not normalized text')
            equal(Path(argv[1]), Path(argv[2]), 'B actual documentary-delta byte comparison')
        elif argv[0] == 'sha256sum':
            require(argv[1] == '-c' and len(argv) == 3, 'B_actual_delta', 'actual hash command shape')
            names = [line.split('  ', 1)[1] for line in read(Path(argv[2])).decode().splitlines()]
            require(row['stdout'] == ''.join(name+': OK\n' for name in names), 'B_actual_delta', 'all actual hash command output rows')
        elif argv[0] == 'diff':
            require(argv == ['diff', '-u', str(B/'BUILD_REPORT.initial.md'), str(B/'BUILD_REPORT.md')]
                    and '1038' in row['stdout'] and read(B/'BUILD_REPORT.initial.md') != read(B/'BUILD_REPORT.md'),
                    'B_actual_delta', 'actual expected diff exit1 is documentary change, not a hidden failure')
        else:
            require(argv == ['rg', '-n', 'Underfull|Overfull|undefined|Warning', str(B/'cold_build_01/main.log'),
                             str(B/'cold_build_01/pass3.stdout')] and len(row['stdout'].splitlines()) == 2
                    and all('Underfull' in line and '1038' in line for line in row['stdout'].splitlines()),
                    'B_actual_delta', 'actual direct two-file diagnostic output')
    stopped = parsed(B/'DELTA_AUDIT.attempt_01.actual.json')
    require(stopped['exit_code'] == 1 and 'utility completion role differs' in stopped['output'],
            'B_actual_delta', 'genuine packaging stop retained')
    read(B/'check_delta_artifacts.attempt_01.py')
    root_actual = parsed(BATCH/'qa/P207_B_ROOT_DELTA_PINS.actual.json')
    require(root_actual['exit_code'] == 0, 'B_root_delta', 'actual final root delta check')
    root_rows = [json.loads(line) for line in root_actual['output'].splitlines()]
    require(len(root_rows) == 2 and root_rows[0]['manifest_entries'] == 138 and
            root_rows[0]['manifest_sha256'] == digest(B/'SHA256SUMS') and
            root_rows[0]['delta_sha256'] == digest(B/'DELTA.md') and
            root_rows[0]['archived_delta_consumed_objects_currently_verified'] == 727,
            'B_root_delta', 'actual final root manifest/delta/full-referent result')
    for command in root_rows[1]['pin_commands']:
        require(command['exit'] == 0 and command['stderr'] == '', 'B_root_delta', command['name'])
        names = [line.split('  ', 1)[1] for line in read(B/command['name']).decode().splitlines()]
        require(command['stdout'] == ''.join(name+': OK\n' for name in names), 'B_root_delta', 'complete recorded pin output')
    RECEIPTS.append({'path': label(B/'DELTA_AUDIT.actual.json'), 'commands': 23, 'artifact_checks': 5258,
                     'consumed_objects': 727, 'new_mathematical_build_or_view_executions': 0})
    return {'A_archived_artifact_checks': 6562, 'B_archived_artifact_checks': 12845,
            'B_delta_checks': 5258, 'B_delta_referents': 727, 'B_delta_expected_diff_exit': 1}


def check_canonical_coverage():
    values = {}
    result = {}
    for role, base in [('author', PAPER), ('a', A), ('b', B)]:
        imports = {'collections', 'hashlib', 'itertools', 'json'}
        if role == 'b':
            imports |= {'fractions', 'sys'}
        producer = inspect_producer(base/'verify.py', imports, author=(role == 'author'))
        raw = read(base/'CANONICAL.json')
        value = json.loads(raw)
        require(value['status'] == 'PASS' and value['assertions'] == COUNTS[role],
                'canonical_coverage', (role, 'actual archived result/census'))
        require(raw == (json.dumps(value, sort_keys=True, indent=2)+'\n').encode(),
                'canonical_coverage', (role, 'complete canonical producer format with exact final LF'))
        if role != 'b':
            require(sum(value['assertions_by_section'].values()) == COUNTS[role],
                    'canonical_coverage', (role, 'full section count sum'))
        values[role] = value
        result[role] = {'assertions_per_archived_run': COUNTS[role], 'bytes': len(raw),
                        'sha256': sha256(raw).hexdigest(), 'scalar_leaves_traversed': leaves(value),
                        'top_level_keys': sorted(value), 'producer': producer}
    author, a, b = values['author'], values['a'], values['b']
    original = author['local_growth_certificate']
    exceptions = original['complete_inner_exception_and_extension_certificate']
    require(len(exceptions) == 204 and len({tuple(row['inner_word']) for row in exceptions}) == 204,
            'canonical_coverage', 'all 204 unique stored author inner exceptions')
    for row in exceptions:
        require(len(row['inner_word']) == 11 and set(row['inner_word']) <= {0, 1, 2},
                'certificate_record_shape', 'inner word shape')
        extensions = row['all_nine_extensions_left_right_time_site']
        require(len(extensions) == 9 and {tuple(v[:2]) for v in extensions} == {(i, j) for i in range(3) for j in range(3)},
                'certificate_record_shape', 'all nine distinct outer extensions retained')
        for left, right, time, site in extensions:
            require(1 <= time <= 4 and abs(site) <= 5-time, 'certificate_record_shape', 'stored witness bounds, not recomputation')
    require(original['inner_case_counts'] == {'center_equal': 158643, 'inner_witness': 18300, 'needs_outer_letters': 204},
            'canonical_coverage', 'all 177147 author inner cases retained')
    alocal = a['local_certificate']
    blocal = b['local_sign_lift_certificate']
    census = blocal['census']
    require(alocal['enumerated_complete_words'] == census['height_lifts'] == 3**13 and
            alocal['equal_centers'] == census['equal_height_lifts'] and
            alocal['unequal_centers_with_witness'] == census['changed_height_lifts'],
            'canonical_coverage', 'complete shared local-height census, independent representation records')
    changed = blocal['changed_sign_classes']
    require(len(changed) == census['changed_classes'] == 20115 and
            len({row[0] for row in changed}) == len(changed) and
            sum(row[1] for row in changed) == census['changed_height_lifts'],
            'canonical_coverage', 'all changed sign-lift records retained, not count-only output')
    for sign_word, weight, time, site in changed:
        require(len(sign_word) == 12 and set(sign_word) <= set('012') and type(weight) is int and weight > 0
                and 1 <= time <= 4 and abs(site) <= 5-time, 'certificate_record_shape', sign_word)
    require(census['sign_words'] == 3**12 and census['realizable']+census['unrealizable'] == 3**12 and
            census['equal_classes']+census['changed_classes'] == census['realizable'] and
            census['equal_height_lifts']+census['changed_height_lifts'] == 3**13,
            'canonical_coverage', 'complete sign/lift partition consistency')
    bgraph = b['two_time_column_pair_graph']
    agraph = a['independent_overlap_core_graph']
    require(len(bgraph['columns']) == 6 and len(bgraph['vertices']) == 36 and len(bgraph['allowed_triples']) == 45
            and len(bgraph['integer_determinant_samples_z0_to36']) == 37
            and len(bgraph['determinant_coefficients_degree0_to36']) == 37
            and len(bgraph['closed_walk_traces_1_to60']) == 60
            and len(agraph['vertices_four_heights']) == 81
            and len(agraph['det_I_minus_zR_coefficients_all_82']) == 82
            and len(agraph['trace_exponents_1_to_81']) == 81,
            'canonical_coverage', 'all representation/determinant coefficient and trace slots retained')
    for i, row in enumerate(author['core_certificate']['traces_n1_to_60']):
        require(row['all_core_points'] == agraph['trace_exponents_1_to_81'][i] == bgraph['closed_walk_traces_1_to60'][i],
                'canonical_cross_records', ('all 60 common traces', i+1))
    oboxes, aboxes, bboxes = author['complete_cyclic_source_target_boxes'], a['complete_cyclic_boxes'], b['source_pair_inverse_and_time_filtration']['boxes']
    for boxes in (oboxes, aboxes, bboxes):
        require([row['n'] for row in boxes] == list(range(3, 11)), 'canonical_coverage', 'every original full cyclic box')
    for o, ar, br in zip(oboxes, aboxes, bboxes, strict=True):
        for ok, ak, bk in [('n', 'n', 'n'), ('image_points', 'image_points', 'image'), ('core_points', 'core_points', 'core'),
                           ('maximum_fibre', 'maximum_fibre', 'max_fibre'), ('all_labelled_maximizers', 'all_labelled_maximizers', 'all_maximizers'),
                           ('successor_index_vector_sha256', 'successor_vector_sha256', 'successor_sha256'),
                           ('observed_sharp_height_in_this_complete_box', 'observed_height_not_all_n_formula', 'max_height')]:
            require(o[ok] == ar[ak] == br[bk], 'canonical_cross_records', (br['n'], ok))
        require(br['states'] == ar['sources_targets_sign_words_each'] == 3**br['n'] and sum(br['height_distribution']) == br['states'],
                'canonical_cross_records', (br['n'], 'full source/target and depth totals'))
        require(o['depth_histogram'] == ar['exact_depth_histogram'] == list(map(list, enumerate(br['height_distribution']))) and
                o['target_fibre_histogram_including_empty'] == ar['fibre_size_histogram_including_empty'],
                'canonical_cross_records', (br['n'], 'all shared depth/fibre bins'))
        for key in ('successor_sha256', 'fibre_counts_sha256', 'every_labelled_inverse_set_sha256'):
            require(re.fullmatch('[0-9a-f]{64}', br[key]) is not None, 'canonical_coverage', (br['n'], key))
    require(sum(row['states'] for row in bboxes) == 88560, 'canonical_coverage', 'each complete labelled source/target union')
    for rows in (author['single_seed_only_checks'], a['seed_only_n4_to_64'], b['single_seed_witnesses']):
        require([row['n'] for row in rows] == list(range(4, 65)), 'canonical_coverage', 'all 61 seed-only rows, no bigger complete carrier')
    for o, ar, br in zip(author['single_seed_only_checks'], a['seed_only_n4_to_64'], b['single_seed_witnesses'], strict=True):
        require((o['single_seed_hitting_time'], o['one_hole_source_hitting_time']) ==
                (ar['seed_entrance'], ar['source_entrance']) == (br['seed20_height'], br['seed01_height']),
                'canonical_cross_records', ('all seed clocks', br['n']))
    require([r['length'] for r in b['positive_kernels']['census']] == list(range(1, 7)) and
            [r['length'] for r in b['mixed_matrix_pressure']] == list(range(2, 11)) and
            [r['n'] for r in b['deducted_independent_set_attainers']] == [4, 6, 8, 10],
            'canonical_coverage', 'all local/matrix/classical fixed bounds')
    for o, br in zip(author['mixed_kernel_checks']['matrix_word_boxes'], b['mixed_matrix_pressure'], strict=True):
        require(o['length'] == br['length'] and sum(v[-1] for v in o['by_B_count_J_count_equality']) == br['words'] == 3**br['length']
                and sum(v[-1] for v in br['class_counts']) == br['words'],
                'canonical_cross_records', ('whole matrix-word census', br['length']))
    return result


def check_postbuild_runtime_style():
    rec = parsed(FINAL/'POSTBUILD_RUNTIME_STYLE.json')
    require(rec['kind'] == 'ACTUAL_POST_BUILD_STYLE_AND_RUNTIME_SNAPSHOT_NOT_PREBUILD_OR_HERMETIC' and
            len(rec['commands']) == 4 and len(rec['postbuild_files']) == 4,
            'postbuild_style', 'explicit separate post-build, not pre-build or hermetic receipt')
    expected_commands = [['kpsewhich', 'plainnat.bst'], ['pdflatex', '--version'], ['bibtex', '--version'], ['pdftoppm', '-v']]
    for row, command in zip(rec['commands'], expected_commands, strict=True):
        require(row['command'] == command and row['exit'] == 0, 'postbuild_style', command)
        if command[0] != 'pdftoppm':
            require(row['stderr'] == '', 'postbuild_style', ('empty ordinary command stderr', command))
        else:
            require(row['stdout'] == '' and 'pdftoppm version' in row['stderr'],
                    'postbuild_style', 'renderer version is normally on stderr, not a failure')
    style = rec['commands'][0]['stdout'].strip()
    require(style == '/usr/share/texlive/texmf-dist/bibtex/bst/natbib/plainnat.bst' and
            set(rec['postbuild_files']) == {style, '/usr/bin/bibtex.original', '/usr/bin/pdftex', '/usr/bin/pdftoppm'},
            'postbuild_style', 'exact located bibliography style and resolved runtime binaries')
    for name, wanted in rec['postbuild_files'].items():
        check_info(Path(name), wanted, 'postbuild_style')
    require(rec['commands'][1]['stdout'].encode() == read(FINAL/'cold_build_1/ENGINE.txt') and
            rec['commands'][2]['stdout'].encode() == read(FINAL/'cold_build_1/BIBTEX_ENGINE.txt'),
            'postbuild_style', 'post-build engine versions agree with actual build record')
    return {'files': len(rec['postbuild_files']), 'actual_commands': 4, 'boundary': rec['boundary']}


def main():
    require(len(sys.argv) == 1 and __debug__ and sys.flags.optimize == 0 and sys.flags.isolated == 1,
            'auditor_invocation', 'exact no-argument isolated assertion-enabled artifact check')
    started = datetime.now(timezone.utc).isoformat()
    source_hash = digest(Path(__file__).resolve())
    whole_paper = manifest(PAPER/'SHA256SUMS', PAPER, complete=True)
    require(len(whole_paper) == 614, 'whole_paper_closure', 'complete held pre-acceptance paper artifact seal')
    freezes = check_freezes()
    reviews = check_review_packages()
    canonicals = check_canonical_coverage()
    author = check_author_archive()
    check_root_author()
    check_review_execution_archives()
    check_root_review('a', controlled=False)
    check_root_review('a', controlled=True)
    check_root_review('b', controlled=True)
    initial = check_initial_artifact_history()
    artifact_history = check_prior_artifact_and_delta_audits()
    builds = check_terminal_builds()
    runtime = check_postbuild_runtime_style()
    views = check_page_views_and_links()
    status = read(PAPER/'PAPER_STATUS.md').decode()
    require('P207' in status and 'HOLD_EXTERNAL' in status, 'lifecycle_boundary', 'paper status preserves identity/external hold')
    # Snapshot every actually read artifact/dependency only after collection,
    # then verify all bytes and any host-path symlink resolution again.
    before = dict(READS)
    for name, wanted in before.items():
        path = Path(name) if Path(name).is_absolute() else ROOT/name
        raw = path.read_bytes()
        require(wanted == {'bytes': len(raw), 'sha256': sha256(raw).hexdigest()},
                'final_full_dependency_recheck', name)
    for name, target in HOST_SYMLINKS.items():
        require(str(Path(name).resolve(strict=True)) == target, 'final_host_alias_recheck', name)
    result = {'paper': 'P207', 'status': 'PASS_P207_TERMINAL_ARTIFACT_GATE',
              'started_utc': started, 'ended_utc': datetime.now(timezone.utc).isoformat(),
              'auditor_sha256': source_hash, 'checks': sum(CHECKS.values()), 'checks_by_section': dict(CHECKS),
              'whole_paper_manifest_entries': len(whole_paper),
              'fresh_mathematical_executions': 0, 'fresh_builds': 0, 'fresh_page_views': 0,
              'role': 'Artifact gate only; no new proof, manuscript review, delta acceptance or external clearance.',
              'frozen_rounds': freezes, 'accepted_reviews': reviews, 'complete_canonicals': canonicals,
              'author_original_evidence': author, 'actual_archived_receipts': RECEIPTS,
              'initial_artifact_finding_and_packaging_history': initial,
              'prior_artifact_and_delta_audits': artifact_history, 'terminal_builds': builds,
              'postbuild_style_and_runtime': runtime, 'actual_final_page_attestations_and_links': views,
              'validated_manifests': MANIFESTS, 'explicit_historical_aliases_used': ALIASES_USED,
              'contemporaneous_host_symlink_resolutions': HOST_SYMLINKS,
              'all_consumed_input_count': len(before), 'all_consumed_inputs_rechecked': before,
              'limits': ['Root original proof/source assessment remains controlling; no all-parameter theorem is proved here.',
                         'Prior actual root author/A/B pairs are reused under checked recorded dependencies, not rerun by this auditor.',
                         'The original author/A nonisolated runtime records are preserved; controlled root A/B probes are separate.',
                         'Historical host stdlib/libraries are not a hermetic snapshot; terminal host/style pins are explicitly post-build.',
                         'Seven actual root final-page attestations are validated; image hashes are not new viewing.',
                         'The resolved B underfull-report finding and earlier artifact/packaging stops remain preserved.',
                         'No scientific producer/build/view/source dependency may be changed without affected new checks.',
                         'Only P207 is checked; exactly five retained papers and batch terminal completion are not asserted.'],
              'owner': 'OWNER_AMBER', 'external_status': 'HOLD_EXTERNAL'}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
