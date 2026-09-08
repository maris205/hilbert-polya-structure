#!/usr/bin/env python3
"""AST and sealed documentary-data checks ONLY; never run/import the receiver."""
import ast
from collections import Counter
from datetime import datetime, timezone
import gzip
from hashlib import sha256
import json
from pathlib import Path
import re

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
PREP = ROOT / 'docs/papers204_208_sequence/qa/p210_b_initial_reception_preparation'
B = ROOT / 'docs/papers204_208_sequence/reviews/p210_b'
R1 = ROOT / 'papers/210-weakly-increasing-run-aggregation/frozen_round1'
PINS, CHECKS = {}, Counter()


def ck(ok, name):
    CHECKS[name] += 1
    if not ok:
        raise AssertionError(name)


def raw(path):
    data = Path(path).read_bytes()
    PINS[str(path)] = {'bytes': len(data), 'sha256': sha256(data).hexdigest()}
    return data


def obj(path):
    data = raw(path)
    return json.loads(gzip.decompress(data) if str(path).endswith('.gz') else data)


def rows(path):
    records = [re.fullmatch(r'([0-9a-f]{64})  (.+)', v).groups() for v in raw(path).decode().splitlines()]
    ck(len(records) == len({v[1] for v in records}), 'unique_manifest_names')
    return {n: h for h, n in records}


