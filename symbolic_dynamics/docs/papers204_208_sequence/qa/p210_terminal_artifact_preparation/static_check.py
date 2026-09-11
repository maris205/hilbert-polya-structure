#!/usr/bin/env python3
"""AST and named original DATA only; never import/execute the design reader."""
import ast
from collections import Counter
import gzip
from hashlib import sha256
import json
import os
from pathlib import Path

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
PREP = QA / 'p210_terminal_artifact_preparation'
PAPER = ROOT / 'papers/210-weakly-increasing-run-aggregation'
COUNTS, READ = Counter(), {}


def need(value, label):
    COUNTS[label] += 1
    if not value:
        raise AssertionError(label)


def raw(path):
    path = Path(path)
    value = path.read_bytes()
    key = {'real': str(path.resolve()), 'sha256': sha256(value).hexdigest(),
           'size': len(value),
           'symlink': os.readlink(path) if path.is_symlink() else None}
    need(str(path) not in READ or READ[str(path)] == key, 'named read stable')
    READ[str(path)] = key
    return value


def obj(path):
    value = raw(path)
    return json.loads(gzip.decompress(value) if str(path).endswith('.gz') else value)


def main():
    source = raw(PREP / 'inspect_p210_artifact.py')
    tree = ast.parse(source, filename='inspect_p210_artifact.py')
    functions = {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}
    need(all(isinstance(node, (ast.Expr, ast.Assign, ast.FunctionDef, ast.If))
             for node in tree.body), 'no executable top-level imports or setup')
    main_body = functions['main'].body
    need(len(main_body) == 1 and isinstance(main_body[0], ast.Raise) and
         isinstance(main_body[0].exc, ast.Call) and
         isinstance(main_body[0].exc.func, ast.Name) and
         main_body[0].exc.func.id == 'SystemExit', 'unconditional main rejection before reads/output')
    stubs = ('check_all_three_native_originals_and_source_runtime',
             'check_round0_round1_round2_physical_provenance_and_links',
             'check_terminal_builds_originals_and_complete_dependency_reuse',
             'check_six_actual_final_page_views', 'initial_artifact_gate',
             'distinct_lifecycle_followup')
    for name in stubs:
        body = functions[name].body
        need(len(body) == 1 and isinstance(body[0], ast.Raise), 'unbound phase has no acceptance path')
    prohibited = {'exec', 'eval', 'compile', '__import__', 'Popen', 'run', 'system',
                  'write_text', 'write_bytes', 'mkdir', 'unlink', 'rename', 'replace'}
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            name = node.func.id if isinstance(node.func, ast.Name) else (
                node.func.attr if isinstance(node.func, ast.Attribute) else None)
            need(name not in prohibited, 'no writer importer executor or native child call')
    for name in ('capture_roles.py', 'static_check.py'):
        ast.parse(raw(PREP / name), filename=name)
    contract_raw = raw(PREP / 'ACTUAL_ROLES.json')
    contract = json.loads(contract_raw)
    native = obj(PREP / 'ROLE_CAPTURE_NATIVE.actual.json')
    need(native['result']['exit_code'] == 0 and
         native['result']['output'].encode() == contract_raw,
         'complete native data capture stdout exactly retained')
    need(native['launch_result']['session_id'] == native['completion_call']['session_id'] == 45418 and
         native['launch_result']['output'] == '' and native['result']['chunk_id'] == 'be5a61',
         'actual data capture launch/completion identity')
    constants = {node.targets[0].id: ast.literal_eval(node.value) for node in tree.body
                 if isinstance(node, ast.Assign) and isinstance(node.targets[0], ast.Name)
                 and node.targets[0].id in ('STATE', 'FUTURE_ROLES')}
    need(constants['STATE'] == 'UNBOUND_DESIGN_SOURCE_ONLY', 'explicit unbound source state')
    need(set(contract['unbound_future_roles']) == set(constants['FUTURE_ROLES']) and
         all(value is None for value in contract['unbound_future_roles'].values()),
         'all seven future roles genuinely null')
    for path, expected in contract['named_actual_file_keys'].items():
        raw(path)
        need(READ[path] == expected, 'exact entire named role pin')
    base = obj(PREP / 'BASE_SELECTION.json')
    need(base['verbatim_copied_functions'] == [], 'new source no falsely asserted verbatim inheritance')
    for path, record in base['sources'].items():
        value = raw(path)
        need(len(value) == record['bytes'] and sha256(value).hexdigest() == record['sha256'] and
             len(value.splitlines()) == record['lines'], 'actual chosen source identity')
        ast.parse(value, filename=path)
    pair_results = {}
    old_fields = {'new_owned_session_requested', 'stdin', 'interrupted', 'process_group_settlement'}
    for role, expectation in (('author', (3639, 197471, 54, 9)),
                              ('a', (3634, 133978, 59, 10)), ('b', (3558, 51129, 59, 10))):
        record = contract['pairs'][role]
        pair = Path(record['directory'])
        need((record['known_keys'], record['checks_each'], record['payloads'],
              record['native_command_count']) == expectation, 'exact three accepted pair roles')
        before = obj(pair / 'INPUTS_BEFORE.json')
        after = obj(pair / 'INPUTS_AFTER.json')
        need(before == after and len(before) == expectation[0], 'whole archived strict interval')
        for path, key in before.items():
            need(path.startswith('/') and set(key) == {'resolved', 'sha256', 'bytes', 'symlink'} and
                 type(key['bytes']) is int and len(key['sha256']) == 64, 'all original strict rich schemas')
        result = obj(pair / 'RESULT.json')
        need([command['label'] for command in result['commands']] == record['native_labels'],
             'all actual ordered native command roles')
        for command in result['commands']:
            directory = pair / 'commands' / command['label']
            receipt = obj(directory / 'RECEIPT.json')
            attempt = obj(directory / 'ATTEMPT.json')
            specification = record['native_schemas_and_argv'][command['label']]
            need(sorted(receipt) == specification['receipt_fields'] and
                 sorted(attempt) == specification['attempt_fields'] and
                 receipt['argv'] == specification['argv'] and
                 command == dict(receipt, label=command['label']), 'whole actual native schema and argv')
            need((not (set(receipt) & old_fields)) if role != 'b' else old_fields <= set(receipt),
                 'old author A absent fields not upgraded to B schema')
            if role == 'b':
                settlement = receipt['process_group_settlement']
                need(set(settlement) == {'native_returncode', 'owned_pgid', 'owned_sid', 'quiescent',
                                         'remaining_members', 'signals'} and
                     settlement['native_returncode'] == 0 and settlement['quiescent'] is True and
                     settlement['remaining_members'] == settlement['signals'] == [] and
                     settlement['owned_pgid'] == settlement['owned_sid'] > 0,
                     'actual B owned settlement retained')
        pair_results[role] = {'known_keys': len(before), 'native_commands': len(result['commands']),
                              'current_host_revalidation': False}
    aliases = contract['exact_available_historical_aliases']
    need(len(aliases) == 6, 'four initial review aliases and two physical PRE_ROUND1 anchors')
    for alias in aliases:
        physical = alias['physical']
        raw(physical)
        need(READ[physical] == alias['physical_record'] and
             alias['original_sha256'] == READ[physical]['sha256'] and
             alias['original_size'] == READ[physical]['size'], 'exact physical historical-role bytes')
        provenance = obj(alias['provenance_role'])
        if '/frozen_round1/' in physical:
            anchor = provenance['anchors'][Path(physical).name]
            need(anchor['original_path'] == alias['logical'] and
                 anchor['sha256'] == alias['original_sha256'] and
                 str(PAPER / 'frozen_round1' / anchor['physical_path']) == physical,
                 'actual PRE_ROUND1 anchor provenance')
        else:
            recorded = provenance['initial_review_aliases']
            if isinstance(recorded, list):
                selected = [row for row in recorded if row['original_path'] == alias['logical']]
                need(len(selected) == 1 and selected[0]['sha256'] == alias['original_sha256'] and
                     selected[0]['physical_path'] == physical, 'actual A exact alias attestation')
            else:
                need(recorded[alias['logical']] == {'physical': physical,
                     'sha256': alias['original_sha256']}, 'actual B exact alias attestation')
    recipe = contract['actual_b_final_map_recipe']
    common = obj(recipe['common_path'])
    outer = obj(recipe['root_completion'])
    actual = json.loads(outer['result']['output'])
    extra = actual['current_read_keys_outside_B_common']
    need(len(common) == 121013 and len(extra) == 44 and not (set(common) & set(extra)),
         'whole B common plus exact disjoint extras')
    converted = {}
    for path, record in common.items():
        need(set(record) == {'resolved', 'sha256', 'bytes', 'symlink'}, 'all original common rich schemas')
        converted[path] = {'real': record['resolved'], 'sha256': record['sha256'],
                           'size': record['bytes'], 'symlink': record['symlink']}
    for path, record in extra.items():
        need(set(record) == {'real', 'sha256', 'size', 'symlink'}, 'all exact extra rich schemas')
        converted[path] = record
    encoded = json.dumps(converted, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode()
    need(len(converted) == recipe['complete_keys'] == 121057 and len(encoded) == recipe['canonical_bytes'] and
         sha256(encoded).hexdigest() == recipe['canonical_sha256'] ==
         actual['complete_current_read_map_canonical_sha256'], 'entire archived B map reconstructed not host revalidation')
    for path, record in recipe['old_control_roles_requiring_actual_Round2_history'].items():
        need(converted[path] == record, 'original B control keys retained no guessed Round2 alias')
    for name in ('README.md', 'SCOPE.md'):
        raw(PREP / name)
    for path in list(READ):
        raw(path)
    print(json.dumps({'status': 'PASS_AST_AND_NAMED_DATA_ONLY_UNBOUND_DESIGN',
        'checks': sum(COUNTS.values()), 'checks_by_kind': dict(sorted(COUNTS.items())),
        'named_files_reread': len(READ), 'named_file_keys': dict(sorted(READ.items())),
        'pairs': pair_results, 'common_plus_extra_complete_map_keys': len(converted),
        'main_unconditionally_rejects_before_role_host_reads_or_stdout': True,
        'all_seven_future_roles_null': True, 'reader_executed_or_imported': False,
        'old_programs_imported_or_executed': False, 'host_tree_walks': 0,
        'full_current_dependency_rehash_passes': 0, 'new_scientific_runs': 0,
        'new_builds': 0, 'new_page_views': 0, 'paper_or_five_acceptance': False,
        'external': 'OWNER_AMBER / HOLD_EXTERNAL'}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
