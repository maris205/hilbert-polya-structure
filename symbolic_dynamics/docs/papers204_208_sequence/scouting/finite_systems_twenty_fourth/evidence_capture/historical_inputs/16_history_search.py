"""Bounded read-only historical discovery; no mathematical map execution."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import time

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[3]
MIRROR = Path('/root/autodl-tmp/hilbert-polya-structure')
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
EXCLUDE = ('paper208', 'paper_208', '/p208', '/ofs', '/papers/208-',
    '/order_geometry_tenth', '/fth_gate/', '/finite_systems_nineteenth/',
    '/reviewed_input_snapshot/', '/input_snapshot/', '/source_only/', '/qa_',
    '/build_', '/cold_build_', '/finite_systems_tenth', '/finite_systems_twenty_third',
    '/reviews/', '/frozen', '/execution_', '/proof_execution_', '/runs/',
    '/artifact', '/runtime', '/source_inputs/')
QUERIES = [
    ('incidence', r'transitive.*(reduc|delet)|shortcut|triangle.*delet|two.step.*edge|bypass'),
    ('algebra', r'Gram|transpose.*commutator|commutator.*transpose|symmetric.*inverse.*monoid|sandwich|partial.*biject'),
    ('rewrite', r'free.*reduc|adjacent.*cancel|parallel.*cancel|Thue|Knuth|rewrit|plactic'),
]

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def save(path, obj):
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + '\n')

def run(argv, out, tag):
    save(out / (tag + '.ATTEMPT.json'), dict(argv=argv, cwd=str(ROOT),
        environment=ENV, started_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())))
    with (out / (tag + '.stdout')).open('xb') as stdout, (out / (tag + '.stderr')).open('xb') as stderr:
        proc = subprocess.run(argv, cwd=ROOT, env=ENV, stdout=stdout, stderr=stderr, check=False)
    save(out / (tag + '.RESULT.json'), dict(exit=proc.returncode,
        stdout_sha256=sha(out / (tag + '.stdout')), stderr_sha256=sha(out / (tag + '.stderr'))))
    return proc.returncode

def main():
    out = BASE / sys.argv[1]
    out.mkdir(exist_ok=False)
    roots = [ROOT / 'papers', ROOT / 'docs', MIRROR / 'papers', MIRROR / 'docs',
             MIRROR / 'symbolic_dynamics/papers', MIRROR / 'symbolic_dynamics/docs']
    rg = str(Path(shutil.which('rg')).resolve())
    save(out / 'rg.before.json', {rg: sha(rg)})
    assert run([rg, '--files', *map(str, roots)], out, 'inventory') == 0
    selected = []
    for filename in (out / 'inventory.stdout').read_text().splitlines():
        p = Path(filename)
        if any(token in filename.lower() for token in EXCLUDE):
            continue
        if p.suffix == '.tex' or any(token in p.name.upper() for token in ('SCOUT', 'INTAKE', 'KILL', 'LEDGER', 'PROOF')):
            selected.append(filename)
    selected.sort()
    save(out / 'selected.json', selected)
    before = {p: sha(p) for p in selected}
    save(out / 'inputs.before.json', before)
    rows = []
    for tag, query in QUERIES:
        code = run([rg, '-n', '-i', '-e', query, *selected], out, tag)
        rows.append(dict(tag=tag, query=query, exit=code))
    after = {p: sha(p) for p in selected}
    save(out / 'inputs.after.json', after)
    save(out / 'rg.after.json', {rg: sha(rg)})
    report = dict(status='PASS' if before == after and all(r['exit'] in (0, 1) for r in rows) else 'FAIL',
        selected_files=len(selected), roots=list(map(str, roots)), queries=rows,
        exclusions=EXCLUDE, excluded_remaining=[p for p in selected if any(t in p.lower() for t in EXCLUDE)],
        before_after_equal=before == after, scope='Discovery only; zero map executions; nonhits do not establish novelty.')
    save(out / 'REPORT.json', report)
    print(json.dumps(report, sort_keys=True))

if __name__ == '__main__':
    main()
