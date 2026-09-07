"""Preserve live-index changes and check explicit historical aliases, no science."""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import time

BASE = Path(__file__).resolve().parent
ROOT = BASE.parents[3]
OUT = BASE / 'postcheck'
ENV = {'PATH': '/usr/bin:/bin', 'LANG': 'C.UTF-8', 'LC_ALL': 'C.UTF-8', 'TZ': 'UTC'}
CONTROLS = {'SYMBOLIC_DYNAMICS_STATE.md', 'docs/papers204_208_sequence/PIPELINE_STATE.md'}

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def save(path, obj):
    path.write_text(json.dumps(obj, indent=2, sort_keys=True) + '\n')

def run(argv, cwd, tag):
    save(OUT / (tag + '.ATTEMPT.json'), dict(argv=argv, cwd=str(cwd), environment=ENV,
        start_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())))
    with (OUT / (tag + '.stdout')).open('xb') as out, (OUT / (tag + '.stderr')).open('xb') as err:
        proc = subprocess.run(argv, cwd=cwd, env=ENV, stdout=out, stderr=err, check=False)
    save(OUT / (tag + '.RESULT.json'), dict(exit=proc.returncode,
        stdout_sha256=sha(OUT / (tag + '.stdout')), stderr_sha256=sha(OUT / (tag + '.stderr'))))
    return proc.returncode

OUT.mkdir(exist_ok=False)
before_program = sha(Path(__file__).resolve())
inputs = {}
for filename in ('HISTORICAL_INPUTS.sha256', 'SUPPLEMENTARY_INPUTS.sha256'):
    for line in (BASE / filename).read_text().splitlines():
        expected, name = line.split('  ', 1)
        inputs[name] = expected
before_live = {name: sha(ROOT / name) for name in inputs}
save(OUT / 'live.before.json', before_live)
aliases = []
for name in sorted(CONTROLS):
    old = BASE / 'historical_inputs' / name
    current_copy = OUT / 'current_controls' / name
    current_copy.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(ROOT / name, current_copy)
    aliases.append(dict(original_path=str(ROOT / name), old_sha256=inputs[name],
        historical_path=str(old), historical_sha256=sha(old),
        new_copy=str(current_copy), new_sha256=sha(current_copy)))
save(OUT / 'CONTROL_ALIASES.json', aliases)
exits = {}
exits['live_original'] = run(['/usr/bin/sha256sum', '-c', str(BASE / 'HISTORICAL_INPUTS.sha256')], ROOT, 'live_original')
exits['physical_originals'] = run(['/usr/bin/sha256sum', '-c', str(BASE / 'HISTORICAL_INPUTS.sha256')], BASE / 'historical_inputs', 'physical_originals')
exits['supplement'] = run(['/usr/bin/sha256sum', '-c', str(BASE / 'SUPPLEMENTARY_INPUTS.sha256')], ROOT, 'supplement')
for number, row in enumerate(aliases):
    exits['control_diff_' + str(number)] = run(['/usr/bin/diff', '--unified', row['historical_path'], row['new_copy']], ROOT, 'control_diff_' + str(number))
resolved = {}
with (OUT / 'RESOLVED_INPUTS.sha256').open('x', encoding='utf8') as target:
    for name, expected in inputs.items():
        path = BASE / 'historical_inputs' / name if name in CONTROLS else ROOT / name
        resolved[str(path)] = expected
        target.write(expected + '  ' + str(path) + '\n')
exits['resolved'] = run(['/usr/bin/sha256sum', '-c', str(OUT / 'RESOLVED_INPUTS.sha256')], ROOT, 'resolved')
after_live = {name: sha(ROOT / name) for name in inputs}
save(OUT / 'live.after.json', after_live)
changed = sorted(name for name in inputs if before_live[name] != inputs[name])
resolved_actual = {path: sha(Path(path)) for path in resolved}
save(OUT / 'resolved.actual.json', resolved_actual)
report = dict(status='PASS_EXPLICIT_HISTORICAL_RESOLUTION' if set(changed) == CONTROLS
    and before_live == after_live and all(r['historical_sha256'] == r['old_sha256'] for r in aliases)
    and exits['live_original'] != 0 and all(exits[k] == 0 for k in ('physical_originals', 'supplement', 'resolved'))
    and all(exits['control_diff_' + str(i)] == 1 for i in range(len(aliases)))
    and resolved == resolved_actual and before_program == sha(Path(__file__).resolve()) else 'FAIL',
    historical_inputs=len(inputs), live_control_changes=changed, recorded_exits=exits,
    live_stable_during_postcheck=before_live == after_live,
    recorder_sha256=before_program, science_executions=0,
    boundary='Original live check really fails; only explicitly named old control hashes resolve to physical historical copies.')
save(OUT / 'REPORT.json', report)
print(json.dumps(report, sort_keys=True))
if report['status'] == 'FAIL':
    raise SystemExit(1)
