#!/usr/bin/env python3
"""Root documentary closure, not a scientific implementation or review.
Reads originals directly. Only fresh child commands are the 15 named cmp calls.
Never imports/executes archived inspectors, producers, verifiers or projections.
"""
import argparse
import ast
from collections import Counter
from datetime import datetime, timezone
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
PREP = QA / 'mna_root_original_preparation'
AUDIT = QA / 'mna_gate_documentary_audit'
GATE = ROOT / 'docs/papers204_208_sequence/scouting/MNA_GATE'
AUTHOR = ROOT / 'docs/papers204_208_sequence/scouting/finite_systems_fortieth'
FROZEN = GATE / 'inputs/author_lane40'
GATE_SHA = '5e15111b5dc6b4a585126e32fc59752b10cba8605f846d225e9efa26c656dc34'
AUDIT_SHA = '921de8d98e2a2a7ab968cec622054338a59da2ebbf7ffed15c23936b4c16bccd'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
READS, RESOLUTIONS, CHECKS, FRESH = {}, {}, Counter(), []


def ck(test, section, detail):
    CHECKS[section] += 1
    if not test:
        raise AssertionError((section, detail))


def meta(data):
    return {'bytes': len(data), 'sha256': sha256(data).hexdigest()}


def raw(path):
    p = Path(path)
    ck(p.is_absolute() and '..' not in p.parts and not str(p).startswith('/proc/') and p.is_file(), 'physical_file', str(p))
    if p.is_relative_to(ROOT):
        ck(not p.is_symlink(), 'workspace_not_symlink', str(p))
    data = p.read_bytes()
    digest, resolved = meta(data), str(p.resolve(strict=True))
    ck(str(p) not in READS or READS[str(p)] == digest, 'read_byte_stability', str(p))
    ck(str(p) not in RESOLUTIONS or RESOLUTIONS[str(p)] == resolved, 'read_resolution_stability', str(p))
    READS[str(p)], RESOLUTIONS[str(p)] = digest, resolved
    return data


def pin(path, expected):
    actual = meta(raw(path))
    ck(actual == expected if isinstance(expected, dict) else actual['sha256'] == expected, 'exact_pin', str(path))
    return actual


def obj(path):
    return json.loads(raw(path))


def encoded(data):
    return (json.dumps(data, sort_keys=True, indent=2) + '\n').encode()


def manifest(base, digest, count):
    pin(base / 'SHA256SUMS', digest)
    rows = {}
    for line in raw(base / 'SHA256SUMS').decode().splitlines():
        m = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        ck(m is not None, 'manifest_syntax', str(base))
        h, name = m.groups()
        p = Path(name)
        ck(p.parts and not p.is_absolute() and '..' not in p.parts and name not in rows and name != 'SHA256SUMS', 'manifest_safe_nonself', name)
        rows[name] = h
        pin(base / name, h)
    files = set()
    for p in base.rglob('*'):
        ck(not p.is_symlink(), 'manifest_no_symlinks', str(p))
        if p.is_file():
            files.add(p.relative_to(base).as_posix())
    ck(len(rows) == count and set(rows) == files - {'SHA256SUMS'}, 'entire_manifest_coverage', (str(base), count))
    return rows


def native(folder, wanted, outer=False, code=0):
    ck({p.name for p in folder.iterdir()} == {'attempt.json', 'receipt.json', 'stdout.raw', 'stderr.raw'}, 'native_four_files', str(folder))
    attempt, receipt = obj(folder / 'attempt.json'), obj(folder / 'receipt.json')
    ck(wanted == {'folder': folder.relative_to(GATE).as_posix(), 'attempt': attempt, 'receipt': receipt}, 'entire_embedded_native_record', str(folder))
    ck(all(attempt[k] == receipt[k] for k in ('argv', 'cwd', 'environment')) and receipt['cwd'] == str(ROOT) and receipt['environment'] == ENV, 'native_context', str(folder))
    ck(attempt['started_epoch'] <= receipt['started_epoch'] <= receipt['finished_epoch'] and receipt['exit'] == code, 'native_actual_chronology_exit', str(folder))
    if outer:
        ck(attempt['started_epoch'] == receipt['started_epoch'], 'outer_start_equality', str(folder))
        pin(receipt['argv'][-1], receipt['script_sha256'])
    else:
        ck(attempt['timeout_seconds'] == 60 and receipt['timed_out'] is False, 'inner_timeout_schema', str(folder))
    for stream in ('stdout', 'stderr'):
        pin(folder / (stream + '.raw'), receipt[stream])
    return receipt


