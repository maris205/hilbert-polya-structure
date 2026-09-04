#!/usr/bin/env python3
"""Independent fail-closed verifier for HCS-C361; never imports the producer."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("c361 checker refuses optimized Python")
import argparse, hashlib, itertools, json, math, sys
from fractions import Fraction
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]
EVIDENCE=ROOT/"results/c361_markov_entropy_evidence.json"
YAML_PATH=ROOT/"evaluations/route_a/HCS-C361/2026-09-04.yaml"
YAML_RAW="e61d1cc50b0891d2ecefb02bd460bf8b2bde48bf8f78fa6fb0e7524c6c931c7b"
YAML_SEM="f8b6e53916659fb22cdc2b4278c5ef43ce5a24ea09ece76e86ada0dd3ff3c09b"
SOURCE="05ca5f96b2c69a6ad6ba153d1084df750d7722c0"
EVAL_SHA="6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
PANELS={
 "two_state":[[0,2],[3,0]],
 "three_cycle":[[0,2,1],[1,0,2],[2,1,0]],
 "four_complete":[[0,2,1,2],[1,0,3,2],[3,2,0,4],[5,4,1,0]],
 "five_ring_chords":[[0,4,2,2,1],[1,0,4,2,2],[2,1,0,4,2],[2,2,1,0,4],[4,2,2,1,0]],
}
TOP={"schema","candidate_id","obstruction_id","evaluation_date","source_commit","fixed_epoch","scope_literal",
 "evaluator","route_a_yaml","model","theorem_contract","finite_grid","collision_boundary","nonclaims","references",
 "scope_flags","route_a","panel_rows","tree_rows","edge_rows","cycle_rows","tilt_rows","path_rows","boundary_rows",
 "section_sha256","payload_sha256"}
SECTIONS=("panel_rows","tree_rows","edge_rows","cycle_rows","tilt_rows","path_rows","boundary_rows")
EXPECTED_MODEL={"state_labels":"0,...,d-1","generator":"row generator on column functions; L_ij=q_ij and L_ii=-sum_j q_ij",
 "support":"connected bidirected finite graph; q_ij>0 iff q_ji>0","initial_law":"unique stationary law pi",
 "total_entropy":"log stationary forward path density divided by reversed path density",
 "medium_tilt":"offdiag q_ij^(1-lambda) q_ji^lambda; diagonal unchanged"}
EXPECTED_CONTRACT={"stationary":"pi_i=tau_i/sum tau by in-arborescences toward i",
 "epr":"sigma=sum_{i<j}(pi_i q_ij-pi_j q_ji) log((pi_i q_ij)/(pi_j q_ji)) >=0",
 "equivalence":"sigma=0 iff detailed balance iff every oriented cycle has unit rate-product ratio",
 "finite_time":"with P^R=P_pi o Theta^(-1), stationary path reversal gives dP_pi/dP^R=exp(Sigma_T), DFT, and E exp(-Sigma_T)=1",
 "tilt":"for every real lambda, L_lambda^T=L_(1-lambda); the full characteristic polynomial is symmetric and the Perron SCGF is finite, real analytic, and symmetric",
 "rate_function":"I(a)-I(-a)=-a only if W_T/T obeys a full LDP whose rate equals the Legendre-Fenchel transform of psi"}
EXPECTED_COLLISION={"C342":"directed edge-reinforced random walk in a random Dirichlet environment, not a fixed CTMC entropy theorem",
 "C351":"open Jackson queues and quasireversibility, not cycle affinities or fluctuation symmetry",
 "C355":"discrete random walk on a free group, not a finite continuous-time Markov network"}
EXPECTED_NONCLAIMS=["no arithmetic local data","no Euler factor or root number","no target functional equation or divisor",
 "no primitive arithmetic orbit interpretation","no Hilbert-Polya operator","no Route B"]


def pairs_hook(pairs):
    out={}
    for k,v in pairs:
        if k in out: raise ValueError("duplicate JSON key")
        out[k]=v
    return out


def bad_constant(x): raise ValueError(f"nonfinite JSON {x}")


def load_json(path):
    return json.loads(path.read_text(),object_pairs_hook=pairs_hook,parse_constant=bad_constant)


class StrictLoader(yaml.SafeLoader): pass
StrictLoader.yaml_implicit_resolvers={k:[(tag,rx) for tag,rx in v if tag!="tag:yaml.org,2002:timestamp"] for k,v in yaml.SafeLoader.yaml_implicit_resolvers.items()}
def strict_mapping(loader,node,deep=False):
    out={}
    for kn,vn in node.value:
        if kn.tag=="tag:yaml.org,2002:merge": raise ValueError("merge key")
        key=loader.construct_object(kn,deep=deep)
        if type(key) is not str or key in out: raise ValueError("duplicate/non-string YAML key")
        out[key]=loader.construct_object(vn,deep=deep)
    return out
StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,strict_mapping)
def load_yaml(path):
    raw=path.read_text()
    for tok in yaml.scan(raw):
        if isinstance(tok,(yaml.tokens.AnchorToken,yaml.tokens.AliasToken)): raise ValueError("anchors forbidden")
    x=yaml.load(raw,Loader=StrictLoader)
    if type(x) is not dict: raise TypeError("YAML root")
    return x


def canon(x): return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def F(x): return Fraction(x)
def fs(x):
    x=F(x); return str(x.numerator) if x.denominator==1 else f"{x.numerator}/{x.denominator}"
def keys(x,s):
    if type(x) is not dict or set(x)!=set(s): raise AssertionError(f"keys {set(x) if isinstance(x,dict) else type(x)} != {set(s)}")


def det(a):
    a=[[F(x) for x in row] for row in a]; n=len(a); sign=1; out=F(1)
    for k in range(n):
        pivot=next((r for r in range(k,n) if a[r][k]),None)
        if pivot is None:return F(0)
        if pivot!=k:a[k],a[pivot]=a[pivot],a[k];sign*=-1
        p=a[k][k];out*=p
        for r in range(k+1,n):
            f=a[r][k]/p
            for c in range(k,n):a[r][c]-=f*a[k][c]
    return sign*out


def taus_by_cofactor(q):
    n=len(q); lap=[]
    # column master operator Q^T; delete root row/column.
    for i in range(n):
        lap.append([F(sum(q[i])) if i==j else F(-q[j][i]) for j in range(n)])
    return [int(det([[lap[i][j] for j in range(n) if j!=r] for i in range(n) if i!=r])) for r in range(n)]


def matmul(a,b): return [[sum((a[i][k]*b[k][j] for k in range(len(b))),F(0)) for j in range(len(b[0]))] for i in range(len(a))]
def trace(a): return sum((a[i][i] for i in range(len(a))),F(0))
def charpoly_faddeev(a):
    n=len(a); ident=[[F(i==j) for j in range(n)] for i in range(n)]; b=ident; coeff=[F(1)]
    for k in range(1,n+1):
        ab=matmul(a,b); ck=-trace(ab)/k; coeff.append(ck)
        b=[[ab[i][j]+ck*ident[i][j] for j in range(n)] for i in range(n)]
    return [fs(x) for x in coeff]


def validate_yaml(path):
    raw=path.read_bytes(); y=load_yaml(path)
    assert hashlib.sha256(raw).hexdigest()==YAML_RAW
    assert hashlib.sha256(canon(y)).hexdigest()==YAML_SEM
    keys(y,{"schema","candidate_id","title","evaluation_date","source_commit","fixed_epoch","scope_literal","evaluator_authority",
      "evaluator_version","evaluator_authority_sha256","obstruction_id","candidate_definition","family","phase_space","dynamics",
      "parameters","parameter_provenance","arithmetic_origin","clock","normalization","determinant_convention","orbit_cutoff","precision",
      "training_data","forbidden_data","artifact_paths","a0","a1","a2","a3","a4","tuple","overall_verdict",
      "route_b_invocation_allowed","route_b_lock_reason","scope_flags","theorem_status","finite_evidence_role","source_owner_tokens"})
    fixed={"schema":"route-a-evaluation-v0.2.0","candidate_id":"HCS-C361","evaluation_date":"2026-09-04","source_commit":SOURCE,
      "fixed_epoch":1788480000,"scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER","evaluator_authority":"flow_systems/skills/route-a-evaluator.md",
      "evaluator_version":"0.2.0","evaluator_authority_sha256":EVAL_SHA,"obstruction_id":"HEN-O345",
      "artifact_paths":["results/c361_markov_entropy_evidence.json","THEOREM_PACKAGE.md","paper/main.pdf"],
      "tuple":["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_FAIL"],"overall_verdict":"ROUTE_A_REJECTED",
      "route_b_invocation_allowed":False,"theorem_status":"PROVABLE_AS_STATED",
      "source_owner_tokens":["10.1103/RevModPhys.48.571","10.1023/A:1004589714161"]}
    for k,v in fixed.items(): assert y[k]==v,k
    for idx,b in enumerate(("a0","a1","a2","a3","a4")):
        keys(y[b],{"verdict","evidence_status","strongest_evidence","strongest_failure"})
        assert y[b]["verdict"]=="A0_FAIL A1_FAIL A2_FAIL A3_FAIL A4_FAIL".split()[idx]
    assert y["a0"]["evidence_status"]==y["a1"]["evidence_status"]=="PROVED"
    assert all(y[b]["evidence_status"]=="STOP_SCOPED" for b in ("a2","a3","a4"))
    flags={"claims_target_arithmetic_local_data":False,"claims_target_euler_factors":False,"claims_root_number":False,
      "claims_automorphy":False,"claims_target_divisor_or_counting_law":False,"claims_target_functional_equation":False,
      "claims_target_zero_match":False,"claims_hilbert_polya_operator":False,"invokes_route_b":False}
    assert y["scope_flags"]==flags
    assert y["route_b_lock_reason"]=="no arithmetic origin, prime clock, target Euler factor, target divisor, or target-zero match exists"
    return y


def main():
    ap=argparse.ArgumentParser();ap.add_argument("--input",type=Path,default=EVIDENCE);ap.add_argument("--evaluation",type=Path,default=YAML_PATH);a=ap.parse_args()
    validate_yaml(a.evaluation); obj=load_json(a.input); count=0
    keys(obj,TOP); count+=len(TOP)
    fixed={"schema":"hcs-c361-markov-entropy-evidence-v1","candidate_id":"HCS-C361","obstruction_id":"HEN-O345",
      "evaluation_date":"2026-09-04","source_commit":SOURCE,"fixed_epoch":1788480000,"scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER",
      "evaluator":{"authority":"flow_systems/skills/route-a-evaluator.md","version":"0.2.0","sha256":EVAL_SHA},
      "route_a_yaml":{"relative_path":"evaluations/route_a/HCS-C361/2026-09-04.yaml","raw_sha256":YAML_RAW,"semantic_sha256":YAML_SEM},
      "model":EXPECTED_MODEL,"theorem_contract":EXPECTED_CONTRACT,"collision_boundary":EXPECTED_COLLISION,"nonclaims":EXPECTED_NONCLAIMS,
      "references":[{"doi":"10.1103/RevModPhys.48.571","role":"network currents, affinities, and graph-theoretic stationary lineage"},
                    {"doi":"10.1023/A:1004589714161","role":"stochastic path-action and Gallavotti-Cohen lineage"}],
      "route_a":{"tuple":["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_FAIL"],"overall":"ROUTE_A_REJECTED",
                 "route_b_invocation_allowed":False,"theorem_status":"PROVABLE_AS_STATED"}}
    for k,v in fixed.items(): assert obj[k]==v,k; count+=1
    assert obj["scope_flags"]=={k:False for k in ("claims_target_arithmetic_local_data","claims_target_euler_factors","claims_root_number",
      "claims_automorphy","claims_target_divisor_or_counting_law","claims_target_functional_equation","claims_target_zero_match","claims_hilbert_polya_operator","invokes_route_b")};count+=9
    tmp=dict(obj); claimed=tmp.pop("payload_sha256"); assert claimed==hashlib.sha256(canon(tmp)).hexdigest();count+=1
    keys(obj["section_sha256"],SECTIONS)
    for s in SECTIONS: assert obj["section_sha256"][s]==hashlib.sha256(canon(obj[s])).hexdigest();count+=1
    panel_by={r["panel"]:r for r in obj["panel_rows"]}; assert set(panel_by)==set(PANELS);count+=4
    tree_coords=set(); path_coords=set(); edge_coords=set(); cycle_coords=set(); tilt_coords=set()
    for name,q in PANELS.items():
        n=len(q); tau=taus_by_cofactor(q); z=sum(tau); p=panel_by[name]
        keys(p,{"panel","states","rates","exit_rates","tree_count","tau","tree_normalizer","stationary","edge_count","cycle_count","tilt_count","path_count","path_max_jumps"})
        assert p["states"]==n and p["rates"]==q and p["exit_rates"]==[sum(x) for x in q] and p["tau"]==tau and p["tree_normalizer"]==z
        assert p["stationary"]==[fs(Fraction(x,z)) for x in tau];count+=6
        for row in [r for r in obj["tree_rows"] if r["panel"]==name]:
            keys(row,{"panel","root","ordinal","parent_map","weight"}); coord=(name,row["root"],row["ordinal"]);assert coord not in tree_coords;tree_coords.add(coord)
            parent=dict(row["parent_map"]); assert set(parent)==set(range(n))-{row["root"]}; w=1
            for u,v in parent.items():
                assert u!=v and q[u][v]>0; w*=q[u][v];seen=set();x=u
                while x!=row["root"]: assert x not in seen and x in parent;seen.add(x);x=parent[x]
            assert w==row["weight"]
        for root in range(n):
            rr=sorted([r for r in obj["tree_rows"] if r["panel"]==name and r["root"]==root],key=lambda x:x["ordinal"])
            assert [x["ordinal"] for x in rr]==list(range(1,len(rr)+1)); assert sum(x["weight"] for x in rr)==tau[root];count+=2
        er=[r for r in obj["edge_rows"] if r["panel"]==name]
        expected_edges={(i,j) for i in range(n) for j in range(i+1,n) if q[i][j]}
        assert {tuple(r["edge"]) for r in er}==expected_edges
        for row in er:
            keys(row,{"panel","edge","flux_ij","flux_ji","current_ij","total_affinity_ratio","medium_affinity_ratio","epr_term_sign"})
            i,j=row["edge"];coord=(name,i,j);assert coord not in edge_coords;edge_coords.add(coord)
            aa=Fraction(tau[i]*q[i][j],z);bb=Fraction(tau[j]*q[j][i],z)
            assert row=={"panel":name,"edge":[i,j],"flux_ij":fs(aa),"flux_ji":fs(bb),"current_ij":fs(aa-bb),
              "total_affinity_ratio":fs(aa/bb),"medium_affinity_ratio":fs(Fraction(q[i][j],q[j][i])),"epr_term_sign":0 if aa==bb else 1};count+=1
        cr=[r for r in obj["cycle_rows"] if r["panel"]==name]
        for row in cr:
            keys(row,{"panel","cycle","forward_product","reverse_product","cycle_affinity_ratio","zero_affinity"});cy=tuple(row["cycle"])
            assert cy[0]==min(cy) and cy <= (cy[0],)+tuple(reversed(cy[1:]));coord=(name,cy);assert coord not in cycle_coords;cycle_coords.add(coord)
            fw=math.prod(q[cy[k]][cy[(k+1)%len(cy)]] for k in range(len(cy)));bw=math.prod(q[cy[(k+1)%len(cy)]][cy[k]] for k in range(len(cy)))
            assert row["forward_product"]==fw and row["reverse_product"]==bw and row["cycle_affinity_ratio"]==fs(Fraction(fw,bw)) and row["zero_affinity"]==(fw==bw);count+=1
        tl=[r for r in obj["tilt_rows"] if r["panel"]==name];assert [r["lambda"] for r in tl]==[-2,-1,0,1,2,3]
        for row in tl:
            keys(row,{"panel","lambda","partner","characteristic_coefficients_descending"});lam=row["lambda"];coord=(name,lam);assert coord not in tilt_coords;tilt_coords.add(coord);assert row["partner"]==1-lam
            m=[[F(-sum(q[i])) if i==j else F(q[i][j])**(1-lam)*F(q[j][i])**lam for j in range(n)] for i in range(n)]
            assert row["characteristic_coefficients_descending"]==charpoly_faddeev(m);count+=1
        bylam={r["lambda"]:r["characteristic_coefficients_descending"] for r in tl}
        assert all(bylam[x]==bylam[1-x] for x in (-2,-1,0,1,2,3));count+=6
        pr=[r for r in obj["path_rows"] if r["panel"]==name]; expected=[]
        for jumps in range(p["path_max_jumps"]+1):
            expected.extend(path for path in itertools.product(range(n),repeat=jumps+1) if all(path[k]!=path[k+1] and q[path[k]][path[k+1]] for k in range(jumps)))
        assert len(pr)==len(expected) and [tuple(r["states"]) for r in pr]==expected
        for ordinal,(row,path) in enumerate(zip(pr,expected),1):
            keys(row,{"panel","jumps","ordinal","states","forward_weight","reverse_weight","total_entropy_ratio","medium_ratio","boundary_ratio"})
            assert row["ordinal"]==ordinal and row["jumps"]==len(path)-1;coord=(name,ordinal);assert coord not in path_coords;path_coords.add(coord)
            fw=Fraction(tau[path[0]],z);rv=Fraction(tau[path[-1]],z);med=F(1)
            for i,j in zip(path,path[1:]):fw*=q[i][j];rv*=q[j][i];med*=Fraction(q[i][j],q[j][i])
            assert row["forward_weight"]==fs(fw) and row["reverse_weight"]==fs(rv) and row["total_entropy_ratio"]==fs(fw/rv)
            assert row["medium_ratio"]==fs(med) and row["boundary_ratio"]==fs(Fraction(tau[path[0]],tau[path[-1]]));count+=1
        assert p["tree_count"]==sum(r["panel"]==name for r in obj["tree_rows"]) and p["edge_count"]==len(er) and p["cycle_count"]==len(cr) and p["tilt_count"]==len(tl) and p["path_count"]==len(pr);count+=5
    assert obj["boundary_rows"]==[
      {"case":"singleton","status":"included by empty-tree convention; pi=1, L=0, entropy=0"},
      {"case":"two_state","status":"every irreducible bidirected two-state chain is detailed balanced and Sigma_T=0 pathwise"},
      {"case":"reducible","status":"excluded; apply classwise after choosing a closed irreducible class"},
      {"case":"one_way_edge","status":"excluded; reversal can be singular and affinity can be infinite"},
      {"case":"self_loop","status":"phantom self-jumps are excluded from the jump ledger and absorbed into holding conventions"}];count+=5
    grid=obj["finite_grid"];keys(grid,{"panels","panel_rows","tree_rows","edge_rows","cycle_rows","tilt_rows","path_rows","boundary_rows"})
    assert grid=={"panels":4,"panel_rows":len(obj["panel_rows"]),"tree_rows":len(obj["tree_rows"]),"edge_rows":len(obj["edge_rows"]),
      "cycle_rows":len(obj["cycle_rows"]),"tilt_rows":len(obj["tilt_rows"]),"path_rows":len(obj["path_rows"]),"boundary_rows":len(obj["boundary_rows"])};count+=8
    print(f"C361 checker PASS: assertions={count} trees={len(tree_coords)} paths={len(path_coords)} payload={claimed}")


if __name__=="__main__":
    try: main()
    except Exception as exc:
        print(f"C361 checker FAIL: {type(exc).__name__}: {exc}",file=sys.stderr);sys.exit(1)
