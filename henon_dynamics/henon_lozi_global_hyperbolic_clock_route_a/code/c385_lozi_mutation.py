#!/usr/bin/env python3
"""Repaired-hash mathematical attacks and strict JSON/YAML refusals."""
if not __debug__:
    raise RuntimeError('c385 mutation refuses optimized Python')
import copy
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
def main():
    original=json.loads((ROOT/'results/c385_lozi_evidence.json').read_text())
    changes=[
      ('candidate',lambda x:x.update(candidate_id='HCS-C385x')),
      ('baseline',lambda x:x.update(source_commit='0'*40)),
      ('epoch bool',lambda x:x.update(fixed_epoch=True)),
      ('claim',lambda x:x['scope_flags'].update(claims_target_zero_match=True)),
      ('route B',lambda x:x['route_a'].update(route_b_invocation_allowed=True)),
      ('scope false to integer zero',lambda x:x['scope_flags'].update(claims_target_zero_match=0)),
      ('route B false to integer zero',lambda x:x['route_a'].update(route_b_invocation_allowed=0)),
      ('route upgrade',lambda x:x['route_a']['tuple'].__setitem__(1,'A1_PASS_ANALYTIC')),
      ('word omission',lambda x:x['rows'].pop()),
      ('word duplicate',lambda x:x['rows'].append(x['rows'][0])),
      ('coordinate',lambda x:x['rows'][0]['x_cycle'].__setitem__(0,[1,2])),
      ('parameter',lambda x:x['rows'][0].update(a=[4,1])),
      ('period',lambda x:x['rows'][2].update(least_period=2)),
      ('orientation',lambda x:x['rows'][1].update(unstable_sign=1)),
      ('matrix order',lambda x:x['rows'][-1]['matrix'].__setitem__(1,[0,1])),
      ('trace',lambda x:x['rows'][0].update(trace=[0,1])),
      ('weight',lambda x:x['rows'][0].update(flat_denominator=[1,1])),
      ('necklace',lambda x:x['rows'][0].update(necklace='1')),
      ('reversal',lambda x:x['rows'][-1].update(reversed_necklace='0')),
      ('primitive omission',lambda x:x['primitive_rows'].pop()),
      ('fixed count',lambda x:x['summaries'][0].update(fixed=3)),
      ('trace summary',lambda x:x['summaries'][0].update(flat_trace=[1,1])),
      ('sign margin',lambda x:x['summaries'][0].update(minimum_abs_coordinate=[0,1])),
      ('noncanonical fraction',lambda x:x['rows'][0].update(a=[18,4])),
      ('nested bool',lambda x:x['rows'][0].update(n=True)),
      ('unknown',lambda x:x.update(extra='unchecked')),
    ]
    source=(ROOT/'evaluations/route_a/HCS-C385/2026-09-05.yaml').read_text();passed=0
    with tempfile.TemporaryDirectory(prefix='c385-hostile-') as tmp:
        work=Path(tmp);ep=work/'evidence.json';yp=work/'evaluation.yaml'
        def reject(label,raw,yaml_text=source):
            nonlocal passed
            ep.write_text(raw);yp.write_text(yaml_text)
            cmd=[sys.executable,'-B',str(ROOT/'code/c385_lozi_checker.py'),str(ep),'--evaluation',str(yp)]
            p=subprocess.run(cmd,capture_output=True,text=True)
            assert p.returncode!=0,'survived '+label
            passed+=1
        for label,change in changes:
            x=copy.deepcopy(original);change(x);x.pop('payload_sha256')
            x['payload_sha256']=hashlib.sha256(canonical(x)).hexdigest();reject(label,json.dumps(x))
        raw=json.dumps(original)
        reject('duplicate JSON',raw[:-1]+',"candidate_id":"HCS-C385"}')
        reject('NaN',raw[:-1]+',"extra":NaN}')
        variants=[source+'\ncandidate_id: HCS-C385\n',source+'\nunknown: 1\n',
          source.replace('finite_based_returns: 762','finite_based_returns: true'),
          source.replace("evaluation_date: '2026-09-05'",'evaluation_date: 2026-09-05'),
          source+'\na: &v 1\nb: *v\n',source+'\n1: value\n',
          source.replace('route_b_invocation_allowed: false','route_b_invocation_allowed: true'),source+'\n<<: {x: 1}\n']
        for i,variant in enumerate(variants):
            assert variant!=source;reject('YAML '+str(i),raw,variant)
    print(f'C385 hostile PASS: {len(changes)} repaired-hash + 10 serialization = {passed}/{passed}')
if __name__=='__main__':main()