def source_diffs():
    records = obj(AUDIT / 'CAPSULE_SOURCE_DIFFS.actual.json')
    ck(len(records) == 2, 'two_complete_source_diffs', len(records))
    pairs = [('run_pair.py', 'run_pair_v2.py'), ('run_pair_v2.py', 'run_pair_v3.py')]
    for record, (left, right) in zip(records, pairs):
        left_rel, right_rel = [(GATE / name).relative_to(ROOT).as_posix() for name in (left, right)]
        ck(record['cmd'] == 'diff -u ' + left_rel + ' ' + right_rel and record['native_return']['exit_code'] == 1, 'native_diff_command_and_difference_exit', record['cmd'])
        lines = record['native_return']['output'].encode().splitlines(keepends=True)
        ck(lines[0].startswith(('--- ' + left_rel + '\t').encode()) and lines[1].startswith(('+++ ' + right_rel + '\t').encode()), 'original_diff_headers_preserved', record['cmd'])
        old = raw(GATE / left).splitlines(keepends=True)
        target = raw(GATE / right)
        rebuilt, cursor, i, hunks = [], 0, 2, 0
        while i < len(lines):
            header = re.fullmatch(rb'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@[^\n]*\n', lines[i])
            ck(header is not None, 'complete_unified_hunk_header', lines[i].decode())
            start, take, newstart, give = [int(x) if x is not None else 1 for x in header.groups()]
            position = start - 1 if take else start
            ck(cursor <= position <= len(old), 'diff_old_position', position)
            rebuilt.extend(old[cursor:position]); cursor = position
            ck(newstart == len(rebuilt) + 1 if give else newstart == len(rebuilt), 'diff_new_position', newstart)
            i += 1; consumed = produced = 0
            while i < len(lines) and not lines[i].startswith(b'@@ '):
                line = lines[i]; tag, data = line[:1], line[1:]
                ck(tag in (b' ', b'-', b'+'), 'full_unified_diff_line', line.decode())
                if tag in (b' ', b'-'):
                    ck(cursor < len(old) and old[cursor] == data, 'diff_original_context_or_deletion', cursor)
                    cursor += 1; consumed += 1
                if tag in (b' ', b'+'):
                    rebuilt.append(data); produced += 1
                i += 1
            ck((consumed, produced) == (take, give), 'diff_entire_hunk_counts', (consumed, produced, take, give))
            hunks += 1
        rebuilt.extend(old[cursor:])
        ck(b''.join(rebuilt) == target and hunks > 0, 'full_diff_applies_to_original_bytes', record['cmd'])
    return len(records)


