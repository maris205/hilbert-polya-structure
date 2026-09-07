#!/usr/bin/env python3
"""Standalone documentary inspector; fresh children are read-only cmp only.

Never imports or executes gate/author science, archived capsule producers,
or archived auditors. Full JSON goes to stdout; capture.py preserves it.
"""
import ast
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys

HERE = Path(__file__).absolute().parent
ROOT = HERE.parents[3]
GATE = ROOT / 'docs/papers204_208_sequence/scouting/MNA_GATE'
AUTHOR = ROOT / 'docs/papers204_208_sequence/scouting/finite_systems_fortieth'
FROZEN = GATE / 'inputs/author_lane40'
SEAL = '5e15111b5dc6b4a585126e32fc59752b10cba8605f846d225e9efa26c656dc34'
AUTHOR_SEAL = '807914fee97a2fa9380074688ad1ab803a601215e10011869f6a713075a9a55a'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
PINS, COMPARISONS, CHECKS = {}, [], 0


def check(ok, detail):
    global CHECKS
    CHECKS += 1
    if not ok:
        raise AssertionError(detail)


def body_meta(body):
    return {'bytes': len(body), 'sha256': hashlib.sha256(body).hexdigest()}


def raw(path):
    path = Path(path)
    check(path.is_absolute() and '..' not in path.parts and not str(path).startswith('/proc/'),
          ('safe physical input', str(path)))
    check(path.is_file(), ('physical file', str(path)))
    return path.read_bytes()


def pin(path, expected=None):
    name = str(path)
    record = body_meta(raw(path))
    if expected is not None:
        check(record == expected, ('exact pin', name, expected, record))
    check(name not in PINS or PINS[name] == record, ('in-inspection drift', name))
    PINS[name] = record
    return record


def read(path):
    return json.loads(raw(path))


def encoded(obj, compact=False):
    return (json.dumps(obj, sort_keys=True, **({'separators': (',', ':')} if compact else {'indent': 2})) + '\n').encode()


def cmp(left, right, role):
    argv = ['/usr/bin/cmp', '--', str(left), str(right)]
    result = subprocess.run(argv, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            timeout=30, check=False)
    row = {'role': role, 'argv': argv, 'exit': result.returncode,
           'stdout_utf8': result.stdout.decode(), 'stderr_utf8': result.stderr.decode()}
    COMPARISONS.append(row)
    check(result.returncode == 0 and result.stdout == result.stderr == b'', ('fresh cmp', row))


def manifest(base, expected, count):
    source = base / 'SHA256SUMS'
    check(pin(source)['sha256'] == expected, ('assigned manifest digest', str(base)))
    names = {}
    for line in raw(source).decode().splitlines():
        sha, rel = line.split('  ', 1)
        check(re.fullmatch('[0-9a-f]{64}', sha) is not None and rel not in names
              and not Path(rel).is_absolute() and '..' not in Path(rel).parts
              and rel != 'SHA256SUMS', ('manifest syntax', rel))
        names[rel] = sha
        check(pin(base / rel)['sha256'] == sha, ('sealed bytes', rel))
    actual = set()
    for path in base.rglob('*'):
        check(not path.is_symlink(), ('package symlink', str(path)))
        if path.is_file() and path != source:
            actual.add(path.relative_to(base).as_posix())
    check(len(names) == count and set(names) == actual, ('complete nonself coverage', str(base)))
    return names


def native(folder, outer=False, expected_exit=0):
    check({p.name for p in folder.iterdir()} == {'attempt.json', 'receipt.json', 'stdout.raw', 'stderr.raw'},
          ('complete four-part native record', str(folder)))
    attempt, receipt = read(folder / 'attempt.json'), read(folder / 'receipt.json')
    for field in ('argv', 'cwd', 'environment'):
        check(attempt[field] == receipt[field], ('native paired field', str(folder), field))
    check(receipt['cwd'] == str(ROOT) and receipt['environment'] == ENV, 'native execution context')
    # The inner command recorder calls time.time twice before launch; exact start equality is not its schema.
    check(attempt['started_epoch'] <= receipt['started_epoch'] <= receipt['finished_epoch'], 'native chronology')
    check(receipt['exit'] == expected_exit, ('native actual exit', str(folder)))
    if outer:
        check(attempt['started_epoch'] == receipt['started_epoch'], 'outer exact start')
        check(pin(Path(receipt['argv'][-1]))['sha256'] == receipt['script_sha256'], 'outer script pin')
    else:
        check(attempt['timeout_seconds'] == 60 and receipt['timed_out'] is False, 'native timeout')
    for stream in ('stdout', 'stderr'):
        pin(folder / (stream + '.raw'), receipt[stream])
    return {'folder': folder.relative_to(GATE).as_posix(), 'attempt': attempt, 'receipt': receipt}


