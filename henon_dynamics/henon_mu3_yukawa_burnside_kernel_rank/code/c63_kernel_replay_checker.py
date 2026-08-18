#!/usr/bin/env python3
"""Independent source-reconstructing replay for C63 (no writes)."""
from __future__ import annotations
from collections import deque
from fractions import Fraction
import hashlib, json
from pathlib import Path

ROOT = Path('/root/autodl-tmp/hilbert-polya-structure')
TARGET = ROOT/'henon_dynamics/henon_mu3_yukawa_burnside_kernel_rank'
EVIDENCE = TARGET/'results/c63_kernel_evidence.json'
C61 = ROOT/'henon_dynamics/henon_mu3_yukawa_tensor_fourier_descent/results/c61_group_evidence.json'
ATLAS = ROOT/'henon_dynamics/henon_mu3_yukawa_lambda_square_shadow/results/c62_atlas_evidence.json'
DICT = ROOT/'henon_dynamics/henon_mu3_yukawa_lambda_square_shadow/results/c62_dictionary_evidence.json'
H_C61='f4be3a2c5990120a97264505ba9f21b55b8f8c330521044936a52f68e8cd89e9'
H_ATLAS='3c40a674779a0e2d6d1c69b7c4ccc9115c4b9a2ba049684e8c5204b94b621c40'
H_DICT='85dc05d043e3781631330083303b98995201c7c30b53aae2901d5fd874b6cd5e'
MATRIX_SHA='e912b0f37f69ac1e23cf432915aa4258818312f84fba776986876c7625a84a9b'
TYPES=[f'S{i}' for i in range(1,17)]
ID=tuple(range(27))

def canon(x): return (json.dumps(x,sort_keys=True,separators=(',',':'))+'\n').encode()
def h(x): return hashlib.sha256(x).hexdigest()
def digest(x): return h(canon(x))
def comp(a,b): return tuple(a[b[i]] for i in range(len(a)))
def inv(a):
    r=[0]*len(a)
    for i,j in enumerate(a): r[j]=i
    return tuple(r)
def perms(rows):
    out=[]; target=list(range(1,28))
    for row in rows:
        row=list(row)
        if sorted(row)!=target: raise RuntimeError('bad permutation')
        out.append(tuple(x-1 for x in row))
    return tuple(out)
def close(gs):
    gs=tuple(gs); out={tuple(range(len(gs[0])))}; q=deque(out)
    while q:
        x=q.popleft()
        for g in gs:
            y=comp(g,x)
            if y not in out: out.add(y); q.append(y)
    return frozenset(out)
def classes(G):
    ii={x:inv(x) for x in G}; left=set(G); ans=[]; carriers=tuple(sorted(G))
    while left:
        x=min(left); C=frozenset(comp(comp(y,x),ii[y]) for y in carriers)
        if x not in C or not C<=G: raise RuntimeError('bad class')
        ans.append(C); left-=C
    return sorted(ans,key=min)
