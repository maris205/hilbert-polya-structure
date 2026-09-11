"""Exact root no-change response keys; no producer or build invocation."""
from pathlib import Path
from hashlib import sha256
import json
import os
import re

ROOT = Path('/root/autodl-tmp/symbolic_dynamics')
HERE = Path(__file__).resolve().parent
A = ROOT / 'docs/papers211_215_sequence/reviews/p211_a'
PAPER = ROOT / 'papers/211-kernel-image-projection-feedback'
RESPONSE = ROOT / 'docs/papers211_215_sequence/P211_A_RESPONSE.md'
checks = 0
def need(ok, label):
    global checks
    checks += 1
    assert ok, label
def key(path):
    p = Path(path)
    b = p.read_bytes()
    return {'sha256':sha256(b).hexdigest(), 'bytes':len(b),
            'resolved':str(p.resolve(strict=True)),
            'symlink':os.readlink(p) if p.is_symlink() else None}
def manifest(path, base, count):
    rows = {}
    for line in path.read_text().splitlines():
        m = re.fullmatch(r'([0-9a-f]{64})  (.+)', line)
        need(m is not None, 'manifest syntax')
        h, r = m.groups()
        need(r not in rows and not Path(r).is_absolute() and '..' not in Path(r).parts, 'safe unique row')
        need(key(base/r)['sha256'] == h, ('payload', r))
        rows[r] = key(base/r)
    need(len(rows) == count, 'exact manifest count')
    return rows

before = json.loads((HERE/'INPUTS.json').read_text())
need(len(before) == 498, 'complete previous root key')
for p, k in before.items():
    need(key(p) == k, ('all full key fields unchanged', p))
author = manifest(PAPER/'frozen_round0/SHA256SUMS', PAPER/'frozen_round0', 32)
stage = manifest(A/'REPORT_STAGE_SHA256SUMS', A, 41)
need(not os.path.lexists(A/'DELTA.md') and not os.path.lexists(A/'SHA256SUMS'), 'response before actual delta')
live_files = set()
for parent, dirs, files in os.walk(PAPER):
    if Path(parent) == PAPER:
        dirs.remove('frozen_round0')
    for name in dirs + files:
        need(not (Path(parent)/name).is_symlink(), 'ordinary author entries')
    for name in files:
        p = Path(parent)/name
        need(p.is_file(), 'regular author file')
        live_files.add(p.relative_to(PAPER).as_posix())
need(live_files == set(author), 'exact unchanged author membership')
author_delta = {}
for r in author:
    live = PAPER/r
    need(live.read_bytes() == (PAPER/'frozen_round0'/r).read_bytes(), 'physical raw author equality')
    need(key(live) == before[str(live)], 'exact live before/after')
    author_delta[r] = {'before':before[str(live)], 'after':key(live), 'frozen':author[r]}
for p, k in before.items():
    need(key(p) == k, ('final stable key', p))
result = {'status':'PASS_EXACT_NO_CHANGE_RESPONSE_KEYS', 'checks':checks,
          'response_path':str(RESPONSE), 'response_key':key(RESPONSE),
          'root_reception_key':key(HERE/'RECEPTION.md'), 'source_key':key(__file__),
          'prior_root_input_ledger_key':key(HERE/'INPUTS.json'),
          'complete_prior_keys_checked':498, 'author_before_after':author_delta,
          'author_payload_count':32, 'report_stage_payload_count':41,
          'report_stage_manifest_key':key(A/'REPORT_STAGE_SHA256SUMS'),
          'report_stage_payload_keys':stage, 'delta_accepted':False,
          'new_scientific_runs':0, 'new_builds':0, 'new_page_views':0}
with (HERE/'RESPONSE_KEYS.json').open('xb') as f:
    f.write((json.dumps(result,sort_keys=True,indent=2)+'\n').encode())
print(json.dumps({'status':result['status'], 'checks':checks,
                  'response_key':result['response_key'],
                  'result_key':key(HERE/'RESPONSE_KEYS.json')},sort_keys=True))
