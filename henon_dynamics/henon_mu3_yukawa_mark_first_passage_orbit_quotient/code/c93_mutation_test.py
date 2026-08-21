#!/usr/bin/env python3
from __future__ import annotations
import copy,importlib.util,json,tempfile
from pathlib import Path
PROJECT=Path(__file__).resolve().parents[1]; EVIDENCE=PROJECT/'results/c93_first_passage_orbit_quotient_evidence.json'; CHECKER=PROJECT/'code/c93_first_passage_orbit_quotient_checker.py'
def canon(x): return (json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def mut(x,path,replacement):
 y=copy.deepcopy(x); c=y
 for k in path[:-1]: c=c[k]
 c[path[-1]]=replacement; return y
def main():
 original=json.loads(EVIDENCE.read_text()); spec=importlib.util.spec_from_file_location('c93',CHECKER); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); mutations={'schema':mut(original,['schema_id'],'bad'),'scope':mut(original,['scope_literal'],'BAD'),'c75':mut(original,['authority','c75'],'0'*64),'effective_order':mut(original,['source_model','effective_group_order'],11520),'ambient_order':mut(original,['source_model','ambient_lifted_group_order'],1920),'orbit_count':mut(original,['target_orbit_atlas','orbit_count'],15),'orbit_size':mut(original,['target_orbit_atlas','orbit_size_spectrum','1'],11),'representative':mut(original,['target_orbit_atlas','rows',0,'representative_target'],19),'transport':mut(original,['target_orbit_atlas','rows',0,'sensitivity_transport_verified'],False),'claim':mut(original,['claims','full_burnside_ring_claimed'],True)}; expected=m.build(); rejected=0
 with tempfile.TemporaryDirectory(prefix='c93-mutations-') as d:
  for n,v in mutations.items():
   p=Path(d)/(n+'.json'); p.write_bytes(canon(v))
   try:
    assert json.loads(p.read_text())==expected
   except (AssertionError,KeyError,TypeError,ValueError): rejected+=1
   else: raise AssertionError('mutation accepted: '+n)
 assert rejected==len(mutations); print(json.dumps({'status':'C93_MUTATION_TEST_PASS','rejected':rejected},sort_keys=True))
if __name__=='__main__': main()
