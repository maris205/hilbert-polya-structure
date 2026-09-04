#!/usr/bin/env python3
"""Canonical exact evidence producer for HCS-C361."""
from __future__ import annotations

if not __debug__:
    raise RuntimeError("c361 producer refuses optimized Python")
import argparse, hashlib, itertools, json, sys
from fractions import Fraction
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results/c361_markov_entropy_evidence.json"
YAML = ROOT / "evaluations/route_a/HCS-C361/2026-09-04.yaml"
SOURCE = "05ca5f96b2c69a6ad6ba153d1084df750d7722c0"
EVAL_SHA = "6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c"
YAML_RAW = "e61d1cc50b0891d2ecefb02bd460bf8b2bde48bf8f78fa6fb0e7524c6c931c7b"
YAML_SEM = "f8b6e53916659fb22cdc2b4278c5ef43ce5a24ea09ece76e86ada0dd3ff3c09b"
SCOPE = "NO_BAD_EULER_OR_ROOT_NUMBER"


class StrictLoader(yaml.SafeLoader):
    pass


StrictLoader.yaml_implicit_resolvers = {
    k: [(tag, rx) for tag, rx in v if tag != "tag:yaml.org,2002:timestamp"]
    for k, v in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def strict_mapping(loader, node, deep=False):
    out = {}
    for kn, vn in node.value:
        if kn.tag == "tag:yaml.org,2002:merge":
            raise ValueError("merge key")
        key = loader.construct_object(kn, deep=deep)
        if type(key) is not str or key in out:
            raise ValueError("duplicate/non-string YAML key")
        out[key] = loader.construct_object(vn, deep=deep)
    return out


StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG, strict_mapping)


def load_yaml(path):
    raw = path.read_text()
    for token in yaml.scan(raw):
        if isinstance(token, (yaml.tokens.AnchorToken, yaml.tokens.AliasToken)):
            raise ValueError("anchors forbidden")
    value = yaml.load(raw, Loader=StrictLoader)
    if type(value) is not dict:
        raise TypeError("YAML root")
    return value


def canon(x):
    return json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()


def fs(x):
    x = Fraction(x)
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


PANELS = {
    "two_state": [[0, 2], [3, 0]],
    "three_cycle": [[0, 2, 1], [1, 0, 2], [2, 1, 0]],
    "four_complete": [[0, 2, 1, 2], [1, 0, 3, 2], [3, 2, 0, 4], [5, 4, 1, 0]],
    "five_ring_chords": [
        [0, 4, 2, 2, 1], [1, 0, 4, 2, 2], [2, 1, 0, 4, 2],
        [2, 2, 1, 0, 4], [4, 2, 2, 1, 0],
    ],
}


def tree_rows(name, q):
    n = len(q); rows = []
    for root in range(n):
        others = [u for u in range(n) if u != root]
        choices = [[v for v in range(n) if v != u and q[u][v]] for u in others]
        ordinal = 0
        for vals in itertools.product(*choices):
            parent = dict(zip(others, vals)); good = True
            for u in others:
                seen = set(); v = u
                while v != root:
                    if v in seen or v not in parent:
                        good = False; break
                    seen.add(v); v = parent[v]
                if not good: break
            if good:
                ordinal += 1; weight = 1
                for u, v in parent.items(): weight *= q[u][v]
                rows.append({"panel": name, "root": root, "ordinal": ordinal,
                             "parent_map": [[u, parent[u]] for u in others], "weight": weight})
    return rows


def taus(name, q, rows):
    return [sum(r["weight"] for r in rows if r["panel"] == name and r["root"] == i)
            for i in range(len(q))]


def edge_rows(name, q, tau):
    z = sum(tau); rows = []
    for i in range(len(q)):
        for j in range(i + 1, len(q)):
            if q[i][j]:
                a = Fraction(tau[i] * q[i][j], z); b = Fraction(tau[j] * q[j][i], z)
                rows.append({"panel": name, "edge": [i, j], "flux_ij": fs(a),
                             "flux_ji": fs(b), "current_ij": fs(a-b),
                             "total_affinity_ratio": fs(a/b),
                             "medium_affinity_ratio": fs(Fraction(q[i][j], q[j][i])),
                             "epr_term_sign": 0 if a == b else 1})
    return rows


def simple_cycles(name, q):
    n = len(q); found = set(); rows = []
    for length in range(3, n + 1):
        for cyc in itertools.permutations(range(n), length):
            if cyc[0] != min(cyc): continue
            rev = (cyc[0],) + tuple(reversed(cyc[1:]))
            key = min(cyc, rev)
            if cyc != key or key in found: continue
            if all(q[cyc[k]][cyc[(k+1)%length]] for k in range(length)):
                found.add(key); fw = bw = 1
                for k in range(length):
                    i, j = cyc[k], cyc[(k+1)%length]
                    fw *= q[i][j]; bw *= q[j][i]
                rows.append({"panel": name, "cycle": list(cyc), "forward_product": fw,
                             "reverse_product": bw, "cycle_affinity_ratio": fs(Fraction(fw,bw)),
                             "zero_affinity": fw == bw})
    return rows


