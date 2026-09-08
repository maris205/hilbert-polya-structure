#!/usr/bin/env python3
"""P210 artifact/lifecycle reader DESIGN SOURCE; deliberately UNBOUND.

This file has no executable acceptance path. main() rejects before opening
the role contract, checking any host path, or producing stdout. A separate
fully bound revision and independent root source reception are required.
No old writer, verifier, receiver, build or view program is imported.
"""

STATE = 'UNBOUND_DESIGN_SOURCE_ONLY'
ROOT = '/root/autodl-tmp/symbolic_dynamics'
PAPER = ROOT + '/papers/210-weakly-increasing-run-aggregation'
QA = ROOT + '/docs/papers204_208_sequence/qa'
RICH_FIELDS = ('resolved', 'sha256', 'bytes', 'symlink')
CURRENT_FIELDS = ('real', 'sha256', 'size', 'symlink')
FUTURE_ROLES = (
    'physical_round2_and_actual_root_reception',
    'round2_exact_pre_round2_lifecycle_and_whole_manifest_aliases',
    'terminal_two_physical_source_only_builds_and_full_native_originals',
    'terminal_full_dependency_map_and_actual_root_reception',
    'six_actual_root_page_views_and_exact_selected_pdf',
    'initial_terminal_artifact_gate_actual_native_result',
    'post_artifact_exact_lifecycle_transition_and_root_reception',
)


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def is_sha256(value):
    return (isinstance(value, str) and len(value) == 64 and
            all(character in '0123456789abcdef' for character in value))


def absolute_name(value):
    """Lexical path validation only; never resolve or inspect the host here."""
    require(isinstance(value, str) and value.startswith('/'), 'absolute name')
    require(value != '/' and '\x00' not in value, 'non-root non-NUL name')
    require(all(part not in ('', '.', '..') for part in value.split('/')[1:]),
            'canonical absolute spelling')
    return value


def relative_name(value):
    require(isinstance(value, str) and not value.startswith('/'), 'relative name')
    require('\x00' not in value and '\\' not in value, 'ordinary relative spelling')
    require(all(part not in ('', '.', '..') for part in value.split('/')),
            'nonempty relative path without traversal')
    return value


def validate_rich_record(record):
    require(isinstance(record, dict) and set(record) == set(RICH_FIELDS),
            'exact original resolved/bytes rich schema')
    absolute_name(record['resolved'])
    require(is_sha256(record['sha256']), 'rich SHA256')
    require(type(record['bytes']) is int and record['bytes'] >= 0, 'rich bytes')
    require(record['symlink'] is None or isinstance(record['symlink'], str),
            'rich literal link value')
    return record


def validate_current_record(record):
    require(isinstance(record, dict) and set(record) == set(CURRENT_FIELDS),
            'exact current real/size rich schema')
    absolute_name(record['real'])
    require(is_sha256(record['sha256']), 'current SHA256')
    require(type(record['size']) is int and record['size'] >= 0, 'current size')
    require(record['symlink'] is None or isinstance(record['symlink'], str),
            'current literal link value')
    return record


def convert_original_rich(record):
    validate_rich_record(record)
    return {'real': record['resolved'], 'sha256': record['sha256'],
            'size': record['bytes'], 'symlink': record['symlink']}


def complete_map_digest(records):
    """Pure data encoding, identical to actual B final's declared encoding."""
    from hashlib import sha256
    import json
    require(isinstance(records, dict), 'complete map is an object')
    for name, value in records.items():
        absolute_name(name)
        validate_current_record(value)
    encoded = json.dumps(records, sort_keys=True, separators=(',', ':'),
                         ensure_ascii=True).encode()
    return {'sha256': sha256(encoded).hexdigest(), 'bytes': len(encoded),
            'keys': len(records)}


def reconstruct_actual_b_final_map(common, exact_extra, expected_sha256):
    """Reconstruct archived logical evidence; this alone is NOT reuse acceptance.

    The actual root result has 121013 common + 44 disjoint extra keys.
    Current physical bytes must later be verified independently, including
    only the actual PRE_ROUND2 historical aliases after lifecycle changes.
    """
    require(isinstance(common, dict) and len(common) == 121013,
            'all actual B common keys')
    require(isinstance(exact_extra, dict) and len(exact_extra) == 44,
            'all actual B final root extra keys')
    require(not (set(common) & set(exact_extra)), 'B extra keys disjoint')
    result = {}
    for name, value in common.items():
        absolute_name(name)
        result[name] = convert_original_rich(value)
    for name, value in exact_extra.items():
        absolute_name(name)
        result[name] = validate_current_record(value).copy()
    require(complete_map_digest(result)['sha256'] == expected_sha256,
            'entire B final logical map canonical digest')
    return result


