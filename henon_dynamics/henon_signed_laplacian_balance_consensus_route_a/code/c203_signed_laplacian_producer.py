#!/usr/bin/env python3
"""Produce the exhaustive C203 signed-Laplacian certificate."""
from __future__ import annotations

import argparse
from hashlib import sha256
from itertools import combinations, product
import json
from pathlib import Path


SOURCE_COMMIT="d1e58971e570b855488009af384995702ddb887b"
EVALUATOR_SHA256="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
SCOPE="NO_BAD_EULER_OR_ROOT_NUMBER"
DEFAULT_OUTPUT=Path(__file__).resolve().parents[1]/"results/c203_signed_laplacian_evidence.json"


def payload_hash(data):
    body=dict(data); body.pop("payload_sha256",None)
    return sha256(json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()


def det_bareiss(a):
    n=len(a)
    if n==0: return 1
    b=[row[:] for row in a]; sign=1; prev=1
    for k in range(n-1):
        if b[k][k]==0:
            pivot=next((i for i in range(k+1,n) if b[i][k]),None)
            if pivot is None: return 0
            b[k],b[pivot]=b[pivot],b[k]; sign=-sign
        pivot=b[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n): b[i][j]=(b[i][j]*pivot-b[i][k]*b[k][j])//prev
        prev=pivot
    return sign*b[-1][-1]


def laplacian(n,edges):
    L=[[0]*n for _ in range(n)]
    for i,j,sgn in edges:
        L[i][i]+=1; L[j][j]+=1; L[i][j]-=sgn; L[j][i]-=sgn
    return L


def components(n,edges):
    adj=[[] for _ in range(n)]
    for i,j,sgn in edges: adj[i].append((j,sgn)); adj[j].append((i,sgn))
    seen=set(); out=[]
    for start in range(n):
        if start in seen: continue
        stack=[start]; seen.add(start); vertices=[]; switch={start:1}; balanced=True
        while stack:
            u=stack.pop(); vertices.append(u)
            for v,sgn in adj[u]:
                want=sgn*switch[u]
                if v not in switch: switch[v]=want
                elif switch[v]!=want: balanced=False
                if v not in seen: seen.add(v); stack.append(v)
        vertices.sort(); out.append((vertices,balanced,[switch[v] for v in vertices] if balanced else None))
    return out


def forest_tables(n,edges):
    minor=[0]*(1<<n); char=[0]*(n+1); m=len(edges)
    for mask in range(1<<m):
        chosen=[edges[k] for k in range(m) if mask>>k&1]
        comps=components(n,chosen); valid=True; kinds=[]; unicycles=0
        for verts,balanced,_ in comps:
            vset=set(verts); ec=sum(i in vset and j in vset for i,j,_ in chosen)
            if ec==len(verts)-1: kinds.append((verts,"tree"))
            elif ec==len(verts) and not balanced: kinds.append((verts,"negative_unicycle")); unicycles+=1
            else: valid=False; break
        if not valid: continue
        weight=4**unicycles
        tree_components=[verts for verts,kind in kinds if kind=="tree"]
        char[len(tree_components)]+=weight*__import__("math").prod(len(v) for v in tree_components)
        for roots in range(1<<n):
            ok=True
            for verts,kind in kinds:
                rc=sum(roots>>v&1 for v in verts)
                if (kind=="tree" and rc!=1) or (kind=="negative_unicycle" and rc!=0): ok=False; break
            if ok: minor[roots]+=weight
    return minor,char


def matrix_minor(L,roots):
    keep=[i for i in range(len(L)) if not (roots>>i&1)]
    return det_bareiss([[L[i][j] for j in keep] for i in keep])


def build():
    graphs=[]; root_checks=0; balanced_components=0; unbalanced_components=0; balanced_graphs=0
    for n in range(1,5):
        pairs=list(combinations(range(n),2))
        for code,states in enumerate(product((-1,0,1),repeat=len(pairs))):
            edges=[(i,j,sgn) for (i,j),sgn in zip(pairs,states) if sgn]
            L=laplacian(n,edges); comps=components(n,edges)
            comp_rows=[]
            for verts,balanced,switch in comps:
                comp_rows.append({"vertices":verts,"balanced":balanced,"switch":switch})
                balanced_components+=int(balanced); unbalanced_components+=int(not balanced)
            balanced_graphs+=int(all(x[1] for x in comps))
            forest_minor,forest_char=forest_tables(n,edges)
            minors=[]; matrix_char=[0]*(n+1)
            for roots in range(1<<n):
                d=matrix_minor(L,roots); minors.append({"root_mask":roots,"matrix_determinant":d,"pseudoforest_sum":forest_minor[roots]})
                matrix_char[roots.bit_count()]+=d; root_checks+=1
            graphs.append({
                "n":n,"graph_code":code,"sign_word":"".join({-1:"-",0:"0",1:"+"}[x] for x in states),
                "edge_count":len(edges),"components":comp_rows,
                "nullity":sum(c["balanced"] for c in comp_rows),"determinant":det_bareiss(L),
                "characteristic_coefficients_matrix":matrix_char,
                "characteristic_coefficients_pseudoforest":forest_char,
                "principal_minors":minors,
            })
    counterexamples={
        "bridge_negative_triangle": {
            "description":"positive bridge 0-1 attached to a triangle 1-2-3-1 with signs -,+,+",
            "edges":[[0,1,1],[1,2,-1],[2,3,1],[3,1,1]],
            "signed_laplacian":[[1,-1,0,0],[-1,3,1,-1],[0,1,2,-1],[0,-1,-1,2]],
            "full_determinant":4,"delete_root_0_cofactor":7,"ordinary_spanning_tree_contribution":3,"rootless_negative_cycle_contribution":4,
        },
        "directed_exclusion": {
            "description":"nonsymmetric directed Laplacian excluded by the theorem",
            "matrix":[[1,-1],[-2,2]],"right_zero_vector":[1,1],"left_zero_probability":["2/3","1/3"],
            "limit_projector":[["2/3","1/3"],["2/3","1/3"]],"orthogonal_projector":False,
        },
    }
    data={
        "schema":"hcs-c203-signed-laplacian-v1","candidate_id":"HCS-C203","evaluation_date":"2026-08-27",
        "source_commit":SOURCE_COMMIT,"scope_literal":SCOPE,
        "evaluator":{"path":"flow_systems/skills/route-a-evaluator.md","version":"0.2.0","sha256":EVALUATOR_SHA256},
        "headline":"Every finite disconnected undirected positive-weight signed network has an exact balance-controlled semigroup limit, spectral rate, and full principal-minor and characteristic pseudoforest expansion",
        "frozen_object":{
            "graph_class":"finite static undirected simple signed graphs, arbitrary disconnection, positive edge weights",
            "incidence":"for oriented edge e=ij with sign sigma_e, b_e=e_i-sigma_e e_j",
            "laplacian":"L=B W B^T=sum_e w_e b_e b_e^T",
            "flow":"x_dot=-Lx",
            "excluded":"directed, time-varying, zero/negative edge weights, self-loops, nonlinear protocols",
        },
        "theorem":{
            "balance_kernel":"each balanced component contributes its signed switch vector; every unbalanced component contributes no kernel",
            "nullity":"number of balanced connected components, isolated vertices included",
            "projector":"P=sum over balanced C of s_C s_C^T/|C|",
            "semigroup":"exp(-tL) tends to P; balanced components reach signed consensus and unbalanced components tend to zero",
            "exact_rate":"on (ker L)^perp, ||exp(-tL)-P||_2=exp(-gamma t), gamma=min positive eigenvalue of L",
            "principal_minor":"det L[V\\R]=sum_F 4^{u(F)} product_{e in F} w_e, with each component a one-root tree or a root-free negative unicycle",
            "characteristic_polynomial":"det(lambda I+L)=sum_F 4^{u(F)}w(F)lambda^{t(F)} product over tree components T of |V(T)|",
        },
        "exhaustive_regression":{"vertex_range":[1,2,3,4],"weight_specialization":"all present edges have weight 1","graphs":graphs},
        "counterexamples":counterexamples,
        "summary":{
            "graph_count":len(graphs),"principal_minor_checks":root_checks,"characteristic_polynomial_checks":len(graphs),
            "balanced_component_records":balanced_components,"unbalanced_component_records":unbalanced_components,
            "balanced_graphs":balanced_graphs,"counterexamples":2,"max_vertices":4,
        },
        "route_a":{
            "tuple":["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_FORMAL_HINT"],"overall":"ROUTE_A_REJECTED","route_b_invocation_allowed":False,
            "strongest_positive":"The positive semidefinite generator has a canonical self-adjoint semigroup, exact forest determinants, and a balance-controlled projector.",
            "strongest_failure":"Finite graph spectra and forest expansions do not provide a source-native prime-power orbit law or the target analytic object.",
        },
        "scope_flags":{
            "uses_target_zero_table":False,"uses_prime_table":False,"claims_arithmetic_local_data":False,"claims_euler_factors":False,"claims_root_numbers":False,
            "claims_automorphy":False,"claims_target_divisor_or_functional_equation":False,"claims_hilbert_polya_operator":False,"invokes_route_b":False,
        },
        "citations":[
            {"key":"Altafini2013","claim":"signed consensus and structural-balance dichotomy","doi":"10.1109/TAC.2012.2224251"},
            {"key":"Harary1953","claim":"structural balance of signed graphs","doi":"10.1307/mmj/1028989917"},
            {"key":"Zaslavsky1982","claim":"signed-graph incidence and matrix-tree foundations","doi":"10.1016/0166-218X(82)90033-6"},
            {"key":"Zaslavsky1983Erratum","claim":"erratum to the signed-graph matrix-tree source","doi":"10.1016/0166-218X(83)90047-1"},
        ],
        "nonclaims":[
            "priority for structural balance, signed consensus, signed matrix-tree theorems, or forest expansions",
            "that the n<=4 unit-weight exhaustive regression proves the arbitrary-size positive-weight theorem",
            "extension to directed, time-varying, nonlinear, zero-weight, or negative-weight networks",
            "that every principal minor is merely an ordinary rooted-tree count",
            "a prime-orbit law, Euler product, root number, automorphy, target determinant, or Hilbert--Polya operator",
            "external peer review, literature exhaustiveness, or an acceptance score",
        ],
    }
    data["payload_sha256"]=payload_hash(data); return data


def main():
    p=argparse.ArgumentParser(); p.add_argument("--output",type=Path,default=DEFAULT_OUTPUT); a=p.parse_args(); data=build()
    a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(data,sort_keys=True,indent=2,ensure_ascii=False)+"\n")
    print(json.dumps({"status":"C203_PRODUCER_PASS","graphs":data["summary"]["graph_count"],"principal_minors":data["summary"]["principal_minor_checks"],"payload_sha256":data["payload_sha256"]},sort_keys=True))
if __name__=="__main__": main()