def source_science_names(path):
    """Extract literal dependency tuple from source AST; execute no source code."""
    tree = ast.parse(raw(path).decode(), filename=str(path))
    assignments = [node for node in ast.walk(tree) if isinstance(node, ast.Assign)
                   and any(isinstance(t, ast.Name) and t.id == 'science' for t in node.targets)]
    check(len(assignments) == 1 and isinstance(assignments[0].value, ast.ListComp), 'source science dependency expression')
    return ast.literal_eval(assignments[0].value.generators[0].iter)


def capsule(pair_name, frozen_paths, canonical):
    pair = GATE / 'evidence' / pair_name
    version = {'pair01': 'run_pair.py', 'pair02': 'run_pair_v2.py', 'pair03': 'run_pair_v3.py'}[pair_name]
    source = GATE / version
    config = read(pair / 'configuration.json')
    before, after = read(pair / 'inputs_before.json'), read(pair / 'inputs_after.json')
    check(before == after and raw(pair / 'inputs_before.json') == raw(pair / 'inputs_after.json'), 'capsule raw before/after')
    check(config['environment'] == ENV and config['strace_available'] is None, 'capsule bounded environment/strace')
    check(config['known_inputs'] == len(before) == {'pair01': 977, 'pair02': 994, 'pair03': 997}[pair_name], 'capsule count')
    cache = pair / 'cache_must_remain_absent'
    check(not cache.exists(), 'recorded unused cache remains absent')
    expected_flags = ['-I', '-S', '-B', '-X', 'pycache_prefix=' + str(cache)]
    check(config['interpreter_flags'] == expected_flags, 'capsule flags')
    for name, record in before.items():
        pin(Path(name), record)
    # Reconstruct the known-input union from the original source algorithm.
    # os.walk is a current pathname census only, restricted to the recorded stdlib root.
    stdlib = Path(config['stdlib'])
    check(str(stdlib) == '/root/miniconda3/lib/python3.12', 'exact stdlib tree')
    runtime = {Path(config['executable']), Path('/usr/bin/cmp'), Path('/usr/bin/ldd')}
    source_files, extension_files = set(), set()
    for directory, subdirs, files in os.walk(stdlib):
        subdirs[:] = [d for d in subdirs if d not in ('site-packages', '__pycache__', 'test', 'tests', 'idle_test')]
        for name in files:
            if name.endswith(('.py', '.so')):
                path = Path(directory) / name
                runtime.add(path)
                (extension_files if name.endswith('.so') else source_files).add(path)
    ldd_attempt = read(pair / '00_ldd/attempt.json')
    check(ldd_attempt['argv'][:3] == ['/usr/bin/ldd', config['executable'], '/usr/bin/cmp'], 'original ldd prefix')
    check(set(ldd_attempt['argv'][3:]) == set(map(str, extension_files))
          and len(ldd_attempt['argv'][3:]) == len(extension_files), 'complete original ldd extension argv')
    links = {Path(os.fsdecode(x)).resolve() for x in re.findall(rb'(/[^\s()]+)', raw(pair / '00_ldd/stdout.raw'))
             if Path(os.fsdecode(x)).is_file()}
    runtime.update(links)
    locale_paths = set()
    if pair_name != 'pair01':
        locale_paths = {p for p in Path('/usr/lib/locale/C.utf8').rglob('*') if p.is_file()}
        runtime.update(locale_paths)
        runtime.update([Path('/etc/ld.so.cache'), Path('/etc/localtime').resolve()])
    if pair_name == 'pair03':
        runtime.add(Path('/usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache'))
    science = {GATE / name for name in source_science_names(source)}
    reconstructed = runtime | science | frozen_paths
    check(set(map(str, reconstructed)) == set(before), ('complete source-reconstructed capsule keys', pair_name))
    commands = []
    names = ['00_ldd', '01_verify', '02_verify', '03_cmp_canonical_1', '04_cmp_canonical_2', '05_cmp_pair']
    check(sorted(p.name for p in pair.iterdir() if p.is_dir()) == names, 'six original child directories')
    for name in names:
        commands.append(native(pair / name))
    base_argv = [config['executable'], *expected_flags, str(GATE / 'run_observed.py'), str(GATE / 'verify.py')]
    for number in (1, 2):
        check(commands[number]['receipt']['argv'] == base_argv + [str(pair / f'runtime0{number}.json')], 'original verifier argv')
        check(raw(pair / f'0{number}_verify/stdout.raw') == raw(canonical), 'original full canonical bytes')
        check(commands[number]['receipt']['stderr']['bytes'] == 0, 'original verifier empty stderr')
        cmp(pair / f'0{number}_verify/stdout.raw', canonical, pair_name + f' archived run{number}/canonical')
    expected_cmp = [
        ['/usr/bin/cmp', str(pair / '01_verify/stdout.raw'), str(canonical)],
        ['/usr/bin/cmp', str(pair / '02_verify/stdout.raw'), str(canonical)],
        ['/usr/bin/cmp', str(pair / '01_verify/stdout.raw'), str(pair / '02_verify/stdout.raw')]]
    for row, argv in zip(commands[3:], expected_cmp):
        check(row['receipt']['argv'] == argv and row['receipt']['stdout']['bytes'] == row['receipt']['stderr']['bytes'] == 0,
              'original raw comparison argv/empty streams')
    cmp(pair / '01_verify/stdout.raw', pair / '02_verify/stdout.raw', pair_name + ' archived pair')
    observations = []
    for filename in ('runtime01.json', 'runtime02.json'):
        observed = read(pair / filename)
        check(observed['environment'] == ENV and observed['executable'] == config['executable']
              and observed['pycache_prefix'] == str(cache), 'observed exact runtime settings')
        for flag in ('optimize=0', 'dont_write_bytecode=1', 'no_user_site=1', 'no_site=1',
                     'ignore_environment=1', 'isolated=1', 'safe_path=True'):
            check(flag in observed['flags'], ('actual observed flag', flag))
        check(observed['sys_path'] == ['/root/miniconda3/lib/python312.zip', str(stdlib), str(stdlib / 'lib-dynload')],
              'observed isolated module search path')
        mapped = sorted({line.split()[-1] for line in observed['proc_maps'].splitlines()
                         if len(line.split()) >= 6 and line.split()[-1].startswith('/')})
        check(mapped == observed['mapped_paths'], 'archived proc-map pathname extraction')
        volatile = [p for p in observed['files'] if re.fullmatch(r'/proc/[0-9]+/maps', p)]
        check(len(volatile) == 1 and observed['files'][volatile[0]]['bytes'] == 0, 'volatile proc role/stat size')
        check(observed['audit_open_paths'] == ['/proc/self/maps', str(GATE / 'verify.py')], 'audited Python opens')
        paths = observed['audit_open_paths'] + observed['module_files'] + observed['mapped_paths']
        rebuilt = {volatile[0] if p == '/proc/self/maps' else str(Path(p).resolve()) for p in paths}
        check(rebuilt == set(observed['files']) and len(rebuilt) == 55, '55 observed keys reconstructed')
        missing = []
        for path, record in observed['files'].items():
            if path in volatile:
                continue
            pin(Path(path), record)
            if path not in before:
                missing.append(path)
            else:
                check(before[path] == record, 'ordinary observed matching key')
        expected_missing = {'pair01': ['/usr/lib/locale/C.utf8/LC_CTYPE', '/usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache'],
                            'pair02': ['/usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache'], 'pair03': []}[pair_name]
        check(sorted(missing) == expected_missing, 'honest missing dependency set')
        observations.append({'runtime': filename, 'observed_file_count': len(rebuilt), 'ordinary_files': len(rebuilt) - 1,
                             'nonproc_missing_from_before': sorted(missing), 'volatile_key': volatile[0],
                             'volatile_limit': 'Archived metadata only; never re-read, rehashed, or treated as immutable input.'})
    if pair_name != 'pair03':
        check(not (pair / 'RESULT.json').exists(), 'no fabricated failed-pair RESULT')
    return {'pair': pair_name, 'source': str(source), 'known_inputs': len(before),
            'capsule_source_components': {'stdlib_py': len(source_files), 'stdlib_so': len(extension_files),
                'resolved_ldd_objects': len(links), 'locale_paths': len(locale_paths),
                'scientific_and_recorder_files': sorted(map(str, science)), 'frozen_paths': len(frozen_paths)},
            'known_input_keys_sha256': body_meta(encoded(sorted(before)))['sha256'],
            'source_reconstructed_keys_exact': True, 'before_after_raw_equal': True,
            'commands': commands, 'observations': observations}


