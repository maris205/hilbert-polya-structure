#!/usr/bin/env python3
"""Append-only documentary recorder; no mathematical producer imported."""
import hashlib
import json
import pathlib
import re
import subprocess
import sys
import time

ROOT = pathlib.Path('/root/autodl-tmp/symbolic_dynamics')
OWN = ROOT / 'docs/papers204_208_sequence/scouting/finite_systems_thirty_second'

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def run(label, argv, inputs=()):
    out = OWN / 'commands' / label
    out.mkdir(parents=True, exist_ok=False)
    rels = sorted(set(str(p) for p in inputs))
    paths = [ROOT / p for p in rels]
    (out / 'pathset.json').write_text(json.dumps(rels, indent=2) + '\n')
    before = {p: digest(ROOT / p) for p in rels}
    (out / 'inputs_before.json').write_text(json.dumps(before, indent=2) + '\n')
    start = time.time()
    result = subprocess.run(argv, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out / 'stdout.raw').write_bytes(result.stdout)
    (out / 'stderr.raw').write_bytes(result.stderr)
    after = {p: digest(ROOT / p) for p in rels}
    (out / 'inputs_after.json').write_text(json.dumps(after, indent=2) + '\n')
    receipt = dict(label=label, argv=argv, cwd=str(ROOT), exit=result.returncode,
                   started_epoch=start, finished_epoch=time.time(),
                   input_count=len(rels), unchanged=before == after,
                   recorder_sha256=digest(pathlib.Path(__file__)),
                   stdout_sha256=hashlib.sha256(result.stdout).hexdigest(),
                   stderr_sha256=hashlib.sha256(result.stderr).hexdigest())
    (out / 'receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    print(json.dumps({k: v for k, v in receipt.items() if k != 'argv'}))
    return result

def original(p):
    if str(OWN.relative_to(ROOT)) in p:
        return False
    if any(re.search(r'review|qa|freez|snapshot|source|runtime|history|historical|command|build|compile|copied|receipt|execution', s, re.I) for s in p.split('/')[:-1]):
        return False
    if re.fullmatch(r'papers/[0-9]+-[^/]+/(main\.tex|sections/[^/]+\.tex|PROOF_PACKAGE\.md)', p):
        return True
    if re.fullmatch(r'docs/papers[0-9]+_[0-9]+_sequence/scouting/[^/]+/[^/]+\.md', p):
        return any(s in p.rsplit('/', 1)[1] for s in ('PROOF', 'SCOUT_REPORT', 'KILL', 'CANDIDATE_LEDGER', 'INTAKE', 'DISPOSITION', 'HANDOFF', 'COLLISION', 'THEOREM', 'DOSSIER'))
    return bool(re.fullmatch(r'docs/papers[0-9]+_[0-9]+_sequence/phase1/(CANDIDATE_POOL_AND_KILL_LEDGER|THEOREM_CONTRACTS|SYSTEM_COLLISION_FIREWALL)\.md', p))

def main():
    op = sys.argv[1]
    if op == 'discover':
        argv = ['rg', '--files', 'papers', 'docs', '-g', '*.md', '-g', '*.tex']
        for pattern in ('**/reviews/**', '**/qa/**', '**/*froz*/**', '**/*freez*/**', '**/*snapshot*/**', '**/*source*/**', '**/*runtime*/**', '**/*history*/**', '**/*historical*/**', '**/*commands*/**', '**/*build*/**', '**/*compile*/**', '**/*copied*/**', '**/*receipts*/**', '**/*execution*/**'):
            argv += ['-g', '!' + pattern]
        result = run('01_path_discovery', argv, [str((OWN / 'SCOPE.md').relative_to(ROOT))])
        listed = result.stdout.decode().splitlines()
        selected = sorted(p for p in listed if original(p))
        (OWN / 'SELECTED_ORIGINALS.json').write_text(json.dumps(selected, indent=2) + '\n')
        print(json.dumps(dict(discovered=len(listed), selected=len(selected))))
    elif op == 'search':
        label, pattern = sys.argv[2:4]
        selected = json.loads((OWN / 'SELECTED_ORIGINALS.json').read_text())
        if not all(original(p) for p in selected):
            raise SystemExit('Invalid historical pathset')
        run(label, ['rg', '-n', '-i', '--', pattern] + selected, selected)
    elif op == 'read':
        label, path = sys.argv[2:4]
        if not original(path) and not path.startswith(str(OWN.relative_to(ROOT)) + '/'):
            raise SystemExit('Read target outside original-only policy')
        run(label, ['sed', '-n', sys.argv[4] if len(sys.argv)>4 else '1,99999p', path], [path])
    elif op == 'control':
        label, path = sys.argv[2:4]
        allowed = [str(OWN.relative_to(ROOT)) + '/controls/' + s for s in ('SYMBOLIC_DYNAMICS_STATE.md','PIPELINE_STATE.md','GIT_SYNC_RECEIPT.md')]
        if path not in allowed:
            raise SystemExit('Not an initial copied control')
        run(label, ['sed', '-n', sys.argv[4] if len(sys.argv)>4 else '1,99999p', path], [path])
    elif op == 'seal':
        paths = sorted(p for p in OWN.rglob('*') if p.is_file() and p != OWN / 'SHA256SUMS')
        target = OWN / 'SHA256SUMS'
        if target.exists():
            raise SystemExit('Do not overwrite a seal')
        target.write_text(''.join(digest(p) + '  ' + str(p.relative_to(OWN)) + '\n' for p in paths))
        print(json.dumps(dict(payloads=len(paths), sha256=digest(target))))
    else:
        raise SystemExit(op)

if __name__ == '__main__':
    main()
