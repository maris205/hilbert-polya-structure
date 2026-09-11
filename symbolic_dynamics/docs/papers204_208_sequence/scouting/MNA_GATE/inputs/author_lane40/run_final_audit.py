#!/usr/bin/env python3
"""Declare all actual documentary audit file inputs before its recorded run."""
import json
from pathlib import Path
import subprocess
import sys

OWN = Path(__file__).absolute().parent
ROOT = OWN.parents[3]


def main():
    assert not (OWN / 'commands/20_artifact_audit').exists()
    inputs = {p for p in OWN.rglob('*') if p.is_file()}
    for folder in (OWN / 'commands').iterdir():
        if folder.is_dir():
            mapping = json.loads((folder / 'inputs_before.json').read_text())
            inputs.update(Path(p) for p in mapping)
    for filename in ('CONTROL_ROLES.json', 'ROOT_REFERENCE_ROLES.json'):
        for role in json.loads((OWN / filename).read_text()):
            inputs.add(Path(role['original_path']))
            inputs.add(Path(role['copy_path']))
    for path in inputs:
        assert path.is_absolute() and path.is_file() and not path.is_symlink()
    argv = [sys.executable, '-I', '-S', '-B', str(OWN / 'record.py'), '20_artifact_audit']
    for path in sorted(inputs):
        argv.extend(('--input', str(path)))
    argv.extend(('--role', 'documentary_artifact_validation_not_scientific_pilot', '--',
                 sys.executable, '-I', '-S', '-B', str(OWN / 'audit.py')))
    result = subprocess.run(argv, cwd=ROOT, check=False)
    raise SystemExit(result.returncode)


if __name__ == '__main__':
    main()