def p_add(a, b):
    out = [Fraction(0)] * max(len(a), len(b))
    for i, v in enumerate(a): out[i] += v
    for i, v in enumerate(b): out[i] += v
    while len(out) > 1 and not out[-1]: out.pop()
    return out


def p_mul(a, b):
    out = [Fraction(0)] * (len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i+j] += x*y
    return out


def parity(perm):
    return -1 if sum(perm[i] > perm[j] for i in range(len(perm)) for j in range(i+1,len(perm))) % 2 else 1


def charpoly(matrix):
    n = len(matrix); total = [Fraction(0)]
    for perm in itertools.permutations(range(n)):
        term = [Fraction(parity(perm))]
        for i, j in enumerate(perm):
            term = p_mul(term, [-matrix[i][j], 1] if i == j else [-matrix[i][j]])
        total = p_add(total, term)
    return [fs(v) for v in reversed(total)]


def tilt_rows(name, q):
    n = len(q); exit_rates = [sum(row) for row in q]; rows=[]
    for lam in (-2,-1,0,1,2,3):
        m = []
        for i in range(n):
            row=[]
            for j in range(n):
                if i == j: row.append(Fraction(-exit_rates[i]))
                else: row.append(Fraction(q[i][j]) ** (1-lam) * Fraction(q[j][i]) ** lam)
            m.append(row)
        rows.append({"panel":name,"lambda":lam,"partner":1-lam,
                     "characteristic_coefficients_descending":charpoly(m)})
    return rows


def path_rows(name, q, tau, max_jumps):
    z=sum(tau); n=len(q); rows=[]; ordinal=0
    for jumps in range(max_jumps+1):
        for path in itertools.product(range(n), repeat=jumps+1):
            if any(path[k]==path[k+1] or not q[path[k]][path[k+1]] for k in range(jumps)): continue
            fw=Fraction(tau[path[0]],z); rv=Fraction(tau[path[-1]],z); med=Fraction(1)
            for i,j in zip(path,path[1:]):
                fw*=q[i][j]; rv*=q[j][i]; med*=Fraction(q[i][j],q[j][i])
            ordinal+=1
            rows.append({"panel":name,"jumps":jumps,"ordinal":ordinal,"states":list(path),
                         "forward_weight":fs(fw),"reverse_weight":fs(rv),
                         "total_entropy_ratio":fs(fw/rv),"medium_ratio":fs(med),
                         "boundary_ratio":fs(Fraction(tau[path[0]],tau[path[-1]]))})
    return rows


def digest(rows): return hashlib.sha256(canon(rows)).hexdigest()


