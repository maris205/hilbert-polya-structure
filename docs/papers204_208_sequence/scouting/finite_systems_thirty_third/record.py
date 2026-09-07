#!/usr/bin/env python3
"""Documentary recorder adapted from scout32/audit.py; not scientific code."""
import hashlib
import json
import pathlib
import re
import subprocess
import sys
import time

ROOT = pathlib.Path('/root/autodl-tmp/symbolic_dynamics')
OWN = ROOT / 'docs/papers204_208_sequence/scouting/finite_systems_thirty_third'

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def save(p, data):
    p.write_text(json.dumps(data, indent=2, sort_keys=True) + '\n')

def run(label, argv, inputs=()):
    out = OWN / 'commands' / label
    out.mkdir(parents=True, exist_ok=False)
    rels = sorted(set(map(str, inputs)))
    save(out / 'pathset.json', rels)
    before = {p: digest(ROOT / p) for p in rels}
    save(out / 'inputs_before.json', before)
    start = time.time()
    result = subprocess.run(argv, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (out / 'stdout.raw').write_bytes(result.stdout)
    (out / 'stderr.raw').write_bytes(result.stderr)
    after = {p: digest(ROOT / p) for p in rels}
    save(out / 'inputs_after.json', after)
    receipt = dict(label=label, argv=argv, cwd=str(ROOT), exit=result.returncode,
                   started_epoch=start, finished_epoch=time.time(), input_count=len(rels),
                   unchanged=before == after, recorder_sha256=digest(pathlib.Path(__file__)),
                   stdout_sha256=hashlib.sha256(result.stdout).hexdigest(),
                   stderr_sha256=hashlib.sha256(result.stderr).hexdigest())
    save(out / 'receipt.json', receipt)
    print(json.dumps({k: v for k, v in receipt.items() if k != 'argv'}))
    return result

def original(p):
    parts = p.split('/')
    if str(OWN.relative_to(ROOT)) in p:
        return False
    if any(re.search(r'review|qa|freez|froz|snapshot|source|runtime|history|historical|command|build|compile|copied|receipt|execution', s, re.I) for s in parts[:-1]):
        return False
    if any(re.search(r'(^|[^a-z0-9])(p?208|p?209|ofs|fth)([^a-z0-9]|$)', s, re.I) for s in parts[2:] if not re.fullmatch(r'papers[0-9]+_[0-9]+_sequence', s)):
        return False
    if re.match(r'papers/(208|209)-', p):
        return False
    if re.fullmatch(r'papers/[0-9]+-[^/]+/(main\.tex|sections/[^/]+\.tex|PROOF_PACKAGE\.md)', p):
        return True
    if re.fullmatch(r'docs/papers[0-9]+_[0-9]+_sequence/scouting/[^/]+/[^/]+\.md', p):
        return any(s in parts[-1] for s in ('PROOF', 'SCOUT_REPORT', 'KILL', 'CANDIDATE_LEDGER', 'INTAKE', 'DISPOSITION', 'COLLISION', 'THEOREM', 'DOSSIER'))
    return bool(re.fullmatch(r'docs/papers[0-9]+_[0-9]+_sequence/phase1/(CANDIDATE_POOL_AND_KILL_LEDGER|THEOREM_CONTRACTS|SYSTEM_COLLISION_FIREWALL)\.md', p))

def main():
    op = sys.argv[1]
    if op == 'discover':
        argv = ['rg', '--files', 'papers', 'docs', '-g', '*.md', '-g', '*.tex']
        for pattern in ('**/reviews/**', '**/qa/**', '**/*froz*/**', '**/*freez*/**', '**/*snapshot*/**', '**/*source*/**', '**/*runtime*/**', '**/*history*/**', '**/*historical*/**', '**/*commands*/**', '**/*build*/**', '**/*compile*/**', '**/*copied*/**', '**/*receipts*/**', '**/*execution*/**', 'papers/208-*/**', 'papers/209-*/**', '**/OFS*/**', '**/FTH*/**'):
            argv += ['-g', '!' + pattern]
        r = run('01_path_discovery', argv, [str((OWN / 'SCOPE.md').relative_to(ROOT)), str(pathlib.Path(__file__).relative_to(ROOT))])
        listed = r.stdout.decode().splitlines()
        selected = sorted(p for p in listed if original(p))
        save(OWN / 'SELECTED_ORIGINALS.json', selected)
        print(json.dumps(dict(discovered=len(listed), selected=len(selected))))
    elif op == 'verify_paths':
        selected = json.loads((OWN / 'SELECTED_ORIGINALS.json').read_text())
        assert selected == sorted(set(selected))
        for p in selected:
            assert original(p), p
            assert (ROOT / p).is_file() and not (ROOT / p).is_symlink(), p
            print(p)
        print(json.dumps(dict(actual_paths=len(selected), all_grammar_valid=True)))
    elif op == 'search':
        label, pattern = sys.argv[2:4]
        selected = json.loads((OWN / 'SELECTED_ORIGINALS.json').read_text())
        assert all(original(p) and (ROOT / p).is_file() for p in selected)
        run(label, ['rg', '-n', '-i', '--', pattern] + selected, selected)
    elif op == 'read':
        label, path = sys.argv[2:4]
        assert original(path) or path.startswith(str(OWN.relative_to(ROOT)) + '/'), path
        run(label, ['sed', '-n', sys.argv[4] if len(sys.argv)>4 else '1,99999p', path], [path])
    elif op == 'seal':
        target = OWN / 'SHA256SUMS'
        assert not target.exists()
        paths = sorted(p for p in OWN.rglob('*') if p.is_file() and p != target)
        target.write_text(''.join(digest(p) + '  ' + str(p.relative_to(OWN)) + '\n' for p in paths))
        print(json.dumps(dict(payloads=len(paths), sha256=digest(target))))
    else:
        raise SystemExit(op)

if __name__ == '__main__':
    main()