def runtime(inputs):
    result = {'modules': {}, 'mapped_files': {}, 'flags': repr(sys.flags), 'environment': dict(os.environ),
              'executable': str(Path(sys.executable).resolve()), 'sys_path': sys.path, 'pycache_prefix': sys.pycache_prefix}
    for name, module in sorted(sys.modules.items()):
        source = getattr(module, '__file__', None)
        if source and Path(source).is_file():
            p = Path(source).resolve(strict=True)
            ck(p.suffix not in ('.pyc', '.pyo'), 'source_only_module', name)
            result['modules'][name] = {'path': str(p), **meta(raw(p))}
    maps = Path('/proc/self/maps').read_bytes()
    result['volatile_proc_maps'] = maps.decode()
    result['volatile_proc_maps_metadata'] = meta(maps)
    for line in maps.decode().splitlines():
        fields = line.split(None, 5)
        if len(fields) == 6 and fields[5].startswith('/'):
            ck(not fields[5].endswith(' (deleted)'), 'mapped_file_not_deleted', fields[5])
            p = Path(fields[5]).resolve(strict=True)
            result['mapped_files'][str(p)] = meta(raw(p))
    for path, expected in list(result['mapped_files'].items()) + [(v['path'], {k: v[k] for k in ('bytes', 'sha256')}) for v in result['modules'].values()]:
        ck(inputs.get(path) == expected, 'root_runtime_before_capsule_coverage', path)
    result['scope'] = 'Own file-backed samples, not startup/continuous/OS syscall tracing; raw proc bytes are observations, not reused paths.'
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--expected-preparation-sha256', required=True)
    parser.add_argument('--runtime-inputs', required=True)
    args = parser.parse_args()
    ck(Path(__file__).resolve() == PREP / 'inspect.py' and Path.cwd() == ROOT and Path(sys.executable).resolve() == Path('/usr/bin/python3.10') and
       dict(os.environ) == ENV and sys.flags.isolated and sys.flags.no_site and sys.flags.optimize == 0 and sys.dont_write_bytecode and
       sys.pycache_prefix and not os.path.lexists(sys.pycache_prefix), 'root_isolated_exact_entry', sys.executable)
    runtime_path = Path(args.runtime_inputs)
    ck(runtime_path.is_absolute() and runtime_path.name == 'INPUTS_BEFORE.json' and runtime_path.parent.parent == QA and
       re.fullmatch(r'mna_root_original_[0-9]{2}', runtime_path.parent.name) and runtime_path.parent.resolve(strict=True) == runtime_path.parent and
       sys.pycache_prefix == str(runtime_path.parent / 'unused_checker_cache') and
       sys.path == ['/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload'] and
       not os.path.lexists('/usr/lib/python310.zip'), 'exact_recorder_runtime_capsule_and_source_import_path', args.runtime_inputs)
    gate_rows = manifest(GATE, GATE_SHA, 309)
    manifest(AUDIT, AUDIT_SHA, 10)
    manifest(PREP, args.expected_preparation_sha256, 5)
    for path, expected in obj(PREP / 'INPUT_PINS.json')['inputs'].items():
        pin(path, expected)
    runtime_inputs = obj(runtime_path)
    for name, lines in [('inspect.py', 455), ('capture.py', 61)]:
        source = raw(AUDIT / name)
        ck(len(source.splitlines()) == lines, 'exact_original_auditor_source_lines', name)
        ast.parse(source, filename=str(AUDIT / name))
    early = runtime(runtime_inputs)
    doc = obj(AUDIT / 'attempt_01/stdout.raw')
    before, after = doc['physical_inputs_before'], doc['physical_inputs_after']
    ck(before == after and len(before) == doc['physical_input_count'] == 1294 and doc['physical_union_unchanged'] is True,
       'full_archived_1294_ledgers', 'all paths, not samples')
    for name, expected in before.items():
        pin(name, expected)
    attempt, receipt = obj(AUDIT / 'attempt_01/attempt.json'), obj(AUDIT / 'attempt_01/receipt.json')
    ck(receipt['argv'] == ['/root/miniconda3/bin/python3.12', '-I', '-S', '-B', str(AUDIT / 'inspect.py')] and
       attempt['argv'] == receipt['argv'] and attempt['cwd'] == receipt['cwd'] == str(ROOT) and
       attempt['started_epoch'] == receipt['started_epoch'] <= receipt['finished_epoch'] and attempt['timeout_seconds'] == 60 and
       receipt['exit'] == 0 and receipt['timed_out'] is False, 'actual_documentary_capture_schema', 'no inferred environment/cold-cache fields')
    ck(attempt['producer_input_pins'] == receipt['producer_inputs_before'] == receipt['producer_inputs_after'] and receipt['producer_unchanged'] is True and
       set(receipt['producer_inputs_before']) == {str(AUDIT / 'inspect.py'), str(AUDIT / 'capture.py'), '/root/miniconda3/bin/python3.12'}, 'entire_three_producer_pins', 'source/source/interpreter')
    for path, expected in receipt['producer_inputs_before'].items():
        pin(path, expected)
    for stream in ('stdout', 'stderr'):
        pin(AUDIT / 'attempt_01' / (stream + '.raw'), receipt[stream])
    ck(raw(AUDIT / 'attempt_01/stderr.raw') == b'', 'actual_empty_documentary_stderr', 'attempt_01')
    tool = obj(AUDIT / 'ATTEMPT_01.actual_tool_return.json')
    ck(tool['cmd'] == 'python3 -I -S -B docs/papers204_208_sequence/qa/mna_gate_documentary_audit/capture.py attempt_01' and
       tool['native_return']['exit_code'] == 0 and tool['native_return']['output'].encode() == raw(AUDIT / 'attempt_01/receipt.json'), 'full_native_capture_tool_return', 'receipt bytes, not child stdout')
    close = obj(AUDIT / 'CLOSURE_BEFORE_SEAL.actual.json')['native_return']
    expected_close = {'status': 'PASS', 'native_return_matches_actual_capture_receipt_bytes': True, 'complete_child_stdout': receipt['stdout'],
        'complete_child_stderr': receipt['stderr'], 'checks': 38755, 'physical_inputs': 1294, 'actual_fresh_comparisons': 15, 'producer_pins_unchanged': True}
    ck(close['exit_code'] == 0 and json.loads(close['output']) == expected_close and doc['status'] == 'PASS_DOCUMENTARY_ONLY' and doc['checks'] == 38755 and
       doc['gate_payloads'] == 309 and doc['gate_seal'] == GATE_SHA, 'native_closure_exact_result', 'recorded documentary count only')
    roles = obj(GATE / 'INPUT_ROLES.json')['roles']
    census = Counter(r['role'] for r in roles)
    ck(dict(census) == doc['input_role_census'] and len(roles) == 173, 'complete_173_roles', dict(census))
    orientation, nonorientation = [], []
    for row in roles:
        expected = {k: row[k] for k in ('bytes', 'sha256')}
        pin(row['copy'], expected)
        if row['role'] == 'orientation_snapshot_not_current_live_alias':
            ck(row['original'] not in before and row['raw_equal_at_documentation'] is True and row['original_at_documentation_sha256'] == row['sha256'], 'frozen_orientation_not_live_alias', row['original'])
            orientation.append(row)
        else:
            pin(row['original'], expected)
            ck(raw(row['original']) == raw(row['copy']), 'complete_original_copy_bytes', row['original'])
            nonorientation.append(row)
    ck(orientation == doc['orientation_copies_consumed_not_live_originals'] and len(orientation) == 5 and len(nonorientation) == 168, 'exact_orientation_boundary', 5)
    expected_pinlist = ''.join(sorted(row['sha256'] + '  ' + Path(row['copy']).relative_to(ROOT).as_posix() + '\n' for row in roles)).encode()
    ck(raw(GATE / 'INPUT_PINS.sha256') == expected_pinlist, 'entire_input_pinlist_bytes', 173)
    manifest(FROZEN, '807914fee97a2fa9380074688ad1ab803a601215e10011869f6a713075a9a55a', 155)
    original997 = obj(GATE / 'evidence/pair03/inputs_before.json')
    union = {str(GATE / n) for n in gate_rows} | {str(GATE / 'SHA256SUMS')} | set(original997) | {r['original'] for r in nonorientation} | {str(AUDIT / 'inspect.py'), str(AUDIT / 'capture.py')}
    ck(set(before) == union and len(original997) == 997 and all(before.get(p) == v for p, v in original997.items()), 'independent_entire_1294_union', '997 plus exact gate/original/source roles')
    native_count = 0
    ck([cap['pair'] for cap in doc['capsules']] == ['pair01', 'pair02', 'pair03'], 'three_archived_pairs', 'unchanged historical scope')
    for cap, count in zip(doc['capsules'], (977, 994, 997)):
        pair = GATE / 'evidence' / cap['pair']
        old = obj(pair / 'inputs_before.json')
        ck(old == obj(pair / 'inputs_after.json') and raw(pair / 'inputs_before.json') == raw(pair / 'inputs_after.json') and len(old) == cap['known_inputs'] == count, 'all_original_pair_ledgers', cap['pair'])
        ck(meta(encoded(sorted(old)))['sha256'] == cap['known_input_keys_sha256'] and cap['source_reconstructed_keys_exact'] is True, 'archived_source_capsule_membership_record', cap['pair'])
        for path, expected in old.items():
            pin(path, expected)
        ck([r['folder'].split('/')[-1] for r in cap['commands']] == ['00_ldd', '01_verify', '02_verify', '03_cmp_canonical_1', '04_cmp_canonical_2', '05_cmp_pair'], 'six_original_command_roles', cap['pair'])
        for record in cap['commands']:
            native(GATE / record['folder'], record); native_count += 1
        missing_expected = {'pair01': ['/usr/lib/locale/C.utf8/LC_CTYPE', '/usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache'], 'pair02': ['/usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache'], 'pair03': []}[cap['pair']]
        for observation in cap['observations']:
            observed = obj(pair / observation['runtime'])
            volatile = [p for p in observed['files'] if re.fullmatch(r'/proc/[0-9]+/maps', p)]
            ck(len(volatile) == 1 and observation['volatile_key'] == volatile[0] and observed['files'][volatile[0]]['bytes'] == 0, 'archived_volatile_proc_role_not_reopened', observation['runtime'])
            missing = sorted(p for p in observed['files'] if p not in volatile and p not in old)
            ck(missing == observation['nonproc_missing_from_before'] == missing_expected and len(observed['files']) == observation['observed_file_count'] == 55, 'exact_preserved_dependency_failure_scope', cap['pair'])
            for path, expected in observed['files'].items():
                if path not in volatile:
                    pin(path, expected)
                    ck(path not in old or old[path] == expected, 'ordinary_archived_runtime_pin', path)
        if cap['pair'] != 'pair03':
            ck(not os.path.lexists(pair / 'RESULT.json'), 'no_failed_pair_promoted_result', cap['pair'])
    ck([r['folder'].split('/')[-1] for r in doc['outer_native_records']] == ['outer_pair_v2', 'outer_pair_v3', 'outer_compare_author', 'outer_audit_final'], 'four_original_outer_roles', 4)
    for row, code in zip(doc['outer_native_records'], (1, 0, 0, 0)):
        native(GATE / row['folder'], row, True, code); native_count += 1
    ck('exit_code: 1' in raw(GATE / 'evidence/PAIR01_FAILURE.tool_return.txt').decode() and "'runtime01.json', '/usr/lib/locale/C.utf8/LC_CTYPE'" in raw(GATE / 'evidence/PAIR01_FAILURE.tool_return.txt').decode(), 'pair01_transcription_not_native_outer_stderr', 'historical limitation unchanged')
    ck("'runtime01.json', '/usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache'" in raw(GATE / 'evidence/outer_pair_v2/stderr.raw').decode(), 'pair02_full_native_failure', 'exit 1 retained')
    ck(doc['old_failure_roles'] == {'pair01': 'tool-return transcription; first missing locale key; no RESULT',
       'pair02': 'full outer native exit1, missing gconv key; no RESULT'}, 'exact_reported_old_failure_roles', 'no provenance promotion')
    differences = source_diffs()
    projection = obj(GATE / 'evidence/author_comparison/RESULT.json')
    ck(projection['status'] == 'PASS' and projection['exit'] == 0 and projection['checks'] == doc['projection_reconstruction']['recorded_check_count'] == 40969 and
       projection['matched_state_rows'] == doc['projection_reconstruction']['state_rows'] == 4095 and projection['summary_rows'] == doc['projection_reconstruction']['summary_rows'] and
       projection['event_counts'] == doc['projection_reconstruction']['event_counts'] and projection['inputs_before'] == projection['inputs_after'], 'complete_projection_record_crosslinks', 'archived mathematical reconstruction not rerun')
    for path, expected in projection['inputs_before'].items():
        pin(path, expected)
    for name, expected in projection['projection_pins'].items():
        pin(GATE / 'evidence/author_comparison' / name, expected)
    left, right = [GATE / 'evidence/author_comparison' / name for name in ('AUTHOR_PROJECTION.json', 'INDEPENDENT_PROJECTION.json')]
    ck(raw(left) == raw(right) and len(obj(left)) == 4095, 'complete_projection_bytes_and_row_census', 'no field/formula regeneration')
    pin(left, doc['projection_reconstruction']['projection_pin'])
    for stream in ('stdout', 'stderr'):
        pin(GATE / 'evidence/author_comparison' / ('cmp.' + stream + '.raw'), projection[stream])
        ck(projection[stream]['bytes'] == 0, 'original_projection_cmp_empty_stream', stream)
    ck(raw(GATE / 'evidence/author_comparison/RESULT.json') == raw(GATE / 'evidence/outer_compare_author/stdout.raw'), 'entire_projection_outer_result_bytes', 'old original')
    for name, output, key in [('pair03/RESULT.json', 'outer_pair_v3/stdout.raw', 'final_pair_stdout_reconstructed'), (None, 'outer_audit_final/stdout.raw', 'final_audit_stdout_reconstructed')]:
        pin(GATE / 'evidence' / output, doc[key])
        if name:
            ck(raw(GATE / 'evidence' / name) == raw(GATE / 'evidence' / output), 'entire_final_pair_outer_bytes', name)
    original_audit = obj(GATE / 'evidence/outer_audit_final/stdout.raw')
    ck(original_audit['checks'] == doc['original_audit_predicate_count_reconstructed'] == 1890 and len(original_audit['actual_native_receipts']) == 21, 'original_audit_nonself_receipt_census', '18 plus 3, not its own outer receipt')
    for original, row in original_audit['historical_pilot_exact_roles'].items():
        pin(row['resolved'], row['pin'])
    ck(len(original_audit['historical_pilot_exact_roles']) == 6, 'six_original_pilot_roles', 'no rerun')
    for source in doc['source_payloads']:
        pin(source['path'], source['file'])
        web = obj(source['path'])
        ck(set(web) == {'args', 'result'} and web['args'] == source['args'] and meta(web['result'].encode()) == source['result_utf8'], 'complete_source_serialization', source['path'])
    ck(len(doc['source_payloads']) == 7 and sum(len(x['args'].get('search_query', [])) for x in doc['source_payloads']) == doc['source_queries'] == 13, 'exact_source_return_query_census', 'no new web')
    for row in original_audit['report_links']:
        target = (GATE / row['target']).resolve(strict=True)
        ck(target.is_relative_to(GATE) and target.is_file(), 'recorded_local_report_link', row)
        raw(target)
    expected_cmps = [(AUTHOR / 'SHA256SUMS', FROZEN / 'SHA256SUMS')]
    expected_cmps += [(Path(r['original']), Path(r['copy'])) for r in nonorientation if Path(r['original']).is_relative_to(ROOT / 'papers')]
    for pair in ('pair01', 'pair02', 'pair03'):
        p = GATE / 'evidence' / pair
        expected_cmps += [(p / '01_verify/stdout.raw', GATE / 'CANONICAL.json'), (p / '02_verify/stdout.raw', GATE / 'CANONICAL.json'), (p / '01_verify/stdout.raw', p / '02_verify/stdout.raw')]
    expected_cmps.append((left, right))
    ck(len(doc['fresh_raw_comparisons']) == len(expected_cmps) == 15, 'all_original_cmp_roles', 15)
    for prior, (left, right) in zip(doc['fresh_raw_comparisons'], expected_cmps):
        argv = ['/usr/bin/cmp', '--', str(left), str(right)]
        ck(prior['argv'] == argv and prior['exit'] == 0 and prior['stdout_utf8'] == prior['stderr_utf8'] == '', 'original_full_cmp_record', prior['role'])
        first = {str(p): meta(raw(p)) for p in (left, right)}
        row = {'argv': argv, 'cwd': str(ROOT), 'environment': ENV, 'timeout_seconds': 30, 'status': 'ATTEMPTED',
               'exit': None, 'stdout_utf8': '', 'stderr_utf8': '', 'inputs_before': first, 'started_utc': datetime.now(timezone.utc).isoformat()}
        FRESH.append(row)
        try:
            result = subprocess.run(argv, cwd=ROOT, env=ENV, capture_output=True, timeout=30, check=False)
            row.update(status='COMPLETED', exit=result.returncode, stdout_utf8=result.stdout.decode(), stderr_utf8=result.stderr.decode(), streams_complete=True, failure=None)
        except subprocess.TimeoutExpired as exc:
            row.update(status='TIMED_OUT', wrapper_exit=124, stdout_utf8=(exc.stdout or b'').decode(errors='replace'),
                       stderr_utf8=(exc.stderr or b'').decode(errors='replace'), streams_complete=False, failure=repr(exc))
        except OSError as exc:
            row.update(status='SPAWN_FAILED', wrapper_exit=127, streams_complete=False, failure=repr(exc))
        row['ended_utc'] = datetime.now(timezone.utc).isoformat()
        row['inputs_after'] = {str(p): meta(raw(p)) for p in (left, right)}
        ck(row['exit'] == 0 and row['stdout_utf8'] == row['stderr_utf8'] == '' and row['inputs_before'] == row['inputs_after'], 'fresh_native_original_byte_comparison', argv)
    late = runtime(runtime_inputs)
    for name, expected in after.items():
        pin(name, expected)
    manifest(GATE, GATE_SHA, 309); manifest(AUDIT, AUDIT_SHA, 10)
    root_before = dict(READS)
    root_after = {name: meta(Path(name).read_bytes()) for name in root_before}
    ck(root_before == root_after and all(str(Path(p).resolve(strict=True)) == r for p, r in RESOLUTIONS.items()), 'entire_root_read_reference_closure_after', len(root_before))
    print(json.dumps({'status': 'PASS_ROOT_MNA_ORIGINAL_DOCUMENTARY_CLOSURE', 'checks': sum(CHECKS.values()), 'checks_by_section': dict(CHECKS),
        'gate_payloads': 309, 'gate_manifest_sha256': GATE_SHA, 'documentary_payloads': 10, 'documentary_manifest_sha256': AUDIT_SHA,
        'original_documentary_checks_recorded_not_rerun': 38755, 'original_physical_paths_checked_twice': 1294, 'original_gate_native_records_checked': native_count,
        'complete_source_diffs_checked': differences, 'complete_projection_bytes_checked_not_recomputed': meta(raw(left)), 'fresh_native_comparisons': FRESH,
        'root_runtime_before': early, 'root_runtime_after': late, 'root_physical_input_count': len(root_before), 'root_physical_inputs_before': root_before,
        'root_physical_inputs_after': root_after, 'host_resolutions_rechecked': RESOLUTIONS, 'root_reference_closure_unchanged': True,
        'new_scientific_executions': 0, 'old_inspector_or_producer_executions': 0, 'new_web_or_build_or_view': 0,
        'limits': ['Documentary original closure, not theorem/source semantic judgment or third review.', 'Projection reconstruction is reused from its fully pinned inspected original, not recalculated.',
                   'Old capture inherited environment and lacks a full cold-cache runtime capsule; this checker does not retroactively add one.', 'Own runtime samples are not OS/startup/continuous tracing.', 'No admission or paper numbering.'],
        'owner': 'OWNER_AMBER', 'external_status': 'HOLD_EXTERNAL'}, sort_keys=True, indent=2))


if __name__ == '__main__':
    try:
        main()
    except Exception as exc:
        print(json.dumps({'status': 'FAIL_ROOT_MNA_ORIGINAL_DOCUMENTARY_CLOSURE', 'failure': repr(exc), 'checks_by_section': dict(CHECKS), 'fresh_native_comparisons': FRESH}, sort_keys=True, indent=2))
        raise
