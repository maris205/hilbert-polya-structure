#!/usr/bin/env python3
"""Documentary provenance audit, never a scientific replay or proof check."""
import hashlib
import json
import pathlib
import re
import sys

OWN = pathlib.Path(__file__).resolve().parent
ROOT = OWN.parents[3]
BASE = ROOT / 'docs/papers204_208_sequence/scouting'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(path.read_text())


def save(path, value):
    assert not path.exists(), str(path)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + '\n')


def protected(path):
    if path.is_relative_to(OWN):
        return False
    for part in path.relative_to(ROOT).parts:
        token = part.lower()
        if token in {'qa', 'review', 'reviews', 'freeze', 'freezes', 'build', 'builds'}:
            return True
        if 'gate' in token or token.startswith(('fth', 'ofs', '208', '209', 'p208', 'p209', 'round0', 'round1', 'round2', 'terminal')):
            return True
        if re.search(r'(^|[^a-z0-9])(fth|ofs)([^a-z0-9]|$)', token):
            return True
    return False


def audit():
    roles = read(OWN / 'CONTROL_ROLES.json')
    controls = {}
    for row in roles:
        original = pathlib.Path(row['original_path'])
        copy = pathlib.Path(row['copy_path'])
        assert copy.is_relative_to(OWN / 'controls')
        assert row['role'] == 'exact_physical_copy_before_body_read'
        assert digest(copy) == row['sha256']
        controls[str(original)] = row
    assert len(controls) == 3
    allowed = {
        str(BASE / 'word_local/HVD_PROOF_WORK' / name)
        for name in ('PROOF_AND_DISPOSITION.md', 'SOURCE_AND_REPLAY.md', 'WORK_CONTRACT.md')
    }
    allowed.update(str(BASE / 'word_local' / name) for name in ('NCC_INTAKE.md', 'NCC_PROOF_BOUNDARY.md'))
    allowed.update(str(BASE / 'finite_systems_twenty_second' / name) for name in ('INTAKE.md', 'PRECODE_PROOFS.md', 'ORR_FIBRE_PROOF.md', 'SOURCE_AND_HISTORY.md'))
    allowed.add(str(BASE / 'ORR_ROOT_CLOCK_BOUNDARY.md'))
    allowed.update(str(BASE / 'ORR_SECOND_CLOCK_ATTEMPT' / name) for name in ('PROOF_PACKAGE.md', 'ATTEMPT_REPORT.md', 'SOURCE_READS.md'))
    allowed.update(str(BASE / 'finite_systems_twenty_first' / name) for name in ('INTAKE.md', 'PROOF_PACKAGE.md', 'SOURCE_AND_HISTORY.md', 'SOURCE_SUPPLEMENT.md'))
    allowed.update(str(BASE / 'finite_systems_twenty_eighth' / name) for name in ('INTAKE.md', 'PROOF_PACKAGE.md', 'SOURCE_AND_HISTORY.md'))
    allowed.update(str(BASE / 'finite_systems_twenty_seventh' / name) for name in ('INTAKE.md', 'PREPILOT_PROOF.md', 'PROOF_PACKAGE.md', 'PREPILOT_SOURCE.md', 'SOURCE_AND_HISTORY.md'))
    directories = sorted(p for p in (OWN / 'commands').iterdir() if p.is_dir() and int(p.name[:2]) <= 24)
    assert len(directories) == 24
    assert [int(p.name[:2]) for p in directories] == list(range(1, 25))
    merged = {}
    rows = []
    for directory in directories:
        receipt = read(directory / 'receipt.json')
        before = read(directory / 'inputs_before.json')
        after = read(directory / 'inputs_after.json')
        pathset = read(directory / 'pathset.json')
        assert before == after
        assert set(pathset) == set(before)
        assert len(pathset) == receipt['input_count']
        assert receipt['unchanged'] is True and receipt['exit'] == 0
        assert receipt['role'] == 'new_native_documentary_command_not_scientific_execution'
        assert digest(directory / 'stdout.raw') == receipt['stdout_sha256']
        assert digest(directory / 'stderr.raw') == receipt['stderr_sha256']
        assert (directory / 'stderr.raw').read_bytes() == b''
        assert receipt['argv'][0] in ('cp', 'rg', 'sed')
        checked = 0
        for name, expected in before.items():
            p = pathlib.Path(name)
            assert p.is_absolute() and p.is_relative_to(ROOT)
            assert not protected(p), name
            if name in controls:
                assert directory.name == '01_control_copy'
                assert expected == controls[name]['sha256']
                effective = pathlib.Path(controls[name]['copy_path'])
            else:
                assert p.is_relative_to(OWN) or name in allowed, name
                effective = p
            assert not effective.is_symlink(), name
            assert digest(effective) == expected, name
            if name in merged:
                assert merged[name] == expected
            merged[name] = expected
            checked += 1
        rows.append(dict(label=directory.name, exit=receipt['exit'], pinned_paths_checked=checked,
                         stdout_bytes=(directory / 'stdout.raw').stat().st_size,
                         status='PASS_DOCUMENTARY_ONLY'))
    original_pins = {name: value for name, value in merged.items()
                     if not pathlib.Path(name).is_relative_to(OWN) and name not in controls}
    assert set(original_pins).issubset(allowed)
    control_command = read(OWN / 'commands/01_control_copy/receipt.json')
    first_body = read(OWN / 'commands/02_control_key_search/receipt.json')
    assert control_command['finished_epoch'] <= first_body['started_epoch']
    report = (OWN / 'TRIAGE_REPORT.md').read_text()
    links = re.findall(r'\]\(([^)]+)\)', report)
    pending = {'DOCUMENTARY_AUDIT.json'}
    for link in links:
        p = OWN / link
        assert p.is_relative_to(OWN)
        assert p.is_file() or link in pending, link
    save(OWN / 'ORIGINAL_INPUT_PINS.json', original_pins)
    outcome = dict(
        verdict='PASS_DOCUMENTARY_ONLY', native_command_packages=24,
        subjects=['HVD', 'NCC', 'ORR', 'NED', 'CTM', 'GCF+'],
        conditional_opportunities=['ORR'], tractability_established=False,
        unique_original_note_files=len(original_pins), original_inputs_unchanged=True,
        exact_control_copies=3, live_control_revalidation='not_performed_root_may_update',
        control_copy_preceded_body_search=True, no_protected_input_paths_in_native_pathsets=True,
        subject_scope='six_legacy_subjects_with_GCF0_context_only',
        scientific_executions=0, scientific_kernels_added=0, proof_contributions=0,
        primary_body_reads_this_task=0, independent_reviews=0,
        complete_native_stdout_stderr=True,
        outer_failure_record='SCOPE_REFUSAL_TRANSCRIPTION.md: honest tool transcription, not native stdout',
        report_links_checked=len(links), commands=rows)
    save(OWN / 'DOCUMENTARY_AUDIT.json', outcome)
    print(json.dumps(outcome, sort_keys=True))


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'record':
        sys.path.insert(0, str(OWN))
        import scope_adapter
        inputs = sorted(p for p in OWN.rglob('*') if p.is_file())
        result = scope_adapter.record.capture('25_documentary_audit',
            ['python3', '-I', '-B', str(pathlib.Path(__file__).resolve())], inputs)
        assert result.returncode == 0
    else:
        audit()