def projections(data):
    author_path = FROZEN / 'commands/17_one_mna_pilot/stdout.raw'
    author = [json.loads(line) for line in raw(author_path).splitlines()]
    check(len(author) == 4109 and Counter(r['type'] for r in author) ==
          {'contract': 1, 'state': 4095, 'summary': 12, 'completion': 1}, 'full author JSON-line census')
    lookup = {(r['N'], tuple(r['state'])): r for r in author if r['type'] == 'state'}
    summary_lookup = {r['N']: r for r in author if r['type'] == 'summary'}
    check(len(lookup) == 4095, 'unique author state lookup')
    left, right, summaries, events = [], [], [], Counter()
    check(len(data['boxes']) == 12 and [b['N'] for b in data['boxes']] == list(range(1, 13)), 'canonical box census')
    for box in data['boxes']:
        n = box['N']
        rows = box['states']
        local = {tuple(r['state']): r for r in rows}
        check(len(local) == len(rows) == 1 << (n - 1), 'canonical unique state census')
        destinations = Counter(tuple(r['next']) for r in rows)
        histogram = Counter(r['tail'] for r in rows)
        for row in rows:
            original = lookup[n, tuple(row['state'])]
            projection = {'N': n, 'state': row['state'], 'next': row['next'], 'tail': row['tail'],
                          'terminal': row['terminal'], 'orbit': row['orbit'], 'fibre': row['fibre'],
                          'fibre_formula': row['formula'], 'image_threshold': row['minimum_first'] is not None}
            original_projection = {k: v for k, v in original.items() if k != 'type'}
            check(original_projection == projection, 'all recorded author projection fields')
            left.append(original_projection)
            right.append(projection)
            check(row['fibre'] == len(row['preimages']) == destinations[tuple(row['state'])], 'recorded preimage census')
            check(len({tuple(x) for x in row['preimages']}) == len(row['preimages'])
                  and all(local[tuple(x)]['next'] == row['state'] for x in row['preimages']), 'recorded predecessor references')
            check(len(row['events']) == row['tail'] and [x['t'] for x in row['events']] == list(range(1, row['tail'] + 1)),
                  'event chronology')
            for event in row['events']:
                events['deleted_cut_A'] += len(event['deleted'])
                events['new_block_B'] += len(event['created'])
                if event['t'] >= 2:
                    events['previous_round_right_block'] += len(event['deleted'])
        s, old = box['summary'], summary_lookup[n]
        projected = {'type': 'summary', 'N': n, 'states': s['state_count'], 'image': s['image_count'],
                     'fixed': s['fixed_count'], 'max_tail': s['max_tail'], 'bound': s['max_tail'],
                     'tail_histogram': {str(k): v for k, v in histogram.items()},
                     'max_tail_states': histogram[s['max_tail']], 'max_fibre': s['max_fibre'],
                     'max_fibre_targets': sorted(s['max_fibre_targets']), 'witness': old['witness'],
                     'witness_orbit': local[tuple(old['witness'])]['orbit']}
        old_normalized = dict(old, max_fibre_targets=sorted(old['max_fibre_targets']))
        check(projected == old_normalized, 'all recorded summary fields, documented list ordering normalization')
        check(s['state_count'] == len(rows) and s['image_count'] == len(destinations)
              and s['fixed_count'] == histogram[0] and s['max_tail'] == max(histogram)
              and s['max_fibre'] == max(r['fibre'] for r in rows), 'independent summary aggregates')
        codes = box['triangular_preimages']
        check(len(codes) == len({tuple(x['code']) for x in codes}) == s['image_count'], 'recorded code census')
        check({tuple(x['image']) for x in codes} == set(destinations), 'recorded code/image coverage')
        check(all(local[tuple(x['image'])]['triangular_code'] == x['code'] for x in codes), 'recorded code cross-reference')
        summaries.append({'N': n, 'all_summary_fields_match': True})
    folder = GATE / 'evidence/author_comparison'
    for name, projection in [('AUTHOR_PROJECTION.json', left), ('INDEPENDENT_PROJECTION.json', right)]:
        check(encoded(projection, compact=True) == raw(folder / name), ('byte-exact projection reconstruction', name))
    cmp(folder / 'AUTHOR_PROJECTION.json', folder / 'INDEPENDENT_PROJECTION.json', 'archived author/independent projections')
    check(dict(events) == author[-1]['event_checks'], 'recorded event census')
    result = read(folder / 'RESULT.json')
    check(result['checks'] == 5 + 4095 * 10 + 12 + 1 + 1 == 40969, 'source count before final cmp assertion')
    check(result['status'] == 'PASS' and result['exit'] == 0 and result['matched_state_rows'] == len(left)
          and result['summary_rows'] == summaries and result['event_counts'] == dict(events), 'comparison result reconstructed fields')
    check(result['inputs_before'] == result['inputs_after'], 'projection input before/after')
    check(set(result['inputs_before']) == {str(author_path), str(GATE / 'CANONICAL.json'), str(GATE / 'compare_author.py')},
          'source-reconstructed projection input set')
    for name, record in result['inputs_before'].items():
        pin(Path(name), record)
    for name, record in result['projection_pins'].items():
        pin(folder / name, record)
    for stream in ('stdout', 'stderr'):
        pin(folder / ('cmp.' + stream + '.raw'), result[stream])
        check(result[stream]['bytes'] == 0, 'original projection cmp empty streams')
    check(raw(folder / 'RESULT.json') == raw(GATE / 'evidence/outer_compare_author/stdout.raw'), 'full comparison RESULT/outer stdout bytes')
    return {'state_rows': len(left), 'summary_rows': summaries, 'event_counts': dict(events),
            'recorded_check_count': result['checks'], 'projection_pin': pin(folder / 'AUTHOR_PROJECTION.json'),
            'limit': 'Data-field projection and aggregate reconstruction only; no original map, formula, witness rule, or bijection evaluated.'}


