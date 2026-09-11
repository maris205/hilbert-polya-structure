#!/usr/bin/python3.10
"""B's read-only documentary intake. No submitted import or science recomputation.

Reads every byte and recursively visits every parsed JSON node in the two
closed binding packages, both whole execution trees, root reception/closure,
and the adopted canonical. It checks file evidence, not mathematical claims.
Only stdout is written. A real caller must retain the native tool envelope.
"""
import hashlib
import json
import math
import os
from pathlib import Path
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASE = ROOT / 'docs/papers211_215_sequence'
B = BASE / 'reviews/p211_b'
QA = BASE / 'qa'
READ = {}
PARSED = {}
checks = 0


def need(condition, message):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(message)


def raw(path):
    path = Path(path)
    data = path.read_bytes()
    row = {'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest(),
           'resolved': str(path.resolve()),
           'symlink': os.readlink(path) if path.is_symlink() else None}
    if str(path) in READ:
        need(READ[str(path)] == row, 'changed while receiving: ' + str(path))
    READ[str(path)] = row
    return data


def pairs(rows):
    out = {}
    for key, value in rows:
        if key in out:
            raise ValueError('duplicate JSON key ' + key)
        out[key] = value
    return out


def bad_constant(value):
    raise ValueError('nonfinite JSON constant ' + value)


def traverse(value, census):
    tag = type(value).__name__
    census[tag] = census.get(tag, 0) + 1
    if type(value) is dict:
        for key, item in value.items():
            need(type(key) is str, 'nonstring JSON key')
            census['object_keys'] = census.get('object_keys', 0) + 1
            traverse(item, census)
    elif type(value) is list:
        for item in value:
            traverse(item, census)
    elif type(value) is float:
        need(math.isfinite(value), 'nonfinite JSON float')
    else:
        need(value is None or type(value) in (str, int, bool), 'unknown JSON type')


def document(path):
    path = Path(path)
    data = raw(path)
    value = json.loads(data.decode('utf-8'), object_pairs_hook=pairs,
                       parse_constant=bad_constant)
    census = {}
    traverse(value, census)
    PARSED[str(path)] = census
    return value


def manifest(path, exact=True):
    path = Path(path)
    rows = {}
    for line in raw(path).decode('ascii').splitlines():
        need(len(line) > 66 and line[64:66] == '  ', 'manifest syntax')
        digest, name = line[:64], line[66:]
        need(len(digest) == 64 and all(c in '0123456789abcdef' for c in digest), 'digest')
        need(name not in rows and not Path(name).is_absolute()
             and '..' not in Path(name).parts, 'unsafe/duplicate member')
        target = path.parent / name
        need(target != path and target.is_file() and not target.is_symlink(), 'member kind')
        need(hashlib.sha256(raw(target)).hexdigest() == digest, 'manifest mismatch ' + name)
        rows[name] = digest
    if exact:
        actual = {str(p.relative_to(path.parent)) for p in path.parent.rglob('*') if p.is_file()}
        need(actual == set(rows) | {path.name}, 'nonself complete membership ' + str(path))
    return {'path': str(path), 'payloads': len(rows), **READ[str(path)]}


def tree(path):
    path = Path(path)
    for member in sorted(path.rglob('*')):
        need(not member.is_symlink(), 'unexpected tree symlink')
        if member.is_file():
            if member.suffix == '.json':
                document(member)
            else:
                raw(member)


def rich_inputs(path):
    value = document(path)
    need(type(value) is dict, 'rich input map')
    for spelling, expected in value.items():
        need(Path(spelling).is_absolute(), 'absolute input spelling')
        raw(spelling)
        need(READ[spelling] == expected, 'complete rich input mismatch: ' + spelling)
    return len(value)


