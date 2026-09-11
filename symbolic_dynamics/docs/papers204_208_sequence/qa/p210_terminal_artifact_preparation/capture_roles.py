#!/usr/bin/env python3
"""Named-file DATA capture only. No old source execution/import or host walk.

Prints actual unbound role JSON to stdout; caller saves via apply_patch.
"""
from hashlib import sha256
import gzip
import json
import os
from pathlib import Path

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
PAPER = ROOT / 'papers/210-weakly-increasing-run-aggregation'
REVIEW = QA.parent / 'reviews'
PINS = {}


def raw(path):
    path = Path(path)
    value = path.read_bytes()
    key = {'real': str(path.resolve()), 'sha256': sha256(value).hexdigest(),
           'size': len(value),
           'symlink': os.readlink(path) if path.is_symlink() else None}
    assert str(path) not in PINS or PINS[str(path)] == key
    PINS[str(path)] = key
    return value


def obj(path):
    value = raw(path)
    return json.loads(gzip.decompress(value) if str(path).endswith('.gz') else value)


def capture_pair(role, expected_keys, checks, payloads):
    base = QA / ('root_replays/p210_' + role + '_strict_pair_01')
    before, after = (obj(base / ('INPUTS_' + phase + '.json'))
                     for phase in ('BEFORE', 'AFTER'))
    assert before == after and len(before) == expected_keys
    assert all(set(value) == {'bytes', 'resolved', 'sha256', 'symlink'}
               for value in before.values())
    resources = obj(base / 'RESOURCE_NAMES_BEFORE.json')
    assert resources == obj(base / 'RESOURCE_NAMES_AFTER.json') and len(resources) == 3121
    config = obj(base / 'CONFIGURATION_BEFORE.json')
    assert config == obj(base / 'CONFIGURATION_AFTER.json') and len(config) == 41
    result = obj(base / 'RESULT.json')
    capsule = obj(base / 'SOURCE_ONLY_INITIAL.json')
    assert set(capsule) == ({'run_pair.py', 'verify.py'} if role == 'author' else
                            {'run_pair.py', 'verify.py', 'PARAMETERS.json'})
    for value in capsule.values():
        assert set(value) == {'bytes', 'copy', 'origin', 'sha256'}
        assert raw(value['copy']) == raw(value['origin'])
    seal = raw(base / 'SHA256SUMS')
    assert len(seal.splitlines()) == payloads
    closure = obj(base / 'PACKAGE_AND_PREPARATION_CLOSURE.json')
    assert set(closure) == {'before', 'after'} and closure['before'] == closure['after']
    cmd_closure = obj(base / 'COMMAND_CLOSURE.json')
    commands = result['commands']
    expected_commands = 9 if role == 'author' else 10
    assert len(commands) == expected_commands == cmd_closure['command_count']
    labels = []
    native_schemas = {}
    for command in commands:
        label = command['label']
        labels.append(label)
        directory = base / 'commands' / label
        attempt = obj(directory / 'ATTEMPT.json')
        receipt = obj(directory / 'RECEIPT.json')
        assert command == dict(receipt, label=label)
        assert receipt['exit_code'] == receipt['wrapper_exit_code'] == 0
        assert receipt['streams_complete'] is True
        assert receipt['status'] == 'COMPLETED' and receipt['failure'] is None
        assert not receipt['timed_out'] and receipt['spawned'] is True
        for stream in ('stdout', 'stderr'):
            value = raw(directory / (stream + '.raw'))
            assert receipt[stream] == {'bytes': len(value), 'sha256': sha256(value).hexdigest()}
        native_schemas[label] = {'attempt_fields': sorted(attempt),
                                'receipt_fields': sorted(receipt),
                                'argv': receipt['argv'],
                                'timeout_seconds': receipt['timeout_seconds']}
    observations = {}
    for index in ('01', '02'):
        observation = obj(base / ('observations/child_' + index + '.json'))
        observations[index] = {
            'source_fields': sorted(observation),
            'scientific_argv_field_present': 'scientific_argv' in observation,
            'scientific_argv': observation.get('scientific_argv'),
            'parameter_locator_field_present': 'parameter_locator' in observation,
            'parameter_locator': observation.get('parameter_locator'),
            'parameters_field_present': 'parameters' in observation,
            'parameters': observation.get('parameters'),
            'before_argv': observation['before']['argv'],
            'after_argv': observation['after']['argv'],
        }
    for name in ('LINKED_RUNTIME.json', 'RUN_ENTERED.json',
                 'observations/parent_before.json', 'observations/parent_after.json'):
        raw(base / name)
    return {'directory': str(base), 'checks_each': checks,
            'known_keys': expected_keys, 'resource_names': len(resources),
            'configuration_names': len(config), 'payloads': payloads,
            'manifest_sha256': sha256(seal).hexdigest(),
            'known_schema': ['bytes', 'resolved', 'sha256', 'symlink'],
            'native_command_count': expected_commands, 'native_labels': labels,
            'native_schemas_and_argv': native_schemas,
            'source_only_initial_actual': capsule, 'child_actual_fields': observations,
            'recorded_interval_equal': True, 'current_host_revalidation': False,
            'old_receipt_owned_settlement_fields_absent': role in ('author', 'a')}


