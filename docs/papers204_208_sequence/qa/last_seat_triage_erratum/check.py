#!/usr/bin/env python3
"""Scoped native documentary table/basename check; no candidate body reads."""
import hashlib
import json
import pathlib
import re
import subprocess
import sys
import time

OWN = pathlib.Path(__file__).resolve().parent
ROOT = OWN.parents[3]
TRIAGE = ROOT / 'docs/papers204_208_sequence/scouting/LAST_SEAT_PROOF_TRIAGE'
ROWS = {
 'HVD': ['10_hvd_full'], 'NCC': ['11_ncc_full'],
 'ORR': ['13_orr_deduction_full', '14_orr_precode', '15_orr_primary_boundary', '16_orr_intake'],
 'NED': ['17_ned_full'], 'CTM': ['18_ctm_full'],
 'GCF+': ['20_gcf_intake', '21_gcf_preproof', '22_gcf_finalproof', '23_gcf_primary_initial', '24_gcf_primary_final'],
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def save(path, value):
    assert not path.exists(), str(path)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + '\n')


def inputs():
    paths = {TRIAGE / 'TRIAGE_REPORT.md', TRIAGE / 'SHA256SUMS', pathlib.Path(__file__).resolve(), OWN / 'CLARIFICATION.md'}
    paths.update(TRIAGE / 'commands' / cmd / 'receipt.json' for commands in ROWS.values() for cmd in commands)
    paths.update((TRIAGE / 'commands/17_ned_full').iterdir())
    return sorted(paths)


def check():
    report = (TRIAGE / 'TRIAGE_REPORT.md').read_text()
    manifest = (TRIAGE / 'SHA256SUMS').read_text().splitlines()
    report_hash = next(line[:64] for line in manifest if line[66:] == 'TRIAGE_REPORT.md')
    assert digest(TRIAGE / 'TRIAGE_REPORT.md') == report_hash
    assert digest(TRIAGE / 'SHA256SUMS') == '186a6f0463aec4e02a12e6bccef78f9bb700c0dd569704a2f84c8819fb370231'
    results = []
    for subject, commands in ROWS.items():
        line = next(line for line in report.splitlines() if line.startswith('| ' + subject + ' |'))
        explicit = []
        for literal in re.findall(r'`([^`]+)`', line):
            m = re.search(r'\{([^}]+)\}\.md$', literal)
            if m:
                explicit.extend(name + '.md' for name in m.group(1).split(','))
            elif literal.endswith('.md'):
                explicit.append(pathlib.PurePosixPath(literal).name)
        argv_basenames = []
        for command in commands:
            receipt = json.loads((TRIAGE / 'commands' / command / 'receipt.json').read_text())
            assert receipt['exit'] == 0 and receipt['argv'][0] == 'sed'
            argv_basenames.extend(pathlib.PurePosixPath(p).name for p in receipt['argv'][3:])
        assert set(explicit).issubset(argv_basenames), (subject, explicit, argv_basenames)
        if subject != 'ORR':
            assert sorted(explicit) == sorted(argv_basenames), subject
        else:
            assert set(argv_basenames) - set(explicit) == {'INTAKE.md', 'PRECODE_PROOFS.md', 'SOURCE_AND_HISTORY.md'}
        results.append(dict(subject=subject, explicitly_named_basenames=explicit, actual_argv_basenames=argv_basenames, match=True))
    assert 'FINAL_SOURCE_BOUNDARY.md' not in report
    command = TRIAGE / 'commands/17_ned_full'
    before = json.loads((command / 'inputs_before.json').read_text())
    after = json.loads((command / 'inputs_after.json').read_text())
    pathset = json.loads((command / 'pathset.json').read_text())
    receipt = json.loads((command / 'receipt.json').read_text())
    assert before == after and set(before) == set(pathset)
    assert digest(command / 'stdout.raw') == receipt['stdout_sha256']
    assert digest(command / 'stderr.raw') == receipt['stderr_sha256']
    print(json.dumps(dict(verdict='NO_ERRATUM_TO_SEALED_BYTES_NEEDED', sealed_report_matches_manifest=True,
        ned_sealed_name='SOURCE_SUPPLEMENT.md', wrong_name='pre_seal_draft_only', checked_rows=results,
        candidate_body_reads=0, scientific_executions=0), sort_keys=True))


if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'check'
    if mode == 'record':
        directory = OWN / 'check'
        directory.mkdir(exist_ok=False)
        paths = inputs()
        before = {str(p): digest(p) for p in paths}
        save(directory / 'inputs_before.json', before)
        start = time.time()
        argv = ['python3', '-I', '-B', str(pathlib.Path(__file__).resolve())]
        run = subprocess.run(argv, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        (directory / 'stdout.raw').write_bytes(run.stdout)
        (directory / 'stderr.raw').write_bytes(run.stderr)
        after = {str(p): digest(p) for p in paths}
        save(directory / 'inputs_after.json', after)
        receipt = dict(argv=argv, cwd=str(ROOT), started_epoch=start, finished_epoch=time.time(), exit=run.returncode,
                       input_count=len(paths), unchanged=before == after,
                       stdout_sha256=digest(directory / 'stdout.raw'), stderr_sha256=digest(directory / 'stderr.raw'))
        save(directory / 'receipt.json', receipt)
        print(json.dumps(receipt, sort_keys=True))
        assert before == after and run.returncode == 0
    elif mode == 'seal':
        target = OWN / 'SHA256SUMS'
        assert not target.exists()
        paths = sorted(p for p in OWN.rglob('*') if p.is_file() and p != target)
        target.write_text(''.join(digest(p) + '  ' + str(p.relative_to(OWN)) + '\n' for p in paths))
        print(json.dumps(dict(nonself_payloads=len(paths), sha256=digest(target))))
    else:
        check()
