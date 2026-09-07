"""Terminal source/history archival and nonself seal for a zero-pilot desk."""
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
HISTORICAL = [
    'SYMBOLIC_DYNAMICS_STATE.md',
    'docs/papers204_208_sequence/PIPELINE_STATE.md',
    'docs/research_state/WORKFLOW.md',
    'docs/research_state/HISTORY_AND_CAVEATS.md',
    'docs/papers204_208_sequence/PROBLEM_ANCHOR.md',
    'docs/papers197_201_sequence/PROBLEM_ANCHOR.md',
    'docs/papers204_208_sequence/scouting/ROOT_PREINTAKE_EXCLUSIONS_20260906.md',
    'docs/papers122_126_sequence/scouting/algebraic/SCOUT.md',
    'docs/papers117_121_sequence/scouting/COMBINATORIAL_SCOUT.md',
    'docs/papers157_161_sequence/scouting/algebraic/SCOUT.md',
    'docs/papers152_156_sequence/scouting/algebraic_replacement2/SCOUT.md',
    'docs/papers204_208_sequence/scouting/algebra_third/SCOUT_REPORT.md',
    'docs/papers204_208_sequence/scouting/finite_systems_thirteenth/INTAKE.md',
    'docs/papers204_208_sequence/scouting/finite_systems_twentieth/INTAKE.md',
    'docs/papers204_208_sequence/scouting/finite_systems_seventeenth/INTAKE.md',
    'docs/papers204_208_sequence/scouting/finite_systems_eighteenth/PROOF_AND_ADAPTERS.md',
    'docs/papers187_191_sequence/scouting/graph_lane/CANDIDATES.md',
    'docs/papers187_191_sequence/scouting/graph_lane/KILL_LEDGER.md',
    'docs/papers204_208_sequence/scouting/finite_systems_twenty_second/evidence.py',
]
EXCLUDE = ('paper208', 'paper_208', '/p208', '/ofs', '/papers/208-',
    '/order_geometry_tenth', '/fth', '/finite_systems_nineteenth/',
    '/reviewed_input_snapshot/', '/input_snapshot/', '/source_only/', '/qa_',
    '/build_', '/cold_build_', '/finite_systems_tenth', '/finite_systems_twenty_third',
    '/reviews/', '/frozen', '/execution_', '/proof_execution_', '/runs/',
    '/artifact', '/runtime', '/source_inputs/', '/historical_inputs/', '/current_inputs/')

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def save(path, obj):
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + '\n')

def run(argv, cwd, out, tag):
    save(out / (tag + '.ATTEMPT.json'), dict(argv=argv, cwd=str(cwd), environment=ENV,
        start_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())))
    with (out / (tag + '.stdout')).open('xb') as stdout, (out / (tag + '.stderr')).open('xb') as stderr:
        proc = subprocess.run(argv, cwd=cwd, env=ENV, stdout=stdout, stderr=stderr, check=False)
    save(out / (tag + '.RESULT.json'), dict(exit=proc.returncode,
        stdout_sha256=sha(out / (tag + '.stdout')), stderr_sha256=sha(out / (tag + '.stderr'))))
    return proc.returncode

