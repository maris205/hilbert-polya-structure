#!/usr/bin/env python3
"""Documentary schema/pin/raw-read audit only; no candidate implementation."""
import hashlib
import json
import pathlib
import subprocess
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import record

OWN = record.OWN
CHILD = OWN / 'orientation_source_desk'
SELF = pathlib.Path(__file__).resolve()
LABEL = '08_documentary_audit'
ROLES = json.loads((OWN / 'CONTROL_ROLES.json').read_text())
ALIASES = {r['original_path']: r for r in ROLES}


def resolved_pin(path, digest):
    if path in ALIASES:
        item = ALIASES[path]
        assert item['sha256'] == digest, ('control historical identity', path)
        return pathlib.Path(item['copy_path'])
    return pathlib.Path(path)


def parent_receipts():
    return sorted(p for p in (OWN / 'commands').glob('*/receipt.json') if p.parent.name != LABEL)


def child_receipts():
    return sorted((CHILD / 'commands').glob('*/receipt.json'))


def all_audit_inputs():
    paths = {p for p in OWN.rglob('*') if p.is_file() and '08_documentary_audit' not in p.parts}
    for receipt in parent_receipts():
        for path, digest in json.loads((receipt.parent / 'inputs_before.json').read_text()).items():
            paths.add(resolved_pin(path, digest))
    for receipt in child_receipts():
        obj = json.loads(receipt.read_text())
        for pin in obj['inputs_before'] + [obj['executable'], obj['recorder']]:
            paths.add(resolved_pin(pin['path'], pin['sha256']))
    return sorted(paths)


def main():
    identities = set()
    occurrences = 0
    raw_reads = 0
    for role in ROLES:
        assert record.sha(pathlib.Path(role['copy_path'])) == role['sha256']
    for path in parent_receipts():
        base = path.parent
        obj = json.loads(path.read_text())
        before = json.loads((base / 'inputs_before.json').read_text())
        after = json.loads((base / 'inputs_after.json').read_text())
        assert before == after and obj['unchanged'] and obj['input_count'] == len(before), str(path)
        assert obj['exit'] == 0, str(path)
        for original, digest in before.items():
            actual = resolved_pin(original, digest)
            assert record.sha(actual) == digest, ('parent pin', original)
            identities.add((original, digest))
            occurrences += 1
        for stream in ('stdout', 'stderr'):
            assert record.sha(base / (stream + '.raw')) == obj[stream + '_sha256'], str(path)
        reread = False
        if obj['argv'][0] == 'sed':
            fresh = subprocess.run(obj['argv'], cwd=obj['cwd'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            assert fresh.returncode == obj['exit']
            assert fresh.stdout == (base / 'stdout.raw').read_bytes()
            assert fresh.stderr == (base / 'stderr.raw').read_bytes()
            raw_reads += 1
            reread = True
        print(json.dumps(dict(schema='parent', command=base.name, exit=obj['exit'],
            pin_count=len(before), raw_sed_reexecution_byte_exact=reread), sort_keys=True))

    for path in child_receipts():
        obj = json.loads(path.read_text())
        initial = json.loads((path.parent / 'invocation.json').read_text())
        assert all(obj[key] == value for key, value in initial.items()), str(path)
        assert obj['inputs_before'] == obj['inputs_after'], str(path)
        expected = 22 if path.parent.name in {'r1_acm_curl', 'r2_tcs_curl'} else 0
        assert obj['exit_code'] == expected, str(path)
        for pin in obj['inputs_before'] + [obj['executable'], obj['recorder'], obj['stdout'], obj['stderr']]:
            actual = resolved_pin(pin['path'], pin['sha256'])
            assert record.sha(actual) == pin['sha256'], ('child pin', pin['path'])
            assert actual.stat().st_size == pin['bytes'], ('child size', pin['path'])
            identities.add((pin['path'], pin['sha256']))
            occurrences += 1
        reread = False
        if obj['argv'][0] == 'sed':
            fresh = subprocess.run(obj['argv'], cwd=obj['cwd'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            assert fresh.returncode == obj['exit_code']
            assert fresh.stdout == pathlib.Path(obj['stdout']['path']).read_bytes()
            assert fresh.stderr == pathlib.Path(obj['stderr']['path']).read_bytes()
            raw_reads += 1
            reread = True
        print(json.dumps(dict(schema='child', command=path.parent.name, exit=obj['exit_code'],
            explicit_pin_count=len(obj['inputs_before']), raw_sed_reexecution_byte_exact=reread,
            incomplete_initial_read_disclosed=path.parent.name == 'read_failures'), sort_keys=True))

    manifest = CHILD / 'SHA256SUMS'
    listed = []
    for line in manifest.read_text().splitlines():
        digest, relative = line.split('  ', 1)
        target = CHILD / relative
        assert record.sha(target) == digest, relative
        listed.append(relative)
    seal = json.loads((CHILD / 'SEAL_CHECK.json').read_text())
    assert record.sha(manifest) == seal['manifest_sha256']
    assert seal['payload_count'] == len(listed) == 60 and seal['exit_code'] == 0
    assert record.sha(CHILD / 'SEAL_CHECK.stdout') == seal['stdout_sha256']
    assert record.sha(CHILD / 'SEAL_CHECK.stderr') == seal['stderr_sha256']
    expected_lines = ''.join(relative + ': OK\n' for relative in listed).encode()
    assert (CHILD / 'SEAL_CHECK.stdout').read_bytes() == expected_lines
    child_files = sorted(str(p.relative_to(CHILD)) for p in CHILD.rglob('*') if p.is_file())
    assert set(child_files) - set(listed) == {'SHA256SUMS', 'SEAL_CHECK.json', 'SEAL_CHECK.stdout', 'SEAL_CHECK.stderr'}
    assert len(child_files) == 64

    discovery = json.loads((OWN / 'DISCOVERY_SCOPE.json').read_text())
    assert len(discovery['selected_paths']) == 104 and discovery['metadata_paths'] == 901
    query = json.loads((OWN / 'commands/04_scoped_body_search/receipt.json').read_text())['argv']
    assert query[query.index('--') + 1:] == discovery['selected_paths']
    hits = (OWN / 'commands/04_scoped_body_search/stdout.raw').read_bytes().splitlines()
    assert len(hits) == 55
    print(json.dumps(dict(result='PASS_DOCUMENTARY_ONLY', parent_commands=len(parent_receipts()),
        child_commands=len(child_receipts()), checked_pin_occurrences=occurrences,
        distinct_historical_identities=len(identities), control_copy_aliases=len(ROLES),
        raw_sed_reexecutions_byte_exact=raw_reads, child_inner_payloads=len(listed),
        child_all_files_to_be_parent_sealed=len(child_files), selected_historical_notes=104,
        historical_match_lines=len(hits), scientific_executions=0, pilots=0), sort_keys=True))


if __name__ == '__main__':
    if sys.argv[1:] == ['check']:
        main()
    elif sys.argv[1:] == ['capture']:
        result = record.capture(LABEL, [sys.executable, '-B', str(SELF), 'check'], all_audit_inputs())
        print(result.stdout.decode(), end='')
        print(result.stderr.decode(), end='', file=sys.stderr)
        raise SystemExit(result.returncode)
    else:
        raise SystemExit('use capture or check')
