#!/usr/bin/env python3
"""Read-only lane40 documentary audit. Never imports/runs archived producers.

Only fresh children are four exact cmp commands on the root-reference roles.
The three central-control original/copy cmp calls were captured separately
before possible lifecycle edits. Their already-sealed copies are historical
physical aliases here, not claims that current central indexes stay unchanged.
Stdout is complete structured evidence; the caller preserves the native return.
"""
import ast
from collections import Counter
import hashlib
import json
from pathlib import Path
import subprocess
import sys

HERE = Path(__file__).absolute().parent
ROOT = HERE.parents[3]
LANE = ROOT / 'docs/papers204_208_sequence/scouting/finite_systems_fortieth'
SEAL = '807914fee97a2fa9380074688ad1ab803a601215e10011869f6a713075a9a55a'
CMP = Path('/usr/bin/cmp').resolve()
PHYSICAL = {}
CHECKS = 0


def require(value, label):
    global CHECKS
    CHECKS += 1
    if not value:
        raise AssertionError(label)


def meta_bytes(body):
    return {'bytes': len(body), 'sha256': hashlib.sha256(body).hexdigest()}


def safe(path):
    path = Path(path)
    require(path.is_absolute() and '..' not in path.parts, ('absolute path', str(path)))
    require('MNA_GATE' not in path.parts, ('protected gate', str(path)))
    require(not any(x.is_symlink() for x in [path, *path.parents]), ('symlink', str(path)))
    require(path.is_file(), ('regular file', str(path)))
    return path


def raw(path):
    return safe(path).read_bytes()


def read(path):
    return json.loads(raw(path))


def add(path, expected=None):
    path = safe(path)
    actual = meta_bytes(raw(path))
    if expected is not None:
        require(actual == expected, ('pin mismatch', str(path), expected, actual))
    if str(path) in PHYSICAL:
        require(PHYSICAL[str(path)] == actual, ('in-pass drift', str(path)))
    PHYSICAL[str(path)] = actual


def safe_expr(node, env):
    """Interpret only the original final print's data expression, not its code."""
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Name):
        return env[node.id]
    if isinstance(node, ast.Dict):
        return {safe_expr(k, env): safe_expr(v, env) for k, v in zip(node.keys, node.values)}
    if isinstance(node, (ast.Tuple, ast.List)):
        return [safe_expr(x, env) for x in node.elts]
    if isinstance(node, ast.Subscript):
        return safe_expr(node.value, env)[safe_expr(node.slice, env)]
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Div):
        return safe_expr(node.left, env) / safe_expr(node.right, env)
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
        require(not node.keywords and len(node.args) == 1, 'limited expression call')
        arg = safe_expr(node.args[0], env)
        if node.func.id == 'len':
            return len(arg)
        if node.func.id == 'list':
            return list(arg)
        if node.func.id == 'read':
            require(arg == LANE / 'EXTRA_TOOL_RETURN.json', 'limited expression read')
            return read(arg)
    raise AssertionError(('unsupported print AST', ast.dump(node)))


