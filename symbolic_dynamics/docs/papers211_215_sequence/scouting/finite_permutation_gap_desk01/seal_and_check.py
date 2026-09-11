#!/usr/bin/env python3
"""Documentary pins and exclusive artifact generation; never run scientific code."""
from hashlib import sha256
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[3]
EXPECTED = {
    'HANDOFF.md', 'PROOF_PACKAGE.md', 'SOURCES_AND_SUBTRACTION.md',
    'INPUT_PINS.sha256', 'LOCAL_NATIVE_RECORDS.json',
    'PRIMARY_SOURCE_RECORDS.json', 'seal_and_check.py',
}


def main():
    assert BASE.name == 'finite_permutation_gap_desk01'
    assert ROOT == Path('/root/autodl-tmp/symbolic_dynamics')
    assert {p.name for p in BASE.iterdir()} == EXPECTED
    assert all(p.is_file() and not p.is_symlink() for p in BASE.iterdir())
    lines = (BASE / 'INPUT_PINS.sha256').read_text().splitlines()
    # apply_patch adds a terminal newline; only nonempty SHA rows are entries.
    lines = [line for line in lines if line]
    assert len(lines) == 16
    pins = {}
    for line in lines:
        digest, relative = line.split('  ', 1)
        assert len(digest) == 64 and all(c in '0123456789abcdef' for c in digest)
        path = ROOT / relative
        assert path.is_file() and not path.is_symlink() and path.resolve().is_relative_to(ROOT)
        data = path.read_bytes()
        assert sha256(data).hexdigest() == digest
        pins[relative] = {'sha256': digest, 'bytes': len(data)}
    assert len(pins) == 16
    local = json.loads((BASE / 'LOCAL_NATIVE_RECORDS.json').read_bytes())
    assert local['schema'] == 'finite-permutation-gap-selected-local-records-v1'
    assert len(local['records']) == 7
    for row in local['records']:
        assert isinstance(row['request']['cmd'], str)
        assert isinstance(row['result']['output'], str)
        assert row['result']['exit_code'] == 0
    # An outer exit 0 is not a per-subcommand pass: preserve known diagnostics.
    combined = '\n'.join(row['result']['output'] for row in local['records'])
    assert 'binary file matches' in combined
    assert 'COMBINATORIAL_SCOUT.md: No such file or directory' in combined
    primary = json.loads((BASE / 'PRIMARY_SOURCE_RECORDS.json').read_bytes())
    assert len(primary['records']) == 5
    assert primary['full_provider_or_http_bodies_archived'] is False
    assert primary['scientific_execution'] is False
    assert '404' in primary['failures'][0]['provider_failure_return']
    for name, pin in pins.items():
        data = (ROOT / name).read_bytes()
        assert {'sha256': sha256(data).hexdigest(), 'bytes': len(data)} == pin
    result = {
        'status': 'PASS_DOCUMENTARY_ONLY_ZERO_NEW_LITERAL',
        'selected_original_pins_before_and_after': pins,
        'selected_originals_unchanged': 16,
        'selected_local_read_records': 7, 'primary_source_read_entries': 5,
        'science_executions': 0, 'saved_pointer_output_reads': 0,
        'new_literal_nominations': 0, 'closed_attempt_increment': 0,
        'receiver_source_and_manifest_unchanged': True,
        'limits': 'Documentary hash/shape check only, not proof verification, source reception, a complete native transcript, reviewer verdict or admission.',
    }
    encoded = (json.dumps(result, sort_keys=True, indent=2) + '\n').encode()
    with (BASE / 'DOCUMENTARY_RESULT.json').open('xb') as stream:
        stream.write(encoded)
    payloads = sorted(p for p in BASE.iterdir() if p.is_file())
    assert len(payloads) == 8
    raw = ''.join(sha256(p.read_bytes()).hexdigest() + '  ' + p.name + '\n'
                  for p in payloads).encode()
    with (BASE / 'MANIFEST.sha256').open('xb') as stream:
        stream.write(raw)
    assert {p.name for p in BASE.iterdir()} == EXPECTED | {'DOCUMENTARY_RESULT.json', 'MANIFEST.sha256'}
    print(json.dumps({'status': result['status'], 'payloads': len(payloads),
          'payload_bytes': sum(p.stat().st_size for p in payloads),
          'manifest_sha256': sha256(raw).hexdigest(), 'manifest_bytes': len(raw),
          'original_pins': len(pins), 'science_executions': 0}, sort_keys=True))


if __name__ == '__main__':
    main()
