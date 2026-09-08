#!/usr/bin/env python3
"""P210 terminal source-only build revision 02; corrected actual list schema.

Disclosed reduction of the fully read accepted four-build infrastructure.
No old program is imported or executed. Exact actual B/root-pair/delta and
physical-Round2 originals are checked before qa_final or any child command.
Only the separately sealed, root-read final preparation may be launched.
"""
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import sysconfig
import time
import traceback

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
PREP = QA / 'p210_terminal_build_revision_02'
SCRIPT = PREP / 'build_p210.py'
PAPER = ROOT / 'papers/210-weakly-increasing-run-aggregation'
SOURCE_NAMES = ('main.tex', 'math_commands.tex', 'references.bib',
    'sections/0_abstract.tex', 'sections/1_introduction.tex', 'sections/2_clock.tex',
    'sections/3_image.tex', 'sections/4_coding.tex', 'sections/5_fibres.tex', 'sections/6_scope.tex')
PYTHON = Path('/usr/bin/python3.10')
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C', 'LC_ALL': 'C', 'TZ': 'UTC',
       'SOURCE_DATE_EPOCH': '1704067200', 'FORCE_SOURCE_DATE': '1',
       'openin_any': 'p', 'openout_any': 'p'}
TOOLS = [Path('/usr/bin') / n for n in ('pdflatex', 'bibtex', 'kpsewhich',
         'pdfinfo', 'pdffonts', 'pdftotext', 'pdftoppm', 'ldd', 'cmp', 'env')]
TOOLS += [PYTHON, Path('/bin/bash'), Path('/bin/sh')]
STDLIB = Path('/usr/lib/python3.10')
TEX_ROOTS = tuple(map(Path, ('/usr/share/texlive/texmf-dist', '/usr/share/texmf',
    '/var/lib/texmf', '/etc/texmf', '/usr/local/share/texmf', '/root/texmf',
    '/root/.texlive2021/texmf-config', '/root/.texlive2021/texmf-var')))
LIB_ROOTS = tuple(map(Path, ('/usr/lib/x86_64-linux-gnu', '/usr/lib64', '/usr/local/lib')))
CONFIG_ROOTS = tuple(map(Path, ('/etc/ld.so.conf.d', '/usr/share/fonts', '/etc/fonts',
    '/var/cache/fontconfig', '/usr/share/fontconfig', '/usr/lib/locale/C.utf8',
    '/usr/lib/x86_64-linux-gnu/gconv', '/usr/lib/gconv', '/usr/share/poppler',
    '/usr/local/share/fonts', '/etc/xdg/fontconfig', '/etc/profile.d', '/root/.fonts',
    '/root/.fontconfig', '/root/.fonts.conf.d', '/root/.config/fontconfig',
    '/root/.cache/fontconfig', '/root/.local/share/fonts')))
USER_VARS = ('TEXMFHOME', 'TEXMFCONFIG', 'TEXMFVAR')


def require(condition, label):
    if not condition:
        raise RuntimeError(label)


