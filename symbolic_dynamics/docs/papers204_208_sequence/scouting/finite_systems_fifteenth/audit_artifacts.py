#!/usr/bin/env python3
"""Read-only complete local seals/receipts audit; not a mathematical run."""
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]


def require(condition, label):
    if not condition:
        raise AssertionError(label)


def info(path):
    raw = path.read_bytes()
    return {'bytes': len(raw), 'sha256': sha256(raw).hexdigest()}


def parse_pins(path):
    result = {}
    for line in path.read_text().splitlines():
        match = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        require(match is not None, 'pin syntax: '+str(path))
        value, name = match.groups()
        require(name not in result, 'duplicate pin')
        result[name] = value
    return result


def main():
    manifests = sorted(HERE.rglob('SHA256SUMS'))
    require(len(manifests) == 6, 'six complete manifests including outer')
    manifest_entries = 0
    for manifest in manifests:
        pins = parse_pins(manifest)
        actual = {str(p.relative_to(manifest.parent)) for p in manifest.parent.rglob('*')
                  if p.is_file() and p != manifest}
        require(actual == set(pins), 'exact coverage: '+str(manifest))
        for name, value in pins.items():
            require(info(manifest.parent/name)['sha256'] == value, 'manifest content: '+name)
        manifest_entries += len(pins)
    external_pin_count = 0
    for file in (HERE/'desk/INPUT_PINS.sha256', HERE/'AUTHOR_ADDITIONAL_HISTORY_PINS.sha256'):
        for name, value in parse_pins(file).items():
            require(info(ROOT/name)['sha256'] == value, 'documentary historical input: '+name)
            external_pin_count += 1
    input_references, output_references = 0, 0
    for label in ('execution_01', 'execution_02'):
        folder = HERE/label
        receipt = json.loads((folder/'RECEIPT.json').read_bytes())
        require(receipt['child_exit_code'] == 0 and receipt['pass_and_inputs_stable'], label+' success')
        require(receipt['all_inputs_before'] == receipt['all_inputs_after'], label+' before/after')
        require(receipt['all_input_count'] == 30 == len(receipt['all_inputs_before']), label+' inputs')
        for name, reference in receipt['all_inputs_before'].items():
            require(info(ROOT/name) == reference, label+' current actual input: '+name)
            input_references += 1
        require(receipt['command'][1:3] == ['-I', '-B'], 'isolated source command')
        require(Path(receipt['command'][0]).is_file(), 'runtime binary exists')
        require(receipt['box_count'] == 262 and receipt['state_map_pairs'] == 14341, 'immutable box receipt')
        for key in ('stdout', 'stderr'):
            reference = receipt[key]
            require(info(folder/reference['path']) == {k: reference[k] for k in ('bytes', 'sha256')}, label+' '+key)
            output_references += 1
        comparison = receipt['raw_comparison']
        require(comparison['exit_code'] == 0, 'recorded raw cmp exit')
        for key in ('stdout', 'stderr'):
            reference = comparison[key]
            require(info(folder/reference['path']) == {k: reference[k] for k in ('bytes', 'sha256')}, 'cmp '+key)
            output_references += 1
        reference = comparison['canonical']
        require(info(ROOT/reference['path']) == {k: reference[k] for k in ('bytes', 'sha256')}, 'canonical bytes')
        output_references += 1
    comparisons = []
    for left, right in ((HERE/'execution_01/run.stdout', HERE/'execution_02/run.stdout'),
                        (HERE/'execution_01/run.stdout', HERE/'CANONICAL.json')):
        command = ['cmp', str(left), str(right)]
        child = subprocess.run(command, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False)
        require(child.returncode == 0 and not child.stdout and not child.stderr, 'actual raw comparison')
        comparisons.append({'command': command, 'exit_code': child.returncode})
    canonical = json.loads((HERE/'CANONICAL.json').read_bytes())
    require(canonical['assertion_total'] == 82023 == sum(canonical['assertions'].values()), 'assertion sum')
    require(len(canonical['boxes']) == 262, 'canonical box count')
    require(sum(b['state_count'] for b in canonical['boxes']) == 14341, 'canonical state count')
    print(json.dumps({'status': 'PASS_READ_ONLY_FIFTEENTH_ARTIFACT_AUDIT_NOT_REVIEW',
                      'manifest_count': len(manifests), 'manifest_entries': manifest_entries,
                      'outer_entries': len(parse_pins(HERE/'SHA256SUMS')),
                      'documentary_history_pins': external_pin_count,
                      'receipt_input_references': input_references,
                      'receipt_output_references': output_references,
                      'actual_raw_comparisons': comparisons,
                      'fresh_mathematical_executions': 0,
                      'source_erratum_preserved': (HERE/'SOURCE_ERRATUM.md').is_file(),
                      'external_status': 'HOLD_EXTERNAL'}, indent=2))


if __name__ == '__main__':
    main()