def main():
    check(sys.flags.isolated == sys.flags.no_site == sys.flags.dont_write_bytecode == 1
          and sys.flags.optimize == 0, 'documentary runtime flags')
    manifest(GATE, SEAL, 309)
    manifest(FROZEN, AUTHOR_SEAL, 155)
    pin(Path(__file__).absolute())
    pin(HERE / 'capture.py')
    pin(Path(sys.executable).resolve())
    roles = read(GATE / 'INPUT_ROLES.json')
    rows = roles['roles']
    check(roles['status'] == 'PASS' and roles['author_payloads'] == 155, 'frozen role record')
    role_census = Counter(row['role'] for row in rows)
    check(role_census == {'frozen_author_payload': 155, 'author_manifest_at_original_author_base': 1,
                         'exact_contract_or_collision_original': 10, 'orientation_snapshot_not_current_live_alias': 5,
                         'selected_skill': 2}, '173 exact frozen roles')
    frozen_paths, orientation, origins = set(), [], []
    for row in rows:
        copy = Path(row['copy'])
        check(copy.is_relative_to(GATE) and copy not in frozen_paths, 'unique in-gate role copy')
        frozen_paths.add(copy)
        pin(copy, {'bytes': row['bytes'], 'sha256': row['sha256']})
        if row['role'] == 'orientation_snapshot_not_current_live_alias':
            check(row['raw_equal_at_documentation'] is True and row['original_at_documentation_sha256'] == row['sha256'],
                  'recorded historical orientation equality')
            orientation.append(row)
        else:
            original = Path(row['original'])
            pin(original, {'bytes': row['bytes'], 'sha256': row['sha256']})
            check(raw(original) == raw(copy), 'actual original/frozen raw bytes')
            origins.append(row)
    expected_input_pins = ''.join(sorted(row['sha256'] + '  ' + str(Path(row['copy']).relative_to(ROOT)) + '\n' for row in rows)).encode()
    check(expected_input_pins == raw(GATE / 'INPUT_PINS.sha256'), 'byte-exact input pin reconstruction')
    cmp(AUTHOR / 'SHA256SUMS', FROZEN / 'SHA256SUMS', 'assigned author manifest physical copy')
    for row in origins:
        if Path(row['original']).is_relative_to(ROOT / 'papers'):
            cmp(row['original'], row['copy'], 'exact named historical paper copy hash/raw only')
    code_names = ['audit_final.py', 'compare_author.py', 'freeze_inputs.py', 'record_outer.py', 'record_outer_v3.py',
                  'run_observed.py', 'run_pair.py', 'run_pair_v2.py', 'run_pair_v3.py', 'seal.py']
    for name in code_names:
        ast.parse(raw(GATE / name).decode(), filename=name)
    canonical = GATE / 'CANONICAL.json'
    data = read(canonical)
    check(data['status'] == 'PASS' and data['state_count'] == 4095 and data['N_min'] == 1 and data['N_max'] == 12,
          'recorded canonical contract')
    check(sum(data['checks'].values()) == data['check_count'] == 115680, 'recorded named-check sum, not new mathematical checks')
    check(sum(len(b['states']) for b in data['boxes']) == 4095 and
          sum(len(b['triangular_preimages']) for b in data['boxes']) == 265 and len(data['endpoint_coefficients']) == 364,
          'canonical serialized census')
    capsules = [capsule(name, frozen_paths, canonical) for name in ('pair01', 'pair02', 'pair03')]
    outer_names = [('outer_pair_v2', 1), ('outer_pair_v3', 0), ('outer_compare_author', 0), ('outer_audit_final', 0)]
    outer = [native(GATE / 'evidence' / name, outer=True, expected_exit=code) for name, code in outer_names]
    failed1 = raw(GATE / 'evidence/PAIR01_FAILURE.tool_return.txt').decode()
    failed2 = raw(GATE / 'evidence/outer_pair_v2/stderr.raw').decode()
    check('exit_code: 1' in failed1 and "'runtime01.json', '/usr/lib/locale/C.utf8/LC_CTYPE'" in failed1,
          'preserved first actual failure transcription')
    check("'runtime01.json', '/usr/lib/x86_64-linux-gnu/gconv/gconv-modules.cache'" in failed2,
          'preserved second full native failure')
    projection = projections(data)
    pair_result = {'status': 'PASS', 'role': 'actual_independent_source_only_pair', 'known_inputs_unchanged': 997,
                   'commands': 6, 'stdout': pin(canonical), 'checks_each': data['check_count'], 'states_each': data['state_count'],
                   'runtime_observations': [{'runtime': name, 'observed_file_count': 55,
                       'all_nonproc_files_in_before_capsule': True} for name in ('runtime01.json', 'runtime02.json')],
                   'raw_comparisons': 3, 'OS_syscall_trace': 'UNAVAILABLE_strace_not_installed',
                   'runtime_limit': 'Python opens/modules/proc maps observed, not complete OS file syscall tracing'}
    check(encoded(pair_result) == raw(GATE / 'evidence/pair03/RESULT.json') == raw(GATE / 'evidence/outer_pair_v3/stdout.raw'),
          'byte-exact complete final pair RESULT/outer stdout reconstruction')
    historical = read(FROZEN / 'commands/17_one_mna_pilot/inputs_before.json')
    pilot_resolution = {}
    for original, record in historical.items():
        if original == str(ROOT / 'docs/papers204_208_sequence/scouting/MNA_ROOT_CLOCK_ATTEMPT/PROOF_PACKAGE.md'):
            resolved = FROZEN / 'commands/16_root_clock_proof_read/stdout.raw'
        elif original.startswith(str(AUTHOR) + '/'):
            resolved = FROZEN / Path(original).name
        else:
            resolved = Path(original)
        pin(resolved, record)
        pilot_resolution[original] = {'resolved': str(resolved), 'pin': record}
    check(len(pilot_resolution) == 6, 'six original pilot exact archival roles')
    findings = read(GATE / 'FINDINGS.json')
    check(findings['open_count'] == 0 and findings['resolved_count'] == 2 and
          Counter(x['state'] for x in findings['findings']) == {'resolved': 2}, 'recorded findings census only')
    links = []
    for name in ('CANDIDATE_GATE.md', 'SOURCE_AND_PROOF.md', 'REPLAY_LOG.md'):
        # Text is consumed only to extract link targets, not evaluated as mathematical proof.
        for target in re.findall(r'\]\(([^)]+)\)', raw(GATE / name).decode()):
            if target.startswith(('http://', 'https://')):
                continue
            path = (GATE / target).resolve()
            check(path.is_file() and path.is_relative_to(GATE), 'exact local report link')
            pin(path)
            links.append({'file': name, 'target': target})
    sources, query_count = [], 0
    for path in sorted((GATE / 'evidence').glob('mna_web*.actual.json')):
        web = read(path)
        check(set(web) == {'args', 'result'} and isinstance(web['args'], dict)
              and isinstance(web['result'], str) and web['result'], 'source serialization schema')
        check(set(web['args']) <= {'search_query', 'open', 'click', 'find', 'response_length'}, 'read-only source requests')
        query_count += len(web['args'].get('search_query', []))
        sources.append({'path': str(path), 'args': web['args'], 'file': pin(path),
                        'result_utf8': body_meta(web['result'].encode()),
                        'role': 'full_available_serialized_browser_return_not_native_HTTP'})
    check(len(sources) == 7 and query_count == 13, 'source return/query census')
    original_count = (173 + 168 + 173 + 1 + 1 + 155 + 1 + 6 + 4 + 1 + 1 + 997
                      + 2 * (54 + 1) + 18 * 3 + 6 + 3 * 4 + 2 + 1 + 2 + 1 + 2 + len(links) + 7 + 1)
    check(original_count == 1890, 'original audit predicate-count reconstruction')
    original_summary = {'status': 'PASS', 'role': 'actual_candidate_science_evidence_closure_before_final_nonself_seal',
        'checks': original_count, 'author_payloads': 155, 'input_roles': 173,
        'accepted_pair_known_inputs': 997,
        'actual_native_receipts': [x['folder'] + '/receipt.json' for cap in capsules for x in cap['commands']]
                                 + [x['folder'] + '/receipt.json' for x in outer[:3]],
        'historical_pilot_exact_roles': pilot_resolution, 'canonical': pin(canonical),
        'source_returns': len(sources), 'queries': query_count, 'report_links': links,
        'not_claimed': ['new_scientific_execution', 'OS_syscall_trace', 'manuscript_review', 'admission',
                        'global_novelty', 'central_lifecycle_update']}
    check(encoded(original_summary) == raw(GATE / 'evidence/outer_audit_final/stdout.raw'), 'full original final audit stdout byte reconstruction')
    before = dict(sorted(PINS.items()))
    after = {name: body_meta(raw(Path(name))) for name in before}
    check(before == after, 'entire consumed physical union unchanged')
    print(json.dumps({'status': 'PASS_DOCUMENTARY_ONLY', 'checks': CHECKS, 'gate_payloads': 309,
        'gate_seal': SEAL, 'author_payloads': 155, 'input_role_census': dict(role_census),
        'orientation_copies_consumed_not_live_originals': orientation,
        'named_historical_paper_paths_hash_raw_only': [r['original'] for r in origins if Path(r['original']).is_relative_to(ROOT / 'papers')],
        'capsules': capsules, 'outer_native_records': outer, 'fresh_raw_comparisons': COMPARISONS,
        'source_payloads': sources, 'source_queries': query_count,
        'canonical_census': {'recorded_check_sum_not_reexecution': 115680, 'states': 4095,
                             'triangular_record_rows': 265, 'endpoint_coefficient_rows': 364},
        'projection_reconstruction': projection,
        'final_pair_stdout_reconstructed': body_meta(encoded(pair_result)),
        'final_audit_stdout_reconstructed': body_meta(encoded(original_summary)),
        'original_audit_predicate_count_reconstructed': original_count,
        'old_failure_roles': {'pair01': 'tool-return transcription; first missing locale key; no RESULT',
                             'pair02': 'full outer native exit1, missing gconv key; no RESULT'},
        'physical_input_count': len(before), 'physical_inputs_before': before, 'physical_inputs_after': after,
        'physical_union_unchanged': True, 'read_artifact_source_files': code_names,
        'limits': ['No scientific source was executed or imported; gate/author proof truth was not evaluated.',
                   'Only literal archived data projections/aggregates were reconstructed, not maps/formulas/bijections.',
                   'Ordinary files are current hash-checked; volatile archived proc files are not replayed.',
                   'Current stdlib pathname census plus archived ldd stdout reconstructs the original declared set; no new ldd was run.',
                   'Serialized browser integrity is not native HTTP authentication or source novelty clearance.',
                   'No current central control original was consumed, and no central, original package or science file was changed.',
                   'Candidate GO remains a recorded gate verdict, not admission or manuscript acceptance.']}, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