def validate_pilot():
    body = raw(LANE / 'commands/17_one_mna_pilot/stdout.raw')
    rows = [json.loads(line) for line in body.splitlines()]
    require(body.endswith(b'\n'), 'pilot terminal LF')
    require(Counter(row['type'] for row in rows) ==
            {'contract': 1, 'state': 4095, 'summary': 12, 'completion': 1}, 'pilot census')
    require(rows[0] == {'type': 'contract', 'map': 'sum_maximal_weakly_increasing_old_runs',
                       'carrier': 'positive_compositions_fixed_total', 'N_min': 1, 'N_max': 12,
                       'expected_total_states': 4095,
                       'role': 'one_fixed_pilot_not_proof_or_independent_review'}, 'pilot header')
    require(rows[-1]['status'] == 'PASS' and rows[-1]['total_states'] == 4095
            and rows[-1]['N_min'] == 1 and rows[-1]['N_max'] == 12, 'completion fields')
    events = Counter()
    tables = []
    cursor = 1
    for n in range(1, 13):
        count = 1 << (n - 1)
        records = rows[cursor:cursor + count]
        summary = rows[cursor + count]
        cursor += count + 1
        require(all(r['type'] == 'state' and r['N'] == n for r in records), ('row order', n))
        require(summary['type'] == 'summary' and summary['N'] == n, ('summary order', n))
        index = {tuple(r['state']): r for r in records}
        require(len(index) == count, ('unique positive compositions', n))
        next_counts = Counter(tuple(r['next']) for r in records)
        tails = Counter(r['tail'] for r in records)
        for offset, r in enumerate(records):
            require(set(r) == {'type', 'N', 'state', 'next', 'tail', 'terminal', 'orbit',
                               'fibre', 'fibre_formula', 'image_threshold'}, 'state schema')
            state = r['state']
            require(all(type(x) is int and x > 0 for x in state) and sum(state) == n,
                    ('recorded carrier', n, offset))
            pos, mask = 0, 0
            for value in state[:-1]:
                pos += value
                mask |= 1 << (pos - 1)
            require(mask == offset, ('serialized composition ordering', n, offset))
            require(type(r['tail']) is int and r['tail'] >= 0, 'tail type')
            require(type(r['fibre']) is int and r['fibre'] >= 0, 'fibre type')
            require(type(r['image_threshold']) is bool, 'image flag type')
            require(r['fibre'] == next_counts[tuple(state)] == r['fibre_formula'], 'recorded fibres')
            require(r['image_threshold'] == (r['fibre'] > 0), 'recorded image flag')
            orbit = r['orbit']
            require(len(orbit) == r['tail'] + 1 and orbit[0] == state
                    and orbit[-1] == r['terminal'], 'orbit endpoints/length')
            require(len({tuple(x) for x in orbit}) == len(orbit), 'no repeated recorded orbit state')
            for t, current in enumerate(orbit):
                current_row = index[tuple(current)]
                require(current_row['tail'] == r['tail'] - t
                        and current_row['terminal'] == r['terminal']
                        and current_row['orbit'] == orbit[t:], 'cross-record orbit suffix')
                if t + 1 < len(orbit):
                    nxt = orbit[t + 1]
                    require(current_row['next'] == nxt, 'cross-record transition reference')
                    # Count only the events represented by archived orbit partitions.
                    # No map, formula, mass inequality or theorem predicate is evaluated.
                    def recorded_intervals(parts):
                        ans, start = set(), 0
                        for value in parts:
                            ans.add((start, start + value))
                            start += value
                        return ans
                    old_intervals = recorded_intervals(current)
                    next_intervals = recorded_intervals(nxt)
                    old_cuts = {a for a, b in old_intervals if a}
                    next_cuts = {a for a, b in next_intervals if a}
                    deleted = len(old_cuts - next_cuts)
                    events['deleted_cut_A'] += deleted
                    events['new_block_B'] += len(next_intervals - old_intervals)
                    if t >= 1:
                        events['previous_round_right_block'] += deleted
                else:
                    require(current_row['next'] == current, 'recorded terminal fixed point')
        maximum_fibre = max(r['fibre'] for r in records)
        require(summary['states'] == count and summary['image'] == len(next_counts), 'summary sizes')
        require(summary['fixed'] == tails[0], 'summary fixed')
        require(summary['tail_histogram'] == {str(k): v for k, v in tails.items()}, 'summary histogram')
        require(summary['max_tail'] == max(tails) == summary['bound'], 'summary recorded bound')
        require(summary['max_tail_states'] == tails[max(tails)], 'summary maximum tail states')
        require(summary['max_fibre'] == maximum_fibre, 'summary maximum fibre')
        require(summary['max_fibre_targets'] == [r['state'] for r in records
                                                if r['fibre'] == maximum_fibre], 'summary fibre targets')
        witness = index[tuple(summary['witness'])]
        require(summary['witness_orbit'] == witness['orbit']
                and witness['tail'] == summary['bound'], 'summary witness')
        require(sum(r['fibre'] for r in records) == count, 'fibre sum')
        tables.append(summary)
    require(cursor == len(rows) - 1, 'pilot exact row exhaustion')
    require(dict(events) == rows[-1]['event_checks'] == {
        'deleted_cut_A': 17215, 'new_block_B': 9956,
        'previous_round_right_block': 3106}, 'recorded orbit event aggregates')
    return {'state_records': 4095, 'json_lines': len(rows), 'summaries': tables,
            'event_counts_from_serialized_orbits': dict(events),
            'endpoint_partition_cache_entries_retained_not_recomputed':
            rows[-1]['endpoint_partition_cache_entries'], 'stdout': meta_bytes(body),
            'limit': 'No literal transition, inverse formula, image predicate, mass bound, or scientific producer evaluated.'}


