#!/usr/bin/env python3
"""Own documentary audit only; no candidate states or transition code."""
import json
import pathlib
import subprocess
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import record

SELF = pathlib.Path(__file__).resolve()


def objects():
    return [(p.parent, json.loads(p.read_text()))
            for p in sorted((record.OWN / 'commands').glob('*/receipt.json'))
            if p.parent.name != '11_documentary_audit']


def alias_table():
    return {item['original_path']: item
            for item in json.loads((record.OWN / 'CONTROL_ROLES.json').read_text())}


def resolved(original, aliases):
    return pathlib.Path(aliases[original]['copy_path'] if original in aliases else original)


def check():
    aliases = alias_table()
    checked_pins = 0
    unique_pins = {}
    textual_reads = []
    receipts = objects()
    for item in aliases.values():
        assert record.digest(pathlib.Path(item['copy_path'])) == item['sha256']
    for folder, receipt in receipts:
        before = json.loads((folder / 'inputs_before.json').read_text())
        after = json.loads((folder / 'inputs_after.json').read_text())
        paths = json.loads((folder / 'pathset.json').read_text())
        assert before == after and receipt['unchanged'] is True, str(folder)
        assert sorted(before) == paths and len(paths) == receipt['input_count'], str(folder)
        assert receipt['exit'] == 0, str(folder)
        assert receipt['stdout_sha256'] == record.digest(folder / 'stdout.raw'), str(folder)
        assert receipt['stderr_sha256'] == record.digest(folder / 'stderr.raw'), str(folder)
        for original, expected in before.items():
            actual = resolved(original, aliases)
            assert actual.is_file() and not actual.is_symlink(), str(actual)
            assert not record.forbidden(actual), str(actual)
            assert record.digest(actual) == expected, (original, str(actual))
            if original in aliases:
                assert expected == aliases[original]['sha256']
            unique_pins[original] = expected
            checked_pins += 1
        if receipt['argv'][0] == 'sed':
            args = receipt['argv']
            for value in args[3:]:
                path = pathlib.Path(value)
                assert str(path) in before and not record.forbidden(path), str(path)
            replay = subprocess.run(args, cwd=receipt['cwd'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            assert replay.returncode == 0 and replay.stdout == (folder / 'stdout.raw').read_bytes()
            assert replay.stderr == (folder / 'stderr.raw').read_bytes()
            textual_reads.append(dict(receipt=folder.name, argv=args, exit=replay.returncode,
                                      bytes=len(replay.stdout), raw_byte_equal=True))
    scope = json.loads((record.OWN / 'DISCOVERY_SCOPE.json').read_text())
    assert len(scope['body_paths_selected']) == 109 and scope['filenames_seen'] == 892
    assert len((record.OWN / 'commands/06_scoped_body_search/stdout.raw').read_bytes().splitlines()) == 15
    for original in scope['body_paths_selected']:
        assert not record.forbidden(pathlib.Path(original)), original
    for name in ('register', 'carlitz'):
        assert (record.OWN / 'sources' / name / 'body.raw').read_bytes().startswith(b'%PDF-')
        assert (record.OWN / 'sources' / name / 'body.txt').is_file()
    for name in ('PROOF_PACKAGE.md', 'SOURCE_AND_HISTORY.md', 'SCOUT_REPORT.md', 'INTAKE.md'):
        assert (record.OWN / name).stat().st_size > 100
    assert not (record.OWN / 'CANONICAL.json').exists()
    assert not (record.OWN / '__pycache__').exists()
    print(json.dumps(dict(status='PASS_DOCUMENTARY_ONLY', scientific_executions=0,
        candidate_pilots=0, independent_reviews=0, historical_receipts=len(receipts),
        pin_occurrences_checked=checked_pins, distinct_original_pin_identities=len(unique_pins),
        physically_copied_control_aliases=len(aliases), body_scope_count=109, discovery_hits=15,
        textual_command_reexecutions=textual_reads,
        limit='Documentary raw/pin checks and sed reexecutions, not numerical or independent mathematical validation'),
        indent=2, sort_keys=True))


if __name__ == '__main__':
    if sys.argv[1:] == ['run']:
        aliases = alias_table()
        inputs = set(p for p in record.OWN.rglob('*') if p.is_file())
        for folder, receipt in objects():
            before = json.loads((folder / 'inputs_before.json').read_text())
            inputs.update(resolved(original, aliases) for original in before)
        result = record.capture('11_documentary_audit', [sys.executable, '-B', str(SELF), 'check'], inputs)
        raise SystemExit(result.returncode)
    elif sys.argv[1:] == ['check']:
        check()
    else:
        raise SystemExit('run or check required')
