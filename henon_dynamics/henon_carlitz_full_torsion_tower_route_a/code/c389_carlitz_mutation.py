#!/usr/bin/env python3
"""Actual repaired-hash semantic attacks plus strict JSON/YAML attacks."""
from copy import deepcopy
import hashlib
import json
from pathlib import Path
import tempfile
from c389_carlitz_checker import check

ROOT=Path(__file__).resolve().parents[1]
def main():
    if not __debug__: raise SystemExit('optimized mode forbidden')
    original=json.loads((ROOT/'results/c389_carlitz_evidence.json').read_text()); attacks=[]
    def edit(path,value):
        def attack(payload):
            for key in path[:-1]: payload=payload[key]
            payload[path[-1]]=value
        return attack
    cases=[('baseline',['baseline'],'0'*40),('scope',['scope'],'TARGET_PROMOTED'),
      ('route',['tuple',2],'A2_PASS_ANALYTIC'),('q_bool',['ring_cases',0,'q'],True),
      ('a_bool',['ring_cases',0,'a',0],True),('size_bool',['ring_cases',0,'size'],True),
      ('linear_bool',['ring_cases',0,'carlitz',0,0],True),('b_bool',['ring_cases',0,'maps',0,'b',0],False),
      ('h_bool',['ring_cases',0,'maps',0,'joint',0,0],False),('period_bool',['ring_cases',0,'maps',0,'joint',0,1],True),
      ('population_bool',['ring_cases',0,'maps',0,'joint',0,2],True),('fixed_bool',['ring_cases',0,'maps',0,'fixed',0],True),
      ('stratum_bool',['ring_cases',0,'strata',0,1],True),('clock',['ring_cases',30,'maps',0,'joint',0,1],7),
      ('fixed',['ring_cases',50,'maps',0,'fixed',0],99),('cycle',['ring_cases',40,'maps',0,'cycles',0,1],99),
      ('q4',['field_encoding','4'],'F4 integer modulo four'),('P_bool',['tower_cases',0,'P',0],False),
      ('k_bool',['tower_cases',0,'k'],True),('Q_bool',['tower_cases',0,'Q'],True),
      ('degree_bool',['tower_cases',0,'degree'],True),('valuation_bool',['tower_cases',0,'valuation',0],True),
      ('constant',['tower_cases',0,'psi',0,1],[1]),('psi_exponent_bool',['tower_cases',0,'psi',0,0],False),
      ('lower_bool',['tower_cases',0,'lower_groups',0,0],False),('hist_bool',['tower_cases',0,'ramification_histogram',0,1],False),
      ('different_bool',['tower_cases',0,'different'],False),('kernel_bool',['tower_cases',0,'restriction_kernel'],True),
      ('different',['tower_cases',50,'different'],999),('valuation',['tower_cases',50,'valuation',1],999),
      ('lower_size',['tower_cases',50,'lower_groups',0,2],999)]
    for name,path,value in cases: attacks.append((name,edit(path,value)))
    for flag in original['payload']['scope_flags']:
        attacks.append(('scope_'+flag,edit(['scope_flags',flag],True)))
    for key,value in original['payload']['controls'].items():
        attacks.append(('control_type_'+key,edit(['controls',key],0 if type(value) is bool else False)))
    attacks.extend([('unknown',lambda p:p.__setitem__('unknown',0)),
      ('nested_unknown',lambda p:p['tower_cases'][0].__setitem__('unknown',0)),
      ('missing_ring',lambda p:p['ring_cases'].pop()),('reordered_towers',lambda p:p['tower_cases'].reverse())])
    names=[]
    with tempfile.TemporaryDirectory(prefix='c389-hostile-') as d:
        path=Path(d)/'bad.json'
        for name,attack in attacks:
            bad=deepcopy(original); attack(bad['payload'])
            if json.dumps(bad,sort_keys=True)==json.dumps(original,sort_keys=True): raise ValueError('ineffective attack '+name)
            bad['payload_sha256']=hashlib.sha256(json.dumps(bad['payload'],sort_keys=True,separators=(',',':')).encode()).hexdigest()
            path.write_text(json.dumps(bad))
            try: check(path)
            except (ValueError,KeyError,TypeError,IndexError): names.append(name)
            else: raise ValueError('accepted attack '+name)
        for name,raw in [('duplicate','{"payload":{},"payload":{}}'),('nonfinite','{"x":NaN}')]:
            path.write_text(raw)
            try: check(path)
            except (ValueError,KeyError,TypeError,IndexError): names.append('json_'+name)
            else: raise ValueError('accepted JSON '+name)
        from c389_release_manifest import content_gate
        raw=(ROOT/'evaluations/route_a/HCS-C389/2026-09-05.yaml').read_text()
        content_gate()
        yamls=[('unknown',raw+'extra_field: true\n'),
          ('false_zero',raw.replace('invokes_route_b: false','invokes_route_b: 0')),
          ('date',raw.replace("evaluation_date: '2026-09-05'",'evaluation_date: 2026-09-05')),
          ('duplicate',raw+'candidate_id: HCS-C389\n'),
          ('anchor',raw.replace('invokes_route_b: false','invokes_route_b: &lock false')),
          ('alias',raw+'extra_field: *missing\n'),('merge',raw+'<<: {extra: true}\n'),
          ('nonstring',raw+'1: false\n'),('promotion',raw.replace('A1_WEAK','A1_STRONG')),
          ('route_b',raw.replace('route_b_invocation_allowed: false','route_b_invocation_allowed: true'))]
        for name,bad in yamls:
            path=Path(d)/'bad.yaml'; path.write_text(bad)
            try: content_gate(path)
            except Exception: names.append('yaml_'+name)
            else: raise ValueError('accepted YAML '+name)
    print('C389_MUTATION_PASS rejected='+str(len(names))+'/'+str(len(names))+
          ' repaired_hash_json='+str(len(attacks))+' parser_json=2 strict_yaml=10 names='+','.join(names))
if __name__=='__main__': main()
