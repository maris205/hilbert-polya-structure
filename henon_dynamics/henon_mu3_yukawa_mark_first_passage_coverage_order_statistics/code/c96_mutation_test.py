#!/usr/bin/env python3
"""Hostile semantic mutation audit for C96."""
from __future__ import annotations
import copy,importlib.util,json,tempfile
from pathlib import Path
PROJECT=Path(__file__).resolve().parents[1]; EVIDENCE=PROJECT/'results/c96_coverage_order_statistics_evidence.json'; CHECKER=PROJECT/'code/c96_coverage_order_statistics_checker.py'
def canonical(v): return (json.dumps(v,sort_keys=True,separators=(',',':'))+'\n').encode()
def mutate(v,path,replacement):
 r=copy.deepcopy(v); c=r
 for key in path[:-1]: c=c[key]
 c[path[-1]]=replacement; return r
def main():
 o=json.loads(EVIDENCE.read_text()); row=o['coverage_atlas']['rank_rows'][1]
 ms={'schema':mutate(o,['schema_id'],'bad'),'status':mutate(o,['status'],'RELEASED'),'scope':mutate(o,['scope_literal'],'BAD'),'c88':mutate(o,['authority','c88'],'0'*64),'rank_count':mutate(o,['source_model','coverage_rank_range'],[1,19]),'rank_index':mutate(o,['coverage_atlas','rank_rows',1,'coverage_rank'],99),'support_count':mutate(o,['source_model','support_count'],1),'cdf':mutate(o,['coverage_atlas','rank_rows',1,'cdf_by_prefix_size','2','numerator'],999),'pmf':mutate(o,['coverage_atlas','rank_rows',1,'permutation_count_by_first_reach_time','2'],0),'factorial_certificate':mutate(o,['coverage_atlas','rank_rows',1,'first_reach_support_edge_factorial_certificate','2','support_or_edge_count'],0),'mean':mutate(o,['coverage_atlas','rank_rows',1,'mean','numerator'],999),'variance':mutate(o,['coverage_atlas','rank_rows',1,'variance','numerator'],999),'hist':mutate(o,['coverage_atlas','exact_support_count_by_prefix_size_and_coverage','0','1'],0),'check':mutate(o,['checks','all_20_means_match_survival_sums'],False),'claim':mutate(o,['claims','full_table_of_marks_claimed'],True)}
 spec=importlib.util.spec_from_file_location('c96_checker',CHECKER); assert spec and spec.loader; mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); expected,_=mod.build_expected(); rejected=0
 with tempfile.TemporaryDirectory(prefix='c96-mutations-') as td:
  for name,v in ms.items():
   p=Path(td)/(name+'.json'); p.write_bytes(canonical(v))
   try: mod.validate_evidence_path(p,expected)
   except (AssertionError,KeyError,TypeError,ValueError): rejected+=1
   else: raise AssertionError('mutation accepted: '+name)
 assert rejected==len(ms); print(json.dumps({'status':'C96_MUTATION_TEST_PASS','rejected':rejected},sort_keys=True))
if __name__=='__main__': main()