def pin(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(chunk)
    return {'sha256': h.hexdigest(), 'bytes': Path(path).stat().st_size}


def save(path, value):
    raw = value if isinstance(value, bytes) else (json.dumps(value, sort_keys=True, indent=2) + '\n').encode()
    with Path(path).open('xb') as stream:
        stream.write(raw)


def save_ledger(path, value):
    raw = (json.dumps(value, sort_keys=True, indent=2) + '\n').encode()
    compressed = gzip.compress(raw, mtime=0)
    require(gzip.decompress(compressed) == raw, 'Lossless ledger compression')
    save(path, compressed)
    save(path.with_name(path.name + '.meta.json'), {
        'encoding': 'gzip of exact UTF-8 JSON with terminal LF; mtime=0',
        'json_bytes': len(raw), 'json_sha256': hashlib.sha256(raw).hexdigest(),
        'compressed': pin(path), 'semantic_groups': {k: len(v) for k, v in value.items()}})


def manifest(base, expected_sha, expected_count=None):
    require(base.resolve() == base and not base.is_symlink(), 'Aliased manifest root')
    seal = base / 'SHA256SUMS'
    require(pin(seal)['sha256'] == expected_sha, 'Manifest identity changed: ' + str(base))
    result = {}
    for row in seal.read_text().splitlines():
        digest, name = row.split('  ', 1)
        relative, path = Path(name), base / name
        require(re.fullmatch('[0-9a-f]{64}', digest) and relative.as_posix() == name and
                relative.parts and not relative.is_absolute() and '..' not in relative.parts and
                name != 'SHA256SUMS' and str(path) not in result, 'Unsafe or duplicate manifest entry')
        require(path.resolve() == path and not path.is_symlink() and pin(path)['sha256'] == digest,
                'Manifest payload changed: ' + str(path))
        result[str(path)] = pin(path)
    entries = list(base.rglob('*'))
    require(not any(p.is_symlink() for p in entries), 'Symlink in sealed package')
    require(set(result) == {str(p) for p in entries if p.is_file() and p != seal}, 'Incomplete manifest')
    require(expected_count is None or len(result) == expected_count, 'Manifest count changed')
    return {**result, str(seal): pin(seal)}


def final_schema_binding(recipe):
    """Bind actual accepted originals only; no old code or host-ledger execution.

    Root's B and physical-Round2 gates are semantic inputs, not replacements
    for the later full terminal artifact inspector. All bytes consumed here
    enter required_input_pins. Prior lifecycle/whole roles have exactly two
    physical Round2 anchors; current preterminal controls are pinned separately.
    """
    require(recipe['schema'] == 'p210-terminal-build-actual-bound-contract-v1' and
            recipe['stage'] == 'ACTUAL_B_ROOT_DELTA_PHYSICAL_ROUND2_BOUND_NOT_EXECUTED',
            'Exact actual-bound contract, not an unbound or caller boolean gate')
    binding = recipe['final_schema_binding']
    specs, roles, required = binding['manifests'], binding['roles'], {}
    expected_packages = {
        'b_review': (QA.parent / 'reviews/p210_b', 441),
        'b_pair': (QA / 'root_replays/p210_b_strict_pair_01', 59),
        'round1': (PAPER / 'frozen_round1', 508),
        'round2': (PAPER / 'frozen_round2', 524),
        'round2_preparation': (QA / 'p210_round2_preparation', 11),
        'round2_reception': (QA / 'p210_round2_root_reception', 1),
        'b_final_preparation': (QA / 'p210_b_final_reception_preparation', 12),
        'b_strict_preparation': (QA / 'p210_b_strict_preparation', 4)}
    require(set(specs) == set(expected_packages), 'Exact eight actual package roles')
    for role, (base, count) in expected_packages.items():
        spec = specs[role]
        require(spec['path'] == str(base) and spec['payloads'] == count and
                pin(base / 'SHA256SUMS') == spec['seal'], 'Actual package role identity')
        required.update(manifest(base, spec['seal']['sha256'], count))
    for role, value in roles.items():
        path = Path(value['path'])
        expected = {k: value[k] for k in ('sha256', 'bytes')}
        require(path.is_absolute() and path.resolve() == path and not path.is_symlink() and
                pin(path) == expected, 'Actual named original changed: ' + role)
        require(str(path) not in required or required[str(path)] == expected, 'Conflicting original roles')
        required[str(path)] = expected

    def raw(role):
        return Path(roles[role]['path']).read_bytes()

    def data(role):
        return json.loads(raw(role))

    def digest(role):
        return roles[role]['sha256']

    def native(role, expected_status):
        launch, completion = data(role + '_launch'), data(role + '_completion')
        require(completion['launch_record'] == Path(roles[role + '_launch']['path']).name and
                completion['session_id'] == launch['result']['session_id'] and
                launch['result']['output'] == '' and type(completion['result']['exit_code']) is int and
                completion['result']['exit_code'] == 0, 'Actual native session/exit chain: ' + role)
        output = json.loads(completion['result']['output'])
        require(output['status'] == expected_status, 'Actual native result status: ' + role)
        # Outer tool output is not a separately captured stderr field.
        # Missing old cwd/start/stderr/group fields are never retrospectively filled.
        return output

    root_b, current = data('root_b'), data('b_current')
    require(root_b['schema'] == 'p210-b-root-delta-closure-v1' and
            root_b['status'] == 'ROOT_ACCEPTED_B_DELTA_ORIGINAL_CLOSURE_PASS' and
            root_b['paper'] == 'P210' and root_b['input_round'] == 1 and
            root_b['reviewer'] == current['reviewer'] == '/root/p210_b_reviewer' and
            root_b['reviewer_delta_accepted'] is True and root_b['root_original_inspection_complete'] is True and
            root_b['root_replay_closure_complete'] is True and root_b['current_open_findings'] == 0,
            'Actual same-B accepted root delta closure')
    require(current['phase'] == 'ACCEPTED_EXACT_NOCHANGE_DELTA' and current['verdict'] == 'PASS_NARROW' and
            current['accepted_delta'] is True and current['same_actual_initial_reviewer'] is True and
            current['current_open_counts'] == {'Critical': 0, 'Major': 0, 'Minor': 0} and
            current['current_manuscript_findings'] == [] and current['initial_findings_unchanged'] is True and
            current['reviewer_infrastructure_resolved_counts'] == {'Critical': 0, 'Major': 0, 'Minor': 2} and
            current['inherited_A_findings']['resolved_Major'] == 1 and
            len(current['reviewer_infrastructure_findings']) == 2 and
            all(v['status'] == 'RESOLVED_BEFORE_INITIAL_SEAL' and v['failed_evidence_preserved'] is True
                for v in current['reviewer_infrastructure_findings']), 'Zero-open narrow decision; retain failures')
    for field, role in (('delta_sha256', 'b_delta'), ('current_findings_sha256', 'b_current'),
                        ('findings_sha256', 'b_findings'), ('response_sha256', 'b_response'),
                        ('author_manifest_sha256', 'author_manifest'),
                        ('prior_lifecycle_sha256', 'prior_lifecycle'), ('prior_whole_manifest_sha256', 'prior_whole')):
        require(root_b[field] == digest(role), 'Root B exact documentary binding: ' + field)
    for field, role in (('review_manifest_sha256', 'b_review'), ('root_pair_manifest_sha256', 'b_pair'),
                        ('round1_manifest_sha256', 'round1')):
        require(root_b[field] == specs[role]['seal']['sha256'], 'Root B package binding')
    require(root_b['review_manifest_entries'] == 441 and root_b['initial_review_payloads_preserved'] == 407 and
            root_b['unchanged_in_place_initial_payloads'] == 406 and root_b['unchanged_author_payloads'] == 489 and
            root_b['unchanged_round1_payloads'] == 508 and root_b['resolved_B_infrastructure_minor'] == 2 and
            root_b['resolved_inherited_A_major'] == 1 and current['initial_payloads_preserved'] == 407 and
            current['accepted_response_sha256'] == digest('b_response') and
            current['initial_findings_sha256'] == digest('b_findings'), 'Preserved exact initial/history census')
    for name, expected in root_b['evidence'].items():
        require(name in required and required[name]['sha256'] == expected, 'Complete actual root B evidence keys')
    review = Path(specs['b_review']['path'])
    aliases = {str(review / name): {'physical': roles[role]['path'], 'sha256': digest(role)}
               for name, role in (('DELTA.md', 'b_initial_delta'), ('SHA256SUMS', 'b_initial_manifest'))}
    require(root_b['initial_review_aliases'] == aliases, 'Only exact two historical B roles')
    initial_rows = raw('b_initial_manifest').decode().splitlines()
    require(len(initial_rows) == 407, 'Actual initial 407 manifest')
    for row in initial_rows:
        expected, name = row.split('  ', 1)
        path = Path(roles['b_initial_delta']['path']) if name == 'DELTA.md' else review / name
        require(str(path) in required and required[str(path)]['sha256'] == expected, 'Preserved initial B bytes')
    strict = native('b_strict', 'PASS_ROOT_P210_B_STRICT_PAIR')
    require(strict['role'] == 'p210_b' and strict['checks_each'] == [51129, 51129] and
            strict['command_count'] == 10 and strict['known_inputs'] == 3558 and strict['errors'] == [] and
            strict['closure'] == {'manifest': specs['b_pair']['seal'], 'payloads': 59}, 'Actual strict pair closure')
    strict_receive = native('b_strict_reception', 'PASS_ROOT_P210_B_STRICT_PAIR_ORIGINAL_RECEPTION_REVISION_01')
    require(strict_receive['schema'] == 'p210-B-strict-actual-root-receiver-revision-01' and
            strict_receive['pair_manifest'] == specs['b_pair']['seal'] and strict_receive['pair_payloads'] == 59 and
            strict_receive['full_recorded_native_commands'] == 10 and strict_receive['known_inputs'] == 3558 and
            strict_receive['physical_read_paths_rechecked'] == 3633 and
            strict_receive['all_3558_actual_rich_keys_rechecked'] is True and
            strict_receive['all_native_argv_and_timeout_reconstructed'] is True, 'Actual root strict original reception')
    final_b = native('b_final', 'PASS_ROOT_P210_B_FINAL_SAME_REVIEWER_DELTA_AND_ORIGINAL_RECEPTION')
    require(final_b['schema'] == 'p210-B-final-root-original-receiver-v1' and
            final_b['B_final_manifest'] == specs['b_review']['seal'] and final_b['B_final_payloads'] == 441 and
            final_b['accepted_same_reviewer_delta'] is True and final_b['current_open'] == current['current_open_counts'] and
            final_b['exact_two_historical_aliases'] == aliases and final_b['initial_payloads_preserved'] == 407 and
            final_b['initial_unchanged_in_place'] == 406 and final_b['phase_reception']['common_keys'] == 121013 and
            final_b['current_extra_key_count'] == 44 and final_b['physical_paths_fully_reread_twice'] == 121057 and
            final_b['complete_current_read_map_canonical_sha256'] ==
            root_b['actual_final_root_inspection']['complete_current_map_sha256'],
            'Exact actual final B reception, not a new full host-key pass')

    actual_binding, provenance = data('round2_binding'), data('round2_provenance')
    r2 = PAPER / 'frozen_round2'
    require(actual_binding['schema'] == 'p210-round2-actual-final-b-binding-v1' and
            actual_binding['status'] == 'BOUND_AFTER_ACTUAL_B_ACCEPTANCE_AND_ROOT_FINAL_CLOSURE' and
            actual_binding['bound_by'] == '/root' and actual_binding['paper'] == 'P210' and
            len(actual_binding['roles']) == 13 and len(actual_binding['selectors']) == 26 and
            provenance['schema'] == 'p210-round2-provenance-v1' and
            provenance['actual_final_b_binding'] == actual_binding and
            provenance['actual_final_b_binding_sha256'] == digest('round2_binding') and
            provenance['accepted_root_closure_sha256'] == digest('root_b') and
            provenance['round1_core_payloads_copied'] == 508 and len(provenance['core_payload_pins']) == 508 and
            provenance['acceptance_anchor_payloads'] == 14 and len(provenance['anchors']) == 14 and
            isinstance(provenance['raw_byte_comparisons'], list) and len(provenance['raw_byte_comparisons']) == 1016 and
            all(set(row) == {'bytes', 'equal', 'left', 'method', 'right', 'role'} and row['equal'] is True and
                type(row['bytes']) is int and row['bytes'] >= 0 and Path(row['left']).is_absolute() and
                Path(row['right']).is_absolute() and isinstance(row['role'], str) and
                row['method'] == 'complete Python bytes comparison; not a native cmp command'
                for row in provenance['raw_byte_comparisons']), 'Actual Round2 accepted binding and provenance')
    prior = {str(PAPER / 'ROOT_LIFECYCLE.md'): Path(roles['prior_lifecycle']['path']),
             str(PAPER / 'PAPER_MANIFEST.sha256'): Path(roles['prior_whole']['path'])}
    require(prior[str(PAPER / 'ROOT_LIFECYCLE.md')] == r2 / 'ROUND2_ACCEPTANCE/PRE_ROUND2_ROOT_LIFECYCLE.md' and
            prior[str(PAPER / 'PAPER_MANIFEST.sha256')] == r2 / 'ROUND2_ACCEPTANCE/PRE_ROUND2_PAPER_MANIFEST.sha256',
            'Exact physical historical pre-Round2 roles; never compare old keys to refreshed live documents')
    for name, anchor in provenance['anchors'].items():
        physical = r2 / anchor['physical_path']
        original = prior.get(anchor['original_path'], Path(anchor['original_path']))
        require(physical == r2 / 'ROUND2_ACCEPTANCE' / name and str(physical) in required and str(original) in required and
                required[str(physical)] == required[str(original)] and
                required[str(physical)]['sha256'] == anchor['sha256'], 'Exact physical acceptance anchor')
    freeze = native('round2_freeze', 'PASS_PHYSICAL_P210_ROUND2')
    require(freeze['manifest_sha256'] == specs['round2']['seal']['sha256'] and freeze['payloads'] == 524 and
            freeze['physical_files'] == 525 and freeze['core_payloads'] == 508 and
            freeze['acceptance_anchor_payloads'] == 14 and freeze['complete_raw_byte_comparisons'] == 1016 and
            freeze['actual_final_b_binding_sha256'] == digest('round2_binding'), 'Actual physical freeze native')
    received = native('round2_inspection', 'PASS_ROOT_PHYSICAL_P210_ROUND2_RECEPTION')
    receipt = data('round2_reception')
    require(receipt['status'] == received['status'] and receipt['checks'] == received['checks'] == 38968 and
            receipt['round2_manifest_sha256'] == received['round2_manifest_sha256'] == specs['round2']['seal']['sha256'] and
            receipt['current_input_count'] == received['current_input_count'] == 2603 and
            len(receipt['complete_input_pins']) == 2603 and receipt['full_raw_copy_comparisons'] == 523 and
            receipt['current_open_findings'] == 0 and receipt['payloads'] == 524 and receipt['physical_files'] == 525 and
            received['actual_freeze_completion_sha256'] == digest('round2_freeze_completion') and
            received['root_reception_manifest_sha256'] == specs['round2_reception']['seal']['sha256'],
            'Actual complete Round2 original reception')
    actual_commands = receipt['actual_native_commands']
    require(len(actual_commands) == received['native_commands_all_zero'] == 6, 'Six complete actual native receipts')
    bases = [PAPER / 'frozen_round1', r2, review, Path(specs['b_pair']['path']), Path(specs['round2_preparation']['path'])]
    for index, command in enumerate(actual_commands):
        require(command['exit'] == 0 and command['stderr_utf8'] == '' and command['environment'] ==
                {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'},
                'Actual Round2 native exit/environment/separate stderr')
        for stream in ('stdout', 'stderr'):
            require(hashlib.sha256(command[stream + '_utf8'].encode()).hexdigest() == command[stream + '_sha256'],
                    'Actual complete native stream bytes')
        if index < 5:
            base = bases[index]
            require(command['argv'] == ['/usr/bin/sha256sum', '--check', 'SHA256SUMS'] and
                    command['cwd'] == str(base) and command['stdout_utf8'] ==
                    ''.join(row.split('  ', 1)[1] + ': OK\n' for row in (base / 'SHA256SUMS').read_text().splitlines()),
                    'Exact complete manifest native return')
        else:
            require(command['argv'] == ['/usr/bin/cmp', str(r2 / 'AUTHOR_MANIFEST.sha256'), str(PAPER / 'AUTHOR_MANIFEST.sha256')] and
                    command['cwd'] == str(ROOT) and command['stdout_utf8'] == '' and
                    required[str(r2 / 'AUTHOR_MANIFEST.sha256')] == required[str(PAPER / 'AUTHOR_MANIFEST.sha256')],
                    'Actual original author-seal native comparison')
    metadata = data('round2_metadata')
    require(metadata['result']['exit_code'] == 0, 'Actual root full-key metadata native exit')
    measured = json.loads(metadata['result']['output'])
    require(measured['status'] == 'PASS_ROOT_ROUND2_NATIVE_ORIGINAL_FULL_INPUT_AND_SIX_RAW_RETURNS' and
            measured['actual_receiver_inputs_rehashed'] == 2603 and measured['actual_native_commands_checked'] == 6 and
            measured['actual_full_copy_comparisons'] == 523, 'Accepted actual root full-input gate')
    for name, value in measured['evidence'].items():
        require(required.get(name) == value, 'Exact root metadata evidence')

    refresh = native('lifecycle_refresh', 'PASS_P210_ROUND2_LIFECYCLE_AND_WHOLE_MANIFEST_REFRESH')
    refresh_full = data('lifecycle_refresh')
    require({k: v for k, v in refresh_full.items() if k != 'native'} == refresh and
            refresh['current_payloads'] == 2021 and refresh['physical_files'] == 2022 and
            refresh['added_round2_files'] == 525 and refresh['old_payloads'] == 1496 and
            refresh['sole_changed_old_payload'] == 'ROOT_LIFECYCLE.md' and
            refresh['new_lifecycle_sha256'] == digest('lifecycle') and refresh['new_whole_sha256'] == digest('whole') and
            refresh['old_lifecycle_sha256'] == digest('prior_lifecycle') and
            refresh['old_whole_sha256'] == digest('prior_whole') and
            refresh['round2_sha256'] == specs['round2']['seal']['sha256'], 'Actual preterminal lifecycle refresh')
    rows, native_refresh = raw('whole').decode().splitlines(), refresh_full['native']
    require(len(rows) == 2021 and native_refresh['exit'] == 0 and native_refresh['stderr'] == '' and
            native_refresh['argv'] == ['/usr/bin/sha256sum', '--check', 'PAPER_MANIFEST.sha256'] and
            native_refresh['cwd'] == str(PAPER) and native_refresh['stdout'] ==
            ''.join(row.split('  ', 1)[1] + ': OK\n' for row in rows), 'Actual complete prior rolling-manifest return')
    # Do not assert whole-tree completeness after qa_final is created. The live
    # preterminal document and manifest remain exact byte anchors throughout.
    paper = binding['papers']['P210']
    require(set(binding['papers']) == {'P210'} and paper['freeze'] == str(r2) and paper['round'] == 2 and
            paper['freeze_manifest'] == specs['round2']['seal'] and paper['freeze_payloads'] == 524,
            'Final actual physical Round2 source role')
    require(all(pin(Path(name)) == value for name, value in required.items()), 'Full consumed-key preflight reread')
    return {'status': 'BOUND_ACTUAL_P210_B_ROOT_ROUND2_PRETERMINAL_ORIGINALS',
            'papers': binding['papers'], 'required_input_pins': required,
            'scope': 'Actual B/root/Round2 semantic originals and eight complete packages; no new B host-key expansion. Preterminal lifecycle/whole byte anchors only; terminal views/artifact/paper/five gates remain.'}

def originals(recipe, preparation_sha):
    result = manifest(PREP, preparation_sha)
    # This exact actual-schema prerequisite executes before out.mkdir, host
    # inventory and all child processes; it is not a caller boolean gate.
    final = final_schema_binding(recipe)
    require(set(final['papers']) == {'P210'}, 'Only P210 belongs to this builder')
    require(all(name not in recipe['infrastructure_pins'] or recipe['infrastructure_pins'][name] == expected
                for name, expected in final['required_input_pins'].items()), 'Conflicting original pin roles')
    for name, expected in {**recipe['infrastructure_pins'], **final['required_input_pins']}.items():
        path = Path(name)
        require(path.resolve() == path and not path.is_symlink() and pin(path) == expected,
                'Pinned original changed: ' + name)
        result[name] = expected
    paper = final['papers']['P210']
    freeze, live = Path(paper['freeze']), Path(paper['paper'])
    require(live == PAPER and freeze.parent == PAPER and freeze != live and paper['round'] == 2,
            'Final adapter must bind physical P210 Round2')
    result.update(manifest(freeze, paper['freeze_manifest']['sha256'], paper['freeze_payloads']))
    names = paper['source_names']
    require(tuple(names) == SOURCE_NAMES and set(names) == set(paper['source_pins']),
            'Exact ten source-only input names')
    for base in (freeze, live):
        actual = {p.relative_to(base).as_posix() for p in (base / 'sections').rglob('*') if p.is_file()}
        require(actual == {n for n in names if n.startswith('sections/')}, 'Unexpected or orphan section source')
        require(all(pin(base / n) == v for n, v in paper['source_pins'].items()), 'Accepted source equality')
        require(pin(base / 'main.pdf') == paper['pdf_pin'], 'Accepted PDF changed')
        result.update({str(base / n): pin(base / n) for n in (*names, 'main.pdf')})
        main = (base / 'main.tex').read_text()
        inputs = {n if n.endswith('.tex') else n + '.tex' for n in re.findall(r'\\input\{([^}]+)\}', main)}
        require(inputs == set(names) - {'main.tex', 'references.bib'}, 'Exact main input graph; no stale sections')
        require('\\bibliography{references}' in main and '\\bibliographystyle{plainnat}' in main,
                'Named bibliography inputs')
        require('\\author{Anonymous}' in main and 'pdfauthor={}' in main, 'Anonymous source metadata')
    require(paper['pages'] == 6 and paper['underfull'] == [], 'Bound baseline expects six pages and no underfull')
    return result, final


def entry(path):
    return {'exists': path.exists(), 'symlink': path.is_symlink(),
            'link': os.readlink(path) if path.is_symlink() else None,
            'resolved': str(path.resolve()), 'is_file': path.is_file(), 'is_dir': path.is_dir(),
            **(pin(path) if path.is_file() else {})}


def inventory():
    """Known candidate paths, presence, link resolution, membership and file bytes."""
    std = {STDLIB}
    for directory, folders, files in os.walk(STDLIB):
        folders[:] = [n for n in folders if n not in {'site-packages', 'dist-packages', '__pycache__'}]
        std.update(Path(directory) / n for n in files if not n.endswith(('.pyc', '.pyo')))
    runtime = std | set(TOOLS) | set(LIB_ROOTS)
    for base in LIB_ROOTS:
        paths = base.glob('*') if base == Path('/usr/local/lib') else base.rglob('*')
        runtime.update(p for p in paths if p.is_file() and (p.name.endswith('.so') or '.so.' in p.name))
    tex = set(TEX_ROOTS)
    config = set(CONFIG_ROOTS)
    for collection, roots in ((tex, TEX_ROOTS), (config, CONFIG_ROOTS)):
        for base in roots:
            if base.is_dir():
                collection.update(base.rglob('*'))
    config.update(map(Path, ('/etc/ld.so.cache', '/etc/ld.so.conf', '/etc/ld.so.preload',
        '/etc/locale.conf', '/etc/default/locale', '/etc/nsswitch.conf', '/etc/localtime',
        '/etc/bash.bashrc', '/etc/profile', '/etc/passwd', '/etc/group', '/etc/fonts/local.conf',
        '/usr/lib/locale/locale-archive', '/root/.fonts.conf', '/root/.config/fontconfig/fonts.conf',
        '/usr/lib/python310.zip', '/usr/bin/pyvenv.cfg', '/usr/pyvenv.cfg')))
    for base in (Path('/usr/bin'), Path('/usr/lib')):
        config.update(base / n for n in ('python._pth', 'python3._pth', 'python310._pth', 'python3.10._pth'))
    config.update(map(Path, (sysconfig.get_makefile_filename(), sysconfig.get_config_h_filename())))
    for key in ('LDLIBRARY', 'INSTSONAME'):
        value = sysconfig.get_config_var(key)
        if value:
            config.add(STDLIB.parent / (value + '._pth'))
    ldd = Path('/usr/bin/ldd').read_text()
    match = re.search(r'^RTLDLIST="([^"]+)"', ldd, re.M)
    require(ldd.startswith('#!/bin/bash\n') and match is not None, 'Unknown ldd interpreter/loader list')
    config.update(map(Path, match.group(1).split()))
    return {label: {str(p): entry(p) for p in sorted(paths)}
            for label, paths in (('runtime', runtime), ('tex', tex), ('configuration', config))}


def coverage(snapshot):
    return {value['resolved']: {k: value[k] for k in ('sha256', 'bytes')}
            for group in snapshot.values() for value in group.values() if value['is_file']}


def observed(phase, known, source):
    modules = {}
    for name, module in sorted(sys.modules.items()):
        path = getattr(module, '__file__', None)
        if path and Path(path).is_file():
            p = Path(path).resolve()
            require(p.suffix not in {'.pyc', '.pyo'}, 'Imported bytecode')
            modules[name] = {'path': str(p), **pin(p)}
    maps = Path('/proc/self/maps').read_bytes()
    mapped = {}
    for line in maps.decode().splitlines():
        parts = line.split(None, 5)
        if len(parts) == 6 and parts[5].startswith('/'):
            p = Path(parts[5]).resolve()
            mapped[str(p)] = pin(p)
    allowed = {**known, **source}
    for path, value in {**mapped, **{v['path']: {k: v[k] for k in ('sha256', 'bytes')} for v in modules.values()}}.items():
        require(allowed.get(path) == value, 'Observed parent file absent from before key: ' + path)
    require(dict(os.environ) == ENV and not os.path.lexists(sys.pycache_prefix), 'Parent environment/cache changed')
    return {'phase': phase, 'modules': modules, 'mapped_files': mapped, 'maps_raw': maps.decode(),
            'maps_bytes': len(maps), 'maps_sha256': hashlib.sha256(maps).hexdigest(),
            'argv': sys.orig_argv, 'cwd': str(Path.cwd()), 'env': dict(os.environ), 'flags': str(sys.flags),
            'sys_path': sys.path, 'cache_prefix': sys.pycache_prefix, 'cache_absent': True}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', required=True, type=Path)
    parser.add_argument('--expected-preparation-sha256', required=True)
    parser.add_argument('--preflight-only', action='store_true')
    args = parser.parse_args()
    out = args.output
    require(out == PAPER / 'qa_final' and out.resolve() == out and not os.path.lexists(out),
            'Require nonexistent physical P210 qa_final; never replace or resume a prior attempt')
    require(Path(__file__) == SCRIPT and Path.cwd() == ROOT and Path(sys.executable).resolve() == PYTHON,
            'Require exact source/interpreter/cwd')
    require(dict(os.environ) == ENV and sys.flags.isolated == 1 and sys.flags.no_site == 1 and
            sys.flags.optimize == 0 and sys.dont_write_bytecode and
            sys.pycache_prefix == str(out / 'unused_parent_cache') and not os.path.lexists(sys.pycache_prefix),
            'Require minimal environment, -I -S -B, optimization zero and absent exact cache')
    require(sys.path == ['/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload'],
            'Unexpected isolated import search path')
    recipe = json.loads((PREP / 'INPUT_CONTRACT.json').read_bytes())
    before_originals, final = originals(recipe, args.expected_preparation_sha256)
    if args.preflight_only:
        require(not os.path.lexists(out) and not os.path.lexists(sys.pycache_prefix), 'Read-only preflight created no output/cache')
        print(json.dumps({'status': 'PASS_P210_FINAL_SCHEMA_PREFLIGHT_ONLY', 'source': pin(SCRIPT),
            'preparation_seal': pin(PREP / 'SHA256SUMS'), 'original_input_count': len(before_originals),
            'original_input_pins': before_originals, 'final_schema_binding_return': final,
            'output': str(out), 'output_created': False, 'child_commands': 0, 'host_inventory_collections': 0,
            'new_science_build_view_executions': 0, 'terminal_acceptance': False,
            'scope': 'Actual originals/schema gate only; return before mkdir, host inventory and every child command.'}, sort_keys=True))
        return 0
    out.mkdir(mode=0o700)
    save(out / 'executed_source.py', SCRIPT.read_bytes())
    require(pin(out / 'executed_source.py') == before_originals[str(SCRIPT)], 'Executed source snapshot mismatch')
    save(out / 'ORIGINALS_BEFORE.json', before_originals)
    save(out / 'FINAL_SCHEMA_BINDING_RETURN.json', final)
    commands, builds, failures, unresolved = [], [], [], []
    consumed, user_roots, known_before, libraries_before = {}, {}, {}, {}

    def command(label, argv, cwd, inputs=(), mutable_inputs=()):
        work = out / 'commands' / label
        work.mkdir(parents=True)
        direct = {str(p): pin(p) for p in [Path(argv[0]), *map(Path, inputs)]}
        row = {'label': label, 'argv': list(map(str, argv)), 'cwd': str(cwd), 'env': ENV,
               'started_epoch': time.time(), 'timeout_seconds': 600, 'start_new_session': True,
               'exit_code': None, 'status': 'ATTEMPTED', 'inputs_before': direct,
               'generated_inputs_before': {str(p): entry(p) for p in mutable_inputs}}
        save(work / 'ATTEMPT.json', row)
        proc, error, settled = None, None, True
        try:
            with (work / 'stdout').open('xb') as stdout, (work / 'stderr').open('xb') as stderr:
                proc = subprocess.Popen(row['argv'], cwd=cwd, env=ENV, stdout=stdout, stderr=stderr, start_new_session=True)
                row['pid'] = proc.pid
                row['exit_code'] = proc.wait(timeout=600)
                row['status'] = 'COMPLETED'
        except BaseException:
            error = traceback.format_exc()
            row['status'] = 'FAILED_OR_INTERRUPTED'
        if proc is not None:
            try:
                os.killpg(proc.pid, 0)
            except ProcessLookupError:
                pass
            else:
                row['cleanup'] = 'SIGKILL_OWNED_PROCESS_GROUP'
                try:
                    os.killpg(proc.pid, signal.SIGKILL)
                    row['exit_code'] = proc.wait(timeout=10)
                    os.killpg(proc.pid, 0)
                    settled = False
                except ProcessLookupError:
                    pass
                except BaseException:
                    settled = False
                    error = (error or '') + traceback.format_exc()
                error = (error or '') + '\nOwned command group remained after wait/exception; no success.'
            if settled:
                try:
                    row['exit_code'] = proc.wait(timeout=10)
                except BaseException:
                    settled = False
                    error = (error or '') + traceback.format_exc()
        row.update(ended_epoch=time.time(), error=error, streams_settled=settled)
        if not settled:
            unresolved.append(row)
            save(work / 'UNCLOSED.json', row)
            raise RuntimeError('Unsettled command; no final stream hashes or package seal')
        row['inputs_after'] = {}
        for p in direct:
            try:
                row['inputs_after'][p] = pin(p)
            except BaseException:
                row['inputs_after'][p] = {'read_error': traceback.format_exc()}
        row['generated_inputs_after'] = {}
        for p in mutable_inputs:
            try:
                row['generated_inputs_after'][str(p)] = entry(p)
            except BaseException:
                row['generated_inputs_after'][str(p)] = {'read_error': traceback.format_exc()}
        row['streams'] = {n: pin(work / n) for n in ('stdout', 'stderr') if (work / n).is_file()}
        save(work / 'RECEIPT.json', row)
        commands.append(row)
        require(error is None and row['status'] == 'COMPLETED' and row['exit_code'] == 0 and
                row['inputs_after'] == direct and
                all('read_error' not in value for value in row['generated_inputs_after'].values()),
                'Native command failed: ' + label)
        return (work / 'stdout').read_bytes()

    def libraries(label):
        elf = []
        for p in set(TOOLS) | set((STDLIB / 'lib-dynload').glob('*.so')):
            with p.open('rb') as stream:
                if stream.read(4) == b'\x7fELF':
                    elf.append(p)
        raw = command(label, ['/usr/bin/ldd', *sorted(map(str, elf))], out, elf)
        require(b'not found' not in raw, 'ldd unresolved dependency')
        found = set(re.findall(r'(/[^\s():]+)', raw.decode()))
        result = {str(Path(p).resolve()): pin(Path(p).resolve()) for p in found}
        require(result and all(known_before.get(p) == value for p, value in result.items()), 'Unpinned ldd resolution')
        return result

    try:
        snapshot = inventory()
        save_ledger(out / 'KNOWN_INPUTS_BEFORE.json.gz', snapshot)
        known_before = coverage(snapshot)
        save(out / 'PARENT_RUNTIME_BEFORE.json', observed('before_first_child', known_before, before_originals))
        command('source_cmp', ['/usr/bin/cmp', '--', str(SCRIPT), str(out / 'executed_source.py')], out,
                [SCRIPT, out / 'executed_source.py'])
        libraries_before = libraries('ldd_before')
        save(out / 'LIBRARIES_BEFORE.json', libraries_before)
        for tool in ('pdflatex', 'bibtex'):
            command(tool + '_version', ['/usr/bin/' + tool, '--version'], out)
        command('texmf_roots', ['/usr/bin/kpsewhich', '-var-value=TEXMF'], out)
        for ident, paper in final['papers'].items():
            freeze = Path(paper['freeze'])
            round2_metadata = command('P210_round2_pdfinfo', ['/usr/bin/pdfinfo', str(freeze / 'main.pdf')],
                                      out, [freeze / 'main.pdf']).decode()
            round2_pages = int(re.search(r'^Pages:\s+(\d+)$', round2_metadata, re.M).group(1))
            require(round2_pages == paper['pages'] == 6, 'Measure actual Round2 six-page baseline before builds')
            for number in (1, 2):
                label = ident + '_cold_build_' + str(number)
                cold = out / ('cold_build_' + str(number))
                cold.mkdir()
                for name in paper['source_names']:
                    target = cold / name
                    target.parent.mkdir(parents=True, exist_ok=True)
                    save(target, (freeze / name).read_bytes())
                initial = {p.relative_to(cold).as_posix(): pin(p) for p in cold.rglob('*') if p.is_file()}
                require(initial == paper['source_pins'], 'Not an exact source-only initial directory')
                save(out / (label + '_SOURCE_ONLY_INITIAL.json'), initial)
                for variable in USER_VARS:
                    raw = command(label + '_' + variable, ['/usr/bin/kpsewhich', '-var-value=' + variable], cold).decode().strip()
                    p = Path(raw); p = (p if p.is_absolute() else cold / p).resolve()
                    require(raw and not os.path.lexists(p), 'Unexpected user TeX root: ' + variable)
                    user_roots[label + ':' + variable] = {'query': raw, 'resolved': str(p), 'absent': True}
                for number_pass in (1, 2, 3):
                    stem = label + '_pass' + str(number_pass)
                    command(stem, ['/usr/bin/pdflatex', '-no-shell-escape', '-recorder',
                            '-interaction=nonstopmode', '-halt-on-error', 'main.tex'], cold,
                            [cold / n for n in paper['source_names']],
                            [cold / ('main.' + suffix) for suffix in ('aux', 'bbl', 'out', 'toc')])
                    for suffix in ('log', 'fls', 'aux'):
                        save(out / (stem + '.' + suffix), (cold / ('main.' + suffix)).read_bytes())
                    local, external = {}, {}
                    for line in (cold / 'main.fls').read_text().splitlines():
                        if line.startswith('INPUT '):
                            p = Path(line[6:]); p = (p if p.is_absolute() else cold / p).resolve()
                            value = pin(p)
                            if p.is_relative_to(cold):
                                name = p.relative_to(cold).as_posix()
                                require(value == initial.get(name) if name in initial else
                                        p.suffix in {'.aux', '.bbl', '.out', '.toc'}, 'Unexpected local TeX input')
                                local[str(p)] = value
                            else:
                                require(known_before.get(str(p)) == value, 'Unpinned external TeX input: ' + str(p))
                                external[str(p)] = value
                                consumed[str(p)] = value
                    save(out / (stem + '_INPUTS.json'), {'local': local, 'external': external})
                    if number_pass == 1:
                        raw = command(label + '_bst', ['/usr/bin/kpsewhich', 'plainnat.bst'], cold).decode().strip()
                        bst = Path(raw).resolve()
                        require(known_before.get(str(bst)) == pin(bst), 'Unpinned bibliography style')
                        consumed[str(bst)] = pin(bst)
                        command(label + '_bibtex', ['/usr/bin/bibtex', 'main'], cold,
                                [cold / 'main.aux', cold / 'references.bib', bst])
                        for suffix in ('bbl', 'blg'):
                            save(out / (label + '.' + suffix), (cold / ('main.' + suffix)).read_bytes())
                pdf = cold / 'main.pdf'
                metadata = command(label + '_pdfinfo', ['/usr/bin/pdfinfo', 'main.pdf'], cold, [pdf]).decode()
                fonts = command(label + '_pdffonts', ['/usr/bin/pdffonts', 'main.pdf'], cold, [pdf]).decode()
                command(label + '_pdftotext', ['/usr/bin/pdftotext', '-layout', 'main.pdf', str(out / (label + '.txt'))], cold, [pdf])
                pages = int(re.search(r'^Pages:\s+(\d+)$', metadata, re.M).group(1))
                font_rows = [line.split()[-5:] for line in fonts.splitlines()[2:] if line.strip()]
                log = (cold / 'main.log').read_text()
                diagnostics = {name: re.findall(pattern, log, re.M) for name, pattern in {
                    'undefined': r'^.*undefined.*$', 'overfull': r'^.*Overfull.*$',
                    'underfull': r'^.*Underfull.*$', 'warnings': r'^.*Warning.*$',
                    'rerun': r'^.*(?:Rerun to|Please .*rerun|Label\(s\) may have changed).*$'}.items()}
                require(pages == paper['pages'] and pin(pdf) == paper['pdf_pin'], 'PDF page/hash expectation')
                require(pin(pdf)['bytes'] > 100 * 1024, 'Nonempty publication PDF sanity bound')
                author_metadata = re.search(r'^Author:[ \t]*([^\r\n]*)$', metadata, re.M)
                require(author_metadata is None or not author_metadata.group(1).strip(), 'Anonymous measured PDF metadata')
                require(font_rows and all(row[0] == 'yes' for row in font_rows), 'Unembedded PDF font')
                require(diagnostics['underfull'] == paper['underfull'] and
                        all(not value for key, value in diagnostics.items() if key != 'underfull'), 'Final diagnostics differ')
                text = (out / (label + '.txt')).read_text()
                require(not any(marker in text for marker in ('[VERIFY]', '??', '[?]')), 'Unresolved PDF marker')
                bibliography_log = (cold / 'main.blg').read_text()
                require(re.search(r"(?im)Warning--|I couldn't open|There (?:was|were) [1-9][0-9]* error messages?",
                                  bibliography_log) is None, 'BibTeX warning or error retained; no automatic source fix')
                text_pages = text.split('\f')
                if text_pages and not text_pages[-1].strip():
                    text_pages.pop()
                require(len(text_pages) == pages, 'Measured text/PDF page census agreement')
                bibliography_pages = [i + 1 for i, page_text in enumerate(text_pages)
                                      if re.search(r'^\s*(?:References|Bibliography)\s*$', page_text, re.M)]
                require(bibliography_pages, 'Measure reference heading location; do not infer a venue limit')
                command(label + '_frozen_cmp', ['/usr/bin/cmp', '--', str(pdf), str(freeze / 'main.pdf')], cold,
                        [pdf, freeze / 'main.pdf'])
                if number == 1:
                    images = cold / 'pages'; images.mkdir()
                    command(label + '_render', ['/usr/bin/pdftoppm', '-png', '-r', '105', 'main.pdf', str(images / 'page')], cold, [pdf])
                    require(len(list(images.glob('page-*.png'))) == pages, 'Rendered page count')
                require(initial == {n: pin(cold / n) for n in initial}, 'Copied source changed')
                result = {'label': label, 'pages': pages, 'pdf': pin(pdf), 'fonts': len(font_rows),
                          'diagnostics': diagnostics, 'source_count': len(initial), 'visual_review': 'NOT_VIEWED',
                          'reference_heading_pages': bibliography_pages, 'round2_measured_pages': round2_pages,
                          'venue_page_limit': None, 'bibtex_warnings_or_errors': []}
                save(out / (label + '_MEASURED.json'), result)
                builds.append(result)
            pair = [out / ('cold_build_' + str(n)) / 'main.pdf' for n in (1, 2)]
            command(ident + '_pair_cmp', ['/usr/bin/cmp', '--', *map(str, pair)], out, pair)
    except BaseException:
        failures.append({'phase': 'build', 'traceback': traceback.format_exc()})
    if unresolved:
        save(out / 'UNCLOSED.json', {'status': 'UNCLOSED_NO_SEAL', 'commands': unresolved, 'failures': failures})
        return 1
    for phase, collect in (
        ('KNOWN_INPUTS_AFTER', inventory),
        ('ORIGINALS_AFTER', lambda: originals(recipe, args.expected_preparation_sha256)[0]),
        ('LIBRARIES_AFTER', lambda: libraries('ldd_after')),
        ('CONSUMED_TEX_AFTER', lambda: {p: pin(p) for p in consumed}),
        ('PARENT_RUNTIME_AFTER', lambda: observed('after_last_child_and_inventory', known_before, before_originals))):
        try:
            value = collect()
            if phase == 'KNOWN_INPUTS_AFTER':
                save_ledger(out / (phase + '.json.gz'), value)
            else:
                save(out / (phase + '.json'), value)
            expected = {'KNOWN_INPUTS_AFTER': locals().get('snapshot'), 'ORIGINALS_AFTER': before_originals,
                        'LIBRARIES_AFTER': libraries_before, 'CONSUMED_TEX_AFTER': consumed}.get(phase, value)
            require(value == expected, 'Before/after mismatch: ' + phase)
        except BaseException:
            failures.append({'phase': phase, 'traceback': traceback.format_exc()})
    save(out / 'CONSUMED_TEX_BEFORE.json', consumed)
    save(out / 'USER_ROOTS.json', user_roots)
    if any(os.path.lexists(value['resolved']) for value in user_roots.values()):
        failures.append({'phase': 'user_roots', 'error': 'Previously absent user root now exists'})
    if unresolved:
        save(out / 'UNCLOSED.json', {'status': 'UNCLOSED_NO_SEAL', 'commands': unresolved, 'failures': failures})
        return 1
    expected_commands = ['source_cmp', 'ldd_before', 'pdflatex_version', 'bibtex_version', 'texmf_roots']
    for ident in ('P210',):
        expected_commands.append('P210_round2_pdfinfo')
        for number in (1, 2):
            label = ident + '_cold_build_' + str(number)
            suffixes = [*USER_VARS, 'pass1', 'bst', 'bibtex', 'pass2', 'pass3',
                        'pdfinfo', 'pdffonts', 'pdftotext', 'frozen_cmp']
            expected_commands.extend(label + '_' + n for n in suffixes)
            if number == 1:
                expected_commands.append(label + '_render')
        expected_commands.append(ident + '_pair_cmp')
    expected_commands.append('ldd_after')
    census = [row['label'] for row in commands] == expected_commands
    if not census:
        failures.append({'phase': 'command_census', 'actual': [r['label'] for r in commands], 'expected': expected_commands})
    passed = not failures and len(builds) == 2 and census
    result = {'status': 'PASS_P210_SOURCE_ONLY_BUILD_PAIR_NOT_VIEWED' if passed else 'FAIL_PRESERVED',
              'builds': builds, 'commands': commands, 'failures': failures,
              'expected_command_count': len(expected_commands), 'expected_command_labels': expected_commands,
              'visual_review': 'NOT_VIEWED_ROOT_ACTUAL_PAGE_INSPECTION_REQUIRED',
              'new_mathematical_executions': 0, 'external': 'OWNER_AMBER / HOLD_EXTERNAL',
              'paper_completion': False, 'five_paper_completion': False,
              'scope': 'Known candidate before/after bytes/presence/link-membership, link-time ldd closure, per-pass TeX fls, early/late parent modules/maps. No child-map, transient dlopen, non-fls access or OS/startup continuous trace.'}
    save(out / 'RESULT.json', result)
    rows = [(pin(p)['sha256'], p.relative_to(out).as_posix()) for p in sorted(out.rglob('*')) if p.is_file()]
    save(out / 'SHA256SUMS', ''.join(h + '  ' + n + '\n' for h, n in rows).encode())
    manifest(out, pin(out / 'SHA256SUMS')['sha256'], len(rows))
    print(json.dumps({'status': result['status'], 'output': str(out), 'commands': len(commands),
                      'builds': builds, 'failures': failures, 'seal': pin(out / 'SHA256SUMS'), 'payloads': len(rows)}, sort_keys=True))
    return 0 if passed else 1


if __name__ == '__main__':
    raise SystemExit(main())
