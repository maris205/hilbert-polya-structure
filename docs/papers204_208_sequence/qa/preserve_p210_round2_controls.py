#!/usr/bin/env python3
"""One-shot exact control preservation before the actual P210 Round2 milestone."""
from pathlib import Path
from hashlib import sha256
import json
import subprocess

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
QA = ROOT / 'docs/papers204_208_sequence/qa'
OUT = QA / 'central_round2_p210'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
INPUTS = {
    "/root/autodl-tmp/symbolic_dynamics/SYMBOLIC_DYNAMICS_STATE.md": "793212fc1470dca28e97851eb19d356d26ce3ee6199320efac5bca1dc8b58158",
    "/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/FINAL_THEOREM_CONTRACTS.md": "329cb32f4764dd59b1a500a8c21ef7dd4b2d83c87dd781d9934a413142f2a914",
    "/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/GIT_SYNC_RECEIPT.md": "55b13eb843175a36a7027eafcaa3324dc0251970920faf5ff4b58b1cab1215cc",
    "/root/autodl-tmp/symbolic_dynamics/docs/papers204_208_sequence/PIPELINE_STATE.md": "592b60ef55cc39f1efdf8c81459beff8e55c9d86bce0e2eb0213aeafdb1d595d"
}

def info(path):
    path = Path(path)
    assert path.is_file() and not path.is_symlink() and path.resolve() == path
    data = path.read_bytes()
    return {'bytes': len(data), 'sha256': sha256(data).hexdigest()}

def main():
    closure = QA / 'P210_B_ROOT_DELTA_INSPECTION.actual.json'
    completed = QA / 'P210_ROUND2_ROOT_INSPECTION_COMPLETION.actual.json'
    assert info(closure)['sha256'] == '56e82ffa5554853023b940369727ffba100bd3f82a8518c3804c206a063e6adc'
    assert info(completed)['sha256'] == 'f928c5436fbc079ef8eb4a6973ecd82af5c9e61b9a85882e8f18509f85bea983'
    accepted = json.loads(closure.read_bytes())
    actual = json.loads(completed.read_bytes())['result']
    assert accepted['status'] == 'ROOT_ACCEPTED_B_DELTA_ORIGINAL_CLOSURE_PASS' and accepted['current_open_findings'] == 0
    assert actual['exit_code'] == 0 and json.loads(actual['output'])['status'] == 'PASS_ROOT_PHYSICAL_P210_ROUND2_RECEPTION'
    assert Path.cwd() == ROOT and not OUT.exists()
    before = {p: info(p) for p in INPUTS}
    assert all(before[p]['sha256'] == value for p, value in INPUTS.items())
    OUT.mkdir()
    records = []
    for name in INPUTS:
        source = Path(name)
        target = OUT / source.name
        assert not target.exists()
        commands = []
        for argv in (['/usr/bin/cp', '--', str(source), str(target)],
                     ['/usr/bin/cmp', '--', str(source), str(target)]):
            run = subprocess.run(argv, cwd=ROOT, env=ENV, capture_output=True, timeout=60)
            commands.append({'argv': argv, 'cwd': str(ROOT), 'environment': ENV,
                'exit_code': run.returncode, 'stdout': run.stdout.decode(), 'stderr': run.stderr.decode()})
            assert run.returncode == 0 and run.stdout == run.stderr == b''
        row = {'original': name, 'copy': str(target), 'before': before[name],
               'copy_pin': info(target), 'after': info(source), 'commands': commands}
        assert row['before'] == row['copy_pin'] == row['after']
        records.append(row)
    assert {p: info(p) for p in INPUTS} == before
    result = {'status': 'PASS_FOUR_EXACT_PRE_P210_ROUND2_CONTROL_COPIES',
        'prerequisites': {str(p): info(p) for p in (closure, completed)}, 'source': info(Path(__file__).resolve()),
        'copies': records, 'new_scientific_build_or_view_executions': 0, 'external_status': 'HOLD_EXTERNAL'}
    with (OUT / 'PRESERVATION.actual.json').open('x') as stream:
        json.dump(result, stream, sort_keys=True, indent=2)
        stream.write('\n')
    readme = """# Exact pre-Round2 central control originals

These four physical copies preserve the immediately preceding batch,
theorem-contract, recovery and private-Git receipt bytes before the current
P210 accepted-B/physical-Round2 index update. The actual accepted B and
separate native-zero Round2 reception were checked before copying.
All original source paths, hashes, complete native cp/cmp returns and
before/copy/after equality appear in PRESERVATION.actual.json.

The copied Markdown retains its original document origin and historical
pending scope. It is not a new current index, scientific claim, private
push or five-paper acceptance. No accepted manuscript/review/frozen input
was changed. The live Git receipt has merely been copied, not updated or
asserted to include later material. OWNER_AMBER / HOLD_EXTERNAL.
"""
    with (OUT / 'README.md').open('x') as stream:
        stream.write(readme)
    members = sorted(p for p in OUT.iterdir() if p.is_file())
    assert len(members) == 6
    manifest = ''.join(info(p)['sha256'] + '  ' + p.name + '\n' for p in members)
    with (OUT / 'SHA256SUMS').open('x') as stream:
        stream.write(manifest)
    assert (OUT / 'SHA256SUMS').read_text() == manifest
    assert {p.name for p in OUT.iterdir()} == {p.name for p in members} | {'SHA256SUMS'}
    for p in members:
        assert info(p)['sha256'] in manifest
    print(json.dumps({'status': result['status'], 'preserved_controls': 4,
        'actual_native_copy_comparisons': 8, 'payloads': 6, 'physical_files': 7,
        'manifest_sha256': info(OUT / 'SHA256SUMS')['sha256'],
        'preservation_record': info(OUT / 'PRESERVATION.actual.json')}, sort_keys=True))

if __name__ == '__main__':
    main()

