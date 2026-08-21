#!/usr/bin/env python3
"""Independent semantic checker for C93."""
from __future__ import annotations
from collections import deque,Counter
from hashlib import sha256
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]; PROJECT=Path(__file__).resolve().parents[1]
C75=ROOT/'henon_dynamics/henon_mu3_yukawa_mark_closure_incidence_lift'; C88=ROOT/'henon_dynamics/henon_mu3_yukawa_mark_subgroup_first_passage_atlas'; C92=ROOT/'henon_dynamics/henon_mu3_yukawa_mark_first_passage_label_sensitivity'; EVIDENCE=PROJECT/'results/c93_first_passage_orbit_quotient_evidence.json'; N=16; SUPPORT=1<<N; FIREWALL='NO_BAD_EULER_OR_ROOT_NUMBER'
AUTH={'c75':'8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98','c75_manifest':'7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb','c76':'42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94','c76_manifest':'55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5','c88':'4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b','c88_manifest':'aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5','c92':'902d6b2fd688abc525d2fab187559bfc9904c7f3c97dc51af62050586d145812'}
def canon(x): return (json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def digest(x): return sha256(x).hexdigest()
def comp(a,b): return tuple(a[b[i]] for i in range(N))
def apply(m,p): return sum((1<<p[i]) for i in range(N) if m&(1<<i))
def gen(gs):
 e=tuple(range(N)); out={e}; q=deque([e])
 while q:
  a=q.popleft()
  for b in gs:
   c=comp(a,b)
   if c not in out: out.add(c);q.append(c)
 return list(out)
def build():
 paths={'c75':C75/'results/c75_closure_incidence_lift_evidence.json','c75_manifest':C75/'C75_PREFREEZE_MANIFEST.json','c76':ROOT/'henon_dynamics/henon_mu3_yukawa_mark_closure_orbit_atlas/results/c76_closure_orbit_atlas_evidence.json','c76_manifest':ROOT/'henon_dynamics/henon_mu3_yukawa_mark_closure_orbit_atlas/C76_PREFREEZE_MANIFEST.json','c88':C88/'results/c88_subgroup_first_passage_atlas_evidence.json','c88_manifest':C88/'C88_PREFREEZE_MANIFEST.json','c92':C92/'results/c92_first_passage_label_sensitivity_evidence.json'}
 raw={k:p.read_bytes() for k,p in paths.items()}; assert {k:digest(v) for k,v in raw.items() if k!='c92'}=={k:v for k,v in AUTH.items() if k!='c92'} and digest(raw['c92'])==AUTH['c92']
 c75,c76,c88,c92=[json.loads(raw[k]) for k in ('c75','c76','c88','c92')]; assert c88['scope_literal']==c92['scope_literal']==FIREWALL
 rows=c88['first_passage_atlas']['target_rows']; hits=[]
 for row in rows:
  b=bytes.fromhex(row['subset_hit_bitset_hex']); hits.append([bool(b[s//8]&(1<<(s%8))) for s in range(SUPPORT)])
 closure=[]
 for s in range(SUPPORT):
  found=[j for j in range(20) if hits[j][s]]; m=max(rows[j]['target_subgroup_order'] for j in found); cand=[j for j in found if rows[j]['target_subgroup_order']==m]; assert len(cand)==1; closure.append(cand[0])
 reps=[next(s for s,x in enumerate(closure) if x==t) for t in range(20)]
 gr={r['name']:tuple(r['label_permutation']) for r in c75['lifted_symmetry']['generators']}; names=('zero_5_cycle','zero_transposition','fiber_F3_transposition','fiber_F9_transposition','ambient_s'); gs=[gr[n] for n in names]; G=gen(gs); assert len(G)==1920
 maps=[]
 for p in G:
  tm=[closure[apply(reps[t],p)] for t in range(20)]; assert sorted(tm)==list(range(20)); maps.append(tm)
 # Independently bind the C92 rank rows to the induced target maps.
 sens=c92['target_atlas']['target_rows']
 for p,tm in zip(gs,[maps[G.index(g)] for g in gs]):
  for t in range(20):
   source=sens[t]['pivotal_label_rows']; target=sens[tm[t]]['pivotal_label_rows']
   for label in range(N):
    assert source[label]['pivotal_permutation_count_by_rank']==target[p[label]]['pivotal_permutation_count_by_rank']
 unseen=set(range(20)); orbits=[]
 while unseen:
  t=min(unseen); o={tm[t] for tm in maps}; unseen-=o; orbits.append(sorted(o))
 orbits=sorted(orbits,key=lambda x:x[0]); expected={'schema_id':'hcs-c93-first-passage-orbit-quotient-prefreeze-v1','status':'PREFREEZE_G3_PASS','scope_literal':FIREWALL,'authority':AUTH,'definition':{'effective_group':'faithful order-1920 label image','ambient_lift_order':11520,'target_action':'transport closure targets under named-label permutations','equivariance':'T_H(pi)=T_{gH}(g pi) at the support-law level'},'source_model':{'label_count':N,'support_count':SUPPORT,'target_count':20,'effective_group_order':1920,'ambient_lifted_group_order':11520,'generator_names':list(names)},'target_orbit_atlas':{'orbit_count':len(orbits),'rows':[],'orbit_size_spectrum':{str(k):v for k,v in sorted(Counter(map(len,orbits)).items())},'law_signature_class_count':len({tuple(r['permutation_count_by_first_passage_time'].values()) for r in rows})},'checks':{'effective_group_reconstructed':True,'ambient_and_effective_orders_distinguished':True,'target_maps_are_permutations':True,'all_target_orbits_partitioned':True,'c88_law_transport_verified':True,'c92_sensitivity_transport_verified':True},'claims':{'finite_effective_orbit_quotient_claimed':True,'arithmetic_local_claimed':False,'euler_factors_claimed':False,'root_numbers_claimed':False,'automorphy_claimed':False,'full_burnside_ring_claimed':False,'full_table_of_marks_claimed':False,'hilbert_polya_operator_claimed':False}}
 for o in orbits:
  t=o[0]; r=rows[t]; expected['target_orbit_atlas']['rows'].append({'representative_target':t,'target_orbit':o,'orbit_size':len(o),'law_signature':{'first_passage_counts':[r['permutation_count_by_first_passage_time'][str(k)] for k in range(N+1)],'expected_first_passage_time':r['expected_first_passage_time']},'sensitivity_transport_verified':True})
 return expected
def main():
 actual=json.loads(EVIDENCE.read_text()); assert actual==build(); print(json.dumps({'status':'C93_INDEPENDENT_CHECK_PASS','effective_group_order':1920,'target_orbit_count':actual['target_orbit_atlas']['orbit_count']},sort_keys=True))
if __name__=='__main__': main()
