#!/usr/bin/env python3
"""Independent certificate checker; no square-root routine or producer import."""
from __future__ import annotations
if not __debug__:
    raise RuntimeError("c381 checker refuses optimized Python")
import argparse
import hashlib
import json
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import yaml

ROOT=Path(__file__).resolve().parents[1]
EVAL=ROOT/"evaluations/route_a/HCS-C381/2026-09-05.yaml"
EVAL_SHA="64497976fcfba315d3efd8de1a821982c42b415fe63cd9abceee3d301e18f626"
Q=2**160;MQ=2**80
FLAGS=("claims_target_arithmetic_local_data","claims_target_euler_factors","claims_root_number","claims_automorphy","claims_target_divisor_or_counting_law","claims_target_functional_equation","claims_target_zero_match","claims_hilbert_polya_operator","invokes_route_b")
TUPLE=["A0_FAIL","A1_WEAK","A2_FAIL","A3_FAIL","A4_FAIL"]
BOOLS=FLAGS+("route_b_invocation_allowed","neutral","infinite_trace_claim","outside_terms_tend_to_zero","mean_return_finite","compact","zero_integral_uniform_exponential_decay","invariant_density_claim")
def canonical(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def unique(pairs):
    d={}
    for k,v in pairs:
        if k in d:raise ValueError("duplicate JSON")
        d[k]=v
    return d
def load(path):return json.loads(path.read_text(),object_pairs_hook=unique,parse_constant=lambda x:(_ for _ in ()).throw(ValueError("nonfinite JSON")))
def shape(x,path=()):
    if type(x) is dict:
        assert all(type(k)is str for k in x)
        for k,v in x.items():shape(v,path+(k,))
    elif type(x)is list:
        for i,v in enumerate(x):shape(v,path+(i,))
    else:
        assert type(x) in (int,str,bool)
        if type(x)is bool:assert path[-1] in BOOLS,"bool as integer"
        if path and path[-1] in BOOLS:assert type(x)is bool,"integer as bool"
class StrictLoader(yaml.SafeLoader):pass
def mapping(loader,node,deep=False):
    out={}
    for k,v in node.value:
        key=loader.construct_object(k,deep=deep)
        if type(key)is not str or key in out or key=="<<":raise ValueError("invalid YAML key")
        out[key]=loader.construct_object(v,deep=deep)
    return out
StrictLoader.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,mapping)
def evaluation(path):
    raw=path.read_text()
    for t in yaml.scan(raw):
        if isinstance(t,(yaml.tokens.AliasToken,yaml.tokens.AnchorToken,yaml.tokens.TagToken)):raise ValueError("YAML references forbidden")
    value=yaml.load(raw,Loader=StrictLoader);shape(value)
    assert hashlib.sha256(canonical(value)).hexdigest()==EVAL_SHA,"evaluation semantic lock"
    return value
def bounded(pair,scale=Q):
    assert type(pair)is list and len(pair)==2 and all(type(v)is int for v in pair)
    lo,hi=pair;assert lo<=hi
    return F(lo,scale),F(hi,scale)
