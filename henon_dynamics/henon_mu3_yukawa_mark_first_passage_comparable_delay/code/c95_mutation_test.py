#!/usr/bin/env python3
"""Hostile semantic mutation audit for C95."""
from __future__ import annotations
import copy,importlib.util,json,tempfile
from pathlib import Path
PROJECT=Path(__file__).resolve().parents[1]; EVIDENCE=PROJECT/'results/c95_comparable_delay_evidence.json'; CHECKER=PROJECT/'code/c95_comparable_delay_checker.py'
def canonical(v): return (json.dumps(v,sort_keys=True,separators=(',',':'))+'\n').encode()
def mutate(v,path,replacement):
 r=copy.deepcopy(v); c=r
 for key in path[:-1]: c=c[key]
 c[path[-1]]=replacement; return r
def main():
 o=json.loads(EVIDENCE.read_text()); row=o['delay_atlas']['pair_rows'][1]; cond=next(i for i,c in enumerate(row['conditional_delay_rows_given_lower_time']) if c['conditioning_permutation_count'])
 ms={
  'schema':mutate(o,['schema_id'],'bad'),'status':mutate(o,['status'],'RELEASED'),'scope':mutate(o,['scope_literal'],'BAD'),'c88':mutate(o,['authority','c88'],'0'*64),'c90':mutate(o,['authority','c90'],'0'*64),
  'pair_count':mutate(o,['delay_atlas','ordered_pair_count'],101),'pair_index':mutate(o,['delay_atlas','pair_rows',1,'upper_target_index'],0),'relation':mutate(o,['delay_atlas','pair_rows',1,'comparable_relation_certified'],False),
  'pmf':mutate(o,['delay_atlas','pair_rows',1,'joint_pmf_permutation_counts','0','0'],1),'order':mutate(o,['delay_atlas','pair_rows',1,'target_time_order','violation_permutation_count'],1),
  'delay':mutate(o,['delay_atlas','pair_rows',1,'delay_permutation_count_by_delta','1'],0),'mean':mutate(o,['delay_atlas','pair_rows',1,'delay_mean','numerator'],999),
  'conditional_count':mutate(o,['delay_atlas','pair_rows',1,'conditional_delay_rows_given_lower_time',cond,'conditioning_permutation_count'],1),'conditional_mean':mutate(o,['delay_atlas','pair_rows',1,'conditional_delay_rows_given_lower_time',cond,'conditional_mean_delay','numerator'],999),
  'marginal':mutate(o,['delay_atlas','pair_rows',1,'marginal_identity','left_pmf_matches_c88'],False),'check':mutate(o,['checks','all_102_target_time_orders_certified'],False),'claim':mutate(o,['claims','euler_factors_claimed'],True),
 }
 spec=importlib.util.spec_from_file_location('c95_checker',CHECKER); assert spec and spec.loader; mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); expected,_=mod.build_expected(); rejected=0
 with tempfile.TemporaryDirectory(prefix='c95-mutations-') as td:
  for name,v in ms.items():
   p=Path(td)/(name+'.json'); p.write_bytes(canonical(v))
   try: mod.validate_evidence_path(p,expected)
   except (AssertionError,KeyError,TypeError,ValueError): rejected+=1
   else: raise AssertionError('mutation accepted: '+name)
 assert rejected==len(ms); print(json.dumps({'status':'C95_MUTATION_TEST_PASS','rejected':rejected},sort_keys=True))
if __name__=='__main__': main()
