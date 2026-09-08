#!/usr/bin/env python3
"""AST/data-only review. Does not import/execute the prepared receiver.

Consumes explicitly named documentary files, decoded recorded maps and native
records. Does not inventory/re-hash the host keys or execute old programs.
"""
import ast
from collections import Counter
import difflib
import gzip
from hashlib import sha256
import json
import os
from pathlib import Path
import re
import shlex
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
PREP = QA / 'p210_b_final_reception_preparation'
B = QA.parent / 'reviews/p210_b'
PAIR = QA / 'root_replays/p210_b_strict_pair_01'
READS, CHECKS = {}, Counter()

def ck(ok, label):
    CHECKS[label] += 1
    if not ok:
        raise AssertionError(label)

def raw(path):
    p = Path(path)
    data = p.read_bytes()
    row = {'sha256':sha256(data).hexdigest(),'bytes':len(data)}
    ck(str(p) not in READS or READS[str(p)] == row, 'documentary_read_stability')
    READS[str(p)] = row
    return data

def js(path):
    data = raw(path)
    return json.loads(gzip.decompress(data) if str(path).endswith('.gz') else data)

def digest(value):
    return sha256(json.dumps(value,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def functions(path):
    source = raw(path)
    tree = ast.parse(source)
    return tree, {n.name:ast.dump(n,include_attributes=False) for n in tree.body if isinstance(n,ast.FunctionDef)}

def rows(path):
    value = {}
    for line in raw(path).decode().splitlines():
        m = re.fullmatch(r'([0-9a-f]{64})  (.+)',line)
        ck(m is not None,'strict_manifest_rows')
        h,n = m.groups()
        ck(not Path(n).is_absolute() and '..' not in Path(n).parts and n not in value,'safe_unique_manifest_rows')
        value[n] = h
    return value

def main():
    ck(Path.cwd() == ROOT and sys.flags.isolated and sys.flags.no_site and sys.dont_write_bytecode
       and not sys.flags.optimize, 'static_source_only_interpreter')
    source = PREP / 'receive_p210_b_final.py'
    tree, functions_now = functions(source)
    old_initial, f_initial = functions(QA / 'p210_b_initial_reception_preparation/receive_p210_b_initial.py')
    old_strict, f_strict = functions(QA / 'p210_b_strict_receiver_revision_01/receive_p210_b_strict.py')
    saved = PREP / 'history/ROOT_READ_UNBOUND_750.py'
    raw(saved)
    ck(READS[str(saved)]['sha256'] == '5aa100d91f8e6daa568718a89d455041680e9a35fa06c9d6edcb819185567b62',
       'exact_root_read_750_source_retained')
    for before_path,diff_name in [(saved,'SOURCE_DIFF.diff'),
        (QA / 'p210_b_initial_reception_preparation/receive_p210_b_initial.py','SOURCE_FROM_INITIAL_DIFF.diff')]:
        expected = ''.join(difflib.unified_diff(raw(before_path).decode().splitlines(True),raw(source).decode().splitlines(True),
            fromfile=str(before_path.relative_to(ROOT)),tofile=str(source.relative_to(ROOT))))
        ck(raw(PREP / diff_name).decode() == expected,'entire_actual_new_source_diff')
    adaptation = js(PREP / 'SOURCE_ADAPTATION.json')
    ck(adaptation['final_source'] == READS[str(source)] and adaptation['receiver_executed'] is False,
       'complete_source_adaptation_identity')
    initial_names = ('file_key','pin','raw','obj','physical','stripped_links','current_configuration',
                     'configuration_scope','selected_tree_path','current_membership','native')
    strict_names = ('configuration_snapshot','current_resources')
    for name in initial_names:
        ck(functions_now[name] == f_initial[name], 'eleven_initial_helpers_exact_AST')
    for name in strict_names:
        ck(functions_now[name] == f_strict[name], 'two_strict_helpers_exact_AST')
    forbidden = {'subprocess','runpy','importlib','socket'}
    for node in ast.walk(tree):
        if isinstance(node,(ast.Import,ast.ImportFrom)):
            imported = [a.name.split('.')[0] for a in node.names] if isinstance(node,ast.Import) else [node.module.split('.')[0]]
            ck(not forbidden.intersection(imported),'no_old_program_or_child_imports')
        if isinstance(node,ast.Call):
            if isinstance(node.func,ast.Name):
                ck(node.func.id not in {'exec','eval','compile','__import__'},'no_dynamic_program_execution')
            if isinstance(node.func,ast.Attribute):
                ck(node.func.attr not in {'write_text','write_bytes','mkdir','unlink','rename','replace','Popen','run','system'},
                   'no_receiver_mutation_or_native_execution')
                if node.func.attr == 'open':
                    ck(node.args and isinstance(node.args[0],ast.Constant) and node.args[0].value == 'rb',
                       'only_read_binary_open')
    binding = js(PREP / 'INPUT_BINDINGS.json')
    ck(binding['stage'] == 'ACTUAL_FINAL_SCHEMA_BOUND_NOT_EXECUTED','actual_final_binding_stage')
    ck(binding['final_payload_count'] == 441 and binding['final_manifest_sha256'] ==
       '57b7b7919846e3ff5890543f0373439b03cc7f0cf0e896b9db38cd14d5171462','actual_final_441_identity')
    for name,wanted in binding['fixed_inputs'].items():
        raw(name)
        ck(READS[name] == wanted,'all_fixed_documentary_binding_keys')
    final = rows(B / 'SHA256SUMS')
    initial = rows(B / 'history/initial_before_delta/SHA256SUMS')
    ck(len(final) == 441 and len(initial) == 407,'actual_initial_final_manifest_census')
    physical = {p.relative_to(B).as_posix() for p in B.rglob('*') if p.is_file()}
    ck(set(final) | {'SHA256SUMS'} == physical,'static_final_package_name_membership')
    ck(set(initial) <= set(final) and {n for n in initial if initial[n] != final[n]} == {'DELTA.md'},
       'only_one_original_payload_digest_changed')
    preserved = js(B / 'INITIAL_PRESERVATION.actual.json')
    projected = {str((B / 'history/initial_before_delta' / n if n == 'DELTA.md' else B / n).relative_to(ROOT)):h
                 for n,h in initial.items()}
    projected[str((B / 'history/initial_before_delta/SHA256SUMS').relative_to(ROOT))] = binding['initial_manifest_sha256']
    ck(rows(B / 'INITIAL_PRESERVED_PINS.sha256') == projected and len(preserved['roles']) == 408,
       'all_408_actual_ROOT_relative_initial_roles')
    before = js(B / 'DELTA_INPUTS_BEFORE.json.gz')
    after = js(B / 'DELTA_INPUTS_AFTER.json.gz')
    extra = js(B / 'DELTA_AFTER_EXTRA_INPUTS.actual.json')
    ck(before == after and len(before) == 121013 and len(extra) == 3 and not set(before) & set(extra),
       'entire_decoded_common_plus_separate_actual_extra_schema')
    for name,row in (before | extra).items():
        ck(Path(name).is_absolute() and set(row) == {'sha256','bytes','resolved','symlink'},
           'all_actual_delta_rich_record_schemas')
    audit = js(B / 'AUDIT_INPUTS.actual.json.gz')
    known = js(PAIR / 'INPUTS_BEFORE.json')
    ck(len(audit) == 120840 and len(known) == 3558 and known == js(PAIR / 'INPUTS_AFTER.json'),
       'complete_original_B_and_strict_map_structure')
    root = {}
    for stem,row in binding['root_native'].items():
        launch = js(QA / (stem + '_LAUNCH.actual.json'))
        complete = js(QA / (stem + '_COMPLETION.actual.json'))
        ck(launch['result']['output'] == '' and launch['result']['session_id'] == complete['session_id'] == row['session'],
           'all_four_actual_root_session_bindings')
        ck(shlex.split(launch['command']) == row['command_argv'] and complete['result']['exit_code'] == 0,
           'all_four_actual_root_argv_native_bindings')
        root[stem] = json.loads(complete['result']['output'])
        ck(root[stem]['status'] == row['status'],'all_four_original_status_schemas')
    extra55 = root['P210_B_INITIAL_ORIGINALS_ROOT']['extra_read_keys_not_in_B_audit_ledger']
    extra75 = root['P210_B_STRICT_ORIGINALS_ROOT']['extra_read_keys_outside_original_known_ledger']
    ck(len(extra55) == 55 and len(extra75) == 75 and digest(audit | extra55) ==
       root['P210_B_INITIAL_ORIGINALS_ROOT']['all_current_read_keys_canonical_json_sha256'],
       'entire_original_initial_120895_logical_map')
    projected = {n:{k:r[k] for k in ('sha256','bytes')} for n,r in known.items()} | extra75
    ck(len(projected) == 3633 and digest(projected) == root['P210_B_STRICT_ORIGINALS_ROOT']['read_ledger_sha256'],
       'entire_original_strict_3633_logical_map')
    roles = {}
    for phase in ('before','after'):
        roles[phase] = js(B / ('DELTA_ROLES_' + phase.upper() + '.actual.json'))
        ck(set().union(*map(set,roles[phase].values())) == set(before) | (set(extra) if phase == 'after' else set()),
           'all_recorded_role_groups_complete_union')
        summary = js(B / ('DELTA_' + phase.upper() + '.actual.json'))
        ck(summary == binding['phase_summaries'][phase] ==
           js(B / ('native/delta_' + phase + '01/stdout')), 'actual_complete_phase_summary_and_native_stdout')
        ck(summary['checks'] == (1978529 if phase == 'before' else 1978541),'actual_phase_checks')
        runtime = js(B / ('DELTA_RUNTIME_' + phase.upper() + '.actual.json'))
        ck(set(runtime) == {'before','after'},'complete_recorded_runtime_intervals')
        observed = set()
        for sample in runtime.values():
            ck(sample['argv'] == binding['delta_native']['delta_' + phase + '01']['argv'],
               'actual_runtime_argv')
            names = {n for n in sample['modules'].values() if n}
            for line in sample['proc_maps'].splitlines():
                fields = line.split(None,5)
                if len(fields) == 6 and fields[5].startswith('/'):
                    names.add(fields[5])
            ck(names <= set(before),'all_recorded_runtime_module_map_names_in_common')
            observed.update(names)
        ck(observed == set(roles[phase]['delta_runtime_module_or_map']),'complete_raw_runtime_role_reconstruction')
    comparisons = js(B / 'DELTA_FULL_BYTE_COMPARISONS.actual.json')
    ck(len(comparisons) == 995 and Counter(r['role'] for r in comparisons) ==
       {'exact strict source copy':3,'rechecked actual native cmp operands':6,'complete actual strict output':2,
        'unchanged author seal alias':1,'unchanged frozen author seal':1,'unchanged all author input bytes':489,
        'unchanged all Round0 core bytes':493},'all_995_actual_comparison_role_schema')
    closure = js(B / 'DELTA_CLOSURE.actual.json')
    ck(closure['native_record_count'] == len(closure['native_records']) == 66 and len(closure['links']) == 29,
       'actual_final_66_native_29_link_schema')
    for name,row in binding['delta_native'].items():
        attempt = js(B / 'native' / name / 'ATTEMPT.json')
        result = js(B / 'native' / name / 'RESULT.json')
        ck(attempt['argv'] == row['argv'] and result['native_returncode'] == row['native_returncode'] == 0
           and all(result[k] == v for k,v in attempt.items()),'all_three_actual_delta_native_field_bindings')
        for stream in ('stdout','stderr'):
            raw(B / 'native' / name / stream)
            ck(READS[str(B / 'native' / name / stream)] == result[stream], 'all_six_complete_delta_streams')
        ck(result['pid'] == result['owned_pgid'] == result['owned_sid'] > 0
           and result['settlement'] == {'quiescent':True,'remaining_members':[]},'all_three_actual_settled_groups')
    findings = js(B / 'CURRENT_FINDINGS.json')
    ck(findings['accepted_delta'] is True and findings['same_actual_initial_reviewer'] is True
       and findings['accepted_response_sha256'] == binding['response_sha256']
       and findings['current_open_counts'] == {'Critical':0,'Major':0,'Minor':0}, 'actual_same_B_final_decision')
    external = js(binding['external_final_seal']['path'])
    ck(external == binding['external_final_seal']['record'] and external['result']['exit_code'] == 0,
       'actual_external_seal_return_not_future_placeholder')
    failure = js(PREP / 'DRAFT_PARSE_FAILURE_NATIVE.actual.json')
    bad = raw(PREP / 'history/DRAFT_PARSE_FAILURE_SOURCE.py')
    ck(sha256(bad).hexdigest() == failure['source']['sha256'] and len(bad) == failure['source']['bytes']
       and failure['result']['exit_code'] == 1,'original_AST_only_failure_source_and_native_retained')
    try:
        ast.parse(bad)
    except SyntaxError as error:
        ck(error.lineno == 597 and 'was never closed' in str(error),'historical_AST_only_error_exact')
    else:
        raise AssertionError('historical parse failure unexpectedly absent')
    report = {'status':'PASS_AST_DATA_ONLY_FINAL_RECEIVER_PREPARATION_NOT_RECEIVER_EXECUTION',
        'checks':sum(CHECKS.values()),'checks_by_kind':dict(CHECKS),'documentary_inputs':READS,
        'documentary_file_count':len(READS),'source':READS[str(source)],'source_lines':len(raw(source).splitlines()),
        'verbatim_accepted_helpers':{'initial':list(initial_names),'strict':list(strict_names)},
        'final_B_payloads':441,'original_B_payloads':407,'common_decoded_records':len(before),'after_extra_records':len(extra),
        'original_B_record_schema_count':len(audit),'original_strict_record_schema_count':len(known),
        'actual_added_native_records':3,'old_native_records_not_reexecuted':63,'final_native_census':66,
        'actual_phase_checks':{'before':1978529,'after':1978541},'actual_comparison_operand_records':995,
        'old_receiver_or_B_writer_imports_executions':0,'prepared_receiver_executions':0,
        'current_host_inventory_or_full_dependency_hash_passes':0,'science_builds_views':0,
        'old_A_nested_host_ledger_expansions':0,'output_scope':'Source/record validation only; root must independently read and execute the prepared receiver before Round2.',
        'owner':'OWNER_AMBER','external':'HOLD_EXTERNAL'}
    print(json.dumps(report,sort_keys=True,indent=2))

if __name__ == '__main__':
    main()