def build(yaml_path):
    raw=yaml_path.read_bytes(); sem=load_yaml(yaml_path)
    assert hashlib.sha256(raw).hexdigest()==YAML_RAW
    assert hashlib.sha256(canon(sem)).hexdigest()==YAML_SEM
    trees=[]; edges=[]; cycles=[]; tilts=[]; paths=[]; panel_rows=[]
    for name,q in PANELS.items():
        tr=tree_rows(name,q); tau=taus(name,q,tr); z=sum(tau)
        trees.extend(tr); er=edge_rows(name,q,tau); cr=simple_cycles(name,q); tl=tilt_rows(name,q)
        edges.extend(er); cycles.extend(cr); tilts.extend(tl)
        maxj={"two_state":8,"three_cycle":7,"four_complete":5,"five_ring_chords":0}[name]
        pr=path_rows(name,q,tau,maxj); paths.extend(pr)
        panel_rows.append({"panel":name,"states":len(q),"rates":q,"exit_rates":[sum(x) for x in q],
                           "tree_count":len(tr),"tau":tau,"tree_normalizer":z,
                           "stationary":[fs(Fraction(x,z)) for x in tau],
                           "edge_count":len(er),"cycle_count":len(cr),"tilt_count":len(tl),
                           "path_count":len(pr),"path_max_jumps":maxj})
    boundary_rows=[
      {"case":"singleton","status":"included by empty-tree convention; pi=1, L=0, entropy=0"},
      {"case":"two_state","status":"every irreducible bidirected two-state chain is detailed balanced and Sigma_T=0 pathwise"},
      {"case":"reducible","status":"excluded; apply classwise after choosing a closed irreducible class"},
      {"case":"one_way_edge","status":"excluded; reversal can be singular and affinity can be infinite"},
      {"case":"self_loop","status":"phantom self-jumps are excluded from the jump ledger and absorbed into holding conventions"},
    ]
    sections={"panel_rows":panel_rows,"tree_rows":trees,"edge_rows":edges,"cycle_rows":cycles,
              "tilt_rows":tilts,"path_rows":paths,"boundary_rows":boundary_rows}
    body={
      "schema":"hcs-c361-markov-entropy-evidence-v1","candidate_id":"HCS-C361","obstruction_id":"HEN-O345",
      "evaluation_date":"2026-09-04","source_commit":SOURCE,"fixed_epoch":1788480000,"scope_literal":SCOPE,
      "evaluator":{"authority":"flow_systems/skills/route-a-evaluator.md","version":"0.2.0","sha256":EVAL_SHA},
      "route_a_yaml":{"relative_path":"evaluations/route_a/HCS-C361/2026-09-04.yaml","raw_sha256":YAML_RAW,"semantic_sha256":YAML_SEM},
      "model":{"state_labels":"0,...,d-1","generator":"row generator on column functions; L_ij=q_ij and L_ii=-sum_j q_ij",
               "support":"connected bidirected finite graph; q_ij>0 iff q_ji>0","initial_law":"unique stationary law pi",
               "total_entropy":"log stationary forward path density divided by reversed path density",
               "medium_tilt":"offdiag q_ij^(1-lambda) q_ji^lambda; diagonal unchanged"},
      "theorem_contract":{"stationary":"pi_i=tau_i/sum tau by in-arborescences toward i",
        "epr":"sigma=sum_{i<j}(pi_i q_ij-pi_j q_ji) log((pi_i q_ij)/(pi_j q_ji)) >=0",
        "equivalence":"sigma=0 iff detailed balance iff every oriented cycle has unit rate-product ratio",
        "finite_time":"with P^R=P_pi o Theta^(-1), stationary path reversal gives dP_pi/dP^R=exp(Sigma_T), DFT, and E exp(-Sigma_T)=1",
        "tilt":"for every real lambda, L_lambda^T=L_(1-lambda); the full characteristic polynomial is symmetric and the Perron SCGF is finite, real analytic, and symmetric",
        "rate_function":"I(a)-I(-a)=-a only if W_T/T obeys a full LDP whose rate equals the Legendre-Fenchel transform of psi"},
      "finite_grid":{"panels":len(panel_rows),"panel_rows":len(panel_rows),"tree_rows":len(trees),"edge_rows":len(edges),
                     "cycle_rows":len(cycles),"tilt_rows":len(tilts),"path_rows":len(paths),"boundary_rows":len(boundary_rows)},
      "collision_boundary":{"C342":"directed edge-reinforced random walk in a random Dirichlet environment, not a fixed CTMC entropy theorem",
                            "C351":"open Jackson queues and quasireversibility, not cycle affinities or fluctuation symmetry",
                            "C355":"discrete random walk on a free group, not a finite continuous-time Markov network"},
      "nonclaims":["no arithmetic local data","no Euler factor or root number","no target functional equation or divisor",
                   "no primitive arithmetic orbit interpretation","no Hilbert-Polya operator","no Route B"],
      "references":[{"doi":"10.1103/RevModPhys.48.571","role":"network currents, affinities, and graph-theoretic stationary lineage"},
                    {"doi":"10.1023/A:1004589714161","role":"stochastic path-action and Gallavotti-Cohen lineage"}],
      "scope_flags":{"claims_target_arithmetic_local_data":False,"claims_target_euler_factors":False,"claims_root_number":False,
                     "claims_automorphy":False,"claims_target_divisor_or_counting_law":False,"claims_target_functional_equation":False,
                     "claims_target_zero_match":False,"claims_hilbert_polya_operator":False,"invokes_route_b":False},
      "route_a":{"tuple":["A0_FAIL","A1_FAIL","A2_FAIL","A3_FAIL","A4_FAIL"],"overall":"ROUTE_A_REJECTED",
                 "route_b_invocation_allowed":False,"theorem_status":"PROVABLE_AS_STATED"},
      **sections,"section_sha256":{k:digest(v) for k,v in sections.items()}}
    body["payload_sha256"]=hashlib.sha256(canon(body)).hexdigest()
    return body


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--output",type=Path,default=OUT); ap.add_argument("--evaluation",type=Path,default=YAML)
    a=ap.parse_args(); obj=build(a.evaluation); a.output.parent.mkdir(parents=True,exist_ok=True)
    a.output.write_bytes(json.dumps(obj,sort_keys=True,indent=2,ensure_ascii=False).encode()+b"\n")
    print(f"C361 producer PASS: panels={len(obj['panel_rows'])} trees={len(obj['tree_rows'])} paths={len(obj['path_rows'])} payload={obj['payload_sha256']}")


if __name__=="__main__": main()
