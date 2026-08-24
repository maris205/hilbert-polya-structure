#!/usr/bin/env python3
from __future__ import annotations
import copy,json,tempfile
from pathlib import Path
from c118_damped_dimer_checker import validate
ROOT=Path(__file__).resolve().parents[1]; D=json.loads((ROOT/'results/c118_damped_dimer_evidence.json').read_text())
def m(fn): x=copy.deepcopy(D);fn(x);return x
cases=[
 m(lambda x:x.__setitem__('scope_literal','BROKEN')),
 m(lambda x:x['source_model']['parameters'].__setitem__('gamma','1')),
 m(lambda x:x['structural_checks'].__setitem__('expected_jacobian_determinant','1')),
 m(lambda x:x['certified_orbit_ledger']['fixed_rows'][1]['states'][0].__setitem__(0,'4')),
 m(lambda x:x['certified_orbit_ledger']['period_two_rows'][0].__setitem__('cycle_closes',False)),
 m(lambda x:x['certified_orbit_ledger']['period_two_rows'][0]['monodromy'][0].__setitem__(0,'0')),
 m(lambda x:x['mode_factorization']['hessian_at_q2'].__setitem__(1,'5/2')),
 m(lambda x:x['mode_factorization']['two_step_mode_traces'].__setitem__(0,'-13')),
 m(lambda x:x['mode_factorization']['reconstructed_full_det_I_minus_z'].__setitem__(2,'0')),
 m(lambda x:x['uncoupled_control'].__setitem__('coupled_minus_uncoupled_trace','0')),
 m(lambda x:x['route_a_verdict'].__setitem__('A2','A2_CERTIFIED_GLOBAL')),
 m(lambda x:x['claims'].__setitem__('route_b_authorized',True)),
]
rejected=0
for d in cases:
 with tempfile.NamedTemporaryFile('w',suffix='.json',delete=False) as f: json.dump(d,f,sort_keys=True,separators=(',',':'));f.write('\n');p=Path(f.name)
 try: validate(p)
 except (AssertionError,KeyError,ValueError): rejected+=1
 p.unlink()
assert rejected==len(cases);print(f'C118_MUTATION_PASS {rejected}/{len(cases)}')