def main():
    need(len(sys.argv) == 1, 'no caller-controlled inputs')
    seals = []
    packages = []
    command_rows = []
    bindings = []
    for mode, expected_payloads, expected_inputs, expected_commands in (
            ('initial', 77, 297, 7), ('pair', 104, 317, 11)):
        binding_dir = QA / ('p211_b_' + mode + '_binding')
        execution = QA / 'root_replays' / ('p211_b_' + mode + '_01')
        tree(binding_dir)
        tree(execution)
        seals.append(manifest(binding_dir / 'SHA256SUMS'))
        top = manifest(execution / 'SHA256SUMS')
        need(top['payloads'] == expected_payloads, 'execution payload census')
        seals.append(top)
        for child_seal in sorted(execution.rglob('SHA256SUMS')):
            if child_seal.parent != execution:
                seals.append(manifest(child_seal))
        inputs = rich_inputs(binding_dir / 'INPUTS_AT_BINDING.json')
        need(inputs == expected_inputs, 'binding input census')
        bindings.append(document(binding_dir / 'BINDING.json'))
        receipts = sorted(execution.glob('*/commands/*/RECEIPT.json'))
        need(len(receipts) == expected_commands, 'native command census')
        for receipt_path in receipts:
            receipt = document(receipt_path)
            attempt = document(receipt_path.with_name('ATTEMPT.json'))
            need(receipt['exit_code'] == 0 and receipt['failure'] is None
                 and receipt['status'] == 'COMPLETED' and receipt['streams_complete'] is True
                 and receipt['timed_out'] is False and receipt['interrupted'] is False,
                 'unsuccessful native command')
            for stream in ('stdout', 'stderr'):
                stream_path = receipt_path.with_name(stream + '.raw')
                raw(stream_path)
                need({k: READ[str(stream_path)][k] for k in ('bytes', 'sha256')}
                     == receipt[stream], 'receipt raw stream mismatch')
            settled = receipt['process_group_settlement']
            need(settled['quiescent'] is True and settled['remaining_members'] == []
                 and settled['signals'] == [], 'owned group unsettled')
            command_rows.append({'mode': mode, 'receipt': str(receipt_path),
                                 'whole_attempt': attempt, 'whole_receipt': receipt})
        packages.append({'mode': mode, 'rich_inputs': inputs,
                         'execution_payloads': expected_payloads,
                         'native_commands': len(receipts)})
    tree(QA / 'p211_b_root_reception')
    tree(QA / 'p211_b_binding_closure')
    raw(QA / 'P211_B_RUNTIME_RECEPTION.md')
    need(set(bindings[0]) == set(bindings[1]), 'binding key sets')
    differences = {key: {'before': bindings[0][key], 'after': bindings[1][key]}
                   for key in bindings[0] if bindings[0][key] != bindings[1][key]}
    need(differences == document(QA / 'p211_b_pair_binding/EXACT_INITIAL_TO_PAIR_DELTA.json'),
         'exact initial/pair binding delta')
    canonical_path = B / 'CANONICAL.json'
    canonical_raw = raw(canonical_path)
    need(len(canonical_raw) == 3053387 and hashlib.sha256(canonical_raw).hexdigest()
         == '10daa982cc755162b09c4e1e4783343f4ea25ca4c464e2123693e2156b810658',
         'accepted canonical physical bytes')
    canonical = document(canonical_path)
    need(canonical_raw == (json.dumps(canonical, sort_keys=True, separators=(',', ':'),
                                     ensure_ascii=True, allow_nan=False) + '\n').encode('ascii'),
         'complete compact serialization')
    equality = []
    for mode, labels in (('initial', ('01',)), ('pair', ('01', '02'))):
        for label in labels:
            output = QA / 'root_replays' / ('p211_b_' + mode + '_01') / 'recorder/commands' / ('03_verify_' + label) / 'stdout.raw'
            need(raw(output) == canonical_raw, 'whole raw canonical equality')
            parsed = document(output)
            need(parsed == canonical, 'whole parsed output equality')
            equality.append(str(output))
    # Existing values are extracted verbatim, not recomputed as new science.
    saved_totals = {k: canonical[k] for k in ('schema', 'role', 'carrier_count',
                     'total_states', 'total_targets', 'total_edges', 'check_counts',
                     'carrier_check_total', 'hand_attack_checks', 'check_total', 'status', 'scope')}
    seals.append(manifest(B / 'PREPARATION_SHA256SUMS', exact=False))
    result = {'status': 'DOCUMENTARY_INTAKE_COMPLETE_NOT_NEW_SCIENCE_OR_INFRASTRUCTURE_CERTIFICATION',
              'scientific_executions': 0, 'submitted_imports': 0, 'builds': 0,
              'documentary_checks': checks, 'packages': packages, 'seals': seals,
              'binding_changed_keys': sorted(differences), 'saved_totals': saved_totals,
              'complete_raw_equals_canonical': equality,
              'canonical_json_node_census': PARSED[str(canonical_path)],
              'actual_native_commands': command_rows, 'whole_parsed_json_censuses': PARSED,
              'read_inputs': READ, 'read_paths': len(READ)}
    sys.stdout.write(json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + '\n')


if __name__ == '__main__':
    main()
