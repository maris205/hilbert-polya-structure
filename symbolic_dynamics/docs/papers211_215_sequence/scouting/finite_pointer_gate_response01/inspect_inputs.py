#!/usr/bin/env python3
"""Read-only attribution/history artifact check. No science import or run.

Manuscript bytes are used only for recorded-read equality/line-count/hash.
No proof, equation, scientific source or coefficient is parsed or evaluated.
"""
from hashlib import sha256
import json
from pathlib import Path

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
BATCH = ROOT / 'docs/papers211_215_sequence'
SCOUTING = BATCH / 'scouting'
GATE = SCOUTING / 'finite_pointer_residual_gate'
AUTHOR = SCOUTING / 'finite_local_state_fresh_desk'
reads = {}
checks = 0

def need(test, reason):
    global checks
    checks += 1
    if not test:
        raise AssertionError(reason)

def read(path):
    path = Path(path)
    need(path.is_file() and not path.is_symlink(), ('ordinary_original', str(path)))
    data = path.read_bytes()
    reads[str(path)] = {'sha256': sha256(data).hexdigest(), 'bytes': len(data)}
    return data

def obj(path):
    return json.loads(read(path))

def manifest(base, expected_count, expected_digest):
    data = read(base / 'MANIFEST.sha256')
    need(sha256(data).hexdigest() == expected_digest, 'pinned_original_manifest')
    names = []
    for line in data.decode().splitlines():
        digest, name = line.split('  ', 1)
        rel = Path(name)
        need(not rel.is_absolute() and '..' not in rel.parts and name != 'MANIFEST.sha256', 'safe_nonself_row')
        need(sha256(read(base / name)).hexdigest() == digest, ('original_payload_pin', name))
        names.append(name)
    need(len(names) == len(set(names)) == expected_count, 'exact_manifest_count')
    need({p.relative_to(base).as_posix() for p in base.rglob('*') if p.is_file()} ==
         set(names) | {'MANIFEST.sha256'}, 'complete_original_inventory')

def main():
    manifest(GATE, 8, 'da1bf1d5a2daf9e1de2b4731187dab2029dd02b25ec8aa8b14fa55b5f63f1364')
    manifest(AUTHOR, 5, 'd6299f026e02195f145f33f819dcedb27b367c300280b3d3f7255fea1e136ada')
    findings = obj(GATE / 'FINDINGS.json')
    need([(r['id'], r['status']) for r in findings['major']] == [('PTR-G-E1', 'OPEN')], 'E1_remains_open')
    need([(r['id'], r['status']) for r in findings['minor']] == [
        ('PTR-G-S1', 'OPEN'), ('PTR-G-C1', 'OPEN'), ('PTR-G-D1', 'OPEN')], 'reviewer_minors_remain_open')
    author_records = obj(AUTHOR / 'NATIVE_READS.json')['records']
    old = [r for r in author_records if r['result'].get('chunk_id') == 'c59488']
    need(len(old) == 1, 'unique_original_read')
    old = old[0]
    need(old['cmd'] == "sed -n '1,180p' papers/167-minimum-inverse-position-feedback/main.tex" and
         old['result']['exit_code'] == 0, 'actual_original_command_and_exit')
    gate_records = obj(GATE / 'NATIVE_READS.json')['records']
    later = [r for r in gate_records if r['args']['cmd'] == 'cat papers/167-minimum-inverse-position-feedback/main.tex']
    need(len(later) == 1 and later[0]['result']['exit_code'] == 0, 'unique_separate_gate_full_read')
    later = later[0]
    source_path = ROOT / 'papers/167-minimum-inverse-position-feedback/main.tex'
    source = read(source_path)
    need(sha256(source).hexdigest() == '500fdea81499204a92bd3b6e24c5f9fd7b758d29b5c5dcdbf60e5e3f8e861d73',
         'same_pinned_P167_original')
    need(len(source.splitlines()) == 385, 'actual_385_lines')
    need(old['result']['output'].encode() == b''.join(source.splitlines(keepends=True)[:180]),
         'old_native_output_exact_first180_only')
    need(later['result']['output'].encode() == source, 'later_gate_native_output_exact_complete385')
    for path, digest in [
        (SCOUTING / 'finite_pointer_pilot_preparation01/MANIFEST.sha256',
         '828b135ed4aefbb9d0a1f030e52b48c45c32288ff05d6ea413946bcbcf104a75'),
        (BATCH / 'qa/finite_pointer_runtime_preparation01/MANIFEST.sha256',
         'bb71a0b54f367f3c1116263081f06f37817677ed334788c1b1950227ba1f07f7')]:
        need(sha256(read(path)).hexdigest() == digest, 'unchanged_adjacent_control_manifest_only')
    print(json.dumps({'status': 'PASS_DOCUMENTARY_INPUT_CHECK_ONLY', 'checks': checks,
          'inputs': reads, 'history': {
              'original': {'chunk_id': old['result']['chunk_id'], 'command': old['cmd'],
                           'line_count': len(old['result']['output'].splitlines()),
                           'last_line': old['result']['output'].splitlines()[-1],
                           'native_exit': old['result']['exit_code'], 'exact_source_prefix': True},
              'later_gate': {'chunk_id': later['result']['chunk_id'], 'command': later['args']['cmd'],
                             'line_count': len(later['result']['output'].splitlines()),
                             'native_exit': later['result']['exit_code'], 'exact_full_source': True}},
          'open_findings': ['PTR-G-E1', 'PTR-G-S1', 'PTR-G-C1', 'PTR-G-D1'],
          'scientific_execution_or_import_count': 0,
          'scope': 'Complete 8/5 gate/author manifests and mechanical archival read binding; adjacent pilot/runtime manifest pins only, not their payload re-audits.'},
          sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