def main():
    pairs = {role: capture_pair(role, known, checks, payloads)
             for role, known, checks, payloads in
             (('author', 3639, 197471, 54), ('a', 3634, 133978, 59),
              ('b', 3558, 51129, 59))}
    named_root = (
        'P210_AUTHOR_STRICT_ROOT_INSPECTION.md',
        'P210_AUTHOR_STRICT_LAUNCH.actual.json', 'P210_AUTHOR_STRICT_COMPLETION.actual.json',
        'P210_AUTHOR_STRICT_ROOT_LAUNCH.actual.json', 'P210_AUTHOR_STRICT_ROOT_COMPLETION.actual.json',
        'P210_A_STRICT_ROOT_INSPECTION.md',
        'P210_A_STRICT_LAUNCH.actual.json', 'P210_A_STRICT_COMPLETION.actual.json',
        'P210_A_STRICT_ROOT_LAUNCH.actual.json', 'P210_A_STRICT_ROOT_COMPLETION.actual.json',
        'P210_A_ROOT_DELTA_INSPECTION.md', 'P210_A_ROOT_DELTA_INSPECTION.actual.json',
        'P210_B_ROOT_INITIAL_INSPECTION.md',
        'P210_B_STRICT_ROOT_LAUNCH.actual.json', 'P210_B_STRICT_ROOT_COMPLETION.actual.json',
        'P210_B_STRICT_ORIGINALS_ROOT_LAUNCH.actual.json',
        'P210_B_STRICT_ORIGINALS_ROOT_COMPLETION.actual.json',
        'P210_B_ROOT_DELTA_INSPECTION.md', 'P210_B_ROOT_DELTA_INSPECTION.actual.json',
        'P210_B_FINAL_ORIGINALS_ROOT_LAUNCH.actual.json',
        'P210_B_FINAL_ORIGINALS_ROOT_COMPLETION.actual.json',
        'P210_B_FINAL_ORIGINALS_METADATA_ROOT.actual.json',
        'P210_ROUND0_ROOT_INSPECTION.md', 'P210_ROUND1_ROOT_INSPECTION.md')
    for name in named_root:
        raw(QA / name)
    aliases = []
    for role in ('a', 'b'):
        for name in ('DELTA.md', 'SHA256SUMS'):
            logical = REVIEW / ('p210_' + role) / name
            physical = REVIEW / ('p210_' + role) / 'history/initial_before_delta' / name
            raw(physical)
            key = PINS[str(physical)]
            aliases.append({'logical': str(logical), 'original_sha256': key['sha256'],
                            'original_size': key['size'], 'physical': str(physical),
                            'physical_record': key,
                            'provenance_role': str(QA / ('P210_' + role.upper() + '_ROOT_DELTA_INSPECTION.actual.json'))})
    for logical, name in (('ROOT_LIFECYCLE.md', 'PRE_ROUND1_ROOT_LIFECYCLE.md'),
                          ('PAPER_MANIFEST.sha256', 'PRE_ROUND1_PAPER_MANIFEST.sha256')):
        physical = PAPER / 'frozen_round1/ROUND1_ACCEPTANCE' / name
        raw(physical)
        key = PINS[str(physical)]
        aliases.append({'logical': str(PAPER / logical), 'original_sha256': key['sha256'],
                        'original_size': key['size'], 'physical': str(physical),
                        'physical_record': key,
                        'provenance_role': str(PAPER / 'frozen_round1/ROUND1_PROVENANCE.json')})
    for name in ('frozen_round0/SHA256SUMS', 'frozen_round1/SHA256SUMS',
                 'frozen_round1/ROUND1_PROVENANCE.json'):
        raw(PAPER / name)
    outer = obj(QA / 'P210_B_FINAL_ORIGINALS_ROOT_COMPLETION.actual.json')
    actual_b = json.loads(outer['result']['output'])
    common_path = REVIEW / 'p210_b/DELTA_INPUTS_BEFORE.json.gz'
    common = obj(common_path)
    extras = actual_b['current_read_keys_outside_B_common']
    assert len(common) == 121013 and len(extras) == 44 and not (set(common) & set(extras))
    reconstructed = {name: {'real': value['resolved'], 'sha256': value['sha256'],
                             'size': value['bytes'], 'symlink': value['symlink']}
                     for name, value in common.items()}
    reconstructed.update(extras)
    encoded = json.dumps(reconstructed, sort_keys=True, separators=(',', ':'), ensure_ascii=True).encode()
    assert sha256(encoded).hexdigest() == actual_b['complete_current_read_map_canonical_sha256']
    b_old_controls = {str(PAPER / name): reconstructed[str(PAPER / name)]
                      for name in ('ROOT_LIFECYCLE.md', 'PAPER_MANIFEST.sha256')}
    result = {
        'schema': 'p210-terminal-artifact-unbound-actual-role-capture-v1',
        'stage': 'UNBOUND_DESIGN_ONLY', 'reader_executed_or_imported': False,
        'new_scientific_runs': 0, 'new_builds': 0, 'new_page_views': 0,
        'host_tree_walks_or_dependency_rehash_passes': 0,
        'scope': 'Named documentary/source/stream files read; archived maps decoded. No full host or paper copy. No current dependency reuse verdict.',
        'pairs': pairs, 'exact_available_historical_aliases': aliases,
        'actual_b_final_map_recipe': {
            'root_completion': str(QA / 'P210_B_FINAL_ORIGINALS_ROOT_COMPLETION.actual.json'),
            'common_path': str(common_path), 'common_keys': len(common),
            'conversion': {'real': 'resolved', 'sha256': 'sha256', 'size': 'bytes', 'symlink': 'symlink'},
            'extra_pointer': 'result.output JSON -> current_read_keys_outside_B_common',
            'extra_keys': len(extras), 'complete_keys': len(reconstructed),
            'canonical_bytes': len(encoded), 'canonical_sha256': sha256(encoded).hexdigest(),
            'old_control_roles_requiring_actual_Round2_history': b_old_controls},
        'unbound_future_roles': {name: None for name in (
            'physical_round2_and_actual_root_reception',
            'round2_exact_pre_round2_lifecycle_and_whole_manifest_aliases',
            'terminal_two_physical_source_only_builds_and_full_native_originals',
            'terminal_full_dependency_map_and_actual_root_reception',
            'six_actual_root_page_views_and_exact_selected_pdf',
            'initial_terminal_artifact_gate_actual_native_result',
            'post_artifact_exact_lifecycle_transition_and_root_reception')},
        'named_actual_file_keys': dict(sorted(PINS.items())),
        'external': 'OWNER_AMBER / HOLD_EXTERNAL'}
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
