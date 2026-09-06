"""Post-run evidence capture and complete nonself sealing, no science."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import time
import shutil

import record_execution as infrastructure

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[3]
MIRROR = Path('/root/autodl-tmp/hilbert-polya-structure')
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
sha, save, run = infrastructure.sha, infrastructure.save, infrastructure.run


def capture():
    out = BASE / 'evidence_capture_02'
    out.mkdir(exist_ok=False)
    comparator_files = [Path('/usr/bin/cmp').resolve(), Path('/usr/bin/ldd').resolve()]
    linked = subprocess.run(['/usr/bin/ldd', '/usr/bin/cmp'], env=ENV, capture_output=True, check=False)
    comparator_files += [Path(x).resolve() for x in linked.stdout.decode().split()
                        if x.startswith('/') and Path(x).is_file()]
    before = {str(p): sha(p) for p in comparator_files}
    save(out / 'comparator.before.json', before)
    pairs = [('pilot', 'execution_01', 'execution_02'),
             ('proof', 'proof_execution_01', 'proof_execution_02')]
    comparison = []
    for tag, left, right in pairs:
        a, b = BASE / left / 'producer.stdout', BASE / right / 'producer.stdout'
        inputs_before = {str(p): sha(p) for p in (a, b)}
        code = run(['/usr/bin/cmp', str(a), str(b)], out, tag + '.cmp', ENV)
        inputs_after = {str(p): sha(p) for p in (a, b)}
        comparison.append(dict(tag=tag, exit=code, source_before=inputs_before,
                               source_after=inputs_after, unchanged=inputs_before == inputs_after))
    after = {str(p): sha(p) for p in comparator_files}
    save(out / 'comparator.after.json', after)
    save(out / 'COMPARISON.json', dict(comparisons=comparison, runtime_unchanged=before == after,
        status='PASS' if before == after and all(r['exit'] == 0 and r['unchanged'] for r in comparison) else 'FAIL'))
    roots = [ROOT / 'papers', ROOT / 'docs', MIRROR / 'papers', MIRROR / 'docs',
             MIRROR / 'symbolic_dynamics/papers', MIRROR / 'symbolic_dynamics/docs']
    rg = str(Path(shutil.which('rg')).resolve())
    save(out / 'rg.before.json', {rg: sha(rg)})
    code = run([rg, '--files', *map(str, roots)], out, 'history_inventory', ENV)
    if code:
        raise SystemExit(code)
    candidates = (out / 'history_inventory.stdout').read_text().splitlines()
    selected = []
    for filename in candidates:
        p = Path(filename)
        lower = filename.lower()
        if any(token in lower for token in ('paper208', 'paper_208', '/p208', '/ofs',
            '/finite_systems_tenth', '/finite_systems_nineteenth', '/frozen', '/execution_',
            '/proof_execution_', '/runs/', '/artifact', '/runtime', '/source_inputs/')):
            continue
        if p.suffix == '.tex' or any(token in p.name.upper() for token in ('SCOUT', 'INTAKE', 'KILL', 'LEDGER', 'PROOF')):
            selected.append(filename)
    save(out / 'history_selected.json', sorted(selected))
    selected_before = {p: sha(p) for p in selected}
    save(out / 'history_search.before.json', selected_before)
    families = [
        ('functional', r'functional.digraph|fibre.thread|fiber.thread|next.sibling|last.child|ordered.preimage|star.to.chain|linearization|ISPRP'),
        ('equality', r'next.equal|next.occurrence|next.repetition|fibre.*chain|fiber.*chain|FSP|NOG|least.predecessor'),
        ('matching', r'matching.*consensus|consensus.*matching|majority.*matching|Brauer|alternating.path|Hurwitz'),
        ('relational', r'ternary.*relation|corner.*recombin|difunction|tetrahedr|all.but.one|unanimity|RR.*mathsf'),
        ('proof_engine', r'backward.height|backward.image|iterated.image.*inclus|path.cover.*fibre|path.cover.*fiber|maximum.*fibre|maximum.*fiber'),
    ]
    results = []
    for tag, query in families:
        command = [rg, '-n', '-i', '-e', query, *selected]
        exit_code = run(command, out, 'history_' + tag, ENV)
        results.append(dict(family=tag, query=query, exit=exit_code))
    selected_after = {p: sha(p) for p in selected}
    save(out / 'history_search.after.json', selected_after)
    save(out / 'rg.after.json', {rg: sha(rg)})
    save(out / 'HISTORY_SEARCH.json', dict(status='PASS' if selected_before == selected_after and
        all(x['exit'] in (0, 1) for x in results) else 'FAIL', selected_files=len(selected),
        roots=list(map(str, roots)), results=results, before_after_equal=selected_before == selected_after,
        scope='bounded discovery; no nonhit implies novelty; tenth/P208/OFS paths excluded'))
    historical = infrastructure.HISTORICAL + ['docs/papers204_208_sequence/scouting/FTH_ROOT_LOCAL_OBSERVATIONS.md']
    with (BASE / 'HISTORICAL_INPUTS.sha256').open('x', encoding='utf8') as target:
        for path in historical:
            target.write(sha(ROOT / path) + '  ' + path + '\n')
    print(json.dumps(dict(capture='DONE', selected_history_files=len(selected),
                          cmp_exits=[r['exit'] for r in comparison]), sort_keys=True))


def seal():
    manifest = BASE / 'SHA256SUMS'
    if manifest.exists():
        raise FileExistsError('seal already exists; do not silently overwrite')
    files = sorted(p for p in BASE.rglob('*') if p.is_file() and p != manifest)
    with manifest.open('x', encoding='utf8') as target:
        for p in files:
            target.write(sha(p) + '  ' + str(p.relative_to(BASE)) + '\n')
    verify = subprocess.run(['/usr/bin/sha256sum', '-c', 'SHA256SUMS'], cwd=BASE,
                            env=ENV, capture_output=True, check=False)
    print(json.dumps(dict(seal='PASS' if verify.returncode == 0 else 'FAIL', files=len(files),
        manifest_sha256=sha(manifest), total_bytes=sum(p.stat().st_size for p in files),
        verifier_exit=verify.returncode), sort_keys=True))
    if verify.returncode:
        print(verify.stdout.decode(), end='')
        print(verify.stderr.decode(), end='', file=sys.stderr)
        raise SystemExit(verify.returncode)


if __name__ == '__main__':
    {'capture': capture, 'seal': seal}[sys.argv[1]]()