def parse_nonself_manifest(raw_bytes, self_name):
    """Exact directory-relative SHA256SUMS grammar; no legacy fallback."""
    import re
    require(isinstance(raw_bytes, bytes) and raw_bytes.endswith(b'\n'),
            'complete raw manifest newline')
    relative_name(self_name)
    rows = {}
    for line in raw_bytes.decode('utf-8').splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        require(match is not None, 'exact manifest row')
        digest, name = match.groups()
        relative_name(name)
        require(name != self_name and name not in rows, 'nonself unique manifest')
        rows[name] = digest
    return rows


def strict_pair_data_interval(before, after, role):
    """Data-only original interval check; no host traversal or new science."""
    expected = {'author': 3639, 'a': 3634, 'b': 3558}
    require(role in expected, 'one of the three exact P210 roles')
    require(isinstance(before, dict) and len(before) == expected[role],
            'entire strict known-key census')
    require(before == after, 'complete recorded strict interval equality')
    for name, value in before.items():
        absolute_name(name)
        validate_rich_record(value)
    return {'role': role, 'known_keys': len(before),
            'current_physical_recheck_done': False, 'new_science_runs': 0}


def select_exact_historical_role(logical_name, original_record, alias_rows):
    """Match path+SHA+size, never search by basename or try arbitrary history.

    An unchanged logical name stays itself. A selected historical record must
    subsequently be hashed at its own physical path, checking its *physical*
    resolution/link separately from the original logical metadata. No record
    is rewritten to pretend its original resolution was the saved copy.
    """
    absolute_name(logical_name)
    validate_current_record(original_record)
    matches = []
    for alias in alias_rows:
        require(set(alias) == {'logical', 'original_sha256', 'original_size',
                              'physical', 'physical_record', 'provenance_role'},
                'exact historical role schema')
        absolute_name(alias['logical'])
        absolute_name(alias['physical'])
        validate_current_record(alias['physical_record'])
        require(alias['original_sha256'] == alias['physical_record']['sha256'] and
                alias['original_size'] == alias['physical_record']['size'],
                'saved physical bytes equal exact original role')
        if (logical_name, original_record['sha256'], original_record['size']) == (
                alias['logical'], alias['original_sha256'], alias['original_size']):
            matches.append(alias)
    require(len(matches) <= 1, 'no ambiguous historical target')
    return matches[0] if matches else None


def verify_named_current_bytes(path, expected):
    """Read-only primitive. Not called in this UNBOUND design package."""
    from hashlib import sha256
    import os
    from pathlib import Path
    absolute_name(path)
    validate_current_record(expected)
    physical = Path(path)
    require(physical.is_file(), 'actual named physical file')
    value = physical.read_bytes()
    observed = {'real': str(physical.resolve()), 'sha256': sha256(value).hexdigest(),
                'size': len(value),
                'symlink': os.readlink(physical) if physical.is_symlink() else None}
    require(observed == expected, 'full named physical rich-key equality')
    return value


def check_all_three_native_originals_and_source_runtime():
    raise RuntimeError('UNBOUND: actual role-specific author/A/B native, argv, '
                       'source, resources, configuration and bounded module/maps '
                       'checks require a separately reviewed full implementation')


def check_round0_round1_round2_physical_provenance_and_links():
    raise RuntimeError('UNBOUND: actual complete Round2 and its root reception '
                       'must determine exact PRE_ROUND2 aliases and role census')


def check_terminal_builds_originals_and_complete_dependency_reuse():
    raise RuntimeError('UNBOUND: actual planner build/reception source and '
                       'native output determine the real schema and full keys')


def check_six_actual_final_page_views():
    raise RuntimeError('UNBOUND: six actual root page-view observations and '
                       'their exact final PDF must exist; image hashes are not views')


def initial_artifact_gate():
    raise RuntimeError('UNBOUND: no initial artifact verdict can be emitted '
                       'before every required actual input and full reader exists')


def distinct_lifecycle_followup():
    raise RuntimeError('UNBOUND: requires preserved successful initial gate, '
                       'physical pre-update lifecycle/whole-manifest bytes, '
                       'and exactly the actual authorized lifecycle-only change')


def main():
    # Intentionally unconditional: changing JSON or supplying arbitrary argv
    # cannot enable this preparation. No role/host reads and no stdout precede it.
    raise SystemExit('UNBOUND: P210 artifact/lifecycle DESIGN SOURCE only; '
                     'create a separately reviewed final bound revision')


if __name__ == '__main__':
    main()