def main():
    started = datetime.now(timezone.utc).isoformat()
    source = raw(PREP / 'receive_p210_b_initial.py').decode()
    tree = ast.parse(source)
    imports = {n.module for n in ast.walk(tree) if isinstance(n, ast.ImportFrom)}
    imports |= {a.name for n in ast.walk(tree) if isinstance(n, ast.Import) for a in n.names}
    ck(imports == {'collections', 'datetime', 'gzip', 'hashlib', 'json', 'os', 'pathlib', 're', 'sys', 'sysconfig', 'urllib.parse'}, 'only_stdlib_readonly_imports')
    forbidden = {'write_text', 'write_bytes', 'mkdir', 'unlink', 'rename', 'replace', 'rmdir', 'touch', 'chmod', 'chown', 'system', 'popen', 'Popen', 'run', 'call', 'check_call', 'check_output', 'exec', 'eval', '__import__', 'compile'}
    calls = [n for n in ast.walk(tree) if isinstance(n, ast.Call)]
    for call in calls:
        name = call.func.id if isinstance(call.func, ast.Name) else call.func.attr if isinstance(call.func, ast.Attribute) else None
        ck(name not in forbidden - {'replace'}, 'no_writer_process_dynamic_execution_call')
        if name == 'open':
            ck(len(call.args) == 1 and isinstance(call.args[0], ast.Constant) and call.args[0].value == 'rb', 'only_binary_read_file_open')
    functions = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
    ck(len(functions) == 17 and 'main' in functions, 'expected_complete_receiver_function_set')
    main_source = ast.get_source_segment(source, functions['main'])
    for token in ['initial-B-only', 'never_created_cache', 'force=True', '120840', '515', '63', '407', '509', '2461', 'accepted_delta', 'extra_read_keys_not_in_B_audit_ledger']:
        ck(token in main_source, 'required_main_contract_literal')
    ck('for path, expected in audit_inputs.items()' in main_source and 'for path, expected in original_reads.items()' in main_source, 'both_full_named_key_read_loops_present_not_executed')
    ck('print(json.dumps(main(), sort_keys=True, indent=2))' in source, 'single_json_stdout_entrypoint')
    package, frozen, input_pins = rows(B / 'SHA256SUMS'), rows(R1 / 'SHA256SUMS'), rows(B / 'INPUT_PINS.sha256')
    ck(PINS[str(B / 'SHA256SUMS')]['sha256'] == '81b5f97a6b25d6f9e82db87001da1a54668c01268038694d4b8a3b61006b02c3', 'exact_B_initial_seal')
    ck(PINS[str(R1 / 'SHA256SUMS')]['sha256'] == 'be54b79806d90f22037cee877f92074e744b2ef27bcc0b6b2e4f8dfa658446e0', 'exact_Round1_seal')
    ck(len(package) == 407 and len(frozen) == 508 and len(input_pins) == 509, 'actual_manifest_schema_counts')
    ck(set(input_pins) == {str((R1 / n).relative_to(ROOT)) for n in set(frozen) | {'SHA256SUMS'}}, 'declared_509_Round1_physical_roles')
    audit, seal = obj(B / 'AUDIT.actual.json'), obj(B / 'SEAL_AUDIT.actual.json')
    ck(audit['native_commands_checked'] == 62 and seal['native_receipts_checked'] == 63 and audit['accepted_delta'] is False, 'initial_audit_vs_completed_seal_census')
    ledger, roles, comparisons = obj(B / 'AUDIT_INPUTS.actual.json.gz'), obj(B / 'AUDIT_ROLES.actual.json'), obj(B / 'AUDIT_COMPARISONS.actual.json')
    ck(len(ledger) == 120840 and len(roles) == 50 and set().union(*map(set, roles.values())) == set(ledger), 'complete_120840_declared_role_union_structure_only')
    ck(all(set(v) == {'real', 'sha256', 'size', 'symlink'} for v in ledger.values()), 'all_declared_physical_key_shapes')
    ck(len(comparisons) == 515 and all(set(v) == {'equal', 'left', 'right', 'role', 'method'} and v['equal'] is True for v in comparisons), '515_comparison_row_structures_no_recomparison')
    native_counts = Counter()
    for row in seal['native_receipts']:
        folder = B / row['directory']
        attempt, result = obj(folder / 'ATTEMPT.json'), obj(folder / 'RESULT.json')
        ck(type(result['native_returncode']) is int and result['native_returncode'] == row['native_returncode'], 'actual_native_return_type_census_structure')
        native_counts[('inner' if 'start_ns' in attempt else 'outer', result['native_returncode'])] += 1
    ck(native_counts == {('inner', 0): 54, ('outer', 0): 7, ('outer', 1): 2}, '63_native_records_with_two_retained_outer_failures')
    ck(obj(B / 'native/audit02/stdout') == audit, 'completed_audit02_raw_json_schema_binding')
    ledgers = {}
    for label, count, config_count in [('produce01',3651,40),('pair01',3653,40),('build01',118353,61),('build02',118355,61)]:
        before = obj(B / label / 'INPUTS_BEFORE.json.gz')
        ck(set(before) == {'files','configuration','membership'} and len(before['files']) == count and len(before['configuration']) == config_count and before['membership'] == sorted(before['files']), 'complete_decoded_before_schema_not_current_host_hashes')
        ck(all(set(v) == {'lexists','exists','is_file','is_dir','resolved','symlink'} for v in before['configuration'].values()), 'configuration_record_shapes')
        extras = set(before['files']) - set(ledger)
        ck(len(extras) == (12 if label == 'build01' else 0), 'failed_build_only_twelve_extra_declared_roles')
        ck(all(Path(p).is_relative_to(B / 'build01') and Path(p).relative_to(B).as_posix() in package for p in extras), 'all_failed_extras_are_current_sealed_B_payload_names')
        ck(all(v == ledger[p] for p,v in before['files'].items() if p in ledger), 'declared_shared_before_keys_agree')
        if label != 'build01':
            ck(before == obj(B / label / 'INPUTS_AFTER.json.gz'), 'actual_complete_archived_before_after_equality')
        else:
            ck(not (B / label / 'INPUTS_AFTER.json.gz').exists() and not (B / label / 'REPORT.json').exists(), 'retained_incomplete_failed_build_no_success_schema')
        ledgers[label] = {'files': count, 'configuration': config_count, 'extra_sealed_names': len(extras)}
    fls = obj(B / 'build02/FLS_CLOSURE.json')
    ck(len(fls) == 2461 and all(set(v) == {'final_sha256','pass_number','path','role'} and Path(v['path']).name != 'main.pdf' for v in fls), '2461_fls_shapes_and_no_intermediate_pdf_inputs')
    ck({v['role'] for v in fls} == {'pinned_external','prior_product','same_pass_recorded_output'}, 'three_original_fls_roles')
    old_engine, new_engine = raw(B / 'instrumentation/evidence.py'), raw(B / 'instrumentation/evidence_build_v2.py')
    ck(new_engine == old_engine.replace(b'for v in cap.before.values()', b'for v in cap.before["files"].values()'), 'one_line_actual_build_adapter_correction')
    old_audit = raw(B / 'history/audit_package.attempt01.py')
    corrected = old_audit.replace(b"str(PAPER / 'SHA256SUMS')", b"str(PAPER / 'PAPER_MANIFEST.sha256')")
    corrected = corrected.replace(b"directory.name == 'build01'", b"directory.name in {'build01', 'audit01'}")
    ck(corrected == raw(B / 'audit_package.py'), 'two_actual_preserved_audit_corrections')
    ck(sha256(raw(B / 'history/verify.initial_reconstructed.py')).hexdigest() == obj(B / 'COMMITMENT.actual.json')['files']['verify.py'], 'declared_reconstructed_initial_source_role_not_new_prehash')
    prov = obj(R1 / 'ROUND1_PROVENANCE.json')
    ck(len(prov['round1_core_link_map']) == 57 and len(prov['acceptance_anchor_link_map']) == 14 and len(prov['anchors']) == 13, '71_explicit_frozen_link_and_13_anchor_schemas')
    ck(len(prov['prior_whole_manifest']['original_referent_pins']) == 987 and not prov['prior_whole_manifest']['current_whole_manifest_after_creation'], '987_historical_whole_not_current_schema')
    ck(len(seal['links']) == 17 and len(obj(B / 'VIEW_build02.actual.json')['pages']) == 6, '17_link_and_six_old_view_records_not_new_views')
    external = ROOT / 'docs/papers204_208_sequence/qa/P210_B_INITIAL_SEAL_NATIVE_RETURN.actual.json'
    ck(obj(external)['result']['exit_code'] == 0 and PINS[str(external)]['sha256'] == '8f0ae99ae62c571e0b8eb8371ee6e29c75a90059f49d0d2edbbf88132098b019', 'external_actual_native_seal_return_key')
    return {'status':'PASS_AST_AND_DOCUMENTARY_SCHEMA_ONLY_RECEIVER_NOT_EXECUTED', 'started_utc':started,
        'ended_utc':datetime.now(timezone.utc).isoformat(), 'checks':sum(CHECKS.values()), 'checks_by_kind':dict(CHECKS),
        'receiver_lines':len(source.splitlines()), 'receiver_source':PINS[str(PREP / 'receive_p210_b_initial.py')],
        'schema_ledgers':ledgers, 'native_record_census':{str(k):v for k,v in native_counts.items()},
        'comparison_role_census':dict(Counter(v['role'] for v in comparisons)),
        'actual_documentary_file_reads':len(PINS), 'documentary_input_pins':PINS,
        'receiver_imports_or_executions':0, 'old_program_executions':0, 'new_scientific_runs':0,
        'new_host_inventory_regeneration':0, 'new_current_120840_host_hash_passes':0, 'new_builds':0, 'new_views':0,
        'boundary':'This checks AST and actual archived data schemas, not prepared receiver acceptance. Root must independently execute receiver.'}


if __name__ == '__main__':
    print(json.dumps(main(), sort_keys=True, indent=2))
