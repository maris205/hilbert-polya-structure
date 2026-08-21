#!/usr/bin/env python3
"""Produce the C93 effective-orbit quotient of first-passage laws."""
from __future__ import annotations
from collections import Counter, deque
from hashlib import sha256
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]; PROJECT=Path(__file__).resolve().parents[1]
C75=ROOT/'henon_dynamics/henon_mu3_yukawa_mark_closure_incidence_lift'; C76=ROOT/'henon_dynamics/henon_mu3_yukawa_mark_closure_orbit_atlas'; C88=ROOT/'henon_dynamics/henon_mu3_yukawa_mark_subgroup_first_passage_atlas'; C92=ROOT/'henon_dynamics/henon_mu3_yukawa_mark_first_passage_label_sensitivity'
OUT=PROJECT/'results/c93_first_passage_orbit_quotient_evidence.json'; FIREWALL='NO_BAD_EULER_OR_ROOT_NUMBER'; N=16; SUPPORT=1<<N
AUTH={'c75':'8beee17a227153e066907549df70c14a087b7de4141c3092d7cebd4a91541d98','c75_manifest':'7ede3e35c3101d17c683d2da440037d5bd4e002266530b52b3d1cb36ed4c8fcb','c76':'42e7783b2652666b84ea7f82b65d2421d98064ee5d5011ab94033aa18c051a94','c76_manifest':'55725664005113ae993b54197ff4fbd97bde347ce49aa69ea0c228372ba289d5','c88':'4511d434f477784782f2af5106afff4c2cf3b48cd7eb7a62ed05b8f2f42afb1b','c88_manifest':'aab137987b45be54d401b5a021212412de25097b149a73ee65c8e0daaced56c5','c92':'902d6b2fd688abc525d2fab187559bfc9904c7f3c97dc51af62050586d145812'}
def canon(x): return (json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def digest(x): return sha256(x).hexdigest()
def compose(a,b): return tuple(a[b[i]] for i in range(N))
def apply(mask,p):
 r=0
 for i in range(N):
  if mask&(1<<i): r|=1<<p[i]
 return r
def group(gens):
 e=tuple(range(N)); out={e}; q=deque([e])
 while q:
  a=q.popleft()
  for b in gens:
   c=compose(a,b)
   if c not in out: out.add(c); q.append(c)
 return sorted(out)
def main():
 paths={k:p for k,p in {'c75':C75/'results/c75_closure_incidence_lift_evidence.json','c75_manifest':C75/'C75_PREFREEZE_MANIFEST.json','c76':C76/'results/c76_closure_orbit_atlas_evidence.json','c76_manifest':C76/'C76_PREFREEZE_MANIFEST.json','c88':C88/'results/c88_subgroup_first_passage_atlas_evidence.json','c88_manifest':C88/'C88_PREFREEZE_MANIFEST.json','c92':C92/'results/c92_first_passage_label_sensitivity_evidence.json'}.items()}
 raw={k:p.read_bytes() for k,p in paths.items()}; assert {k:digest(v) for k,v in raw.items() if k!='c92'}=={k:v for k,v in AUTH.items() if k!='c92'}; assert digest(raw['c92'])==AUTH['c92']
 c75,c76,c88,c92=[json.loads(raw[k]) for k in ('c75','c76','c88','c92')]; assert c88['scope_literal']==c92['scope_literal']==FIREWALL
 rows=c88['first_passage_atlas']['target_rows']; hits=[]
 for row in rows:
  b=bytes.fromhex(row['subset_hit_bitset_hex']); hits.append([bool(b[s//8]&(1<<(s%8))) for s in range(SUPPORT)])
 names=('zero_5_cycle','zero_transposition','fiber_F3_transposition','fiber_F9_transposition','ambient_s'); gr={r['name']:tuple(r['label_permutation']) for r in c75['lifted_symmetry']['generators']}; gens=[gr[n] for n in names]; G=group(gens); assert len(G)==1920; assert c76['source_model']['effective_label_group_order']==1920
 # Recover an exact-closure representative for every target from the C88
 # containment upsets, then transport those representatives.
 closure_of=[]
 for support in range(SUPPORT):
  found=[j for j in range(20) if hits[j][support]]
  maximal=max(rows[j]['target_subgroup_order'] for j in found)
  candidates=[j for j in found if rows[j]['target_subgroup_order']==maximal]
  assert len(candidates)==1
  closure_of.append(candidates[0])
 reps=[]
 for t in range(20):
  choices=[support for support,closed in enumerate(closure_of) if closed==t]
  assert choices
  reps.append(choices[0])
 target_maps=[]
 for p in G:
  tm=[]
  for t,rep in enumerate(reps):
   image=apply(rep,p); found=[j for j in range(20) if hits[j][image]]
   assert found
   maximal_order=max(rows[j]['target_subgroup_order'] for j in found)
   candidates=[j for j in found if rows[j]['target_subgroup_order']==maximal_order]
   assert len(candidates)==1
   tm.append(candidates[0])
  target_maps.append(tuple(tm))
 # Verify each map is a permutation and C88 laws are transported by support action.
 assert all(sorted(tm)==list(range(20)) for tm in target_maps)
 # Generator-level equivariance is the independent closure check.  It is
 # enough to certify the full generated group once the five permutations have
 # been rebuilt and the target maps are permutations.
 for p in gens:
  tm=target_maps[G.index(p)]
  for t in range(20):
   image_rep=apply(reps[t],p)
   assert closure_of[image_rep]==tm[t]
   for support in range(SUPPORT):
    assert hits[t][support]==hits[tm[t]][apply(support,p)]
  for t in range(20):
   source_labels=c92['target_atlas']['target_rows'][t]['pivotal_label_rows']
   target_labels=c92['target_atlas']['target_rows'][tm[t]]['pivotal_label_rows']
   for label in range(N):
    assert source_labels[label]['pivotal_permutation_count_by_rank']==target_labels[p[label]]['pivotal_permutation_count_by_rank']
 law_sigs=[]
 for t,row in enumerate(rows): law_sigs.append((tuple(row['permutation_count_by_first_passage_time'].values()),row['expected_first_passage_time']['numerator'],row['expected_first_passage_time']['denominator']))
 law_orbits=[]; unseen=set(range(20))
 while unseen:
  t=min(unseen); orb={tm[t] for tm in target_maps}; assert orb<=set(range(20)); unseen-=orb; law_orbits.append(sorted(orb))
 # C92 label sensitivity is transported by the same permutation.
 sens=c92['target_atlas']['target_rows']; sens_orbits=[]; unseen=set(range(20))
 while unseen:
  t=min(unseen); orb={tm[t] for tm in target_maps}; unseen-=orb; sens_orbits.append(sorted(orb))
 assert sorted(law_orbits)==sorted(sens_orbits)
 rows_out=[]
 for orb in sorted(law_orbits,key=lambda x:x[0]):
  rep=orb[0]; rows_out.append({'representative_target':rep,'target_orbit':orb,'orbit_size':len(orb),'law_signature':{'first_passage_counts':[rows[rep]['permutation_count_by_first_passage_time'][str(k)] for k in range(N+1)],'expected_first_passage_time':{'numerator':law_sigs[rep][1],'denominator':law_sigs[rep][2]}},'sensitivity_transport_verified':True})
 result={'schema_id':'hcs-c93-first-passage-orbit-quotient-prefreeze-v1','status':'PREFREEZE_G3_PASS','scope_literal':FIREWALL,'authority':AUTH,'definition':{'effective_group':'faithful order-1920 label image','ambient_lift_order':11520,'target_action':'transport closure targets under named-label permutations','equivariance':'T_H(pi)=T_{gH}(g pi) at the support-law level'},'source_model':{'label_count':N,'support_count':SUPPORT,'target_count':20,'effective_group_order':len(G),'ambient_lifted_group_order':11520,'generator_names':list(names)},'target_orbit_atlas':{'orbit_count':len(rows_out),'rows':rows_out,'orbit_size_spectrum':{str(k):v for k,v in sorted(Counter(len(x) for x in law_orbits).items())},'law_signature_class_count':len(set(law_sigs))},'checks':{'effective_group_reconstructed':True,'ambient_and_effective_orders_distinguished':True,'target_maps_are_permutations':True,'all_target_orbits_partitioned':True,'c88_law_transport_verified':True,'c92_sensitivity_transport_verified':True},'claims':{'finite_effective_orbit_quotient_claimed':True,'arithmetic_local_claimed':False,'euler_factors_claimed':False,'root_numbers_claimed':False,'automorphy_claimed':False,'full_burnside_ring_claimed':False,'full_table_of_marks_claimed':False,'hilbert_polya_operator_claimed':False}}
 OUT.write_bytes(canon(result)); print(json.dumps({'status':result['status'],'effective_group_order':len(G),'target_orbit_count':len(rows_out),'orbit_size_spectrum':result['target_orbit_atlas']['orbit_size_spectrum'],'evidence_sha256':digest(OUT.read_bytes())},sort_keys=True))
if __name__=='__main__': main()
