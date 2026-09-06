#!/usr/bin/env python3
"""No-overwrite raw recorder for an explicitly artifact-consuming theorem audit."""
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
INPUTS = ('audit_extrema.py', 'CANONICAL.json', 'PROOF_AND_DISPOSITION.md')


def info(path):
    raw = path.read_bytes()
    return {'bytes': len(raw), 'sha256': sha256(raw).hexdigest()}


def save(path, raw):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('xb') as stream:
        stream.write(raw)


def pins(paths):
    return {str(path): info(path) for path in sorted(paths)}


def main():
    if len(sys.argv) != 2 or not re.fullmatch('[a-z0-9_]+', sys.argv[1]):
        raise SystemExit('Expected fresh lowercase attempt label')
    out = HERE/sys.argv[1]
    out.mkdir(exist_ok=False)
    source = out/'source_inputs'
    for name in INPUTS:
        save(source/name, (HERE/name).read_bytes())
    python = Path(sys.executable).resolve()
    paths = {HERE/name for name in INPUTS} | {source/name for name in INPUTS} | {Path(__file__).resolve(), python}
    before = pins(paths)
    command = [str(python), '-I', '-B', str(source/'audit_extrema.py')]
    started = datetime.now(timezone.utc).isoformat()
    with (out/'run.stdout').open('xb') as stdout, (out/'run.stderr').open('xb') as stderr:
        child = subprocess.run(command, cwd=source, stdout=stdout, stderr=stderr, check=False)
    after = pins(paths)
    raw = (out/'run.stdout').read_bytes()
    parsed = json.loads(raw) if child.returncode == 0 else None
    passed = (child.returncode == 0 and before == after and parsed is not None
              and parsed.get('status') == 'PASS_POST_PILOT_AMC_EXTREMA_ARTIFACT_AUDIT')
    reference = HERE/'EXTREMA_AUDIT_CANONICAL.json'
    created_reference = False
    comparison = None
    if passed:
        if not reference.exists():
            save(reference, raw)
            created_reference = True
        cmp_command = ['cmp', str(out/'run.stdout'), str(reference)]
        cmp_child = subprocess.run(cmp_command, cwd=HERE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
        save(out/'cmp.stdout', cmp_child.stdout)
        save(out/'cmp.stderr', cmp_child.stderr)
        comparison = {'command': cmp_command, 'cwd': str(HERE), 'exit_code': cmp_child.returncode,
                      'stdout': info(out/'cmp.stdout'), 'stderr': info(out/'cmp.stderr'),
                      'canonical': {'path': str(reference), **info(reference)}}
        passed = passed and cmp_child.returncode == 0 and raw == reference.read_bytes()
    record = {'kind': 'ACTUAL_AUTHOR_ARTIFACT_CONSUMING_EXTREMA_AUDIT_NOT_MAP_REPLAY',
              'started_utc': started, 'ended_utc': datetime.now(timezone.utc).isoformat(),
              'command': command, 'cwd': str(source), 'child_exit_code': child.returncode,
              'pass_and_inputs_stable': passed, 'runtime': {'python': str(python), 'version': sys.version,
                  'platform': sys.platform, 'flags': ['-I', '-B'], 'hermetic_stdlib_snapshot': False},
              'all_input_count': len(before), 'all_inputs_before': before, 'all_inputs_after': after,
              'producer': 'source_inputs/audit_extrema.py', 'actual_data_input': 'source_inputs/CANONICAL.json',
              'copied_but_unread_documentary_input': 'source_inputs/PROOF_AND_DISPOSITION.md',
              'stdout': {'path': 'run.stdout', **info(out/'run.stdout')},
              'stderr': {'path': 'run.stderr', **info(out/'run.stderr')}, 'raw_comparison': comparison,
              'reference_created_from_this_successful_actual_stdout': created_reference,
              'assertions': parsed.get('assertions') if parsed else None,
              'fresh_artifact_audit_executions': 1, 'fresh_map_executions': 0, 'new_state_boxes': 0,
              'independent_review': False, 'external_status': 'HOLD_EXTERNAL'}
    save(out/'RECEIPT.json', (json.dumps(record, indent=2, sort_keys=True)+'\n').encode())
    files = sorted(path for path in out.rglob('*') if path.is_file())
    save(out/'SHA256SUMS', ''.join(info(path)['sha256']+'  '+str(path.relative_to(out))+'\n' for path in files).encode())
    print(json.dumps({'pass': passed, 'child_exit_code': child.returncode, 'assertions': record['assertions'],
                      'stdout': record['stdout'], 'stderr': record['stderr'],
                      'cmp_exit_code': comparison['exit_code'] if comparison else None,
                      'receipt': str(out/'RECEIPT.json')}, indent=2))
    raise SystemExit(0 if passed else 1)


if __name__ == '__main__':
    main()
