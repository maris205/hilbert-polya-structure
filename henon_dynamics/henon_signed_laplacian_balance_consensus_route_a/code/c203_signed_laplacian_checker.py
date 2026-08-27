#!/usr/bin/env python3
"""Independent exact-schema checker for the exhaustive C203 ledger."""
from __future__ import annotations
import argparse, json
from hashlib import sha256
from itertools import combinations, product
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]; DEFAULT=ROOT/"results/c203_signed_laplacian_evidence.json"
SOURCE_COMMIT="d1e58971e570b855488009af384995702ddb887b"; EVALUATOR_SHA256="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
HEADLINE="Every finite disconnected undirected positive-weight signed network has an exact balance-controlled semigroup limit, spectral rate, and full principal-minor and characteristic pseudoforest expansion"
def payload_hash(d):
    b=dict(d); b.pop("payload_sha256",None); return sha256(json.dumps(b,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
def lap(n,edges):
    M=sp.zeros(n)
    for i,j,z in edges: M[i,i]+=1; M[j,j]+=1; M[i,j]-=z; M[j,i]-=z
    return M
def comps(n,edges):
    adj=[[] for _ in range(n)]
    for i,j,z in edges: adj[i].append((j,z)); adj[j].append((i,z))
    used=set(); out=[]
    for r in range(n):
        if r in used: continue
        queue=[r]; used.add(r); vs=[]; sw={r:1}; bal=True
        while queue:
            u=queue.pop(0); vs.append(u)
            for v,z in adj[u]:
                if v in sw and sw[v]!=z*sw[u]: bal=False
                if v not in sw: sw[v]=z*sw[u]
                if v not in used: used.add(v); queue.append(v)
        vs.sort(); out.append((vs,bal,[sw[v] for v in vs] if bal else None))
    return out
def forests(n,edges):
    minors=[0]*(1<<n); coeff=[0]*(n+1)
    for bits in product((0,1),repeat=len(edges)):
        E=[e for e,b in zip(edges,bits) if b]; parts=comps(n,E); kinds=[]; u=0; good=True
        for vs,bal,_ in parts:
            S=set(vs); ec=sum(i in S and j in S for i,j,_ in E)
            if ec==len(vs)-1: kinds.append((vs,0))
            elif ec==len(vs) and not bal: kinds.append((vs,1)); u+=1
            else: good=False; break
        if not good: continue
        weight=4**u; trees=[v for v,k in kinds if k==0]
        coeff[len(trees)]+=weight*sp.prod(len(v) for v in trees)
        for R in range(1<<n):
            if all(sum(R>>v&1 for v in vs)==(1 if kind==0 else 0) for vs,kind in kinds): minors[R]+=weight
    return minors,[int(x) for x in coeff]
def main():
    p=argparse.ArgumentParser(); p.add_argument("--evidence",type=Path,default=DEFAULT); d=json.loads(p.parse_args().evidence.read_text()); assertions=0
    def check(c,msg):
        nonlocal assertions; assertions+=1
        if not c: raise AssertionError(msg)
    def keys(x,k,w): check(isinstance(x,dict),w+" type"); check(set(x)==set(k),w+" keys")
    keys(d,{"schema","candidate_id","evaluation_date","source_commit","scope_literal","evaluator","headline","frozen_object","theorem","exhaustive_regression","counterexamples","summary","route_a","scope_flags","citations","nonclaims","payload_sha256"},"top")
    keys(d["evaluator"],{"path","version","sha256"},"eval"); keys(d["frozen_object"],{"graph_class","incidence","laplacian","flow","excluded"},"frozen")
    keys(d["theorem"],{"balance_kernel","nullity","projector","semigroup","exact_rate","principal_minor","characteristic_polynomial"},"theorem")
    keys(d["exhaustive_regression"],{"vertex_range","weight_specialization","graphs"},"regression")
    keys(d["counterexamples"],{"bridge_negative_triangle","directed_exclusion"},"counterexamples")
    keys(d["summary"],{"graph_count","principal_minor_checks","characteristic_polynomial_checks","balanced_component_records","unbalanced_component_records","balanced_graphs","counterexamples","max_vertices"},"summary")
    keys(d["route_a"],{"tuple","overall","route_b_invocation_allowed","strongest_positive","strongest_failure"},"route")
    keys(d["scope_flags"],{"uses_target_zero_table","uses_prime_table","claims_arithmetic_local_data","claims_euler_factors","claims_root_numbers","claims_automorphy","claims_target_divisor_or_functional_equation","claims_hilbert_polya_operator","invokes_route_b"},"flags")
    check(d["payload_sha256"]==payload_hash(d),"hash"); check(d["schema"]=="hcs-c203-signed-laplacian-v1","schema"); check(d["candidate_id"]=="HCS-C203","id")
    check(d["evaluation_date"]=="2026-08-27","date"); check(d["source_commit"]==SOURCE_COMMIT,"source"); check(d["scope_literal"]=="NO_BAD_EULER_OR_ROOT_NUMBER","scope")
    check(d["evaluator"]["sha256"]==EVALUATOR_SHA256,"evaluator"); check(d["headline"]==HEADLINE,"headline")
    check(d["route_a"]["tuple"]==["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"],"tuple"); check(d["route_a"]["overall"]=="ROUTE_A_REJECTED","overall")
    check(d["route_a"]["route_b_invocation_allowed"] is False,"route B"); check(all(x is False for x in d["scope_flags"].values()),"flags")
    dois=["10.1109/TAC.2012.2224251","10.1307/mmj/1028989917","10.1016/0166-218X(82)90033-6","10.1016/0166-218X(83)90047-1"]
    check(len(d["citations"])==4,"cit len")
    for i,x in enumerate(d["citations"]): keys(x,{"key","claim","doi"},f"cit {i}"); check(x["doi"]==dois[i],"doi")
    records=d["exhaustive_regression"]["graphs"]; pos=0; root_count=0; bc=uc=bg=0
    for n in range(1,5):
        pairs=list(combinations(range(n),2))
        for code,states in enumerate(product((-1,0,1),repeat=len(pairs))):
            row=records[pos]; pos+=1
            keys(row,{"n","graph_code","sign_word","edge_count","components","nullity","determinant","characteristic_coefficients_matrix","characteristic_coefficients_pseudoforest","principal_minors"},f"graph {pos}")
            check(row["n"]==n and row["graph_code"]==code,"graph identity"); check(row["sign_word"]=="".join({-1:"-",0:"0",1:"+"}[x] for x in states),"word")
            E=[(i,j,z) for (i,j),z in zip(pairs,states) if z]; check(row["edge_count"]==len(E),"edge count"); M=lap(n,E); C=comps(n,E)
            check(len(row["components"])==len(C),"component count")
            for k,(got,want) in enumerate(zip(row["components"],C)):
                keys(got,{"vertices","balanced","switch"},f"component {pos}.{k}"); check(got["vertices"]==want[0] and got["balanced"]==want[1] and got["switch"]==want[2],"component data")
                bc+=int(want[1]); uc+=int(not want[1])
            bg+=int(all(x[1] for x in C)); check(row["nullity"]==sum(x[1] for x in C)==n-M.rank(),"nullity")
            check(row["determinant"]==int(M.det()),"determinant")
            fm,fc=forests(n,E); check(row["characteristic_coefficients_pseudoforest"]==fc,"forest char")
            lam=sp.symbols("lambda"); poly=sp.Poly((lam*sp.eye(n)+M).det(),lam); mc=[int(poly.nth(k)) for k in range(n+1)]
            check(row["characteristic_coefficients_matrix"]==mc==fc,"matrix char")
            check(len(row["principal_minors"])==1<<n,"minor count")
            for R,mrow in enumerate(row["principal_minors"]):
                keys(mrow,{"root_mask","matrix_determinant","pseudoforest_sum"},f"minor {pos}.{R}"); keep=[i for i in range(n) if not(R>>i&1)]
                dm=int(M.extract(keep,keep).det()) if keep else 1
                check(mrow["root_mask"]==R and mrow["matrix_determinant"]==dm and mrow["pseudoforest_sum"]==fm[R]==dm,"minor identity"); root_count+=1
    check(pos==len(records)==760,"graph total"); check(root_count==11894,"root total")
    s=d["summary"]; check(s["graph_count"]==760,"summary graphs"); check(s["principal_minor_checks"]==11894,"summary minors"); check(s["characteristic_polynomial_checks"]==760,"summary char")
    check(s["balanced_component_records"]==bc and s["unbalanced_component_records"]==uc,"component summaries"); check(s["balanced_graphs"]==bg,"balanced summary"); check(s["counterexamples"]==2 and s["max_vertices"]==4,"other summaries")
    b=d["counterexamples"]["bridge_negative_triangle"]; keys(b,{"description","edges","signed_laplacian","full_determinant","delete_root_0_cofactor","ordinary_spanning_tree_contribution","rootless_negative_cycle_contribution"},"bridge")
    BM=sp.Matrix(b["signed_laplacian"]); check(BM.det()==b["full_determinant"]==4,"bridge det"); check(BM[1:,1:].det()==b["delete_root_0_cofactor"]==7,"bridge cofactor"); check(b["ordinary_spanning_tree_contribution"]+b["rootless_negative_cycle_contribution"]==7,"bridge decomposition")
    z=d["counterexamples"]["directed_exclusion"]; keys(z,{"description","matrix","right_zero_vector","left_zero_probability","limit_projector","orthogonal_projector"},"directed")
    A=sp.Matrix(z["matrix"]); right=sp.Matrix(z["right_zero_vector"]); left=sp.Matrix([[sp.Rational(x) for x in z["left_zero_probability"]]])
    check(A*right==sp.zeros(2,1) and left*A==sp.zeros(1,2),"directed nullvectors"); check(z["orthogonal_projector"] is False,"directed exclusion")
    print(json.dumps({"status":"C203_CHECKER_PASS","assertions":assertions,"graphs":pos,"principal_minors":root_count,"balanced_components":bc,"unbalanced_components":uc},sort_keys=True))
if __name__=="__main__": main()
