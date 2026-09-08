"""Bind B's completed manual six-page tool views to their actual files.

This recorder does not perform vision. Its comments transcribe the reviewer's
actual prior view_image observations, pages 1-3 then 4-6, on build02.
"""
import datetime
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
comments = [
    'Title, anonymous author, full abstract, map example and comparison table readable; no clipping or broken mathematics.',
    'Clock lemmas, integral mass inequalities, sharp clock display and witness start readable; page-break continuation is coherent.',
    'Witness conclusion, unique-refinement lemma and three-branch image theorem/proof readable; case brace and indices intact.',
    'Codec proof, reserved last triangle, formal generating function and endpoint coefficient display readable; no overlap.',
    'Full fibre formula and transfer, scope/finite counts/ownership limitations readable; bibliography begins with first record.',
    'Remaining six bibliography records readable, long URLs wrap within margins; substantial final whitespace is benign.'
]
def pin(p):
    return {'sha256': hashlib.sha256(p.read_bytes()).hexdigest(), 'bytes': p.stat().st_size}

pdf = HERE / 'build02/source/main.pdf'
record = {'reviewer': '/root/p210_b_reviewer', 'status': 'ALL_SIX_PAGES_ACTUALLY_VIEWED',
          'recorded_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
          'pdf_path': str(pdf), 'pdf': pin(pdf),
          'method': 'Actual view_image results inspected in two groups: pages 1,2,3 and pages 4,5,6; this script only binds those observations.',
          'pages': [{'page': i, 'image_path': str(HERE / f'build02/page-{i}.png'),
                     'image': pin(HERE / f'build02/page-{i}.png'),
                     'actually_viewed': True, 'observation': comments[i-1]}
                    for i in range(1,7)], 'new_terminal_build_claim': False}
with (HERE / 'VIEW_build02.actual.json').open('x') as out:
    json.dump(record, out, sort_keys=True, indent=2)
    out.write('\n')
print(json.dumps(record, sort_keys=True))
