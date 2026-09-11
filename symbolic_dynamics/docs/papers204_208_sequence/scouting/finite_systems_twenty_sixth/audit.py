"""Current documentary audit; not a scientific producer or hermetic replay."""
import hashlib
import json
from pathlib import Path
import sys

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BASE = ROOT / 'docs/papers204_208_sequence/scouting/finite_systems_twenty_sixth'

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None

def read(path):
    return json.loads(path.read_text())

def main():
    errors = []
    snapshots = []
    original_checks = []
    for label in ['controls', 'focused_controls', 'structural_controls', 'originals']:
        for entry in read(BASE / 'history' / f'{label}.json'):
            item = dict(entry, label=label)
            item['snapshot_current_sha256'] = digest(BASE / entry['snapshot'])
            item['origin_current_sha256'] = digest(ROOT / entry['origin'])
            if item['snapshot_current_sha256'] != entry['sha256']:
                errors.append({'kind': 'snapshot_drift', **item})
            if label == 'originals':
                original_checks.append(item)
                if item['origin_current_sha256'] != entry['sha256']:
                    errors.append({'kind': 'scientific_original_drift', **item})
            snapshots.append(item)

    selected = (BASE / 'evidence/selected_paths.txt').read_text().splitlines()
    scope = read(BASE / 'evidence/search_scope.json')
    discovery = (BASE / 'evidence/discovery_paths/stdout.bin').read_text().splitlines()
    reconstructed = sorted(n for n in discovery if n.endswith(('.md', '.tex'))
        and not any(x in n for x in scope['exclusions']))
    if selected != reconstructed or len(selected) != scope['count']:
        errors.append({'kind': 'discovery_selection_mismatch'})
    aliases = []
    searches = []
    lifecycle = {'SYMBOLIC_DYNAMICS_STATE.md',
                 'docs/papers204_208_sequence/PIPELINE_STATE.md'}
    for label in ['search', 'focused', 'structural']:
        before = read(BASE / 'evidence' / f'{label}_inputs_before.json')
        after = read(BASE / 'evidence' / f'{label}_inputs_after.json')
        if before != after or [r['path'] for r in before] != selected:
            errors.append({'kind': 'search_pinset_mismatch', 'search': label})
        current_exact = 0
        drift_count = 0
        for entry in before:
            current = digest(ROOT / entry['path'])
            if current == entry['sha256']:
                current_exact += 1
                continue
            drift_count += 1
            candidates = [r for r in snapshots if r['origin'] == entry['path']
                and r['sha256'] == entry['sha256']
                and r['snapshot_current_sha256'] == entry['sha256']]
            if entry['path'] in lifecycle and candidates:
                aliases.append({'search': label, 'origin': entry['path'],
                    'expected_sha256': entry['sha256'],
                    'current_origin_sha256': current,
                    'physical_alias': candidates[0]['snapshot'],
                    'physical_alias_sha256': candidates[0]['snapshot_current_sha256'],
                    'scope': 'exact historical lifecycle input, not scientific substitution'})
            else:
                errors.append({'kind': 'unresolved_search_input_drift',
                               'search': label, **entry, 'current_sha256': current})
        searches.append({'search': label, 'entries': len(before),
            'before_after_identical': before == after,
            'current_exact': current_exact, 'current_drift': drift_count})

    receipt_checks = []
    for path in sorted((BASE / 'evidence').glob('*/receipt.json')):
        receipt = read(path)
        ok = all(digest(path.parent / f'{channel}.bin') == receipt[f'{channel}_sha256']
                 for channel in ['stdout', 'stderr'])
        receipt_checks.append({'receipt': str(path.relative_to(BASE)),
            'exit': receipt['exit'], 'streams_exact': ok,
            'stdout_bytes': (path.parent / 'stdout.bin').stat().st_size,
            'stderr_bytes': (path.parent / 'stderr.bin').stat().st_size})
        if not ok:
            errors.append({'kind': 'receipt_stream_mismatch', 'receipt': str(path)})
    binary_checks = []
    for pin in read(BASE / 'evidence/named_tool_pins.json'):
        current = digest(Path(pin['path'])) if pin['path'] else None
        binary_checks.append(dict(pin, current_sha256=current,
                                  current_exact=current == pin['sha256']))
        if current != pin['sha256']:
            errors.append({'kind': 'named_binary_drift', 'name': pin['name']})
    result = {'audit_scope': 'documentary current check only; no hermetic/scientific replay',
        'searches': searches, 'aliases': aliases, 'snapshots_checked': len(snapshots),
        'scientific_originals_checked': len(original_checks),
        'scientific_originals_current_exact': all(r['origin_current_sha256'] == r['sha256']
                                                 for r in original_checks),
        'receipt_checks': receipt_checks, 'binary_checks': binary_checks,
        'errors': errors, 'pass': not errors}
    print(json.dumps(result, indent=2))
    return 0 if not errors else 1

if __name__ == '__main__':
    sys.exit(main())
