#!/usr/bin/env python3
"""Repair the evidence hash before every semantic adversarial attack."""
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
import sys
import tempfile
from c387_nilflow_checker import check

ROOT=Path(__file__).resolve().parents[1]

def main():
    if sys.flags.optimize:raise RuntimeError('C387 mutation refuses optimized Python')
    original=json.loads((ROOT/'results/c387_nilflow_evidence.json').read_text())
    attacks=[]
    for index in [0,731,-1]:
        attacks.append((f'least_period_{index}',lambda x,i=index:x['orbit_rows'][i].__setitem__('least_period',0)))
        attacks.append((f'displacement_{index}',lambda x,i=index:x['orbit_rows'][i]['central_lattice_displacements'][3].__setitem__(0,999)))
    attacks += [
      ('missing_orbit',lambda x:x['orbit_rows'].pop()),
      ('order',lambda x:x['orbit_rows'].reverse()),
      ('negative_returns',lambda x:x['orbit_rows'][0]['negative_return_multipliers'].pop()),
      ('half_integer',lambda x:x['orbit_rows'][0].__setitem__('nonhorizontal_half_integer_returns',True)),
      ('fixed_tori',lambda x:x['fixed_torus_rows'][-1].__setitem__('fixed_tori',1)),
      ('primitive_tori',lambda x:x['fixed_torus_rows'][0].__setitem__('primitive_tori',0)),
      ('return_matrix',lambda x:x['fixed_torus_rows'][2]['return_matrix'][2].__setitem__(1,0)),
      ('isolated',lambda x:x['fixed_torus_rows'][0].__setitem__('isolated',True)),
      ('reversal',lambda x:x['flow_identity_rows'][0]['reversed_flow_result'][2].__setitem__(0,999)),
      ('section',lambda x:x['flow_identity_rows'][-1]['section_iterate'][2].__setitem__(0,999)),
      ('negative_m',lambda x:x['signed_block_rows'][0].__setitem__('m',6)),
      ('chirp_sign',lambda x:x['signed_block_rows'][0]['chirp_over_pi'][2].__setitem__(0,999)),
      ('domain',lambda x:x['signed_block_rows'][0].__setitem__('domain','H1_intersection_uL2')),
      ('irrational_return',lambda x:x['irrational_controls'][0].__setitem__('return_exists',True)),
      ('time_one',lambda x:x['global_theorem'].__setitem__('time_one_map_ergodic',True)),
      ('heat_compact',lambda x:x['global_theorem'].__setitem__('heat_compact',True)),
      ('target_route',lambda x:x['route_tuple'].__setitem__(2,'A2_PASS_ANALYTIC')),
      ('clock',lambda x:x['source'].__setitem__('clock','time changed roof')),
      ('baseline',lambda x:x.__setitem__('source_commit','0'*40)),
      ('bool_to_zero',lambda x:x.__setitem__('route_b_invocation_allowed',0)),
      ('unknown_field',lambda x:x.__setitem__('unexpected',True))]
    for flag in original['payload']['scope_flags']:
        attacks.append(('flag_'+flag,lambda x,k=flag:x['scope_flags'].__setitem__(k,True)))
    names=[]
    with tempfile.TemporaryDirectory(prefix='c387-hostile-') as directory:
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
        from c387_release_manifest import content_gate
        yml=ROOT/'evaluations/route_a/HCS-C387/2026-09-05.yaml';raw=yml.read_text()
        yamls=[('unknown_field',raw+'extra_field: true\n'),
          ('bool_zero',raw.replace('invokes_route_b: false','invokes_route_b: 0')),
          ('date_timestamp',raw.replace("evaluation_date: '2026-09-05'",'evaluation_date: 2026-09-05')),
          ('duplicate',raw+'candidate_id: HCS-C387\n'),
          ('anchor',raw.replace('invokes_route_b: false','invokes_route_b: &lock false')),
          ('alias',raw+'extra_field: *missing\n'),
          ('merge',raw+'<<: {extra: true}\n'),('nonstring',raw+'1: false\n'),
          ('route_promotion',raw.replace('A4_FORMAL_HINT','A4_PASS_ANALYTIC')),
          ('route_b',raw.replace('route_b_invocation_allowed: false','route_b_invocation_allowed: true'))]
        for name,content in yamls:
            path=Path(directory)/'bad.yaml';path.write_text(content)
            try:content_gate(path)
            except Exception:names.append('yaml_'+name)
            else:raise ValueError('accepted YAML hostile '+name)
    print('C387_MUTATION_PASS rejected='+str(len(names))+'/'+str(len(names))+' repaired_hash_json='+str(len(attacks))+' strict_yaml=10 names='+','.join(names))

if __name__=='__main__':main()
