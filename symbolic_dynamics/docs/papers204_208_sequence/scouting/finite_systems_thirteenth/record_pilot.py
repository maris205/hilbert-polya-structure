#!/usr/bin/env python3
"""No-overwrite source-only isolated recorder for this fixed three-rule pilot."""
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
LOCAL_INPUTS = ('pilot.py', 'INTAKE.md', 'SOURCE_AND_COLLISION.md',
                'desk/HISTORY.md', 'desk/INPUT_PINS.sha256', 'desk/SHA256SUMS')


def info(path):
    raw = path.read_bytes()
    return {'bytes': len(raw), 'sha256': sha256(raw).hexdigest()}


def save(path, raw):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open('xb') as stream:
        stream.write(raw)


def pin_name(path):
    return str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)


def current_pins(paths):
    return {pin_name(path): info(path) for path in sorted(paths)}


def main():
    if len(sys.argv) != 2 or not re.fullmatch('[a-z0-9_]+', sys.argv[1]):
        raise SystemExit('Expected one fresh lowercase attempt label')
    out = HERE/sys.argv[1]
    out.mkdir(exist_ok=False)
    source = out/'source_inputs'
    for name in LOCAL_INPUTS:
        save(source/name, (HERE/name).read_bytes())
    historical = []
    for line in (HERE/'desk/INPUT_PINS.sha256').read_text().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        if match is None:
            raise RuntimeError('Historical pin syntax')
        digest, name = match.groups()
        target = ROOT/name
        if not target.is_file() or info(target)['sha256'] != digest:
            raise RuntimeError('Historical input mismatch: '+name)
        historical.append(target)
    python = Path(sys.executable).resolve()
    originals = {HERE/name for name in LOCAL_INPUTS} | {Path(__file__).resolve(), python} | set(historical)
    snapshots = {source/name for name in LOCAL_INPUTS}
    before = current_pins(originals | snapshots)
    command = [str(python), '-I', '-B', str(source/'pilot.py')]
    started = datetime.now(timezone.utc).isoformat()
    with (out/'run.stdout').open('xb') as stdout, (out/'run.stderr').open('xb') as stderr:
        child = subprocess.run(command, cwd=source, stdout=stdout, stderr=stderr, check=False)
    after = current_pins(originals | snapshots)
    raw = (out/'run.stdout').read_bytes()
    parse_error = None
    try:
        parsed = json.loads(raw) if child.returncode == 0 else None
    except (ValueError, UnicodeDecodeError) as exc:
        parsed, parse_error = None, str(exc)
    passed = (child.returncode == 0 and before == after and parsed is not None
              and parsed.get('status') == 'PASS_FIXED_THIRTEENTH_AUTHOR_PILOT')
    canonical = HERE/'CANONICAL.json'
    created_canonical = False
    comparison = None
    if passed:
        if not canonical.exists():
            save(canonical, raw)
            created_canonical = True
        cmp_command = ['cmp', str(out/'run.stdout'), str(canonical)]
        cmp_child = subprocess.run(cmp_command, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
        save(out/'cmp.stdout', cmp_child.stdout)
        save(out/'cmp.stderr', cmp_child.stderr)
        comparison = {'command': cmp_command, 'cwd': str(ROOT), 'exit_code': cmp_child.returncode,
                      'stdout': {'path': 'cmp.stdout', **info(out/'cmp.stdout')},
                      'stderr': {'path': 'cmp.stderr', **info(out/'cmp.stderr')},
                      'canonical': {'path': pin_name(canonical), **info(canonical)}}
        passed = passed and cmp_child.returncode == 0 and raw == canonical.read_bytes()
    record = {'kind': 'ACTUAL_THIRTEENTH_FIXED_AUTHOR_PILOT_NOT_INDEPENDENT_REVIEW',
              'started_utc': started, 'ended_utc': datetime.now(timezone.utc).isoformat(),
              'command': command, 'cwd': str(source), 'child_exit_code': child.returncode,
              'pass_and_inputs_stable': passed, 'parse_error': parse_error,
              'runtime': {'python': str(python), 'version': sys.version, 'platform': sys.platform,
                          'child_flags': ['-I', '-B'], 'historical_stdlib_hermetic_snapshot': False},
              'mathematical_producer': 'source_inputs/pilot.py',
              'documentary_context_copied_but_not_read_by_producer': list(LOCAL_INPUTS[1:]),
              'all_input_count': len(before), 'all_inputs_before': before, 'all_inputs_after': after,
              'stdout': {'path': 'run.stdout', **info(out/'run.stdout')},
              'stderr': {'path': 'run.stderr', **info(out/'run.stderr')},
              'canonical_created_from_this_actual_stdout_after_success': created_canonical,
              'raw_comparison': comparison,
              'assertions': parsed.get('assertions') if parsed else None,
              'box_count': parsed.get('box_count') if parsed else None,
              'state_map_pairs': parsed.get('state_map_pairs') if parsed else None,
              'raw_capture': 'Direct binary child streams; no normalization, JSON reserialization or tool-text copying.',
              'fresh_mathematical_executions': 1, 'fresh_builds': 0, 'fresh_views': 0,
              'external_status': 'HOLD_EXTERNAL'}
    save(out/'RECEIPT.json', (json.dumps(record, indent=2, sort_keys=True)+'\n').encode())
    files = sorted(path for path in out.rglob('*') if path.is_file())
    save(out/'SHA256SUMS', ''.join(info(path)['sha256']+'  '+str(path.relative_to(out))+'\n' for path in files).encode())
    print(json.dumps({'pass': passed, 'child_exit_code': child.returncode, 'assertions': record['assertions'],
                      'box_count': record['box_count'], 'state_map_pairs': record['state_map_pairs'],
                      'receipt': str(out/'RECEIPT.json'), 'stdout': record['stdout'], 'stderr': record['stderr'],
                      'cmp_exit_code': comparison['exit_code'] if comparison else None}, indent=2))
    raise SystemExit(0 if passed else 1)


if __name__ == '__main__':
    main()