def archive():
    out = BASE / 'terminal_history'
    out.mkdir(exist_ok=False)
    archive_dir = BASE / 'historical_inputs'
    archive_dir.mkdir(exist_ok=False)
    source_before = {str(BASE / 'finish.py'): sha(BASE / 'finish.py')}
    save(out / 'recorder.before.json', source_before)
    before = {name: sha(ROOT / name) for name in HISTORICAL}
    save(out / 'named_history.before.json', before)
    for name in HISTORICAL:
        target = archive_dir / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(ROOT / name, target)
    after = {name: sha(ROOT / name) for name in HISTORICAL}
    copies = {name: sha(archive_dir / name) for name in HISTORICAL}
    save(out / 'named_history.after.json', after)
    save(out / 'named_history.copies.json', copies)
    manifest = BASE / 'HISTORICAL_INPUTS.sha256'
    with manifest.open('x', encoding='utf8') as target:
        for name in HISTORICAL:
            target.write(before[name] + '  ' + name + '\n')
    live_exit = run(['/usr/bin/sha256sum', '-c', str(manifest)], ROOT, out, 'history_live_check')
    copy_exit = run(['/usr/bin/sha256sum', '-c', str(manifest)], archive_dir, out, 'history_copy_check')
    roots = [ROOT / 'papers', ROOT / 'docs', MIRROR / 'papers', MIRROR / 'docs',
             MIRROR / 'symbolic_dynamics/papers', MIRROR / 'symbolic_dynamics/docs']
    rg = str(Path(shutil.which('rg')).resolve())
    save(out / 'rg.before.json', {rg: sha(rg)})
    assert run([rg, '--files', *map(str, roots)], ROOT, out, 'inventory') == 0
    selected = []
    for filename in (out / 'inventory.stdout').read_text().splitlines():
        p = Path(filename)
        if any(token in filename.lower() for token in EXCLUDE) or 'review' in p.name.lower():
            continue
        if p.suffix == '.tex' or any(token in p.name.upper() for token in ('SCOUT', 'INTAKE', 'KILL', 'LEDGER', 'PROOF')):
            selected.append(filename)
    selected.sort()
    save(out / 'selected.json', selected)
    selected_before = {p: sha(p) for p in selected}
    save(out / 'selected.before.json', selected_before)
    queries = [
        ('msp', r'Vieta|sum.product|sum.product.feedback|matrix.solvent|quadratic.matrix.equation|\(x\+y,xy\)|\(a\+b,ab\)'),
        ('mfi', r'facet.nerve|square.nerve|nerve.iteration|strong.core|strong.collaps|dominated.vert|facet.incidence'),
        ('controls', r'Gram.cube|transpose.commutator|adjacent.equal.cancell|transitive.reduction|double.blocker'),
    ]
    rows = []
    for tag, query in queries:
        code = run([rg, '-n', '-i', '-e', query, *selected], ROOT, out, tag)
        rows.append(dict(tag=tag, query=query, exit=code))
    selected_after = {p: sha(p) for p in selected}
    save(out / 'selected.after.json', selected_after)
    save(out / 'rg.after.json', {rg: sha(rg)})
    source_after = {str(BASE / 'finish.py'): sha(BASE / 'finish.py')}
    save(out / 'recorder.after.json', source_after)
    report = dict(status='PASS' if before == after == copies and live_exit == copy_exit == 0
        and selected_before == selected_after and source_before == source_after
        and all(r['exit'] in (0, 1) for r in rows) else 'FAIL',
        named_history=len(HISTORICAL), copied_history_equal=before == after == copies,
        live_check_exit=live_exit, copy_check_exit=copy_exit, selected_files=len(selected),
        selected_before_after_equal=selected_before == selected_after, queries=rows,
        excluded_remaining=[p for p in selected if any(t in p.lower() for t in EXCLUDE) or 'review' in Path(p).name.lower()],
        science_executions=0, raw_science_comparisons='NOT_APPLICABLE',
        scope='Terminal documentary snapshots and targeted discovery, not scientific runtime reuse.')
    save(out / 'REPORT.json', report)
    print(json.dumps(report, sort_keys=True))
    if report['status'] != 'PASS':
        raise SystemExit(1)

def seal():
    manifest = BASE / 'SHA256SUMS'
    if manifest.exists():
        raise FileExistsError('Do not overwrite an existing seal')
    files = sorted(p for p in BASE.rglob('*') if p.is_file() and p != manifest)
    with manifest.open('x', encoding='utf8') as target:
        for path in files:
            target.write(sha(path) + '  ' + str(path.relative_to(BASE)) + '\n')
    proc = subprocess.run(['/usr/bin/sha256sum', '-c', 'SHA256SUMS'], cwd=BASE,
        env=ENV, capture_output=True, check=False)
    print(json.dumps(dict(status='PASS' if proc.returncode == 0 else 'FAIL',
        payload_files=len(files), total_payload_bytes=sum(p.stat().st_size for p in files),
        manifest_sha256=sha(manifest), actual_sha256sum_check_exit=proc.returncode), sort_keys=True))
    if proc.returncode:
        sys.stdout.buffer.write(proc.stdout)
        sys.stderr.buffer.write(proc.stderr)
        raise SystemExit(proc.returncode)

if __name__ == '__main__':
    {'archive': archive, 'seal': seal}[sys.argv[1]]()