def floorfrac(x,scale):return x.numerator*scale//x.denominator
def ceilfrac(x,scale):return -((-x.numerator*scale)//x.denominator)
def least(w):
    divisors=[d for d in range(1,len(w)+1) if len(w)%d==0]
    return min(d for d in divisors if all(w[k]==w[k%d] for k in range(len(w))))
def mobius(n):
    k=2;sign=1
    while k*k<=n:
        if n%k==0:
            n//=k;sign=-sign
            if n%k==0:return 0
        k+=1
    return -sign if n>1 else sign

def point_certificate(word,point,mult):
    left,right=bounded(point);assert 0<=left<=right<=1 and point[1]-point[0]<=1024
    a,b=left,right;da=db=F(1)
    for symbol in word:
        if symbol=="0":
            assert 0<=a<=b<=F(1,2),"wrong left itinerary"
            da*=1+4*a;db*=1+4*b;a+=2*a*a;b+=2*b*b
        else:
            assert F(1,2)<a<=b<=1,"wrong right itinerary"
            da*=2;db*=2;a=2*a-1;b=2*b-1
    assert a<=left and b>=right,"fixed-point sign bracket"
    assert mult==[floorfrac(da,MQ),ceilfrac(db,MQ)],"multiplier interval"
    if "1" in word:assert mult[0]>=2*MQ
    return left,right

def check(path,evaluation_path=EVAL):
    x=load(path);shape(x);claimed=x.pop("payload_sha256")
    assert claimed==hashlib.sha256(canonical(x)).hexdigest()
    expected_keys="schema candidate_id obstruction_id source_commit evaluation_date fixed_epoch evaluator_authority evaluator_version evaluator_authority_sha256 scope_literal scope_flags route_a partition base clock domain cutoffs periodic_rows primitive_rows return_rows tail_rows induced_rows trace_head_rows complex_bounds tail_asymptotic uninduced nonclaims".split()
    assert set(x)==set(expected_keys),"unknown evidence field"
    fixed={"schema":"c381-lsv-evidence-v1","candidate_id":"HCS-C381","obstruction_id":"HEN-O365","source_commit":"0596f9d680277288225062a6fdd7ad7ce116e01d","evaluation_date":"2026-09-05","fixed_epoch":1788566400,"evaluator_authority":"flow_systems/skills/route-a-evaluator.md","evaluator_version":"0.2.0","evaluator_authority_sha256":"6f13fc94be84eaf22c518dd0c530e442cd625f3cdcb9d3d34e67cc11c881194c","scope_literal":"NO_BAD_EULER_OR_ROOT_NUMBER","scope_flags":{k:False for k in FLAGS},"route_a":{"tuple":TUPLE,"overall_verdict":"ROUTE_A_REJECTED","route_b_invocation_allowed":False},"partition":"left [0,1/2]; right (1/2,1]","base":"Y=(1/2,1]","clock":"u counts returns; zeta counts original iterations","domain":"Hardy H2 on disk center 1 radius 3/4","cutoffs":{"period_max":6,"return_branch_max":128,"tail_m_max":256,"induced_alphabet_max":3,"induced_period_max":3,"point_bits":160,"multiplier_bits":80},"complex_bounds":{"domain_radius":[3,4],"image_radius":[1,2],"hardy_ratio":[2,3],"initial_reciprocal_real_lower":[4,7],"reciprocal_increment_real_lower":[2,25],"derivative_bound_prefactor":1250,"derivative_bound_exp_pi2_coefficient":[625,6],"nuclear_rank_sum":3,"absolute_branch_domain":"abs(zeta)<=1","outside_terms_tend_to_zero":False},"tail_asymptotic":{"lebesgue_constant":[1,4],"normalized_constant":[1,2],"mean_return_finite":False},"uninduced":{"space":"Lebesgue L1([0,1])","compact":False,"zero_integral_uniform_exponential_decay":False,"approximate_vector_norm":1,"residual_bound_factor":12,"invariant_density_claim":False},"nonclaims":["no target arithmetic carrier","no full uninduced Fredholm determinant","no infinite determinant inferred from branch cutoff","no claim against regularized determinants on other spaces","no literature-priority claim"]}
    for k,v in fixed.items():assert canonical(x[k])==canonical(v),k
    expected=["".join(w) for n in range(1,7) for w in product("01",repeat=n)]
    assert [r["word"] for r in x["periodic_rows"]]==expected
    for row in x["periodic_rows"]:
        assert set(row)==set("word n least_period repetition point_bounds multiplier_bounds neutral orientation".split())
        word=row["word"];n=len(word);d=least(word)
        assert (row["n"],row["least_period"],row["repetition"],row["orientation"])==(n,d,n//d,1)
        assert row["neutral"] is ("1" not in word)
        point_certificate(word,row["point_bounds"],row["multiplier_bounds"])
    expected=[{"n":n,"fixed_count":2**n,"primitive_cycles":sum(mobius(d)*2**(n//d) for d in range(1,n+1) if n%d==0)//n,"neutral_cycles":1 if n==1 else 0} for n in range(1,7)]
    assert x["primitive_rows"]==expected,"Mobius census"
    coordinates=((1,2),(5,8),(3,4),(7,8),(1,1))
    assert [(tuple(r["x"]),r["n"]) for r in x["return_rows"]]==[(p,n) for p in coordinates for n in range(1,129)]
    previous={}
    for r in x["return_rows"]:
        assert set(r)==set("x n preimage_bounds preimage_derivative_bounds h_bounds h_derivative_bounds".split())
        key=tuple(r["x"]);n=r["n"];lo,hi=bounded(r["preimage_bounds"]);dl,du=bounded(r["preimage_derivative_bounds"])
        assert 0<lo<=hi<=1 and 0<dl<=du<=1
        assert r["preimage_bounds"][1]-r["preimage_bounds"][0]<=1024
        if n==1:
            assert lo==hi==F(*key) and dl==du==1
        else:
            pl,pu,pdl,pdu=previous[key]
            assert lo+2*lo*lo<=pl and hi+2*hi*hi>=pu,"inverse quadratic inclusion"
            assert dl<=pdl/(1+4*hi) and du>=pdu/(1+4*lo),"inverse derivative inclusion"
            assert pdl/(1+4*hi)-dl<F(2,Q) and du-pdu/(1+4*lo)<F(2,Q)
        a,b=bounded(r["h_bounds"]);c,d=bounded(r["h_derivative_bounds"])
        assert a<=(1+lo)/2 and b>=(1+hi)/2 and (1+lo)/2-a<F(2,Q) and b-(1+hi)/2<F(2,Q)
        assert c<=dl/2 and d>=du/2 and dl/2-c<F(2,Q) and d-du/2<F(2,Q)
        previous[key]=(lo,hi,dl,du)
    assert [r["m"] for r in x["tail_rows"]]==list(range(257))
    previous=None
    for row in x["tail_rows"]:
        assert set(row)==set("m a_bounds reciprocal_bounds return_tail_n tail_bounds".split())
        m=row["m"];lo,hi=bounded(row["a_bounds"])
        assert 0<lo<=hi<=F(1,2),"tail interval positivity"
        assert row["a_bounds"][1]-row["a_bounds"][0]<=1024,"tail certificate width"
        assert row["reciprocal_bounds"]==[[1,2*m+2],[1,m+2]] and row["return_tail_n"]==m+1
        if m==0:assert lo==hi==F(1,2)
        else:
            assert lo+2*lo*lo<=previous[0] and hi+2*hi*hi>=previous[1]
            assert F(1,2*m+2)<=hi and lo<=F(1,m+2)
        a,b=bounded(row["tail_bounds"]);assert a<=lo/2 and b>=hi/2 and lo/2-a<F(2,Q) and b-hi/2<F(2,Q)
        previous=(lo,hi)
    expected=[list(v) for r in range(1,4) for v in product(range(1,4),repeat=r)]
    assert [r["branches"] for r in x["induced_rows"]]==expected
    for r in x["induced_rows"]:
        assert set(r)==set("branches return_period original_time word point_bounds multiplier_bounds trace_weight_bounds".split())
        assert r["return_period"]==len(r["branches"]) and r["original_time"]==sum(r["branches"])
        assert r["word"]=="".join("1"+"0"*(n-1) for n in r["branches"])
        point_certificate(r["word"],r["point_bounds"],r["multiplier_bounds"])
        lo,hi=bounded(r["multiplier_bounds"],MQ)
        expected=[floorfrac(1/(hi-1),MQ),ceilfrac(1/(lo-1),MQ)]
        assert r["trace_weight_bounds"]==expected,"fixed derivative/(1-derivative)"
    expected=[]
    for order in range(1,4):
        a=b=F(0)
        for r in x["induced_rows"]:
            if r["return_period"]==order:
                lo,hi=bounded(r["trace_weight_bounds"],MQ);factor=F(1,4**r["original_time"])
                a+=lo*factor;b+=hi*factor
        expected.append({"return_period":order,"branch_cutoff":3,"zeta":[1,4],"trace_head_bounds":[floorfrac(a,MQ),ceilfrac(b,MQ)],"infinite_trace_claim":False})
    assert canonical(x["trace_head_rows"])==canonical(expected),"trace clock or cutoff"
    evaluation(evaluation_path)
    return {"periodic":126,"return":640,"tail":257,"induced":39,"trace_heads":3,"payload":claimed}

def main():
    p=argparse.ArgumentParser();p.add_argument("evidence",nargs="?",type=Path,default=ROOT/"results/c381_lsv_evidence.json");p.add_argument("--evaluation",type=Path,default=EVAL);a=p.parse_args()
    print("C381 independent checker PASS: "+json.dumps(check(a.evidence,a.evaluation),sort_keys=True))

if __name__=="__main__":main()
