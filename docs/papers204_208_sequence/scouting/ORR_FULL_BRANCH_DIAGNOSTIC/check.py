#!/usr/bin/env python3
"""Small documentary check; no mathematical kernel, pilot or proof checker."""
import json
import pathlib
import re
import sys

OWN = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(OWN))
import record


def check():
    roles = json.loads((OWN / 'ORIGINAL_ROLES.json').read_text())
    assert len(roles) == len(record.ORIGINALS) == 7
    assert {r['original_path'] for r in roles} == {str(p) for p in record.ORIGINALS}
    for row in roles:
        original = pathlib.Path(row['original_path'])
        copy = pathlib.Path(row['copy_path'])
        assert copy == OWN / 'inputs' / original.relative_to(record.ROOT)
        assert row['role'] == 'exact_copy_before_new_body_read'
        assert record.digest(original) == record.digest(copy) == row['sha256']
        assert not original.is_symlink() and not copy.is_symlink()
        assert len(copy.read_bytes().splitlines()) <= 4000
    checked = []
    for name in ('01_original_copy', '02_original_read', '03_second_attempt_read'):
        directory = OWN / 'commands' / name
        receipt = json.loads((directory / 'receipt.json').read_text())
        before = json.loads((directory / 'inputs_before.json').read_text())
        after = json.loads((directory / 'inputs_after.json').read_text())
        pathset = json.loads((directory / 'pathset.json').read_text())
        assert before == after and set(before) == set(pathset)
        assert receipt['exit'] == 0 and receipt['unchanged'] is True
        assert receipt['inputs'] == len(pathset)
        assert record.digest(directory / 'stdout.raw') == receipt['stdout_sha256']
        assert record.digest(directory / 'stderr.raw') == receipt['stderr_sha256']
        assert (directory / 'stderr.raw').read_bytes() == b''
        for path, expected in before.items():
            p = pathlib.Path(path)
            assert p.is_relative_to(OWN) or p in record.ORIGINALS
            assert record.digest(p) == expected
        if receipt['argv'][0] == 'sed':
            inputs = [pathlib.Path(p) for p in receipt['argv'][3:]]
            expected_stdout = b''.join(p.read_bytes() for p in inputs)
            assert (directory / 'stdout.raw').read_bytes() == expected_stdout
        else:
            assert receipt['argv'][0] == 'cp'
            assert (directory / 'stdout.raw').read_bytes() == b''
        checked.append(dict(command=name, exit=0, pins=len(before),
                            stdout_bytes=(directory / 'stdout.raw').stat().st_size))
    copy_end = json.loads((OWN / 'commands/01_original_copy/receipt.json').read_text())['finished_epoch']
    for name in ('02_original_read', '03_second_attempt_read'):
        read_start = json.loads((OWN / 'commands' / name / 'receipt.json').read_text())['started_epoch']
        assert copy_end <= read_start
    link_count = 0
    for name in ('INTAKE.md', 'PROOF_PACKAGE.md', 'HANDOFF.md'):
        body = (OWN / name).read_text()
        for target in re.findall(r'\]\(([^)]+)\)', body):
            assert (OWN / target).is_file() or target == 'DOCUMENTARY_CHECK.json'
            link_count += 1
    outcome = dict(verdict='PASS_DOCUMENTARY_ONLY', original_files=7,
        originals_copies_and_read_pins_unchanged=True,
        complete_read_stdout_byte_equality=True, copy_preceded_new_original_body_reads=True,
        native_read_copy_commands=3, commands=checked, document_links_checked=link_count,
        mathematical_proof_checked_by_program=False, original_sharp_claim='NOT_CURRENTLY_JUSTIFIED',
        representation_deductions='author_proof_only', scientific_executions=0,
        primary_reads=0, new_candidate_gates=0, independent_reviews=0,
        source_value_clearance=False, scope='one_ORR_full_branch_representation_diagnostic')
    record.save(OWN / 'DOCUMENTARY_CHECK.json', outcome)
    print(json.dumps(outcome, sort_keys=True))


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'record':
        inputs = sorted(p for p in OWN.rglob('*') if p.is_file())
        record.capture('04_documentary_check', ['python3', '-I', '-B', str(pathlib.Path(__file__).resolve())], inputs)
    else:
        check()
