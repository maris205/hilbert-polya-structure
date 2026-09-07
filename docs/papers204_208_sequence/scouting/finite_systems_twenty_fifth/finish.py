"""Desk-only archival/query evidence and non-self outer manifest."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import time

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[3]
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
INPUTS = [
    'SYMBOLIC_DYNAMICS_STATE.md',
    'docs/papers204_208_sequence/PIPELINE_STATE.md',
    'docs/papers204_208_sequence/PROBLEM_ANCHOR.md',
    'docs/papers197_201_sequence/PROBLEM_ANCHOR.md',
    'docs/research_state/WORKFLOW.md',
    'docs/research_state/HISTORY_AND_CAVEATS.md',
    '.agents/skills/symbolic-dynamics-research/SKILL.md',
    'papers/202-ternary-ordered-reset/main.tex',
    'papers/205-conflict-triggered-cyclic-increments/sections/01_setup.tex',
    'docs/papers204_208_sequence/scouting/graph_relation_second/SCOUT_REPORT.md',
    'docs/papers204_208_sequence/scouting/word_local/CPC_INTAKE.md',
    'docs/papers204_208_sequence/scouting/graph_relation/SCOUT_REPORT.md',
    'docs/papers197_201_sequence/scouting/second_replacement_20260905/CONTRACTS_AND_PROOF.md',
    'papers/171-boolean-gram-dynamics/main.tex',
    'docs/papers204_208_sequence/scouting/finite_systems_twenty_fourth/finish.py',
]
QUERIES = [
    ('neighborhood', r'open.neighbou?rhood.graph|iterated.neighbou?rhood|common.neighbou?r|metamour|Boolean.Gram'),
    ('threshold', r'threshold.*(chain|graph|lift)|nested.*(graph|threshold)|min.max|bottleneck|ultrametric|weighted.tree|tree.metric'),
    ('local_controls', r'cyclic.predator|cyclic.cellular|Greenberg|Hastings|CPC|conflict.triggered'),
]

def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def save(path, obj):
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + '\n')

def run(argv, out, tag, cwd):
    save(out / (tag + '.ATTEMPT.json'), dict(argv=argv, cwd=str(cwd), environment=ENV,
        started_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())))
    with (out / (tag + '.stdout')).open('xb') as stdout, (out / (tag + '.stderr')).open('xb') as stderr:
        proc = subprocess.run(argv, cwd=cwd, env=ENV, stdout=stdout, stderr=stderr, check=False)
    save(out / (tag + '.RESULT.json'), dict(exit=proc.returncode,
        stdout_sha256=sha(out / (tag + '.stdout')), stderr_sha256=sha(out / (tag + '.stderr'))))
    return proc.returncode

def archive():
    out = BASE / 'evidence_capture'
    out.mkdir(exist_ok=False)
    copies = out / 'historical_inputs'
    copies.mkdir()
    rg = str(Path(shutil.which('rg')).resolve())
    sumtool = str(Path(shutil.which('sha256sum')).resolve())
    recorder = str(Path(__file__).resolve())
    tools_before = {p: sha(p) for p in (recorder, rg, sumtool)}
    save(out / 'tools.before.json', tools_before)
    before = {p: sha(ROOT / p) for p in INPUTS}
    save(out / 'historical.before.json', before)
    mappings = []
    for number, relative in enumerate(INPUTS, 1):
        copied = copies / (f'{number:02d}_' + Path(relative).name)
        shutil.copyfile(ROOT / relative, copied)
        mappings.append(dict(original=relative, copied=copied.relative_to(BASE).as_posix(), sha256=sha(copied)))
    save(out / 'HISTORICAL_COPIES.json', mappings)
    (BASE / 'HISTORICAL_INPUTS.sha256').write_text(''.join(f'{before[p]}  {p}\n' for p in INPUTS))
    (BASE / 'HISTORICAL_COPIES.sha256').write_text(''.join(f"{r['sha256']}  {r['copied']}\n" for r in mappings))
    selected = json.loads((BASE / 'history_01/selected.json').read_text())
    original_receipt = json.loads((BASE / 'history_01/REPORT.json').read_text())
    exclusions = original_receipt['exclusions']
    excluded_remaining = [p for p in selected if any(t in p.lower() for t in exclusions) or 'review' in Path(p).name.lower()]
    assert not excluded_remaining
    selected_before = {p: sha(p) for p in selected}
    save(out / 'selected.json', selected)
    save(out / 'search.before.json', selected_before)
    rows = []
    for tag, query in QUERIES:
        code = run([rg, '-n', '-i', '-e', query, *selected], out, tag, ROOT)
        rows.append(dict(tag=tag, query=query, exit=code,
            output_lines=len((out / (tag + '.stdout')).read_text().splitlines())))
    livecheck = run([sumtool, '-c', str(BASE / 'HISTORICAL_INPUTS.sha256')], out, 'live_check', ROOT)
    copycheck = run([sumtool, '-c', str(BASE / 'HISTORICAL_COPIES.sha256')], out, 'copies_check', BASE)
    after = {p: sha(ROOT / p) for p in INPUTS}
    save(out / 'historical.after.json', after)
    selected_after = {p: sha(p) for p in selected}
    save(out / 'search.after.json', selected_after)
    tools_after = {p: sha(p) for p in (recorder, rg, sumtool)}
    save(out / 'tools.after.json', tools_after)
    old_search = json.loads((BASE / 'history_01/inputs.before.json').read_text())
    old_intersection = {p: old_search[str(ROOT / p)] == before[p] for p in INPUTS if str(ROOT / p) in old_search}
    report = dict(status='PASS' if before == after and selected_before == selected_after and tools_before == tools_after
        and all(r['exit'] in (0, 1) for r in rows) and livecheck == copycheck == 0
        and all(r['sha256'] == before[r['original']] for r in mappings) and all(old_intersection.values()) else 'FAIL',
        capture_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), historical_files=len(INPUTS),
        selected_files=len(selected), roots=original_receipt['roots'], exclusions=exclusions,
        excluded_remaining=excluded_remaining, historical_before_after_equal=before == after,
        selected_before_after_equal=selected_before == selected_after, tools_before_after_equal=tools_before == tools_after,
        original_search_overlap_equal=old_intersection, live_check_exit=livecheck, copies_check_exit=copycheck,
        queries=rows, scope='Read-only desk receipts; one literal description, zero implemented science kernels, boxes, states, producer executions, pairs or scientific comparisons.')
    save(out / 'REPORT.json', report)
    print(json.dumps(report, sort_keys=True))
    assert report['status'] == 'PASS'

def seal():
    manifest = BASE / 'SHA256SUMS'
    assert not manifest.exists(), 'Do not replace a sealed manifest'
    files = sorted(p for p in BASE.rglob('*') if p.is_file() and p != manifest)
    assert all(not p.is_symlink() for p in files)
    manifest.write_text(''.join(f'{sha(p)}  {p.relative_to(BASE).as_posix()}\n' for p in files))
    print(json.dumps(dict(payload_files=len(files), payload_bytes=sum(p.stat().st_size for p in files),
        manifest_sha256=sha(manifest), only_excluded_file='SHA256SUMS'), sort_keys=True))

if __name__ == '__main__':
    if sys.argv[1:] == ['archive']:
        archive()
    elif sys.argv[1:] == ['seal']:
        seal()
    else:
        raise SystemExit('Use exactly archive or seal')
