#!/usr/bin/env python3
"""Source AST and existing canonical schema only; no reviewed program executes."""
import ast
from hashlib import sha256
import json
from pathlib import Path

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
HERE = QA / 'p210_b_strict_receiver_static_review'
PINS, CHECKS = {}, []


def raw(path):
    data = Path(path).read_bytes()
    PINS[str(path)] = {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}
    return data


def check(ok, label):
    CHECKS.append(label)
    if not ok:
        raise AssertionError(label)


def functions(tree):
    return {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}


def dictkeys(node):
    return {n.value for n in node.keys if isinstance(n, ast.Constant) and isinstance(n.value, str)}


def assignment(function, name):
    return next(n.value for n in ast.walk(function) if isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id == name for t in n.targets))


def consumed(function, name):
    return {n.slice.value for n in ast.walk(function) if isinstance(n, ast.Subscript) and isinstance(n.value, ast.Name) and n.value.id == name and isinstance(n.slice, ast.Constant) and isinstance(n.slice.value, str)}


def main():
    original = raw(HERE / 'inspect_p210_b_strict_pair.before_root_followup.py')
    live = raw(QA / 'inspect_p210_b_strict_pair.py')
    check(sha256(original).hexdigest() == '7234bba399e556b5d22560412785f2d64886471642baf53b7544ae9b41d6053a', 'exact_reviewed_232_line_source_key')
    check(original == live, 'exact_live_and_preserved_source_before_root_followup')
    old = raw(QA / 'inspect_p210_a_strict_pair.py')
    runner = raw(QA / 'p210_b_strict_preparation/run_pair.py')
    check(sha256(runner).hexdigest() == 'bacc8bf0351bdfbcc2bc671cd61131d6382fe5caccd00f02e3988afbf1d066d1', 'exact_623_line_generator_key')
    b, a, r = map(lambda data: functions(ast.parse(data)), (original, old, runner))
    check(set(b) == set(a) and [n for n in b if ast.dump(b[n]) != ast.dump(a[n])] == ['main'], 'eight_original_helpers_unchanged_only_main_adapted')
    receipt_fields = dictkeys(assignment(r['command'], 'entry')) | dictkeys(assignment(r['command'], 'receipt'))
    settlement_fields = dictkeys(next(n.value for n in r['settle_group'].body if isinstance(n, ast.Return)))
    child_fields = dictkeys(next(n for n in ast.walk(r['child']) if isinstance(n, ast.Dict) and 'parameter_locator' in dictkeys(n)))
    schemas = {'receipt': receipt_fields, 'settlement': settlement_fields, 'observed': child_fields}
    for name, producer in schemas.items():
        check(consumed(b['main'], name) <= producer, 'all_' + name + '_literal_consumers_are_actual_producer_fields')
    for forbidden in [b"receipt['start_new_session']", b"settlement['leader_returncode']", b"data['parameters']"]:
        check(forbidden not in original, 'incorrect_old_field_spelling_absent')
    check(b"new_owned_session_requested': True" in runner and b"'native_returncode':p.returncode" in runner and b"'owned_sid':p.pid" in runner, 'actual_owned_session_generator_fields')
    package = ROOT / 'docs/papers204_208_sequence/reviews/p210_b'
    canonical, parameters = [json.loads(raw(package / n)) for n in ['CANONICAL.json', 'PARAMETERS.json']]
    check(canonical['checks'] == 51129 and canonical['states'] == 4095 and sum(len(m['states']) for m in canonical['census']) == 4095, 'actual_B_canonical_checks_and_state_rows')
    check(canonical['representation'] == parameters['carrier'] and canonical['edge_construction'] == parameters['edges'], 'actual_B_representation_and_edge_fields_not_parameters_object')
    check(parameters['masses'] == [m['mass'] for m in canonical['census']] == list(range(1,13)) and sum(len(m['triangular_codes']) for m in canonical['census']) == 265, 'actual_original_mass_and_triangle_box')
    check(b"sys.argv = [str(source)]" in runner and b"'scientific_argv': [str(source)], 'parameter_locator': 'sibling of scientific __file__'" in runner, 'actual_single_argv_sibling_parameter_interface')
    unparsed = ['RUN_ENTERED.json', 'SOURCE_ONLY_INITIAL.json', 'COMMAND_CLOSURE.json']
    check(all(n.encode() in runner and n.encode() not in original for n in unparsed), 'three_generated_records_only_hash_read_by_current_inspector')
    check(b'ROOT_B_OWNED_NATIVE_RUNNING' in runner and b"native = json.loads(completion['output'])" in original, 'conditional_heartbeat_and_single_json_parser_boundary_not_actual_failure')
    prior_static = json.loads(raw(QA / 'P210_B_STRICT_ORIGINALS_PREPARATION.actual.json'))
    check(prior_static['result']['exit_code'] == 0 and json.loads(prior_static['result']['output'])['source'] == PINS[str(QA / 'inspect_p210_b_strict_pair.py')], 'actual_prior_static_return_bound_to_reviewed_source')
    return {'status':'STATIC_SCHEMA_REVIEW_WITH_CONCRETE_ROOT_FOLLOWUP_OBLIGATIONS_NO_EXECUTION',
        'checks':len(CHECKS), 'checks_passed':CHECKS, 'input_pins':PINS,
        'producer_and_consumer_fields':{n:{'producer':sorted(v),'literal_consumers':sorted(consumed(b['main'],n))} for n,v in schemas.items()},
        'unchanged_helpers':sorted(set(b)-{'main'}), 'hash_only_generated_records':unparsed,
        'actual_scientific_executions':0,'inspector_or_generator_imports':0,'inspector_or_generator_executions':0,
        'root_sources_changed':False,'host_inventory_regeneration':0,'old_A_deep_ledger_expansion':0,
        'meaning':'No current field-name incompatibility found in the reviewed consumer groups. Root must close documented original-reception obligations before first inspector execution; no pair or receiver PASS asserted.'}


if __name__ == '__main__':
    print(json.dumps(main(), sort_keys=True, indent=2))