def rankq(A):
    if not A:return 0
    A=[[Fraction(x) for x in row] for row in A]; m,n=len(A),len(A[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None:continue
        A[r],A[p]=A[p],A[r]; z=A[r][c]; A[r]=[x/z for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]; A[i]=[x-z*y for x,y in zip(A[i],A[r])]
        r+=1
    return r
def sgenerators(H):
    chosen=[]; cur=frozenset({ID})
    for x in sorted(H):
        if x in cur:continue
        chosen.append(x); cur=close(chosen)
        if cur==H:return tuple(chosen)
    raise RuntimeError('subgroup generation')
def conj(G,H,K):
    if len(H)!=len(K):return False
    gs=sgenerators(H)
    for x in sorted(G):
        xi=inv(x)
        if all(comp(comp(x,g),xi) in K for g in gs):return True
    return False
def load(path,expected=None):
    raw=path.read_bytes()
    if expected is not None and h(raw)!=expected:raise RuntimeError(f'hash {path}')
    return raw,json.loads(raw)
def main():
    rc,c61=load(C61,H_C61); ra,atlas=load(ATLAS,H_ATLAS); rd,dic=load(DICT,H_DICT); re,e=load(EVIDENCE)
    if re!=canon(e):raise RuntimeError('noncanonical evidence')
    assert e['schema_id']=='hcs-c63-burnside-kernel-prefreeze-v1' and e['status']=='PREFREEZE_G3_PASS'
    assert e['scope_literal']=='NO_BAD_EULER_OR_ROOT_NUMBER'
    assert atlas['schema_id']=='hcs-c62-complete-atlas-prefreeze-v1' and atlas['scope_literal']==e['scope_literal']
    assert dic['schema_id']=='hcs-c62-fixed-field-dictionary-prefreeze-v1' and dic['scope_literal']==e['scope_literal']
    assert e['authority']=={'ambient_order':51840,'class_count':25,'type_count':16,'c61_group_evidence_sha256':h(rc),'c62_atlas_evidence_sha256':h(ra),'c62_dictionary_evidence_sha256':h(rd)}
    ad=c61['python_projection']['ambient']; G=close(perms(ad['W_generators_one_based'])); Hp=close(perms(ad['Hplus_generators_one_based'])); Hm=close(perms(ad['Hminus_generators_one_based']))
    assert len(G)==51840 and len(Hp)==len(Hm)==162
    C=classes(G); assert len(C)==25 and sum(map(len,C))==len(G)
    cm=[{'class_id':i+1,'representative_one_based':[x+1 for x in min(c)],'size':len(c),'centralizer_order':len(G)//len(c)} for i,c in enumerate(C)]
    assert e['conjugacy_classes']==cm
    # Full atlas sets are independently digested and dictionary representatives selected.
    ag={}
    for family in atlas['atlases'].values():
        for row in family['rows']:
            for side in ('plus','minus'):
                d=row[side]; S=frozenset(perms(d['stabilizer_elements_one_based']))
                assert len(S)==d['stabilizer_order'] and digest([[x+1 for x in z] for z in sorted(S)])==d['stabilizer_sha256']; ag[d['stabilizer_sha256']]=S
    tm={x['type_id']:x for x in dic['types']}; assert sorted(tm,key=lambda x:int(x[1:]))==TYPES
    Ts={}
    expected_types=[]
    for t in TYPES:
        m=tm[t]; S=ag[m['representative_sha256']]; assert len(S)==m['order'] and m['field_degree']*len(S)==len(G) and m['core_order']==1
        Ts[t]=S; expected_types.append({'type_id':t,'subgroup_order':len(S),'field_degree':m['field_degree'],'stabilizer_sha256':m['representative_sha256']})
    assert e['types']==expected_types
    ci={z:i for i,c in enumerate(C) for z in c}
    def char(S):
        count=[0]*len(C)
        for z in S:count[ci[z]]+=1
        out=[]
        for i,c in enumerate(C):
            num=(len(G)//len(c))*count[i]; assert num%len(S)==0; out.append(num//len(S))
        return out
    M=[list(row) for row in zip(*(char(Ts[t]) for t in TYPES))]
    assert e['column_order']==TYPES and e['character_matrix']==M and len(M)==25 and all(len(r)==16 for r in M)
    assert digest(M)==MATRIX_SHA==e['matrix_sha256'] and rankq(M)==e['rank_over_Q']==13 and e['nullity_over_Q']==3
    # Exact ambient-conjugacy mapping of the original C61 H pair.
    assert [t for t,S in Ts.items() if conj(G,Hp,S)]==['S15']
    assert [t for t,S in Ts.items() if conj(G,Hm,S)]==['S16']
    assert not conj(G,Hp,Hm) and e['hplus_type']=='S15' and e['hminus_type']=='S16'
    assert char(Hp)==char(Hm)==e['common_hplus_hminus_character']
    pos={t:i for i,t in enumerate(TYPES)}
    def vec(d):
        v=[0]*16
        for t,z in d.items():v[pos[t]]=z
        return v
    def rel(kind):
        v=[0]*16
        for row in dic['rows'][kind]['plus']:v[pos[row['field_type']]]+=1
        for row in dic['rows'][kind]['minus']:v[pos[row['field_type']]]-=1
        return v
    r=vec({'S15':1,'S16':-1}); qe=rel('exterior_square'); qs=rel('symmetric_square')
    assert e['relation_vectors']=={'r_c61':r,'q_exterior':qe,'q_symmetric':qs} and qs==[a+b for a,b in zip(qe,r)]
    assert all(all(sum(M[i][j]*v[j] for j in range(16))==0 for i in range(25)) for v in (r,qe,qs))
    basis={'z1':vec({'S10':1,'S9':-1}),'z2':vec({'S2':-1,'S3':-1,'S5':-1,'S6':-1,'S11':1,'S12':1,'S13':1,'S14':1}),'z3':vec({'S16':1,'S15':-1})}
    assert e['nullspace_basis']==basis and all(all(sum(M[i][j]*v[j] for j in range(16))==0 for i in range(25)) for v in basis.values()) and rankq(list(basis.values()))==3
    primitive=e['primitive_support']; support=[i for i,x in enumerate(qe) if x]
    assert primitive['type_ids']==[TYPES[i] for i in support]
    assert primitive['support_size']==8
    assert primitive['restricted_rank_over_Q']==rankq([[row[i] for i in support] for row in M])==7
    assert primitive['restricted_nullity_over_Q']==1
    assert e['claims']=={'restricted_16_type_kernel_only':True,'full_burnside_ring_kernel_claimed':False,'arithmetic_local_claimed':False}
    print(json.dumps({'status':'REPLAY_PASS','ambient_order':len(G),'class_count':len(C),'type_count':16,'matrix_shape':[25,16],'matrix_sha256':MATRIX_SHA,'rank_over_Q':13,'nullity_over_Q':3,'hplus_type':'S15','hminus_type':'S16','lambda_exterior_zero':True,'lambda_symmetric_zero':True},sort_keys=True))
if __name__=='__main__':main()
