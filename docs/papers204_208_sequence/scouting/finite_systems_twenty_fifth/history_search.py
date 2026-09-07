"""Twenty-fifth read-only discovery; no scientific map evaluation."""
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
EXCLUDE = ('paper208', 'paper_208', '/p208', '/papers/208-', 'paper209', 'paper_209',
    '/p209', '/papers/209-', '/ofs', '/order_geometry_tenth', '/fth',
    '/finite_systems_nineteenth/', '/finite_systems_tenth/',
    '/finite_systems_twenty_fifth/', '/reviews/', '/reviewers/',
    '/reviewed_input', '/input_snapshot/', '/source_only', '/qa/', '/qa_', '/build_',
    '/cold_build_', '/frozen', '/execution_', '/proof_execution_', '/runs/',
    '/artifact', '/runtime', '/source_inputs/', '/historical_inputs/', '/current_inputs/')
QUERIES = [
    ('local', r'cyclic.cellular|Greenberg|Hastings|excitable|predator|multicolou?r|multistate|three.colou?r|three.state|quasigroup|quandle|permutive'),
    ('metric', r'distance.two|2.distance|common.neighbou?r|weighted.tree|tree.metric|ultrametric|dissimilarity|eccentricity|tropical|bottleneck|min.max'),
    ('coupling', r'conjugat.*(neighbou?r|cyclic)|cyclic.*conjugat|colour.*relation|color.*relation|edge.colou?r|relation.*squar|neighbou?r.*exchange'),
]

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def save(path, obj):
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + '\n')

def run(argv, out, tag):
    save(out / (tag + '.ATTEMPT.json'), dict(argv=argv, cwd=str(ROOT), environment=ENV,
        started_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())))
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
    recorder = str(Path(__file__).resolve())
    save(out / 'tools.before.json', {p: sha(p) for p in (recorder, rg)})
    assert run([rg, '--files', *map(str, roots)], out, 'inventory') == 0
    selected = []
    pdfs = []
    for filename in (out / 'inventory.stdout').read_text().splitlines():
        p = Path(filename)
        if any(token in filename.lower() for token in EXCLUDE) or 'review' in p.name.lower():
            continue
        if p.suffix == '.tex' or any(token in p.name.upper() for token in ('SCOUT', 'INTAKE', 'KILL', 'LEDGER', 'PROOF')):
            selected.append(filename)
        if p.suffix == '.pdf' and str(p).startswith(str(ROOT / 'papers')):
            pdfs.append(filename)
    selected.sort()
    save(out / 'selected.json', selected)
    save(out / 'local_pdf_filenames.json', sorted(pdfs))
    before = {p: sha(p) for p in selected}
    save(out / 'inputs.before.json', before)
    rows = []
    for tag, query in QUERIES:
        code = run([rg, '-n', '-i', '-e', query, *selected], out, tag)
        rows.append(dict(tag=tag, query=query, exit=code,
            output_lines=len((out / (tag + '.stdout')).read_text().splitlines())))
    after = {p: sha(p) for p in selected}
    save(out / 'inputs.after.json', after)
    save(out / 'tools.after.json', {p: sha(p) for p in (recorder, rg)})
    report = dict(status='PASS' if before == after and all(r['exit'] in (0, 1) for r in rows) else 'FAIL',
        selected_files=len(selected), roots=list(map(str, roots)), queries=rows,
        exclusions=EXCLUDE, excluded_remaining=[p for p in selected if any(t in p.lower() for t in EXCLUDE) or 'review' in Path(p).name.lower()],
        before_after_equal=before == after, scope='Discovery only; zero science-map evaluations; nonhits do not establish novelty.')
    save(out / 'REPORT.json', report)
    print(json.dumps(report, sort_keys=True))

if __name__ == '__main__':
    main()
