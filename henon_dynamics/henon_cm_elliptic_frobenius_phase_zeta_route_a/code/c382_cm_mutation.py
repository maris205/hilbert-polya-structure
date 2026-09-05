#!/usr/bin/env python3
"""Hostile semantic attacks retain a repaired payload hash."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile

if sys.flags.optimize:
    raise RuntimeError('C382 mutation refuses optimized Python')
root=Path(__file__).resolve().parents[1]
original=json.loads((root/'results/c382_cm_evidence.json').read_text())
attacks=[]
def add(label, mutate):
    obj=copy.deepcopy(original)
    mutate(obj)
    obj.pop('payload_sha256',None)
    obj['payload_sha256']=hashlib.sha256(json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
    attacks.append((label,json.dumps(obj)))

for key in ('source_commit','curve','phase_convention','frobenius_convention',
            'determinant_convention','scope_literal','theorem_range'):
    add(key,lambda d,k=key:d.__setitem__(k,'hostile-replacement'))
add('trace sign',lambda d:d['prime_ledger'][1].__setitem__('trace',2))
add('Gaussian primary sign',lambda d:d['prime_ledger'][1]['primary_upper_pair'].__setitem__(0,1))
add('conjugation display',lambda d:d['prime_ledger'][1]['primary_upper_pair'].__setitem__(1,-2))
add('supersingular parity',lambda d:d['prime_ledger'][0]['fixed_counts'].__setitem__(1,4))
add('primitive count',lambda d:d['prime_ledger'][0]['primitive_counts'].__setitem__(2,999))
add('last cell corruption',lambda d:d['prime_ledger'][-1]['fixed_counts'].__setitem__(23,0))
add('missing prime',lambda d:d['prime_ledger'].pop())
add('twist label',lambda d:d['prime_ledger'][1]['quadratic_twist'].__setitem__('nonsquare',1))
add('twist trace',lambda d:d['prime_ledger'][1]['quadratic_twist'].__setitem__('trace',-2))
add('P1 count',lambda d:d['prime_ledger'][0]['parent_p1_counts'].__setitem__(0,0))
add('extension count',lambda d:d['quadratic_extension_ledger'][0].__setitem__('point_count',0))
add('mixed composite owner',lambda d:d['arithmetic_controls'].__setitem__('mixed_composite_field_characteristic',True))
add('prime power reassignment',lambda d:d['arithmetic_controls']['prime_power_labels'].append(15))
add('A1 escalation',lambda d:d['route_tuple'].__setitem__(1,'A1_PASS_ANALYTIC'))
add('A3 escalation',lambda d:d['route_tuple'].__setitem__(3,'A3_PARTIAL_ANALYTIC_STRUCTURE'))
add('absent controls claimed',lambda d:d.__setitem__('mandatory_a1_controls_completed',6))
add('Route B escalation',lambda d:d.__setitem__('route_b_invocation_allowed',True))
for flag in original['scope_flags']:
    add(flag,lambda d,k=flag:d['scope_flags'].__setitem__(k,True))
add('unknown field',lambda d:d.__setitem__('unknown',0))
add('missing field',lambda d:d.pop('native_results'))
add('bool trace',lambda d:d['prime_ledger'][0].__setitem__('trace',False))
add('float grid',lambda d:d['finite_grid'].__setitem__('prime_max',1000.0))
add('float direct count',lambda d:d['prime_ledger'][0].__setitem__('direct_prime_count',4.0))
add('float twist count',lambda d:d['prime_ledger'][0]['quadratic_twist'].__setitem__('point_count',4.0))
add('float extension degree',lambda d:d['quadratic_extension_ledger'][0].__setitem__('degree',2.0))
add('numeric native boolean',lambda d:d['native_results'].__setitem__('graded_determinant',1))
add('numeric field boolean',lambda d:d['arithmetic_controls'].__setitem__('mixed_composite_field_characteristic',0))
raw=json.dumps(original)
attacks.extend([('stale hash',raw.replace(original['payload_sha256'],'0'*64)),
                ('duplicate JSON','{"candidate_id":"hostile",'+raw[1:]),
                ('nonfinite JSON',raw.replace('1788566400','NaN',1))])
with tempfile.TemporaryDirectory(prefix='c382-hostile-') as directory:
    for index,(label,raw) in enumerate(attacks):
        path=Path(directory)/f'{index}.json'
        path.write_text(raw)
        result=subprocess.run([sys.executable,'-B',str(root/'code/c382_cm_checker.py'),str(path)],capture_output=True,text=True)
        if result.returncode==0:
            raise ValueError('survived attack: '+label)
spec=importlib.util.spec_from_file_location('c382_release_audit',root/'code/c382_release_manifest.py')
release=importlib.util.module_from_spec(spec)
spec.loader.exec_module(release)
raw=(root/'evaluations/route_a/HCS-C382/2026-09-05.yaml').read_text()
yaml_attacks=[
    ('unknown YAML field',raw+'unknown: 0\n'),
    ('numeric YAML boolean',raw.replace('claims_hilbert_polya_operator: false','claims_hilbert_polya_operator: 0')),
    ('implicit YAML timestamp',raw.replace("evaluation_date: '2026-09-05'",'evaluation_date: 2026-09-05')),
    ('duplicate YAML key',raw+'candidate_id: HCS-C382\n'),
    ('YAML anchor',raw.replace('candidate_id: HCS-C382','candidate_id: &owner HCS-C382')),
    ('YAML alias',raw.replace('candidate_id: HCS-C382','candidate_id: &owner HCS-C382').replace('title: Primary CM elliptic Frobenius phases and all-degree closed points','title: *owner')),
    ('YAML merge',raw+'<<: {unknown: 1}\n'),
    ('nonstring YAML key',raw+'1: unknown\n'),
    ('renamed scope flag',raw.replace('claims_target_zero_match: false','unknown_scope: false')),
    ('YAML A1 escalation',raw.replace('A1_WEAK','A1_PASS_ANALYTIC')),
]
with tempfile.TemporaryDirectory(prefix='c382-yaml-hostile-') as directory:
    for index,(label,value) in enumerate(yaml_attacks):
        path=Path(directory)/f'{index}.yaml'
        path.write_text(value)
        try:
            release.content_gate(path)
        except (ValueError, TypeError, release.yaml.YAMLError):
            pass
        else:
            raise ValueError('survived YAML attack: '+label)
print('C382 hostile mutation suite: PASS (%d attacks)'%(len(attacks)+len(yaml_attacks)))