def main():
    seal_path = LANE / 'SHA256SUMS'
    require(meta_bytes(raw(seal_path))['sha256'] == SEAL, 'specified seal digest')
    declared = {}
    for line in raw(seal_path).decode().splitlines():
        digest, name = line.split('  ', 1)
        require(len(digest) == 64 and all(c in '0123456789abcdef' for c in digest), 'digest syntax')
        require(name not in declared and name != 'SHA256SUMS'
                and not Path(name).is_absolute() and '..' not in Path(name).parts, 'manifest path')
        declared[name] = digest
    actual = {p.relative_to(LANE).as_posix() for p in LANE.rglob('*') if p.is_file()}
    require(len(declared) == 155 and actual == set(declared) | {'SHA256SUMS'}, 'complete nonself seal')
    for path in LANE.rglob('*'):
        require(not path.is_symlink(), ('lane symlink', str(path)))
    for name, digest in declared.items():
        add(LANE / name)
        require(PHYSICAL[str(LANE / name)]['sha256'] == digest, ('sealed payload', name))
    add(seal_path)
    add(Path(__file__).absolute())
    add(HERE / 'INITIAL_CMP.actual.json')
    add(Path(sys.executable).resolve())
    add(CMP)
    controls = read(LANE / 'CONTROL_ROLES.json')
    roots = read(LANE / 'ROOT_REFERENCE_ROLES.json')
    require(len(controls) == 3 and len(roots) == 4, 'copy role census')
    aliases = {r['original_path']: r['copy_path'] for r in controls}
    initial = read(HERE / 'INITIAL_CMP.actual.json')
    require(len(initial) == 7, 'seven actual original cmp records')
    for row, role in zip(initial, controls + roots):
        cmd = "cmp -- '" + role['original_path'] + "' '" + role['copy_path'] + "'"
        require(row['cmd'] == cmd, 'initial cmp exact role argv')
        ret = row['native_return']
        require(ret['exit_code'] == 0 and ret['output'] == '' and 'session_id' not in ret,
                'initial actual native cmp exit')
    role_rows = []
    cmp_rows = []
    for role in controls + roots:
        original, copy = role['original_path'], role['copy_path']
        expected = {'bytes': role['bytes'], 'sha256': role['sha256']}
        require(Path(copy).is_relative_to(LANE), 'in-lane role copy')
        physical = aliases.get(original, original)
        add(physical, expected)
        add(copy, expected)
        if original not in aliases:
            argv = [str(CMP), '--', original, copy]
            result = subprocess.run(argv, cwd=ROOT, stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, timeout=30, check=False)
            cmp_rows.append({'argv': argv, 'exit': result.returncode,
                             'stdout_utf8': result.stdout.decode(), 'stderr_utf8': result.stderr.decode()})
            require(result.returncode == 0 and result.stdout == result.stderr == b'', 'fresh root-role cmp')
        role_rows.append({'original_path': original, 'consumed_physical_path': physical,
                          'copy_path': copy, **expected,
                          'historical_central_alias': original in aliases})
    command_rows, prior, failures = [], {}, []
    folders = sorted((LANE / 'commands').iterdir())
    require([int(p.name[:2]) for p in folders] == list(range(1, 21)), '20 command folders')
    required_names = {'attempt.json', 'inputs_before.json', 'inputs_after.json',
                      'stdout.raw', 'stderr.raw', 'receipt.json'}
    final_before = None
    for number, folder in enumerate(folders, 1):
        require({p.name for p in folder.iterdir()} == required_names, 'six artifacts per command')
        attempt, receipt = read(folder / 'attempt.json'), read(folder / 'receipt.json')
        before, after = read(folder / 'inputs_before.json'), read(folder / 'inputs_after.json')
        require(before == after and raw(folder / 'inputs_before.json') == raw(folder / 'inputs_after.json')
                and receipt['unchanged'] is True, ('before after', number))
        require(receipt['input_count'] == len(before), ('input count', number))
        for field in ('argv', 'cwd', 'role', 'started_epoch'):
            require(attempt[field] == receipt[field], ('attempt receipt', number, field))
        require(receipt['cwd'] == str(ROOT) and receipt['finished_epoch'] >= receipt['started_epoch']
                and attempt['timeout_seconds'] == 60 and receipt['timed_out'] is False, 'command timing/cwd')
        expected_exit = {8: 1, 13: 35}.get(number, 0)
        require(receipt['exit'] == expected_exit, ('preserved exit', number))
        for stream in ('stdout', 'stderr'):
            require(receipt[stream] == meta_bytes(raw(folder / (stream + '.raw'))), 'stream pin')
        if expected_exit:
            failures.append({'command': folder.name, 'exit': expected_exit,
                             'stdout_bytes': receipt['stdout']['bytes'], 'stderr_bytes': receipt['stderr']['bytes']})
        else:
            require(receipt['stderr']['bytes'] == 0, 'successful empty stderr')
        for logical, pin in before.items():
            # Historical paper reads are exactly the nine explicitly authorized keys.
            add(aliases.get(logical, logical), pin)
            if number < 20:
                require(logical not in prior or prior[logical] == pin, 'consistent prior identity')
                prior[logical] = pin
        command_rows.append({'name': folder.name, 'argv': receipt['argv'], 'role': receipt['role'],
                             'input_count': len(before), 'exit': receipt['exit'],
                             'stdout': receipt['stdout'], 'stderr': receipt['stderr'],
                             'before_after_raw_equal': True, 'timed_out': False})
        if number == 20:
            final_before = before
    require(len(prior) == 63, '63 prior declared identities')
    paper_keys = sorted(p for p in final_before if Path(p).is_relative_to(ROOT / 'papers'))
    require(len(paper_keys) == 9 and set(paper_keys) == {p for p in prior
            if Path(p).is_relative_to(ROOT / 'papers')}, 'nine historical paper hash keys')
    # Reconstruct run_final_audit.py's pre-command tree and unions, not its reported count.
    pre20 = {str(LANE / name) for name in declared if not name.startswith('commands/20_')}
    role_set = {r[k] for r in controls + roots for k in ('original_path', 'copy_path')}
    reconstructed = pre20 | set(prior) | role_set | {str(LANE / 'record.py'), str(Path(sys.executable).resolve())}
    require(len(pre20) == 149 and len(reconstructed) == 205
            and reconstructed == set(final_before), 'source-reconstructed final 205-input set')
    source_rows = []
    source_files = sorted((LANE / 'sources').glob('*.json'))
    require(len(source_files) == 10, 'ten web source payloads')
    for path in source_files:
        obj = read(path)
        require(set(obj) == {'role', 'request', 'result'} and isinstance(obj['role'], str)
                and isinstance(obj['request'], dict) and isinstance(obj['result'], str)
                and obj['result'], 'serialized web payload schema')
        require(set(obj['request']) <= {'search_query', 'open', 'find', 'screenshot', 'response_length'},
                'read-only web operation types')
        require(obj['request']['response_length'] == 'long', 'web response setting')
        source_rows.append({'file': str(path), 'role': obj['role'], 'request': obj['request'],
                            'payload_file': meta_bytes(raw(path)),
                            'result_utf8': meta_bytes(obj['result'].encode()),
                            'result_type': 'serialized_available_web_return_not_native_HTTP'})
    screenshot = read(source_files[-1])
    require('TimeoutError' in screenshot['result'] and 'Internal Error' in screenshot['result'],
            'actual screenshot failure preserved')
    code_names = ('record.py', 'mna_pilot.py', 'audit.py', 'run_final_audit.py', 'seal.py')
    asts = {name: ast.parse(raw(LANE / name).decode(), filename=name) for name in code_names}
    pilot = validate_pilot()
    # Evaluate only the original audit.py final print dictionary under documentary values.
    prints = [node for node in ast.walk(asts['audit.py']) if isinstance(node, ast.Call)
              and isinstance(node.func, ast.Name) and node.func.id == 'print']
    require(len(prints) == 1 and len(prints[0].args) == 1, 'single original audit print')
    dumps = prints[0].args[0]
    require(isinstance(dumps, ast.Call) and isinstance(dumps.func, ast.Attribute)
            and isinstance(dumps.func.value, ast.Name) and dumps.func.value.id == 'json'
            and dumps.func.attr == 'dumps' and len(dumps.args) == 1, 'original JSON emitter')
    options = {k.arg: ast.literal_eval(k.value) for k in dumps.keywords}
    require(options == {'sort_keys': True, 'indent': 2}, 'original JSON options')
    original_obj = safe_expr(dumps.args[0], {'current_meta': prior, 'role_counts': {
        'CONTROL_ROLES.json': 3, 'ROOT_REFERENCE_ROLES.json': 4}, 'source_files': source_files,
        'code_names': code_names, 'failure_rows': failures, 'OWN': LANE})
    reconstructed_stdout = (json.dumps(original_obj, **options) + '\n').encode()
    require(reconstructed_stdout == raw(LANE / 'commands/20_artifact_audit/stdout.raw'),
            'byte-for-byte original final stdout reconstruction')
    require(read(LANE / 'EXTRA_TOOL_RETURN.json')['exit_code'] == 2, 'auxiliary failure retained')
    before = dict(sorted(PHYSICAL.items()))
    after = {name: meta_bytes(raw(name)) for name in before}
    require(before == after, 'all physical consumed inputs unchanged after audit')
    print(json.dumps({'status': 'PASS', 'role': 'documentary_only_not_candidate_review',
        'sealed_payloads': 155, 'seal_sha256': SEAL, 'recorded_commands': command_rows,
        'prior_command_records': 19, 'prior_declared_identities': 63,
        'source_reconstructed_final_input_count': len(reconstructed), 'pre20_own_payloads': len(pre20),
        'historical_paper_paths_hash_only': paper_keys, 'copy_roles': role_rows,
        'fresh_root_reference_cmp': cmp_rows,
        'historical_central_cmp_evidence': str(HERE / 'INITIAL_CMP.actual.json'),
        'source_payloads': source_rows, 'pilot_record_consistency': pilot,
        'original_final_stdout_reconstruction': {'bytes_equal': True,
            **meta_bytes(reconstructed_stdout), 'utf8': reconstructed_stdout.decode(),
            'limit': 'Reconstructs all original source literals; not endorsement of runtime-inventory or protected-access claims.'},
        'preserved_nonzero_commands': failures, 'auxiliary_lookup_exit': 2,
        'physical_inputs_before': before, 'physical_inputs_after': after,
        'physical_input_count': len(before), 'physical_before_after_equal': True,
        'checks': CHECKS,
        'runtime_scope': {'interpreter': str(Path(sys.executable).resolve()),
            'flags': {'isolated': sys.flags.isolated, 'no_site': sys.flags.no_site,
                      'dont_write_bytecode': sys.flags.dont_write_bytecode, 'optimize': sys.flags.optimize},
            'limit': 'Explicit documentary file union and interpreter/cmp pins, not full imported-module/dynamic-library/environment capture.'},
        'limits': ['No archived command was reexecuted.', 'No pilot or verifier was imported or executed.',
                   'No web request, mathematical verdict, candidate admission, or central edit.',
                   'Sealed browser payload integrity does not authenticate native HTTP or repeat source retrieval.',
                   'Event totals aggregate recorded orbit partitions only; proof inequalities and cache size are not rechecked.']},
        sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
