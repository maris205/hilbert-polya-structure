#!/usr/bin/env python3
"""Semantic adversaries repair the evidence payload hash before checking."""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import sys
import tempfile
from c384_wild_checker import check

ROOT=Path(__file__).resolve().parents[1]

def main():
    if sys.flags.optimize:raise RuntimeError('C384 mutation refuses optimized Python')
    original=json.loads((ROOT/'results/c384_wild_evidence.json').read_text())
    attacks=[]
    for key in ['geometric','multiplicity','scheme_length','valuation_power','primitive_cycles']:
        for index in [0,95,-1]:
            attacks.append((f'period_{index}_{key}',lambda x,i=index,k=key:x['period_rows'][i].__setitem__(k,x['period_rows'][i][k]+1)))
    for key in ['count','exact_period_degree_points','exact_degree_cycles']:
        for index in [0,25,-1]:
            attacks.append((f'extension_{index}_{key}',lambda x,i=index,k=key:x['extension_rows'][i].__setitem__(k,x['extension_rows'][i][k]+1)))
    attacks += [
      ('gcd_factor',lambda x:x['extension_rows'][25]['gcd'].__setitem__(0,0)),
      ('drop_period',lambda x:x['period_rows'].pop()),('drop_extension',lambda x:x['extension_rows'].pop()),
      ('swap_periods',lambda x:x['period_rows'].reverse()),
      ('neighbor',lambda x:x['neighbor_controls'][-1].__setitem__('geometric',0)),
      ('neighbor_bool',lambda x:x['neighbor_controls'][0].__setitem__('a',False)),
      ('direct_recount',lambda x:x['direct_field_recounts'][-1]['counts'].__setitem__(11,0)),
      ('direct_r_bool',lambda x:x['direct_field_recounts'][0].__setitem__('r',True)),
      ('direct_r_float',lambda x:x['direct_field_recounts'][0].__setitem__('r',1.0)),
      ('direct_p_float',lambda x:x['direct_field_recounts'][0].__setitem__('p',2.0)),
      ('modulus',lambda x:x['direct_field_recounts'][-1]['modulus'].__setitem__(3,0)),
      ('residue_sign',lambda x:x['residue_intervals'][0]['residue_lower'].__setitem__(0,-1)),
      ('tail_bound',lambda x:x['interior_tail_bounds'][-1]['bound'].__setitem__(0,0)),
      ('composite_admissible',lambda x:x['composite_characteristic_controls'][0].__setitem__('admissible',True)),
      ('route',lambda x:x['route_tuple'].__setitem__(1,'A1_PASS_ANALYTIC')),
      ('target_flag',lambda x:x['scope_flags'].__setitem__('claims_target_euler_factors',True)),
      ('flag_bool_zero',lambda x:x['scope_flags'].__setitem__('invokes_route_b',0)),
      ('route_b',lambda x:x.__setitem__('route_b_invocation_allowed',True)),
      ('unknown_field',lambda x:x.__setitem__('unregistered',1)),
      ('source_clock',lambda x:x['source'].__setitem__('clock','rational primes')),
      ('baseline',lambda x:x.__setitem__('source_commit','0'*40)),
      ('schema',lambda x:x.__setitem__('schema','hcs-c384-wild-v2'))]
    names=[]
    with tempfile.TemporaryDirectory(prefix='c384-hostile-') as directory:
        path=Path(directory)/'bad.json'
        for name,attack in attacks:
            bad=deepcopy(original);attack(bad['payload'])
            bad['payload_sha256']=sha256(json.dumps(bad['payload'],sort_keys=True,separators=(',',':')).encode()).hexdigest()
            path.write_text(json.dumps(bad))
            try:check(path)
            except (ValueError,TypeError,KeyError,IndexError):names.append(name)
            else:raise ValueError('accepted hostile '+name)
        for name,raw in [('duplicate_json','{"payload":{},"payload":{},"payload_sha256":"x"}'),
                         ('nonfinite_json','{"payload":NaN,"payload_sha256":"x"}')]:
            path.write_text(raw)
            try:check(path)
            except (ValueError,TypeError,KeyError,IndexError):names.append(name)
            else:raise ValueError('accepted hostile '+name)
        from c384_release_manifest import content_gate
        yml=ROOT/'evaluations/route_a/HCS-C384/2026-09-05.yaml';raw=yml.read_text()
        yamls=[('unknown_field',raw+'extra_field: true\n'),
          ('bool_zero',raw.replace('invokes_route_b: false','invokes_route_b: 0')),
          ('implicit_date',raw.replace("'2026-09-05'",'2026-09-05')),
          ('duplicate_key',raw+'candidate_id: HCS-C384\n'),
          ('anchor',raw.replace('route_b_invocation_allowed: false','route_b_invocation_allowed: &a false')),
          ('alias',raw+'extra: *a\n'),('merge',raw+'extra: {<<: {x: 1}}\n'),
          ('nonstring_key',raw+'1: text\n'),
          ('rename_flag',raw.replace('claims_target_euler_factors:','claims_euler_factors:')),
          ('promote_a1',raw.replace('A1_WEAK','A1_PASS_ANALYTIC'))]
        for name,bad in yamls:
            file=Path(directory)/'bad.yaml';file.write_text(bad)
            try:content_gate(file)
            except Exception:names.append('yaml_'+name)
            else:raise ValueError('accepted YAML '+name)
    print('C384_MUTATION_PASS rejected='+str(len(names))+'/'+str(len(attacks)+12)+' json='+str(len(attacks)+2)+' yaml=10')

if __name__=='__main__':main()
